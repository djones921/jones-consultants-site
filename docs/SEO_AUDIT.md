# SEO Audit — jcseng.com

**Audited:** 2026-09-08 · **Commit audited:** `cc38f49` (live `main`) · **Method:** repository inspection, headless-Chromium crawl of the built site at every route, Lighthouse 12.6 (mobile emulation and desktop) on the home page and the three most important interior pages, axe-core accessibility scan, html-validate.

**Stack confirmed:** hand-maintained static HTML (no framework, no build step) generated from a Python template script; hosted on Cloudflare Pages, deployed on push to `main`; assets served with content-hashed URLs and `_headers` cache policy; fonts self-hosted; contact form via Formspree.

---

## Prioritized findings

| # | Finding | Impact | Effort | Phase |
|---|---|---|---|---|
| 1 | **All six services share one page** (`/capabilities/`, 584 words ≈ 97 words per service). No page can rank for a specific service query; no FAQ per service. | High | Med | 2–3 |
| 2 | **No location / service-area signal beyond "Raleigh, NC" in the footer.** No address, no geo, no service-area list, no `areaServed` entities. Google Maps and "near me" queries have nothing to attach to. | High | Low | 3–4 |
| 3 | **No blog / insights section.** Zero informational content; nothing for AI answer engines to cite; no internal-link targets beyond six pages. | High | High | 2 |
| 4 | **Structured data is a single `ProfessionalService` block** repeated on every page (plus FAQPage on home). No `Person`, `Service`, `BreadcrumbList`, `WebSite`, `WebPage`, `Article`, no `sameAs`, no `hasOfferCatalog`, no `areaServed`. | High | Med | 4 |
| 5 | **Metadata lengths.** Home `<title>` is 79 chars (truncates ≈ 60). Five of six descriptions are 168–196 chars (truncate ≈ 160). No `<meta name="robots">`. `lang="en"` rather than `en-US`. | Med | Low | 3 |
| 6 | **Thin pages:** `/about/` 162 words, `/contact/` 156 words. | Med | Med | 3 |
| 7 | **No off-site entity links** (LinkedIn, Google Business Profile) referenced from the site, so search engines cannot connect the website to the existing profiles. | Med | Low | 4, 6 |
| 8 | **No `llms.txt`, no `humans.txt`, no web manifest, no 192/512 icons.** AI crawlers not explicitly addressed in `robots.txt`. | Med | Low | 5 |
| 9 | **Security headers incomplete:** no `Strict-Transport-Security`, no `Content-Security-Policy`. | Med | Low | 5 |
| 10 | **Sitemap has no `<lastmod>` accuracy, no image entries.** No IndexNow. No Search Console / Bing verification present. | Med | Low | 5 |
| 11 | **No CI regression guard** — nothing prevents a future edit from shipping a broken link, invalid HTML, or a Lighthouse regression. | Med | Med | 5 |
| 12 | Dead asset `assets/img/bioreactors.jpg` (231 KB) unreferenced in repo. | Low | Low | 5 |
| 13 | Footer NAP lacks hours and address (or service-area statement); cannot yet be matched to Google Business Profile. | Med | Low | 3 (needs owner input) |
| 14 | 404 page has navigation but no search. | Low | Low | 3 |

**What is already right (do not regress):** Lighthouse 99–100 in every category; CLS 0.000; page weight 135–202 KB; self-hosted, subset, preloaded fonts; responsive WebP with JPEG fallback; content-hashed CSS/JS with immutable caching; HTML never cached; one `<h1>` per page; no skipped heading levels; unique canonicals; OG/Twitter tags with a 1200×630 card; skip link, landmarks, ≥24 px tap targets, AA contrast; axe-core clean; html-validate clean; zero console errors; zero horizontal overflow at 390–1440 px.

---

## Page inventory (before)

| URL | Status | Title (len) | Description (len) | H1 | Words | Images | JSON-LD | Inbound links | Robots meta |
|---|---|---|---|---|---|---|---|---|---|
| `/` | 200 | JCS Engineering — Project Engineering, Design & CQV for Regulated Manufacturing (79) | 191 | 1 | 415 | 3 | ProfessionalService, FAQPage | 6 | none |
| `/capabilities/` | 200 | Capabilities — JCS Engineering (30) | 196 | 1 | 584 | 2 | ProfessionalService | 6 | none |
| `/approach/` | 200 | Approach — JCS Engineering (26) | 168 | 1 | 463 | 2 | ProfessionalService | 6 | none |
| `/about/` | 200 | About — JCS Engineering (23) | 189 | 1 | 162 | 3 | ProfessionalService | 6 | none |
| `/contact/` | 200 | Contact — JCS Engineering (25) | 133 | 1 | 156 | 2 | ProfessionalService | 6 | none |
| `/privacy/` | 200 | Privacy Policy — JCS Engineering (32) | 106 | 1 | 385 | 2 | ProfessionalService | 6 | none |
| `/404.html` | 200* | Page not found — JCS Engineering (32) | 42 | 1 | 22 | 2 | ProfessionalService | 0 | noindex |

