#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static site generator for jcseng.com.
    python3 tools/build.py            # regenerate every page + robots/sitemap/llms/manifest + inventory CSV
Everything reads from tools/siteconfig.py (data) and tools/posts.py (post bodies). No dependencies beyond
the Python standard library. The build fails loudly on SEO rule violations (see validate()).
"""
import os, re, csv, json, html, hashlib, datetime
import siteconfig as C
from posts import POST_BODIES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = C.CONTENT_DATE
SITE, BRAND, LEGAL = C.SITE, C.BRAND, C.LEGAL
ORG_ID, PERSON_ID, SITE_ID = SITE + "/#organization", SITE + "/about/#drew-jones", SITE + "/#website"

def _v(rel):
    with open(os.path.join(ROOT, rel.lstrip("/")), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]
CSS_URL = "/assets/css/styles.css?v=" + _v("/assets/css/styles.css")
JS_URL = "/assets/js/main.js?v=" + _v("/assets/js/main.js")
ICON_V = _v("/assets/img/favicon.svg")

def unesc(s): return html.unescape(re.sub(r"<[^>]+>", "", s))
def svc(slug): return next(s for s in C.SERVICES if s["slug"] == slug)
def post(slug): return next(p for p in C.POSTS if p["slug"] == slug)
def svc_url(s): return f"/capabilities/{s['slug']}/"
def post_url(p): return f"/insights/{p['slug']}/"

ARROW = ('<svg class="arrow" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" '
         'stroke-linejoin="round" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg>')
MORE = ARROW.replace('class="arrow"', 'class="more"')
CHECK = ('<svg class="mark" viewBox="0 0 56 56" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
         'stroke-linejoin="round" aria-hidden="true"><circle cx="28" cy="28" r="26"/><path d="M17 29l7 7 15-16"/></svg>')

# =============================================================================================
# Structured data
# =============================================================================================
def ld_org():
    o = {"@type": "ProfessionalService", "@id": ORG_ID, "name": BRAND, "legalName": LEGAL, "url": SITE + "/",
         "logo": {"@type": "ImageObject", "url": SITE + "/assets/img/logo.svg"},
         "image": SITE + "/assets/img/og-card.png", "telephone": "+1-704-500-3033", "email": C.EMAIL,
         "description": unesc(C.TAGLINE) + " — pharmaceutical, biotech and advanced manufacturing.",
         "address": {"@type": "PostalAddress", "addressLocality": C.ADDRESS["locality"], "addressRegion": C.ADDRESS["region"], "addressCountry": C.ADDRESS["country"]},
         "areaServed": [{"@type": t, "name": n} for n, t in C.AREA_SERVED],
         "founder": {"@id": PERSON_ID}, "employee": {"@id": PERSON_ID},
         "knowsAbout": [unesc(s["title"]) for s in C.SERVICES],
         "hasCredential": {"@type": "EducationalOccupationalCredential", "credentialCategory": "license",
                           "name": f"North Carolina Engineering Firm License {C.PRINCIPAL['firm_lic']}",
                           "recognizedBy": {"@type": "GovernmentOrganization", "name": "North Carolina Board of Examiners for Engineers and Surveyors"}},
         "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Engineering services",
                             "itemListElement": [{"@type": "Offer", "itemOffered": {"@id": SITE + svc_url(s) + "#service"}} for s in C.SERVICES]}}
    if C.ADDRESS.get("street"): o["address"]["streetAddress"] = C.ADDRESS["street"]
    if C.ADDRESS.get("postal"): o["address"]["postalCode"] = C.ADDRESS["postal"]
    if C.GEO: o["geo"] = {"@type": "GeoCoordinates", "latitude": C.GEO["lat"], "longitude": C.GEO["lng"]}
    if C.HOURS: o["openingHoursSpecification"] = [{"@type": "OpeningHoursSpecification", "dayOfWeek": _days(a, b), "opens": op, "closes": cl} for a, b, op, cl in C.HOURS]
    if C.FOUNDING_YEAR: o["foundingDate"] = C.FOUNDING_YEAR
    same = [u for k, u in C.PROFILES.items() if u and k in ("linkedin_company", "google_business")]
    if same: o["sameAs"] = same
    return o

def _days(a, b):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[days.index(a):days.index(b) + 1]

def ld_person():
    P = C.PRINCIPAL
    p = {"@type": "Person", "@id": PERSON_ID, "name": "Drew W. Jones", "givenName": P["given"], "familyName": P["family"], "honorificSuffix": "PE",
         "jobTitle": unesc(P["title"]), "worksFor": {"@id": ORG_ID}, "url": SITE + "/about/", "image": SITE + "/assets/img/drew-jones-400.jpg",
         "alumniOf": {"@type": "CollegeOrUniversity", "name": P["school"]},
         "hasCredential": [
             {"@type": "EducationalOccupationalCredential", "credentialCategory": "license", "name": f"Professional Engineer, North Carolina, No. {P['pe_no']}",
              "recognizedBy": {"@type": "GovernmentOrganization", "name": "North Carolina Board of Examiners for Engineers and Surveyors"}},
             {"@type": "EducationalOccupationalCredential", "credentialCategory": "degree", "name": unesc(P["education"])},
             {"@type": "EducationalOccupationalCredential", "credentialCategory": "certification", "name": "Lean Six Sigma Green Belt"}],
         "knowsAbout": ["Pharmaceutical process engineering", "Commissioning, qualification and validation", "Capital project management", "Spray drying", "Aseptic processing", "Tech transfer"]}
    if C.PROFILES.get("linkedin_person"): p["sameAs"] = [C.PROFILES["linkedin_person"]]
    return p

def ld_website():
    return {"@type": "WebSite", "@id": SITE_ID, "url": SITE + "/", "name": BRAND, "publisher": {"@id": ORG_ID}, "inLanguage": "en-US"}

def ld_webpage(path, title, desc, ptype="WebPage", extra=None):
    w = {"@type": ptype, "@id": SITE + path + "#webpage", "url": SITE + path, "name": unesc(title), "description": unesc(desc),
         "isPartOf": {"@id": SITE_ID}, "about": {"@id": ORG_ID}, "inLanguage": "en-US",
         "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + "/assets/img/og-card.png"}}
    if extra: w.update(extra)
    return w

def ld_breadcrumbs(crumbs):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": unesc(n), **({"item": SITE + u} if u else {})} for i, (n, u) in enumerate(crumbs)]}

def ld_faq(items):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": unesc(q), "acceptedAnswer": {"@type": "Answer", "text": unesc(a)}} for q, a in items]}

def ld_service(s):
    return {"@type": "Service", "@id": SITE + svc_url(s) + "#service", "name": unesc(s["title"]), "serviceType": unesc(s["title"]),
            "description": unesc(s["intro"]), "provider": {"@id": ORG_ID}, "url": SITE + svc_url(s),
            "areaServed": [{"@type": t, "name": n} for n, t in C.AREA_SERVED],
            "audience": {"@type": "BusinessAudience", "name": "Pharmaceutical, biotechnology and advanced manufacturing owners"},
            "hasOfferCatalog": {"@type": "OfferCatalog", "name": unesc(s["title"]) + " deliverables",
                                "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": unesc(d)}} for d in s["deliv"]]}}

def ld_article(p):
    return {"@type": "Article", "@id": SITE + post_url(p) + "#article", "headline": unesc(p["title"]), "description": unesc(p["meta"]),
            "author": {"@id": PERSON_ID}, "publisher": {"@id": ORG_ID}, "datePublished": p["date"], "dateModified": p["modified"],
            "image": SITE + "/assets/img/og-card.png", "mainEntityOfPage": {"@id": SITE + post_url(p) + "#webpage"},
            "inLanguage": "en-US", "about": [{"@id": SITE + svc_url(svc(x)) + "#service"} for x in p["services"]]}

def ld_graph(*nodes):
    return {"@context": "https://schema.org", "@graph": [ld_org(), ld_person(), ld_website()] + [n for n in nodes if n]}

# =============================================================================================
# Chrome
# =============================================================================================
def head(title, desc, path, ld, og_type="website", noindex=False, article=None):
    url = SITE + path
    t = html.unescape(title); d = html.unescape(desc)
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
    verify = ""
    if C.GOOGLE_SITE_VERIFICATION: verify += f'\n  <meta name="google-site-verification" content="{C.GOOGLE_SITE_VERIFICATION}" />'
    if C.BING_SITE_VERIFICATION: verify += f'\n  <meta name="msvalidate.01" content="{C.BING_SITE_VERIFICATION}" />'
    art = ""
    if article:
        art = (f'\n  <meta property="article:published_time" content="{article["date"]}" />'
               f'\n  <meta property="article:modified_time" content="{article["modified"]}" />'
               f'\n  <meta property="article:author" content="{SITE}/about/" />')
    return f'''<!DOCTYPE html>
<html lang="en-US">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="robots" content="{robots}" />
  <link rel="canonical" href="{url}" />
  <meta name="theme-color" content="#111318" />
  <meta name="author" content="{LEGAL}" />{verify}

  <meta property="og:type" content="{og_type}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:site_name" content="{BRAND}" />
  <meta property="og:locale" content="{C.LOCALE}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:image" content="{SITE}/assets/img/og-card.png" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="JCS Engineering — project engineering, design and CQV for regulated manufacturing" />{art}
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{desc}" />
  <meta name="twitter:image" content="{SITE}/assets/img/og-card.png" />

  <link rel="icon" href="/assets/img/favicon.svg?v={ICON_V}" type="image/svg+xml" />
  <link rel="icon" href="/assets/img/favicon-32.png?v={ICON_V}" sizes="32x32" type="image/png" />
  <link rel="icon" href="/assets/img/favicon-16.png?v={ICON_V}" sizes="16x16" type="image/png" />
  <link rel="apple-touch-icon" sizes="180x180" href="/assets/img/apple-touch-icon.png" />
  <link rel="manifest" href="/site.webmanifest" />
  <link rel="preload" href="/assets/fonts/inter-var-latin.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="stylesheet" href="{CSS_URL}" />

  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
'''

def header(path):
    CUR = ' aria-current="page"'
    def cur(h): return CUR if (h == path or (h != "/" and path.startswith(h))) else ""
    links = "".join(f'<a href="{h}"{cur(h)}>{t}</a>' for h, t in C.NAV)
    return f'''
  <header class="site-header" id="top">
    <div class="container nav">
      <a href="/" class="logo" aria-label="{BRAND} — home">
        <img src="/assets/img/logo.svg" alt="{BRAND}" width="180" height="114" />
      </a>
      <nav id="primary-nav" class="primary-nav" aria-label="Primary">
        {links}
        <a href="/contact/" class="btn btn-sm"{CUR if path == "/contact/" else ""}>Schedule a Call</a>
      </nav>
      <button type="button" class="nav-toggle" id="nav-toggle" aria-expanded="false" aria-controls="primary-nav" aria-label="Open menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <main id="main">
'''

def crumbs_html(crumbs):
    items = []
    for i, (n, u) in enumerate(crumbs):
        last = i == len(crumbs) - 1
        cur = ' aria-current="page"' if last else ''
        label = n if (last or not u) else f'<a href="{u}">{n}</a>'
        items.append(f'<li{cur}>{label}</li>')
    return f'<nav class="crumb" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'

def eyebrow(t): return f'<p class="eyebrow"><span class="tick"></span>{t}</p>'

def page_head(crumbs, h1, lede, extra=""):
    return f'''
    <section class="page-head grid-bg">
      <div class="container">
        {crumbs_html(crumbs)}
        <h1 class="reveal">{h1}</h1>
        <p class="lede reveal">{lede}</p>
        {extra}
      </div>
    </section>
'''

def cta_band(h="Let's talk about your project.", p="Tell us where it stands — concept, design, construction, or startup — and we'll come back within one business day."):
    return f'''
    <section class="section-dark grid-bg-dark cta-band">
      <div class="container inner">
        <div class="reveal"><h2>{h}</h2><p>{p}</p></div>
        <div class="ctas reveal">
          <a class="btn btn-lg" href="/contact/">Start a conversation {ARROW}</a>
          <a class="btn ghost btn-lg" href="tel:{C.PHONE_E164}">{C.PHONE_DISPLAY}</a>
        </div>
      </div>
    </section>
'''

def faq_block(items):
    out = ['<div class="faq reveal">']
    for q, a in items:
        out.append(f'<div class="faq-item"><h3><button type="button" class="faq-q" aria-expanded="false">{q}<span class="chev" aria-hidden="true"></span></button></h3>'
                   f'<div class="faq-a" hidden><p>{a}</p></div></div>')
    out.append('</div>')
    return "\n".join(out)

def standards_html():
    return "".join(f'<div class="std reveal"><h3>{cat}</h3><ul>{"".join(f"<li>{n}<span class=mono>{d}</span></li>" for n, d in items)}</ul></div>' for cat, items in C.STANDARDS)

def footer():
    caps = "".join(f'<li><a href="{svc_url(s)}">{s["title"]}</a></li>' for s in C.SERVICES)
    addr = (f'{C.ADDRESS["street"]}<br>' if C.ADDRESS.get("street") else "") + f'{C.ADDRESS["locality"]}, {C.ADDRESS["region"]}' + (f' {C.ADDRESS["postal"]}' if C.ADDRESS.get("postal") else "")
    hours = ""
    if C.HOURS:
        hours = "<br>" + " · ".join(f'{a[:3]}–{b[:3]} {op}–{cl}' for a, b, op, cl in C.HOURS)
    return f'''
  </main>

  <footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <a href="/" class="logo" aria-label="{BRAND} — home">
          <img src="/assets/img/logo-inverse.svg" alt="{BRAND}" width="180" height="114" loading="lazy" />
        </a>
        <address class="nap">
          <strong>{LEGAL}</strong><br>
          {addr}<br>
          {C.SERVICE_AREA_LINE}<br>
          <a href="tel:{C.PHONE_E164}">{C.PHONE_DISPLAY}</a> · <a href="mailto:{C.EMAIL}">{C.EMAIL}</a>{hours}
        </address>
      </div>
      <div>
        <p class="footer-h">Company</p>
        <ul>
          <li><a href="/capabilities/">Capabilities</a></li>
          <li><a href="/approach/">Approach</a></li>
          <li><a href="/experience/">Experience</a></li>
          <li><a href="/insights/">Insights</a></li>
          <li><a href="/about/">About</a></li>
          <li><a href="/contact/">Contact</a></li>
        </ul>
      </div>
      <div>
        <p class="footer-h">Capabilities</p>
        <ul>{caps}</ul>
      </div>
      <div>
        <p class="footer-h">More</p>
        <ul>
          <li><a href="/service-areas/">Service areas</a></li>
          <li><a href="/faq/">FAQ</a></li>
          <li><a href="/privacy/">Privacy</a></li>
          <li><a href="/sitemap.xml">Sitemap</a></li>
        </ul>
      </div>
    </div>
    <div class="container legal">
      <p>&copy; <span id="year">2026</span> {LEGAL}. All rights reserved. <span class="lic">NC Engineering Firm License {C.PRINCIPAL["firm_lic"]}</span></p>
      <p class="mono">jcseng.com</p>
    </div>
  </footer>

  <script src="{JS_URL}" defer></script>
</body>
</html>
'''

def related_html(s):
    rel = "".join(f'<li><a href="{svc_url(svc(r))}">{svc(r)["title"]} {ARROW}</a></li>' for r in s["related"])
    p = post(s["post"])
    return f'''
        <aside class="related reveal">
          <div><p class="footer-h">Related capabilities</p><ul>{rel}</ul></div>
          <div><p class="footer-h">From Insights</p><ul><li><a href="{post_url(p)}">{p["title"]} {ARROW}</a></li></ul></div>
        </aside>'''

# =============================================================================================
# Pages
# =============================================================================================
PAGES = []  # (path, title, desc, noindex)

def page(path, title, desc, body, ld, og_type="website", noindex=False, article=None):
    full = head(title, desc, path, ld, og_type, noindex, article) + header(path) + body + footer()
    PAGES.append((path, title, desc, noindex))
    return full

def home():
    caps = "".join(f'<li class="reveal"><a href="{svc_url(c)}"><span class="num">{c["n"]}</span><span><strong>{c["title"]}</strong><span class="d">{c["short"]}</span></span>{MORE}</a></li>' for c in C.SERVICES)
    inds = "".join(f'<article class="ind reveal"><h3>{i["title"]}</h3><p>{i["body"]}</p></article>' for i in C.INDUSTRIES)
    posts = "".join(f'<article class="card reveal"><p class="eyebrow"><span class="tick"></span>{p["minutes"]} min read</p><h3><a href="{post_url(p)}">{p["title"]}</a></h3><p>{p["excerpt"]}</p><a class="link-arrow" href="{post_url(p)}">Read the article {ARROW}</a></article>' for p in C.POSTS)
    title = "JCS Engineering PLLC | Pharma Project Engineers, Raleigh NC"
    desc = "Licensed NC engineering firm providing project engineering, design, CQV and project management for pharmaceutical, biotech and advanced manufacturing clients."
    body = f'''
    <section class="hero grid-bg">
      <div class="container hero-inner">
        <div class="hero-copy reveal">
          {eyebrow("Project Engineering for Regulated Manufacturing")}
          <h1>Capital projects delivered with <em>engineering discipline</em>.</h1>
          <p class="lede">JCS Engineering provides project engineering, design, CQV, and project management for pharmaceutical, biotech, and advanced manufacturing facilities in the Research Triangle and across North Carolina — from concept through qualified handover.</p>
          <div class="ctas">
            <a class="btn" href="/contact/">Start a conversation {ARROW}</a>
            <a class="btn ghost" href="/capabilities/">What we do</a>
          </div>
          <dl class="stats">
            <div><dt>PE</dt><dd>Licensed engineering firm, North Carolina</dd></div>
            <div><dt>Concept<span>→</span>CQV</dt><dd>Full lifecycle coverage</dd></div>
          </dl>
        </div>
        <figure class="hero-art reveal">
          <div class="frame">
            <picture>
              <source type="image/webp" srcset="/assets/img/bioreactors-800.webp 800w, /assets/img/bioreactors-1200.webp 1200w" sizes="(max-width: 1000px) 92vw, 540px" />
              <img src="/assets/img/bioreactors-1200.jpg" srcset="/assets/img/bioreactors-800.jpg 800w, /assets/img/bioreactors-1200.jpg 1200w" sizes="(max-width: 1000px) 92vw, 540px"
                   alt="Stainless steel bioreactor vessels in a GMP biotech manufacturing suite" width="1200" height="701" fetchpriority="high" />
            </picture>
          </div>
        </figure>
      </div>
    </section>

    <div class="strip"><div class="container strip-inner">
      <span>Pharmaceutical</span><span>Biotechnology</span><span>Advanced Manufacturing</span><span>cGMP &amp; GxP</span><span>NC Firm License {C.PRINCIPAL["firm_lic"]}</span><span>Raleigh, NC</span>
    </div></div>

    <section id="capabilities" class="section">
      <div class="container">
        <header class="section-head reveal">{eyebrow("What We Do")}<h2>Six services across the capital project lifecycle.</h2>
          <p class="section-sub">Engineering and project services for regulated manufacturing — engaged individually or as an integrated scope, and scaled from a single owner's engineer to an embedded project team.</p></header>
        <ol class="cap-list">{caps}</ol>
        <div class="ctas"><a class="link-arrow" href="/capabilities/">All capabilities in detail {ARROW}</a></div>
      </div>
    </section>

    <section id="industries" class="section section-alt">
      <div class="container">
        <header class="section-head reveal">{eyebrow("Industries")}<h2>Where we work</h2></header>
        <div class="ind-grid">{inds}</div>
      </div>
    </section>

    <section id="why" class="section">
      <div class="container split">
        <div class="reveal">
          {eyebrow("Why JCS Engineering")}
          <h2>A licensed firm that scales to the work.</h2>
          <p class="lede">One engineer for a targeted upgrade, or a coordinated team for a site-wide program — every engagement is led by a licensed Professional Engineer and built on hands-on GMP operations experience.</p>
          <p class="p-body">Based in the Raleigh area, we serve North Carolina's biomanufacturing corridor — Research Triangle Park, Durham, Holly Springs, Clayton, Sanford, Wilson, and Greenville — on-site, remotely, or in a hybrid arrangement. <a href="/service-areas/">See our service area</a>.</p>
          <div class="ctas"><a class="link-arrow" href="/about/">About the firm {ARROW}</a><a class="link-arrow link-muted" href="/experience/">Representative experience {ARROW}</a></div>
        </div>
        <ul class="diff reveal">
          <li><h3>Trusted partner</h3><p>An extension of your team, protecting the owner's interests with compliance, quality, and performance as the priority.</p></li>
          <li><h3>Expertise with agility</h3><p>Capital project experience without the overhead of a large firm — the engagement fits the project.</p></li>
          <li><h3>Lifecycle coverage</h3><p>From conceptual planning through design, construction, CQV, and GMP-ready handover.</p></li>
          <li><h3>Operational insight</h3><p>Hands-on GMP operations experience means projects that minimize disruption to production.</p></li>
        </ul>
      </div>
    </section>

    <section id="insights" class="section section-alt">
      <div class="container">
        <header class="section-head reveal">{eyebrow("Insights")}<h2>Notes from the owner's side of the table</h2></header>
        <div class="cards">{posts}</div>
        <div class="ctas"><a class="link-arrow" href="/insights/">All insights {ARROW}</a></div>
      </div>
    </section>

    <section id="faq" class="section">
      <div class="container narrow">
        <header class="section-head reveal">{eyebrow("FAQ")}<h2>Frequently asked questions</h2></header>
        {faq_block(C.FAQ[:7])}
        <div class="ctas"><a class="link-arrow" href="/faq/">More questions answered {ARROW}</a></div>
      </div>
    </section>
    {cta_band()}
'''
    ld = ld_graph(ld_webpage("/", title, desc), ld_faq(C.FAQ[:7]))
    return page("/", title, desc, body, ld)

def capabilities():
    caps = "".join(f'''
        <article class="cap-simple reveal" id="{c["slug"]}">
          <span class="num">{c["n"]}</span>
          <div><h2><a href="{svc_url(c)}">{c["title"]}</a></h2><p>{c["intro"]}</p>
            <div class="deliv"><span class="lbl">Typical deliverables</span>{"".join(f"<span>{x}</span>" for x in c["deliv"][:5])}</div>
            <p class="more-link"><a class="link-arrow" href="{svc_url(c)}">{c["title"]} in detail {ARROW}</a></p></div>
        </article>''' for c in C.SERVICES)
    idx = "".join(f'<a href="{svc_url(c)}">{c["n"]} · {c["title"]}</a>' for c in C.SERVICES)
    title = "Pharmaceutical Engineering Services | JCS Engineering PLLC"
    desc = "Six engineering services for pharma and biotech capital projects: project engineering, design, construction oversight, CQV, change management and tech transfer."
    crumbs = [("Home", "/"), ("Capabilities", None)]
    body = page_head(crumbs, "Engineering services for regulated manufacturing.",
        "Six services covering a capital project from concept through a qualified, operating facility — engaged individually or as an integrated scope, for pharmaceutical, biotech, and advanced manufacturing owners in North Carolina.",
        f'<nav class="cap-index reveal" aria-label="Capabilities">{idx}</nav>') + f'''
    <section class="section-tight"><div class="container narrow">{caps}</div></section>
    {cta_band("Not sure which of these you need?", "Most engagements start with a short conversation about where the project stands. We'll tell you plainly what would help.")}
'''
    ld = ld_graph(ld_webpage("/capabilities/", title, desc, "CollectionPage"), ld_breadcrumbs(crumbs),
                  {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": SITE + svc_url(s), "name": unesc(s["title"])} for i, s in enumerate(C.SERVICES)]})
    return page("/capabilities/", title, desc, body, ld)

def service_page(s):
    title = f'{s["page_title"]} | {LEGAL}'
    path = svc_url(s)
    crumbs = [("Home", "/"), ("Capabilities", "/capabilities/"), (s["title"], None)]
    body = page_head(crumbs, s["h1"], s["intro"]) + f'''
    <section class="section">
      <div class="container narrow svc">
        <h2>Scope of service</h2>
        <ul class="scope reveal">{"".join(f"<li>{x}</li>" for x in s["scope"])}</ul>

        <h2>How we work</h2>
        <p class="reveal">{s["process"]}</p>

        <h2>Deliverables</h2>
        <ul class="deliv-list reveal">{"".join(f"<li>{x}</li>" for x in s["deliv"])}</ul>

        <h2>Who this is for</h2>
        <p class="reveal">{s["who"]}</p>

        <h2>Why JCS Engineering</h2>
        <p class="reveal">{s["why"]}</p>

        <h2>Frequently asked questions</h2>
        {faq_block(s["faq"])}

        <div class="svc-cta reveal">
          <p>Ready to talk about {s["title"].lower()} on your project? Call <a href="tel:{C.PHONE_E164}">{C.PHONE_DISPLAY}</a> or <a href="/contact/">send us the details</a> — we respond within one business day.</p>
        </div>
        {related_html(s)}
      </div>
    </section>
    {cta_band()}
'''
    ld = ld_graph(ld_webpage(path, title, s["meta"], "WebPage", {"mainEntity": {"@id": SITE + path + "#service"}}), ld_service(s), ld_breadcrumbs(crumbs), ld_faq(s["faq"]))
    return page(path, title, s["meta"], body, ld)

def approach():
    steps = [("01", "Concept", "Turn a business need into a defensible project: capacity basis, options, order-of-magnitude cost, and the risks that decide whether it's worth pursuing."),
             ("02", "Design", "Lock intent before it's expensive to change: user requirements, basis of design, and owner-side review at each design milestone."),
             ("03", "Procurement", "Buy the right equipment from the right vendors, with FAT and delivery sequenced against the schedule."),
             ("04", "Construction", "Verify that what's built matches what was designed — while protecting the operations next door."),
             ("05", "CQV", "Bring systems to a documented, GMP-ready state with protocols that trace back to requirements."),
             ("06", "Handover", "Turn a construction project into a production asset: turnover packages, training, punch closure, and lessons learned.")]
    steps_html = "".join(f'<li class="reveal"><span class="n">PHASE {n}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for n, t, d in steps)
    title = "Stage-Gate Project Delivery | JCS Engineering PLLC"
    desc = "How JCS Engineering delivers pharma and biotech capital projects: six phases with defined deliverables, four engagement models, and the standards we work to."
    crumbs = [("Home", "/"), ("Approach", None)]
    body = page_head(crumbs, "How we work.", "Clear phases, defined deliverables, and one accountable engineer at each gate. Engagements are sized to the work — a scoped deliverable, milestone oversight, a full program, or staff embedded in your team.") + f'''
    <section class="section"><div class="container narrow">
      <header class="section-head reveal">{eyebrow("Delivery")}<h2>Six phases, in order.</h2>
        <p class="section-sub">Each phase ends with defined deliverables and a go/no-go decision, so leadership sees a decision at every transition rather than a surprise at the end. <a href="/capabilities/project-engineering/">Project engineering and management</a> carries the thread across all six.</p></header>
      <ol class="steps">{steps_html}</ol>
    </div></section>
    <section class="section section-alt"><div class="container narrow">
      <header class="section-head reveal">{eyebrow("Engagement")}<h2>Shaped to the project</h2></header>
      <ul class="diff reveal">
        <li><h3>Defined scope</h3><p>A specific deliverable — a <a href="/capabilities/engineering-design/">design package</a>, a <a href="/capabilities/cqv/">CQV package</a>, a fit-gap assessment, a design review — with a clear start and finish.</p></li>
        <li><h3>Milestone oversight</h3><p>Part-time involvement concentrated at design reviews, gate decisions, FATs, and startup.</p></li>
        <li><h3>Full program</h3><p>Continuous, often on-site engineering and project management through the life of a project.</p></li>
        <li><h3>Embedded engineer or team</h3><p>Engineers, project managers, or CQV leads placed in your organization for the life of a program.</p></li>
      </ul>
    </div></section>
    <section class="section" id="standards"><div class="container">
      <header class="section-head reveal">{eyebrow("Standards")}<h2>Codes and guidance we design and qualify against</h2></header>
      <div class="standards">{standards_html()}</div>
    </div></section>
    {cta_band()}
'''
    ld = ld_graph(ld_webpage("/approach/", title, desc), ld_breadcrumbs(crumbs))
    return page("/approach/", title, desc, body, ld)

def service_areas():
    hubs = "".join(f'<li class="reveal"><h3>{n}</h3><p>{d}</p></li>' for n, d in C.HUBS)
    munis = ", ".join(n for n, t in C.AREA_SERVED if t == "City")
    title = "Serving the Research Triangle | JCS Engineering PLLC"
    desc = "Engineering consultant for pharma and biotech capital projects across the Research Triangle and North Carolina: Raleigh, Durham, RTP, Holly Springs and Clayton."
    crumbs = [("Home", "/"), ("Service areas", None)]
    body = page_head(crumbs, "Serving North Carolina's biomanufacturing corridor.",
        f"JCS Engineering is based in the Raleigh area and works on-site, remotely, and in hybrid arrangements across the Research Triangle and the state's life-sciences manufacturing hubs. Firm License {C.PRINCIPAL['firm_lic']} covers engineering practice statewide.") + f'''
    <section class="section"><div class="container narrow svc">
      <h2>Where the work is</h2>
      <p class="reveal">North Carolina has become one of the largest concentrations of pharmaceutical and biologics manufacturing in the United States, and almost all of it sits within a ninety-minute drive of Raleigh. That geography is why a Raleigh-based firm can offer on-site engineering, construction oversight, and CQV leadership without travel overhead — and why we know the contractors, design firms, vendors, and regulators our clients work with.</p>
      <ul class="hubs">{hubs}</ul>
      <h2>How we serve the area</h2>
      <p class="reveal">On-site presence scales with the phase: field time during construction, tie-ins, and CQV; remote work during design review and planning. For programs that need continuous coverage we <a href="/approach/">embed engineers and project managers</a> in the client's organization for the duration. Same-day site visits are practical anywhere in Wake, Durham, and Johnston counties; the corridor east and south of the Triangle is a regular day trip.</p>
      <h2>Municipalities served</h2>
      <p class="reveal">{munis}, and communities throughout Wake, Durham, and Johnston counties. Statewide engagements are welcome under our North Carolina firm license; our principal has also delivered projects in Massachusetts.</p>
      <div class="svc-cta reveal"><p>Have a project in the Triangle or along the corridor? <a href="/contact/">Tell us where it stands</a> or call <a href="tel:{C.PHONE_E164}">{C.PHONE_DISPLAY}</a>.</p></div>
    </div></section>
    {cta_band()}
'''
    ld = ld_graph(ld_webpage("/service-areas/", title, desc), ld_breadcrumbs(crumbs))
    return page("/service-areas/", title, desc, body, ld)

def experience():
    exps = "".join(f'''
        <article class="exp reveal" id="{e["slug"]}">
          <div class="meta"><span class="hl">{e["hl"]}</span>{"".join(f"<span>{m}</span>" for m in e["meta"])}</div>
          <h2>{e["title"]}</h2>
          <p class="role"><strong>Role:</strong> {e["role"]}</p>
          <p class="summary">{e["summary"]}</p>
          <ul class="scope">{"".join(f"<li>{x}</li>" for x in e["scope"])}</ul>
          <div class="tags">{"".join(f"<span>{t}</span>" for t in e["tags"])}</div>
        </article>''' for e in C.EXPERIENCE)
    title = "Pharma Project Experience | JCS Engineering PLLC"
    desc = "Representative capital project experience: a $25M spray-drying facility expansion, inhaler and microvial programs, a biologics site startup and an API program."
    crumbs = [("Home", "/"), ("Experience", None)]
    body = page_head(crumbs, "Representative experience.",
        "Drawn from our team's responsible-engineer roles in industry, prior to and alongside founding JCS Engineering. Each covers the phases you would hire an owner's engineer, a design engineer, or a CQV lead to own. Locations are shown; employers and clients are not.") + f'''
    <section class="section-tight"><div class="container"><div class="exp-list">{exps}</div></div></section>
    {cta_band("Have a project like one of these?", "The fastest way to find out whether the experience fits is a short technical conversation about where your project stands.")}
'''
    ld = ld_graph(ld_webpage("/experience/", title, desc, "CollectionPage"), ld_breadcrumbs(crumbs),
                  {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": unesc(e["title"]), "url": SITE + "/experience/#" + e["slug"]} for i, e in enumerate(C.EXPERIENCE)]})
    return page("/experience/", title, desc, body, ld)

def faq_page():
    groups = [("General", C.FAQ)] + [(s["title"], s["faq"]) for s in C.SERVICES]
    sections = "".join(f'<h2 id="{re.sub(r"[^a-z0-9]+","-",unesc(g).lower()).strip("-")}">{g}</h2>{faq_block(items)}' for g, items in groups)
    allq = [qa for _, items in groups for qa in items]
    title = "Frequently Asked Questions | JCS Engineering PLLC"
    desc = "Answers to common questions about hiring an engineering consultant for pharma and biotech capital projects: owner's rep, design, CQV and tech transfer."
    crumbs = [("Home", "/"), ("FAQ", None)]
    body = page_head(crumbs, "Frequently asked questions.", "What owners, project managers, and quality leaders ask before engaging an engineering consultant on a cGMP capital project. If yours isn't here, ask us directly.") + f'''
    <section class="section"><div class="container narrow svc faq-page">{sections}
      <div class="svc-cta reveal"><p>Still have a question? Call <a href="tel:{C.PHONE_E164}">{C.PHONE_DISPLAY}</a> or <a href="/contact/">send it to us</a>.</p></div>
    </div></section>
    {cta_band()}
'''
    ld = ld_graph(ld_webpage("/faq/", title, desc, "FAQPage", {"mainEntity": ld_faq(allq)["mainEntity"]}), ld_breadcrumbs(crumbs))
    return page("/faq/", title, desc, body, ld)

def insights_index():
    cards = "".join(f'<article class="card reveal"><p class="eyebrow"><span class="tick"></span><time datetime="{p["date"]}">{_pretty(p["date"])}</time> · {p["minutes"]} min read</p><h2><a href="{post_url(p)}">{p["title"]}</a></h2><p>{p["excerpt"]}</p><a class="link-arrow" href="{post_url(p)}">Read the article {ARROW}</a></article>' for p in C.POSTS)
    title = "Insights on Pharma Capital Projects | JCS Engineering PLLC"
    desc = "Practical articles on pharmaceutical and biotech capital projects: owner's representation, CQV planning, tech transfer, design and construction oversight."
    crumbs = [("Home", "/"), ("Insights", None)]
    body = page_head(crumbs, "Insights.", "Practical notes on capital projects in regulated manufacturing, written from the owner's side of the table. New articles monthly.") + f'''
    <section class="section"><div class="container"><div class="cards cards-3">{cards}</div></div></section>
    {cta_band()}
'''
    ld = ld_graph(ld_webpage("/insights/", title, desc, "CollectionPage"), ld_breadcrumbs(crumbs),
                  {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": SITE + post_url(p), "name": unesc(p["title"])} for i, p in enumerate(C.POSTS)]})
    return page("/insights/", title, desc, body, ld)

def _pretty(d):
    y, m, dd = d.split("-"); return f"{['January','February','March','April','May','June','July','August','September','October','November','December'][int(m)-1]} {int(dd)}, {y}"

def post_page(p):
    title = f'{p["page_title"]} | {LEGAL}'
    path = post_url(p)
    crumbs = [("Home", "/"), ("Insights", "/insights/"), (p["title"], None)]
    rel = "".join(f'<li><a href="{svc_url(svc(x))}">{svc(x)["title"]} {ARROW}</a></li>' for x in p["services"])
    others = "".join(f'<li><a href="{post_url(o)}">{o["title"]} {ARROW}</a></li>' for o in C.POSTS if o["slug"] != p["slug"])
    body = f'''
    <article class="post">
      <header class="page-head grid-bg"><div class="container narrow">
        {crumbs_html(crumbs)}
        <h1 class="reveal">{p["title"]}</h1>
        <p class="post-meta reveal">By <a href="/about/#drew-jones">Drew Jones, PE</a> · <time datetime="{p["date"]}">{_pretty(p["date"])}</time> · {p["minutes"]} min read</p>
      </div></header>
      <div class="section"><div class="container prose post-body reveal">{POST_BODIES[p["slug"]]}
        <aside class="related">
          <div><p class="footer-h">Related capabilities</p><ul>{rel}</ul></div>
          <div><p class="footer-h">More insights</p><ul>{others}</ul></div>
        </aside>
      </div></div>
    </article>
    {cta_band()}
'''
    ld = ld_graph(ld_webpage(path, title, p["meta"], "WebPage"), ld_article(p), ld_breadcrumbs(crumbs))
    return page(path, title, p["meta"], body, ld, og_type="article", article=p)

def about():
    P = C.PRINCIPAL
    facts = [("Legal name", LEGAL), ("Founded by", "Drew W. Jones, PE"), ("Office", f'{C.ADDRESS["street"] + ", " if C.ADDRESS.get("street") else ""}{C.ADDRESS["locality"]}, NC {C.ADDRESS.get("postal") or ""}'.strip()),
             ("Serves", "The Research Triangle and North Carolina; projects also delivered in Massachusetts"),
             ("Firm license", f"NC Board of Examiners for Engineers &amp; Surveyors, {P['firm_lic']}"), ("Principal's license", f"Professional Engineer, North Carolina, No. {P['pe_no']}"),
             ("Industries", "Pharmaceutical · Biotechnology · Advanced manufacturing"), ("Services", ", ".join(s["title"] for s in C.SERVICES))]
    if C.FOUNDING_YEAR: facts.insert(2, ("Founded", C.FOUNDING_YEAR))
    facts_html = "".join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in facts)
    title = "About the Firm | JCS Engineering PLLC"
    desc = "JCS Engineering PLLC is a licensed North Carolina engineering firm led by Drew Jones, PE: project engineering, design, CQV and project management for cGMP."
    crumbs = [("Home", "/"), ("About", None)]
    body = page_head(crumbs, "About JCS Engineering.", "A licensed North Carolina engineering firm serving pharmaceutical, biotech, and advanced manufacturing.") + f'''
    <section class="section"><div class="container narrow">
      <p class="about-para reveal">JCS Engineering PLLC provides project engineering, design, CQV, and project management to pharmaceutical, biotech, and advanced manufacturing clients. The firm was founded by Drew Jones, PE, a chemical engineer with more than eight years on the owner's side of cGMP capital projects — from process and mechanical design through construction, commissioning, and qualification — and it scales from a single engineer to a full project team, accountable for every engagement under its North Carolina engineering license.</p>
      <dl class="facts reveal">{facts_html}</dl>
    </div></section>
    <section class="section section-alt" id="leadership"><div class="container narrow">
      <div class="person" id="drew-jones">
        <figure class="photo reveal"><picture><source type="image/webp" srcset="/assets/img/drew-jones-400.webp" />
          <img src="/assets/img/drew-jones-400.jpg" alt="Drew Jones, PE, founder and principal engineer of JCS Engineering" width="400" height="400" loading="lazy" /></picture></figure>
        <div class="reveal">
          {eyebrow("Leadership")}
          <h2 class="name">{P["name"]}</h2>
          <p class="title">{P["title"]}</p>
          <ul class="cred-lines">
            <li>Professional Engineer, {P["pe_state"]} · No. {P["pe_no"]}</li>
            <li>NC Engineering Firm License {P["firm_lic"]}</li>
            <li>{P["education"]}, {P["school"]}</li>
            <li>Lean Six Sigma Green Belt</li>
          </ul>
          <p class="p-body">See <a href="/experience/">representative experience</a> and <a href="/insights/">Insights</a>.</p>
        </div>
      </div>
    </div></section>
    {cta_band("Talk to an engineer.", "A first conversation is a technical one: where the project stands, what's at risk, and whether we're the right fit.")}
'''
    ld = ld_graph(ld_webpage("/about/", title, desc, "AboutPage", {"mainEntity": {"@id": ORG_ID}}), ld_breadcrumbs(crumbs))
    return page("/about/", title, desc, body, ld)

def contact():
    title = "Contact an Engineer in Raleigh, NC | JCS Engineering PLLC"
    desc = "Contact JCS Engineering in Raleigh, NC about project engineering, design, CQV or owner's representation for a pharma or biotech project. Reply within a day."
    crumbs = [("Home", "/"), ("Contact", None)]
    body = page_head(crumbs, "Let's scope your project.", "Tell us where the project stands — concept, mid-design, or already in the field. We respond within one business day.") + f'''
    <section class="section"><div class="container contact-grid">
      <div class="reveal">
        {eyebrow("Reach Us")}
        <h2>Direct line to an engineer.</h2>
        <ul class="contact-list">
          <li><span class="mono">ADDRESS</span><span>{C.ADDRESS["street"] + "<br>" if C.ADDRESS.get("street") else ""}{C.ADDRESS["locality"]}, {C.ADDRESS["region"]} {C.ADDRESS.get("postal") or ""}<br><span class="dim">{C.SERVICE_AREA_LINE}</span></span></li>
          <li><span class="mono">PHONE</span><a href="tel:{C.PHONE_E164}">{C.PHONE_DISPLAY}</a></li>
          <li><span class="mono">EMAIL</span><a href="mailto:{C.EMAIL}">{C.EMAIL}</a></li>
        </ul>
        <h3 class="mt-44">What to expect</h3>
        <ol class="expect">
          <li><span class="n">01</span><div><strong>A reply within one business day</strong>From an engineer, not an autoresponder.</div></li>
          <li><span class="n">02</span><div><strong>A short scoping call</strong>Where the project stands, what's at risk, what a sensible engagement would look like.</div></li>
          <li><span class="n">03</span><div><strong>A written proposal</strong>Scope, structure, and fees in plain language — or a straight answer if we're not the right fit.</div></li>
        </ol>
        <h3 class="mt-44">Useful to include</h3>
        <p class="p-body">The facility and product type, the project phase, what is driving the timeline, and what has you concerned. If there is a URS, a schedule, or a drawing set, say so — we will ask to see it on the call. Whether you need <a href="/capabilities/project-engineering/">owner's representation</a>, <a href="/capabilities/engineering-design/">design</a>, <a href="/capabilities/cqv/">CQV</a>, or an <a href="/approach/">embedded engineer</a>, the first conversation is the same: technical, specific, and confidential.</p>
      </div>
      <form class="contact-form reveal" id="contact-form" action="{C.FORMSPREE}" method="POST" novalidate>
        <div class="form-row">
          <div class="field"><label for="cf-name">Name</label><input id="cf-name" type="text" name="name" autocomplete="name" required></div>
          <div class="field"><label for="cf-email">Email</label><input id="cf-email" type="email" name="email" autocomplete="email" required></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="cf-company">Company <span class="opt">(optional)</span></label><input id="cf-company" type="text" name="company" autocomplete="organization"></div>
          <div class="field"><label for="cf-phone">Phone <span class="opt">(optional)</span></label><input id="cf-phone" type="tel" name="phone" autocomplete="tel"></div>
        </div>
        <div class="field"><label for="cf-stage">Project stage</label>
          <select id="cf-stage" name="project_stage"><option value="">Select one</option><option>Concept / feasibility</option><option>Design</option><option>Procurement</option><option>Construction</option><option>CQV / startup</option><option>Operating facility — improvement or expansion</option><option>Not sure yet</option></select></div>
        <div class="field"><label for="cf-message">Project details</label><textarea id="cf-message" name="message" rows="5" required></textarea></div>
        <div class="hp" aria-hidden="true"><label for="cf-gotcha">Leave this field empty</label><input id="cf-gotcha" type="text" name="_gotcha" tabindex="-1" autocomplete="off"></div>
        <input type="hidden" name="_subject" value="New inquiry from jcseng.com">
        <button type="submit" class="btn">Send message {ARROW}</button>
        <div class="form-status" id="form-status" role="status" aria-live="polite" hidden></div>
        <p class="form-note">We'll respond within one business day. Your details are used only to reply to you — see our <a href="/privacy/">privacy policy</a>.</p>
      </form>
      <template id="form-success-tpl"><div class="form-success">{CHECK}<h3>Message received.</h3><p>Thanks — we'll be in touch within one business day. If it's time-sensitive, call <a href="tel:{C.PHONE_E164}">{C.PHONE_DISPLAY}</a>.</p></div></template>
    </div></section>
    <div class="map-section"><iframe title="Map showing the JCS Engineering office at 5540 Centerview Drive, Raleigh, North Carolina" src="{C.MAP_SRC}" width="1200" height="420" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
'''
    ld = ld_graph(ld_webpage("/contact/", title, desc, "ContactPage", {"mainEntity": {"@id": ORG_ID}}), ld_breadcrumbs(crumbs))
    return page("/contact/", title, desc, body, ld)

def privacy():
    title = "Privacy Policy | JCS Engineering PLLC"
    desc = "What jcseng.com collects and why: contact-form details used only to reply to you, standard server logs, no advertising and no analytics cookies. Plain language."
    crumbs = [("Home", "/"), ("Privacy", None)]
    body = page_head(crumbs, "Privacy policy.", "What this website collects, why, and who else is involved. Written to be read.") + f'''
    <section class="section"><div class="container prose prose-body reveal">
      <p class="meta">EFFECTIVE 8 SEPTEMBER 2026 · {LEGAL.upper()}</p>
      <h2>Summary</h2>
      <p>This site collects personal information in exactly one place: the contact form. We use what you send us to reply to you. We don't run advertising, we don't sell or share your information for marketing, and we don't set analytics cookies.</p>
      <h2>What we collect</h2>
      <h3>Contact form</h3>
      <p>If you submit the form on our <a href="/contact/">contact page</a>, we receive the information you enter: your name, email address, message, and — if you choose to provide them — company, phone number, and project stage. We use this to respond to your inquiry and, if we work together, as part of our business records.</p>
      <h3>Server logs</h3>
      <p>Like every website, our hosting provider records technical information about requests — IP address, browser type, pages requested, and timestamps — for security and to keep the site running. We don't combine this with anything that identifies you.</p>
      <h2>Third parties involved in this site</h2>
      <ul>
        <li><strong>Formspree</strong> processes contact-form submissions and delivers them to us by email. See <a href="https://formspree.io/legal/privacy-policy/" rel="noopener">Formspree's privacy policy</a>.</li>
        <li><strong>Cloudflare</strong> hosts and serves this website and provides security services. See <a href="https://www.cloudflare.com/privacypolicy/" rel="noopener">Cloudflare's privacy policy</a>.</li>
        <li><strong>Google Maps</strong> provides the embedded map on the contact page. Loading it sends a request to Google, which may set cookies according to <a href="https://policies.google.com/privacy" rel="noopener">Google's privacy policy</a>. The map only loads when you scroll to it.</li>
      </ul>
      <p>Fonts are served from our own domain, not from a third-party font service. We notify search engines of new pages through the IndexNow protocol; that sends them our page URLs and nothing about you. We may use <strong>Cloudflare Web Analytics</strong> to count page views; it is cookieless, does not fingerprint devices, and does not track you across sites — see <a href="https://www.cloudflare.com/web-analytics/" rel="noopener">how it works</a>.</p>
      <h2>Cookies</h2>
      <p>We do not set cookies for analytics, advertising, or tracking; Cloudflare Web Analytics works without cookies. The embedded Google Map may set its own cookies when it loads, as described above.</p>
      <h2>How long we keep it</h2>
      <p>Contact-form inquiries are kept as long as needed to respond and, where an inquiry leads to an engagement, as part of our business records. You can ask us to delete your inquiry at any time.</p>
      <h2>Your choices</h2>
      <p>You can ask us what information we hold about you, ask us to correct it, or ask us to delete it. Email <a href="mailto:{C.EMAIL}">{C.EMAIL}</a> and we'll respond within a reasonable time.</p>
      <h2>Changes</h2>
      <p>If this policy changes, we'll update the effective date above. Material changes will be noted on this page.</p>
      <h2>Contact</h2>
      <p>{LEGAL}<br>{C.ADDRESS["locality"]}, North Carolina<br><a href="mailto:{C.EMAIL}">{C.EMAIL}</a> · <a href="tel:{C.PHONE_E164}">{C.PHONE_DISPLAY}</a></p>
    </div></section>
'''
    ld = ld_graph(ld_webpage("/privacy/", title, desc), ld_breadcrumbs(crumbs))
    return page("/privacy/", title, desc, body, ld)

def notfound():
    title = "Page Not Found | JCS Engineering PLLC"
    desc = "The page you requested could not be found. Search the site or use the navigation to find JCS Engineering's services, approach, experience and contact details."
    links = "".join(f'<li><a href="{svc_url(s)}">{s["title"]}</a></li>' for s in C.SERVICES)
    body = f'''
    <section class="page-head grid-bg nf">
      <div class="container narrow center">
        <p class="eyebrow center"><span class="tick"></span>Error 404</p>
        <h1>This page isn't here.</h1>
        <p class="lede">The page may have moved or no longer exists. Search the site, or start from one of the pages below.</p>
        <form class="site-search" action="https://www.google.com/search" method="get" role="search">
          <input type="hidden" name="as_sitesearch" value="jcseng.com">
          <label for="q" class="visually-hidden">Search jcseng.com</label>
          <input id="q" type="search" name="q" placeholder="Search jcseng.com" required>
          <button type="submit" class="btn">Search</button>
        </form>
        <div class="ctas center"><a class="btn ghost" href="/">Home</a><a class="btn ghost" href="/capabilities/">Capabilities</a><a class="btn ghost" href="/contact/">Contact</a></div>
        <ul class="nf-links">{links}</ul>
      </div>
    </section>
'''
    ld = ld_graph(ld_webpage("/404.html", title, desc))
    return page("/404.html", title, desc, body, ld, noindex=True)

# =============================================================================================
# Non-HTML outputs
# =============================================================================================
def robots():
    ai = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "PerplexityBot", "ClaudeBot", "Claude-SearchBot", "anthropic-ai", "Google-Extended", "Applebot-Extended", "Bytespider", "CCBot", "cohere-ai", "meta-externalagent"]
    lines = ["# jcseng.com — all major search and AI crawlers welcome; utility paths excluded.", "User-agent: *", "Allow: /", "Disallow: /docs/", "Disallow: /tools/", "Disallow: /.github/", ""]
    for ua in ["Googlebot", "Bingbot", "DuckDuckBot", "Slurp", "Applebot"] + ai:
        lines += [f"User-agent: {ua}", "Allow: /", ""]
    lines += [f"Sitemap: {SITE}/sitemap.xml", ""]
    return "\n".join(lines)

def sitemap():
    img = {"/": ["/assets/img/bioreactors-1200.jpg", "/assets/img/og-card.png"], "/about/": ["/assets/img/drew-jones-400.jpg"]}
    pri = {"/": "1.0", "/capabilities/": "0.9", "/contact/": "0.8", "/approach/": "0.7", "/experience/": "0.7", "/insights/": "0.7", "/about/": "0.6", "/service-areas/": "0.7", "/faq/": "0.5", "/privacy/": "0.2"}
    out = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
    for path, title, desc, noindex in PAGES:
        if noindex: continue
        lastmod = TODAY
        for p in C.POSTS:
            if post_url(p) == path: lastmod = p["modified"]
        p_ = pri.get(path, "0.8" if path.startswith("/capabilities/") else "0.6")
        out.append(f"  <url><loc>{SITE}{path}</loc><lastmod>{lastmod}</lastmod><changefreq>monthly</changefreq><priority>{p_}</priority>"
                   + "".join(f"<image:image><image:loc>{SITE}{i}</image:loc></image:image>" for i in img.get(path, [])) + "</url>")
    out.append("</urlset>\n")
    return "\n".join(out)

def llms_txt():
    lines = [f"# {LEGAL}", "", f"> {unesc(C.TAGLINE)}. Licensed North Carolina engineering firm (Firm License {C.PRINCIPAL['firm_lic']}) based in the Raleigh area, serving the Research Triangle and North Carolina's biomanufacturing corridor. Founded and led by Drew W. Jones, PE (NC License {C.PRINCIPAL['pe_no']}).", "",
             "## Facts", f"- Legal name: {LEGAL}", f"- Website: {SITE}/", f"- Phone: {C.PHONE_PLAIN}", f"- Email: {C.EMAIL}", f"- Location: {C.ADDRESS['locality']}, North Carolina, US", "- Industries: pharmaceutical, biotechnology, advanced manufacturing",
             "- Clients: manufacturing owners, CDMOs, and the design firms and contractors that serve them", ""]
    if C.FOUNDING_YEAR: lines.insert(6, f"- Founded: {C.FOUNDING_YEAR}")
    lines += ["## Services"] + [f"- [{unesc(s['title'])}]({SITE}{svc_url(s)}): {unesc(s['short'])}" for s in C.SERVICES] + [""]
    lines += ["## Key pages", f"- [Capabilities]({SITE}/capabilities/)", f"- [Approach — stage-gate delivery, engagement models, standards]({SITE}/approach/)", f"- [Representative experience]({SITE}/experience/)",
              f"- [Service areas]({SITE}/service-areas/)", f"- [About and leadership]({SITE}/about/)", f"- [FAQ]({SITE}/faq/)", f"- [Contact]({SITE}/contact/)", ""]
    lines += ["## Insights"] + [f"- [{unesc(p['title'])}]({SITE}{post_url(p)}): {unesc(p['excerpt'])}" for p in C.POSTS] + [""]
    lines += ["## Optional", f"- [Privacy policy]({SITE}/privacy/)", f"- [Sitemap]({SITE}/sitemap.xml)", ""]
    return "\n".join(lines)

def humans_txt():
    return f"/* TEAM */\n{LEGAL}\nPrincipal: Drew W. Jones, PE\nLocation: {C.ADDRESS['locality']}, North Carolina, US\nContact: {C.EMAIL}\n\n/* SITE */\nLast update: {TODAY}\nStandards: HTML5, CSS3, vanilla JS, JSON-LD\nFonts: Inter, IBM Plex Mono (self-hosted)\nHosting: Cloudflare Pages\n"

def manifest():
    return json.dumps({"name": LEGAL, "short_name": BRAND, "description": unesc(C.TAGLINE), "start_url": "/", "scope": "/", "display": "browser",
                       "background_color": "#ffffff", "theme_color": "#111318", "lang": "en-US",
                       "icons": [{"src": "/assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
                                 {"src": "/assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"},
                                 {"src": "/assets/img/icon-512-maskable.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}, indent=2) + "\n"

# =============================================================================================
# Validation + write
# =============================================================================================
def validate(path, content):
    t = re.search(r"<title>(.*?)</title>", content, re.S).group(1); d = re.search(r'<meta name="description" content="(.*?)"', content).group(1)
    errs = []
    if len(html.unescape(t)) > 60: errs.append(f"title {len(html.unescape(t))} chars > 60: {t}")
    if not 140 <= len(html.unescape(d)) <= 160: errs.append(f"description {len(html.unescape(d))} chars not in 140-160")
    if content.count("<h1") != 1: errs.append(f"{content.count('<h1')} h1 elements")
    if "[VERIFY]" in content or "None" in re.sub(r"<script.*?</script>", "", content, flags=re.S) and "None<" in content: errs.append("placeholder leaked")
    if 'lang="en-US"' not in content: errs.append("lang")
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', content, re.S):
        json.loads(m.group(1))
    if errs: raise SystemExit(f"BUILD FAILED {path}: " + "; ".join(errs))

def write(path, content, validate_html=True):
    full = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    if validate_html: validate(path, content)
    open(full, "w", encoding="utf-8").write(content)
    print(f"{path:60s} {len(content.encode()):>7,} bytes")

def inventory_csv():
    rows = []
    for path, title, desc, noindex in PAGES:
        full = os.path.join(ROOT, path.lstrip("/"), "index.html") if path.endswith("/") else os.path.join(ROOT, path.lstrip("/"))
        c = open(full, encoding="utf-8").read()
        h1 = html.unescape(re.sub(r"<[^>]+>", "", re.search(r"<h1[^>]*>(.*?)</h1>", c, re.S).group(1))).strip()
        words = len(re.sub(r"<[^>]+>", " ", re.search(r"<main[^>]*>(.*?)</main>", c, re.S).group(1)).split())
        types = sorted({n.get("@type") if isinstance(n.get("@type"), str) else "/".join(n.get("@type")) for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', c, re.S) for n in json.loads(m.group(1))["@graph"]})
        rows.append([SITE + path, "noindex" if noindex else "index", html.unescape(title), len(html.unescape(title)), html.unescape(desc), len(html.unescape(desc)), h1, words, SITE + path, "yes", ";".join(types)])
    with open(os.path.join(ROOT, "docs/seo_page_inventory.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["url", "indexability", "title", "title_length", "meta_description", "description_length", "h1", "word_count", "canonical", "og_tags", "schema_types"]); w.writerows(rows)
    print(f"docs/seo_page_inventory.csv                                   {len(rows)} rows")

if __name__ == "__main__":
    write("index.html", home())
    write("capabilities/index.html", capabilities())
    for s in C.SERVICES: write(svc_url(s) + "index.html", service_page(s))
    write("approach/index.html", approach())
    write("service-areas/index.html", service_areas())
    write("experience/index.html", experience())
    write("faq/index.html", faq_page())
    write("insights/index.html", insights_index())
    for p in C.POSTS: write(post_url(p) + "index.html", post_page(p))
    write("about/index.html", about())
    write("contact/index.html", contact())
    write("privacy/index.html", privacy())
    write("404.html", notfound())
    write("robots.txt", robots(), False)
    write("sitemap.xml", sitemap(), False)
    write("llms.txt", llms_txt(), False)
    write("humans.txt", humans_txt(), False)
    write("site.webmanifest", manifest(), False)
    write(f"{C.INDEXNOW_KEY}.txt", C.INDEXNOW_KEY + "\n", False)
    inventory_csv()
