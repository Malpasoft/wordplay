# Word Play — Project Guide

> **This file is the single source of truth for project rules.** Design system, git
> workflow, conventions, and pedagogy live here. Other docs (AI_HANDOVER.md,
> SESSION_CONTEXT.md, CONTRIBUTING.md) link back to this file instead of restating
> rules — so there is only ever one place to update.
>
> **Known technical debt is tracked in `TECH_DEBT.md`** — check it before large refactors.

## Project

Static multi-language course site (English, Spanish, French) on Cloudflare Pages.
Vanilla HTML/CSS/JS, no build system, no backend. All student progress lives in browser
localStorage. Teacher tools (calendar, profiles, dev-hub, builder, coverage) at root level.

**Repo:** `malpasoft/wordplay`
**Orientation:** read `AI_HANDOVER.md` after this file for who the project is for and its current state.

### Course architecture (June 2026)

Homepage = 3 language cards → language hub → courses for that language.

| Hub | Course | Dir | UI lang | Levels | Exams |
|---|---|---|---|---|---|
| `/english/` | Main English | `a/ b/ c/` | en | A1–C2 | KET PET FCE CAE CPE |
| `/english/` | English for Spanish speakers | `es/` | es | A1–B2 | — |
| `/english/` | English for French speakers | `fr/` | fr | A1–B2 | — |
| `/espanol/` | Main Spanish | `espanol/` | es | A1–C2 (building) | DELE |
| `/espanol/` | Spanish for English speakers | `espanol-en/` | en | A1–B2 | — |
| `/francais/` | Main French | `francais/` | fr | A1–C2 (planned) | DELF/DALF |
| `/francais/` | French for EN / ES speakers | `francais-en/ francais-es/` | en / es | A1–B2 (planned) | — |

**Rule: L1-mediated courses run A1–B2 only.** At C1+, learners continue in the main
course taught in the target language (each L1 landing page has a handoff card).
es/ and espanol-en/ C1+C2 were deleted June 2026; `_redirects` covers old URLs.

### Per-chapter standard

- **Grammar**: index · slides (Lesson) · worksheet (Review) · game (Mastery) · printables
- **Vocab**: index · flashcards · slides (word list) · game (Mastery) · match
- **Writing**: index · slides · worksheet · game · printables
- Exam prep follows the FCE model (`b/b2/fce/`): about · strategy · writing-overview ·
  part-N (index + graded practice) · mock-1..3 (timed).

---

## Design System

- **Accent colour: amber only.** Always use `var(--amber)` — never hardcode a hex.
  Its real values are `#B8860B` (light mode) / `#C9A050` (dark mode). No second accent
  colour: no teal, gold, navy, or per-card colours.
  - **Allowed exception — activity-card type colours:** chapter hub `index.html` pages use
    `--ac-color` on activity cards. Lesson/practice cards: `var(--amber)`. Game cards:
    `#2E7D52` (green). Print cards: `#6B6B6B` (grey). These type colours are intentional UX
    and are **not** a design-system violation.
- **Background:** `var(--paper)` = `#F7F3EE` (warm parchment) / `#0E0E0E` dark. Ink text
  `var(--ink)` = `#1A1A1A` / `#F0F0F0` dark.
- **Clean, no-emoji UI.** The only symbols used as UI are `◐`/`◑` (dark-mode toggle) and
  `◆` (streak badge). A `.claude/hooks/design-check.sh` hook enforces this automatically
  on every edit — you don't need to police it manually.
- **SVG hearts** are used in match.html and worksheet.js for lives/hearts display. Use the
  standard path with `fill="currentColor"` so CSS color tokens drive the tint — never use
  the `♥`/`♡` Unicode glyphs (they trigger the hook).
- **Dark mode works on every element** — use `!important` overrides in CSS where needed.
- **`class="deck-body"`** on the `<body>` of every `slides.html` lesson page.
- **`class="sect-card"`** for section cards on level hub pages — never inline
  `onmouseover`/`onmouseout`.

---

## Git Workflow & Deployment