\* Served with 404 status by Cloudflare Pages for unknown routes; 200 when fetched directly. All canonicals are self-referencing absolute `https://jcseng.com/…/` URLs. Trailing-slash policy: directory URLs with trailing slash, enforced by Cloudflare Pages. `www` policy: **not yet enforced** (see Phase 5).

**Heading hierarchy:** every page has exactly one `<h1>` and no skipped levels (footer labels were converted from `<h4>` to non-heading text in the last QA pass).

**Duplicate / near-duplicate content:** none. Footer and header are intentionally identical across pages.

---

## Image inventory (before)

| File | Size | Dimensions | Format | Used | Alt | width/height attrs |
|---|---|---|---|---|---|---|
| `bioreactors-1200.webp` / `.jpg` | 106 / 160 KB | 1200×701 | WebP / JPEG | Home hero (`<picture>`, `fetchpriority=high`) | descriptive | yes |
| `bioreactors-800.webp` / `.jpg` | 57 / 80 KB | 800×467 | WebP / JPEG | Home hero srcset | descriptive | yes |
| `bioreactors.jpg` | 231 KB | 1233×720 | JPEG | **unreferenced — remove** | — | — |
| `drew-jones-400.webp` / `.jpg` | 17 / 28 KB | 400×400 | WebP / JPEG | About | descriptive | yes |
| `logo.svg` / `logo-inverse.svg` | 4 KB each | vector | SVG | Header / footer | "JCS Engineering" | yes |
| `og-card.png` | 51 KB | 1200×630 | PNG | og:image | — | — |
| `favicon.svg`, `favicon-32.png`, `favicon-16.png`, `apple-touch-icon.png` | 4 / 1 / <1 / 5 KB | — | — | icons | — | — |

Missing for PWA / rich results: 192×192 and 512×512 PNG icons, `site.webmanifest`. Hero image is above the 150 KB target only in its JPEG fallback (160 KB); the WebP that modern browsers actually load is 106 KB.

---

## Structured data (before)

One `ProfessionalService` object on every page with `name`, `legalName`, `url`, `logo`, `image`, `email`, `telephone`, `address` (locality/region/country only), `areaServed: "US"`, `description`, `knowsAbout`, `founder` (Person with two credentials), `hasCredential` (firm license). Home page adds `FAQPage` with 7 questions. Validates without errors, but:

- No `@id` on the organization, so nothing else can reference it
- No `sameAs` (LinkedIn, Google Business Profile)
- No `geo`, `openingHoursSpecification`, `priceRange`, `areaServed` as City/State entities
- No `hasOfferCatalog` → `Service` entities
- No `WebSite`, `WebPage`/`AboutPage`/`ContactPage`, `BreadcrumbList`, `Service`, `Article`
- `Person` exists only nested under `founder`; no standalone Person with `sameAs`

---

## Internal linking (before)

Every page receives 6 inbound links (header + footer), so there are no orphans and no page has < 2 inbound links. However, **all links are navigational**; there are zero contextual (in-body) links between pages, and the six services on `/capabilities/` are anchors, not pages, so they cannot accumulate link equity individually. No broken links; no redirect chains.

---

## Core Web Vitals (Lighthouse 12.6, before)

| Page | Form | Perf | A11y | BP | SEO | LCP | TBT | CLS | Weight |
|---|---|---|---|---|---|---|---|---|---|
| `/` | mobile | 99 | 100 | 100 | 100 | 2.10 s | 0 ms | 0.000 | 202 KB |
| `/` | desktop | 100 | 100 | 100 | 100 | 0.50 s | 0 ms | 0.000 | 202 KB |
| `/capabilities/` | mobile | 100 | 100 | 100 | 100 | 1.65 s | 0 ms | 0.000 | 137 KB |
| `/capabilities/` | desktop | 100 | 100 | 100 | 100 | 0.41 s | 0 ms | 0.000 | 137 KB |
| `/approach/` | mobile | 100 | 100 | 100 | 100 | 1.66 s | 0 ms | 0.000 | 135 KB |
| `/approach/` | desktop | 100 | 100 | 100 | 100 | 0.40 s | 0 ms | 0.000 | 135 KB |
| `/contact/` | mobile | 100 | 100 | 100 | 100 | 1.66 s | 0 ms | 0.000 | 135 KB |
| `/contact/` | desktop | 100 | 100 | 100 | 100 | 0.41 s | 0 ms | 0.000 | 140 KB |

