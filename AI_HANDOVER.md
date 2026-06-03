# Word Play — AI & Developer Handover

**Read `CLAUDE.md` first (it holds all the rules), then this file for orientation.**

**Total HTML pages:** ~2,372  
**Live URL:** https://wordplay-38t.pages.dev (Cloudflare Pages project `wordplay-38t`)  
**GitHub repo:** `malpasoft/wordplay` → Cloudflare Pages auto-deploys from `main`

---

## 1. The person you are working with

**Em** — freelance English teacher in Catalunya, Spain. Works via GitHub + Claude Code (remote sessions). Does not run local code, has no IDE.

**Communication style:** Direct. Brief. No filler. No flattery. Pushes back on padded responses.

**What she values:**
- Clean minimal formatting (no decorative emoji, no headers everywhere)
- Amber-only accent colour — no navy/gold/teal drift
- Finishing and polishing existing content over adding new features
- Pushback when she's wrong (constructively)

**What annoys her:**
- AI over-explaining instead of doing
- Any drift from established patterns without telling her
- Spanish-specific content mixed into the main English course

---

## 2. How a session works

The project is on GitHub. Claude Code is used in remote sessions with direct push access.
The full git/deploy/cache-bust rules are in **CLAUDE.md** — in short:

1. Develop on the session's feature branch (never `main` directly); the branch name is given per session.
2. Deploy with `git push origin HEAD:main` (Cloudflare Pages auto-deploys `main`), then
   sync the feature branch.
3. Bump the per-file `?v=vNN` suffix only on the shared assets you actually change.
4. No zip packaging. Just commit + push.

---

## 3. What Word Play is

A **static** Cambridge English course (A1 to C2) on Cloudflare Pages. Vanilla HTML / CSS / JS. No build system. No backend for content — student progress lives in **browser localStorage**. Teacher tools (calendar, profiles) sync to Cloudflare D1 via passphrase code.

---

## 4. Content state

### English track — 213 chapters

**Grammar — 110 chapters**
| Level | Chapters | Notes |
|-------|----------|-------|
| A1    | 24       | Fully enriched |
| A2    | 19       | Fully enriched |
| B1    | 21       | Fully enriched |
| B2    | 18       | Mostly enriched |
| C1    | 17       | Scaffolded; grammar complete, vocab has 13/14 placeholder |
| C2    | 11       | Scaffolded; grammar complete, vocab has 10/12 placeholder |

**Vocabulary — 77 topics**
| Level | Topics | Template | Notes |
|-------|--------|----------|-------|
| A1    | 12     | Old (renderCard / STORAGE_KEY) | animals chapter: split flashcards + match game |
| A2    | 12     | New (showCard / MASTERY_KEY) | |
| B1    | 11     | New | |
| B2    | 16     | New | |
| C1    | 14     | New | 13/14 chapters have placeholder word data |
| C2    | 12     | New | 10/12 chapters have placeholder word data |

**Writing — 26 chapters** (A1/A2/B1: 3 each; B2: 5; C1/C2: 6 each)

**Exam prep** — FCE (B2) full 7-part coverage; CAE (C1) and CPE (C2) strategy + part guides. Mock papers are placeholders.

---

### Spanish / ES track (`/es/`) — vocab + writing, all 6 levels

Grammar section is entirely missing from the ES track (no es/*/grammar folders).  
All 71 vocabulary flashcard files (es/a1–c2/vocabulary/*/flashcards.html) are stub placeholders.  
Writing sections are complete across all levels.

Fill tooling: `scripts/fill_chapter.py` + content modules in `scripts/content/`.

---

### Espanol-en track (`/espanol-en/`) — Spanish course for English speakers

A1: fully complete (vocabulary + grammar + writing).  
A2–C2: stub hub pages only (index.html per level, no chapter content).

---

### French track (`/fr/`)

Not yet generated as files. The builder (`builder.html`) fully supports `fr` track content creation with French UI strings. No actual lesson files exist yet.

---

## 5. Teacher tools (root level)

