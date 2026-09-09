# SEO Results — before / after

**Branch:** `seo/technical-optimization` · **Baseline:** `cc38f49` (live `main`, 2026-09-08) · **Method:** Lighthouse 12.6 via headless Chromium against the built site on a local server; mobile = default slow-4G/Moto G emulation, desktop = `--preset=desktop`. Scores are single runs and vary ±1–2 points between runs.

## Lighthouse

| Page | Form | Perf before → after | A11y | Best Practices | SEO | LCP before → after | CLS | Weight before → after |
|---|---|---|---|---|---|---|---|---|
| `/` | mobile | 99 → 98 | 100 → 100 | 100 → 100 | 100 → 100 | 2.10 s → 2.25 s | 0.000 → 0.000 | 202 KB → 218 KB |
| `/` | desktop | 100 → 100 | 100 → 100 | 100 → 100 | 100 → 100 | 0.50 s → 0.49 s | 0.000 → 0.000 | 202 KB → 218 KB |
| `/capabilities/cqv/` (new) | mobile | — → 99 | — → 100 | — → 100 | — → 100 | — → 1.80 s | — → 0.000 | — → 155 KB |
| `/capabilities/cqv/` (new) | desktop | — → 100 | — → 100 | — → 100 | — → 100 | — → 0.44 s | — → 0.000 | — → 155 KB |
| `/capabilities/project-engineering/` (new) | mobile | — → 99 | — → 100 | — → 100 | — → 100 | — → 1.95 s | — → 0.000 | — → 156 KB |
| `/capabilities/project-engineering/` (new) | desktop | — → 100 | — → 100 | — → 100 | — → 100 | — → 0.45 s | — → 0.000 | — → 156 KB |
| `/capabilities/engineering-design/` (new) | mobile | — → 99 | — → 100 | — → 100 | — → 100 | — → 1.80 s | — → 0.000 | — → 156 KB |
| `/capabilities/engineering-design/` (new) | desktop | — → 100 | — → 100 | — → 100 | — → 100 | — → 0.44 s | — → 0.000 | — → 156 KB |

The baseline was already at the performance ceiling; the goal of this work was to keep it there while tripling the site's content. Home page weight grew 16 KB for the Insights cards, service-area paragraph, and richer structured data. All pages remain well under the 2.5 s LCP / 0.1 CLS targets on mobile.

## Site inventory

| Metric | Before | After |
|---|---|---|
| Indexable pages | 6 | 19 |
| Pages with ≥ 500 words | 1 (capabilities hub) | 12 (six services, three posts, FAQ, experience, service areas) |
| Service pages | 0 (one shared hub) | 6 |
| Blog / insights posts | 0 | 3 (890 / 934 / 912 words) + 12-post calendar |
| Pages with FAQ + FAQPage schema | 1 | 8 |
| Schema types | 2 (ProfessionalService, FAQPage) | 12 (ProfessionalService, Person, WebSite, WebPage, AboutPage, ContactPage, CollectionPage, FAQPage, Service, Article, BreadcrumbList, ItemList) with cross-referenced `@id`s |
| Contextual (in-body) internal links | 0 | 60+ (every service → 3 related services + 1 post + contact; every post → 2 services + contact + 2 posts) |
| Titles within 60 chars | 5 / 6 | 20 / 20 (enforced by build) |
| Descriptions within 140–160 chars | 1 / 6 | 20 / 20 (enforced by build) |
| `<meta name="robots">` | none | on every page |
| `lang` | `en` | `en-US` |
| Breadcrumbs (visible + schema) | none | every non-home page |
| Footer NAP block | name + phone + email | name, city, service-area line, phone, email (+ street, hours when set) |
| `robots.txt` AI crawlers | implicit | 13 named crawlers explicitly allowed |
| Sitemap | 6 URLs, static lastmod | 19 URLs, per-page lastmod, image entries |
| `llms.txt` / `humans.txt` / manifest / 192–512 icons | none | all present |
| Security headers | 4 | 7 incl. HSTS (preload) and a strict CSP (tested: zero violations on 20 pages, form works) |
| CI regression guard | none | html-validate + build-freshness check + lychee link check + Lighthouse CI budgets on every PR |
| Search-engine notification | none | IndexNow key + post-deploy submission workflow |
| Dead assets | 231 KB | 0 |

## Verification performed on the built site (all 20 pages × 1440 / 1024 / 768 / 390 px)

- Horizontal overflow: none · Console/JS errors: none · Broken internal links or anchors: none
- axe-core (WCAG 2.1 AA + best practice), desktop and mobile: 0 violations
- html-validate (recommended ruleset): 0 errors
- JSON-LD: every block parses; every `@id` reference resolves to a node in the same page graph or to a service page that exists
- Content-Security-Policy applied to every local response: 0 violations; contact form completes
- Contact form: native validation, success state, failure state — all pass
- Every referenced `/assets/...` file exists

## Search baseline (owner survey, 2026-09-08)

Fourteen target phrases searched from Raleigh/Knightdale in a private window: JCS appeared for **0 of 14** (site indexed only under the stale "Jones Consultants" title). Competitor detail and the resulting changes are in `SEO_KEYWORD_MAP.md` §Competitors. Re-run the same fourteen searches at 30, 60, and 90 days and record position (Places pack / AI Overview / page 1 / not shown) here.

## Not done, and why

- **Competitor crawl** — sandbox has no external web access; see `SEO_KEYWORD_MAP.md` §Competitors for the owner to fill in.
- **Google Rich Results Test / Schema.org validator** — external services; the JSON-LD was validated structurally here and should be pasted into https://validator.schema.org/ once deployed (expected: no errors; FAQPage rich results are limited by Google policy to authoritative sites but the markup still aids entity understanding).
- **Per-city location pages** — deliberately one `/service-areas/` page instead of ten near-duplicate city pages (doorway-page risk; no genuinely distinct content per suburb for a B2B pharma consultancy).
- **GA4** — not added; the privacy policy states no analytics cookies. Cloudflare Web Analytics (cookieless) is pre-allowed in the CSP if the owner wants measurement.
- **www → non-www redirect and HSTS preload submission** — require Cloudflare dashboard access; steps in `SEO_OWNER_CHECKLIST.md` §4.
- **Search Console / Bing verification, GBP, LinkedIn, citations, outreach** — require owner logins; fully scripted in `SEO_OWNER_CHECKLIST.md`.

## 90-day maintenance plan

**Weekly (15 min):** Search Console → Performance: note new queries and pages gaining impressions; Pages report: fix anything "Crawled – not indexed"; reply to any Google review; publish the week's Google Business Profile post and two LinkedIn posts from the calendars.

**Monthly (2–3 h):** publish one Insights post from `SEO_CONTENT_CALENDAR.md` (update `siteconfig.POSTS`, add the body to `posts.py`, run the build); share it on LinkedIn and GBP; add one new GBP photo; complete five directory listings from §6 of the checklist; send two partner-link asks from §7.

**Quarterly (half a day):** re-run `python3 tools/build.py` and the CI checks; re-run Lighthouse on home + top three service pages and append to this file; review titles/descriptions against Search Console CTR and rewrite the two lowest; refresh the oldest post's `dateModified` with a genuine update; check every citation for NAP drift; archive the site (`archive/vX.Y.Z-…` branch + release) before any redesign.

**Expectations:** first impressions in Search Console within 2–4 weeks of indexing; measurable movement on long-tail service + location queries at 6–10 weeks; competitive positions for the primary keywords in `SEO_KEYWORD_MAP.md` at 3–6 months of consistent execution. Organic results compound; the content and off-site work in the checklist matter more than any further technical change.