Mobile scores are under simulated slow-4G throttling. Home LCP of 2.10 s is the hero photograph; it is preloaded via `fetchpriority="high"` and already WebP. Render-blocking resources: one 29 KB stylesheet. Unused CSS: negligible after the dead-rule sweep. No third-party scripts. The Google Maps iframe on `/contact/` is `loading="lazy"` and below the fold.

---

## Mobile usability

Viewport meta present. No horizontal overflow at 320–1440 px. Tap targets ≥ 24 px (footer links, contact list, arrow links padded in the last QA pass). Body text 16 px; smallest visible text is 11 px monospace labels (uppercase, high contrast, decorative captions — not body copy).

---

## Security & trust

- HTTPS enforced by Cloudflare (Pages projects are HTTPS-only); **HSTS not set** → add `Strict-Transport-Security` in `_headers`
- No mixed content (all assets same-origin; map iframe and Formspree over HTTPS)
- Present: `X-Content-Type-Options: nosniff`, `X-Frame-Options: SAMEORIGIN`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy`
- **Missing:** `Content-Security-Policy`, `Strict-Transport-Security`

---

## Crawl infrastructure

| Item | Status |
|---|---|
| `robots.txt` | Present; `Allow: /`; sitemap directive. No explicit AI-crawler allowances. |
| `sitemap.xml` | Present; 6 URLs; static `<lastmod>` (all the same date); no image entries |
| `404.html` | Present, branded, `noindex`, navigation; no search |
| Favicon set | SVG (dark-mode aware) + 32/16 PNG + 180 apple-touch-icon. No 192/512, no manifest |
| `humans.txt`, `llms.txt` | Absent |
| Analytics | None (privacy policy states none) |
| Search Console / Bing verification | None present in HTML; DNS status unknown |

---

## Local SEO signals

| Signal | Status |
|---|---|
| Business name | "JCS Engineering" (display) / "JCS Engineering PLLC" (legal, footer, schema) — consistent |
| Address | Locality only ("Raleigh, NC"). Owner brief mentions Knightdale, NC → **[VERIFY]** which to publish and whether to show a street address |
| Phone | (704) 500-3033, click-to-call, consistent on every page |
| Email | drew@jcseng.com, mailto, consistent |
| Hours | Not displayed → **[VERIFY]** against Google Business Profile |
| Map | Google Maps embed of the Raleigh area on `/contact/` |
| Service area | Not stated beyond Raleigh |
| Schema | `ProfessionalService` with locality; no `geo`, no `areaServed` entities, no `sameAs` to GBP/LinkedIn |
| Profiles | Google Business Profile and LinkedIn exist (per owner) but are not linked from the site |

---

## Competitor snapshot

The sandbox used for this audit cannot reach external websites (egress is restricted to package registries and GitHub), so competitor pages were **not crawled**. The owner named Jacobs, IPS, and Arcadis as aspirational references; those are global firms with thousands of pages and are not the realistic ranking competition for a Triangle-area consultancy on local and long-tail queries. The relevant competitive set for JCS is:

- Regional life-sciences engineering and CQV consultancies serving the NC biomanufacturing corridor (RTP/Durham, Holly Springs, Clayton, Sanford, Wilson)
- Owner's-representative and project-controls boutiques marketing to pharma/biotech owners
- Individual PE consultants with Google Business Profiles in Wake County

Known patterns from that segment (from general industry knowledge, to be confirmed by the owner in Search Console once data accrues): titles of the form "*Service* Consulting | *Firm*", dedicated pages per service (CQV, commissioning, validation, project management, owner's rep), a "Projects" or "Experience" page, a "Careers" page, and `Organization` schema; few have `Service` or `FAQPage` markup, few have location content, and almost none have `llms.txt` or explicit AI-crawler policies — those are the gaps this work exploits. **Action for owner:** list three to five firms that actually appear when you search your own target phrases, and add them to `SEO_KEYWORD_MAP.md` §Competitors.
