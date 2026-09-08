# SEO Owner Checklist — jcseng.com

Everything here requires a login the site cannot hold (Google, Bing, LinkedIn, Cloudflare, directories). All of it is free. Work top to bottom; the first two sections matter most. Where text is marked **copy**, paste it verbatim — it is written to match the website exactly, which is what search engines check.

**The one rule:** name, address, phone, and website must be *identical* everywhere — site, Google Business Profile, Bing, LinkedIn, every directory. Use exactly:

| Field | Value |
|---|---|
| Business name | `JCS Engineering PLLC` |
| Short name (where a display name is allowed) | `JCS Engineering` |
| Phone | `(704) 500-3033` |
| Website | `https://jcseng.com/` |
| Email | `drew@jcseng.com` |
| Address | `5540 Centerview Dr, Ste 200-210, Raleigh, NC 27606` |
| Category wording | `Engineering consultant` |

---

## 0. Fill the site's open fields first (5 minutes)

Open `tools/siteconfig.py` and set the `None` values, then run `python3 tools/build.py` and commit (or send the values to Claude):

- ~~`ADDRESS`~~ set (5540 Centerview Dr, Ste 200-210, Raleigh, NC 27606)
- `GEO` — latitude/longitude of the office: in Google Maps right-click the building at 5540 Centerview Dr → click the coordinates line to copy → send to Claude
- `HOURS` — set **after** fixing the profile hours (see §1); "Open 24 hours" must not be copied to the site
- ~~`PROFILES.linkedin_company`, `PROFILES.google_business`~~ set · `PROFILES.linkedin_person` — still needed
- ~~`FOUNDING_YEAR`~~ intentionally left unset (owner preference)
- `GOOGLE_SITE_VERIFICATION`, `BING_SITE_VERIFICATION` (from §3 below)

Until these are set the site omits those fields rather than publishing placeholders.

---

## 1. Google Business Profile (highest impact — do this week)

Go to https://business.google.com → your profile → **Edit profile**.

> **Fix these four things first — they were visible on the profile on 2026-09-08:**
> 1. **The map pin is in the Chesapeake Bay.** The profile's coordinates are 38.71, −75.88 (off Maryland's Eastern Shore), not Raleigh. Until this is fixed the business cannot appear in any Raleigh-area local search. *Edit profile → Location → Business location → enter `5540 Centerview Dr Ste 200-210, Raleigh, NC 27606` → drag the pin onto the building → Save.* Google may ask to re-verify by postcard or video; do it.
> 2. **Hours show "Open 24 hours."** Consultancies that claim 24-hour service look automated to Google and to prospects. Set real hours (e.g. Mon–Fri 8:00–5:00) and then copy them into `HOURS` in `tools/siteconfig.py`.
> 3. **Primary category is "Design engineer."** Change it to **Engineering consultant** and add "Design engineer" as a secondary category (see list below) — "Engineering consultant" is what buyers search and is the category the site's schema aligns to.
> 4. **The description differs from the website.** Replace it with the 736-character description below so every source describes the business identically.

**Business name:** `JCS Engineering PLLC`

**Primary category:** `Engineering consultant`
**Secondary categories** (add all that appear): `Consulting engineer` · `Mechanical engineer` · `Engineer` · `Project management consultant` · `Business to business service`

**Description (736 characters — copy):**
> JCS Engineering PLLC is a licensed North Carolina engineering firm (Firm License P-3451) providing project engineering, conceptual and detailed design, construction oversight, commissioning/qualification/validation (CQV), change and risk management, and tech transfer for pharmaceutical, biotech, and advanced manufacturing facilities. Led by Drew Jones, PE, a chemical engineer with hands-on experience on the owner's side of cGMP capital projects — from process design through IQ/OQ and handover — we act as the owner's representative and scale from a single embedded engineer to a full project team. Based in the Raleigh area, serving the Research Triangle and North Carolina's biomanufacturing corridor on-site, remotely, or hybrid.

**Services** (Edit profile → Services → add each; use these descriptions):

