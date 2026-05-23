# Word Play — Session Context

**Version:** v100
**Live URL:** `https://delicate-mode-2bce.emi-dom123.workers.dev/`
**Maintainer:** Em — freelance English teacher, Catalunya
**Working method:** Chat → zip → upload to Cloudflare (no local dev)

> **Read AI_HANDOVER.md first** before reading this. That file orients you to who Em is and how the workflow runs. This file is the technical state-of-the-project.

---

## 1. What was just shipped (v90 → v96)

### Grammar enrichment — 100% COMPLETE
All 110 grammar chapters across A1-C2 now have substantive enriched slide decks (6-7 slides each with overview-rows, formula-blocks, panel-pairs, trap-rows, watch-outs, summary-slides with amber CTA). Zero stubs remain.

| Level | Chapters | Status |
|-------|----------|--------|
| A1    | 25       | Complete — includes 7 chapters rebuilt from stubs in v94 |
| A2    | 18       | Complete — includes 3 chapters rebuilt from stubs in v94 |
| B1    | 19       | Complete — 4 chapters use simpler template (acceptable) |
| B2    | 20       | Complete |
| C1    | 17       | Complete — all 17 fully enriched with C1-level content |
| C2    | 11       | Complete — all 11 fully enriched with C2-level content |

### Vocabulary — 53 topics, all standardised
All 53 vocab games have 10+ items in the 7-field format. Total: 534 items. Zero empty games.

### Exam prep — CAE + CPE fully built
- **FCE (B2)** — complete: about, strategy, writing-overview, parts 1-7 (strategy + practice), mocks 1-3
- **CAE (C1)** — complete: about, strategy, writing-overview, mock-1 placeholder, ALL 8 parts have strategy guides + auto-graded practice questions (48 total questions)
- **CPE (C2)** — complete: about, strategy, writing-overview, mock-1 placeholder, ALL 7 parts have strategy guides + auto-graded practice questions (52 total questions)

### Handover docs — all rewritten from scratch in v90
README.md (Em-friendly), AI_HANDOVER.md (full AI orientation), this file.

---

## 2. Content inventory (accurate)

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
index.html, dashboard.html, placement-test.html, progress-certificate.html, 404.html, 6x certificate.html

### Total: ~822 HTML pages

---

## 3. Engine files in `shared/`

```
shared/
  base.css           Layout, variables, header/footer/breadcrumb/nav
  slides.css         Slide deck styles (full dark mode block)
  worksheet.css      Auto-graded practice styles
  game.css           4-stage mastery game styles
  store.js           FCEStore — localStorage wrapper, CHAPTERS registry
  deck.js            Slide navigation, progress bar, completion banner
  worksheet.js       Auto-grading: MCQ + text inputs + explanations
  game.js            4-stage mastery engine
  writing-grader.js  Live writing feedback (regex, no AI)
  sentence-grader.js Regex-based open sentence grader
  dark-init.js       Dark/light toggle + back-to-top button
```

---

## 4. Contracts

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

---

## 5. Design system
Palette: navy #0E1A2B/#1A2A40, ink #1A1A1A, paper #F5EFE0, amber #C9A050, teal #1A7A8A, muted #6B7280.
Dark mode: all CSS files have explicit `!important` overrides. Headings #FFF, body #F0F0F0, strong/b #FFE4A0, CTA buttons keep #1A1A1A text.

---

## 6. Next steps (priority order)

1. **Vocab expansion** — A1/A2 have only 6 topics each (thin vs B1's 11, B2's 16). Add 4-6 topics per level.
2. **KET (A2) + PET (B1) exam prep skeletons** — modelled on FCE/CAE/CPE structure
3. **CAE/CPE mock exams** — full timed Reading & UoE papers (mock-1 pages are currently placeholders)
4. **Game polish** — typed vs MCQ toggle, streak bonuses, audio for IPA
5. **Phase 2** — GitHub → Cloudflare Pages auto-deploy

---

*This file replaces all prior SESSION_CONTEXT.md content. v96.*
