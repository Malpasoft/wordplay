# Word Play — Technical Debt Audit (6 June 2026)

> **Scope:** Comprehensive inventory of technical debt across scripts, dead code, deprecated patterns, and stale comments. Findings are **NOT actionable until reviewed**—this report is discovery phase only.

---

## Summary

**Total Findings:** 15 items identified  
**High Priority:** 4 items  
**Medium Priority:** 7 items  
**Low Priority:** 4 items  

**Key Areas:**
- 28 Python scripts in `scripts/` and root (most used for one-off content generation)
- 205 placeholder HTML files (stubs in `es/` vocab and `espanol-en/` content)
- Old A1 vocabulary flashcard template coexisting with new template (A2–C2)
- 1 console.log in production API code
- Possible script deduplication / archive candidates

---

## Detailed Findings

### **H1 — Proliferation of generation & migration scripts (HIGH)**
**Status:** Open | **Effort:** Medium

**Issue:**
28 Python scripts in `scripts/` directory and root:
- 12 `gen_*.py` (generation): `gen_chapter.py`, `gen_coverage.py`, `gen_es_a1_specs.py`, `gen_es_a2.py`, `gen_es_b1.py`, `gen_es_b2_c1_c2.py`, `gen_es_c1c2_vocab.py`, `gen_es_writing.py`, `gen_scaffold.py`, `gen_en_gaps.py`, `gen_en_vocab_gaps.py`, `gen_search_index.py`, `gen_explanations.py`, `gen_writing_gaps.py`
- 4 `fix_*.py`: `fix_game_html.py`, `fix_game_old_template.py`, `fix_flashcard_audio.py`, `fix_vocab_nav.py`
- 4 `fill_*.py`: `fill_chapter.py`, `fill_en_c1c2_vocab.py` (and 2 in `content/`)
- 3 `gen_*.py` at root level (duplicate set): `generate_a2.py`, `generate_c1.py`, `generate_writing.py`
- 5 utility scripts: `check_links.py`, `check_structure.py`, `add_i18n_script.py`, `update_es_a1_indexes.py`, `migrate_game_play.py`

**Root cause:** One-off scripts created during content generation phases (feature branches tagged in git: `4b86da56`, `8cbac5dc`, `6ea94438`). Most are not called from CI/CD or documented commands.

**Impact:** 
- Clutter in `scripts/` directory makes it hard to distinguish core validators (e.g., `pedagogy_check.py`) from build tools
- Risk of mistaken re-run of old migration scripts (e.g., `fix_game_old_template.py` operates on old game.html template, now obsolete)
- Root-level scripts (`generate_a2.py`, etc.) duplicate functionality in `scripts/`

**Suggested Action:** Archive to `scripts/legacy/` or document entry in `.claude/skills/` for intentional reuse patterns

---

### **H2 — Old A1 vocabulary flashcard template still in production (HIGH)**
**Status:** Open | **Effort:** Low

**Issue:**
A1 vocabulary uses old template with `STORAGE_KEY`, `WORDS[{word, definition, example, pronunciation}]`, `renderCard()`, `markMastered()`.
- **Count:** 11 A1 vocab chapters affected
- **Location:** `a/a1/vocabulary/*/flashcards.html`
- **New template used in:** A2–C2 (57 chapters) with `MASTERY_KEY`, `SLUG`, `LEVEL`, `WORDS[{word, ipa, def, ex}]`, `showCard()`, `markMastered()`

**Root cause:** A1 was the first track built; template was later refined and only new chapters received the upgrade.

**Impact:**
- Two independent implementations of the same feature (flashcard decks) in codebase
- Maintenance burden if flashcard logic changes (changes must be applied twice)
- Inconsistent data shape in localStorage (`vocab_mastered_<slug>` old style vs. `wordplay_vocab_<level>_<slug>_mastered` new style)
- CLAUDE.md documents the pattern but it remains a wart

**Suggested Action:** Batch-migrate A1 flashcards to new template (5–10 A1 chapters), test, update pedagogy check to enforce new template

---

