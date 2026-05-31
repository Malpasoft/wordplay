# Directory `a`: CEFR A1 and A2

Beginner (A1) and Elementary (A2) levels. Vocabulary and grammar aligned with Cambridge A1 Starters/Movers and A2 Key (KET).

## Folder structure

- **a1/** — CEFR A1: 24 grammar + 12 vocabulary + 3 writing = **39 chapters**
- **a2/** — CEFR A2: 19 grammar + 12 vocabulary + 3 writing = **34 chapters**

Each chapter folder contains:
- `slides.html` — lesson deck (`class="deck-body"` on `<body>`, powered by `deck.js`)
- `worksheet.html` — auto-graded practice (powered by `worksheet.js`)
- `game.html` — 4-stage mastery game (powered by `game.js`)
- `printables.html` — print-ready A4 (grammar chapters)
- `flashcards.html` — flip cards + match game + word list (vocabulary chapters)

## Notes

- A1 vocab uses the **old** flashcard template (`STORAGE_KEY`, `renderCard()`) with audio pronunciation and auto-complete.
- A2–C2 vocab uses the **new** template (`MASTERY_KEY`, `showCard()`); audio and auto-complete are a known pending item.
- KET (A2 Key) exam prep is a future roadmap item.
