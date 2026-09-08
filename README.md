# jcseng.com — JCS Engineering PLLC

Static website for JCS Engineering, hosted on **Cloudflare Pages** and deployed automatically from this repository.

> **Live site = the `main` branch.** Anything pushed to `main` is live within about a minute. Everything else in this file explains how to change it safely, how to archive a version, and how to roll back.

---

## Contents

1. [How deployment works](#how-deployment-works)
2. [Site structure](#site-structure)
3. [Making changes](#making-changes)
4. [Archiving a version](#archiving-a-version)
5. [Restoring an archived version](#restoring-an-archived-version)
6. [Version history](#version-history)
7. [Third-party services](#third-party-services)
8. [After every deploy](#after-every-deploy)

---

## How deployment works

| You do this | Cloudflare does this |
|---|---|
| Push (or merge) to `main` | Builds and publishes to **jcseng.com** — live in ~30–90 seconds |
| Push to any other branch | Builds a **preview** at a `*.pages.dev` URL — the live site is untouched |

There is no build step. The files in this repo are served exactly as they are.

**Where to look in Cloudflare:** Workers & Pages → the Pages project → **Deployments** shows every build and whether it succeeded. **Custom domains** is where `jcseng.com` is attached.

---

## Site structure

```
/                      index.html            Home
/capabilities/         capabilities/index.html
/approach/             approach/index.html
/about/                about/index.html
/contact/              contact/index.html
/privacy/              privacy/index.html
/capabilities/<slug>/  six service pages        (generated)
/service-areas/        service-areas/index.html
/experience/           experience/index.html
/faq/                  faq/index.html
/insights/             insights/index.html + /insights/<slug>/ posts
/llms.txt, /humans.txt, /site.webmanifest, /<indexnow-key>.txt
/404.html                                    Custom not-found page
/assets/css/styles.css                       All styling (one file)
/assets/js/main.js                           Mobile nav, FAQ, form submission, reveal animation
/assets/fonts/                               Inter + IBM Plex Mono, self-hosted (no Google Fonts)
/assets/img/                                 Logo (SVG), favicon set, headshot, hero photo, social card
/_headers                                    Cloudflare cache + security headers
/robots.txt, /sitemap.xml
```

Clean URLs (`/about/` instead of `/about.html`) come from the folder-plus-`index.html` layout — keep that pattern for any new page.

---

## Making changes

### Editing text or content
Edit the relevant `index.html` directly. Two things to know:

- **The header and footer are repeated in every page.** If you change a nav link, phone number, or footer line, change it in all seven HTML files (`index.html`, the six `*/index.html`, and `404.html`). Search the repo for the old text to find every copy.
- **Ampersands are written as `&amp;`** in the HTML. Write `Design &amp; CQV`, not `Design & CQV`.

### Editing styles or JavaScript
Every HTML file loads the stylesheet and script with a **version stamp** (now set automatically by `tools/build.py` — run the build after any CSS/JS change):

```html
<link rel="stylesheet" href="/assets/css/styles.css?v=2c090a25" />
<script src="/assets/js/main.js?v=43fb5e86" defer></script>
```

Browsers and Cloudflare cache these files for a year (see `_headers`). If you edit `styles.css` or `main.js` **and don't change the `?v=` value in every HTML file**, visitors keep seeing the old version — this was the cause of the "gray button / bunched text" problems during the build. Any new value works (e.g. `?v=2026-09-15`). Change it in all seven files.

### Adding a page
Create `newpage/index.html` by copying an existing page, update its `<title>`, `<meta name="description">`, `<link rel="canonical">`, and `og:` tags, add it to the nav and footer in all pages, and add a `<url>` entry to `sitemap.xml`.

### Contact form
The form posts to Formspree (`https://formspree.io/f/xqadzgzp`). **Which email receives submissions is set in the Formspree account, not in this code.** Log in at formspree.io to change it.

---

## Archiving a version

Do this **before** any significant redesign so the current site can always be recovered. Two layers — the branch takes 30 seconds; the release is the gold standard and takes two minutes in the GitHub UI.

### Layer 1 — archive branch (always do this)

From a terminal, with `main` up to date:

```bash
git fetch origin
git branch archive/vX.Y.Z-short-name origin/main
git push origin archive/vX.Y.Z-short-name
```

Or in the GitHub UI: open the branch dropdown on the repo home page, type the new name `archive/vX.Y.Z-short-name`, and choose **Create branch from main**.

Naming: `archive/v1.1.0-new-photos`, `archive/v2.0.0-redesign`, etc. Bump the first number for a redesign, the second for new pages or sections, the third for small fixes.

### Layer 2 — tag + GitHub Release (recommended)

A Release gets its own permanent page with a downloadable zip, and a tag can't be mistaken for a working branch.

1. Go to **https://github.com/djones921/jones-consultants-site/releases/new**
2. **Choose a tag** → type the version, e.g. `v1.1.0` → click **Create new tag on publish**
3. **Target** → select the archive branch you just made (or `main` if you haven't)
4. **Release title:** `v1.1.0 — short description`
5. **Description:** one or two lines on what this version is (what changed, why it's being archived)
6. **Publish release**

### Layer 3 — protect archives from deletion (do once)

Settings → **Rules** → **Rulesets** → **New ruleset**

- **Branch ruleset:** target `archive/**` → enable **Restrict deletions** and **Block force pushes** → Save
- **Tag ruleset:** target `v*` → enable **Restrict deletions** → Save

After this, an archive can only be removed by deliberately editing the rule first.

---

## Restoring an archived version

**To view it:** open the archive branch on GitHub, or the Release page, or download the zip from either.

**To make it live again** (roll back the site):

```bash
git fetch origin
git checkout main
git reset --hard origin/archive/vX.Y.Z-short-name    # or: git reset --hard vX.Y.Z
git push --force-with-lease origin main
```

Cloudflare redeploys `main` automatically. If you'd rather not force-push, archive the *current* `main` first (Layer 1 above), then do the reset — nothing is lost either way.

**To recover a single file** from an old version without rolling back everything:

```bash
git checkout vX.Y.Z -- path/to/file
git commit -m "Restore path/to/file from vX.Y.Z"
git push origin main
```

---

## Version history

| Version | Date | Commit | Archive branch | Notes |
|---|---|---|---|---|
| **v1.0.0** | 2026-09-08 | `e93d548` | `archive/v1.0.0-launch` | Launch version under the JCS Engineering brand. Six-page site, six services, vector logo, self-hosted fonts, cache-busted assets. |

Add a row each time you archive.

---

## Third-party services

| Service | Used for | Where it's configured |
|---|---|---|
| **Cloudflare Pages** | Hosting, deploys, `jcseng.com` domain, cache | Cloudflare dashboard |
| **Formspree** (`f/xqadzgzp`) | Contact form delivery | formspree.io account — destination email lives here |
| **Google Maps embed** | Map on the contact page | `contact/index.html` (iframe `src`) |
| **GitHub** | Source of truth, archives | This repo |

Fonts are self-hosted in `/assets/fonts/`; there is no Google Fonts, analytics, or tracking dependency. The privacy policy at `/privacy/` describes exactly this set — **update it if you add a service.**

---

## After every deploy

1. Wait a minute, then check **Deployments** in Cloudflare shows a green build for `main`.
2. **Hard-refresh** the site (Ctrl+Shift+R / Cmd+Shift+R) or open it in a private window.
3. If something still looks stale and you changed CSS or JS: confirm the `?v=` stamps were updated (see *Making changes*). If they were, purge Cloudflare's cache: your domain → **Caching** → **Configuration** → **Purge Everything**.
4. Check one page on a phone.

---

## SEO build system (added September 2026)

Pages are **generated**, not hand-edited. The source of truth is `tools/siteconfig.py` (business facts, services, FAQs, posts metadata) and `tools/posts.py` (article bodies); `tools/build.py` renders every page, `robots.txt`, `sitemap.xml`, `llms.txt`, `site.webmanifest`, the IndexNow key file, and `docs/seo_page_inventory.csv`.

```bash
python3 tools/build.py      # regenerate everything; fails if a title > 60 chars, a description is outside 140–160, or a page has ≠ 1 <h1>
```

Edit content in `tools/siteconfig.py`, run the build, commit the result. Hand-editing an `index.html` will be overwritten on the next build and fails CI ("committed HTML is out of date"). Asset URLs are versioned automatically by the build — you no longer need to bump `?v=` by hand.

**Open fields to fill** (`None` in `siteconfig.py`; omitted from output until set): address basis, geo coordinates, hours, LinkedIn URLs, Google Business Profile URL, founding year, Search Console and Bing verification tokens. See `docs/SEO_OWNER_CHECKLIST.md` §0.

**CI:** `.github/workflows/seo-check.yml` runs on every pull request — build freshness, html-validate, link check (lychee), Lighthouse CI budgets (`lighthouserc.json`). `.github/workflows/indexnow.yml` notifies Bing/IndexNow after each deploy to `main`.

**SEO documents** (`docs/`, served with `X-Robots-Tag: noindex`): `SEO_AUDIT.md` · `SEO_KEYWORD_MAP.md` · `SEO_CONTENT_CALENDAR.md` · `SEO_OWNER_CHECKLIST.md` · `SEO_RESULTS.md` · `seo_page_inventory.csv`.

---

*Maintained for JCS Engineering PLLC · Raleigh, NC · NC Engineering Firm License P-3451*
