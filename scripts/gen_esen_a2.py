#!/usr/bin/env python3
"""Render espanol-en/a2 grammar chapters from compact content data.

Uses the completed espanol-en/a2/grammar/past-simple chapter as the runtime
template (structure, asset versions, wiring) and swaps the content regions by
stable anchors. Content lives in scripts/content/esen_a2_*.py batch modules,
each exposing CHAPTERS = { slug: {...} }.

Chapter data shape:
  num        'G05'
  short      'Comparatives'                  (crumb + hub h1)
  title      'Comparatives — Comparativos'   (page h1)
  subtitle   'Compare people and things'
  slides     [ (h2, sub_or_None, inner_html), ... ]   4-6 content slides
  traps      [ (wrong, right, note) x4-5 ]
  summary    [ (label, form, ex) x5-6 ]
  ex1        (title, instruct, [ (qtext, [opts], answer, expl) x6 ])   MC
  ex2        (title, instruct, [ (qtext, answer, expl) x5 ])           typed
  ex3        (title, instruct, [ (qtext, [opts], answer, expl) x5 ])   MC
  game_desc  one-sentence start-screen description
  items      [ (id, term, meaning, synonym, example, completion, answer) x8 ]

Usage: python3 scripts/gen_esen_a2.py scripts/content/esen_a2_g1.py
"""
import importlib.util
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL_DIR = os.path.join(ROOT, 'espanol-en/a2/grammar/past-simple')
LEVEL = 'a2'  # overridable via --level b1|b2 (template stays the a2 chapter)
OUT_BASE = os.path.join(ROOT, 'espanol-en/a2/grammar')


def lvl_fix(s):
    """Swap the template's A2 level markers for the target level."""
    if LEVEL == 'a2':
        return s
    lv = LEVEL.upper()
    s = s.replace('espanol-en/a2/index.html', f'espanol-en/{LEVEL}/index.html')
    s = s.replace('>A2</a>', f'>{lv}</a>')
    s = s.replace('Spanish A2', f'Spanish {lv}')
    s = s.replace('A2 Grammar', f'{lv} Grammar')
    s = s.replace('Grammar A2', f'Grammar {lv}')
    return s


def esc(s):
    return s  # content is authored HTML-safe; <b> allowed in slide/example html


def build_slides(d):
    out = []
    for i, (h2, sub, inner) in enumerate(d['slides'], 1):
        subh = f'<p class="slide-sub">{sub}</p>' if sub else ''
        out.append(
            f'\n<!-- Slide {i} -->\n<div class="slide"><div class="slide-card">\n'
            f'  <div class="slide-header"><h2>{h2}</h2>{subh}</div>\n  {inner}\n</div></div>\n')
    traps = ''.join(
        f'\n  <div class="trap-row"><div class="trap-wrong">{w}</div>'
        f'<div class="trap-arrow">→</div><div class="trap-right">{r}</div>'
        f'<div class="trap-note">{n}</div></div>'
        for w, r, n in d['traps'])
    out.append(
        '\n<!-- Common mistakes -->\n<div class="slide"><div class="slide-card">\n'
        '  <div class="slide-header"><h2>Common Mistakes</h2>'
        '<p class="slide-sub">Traps for English speakers</p></div>\n'
        '  <p class="slide-explanation">These are the errors English speakers make most often.</p>'
        f'{traps}\n</div></div>\n')
    rows = ''.join(
        f'\n  <div class="summary-row"><div class="label">{l}</div>'
        f'<div class="form">{f}</div><div class="ex">{e}</div></div>'
        for l, f, e in d['summary'])
    out.append(
        '\n<!-- Summary slide -->\n<div class="slide summary-slide"><div class="slide-card">\n'
        f'  <div class="slide-header"><h2>Recap: {d["short"]}</h2></div>{rows}\n'
        '  <div style="margin-top:28px;text-align:center"><a href="worksheet.html" '
        'style="display:inline-block;padding:13px 32px;background:var(--amber);color:#1A1A1A;'
        'font-family:var(--font-sans);font-size:.8rem;font-weight:800;letter-spacing:1.5px;'
        'text-transform:uppercase;text-decoration:none;border-radius:5px">Practice now →</a></div>\n'
        '</div></div>\n')
    return ''.join(out)


