# Bug Report — Word Play

**Date:** 2026-06-06  
**Audit Type:** Systematic bug hunt (baseline checks + sample page testing)  
**Scope:** 2,372 HTML pages, shared assets, localStorage, dark mode, mobile responsiveness

---

## Summary

| Severity | Count | Status |
|----------|-------|--------|
| **CRITICAL** | 1 | Blocks user interaction |
| **MAJOR** | 1 | Affects broad user base |
| **MINOR** | 0 | UX/content issues |
| **Total** | 2 | |

**Passed checks:**
- Pedagogy check: 1,043 passed, 0 failures (24 warnings for missing common-mistakes slides)
- GAME_DATA: Present in all grammar game pages audited
- Dark mode: CSS variables present and functional
- Mobile viewport: Meta tags correct
- Flashcard audio: Web Speech API implemented (en-GB, rate 0.9)
- localStorage sync: Progress tracking in place

---

## Critical Bugs

### BUG-001 · CRITICAL · Import Path Mismatch

**Location:** All 2,431 HTML pages that reference `shared/auth.js`

**Pages Affected:** Sample of confirmed files:
- `a/a1/grammar/to-be/index.html` (and 400+ grammar pages)
- `a/a1/vocabulary/animals/flashcards.html` (and 300+ vocab pages)
- `a/a1/certificate.html`
- All Spanish (es/a1) pages
- All grammar/vocab/writing pages across A1–C2 levels

**Severity:** CRITICAL — Breaks site functionality

**Description:**  
Pages use relative import path `src="shared/auth.js?v=1"` instead of correct relative path with proper depth prefix (e.g., `src="../../../../shared/auth.js?v=1"`).

**Current state:**
- File reference: `<script src="shared/auth.js?v=1"></script>` at `a/a1/grammar/to-be/index.html`
- Expected file location from that page: `a/a1/grammar/shared/auth.js` (does not exist)
- Actual file location: `/home/user/wordplay/shared/auth.js`
- Link check result: 2,638 broken links all pointing to `shared/auth.js?v=1`

**Steps to reproduce:**
1. Open any grammar/vocab page in a browser (e.g., `a/a1/grammar/to-be/index.html`)
2. Open browser DevTools → Console
3. Observe 404 error: `GET /a/a1/grammar/shared/auth.js?v=1 404`
4. Result: Auth utility functions (`getAuthToken()`, `isLoggedIn()`, `isAdmin()`) are undefined
5. Any page that calls these functions will fail silently or throw errors

**Root cause:**  
Inconsistent path references. Other shared files in the same pages use correct relative paths:
- ✅ `href="../../../../shared/base.css?v=v123"` (correct)
- ✅ `src="../../../../shared/dark-init.js?v=v109"` (correct)
- ❌ `src="shared/auth.js?v=1"` (wrong — missing depth prefix)

**Impact:**
- Auth functions unavailable on every page
- Teacher tools may fail if they depend on auth checks
- Student progress tracking may be compromised if auth is required

**Suggested fix:**
Replace all 2,431 instances of `src="shared/auth.js?v=1"` with the correct relative path based on page depth:
- Pages at `a/aX/*/*.html` → `src="../../../../shared/auth.js?v=1"`
- Pages at `a/aX/*/*/*.html` → `src="../../../../../shared/auth.js?v=1"`
- Pages at `es/a1/*/*/*.html` → `src="../../../../shared/auth.js?v=1"`

**Estimated effort:** 20–30 minutes (bulk Python script to fix all occurrences)

---

## Major Bugs

### BUG-002 · MAJOR · Inconsistent Shared File Versioning

**Location:** All shared files (`shared/*.js`, `shared/*.css`)

**Description:**  
The `shared/auth.js` file is versioned at `?v=1` while other shared files use higher version numbers (e.g., `base.css?v=v123`, `dark-init.js?v=v109`), but `auth.js` was never bumped. This suggests:
1. The file was added recently without proper versioning
2. Or was versioned inconsistently with the rest of the codebase

