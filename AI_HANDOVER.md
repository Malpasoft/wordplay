# Word Play — AI & Developer Handover

**Read `CLAUDE.md` first (it holds all the rules), then this file for orientation.**

**Project version marker:** see `version.json`  
**Total HTML pages:** ~2,187  
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
- Spanish-specific content mixed into the main course (reserved for Phase 4 `/es/`)

---

## 2. How a session works now

The project is on GitHub. Claude Code is used in remote sessions with direct push access.
The full git/deploy/cache-bust rules are in **CLAUDE.md** — in short:

1. Develop on `claude/website-design-token-optimization-1ZNUG`.
2. Deploy with `git push origin HEAD:main` (Cloudflare Pages auto-deploys `main`), then
   sync the dev branch.
3. Bump the per-file `?v=vNN` suffix only on the shared assets you actually change.
4. No zip packaging. Just commit + push.

---

## 3. What Word Play is

A **static** Cambridge English course (A1 to C2) on Cloudflare Pages. Vanilla HTML / CSS / JS. No build system. No backend. All student progress lives in **browser localStorage**.

---

## 4. Content state

### English track — 213 chapters total

**Grammar — 110 chapters**
| Level | Chapters | Notes |
|-------|----------|-------|
| A1    | 24       | Fully enriched |
| A2    | 19       | Fully enriched (indirect-questions added) |
| B1    | 21       | Fully enriched (wish-if-only, passive-variations added) |
| B2    | 18       | Mostly enriched; a few advanced topics minimal |
| C1    | 17       | Scaffolded; needs enrichment |
| C2    | 11       | Scaffolded; needs enrichment |

**Vocabulary — 77 topics**
| Level | Topics | Template |
|-------|--------|----------|
| A1    | 12     | Old (renderCard / STORAGE_KEY) |
| A2    | 12     | New (showCard / MASTERY_KEY) |
| B1    | 11     | New |
| B2    | 16     | New |
| C1    | 14     | New (expanded from 7 to 14 this session) |
| C2    | 12     | New (expanded from 7 to 12 this session) |

All vocab games use 10-item standardised GAME_DATA structure.  
A1 flashcards: audio pronunciation + auto-complete after all cards viewed.  
A2–C2 flashcards: no audio, no auto-complete (known pending item).

**Writing — 26 chapters**
| Level | Chapters |
|-------|----------|
| A1    | 3 |
| A2    | 3 |
| B1    | 3 |
| B2    | 5 |
| C1    | 6 |
| C2    | 6 |

**Exam prep** — FCE (B2) full 7-part coverage; CAE (C1) and CPE (C2) strategy + part guides. Mock papers are placeholders.

---

### Spanish track (`/es/`) — 210 chapters total, all 6 levels live

Built in parallel to the English track; mirrors English curriculum with Spanish-native explanations and interference-error slides.

**Grammar — 107 chapters**
| Level | Chapters | Folder |
|-------|----------|--------|
| A1    | 24       | `es/a1/gramatica/` |
| A2    | 18       | `es/a2/gramatica/` |
| B1    | 19       | `es/b1/gramatica/` |
| B2    | 18       | `es/b2/gramatica/` |
| C1    | 17       | `es/c1/gramatica/` |
| C2    | 11       | `es/c2/gramatica/` |

**Vocabulary — 77 topics** (same counts as English per level)  
**Writing — 26 chapters** (same counts as English per level)

**Content fill status:** 4 ES A1 grammar chapters have full authored content (present-continuous, going-to-future, question-words, imperatives). All other Spanish chapters are scaffolded with placeholder HTML — the `scripts/fill_chapter.py` tooling and content modules in `scripts/content/` are ready for the remaining fill passes.

---

## 5. The shared engines in `shared/`

No dependencies, no imports. Pages link with `?v=vNN` cache-busting.

### `base.css`
Global styles. Key variables: `--amber` (`#B8860B` / `#C9A050` dark), `--paper: #F7F3EE`
(warm parchment), `--ink: #1A1A1A`. Always use `var(--amber)`, never a literal hex.  
Dark mode via `body.dark`.  
`.ch-card` = vocab/grammar topic cards with amber hover.  
`.sect-card` = dark section cards on level hub pages with amber hover border.

### `slides.css`
Lesson page styles. Requires `class="deck-body"` on `<body>`. Background: `var(--paper)`.  
`.chapter-nav { display: none !important; }` — hides nav tabs on lesson pages.

### `deck.js`
Slide navigation + completion tracking. Injects Dashboard link in header.  
Fires confetti on lesson complete. Reads `window.LEVEL` + `window.CHAPTER_ID`.

### `game.css` + `game.js`
4-stage mastery game (recognition → meaning → context → production).  
Fires confetti on game completion. Reads `window.GAME_DATA`.

### `worksheet.js`
Auto-grader. Reads `window.ANSWERS`, `window.EXPLANATIONS`, `window.TOTAL_POINTS`.

### `store.js`
Wraps localStorage. `FCEStore.saveResult(...)`, `FCEStore.getLevel(level)`, etc.

### `dark-init.js`
Dark/light toggle. Also injects Dashboard link on all sub-pages (skips homepage + dashboard).  
Also injects floating back-to-top button.

---

## 6. Two flashcard templates — CRITICAL

