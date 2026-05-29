# /frontend-design

Design-system-compliant front-end implementation workflow. Takes a task description as args.

## Non-negotiables (check before every edit and again at end)
- Accent colour: amber only — `#E8A020` / `var(--amber)` / `var(--accent)`. No other accent colours.
- No emojis in HTML, CSS, or JS. Allowed symbols only: ◐ ◑ ◆
- Dark mode must work on every element. Use `body.dark` overrides with tokens from `shared/base.css :root`.
- Cache-bust: any `shared/` file touched must have its `?v=vNN` bumped in ALL consumer pages.
- Bulk edits: use Edit tool file-by-file for < 50 files. Python script only for 50+ files; verify on 2–3 samples first.

## Steps

### 0. Guard: require args
If no args were given, reply:
"Describe the front-end task. Example: `/frontend-design implement option 2 from brainstorm — card grid refresh`"
Then stop.

### 1. Read design tokens
Read `shared/base.css`. Extract the `:root` block. Keep this in working context — never invent a new CSS variable without first checking this block.

### 2. Identify affected files
Run:
```
grep -rn "<component-keyword>" --include="*.html" --include="*.css" . | head -40
```
Replace `<component-keyword>` with the relevant class name or element from the task.
List every file to edit. Group them: shared/ files first, then page HTML files.

### 3. Implement shared/ changes first
For each shared/ file changed:
a. Edit with the Edit tool.
b. Find the current version: `grep -r "shared/<filename>?v=" --include="*.html" . | head -1`
c. Increment NN by 1.
d. Update ALL consumers: Python with `glob.glob('**/*.html', recursive=True)` string-replace.
e. Verify zero old-version refs: `grep -r "shared/<filename>?v=v<OLD>" --include="*.html" . | wc -l` must output 0.

### 4. Implement page-level changes (file-by-file)
For each affected HTML/CSS file not in shared/:
a. Read the file to confirm current state.
b. Edit with the Edit tool — one file at a time.
c. After each edit, check the edited block for hardcoded colours (hex or rgb) that lack a `body.dark` override. Fix before moving on.

### 5. Dark-mode verification
After all edits:
- Navigate a representative affected page via Playwright MCP.
- Click the dark toggle.
- Take a screenshot.
- Confirm: no light background in dark mode, amber accent present, no invisible text.
- If a violation is found, return to Step 4 for that file.

### 6. Final design-system scan
Scan every edited file:
- No emojis outside ◐ ◑ ◆: `grep -Pn "[^\x00-\x7F◐◑◆›✓✕←→↓↑·«»…''""▸▶◀•—–×÷]" <file>`
- No off-palette hex colours (non-amber, non-greyscale)
- No `onmouseover`/`onmouseout` inline handlers — use CSS hover instead

Fix any violations before proceeding.

### 7. Playwright audit
Invoke `/playwright-audit` scoped to the page types touched (slides / worksheet / game / index).
Fix any new bugs introduced by this change before deploying.

### 8. Ship
Invoke `/ship`.
