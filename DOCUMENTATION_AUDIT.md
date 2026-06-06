# Word Play — Documentation Audit

**Conducted:** June 6, 2026  
**Scope:** Gap analysis of existing documentation vs. actual codebase complexity

---

## Existing Documentation (✅ Completed)

| Document | Purpose | Scope | Completeness |
|----------|---------|-------|--------------|
| **CLAUDE.md** | Single source of truth for project rules | Design system, git workflow, cache-busting, pedagogy principles | Excellent |
| **AI_HANDOVER.md** | Orientation for AI/developer sessions | Content state, shared engines, localStorage schema, roadmap | Excellent |
| **SESSION_CONTEXT.md** | Deep technical reference | JS contracts, localStorage schema, next steps | Good |
| **CONTRIBUTING.md** | Git/PR workflow for contributors | Branch naming, PR checklist, design rules | Good |
| **PEDAGOGY.md** | Learning design principles | 8 core principles, automated checks | Excellent |
| **CLOUDFLARE_SETUP.md** | D1 database one-time setup | Migrations, binding, verification, API contracts | Good |
| **README.md** | Project root overview | File structure, track descriptions | Good |
| **TECH_DEBT.md** | Technical debt register | Known issues, remediation order, roadmap | Excellent |
| **AUTH_PROPOSAL.md** | Future auth implementation | Phase 3 plan (not yet built) | Adequate |
| **SYLLABUS.md** | Cambridge syllabus mapping | (not examined in detail) | Unknown |

---

## Missing Documentation (❌ Needed)

### HIGH PRIORITY

#### 1. **Shared Engines Deep Dive** (game.js, deck.js, store.js, worksheet.js)
- **Why needed:** These files are complex, multi-stage state machines. Current docs only list what they do, not *how* they work or how to extend them.
- **What's missing:**
  - Game.js algorithm: 4-stage flow (recognition → meaning → context → production), scoring rules, bonus calculation, grading logic
  - Store.js contract: localStorage mutation patterns, chapter registry, streak calculation, XP level mapping
  - Deck.js: slide navigation, progress badge injection, confetti trigger, completion state
  - Worksheet.js: question grading, explanation display, per-exercise scoring, normalization logic (e.g., case-insensitive matching)
- **Who needs this:** Anyone modifying game logic, fixing grading bugs, or creating new content programmatically
- **Estimated effort:** 4–5 hours (requires reading 500+ lines per file, synthesizing algorithm descriptions)
- **Sample outline:**
  ```
  # Shared Engines Documentation
  ## 1. game.js — 4-Stage Mastery Engine
  - Game lifecycle: init → round loop → scoring → win/lose
  - GAME_CONFIG: magic numbers (SCORE_GOAL, BONUSES, AUDIO_TONES)
  - Scoring algorithm: base 10pts per correct, bonuses (same-item +5, cross-item +3)
  - Grading by question type: significado/contexto (MC match), produccion (normalized text or aliases)
  - State management: queued items, selectedIdx, streak tracking
  - Error cases: malformed GAME_DATA, missing fields
  
  ## 2. store.js — Progress Storage & XP
  - localStorage schema: wordplay_progress, wordplay_dark, wordplay_sync_code
  - Chapter registry (CHAPTERS object): how to register new chapters
  - Mutation patterns: saveResult, saveGameResult, saveVocabMastery
  - XP levels: Beginner (0), Elementary (100), ..., Advanced (2000)
  - Streak calculation: local date (en-CA), consecutive day logic
  - Migration from old storage keys
  
  ## 3. deck.js — Slide Navigation
  - Slide lifecycle: init, prev/next/goto handlers
  - Progress badge: injection into lesson nav, completion criteria
  - Confetti animation: trigger on mastery, particle config
  - Completion flow: auto-call next chapter link
  
  ## 4. worksheet.js — Auto-Grading
  - Question types: MCQ (exact match), text (normalized), fill-in
  - Explanation display: always shown after submission
  - Per-exercise scoring: score, total, pct calculation
  - Text normalization: lowercase, punctuation, whitespace
  ```

---

#### 2. **API & Backend Reference** (functions/api/)
- **Why needed:** Multiple endpoints exist for auth, profiles, lessons, progress, admin. Current CLOUDFLARE_SETUP.md covers only profiles + lessons. Auth endpoints are undocumented.
- **What's missing:**
  - All endpoint signatures: `/api/profiles/:code`, `/api/lessons/:code`, `/api/progress/:user_id`, `/api/auth/signup`, `/api/auth/login`, `/api/auth/logout`
  - Request/response schemas for each
  - Auth flow: JWT tokens, session management, error codes
  - Admin endpoints: `/api/admin/users`, `/api/admin/migrate-progress`
  - Rate limiting, CORS, security model
