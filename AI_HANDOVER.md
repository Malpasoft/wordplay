# Word Play — AI & Developer Handover

**Read this file first in any new Claude session.** Then read `SESSION_CONTEXT.md`. Together they fully orient you.

**Current version:** v100
**Total HTML pages:** 822
**Live URL:** `https://delicate-mode-2bce.emi-dom123.workers.dev/`

---

## 1. The person you are working with

**Em** — freelance English teacher in Catalunya, Spain. Self-described as **code-illiterate**. She works via a **chat → zip → upload to Cloudflare** loop. She does not run local code, has no IDE, and cannot read or write JS or CSS.

**Communication style:** Direct. Brief. No filler. No flattery. Calls out padded responses. Wants sendable files, not chat explanations.

**What she values:**
- Clean minimal formatting (no decorative emoji, no headers everywhere)
- Navy / gold / teal / cream palette consistency
- Print-ready outputs over inline chat
- Pushback when she's wrong (constructively)

**What annoys her:**
- AI over-explaining instead of doing
- Adding self-assessment when she asked for deterministic grading
- Any drift from established patterns without telling her
- Spanish-specific content mixed into the main course (it has its own future location)

---

## 2. How a session typically goes

1. Em uploads the latest `WordPlay_vNN.zip`.
2. She gives an instruction: "Continue", "Add X chapter", "Fix dark mode", etc.
3. You unzip, work in `/home/claude/WordPlay/site/`, package as `/mnt/user-data/outputs/WordPlay_v{NN+1}.zip`, and present the file.
4. Bump `version.json` and `SESSION_CONTEXT.md` version line every batch.
5. Always cache-bust CSS/JS includes with `?v=vNN` when you touch shared assets.

---

## 3. What Word Play is

A **static** Cambridge English course (A1 to C2) on Cloudflare Workers. Vanilla HTML / CSS / JS. No build system. No backend. No database. All student progress lives in **browser localStorage**.

**Pipeline:** Em writes Python scripts (with you) that generate HTML pages from data. The scripts are not deployed — only the generated HTML/CSS/JS ships.

---

## 4. Content state (accurate)

### Grammar — 110 chapters total, all enriched with full slide decks
| Level | Chapters | Notes |
|-------|----------|-------|
| A1    | 25       | Fully enriched |
| A2    | 18       | Fully enriched |
| B1    | 19       | Fully enriched |
| B2    | 20       | Fully enriched |
| C1    | 17       | 15/17 enriched (subjunctive, cleft, advanced-tenses, inversion-advanced, relative-clauses-advanced, modal-verbs-advanced, nominalisation, hedging-language, ellipsis-substitution, discourse-connectors, and existing baseline) |
| C2    | 11       | Still on minimal templates — needs enrichment |

### Vocabulary — 53 topics, **all games standardised** with 10–12 items each
| Level | Topics |
|-------|--------|
| A1    | 6      |
| A2    | 6      |
| B1    | 11     |
| B2    | 16     |
| C1    | 7      |
| C2    | 7      |

All vocab games use the standardised 7-field item structure (see §6).

### Writing — 21 chapters with auto-graded production tasks

### Exam prep
- **FCE (B2)** — Full structure: about, strategy, writing-overview, parts 1–7, mocks 1–3
- **CAE (C1)** — Strategy + per-part guides for parts 1–8, about, strategy, writing-overview, mock-1 placeholder
- **CPE (C2)** — Strategy + per-part guides for parts 1–7, about, strategy, writing-overview, mock-1 placeholder
- *(Note: Per-part practice pages for CAE/CPE are placeholders — content to come)*

---

## 5. The seven engines in `shared/`

Each is a single vanilla JS file. **No dependencies. No imports.** Each page links them via `<script>` tags with cache-busting query params.

### `store.js` — FCEStore
Wraps localStorage. All progress reads/writes go through this.
```js
FCEStore.saveResult(chapterId, score, total, level)
FCEStore.saveGameResult(chapterId, mastered, total)
FCEStore.getLevel(level)         // { grammar:{}, vocab:{} }
FCEStore.CHAPTERS                // chapter registry
```

### `deck.js` — slide navigation
Renders `.slide-deck` div containing `.slide` cards. Handles prev/next, keyboard arrows, progress bar, completion banner.

