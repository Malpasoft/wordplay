# Word Play — Project Root

A complete Cambridge English course (A1–C2) as a static website on Cloudflare Pages. Vanilla HTML/CSS/JS, no build system, ~2,187 HTML pages. Two parallel tracks: English (main course) and Spanish-native (`/es/`).

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
- **es/** — Spanish-native parallel course. Full A1–C2 curriculum scaffolded across all 6 levels and 3 sections (grammar, vocabulary, writing).
- **shared/** — CSS and JS engines shared across all ~2,187 pages.
- **scripts/** — Python generation and maintenance scripts. `fill_chapter.py` + `scripts/content/` hold content-fill tooling.

---

## For contributors & AI sessions

Start with **CLAUDE.md** (rules), then **AI_HANDOVER.md** (orientation). PR and branch conventions are in **CONTRIBUTING.md**.

All student progress lives in browser localStorage — no backend, no accounts (yet).

---
_Last updated: May 2026_