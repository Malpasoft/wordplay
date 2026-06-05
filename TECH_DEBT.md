# Word Play — Technical Debt Register

> Living record of known technical debt. **Last audited 5 June 2026** against the live tree.
> Rules and conventions live in **CLAUDE.md** — this file tracks where the codebase
> diverges from them and what to do about it. Update the status column as items are closed.

Three Spanish-related tracks are easy to confuse — kept distinct throughout:

| Track | What it is | State |
|-------|-----------|-------|
| `es/` | English course **explained in Spanish** (Spanish speakers learning English) | 107 gramatica/ chapters built, 71 vocab stubs, 26 writing complete |
| `espanol-en/` | Spanish course for English speakers | A1 hub scaffold (120/120 content stubs), A2–C2 stub hubs |
| `espanol/` | Universal Spanish course | Index scaffolds only — Phase 6, out of scope |

---

## Verified clean (no action)

- **D1 frontend ↔ backend** — `profile.html` / `calendar.html` match their Pages Functions
  exactly (POST + action dispatch, `student_ids` arrays, `updated_at` conflict merge). No
  old-schema artefacts remain. The only outstanding step is the one-time DB re-migration
  (see `CLOUDFLARE_SETUP.md`).
- **Cache-bust versions** — every shared asset is pinned to a single `?v=` across all
  consumers (base v123, slides v115, deck v113, game.css v111, game.js v110, store v105,
  worksheet v107, print v102, dark-init v109). No drift.
- **Teacher tools not redundant** — `ai-prompts.html` (prompt factory) → `builder.html`
  (output processor) → `dev-hub.html` (utilities) are sequential, not duplicative.

---

## HIGH

### H1 — Hardcoded amber hex on chapter-hub activity cards · **status: CLOSED**
- 330 chapter `index.html` hubs batch-updated: `--ac-color:#B8860B` → `--ac-color:var(--amber)`.
- **Intentional exceptions (not debt):** game cards use `--ac-color:#2E7D52` (green) and print
  cards use `--ac-color:#6B6B6B` (grey). These distinguish activity types at a glance and are
  formally documented as allowed exceptions to the amber-only rule. CLAUDE.md updated.
- 7 `certificate.html` files: amber is hardcoded for print fidelity — intentional, leave as-is.

---

## MEDIUM

### M1 — Doc drift: stale dev-branch references · **status: CLOSED**
All four docs updated to generic branch guidance (no hardcoded branch names).

### M2 — `es/` vocabulary flashcard stubs *(roadmap priority #3)* · **status: open**
71 `es/` vocab chapters have both `flashcards.html` and `game.html` as stub placeholders (marker: `<!-- FLASHCARDS CONTENT PLACEHOLDER -->`). Breakdown: a1: 6 stubs (6 of 12 filled); a2–c2: all 71 remaining stubs total. These are the **72 `MISSING CRUMB`** structure failures — `/fill-vocab` adds content. Fix: `/fill-vocab es <level> <slug>`, starting es/a1.

### M3 — English C1/C2 vocabulary stubs · **status: CLOSED**
Claimed 14 of 26 empty chapters. Actual: **all C1/C2 vocab chapters are fully populated**. Only 2 chapters per level lack flashcards by design (applied-grammar pattern): `c/c1/vocabulary/applied-grammar-register/` and `c/c2/vocabulary/applied-grammar-collocation/`. English vocab track is essentially complete.

### M4 — `espanol-en/a1` common-mistakes slides + stubs *(roadmap priority #5)* · **status: open**
A1 hub scaffold is complete but **all 120 content files are placeholder stubs** ("Content coming soon"). Only reachable after filling content: 24 `espanol-en/a1/grammar/*/slides.html` need the required `.trap-row` common-mistakes slide. (Moot until content exists, but document the requirement.)

### M5 — `design-check.sh` hook gaps · **status: partial**
- H1 hex drift now closed by batch fix — hook wasn't the root cause.
- `♥`/`♡` eliminated site-wide (match.html, builder.html, worksheet.js all converted to SVG hearts).
- Remaining gap: hook does not catch `--ac-color:#hex` in inline styles. Low priority now that H1 is
  closed, but worth adding if activity-card templates are regenerated at scale.

---

## LOW / housekeeping

