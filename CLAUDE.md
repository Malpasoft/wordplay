# Word Play — Project Guide

> **This file is the single source of truth for project rules.** Design system, git
> workflow, conventions, and pedagogy live here. Other docs (AI_HANDOVER.md,
> SESSION_CONTEXT.md, CONTRIBUTING.md) link back to this file instead of restating
> rules — so there is only ever one place to update.

## Project

Static Cambridge English course (A1–C2) on Cloudflare Pages. Vanilla HTML/CSS/JS, no
build system, no backend. ~2,372 HTML pages. All student progress lives in browser
localStorage. Teacher tools (calendar, profiles, dev-hub, builder, coverage) at root level.

**Repo:** `malpasoft/wordplay`
**Orientation:** read `AI_HANDOVER.md` after this file for who the project is for and its current state.

---

## Design System

- **Accent colour: amber only.** Always use `var(--amber)` — never hardcode a hex.
  Its real values are `#B8860B` (light mode) / `#C9A050` (dark mode). No second accent
  colour: no teal, gold, navy, or per-card colours.
- **Background:** `var(--paper)` = `#F7F3EE` (warm parchment) / `#0E0E0E` dark. Ink text
  `var(--ink)` = `#1A1A1A` / `#F0F0F0` dark.
- **Clean, no-emoji UI.** The only symbols used as UI are `◐`/`◑` (dark-mode toggle) and
  `◆` (streak badge). A `.claude/hooks/design-check.sh` hook enforces this automatically
  on every edit — you don't need to police it manually.
- **Dark mode works on every element** — use `!important` overrides in CSS where needed.
- **`class="deck-body"`** on the `<body>` of every `slides.html` lesson page.
- **`class="sect-card"`** for section cards on level hub pages — never inline
  `onmouseover`/`onmouseout`.

---

## Git Workflow & Deployment

- **Develop on `claude/website-design-token-optimization-1ZNUG`.** Commit there as you go.
- **Deploy:** `git push origin HEAD:main` — Cloudflare Pages auto-deploys `main` (~2 min).
  Then keep the dev branch in sync: `git push -u origin claude/website-design-token-optimization-1ZNUG`.
- After completing a task, commit and push — don't stop before deploying.
- For large tasks, commit after each logical sub-task so a session interruption doesn't
  lose progress.
- If a visual change doesn't appear after deploy, suspect the Cloudflare edge cache.

---

## Cache-Busting (shared assets)

Each file in `shared/` carries its own independent `?v=vNN` suffix in the pages that load
it — the versions are **not** in lockstep (e.g. `base.css` and `slides.css` are on
different numbers). When you change a shared file:

1. `grep` for the current `?v=` value of that one file across the HTML.
2. Bump only that file's consumers to the next number.
3. The `/ship` skill automates this safely.

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
- Match game (match.html): 3 lives, each word must be matched to its definition twice to win. Mastery saved to localStorage on win.
- `python3 scripts/pedagogy_check.py` must stay at 0 failures before pushing.

---

## MCP Configuration

- MCP servers go in `.mcp.json` at the project root — **not** in `.claude/settings.json`.
