#!/usr/bin/env python3
"""
Fix broken vocab-chapter navigation.

Some vocab chapters' game.html / printables.html / slides.html carry a 4-link
nav with a "Review" (worksheet.html) tab and a "Printables" tab that point to
files the chapter does not have — clicking them 404s. The chapter's own
flashcards.html / slides.html already use the correct 3-link nav. This script
rewrites the broken nav blocks to that canonical 3-link form and removes the
stray "Redo practice worksheet" link on game completion screens.

Canonical nav:
  EN: Flashcards (index.html) · Lesson (slides.html) · Game (game.html)
  ES: Lección (slides.html) · Tarjetas (flashcards.html) · Juego (game.html)

Only touches files that link to a worksheet.html / printables.html that does
NOT exist on disk. Idempotent — safe to re-run.
"""
import re, os, glob, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAV_RE = re.compile(r'([ \t]*)<nav class="chapter-nav">.*?</nav>', re.DOTALL)
REDO_RE = re.compile(r'[ \t]*<a href="worksheet\.html"[^>]*>[^<]*</a>\n')


def canonical_nav(indent, track, active):
    pad = indent + '  '
    def cls(name):
        return ' chapter-nav-btn active' if name == active else ' chapter-nav-btn'
    if track == 'es':
        rows = [
            f'{pad}<a href="slides.html" class="{cls("lesson").strip()}">Lección</a>',
            f'{pad}<a href="flashcards.html" class="{cls("fc").strip()}">Tarjetas</a>',
            f'{pad}<a href="game.html" class="{cls("game").strip()}">Juego</a>',
        ]
    else:
        rows = [
            f'{pad}<a href="index.html" class="{cls("fc").strip()}">Flashcards</a>',
            f'{pad}<a href="slides.html" class="{cls("lesson").strip()}">Lesson</a>',
            f'{pad}<a href="game.html" class="{cls("game").strip()}">Game</a>',
        ]
    return f'{indent}<nav class="chapter-nav">\n' + '\n'.join(rows) + f'\n{indent}</nav>'


def active_for(fname):
    if fname == 'slides.html':
        return 'lesson'
    if fname == 'game.html':
        return 'game'
    return ''  # printables.html — no tab is active


def links_to_missing(path, html):
    d = os.path.dirname(path)
    for target in ('worksheet.html', 'printables.html'):
        if f'href="{target}"' in html and not os.path.exists(os.path.join(d, target)):
            return True
    return False


def main():
    fixed = []
    for path in glob.glob(f'{BASE}/**/*.html', recursive=True):
        fname = os.path.basename(path)
        if fname not in ('slides.html', 'game.html', 'printables.html'):
            continue
        with open(path, encoding='utf-8') as f:
            html = f.read()
        if not links_to_missing(path, html):
            continue
        track = 'es' if path.replace(BASE + '/', '').startswith('es/') else 'en'
        active = active_for(fname)
        new = NAV_RE.sub(lambda m: canonical_nav(m.group(1), track, active), html, count=1)
        new = REDO_RE.sub('', new)  # drop stray "Redo practice worksheet" link
        if new != html:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new)
            fixed.append(path.replace(BASE + '/', ''))

    print(f'Fixed: {len(fixed)} files')
    for f in sorted(fixed):
        print(f'  + {f}')


if __name__ == '__main__':
    main()
