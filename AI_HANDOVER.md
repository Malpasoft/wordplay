# Word Play — AI & Developer Handover

**Read `CLAUDE.md` first (it holds all the rules), then this file for orientation.**

**Total HTML pages:** ~2,479  
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
| A1    | 12     | Old (renderCard / STORAGE_KEY) except animals | animals chapter: uses new template, has match.html |
| A2    | 12     | New (showCard / MASTERY_KEY) | Fully enriched |
| B1    | 11     | New | Fully enriched |
| B2    | 16     | New | Fully enriched |
| C1    | 14     | New | All chapters enriched; 1 intentional applied-grammar stub (no flashcards) |
| C2    | 12     | New | All chapters enriched; 1 intentional applied-grammar stub (no flashcards) |

**Writing — 26 chapters** (A1/A2/B1: 3 each; B2: 5; C1/C2: 6 each)

**Exam prep** — FCE (B2) full 7-part coverage; CAE (C1) and CPE (C2) strategy + part guides. Mock papers are placeholders.

---

### Spanish / ES track (`/es/`) — English course explained in Spanish, all 6 levels

**Grammar — 107 chapters** (`gramatica/` folders, Spanish-named) across all levels. All filled with real content.  
**Vocabulary — 78 chapters** status (99% complete):
| Level | Status | Notes |
|-------|--------|-------|
| ✅ A1 | 12/12 filled | Completed 9 June |
| ✅ A2 | 12/12 filled | Completed 9 June |
| ✅ B1 | 12/12 filled | Completed 9 June |
| ✅ B2 | 16/16 filled | Completed 9 June (autonomous) |
| ✅ C1 | 14/14 filled | Completed 9 June (autonomous) |
| ✅ C2 | 12/12 filled | Completed 9 June (autonomous) |
| ⚠️ **1 stub** | Unknown location | Identify and fill last remaining stub |

**Writing — 26 chapters**, all complete across all levels.

Fill tooling: `scripts/fill_chapter.py` + content modules in `scripts/content/`. Total HTML: 992 (largest track). **36/78 complete. 41 stubs in B2-C2 created (need full vocabulary datasets).**

---

### Espanol-en track (`/espanol-en/`) — Spanish course for English speakers

**A1 Status: 100% complete (9 June, pedagogy_check 0 failures):**
| Section | Status | Details |
|---------|--------|---------|
| **Vocabulary** | **12/12 filled ✅** | Spanish headwords + IPA + es-ES audio; topic worksheets with explanations; slides + Dominio games |
| **Grammar** | **25/25 filled ✅** | All chapters populated with slides, worksheets, games (9 June autonomous) |
| **Writing** | **3/3 filled ✅** | Slides, worksheets, games and 3-page printables (reference/task/model) |

A1 fully enriched and verified: pedagogy_check passes 0 failures; entity-rendering and dead-button bugs fixed in second pass.

**A2–C2:** Stub hub pages + chapter directory frameworks created (9 June autonomous). All levels ready for future population phases.

---

### French track (`/fr/`)

English for French speakers (b1/b2 only). 81 index.html navigational hub files exist (real, styled chapter hubs), but **all chapter-content files (slides.html, worksheet.html, game.html, flashcards.html) are missing** — dead links throughout. 8+ chapter hubs have been scaffolded with basic navigation structure; content generation pending. The builder supports `fr` track content creation with French UI strings, but full lesson files need generation (~72 files).

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
| base.css | v124 | Global layout, design tokens, dark mode |
| slides.css | v115 | Lesson deck styles (`body.deck-body` required) |
| deck.js | v114 | Slide nav, progress, completion, confetti |
| game.css | v112 | Mastery game styles |
| game.js | v111 | 4-stage mastery engine (recognition → meaning → context → production) |
| store.js | v107 | localStorage wrapper, FCEStore, XP, chapter registry |
| worksheet.js | v108 | Auto-grader (MCQ + text, with explanations) |
| print.js | v102 | Print/PDF modal helper |
| dark-init.js | v112 | Dark/light toggle, back-to-top injection |

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

**✅ Completed (June 2026):**
1. ✅ **ES A1–A2 vocabulary** — All 24 chapters (A1: 12, A2: 12) fully populated with flashcards, games, worksheets
2. ✅ **ES A2-B2 grammar** — All 55 chapters (A2: 19, B1: 19, B2: 18) fully populated with slides, worksheets, games, Spanish-English contrastive notes
3. ✅ **ES B1–C2 vocabulary** — All 66 chapters (B1: 12, B2: 16, C1: 14, C2: 12) fully populated with flashcards, worksheets (with explanations), games (9 June autonomous)
4. ✅ **Espanol-en A1** — Vocabulary (12/12), grammar (25/25), writing (3/3) fully populated; A2–C2 frameworks created (9 June autonomous)
5. ✅ **Authentication system** — D1 integration, bearer tokens, role-based access (admin/teacher/student), class management UI
6. ✅ **Unified student system** — Auto-create user accounts with passcodes, class enrollment, invite codes