- **Who needs this:** Anyone integrating the backend, debugging sync issues, or adding new endpoints
- **Estimated effort:** 3–4 hours (requires reading ~8 endpoint files, extracting contracts)
- **Sample outline:**
  ```
  # API Reference
  ## Authentication
  ### POST /api/auth/signup
  - Request: { email, password }
  - Response: { ok: true, user_id, token }
  - Errors: 400 (invalid), 409 (already exists)
  
  ### POST /api/auth/login
  - Request: { email, password }
  - Response: { ok: true, user_id, token }
  - Errors: 401 (invalid credentials)
  
  ## Profiles (Passphrase-based)
  ### GET /api/profiles/:code
  - Response: { profiles: [...], updated_at }
  - No auth (passphrase = URL param)
  
  ## Progress
  ### GET /api/progress/:user_id
  - Auth: Bearer token
  - Response: { progress: {...}, lastUpdate }
  ```

---

#### 3. **File Generation & Content Scripts** (scripts/)
- **Why needed:** ~30 Python scripts exist, but no master guide. Developers and AI sessions don't know which script to use, when, or how.
- **What's missing:**
  - Quick reference: what does each script do? (fill_chapter.py vs. gen_chapter.py vs. gen_es_*)
  - Usage examples: `python3 scripts/fill_chapter.py es a1 animals`
  - Input/output formats: what data does it expect, what files does it create?
  - Script dependency graph: which scripts must run in order?
  - Content modules (`scripts/content/`) structure and how to extend them
- **Who needs this:** Content managers using fill_chapter.py, AI sessions generating bulk content, maintainers debugging generation
- **Estimated effort:** 3–4 hours (audit all 30 scripts, categorize, document top 5–7)
- **Sample outline:**
  ```
  # Content Generation Scripts Guide
  ## Core Generators
  ### fill_chapter.py — Fill a single chapter with content
  Usage: python3 scripts/fill_chapter.py <track> <level> <slug>
  Example: python3 scripts/fill_chapter.py es a1 animals
  Input: Expects CLAUDE.md + content modules + track structure
  Output: Writes flashcards.html, game.html into es/a1/vocabulary/animals/
  When to use: After scaffolding a new chapter
  
  ### gen_chapter.py — Generate entire chapter HTML (template)
  Usage: python3 scripts/gen_chapter.py <section> <slug> <level>
  Input: CSV with lesson content
  Output: slides.html, worksheet.html, game.html
  When to use: One-time scaffold generation
  
  ### gen_es_* scripts — Spanish content (language-specific)
  - gen_es_a1_specs.py: A1 spec builder
  - gen_es_a2.py: A2 content generation
  - gen_es_b1.py, gen_es_b2_c1_c2.py: Higher levels
  Purpose: Fill /es/ track content (grammar + vocabulary)
  
  ## Utilities
  ### check_structure.py — Validate chapter structure
  Usage: python3 scripts/check_structure.py <path>
  Output: List missing files (slides.html, flashcards.html, etc.)
  
  ### gen_coverage.py — Build coverage map
  Output: shared/coverage-data.json (used by coverage.html)
  When to use: After bulk content changes
  
  ## Script Dependencies
  - fill_chapter.py depends on content/ modules
  - gen_coverage.py depends on all chapter files existing
  - Pedagogy_check.py validates final output
  ```

---

### MEDIUM PRIORITY

#### 4. **Match Game Specification** (match.html pattern)
- **Why needed:** Match.html is new (exists only for animals/A1). Pattern is proven but not documented. Rollout to 76+ chapters planned.
- **What's missing:**
  - Design spec: 3 lives, double-match (each word matched twice), win condition
  - HTML template: minimum structure required
  - JS contract: MASTERY_KEY, PROG_KEY, SLUG, TOTAL_NEEDED, state machine
  - localStorage mutation pattern for match-specific progress
  - How to generate via builder.html's generateMatch() function
  - Styling overrides (if any) vs. base game.css
