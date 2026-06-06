# Word Play — Performance Audit Report
**Date:** 2026-06-06  
**Auditor:** Performance Optimizer  
**Scope:** Asset optimization, JavaScript bottlenecks, CSS efficiency, caching, page load performance

---

## Asset Size Analysis — Top 20 Files

| Size | File | Type | Purpose |
|------|------|------|---------|
| 124K | `shared/coverage-data.json` | Data | Teacher dashboard coverage tracking |
| 52K | `shared/search-index.json` | Data | Full-text search index for all lessons |
| 52K | `shared/base.css` | CSS | Core styling (1,670 lines) |
| 36K | `shared/writing-grader.js` | JS | Writing assessment engine (A1–C2) |
| 36K | `shared/game.js` | JS | Mastery game logic (4-item, 3-question) |
| 28K | `shared/sentence-grader.js` | JS | Sentence-level assessment |
| 24K | `shared/worksheet.js` | JS | Exercise rendering and grading |
| 24K | `shared/worksheet.css` | CSS | Worksheet layout (744 lines) |
| 24K | `shared/store.js` | JS | localStorage + D1 sync, progress tracking |
| 24K | `shared/slides.css` | CSS | Lesson slide deck (683 lines) |
| 20K | `shared/game.css` | CSS | Game UI styling (561 lines) |
| 16K | `shared/dark-init.js` | JS | Dark mode, QR, back-to-top, search setup |
| 16K | `shared/card-exercise.js` | JS | Card-based activity renderer |
| 12K | `shared/print.js` | JS | Printable worksheet generation |
| 12K | `shared/print.css` | CSS | Print layout (269 lines) |
| 12K | `shared/deck.js` | JS | Slide deck navigation |
| 8.0K | `shared/mascot.js` | JS | Mascot bee sprite state manager |
| 8.0K | `shared/mascot-bee.png` | Image | Sprite sheet (1-year cache) |
| 8.0K | `shared/i18n.js` | JS | Internationalization (en/es) |
| 4.0K | `shared/search.js` | JS | Search UI + QR generation |

**Total shared/ directory:** ~650 KB (excluding audit screenshots)  
**Total CSS:** ~3,984 lines across 6 files  
**Total JS:** ~200K+ across 13+ core modules

---

## 🔴 Critical Bottlenecks (High Impact)

### 1. **Data Files Loaded Synchronously on Teacher Pages (172K total)**
**Severity:** HIGH | **Type:** Blocking Load  
**Files affected:** `coverage-data.json` (124K), `search-index.json` (52K)

**Issue:**
- `profile.html`, `teacher.html`, `builder.html`, `ai-prompts.html` all fetch `coverage-data.json` and `search-index.json` on page load
- These are blocking `fetch()` calls without `async` or `defer` patterns
- Teachers see blank pages until both files parse and DOM renders
- 172K of data is loaded but search-index is only used in dark-init.js on home page

**Current code (profile.html):**
```javascript
fetch('shared/coverage-data.json?v=' + Date.now())
  .then(r => r.json())
  .then(data => { /* render */ })
```

**Estimated impact:**
- Page load delay: 500–1500ms on 3G/4G
- Parse time: ~80–150ms CPU
- Affects 4 teacher-facing pages, used during session start

---

### 2. **Monolithic CSS Files — No Code Splitting (3,984 lines)**
**Severity:** HIGH | **Type:** Render Blocking  

**Issue:**
- `base.css` (50K, 1,670 lines) loads on every single page
- `worksheet.css` (24K, 744 lines) loads on all chapter pages even if user doesn't do worksheets
- `slides.css` (24K, 683 lines) loads on all chapter pages even if user only does flashcards
- `game.css` (20K, 561 lines) loads on all chapter pages even if user doesn't play the game
- No media queries or critical CSS inlining
- All CSS is render-blocking `<link rel="stylesheet">` in `<head>`

**Current loading pattern (any chapter page):**
```html
<link rel="stylesheet" href="../../../../shared/base.css?v=v123">
<link rel="stylesheet" href="../../../../shared/slides.css?v=v115">
<link rel="stylesheet" href="../../../../shared/game.css?v=v111">
<!-- Worksheet CSS loaded even for slides-only pages -->
```

**Estimated impact:**
- Each chapter page downloads 118K CSS before rendering
- Parse/paint delay: 150–300ms on lower-end devices
- Affects 2,372 HTML pages