| File | Purpose | Backend |
|------|---------|---------|
| `teacher.html` | Hub linking all teacher tools | none |
| `calendar.html` | Full lesson calendar: week/month, 5 lesson types, student autocomplete | D1 sync via passphrase |
| `profile.html` | Per-student profiles: name, L1, level, goals, tracks | D1 sync via passphrase |
| `builder.html` | Tokenless content creator — teacher fills data, downloads file | none |
| `dev-hub.html` | AI prompt generator for content tasks (DeepSeek/Gemini free tier) | none |
| `coverage.html` | Static content coverage map: complete vs stub vs missing per level | none |
| `dashboard.html` | Student progress: XP, stats, radar chart, level tiles | localStorage |
| `placement-test.html` | 24-question level finder | localStorage |

### Cloudflare D1 backend (calendar + profiles cross-device sync)

The D1 code is in the repo but the database binding lives in the Cloudflare dashboard —
**see `CLOUDFLARE_SETUP.md` for the one-time setup and how to verify it's live.**

- DB name `wordplay_db`, binding `DB`, no `wrangler.toml` (dashboard-configured)
- Migrations: `migrations/0001_teacher_profiles.sql`, `migrations/0002_lessons.sql`
- Functions: `functions/api/profiles/[code].js`, `functions/api/lessons/[code].js`
- Auth = shared passphrase (`wordplay_sync_code`, 8–64 chars), no accounts yet
- **Graceful fallback:** if the DB isn't bound, both tools still work localStorage-only
  (single browser). Verify sync at `/api/profiles/testtesttest` → `{"profiles":[],...}` = live.

---

## 6. The shared engines in `shared/`

No dependencies, no imports. Pages link with `?v=vNN` cache-busting. Versions are independent per file.

| Asset | Version | Role |
|-------|---------|------|
| base.css | v123 | Global layout, design tokens, dark mode |
| slides.css | v115 | Lesson deck styles (`body.deck-body` required) |
| deck.js | v113 | Slide nav, progress, completion, confetti |
| game.css | v110 | Mastery game styles |
| game.js | v110 | 4-stage mastery engine (recognition → meaning → context → production) |
| store.js | v105 | localStorage wrapper, FCEStore, XP, chapter registry |
| worksheet.js | v106 | Auto-grader (MCQ + text, with explanations) |
| print.js | v102 | Print/PDF modal helper |
| dark-init.js | v109 | Dark/light toggle, back-to-top injection |

**Key variables in `base.css`:**  
`--amber: #B8860B / #C9A050 dark` (only accent — always `var(--amber)`), `--paper: #F7F3EE / #0E0E0E dark`, `--ink: #1A1A1A / #F0F0F0 dark`, `--cream: #F0EBE0`, `--hairline: #E0D8CC`, `--muted: #6B6560`.

---

## 7. Two flashcard templates — CRITICAL, never mix

**Old template (A1 vocab only):**
```js
var STORAGE_KEY = 'wordplay_vocab_a1_{slug}_mastered';
var WORDS = [{ word, definition, example, pronunciation }, ...];
function renderCard(idx) { ... }
function markMastered() { ... }
```

**New template (A2–C2 vocab):**
```js
var MASTERY_KEY = 'wordplay_vocab_{level}_{slug}_mastered';
var SLUG = '...'; var LEVEL = '...';
var WORDS = [{ word, ipa, def, ex }, ...];
function showCard(idx) { ... }
function markMastered() { ... }
```

---

## 8. Match game (match.html) — new standalone design

The match game is now a separate file (`match.html`) distinct from `flashcards.html`.  
Currently exists only for `a/a1/vocabulary/animals/`.

Design: 3 hearts/lives, each word must be matched to its definition **twice** to win.  
Win/lose overlays. Mastery saved to `MASTERY_KEY` + `wordplay_progress` on win.  
Generated by `builder.html` (generateMatch function). Roll-out to all vocab chapters is pending.

---

## 9. Progress / localStorage schema