**Old template (A1 only):**
```js
var STORAGE_KEY = 'wordplay_vocab_a1_{slug}_mastered';
var WORDS = [{ word, definition, example, pronunciation }, ...];
function renderCard(idx) { ... fcSeen.add(idx); ... }
function markMastered() { ... }
```
Completion: auto-triggers `markMastered()` after all cards viewed + after 5 match rounds.

**New template (A2-C2):**
```js
var MASTERY_KEY = 'wordplay_vocab_{level}_{slug}_mastered';
var SLUG = '...'; var LEVEL = '...';
var WORDS = [{ word, def, ex, ipa }, ...];
function showCard(idx) { ... }
```
A2-C2 flashcards do NOT yet have audio or auto-complete. This is a known pending item.

---

## 7. Progress / localStorage schema

```
wordplay_progress = {
  a1: {
    "vocab_mastered_{slug}":      { done: true, date: "ISO" },
    "wordplay_game_{slug}":       { pct: 100, mastered: 10, total: 10 },
    "wordplay_game_a1_{slug}":    { saved game state },
    "slides_{slug}":              { done: true, date: "ISO" },
    "{slug}":                     { score, total, pct, ... }  ← worksheet results
  },
  a2: { ... }, ...
}
wordplay_dark = "1" | "0"
wordplay_student_name = "Maria"
```

Dashboard reads `lv['vocab_mastered_' + slug].done` to count vocab mastered per level.

---

## 8. Standard file structure

**English chapters:**
```
{band}/{level}/{section}/{slug}/
  flashcards.html   (vocab only)
  slides.html       lesson — needs class="deck-body" on <body>
  worksheet.html    auto-graded practice
  game.html         4-stage mastery game
  printables.html   print-ready A4 (grammar only)
```
Where `band` = `a` (A1/A2), `b` (B1/B2), `c` (C1/C2).

**Spanish chapters:**
```
es/{level}/{section}/{slug}/
  slides.html       lesson
  worksheet.html    auto-graded practice
  game.html         4-stage mastery game
  printables.html   print-ready A4
  (vocab: flashcards.html instead of printables)
```
Note: Spanish grammar folder uses Spanish spelling — `gramatica/`. Vocabulary and writing folders keep English spelling (`vocabulary/`, `writing/`) to match the existing site structure.

---

## 9. Conventions

All design, git, cache-bust, and pedagogy rules live in **CLAUDE.md** — read it. The only
handover-specific notes:

- **No Spanish-specific content in the main English course** — the Spanish course is a
  separate parallel site under `/es/`.
- **No filler in chat responses** — Em is direct and values doing over explaining.

---

## 10. Deployment

Push to `main` → Cloudflare Pages auto-deploys (2-3 min). No manual steps needed.

If a visual bug appears after deploy, suspect Cloudflare edge cache — purge via dashboard.

---

## 11. Roadmap (confirmed)

- **Phase 1** — Finish English course (in progress; B2–C2 grammar still needs enrichment)
- **Phase 2** — Auto-deploy via GitHub (done)
- **Phase 3** — User accounts (URL token → Cloudflare D1 + Workers)
- **Phase 4** — Spanish-native version at `/es/` (**scaffolding complete** — all 6 levels, 3 sections, 210 chapters built; content fill in progress starting from ES A1 grammar)
- **Phase 5** — Complete CAE/CPE practice materials, add KET/PET mock papers

---

## 12. Known pending items

- A2–C2 vocab flashcards: no audio button, no auto-complete on view-all or match rounds
- B2–C2 English grammar: scaffolded but needs enrichment
- Spanish A1–C2 chapters: scaffolded with placeholder HTML; content fill in progress (see `scripts/fill_chapter.py`)
- Dashboard link: injected by `deck.js` (lesson pages) and `dark-init.js` (all other sub-pages)
- KET/PET exam prep: not yet built

---

## 13. Recent work (May 2026)

**Week of 26–29 May — Visual polish + navigation**
- Site-wide icon-only back arrow; breadcrumbs always run menu → chapter; chapter-nav tab row hidden on slides/worksheet/game.
- Brand absolutely centred in header; Dark + QR grouped right; Dashboard link hidden on mobile.
- Warm parchment background (`--paper: #F7F3EE`), inkier card borders, section cards adapt light/dark.

**Week of 30–31 May — Full syllabus expansion**
- **English gaps filled:** A2 `indirect-questions` (Ch 19), B1 `wish-if-only` (Ch 20) + `passive-variations` (Ch 21).
- **English vocabulary expanded:** C1 7 → 14 topics, C2 7 → 12 topics (12 new topics total).
- **Spanish track built from scratch:** complete scaffold for all 6 levels × 3 sections = 210 chapters. `gen_chapter.py` extended to handle Spanish folder conventions (`gramatica/` vs `vocabulary/`/`writing/`). Level hubs and section index pages generated for every level. All 6 Spanish levels activated in `es/index.html`.
- **Spanish C1/C2 vocabulary** mirrored from English (same 12 new topics).
- **Content fill tooling created:** `scripts/fill_chapter.py` (idempotent anchor-based filler), authored content modules in `scripts/content/`. First 4 ES A1 grammar chapters filled with complete bilingual content: present-continuous, going-to-future, question-words, imperatives (7 slides + 14 graded questions + 10 game items each).
- Search index regenerated: 424 entries.