def mc_q(num, qtext, opts, answer, key):
    btns = ''.join(
        f'<button type="button" class="choice-btn" data-value="{o}">{o}</button>' for o in opts)
    return (f'<div class="q"><span class="q-num">{num}</span><div class="q-text">{qtext}</div>\n'
            f'  <div class="choice-group" data-q="{key}" data-answer="{answer}">{btns}</div></div>\n')


def typed_q(num, qtext, key):
    return (f'<div class="q"><span class="q-num">{num}</span><div class="q-text">{qtext}'
            f'<br><input type="text" data-q="{key}" style="width:200px" '
            f'aria-label="Answer for {key}"></div></div>\n')


def build_form(d):
    e1t, e1i, e1qs = d['ex1']
    e2t, e2i, e2qs = d['ex2']
    e3t, e3i, e3qs = d['ex3']
    total = len(e1qs) + len(e2qs) + len(e3qs)
    s = ['\n<section class="exercise" id="ex1">\n'
         f'<div class="ex-head">Exercise 1</div>\n<div class="ex-title">{e1t}</div>\n'
         f'<div class="ex-meta">{len(e1qs)} points</div>\n<div class="ex-instruct">{e1i}</div>\n']
    for i, (q, opts, a, _) in enumerate(e1qs, 1):
        s.append(mc_q(i, q, opts, a, f'e1q{i}'))
    s.append('</section>\n\n<section class="exercise" id="ex2">\n'
             f'<div class="ex-head">Exercise 2</div>\n<div class="ex-title">{e2t}</div>\n'
             f'<div class="ex-meta">{len(e2qs)} points</div>\n<div class="ex-instruct">{e2i}</div>\n')
    for i, (q, a, _) in enumerate(e2qs, 1):
        s.append(typed_q(i, q, f'e2q{i}'))
    s.append('</section>\n\n<section class="exercise" id="ex3">\n'
             f'<div class="ex-head">Exercise 3</div>\n<div class="ex-title">{e3t}</div>\n'
             f'<div class="ex-meta">{len(e3qs)} points</div>\n<div class="ex-instruct">{e3i}</div>\n')
    for i, (q, opts, a, _) in enumerate(e3qs, 1):
        s.append(mc_q(i, q, opts, a, f'e3q{i}'))
    s.append('<div class="submit-wrap"><button type="submit" class="submit-btn">Check answers</button></div>\n'
             '</section>\n')
    return ''.join(s), total


def build_ws_config(slug, d, total):
    _, _, e1qs = d['ex1']
    _, _, e2qs = d['ex2']
    _, _, e3qs = d['ex3']
    answers = ',\n'.join(f'  e2q{i}:{{answer:{json.dumps(a, ensure_ascii=False)}}}'
                         for i, (_, a, _) in enumerate(e2qs, 1))
    expl = {}
    for i, (_, _, a, x) in enumerate(e1qs, 1):
        expl[f'e1q{i}'] = x
    for i, (_, a, x) in enumerate(e2qs, 1):
        expl[f'e2q{i}'] = x
    for i, (_, _, a, x) in enumerate(e3qs, 1):
        expl[f'e3q{i}'] = x
    expl_js = ',\n'.join(f'  {json.dumps(k)}: {json.dumps(v, ensure_ascii=False)}'
                         for k, v in expl.items())
    titles = (f'{{ex1:{json.dumps("Exercise 1 - " + d["ex1"][0])},'
              f'ex2:{json.dumps("Exercise 2 - " + d["ex2"][0])},'
              f'ex3:{json.dumps("Exercise 3 - " + d["ex3"][0])}}}')
    return (f"\nwindow.CHAPTER_ID = '{slug}';\nwindow.LEVEL = '{LEVEL}';\n"
            f"window.SECTION = 'grammar';\nwindow.TOTAL_POINTS = {total};\n"
            f"window.ANSWERS = {{\n{answers}\n}};\n"
            f"window.EXPLANATIONS = {{\n{expl_js}\n}};\n"
            f"window.EXERCISE_TITLES = {titles};\n")


def build_game_data(slug, d):
    items = ',\n'.join(
        '    {id:%s, term:%s, meaning:%s, synonym:%s, example:%s, completion:%s, answer:%s}' % tuple(
            json.dumps(v, ensure_ascii=False) for v in it)
        for it in d['items'])
    return (f"\nwindow.GAME_DATA = {{\n  chapterId: '{slug}',\n  level: '{LEVEL}',\n"
            f"  title: {json.dumps(d['title'], ensure_ascii=False)},\n"
            f"  storageKey: 'wordplay_game_es_{LEVEL}_{slug}',\n  items: [\n{items}\n  ]\n}};\n")


