# Word Play — Technical Debt Register

> Living record of known technical debt. Audited 3 June 2026 against the live tree.
> Rules and conventions live in **CLAUDE.md** — this file tracks where the codebase
> diverges from them and what to do about it. Update the status column as items are closed.

Three Spanish-related tracks are easy to confuse — kept distinct throughout:

| Track | What it is | State |
|-------|-----------|-------|
| `es/` | English course **explained in Spanish** (Spanish speakers learning English) | Active, priority track |
| `espanol-en/` | Spanish course for English speakers | A1 built, A2–C2 stub hubs |
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

### M2 — `es/` vocabulary flashcard stubs *(roadmap priority #1)* · **status: open**
~77 `es/` vocab `flashcards.html` carry `var WORDS = []` (a1:12, a2:12, b1:11, b2:16, c1:14, c2:12).
These are also the **71 `MISSING CRUMB`** structure failures — `/fill-vocab` adds page furniture
and content, closing both. Fix: `/fill-vocab es <level> <slug>`, starting es/a1.

### M3 — English C1/C2 vocabulary stubs *(roadmap priority #2)* · **status: open**
14 of 26 chapters empty (c1: 7, c2: 7), e.g. `c/c1/vocabulary/formal-synonyms/`,
`c/c2/vocabulary/advanced-idioms/`. Fix: `/fill-vocab en c1|c2 <slug>`.

### M4 — `espanol-en/a1` grammar missing common-mistakes slides *(roadmap priority #4)* · **status: open**
24 `espanol-en/a1/grammar/*/slides.html` lack the required `.trap-row` slide. Fix: batch-add per
CLAUDE.md bulk-edit rules (grep variants first, sample 2–3).

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
| L4 | 2 empty stubs: `b/b1/vocabulary/applied-grammar-verbs/`, `b/b2/vocabulary/applied-grammar-prepositions/` | open |
| L5 | `a/a1/vocabulary/animals/flashcards.html` WORDS is unquoted JS literal → pedagogy parse warning (file works) | **CLOSED** |
| L6 | Branch clutter: `…-1ZNUG` merged → prunable (keep `…-5BQiv` active); 9 branches with unmerged commits need triage | open |
| L7 | `.claude/` playwright-audit `*.{md,json}` + screenshots not git-ignored | open |
| L8 | ~20 one-off `fix_*`/`migrate_*`/`gen_es_*`/`gen_en_*` scripts linger beside reusable validators | open |

---

## Known roadmap items (tracked work, not debt)
- `match.html` deployed on 1 of ~165 vocab chapters (priority #3).
- `review.html` not built; 299 printables exist but aren't wired into the student flow.
- `espanol/` universal Spanish course = scaffolds only (Phase 6).

---

## Remediation order
1. Commit this register.
2. Quick wins (one batch): H1 · M1 · L1 · L2 · L3 · L5 → `/qa` → `/ship`.
3. Harden `design-check.sh` (M5).
4. Content backlog (dedicated sessions): M2 → M3 → M4 via `/fill-vocab`.
5. Hygiene when convenient: L4 · L6 · L7 · L8.
