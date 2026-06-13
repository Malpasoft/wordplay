#!/usr/bin/env python3
"""Roll out the standalone match.html game to vocab chapters (a/, b/, c/, fr/).

Template: a/a1/vocabulary/animals/match.html (3 lives, every word matched
twice to win, mastery saved to the chapter's existing key). For each vocab
chapter with a parseable WORDS array in flashcards.html:
  1. generate match.html (skipped if it already exists)
  2. insert a Match activity-card in the chapter hub after the Flashcards card
  3. add a Match button to the chapter-nav of sibling pages

Explicit string matching only (no sed/awk). Old A1 template chapters
(definition/example keys) are mapped to def. Chapters whose flashcards have
no WORDS (applied-grammar) are skipped and reported.

Usage:
  python3 scripts/gen_match.py --sample   # 3 chapters
  python3 scripts/gen_match.py            # all
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'a/a1/vocabulary/animals/match.html')

WORDS_RE = re.compile(r'var WORDS\s*=\s*(\[.*?\]);', re.S)
VOCAB_DATA_RE = re.compile(r'(window\.VOCAB_DATA\s*=\s*\{.*?\n\};)', re.S)
KEY_RE = re.compile(r"(?:MASTERY_KEY|STORAGE_KEY)\s*[:=]\s*'([^']+)'")
H1_RE = re.compile(r'<h1>(.*?)</h1>', re.S)
CRUMB_RE = re.compile(r'<div class="breadcrumb">.*?</div>', re.S)
NAV_RE = re.compile(r'<nav class="chapter-nav">.*?</nav>', re.S)
TAG_RE = re.compile(r'<[^>]+>')

MATCH_CARD = '''    <a href="match.html" class="activity-card" data-activity="match">
      <span class="ac-title">Match game</span>
      <p class="ac-desc">Match each word to its definition &mdash; 3 lives, match every word twice to win</p>
      <span class="ac-arrow">&#8594;</span>
    </a>
'''

NAV_BTN_RE = re.compile(
    r'(<a href="flashcards\.html" class="chapter-nav-btn[^"]*">[^<]*</a>)')


def vocab_chapters():
    out = []
    for band, sec in (('a', 'vocabulary'), ('b', 'vocabulary'), ('c', 'vocabulary')):
        base = os.path.join(ROOT, band)
        for level in sorted(os.listdir(base)):
            d = os.path.join(base, level, sec)
            if os.path.isdir(d):
                out.extend(os.path.join(d, s) for s in sorted(os.listdir(d))
                           if os.path.isdir(os.path.join(d, s)))
    for level in ('b1', 'b2'):
        d = os.path.join(ROOT, 'fr', level, 'vocabulaire')
        if os.path.isdir(d):
            out.extend(os.path.join(d, s) for s in sorted(os.listdir(d))
                       if os.path.isdir(os.path.join(d, s)))
    # L1-mediated tracks: es/ and espanol-en/ vocabulary
    for track in ('es', 'espanol-en'):
        for level in ('a1', 'a2', 'b1', 'b2'):
            d = os.path.join(ROOT, track, level, 'vocabulary')
            if os.path.isdir(d):
                out.extend(os.path.join(d, s) for s in sorted(os.listdir(d))
                           if os.path.isdir(os.path.join(d, s)))
    return out


def parse_words(html):
    raw = None
    m = WORDS_RE.search(html)
    if m:
        try:
            raw = json.loads(m.group(1))
        except ValueError:
            raw = None
    if raw is None:
        # fallback: window.VOCAB_DATA = { ... WORDS: [...] } JS object literal
        v = VOCAB_DATA_RE.search(html)
        if not v:
            return None
        import subprocess
        prog = ('var window={};' + v.group(1)
                + ';console.log(JSON.stringify(window.VOCAB_DATA.WORDS));')
        r = subprocess.run(['node', '-e', prog], capture_output=True, text=True)
        if r.returncode != 0:
            return None
        try:
            raw = json.loads(r.stdout)
        except ValueError:
            return None
    words = []
    for it in raw:
        word = it.get('word')
        d = it.get('def') or it.get('definition') or ''
        d = TAG_RE.sub('', d).strip()
        if word and d:
            words.append({'word': word, 'def': d})
    return words if len(words) >= 6 else None


def build_match(tpl, fc_html, words, level, slug, title):
    key_m = KEY_RE.search(fc_html)
    mastery_key = key_m.group(1) if key_m else f'wordplay_vocab_{level}_{slug}_mastered'
    out = tpl
    # Carry lang attribute from source page (e.g. "es" for Spanish-UI tracks)
    lang_m = re.search(r'<html lang="([^"]+)"', fc_html)
    if lang_m and lang_m.group(1) != 'en':
        out = out.replace('<html lang="en">', f'<html lang="{lang_m.group(1)}">')
    out = out.replace('<title>A1 Vocab · Animals — Match Game | Word Play</title>',
                      f'<title>{level.upper()} Vocab · {title} — Match Game | Word Play</title>')
    # breadcrumb: reuse the chapter's own, pointing the last crumb at index.html
    crumb = CRUMB_RE.search(fc_html)
    if crumb:
        c = crumb.group(0)
        c = re.sub(r'<strong>(.*?)</strong>',
                   r'<a href="index.html">\1</a><span>›</span>\n    <strong>Match game</strong>',
                   c, count=1)
        out = CRUMB_RE.sub(lambda _: c, out, count=1)
    out = out.replace('<h1>Animals — Match</h1>', f'<h1>{title} — Match</h1>')
    # chapter-nav: reuse the chapter's own with Match active after Flashcards
    nav = NAV_RE.search(fc_html)
    if nav:
        n = nav.group(0).replace(' active', '')
        n = NAV_BTN_RE.sub(
            r'\1\n    <a href="match.html" class="chapter-nav-btn active">Match</a>', n, count=1)
        out = NAV_RE.sub(lambda _: n, out, count=1)
    out = out.replace('You matched every word twice. Animals vocabulary mastered!',
                      f'You matched every word twice. {title} vocabulary mastered!')
    words_js = ',\n  '.join(json.dumps(w, ensure_ascii=False) for w in words)
    out = WORDS_RE.sub(lambda _: 'var WORDS = [\n  ' + words_js + '\n];', out, count=1)
    out = out.replace("var MASTERY_KEY = 'wordplay_vocab_a1_animals_mastered';",
                      f"var MASTERY_KEY = '{mastery_key}';")
    out = out.replace("var PROG_KEY    = 'a1';", f"var PROG_KEY    = '{level}';")
    out = out.replace("var SLUG        = 'animals';", f"var SLUG        = '{slug}';")
    out = out.replace('0 / 20 matches', f'0 / {len(words) * 2} matches')
    out = out.replace('var(--navy)', 'var(--ink)')
    return out


def add_hub_card(hub_html):
    if 'href="match.html"' in hub_html:
        return hub_html, False
    anchor = '<a href="flashcards.html" class="activity-card"'
    i = hub_html.find(anchor)
    if i == -1:
        return hub_html, False
    j = hub_html.find('</a>', i)
    if j == -1:
        return hub_html, False
    j += len('</a>\n')
    return hub_html[:j] + MATCH_CARD + hub_html[j:], True


def add_nav_btn(html):
    if 'href="match.html"' in html:
        return html, False
    new, n = NAV_BTN_RE.subn(
        r'\1\n    <a href="match.html" class="chapter-nav-btn">Match</a>', html, count=1)
    return new, n > 0


def main():
    sample = '--sample' in sys.argv
    tpl = open(TEMPLATE, encoding='utf-8').read()
    chapters = vocab_chapters()
    done, skipped = [], []
    for ch in chapters:
        rel = os.path.relpath(ch, ROOT)
        fc = os.path.join(ch, 'flashcards.html')
        target = os.path.join(ch, 'match.html')
        if os.path.exists(target) or not os.path.exists(fc):
            continue
        fc_html = open(fc, encoding='utf-8').read()
        words = parse_words(fc_html)
        if not words:
            skipped.append(rel)
            continue
        parts = rel.split(os.sep)
        track, level, slug = parts[0], parts[1], parts[3]
        h1 = H1_RE.search(fc_html)
        title = TAG_RE.sub('', h1.group(1)).strip() if h1 else slug.replace('-', ' ').title()
        with open(target, 'w', encoding='utf-8') as f:
            f.write(build_match(tpl, fc_html, words, level, slug, title))
        # hub card — skip for es/ and espanol-en/ (their hub already says "Flashcards & Match")
        hub_p = os.path.join(ch, 'index.html')
        if os.path.exists(hub_p) and track not in ('es', 'espanol-en'):
            hub, changed = add_hub_card(open(hub_p, encoding='utf-8').read())
            if changed:
                open(hub_p, 'w', encoding='utf-8').write(hub)
        # sibling navs
        for sib in ('flashcards.html', 'slides.html', 'worksheet.html', 'game.html'):
            p = os.path.join(ch, sib)
            if not os.path.exists(p):
                continue
            s, changed = add_nav_btn(open(p, encoding='utf-8').read())
            if changed:
                open(p, 'w', encoding='utf-8').write(s)
        done.append(rel)
        if sample and len(done) >= 3:
            break
    print(f'{len(done)} chapters got match.html')
    for d in done:
        print('  +', d)
    if skipped:
        print('skipped (no parseable WORDS):')
        for s in skipped:
            print('  -', s)


if __name__ == '__main__':
    main()
