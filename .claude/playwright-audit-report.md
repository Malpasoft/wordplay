# Playwright Audit Report — 2026-05-28

## Summary
- **Pages audited:** 20 (representative sample across all 7 levels + placement test)
- **Passed:** 14
- **Errors:** 3 (2 open, 1 fixed during audit)
- **Bugs:** 4 total (P0: 0 · P1: 3 · P2: 1)
- **Fixed during audit:** BUG-004

---

## What was tested

| Level | Pages tested | Status |
|-------|-------------|--------|
| Placement test | placement-test.html | PASS |
| A1 grammar | adjectives-basic: worksheet, game, slides | 2 errors (BUG-001, BUG-002, BUG-003) |
| A2 grammar | comparatives-basic: worksheet, game | PASS |
| B1 grammar | present-perfect: worksheet, game | PASS |
| B2 vocabulary | environment-climate: game | PASS |
| C1 grammar | advanced-tenses: worksheet | PASS |
| C2 grammar | conditionals-mastery: game | PASS |
| ES/A1 gramática | artículos: slides, worksheet, game | PASS |
| ES/A1 gramática | pronombres: game | PASS |
| ES/A1 gramática | have-got: game | FIXED (BUG-004) |
| ES/A1 vocabulario | daily-routines/index.html | PASS |
| ES/A1 vocabulario | food-and-drink/index.html | PASS |

---

## Bugs

### BUG-001 · P1 · pedagogy · OPEN
**Scope:** 13 A1 grammar worksheets (systemic)
**Description:** Exercise 1 multiple-choice questions (keys `e1q1`–`e1q8`) have no entries in `window.EXPLANATIONS`. When a student clicks a wrong answer, feedback shows only "Correct answer: X" with no explanation. Violates the pedagogy rule: *every worksheet question must have an explanation*.

**Repro:** Open `a/a1/grammar/adjectives-basic/worksheet.html` → click a wrong answer in Exercise 1 → feedback shows "Correct answer: blue" with no explanation text.

**Screenshot:** `.claude/playwright-audit-screenshots/` (see placement-test.png for reference)

**Suggested fix:** Add `e1q1`–`e1q8` keys to `window.EXPLANATIONS` in each affected worksheet. Example for adjectives-basic:
```js
"e1q1": "Adjectives NEVER add -s: two <strong>blue</strong> eyes (not blues).",
"e1q2": "Adjective before noun: a <strong>small</strong> cat (not smally).",
```
Run `scripts/pedagogy_check.py` after fixing to confirm 0 failures.

---

### BUG-002 · P1 · layout · OPEN
**Scope:** All `game.html` pages (systemic)
**Description:** The `.game-term` element (the word being tested) starts at `top: 12px` in the viewport, but the sticky navigation bar extends to `bottom: 70px`. The word being answered for is ~80% hidden behind the nav when the game play screen loads.

**Repro:** Open any `game.html` → click Start → the word/term at the top of the play card is obscured by the sticky header.

**Screenshot:** `.claude/playwright-audit-screenshots/a1-game-full.png`

**Suggested fix:** Add `scroll-padding-top` or `padding-top` to the `.game-play` or `.game-wrap` container equal to the sticky nav height. One option:
```css
/* In game.css */
.game-wrap {
  padding-top: calc(var(--nav-height, 70px) + 12px);
}
```
Or programmatically scroll to the play area after starting:
```js
// After transitioning to gamePlay screen
gamePlay.scrollIntoView({ behavior: 'smooth', block: 'start' });
```

---

### BUG-003 · P2 · design-system · OPEN
**Scope:** 19 slides pages across A1–C2 grammar
**Description:** Note panels in slides use `⚠` (U+26A0, WARNING SIGN). CLAUDE.md design system bans all emoji and Unicode symbols in content and UI — only `◐ ◑ ◆` are permitted.

**Repro:** Open `a/a1/grammar/adjectives-basic/slides.html` → scroll to a "Note" box → see `⚠ Note:` label.

**Screenshot:** `.claude/playwright-audit-screenshots/a1-slides.png`

**Suggested fix:** Replace `⚠` with a text label. Options:
```html
<!-- Option A: plain text -->
<div class="deck-note"><strong>Note:</strong> In Spanish…</div>

<!-- Option B: CSS ::before pseudo-element -->
/* deck-note::before { content: "Note — "; font-weight: 700; } */
```
Run: `grep -rl "⚠" a/ b/ c/ --include="*.html" | wc -l` → should go to 0.

---

### BUG-004 · P1 · js-error · FIXED ✓
**Scope:** `es/a1/gramatica/have-got/game.html`
**Description:** Cherry-picked file had only `LEVEL`, `CHAPTER_ID`, `STORAGE_KEY` defined — `window.GAME_DATA` was completely absent. `game.js` logged `GAME_DATA not defined` and no terms could be played.

**Fix applied:** Added `window.GAME_DATA` with 10 items covering have got affirmative/negative/question forms, contractions, short answers, and the age/state "trap" (must use *to be*, not *have got*). Verified: game loads and plays correctly.

---

## Observations (not bugs)

- **Placement test dark mode:** Card background correctly dark (`rgb(30,30,30)`); option buttons use light paper colour that creates good contrast. ✓
- **C2 game structure:** Uses different CSS class names (no `.gp-badge`) than A1–B2, but content is identical. Stage badge, term, and options all render. ✓
- **ES/A1 Spanish pages:** All 3 newly cherry-picked chapters (artículos, pronombres, have-got) render with correct Spanish UI labels, amber highlighting, and no JS errors. The slides for artículos are particularly well-done.
- **Game play counter:** C2 game shows `0 / 5` (5 items); A1–B1 games show `0 / 10`. Item counts vary intentionally by chapter size.
- **Dark mode:** Tested on placement test and A1 slides — both look correct with light text on dark backgrounds.

---

## Checkpoint
State saved to `.claude/playwright-audit-state.json`. To resume and extend coverage:
```
/playwright-audit
```
The agent will skip the 20 already-audited pages and continue from where it left off.