| Service | Description (copy) |
|---|---|
| Project Engineering & Owner's Representation | Owner-side project engineering and management for pharma and biotech capital projects — scope, budget, schedule, and quality from kickoff to closeout. |
| Conceptual & Detailed Design | Process and mechanical design: URS, basis of design, PFDs and P&IDs, calculations, equipment specifications, and construction-ready packages. |
| Construction Administration & Oversight | Submittal and RFI management, field verification, change order review, and turnover for cGMP facilities, sequenced around live production. |
| Commissioning, Qualification & Validation (CQV) | C&Q planning, impact assessments, FAT/SAT, IQ/OQ/PQ protocols and execution, traceability, and turnover packages. |
| Change, Risk & Compliance Management | Project change control, risk registers, document control, design qualification, and inspection readiness. |
| Process Optimization & Tech Transfer | Facility fit-gap assessments, scale-up engineering, equipment and utility modifications, startup and stabilization support. |

**Service areas** (Edit profile → Location and areas → Service area): Raleigh, Durham, Cary, Holly Springs, Clayton, Knightdale, Wendell, Zebulon, Garner, Apex, Wake Forest, Morrisville, Chapel Hill, Sanford, Wilson, Greenville, Research Triangle Park, Wake County, Johnston County, Durham County. (Google allows up to 20.)

**Hours:** set your real hours **[VERIFY]**, then copy them into `HOURS` in `tools/siteconfig.py`.

**Attributes:** Identifies as veteran-owned / etc. only if true. Under "From the business" add `Online appointments` if you take video calls; `Onsite services: Yes`.

**Website / appointment link:** `https://jcseng.com/` and `https://jcseng.com/contact/`.

**Photos — upload plan** (Google favours profiles with 10+ photos; all must be yours):
1. Logo: `assets/img/logo.svg` exported as 720×720 PNG on white (ask Claude for the file)
2. Cover: `assets/img/og-card.png` (1200×630)
3. Headshot: `assets/img/drew-jones-400.jpg` (better: a 1000 px+ original)
4–13. Real photos you have rights to: you on site in PPE, a P&ID on screen, a skid or utility plant you worked on (no client names or proprietary detail visible), your home office/work setup, a marked-up drawing, a FAT in progress, the Raleigh skyline from a jobsite. Add one new photo per month.

**Google Posts — 8-week calendar** (Add update → post; 150–300 words; end each with the link):

| Week | Type | Post (copy, then adjust) | Link |
|---|---|---|---|
| 1 | Update | JCS Engineering PLLC is a licensed NC engineering firm (P-3451) for pharma and biotech capital projects: project engineering, design, CQV, and owner's representation across the Research Triangle. Here's what we do. | /capabilities/ |
| 2 | Update | What does an owner's engineer actually do on a pharma project — and how is it different from the CM or the A/E? New article. | /insights/owners-engineer-pharmaceutical-capital-project/ |
| 3 | Update | CQV usually gets blamed for late startups. Most of the delay was decided during design. Five design-phase decisions that keep qualification off the critical path. | /insights/cqv-planning-starts-in-design/ |
| 4 | Offer (no discount needed) | Free 30-minute scoping call for pharma/biotech owners with a capital project in concept or design. We'll tell you where the risk is — and if we're not the right fit. | /contact/ |
| 5 | Update | Moving a process to a new site? The seven gap categories we assess before anything moves, and the surprises that usually turn up. | /insights/facility-fit-gap-assessment-tech-transfer/ |
| 6 | Update | Commissioning vs. qualification: what each one proves, and why good commissioning makes IQ/OQ faster. From our CQV FAQ. | /capabilities/cqv/ |
| 7 | Update | Serving NC's biomanufacturing corridor — Raleigh, Durham/RTP, Holly Springs, Clayton, Sanford, Wilson — on-site, remote, or hybrid. | /service-areas/ |
| 8 | Update | Six phases, five gates, one accountable engineer. How we structure a capital project so leadership sees a decision at every transition, not a surprise at the end. | /approach/ |

**Q&A seeding** (on your public profile, ask each question from your personal Google account, then answer from the business — this is allowed and expected):

1. *Q: What types of projects does JCS Engineering handle?* — A: Capital projects in pharmaceutical, biotech, and advanced manufacturing: new lines and suites, facility expansions, equipment installations, tech transfers, and CQV programs — from concept through qualified handover.
2. *Q: Is JCS Engineering a licensed engineering firm?* — A: Yes. North Carolina Engineering Firm License P-3451; our principal, Drew Jones, is a NC Professional Engineer (No. 062483).
3. *Q: Do you work on-site?* — A: Yes — on-site, remote, or hybrid depending on the phase. Construction and CQV usually warrant field presence across the Research Triangle and NC's biomanufacturing corridor.
4. *Q: Can you act as an owner's representative?* — A: Yes. Owner's representation is a core service: one point of contact across the design firm, contractors, vendors, and quality organization, answering only to the owner.
5. *Q: How do we start?* — A: A short scoping call about where the project stands. Call (704) 500-3033 or use https://jcseng.com/contact/ — we reply within one business day.

