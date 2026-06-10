#!/usr/bin/env python3
"""Populate empty fr/ chapters from the same-slug English-track chapters.

fr/ is the English course for French speakers; the existing fr/ chapters use
English UI and were built on the same skeleton as the English track. This
script copies the proven English chapter content into fr/ structure with
explicit, anchor-based transforms (no sed/awk; CLAUDE.md bulk-edit rules):

  - section rename:   grammar->grammaire, vocabulary->vocabulaire, writing->redaction
  - drop links to printables.html (fr chapters have no printables)
  - drop next/prev-chapter links whose fr target directory does not exist
  - normalize shared-asset ?v= pins to the current versions

Only fills chapters whose fr directory contains no content files (index.html
only). Never overwrites existing fr content.

Usage:
  python3 scripts/gen_fr_from_en.py --sample   # 3 chapters only
  python3 scripts/gen_fr_from_en.py            # all empty chapters
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECTION_MAP = {
    'grammaire': 'grammar',
    'vocabulaire': 'vocabulary',
    'redaction': 'writing',
}

# current pinned versions (CLAUDE.md / existing fr chapters)
VERSION_PINS = {
    'base.css': 'v124',
    'slides.css': 'v115',
    'worksheet.css': 'v106',
    'game.css': 'v112',
    'print.css': 'v102',
    'dark-init.js': 'v112',
    'deck.js': 'v114',
    'i18n.js': 'v123',
    'store.js': 'v107',
    'worksheet.js': 'v108',
    'game.js': 'v111',
    'print.js': 'v102',
}

CONTENT_FILES = ('slides.html', 'worksheet.html', 'game.html', 'flashcards.html')

PRINTABLES_LINK_RE = re.compile(
    r'\s*<a href="printables\.html"[^>]*>[^<]*</a>')
SIBLING_LINK_RE = re.compile(
    r'<a href="\.\./([a-z0-9-]+)/[a-z]+\.html"[^>]*>.*?</a>', re.S)
VERSION_RE = re.compile(r'(shared/([a-z0-9-]+\.(?:css|js)))\?v=v\d+')


def pin_versions(html):
    def repl(m):
        fname = m.group(2)
        pin = VERSION_PINS.get(fname)
        return f'{m.group(1)}?v={pin}' if pin else m.group(0)
    return VERSION_RE.sub(repl, html)


def prune_dead_siblings(html, fr_section_dir):
    def repl(m):
        slug = m.group(1)
        target = os.path.join(fr_section_dir, slug)
        # keep the link only if the fr sibling chapter exists (hub scaffold)
        return m.group(0) if os.path.isdir(target) else ''
    return SIBLING_LINK_RE.sub(repl, html)


def transform(html, fr_section_dir):
    html = PRINTABLES_LINK_RE.sub('', html)
    html = prune_dead_siblings(html, fr_section_dir)
    html = pin_versions(html)
    return html


def empty_chapters():
    out = []
    for level in ('b1', 'b2'):
        for fr_sec, en_sec in SECTION_MAP.items():
            sec_dir = os.path.join(ROOT, 'fr', level, fr_sec)
            if not os.path.isdir(sec_dir):
                continue
            for slug in sorted(os.listdir(sec_dir)):
                ch_dir = os.path.join(sec_dir, slug)
                if not os.path.isdir(ch_dir):
                    continue
                has_content = any(
                    os.path.exists(os.path.join(ch_dir, f)) for f in CONTENT_FILES)
                if has_content:
                    continue
                en_dir = os.path.join(ROOT, 'b', level, en_sec, slug)
                out.append((level, fr_sec, slug, ch_dir, en_dir))
    return out


def main():
    sample = '--sample' in sys.argv
    chapters = empty_chapters()
    if sample:
        chapters = chapters[:3]
    written, missing_src = [], []
    for level, fr_sec, slug, ch_dir, en_dir in chapters:
        if not os.path.isdir(en_dir):
            missing_src.append(f'{level}/{fr_sec}/{slug}')
            continue
        fr_section_dir = os.path.dirname(ch_dir)
        for fname in CONTENT_FILES:
            src = os.path.join(en_dir, fname)
            if not os.path.exists(src):
                continue  # e.g. grammar chapters have no flashcards.html
            with open(src, encoding='utf-8') as f:
                html = f.read()
            html = transform(html, fr_section_dir)
            with open(os.path.join(ch_dir, fname), 'w', encoding='utf-8') as f:
                f.write(html)
            written.append(f'fr/{level}/{fr_sec}/{slug}/{fname}')
    print(f'{len(written)} files written')
    for w in written:
        print('  ' + w)
    if missing_src:
        print('NO ENGLISH SOURCE (skipped):')
        for m in missing_src:
            print('  ' + m)


if __name__ == '__main__':
    main()
