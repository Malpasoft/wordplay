# Word Play — Project Root

A multi-language Cambridge/CEFR course site (A1–C2) on Cloudflare Pages. Vanilla HTML/CSS/JS
frontend with **no build system**, backed by **Cloudflare Pages Functions + a D1 SQLite
database** for user accounts, token auth, and cross-device progress sync. Tracks: English
(main `a/ b/ c/`), English-for-Spanish-speakers (`es/`), English-for-French-speakers (`fr/`),
Spanish-for-English-speakers (`espanol-en/`), plus planned Spanish (`espanol/`) and French
(`francais/`) main courses. ≈2.5k HTML pages — see `coverage.html` for the live map.

## Read first

- **CLAUDE.md** — the single source of truth: rules, architecture/backend, design system, git
  workflow, cache-busting, engine contracts, and pedagogy. **Start here.**
- **CONTRIBUTING.md** — branch naming, PR workflow, design-rule checklist.
- **PEDAGOGY.md** — learning-design principles every chapter must follow (+ automated checks).
- **SYLLABUS.md** — Cambridge syllabus → site-structure mapping reference.
- **CLOUDFLARE_SETUP.md** — one-time D1 database provisioning + how to verify it's live.
- **TECH_DEBT.md** — open technical-debt register.

## Top-level layout

- **a/ b/ c/** — main English, CEFR A1–A2 / B1–B2 (FCE) / C1–C2 (CAE, CPE).
- **es/** — English explained in Spanish (A1–B2). **espanol-en/** — Spanish for English
  speakers (A1–B2). **fr/** — English for French speakers (A1–B2). **espanol/ francais/** —
  planned main Spanish / French courses.
- **shared/** — CSS + JS engines shared across all pages (see CLAUDE.md → Engine contracts).
- **functions/api/** — Cloudflare Pages Functions (auth, progress, classes, lessons, analytics).
- **migrations/** — D1 SQL schema. **wrangler.jsonc** — D1 binding config.
- **Teacher tools (root):** `teacher.html` (hub), `calendar.html`, `profile.html`,
  `builder.html`, `dev-hub.html`, `coverage.html`, `dashboard.html`, `login.html`.
- **scripts/** — Python generation + maintenance tooling (`pedagogy_check.py`,
  `check_links.py`, `validate_inline_js.py`, `gen_*`, `fill_chapter.py`, `content/`).

## For contributors & AI sessions

Start with **CLAUDE.md** (rules + architecture), then **CONTRIBUTING.md** (branch/PR
conventions). Student progress is cached in browser localStorage and synced to the D1 backend
for signed-in users; logged-out use still works localStorage-only.