def seg_replace(s, start, end, new, incl=False):
    i = s.index(start)
    j = s.index(end, i + len(start))
    if incl:
        return s[:i] + new + s[j + len(end):]
    return s[:i + len(start)] + new + s[j:]


def render(slug, d):
    out_dir = os.path.join(OUT_BASE, slug)
    tpl = {f: open(os.path.join(TPL_DIR, f), encoding='utf-8').read()
           for f in ('slides.html', 'worksheet.html', 'game.html', 'index.html')}

    def common(s, page_crumb_kept=True):
        s = s.replace('Past Simple (Pretérito Indefinido)', d['title'])
        s = s.replace('>Past Simple</a>', f'>{d["short"]}</a>')
        s = s.replace('<strong>Past Simple</strong>', f'<strong>{d["short"]}</strong>')
        s = s.replace('G12 &middot;', f'{d["num"]} &middot;')
        s = s.replace('<h1>Past Simple — Pretérito Indefinido</h1>', f'<h1>{d["title"]}</h1>')
        s = s.replace('<h1 class="chapter-h1">Past Simple</h1>',
                      f'<h1 class="chapter-h1">{d["short"]}</h1>')
        s = s.replace("'past-simple'", f"'{slug}'")
        s = s.replace('"past-simple"', f'"{slug}"')
        return s

    # slides
    s = common(tpl['slides.html'])
    s = s.replace('<p class="chapter-subtitle">Talk about completed actions in the past</p>',
                  f'<p class="chapter-subtitle">{d["subtitle"]}</p>')
    s = seg_replace(s, '<div class="slide-deck" id="slide-deck">',
                    '</div>\n<div class="deck-nav">', build_slides(d) + '\n')
    open(os.path.join(out_dir, 'slides.html'), 'w', encoding='utf-8').write(lvl_fix(s))

    # worksheet
    form, total = build_form(d)
    s = common(tpl['worksheet.html'])
    s = re.sub(r'Complete the exercises then check your answers\. Total: \d+ points\.',
               f'Complete the exercises then check your answers. Total: {total} points.', s)
    s = seg_replace(s, '<form id="worksheet">', '</form>', form)
    s = seg_replace(s, '<div id="results" class="results-panel" style="display:none"></div>\n<script>',
                    '</script>\n<script src="../../../../shared/i18n.js',
                    build_ws_config(slug, d, total))
    open(os.path.join(out_dir, 'worksheet.html'), 'w', encoding='utf-8').write(lvl_fix(s))

    # game
    s = common(tpl['game.html'])
    s = s.replace('<h1>Past Simple — Mastery Game</h1>', f'<h1>{d["short"]} — Mastery Game</h1>')
    s = s.replace('Each preterite form passes through three question types: meaning, context and production. Reach 100 points to win.',
                  d['game_desc'])
    s = seg_replace(s, '&middot; Game</footer>\n<script>',
                    '</script>\n<script src="../../../../shared/i18n.js',
                    build_game_data(slug, d))
    open(os.path.join(out_dir, 'game.html'), 'w', encoding='utf-8').write(lvl_fix(s))

    # hub
    s = common(tpl['index.html'])
    open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8').write(lvl_fix(s))

    # remove stub flashcards.html (grammar chapters have none)
    fc = os.path.join(out_dir, 'flashcards.html')
    if os.path.exists(fc):
        os.remove(fc)

    r = subprocess.run(['python3', os.path.join(ROOT, 'scripts/validate_inline_js.py'),
                        os.path.join(out_dir, 'slides.html'),
                        os.path.join(out_dir, 'worksheet.html'),
                        os.path.join(out_dir, 'game.html')],
                       capture_output=True, text=True)
    status = 'OK' if r.returncode == 0 else 'JS FAIL\n' + r.stdout
    print(f'{slug}: rendered, validate={status}')
    return r.returncode == 0


def main():
    global LEVEL, OUT_BASE
    if '--level' in sys.argv:
        i = sys.argv.index('--level')
        LEVEL = sys.argv[i + 1]
        del sys.argv[i:i + 2]
        OUT_BASE = os.path.join(ROOT, f'espanol-en/{LEVEL}/grammar')
    mod_path = sys.argv[1]
    spec = importlib.util.spec_from_file_location('content', mod_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    ok = True
    for slug, d in mod.CHAPTERS.items():
        ok = render(slug, d) and ok
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
