#!/usr/bin/env python3
"""
Fix old-template game.html files (those using .game-complete class).
- Insert gFinalPct + gMasteryMap after the score/streak paragraph
- Strip &#10003; glyph from completion eyebrow
- Bump game.css / game.js from v104 to v105 (if not already done)
"""
import glob, sys

OLD_TEMPLATE_FILES = [
    '/home/user/wordplay/a/a1/grammar/can-cant/game.html',
    '/home/user/wordplay/a/a1/grammar/demonstratives/game.html',
    '/home/user/wordplay/a/a1/grammar/going-to-future/game.html',
    '/home/user/wordplay/a/a1/grammar/have-got/game.html',
    '/home/user/wordplay/a/a1/grammar/possessive-adjectives/game.html',
    '/home/user/wordplay/a/a1/grammar/prepositions-of-place/game.html',
    '/home/user/wordplay/a/a1/grammar/present-continuous/game.html',
    '/home/user/wordplay/a/a1/grammar/simple-past-irregular/game.html',
    '/home/user/wordplay/a/a1/grammar/simple-past-regular/game.html',
    '/home/user/wordplay/a/a1/grammar/to-be/game.html',
    '/home/user/wordplay/es/a1/gramatica/present-simple/game.html',
    '/home/user/wordplay/es/a1/gramatica/to-be/game.html',
]

# Anchor: both variants of the score/streak closing tags
ANCHORS = [
    'id="gFinalStreak"></strong></p>',
]
INSERT_AFTER = (
    '<div id="gFinalPct" style="font-family:var(--font-serif);font-size:1.4rem;'
    'font-weight:700;color:var(--accent);text-align:center;margin:8px 0"></div>\n'
    '      <div id="gMasteryMap" style="margin:16px 0;text-align:left;"></div>'
)

dry_run = '--dry-run' in sys.argv
changed = 0
skipped = 0

for path in OLD_TEMPLATE_FILES:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f'NOT FOUND: {path}')
        continue

    if 'gFinalPct' in content:
        skipped += 1
        continue

    new_content = content

    # Insert gFinalPct + gMasteryMap after the score/streak line
    for anchor in ANCHORS:
        if anchor in new_content:
            new_content = new_content.replace(anchor, anchor + '\n      ' + INSERT_AFTER)
            break

    # Strip &#10003; glyph from completion eyebrow
    new_content = new_content.replace('&#10003; ', '')

    # Version bumps (if needed)
    new_content = new_content.replace('game.css?v=v104', 'game.css?v=v105')
    new_content = new_content.replace('game.js?v=v104', 'game.js?v=v105')

    if new_content == content:
        print(f'NO CHANGE: {path}')
        continue

    if not dry_run:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
    changed += 1
    print(f'{"DRY " if dry_run else ""}Changed: {path}')

print(f'\nTotal changed: {changed}  Skipped (already done): {skipped}')
