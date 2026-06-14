# Word Play — Technical Debt Register

> Living record of **open** technical debt only. Rules and architecture live in **CLAUDE.md**;
> this file tracks where the codebase diverges from them and what to do about it. When an item
> is fixed, delete it — git history is the archive (don't accumulate "CLOSED" logs here).

The three Spanish-related tracks are easy to confuse — kept distinct throughout:

| Track | What it is | State |
|-------|-----------|-------|
| `es/` | English course **explained in Spanish** | grammar (107 `gramatica/`) ✅, vocab flashcards ✅, writing (26) ✅; A1–B2 only (C1/C2 removed per L1 rule). **Open:** vocab `game.html` are placeholder stubs. |
| `espanol-en/` | Spanish course for English speakers | A1+A2 ✅, B1+B2 ✅ (June 2026); A1–B2 only. |
| `espanol/` | Main Spanish course (taught in Spanish) | scaffolds only — Phase 5, planned. |

---

## Open debt

### D1 — `es/` vocab `game.html` are placeholder stubs
All `es/` vocabulary `game.html` files still contain placeholder `GAME_DATA` items even though
their flashcards are complete. Derive items from each chapter's `WORDS` array (pattern proven in
`scripts/gen_esen_a2_vocab.py`) and regenerate; Spanish UI comes from i18n on `<html lang="es">`.

### D2 — `design-check.sh` doesn't catch inline `--ac-color:#hex`
The design hook flags emoji and off-palette colours but misses hardcoded `--ac-color:#hex` in
inline styles. Low priority (the one historical batch of hardcoded amber is already fixed), but
worth adding if activity-card templates are regenerated at scale.

### D3 — Duplicate migration numbers
`migrations/` has two `0006_*.sql` and two `0007_*.sql` files. They apply cleanly (all use
`CREATE … IF NOT EXISTS`), but the numbering is ambiguous. Renumber sequentially next time the
schema is touched so the apply order is unambiguous.

### D4 — Printables / review pages not wired into the student flow
Printable pages exist for many grammar chapters but aren't consistently surfaced in chapter
hubs; there is no `review.html` step. Decide whether printables get an activity card everywhere
(per the per-chapter standard) and whether a spaced-review page is in scope.

---

## Verified clean (no action — spot-check before relying on)

- **Cache-bust versions** — every shared asset is pinned to a single `?v=` across consumers
  (the canonical list is in CLAUDE.md). No drift at last check.
- **D1 frontend ↔ backend** — `profile.html` / `calendar.html` match their Pages Functions
  (POST + action dispatch, `student_ids` arrays, `updated_at` conflict merge).
- **Applied-grammar vocab chapters** (c1, c2) have empty `flashcards.html` **by design** — not
  stubs. They link to lesson/game only.