| ID | Item | Status |
|----|------|--------|
| L1 | `builder.html` + `match.html` + `worksheet.js` heart glyphs → SVG hearts with `currentColor` | **CLOSED** |
| L2 | `index.html` 2 inline `onmouseover`/`onmouseout` → move to CSS `:hover` | **CLOSED** |
| L3 | `wrangler.jsonc` stale "replace database_id" comment (ID is filled) | **CLOSED** |
| L4 | Applied-grammar chapters: `b/b1/vocabulary/applied-grammar-verbs/` + 3 others (c1, c2 variants) | **CLARIFIED** — These are intentional, complete chapters with empty flashcards.html by design (no vocabulary content, links to lesson/game). Not stubs; working as intended. |
| L5 | `a/a1/vocabulary/animals/flashcards.html` WORDS is unquoted JS literal → pedagogy parse warning (file works) | **CLOSED** |
| L6 | Branch clutter: cleanup + audit (stale branch references) | **CLARIFIED** — Referenced branches (`…-1ZNUG`, `…-5BQiv`, others) no longer in this clone. Either already pruned or never fetched. No action needed if cleanup already happened. |
| L7 | `.claude/` playwright-audit `*.{md,json}` + screenshots not git-ignored | **CLOSED** — Enhanced `.gitignore` to exclude `.playwright-audit-*` and `.claude/playwright-audit*` |
| L8 | ~19 one-off `fix_*`/`migrate_*`/`gen_es_*`/`gen_en_*` scripts linger beside reusable validators | open — Consider archiving to a `scripts/legacy/` or removing if truly unused |
| L9 | `placement-test.html` (v1) superseded but internally linked from `teacher.html`, `profile.html` | open — Update inbound links to v2 or redirect |
| L10 | `shared/card-exercise.js` no `<script>` loader found in audited scope | open — Verify whether consumed by content chapters or orphaned |

---

## Known roadmap items (tracked work, not debt)
- **Mascot debug & mobile fix** · **CLOSED** (5 June) — removed console.log statements, fixed sprite scaling at ≤640px
- **Git tree cleanup** · **CLOSED** (5 June) — removed 11 PNG screenshots, 3 content-dump JSONs, misnamed file
- **Doc recount** · **CLOSED** (5 June) — AI_HANDOVER, SESSION_CONTEXT, README updated to match actual inventory
- **match.html** deployed on 1 of ~165 vocab chapters (roadmap #6).
- **fr/ lessons** — 81 navigational hubs exist with dead links to non-existent slides/worksheets/games (roadmap #4).
- **espanol-en/a1 content** — hub scaffold exists; 120/120 content files are placeholder stubs (roadmap #5).
- `review.html` not built; 299 printables exist but aren't wired into the student flow.
- `espanol/` universal Spanish course = scaffolds only (Phase 6).

---

## Remediation order (as of 5 June 2026)

**Completed this session (5 June):**
- Docs reconciled to ground truth (M1 updated, AI_HANDOVER/SESSION_CONTEXT/README corrected)
- Mascot cleaned (debug logs removed, mobile scaling fixed, v1→v2 cache-bust)
- Git tree hygiene (15 stray files removed, .gitignore enhanced)
- TECH_DEBT inventory audited

**Active roadmap (priority order):**
1. ⚠️ **DONE:** Mascot (removed debug, fixed mobile bug). Merged to main.
2. ⚠️ **DONE:** Git hygiene (cleaned stray assets). Merged to main.
3. **Fill 71 ES vocab stubs** — use dev-hub + DeepSeek/Gemini, run `/fill-vocab es <level> <slug>`. Start es/a1.
4. **Generate fr/ lesson content** — 81 hubs exist with dead links. ~72 files needed. Builder supports `fr` track.
5. **Fill espanol-en/a1 content** — 120/120 stubs. Add 24 missing `.trap-row` common-mistakes slides to grammar.
6. **Roll out match.html** — Pattern proven. ~76 vocab chapters need it. Builder generates file.
7. **Harden `design-check.sh`** (M5) — catch `--ac-color:#hex` in inline styles if needed at scale.
8. **Hygiene:** L8 (archive/remove stale scripts), L9 (placement-test v1→v2 links), L10 (audit card-exercise.js).

**Content tracks summary:**
- English: ✓ Complete (213 chapters, all sections enriched)
- ES: Grammar ✓ (107 chapters), Writing ✓ (26 chapters), Vocab 71 stubs pending
- espanol-en: A1 hub scaffold built (content 120 stubs), A2–C2 stub hubs
- fr: 81 navigation hubs (content dead-linked, ~72 files pending)
- espanol: Phase 6 (out of scope)
