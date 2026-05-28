#!/usr/bin/env python3
"""
Bulk-fix all game.html files:
  1. Add gFinalPct stat + gMasteryMap to completion screen
  2. Bump game.css ref from v104 -> v105
  3. Bump game.js ref from v104 -> v105

Idempotent: skips files that already contain gFinalPct.
"""
import glob, os, sys

# Combined single-pass pattern: capture from the gFinalStreak line through
# the stats-row closing div, then insert both new elements before game-btn-row.
COMBINED_OLD = (
    '</div><div class="game-stat-label">Best streak</div></div>\n'
    '        </div>\n'
    '        <div class="game-btn-row">'
)
COMBINED_NEW = (
    '</div><div class="game-stat-label">Best streak</div></div>\n'
    '          <div class="game-stat"><div class="game-stat-val" id="gFinalPct">0%</div>'
    '<div class="game-stat-label">Mastered</div></div>\n'
    '        </div>\n'
    '        <div id="gMasteryMap"></div>\n'
    '        <div class="game-btn-row">'
)

VERSION_PATTERNS = [
    ('game.css?v=v104', 'game.css?v=v105'),
    ('game.js?v=v104', 'game.js?v=v105'),
]

files = sorted(glob.glob('/home/user/wordplay/**/game.html', recursive=True))

dry_run = '--dry-run' in sys.argv
sample = '--sample' in sys.argv  # only process first 5

if sample:
    files = files[:5]

changed = 0
skipped = 0
errors = []

for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'gFinalPct' in content:
        skipped += 1
        continue

    new_content = content.replace(COMBINED_OLD, COMBINED_NEW)
    for old, new in VERSION_PATTERNS:
        new_content = new_content.replace(old, new)

    if new_content == content:
        errors.append(path)
        continue

    if not dry_run:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
    changed += 1

print(f'Changed: {changed}  Skipped (already done): {skipped}  Errors: {len(errors)}')
if errors:
    print('\nFiles with no matching pattern:')
    for e in errors[:30]:
        print(' ', e)
