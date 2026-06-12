#!/usr/bin/env python3
"""Render espanol-en/a2 vocabulary chapters from 12-word lists.

Language direction: Spanish headwords, English definitions, Spanish example
sentences; audio es-ES (inherited from the A1 animals flashcards template).
The worksheet and Dominio game are auto-derived from the word list, with
de-accented accept[] variants for typed answers (graders do not strip
accents).

Templates at runtime:
  flashcards/slides : espanol-en/a1/vocabulary/animals/
  worksheet/game    : espanol-en/a2/grammar/past-simple/

Content modules expose CHAPTERS = { slug: dict(num, short, words=[(word,
ipa, def, ex), ...]) } with ex containing the word wrapped in <b>...</b>.

Usage: python3 scripts/gen_esen_a2_vocab.py scripts/content/esen_a2_v1.py
"""
import importlib.util
import json
import os
import subprocess
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FC_TPL = os.path.join(ROOT, 'espanol-en/a1/vocabulary/animals')
G_TPL = os.path.join(ROOT, 'espanol-en/a2/grammar/past-simple')
LEVEL = 'a2'  # overridable via --level b1|b2
OUT = os.path.join(ROOT, 'espanol-en/a2/vocabulary')


def lvl_fix(s):
    """Swap the grammar template's A2 markers for the target level."""
    if LEVEL == 'a2':
        return s
    lv = LEVEL.upper()
    s = s.replace('espanol-en/a2/index.html', f'espanol-en/{LEVEL}/index.html')
    s = s.replace('>A2</a>', f'>{lv}</a>')
    s = s.replace('Spanish A2', f'Spanish {lv}')
    s = s.replace('A2 Grammar', f'{lv} Vocabulary')
    s = s.replace('Grammar A2', f'Vocabulary {lv}')
    return s