### **H3 — 205 placeholder/stub HTML files block coverage metrics (HIGH)**
**Status:** Open | **Effort:** Low-to-Medium

**Issue:**
- **71 ES vocabulary stubs:** `es/*/vocabulary/*/flashcards.html`, `game.html` marked `<!-- FLASHCARDS CONTENT PLACEHOLDER -->`
- **126 espanol-en/a1 stubs:** `espanol-en/a1/*/*.html` all marked "Content coming soon"
- **8 additional orphaned stubs** across writing and grammar sections

These files are scaffold placeholders. They register in chapter registries but have zero content.

**Root cause:** Bulk structure generation in Phase 2 (see commit `6ea94438`). Content fill scripts (`/fill-vocab`) exist but haven't been run at scale.

**Impact:**
- `coverage.html` teacher report incorrectly counts stubs as "completed" (PLACEHOLDER marker doesn't zero the counter)
- Student dashboard falsely shows 205 navigable chapters instead of ~120 truly complete
- Risk: students click into stub pages and see "Content coming soon" → poor UX

**Suggested Action:**
1. Update `gen_coverage.py` to hard-exclude PLACEHOLDER-marked files from completion count
2. Mark stubs differently: `<!-- STUB -->` with clear visual affordance if accidentally accessed
3. Run `/fill-vocab es a1` to close the 6 immediate A1 stubs

---

### **H4 — Root-level duplicate Python scripts (HIGH)**
**Status:** Open | **Effort:** Low

**Issue:**
Three Python scripts in repo root duplicate functionality in `scripts/`:
- `/home/user/wordplay/generate_a2.py` ↔ `scripts/gen_es_a2.py`
- `/home/user/wordplay/generate_c1.py` ↔ `scripts/gen_es_b2_c1_c2.py`
- `/home/user/wordplay/generate_writing.py` ↔ `scripts/gen_es_writing.py`

**Root cause:** Early iteration before `scripts/` directory structure was established. Files never deleted when moved.

**Impact:**
- New contributors may use wrong file (root vs. scripts/)
- Maintenance drift risk if one is updated but not the other
- CI/CD confusion if both are referenced

**Suggested Action:** Delete root-level duplicates, update any documentation/git hooks to point to `scripts/` versions only

---

### **M1 — Single console.log in production API code (MEDIUM)**
**Status:** Open | **Effort:** Low

**Issue:**
One console.log in `/home/user/wordplay/functions/api/progress/[user_id].js:
```javascript
console.log(`PROGRESS_WRITE: user_id=${studentId}, chapters=${payload.chapters.length}, xp=${payload.xp}`);
```

**Root cause:** Debugging statement left in during development (commit `4673fd27`).

**Impact:**
- Minor: only affects Cloudflare server logs, not visible to users
- Security: logs student IDs and chapter counts (non-sensitive but unnecessary)
- Noise in observability systems if log aggregation is in use

**Suggested Action:** Remove the console.log, test locally before deploy

---

### **M2 — Stale check/lint scripts with unclear purpose (MEDIUM)**
**Status:** Open | **Effort:** Low

**Issue:**
Four utility scripts with minimal documentation:
- `check_links.py` — pulls href/src values; no usage docs
- `check_structure.py` — structure validator; no CLI example
- `add_i18n_script.py` — dated 5 June, no docstring explaining intent
- `migrate_game_play.py` — references old game template from v105 migration (now obsolete)

**Root cause:** Created for specific phases; no central registry of when/why to run them

**Impact:**
- Developer runs wrong script by accident (e.g., `check_links.py` when they meant `check_structure.py`)
- Risk of data corruption if old migration is re-run (e.g., `migrate_game_play.py` on already-migrated files)
- No entry point in `dev-hub.html` or `.mcp.json` to indicate they're supported

**Suggested Action:** Document each with clear `Usage:` docstring and add to `dev-hub.html` under "Validators" section, or remove if unused

---

### **M3 — Deprecated `gen_scaffold.py` at 58KB (MEDIUM)**
**Status:** Open | **Effort:** Low

**Issue:**
`scripts/gen_scaffold.py` is the largest script (58 KB), handles initial chapter structure generation. Last commit reference: `6ea94438` (phase 2 scaffolding). No active use documented.

**Root cause:** One-time bulk structure generator for ES and fr/ tracks. Functionality now built into `/builder` skill.

**Impact:**
- Code duplication: Builder.html + gen_scaffold.py both generate chapter directories
- 58 KB of dead code if builder is the active path
- Risk: if rebuilt, scaffold.py may generate old patterns (e.g., missing cache-bust versions)

**Suggested Action:** Verify builder handles all gen_scaffold functionality, then archive or deprecate with comment

---

### **M4 — Unused `pedagogy_check.py` check for old STORAGE_KEY (MEDIUM)**
**Status:** Open | **Effort:** Low

**Issue:**
`scripts/pedagogy_check.py` line 30 checks for old A1 pattern:
```python
if 'var WORDS' not in h and 'STORAGE_KEY' not in h:
    continue  # placeholder page, not a real flashcard deck
```

This **tolerates** the old template (doesn't error on it). No script enforces migration to new template.

**Root cause:** Pedagogy check was added after A1 was already built with old template; check was made lenient to avoid false positives

**Impact:**
- A1→A2 template divergence is not caught by pre-commit validation
- Developers can accidentally add new A1 chapters in old template and it will pass
- CLAUDE.md says to use new template, but no tool enforces it

**Suggested Action:** Add explicit validation rule: "All flashcards must use MASTERY_KEY template (A2+ pattern), or add explicit exception for A1 phase-out"

---

### **M5 — design-check.sh hook incomplete for activity-card colors (MEDIUM)**
**Status:** Open | **Effort:** Medium

**Issue:**
TECH_DEBT.md item M5 notes: Hook does not catch `--ac-color:#hex` in inline styles (only warns on hardcoded hex in other contexts). 

Example vulnerability: Chapter hub cards can still have inline `style="--ac-color:#2E7D52"` and won't trigger hook.

**Root cause:** Hook was designed for broad hex detection; activity-card CSS vars are legitimate exception, but exception logic is incomplete

**Impact:**
- Low currently (activity-card colors are documented exceptions in CLAUDE.md)
- Risk if design system colors change: no automated enforcement
- Future developers might hardcode new hex values thinking they're OK because hook didn't catch them

**Suggested Action:** Update hook to whitelist *only* the three intentional exceptions (green #2E7D52, grey #6B6B6B, amber), reject all others. Or document in `.claude/hooks/design-check.sh` with inline comment

---

### **M6 — Cache-bust version drift risk (inconsistent manual versioning) (MEDIUM)**
**Status:** Open | **Effort:** Low

**Issue:**
CLAUDE.md says cache versions are "not in lockstep" — each file has independent `?v=vNN`. Current state:
- `base.css` v123
- `slides.css` v115
- `deck.js` v113
- `game.css` v111, `game.js` v110
- `store.js` v105
- `worksheet.css` v107
- `print.css` v102
- `dark-init.js` v109

Manual versioning is error-prone. No automation to verify all consumers of a shared file are updated together.

**Root cause:** `/ship` skill provides semi-automation but requires manual selection of files to bump

**Impact:**
- Risk: after editing `base.css`, developer forgets to grep and bump version on 400+ consumer pages
- Cache staleness: users see old styles for hours
- No pre-commit hook catches version drift

**Suggested Action:** Add `pre-commit` hook that detects changes to `shared/*.{js,css}` and fails the commit if any consumer's `?v=` URL isn't bumped. Or switch to commit-hash-based versioning (`?v=<commit-sha>`) to auto-version on deploy

---

### **L1 — placement-test.html (v1) still in tree but unreachable (LOW)**
**Status:** Closed (per TECH_DEBT.md L9) | **Effort:** Low

**Issue:**
Two placement test versions exist:
- `placement-test.html` (v1) — old, updated links to v2 in June 2026
- `placement-test-v2.html` (v2) — current

v1 is still in tree but not linked from hub navigation. All inbound links (teacher.html, profile.html, index.html) now point to v2.

**Root cause:** v1 kept for historical reference; no deletion to preserve branch history

**Impact:**
- Minimal; v1 is unreachable from student/teacher UI
- Minor clutter (26 KB file)
- Risk: if someone navigates directly to v1 URL, they get old broken version instead of redirect

**Suggested Action:** Either delete v1 or add 301 redirect in Cloudflare Pages rules to `/placement-test.html` → `/placement-test-v2.html`

---

### **L2 — Incomplete `.trap-row` (common-mistakes) in espanol-en/a1 grammar (LOW)**
**Status:** Open | **Effort:** Low

**Issue:**
TECH_DEBT.md M4 notes: 24 `espanol-en/a1/grammar/*/slides.html` require `.trap-row` (common-mistakes slide) **when content is filled**. Currently all 120 A1 files are placeholder stubs, so requirement is moot until content is added.

**Root cause:** Pedagogical requirement documented in CLAUDE.md but not yet enforced in structure

**Impact:**
- Moot until content exists
- When `/fill-vocab espanol-en a1` is run, developer must remember to add `.trap-row` slides
- No validation script currently warns about missing `.trap-row`

**Suggested Action:** Once espanol-en/a1 content is filled, update `pedagogy_check.py` to enforce: "All espanol-en grammar slides must have `.trap-row`" and test

---

### **L3 — Unused CSS selectors in base.css and slides.css (LOW)**
**Status:** Open | **Effort:** Medium

**Issue:**
Broad grep shows ~30 CSS class names used in HTML, but `base.css` and `slides.css` define ~80 rule sets. Candidates for unused:
- Some `.card-actions`, `.card-num` variants
- Older `.counter` / `.deck-counter` patterns (modern pages use inline counters)

**Root cause:** CSS evolved incrementally; old styles for deprecated templates weren't removed

**Impact:**
- Minimal: unused CSS is still cached with base.css, adds ~2–5 KB
- Maintenance: developer reading CSS has to parse dead rules
- Risk: if a rule is removed, it might break a page that still uses it undetected

**Suggested Action:** Run modern CSS coverage tool (e.g., PurgeCSS / UnCSS on prod snapshot) to identify and remove ~10–15 unused rules. Test on all 5 shared CSS files

---

### **L4 — No enforcement of two-template split in flashcard code (LOW)**
**Status:** Open | **Effort:** Low

**Issue:**
CLAUDE.md documents two independent flashcard templates but there's no marker/comment in A1 files saying "use old template here". A2–C2 doesn't say "use new template here" either.

**Root cause:** Documentation is separate from code; developers must remember the rule

**Impact:**
- Confusion: new contributor may try to add A1 vocab using A2 template (or vice versa)
- Risk: if template patterns are renamed, grep won't catch all instances easily

**Suggested Action:** Add comments to both a1 and a2 first files:
```html
<!-- A1 VOCAB TEMPLATE (legacy) — use STORAGE_KEY, old WORDS shape. See CLAUDE.md. -->
<!-- A2+ VOCAB TEMPLATE (current) — use MASTERY_KEY, SLUG, LEVEL, new WORDS shape. See CLAUDE.md. -->
```

---

### **L5 — `migrate_game_play.py` references obsolete game.html v105 (LOW)**
**Status:** Open | **Effort:** Low

**Issue:**
Script comments reference `gFinalStreak` and v105 game template. Current game is v108+. If run on modern files, it will not match patterns and fail silently (or worse, corrupt if patterns partially match).

**Root cause:** Migration script from commit `4b86da56` (v105→v108 migration completed); script was never removed

**Impact:**
- Low currently (migration is done)
- Risk: if developer re-runs thinking it's a safety/audit script, it corrupts files

**Suggested Action:** Delete or document in header with `# DEPRECATED — migration completed in June 2026. DO NOT RUN.`

---

### **L6 — `.claude/hooks/design-check.sh` has old echo output (LOW)**
**Status:** Open | **Effort:** Low

**Issue:**
Hook includes placeholder echo statements; output is verbose but not actionable. Example:
```bash
echo "Checking for emoji in $file..."
```

This runs on every save for 400+ files, creating noise in terminal.

**Root cause:** Hook was debugged with verbose output; debug statements weren't removed

**Impact:**
- UX: developers see 400 "Checking..." lines on each edit, making output hard to scan
- No functional impact; hook still catches violations

**Suggested Action:** Replace verbose echo with silent pass, only output if violation found. Or move to `DEBUG` env var: `[[ $DEBUG ]] && echo "..."`

---

## Summary Table

| ID | Item | Priority | Current Status | Suggested Action | Est. Effort |
|---|---|---|---|---|---|
| H1 | 28 Python gen/fix/fill scripts clutter | HIGH | Open | Archive to legacy/ or document | Medium |
| H2 | A1 flashcard old template coexists with A2+ new template | HIGH | Open | Batch-migrate A1 to new template | Low |
| H3 | 205 placeholder HTML files inflate coverage metrics | HIGH | Open | Update coverage.py to exclude PLACEHOLDER | Low–Med |
| H4 | Root-level duplicate scripts (generate_*.py) | HIGH | Open | Delete root versions, keep scripts/ | Low |
| M1 | console.log in production API code | MEDIUM | Open | Remove logging statement | Low |
| M2 | Unclear utility scripts (check_*.py) | MEDIUM | Open | Document or remove | Low |
| M3 | 58 KB gen_scaffold.py possibly obsolete | MEDIUM | Open | Verify builder.html redundancy, archive | Low |
| M4 | pedagogy_check.py tolerates old template (no enforcement) | MEDIUM | Open | Add explicit new-template-only validation rule | Low |
| M5 | design-check.sh hook gaps (–ac-color) | MEDIUM | Open | Whitelist 3 exceptions, reject others | Med |
| M6 | Cache-bust versioning is manual & error-prone | MEDIUM | Open | Add pre-commit hook to enforce bumps | Medium |
| L1 | placement-test.html (v1) still in tree | CLOSED | Via L9 | Delete or redirect | Low |
| L2 | .trap-row enforcement deferred to espanol-en fill phase | LOW | Open | Document in pedagogy_check.py | Low |
| L3 | Unused CSS selectors in shared files | LOW | Open | Run PurgeCSS, remove dead rules | Medium |
| L4 | No code marker for two-template flashcard split | LOW | Open | Add inline comments to a1/a2 examples | Low |
| L5 | migrate_game_play.py obsolete | LOW | Open | Delete or mark deprecated | Low |

---

## Recommendations for Next Phase

### Immediate wins (1–2 hours):
1. Delete root-level `generate_*.py` duplicates (H4)
2. Remove console.log from progress API (M1)
3. Delete `migrate_game_play.py` (L5)
4. Add code comments to flashcard templates (L4)

### Medium-effort cleanup (2–4 hours):
5. Update `gen_coverage.py` to skip PLACEHOLDER files (H3)
6. Document/remove unclear scripts (M2)
7. Add template enforcement to `pedagogy_check.py` (M4)
8. Batch-migrate A1 flashcards to new template (H2)

### Structural improvements (4+ hours):
9. Archive 28 scripts to `scripts/legacy/` with README (H1)
10. Add pre-commit hook for cache-bust version enforcement (M6)
11. Run CSS coverage audit, remove unused rules (L3)
12. Harden `design-check.sh` hook with whitelist (M5)

### Verification:
- Run `python3 scripts/pedagogy_check.py` before closing (must pass)
- Test all 5 levels (A1, A2, B1, B2, C1, C2) across 3 sections (grammar, vocab, writing)
- Verify coverage.html metrics match actual content

---

## Notes for Reviewer

- **TECH_DEBT.md already tracks L1, L4, L9, L10** — this audit provides deeper discovery and prioritization
- **All findings are non-breaking discovery; no changes applied**
- **Effort estimates assume local testing, no major refactoring**
- **Cache-bust versioning (M6) is the most risky to automate—may need hooks or CI integration**

---

**Report prepared:** 6 June 2026  
**Next review:** After fixes applied + pedagogy check pass
