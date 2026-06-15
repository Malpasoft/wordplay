#!/usr/bin/env python3
"""Render francais/ (main French course — taught in French) grammar chapters.

French-native course: UI chrome and pedagogical explanations in French,
target content (examples, exercises, answers) in French. Pages set
<html lang="fr"> so shared/i18n.js serves French engine strings.

Content modules expose CHAPTERS = { slug: {...} } with:
  level     'a1' | 'a2' | 'b1' | 'b2' | 'c1' | 'c2'
  section   'grammaire' | 'redaction' | 'vocabulaire'
  num       'G01'
  short     'Les Articles'                              (crumb / hub)
  title     'Les Articles — Définis et Indéfinis'      (page h1)
  subtitle  French one-liner
  slides    [ (h2, sub_or_None, inner_html_fr) ]  4-6 slides, French prose,
            examples in <b>
  traps     [ (wrong, right, note_fr) x4-5 ]      typical learner errors
  summary   [ (label_fr, form, ex) x5-6 ]
  ex1/ex3   (title_fr, instruct_fr, [ (qtext, [opts], answer, expl_fr) ])  MC
  ex2       (title_fr, instruct_fr, [ (qtext, answer, expl_fr) ])          typed
  game_desc French start-screen sentence
  items     [ (id, term, meaning_fr, synonym_fr, example, completion, answer) x8 ]

Usage: python3 scripts/gen_francais.py scripts/content/francais_a1_g1.py
"""
import importlib.util
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HEAD = '''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../../favicon.svg" type="image/svg+xml">
<title>{title}</title>
<link rel="stylesheet" href="../../../../shared/base.css?v=v124">
{extra_css}<script src="/shared/auth.js?v=1"></script>
<script src="../../../../shared/dark-init.js?v=v112"></script>
</head>
'''

HEADER = '''<header class="site-header"><div class="site-header-inner"><a href="index.html" class="back back-link" aria-label="Retour"></a><a href="/" class="brand"><svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px"><rect width="32" height="32" rx="4" fill="currentColor"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>Word Play</a><button class="dark-toggle" aria-label="Basculer mode sombre" onclick="toggleDark()">&#9680; Sombre</button></div></header>
'''

SECTION_FR = {
    'grammaire': 'Grammaire',
    'redaction': 'R&#233;daction',
    'vocabulaire': 'Vocabulaire',
}


def crumb(d, page_fr):
    sec = SECTION_FR[d['section']]
    lv = d['level'].upper()
    return (f'<div class="breadcrumb">\n'
            f'  <a href="../../../../index.html">Accueil</a><span>&#8250;</span>\n'
            f'  <a href="../../../../francais/index.html">Fran&#231;ais</a><span>&#8250;</span>\n'
            f'  <a href="../../index.html">{lv}</a><span>&#8250;</span>\n'
            f'  <a href="../index.html">{sec}</a><span>&#8250;</span>\n'
            f'  <a href="index.html">{d["short"]}</a><span>&#8250;</span>\n'
            f'  <strong>{page_fr}</strong>\n</div>\n')


def nav(active, section):
    has_print = section in ('grammaire', 'redaction')
    items = [('slides.html', 'Le&#231;on'), ('worksheet.html', 'Exercices'), ('game.html', 'Jeu')]
    if has_print:
        items.append(('printables.html', 'Imprimables'))
    btns = ''.join(
        f'  <a href="{h}" class="chapter-nav-btn{" active" if h == active else ""}">{l}</a>\n'
        for h, l in items)
    return f'<nav class="chapter-nav">\n{btns}</nav>\n'


def jd(o):
    return json.dumps(o, ensure_ascii=False)


