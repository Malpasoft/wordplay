# /qa

Run all pre-push quality checks in one blocking gate. Fails loud on any error.
Run this before every `/ship`.

## Steps

### 1. Python checks (run all three, collect all output)

```bash
python3 scripts/pedagogy_check.py
python3 scripts/check_links.py
python3 scripts/check_structure.py
```

- `pedagogy_check.py`: must be **0 failures**. Warnings are reported but non-blocking.
- `check_links.py`: any broken internal link = fail.
- `check_structure.py`: structural errors = fail.

If any check produces failures, **stop here**. List every failure, grouped by script.
Do not proceed to Playwright. Do not ship. Fix and re-run `/qa`.

### 2. Triple-viewport Playwright audit

If all Python checks pass, run the visual audit across three viewports:

| Viewport       | Width  | Notes                       |
|----------------|--------|-----------------------------|
| Desktop        | 1280px | default                     |
| Dark mode      | 1280px | add `?dark=1` or toggle JS  |
| Mobile         | 360px  | portrait                    |

For each recently changed page (from `git diff --name-only HEAD~1..HEAD`), navigate to it
in each viewport and check:

- No layout overflow or clipping
- Dark mode applies to every element (no un-themed white boxes)
- Amber accent (`var(--amber)`) renders, no hardcoded hex visible
- No emoji in rendered UI (allowed symbols: ◐ ◑ ◆ only)
- Interactive elements (buttons, cards, toggles) are reachable at 360px

Screenshot any failure and report the page + viewport + description. Do NOT auto-fix
visual bugs here — just report. Fixes go in the main conversation.

### 3. Report

Output a single pass/fail summary:

```
QA PASS — all checks clean, N pages audited across 3 viewports.
Ready for /ship.
```

or:

```
QA FAIL
  pedagogy_check.py: 2 failures
    - es/a1/vocabulary/colours/flashcards.html: missing IPA
    - ...
  Playwright 360px: 1 issue
    - en/b2/grammar/conditionals/slides.html overflows at 360px [screenshot attached]

Fix the above before shipping.
```

Do NOT commit, push, or run `/ship` from within this skill.
