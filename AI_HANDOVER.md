# Word Play — AI & Developer Handover

**Read this file first in any new Claude session.**

**Current version:** v103  
**Total HTML pages:** ~822  
**Live URL:** https://delicate-mode-2bce.emi-dom123.workers.dev/  
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

1. Work on branch `claude/github-workflow-setup-98Fbf` (this was force-pushed to become `main`)
2. Push with `git push -u origin <branch>` — Cloudflare Pages auto-deploys `main`
3. Bump `?v=vNN` cache-bust suffix on shared asset URLs whenever `shared/` files change
4. No zip packaging. No `present_files`. Just commit + push.

**Active branch for development:** whatever the session context specifies. When in doubt, check `git branch`.

---

## 3. What Word Play is

A **static** Cambridge English course (A1 to C2) on Cloudflare Pages. Vanilla HTML / CSS / JS. No build system. No backend. All student progress lives in **browser localStorage**.

---

## 4. Content state (v103)

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
Global styles. Key variables: `--amber: #E8A020`, `--paper: #FAFAF8`, `--ink: #1A1A1A`.  
Dark mode via `body.dark`. Header dark: `body.dark .site-header { background: #000000 !important; }`.  
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

## 9. Iron-clad conventions

- **No emojis in UI** — only ◐/◑ for dark mode toggle, ◆ for streak
- **Amber ONLY accent** — `#E8A020` / `var(--amber)`. No navy/teal/gold
- **No Spanish-specific content** in main course
- **No filler** in chat responses
- **Always cache-bust** with `?v=vNN` when touching shared assets
- **Dark mode must work everywhere** — `!important` overrides in CSS where needed
- **Always use deterministic grading** — never ask students to self-grade
- **Always include EXPLANATIONS** in worksheets

---

## 10. Deployment

Push to `main` → Cloudflare Pages auto-deploys (2-3 min). No manual steps needed.

If a visual bug appears after deploy, suspect Cloudflare edge cache — purge via dashboard.

---

## 11. Roadmap (confirmed)

- **Phase 1** — Finish English course (in progress; C2 still needs full enrichment)
- **Phase 2** — Auto-deploy via GitHub ✓ (done)
- **Phase 3** — User accounts (URL token → Cloudflare D1 + Workers)
- **Phase 4** — Spanish-native version at `/es/`
- **Phase 5** — Complete CAE/CPE practice materials, add KET/PET

---

## 12. Known pending items (as of v103)

- A2-C2 vocab flashcards: no audio button, no auto-complete on view-all or match rounds
- C2 grammar: still minimal templates, needs enrichment
- chapter-nav tabs still visible on flashcards/game pages for all levels (slides only are hidden)
- Dashboard link: injected by deck.js (lesson pages) and dark-init.js (all other sub-pages)

---

*Last updated: v103*