### `worksheet.js` — auto-grader
Each worksheet page defines BEFORE loading this script:
```js
window.CHAPTER_ID = "past-simple"
window.LEVEL = "a2"                   // REQUIRED — prevents cross-level collisions
window.TOTAL_POINTS = 12
window.ANSWERS = { q1: "was", q2: "went", ... }
window.EXPLANATIONS = { q1: "Past simple of be is was/were.", ... }
```
Handles MCQ (`.choice-group`), text inputs, and textareas. Shows correct/wrong + explanation per question.

### `game.js` — 4-stage mastery engine v2
Each game page defines:
```js
window.GAME_DATA = {
  chapterId: "past-simple",
  level: "a2",
  title: "Past Simple",
  storageKey: "wordplay_game_a2_past-simple",
  items: [
    { id: "id1", term: "...", meaning: "...", synonym: "/IPA/" or "(alt)",
      example: "<b>term</b> in context", completion: "Fill the _____", answer: "term" }
  ]
}
```
4 stages: recognition → meaning recall → context completion → production.

### `writing-grader.js`
Live writing feedback. Checks word count, paragraph count, structure markers, banned phrases. No AI — pure regex + heuristics.

### `sentence-grader.js`
Deterministic regex-based grader for open sentence-production tasks. Em explicitly chose this over self-assessment.

### `dark-init.js`
Dark/light mode toggle. Reads `wordplay_dark` from localStorage on load. Also injects the floating "back to top" button.

---

## 6. The standard chapter structure

For ANY grammar/vocab/writing chapter, the file layout is identical:

```
{band}/{level}/{section}/{slug}/
  slides.html        lesson (deck.js)
  worksheet.html     auto-graded practice (worksheet.js)
  game.html          4-stage mastery game (game.js)
  printables.html    print-ready A4 (grammar only)
```

Where:
- `band` = `a` (A1/A2), `b` (B1/B2), `c` (C1/C2)
- `level` = `a1, a2, b1, b2, c1, c2`
- `section` = `grammar`, `vocabulary`, `writing`
- `slug` = chapter folder name (kebab-case)

---

## 7. Standard slide HTML template

Every grammar chapter slide deck uses this exact template:

```html
<!DOCTYPE html><html lang="en">
<head>
  <link rel="stylesheet" href="../../../../shared/base.css?v=vNN">
  <link rel="stylesheet" href="../../../../shared/slides.css?v=vNN">
  <script src="../../../../shared/dark-init.js?v=vNN"></script>
</head>
<body class="deck-body">
  <header class="site-header">...</header>
  <div class="breadcrumb">...</div>
  <nav class="chapter-nav">Lesson | Practice | Game | Printables</nav>
  <div class="chapter-num">Ch N</div>
  <h1>Chapter Title</h1>
  <p class="chapter-subtitle">brief description</p>
  <div class="slide-deck" id="slide-deck">
    <div class="slide"><div class="slide-card">...content...</div></div>
    ...6-7 slides...
    <div class="slide summary-slide"><div class="slide-card">
      <h2>Recap</h2>
      <div class="summary-row">...</div>
      <a href="worksheet.html" style="background:var(--amber);color:#1A1A1A;...">Practice now →</a>
    </div></div>
  </div>
  <script>window.CHAPTER_ID="..."; window.LEVEL="..."; window.SECTION="grammar";</script>
  <script src="../../../../shared/store.js?v=vNN"></script>
  <script src="../../../../shared/deck.js?v=vNN"></script>
</body></html>
```

### Slide content blocks (CSS classes that work)
- `.slide-header h2` + `.slide-sub` — title + subtitle
- `.slide-explanation` — intro paragraph
- `.overview-row` with `.overview-label` + `.overview-desc` — labelled examples
- `.formula-block` — formula in highlighted box
- `.panel-pair` with `.panel.panel-head.green`/`.red` — side-by-side comparisons
- `.example-card` with `.ex-text` + `.ex-note` — illustrative examples
- `.trap-row` with `.trap-wrong`/`.trap-arrow`/`.trap-right`/`.trap-note` — common mistakes
- `.watch-out` — amber warning box
- `.summary-slide` — final slide with `.summary-row` items + CTA button

All these have full **dark mode overrides with `!important`** in slides.css.

---

