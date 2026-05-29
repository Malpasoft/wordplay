# /playwright-audit

Walk every lesson page as a student, in curriculum order, fixing bugs immediately as they are found. Save progress after each chapter so the audit can resume after any interruption.

## Goal

Produce a fully-working course (placement-test → A1 → A2 → B1 → B2 → C1 → C2 → ES/A1) with zero open P0/P1 bugs. Fixes that touch shared files cascade forward — fix once, benefit every chapter that follows.

---

## Checkpoint file

`.claude/playwright-audit-state.json` — created on first run, updated after every chapter.

```json
{
  "started": "2026-01-01T00:00:00Z",
  "last_updated": "...",
  "current_level": "a1",
  "current_chapter": "grammar/adjectives-basic",
  "pages_done": 12,
  "pages_total": 0,
  "bugs": [],
  "levels": {
    "placement-test": { "status": "done", "chapters": {} },
    "a1": {
      "status": "in-progress",
      "chapters": {
        "grammar/adjectives-basic": {
          "status": "ok|fixed|open",
          "pages": {
            "slides.html": { "status": "ok", "errors": [], "checked_at": "..." },
            "worksheet.html": { "status": "fixed", "errors": ["BUG-001"], "checked_at": "..." },
            "game.html": { "status": "ok", "errors": [], "checked_at": "..." }
          }
        }
      }
    }
  }
}
```

---

## Page order (strict — do not skip ahead)

```
1. placement-test.html

2. a/a1/grammar/*   (alphabetical chapter names)
3. a/a1/vocabulary/*
4. a/a1/writing/*

5. a/a2/grammar/*
6. a/a2/vocabulary/*
7. a/a2/writing/*

8.  b/b1/grammar/*
9.  b/b1/vocabulary/*
10. b/b1/writing/*

11. b/b2/grammar/*
12. b/b2/vocabulary/*
13. b/b2/writing/*

14. c/c1/grammar/*
15. c/c1/vocabulary/*
16. c/c1/writing/*

17. c/c2/grammar/*
18. c/c2/vocabulary/*
19. c/c2/writing/*

20. es/a1/gramatica/*
21. es/a1/vocabulario/*  (or vocabulary/)
```

Within each chapter the page order is: **slides.html → worksheet.html → game.html**.
Skip a page if the file does not exist (redirect pages and stub pages are expected).

---

## Steps

### 0. Load or create checkpoint

```python
import json, os, datetime, glob

STATE_FILE = '/home/user/wordplay/.claude/playwright-audit-state.json'
if os.path.exists(STATE_FILE):
    state = json.load(open(STATE_FILE))
    print(f"Resuming — level {state['current_level']}, chapter {state['current_chapter']}, {state['pages_done']} pages done")
else:
    state = {
        "started": datetime.datetime.utcnow().isoformat() + "Z",
        "last_updated": None,
        "current_level": "placement-test",
        "current_chapter": None,
        "pages_done": 0,
        "pages_total": 0,
        "bugs": [],
        "levels": {}
    }

def save():
    state['last_updated'] = datetime.datetime.utcnow().isoformat() + "Z"
    json.dump(state, open(STATE_FILE, 'w'), indent=2)
```

### 1. Start local server (if not already running)

```bash
cd /home/user/wordplay
lsof -i:8099 | grep LISTEN || python3 -m http.server 8099 &>/tmp/server.log &
```

Base URL: `http://localhost:8099`

### 2. Discover all chapters

```python
BASE = '/home/user/wordplay'
LEVEL_DIRS = [
    ('placement-test', []),
    ('a1', ['a/a1/grammar', 'a/a1/vocabulary', 'a/a1/writing']),
    ('a2', ['a/a2/grammar', 'a/a2/vocabulary', 'a/a2/writing']),
    ('b1', ['b/b1/grammar', 'b/b1/vocabulary', 'b/b1/writing']),
    ('b2', ['b/b2/grammar', 'b/b2/vocabulary', 'b/b2/writing']),
    ('c1', ['c/c1/grammar', 'c/c1/vocabulary', 'c/c1/writing']),
    ('c2', ['c/c2/grammar', 'c/c2/vocabulary', 'c/c2/writing']),
    ('es-a1', ['es/a1/gramatica', 'es/a1/vocabulario', 'es/a1/vocabulary']),
]
PAGE_ORDER = ['slides.html', 'worksheet.html', 'game.html']
```