def deacc(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def strip_b(s):
    return s.replace('<b>', '').replace('</b>', '')


def blank(ex):
    i = ex.index('<b>')
    j = ex.index('</b>')
    return ex[:i] + '______' + ex[j + 4:]


def jd(o):
    return json.dumps(o, ensure_ascii=False)


def vocab_crumb_fix(s):
    s = s.replace('<a href="../index.html">Grammar</a>', '<a href="../index.html">Vocabulary</a>')
    s = s.replace("window.SECTION = 'grammar'", "window.SECTION = 'vocabulary'")
    s = s.replace('window.SECTION="grammar"', 'window.SECTION="vocabulary"')
    return s


def build_worksheet_parts(words, short):
    mc1, typed, mc3 = words[:6], words[6:11], words[3:8]
    form = ['\n<section class="exercise" id="ex1">\n<div class="ex-head">Exercise 1</div>\n'
            '<div class="ex-title">What does it mean?</div>\n<div class="ex-meta">6 points</div>\n'
            '<div class="ex-instruct">Choose the English meaning of each Spanish word.</div>\n']
    expl = {}
    for i, (w, _, df, ex) in enumerate(mc1, 1):
        others = [x[2] for x in words if x[2] != df][:2]
        opts = [df] + others
        opts = opts[:1] + sorted(others)
        btns = ''.join(f'<button type="button" class="choice-btn" data-value="{o}">{o}</button>'
                       for o in [df] + sorted(others))
        form.append(f'<div class="q"><span class="q-num">{i}</span>'
                    f'<div class="q-text"><b>{w}</b></div>\n'
                    f'  <div class="choice-group" data-q="e1q{i}" data-answer="{df}">{btns}</div></div>\n')
        expl[f'e1q{i}'] = f'{w} = {df}. Example: {strip_b(ex)}'
    form.append('</section>\n\n<section class="exercise" id="ex2">\n<div class="ex-head">Exercise 2</div>\n'
                '<div class="ex-title">Translate into Spanish</div>\n<div class="ex-meta">5 points</div>\n'
                '<div class="ex-instruct">Type the Spanish word. Accents are optional.</div>\n')
    answers = []
    for i, (w, _, df, ex) in enumerate(typed, 1):
        form.append(f'<div class="q"><span class="q-num">{i}</span>'
                    f'<div class="q-text">{df}<br>'
                    f'<input type="text" data-q="e2q{i}" style="width:200px" '
                    f'aria-label="Answer for e2q{i}"></div></div>\n')
        acc = [deacc(w)] if deacc(w) != w else []
        answers.append((f'e2q{i}', w, acc))
        expl[f'e2q{i}'] = f'{df} = {w}. Example: {strip_b(ex)}'
    form.append('</section>\n\n<section class="exercise" id="ex3">\n<div class="ex-head">Exercise 3</div>\n'
                '<div class="ex-title">In context</div>\n<div class="ex-meta">5 points</div>\n'
                '<div class="ex-instruct">Choose the word that completes each sentence.</div>\n')
    for i, (w, _, df, ex) in enumerate(mc3, 1):
        others = sorted(x[0] for x in words if x[0] != w)[:2]
        btns = ''.join(f'<button type="button" class="choice-btn" data-value="{o}">{o}</button>'
                       for o in [w] + others)
        form.append(f'<div class="q"><span class="q-num">{i}</span>'
                    f'<div class="q-text">{blank(ex)}</div>\n'
                    f'  <div class="choice-group" data-q="e3q{i}" data-answer="{w}">{btns}</div></div>\n')
        expl[f'e3q{i}'] = f'{strip_b(ex)} — {w} means {df}.'
    form.append('<div class="submit-wrap"><button type="submit" class="submit-btn">Check answers</button></div>\n'
                '</section>\n')
    total = len(mc1) + len(typed) + len(mc3)
    ans_js = ',\n'.join(
        f'  {k}:{{answer:{jd(a)}' + (f', accept:{jd(acc)}' if acc else '') + '}'
        for k, a, acc in answers)
    expl_js = ',\n'.join(f'  {jd(k)}: {jd(v)}' for k, v in expl.items())
    cfg = (f"window.TOTAL_POINTS = {total};\nwindow.ANSWERS = {{\n{ans_js}\n}};\n"
           f"window.EXPLANATIONS = {{\n{expl_js}\n}};\n"
           f'window.EXERCISE_TITLES = {{ex1:"Exercise 1 - What does it mean?",'
           f'ex2:"Exercise 2 - Translate into Spanish",ex3:"Exercise 3 - In context"}};\n')
    return ''.join(form), cfg, total


def build_game_items(words):
    items = []
    for w, _, df, ex in words[:8]:
        acc = f', accept:{jd([deacc(w)])}' if deacc(w) != w else ''
        items.append(
            f'    {{id:{jd(deacc(w).replace(" ", "-"))}, term:{jd(w)}, meaning:{jd(df)}, '
            f'synonym:{jd("Spanish for " + df)}, example:{jd(ex)}, '
            f'completion:{jd(blank(ex))}, answer:{jd(w)}{acc}}}')
    return ',\n'.join(items)


def seg_replace(s, start, end, new):
    i = s.index(start)
    j = s.index(end, i + len(start))
    return s[:i + len(start)] + new + s[j:]


def render(slug, d):
    out_dir = os.path.join(OUT, slug)
    short, num = d['short'], d['num']
    words = d['words']

    # flashcards from animals template
    s = open(os.path.join(FC_TPL, 'flashcards.html'), encoding='utf-8').read()
    s = s.replace('Animals', short).replace('animals', slug)
    s = s.replace("var LEVEL = 'a1';", f"var LEVEL = '{LEVEL}';")
    s = s.replace('>A1</a>', f'>{LEVEL.upper()}</a>')
    s = s.replace('Spanish A1', f'Spanish {LEVEL.upper()}')
    s = s.replace('<div class="chapter-num">V3</div>', f'<div class="chapter-num">{num}</div>')
    words_js = jd([{'word': w, 'ipa': ipa, 'def': df, 'ex': ex} for w, ipa, df, ex in words])
    s = seg_replace(s, 'var WORDS = ', ';\n', words_js)
    open(os.path.join(out_dir, 'flashcards.html'), 'w', encoding='utf-8').write(s)

    # slides from animals template (simple intro deck + word groups)
    s = open(os.path.join(FC_TPL, 'slides.html'), encoding='utf-8').read()
    s = s.replace('Animals', short).replace('animals', slug)
    s = s.replace('window.LEVEL="a1"', f'window.LEVEL="{LEVEL}"')
    s = s.replace('>A1</a>', f'>{LEVEL.upper()}</a>')
    s = s.replace('Spanish A1', f'Spanish {LEVEL.upper()}')
    s = s.replace('<div class="chapter-num">V3</div>', f'<div class="chapter-num">{num}</div>')
    half = (len(words) + 1) // 2
    def word_rows(chunk):
        return ''.join(
            f'<div class="summary-row"><div class="label"><b>{w}</b></div>'
            f'<div class="form">{df}</div><div class="ex">{ex}</div></div>'
            for w, _, df, ex in chunk)
    deck = (
        f'\n<div class="slide"><div class="slide-card"><div class="slide-header">'
        f'<h2>Welcome to {short}!</h2></div>'
        f'<p class="slide-explanation">You will learn {len(words)} essential Spanish words for this topic. '
        f'Each card shows the English meaning and a Spanish example sentence.</p>'
        f'<div class="overview-row"><div class="overview-label">How to learn</div>'
        f'<div class="overview-desc">Read the two word groups, then flip the flashcards, '
        f'listen to the pronunciation, and finish with the mastery game.</div></div></div></div>\n'
        f'<div class="slide"><div class="slide-card"><div class="slide-header"><h2>Words 1–{half}</h2></div>'
        f'{word_rows(words[:half])}</div></div>\n'
        f'<div class="slide"><div class="slide-card"><div class="slide-header"><h2>Words {half+1}–{len(words)}</h2></div>'
        f'{word_rows(words[half:])}</div></div>\n'
        f'<div class="slide summary-slide"><div class="slide-card"><h2>Ready to practise?</h2>'
        f'<div style="margin-top:28px;text-align:center">'
        f'<a href="flashcards.html" style="display:inline-block;padding:13px 32px;background:var(--amber);'
        f'color:#1A1A1A;font-family:var(--font-sans);font-size:.8rem;font-weight:800;letter-spacing:1.5px;'
        f'text-transform:uppercase;text-decoration:none;border-radius:5px;margin:4px">Flashcards →</a>'
        f'<a href="game.html" style="display:inline-block;padding:13px 32px;background:transparent;'
        f'color:var(--ink);border:1.5px solid var(--hairline);font-family:var(--font-sans);font-size:.8rem;'
        f'font-weight:800;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;'
        f'border-radius:5px;margin:4px">Game →</a></div></div></div>\n')
    s = seg_replace(s, '<div class="slide-deck" id="slide-deck">', '</div>\n<div class="deck-nav">', deck)
    open(os.path.join(out_dir, 'slides.html'), 'w', encoding='utf-8').write(s)

    # worksheet from grammar template
    form, cfg, total = build_worksheet_parts(words, short)
    s = open(os.path.join(G_TPL, 'worksheet.html'), encoding='utf-8').read()
    s = vocab_crumb_fix(s)
    s = s.replace('Past Simple (Pretérito Indefinido)', f'{short} — Vocabulary')
    s = s.replace('>Past Simple</a>', f'>{short}</a>')
    s = s.replace('<h1>Past Simple — Pretérito Indefinido</h1>', f'<h1>{short} — Practice</h1>')
    s = s.replace("'past-simple'", f"'{slug}'")
    import re as _re
    s = _re.sub(r'Total: \d+ points\.', f'Total: {total} points.', s)
    s = seg_replace(s, '<form id="worksheet">', '</form>', form)
    s = seg_replace(s, '<div id="results" class="results-panel" style="display:none"></div>\n<script>',
                    '</script>\n<script src="../../../../shared/i18n.js',
                    f"\nwindow.CHAPTER_ID = '{slug}';\nwindow.LEVEL = '{LEVEL}';\n"
                    f"window.SECTION = 'vocabulary';\n" + cfg)
    open(os.path.join(out_dir, 'worksheet.html'), 'w', encoding='utf-8').write(lvl_fix(s))

    # game from grammar template
    s = open(os.path.join(G_TPL, 'game.html'), encoding='utf-8').read()
    s = vocab_crumb_fix(s)
    s = s.replace('Past Simple (Pretérito Indefinido)', f'{short} — Vocabulary')
    s = s.replace('>Past Simple</a>', f'>{short}</a>')
    s = s.replace('<h1>Past Simple — Mastery Game</h1>', f'<h1>{short} — Mastery Game</h1>')
    s = s.replace('Each preterite form passes through three question types: meaning, context and production. Reach 100 points to win.',
                  'Each word passes through three question types: meaning, context and production. Reach 100 points to win.')
    gd = (f"\nwindow.GAME_DATA = {{\n  chapterId: '{slug}',\n  level: '{LEVEL}',\n"
          f"  title: {jd(short + ' — Vocabulary')},\n"
          f"  storageKey: 'wordplay_game_es_{LEVEL}_{slug}',\n  items: [\n{build_game_items(words)}\n  ]\n}};\n")
    s = seg_replace(s, '&middot; Game</footer>\n<script>',
                    '</script>\n<script src="../../../../shared/i18n.js', gd)
    s = s.replace("'past-simple'", f"'{slug}'")
    open(os.path.join(out_dir, 'game.html'), 'w', encoding='utf-8').write(lvl_fix(s))

    # hub: just clear the Coming soon marker
    hub_p = os.path.join(out_dir, 'index.html')
    h = open(hub_p, encoding='utf-8').read()
    h = h.replace(f'{num} &middot; Coming soon', f'{num} &middot; Vocabulary')
    open(hub_p, 'w', encoding='utf-8').write(h)

    r = subprocess.run(['python3', os.path.join(ROOT, 'scripts/validate_inline_js.py')]
                       + [os.path.join(out_dir, f) for f in
                          ('flashcards.html', 'slides.html', 'worksheet.html', 'game.html')],
                       capture_output=True, text=True)
    print(f'{slug}: rendered, validate={"OK" if r.returncode == 0 else "FAIL: " + r.stdout}')
    return r.returncode == 0


def main():
    global LEVEL, OUT
    if '--level' in sys.argv:
        i = sys.argv.index('--level')
        LEVEL = sys.argv[i + 1]
        del sys.argv[i:i + 2]
        OUT = os.path.join(ROOT, f'espanol-en/{LEVEL}/vocabulary')
    spec = importlib.util.spec_from_file_location('content', sys.argv[1])
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    ok = True
    for slug, d in mod.CHAPTERS.items():
        ok = render(slug, d) and ok
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