def build_slides_html(d):
    out = []
    for i, (h2, sub, inner) in enumerate(d['slides'], 1):
        subh = f'<p class="slide-sub">{sub}</p>' if sub else ''
        out.append(f'\n<!-- Diapositive {i} -->\n<div class="slide"><div class="slide-card">\n'
                   f'  <div class="slide-header"><h2>{h2}</h2>{subh}</div>\n  {inner}\n</div></div>\n')
    traps = ''.join(
        f'\n  <div class="trap-row"><div class="trap-wrong">{w}</div>'
        f'<div class="trap-arrow">&#8594;</div><div class="trap-right">{r}</div>'
        f'<div class="trap-note">{n}</div></div>'
        for w, r, n in d['traps'])
    out.append('\n<!-- Erreurs fréquentes -->\n<div class="slide"><div class="slide-card">\n'
               '  <div class="slide-header"><h2>Erreurs fr&#233;quentes</h2>'
               '<p class="slide-sub">Les erreurs les plus courantes des apprenants</p></div>\n'
               '  <p class="slide-explanation">Voici les erreurs que les &#233;tudiants font le plus souvent.</p>'
               f'{traps}\n</div></div>\n')
    rows = ''.join(
        f'\n  <div class="summary-row"><div class="label">{l}</div>'
        f'<div class="form">{f}</div><div class="ex">{e}</div></div>'
        for l, f, e in d['summary'])
    out.append(f'\n<!-- Résumé -->\n<div class="slide summary-slide"><div class="slide-card">\n'
               f'  <div class="slide-header"><h2>R&#233;sum&#233; : {d["short"]}</h2></div>{rows}\n'
               '  <div style="margin-top:28px;text-align:center"><a href="worksheet.html" '
               'style="display:inline-block;padding:13px 32px;background:var(--amber);color:#1A1A1A;'
               'font-family:var(--font-sans);font-size:.8rem;font-weight:800;letter-spacing:1.5px;'
               'text-transform:uppercase;text-decoration:none;border-radius:5px">Aux exercices &#8594;</a></div>\n'
               '</div></div>\n')
    return ''.join(out)