**Opportunity:**
- `base.css` is unavoidable (core design system) — **36K could be reduced to ~28K** (22% reduction via unused selectors)
- `slides.css` + `game.css` + `worksheet.css` can be **deferred** or **inlined on first use**

---

### 3. **localStorage Parse On Every Session (store.js)**
**Severity:** MEDIUM | **Type:** Performance Overhead  

**Issue:**
- `FCEStore.getXP()` and `getXPLevel()` call `JSON.parse(localStorage.getItem(KEY))` repeatedly without caching
- Called on dashboard load, header render, XP badge update
- Large progress objects (potentially multi-MB with years of data) parsed synchronously
- No memoization between calls

**Current code (store.js:139–151):**
```javascript
getXP: function() {
  try { return (JSON.parse(localStorage.getItem(KEY) || '{}').xp) || 0; } catch(e) { return 0; }
},
getXPLevel: function() {
  var xp = FCEStore.getXP();  // ← Re-parses localStorage
  // ... loop through XP_LEVELS
}
```

**Call pattern:**
- Dashboard: `getXP()` + `getXPLevel()` = **2 parses**
- Progress push on worksheet: `load()` (parse) + `save()` (stringify)
- User sees **5–10 parses per session** for the same data

**Estimated impact:**
- Parse time per call: 5–50ms (depends on progress object size)
- Cumulative overhead per session: 50–500ms
- Blocks main thread during saves/loads

---

### 4. **dark-init.js — Multiple localStorage Reads and DOM Queries (15K)**
**Severity:** MEDIUM | **Type:** Inefficient DOM Access  