- **Who needs this:** Content creators rolling out match.html to other vocab chapters
- **Estimated effort:** 1–2 hours
- **Sample outline:**
  ```
  # Match Game (match.html) Specification
  ## Design
  - 3 hearts/lives (SVG-based, currentColor)
  - Each word must be matched to its definition twice (double-match rule)
  - Win = all words matched twice AND lives > 0
  - Lose = lives = 0
  
  ## HTML Template
  <script>
  var MASTERY_KEY = 'wordplay_vocab_{level}_{slug}_mastered';
  var PROG_KEY = '{level}';
  var SLUG = '{slug}';
  var WORDS = [{word, definition}, ...];  // exactly 8 items
  var TOTAL_NEEDED = WORDS.length * 2;
  </script>
  
  ## State Machine
  - state: array of {wordIdx, defIdx, matches}
  - selIdx: currently selected index (null if none)
  - lives: countdown from 3
  - totalDone: cumulative matches
  - animLock: prevents rapid clicks
  
  ## Builder Integration
  - builder.html → generateMatch() function
  - Downloads match.html pre-filled with chapter data
  ```

---

#### 5. **Two Flashcard Templates Comparison** (old vs. new)
- **Why needed:** CLAUDE.md mentions "never mix them" but doesn't explain why or when to use which. A1 is transitioning; confusion risk is high.
- **What's missing:**
  - Migration guide: how to upgrade old template to new?
  - Why the change? (new template is simpler, more extensible, aligns with A2+ naming)
  - Exact differences in object shape, function names, storage keys
  - Edge cases: what breaks if you mix? (answer: vocab progress tracking fails)
  - Code examples showing both templates side-by-side
- **Who needs this:** Content creators working on A1, anyone updating vocab chapters
- **Estimated effort:** 1–2 hours
- **Sample outline:**
  ```
  # Flashcard Templates: Old vs. New
  ## When to use each
  | Template | Where | Status |
  |----------|-------|--------|
  | Old | A1 only (11 chapters) | Deprecated; moving to new |
  | New | A2–C2 (67 chapters) | Standard; use for all new vocab |
  
  ## Old Template (A1 — renderCard/STORAGE_KEY)
  var STORAGE_KEY = 'wordplay_vocab_a1_{slug}_mastered';
  var WORDS = [{word, definition, example, pronunciation}, ...];
  function renderCard(idx) { ... }
  
  ## New Template (A2–C2 — showCard/MASTERY_KEY)
  var MASTERY_KEY = 'wordplay_vocab_{level}_{slug}_mastered';
  var SLUG = '...'; var LEVEL = '...';
  var WORDS = [{word, ipa, def, ex}, ...];
  function showCard(idx) { ... }
  
  ## Why migrate?
  1. Consistent naming (MASTERY_KEY used everywhere)
  2. Smaller object shape (ipa < pronunciation, def < definition)
  3. Extensible (easier to add fields)
  
  ## Migration Checklist
  - [ ] Rename STORAGE_KEY → MASTERY_KEY
  - [ ] Add SLUG, LEVEL variables
  - [ ] Rename WORDS fields: pronunciation→ipa, definition→def, example→ex
  - [ ] Rename renderCard() → showCard()
  - [ ] Update progress key in localStorage reads
  ```

---

#### 6. **Dark Mode Implementation Guide**
- **Why needed:** CLAUDE.md says "dark mode works on every element" but doesn't explain how or what to avoid.
- **What's missing:**
  - How the toggle works: dark-init.js + wordplay_dark localStorage key
  - CSS pattern: when to use !important overrides, when to use media queries
  - Color token mapping: --amber (light vs. dark), --paper, --ink, etc.
  - Gotchas: images in dark mode, emoji filtering by dark-check.sh hook
  - Testing checklist: how to verify dark mode on new pages
- **Who needs this:** Anyone adding new styles or components
- **Estimated effort:** 1–2 hours
- **Sample outline:**
  ```
  # Dark Mode Implementation Guide
  ## How it works
  1. dark-init.js detects system preference and localStorage wordplay_dark flag
  2. Sets html[data-theme="dark"] attribute on document root
  3. CSS uses [data-theme="dark"] selector for overrides
  
  ## Color Tokens
  :root {
    --amber: #B8860B;
    --paper: #F7F3EE;
    --ink: #1A1A1A;
  }
  [data-theme="dark"] {
    --amber: #C9A050;
    --paper: #0E0E0E;
    --ink: #F0F0F0;
  }
  
  ## CSS Patterns
  /* When to use !important (for component overrides) */
  .card { background: var(--paper) !important; }
  
  /* When to use selectors (for general styles) */
  [data-theme="dark"] .card { border-color: var(--hairline); }
  
  ## Testing
  1. Light mode: toggle via ◐ button, verify all text readable
  2. Dark mode: toggle via ◑ button, verify contrast
  3. Prefers dark (system): check auto-detect on fresh session
  ```