def render_slides(d, slug):
    sec_label = SECTION_FR[d['section']]
    lv = d['level'].upper()
    s = HEAD.format(title=f'{d["short"]} — {sec_label} {lv} | Word Play',
                    extra_css='<link rel="stylesheet" href="../../../../shared/slides.css?v=v115">\n')
    s += ('<body class="deck-body">\n'
          '<div class="deck-progress"><div class="deck-progress-fill" id="deck-progress-fill"></div></div>\n')
    s += HEADER + crumb(d, 'Le&#231;on') + nav('slides.html', d['section'])
    s += (f'<div class="chapter-num">{d["num"]} &middot; {sec_label}</div>\n'
          f'<h1>{d["title"]}</h1>\n<p class="chapter-subtitle">{d["subtitle"]}</p>\n'
          f'<div class="slide-deck" id="slide-deck">\n{build_slides_html(d)}\n</div>\n'
          '<div class="deck-nav">'
          '<button class="deck-btn" id="deck-prev" aria-label="Diapositive pr&#233;c&#233;dente">&#9664; Pr&#233;c.</button>'
          '<div class="counter" id="slide-counter"></div>'
          '<button class="deck-btn" id="deck-next" aria-label="Diapositive suivante">Suiv. &#9654;</button>'
          '</div>\n'
          f'<script>window.CHAPTER_ID={jd(slug)};window.LEVEL={jd(d["level"])};'
          f'window.SECTION={jd("grammar" if d["section"] == "grammaire" else "writing")};</script>\n'
          '<script src="../../../../shared/i18n.js?v=v124"></script>\n'
          '<script src="../../../../shared/store.js?v=v107"></script>\n'
          '<script src="../../../../shared/deck.js?v=v114"></script>\n'
          f'<footer class="site-footer">Word Play &middot; Fran&#231;ais {lv} &middot; Le&#231;on</footer>\n'
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

    form = [f'<section class="exercise" id="ex1">\n<div class="ex-head">Exercice 1</div>\n'
            f'<div class="ex-title">{e1t}</div>\n<div class="ex-meta">{len(e1qs)} points</div>\n'
            f'<div class="ex-instruct">{e1i}</div>\n']
    for i, (q, opts, a, _) in enumerate(e1qs, 1):
        form.append(mc_q(i, q, opts, a, f'e1q{i}'))
    form.append(f'</section>\n\n<section class="exercise" id="ex2">\n<div class="ex-head">Exercice 2</div>\n'
                f'<div class="ex-title">{e2t}</div>\n<div class="ex-meta">{len(e2qs)} points</div>\n'
                f'<div class="ex-instruct">{e2i}</div>\n')
    for i, (q, a, _) in enumerate(e2qs, 1):
        form.append(f'<div class="q"><span class="q-num">{i}</span><div class="q-text">{q}'
                    f'<br><input type="text" data-q="e2q{i}" style="width:220px" '
                    f'aria-label="R&#233;ponse e2q{i}"></div></div>\n')
    form.append(f'</section>\n\n<section class="exercise" id="ex3">\n<div class="ex-head">Exercice 3</div>\n'
                f'<div class="ex-title">{e3t}</div>\n<div class="ex-meta">{len(e3qs)} points</div>\n'
                f'<div class="ex-instruct">{e3i}</div>\n')
    for i, (q, opts, a, _) in enumerate(e3qs, 1):
        form.append(mc_q(i, q, opts, a, f'e3q{i}'))
    form.append('<div class="submit-wrap"><button type="submit" class="submit-btn">V&#233;rifier les r&#233;ponses</button></div>\n'
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

    sec_label = SECTION_FR[d['section']]
    lv = d['level'].upper()
    s = HEAD.format(title=f'{d["short"]} — Exercices {lv} | Word Play',
                    extra_css=('<link rel="stylesheet" href="../../../../shared/worksheet.css?v=v106">\n'
                               '<link rel="stylesheet" href="../../../../shared/game.css?v=v112">\n'))
    s += '<body>\n' + HEADER + crumb(d, 'Exercices') + nav('worksheet.html', d['section'])
    s += (f'<h1>{d["title"]}</h1>\n'
          f'<p class="intro-meta">Compl&#232;te les exercices et v&#233;rifie tes r&#233;ponses. Total : {total} points.</p>\n'
          f'<form id="worksheet">\n\n{"".join(form)}</form>\n'
          '<div id="results" class="results-panel" style="display:none"></div>\n'
          '<script>\n'
          f"window.CHAPTER_ID = {jd(slug)};\nwindow.LEVEL = {jd(d['level'])};\n"
          f"window.SECTION = {jd('grammar' if d['section'] == 'grammaire' else 'writing')};\n"
          f'window.TOTAL_POINTS = {total};\n'
          f'window.ANSWERS = {{\n{answers}\n}};\n'
          f'window.EXPLANATIONS = {{\n{expl_js}\n}};\n'
          f'window.EXERCISE_TITLES = {{ex1:{jd("Exercice 1 - " + e1t)},ex2:{jd("Exercice 2 - " + e2t)},ex3:{jd("Exercice 3 - " + e3t)}}};\n'
          '</script>\n'
          '<script src="../../../../shared/i18n.js?v=v124"></script>\n'
          '<script src="../../../../shared/store.js?v=v107"></script>\n'
          '<script src="../../../../shared/worksheet.js?v=v108"></script>\n'
          f'<footer class="site-footer">Word Play &middot; Fran&#231;ais {lv} &middot; Exercices</footer>\n'
          '</body>\n</html>\n')
    return s


def render_game(d, slug):
    items_js = ',\n'.join(
        '    {id:%s, term:%s, meaning:%s, synonym:%s, example:%s, completion:%s, answer:%s}'
        % tuple(jd(v) for v in it) for it in d['items'])
    sec_label = SECTION_FR[d['section']]
    lv = d['level'].upper()
    s = HEAD.format(title=f'{d["short"]} — Jeu {lv} | Word Play',
                    extra_css='<link rel="stylesheet" href="../../../../shared/game.css?v=v112">\n')
    s += '<body>\n' + HEADER + crumb(d, 'Jeu') + nav('game.html', d['section'])
    s += (f'<div class="container">\n  <h1>{d["short"]} — Jeu de Ma&#238;trise</h1>\n'
          '  <div class="game-wrap">\n'
          '    <div id="gameStart" class="game-screen active">\n      <div class="game-start">\n'
          '        <h2>Jeu de Ma&#238;trise</h2>\n'
          f'        <p>{d["game_desc"]}</p>\n'
          '        <p style="font-size:0.8rem;color:var(--muted);margin-top:8px">Les r&#233;ponses cons&#233;cutives sur le m&#234;me concept et les s&#233;ries entre concepts rapportent des points bonus.</p>\n'
          '        <div class="game-stats-row">\n'
          '          <div class="game-stat"><div class="game-stat-val" id="gStartMastered">0</div><div class="game-stat-label">Ma&#238;tris&#233;s</div></div>\n'
          '          <div class="game-stat"><div class="game-stat-val">/ <span id="gStartTotal">0</span></div><div class="game-stat-label">Total</div></div>\n'
          '        </div>\n'
          '        <div id="gResumeSection" style="display:none;background:var(--cream-deep);border-radius:4px;padding:14px;margin-bottom:16px;">\n'
          '          <p style="font-size:0.9rem;margin-bottom:10px;">Vous avez une partie sauvegard&#233;e.</p>\n'
          '          <div class="game-btn-row">\n'
          '            <button id="gBtnResume" class="game-btn primary">Reprendre</button>\n'
          '            <button id="gBtnNewFromResume" class="game-btn ghost small">Nouvelle partie</button>\n'
          '          </div>\n        </div>\n'
          '        <div class="game-btn-row"><button id="gBtnStart" class="game-btn primary">D&#233;marrer</button></div>\n'
          '      </div>\n'
          '      <div class="game-ref-panel" style="margin-top:20px;">\n'
          '        <div class="game-ref-head" id="gRefToggle">&#9660; R&#233;f&#233;rence — tous les concepts</div>\n'
          '        <div class="game-ref-body" id="gRefBody"><div id="gRefList"></div></div>\n'
          '      </div>\n    </div>\n'
          '    <div id="gamePlay" class="game-screen">\n      <div class="game-play"></div>\n    </div>\n'
          '    <div id="gameCompletion" class="game-screen">\n      <div class="game-completion">\n'
          '        <h2>Ma&#238;trise atteinte !</h2>\n        <p>Vous avez compl&#233;t&#233; tous les &#233;l&#233;ments de ce chapitre.</p>\n'
          '        <div class="game-stats-row" style="margin:20px 0;">\n'
          '          <div class="game-stat"><div class="game-stat-val" id="gFinalScore">0</div><div class="game-stat-label">Score</div></div>\n'
          '          <div class="game-stat"><div class="game-stat-val" id="gFinalStreak">0</div><div class="game-stat-label">Meilleure s&#233;rie</div></div>\n'
          '          <div class="game-stat"><div class="game-stat-val" id="gFinalPct">0%</div><div class="game-stat-label">Ma&#238;tris&#233;s</div></div>\n'
          '        </div>\n        <div id="gMasteryMap"></div>\n'
          '        <div class="game-btn-row">\n'
          '          <button id="gBtnPlayAgain" class="game-btn primary">Rejouer</button>\n'
          '          <a href="worksheet.html" class="game-btn secondary">Exercices</a>\n'
          '        </div>\n      </div>\n    </div>\n  </div>\n</div>\n'
          '<div class="game-toast" id="gToast"></div>\n'
          f'<footer class="site-footer">Word Play &middot; Fran&#231;ais {lv} &middot; Jeu</footer>\n'
          '<script>\n'
          f"window.GAME_DATA = {{\n  chapterId: {jd(slug)},\n  level: {jd(d['level'])},\n"
          f"  title: {jd(d['title'])},\n  storageKey: {jd('wordplay_game_fr_' + d['level'] + '_' + slug)},\n"
          f'  items: [\n{items_js}\n  ]\n}};\n'
          '</script>\n'
          '<script src="../../../../shared/i18n.js?v=v124"></script>\n'
          '<script src="../../../../shared/store.js?v=v107"></script>\n'
          '<script src="../../../../shared/game.js?v=v111"></script>\n'
          '</body>\n</html>\n')
    return s


def render_printables(d, slug):
    lv = d['level'].upper()
    sec_label = SECTION_FR[d['section']]

    summary_rows = ''.join(
        f'    <tr><td style="font-weight:700">{l}</td><td style="font-family:Georgia,serif;font-size:1rem">{f}</td><td style="color:#555">{e}</td></tr>\n'
        for l, f, e in d['summary'])
    trap_rows = ''.join(
        f'    <tr><td style="color:#c0392b">{w}</td><td style="color:#1a7a4a;font-weight:700">{r}</td><td style="color:#555;font-size:.85rem">{n}</td></tr>\n'
        for w, r, n in d['traps'])

    e1t, e1i, e1qs = d['ex1']
    e2t, e2i, e2qs = d['ex2']
    e3t, e3i, e3qs = d['ex3']

    e1_qs = ''.join(
        f'<div style="margin:10px 0"><span style="font-weight:700">{i}.</span> {q} '
        f'[{" / ".join(opts)}]</div>\n'
        for i, (q, opts, a, _) in enumerate(e1qs, 1))
    e2_qs = ''.join(
        f'<div style="margin:10px 0"><span style="font-weight:700">{i}.</span> {q} '
        f'<span style="display:inline-block;width:120px;border-bottom:1px solid #999">&nbsp;</span></div>\n'
        for i, (q, a, _) in enumerate(e2qs, 1))
    e3_qs = ''.join(
        f'<div style="margin:10px 0"><span style="font-weight:700">{i}.</span> {q} '
        f'[{" / ".join(opts)}]</div>\n'
        for i, (q, opts, a, _) in enumerate(e3qs, 1))

    key_e1 = ''.join(f'  <span style="margin-right:16px"><b>{i}.</b> {a}</span>'
                     for i, (_, _, a, _) in enumerate(e1qs, 1))
    key_e2 = ''.join(f'  <span style="margin-right:16px"><b>{i}.</b> {a}</span>'
                     for i, (_, a, _) in enumerate(e2qs, 1))
    key_e3 = ''.join(f'  <span style="margin-right:16px"><b>{i}.</b> {a}</span>'
                     for i, (_, _, a, _) in enumerate(e3qs, 1))

    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../../favicon.svg" type="image/svg+xml">
<title>{d["short"]} — Imprimables | Word Play</title>
<link rel="stylesheet" href="../../../../shared/base.css?v=v124">
<link rel="stylesheet" href="../../../../shared/print.css?v=v102">
<script src="/shared/auth.js?v=1"></script>
<script src="../../../../shared/dark-init.js?v=v112"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner"><a href="index.html" class="back back-link" aria-label="Retour"></a><a href="/" class="brand"><svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px"><rect width="32" height="32" rx="4" fill="currentColor"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>Word Play</a><button class="dark-toggle" aria-label="Basculer mode sombre" onclick="toggleDark()">&#9680; Sombre</button></div></header>
<div class="section-page">
  <div class="breadcrumb">
    <a href="../../../../index.html">Accueil</a><span>&#8250;</span>
    <a href="../../../../francais/index.html">Fran&#231;ais</a><span>&#8250;</span>
    <a href="../../index.html">{lv}</a><span>&#8250;</span>
    <a href="../index.html">{sec_label}</a><span>&#8250;</span>
    <a href="index.html">{d["short"]}</a><span>&#8250;</span>
    <strong>Imprimables</strong>
  </div>
  <nav class="chapter-nav">
    <a href="slides.html" class="chapter-nav-btn">Le&#231;on</a>
    <a href="worksheet.html" class="chapter-nav-btn">Exercices</a>
    <a href="game.html" class="chapter-nav-btn">Jeu</a>
    <a href="printables.html" class="chapter-nav-btn active">Imprimables</a>
  </nav>
  <h1>{d["title"]} — Imprimables</h1>
  <p style="color:var(--muted);font-family:var(--font-sans);font-size:.85rem;margin-bottom:24px">R&#233;f&#233;rence, exercices et cl&#233; des r&#233;ponses &#224; imprimer.</p>
  <button class="print-btn" onclick="window.print()">Imprimer / Enregistrer en PDF</button>

  <div class="print-section">
    <h2>R&#233;f&#233;rence : {d["short"]}</h2>
    <table style="width:100%;border-collapse:collapse;margin-top:12px">
      <thead><tr style="background:var(--amber);color:#1A1A1A">
        <th style="padding:8px;text-align:left">Concept</th>
        <th style="padding:8px;text-align:left">Forme</th>
        <th style="padding:8px;text-align:left">Exemple</th>
      </tr></thead>
      <tbody>
{summary_rows}      </tbody>
    </table>
  </div>

  <div class="print-section" style="margin-top:32px">
    <h2>Erreurs fr&#233;quentes</h2>
    <table style="width:100%;border-collapse:collapse;margin-top:12px">
      <thead><tr style="background:#f0f0f0">
        <th style="padding:8px;text-align:left">Incorrect</th>
        <th style="padding:8px;text-align:left">Correct</th>
        <th style="padding:8px;text-align:left">Explication</th>
      </tr></thead>
      <tbody>
{trap_rows}      </tbody>
    </table>
  </div>

  <div class="print-section" style="margin-top:32px">
    <h2>Exercice 1 — {e1t}</h2>
    <p style="color:var(--muted);font-size:.88rem;margin-bottom:12px">{e1i}</p>
{e1_qs}  </div>

  <div class="print-section" style="margin-top:32px">
    <h2>Exercice 2 — {e2t}</h2>
    <p style="color:var(--muted);font-size:.88rem;margin-bottom:12px">{e2i}</p>
{e2_qs}  </div>

  <div class="print-section" style="margin-top:32px">
    <h2>Exercice 3 — {e3t}</h2>
    <p style="color:var(--muted);font-size:.88rem;margin-bottom:12px">{e3i}</p>
{e3_qs}  </div>

  <div class="print-section" style="margin-top:32px;background:#f9f6f2;padding:20px;border-radius:6px;page-break-before:always">
    <h2>Cl&#233; des r&#233;ponses</h2>
    <p><strong>Exercice 1 :</strong> {key_e1}</p>
    <p style="margin-top:12px"><strong>Exercice 2 :</strong> {key_e2}</p>
    <p style="margin-top:12px"><strong>Exercice 3 :</strong> {key_e3}</p>
  </div>
</div>
<footer class="site-footer">Word Play &middot; Fran&#231;ais {lv} &middot; Imprimables</footer>
<script src="../../../../shared/print.js?v=v102"></script>
</body>
</html>
'''


def render_hub(d, slug):
    sec = SECTION_FR[d['section']]
    lv = d['level'].upper()
    has_print = d['section'] in ('grammaire', 'redaction')
    s = HEAD.format(title=f'{d["short"]} — {sec} {lv} | Word Play', extra_css='')
    s = s.replace('href="index.html" class="back', 'href="../index.html" class="back')
    s += '<body>\n' + HEADER.replace('href="index.html" class="back', 'href="../index.html" class="back')
    print_card = ''
    if has_print:
        print_card = ('    <a href="printables.html" class="activity-card" data-activity="print" style="--ac-color:#6B6B6B">\n'
                      '      <span class="ac-icon">&#128438;</span>\n'
                      '      <span class="ac-title">Imprimables</span>\n'
                      '      <p class="ac-desc">R&#233;f&#233;rence, exercices et cl&#233; des r&#233;ponses &#224; imprimer</p>\n'
                      '      <span class="ac-arrow">&#8594;</span>\n    </a>\n')
    s += ('<div class="section-page">\n'
          '  <div class="breadcrumb">\n'
          '    <a href="../../../../index.html">Accueil</a><span>&#8250;</span>\n'
          '    <a href="../../../../francais/index.html">Fran&#231;ais</a><span>&#8250;</span>\n'
          f'    <a href="../../index.html">{lv}</a><span>&#8250;</span>\n'
          f'    <a href="../index.html">{sec}</a><span>&#8250;</span>\n'
          f'    <strong>{d["short"]}</strong>\n  </div>\n'
          f'  <div class="chapter-num">{d["num"]} &middot; {sec}</div>\n'
          f'  <h1 class="chapter-h1">{d["short"]}</h1>\n'
          f'  <p class="chapter-subtitle">{d["subtitle"]}</p>\n'
          '  <div class="activity-grid">\n'
          '    <a href="slides.html" class="activity-card" data-activity="lesson" style="--ac-color:var(--amber)">\n'
          '      <span class="ac-icon">&#128214;</span>\n'
          '      <span class="ac-title">Le&#231;on</span>\n'
          '      <p class="ac-desc">Explications avec exemples et tableau de r&#233;f&#233;rence</p>\n'
          '      <span class="ac-arrow">&#8594;</span>\n    </a>\n'
          '    <a href="worksheet.html" class="activity-card" data-activity="practice" style="--ac-color:var(--amber)">\n'
          '      <span class="ac-icon">&#9997;</span>\n'
          '      <span class="ac-title">Exercices</span>\n'
          '      <p class="ac-desc">Exercices interactifs avec corrections expliqu&#233;es</p>\n'
          '      <span class="ac-arrow">&#8594;</span>\n    </a>\n'
          '    <a href="game.html" class="activity-card" data-activity="game" style="--ac-color:#2E7D52">\n'
          '      <span class="ac-icon">&#9670;</span>\n'
          '      <span class="ac-title">Jeu de Ma&#238;trise</span>\n'
          '      <p class="ac-desc">4 concepts &times; 3 types de question &mdash; atteignez 100 points pour gagner</p>\n'
          '      <span class="ac-arrow">&#8594;</span>\n    </a>\n'
          + print_card +
          '  </div>\n</div>\n'
          f'<footer class="site-footer">Word Play &middot; Fran&#231;ais {lv}</footer>\n'
          '</body>\n</html>\n')
    return s


def render(slug, d):
    section_dir = d['section']
    out_dir = os.path.join(ROOT, 'francais', d['level'], section_dir, slug)
    os.makedirs(out_dir, exist_ok=True)
    open(os.path.join(out_dir, 'slides.html'), 'w', encoding='utf-8').write(render_slides(d, slug))
    open(os.path.join(out_dir, 'worksheet.html'), 'w', encoding='utf-8').write(render_worksheet(d, slug))
    open(os.path.join(out_dir, 'game.html'), 'w', encoding='utf-8').write(render_game(d, slug))
    open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8').write(render_hub(d, slug))
    if d['section'] in ('grammaire', 'redaction'):
        open(os.path.join(out_dir, 'printables.html'), 'w', encoding='utf-8').write(render_printables(d, slug))
    files = [os.path.join(out_dir, f) for f in
             ('slides.html', 'worksheet.html', 'game.html', 'index.html')]
    r = subprocess.run(['python3', os.path.join(ROOT, 'scripts/validate_inline_js.py')] + files,
                       capture_output=True, text=True)
    status = 'OK' if r.returncode == 0 else 'FAIL\n' + r.stdout
    print(f'{d["level"]}/{d["section"]}/{slug}: rendered, validate={status}')
    return r.returncode == 0


def normalize_ex_mc(ex):
    if isinstance(ex, tuple):
        title, instruct, qs = ex
        normalized = []
        for q in qs:
            text, opts, a, expl = q
            if isinstance(a, int):
                a = opts[a]
            normalized.append((text, opts, a, expl))
        return (title, instruct, normalized)
    title = ex['title']
    instruct = ex.get('instruct', '')
    qs = []
    for q in ex['questions']:
        text, opts, a, expl = q
        if isinstance(a, int):
            a = opts[a]
        qs.append((text, opts, a, expl))
    return (title, instruct, qs)


def normalize_ex_typed(ex):
    if isinstance(ex, tuple):
        title, instruct, qs = ex
        normalized = []
        for q in qs:
            if len(q) == 4:
                text, answer, _accepted, expl = q
            else:
                text, answer, expl = q
            normalized.append((text, answer, expl))
        return (title, instruct, normalized)
    title = ex['title']
    instruct = ex.get('instruct', '')
    qs = []
    for q in ex['questions']:
        if len(q) == 4:
            text, answer, _accepted, expl = q
        else:
            text, answer, expl = q
        qs.append((text, answer, expl))
    return (title, instruct, qs)


def normalize_items(items, slug):
    if not items:
        return items
    if isinstance(items[0], dict):
        result = []
        for i, item in enumerate(items):
            term = item['term']
            definition = item['definition']
            example = item['example']
            accepts = item.get('accept', [term])
            answer = accepts[0] if accepts else term
            fill = example.replace(term, '______') if term in example else example
            result.append((f'{slug}-{i+1:02d}', term, definition, definition[:40], example, fill, answer))
        return result
    return items


def normalize_chapter(d, slug):
    d = dict(d)
    d['ex1'] = normalize_ex_mc(d['ex1'])
    d['ex2'] = normalize_ex_typed(d['ex2'])
    d['ex3'] = normalize_ex_mc(d['ex3'])
    d['items'] = normalize_items(d['items'], slug)
    return d


def main():
    mod_path = sys.argv[1]
    spec = importlib.util.spec_from_file_location('content', mod_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    ok = True
    for slug, d in mod.CHAPTERS.items():
        ok = render(slug, normalize_chapter(d, slug)) and ok
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