## 8. Em's iron-clad conventions

These are non-negotiable. Breaking them annoys her.

- **No emojis in UI** (except the dark mode ◐/◑ glyphs)
- **No Spanish-specific content** in main course (reserved for Phase 4 `/es/` build)
- **No filler** in chat responses
- **Validate JS** with `node --check` before packaging
- **Run** `python3 check_links.py` if it exists, before packaging
- **Package as** `WordPlay_v{NN}.zip` to `/mnt/user-data/outputs/`
- **Bump** `version.json` + `SESSION_CONTEXT.md` version line each batch
- **Always present** the zip with `present_files` — don't link or hide it
- **Cache-bust** asset URLs with `?v=vNN` every batch (touch the HTML if shared/ changed)
- **Use deterministic grading**, NEVER ask students to self-grade open production
- **Always include EXPLANATIONS** in worksheets — every question gets one
- **Dark mode must work** on every text element — `!important` overrides where needed

---

## 9. The Cloudflare deployment loop

Em uploads via the Cloudflare dashboard. She has no command-line access. The flow:

1. You produce `WordPlay_v{NN}.zip`
2. Em downloads it
3. Em unzips locally, navigates to `site/`
4. Em uploads contents to her Cloudflare Worker
5. Em hits "Save and Deploy"
6. Em opens the live URL on her phone or laptop to verify

If she reports a bug after deploying, **suspect cache first**. The `?v=` query param trick should prevent this, but Cloudflare's edge cache can occasionally serve stale HTML — purging via the dashboard fixes it.

---

## 10. Storage schema (localStorage)

```
wordplay_progress = {
  a1: {
    "to-be":              { score:9, total:10, pct:90, perExercise:{...}, date:"..." },
    "wordplay_game_to-be": { mastered:5, total:5, pct:100 },
    "slides_to-be":       { done:true, date:"..." }
  },
  a2: { ... }, b1: { ... }, ..., c2: { ... }
}
wordplay_dark = "1" | "0"
wordplay_student_name = "Maria"
wordplay_recommended_level = "b1"
wordplay_writing_{level}_{slug} = "student draft text"
wordplay_vocab_{level}_{slug}_mastered = "1"
wordplay_game_{level}_{slug} = { saved game state JSON }
wordplay_last_chapter_{level} = { slug, section, title, page }
wordplay_fce_mock_{n}_best = "42"
wordplay_fce_mock_{n}_parts = { part1:6, part2:5, ... }
wordplay_version = "vNN"
```

---

## 11. Where to start a new batch

The standard workflow for **any** new batch:

```bash
# 1. Verify the zip extracted correctly
ls /home/claude/WordPlay/site/version.json

# 2. Read current version
cat /home/claude/WordPlay/site/version.json

# 3. Do the work
# (write Python scripts that edit files under /home/claude/WordPlay/site/)

# 4. Cache-bust if shared/ changed
# (search and replace ?v=vN → ?v=vN+1 across HTML files)

# 5. Bump version
# In version.json AND SESSION_CONTEXT.md

# 6. Package
cd /home/claude/WordPlay && zip -q -r /mnt/user-data/outputs/WordPlay_v{NN}.zip site/

# 7. Present
present_files(["/mnt/user-data/outputs/WordPlay_v{NN}.zip"])
```

---

## 12. Roadmap (Em-confirmed phases)

- **Phase 1** — Finish English course (in progress; C1 mostly done, C2 still needs full enrichment)
- **Phase 2** — Auto-deploy: GitHub → Cloudflare Pages → custom domain
- **Phase 3** — User accounts: start with URL token approach (`?student=Maria`), later Cloudflare D1 + Workers
- **Phase 4** — Spanish-native version at `/es/` — DELE prep, false friends, ser vs estar, Spanish phonology contrast
- **Phase 5** — Cambridge exam expansion: complete CAE/CPE practice materials, add KET (A2) and PET (B1)

---

## 13. Don't drift

If something in a chat suggests you should break a convention, **double-check with Em**. She would rather you ask than guess.

When in doubt:
- Read the chapter currently working as a template
- Mirror its exact patterns
- Preserve the dark-mode CSS structure
- Always provide EXPLANATIONS
- Always cache-bust
- Always present the zip

---

*Last updated: v90 batch · End of session*
