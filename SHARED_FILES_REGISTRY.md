# Shared Files Version Registry

**Last Updated:** 2026-06-06  
**Purpose:** Single source of truth for all `shared/` file versions used in cache-bust parameters.  
**Enforcement:** Pre-commit hook blocks commits if modifications lack version bumps.

---

## Active Shared Files

| File | Current Version | Use | Status |
|------|-----------------|-----|--------|
| `shared/auth.js` | v1 | Authentication helpers (login, role checks) | Core — loaded on all pages |
| `shared/base.css` | v124 | Design system, semantic tokens, dark mode | Core — loaded on all pages |
| `shared/dark-init.js` | v112 | Dark mode toggle, QR scan, search, XP badge | Core — loaded on all pages |
| `shared/store.js` | v107 | Progress storage, localStorage ↔ D1 sync | Core — loaded on game/worksheet/slides |
| `shared/game.js` | v111 | Dominio Mastery Game engine (4 stages) | Game-specific |
| `shared/worksheet.js` | v108 | Auto-grading for review exercises | Worksheet-specific |
| `shared/deck.js` | v114 | Slide deck navigation & speaker notes | Lesson-specific |
| `shared/game.css` | v112 | Game UI (screens, buttons, feedback) | Game-specific |
| `shared/slides.css` | v115 | Lesson slide styling | Lesson-specific |
| `shared/worksheet.css` | v106 | Worksheet/review styling | Worksheet-specific |
| `shared/print.css` | v102 | Printable materials styling | Print-specific |
| `shared/writing-grader.js` | v105 | Auto-grader for writing exercises | Writing assessment |
| `shared/sentence-grader.js` | v104 | Sentence-level validation & feedback | Writing assessment |
| `shared/print.js` | v102 | Print functionality & layout | Print-specific |
| `shared/i18n.js` | v123 | Internationalization helpers | Core — loaded on all pages |
| `shared/mascot.js` | v3 | Mascot animation state & interaction | All pages (optional) |
| `shared/mascot.css` | v2 | Mascot sprite animation rules | All pages (optional) |

---

## How to Update This Registry

**When modifying any `shared/` file:**

1. **Edit the file** — make your code changes in `shared/filename`
2. **Bump the version** — increment the "Current Version" in this table
3. **Run the bump script** — `python3 bump-versions.py` updates all 2,372 HTML files
4. **Verify** — check 2-3 sample HTML files to confirm version was updated
5. **Commit** — include both the file change AND version bumps in one commit

**Example:**
```bash
# Edit shared/store.js (add new feature)
# Update this file: shared/store.js v106 → v107
# Run:
python3 bump-versions.py
# Verify:
grep "store.js\?" index.html a/a1/index.html b/b1/vocabulary/travel-holidays/game.html
# Should show: shared/store.js?v=v107
# Then commit:
git add -A
git commit -m "feat: add sync method to store.js; bump version v106 → v107"
```

---

## Incident Log

| Date | File(s) | Issue | Fix |
|------|---------|-------|-----|
| 2026-06-06 | All shared files | 10 files modified without version bumps; Cloudflare immutable cache served stale code forever; all deployments hung with blank pages | Bumped all 10 file versions; updated 2,410 HTML files; deployed to main |

---

## Pre-Commit Hook

A `.git/hooks/pre-commit` script automatically blocks commits where shared files are
modified without version bumps. If you encounter this error:

```
❌ ERROR: shared/store.js was modified but version was not bumped in HTML files
Commit blocked: Shared file modifications require version parameter bumps.
Run: python3 bump-versions.py
```

**Resolution:**
1. Update the version number in this registry (above)
2. Run: `python3 bump-versions.py`
3. Commit again

---

## Testing Cache-Bust Updates

After deploying new versions:

1. **Hard-refresh the live site** (Cmd+Shift+R / Ctrl+Shift+R)
2. **Check DevTools Network tab** — verify responses are HTTP 200, not 304 (cached)
3. **Check browser console** — should be error-free
4. **Test the feature** — verify the change is live

If pages still hang or show errors after deploy:
- Check Cloudflare Pages deployment status (~2 min)
- Force clear browser cache (`DevTools → Application → Clear all`)
- Check `/shared/*` file modification times in deployment logs