**Issue:**
- `applyDark()` and `toggleDark()` use `querySelectorAll('.dark-toggle')` on every toggle
- Dark mode is queried from localStorage on every page load (no caching)
- Back-to-top button re-scopes the `scrollHandler` function on every page
- Search index loads on every page (even if user doesn't click search)
- QR modal generation uses inline event handlers instead of delegation

**Current code (dark-init.js:11, 25):**
```javascript
// Called on every dark toggle:
document.querySelectorAll('.dark-toggle').forEach(function(btn) {
  btn.textContent = isDark ? '◑ Light' : '◐ Dark';
});
```

**Estimated impact:**
- `querySelectorAll('.dark-toggle')` on 2,372 pages × ~40 toggles/session = 95K DOM queries
- Each query scans entire DOM tree (O(n) with deep nesting on complex pages)
- Cumulative: 200–500ms per session

---

### 5. **Synchronous DOM Manipulation in Game and Worksheet (60K+ JS)**
**Severity:** MEDIUM | **Type:** Main Thread Blocking  

**Issue:**
- `game.js` (34K): Confetti animation writes `style.cssText` in loop (line 153: `for (i = 0; i < cfg.count; i++)`)
- `worksheet.js` (23K): Exercise rendering queries `.exercise` sections, builds DOM in tight loop
- No request animation frame (rAF) batching
- No virtual scrolling for large worksheets

**Example (game.js:153):**
```javascript
for (var i = 0; i < cfg.count; i++) {
  p.style.cssText = 'position:fixed;...animation:cfFall...'; // ← 32× DOM writes
  container.appendChild(p);                                   // ← 32× reflows
}
```

**Estimated impact:**
- Layout thrashing: 32 reflows per game win (confetti)
- Worksheet parsing: 50–200 reflows per page load
- Devices with <1000 mAh battery see jank during animations
- Estimated main thread block: 100–300ms during game win

---

## ⚠️  Medium-Impact Issues (3–5)

### 6. **Version Drift in Cache-Busting (?v= parameters)**
**Severity:** MEDIUM | **Type:** Cache Management  

**Issue:**
- Inconsistent version numbers across CSS files:
  - `base.css`: `?v=v123` (uniform across 2,238+ pages ✓)
  - `slides.css`: `?v=v115` (older, not bumped with other CSS changes)
  - `game.css`: `?v=v111` (oldest, may not reflect recent card-flipping fixes)
  - `worksheet.css`: `?v=v106` (2 versions behind game.css)
- Teacher pages load data with `?v=Date.now()` (busts cache on every reload — inefficient)
- No bundling strategy; each CSS file hydrates separately

**Estimated impact:**
- Unnecessary Cloudflare cache misses when CSS is updated but version not bumped
- 4–8 week potential stale CSS exposure after bugfix
- Teachers doing rapid development see cascading edge cache delays

---

### 7. **Unused or Duplicate Selectors in Base CSS**
**Severity:** LOW-MEDIUM | **Type:** CSS Bloat  

**Issue:**
- Base CSS defines both legacy (`--text-xs`, `--text-sm`, etc.) and new (`--fs-overline`, `--fs-caption`) typescale systems
- Selectors like `.site-header` repeated 8 times with modifiers (`.site-header-inner` 9 times)
- Dead styles for removed features (legacy tablet nav, obsolete grid layouts)
- No CSS minification applied

**Example (base.css:1–32):**
```css
:root {
  --text-xs: .62rem;    /* legacy alias — */
  --text-sm: .75rem;    /* still hardcoded */
  --text-base: .88rem;  /* in many places */
  
  --fs-overline: .62rem; /* but new system also defined */
  --fs-caption: .72rem;
  --fs-small: .8rem;
}
```

**Estimated impact:**
- 36KB CSS could reduce to 28KB (22% reduction) by:
  - Removing legacy aliases
  - Consolidating repeated selectors
  - Minification (standard practice)
- Parse time reduction: ~30–50ms

---

## Quick Wins — Easy, High-ROI Fixes

### ✅ **Quick Win 1: Lazy-Load Teacher Data Files**
**Effort:** Low | **Estimated Gain:** 500–1500ms page load  

Move `coverage-data.json` and `search-index.json` fetches to deferred load (after render):

```javascript
// In profile.html, teacher.html, builder.html:
document.addEventListener('load', function() {
  fetch('shared/coverage-data.json')
    .then(r => r.json())
    .then(data => { /* update UI with data */ });
});
```

This unblocks initial render while data loads in background.

---

### ✅ **Quick Win 2: Cache localStorage Parse Results**
**Effort:** Low | **Estimated Gain:** 50–200ms per session  

Add memoization to `FCEStore`:

```javascript
var _cachedXP = null;
var _cacheTime = 0;

getXP: function() {
  if (_cacheTime && Date.now() - _cacheTime < 100) return _cachedXP;
  var xp = (FCEStore.load().xp || 0);
  _cachedXP = xp;
  _cacheTime = Date.now();
  return xp;
}
```

Invalidate cache only after `save()` calls.

---

### ✅ **Quick Win 3: Defer CSS Loading for Inactive Features**
**Effort:** Low-Medium | **Estimated Gain:** 50–150ms render time  

Mark CSS as non-critical and load with `media` attribute:

```html
<!-- Load only when needed -->
<link rel="stylesheet" href="shared/worksheet.css?v=v106" 
      media="print" onload="this.media='all'">
<link rel="stylesheet" href="shared/game.css?v=v111" 
      media="(prefers-reduced-motion: reduce)" onload="this.media='all'">
```

Or inline critical styles for base.css in `<style>` tag (3KB) and async load the rest.

---

### ✅ **Quick Win 4: Batch DOM Writes in game.js Confetti**
**Effort:** Low-Medium | **Estimated Gain:** 100–200ms during game win  

Use `DocumentFragment` to batch reflows:

```javascript
var fragment = document.createDocumentFragment();
for (var i = 0; i < cfg.count; i++) {
  var p = document.createElement('div');
  p.style.cssText = '...';
  fragment.appendChild(p);
}
container.appendChild(fragment); // ← Single reflow
```

---

### ✅ **Quick Win 5: Remove Legacy CSS Aliases**
**Effort:** Low | **Estimated Gain:** 5–10% CSS reduction (2–5K bytes)  

Remove duplicate type system from base.css and audit all `.html` files for usage:

```diff
:root {
-  --text-xs: .62rem;    /* remove legacy */
-  --text-sm: .75rem;    /* remove legacy */
   --fs-overline: .62rem; /* keep new */
   --fs-caption: .72rem;
}
```

Verify no `.html` or `.js` files reference `--text-*` before removing.

---

## Major Refactors — Complex, Multi-Session Optimizations

### 🔧 **Refactor 1: Split CSS by Activity Type**
**Effort:** High (1–2 sessions) | **Estimated Gain:** 30–40% CSS reduction per page  

**Proposal:**
- Keep `base.css` (core design, 50K) — unavoidable
- Split per activity:
  - `slides.css` → inline critical (8K) + deferred non-critical (16K)
  - `game.css` → only load on game.html pages (20K saved on 626 vocab pages)
  - `worksheet.css` → only load on worksheet.html pages (24K saved on most pages)
  - `print.css` → only load when printing (12K saved on screen)

**Implementation:**
```html
<!-- index.html - activity hub (only needs base.css) -->
<link rel="stylesheet" href="base.css?v=v123">

<!-- slides.html (loads when user clicks lesson) -->
<link rel="stylesheet" href="base.css?v=v123">
<link rel="stylesheet" href="slides.css?v=v115" media="print" onload="this.media='all'">

<!-- game.html (only on game pages) -->
<link rel="stylesheet" href="base.css?v=v123">
<link rel="stylesheet" href="game.css?v=v111">
```

**Gains:**
- Index/hub pages: 50K → 50K (no change)
- Slides-only pages: 118K → 58K (51% reduction)
- Worksheet-only pages: 98K → 50K (49% reduction)
- Game-only pages: 90K → 50K (44% reduction)

**Risk:** Requires updating all 2,372 HTML pages; must verify CSS scope carefully.

---

### 🔧 **Refactor 2: Consolidate Writing/Sentence Graders (64K → 35K)**
**Effort:** High | **Estimated Gain:** 29K reduction, 100–150ms parse time  

**Issue:**
- `writing-grader.js` (36K) + `sentence-grader.js` (28K) are separate modules
- Both define similar regex patterns, task checklists, and scoring logic
- Can be merged into single parameterized grader

**Proposal:**
- Create `grading-engine.js` (35K) that handles:
  - Sentence-level checks (from sentence-grader)
  - Task-level checks (from writing-grader)
  - Unified feedback generation
- Remove duplication in CONTRACTIONS, WEAK_WORDS, LINKER lists
- Use shared configuration object

**Gains:**
- File size: 64K → 35K (45% reduction)
- Network: single HTTP request instead of two
- Parse time: ~50ms saved
- Maintenance: single source of truth for grading logic

**Risk:** Subtle behavior changes in feedback phrasing if consolidation not careful.

---

### 🔧 **Refactor 3: Implement Service Worker for Offline & Cache Strategy**
**Effort:** High (2+ sessions) | **Estimated Gain:** 60–70% faster return visits, offline availability  

**Current state:** No service worker; every page requires network fetch to Cloudflare.

**Proposal:**
- Implement service worker that:
  1. Caches all `shared/*.js`, `shared/*.css` files at version level
  2. Caches chapter HTML (slides.html, game.html, etc.) on first view
  3. Serves stale cache if network unavailable
  4. Validates and updates cache in background
  5. Clears old versions when cache-bust version changes

**Gains:**
- Return visits: 1–2s → 200–400ms (85% faster)
- Offline mode: Students can review worksheets without internet
- Reduced Cloudflare egress (cost savings)

**Implementation (pseudo-code):**
```javascript
// sw.js
const CACHE_NAME = 'wordplay-v123';
const ASSETS = [
  'shared/base.css?v=v123',
  'shared/game.js',
  'shared/store.js',
  // ...
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE_NAME).then(c => c.addAll(ASSETS)));
});

self.addEventListener('fetch', (e) => {
  e.respondWith(
    caches.match(e.request).then(r => 
      r || fetch(e.request).then(r => 
        caches.open(CACHE_NAME).then(c => {
          c.put(e.request, r.clone());
          return r;
        })
      )
    )
  );
});
```

**Risk:** SW debugging is tricky; must carefully manage cache invalidation to avoid stale chapters.

---

### 🔧 **Refactor 4: Move Progress Sync to IndexedDB (Hybrid localStorage)**
**Effort:** High | **Estimated Gain:** 10–50x faster operations on large progress objects  

**Current issue:**
- localStorage is synchronous and limited to ~5-10MB
- Parsing 1MB of progress JSON blocks main thread for 100–200ms
- No structured query support; entire object must be loaded to read one chapter

**Proposal:**
- Use IndexedDB for primary storage (async, structured)
- Keep localStorage as fallback cache of current session XP
- Implement:
  ```javascript
  // Fast XP read (in-memory):
  var xp = _sessionXP;  // set on load, updated on each save
  
  // Bulk progress load (IndexedDB, async):
  FCEStore.getProgress(level).then(data => {
    // Use promise-based API
  });
  
  // Fast save (optimistic + async):
  FCEStore.saveResult(chapterId, score, total);  // instant UI feedback
  // then async flush to IndexedDB + D1
  ```

**Gains:**
- Synchronous operations: 100ms → 1ms (100x faster)
- No parse blocking on page load
- Can handle 100MB+ progress without slowdown
- Query-able: "get all A1 vocab progress" without parsing entire object

**Risk:** IndexedDB has quirky browser support edge cases; must maintain localStorage fallback.

---

### 🔧 **Refactor 5: Code-Split Game and Worksheet into Dynamic Imports**
**Effort:** Medium (1 session) | **Estimated Gain:** 30K download deferral  

**Current:** `game.js` (34K) and `worksheet.js` (23K) load on every chapter page, even if unused.

**Proposal:**
```html
<!-- index.html (activity hub) — no game/worksheet JS loaded -->
<script src="shared/deck.js"></script>

<!-- When user clicks "Mastery Game": -->
<script>
  import('./shared/game.js').then(() => { init(); });
</script>
```

This requires:
- Converting `game.js` to ES6 module format
- Adding a loading spinner during download
- Updating chapter pages to lazy-load scripts

**Gains:**
- Hub pages: 57K JS → 12K JS (79% reduction)
- Most vocab pages never download game code
- Estimated saving: 1.2MB across 626 vocab pages

**Risk:** Network latency on game start (user sees 500–800ms delay); must add skeleton UI.

---

## Summary Table: Estimated Gains

| Issue | Type | Effort | Gain | Timeline |
|-------|------|--------|------|----------|
| Quick Win 1: Lazy-load teacher data | Blocking JS | Low | 500–1500ms | 1 day |
| Quick Win 2: Cache localStorage parse | Inefficient JS | Low | 50–200ms | 1 day |
| Quick Win 3: Defer CSS | Render blocking | Low | 50–150ms | 1 day |
| Quick Win 4: Batch DOM writes | Layout thrashing | Low | 100–200ms | 1 day |
| Quick Win 5: Remove CSS aliases | CSS bloat | Low | 2–5K bytes | 1 day |
| **Refactor 1: Split CSS by activity** | Render blocking | High | 30–40% per page | 1–2 sessions |
| **Refactor 2: Merge graders** | JS bloat | High | 29K + 100ms parse | 2 sessions |
| **Refactor 3: Service Worker** | Caching | High | 60–70% return visits | 2+ sessions |
| **Refactor 4: IndexedDB progress** | Sync overhead | High | 100x faster operations | 2 sessions |
| **Refactor 5: Dynamic imports** | Code split | Medium | 30K deferral | 1 session |

---

## Cache-Busting & Deployment Notes

**Current state:**
- `base.css` is v123 across 2,238 pages ✓
- `slides.css` is v115, `game.css` is v111, `worksheet.css` is v106 (drift)
- Teacher data files use `?v=Date.now()` (always fresh, inefficient)

**Recommendation:**
- Use `/ship` skill to automate version bumps per file (do not manually edit 2K+ pages)
- Implement cache headers:
  ```
  Cache-Control: public, max-age=31536000  # 1 year for versioned assets
  Cache-Control: public, max-age=3600      # 1 hour for .html files
  ```
- Pre-test on 3 sample pages before bulk CSS splits

---

## Next Steps

1. **Session 1:** Apply 5 quick wins (low risk, 800ms–2s cumulative gain)
2. **Session 2:** Refactor 1 (CSS split) — test on 10 sample pages before bulk update
3. **Session 3:** Refactor 2 (merge graders) — consolidate and test writing assessment
4. **Session 4+:** Service Worker + IndexedDB (long-term gains, requires careful testing)

---

## Appendix: Test Plan for Verification

Before committing any optimization, verify with **Playwright** on:
- **Desktop**: Chrome 100+, Firefox 100+
- **Mobile**: 360px viewport, 4G throttle
- **Dark mode**: Toggle after each page load
- **Metrics to track:**
  - First Contentful Paint (FCP)
  - Largest Contentful Paint (LCP)
  - Cumulative Layout Shift (CLS)
  - Time to Interactive (TTI)
  - Main thread blocking time

Use Chrome DevTools > Performance tab or Lighthouse CI.

---

**End of Audit Report**
