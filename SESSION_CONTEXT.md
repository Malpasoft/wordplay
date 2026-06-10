# Word Play — Session Context

**Live URL:** `https://wordplay-38t.pages.dev`  
**Maintainer:** Em — freelance English teacher, Catalunya  
**Repo:** `malpasoft/wordplay` → auto-deploys to Cloudflare Pages on push to `main`  
**Working branch:** the session's feature branch (given per session) — never commit to `main` directly

> **Read CLAUDE.md first (all the rules), then AI_HANDOVER.md (orientation).** This file is
> the deep technical reference — JS contracts, shared-engine wiring, and the localStorage schema.

---

## 1. Architecture notes

- Static site: ~2,479 HTML files, vanilla HTML/CSS/JS, no build step
- Shared engines in `shared/` loaded via `?v=vNN` cache-busting (versions are independent per file)
- All student progress in browser localStorage; teacher calendar + profiles sync to Cloudflare D1 via passphrase code (DB `wordplay_db`, binding `DB`; functions in `functions/api/`; setup + verify steps in `CLOUDFLARE_SETUP.md`; graceful localStorage fallback if DB unbound)
- `body class="deck-body"` required on every `slides.html`
- `.sect-card` CSS class for section cards on hub pages — never inline `onmouseover`/`onmouseout`
- Design hook at `.claude/hooks/design-check.sh` runs after every Edit/Write and flags emoji + off-palette colours
- Session-start hook at `.claude/hooks/session-start.sh` copies `.claude/skills/*` to `~/.claude/skills/` so custom skills persist

---

## 2. Content inventory

### English track — 213 chapters (all complete)
| Section | A1 | A2 | B1 | B2 | C1 | C2 |
|---------|----|----|----|----|----|----|
| Grammar | 24 | 19 | 21 | 18 | 17 | 11 |
| Vocabulary | 12 | 12 | 11 | 16 | 14 | 12 |
| Writing | 3 | 3 | 3 | 5 | 6 | 6 |

All vocabulary chapters enriched. Only 2 intentional "applied-grammar" chapters (c1, c2) lack flashcards by design.  
A1 vocabulary: old template (`renderCard`/`STORAGE_KEY`) in 11 chapters, new template in 1 (animals); A2–C2: new template (`showCard`/`MASTERY_KEY`).

### Spanish track (`/es/`) — English explained in Spanish, all 6 levels
**Grammar:** ✅ 107 `gramatica/` chapters (Spanish-named) across all 6 levels, all filled with real content + Spanish-English contrastive notes.  
**Vocabulary:** 78 chapters total; 78/78 flashcards complete (game.html files are still placeholder stubs in all 78). Status:
- ✅ A1: 12/12 filled
- ✅ A2: 12/12 filled
- ✅ B1: 12/12 filled
- ✅ B2: 16/16 filled
- ✅ C1: 14/14 filled
- ✅ C2: 12/12 filled
- ⚠️ 1 stub (location unknown)

**Writing:** ✅ 26 chapters, all complete.  
All sections enriched with full pedagogical content (flashcards, worksheets with explanations, mastery games).

### Espanol-en track — Spanish for English speakers
**A1: 100% complete (verified 9 June, pedagogy_check 0 failures)**
- ✅ Vocabulary: 12/12 — flashcards (Spanish headwords, IPA, es-ES audio), intro slides, topic worksheets with explanations, Dominio games
- ✅ Grammar: 25/25 — 7-slide decks, 8-question worksheets with explanations, 10-question mastery games
- ✅ Writing: 3/3 — slides, worksheets, games AND 3-page printables (reference card / task / model answer)

**A2–C2:** Stub hub pages + chapter directory frameworks created (ready for future population phases).

### Total search index: 424 chapters

---

## 3. Engine files in `shared/`

| Asset | Version | Role |
|-------|---------|------|
| base.css | v124 | Global layout, design tokens, dark mode |
| slides.css | v115 | Slide deck styles |
| deck.js | v114 | Slide nav, confetti, Dashboard injection |
| game.css | v112 | Mastery game styles |
| game.js | v111 | 4-stage mastery engine |
| store.js | v107 | localStorage wrapper, FCEStore, XP |
| worksheet.js | v108 | Auto-grader with explanations |
| print.js | v102 | Print/PDF modal |
| dark-init.js | v112 | Dark/light toggle, back-to-top |

---

## 4. Contracts

### Lesson pages (slides.html)
```html
<body class="deck-body">
<script>
window.LEVEL = "a1";
window.CHAPTER_ID = "animals";
</script>
<script src="../../../../shared/store.js?v=v107"></script>
<script src="../../../../shared/deck.js?v=v114"></script>
```

