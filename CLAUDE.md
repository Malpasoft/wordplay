# Word Play — Claude Code Project Guide

## Project
Static Cambridge English course (A1–C2) on Cloudflare Pages. Vanilla HTML/CSS/JS, no build system, no backend. ~822 HTML pages. All student progress in browser localStorage.

**Repo:** `malpasoft/wordplay`  
**Live deploy:** Cloudflare Pages auto-deploys from `main` on push.  
**Handover doc:** `AI_HANDOVER.md` — read this first in any new session.

---

## Design System (STRICT — check before every edit)

- **Accent colour: amber only** — `#E8A020` / `var(--amber)`. No other accent colours. No teal, gold, navy, per-card colours.
- **No emojis anywhere** — not in UI, not in content, not in commit messages. The only exceptions are `◐`/`◑` for the dark mode toggle and `◆` for the streak badge.
- **Dark mode must work on every element** — use `!important` overrides in CSS where needed.
- **`class="deck-body"`** on `<body>` of every `slides.html` lesson page.
- **`class="sect-card"`** for dark section cards on level hub pages — never inline `onmouseover/onmouseout`.
- **Cache-bust** all shared asset URLs with `?v=vNN` when touching `shared/` files.

---

## Git Workflow

- **Always work on `main`** — Cloudflare Pages deploys from `main`. Never leave work on a feature branch without telling the user.
- After completing any task: `git add`, `git commit`, `git push origin main` — do not stop before pushing.
- For large tasks: commit after each logical sub-task so a session limit doesn't lose progress.
- Current working branch: `claude/github-workflow-setup-98Fbf` — this branch is force-pushed to `main` to deploy.

---

## Bulk Edits

- **Prefer targeted `Edit` calls per file** over Python/shell scripts that rewrite many HTML files at once — batch scripts have repeatedly produced orphaned tags, duplicate blocks, and wrong data.
- If a script is genuinely needed (50+ files), always verify output on 2–3 sample files before running on the full set.
- Never use `sed` or `awk` to rewrite HTML — use Python with proper string matching and write to a temp file first.

---

## MCP Configuration

- MCP servers go in `.mcp.json` at the project root — **not** in `.claude/settings.json`.

---

## Two Flashcard Templates — Never Mix Them

**Old template (A1 vocab only):**
- `STORAGE_KEY`, `WORDS[{word, definition, example, pronunciation}]`, `renderCard()`, `markMastered()`

**New template (A2–C2 vocab):**
- `MASTERY_KEY`, `SLUG`, `LEVEL`, `WORDS[{word, ipa, def, ex}]`, `showCard()`, `markMastered()`

---

## Progress / localStorage

```
wordplay_progress → { a1: { 'vocab_mastered_{slug}': {done,date}, 'wordplay_game_{slug}': {pct} } }
wordplay_dark = "1" | "0"
```

Dashboard reads `lv['vocab_mastered_' + slug].done`.

---

## Pedagogy Principles (non-negotiable)

- Every worksheet question has an EXPLANATION — no exceptions.
- Grading is deterministic — never ask students to self-assess open production.
- Audio pronunciation on all vocab flashcards (Web Speech API, `lang='en-GB'`, `rate=0.9`).
- Flashcards auto-complete after viewing all cards; match game auto-completes after 5 rounds.
