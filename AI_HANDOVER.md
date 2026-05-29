# Word Play — AI & Developer Handover

**Read `CLAUDE.md` first (it holds all the rules), then this file for orientation.**

**Project version marker:** see `version.json`  
**Total HTML pages:** ~1,157  
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

1. Develop on `claude/github-workflow-setup-98Fbf`.
2. Deploy with `git push origin HEAD:main` (Cloudflare Pages auto-deploys `main`), then
   sync the dev branch.
3. Bump the per-file `?v=vNN` suffix only on the shared assets you actually change.
4. No zip packaging. Just commit + push.

---

## 3. What Word Play is

A **static** Cambridge English course (A1 to C2) on Cloudflare Pages. Vanilla HTML / CSS / JS. No build system. No backend. All student progress lives in **browser localStorage**.

---

## 4. Content state

### Grammar — 110 chapters total
| Level | Chapters | Status |
|-------|----------|--------|
| A1    | 25       | Fully enriched |
| A2    | 18       | Fully enriched |
| B1    | 19       | Fully enriched |
| B2    | 20       | Fully enriched |
| C1    | 17       | Mostly done (a few advanced topics minimal) |
| C2    | 11       | Minimal templates — needs enrichment |

### Vocabulary — 53 topics
| Level | Topics | Flashcard template |
|-------|--------|--------------------|
| A1    | 12     | Old (renderCard / STORAGE_KEY) |
| A2    | 6      | New (showCard / MASTERY_KEY) |
| B1    | 11     | New |
| B2    | 16     | New |
| C1    | 7      | New |
| C2    | 7      | New (some minimal) |

All vocab games use 10-item standardised GAME_DATA structure.  
A1 flashcards have audio pronunciation + auto-complete after viewing all cards.  
A1 matching game auto-completes after 5 completed rounds.

### Writing — 21 chapters with auto-graded production tasks

### Exam prep — FCE (B2) full, CAE/CPE strategy + part guides (practice pages = placeholders)

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

```
{band}/{level}/{section}/{slug}/
  flashcards.html   (vocab only)
  slides.html       lesson — needs class="deck-body" on <body>
  worksheet.html    auto-graded practice
  game.html         4-stage mastery game
  printables.html   print-ready A4 (grammar only)
```

Where `band` = `a` (A1/A2), `b` (B1/B2), `c` (C1/C2).

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

- **Phase 1** — Finish English course (in progress; C2 still needs full enrichment)
- **Phase 2** — Auto-deploy via GitHub (done)
- **Phase 3** — User accounts (URL token → Cloudflare D1 + Workers)
- **Phase 4** — Spanish-native version at `/es/` (started — A1 grammar + vocab built)
- **Phase 5** — Complete CAE/CPE practice materials, add KET/PET

---

## 12. Known pending items

- A2-C2 vocab flashcards: no audio button, no auto-complete on view-all or match rounds
- C2 grammar: still minimal templates, needs enrichment
- Dashboard link: injected by deck.js (lesson pages) and dark-init.js (all other sub-pages)

---

## 13. Recent work (week of 26–29 May 2026)

- **Navigation:** site-wide icon-only back arrow in the header (destination = the last
  breadcrumb link); breadcrumbs always run menu → chapter; chapter-nav tab rows now hidden
  on slides/worksheet/game (the chapter hub already links the four parts).
- **Header layout:** brand is absolutely centred (immune to the Dashboard/QR buttons that
  `dark-init.js` injects at runtime); Dark + QR grouped into a right-aligned pill; Dashboard
  link hidden on ≤560px mobile.
- **Visual polish:** warm parchment background (`--paper: #F7F3EE`), inkier card borders,
  section cards adapt between light/dark mode, redundant level-name subtitle removed from
  the six English level hubs.
