# SEO Action Plan — step-by-step, in priority order

Written 2026-09-09 for JCS Engineering PLLC. Items 1–4 today (~45 min). 5–8 this week. 9–13 this month. 14–16 ongoing.
Use these exact values everywhere: **JCS Engineering PLLC · 5540 Centerview Dr, Ste 200-210, Raleigh, NC 27606 · (704) 500-3033 · https://jcseng.com/ · drew@jcseng.com · Category: Engineering consultant.**

---

## 1. Get two or three Google reviews (15 min) — highest value on the list

**Why:** the Raleigh map pack for "pharmaceutical engineering consultant Raleigh NC" contains firms with two and zero reviews. Reviews decide order inside that list.

1. Go to https://business.google.com and open your profile.
2. Click **Ask for reviews** (sometimes under **Get more reviews**). Copy the short link it shows (looks like `https://g.page/r/…/review`).
3. List three people you have completed real work with or alongside — a client-side manager, a contractor PM, a quality lead. Not family, not employees.
4. Send each this message (email or text):
   > Hi [Name] — thanks again for the work on [project/phase]. If you have two minutes, a short Google review would help other owners find us: [link]. A sentence or two about what we did and how it went is perfect. No pressure, and thank you either way. — Drew
5. When a review lands, reply to it within a week (Business Profile → Reviews → Reply). Never offer anything in exchange for a review.

---

## 2. Google Search Console (15 min) — tells Google the site exists

1. Go to https://search.google.com/search-console and sign in with the Google account that owns the Business Profile.
2. Click the property dropdown (top-left) → **Add property**.
3. Choose the **left** box, **Domain**. Type `jcseng.com` → **Continue**.
4. Google shows a TXT record: `google-site-verification=…`. Click **Copy**.
5. New tab → Cloudflare → **Domains → Overview → jcseng.com → DNS → Records → Add record**. Type `TXT` · Name `@` · Content: paste · **Save**.
6. Back in Search Console → **Verify**. If it fails, wait five minutes and try again.
7. Left menu → **Sitemaps** → type `sitemap.xml` → **Submit**.
8. Top search bar → paste each URL below → Enter → **Request indexing** (30 seconds each):
   - `https://jcseng.com/`
   - `https://jcseng.com/capabilities/project-engineering/`
   - `https://jcseng.com/capabilities/engineering-design/`
   - `https://jcseng.com/capabilities/construction-oversight/`
   - `https://jcseng.com/capabilities/cqv/`
   - `https://jcseng.com/capabilities/change-risk-compliance/`
   - `https://jcseng.com/capabilities/optimization-tech-transfer/`
   - `https://jcseng.com/service-areas/holly-springs/`
   - `https://jcseng.com/service-areas/clayton/`
   - `https://jcseng.com/service-areas/durham-rtp/`
9. Left menu → **Settings → Users and permissions** → confirm your email is Owner (alerts go there).
10. Tell Claude **"verified."**

**Checking progress later:** search Google for `site:jcseng.com` — the number of results is how many pages Google has indexed (target 21). **Performance** report (after 2–3 weeks) shows the phrases people found you with.

---

## 3. Fix www and force HTTPS (10 min)

**3a. DNS record**
1. Cloudflare → **Domains → Overview → jcseng.com → DNS → Records**.
2. Find a row named `www`. If it exists with a grey cloud, **Edit** → Proxy status **Proxied** → Save. If it doesn't exist: **Add record** → Type `CNAME` · Name `www` · Target `jcseng.com` · Proxy status **Proxied** (orange) · **Save**.

**3b. Redirect rule**
1. Same domain → **Rules** → **Overview** → **Create rule** → **Redirect Rule**.
2. Name: `www to non-www`.
3. **Custom filter expression** → Field `Hostname` · Operator `equals` · Value `www.jcseng.com`.
4. **Then:** Type `Dynamic` · Expression `concat("https://jcseng.com", http.request.uri.path)` · Status `301` · tick **Preserve query string** → **Deploy**.
   *(If you already deployed the wildcard version — `https://www.jcseng.com/*` → `https://jcseng.com/${1}` — that works too; keep one, not both.)*

**3c. Always Use HTTPS**
1. Same domain → **SSL/TLS → Edge Certificates**.
2. Toggle **Always Use HTTPS** on.
3. **Enable HSTS** → tick the acknowledgement → Max Age **12 months** → **Include subdomains** on → Save.

**Test** (private window): `http://www.jcseng.com/about/`, `https://www.jcseng.com/about/`, `http://jcseng.com/about/` — all three must end at `https://jcseng.com/about/`.

---

## 4. Business Profile: attributes and status (10 min)

