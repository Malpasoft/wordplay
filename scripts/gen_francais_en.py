#!/usr/bin/env python3
"""Render francais-en/ (French course for English speakers) grammar & writing chapters.

English-mediated course: UI chrome and explanations in English, target content
(examples, exercises) in French. Pages set <html lang="en">.

Content modules expose CHAPTERS = { slug: {...} } with the same shape as gen_fr.py:
  level     'a1' | 'a2' | 'b1' | 'b2'
  section   'grammar' | 'writing'
  num       'G01'
  short     'Articles and Gender'
  title     'Articles and Gender — Les Articles et le Genre'
  subtitle  English one-liner
  slides    [ (h2, sub_or_None, inner_html_en) ]   4-6 slides, English prose,
            French examples in <b>
  traps     [ (wrong, right, note_en) x4-5 ]
  summary   [ (label, form, ex) x5-6 ]
  ex1/ex3   (title_en, instruct_en, [ (qtext, [opts], answer, expl_en) ])  MC
  ex2       (title_en, instruct_en, [ (qtext, answer, expl_en) ])          typed
  game_desc English start-screen sentence
  items     [ (id, term, meaning_en, synonym_en, example, completion, answer) x8 ]

Usage: python3 scripts/gen_francais_en.py scripts/content/francais_en_a1_g1.py
"""
import importlib.util, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../../favicon.svg" type="image/svg+xml">
<title>{title}</title>
<link rel="stylesheet" href="../../../../shared/base.css?v=v125">
{extra_css}<script src="/shared/auth.js?v=1"></script>
<script src="../../../../shared/dark-init.js?v=v112"></script>
</head>
'''

HEADER = '<header class="site-header"><div class="site-header-inner"><a href="index.html" class="back back-link" aria-label="Back"></a><a href="/" class="brand"><svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px"><rect width="32" height="32" rx="4" fill="currentColor"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>Word Play</a><button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">&#9680; Dark</button></div></header>\n'

SECTION_EN = {'grammar': 'Grammar', 'writing': 'Writing', 'vocabulary': 'Vocabulary'}


def jd(o):
    return json.dumps(o, ensure_ascii=False)


# French word-ish characters, used to approximate word boundaries that respect
# accents, apostrophes and hyphens in answers like "l'", "est-ce que".
_FR_W = "\\wàâäéèêëïîôöùûüçœæÀÂÄÉÈÊËÏÎÔÖÙÛÜÇŒÆ"


def gap_from_example(example, answer):
    """Return the example sentence with the first whole-word occurrence of the
    answer replaced by the '_____' gap marker the game engine splits on, or None
    if the answer doesn't appear as a standalone token in the example."""
    example = str(example or "")
    answer = str(answer or "").strip()
    if not example or not answer:
        return None
    pat = re.compile(rf'(?<![{_FR_W}]){re.escape(answer)}(?![{_FR_W}])', re.IGNORECASE)
    m = pat.search(example)
    if not m:
        return None
    return example[:m.start()] + '_____' + example[m.end():]


def fix_grammar_completion(d, it):
    """For grammar game items whose completion lacks a gap marker, derive a
    gapped sentence from the validated French example so the 'contexto' question
    is a real fill-in-the-blank (matching every other course track) instead of a
    rule that may show the answer. Falls back to the plain example sentence when
    the answer isn't a surface token in it."""
    iid, term, meaning, syn, ex, comp, ans = it
    if d.get('section') == 'grammar' and '_____' not in str(comp):
        gapped = gap_from_example(ex, ans)
        comp = gapped if gapped is not None else ex
    return (iid, term, meaning, syn, ex, comp, ans)


def crumb(d, page_en):
    sec = SECTION_EN[d['section']]
    return (f'<div class="breadcrumb">\n'
            f'  <a href="../../../../index.html">Home</a><span>&#8250;</span>\n'
            f'  <a href="../../../../francais-en/index.html">French for English speakers</a><span>&#8250;</span>\n'
            f'  <a href="../../index.html">{d["level"].upper()}</a><span>&#8250;</span>\n'
            f'  <a href="../index.html">{sec}</a><span>&#8250;</span>\n'
            f'  <a href="index.html">{d["short"]}</a><span>&#8250;</span>\n'
            f'  <strong>{page_en}</strong>\n</div>\n')


def nav(active, section='grammar'):
    if section == 'vocabulary':
        items = [('slides.html', 'Word List'), ('flashcards.html', 'Flashcards'),
                 ('game.html', 'Mastery Game'), ('match.html', 'Match')]
    else:
        items = [('slides.html', 'Lesson'), ('worksheet.html', 'Exercises'), ('game.html', 'Game')]
    btns = ''.join(f'  <a href="{h}" class="chapter-nav-btn{" active" if h == active else ""}">{l}</a>\n'
                   for h, l in items)
    return f'<nav class="chapter-nav">\n{btns}</nav>\n'


def build_slides_html(d):
    out = []
    for i, slide in enumerate(d['slides'], 1):
        if len(slide) == 3:
            h2, sub, inner = slide
        else:
            h2, inner = slide
            sub = None
        subh = f'<p class="slide-sub">{sub}</p>' if sub else ''
        out.append(f'\n<!-- Slide {i} -->\n<div class="slide"><div class="slide-card">\n'
                   f'<h2 class="slide-h2">{h2}</h2>{subh}\n{inner}\n</div></div>\n')
    if d.get('traps'):
        rows = ''.join(
            f'<tr><td class="trap-wrong">{w}</td><td class="trap-right">{r}</td>'
            f'<td class="trap-note">{n}</td></tr>\n'
            for w, r, n in d['traps'])
        out.append(f'<div class="slide"><div class="slide-card">\n'
                   f'<h2 class="slide-h2">Common Mistakes</h2>\n'
                   '<table class="trap-table">\n'
                   '<thead><tr><th class="trap-wrong">Avoid</th><th class="trap-right">Use</th>'
                   '<th class="trap-note">Why</th></tr></thead>\n'
                   f'<tbody>{rows}</tbody></table>\n</div></div>\n')
    if d.get('summary'):
        rows2 = ''.join(f'<tr><td class="sum-label">{l}</td><td class="sum-form">{f}</td>'
                        f'<td class="sum-ex">{e}</td></tr>\n'
                        for l, f, e in d['summary'])
        out.append(f'<div class="slide"><div class="slide-card">\n'
                   f'<h2 class="slide-h2">Summary</h2>\n'
                   '<table class="sum-table">\n'
                   '<thead><tr><th>Point</th><th>Form</th><th>Example</th></tr></thead>\n'
                   f'<tbody>{rows2}</tbody></table>\n</div></div>\n')
    return ''.join(out)


def render_slides(d, slug):
    sec_label = SECTION_EN[d['section']]
    s = HEAD.format(title=f'{d["short"]} — Lesson {d["level"].upper()} | Word Play',
                    extra_css='<link rel="stylesheet" href="../../../../shared/slides.css?v=v115">\n')
    s += ('<body class="deck-body">\n'
          '<div class="deck-progress"><div class="deck-progress-fill" id="deck-progress-fill"></div></div>\n')
    s += HEADER + crumb(d, 'Lesson') + nav('slides.html')
    s += (f'<div class="chapter-num">{d["num"]} &middot; {sec_label}</div>\n'
          f'<h1>{d["title"]}</h1>\n<p class="chapter-subtitle">{d["subtitle"]}</p>\n'
          f'<div class="slide-deck" id="slide-deck">\n{build_slides_html(d)}\n</div>\n'
          '<div class="deck-nav">'
          '<button class="deck-btn" id="deck-prev" aria-label="Previous slide">&#9664; Prev</button>'
          '<div class="counter" id="slide-counter"></div>'
          '<button class="deck-btn" id="deck-next" aria-label="Next slide">Next &#9654;</button></div>\n'
          f'<script>window.CHAPTER_ID={jd(slug)};window.LEVEL={jd(d["level"])};'
          f'window.SECTION={jd(d["section"])};</script>\n'
          '<script src="../../../../shared/store.js?v=v107"></script>\n'
          '<script src="../../../../shared/deck.js?v=v114"></script>\n'
          f'<footer class="site-footer">Word Play &middot; French {d["level"].upper()} &middot; Lesson</footer>\n'
          '</body>\n</html>\n')
    return s


def mc_q(num, qtext, opts, answer, key):
    btns = ''.join(f'<button type="button" class="choice-btn" data-value="{o}">{o}</button>' for o in opts)
    return (f'<div class="q"><span class="q-num">{num}</span><div class="q-text">{qtext}</div>\n'
            f'  <div class="choice-group" data-q="{key}" data-answer="{answer}">{btns}</div></div>\n')


def render_worksheet(d, slug):
    e1t, e1i, e1qs = d['ex1']
    e2t, e2i, e2qs = d['ex2']
    e3t, e3i, e3qs = d['ex3']
    total = len(e1qs) + len(e2qs) + len(e3qs)

    form = [f'<section class="exercise" id="ex1">\n<div class="ex-head">Exercise 1</div>\n'
            f'<div class="ex-title">{e1t}</div>\n<div class="ex-meta">{len(e1qs)} points</div>\n'
            f'<div class="ex-instruct">{e1i}</div>\n']
    for i, (q, opts, a, _) in enumerate(e1qs, 1):
        form.append(mc_q(i, q, opts, a, f'e1q{i}'))

    form.append(f'</section>\n\n<section class="exercise" id="ex2">\n<div class="ex-head">Exercise 2</div>\n'
                f'<div class="ex-title">{e2t}</div>\n<div class="ex-meta">{len(e2qs)} points</div>\n'
                f'<div class="ex-instruct">{e2i}</div>\n')
    for i, (q, a, _) in enumerate(e2qs, 1):
        form.append(f'<div class="q"><span class="q-num">{i}</span><div class="q-text">{q}'
                    f'<br><input type="text" data-q="e2q{i}" style="width:220px" '
                    f'aria-label="Answer e2q{i}"></div></div>\n')

    form.append(f'</section>\n\n<section class="exercise" id="ex3">\n<div class="ex-head">Exercise 3</div>\n'
                f'<div class="ex-title">{e3t}</div>\n<div class="ex-meta">{len(e3qs)} points</div>\n'
                f'<div class="ex-instruct">{e3i}</div>\n')
    for i, (q, opts, a, _) in enumerate(e3qs, 1):
        form.append(mc_q(i, q, opts, a, f'e3q{i}'))

    form.append('<div class="submit-wrap"><button type="submit" class="submit-btn">Check my answers</button></div>\n'
                '</section>\n')

    answers = ',\n'.join(f'  e2q{i}:{{answer:{jd(a)}}}' for i, (_, a, _) in enumerate(e2qs, 1))
    expl = {}
    for i, (_, _, a, x) in enumerate(e1qs, 1):
        expl[f'e1q{i}'] = x
    for i, (_, a, x) in enumerate(e2qs, 1):
        expl[f'e2q{i}'] = x
    for i, (_, _, a, x) in enumerate(e3qs, 1):
        expl[f'e3q{i}'] = x
    expl_js = ',\n'.join(f'  {jd(k)}: {jd(v)}' for k, v in expl.items())

    s = HEAD.format(title=f'{d["short"]} — Exercises {d["level"].upper()} | Word Play',
                    extra_css='<link rel="stylesheet" href="../../../../shared/worksheet.css?v=v107">\n'
                              '<link rel="stylesheet" href="../../../../shared/game.css?v=v112">\n')
    s += '<body>\n' + HEADER + crumb(d, 'Exercises') + nav('worksheet.html')
    s += (f'<h1>{d["title"]}</h1>\n'
          f'<p class="intro-meta">Complete the exercises, then check your answers. Total: {total} points.</p>\n'
          f'<form id="worksheet">\n\n{"".join(form)}</form>\n'
          '<div id="results" class="results-panel" style="display:none"></div>\n'
          '<script>\n'
          f'window.CHAPTER_ID = {jd(slug)};\nwindow.LEVEL = {jd(d["level"])};\n'
          f'window.SECTION = {jd(d["section"])};\n'
          f'window.TOTAL_POINTS = {total};\n'
          f'window.ANSWERS = {{\n{answers}\n}};\n'
          f'window.EXPLANATIONS = {{\n{expl_js}\n}};\n'
          f'window.EXERCISE_TITLES = {{ex1:{jd("Exercise 1 — " + e1t)},ex2:{jd("Exercise 2 — " + e2t)},ex3:{jd("Exercise 3 — " + e3t)}}};\n'
          '</script>\n'
          '<script src="../../../../shared/i18n.js?v=v124"></script>\n'
          '<script src="../../../../shared/store.js?v=v107"></script>\n'
          '<script src="../../../../shared/worksheet.js?v=v108"></script>\n'
          f'<footer class="site-footer">Word Play &middot; French {d["level"].upper()} &middot; Exercises</footer>\n'
          '</body>\n</html>\n')
    return s


def render_game(d, slug):
    items = ',\n'.join(
        '    {id:%s, term:%s, meaning:%s, synonym:%s, example:%s, completion:%s, answer:%s}'
        % tuple(jd(v) for v in fix_grammar_completion(d, it)) for it in d['items'])
    s = HEAD.format(title=f'{d["short"]} — Game {d["level"].upper()} | Word Play',
                    extra_css='<link rel="stylesheet" href="../../../../shared/game.css?v=v112">\n')
    is_vocab = d['section'] == 'vocabulary'
    second_btn_href = 'flashcards.html' if is_vocab else 'worksheet.html'
    second_btn_label = 'Flashcards' if is_vocab else 'Exercises'
    s += '<body>\n' + HEADER + crumb(d, 'Game') + nav('game.html', d['section'])
    s += (f'<div class="container">\n  <h1>{d["short"]} — Mastery Game</h1>\n'
          '  <div class="game-wrap">\n'
          '    <div id="gameStart" class="game-screen active">\n      <div class="game-start">\n'
          '        <h2>Mastery Game</h2>\n'
          f'        <p>{d["game_desc"]}</p>\n'
          '        <div class="game-stats-row">\n'
          '          <div class="game-stat"><div class="game-stat-val" id="gStartMastered">0</div><div class="game-stat-label">Mastered</div></div>\n'
          '          <div class="game-stat"><div class="game-stat-val">/ <span id="gStartTotal">0</span></div><div class="game-stat-label">Total</div></div>\n'
          '        </div>\n'
          '        <div id="gResumeSection" style="display:none;background:var(--cream-deep);border-radius:4px;padding:14px;margin-bottom:16px;">\n'
          '          <p style="font-size:0.9rem;margin-bottom:10px;">You have a saved game.</p>\n'
          '          <div class="game-btn-row">\n'
          '            <button id="gBtnResume" class="game-btn primary">Resume</button>\n'
          '            <button id="gBtnNewFromResume" class="game-btn ghost small">New game</button>\n'
          '          </div>\n        </div>\n'
          '        <div class="game-btn-row"><button id="gBtnStart" class="game-btn primary">Start</button></div>\n'
          '      </div>\n'
          '      <div class="game-ref-panel" style="margin-top:20px;">\n'
          '        <div class="game-ref-head" id="gRefToggle">&#9660; All items — reference</div>\n'
          '        <div class="game-ref-body" id="gRefBody"><div id="gRefList"></div></div>\n'
          '      </div>\n    </div>\n'
          '    <div id="gamePlay" class="game-screen">\n      <div class="game-play"></div>\n    </div>\n'
          '    <div id="gameCompletion" class="game-screen">\n      <div class="game-completion">\n'
          '        <h2>Mastered!</h2>\n        <p>You\'ve completed all items in this chapter.</p>\n'
          '        <div class="game-stats-row" style="margin:20px 0;">\n'
          '          <div class="game-stat"><div class="game-stat-val" id="gFinalScore">0</div><div class="game-stat-label">Score</div></div>\n'
          '          <div class="game-stat"><div class="game-stat-val" id="gFinalStreak">0</div><div class="game-stat-label">Best streak</div></div>\n'
          '          <div class="game-stat"><div class="game-stat-val" id="gFinalPct">0%</div><div class="game-stat-label">Mastered</div></div>\n'
          '        </div>\n        <div id="gMasteryMap"></div>\n'
          '        <div class="game-btn-row">\n'
          '          <button id="gBtnPlayAgain" class="game-btn primary">Play again</button>\n'
          f'          <a href="{second_btn_href}" class="game-btn secondary">{second_btn_label}</a>\n'
          '        </div>\n      </div>\n    </div>\n  </div>\n</div>\n'
          '<div class="game-toast" id="gToast"></div>\n'
          f'<footer class="site-footer">Word Play &middot; French {d["level"].upper()} &middot; Game</footer>\n'
          '<script>\n'
          f'window.GAME_DATA = {{\n  chapterId: {jd(slug)},\n  level: {jd(d["level"])},\n'
          f'  title: {jd(d["title"])},\n  storageKey: {jd("wordplay_game_" + d["level"] + "_" + slug)},\n'
          f'  items: [\n{items}\n  ]\n}};\n'
          '</script>\n'
          '<script src="../../../../shared/i18n.js?v=v124"></script>\n'
          '<script src="../../../../shared/store.js?v=v107"></script>\n'
          '<script src="../../../../shared/game.js?v=v112"></script>\n'
          '</body>\n</html>\n')
    return s


def render_hub(d, slug):
    sec = SECTION_EN[d['section']]
    s = HEAD.format(title=f'{d["short"]} — {sec} {d["level"].upper()} | Word Play', extra_css='')
    s += '<body>\n' + HEADER.replace('href="index.html"', 'href="../index.html"')
    s += ('<div class="section-page">\n'
          '  <div class="breadcrumb">\n'
          '    <a href="../../../../index.html">Home</a><span>&#8250;</span>\n'
          '    <a href="../../../../francais-en/index.html">French for English speakers</a><span>&#8250;</span>\n'
          f'    <a href="../../index.html">{d["level"].upper()}</a><span>&#8250;</span>\n'
          f'    <a href="../index.html">{sec}</a><span>&#8250;</span>\n'
          f'    <strong>{d["short"]}</strong>\n  </div>\n'
          f'  <div class="chapter-num">{d["num"]} &middot; {sec}</div>\n'
          f'  <h1 class="chapter-h1">{d["short"]}</h1>\n'
          '  <div class="activity-grid">\n'
          '    <a href="slides.html" class="activity-card" data-activity="lesson">\n'
          '      <span class="ac-title">Lesson</span>\n'
          '      <p class="ac-desc">Grammar explained in English with French examples</p>\n'
          '      <span class="ac-arrow">&#8594;</span>\n    </a>\n'
          '    <a href="worksheet.html" class="activity-card" data-activity="practice">\n'
          '      <span class="ac-title">Exercises</span>\n'
          '      <p class="ac-desc">Interactive practice with explained answers</p>\n'
          '      <span class="ac-arrow">&#8594;</span>\n    </a>\n'
          '    <a href="game.html" class="activity-card" data-activity="game">\n'
          '      <span class="ac-title">Mastery Game</span>\n'
          '      <p class="ac-desc">Three rounds per concept to lock it in</p>\n'
          '      <span class="ac-arrow">&#8594;</span>\n    </a>\n'
          '  </div>\n</div>\n'
          f'<footer class="site-footer">Word Play &middot; French {d["level"].upper()}</footer>\n'
          '</body>\n</html>\n')
    return s


FC_CSS = '''<style>
.fc-wrap{perspective:800px;margin:0 auto 20px;max-width:480px}
.fc{width:100%;height:220px;position:relative;transform-style:preserve-3d;transition:transform .5s;cursor:pointer;border-radius:10px}
.fc.flipped{transform:rotateY(180deg)}
.fc-face{position:absolute;inset:0;backface-visibility:hidden;border-radius:10px;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:20px;text-align:center;border:1px solid var(--hairline)}
.fc-front,.fc-back{background:var(--paper)}
.fc-back{transform:rotateY(180deg)}
.fc-word{font-size:1.8rem;font-weight:700;color:var(--ink);margin-bottom:6px}
.fc-ipa{font-family:var(--font-sans);font-size:.85rem;color:var(--muted);margin-bottom:8px}
.fc-def{font-size:.95rem;color:var(--ink);margin-bottom:6px}
.fc-ex{font-size:.82rem;color:var(--muted);font-style:italic}
.fc-hint{font-family:var(--font-sans);font-size:.65rem;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-top:10px}
.fc-audio{background:none;border:1px solid var(--hairline);border-radius:4px;padding:5px 12px;font-family:var(--font-sans);font-size:.65rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:var(--muted);cursor:pointer;margin-top:8px}
.fc-audio:hover{border-color:var(--amber);color:var(--amber)}
.fc-nav{display:flex;align-items:center;gap:16px;justify-content:center;margin-bottom:20px}
.fc-btn{font-family:var(--font-sans);font-size:.72rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:9px 18px;border-radius:4px;cursor:pointer;border:1.5px solid var(--hairline);background:transparent;color:var(--ink)}
.fc-btn.primary{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.fc-counter{font-family:var(--font-sans);font-size:.75rem;color:var(--muted);font-weight:600}
.mastery-badge{display:inline-block;padding:8px 18px;background:rgba(184,134,11,.12);color:var(--amber);font-family:var(--font-sans);font-size:.78rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;border-radius:4px;margin-bottom:16px}
</style>\n'''

MATCH_CSS = '''<style>
.match-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:20px}
.match-col{display:flex;flex-direction:column;gap:8px}
.match-item{padding:12px 14px;border:1.5px solid var(--hairline);border-radius:6px;cursor:pointer;font-size:.9rem;color:var(--ink);transition:border-color .15s,background .15s;user-select:none;min-height:48px;display:flex;align-items:center}
.match-item.selected{border-color:var(--amber);background:rgba(184,134,11,.08)}
.match-item.correct{border-color:#2E7D52;background:rgba(46,125,82,.08);pointer-events:none;color:var(--muted)}
.match-item.wrong{border-color:#C03A2B;background:rgba(192,57,43,.08)}
.match-status{font-family:var(--font-sans);font-size:.85rem;color:var(--muted);text-align:center;margin-bottom:16px}
.heart-row{display:flex;gap:6px;justify-content:center;margin-bottom:12px}
.heart-svg{width:22px;height:22px}
</style>\n'''


def render_flashcards(d, slug):
    words = d['words']
    mastery_key = f'wordplay_vocab_{d["level"]}_{slug}_mastered'
    words_js = json.dumps(
        [{'word': w, 'ipa': ipa, 'def': df, 'ex': ex} for w, ipa, df, ex in words],
        ensure_ascii=False, indent=2)
    n = len(words)
    s = HEAD.format(title=f'{d["short"]} — Flashcards | French {d["level"].upper()} | Word Play',
                    extra_css=FC_CSS)
    s += '<body>\n' + HEADER
    s += (f'<div class="container">\n'
          f'<div class="breadcrumb">\n'
          f'  <a href="../../../../index.html">Home</a><span>&#8250;</span>\n'
          f'  <a href="../../../../francais-en/index.html">French for English speakers</a><span>&#8250;</span>\n'
          f'  <a href="../../index.html">{d["level"].upper()}</a><span>&#8250;</span>\n'
          f'  <a href="../index.html">Vocabulary</a><span>&#8250;</span>\n'
          f'  <a href="index.html">{d["short"]}</a><span>&#8250;</span>\n'
          f'  <strong>Flashcards</strong>\n</div>\n'
          f'<div class="chapter-num">{d["num"]}</div>\n'
          f'<h1>{d["short"]}</h1>\n'
          '<nav class="chapter-nav">\n'
          '  <a href="slides.html" class="chapter-nav-btn">Word List</a>\n'
          '  <a href="flashcards.html" class="chapter-nav-btn active">Flashcards</a>\n'
          '  <a href="game.html" class="chapter-nav-btn">Mastery Game</a>\n'
          '  <a href="match.html" class="chapter-nav-btn">Match</a>\n</nav>\n'
          '<div id="masteryBadge" style="margin:12px 0;display:none"><span class="mastery-badge">&#10003; Mastered</span></div>\n'
          f'<p style="font-family:var(--font-sans);font-size:.75rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:var(--muted);margin-bottom:16px">'
          f'{n} words &middot; tap card to see definition</p>\n'
          '<div class="fc-wrap"><div class="fc" id="fc" onclick="flipCard()">\n'
          '  <div class="fc-face fc-front">\n'
          '    <div class="fc-word" id="fcWord"></div>\n'
          '    <div class="fc-ipa" id="fcIpa"></div>\n'
          '    <button class="fc-audio" onclick="event.stopPropagation();speak()">&#9654; Listen</button>\n'
          '    <div class="fc-hint">Tap to reveal</div>\n'
          '  </div>\n'
          '  <div class="fc-face fc-back">\n'
          '    <div class="fc-def" id="fcDef"></div>\n'
          '    <div class="fc-ex" id="fcEx"></div>\n'
          '  </div>\n</div></div>\n'
          '<div class="fc-nav">\n'
          '  <button class="fc-btn" id="btnPrev" onclick="prev()">&#8592; Prev</button>\n'
          '  <span class="fc-counter"><span id="fcIdx">1</span> / <span id="fcTotal"></span></span>\n'
          '  <button class="fc-btn primary" id="btnNext" onclick="next()">Next &#8594;</button>\n'
          '</div>\n'
          '<div style="text-align:center;margin:20px 0">\n'
          '  <button class="fc-btn" onclick="markMastered()" id="btnMastered" style="width:220px">Mark as mastered</button>\n'
          '</div>\n</div>\n'
          f'<footer class="site-footer">Word Play &middot; French {d["level"].upper()} &middot; Vocabulary</footer>\n'
          f'<script>\nconst MASTERY_KEY = {jd(mastery_key)};\n'
          f'const SLUG = {jd(slug)};\nconst LEVEL = {jd(d["level"])};\n'
          f'const WORDS = {words_js};\n'
          'let idx = 0;\n'
          'function showCard() {\n'
          '  const w = WORDS[idx];\n'
          '  document.getElementById("fcWord").textContent = w.word;\n'
          '  document.getElementById("fcIpa").textContent = w.ipa || "";\n'
          '  document.getElementById("fcDef").textContent = w.def;\n'
          '  document.getElementById("fcEx").textContent = w.ex || "";\n'
          '  document.getElementById("fcIdx").textContent = idx + 1;\n'
          '  document.getElementById("fcTotal").textContent = WORDS.length;\n'
          '  document.getElementById("fc").classList.remove("flipped");\n'
          '}\n'
          'function flipCard() { document.getElementById("fc").classList.toggle("flipped"); }\n'
          'function prev() { if (idx > 0) { idx--; showCard(); } }\n'
          'function next() {\n'
          '  if (idx < WORDS.length - 1) { idx++; showCard(); }\n'
          '  else { markMastered(); }\n'
          '}\n'
          'function speak() {\n'
          '  const u = new SpeechSynthesisUtterance(WORDS[idx].word);\n'
          '  u.lang = "fr-FR"; u.rate = 0.9;\n'
          '  speechSynthesis.speak(u);\n'
          '}\n'
          'function markMastered() {\n'
          '  const prog = JSON.parse(localStorage.getItem("wordplay_progress") || "{}");\n'
          '  if (!prog[LEVEL]) prog[LEVEL] = {};\n'
          '  prog[LEVEL]["vocab_mastered_" + SLUG] = { done: true, date: new Date().toISOString() };\n'
          '  localStorage.setItem("wordplay_progress", JSON.stringify(prog));\n'
          '  document.getElementById("masteryBadge").style.display = "block";\n'
          '  if (typeof pushProgress === "function") pushProgress();\n'
          '}\n'
          'function checkMastered() {\n'
          '  try {\n'
          '    const prog = JSON.parse(localStorage.getItem("wordplay_progress") || "{}");\n'
          '    if (prog[LEVEL] && prog[LEVEL]["vocab_mastered_" + SLUG] && prog[LEVEL]["vocab_mastered_" + SLUG].done)\n'
          '      document.getElementById("masteryBadge").style.display = "block";\n'
          '  } catch(e) {}\n'
          '}\n'
          'showCard(); checkMastered();\n'
          '</script>\n'
          '<script src="../../../../shared/store.js?v=v107"></script>\n'
          '</body>\n</html>\n')
    return s


def render_vocab_slides(d, slug):
    """Bilingual word-list lesson: one slide per word, FR term + IPA + EN gloss + FR example."""
    words = d['words']
    level = d['level']
    slides_html = []
    for w, ipa, df, ex in words:
        ipa_part = f'<p class="slide-sub">{ipa}</p>' if ipa else ''
        slides_html.append(
            f'<div class="slide"><div class="slide-card">\n'
            f'<h2 class="slide-h2">{w}</h2>{ipa_part}\n'
            f'<p style="font-size:1.1rem;color:var(--ink);margin-bottom:10px"><strong>{df}</strong></p>\n'
            f'<p style="font-size:.9rem;color:var(--muted);font-style:italic">{ex}</p>\n'
            f'<button onclick="speakWord({json.dumps(w, ensure_ascii=False)})" '
            f'style="margin-top:12px;background:none;border:1px solid var(--hairline);border-radius:4px;'
            f'padding:5px 12px;font-family:var(--font-sans);font-size:.65rem;font-weight:700;'
            f'letter-spacing:1px;text-transform:uppercase;color:var(--muted);cursor:pointer">'
            f'&#9654; Listen</button>\n'
            f'</div></div>\n'
        )
    s = HEAD.format(
        title=f'{d["short"]} — Word List {level.upper()} | Word Play',
        extra_css='<link rel="stylesheet" href="../../../../shared/slides.css?v=v115">\n')
    s += f'<body class="deck-body">\n'
    s += '<div class="deck-progress"><div class="deck-progress-fill" id="deck-progress-fill"></div></div>\n'
    s += HEADER
    s += (f'<div class="breadcrumb">\n'
          f'  <a href="../../../../index.html">Home</a><span>&#8250;</span>\n'
          f'  <a href="../../../../francais-en/index.html">French for English speakers</a><span>&#8250;</span>\n'
          f'  <a href="../../index.html">{level.upper()}</a><span>&#8250;</span>\n'
          f'  <a href="../index.html">Vocabulary</a><span>&#8250;</span>\n'
          f'  <a href="index.html">{d["short"]}</a><span>&#8250;</span>\n'
          f'  <strong>Word List</strong>\n</div>\n')
    s += ('<nav class="chapter-nav">\n'
          '  <a href="slides.html" class="chapter-nav-btn active">Word List</a>\n'
          '  <a href="flashcards.html" class="chapter-nav-btn">Flashcards</a>\n'
          '  <a href="game.html" class="chapter-nav-btn">Mastery Game</a>\n'
          '  <a href="match.html" class="chapter-nav-btn">Match</a>\n</nav>\n')
    s += (f'<div class="chapter-num">{d["num"]} &middot; Vocabulary</div>\n'
          f'<h1>{d["short"]}</h1>\n'
          f'<p class="chapter-subtitle">{d["subtitle"]}</p>\n'
          f'<div class="slide-deck" id="slide-deck">\n{"".join(slides_html)}\n'
          '<div class="slide"><div class="slide-card" style="text-align:center">\n'
          '<h2 class="slide-h2">Ready to practise?</h2>\n'
          '<p style="color:var(--muted);margin-bottom:20px">You\'ve seen all the words. Now test yourself with flashcards.</p>\n'
          '<a href="flashcards.html" style="display:inline-block;padding:14px 32px;background:var(--ink);color:var(--paper);font-family:var(--font-sans);font-size:.82rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;border-radius:4px;text-decoration:none">Practice with Flashcards &#8594;</a>\n'
          '</div></div>\n'
          '</div>\n'
          '<div class="deck-nav">'
          '<button class="deck-btn" id="deck-prev" aria-label="Previous slide">&#9664; Prev</button>'
          '<div class="counter" id="slide-counter"></div>'
          '<button class="deck-btn" id="deck-next" aria-label="Next slide">Next &#9654;</button></div>\n'
          f'<script>\nwindow.CHAPTER_ID = {jd(slug)};\nwindow.LEVEL = {jd(level)};\n'
          f'window.SECTION = "vocabulary";\n'
          f'function speakWord(w) {{\n'
          f'  const u = new SpeechSynthesisUtterance(w);\n'
          f'  u.lang = "fr-FR"; u.rate = 0.9;\n'
          f'  speechSynthesis.speak(u);\n'
          f'}}\n'
          '</script>\n'
          '<script src="../../../../shared/store.js?v=v107"></script>\n'
          '<script src="../../../../shared/deck.js?v=v114"></script>\n'
          f'<footer class="site-footer">Word Play &middot; French {level.upper()} &middot; Vocabulary</footer>\n'
          '</body>\n</html>\n')
    return s


def render_match_vocab(d, slug):
    words = d['words'][:10]  # match uses first 10 words
    mastery_key = f'wordplay_vocab_{d["level"]}_{slug}_mastered'
    pairs_js = json.dumps(
        [{'fr': w, 'en': df} for w, ipa, df, ex in words],
        ensure_ascii=False, indent=2)
    n = len(words)
    total_needed = n * 2
    s = HEAD.format(title=f'{d["short"]} — Match | French {d["level"].upper()} | Word Play',
                    extra_css=MATCH_CSS)
    s += '<body>\n' + HEADER
    s += (f'<div class="container">\n'
          f'<div class="breadcrumb">\n'
          f'  <a href="../../../../index.html">Home</a><span>&#8250;</span>\n'
          f'  <a href="../../../../francais-en/index.html">French for English speakers</a><span>&#8250;</span>\n'
          f'  <a href="../../index.html">{d["level"].upper()}</a><span>&#8250;</span>\n'
          f'  <a href="../index.html">Vocabulary</a><span>&#8250;</span>\n'
          f'  <a href="index.html">{d["short"]}</a><span>&#8250;</span>\n'
          f'  <strong>Match</strong>\n</div>\n'
          f'<div class="chapter-num">{d["num"]}</div>\n'
          f'<h1>{d["short"]} — Match</h1>\n'
          '<nav class="chapter-nav">\n'
          '  <a href="slides.html" class="chapter-nav-btn">Word List</a>\n'
          '  <a href="flashcards.html" class="chapter-nav-btn">Flashcards</a>\n'
          '  <a href="game.html" class="chapter-nav-btn">Mastery Game</a>\n'
          '  <a href="match.html" class="chapter-nav-btn active">Match</a>\n</nav>\n'
          '<div id="masteryBadge" style="margin:12px 0;display:none"><span class="mastery-badge">&#10003; Mastered</span></div>\n'
          '<div class="heart-row" id="heartRow"></div>\n'
          '<div class="match-status" id="matchStatus">Match the French word to its English meaning</div>\n'
          '<div class="match-grid">\n'
          '  <div class="match-col" id="colFr"></div>\n'
          '  <div class="match-col" id="colEn"></div>\n'
          '</div>\n'
          '<div style="text-align:center;margin-top:20px;display:none" id="winMsg">\n'
          '  <div style="font-size:1.4rem;font-weight:700;color:var(--amber);margin-bottom:12px">Well done!</div>\n'
          f'  <a href="game.html" style="display:inline-block;padding:12px 28px;background:var(--ink);color:var(--paper);font-family:var(--font-sans);font-size:.8rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;border-radius:4px;text-decoration:none">Mastery Game &#8594;</a>\n'
          '</div>\n</div>\n'
          f'<footer class="site-footer">Word Play &middot; French {d["level"].upper()} &middot; Match</footer>\n'
          f'<script>\nconst MASTERY_KEY = {jd(mastery_key)};\n'
          f'const SLUG = {jd(slug)};\nconst LEVEL = {jd(d["level"])};\n'
          f'const PAIRS = {pairs_js};\n'
          f'const TOTAL_NEEDED = {total_needed};\n'
          'const LIVES = 3;\n'
          'let lives = LIVES, matched = 0, round = 0, selFr = null, selEn = null;\n'
          'function heartSVG(full) {\n'
          '  return \'<svg class="heart-svg" viewBox="0 0 24 24"><path d="\' + (full\n'
          '    ? "M12 21.593c-5.63-5.539-11-10.297-11-14.402 0-3.791 3.068-5.191 5.281-5.191 1.312 0 4.151.501 5.719 4.457 1.59-3.968 4.464-4.447 5.726-4.447 2.54 0 5.274 1.621 5.274 5.181 0 4.069-5.136 8.625-11 14.402z"\n'
          '    : "M12 21.593c-5.63-5.539-11-10.297-11-14.402 0-3.791 3.068-5.191 5.281-5.191 1.312 0 4.151.501 5.719 4.457 1.59-3.968 4.464-4.447 5.726-4.447 2.54 0 5.274 1.621 5.274 5.181 0 4.069-5.136 8.625-11 14.402z")\n'
          '    + \'" fill="\' + (full ? "currentColor" : "none") + \'" stroke="currentColor" stroke-width="1.5"/></svg>\';\n'
          '}\n'
          'function renderHearts() {\n'
          '  const r = document.getElementById("heartRow");\n'
          '  r.innerHTML = "";\n'
          '  for (let i = 0; i < LIVES; i++) r.innerHTML += heartSVG(i < lives);\n'
          '}\n'
          'function shuffle(a) { for (let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];} return a; }\n'
          'function buildRound() {\n'
          '  const fr = document.getElementById("colFr");\n'
          '  const en = document.getElementById("colEn");\n'
          '  fr.innerHTML = ""; en.innerHTML = "";\n'
          '  const items = shuffle([...PAIRS]);\n'
          '  const defs = shuffle(items.map(p => p.en));\n'
          '  items.forEach((p,i) => {\n'
          '    const bf = document.createElement("div");\n'
          '    bf.className = "match-item"; bf.dataset.id = p.fr; bf.dataset.type = "fr";\n'
          '    bf.textContent = p.fr; bf.onclick = () => selectItem(bf);\n'
          '    fr.appendChild(bf);\n'
          '    const be = document.createElement("div");\n'
          '    be.className = "match-item"; be.dataset.id = defs[i]; be.dataset.type = "en";\n'
          '    be.textContent = defs[i]; be.onclick = () => selectItem(be);\n'
          '    en.appendChild(be);\n'
          '  });\n'
          '  selFr = null; selEn = null;\n'
          '}\n'
          'function selectItem(el) {\n'
          '  if (el.classList.contains("correct")) return;\n'
          '  if (el.dataset.type === "fr") { if (selFr) selFr.classList.remove("selected"); selFr = el; }\n'
          '  else { if (selEn) selEn.classList.remove("selected"); selEn = el; }\n'
          '  el.classList.add("selected");\n'
          '  if (selFr && selEn) checkMatch();\n'
          '}\n'
          'function findEnDef(frWord) {\n'
          '  const p = PAIRS.find(p => p.fr === frWord);\n'
          '  return p ? p.en : null;\n'
          '}\n'
          'function checkMatch() {\n'
          '  const correct = findEnDef(selFr.dataset.id) === selEn.dataset.id;\n'
          '  if (correct) {\n'
          '    selFr.classList.remove("selected"); selFr.classList.add("correct");\n'
          '    selEn.classList.remove("selected"); selEn.classList.add("correct");\n'
          '    matched++;\n'
          '    if (matched >= TOTAL_NEEDED) { winGame(); return; }\n'
          '    if (document.querySelectorAll(".match-item:not(.correct)").length === 0) {\n'
          '      round++; buildRound();\n'
          '    }\n'
          '  } else {\n'
          '    lives--; renderHearts();\n'
          '    selFr.classList.add("wrong"); selEn.classList.add("wrong");\n'
          '    setTimeout(() => { selFr.classList.remove("wrong","selected"); selEn.classList.remove("wrong","selected"); selFr=null; selEn=null; }, 600);\n'
          '    if (lives <= 0) { document.getElementById("matchStatus").textContent = "Game over — try again!"; setTimeout(resetGame, 1200); return; }\n'
          '  }\n'
          '  selFr = null; selEn = null;\n'
          '}\n'
          'function winGame() {\n'
          '  const prog = JSON.parse(localStorage.getItem("wordplay_progress") || "{}");\n'
          '  if (!prog[LEVEL]) prog[LEVEL] = {};\n'
          '  prog[LEVEL]["vocab_mastered_" + SLUG] = { done: true, date: new Date().toISOString() };\n'
          '  localStorage.setItem("wordplay_progress", JSON.stringify(prog));\n'
          '  document.getElementById("masteryBadge").style.display = "block";\n'
          '  document.getElementById("winMsg").style.display = "block";\n'
          '  document.getElementById("matchStatus").textContent = "All matched!";\n'
          '  if (typeof pushProgress === "function") pushProgress();\n'
          '}\n'
          'function resetGame() { lives = LIVES; matched = 0; round = 0; renderHearts(); buildRound(); document.getElementById("matchStatus").textContent = "Match the French word to its English meaning"; }\n'
          'renderHearts(); buildRound();\n'
          '</script>\n'
          '<script src="../../../../shared/store.js?v=v107"></script>\n'
          '</body>\n</html>\n')
    return s


def render_vocab_hub(d, slug):
    s = HEAD.format(title=f'{d["short"]} — Vocabulary {d["level"].upper()} | Word Play', extra_css='')
    s += '<body>\n' + HEADER.replace('href="index.html"', 'href="../index.html"')
    s += ('<div class="section-page">\n'
          '  <div class="breadcrumb">\n'
          '    <a href="../../../../index.html">Home</a><span>&#8250;</span>\n'
          '    <a href="../../../../francais-en/index.html">French for English speakers</a><span>&#8250;</span>\n'
          f'    <a href="../../index.html">{d["level"].upper()}</a><span>&#8250;</span>\n'
          '    <a href="../index.html">Vocabulary</a><span>&#8250;</span>\n'
          f'    <strong>{d["short"]}</strong>\n  </div>\n'
          f'  <div class="chapter-num">{d["num"]} &middot; Vocabulary</div>\n'
          f'  <h1 class="chapter-h1">{d["short"]}</h1>\n'
          f'  <p style="color:var(--muted);font-size:.9rem;margin-bottom:24px">{d["subtitle"]}</p>\n'
          '  <div class="activity-grid">\n'
          '    <a href="slides.html" class="activity-card" data-activity="lesson">\n'
          '      <span class="ac-title">Word List</span>\n'
          f'      <p class="ac-desc">{len(d["words"])} words — bilingual slides with pronunciation</p>\n'
          '      <span class="ac-arrow">&#8594;</span>\n    </a>\n'
          '    <a href="flashcards.html" class="activity-card" data-activity="lesson">\n'
          '      <span class="ac-title">Flashcards</span>\n'
          f'      <p class="ac-desc">{len(d["words"])} words — tap to flip, listen to pronunciation</p>\n'
          '      <span class="ac-arrow">&#8594;</span>\n    </a>\n'
          '    <a href="game.html" class="activity-card" data-activity="game">\n'
          '      <span class="ac-title">Mastery Game</span>\n'
          '      <p class="ac-desc">Three rounds per word to lock it in</p>\n'
          '      <span class="ac-arrow">&#8594;</span>\n    </a>\n'
          '    <a href="match.html" class="activity-card" data-activity="practice">\n'
          '      <span class="ac-title">Match</span>\n'
          '      <p class="ac-desc">Match French words to their English meanings</p>\n'
          '      <span class="ac-arrow">&#8594;</span>\n    </a>\n'
          '  </div>\n</div>\n'
          f'<footer class="site-footer">Word Play &middot; French {d["level"].upper()}</footer>\n'
          '</body>\n</html>\n')
    return s


def render(slug, d):
    out_dir = os.path.join(ROOT, 'francais-en', d['level'], d['section'], slug)
    os.makedirs(out_dir, exist_ok=True)
    if d['section'] == 'vocabulary':
        files = [('slides.html', render_vocab_slides),
                 ('flashcards.html', render_flashcards),
                 ('match.html', render_match_vocab),
                 ('game.html', render_game),
                 ('index.html', render_vocab_hub)]
        validate_files = ('slides.html', 'flashcards.html', 'game.html', 'match.html', 'index.html')
    else:
        files = [('slides.html', render_slides), ('worksheet.html', render_worksheet),
                 ('game.html', render_game), ('index.html', render_hub)]
        validate_files = ('slides.html', 'worksheet.html', 'game.html', 'index.html')
    for fname, fn in files:
        open(os.path.join(out_dir, fname), 'w', encoding='utf-8').write(fn(d, slug))
    r = subprocess.run(
        ['python3', os.path.join(ROOT, 'scripts/validate_inline_js.py')] +
        [os.path.join(out_dir, f) for f in validate_files],
        capture_output=True, text=True)
    print(f'{d["level"]}/{d["section"]}/{slug}: rendered, validate='
          + ('OK' if r.returncode == 0 else 'FAIL\n' + r.stdout))
    return r.returncode == 0


def main():
    spec = importlib.util.spec_from_file_location('content', sys.argv[1])
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    ok = True
    for slug, d in mod.CHAPTERS.items():
        ok = render(slug, d) and ok
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
