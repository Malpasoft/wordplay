# /playwright-audit

Walk every lesson page as a student, check for visual and functional errors, save progress after each level so the audit can resume if interrupted.

## Checkpoint file
`.claude/playwright-audit-state.json` — created on first run, updated after every level.

Structure:
```json
{
  "started": "2026-01-01T00:00:00Z",
  "last_updated": "...",
  "current_level": "b1",
  "pages_done": 42,
  "pages_total": 0,
  "bugs": [],
  "levels": {
    "a1": { "status": "done", "pages": {...} },
    "b1": { "status": "in-progress", "pages": {...} }
  }
}
```

Each page entry: `{ "status": "ok|error|skip", "errors": [], "checked_at": "..." }`

## Steps

### 0. Load or create checkpoint
```python
import json, os, datetime
STATE_FILE = '.claude/playwright-audit-state.json'
if os.path.exists(STATE_FILE):
    state = json.load(open(STATE_FILE))
    print(f"Resuming — last updated {state['last_updated']}, level {state['current_level']}")
else:
    state = {
        "started": datetime.datetime.utcnow().isoformat() + "Z",
        "last_updated": None,
        "current_level": "a1",
        "pages_done": 0,
        "pages_total": 0,
        "bugs": [],
        "levels": {}
    }
```

### 1. Discover all auditable pages
Collect every `worksheet.html`, `game.html`, `slides.html`, and `placement-test.html`.
```python
import glob
PAGE_TYPES = ['worksheet.html', 'game.html', 'slides.html']
LEVELS = ['a/a1','a/a2','b/b1','b/b2','c/c1','c/c2','es/a1']
pages = []
for lv in LEVELS:
    for ptype in PAGE_TYPES:
        pages.extend(glob.glob(f'{lv}/**/{ptype}', recursive=True))
pages.append('placement-test.html')
state['pages_total'] = len(pages)
```
Filter out pages already in `state['levels'][lv]['pages']` with `status: ok`.

### 2. Start local server
```bash
cd /home/user/wordplay && python3 -m http.server 8099 &
SERVER_PID=$!
trap "kill $SERVER_PID" EXIT
```
Base URL: `http://localhost:8099`

### 3. For each page — run the audit routine

**3a. Navigate and wait for load**
Use `mcp__playwright__browser_navigate` to `http://localhost:8099/<page-path>`.
Use `mcp__playwright__browser_wait_for` — selector `body`, timeout 5000ms.

**3b. Take screenshot** (for visual review and bug evidence)
`mcp__playwright__browser_take_screenshot` — save path `".claude/playwright-audit-screenshots/<page-path-slug>.png"`.

**3c. Check for JS console errors**
`mcp__playwright__browser_console_messages` — flag any `error` level entries that aren't network-404s for fonts/favicons.

**3d. Page-type-specific checks**

*Worksheet:*
- `mcp__playwright__browser_snapshot` — verify question options render (look for `.ws-option` or `.opt-btn` elements).
- Click the first option, verify feedback appears (`.ws-feedback` or `.feedback` is visible).
- Verify the explanation is non-empty.
- Check dark mode: `mcp__playwright__browser_evaluate` `document.body.classList.toggle('dark')` then screenshot — verify no white-on-white.

*Game:*
- Click "Start" button, verify play screen appears (`#gamePlay.active`).
- Verify amber progress bar renders (`#gProgressBar`).
- Verify the mode badge (`#gModeTag`) is non-empty.
- Click the first answer option, verify feedback appears within 2s.

*Slides:*
- Verify `.deck-body` class on `<body>` (required by design system).
- Verify progress bar (`#deck-progress-fill`) exists.
- Simulate swipe right: `mcp__playwright__browser_evaluate` a touch-event sequence on `.deck-slide`.
- Verify slide advances.

**3e. Dark mode toggle**
Click `.dark-toggle` button. Take screenshot. Verify no elements have `background: white` or `color: #000` in computed style that would be unreadable.

**3f. Record result**
```python
entry = {"status": "ok", "errors": [], "checked_at": datetime.datetime.utcnow().isoformat()}
# or
entry = {"status": "error", "errors": ["JS error: ReferenceError: foo is not defined (game.js:42)"], ...}
```

### 4. Save checkpoint after every 10 pages
```python
state['last_updated'] = datetime.datetime.utcnow().isoformat() + "Z"
state['pages_done'] += 1
json.dump(state, open(STATE_FILE, 'w'), indent=2)
```
This ensures a context-limit interruption loses at most 10 pages of work.

### 5. File bugs
For each error found, create a structured bug entry:
```python
bug = {
  "id": f"BUG-{len(state['bugs'])+1:03d}",
  "page": page_path,
  "type": "js-error|layout|dark-mode|pedagogy",
  "severity": "P0|P1|P2",
  "description": "...",
  "repro": "Navigate to X, do Y, observe Z",
  "screenshot": "path/to/screenshot.png",
  "suggested_fix": "..."
}
state['bugs'].append(bug)
```

At the end, write a bug report to `.claude/playwright-audit-report.md`.

### 6. Summary
After completing a level, print:
```
Level A1: 47 pages — 45 ok, 2 errors (BUG-001, BUG-002)
```
Save checkpoint and ask: "Continue to next level, or stop here?"

### 7. Bug report format (`.claude/playwright-audit-report.md`)
```markdown
# Playwright Audit Report — <date>

## Summary
- Pages audited: N
- Passed: N
- Errors: N (P0: N, P1: N, P2: N)

## Bugs

### BUG-001 · P0 · js-error
**Page:** a/a1/grammar/present-simple/game.html
**Description:** ReferenceError: FCEStore is not defined
**Repro:** Open page, click Start
**Screenshot:** .claude/playwright-audit-screenshots/...
**Suggested fix:** Add store.js script tag before game.js
```

## Resuming after interruption
If the context limit is hit mid-audit:
1. The checkpoint file is already saved.
2. In the next session, run `/playwright-audit` again.
3. The skill loads the checkpoint, skips completed pages, and resumes from where it left off.
4. All previously found bugs are preserved in `state['bugs']`.