```
wordplay_progress = {
  a1: {
    'slides_{chapterId}':         { done: true, date: "ISO" },
    '{chapterId}':                { pct: 85, done: true },
    'wordplay_game_{chapterId}':  { pct: 90 },
    'vocab_mastered_{topic}':     { done: true, date: "ISO" },
  }
}
wordplay_dark = "1" | "0"
wordplay_sync_code = "XXXX-XXXX"   // D1 passphrase for calendar + profiles
wordplay_lessons_cache = [...]      // lesson objects cached from D1
wordplay_student_profiles = {...}   // student profile objects
```

---

## 10. Standard file structure

**English chapters:**
```
{band}/{level}/{section}/{slug}/
  slides.html       lesson (body class="deck-body")
  flashcards.html   vocab only
  match.html        vocab only — 3-lives standalone match game (animals only so far)
  worksheet.html    auto-graded practice
  game.html         4-stage mastery game
```
Where `band` = `a` (A1/A2), `b` (B1/B2), `c` (C1/C2).

**Spanish chapters (`es/`):**  
`es/{level}/vocabulary/{slug}/` — flashcards (stub), slides, game  
`es/{level}/writing/{slug}/` — slides, worksheet, game  
Grammar section: not yet built.

---

## 11. MCP + Skills

`.mcp.json` at project root configures `playwright` (headless, isolated).  
Project-level skills live in `.claude/skills/` and are copied to `~/.claude/skills/` on session start via `.claude/hooks/session-start.sh`.

Custom skills: `/insights` — generates a styled HTML project report (coverage, engine versions, gaps, roadmap). Deliver via `SendUserFile`, never commits.

---

## 12. Roadmap

**Active (next sessions):**
1. Fill 71 ES vocabulary flashcard stubs — use dev-hub + DeepSeek/Gemini, run `fill_chapter.py`
2. Fill C1/C2 English vocabulary — 23 chapters with placeholder word data, use `fill_en_c1c2_vocab.py`
3. Roll out match.html to all vocab chapters — pattern proven in animals, builder generates the file
4. Espanol-en A2–C2 content fill
5. ES grammar section (all 6 levels — currently completely missing)

**Parked / horizon:**
- Auth: email + password → passkey (Phase 3, needs custom domain first)
- Payments: Stripe Pro tier (Phase 4, after auth)
- Audio: R2 + OpenAI TTS for listening practice (Phase 5)
- /espanol/ Spanish course + DELE prep (Phase 6)
- /fr/ French track file generation (builder ready, no files yet)
- Review pages + Printable pages (0 exist site-wide)

---

## 13. Known pending items

- A2–C2 vocab flashcards: missing audio button — pedagogy check enforces `speakWord` but A2–C2 template doesn't have it yet
- C1/C2 English vocabulary: 23 of 26 chapters are structural shells with placeholder word data
- 71 ES flashcard stubs: all ES vocabulary flashcards are placeholders
- ES grammar: entire section missing across all 6 levels
- Espanol-en A2–C2: stub hubs only, no chapter content
- match.html: only 1 of ~77 vocab chapters has it (animals/A1)
- 26 pedagogy warnings: espanol-en/a1/grammar slides missing `.trap-row` common-mistakes slide

---

## 14. Recent work (June 2026)

- **Animals chapter split:** `a/a1/vocabulary/animals/` now has separate `flashcards.html` (new template) + `match.html` (new 3-lives double-match game) + `index.html` 4-card hub
- **Builder (`builder.html`):** extended to all content types (lesson, game, worksheet, flashcard, match); French (`fr/`) track support; auto-preview after build
- **Calendar (`calendar.html`):** mobile week-grid now horizontally scrollable on iPhone; lesson modal redesigned to match design system
- **Lesson calendar:** full week/month views, D1 sync via passphrase, 5 lesson types, student autocomplete from profiles
- **Student profiles (`profile.html`):** D1 cloud sync, 4 language tracks, exam target, lesson format fields
- **Teacher hub (`teacher.html`):** menu structure, AI Prompts sub-page, hub cards for all tools
- **Espanol-en scaffold:** A1 complete (vocabulary + 24 grammar + writing); A2–C2 hub stubs
- **Content builder tooling:** `scripts/gen_scaffold.py`, `fill_chapter.py`, `content/` modules
- **Search index:** 424 chapters indexed

*Updated 3 June 2026*