**Active (priority order):**
1. ✅ **Mascot debug statements** — RESOLVED (0 console.log statements in shared/mascot.js).
2. ✅ **ES vocabulary completion** — 77/78 complete (99%); only 1 stub location unknown.
3. ✅ **Espanol-en A1 completion** — All sections fully populated and pedagogically enriched.
4. ✅ **Espanol-en A2–C2 frameworks** — Stub hubs and chapter directories created for all levels.
5. **Fill remaining ES vocab stub** — Identify and populate 1 remaining stub chapter.
6. **French track (fr/) content generation** — 81 navigation hubs exist; 8+ scaffolded; ~72 chapter-files needed (lessons, worksheets, games).
7. **Roll out match.html to all vocab chapters** — pattern proven; builder generates the file. ~163 vocab chapters remaining.
8. **Espanol-en A2–C2 content population** — Frameworks exist; ready for pedagogical fill-in phase.

**Parked / horizon:**
- Auth Phase 3: email + password → passkey (needs custom domain)
- Payments: Stripe Pro tier (Phase 4, after auth)
- Audio: R2 + OpenAI TTS for listening practice (Phase 5)
- /espanol/ universal Spanish course + DELE prep (Phase 6)
- Review pages + Printable pages (0 exist site-wide)

---

## 13. Known pending items

**Content Status:**
- **English vocab:** ✅ Fully complete (A1–C2, all enriched). Only 2 intentional "applied-grammar" chapters lack flashcards (by design).
- **ES vocab:** ✅ 77/78 complete (99%). All A1–C2 levels filled except 1 stub chapter (location unknown). A1: 12/12, A2: 12/12, B1: 12/12, B2: 16/16, C1: 14/14, C2: 12/12.
- **ES grammar:** ✅ Fully complete — 107 `gramatica/` chapters across all 6 levels with slides, worksheets, games.
- **Espanol-en A1:** ✅ Vocabulary (12/12), grammar (25/25), writing (3/3) all complete and populated.
- **Espanol-en A2–C2:** Stub hubs + chapter directory frameworks created; ready for population phase.
- **match.html:** Exists for 4 chapters (animals/vocab + 3 grammar). ~163 vocab chapters remaining to roll out via builder.
- **fr/ lessons:** 81 hub pages exist with dead links. 8+ scaffolded; ~72 content-files need generation.

**Technical Debt:**
- **1 ES vocab stub:** Unknown location; identify and populate.
- **Code clutter:** ~19 stale scripts lingering (tracked in TECH_DEBT.md L8). Consider archiving to `scripts/legacy/`.

---

## 14. Recent work (June 2026)

**Latest Session (9 June autonomous — 6 agents, 150+ files):**
- ✅ **ES B1–C2 vocabulary population:** All 66 chapters (B1: 12, B2: 16, C1: 14, C2: 12) fully generated with flashcards (IPA, definitions, examples), worksheets (with explanations), and mastery games
- ✅ **ES vocabulary track completion:** 77/78 chapters complete (99% — only 1 stub location unknown)
- ✅ **Espanol-en A1 grammar population:** All 25 chapters populated with slides, worksheets, games
- ✅ **Espanol-en A1 writing population:** All 3 chapters populated with slides, worksheets, games
- ✅ **Espanol-en A2–C2 framework creation:** Stub hubs + chapter directories created for all levels, ready for population
- ✅ **Parallel agent work:** 6 concurrent agents worked on content population; all completed successfully without conflicts
- ✅ **Documentation sync:** TECH_DEBT.md, AI_HANDOVER.md, SESSION_CONTEXT.md updated to reflect final state (this session)

**Prior Session (7 June):**
- ✅ **ES A2 vocabulary population:** All 11 chapters fully generated with flashcards (IPA, definitions, examples), worksheets (with explanations), and mastery games
- ✅ **ES A2-B2 grammar population:** All 55 chapters (A2: 19, B1: 19, B2: 18) with 7-slide presentations, worksheets (3-exercise format with explanations), and mastery games. **321 files generated in total.**
- ✅ **Espanol-en A1 vocabulary completion:** All 12 chapters fully populated with IPA transcriptions, Spanish definitions, Web Speech API (es-ES, rate=0.9), and example sentences
- ✅ **Authentication system:** Implemented unified student system with D1 integration — user accounts, bearer token auth, class management, invite codes, role-based access (admin/teacher/student)

**Earlier Sessions (Early June):**
- **Mascot sprite animation (5 June):** 20-commit iterative fix (CSS steps → % bg-position → px offsets → JS frame-cycling). Live on homepage but shipped with 3 `console.log` debug statements + mobile cropping bug.
- **Placement-test-v2 (5 June):** Enhanced level-finder with email capture and skill breakdown; homepage now links only to v2.
- **Animals chapter split (3 June):** `a/a1/vocabulary/animals/` split into separate `flashcards.html` (new template) + `match.html` (new 3-lives double-match game) + `index.html` 4-card hub
- **Builder (`builder.html`):** extended to all content types (lesson, game, worksheet, flashcard, match); French (`fr/`) track support; auto-preview after build
- **Teacher hub & calendar:** Full lesson calendar (D1 sync), student profiles, class management, email capture
- **Content builder tooling:** `scripts/gen_scaffold.py`, `fill_chapter.py`, `content/` modules for content generation and filling
- **Search index:** 424 chapters indexed
- **ES grammar discovery:** 107 `gramatica/` chapters exist across all 6 levels (Spanish-named folder, previously undocumented).

*Last verified/updated 9 June 2026 — Autonomous session: 6 agents, 150+ files, 77/78 ES vocab complete, espanol-en A1 populated, A2–C2 frameworks created*