- **Develop on the session's feature branch — never commit directly to `main`.** Each session
  is told its branch name (branch names change per session; don't hardcode one here). Commit there as you go.
- **Deploy:** `git push origin HEAD:main` — Cloudflare Pages auto-deploys `main` (~2 min).
  Then keep the feature branch in sync: `git push -u origin <feature-branch>`.
- After completing a task, commit and push — don't stop before deploying.
- For large tasks, commit after each logical sub-task so a session interruption doesn't
  lose progress.
- If a visual change doesn't appear after deploy, suspect the Cloudflare edge cache.

---

## Cache-Busting (shared assets) — CRITICAL

**WHY THIS MATTERS:** Cloudflare Pages caches all `shared/` files for 1 year
(`max-age=31536000, immutable`). Without a version bump, **every deployment will serve
stale code forever** — users won't see any fixes or updates. This has caused
production outages (blank pages, hanging loads). The version parameter (`?v=vNN`) is
the ONLY way to force a cache refresh.

**When a shared file changes:**

1. **Identify the file** — e.g., `shared/store.js`, `shared/base.css`
2. **Bump its version** — increment `?v=vNN` to the next number across all ~2,479 HTML files
   - Use: `python3 bump-versions.py` (automates all HTML updates)
   - OR use `/ship` skill (safer, but slower)
   - Manual edits: prone to missing files — avoid
3. **Commit the version bumps** together with the code change
4. **The pre-commit hook enforces this** — commits are blocked if shared files are modified
   without version bumps

**Current versions (kept in sync by hook):**
- `base.css`: v124
- `dark-init.js`: v112
- `store.js`: v107
- `game.js`: v111
- `worksheet.js`: v108
- `deck.js`: v114
- `game.css`: v112
- `writing-grader.js`: v105
- `sentence-grader.js`: v104
- `mascot.js`: v3
- `slides.css`: v115
- `worksheet.css`: v106
- `print.css`: v102
- `i18n.js`: v124
- `print.js`: v102

**Mascot assets** (added Q2 2026):
- `shared/mascot.css` — sprite animation rules (versions with `index.html`)
- `shared/mascot.js` — state manager & click handler (versions with `index.html`)
- `shared/mascot-bee.png` — sprite sheet image (versions with `index.html`)
- All cached 1 year; PNG also matches `/shared/*.png` rule in `_headers`

**Example commit:**
```
fix: sanitize innerHTML in game.js to prevent XSS

Bump game.js version from v110 to v111 across all ~2,479 HTML files.
Updated via bump-versions.py to ensure Cloudflare cache refresh.
```

`version.json` is a coarse project-state marker only — not a per-asset version.

---

## Bulk Edits

- **Prefer targeted `Edit` calls per file** over scripts that rewrite many HTML files at
  once — batch scripts have repeatedly produced orphaned tags, duplicate blocks, wrong data.
- If a script is genuinely needed (50+ files), verify output on 2–3 sample files first.
- **Never** use `sed`/`awk` to rewrite HTML — use Python with explicit string matching.
- Before any templated fix, `grep` for **all** structural/whitespace variants first.
  Grammar pages and Spanish/vocab pages often differ in whitespace — confirm the file
  count per variant matches expectation before running.

---

## Verification

- Verify visual changes with Playwright across **desktop, dark mode, and mobile (360px)**
  before calling them done.
- Never claim a value/state is "already correct" from memory — re-read the actual source
  line (and show a screenshot when it's a rendering question) before concluding.

---

## Two Flashcard Templates — Never Mix Them

**Old template (A1 vocab only):**
`STORAGE_KEY`, `WORDS[{word, definition, example, pronunciation}]`, `renderCard()`, `markMastered()`

**New template (A2–C2 vocab):**
`MASTERY_KEY`, `SLUG`, `LEVEL`, `WORDS[{word, ipa, def, ex}]`, `showCard()`, `markMastered()`

---

## Progress / localStorage

```
wordplay_progress → { a1: { 'vocab_mastered_{slug}': {done,date}, 'wordplay_game_{slug}': {pct} } }
wordplay_dark = "1" | "0"
```

Dashboard reads `lv['vocab_mastered_' + slug].done`. Full schema: see SESSION_CONTEXT.md.

---

## Pedagogy Principles (non-negotiable)

- Every worksheet question has an EXPLANATION — no exceptions.
- Grading is deterministic — never ask students to self-assess open production.
- Audio pronunciation on all vocab flashcards (Web Speech API, `lang='en-GB'`, `rate=0.9`).
- Flashcards auto-complete after viewing all cards.
- **Dominio Mastery Game (game.js):** 4 key items × 3 question types (significado/meaning, contexto/context, produccion/production). Score toward 100 points. Win = score ≥ 100 AND all 4 items correct. Correct answer = 10 pts (+5 same-item run bonus, +3 cross-item streak bonus). Wrong = -3 pts, requeue. Grading: significado/contexto = MC exact match; produccion = norm'd text match or item.accept[] aliases. See game.js JSDoc for full algorithm.
- Match game (match.html): 3 lives, each word must be matched to its definition twice to win. Mastery saved to localStorage on win.
- `python3 scripts/pedagogy_check.py` must stay at 0 failures before pushing.

---

## MCP Configuration

- MCP servers go in `.mcp.json` at the project root — **not** in `.claude/settings.json`.