For each level, list subdirectories alphabetically. For each chapter, check which of `slides.html`, `worksheet.html`, `game.html` exist (skip missing ones). `placement-test` has only `placement-test.html`.

Skip chapters where ALL pages already have `status: ok` or `status: fixed` in the checkpoint.

### 3. Audit routine for each page

**3a. Detect redirect pages (skip them)**
```python
with open(f'{BASE}/{page_path}') as f:
    content = f.read()
if 'http-equiv="refresh"' in content or 'location.replace(' in content:
    # Mark as skip
    continue
```

**3b. Navigate**
Use `mcp__playwright__browser_navigate` to `http://localhost:8099/<page_path>`.

**3c. Check for JS console errors**
`mcp__playwright__browser_console_messages` — flag any `error` level entries that are not 404s for fonts/favicons/images.

**3d. Page-type checks** (see §4 below)

**3e. Record result**
```python
entry = {"status": "ok", "errors": [], "checked_at": datetime.datetime.utcnow().isoformat() + "Z"}
```

### 4. Page-type checks

#### placement-test.html
- `mcp__playwright__browser_snapshot` — verify option buttons render
- Click an incorrect option — verify feedback appears with non-empty explanation text
- Verify progress bar advances (check `#pt-progress-fill` width > 0)

#### slides.html
- `mcp__playwright__browser_snapshot` — capture
- **deck-body check:** verify `<body class="deck-body">` is present (grep the raw HTML file — faster than DOM query)
- **Forbidden symbol check:** accessibility snapshot text must not contain ⚠ ✗ ✎ 🔥 ❌ ★. NOTE: ✓ in nav badges is BUG-005 (tracked separately — do not re-log per page)
- **deck-progress-fill:** `#deck-progress-fill` element must exist in snapshot
- Dark mode: click `.dark-toggle`, take screenshot, verify no obviously broken contrast

#### worksheet.html
- `mcp__playwright__browser_snapshot` — verify at least one question renders (look for `button` elements or `input` elements)
- **EXPLANATIONS coverage:** `grep -c "window.EXPLANATIONS" <file>` — if zero, flag as pedagogy bug
- Click an incorrect option — verify feedback text is non-empty (not just "Not quite.")
- Dark mode toggle

#### game.html
- **GAME_DATA check:** `grep -c "window.GAME_DATA" <file>` and verify `items` array is present
- `mcp__playwright__browser_snapshot` — click Start button
- Verify `#gModeTag` is non-empty in snapshot
- Click first answer option — verify feedback appears
- Dark mode toggle

### 5. Fix-as-you-go protocol

When a bug is found:

**Step A — Classify**
- `isolated`: this one file only
- `systemic`: same root cause affects 3+ files OR the bug is in a shared file (shared/*.css, shared/*.js)

**Step B — Fix**

*Isolated fix:*
1. Edit the file directly
2. Re-navigate to verify the symptom is gone
3. Mark page `status: "fixed"`, add bug entry to `state['bugs']`

*Systemic fix:*
1. Log the bug once with a note of how many files are affected
2. Apply the bulk fix:
   - **Missing EXPLANATIONS** → run `python3 scripts/gen_explanations.py` (covers current level)
   - **Forbidden symbol in shared file** → edit shared file, bump `?v=vNN`, run Python to update all consumers
   - **Missing `deck-body`** → Python script to add class to all affected slides.html body tags
   - **Nav `✓` badges (BUG-005)** → Python script to replace all `✓` in nav tab JS with `◆` or plain text across all HTML files
   - **`theme-color: var(--ink)`** → Python script already exists in prior sessions; re-run if needed
3. After bulk fix: re-navigate the triggering page to verify
4. Mark ALL affected pages `status: "systemic-fixed"` — do NOT re-test each one individually
5. Save checkpoint

**Systemic fix trigger table:**

| Symptom on page | Bulk action |
|-----------------|-------------|
| `window.EXPLANATIONS` missing from worksheet | `python3 scripts/gen_explanations.py` |
| `window.GAME_DATA` missing (non-redirect game.html) | Manually add from slides.html content; check all level game pages |
| ⚠ / ✎ / 🔥 / ❌ / ★ visible in snapshot | Edit shared CSS/JS file once; bump version; update consumers |
| `<body>` lacks `deck-body` on slides page | Python: add class to all missing slides.html body tags |
| `onmouseover` / `onmouseout` inline on index pages | Python: strip all; CSS .sect-card:hover already handles hover |
| `theme-color: var(--ink)` in meta tag | Python: replace all with `#1A1A1A` |

**Step C — Commit after each level**
After all chapters in a level pass (or are fixed), commit and push:
```
git add -u
git commit -m "fix(audit): <level> — <N> bugs fixed, all chapters green"
git push -u origin claude/github-workflow-setup-98Fbf
```

### 6. Save checkpoint after every chapter

```python
state['levels'].setdefault(level_key, {'status': 'in-progress', 'chapters': {}})
state['levels'][level_key]['chapters'][chapter_key] = {
    'status': chapter_status,  # 'ok', 'fixed', or 'open'
    'pages': chapter_pages
}
state['pages_done'] += pages_in_chapter
state['current_chapter'] = next_chapter
save()
```

### 7. Level summary

After finishing all chapters in a level, print:
```
────────────────────────────────────────
Level A1: 40 chapters — 37 ok, 3 fixed, 0 open
  BUG-009 (fixed): grammar/present-simple/game.html — GAME_DATA missing
  BUG-010 (systemic-fixed): 5 worksheets missing EXPLANATIONS → gen_explanations.py
────────────────────────────────────────
```

Mark the level `status: "done"` in state, advance `current_level`, save.

### 8. Write final report

After all levels complete, write `.claude/playwright-audit-report.md`:

```markdown
# Playwright Audit Report — <date>

## Summary
- Pages audited: N
- Passed: N
- Fixed: N (isolated: N, systemic: N)
- Open: N

## Fixed Bugs

### BUG-009 · P1 · js-error (isolated)
**Page:** a/a1/grammar/present-simple/game.html
**Description:** window.GAME_DATA missing
**Fix applied:** Added 8 grammar items from slides.html content

## Open Bugs (require manual review)
...
```

---

## Resuming after interruption

1. The checkpoint file is saved after every chapter.
2. Run `/playwright-audit` again in the next session.
3. The skill loads the checkpoint, skips completed chapters, and resumes from `current_level` / `current_chapter`.
4. All previously found and fixed bugs are preserved in `state['bugs']`.

---

## Known pre-existing bugs (already fixed — do not re-log)

| ID | Summary | Fixed |
|----|---------|-------|
| BUG-001 | 13 A1 grammar worksheets missing EXPLANATIONS | 2026-05-28 |
| BUG-002 | game-term hidden behind sticky nav on all game pages | 2026-05-28 |
| BUG-003 | slides.css .watch-out::before injected forbidden ⚠ (201 pages) | 2026-05-29 |
| BUG-004 | es/a1/gramatica/have-got/game.html missing GAME_DATA | 2026-05-28 |
| BUG-005 | es/a1 vocab index pages: 18 broken links to missing files | 2026-05-29 |
| BUG-006 | writing-grader.js section headers used ✓ ⚠ ✎ | 2026-05-29 |
| BUG-007 | b2/vocab/applied-grammar-prepositions worksheet missing EXPLANATIONS | 2026-05-29 |
| BUG-008 | c1/vocab/applied-grammar-register + c2/vocab/applied-grammar-collocation missing EXPLANATIONS | 2026-05-29 |