1. https://business.google.com → your profile → **Edit profile**.
2. Look for any banner saying *pending*, *needs verification*, or *suspended* (the address move can trigger this). If present, follow it — video or postcard verification — before anything else.
3. **About → From the business** (or **Attributes**): turn on **Online appointments** and **Onsite services**. Leave anything untrue off.
4. **Contact → Website:** `https://jcseng.com/`. **Appointment link:** `https://jcseng.com/contact/`.
5. Confirm still correct after the fixes you made: primary category *Engineering consultant*; hours Mon–Fri 6:00 AM–5:00 PM; the 736-character description from `SEO_OWNER_CHECKLIST.md` §1; pin on 5540 Centerview Dr.

---

## 5. Redirect the old domain jones-consultants.com (10 min)

1. Cloudflare → **Domains → Overview → jones-consultants.com**.
2. **DNS → Records.** You need a *proxied* (orange) record for the root and www so Cloudflare answers for the domain:
   - If rows for `@` (shown as `jones-consultants.com`) and `www` exist with orange clouds: skip to step 3.
   - Otherwise: **Add record** → Type `A` · Name `@` · IPv4 `192.0.2.1` · **Proxied** → Save. Repeat with Name `www`. (The IP is a placeholder; the rule below answers first.)
3. **Rules → Overview → Create rule → Redirect Rule.** Name: `Move to jcseng.com`.
4. **All incoming requests.**
5. **Then:** Type `Dynamic` · Expression `concat("https://jcseng.com", http.request.uri.path)` · `301` · **Preserve query string** → **Deploy**.
6. **SSL/TLS → Edge Certificates → Always Use HTTPS** on for this domain too.
7. **Build → Compute → the Pages project → Custom domains:** if `jones-consultants.com` is listed, **⋯ → Remove**.
8. Test: `jones-consultants.com` → lands on `jcseng.com`. `jones-consultants.com/anything` → lands on `jcseng.com/anything` (your 404 page — correct).

---

## 6. Search Console "Change of address" (10 min, after 2 and 5)

1. Search Console → property dropdown → **Add property → Domain → `jones-consultants.com`** → copy the TXT record.
2. Cloudflare → **jones-consultants.com → DNS → Add record → TXT · `@` · paste → Save**.
3. Search Console → **Verify**.
4. With the **jones-consultants.com** property selected → **Settings** (bottom of left menu) → **Change of address** → choose `jcseng.com` → **Validate & Update**. Google confirms the 301 and migrates the old domain's signals over a few weeks.

---

## 7. Cloudflare hygiene (10 min)

