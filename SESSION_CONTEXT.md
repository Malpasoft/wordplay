# Word Play — Session Context

**Project version marker:** see `version.json`
**Live URL:** `https://wordplay-38t.pages.dev`
**Maintainer:** Em — freelance English teacher, Catalunya
**Repo:** `malpasoft/wordplay` on GitHub → auto-deploys to Cloudflare Pages on push to `main`
**Working branch:** `claude/github-workflow-setup-98Fbf`

> **Read CLAUDE.md first (all the rules), then AI_HANDOVER.md (orientation).** This file is
> the deep technical state — JS contracts, shared-engine wiring, and the localStorage schema.

---

## 1. Key architecture notes

### A1 Chapter 1 + Vocab 1 polish

- **Lesson pages (slides.html)**: switched to one-at-a-time swipeable deck (deck.js rewrite). Fixed body background (`var(--paper)`, was broken invalid var). Chapter-nav tab row hidden on lesson pages via slides.css. Dashboard link injected into lesson header via deck.js. All lesson pages now need `class="deck-body"` on `<body>`.
- **Placement test**: fixed MCQ early-submit bug (button type=submit inside form). Added cache-busting.
- **Animals flashcards**: fixed wrong vocabulary data (was food words). Added audio pronunciation button (Web Speech API, no external deps).
- **Animals slides**: fixed orphan JS outside script tags, fixed wrong progress keys.
- **Confetti**: CSS particle animation on lesson complete (deck.js) and game mastery (game.js).
- **Streak badge**: removed emoji. Now shows `◆ N-day streak` with clean amber text.
- **Section card hover**: replaced inline-JS hover on A1 hub page with `.sect-card` CSS class (amber border on hover). Grammar/Vocab/Writing cards now need `class="sect-card"` on `<a>` elements.

### Cache-busting
Each `shared/` asset carries its own independent `?v=vNN` — bump only the files you change.
See CLAUDE.md for the procedure.

---

## 2. Content inventory

### Grammar — 110 chapters, all enriched
Every chapter has: slides.html (lesson), worksheet.html (auto-graded), game.html (4-stage mastery), printables.html

### Vocab — 53 topics
| Level | Topics |
|-------|--------|
| A1    | 6 |
| A2    | 6 |
| B1    | 11 |
| B2    | 16 |
| C1    | 7 |
| C2    | 7 |

### Writing — 21 chapters with auto-graders
### Exam prep
| Exam | Level | Parts with practice | Total practice Qs |
|------|-------|--------------------|--------------------|
| FCE  | B2    | 7/7                | ~40                |
| CAE  | C1    | 8/8                | 48                 |
| CPE  | C2    | 7/7                | 52                 |

### Special pages
- `index.html` — homepage with level grid, streak badge, onboarding modal
- `dashboard.html` — student progress: XP, stats, radar chart, level tiles, activity pillars
- `placement-test.html` — 24-question level finder
- `progress-certificate.html` — printable certificate generator
- `404.html`, 6x `certificate.html` (one per level)

### Total: ~1,157 HTML pages

---

## 3. Engine files in `shared/`

```
shared/
  base.css           Layout, variables, header/footer/breadcrumb/nav, .sect-card
  slides.css         Slide deck styles — body must have class="deck-body"
  worksheet.css      Auto-graded practice styles
  game.css           4-stage mastery game styles
  store.js           FCEStore — localStorage wrapper, CHAPTERS registry, streak tracking
  deck.js            Slide nav, confetti on complete, Dashboard header injection
  worksheet.js       Auto-grading: MCQ + text inputs + explanations
  game.js            4-stage mastery engine, confetti on full mastery
  writing-grader.js  Live writing feedback (regex, no AI)
  sentence-grader.js Regex-based open sentence grader
  dark-init.js       Dark/light toggle + back-to-top button
```

---

## 4. Contracts

### Lesson pages (slides.html) contract
```html
<body class="deck-body">  ← required for correct background
<script>
window.LEVEL = "a1";
window.CHAPTER_ID = "animals";
</script>
<script src="../../../../shared/store.js?v=vNN"></script>
<script src="../../../../shared/deck.js?v=vNN"></script>
```
(Use the current `?v=` value for each file — see the cache-busting note above.)
deck.js auto-injects the Dashboard header button and confetti on completion.

### Worksheet contract
```html
<script>
window.CHAPTER_ID = "slug";
window.LEVEL = "a2";
window.TOTAL_POINTS = N;
window.ANSWERS = { q1: "answer", ... };
window.EXPLANATIONS = { q1: "reason", ... };
</script>
```

### Game contract
```html
<script>
window.GAME_DATA = {
  chapterId: "slug", level: "a2", title: "Title",
  storageKey: "wordplay_game_a2_slug",
  items: [{ id, term, meaning, synonym, example, completion, answer }]
};
</script>
```

### Vocab flashcards contract (animals pattern)
```js
var WORDS = [{ word, ipa, definition, example }, ...]; // 10 items
var STORAGE_KEY = 'wordplay_vocab_a1_{topic}_mastered';
// Progress key in wordplay_progress: pd['a1']['vocab_mastered_{topic}']
```
- flashcards.html has 3 modes: Flashcards (flip card + audio), Match game, Word list
- game.html is the separate 4-stage mastery game (different from flashcards.html)

---

## 5. Design system

The full palette and design rules live in **CLAUDE.md** (single source of truth). For
reference, the `base.css :root` palette is:
- `--ink: #1A1A1A` / dark `#F0F0F0`
- `--paper: #F7F3EE` / dark `#0E0E0E`
- `--amber: #B8860B` / dark `#C9A050` — the only accent colour (always via `var(--amber)`)
- `--muted: #9A9A9A`, `--hairline: #E5E5E5`, `--green: #2E7D52`, `--red: #C0392B`

---

## 6. localStorage key structure

```
wordplay_progress: {
  streak: N,
  a1: {
    'slides_{chapterId}': { done: true, date: ISO },        // lesson complete
    '{chapterId}': { pct: 85, done: true },                 // worksheet score
    'wordplay_game_{chapterId}': { pct: 90 },               // game score
    'vocab_mastered_{topic}': { done: true, date: ISO },    // flashcard mastery
  }
}
```

---

## 7. Next steps (priority order)

1. **A1 full audit** — Polish remaining A1 grammar/vocab chapters using animals+to-be as template
2. **Vocab expansion** — A1/A2 have only 6 topics each; add 4-6 topics per level
3. **KET (A2) + PET (B1) exam prep skeletons** — modelled on FCE/CAE/CPE
4. **CAE/CPE mock exams** — full timed papers (currently placeholders)
5. **Spanish version** — Once A1 polish is complete, use as base

---

*Updated May 2026 — navigation, header layout, and visual-polish pass; docs refresh.*