### Worksheet
```html
<script>
window.CHAPTER_ID = "slug";
window.LEVEL = "a2";
window.TOTAL_POINTS = N;
window.ANSWERS = { q1: "answer", ... };
window.EXPLANATIONS = { q1: "reason", ... };  // every key in ANSWERS must be in EXPLANATIONS
</script>
```

### Game
```html
<script>
window.GAME_DATA = {
  chapterId: "slug", level: "a2", title: "Title",
  storageKey: "wordplay_game_a2_slug",
  items: [{ id, term, meaning, synonym, example, completion, answer }]  // 8–12 items
};
</script>
```

### Vocab flashcards — OLD template (A1 only)
```js
var STORAGE_KEY = 'wordplay_vocab_a1_{topic}_mastered';
var WORDS = [{ word, definition, example, pronunciation }];  // 10 items
function renderCard(idx) { ... }
function markMastered() { ... }
```

### Vocab flashcards — NEW template (A2–C2)
```js
var MASTERY_KEY = 'wordplay_vocab_{level}_{slug}_mastered';
var SLUG = '...'; var LEVEL = '...';
var WORDS = [{ word, ipa, def, ex }];  // 10 items
function showCard(idx) { ... }
function markMastered() { ... }
```

### Match game (match.html) — new standalone
```js
var MASTERY_KEY = 'wordplay_vocab_{level}_{slug}_mastered';
var PROG_KEY = '{level}';  // e.g. 'a1'
var SLUG = '...';
var TOTAL_NEEDED = WORDS.length * 2;  // each word matched twice
var state = [], lives = 3, selIdx = null, totalDone = 0, rightPool = [], animLock = false;
```
Match game is generated by `builder.html` → `generateMatch()` for one-offs, or `scripts/gen_match.py` in bulk. Rolled out 10 June 2026 to all eligible a/, b/, c/, fr/ vocab chapters (98); es/ + espanol-en/ Spanish-UI variant pending.

---

## 5. localStorage schema

```
wordplay_progress = {
  a1: {
    'slides_{chapterId}':         { done: true, date: "ISO" },
    '{chapterId}':                { pct: 85, done: true },          // worksheet
    'wordplay_game_{chapterId}':  { pct: 90 },                     // game score
    'vocab_mastered_{topic}':     { done: true, date: "ISO" },     // flashcard mastery
  },
  a2: { ... }, ...
}
wordplay_dark = "1" | "0"
wordplay_sync_code = "XXXX-XXXX"         // D1 passphrase (calendar + profiles)
wordplay_lessons_cache = [...]            // calendar lessons from D1
wordplay_student_profiles = { id: {...} } // student profiles
```

Dashboard reads `lv['vocab_mastered_' + slug].done` to count vocab mastered per level.

---

## 6. Design tokens

```css
--amber:   #B8860B (light) / #C9A050 (dark)   /* only accent — always var(--amber) */
--paper:   #F7F3EE (light) / #0E0E0E (dark)   /* background */
--ink:     #1A1A1A (light) / #F0F0F0 (dark)   /* text */
--cream:   #F0EBE0 (light) / #1A1A1A (dark)   /* card backgrounds */
--hairline: #E0D8CC (light) / #2E2E2E (dark)  /* borders */
--muted:   #6B6560 (light) / #9A9590 (dark)   /* secondary text */
```
UI symbols only: `◐` / `◑` (dark toggle), `◆` (streak badge). No emoji anywhere else.

---

## 7. Next steps (priority order)

1. ✅ **Mascot code** — RESOLVED (removed debug statements, fixed mobile sprite scaling)
2. ✅ **Git hygiene** — RESOLVED (removed stray screenshots, JSON files, test artifacts)
3. ✅ **Fill ES vocabulary stubs** — RESOLVED (78/78; the last 'stub' was unresolved merge-conflict markers in es/a2 health-and-body, fixed 10 June)
4. ✅ **Fill espanol-en A1 content** — RESOLVED (all vocabulary, grammar, writing populated)
5. ✅ **Espanol-en A2–C2 frameworks** — RESOLVED (stub hubs and chapter directories created)
6. **Find & fill remaining ES vocab stub** — 1 chapter location unknown; identify and populate.
7. ✅ **Generate fr/ lesson content** — COMPLETE 10 June: all 71 chapters populated from same-slug English chapters via scripts/gen_fr_from_en.py.
8. ✅ **Roll out match.html** — DONE 10 June for a/, b/, c/, fr/ (98 chapters) via scripts/gen_match.py. Spanish-UI variant for es/ + espanol-en/ pending.
9. **Espanol-en A2–C2 content population** — frameworks exist; ready for pedagogical enrichment phase.

---

*Last verified 10 June 2026 — fr/ track complete (71 chapters), match.html rollout (98 chapters), es vocab 78/78 flashcards, espanol-en A2 complete (34 chapters via gen_esen_a2*.py data-driven renderers), 12 production inline-JS bugs fixed, scripts archived (L8).*
