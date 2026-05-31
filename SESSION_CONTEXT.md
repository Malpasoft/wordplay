# Word Play — Session Context

**Project version marker:** see `version.json`
**Live URL:** `https://wordplay-38t.pages.dev`
**Maintainer:** Em — freelance English teacher, Catalunya
**Repo:** `malpasoft/wordplay` on GitHub → auto-deploys to Cloudflare Pages on push to `main`
**Working branch:** `claude/website-design-token-optimization-1ZNUG`

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

### English track — 213 chapters

**Grammar — 110 chapters**
| Level | Chapters | Notes |
|-------|----------|-------|
| A1    | 24       | Fully enriched |
| A2    | 19       | Fully enriched |
| B1    | 21       | Fully enriched |
| B2    | 18       | Partially enriched |
| C1    | 17       | Scaffolded |
| C2    | 11       | Scaffolded |

**Vocabulary — 77 topics**
| Level | Topics | Template |
|-------|--------|----------|
| A1    | 12     | Old (renderCard / STORAGE_KEY) |
| A2    | 12     | New (showCard / MASTERY_KEY) |
| B1    | 11     | New |
| B2    | 16     | New |
| C1    | 14     | New |
| C2    | 12     | New |

**Writing — 26 chapters** (A1/A2/B1: 3 each; B2: 5; C1/C2: 6 each)

**Exam prep**
| Exam | Level | Status |
|------|-------|--------|
| FCE  | B2    | Full — 7 parts + 2 mock papers |
| CAE  | C1    | Strategy + 8 part guides (practice = placeholders) |
| CPE  | C2    | Strategy + 7 part guides (practice = placeholders) |

### Spanish track (`/es/`) — 210 chapters

**All 6 levels scaffolded** (A1–C2), all 3 sections (gramatica / vocabulary / writing).
Grammar per level: A1=24, A2=18, B1=19, B2=18, C1=17, C2=11.
Vocab per level: A1=12, A2=12, B1=11, B2=16, C1=14, C2=12.
Writing per level: A1=3, A2=3, B1=3, B2=5, C1=6, C2=6.

Content fill status: 4 ES A1 grammar chapters filled (present-continuous, going-to-future, question-words, imperatives). All others are scaffold placeholders.

**Fill tooling:**
- `scripts/fill_chapter.py` — idempotent anchor-based filler for slides/worksheet/game
- `scripts/content/es_a1_g_batch1.py` — PC + going-to-future content dicts
- `scripts/content/es_a1_g_batch2.py` — question-words + imperatives content dicts

### Special pages
- `index.html` — homepage with level grid, streak badge, onboarding modal
- `dashboard.html` — student progress: XP, stats, radar chart, level tiles, activity pillars
- `placement-test.html` — 24-question level finder
- `progress-certificate.html` — printable certificate generator
- `404.html`, 6× `certificate.html` (one per level)

### Total: ~2,187 HTML pages · Search index: 424 entries

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

1. **ES A1 content fill** — remaining 20 ES A1 grammar chapters + 12 vocab topics need fill pass using `fill_chapter.py`
2. **ES A2–C2 content fill** — ~200 chapters still placeholder; generate content batches with background agents and run filler
3. **A2–C2 vocab audio** — add audio button and auto-complete to A2–C2 flashcard template (known gap)
4. **B2–C2 English grammar enrichment** — currently scaffolded only
5. **KET (A2) + PET (B1) exam prep skeletons** — modelled on FCE/CAE/CPE
6. **CAE/CPE mock exams** — full timed papers (currently placeholders)

---

*Updated 31 May 2026 — full Spanish track scaffold, English vocab/grammar gap fill, content tooling added.*