1. **jcseng.com → Security** (or **Application security**) → **Bots**. Make sure no setting blocks or challenges verified bots. If **Block AI bots** or **AI Labyrinth** is on, turn it **off**.
2. **jcseng.com → AI Crawl Control:** set to **Allow**. (The site's `robots.txt` and `llms.txt` exist so AI engines can cite you; blocking here cancels that.)
3. **jcseng.com → Caching → Configuration → Purge Everything → Purge.** Repeat any time Claude pushes an update and something looks stale.
4. Web Analytics — already running. View it under **Analytics & Logs → Web Analytics**.

---

## 8. Bing Webmaster Tools (3 min, after 2)

1. https://www.bing.com/webmasters → sign in (Microsoft or Google account).
2. **Import from Google Search Console** → authorize → select `jcseng.com` → **Import**.
3. Later, **IndexNow → Insights** (left menu) shows the automatic submissions the site sends after each deploy.

---

## 9. Finish the Business Profile (45 min over the week)

**Photos** (Business Profile → **Photos → Add**):
1. Logo: ask Claude for a 720×720 PNG export of `logo.svg`.
2. Cover: `assets/img/og-card.png` from the repo (1200×630).
3. Headshot: your photo (a larger original than 400 px if you have one).
4. Seven to ten real photos you have rights to: you on site in PPE, a P&ID on screen, a skid or utility plant (no client names visible), a marked-up drawing, a FAT in progress, the office. One new photo per month after.

**Q&A** (on the public listing, not the dashboard): from your *personal* Google account, click **Ask a question** and post each of the five questions in `SEO_OWNER_CHECKLIST.md` §1; then, from the business, answer each with the text provided.

**Posts:** Business Profile → **Add update** → paste week 1 from the 8-week calendar in §1 → add the link → Post. One per week thereafter.

**Benchmark:** spend twenty minutes on Sequence Inc's Business Profile and website (search "Sequence Inc Morrisville"). They appear in five of your fourteen searches. Note what their profile and service pages contain that yours don't yet.

---

## 10. Bing Places and Apple Business Connect (20 min)

1. https://www.bingplaces.com → **Import from Google Business Profile** → sign in → confirm the imported name, address, phone, website match exactly.
2. https://businessconnect.apple.com → **Get started** → add business → verify (phone or document) → Name `JCS Engineering PLLC` · category `Engineering Service` · same address, phone, hours, website · About = the 736-char description.

---

## 11. LinkedIn (1 hour setup, then 30 min/week)

**Company page** (https://www.linkedin.com/company/jcseng/ → **Edit page**):
1. **Tagline:** `Project engineering, design & CQV for pharmaceutical and biotech capital projects | Licensed NC engineering firm | Raleigh–Durham`
2. **Website:** `https://jcseng.com/` · **Industry:** Engineering Services · **Company size:** 1–10 · **Type:** Privately held · **HQ:** Raleigh, North Carolina.
3. **Specialties:** Owner's Representation, Project Engineering, Capital Project Management, Process Design, P&ID Development, Commissioning Qualification Validation, CQV, Tech Transfer, cGMP Facilities, Pharmaceutical Engineering, Biotech Engineering, Construction Oversight, ISPE, ASTM E2500.
4. **About:** paste the 736-char description, then `Learn more: https://jcseng.com/capabilities/`.
5. **Custom button:** Contact us → `https://jcseng.com/contact/`.

**Personal profile** (https://www.linkedin.com/in/drewjones2):
6. **Headline:** `Founder & Principal Engineer, JCS Engineering PLLC | PE | Owner's Engineer for Pharma & Biotech Capital Projects | Design · Construction · CQV | Raleigh, NC`
7. **About:** first two paragraphs from https://jcseng.com/about/ then `JCS Engineering PLLC is a licensed North Carolina engineering firm. If you have a capital project in concept, design, construction, or startup: https://jcseng.com/contact/`
8. **Experience:** add JCS Engineering PLLC as current position, linked to the company page.
9. **Featured:** add the three Insights articles and the Capabilities page.

**Posting:** two per week from the 30-day plan in `SEO_OWNER_CHECKLIST.md` §5; alternate personal and company page; every post links to a site page.

---

## 12. Licensing and professional listings (1 hour)

1. https://www.ncbels.org/ → licensee search → check the **firm** record (P-3451) and your **PE** record (062483) show 5540 Centerview Dr. If not, file the address update with the Board.
2. ISPE: https://ispe.org → member directory → ensure your profile lists JCS Engineering PLLC and the website; join the Carolina–South Atlantic chapter mailing list.
3. AIChE member directory: same.
4. NC State Alumni Association directory: add employer and website.
5. PENC (Professional Engineers of NC) directory, if a member.

---

## 13. Directories, in tiers (15 min each; ~3 hours total across a month)

Use the identical details at the top of this document every time. Keep a spreadsheet: directory · listing URL · date · login email. (Claude will generate a pre-filled tracker on request.)

**Tier 1 — this week:** Yelp for Business · Better Business Bureau free profile (bbb.org/get-listed) · Yellow Pages (yp.com) · Manta · Nextdoor Business.
**Tier 2 — next week:** Alignable · Foursquare for Business · Hotfrog · Cylex · Crunchbase · Clutch.co · GoodFirms.
**Tier 3 — industry, following week:** Procore Network · BuildZoom · The Blue Book · ConstructConnect/Dodge · PharmaSource / BioProcess International supplier directory · ThomasNet.

Skip Chambers of Commerce unless you join (fee). Government registries — SAM.gov (UEI), NC eVP, NC HUB, Wake County vendor — only if you decide to pursue public or university work.

---

## 14. Earned links (30 min/week)

1. Send the partner-listing email (template in `SEO_OWNER_CHECKLIST.md` §7) to four GCs/CMs and two A/E firms you have worked alongside; offer a reciprocal listing.
2. Email the ISPE Carolina–South Atlantic chapter programs chair offering a talk: "CQV planning starts in design."
3. Submit to Triangle Business Journal *People on the Move*: "Drew Jones, PE, founds JCS Engineering PLLC" (free form on their site).
4. Add JCS to the NC Biotechnology Center life-science company directory.
5. Pitch one guest article (template in §7) to Pharmaceutical Engineering, Pharmaceutical Processing World, or BioProcess Online, based on an Insights post.

---

## 15. Monthly content (2–3 hours/month)

1. First Tuesday: tell Claude "write post #4" (next in `SEO_CONTENT_CALENDAR.md`). Review the draft; Claude builds and pushes it.
2. Same day: LinkedIn post (personal + company) linking to it; Business Profile post linking to it.
3. Add one new Business Profile photo.
4. Complete five directory listings from item 13.
5. Send two partner-link asks from item 14.

---

## 16. Measure (15 min/week; half a day quarterly)

**Weekly:** Search Console → **Performance** (queries and pages gaining impressions) → **Pages** (fix anything "Crawled – not indexed"). Reply to reviews.
**Two weeks from launch:** private window, search "pharmaceutical engineering consultant Raleigh NC" — is JCS in the map list?
**30 / 60 / 90 days:** re-run all fourteen searches from the survey (`SEO_KEYWORD_MAP.md` §Competitors) and record Places pack / AI Overview / page 1 / not shown in `SEO_RESULTS.md`.
**Quarterly:** ask Claude to re-run the build, CI and Lighthouse; rewrite the two lowest-click-rate titles from Search Console; refresh the oldest article; check every citation for drift; archive before any redesign.
