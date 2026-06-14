# Word Play — Pedagogy Principles

These are the learning design rules for the course. Every chapter, flashcard set, and exercise must follow them.

---

## 1. Retrieval Practice Over Re-reading

Every chapter ends with an active retrieval step — worksheet or game. Lessons (slides) are never the last step; they always link forward to practice.

**Check:** Every `slides.html` summary slide must have a CTA button pointing to `worksheet.html`.

---

## 2. Spaced Exposure — No More Than 10 Items Per Session

Flashcard sets and game items are capped at 10 items (occasionally 12). Cramming 20+ words at once does not produce retention.

**Check:** Every `WORDS` array and `GAME_DATA.items` array has 8–12 entries, never more than 15.

---

## 3. Audio on Every Vocabulary Word

Every vocabulary flashcard has a `▶ Pronounce` button using the Web Speech API (`lang='en-GB'`, `rate=0.9`). Students who don't know what a word sounds like cannot use it.

**Check:** Every `flashcards.html` contains `speakWord` function.

---

## 4. Comprehensible Input — Examples Before Rules

Lesson slides show real examples before or alongside grammar rules. Abstract formulae appear only after the student has seen the pattern in a sentence.

**Check:** Every grammar `slides.html` has at least one `.example-card` or `.overview-row` with a real sentence before the `.formula-block`.

---

## 5. Error Correction Targets the Source

Common mistakes slides (`.trap-row`) don't just show wrong/right — they name the reason. For Spanish speakers (`/es/`), interference errors are called out by name ("La trampa del tener").

**Check:** Every grammar chapter has a common-mistakes slide. Every `/es/` chapter has a dedicated interference slide.

---

## 6. Deterministic Grading — No Self-Assessment

All worksheet grading is automatic. Students never grade their own open production. The `ANSWERS` object covers all acceptable forms; `EXPLANATIONS` is required for every question key.

**Check:** `window.ANSWERS` and `window.EXPLANATIONS` in every `worksheet.html` have identical key sets.

---

## 7. Progress Is Visible and Rewarded

Completion is tracked in localStorage (and synced to the D1 backend for signed-in users) and shown as ✓ badges on nav tabs. Games fire confetti on mastery. The dashboard shows total progress per level. Students always know where they stand.

**Check:** Every `slides.html` has the progress badge script. Every `game.html` loads `game.js` (which fires confetti).

---

## 8. The Three-Step Chapter Flow

Every chapter follows: **Lesson → Practice → Game** (→ Printables for grammar). No chapter should be flashcard-only with no game, or game-only with no lesson.

**Check:** Every vocab topic folder has `flashcards.html` + `slides.html` + `game.html`. Every grammar topic has `slides.html` + `worksheet.html` + `game.html`.

---

## Automated Checks (run with `python3 scripts/pedagogy_check.py`)

| Check | Files | Pass condition |
|-------|-------|----------------|
| Audio button | `**/flashcards.html` | Contains `speakWord` |
| Item count | `**/flashcards.html`, `**/game.html` | 8–12 items |
| Explanations parity | `**/worksheet.html` | ANSWERS keys ⊆ EXPLANATIONS keys |
| Lesson CTA | `**/slides.html` | Contains `worksheet.html` link |
| Trap row | `**/grammar/**/slides.html` | Contains `.trap-row` |
| Three files | `vocabulary/*/` | flashcards + slides + game present |
