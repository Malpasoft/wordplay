# Word Play — Project Root

A complete Cambridge English course (A1–C2) as a static website on Cloudflare Pages. Vanilla HTML/CSS/JS, no build system, ~2,372 HTML pages. Tracks: English (main), Spanish-explained (`/es/`), Spanish-for-English-speakers (`/espanol-en/`), French support in builder (`/fr/`).

## Top-level files and directories

- **CLAUDE.md** — Single source of truth for all project rules. Read this first.
- **AI_HANDOVER.md** — Orientation for a new AI/developer session: content state, shared engines, localStorage schema.
- **SESSION_CONTEXT.md** — Deep technical reference: JS contracts, current content counts, next steps.
- **CONTRIBUTING.md** — Branch naming, PR workflow, design rules checklist.
- **PEDAGOGY.md** — Learning design principles that every chapter must follow.
- **SYLLABUS.md** — Cambridge syllabus → site structure mapping reference.
- **AUTH_PROPOSAL.md** — Future user-account implementation proposal (not yet built).
- **404.html** — Custom error page.
- **a/** — CEFR A1 and A2 (Beginner / Elementary).
- **b/** — CEFR B1 and B2 (Pre-Intermediate / Upper-Intermediate, FCE exam prep).
- **c/** — CEFR C1 and C2 (Advanced / Proficiency, CAE and CPE exam prep).
- **es/** — Spanish-explained track. A1–C2 vocab + writing scaffolded; grammar section not yet built; 71 vocab flashcards are stubs.
- **espanol-en/** — Spanish course for English speakers. A1 complete; A2–C2 are stub hubs.
- **shared/** — CSS and JS engines shared across all ~2,372 pages.
- **teacher.html** — Teacher hub: calendar, profiles, dev-hub, builder, coverage, AI prompts.
- **calendar.html** — Full lesson calendar with D1 cloud sync.
- **profile.html** — Student profiles with D1 cloud sync.
- **builder.html** — Tokenless content creator: fill data in browser, download file, push to git.
- **dev-hub.html** — AI prompt generator for content tasks (use with DeepSeek/Gemini free tier).
- **coverage.html** — Static content coverage map per level/section.
- **scripts/** — Python generation and maintenance scripts. `fill_chapter.py` + `scripts/content/` hold content-fill tooling.

---

## For contributors & AI sessions

Start with **CLAUDE.md** (rules), then **AI_HANDOVER.md** (orientation). PR and branch conventions are in **CONTRIBUTING.md**.

All student progress lives in browser localStorage — no backend, no accounts (yet).

---
_Last updated: June 2026_