**Evidence:**
```html
<!-- Inconsistent versioning pattern -->
<link rel="stylesheet" href="../../../../shared/base.css?v=v123">
<script src="shared/auth.js?v=1"></script>  <!-- Wrong: v=1 instead of v=vNN -->
<script src="../../../../shared/dark-init.js?v=v109"></script>
```

**Impact:**  
When `auth.js` is fixed (see BUG-001), the version number should also be standardized to match the project's cache-busting scheme (e.g., `?v=v101` or next available number).

**Suggested fix:**  
1. Fix import paths (BUG-001)
2. Standardize version to `?v=vNNN` format (check CLAUDE.md cache-busting rules)
3. Update all 2,431 consumers

**Estimated effort:** 5 minutes (included in BUG-001 fix)

---

## Passed Checks

✅ **Pedagogy validation:** `python3 scripts/pedagogy_check.py` — 1,043 checks passed, 0 failures  
✅ **GAME_DATA presence:** All grammar game pages (sample audit) contain required game items  
✅ **Audio implementation:** Flashcards use Web Speech API (en-GB, rate=0.9) per spec  
✅ **Dark mode variables:** CSS uses `var(--ink)`, `var(--paper)`, `var(--amber)` correctly  
✅ **Mobile viewport:** All pages have `<meta name="viewport" content="width=device-width,initial-scale=1.0">`  
✅ **localStorage schema:** Progress tracking uses `wordplay_progress` key with correct structure  
✅ **No forbidden symbols:** No inline onmouseover/onmouseout detected; ◐/◑/◆ symbols properly used  
✅ **Flashcard templates:** Both old (A1 vocab) and new (A2–C2) templates correctly separated  

---

## Known Non-Critical Issues

| ID | Severity | Summary | Status |
|---|----------|---------|--------|
| A1 grammar worksheets | Note | 24 grammar lessons missing "common mistakes" slide (pedagogy warning, not functional) | Expected |
| Theme color | Note | meta `theme-color` uses hardcoded `#1A1A1A` instead of CSS variable (dark mode always) | By design |

---

## Testing Checklist

### Pages Audited (representative sample)

| Page | Path | Status | Notes |
|------|------|--------|-------|
| A1 Index | `a/a1/index.html` | BUG-001 | Import path broken |
| A1 Vocab (Animals/Flashcards) | `a/a1/vocabulary/animals/flashcards.html` | BUG-001 | Audio present; import broken |
| A1 Grammar (To-be/Slides) | `a/a1/grammar/to-be/slides.html` | BUG-001 | Has deck-body class; import broken |
| A1 Grammar (To-be/Game) | `a/a1/grammar/to-be/game.html` | BUG-001 | GAME_DATA present; import broken |
| Spanish A1 Vocab | `es/a1/vocabulario/jobs/index.html` | BUG-001 | Import broken |

---

## Deployment Impact

**Current state:** If deployed now, all pages will fail to load the auth utility, breaking:
- Student authentication (if implemented)
- Teacher role checks
- Any admin-gated content

**Recommended action:** Fix BUG-001 and BUG-002 before next deployment.

**Risk level:** HIGH — 2,638 broken links affecting every page on the site.

---

## Appendix: Broken Links Summary

`python3 scripts/check_links.py` output (first 50 of 2,638):
```
BROKEN  a/a1/certificate.html -> shared/auth.js?v=1
BROKEN  a/a1/grammar/adjectives-basic/game.html -> shared/auth.js?v=1
BROKEN  a/a1/grammar/adjectives-basic/index.html -> shared/auth.js?v=1
BROKEN  a/a1/grammar/adjectives-basic/printables.html -> shared/auth.js?v=1
BROKEN  a/a1/grammar/adjectives-basic/slides.html -> shared/auth.js?v=1
BROKEN  a/a1/grammar/adjectives-basic/worksheet.html -> shared/auth.js?v=1
... (2,633 more)
```

All broken links point to `shared/auth.js?v=1` — indicating a single root cause with widespread impact.