**Reviews.** Your direct review link: in the profile dashboard click **Ask for reviews** and copy the short link (format `https://g.page/r/XXXXXXXX/review`). Ask after every completed engagement or milestone:

> Subject: Quick favour — a Google review for JCS Engineering
>
> Hi [Name] — thanks again for the work on [project/phase]. If you have two minutes, a short Google review would help other owners find us: [review link]. A sentence or two about what we did and how it went is perfect. No pressure at all, and thank you either way. — Drew

Reply to every review within a week. Never offer anything in exchange for a review.

---

## 2. Bing Places and Apple Business Connect (20 minutes total)

- **Bing Places:** https://www.bingplaces.com → **Import from Google Business Profile**. Confirm name/phone/website match the table above. Bing powers DuckDuckGo local results and Copilot.
- **Apple Business Connect:** https://businessconnect.apple.com → Add business → verify → same NAP, same description, same categories (`Engineering Service`). Powers Apple Maps and Siri.

---

## 3. Google Search Console and Bing Webmaster Tools (30 minutes; do before merging the PR if possible)

**Google Search Console** — https://search.google.com/search-console
1. Add property → **Domain** → `jcseng.com` → verify by DNS TXT record (Cloudflare → DNS → add the TXT Google gives you). This covers www and non-www in one property. *Alternative:* URL-prefix property → HTML tag → copy the `content` value into `GOOGLE_SITE_VERIFICATION` in `tools/siteconfig.py`, rebuild, deploy, click Verify.
2. **Sitemaps** → add `https://jcseng.com/sitemap.xml`.
3. **URL Inspection** → paste each of these and click **Request indexing**: `/`, `/capabilities/`, all six `/capabilities/<slug>/`, `/approach/`, `/service-areas/`, `/experience/`, `/insights/`, the three posts, `/about/`, `/contact/`, `/faq/`.
4. Settings → **Users and permissions** → make sure email alerts are on.
5. After 2–3 weeks: **Performance** report shows the queries you appear for; **Pages** report shows anything not indexed.

**Bing Webmaster Tools** — https://www.bing.com/webmasters
1. **Import from Google Search Console** (one click), or add site → verify via meta tag → copy the value into `BING_SITE_VERIFICATION`.
2. Submit `https://jcseng.com/sitemap.xml`.
3. **IndexNow** is already wired: the site serves the key at `/9f3a6c2e8d4b4f1a9c7e5b2d8a6f4c3e.txt` and a GitHub Action submits every URL to `api.indexnow.org` after each deploy to `main`. Bing will show received submissions under IndexNow → Insights.

---

## 4. Cloudflare settings (15 minutes; zero cost)

In the Cloudflare dashboard for the `jcseng.com` zone:
- **SSL/TLS → Edge Certificates:** turn on **Always Use HTTPS** and **HSTS** (the site already sends the HSTS header; enabling it here too is belt-and-braces) — set max-age 12 months, include subdomains.
- **Workers & Pages → the project → Custom domains:** ensure both `jcseng.com` and `www.jcseng.com` are attached.
- **Rules → Redirect Rules → Create rule:** *When* hostname equals `www.jcseng.com` → *Then* dynamic redirect to `concat("https://jcseng.com", http.request.uri.path)`, status **301**, preserve query string. This enforces the non-www canonical the site declares.
- **Caching → Configuration → Purge Everything** once after the PR merges.
- **Web Analytics (owner asked for this — free, cookieless, no code):** Workers & Pages → the Pages project → **Settings → Web Analytics → Enable**. Cloudflare injects its beacon automatically on every page; the site's Content-Security-Policy already allows it and the privacy policy already describes it. Reports appear under Analytics & Logs → Web Analytics within a day. Do not add GA4.

---

## 5. LinkedIn (1 hour to set up; 30 minutes per week)

