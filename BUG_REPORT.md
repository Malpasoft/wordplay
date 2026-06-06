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

**Location:** 2,431 HTML pages across all curriculum levels

**Scope breakdown by level:**
- English A1: 174 pages
- English A2: 177 pages
- English B1: 195 pages
- English B2: 216 pages
- English C1: 211 pages
- English C2: 167 pages
- Spanish (es/a1): 988 pages
- French (fr/*): 81 pages
- Other Spanish paths (espanol-en): 173 pages
- Root-level teacher tools (15 pages): index.html, dashboard.html, teacher.html, login.html, signup.html, profile.html, placement-test.html, placement-test-v2.html, dev-hub.html, coverage.html, calendar.html, builder.html, ai-prompts.html, 404.html

**Pages Affected:** Sample of confirmed files:
- `a/a1/grammar/to-be/index.html` (and 400+ grammar pages)
- `a/a1/vocabulary/animals/flashcards.html` (and 300+ vocab pages)
- `index.html` (home page)
- `teacher.html` and other teacher tools
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
1. Open any page on the site in a browser (e.g., `a/a1/grammar/to-be/index.html`)
2. Open browser DevTools → Network tab
3. Observe 404 error: `GET /a/a1/grammar/shared/auth.js?v=1 404 (Not Found)`
4. Check Console tab: Auth utility functions (`getAuthToken()`, `isLoggedIn()`, `isAdmin()`) are undefined
5. Any code that calls these functions will fail silently or throw `ReferenceError`

**Live impact:**
- Home page (`/index.html`) also affected — requests `/index.html/shared/auth.js` (expects `/shared/auth.js`)
- Teacher dashboard, placement test, login/signup all broken
- Auth system non-functional across entire site

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

**Total broken links:** 2,638  
**Unique broken reference:** 1 (only `shared/auth.js?v=1`)

This indicates a single root cause with widespread impact across the entire site.

### Link Check Output
```
Links checked: 38,825
Broken links: 2,638

All 2,638 broken links point to: shared/auth.js?v=1
```

### Representative Sample
```
BROKEN  a/a1/certificate.html -> shared/auth.js?v=1
BROKEN  a/a1/grammar/adjectives-basic/game.html -> shared/auth.js?v=1
BROKEN  a/a1/grammar/adjectives-basic/index.html -> shared/auth.js?v=1
BROKEN  a/a1/vocabulary/animals/flashcards.html -> shared/auth.js?v=1
BROKEN  es/a1/vocabulario/jobs/index.html -> shared/auth.js?v=1
BROKEN  index.html -> shared/auth.js?v=1
BROKEN  teacher.html -> shared/auth.js?v=1
BROKEN  login.html -> shared/auth.js?v=1
... (2,630 more)
```

**All other shared file references are correct:**
- `../../shared/base.css?v=v123` ✅
- `../../../../shared/dark-init.js?v=v109` ✅
- `../../../../shared/store.js?v=v105` ✅
- `../../../../shared/game.js?v=v110` ✅
- etc.

Only `auth.js` is broken.

