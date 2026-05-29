#!/usr/bin/env python3
"""Migrate legacy game.html #gamePlay blocks to the canonical clean v108 card.

Legacy pages use <div class="game-card"> or <div class="game-play-card"> inside
#gamePlay, so game.js buildPlayScreen() bails (it needs `.game-play`). We replace
the whole #gamePlay block with the canonical structure that triggers the clean card.
"""
import os, re, sys, glob

ROOT = '/home/user/wordplay'

CANON_EN = (
    '  <div id="gamePlay" class="game-screen"><div class="game-play"></div>\n'
    '  <div class="game-ref-panel" id="gRefPanel">\n'
    '    <button id="gRefToggle" class="game-ref-head">&#9660; Reference &mdash; all words</button>\n'
    '    <div id="gRefBody" class="game-ref-body"><div id="gRefList"></div></div>\n'
    '  </div></div>\n'
)
CANON_ES = (
    '  <div id="gamePlay" class="game-screen"><div class="game-play"></div>\n'
    '  <div class="game-ref-panel" id="gRefPanel">\n'
    '    <button id="gRefToggle" class="game-ref-head">&#9660; Referencia &mdash; todas las palabras</button>\n'
    '    <div id="gRefBody" class="game-ref-body"><div id="gRefList"></div></div>\n'
    '  </div></div>\n'
)

# anchored: from start of #gamePlay div up to (not including) #gameCompletion div
PAT = re.compile(r'<div id="gamePlay"[^>]*>.*?(?=<div id="gameCompletion")', re.DOTALL)

def is_legacy(txt):
    return ('class="game-card"' in txt) or ('class="game-play-card"' in txt)

def migrate(path, dry):
    rel = os.path.relpath(path, ROOT)
    with open(path, encoding='utf-8') as f:
        txt = f.read()
    if not is_legacy(txt):
        return ('skip-not-legacy', rel)
    if 'id="gameCompletion"' not in txt:
        return ('skip-no-completion', rel)
    canon = CANON_ES if rel.startswith('es/') else CANON_EN
    new, n = PAT.subn(canon, txt)
    if n != 1:
        return (f'skip-bad-anchor(n={n})', rel)
    if dry:
        return ('would-migrate', rel)
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        f.write(new)
    os.replace(tmp, path)
    return ('migrated', rel)

if __name__ == '__main__':
    dry = '--apply' not in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if args:
        files = [os.path.join(ROOT, a) for a in args]
    else:
        files = sorted(glob.glob(os.path.join(ROOT, '**', 'game.html'), recursive=True))
    counts = {}
    for p in files:
        status, rel = migrate(p, dry)
        counts[status.split('(')[0]] = counts.get(status.split('(')[0], 0) + 1
        if status not in ('skip-not-legacy',):
            print(f'{status:24} {rel}')
    print('\n--- summary ---')
    for k, v in sorted(counts.items()):
        print(f'{k}: {v}')
    print('MODE:', 'DRY-RUN' if dry else 'APPLIED')