---

### LOW PRIORITY

#### 7. **Student Progress Dashboard Logic**
- **Why needed:** Dashboard reads from localStorage and renders XP levels, chapter stats, radar charts. Logic is not documented.
- **What's missing:**
  - How XP is calculated from chapter results
  - Radar chart data structure
  - What "Chapter completion" means (vocab mastered + game score?)
  - Level-up thresholds and how they affect display
- **Who needs this:** Anyone building new dashboards or progress-tracking features
- **Estimated effort:** 1 hour

#### 8. **Search & Coverage Features**
- **Why needed:** search-index.json (424 chapters) and coverage.html exist but logic is opaque.
- **What's missing:**
  - How is search-index.json generated? (gen_coverage.py?)
  - Search filtering: by level, section, track
  - Coverage reporting: what counts as "complete" vs. "stub"?
- **Who needs this:** Anyone modifying search or coverage features
- **Estimated effort:** 1 hour

#### 9. **Builder Tool (builder.html) Internals**
- **Why needed:** Builder can generate lessons, games, worksheets, flashcards, match files. No guide exists for extending it.
- **What's missing:**
  - Architecture: how does it generate HTML?
  - Content modules it calls
  - Supported tracks (English, Spanish, French, espanol-en)
  - Limitations: which file types can it generate, which can't?
  - How to add a new content type
- **Who needs this:** Content managers using the builder, developers extending it
- **Estimated effort:** 2 hours

---

## Documentation Gaps by User Persona

| Persona | High Priority | Medium Priority | Low Priority |
|---------|---------------|-----------------|--------------|
| **Content creator** (using fill_chapter.py, builder) | Scripts guide (#3) | Match game spec (#4), Flashcard templates (#5) | Progress dashboard (#7) |
| **JavaScript developer** (modifying game.js, store.js) | Shared engines (#1) | Match game spec (#4), Dark mode (#6) | Search (#8) |
| **Backend engineer** (adding auth, sync) | API reference (#2) | — | — |
| **Designer** (adding new components) | — | Dark mode (#6) | — |
| **New contributor** (onboarding) | Scripts guide (#3) | Flashcard templates (#5) | All three low |

---

## Estimated Effort Summary

| Document | Effort | Priority | Days* |
|----------|--------|----------|-------|
| Shared Engines Deep Dive (#1) | 4–5 hrs | HIGH | 1 day |
| API & Backend Reference (#2) | 3–4 hrs | HIGH | 1 day |
| Scripts Guide (#3) | 3–4 hrs | HIGH | 1 day |
| Match Game Spec (#4) | 1–2 hrs | MEDIUM | 0.5 day |
| Flashcard Templates (#5) | 1–2 hrs | MEDIUM | 0.5 day |
| Dark Mode Guide (#6) | 1–2 hrs | MEDIUM | 0.5 day |
| Progress Dashboard (#7) | 1 hr | LOW | 0.25 day |
| Search & Coverage (#8) | 1 hr | LOW | 0.25 day |
| Builder Internals (#9) | 2 hrs | LOW | 0.5 day |
| **TOTAL** | ~20 hrs | — | **5–6 days** |

*Assumes one person working sequentially. Could be parallelized.

---

## Recommended Rollout (Phase 2)

### Week 1: Foundation (enable code changes)
1. **Shared Engines Deep Dive** (#1) — unblocks game fixes, grading bugs
2. **API & Backend Reference** (#2) — unblocks backend work, auth integration

### Week 2: Content & UX (enable rolling out features)
3. **Scripts Guide** (#3) — unblocks fill_chapter.py usage, ES vocab filling
4. **Match Game Spec** (#4) — unblocks match.html rollout to 76 chapters
5. **Flashcard Templates** (#5) — unblocks A1 migration, new vocab chapters

### Week 3+: Polish (enable maintenance)
6. **Dark Mode Guide** (#6) — prevents regressions, speeds up new components
7. **Progress Dashboard** (#7), **Search** (#8), **Builder** (#9) — as-needed

---

## Notes

- **No new files yet.** This audit identifies gaps only. Phase 2 will create the documents.
- **CLAUDE.md is the source of truth.** New docs should link back to it, not duplicate rules.
- **Audience:** AI sessions, maintainers, content creators — not end users.
- **Format:** Markdown with code examples, inline sample outlines provided above.
- **Priority order reflects:** unblocking active work (scripts, APIs), preventing regressions (dark mode), and reducing onboarding friction for contributors.

---

*Last updated: June 6, 2026*