**Company page** (https://www.linkedin.com/company/… → Edit page):
- **Tagline (copy):** `Project engineering, design & CQV for pharmaceutical and biotech capital projects | Licensed NC engineering firm | Raleigh–Durham`
- **Website:** `https://jcseng.com/` · **Industry:** Engineering Services · **Company size:** 1–10 (or actual) · **Type:** Privately held · **Headquarters:** Raleigh, North Carolina **[VERIFY]**
- **Specialties (copy):** Owner's Representation, Project Engineering, Capital Project Management, Process Design, P&ID Development, Commissioning Qualification Validation, CQV, Tech Transfer, cGMP Facilities, Pharmaceutical Engineering, Biotech Engineering, Construction Oversight, ISPE, ASTM E2500
- **About (copy):** paste the Google Business Profile description above, then add: `Learn more: https://jcseng.com/capabilities/`
- **Custom button:** Contact us → `https://jcseng.com/contact/`

**Personal profile (Drew):**
- **Headline (copy):** `Founder & Principal Engineer, JCS Engineering PLLC | PE | Owner's Engineer for Pharma & Biotech Capital Projects | Design · Construction · CQV | Raleigh, NC`
- **About (copy):** first two paragraphs of the bio on https://jcseng.com/about/, then: `JCS Engineering PLLC is a licensed North Carolina engineering firm. If you have a capital project in concept, design, construction, or startup, the fastest way to find out whether we can help is a short technical conversation: https://jcseng.com/contact/`
- **Featured:** add the three Insights posts and the Capabilities page as links.
- **Experience → add JCS Engineering PLLC** as current position linked to the company page.

**30-day posting plan (2 posts/week, alternate personal and company page; every post links to the site):**

| Day | Post | Link |
|---|---|---|
| 1 | Announce: JCS Engineering PLLC — what the firm does, who it serves, the firm license. | /about/ |
| 4 | "Every party on a capital project has a contract to protect. Except one." Excerpt of the owner's engineer article. | /insights/owners-engineer-pharmaceutical-capital-project/ |
| 8 | One-image post: the six-phase stage-gate model (screenshot the Approach page or ask Claude for a graphic). | /approach/ |
| 11 | "Qualification gets blamed for late startups. It was decided in design." Five decisions, one per line. | /insights/cqv-planning-starts-in-design/ |
| 15 | Poll: "Where does your capital project usually slip? Design / Procurement / Construction / CQV." Follow with a comment linking to CQV page. | /capabilities/cqv/ |
| 18 | Facility fit-gap: the seven categories as a carousel or list. | /insights/facility-fit-gap-assessment-tech-transfer/ |
| 22 | Representative experience: the $25M spray-drying conversion, told as lessons (no client names). | /experience/ |
| 25 | "URS vs basis of design — who writes what." Short explainer (also a future blog post). | /capabilities/engineering-design/ |
| 29 | Serving NC's biomanufacturing corridor — Holly Springs, Clayton, RTP — and what's being built there. | /service-areas/ |

Engage with posts from ISPE Carolina–South Atlantic Chapter, NC Biotechnology Center, NCBIO, and local GC/A/E firms — comments from a PE with substance get noticed.

---

## 6. Free citations and directories (consistent NAP; ~3 hours total, spread over a month)

Priority order. Use the exact NAP table at the top. Where a description is requested, use the GBP description.

**Licensing and professional (do first — these are trust signals search engines weight heavily)**
1. NC Board of Examiners for Engineers and Surveyors — verify the firm (P-3451) and individual (062483) records are accurate at https://www.ncbels.org/ (licensee search). Fix any address discrepancy.
2. NSPE / PENC (Professional Engineers of North Carolina) member directory — if a member
3. ISPE member directory (https://ispe.org) — Carolina–South Atlantic Chapter
4. AIChE member directory
5. NC State University Alumni Association / COE alumni directory
6. ACEC North Carolina member directory (if joining; membership has a fee, listing is part of it — optional)

**General business (free tiers)**
7. Bing Places (§2) · 8. Apple Business Connect (§2) · 9. Yelp for Business · 10. Better Business Bureau free profile (bbb.org/get-listed) · 11. Yellow Pages (yp.com) · 12. Manta · 13. Nextdoor Business · 14. Alignable · 15. MapQuest / Foursquare (via Foursquare for Business) · 16. Hotfrog · 17. Cylex · 18. Chamber of Commerce (Raleigh Chamber or Knightdale Chamber — membership fee; skip if not a member) · 19. Crunchbase (free company profile) · 20. Clutch.co (free listing) · 21. GoodFirms

**Industry and construction**
22. Procore Network (free contractor/consultant profile) · 23. BuildZoom · 24. The Blue Book Building & Construction Network (free basic) · 25. ConstructConnect / Dodge (free company profile) · 26. PharmaSource / BioProcess International supplier directory (free tier) · 27. ThomasNet (free supplier listing)

**Government vendor registries (free; needed to be found by public-sector and university buyers)**
28. SAM.gov (UEI) · 29. NC eVP (NC Electronic Vendor Portal) · 30. NC HUB Office (if eligible) · 31. Wake County vendor registration

Keep a spreadsheet: directory, URL of your listing, date, login. Check quarterly that nothing has drifted.

---

## 7. Earned links (free) — 15 targets and templates

Links from relevant sites are the strongest ranking signal you can earn without paying. Each target below is a realistic, no-cost ask.

| # | Target | Ask |
|---|---|---|
| 1–4 | Four GCs / CMs you have worked alongside in pharma construction | Be listed on their "Partners" or "Consultants we work with" page; offer a reciprocal listing on a future JCS partners page |
| 5–6 | Two A/E firms you have coordinated with | Same as above |
| 7 | ISPE Carolina–South Atlantic Chapter | Volunteer to present a chapter talk ("CQV planning starts in design"); chapters link speakers' firms |
| 8 | NC State Chemical & Biomolecular Engineering department | Alumni spotlight / "where our alumni are" page; offer to speak to the senior design class |
| 9 | NC Biotechnology Center | Add JCS to the NC life-science company directory (free) |
| 10 | Triangle Business Journal — People on the Move | Free submission: "Drew Jones, PE, founds JCS Engineering PLLC" |
| 11 | Wake County / Raleigh economic development | New business announcement; some maintain company directories |
| 12 | Pharmaceutical Engineering (ISPE magazine) / Pharmaceutical Processing World | Pitch a guest article based on an Insights post |
| 13 | BioProcess International / Bioprocess Online | Same — guest article or expert commentary |
| 14 | Connectively (ex-HARO) / Qwoted / Featured.com | Free source-request platforms; answer journalist queries on pharma manufacturing, CQV, capital projects |
| 15 | Vendors whose equipment you have specified or qualified | "Consultants familiar with our equipment" listings, or a joint case note |

**Template — partner listing (copy):**
> Subject: Adding JCS Engineering to your consultants/partners page
>
> Hi [Name] — I've started JCS Engineering PLLC, a licensed NC engineering firm doing owner-side project engineering, design, and CQV for pharma and biotech projects. We've worked together on [project/site], and I'd like to keep doing so. Would you add us to your [partners/consultants] page (https://jcseng.com/)? Happy to list [Firm] on ours in return. Thanks — Drew Jones, PE · (704) 500-3033

**Template — guest article pitch (copy):**
> Subject: Guest article: [title]
>
> Hi [Editor] — I'm a PE who has spent his career on the owner's side of pharma capital projects, most recently leading CQV on a large biologics site startup in Holly Springs, NC. I'd like to offer your readers a practical piece: "[title]" — [one-sentence premise]. Roughly 1,000 words, no promotion beyond a byline. A draft on a related topic is here for style: https://jcseng.com/insights/cqv-planning-starts-in-design/. Would that fit? — Drew Jones, PE, JCS Engineering PLLC

---

## 8. AI search visibility — what is done and what to keep consistent

Done in the site: `/about/` with structured entity facts (who, what, where, licenses), `/llms.txt` at the root summarising the business and linking every key page, `robots.txt` explicitly allowing GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Claude-SearchBot, Google-Extended, Applebot-Extended and others, `Organization`/`Person`/`Service`/`Article` JSON-LD with cross-referenced `@id`s, and FAQ blocks that answer questions in full sentences.

What only you can do: use the **same** name, description, and category wording on every profile (§1, §2, §5, §6). AI engines triangulate entities across sources; inconsistency is the most common reason a small firm is invisible to them.

---

## 9. After the PR merges

1. Cloudflare → Purge Everything; hard-refresh the site.
2. Search Console → request indexing on the URLs in §3.
3. Confirm https://jcseng.com/llms.txt, /robots.txt, /sitemap.xml, /site.webmanifest, and /9f3a6c2e8d4b4f1a9c7e5b2d8a6f4c3e.txt all load.
4. Check the GitHub Actions tab: **SEO & quality check** green on the merge commit; **Notify search engines (IndexNow)** shows a 200/202 response.
5. Start the GBP post calendar (§1) and the LinkedIn plan (§5) the same week.

Expect the first measurable movement in Search Console impressions at 4–8 weeks and meaningful ranking gains at 3–6 months of consistent execution. The 90-day maintenance plan is in `SEO_RESULTS.md`.
