#!/usr/bin/env python3
"""Render espanol/ (main Spanish course — taught in Spanish) grammar chapters.

Spanish-native course: UI chrome and pedagogical explanations in Spanish,
target content (examples, exercises, answers) in Spanish. Pages set
<html lang="es"> so shared/i18n.js serves Spanish engine strings.

Content modules expose CHAPTERS = { slug: {...} } with:
  level     'a1' | 'a2' | 'b1' | 'b2' | 'c1' | 'c2'
  section   'grammar' | 'writing' | 'vocabulary'
  num       'G01'
  short     'El Verbo SER'                               (crumb / hub)
  title     'El Verbo SER — Identidad y Descripción'    (page h1)
  subtitle  Spanish one-liner
  slides    [ (h2, sub_or_None, inner_html_es) ]  4-6 slides, Spanish prose,
            examples in <b>
  traps     [ (wrong, right, note_es) x4-5 ]      typical beginner errors
  summary   [ (label_es, form, ex) x5-6 ]
  ex1/ex3   (title_es, instruct_es, [ (qtext, [opts], answer, expl_es) ])  MC
  ex2       (title_es, instruct_es, [ (qtext, answer, expl_es) ])          typed
  game_desc Spanish start-screen sentence
  items     [ (id, term, meaning_es, synonym_es, example, completion, answer) x8 ]

Usage: python3 scripts/gen_espanol.py scripts/content/espanol_a1_g1.py
"""
import importlib.util
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HEAD = '''<!DOCTYPE html>
<html lang="es">
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

HEADER = '''<header class="site-header"><div class="site-header-inner"><a href="index.html" class="back back-link" aria-label="Atrás"></a><a href="/" class="brand"><svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px"><rect width="32" height="32" rx="4" fill="currentColor"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>Word Play</a><button class="dark-toggle" aria-label="Modo oscuro" onclick="toggleDark()">&#9680; Oscuro</button></div></header>
'''

SECTION_ES = {
    'grammar': 'Gramática',
    'writing': 'Escritura',
    'vocabulary': 'Vocabulario',
}


def crumb(d, page_es):
    sec = SECTION_ES[d['section']]
    lv = d['level'].upper()
    return (f'<div class="breadcrumb">\n'
            f'  <a href="../../../../index.html">Inicio</a><span>&#8250;</span>\n'
            f'  <a href="../../../../espanol/index.html">Espa&#241;ol</a><span>&#8250;</span>\n'
            f'  <a href="../../index.html">{lv}</a><span>&#8250;</span>\n'
            f'  <a href="../index.html">{sec}</a><span>&#8250;</span>\n'
            f'  <a href="index.html">{d["short"]}</a><span>&#8250;</span>\n'
            f'  <strong>{page_es}</strong>\n</div>\n')


def nav(active, section):
    has_print = section == 'grammar' or section == 'writing'
    items = [('slides.html', 'Lecci&#243;n'), ('worksheet.html', 'Ejercicios'), ('game.html', 'Juego')]
    if has_print:
        items.append(('printables.html', 'Imprimibles'))
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
        out.append(f'\n<!-- Diapositiva {i} -->\n<div class="slide"><div class="slide-card">\n'
                   f'  <div class="slide-header"><h2>{h2}</h2>{subh}</div>\n  {inner}\n</div></div>\n')
    traps = ''.join(
        f'\n  <div class="trap-row"><div class="trap-wrong">{w}</div>'
        f'<div class="trap-arrow">&#8594;</div><div class="trap-right">{r}</div>'
        f'<div class="trap-note">{n}</div></div>'
        for w, r, n in d['traps'])
    out.append('\n<!-- Errores comunes -->\n<div class="slide"><div class="slide-card">\n'
               '  <div class="slide-header"><h2>Errores comunes</h2>'
               '<p class="slide-sub">Los errores m&#225;s frecuentes de los principiantes</p></div>\n'
               '  <p class="slide-explanation">Estos son los errores que los estudiantes cometen con m&#225;s frecuencia.</p>'
               f'{traps}\n</div></div>\n')
    rows = ''.join(
        f'\n  <div class="summary-row"><div class="label">{l}</div>'
        f'<div class="form">{f}</div><div class="ex">{e}</div></div>'
        for l, f, e in d['summary'])
    out.append(f'\n<!-- Resumen -->\n<div class="slide summary-slide"><div class="slide-card">\n'
               f'  <div class="slide-header"><h2>Resumen: {d["short"]}</h2></div>{rows}\n'
               '  <div style="margin-top:28px;text-align:center"><a href="worksheet.html" '
               'style="display:inline-block;padding:13px 32px;background:var(--amber);color:#1A1A1A;'
               'font-family:var(--font-sans);font-size:.8rem;font-weight:800;letter-spacing:1.5px;'
               'text-transform:uppercase;text-decoration:none;border-radius:5px">A los ejercicios &#8594;</a></div>\n'
               '</div></div>\n')
    return ''.join(out)


def render_slides(d, slug):
    sec_label = SECTION_ES[d['section']]
    lv = d['level'].upper()
    s = HEAD.format(title=f'{d["short"]} — {sec_label} {lv} | Word Play',
                    extra_css='<link rel="stylesheet" href="../../../../shared/slides.css?v=v115">\n')
    s += ('<body class="deck-body">\n'
          '<div class="deck-progress"><div class="deck-progress-fill" id="deck-progress-fill"></div></div>\n')
    s += HEADER + crumb(d, 'Lecci&#243;n') + nav('slides.html', d['section'])
    s += (f'<div class="chapter-num">{d["num"]} &middot; {sec_label}</div>\n'
          f'<h1>{d["title"]}</h1>\n<p class="chapter-subtitle">{d["subtitle"]}</p>\n'
          f'<div class="slide-deck" id="slide-deck">\n{build_slides_html(d)}\n</div>\n'
          '<div class="deck-nav">'
          '<button class="deck-btn" id="deck-prev" aria-label="Diapositiva anterior">&#9664; Ant.</button>'
          '<div class="counter" id="slide-counter"></div>'
          '<button class="deck-btn" id="deck-next" aria-label="Diapositiva siguiente">Sig. &#9654;</button>'
          '</div>\n'
          f'<script>window.CHAPTER_ID={jd(slug)};window.LEVEL={jd(d["level"])};'
          f'window.SECTION={jd("grammar" if d["section"] == "grammar" else "writing")};</script>\n'
          '<script src="../../../../shared/i18n.js?v=v124"></script>\n'
          '<script src="../../../../shared/store.js?v=v107"></script>\n'
          '<script src="../../../../shared/deck.js?v=v114"></script>\n'
          f'<footer class="site-footer">Word Play &middot; Espa&#241;ol {lv} &middot; Lecci&#243;n</footer>\n'
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

    form = [f'<section class="exercise" id="ex1">\n<div class="ex-head">Ejercicio 1</div>\n'
            f'<div class="ex-title">{e1t}</div>\n<div class="ex-meta">{len(e1qs)} puntos</div>\n'
            f'<div class="ex-instruct">{e1i}</div>\n']
    for i, (q, opts, a, _) in enumerate(e1qs, 1):
        form.append(mc_q(i, q, opts, a, f'e1q{i}'))
    form.append(f'</section>\n\n<section class="exercise" id="ex2">\n<div class="ex-head">Ejercicio 2</div>\n'
                f'<div class="ex-title">{e2t}</div>\n<div class="ex-meta">{len(e2qs)} puntos</div>\n'
                f'<div class="ex-instruct">{e2i}</div>\n')
    for i, (q, a, _) in enumerate(e2qs, 1):
        form.append(f'<div class="q"><span class="q-num">{i}</span><div class="q-text">{q}'
                    f'<br><input type="text" data-q="e2q{i}" style="width:220px" '
                    f'aria-label="Respuesta e2q{i}"></div></div>\n')
    form.append(f'</section>\n\n<section class="exercise" id="ex3">\n<div class="ex-head">Ejercicio 3</div>\n'
                f'<div class="ex-title">{e3t}</div>\n<div class="ex-meta">{len(e3qs)} puntos</div>\n'
                f'<div class="ex-instruct">{e3i}</div>\n')
    for i, (q, opts, a, _) in enumerate(e3qs, 1):
        form.append(mc_q(i, q, opts, a, f'e3q{i}'))
    form.append('<div class="submit-wrap"><button type="submit" class="submit-btn">Comprobar respuestas</button></div>\n'
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

    sec_label = SECTION_ES[d['section']]
    lv = d['level'].upper()
    s = HEAD.format(title=f'{d["short"]} — Ejercicios {lv} | Word Play',
                    extra_css=('<link rel="stylesheet" href="../../../../shared/worksheet.css?v=v106">\n'
                               '<link rel="stylesheet" href="../../../../shared/game.css?v=v112">\n'))
    s += '<body>\n' + HEADER + crumb(d, 'Ejercicios') + nav('worksheet.html', d['section'])
    s += (f'<h1>{d["title"]}</h1>\n'
          f'<p class="intro-meta">Completa los ejercicios y comprueba tus respuestas. Total: {total} puntos.</p>\n'
          f'<form id="worksheet">\n\n{"".join(form)}</form>\n'
          '<div id="results" class="results-panel" style="display:none"></div>\n'
          '<script>\n'
          f"window.CHAPTER_ID = {jd(slug)};\nwindow.LEVEL = {jd(d['level'])};\n"
          f"window.SECTION = {jd('grammar' if d['section'] == 'grammar' else 'writing')};\n"
          f'window.TOTAL_POINTS = {total};\n'
          f'window.ANSWERS = {{\n{answers}\n}};\n'
          f'window.EXPLANATIONS = {{\n{expl_js}\n}};\n'
          f'window.EXERCISE_TITLES = {{ex1:{jd("Ejercicio 1 - " + e1t)},ex2:{jd("Ejercicio 2 - " + e2t)},ex3:{jd("Ejercicio 3 - " + e3t)}}};\n'
          '</script>\n'
          '<script src="../../../../shared/i18n.js?v=v124"></script>\n'
          '<script src="../../../../shared/store.js?v=v107"></script>\n'
          '<script src="../../../../shared/worksheet.js?v=v108"></script>\n'
          f'<footer class="site-footer">Word Play &middot; Espa&#241;ol {lv} &middot; Ejercicios</footer>\n'
          '</body>\n</html>\n')
    return s


def render_game(d, slug):
    items_js = ',\n'.join(
        '    {id:%s, term:%s, meaning:%s, synonym:%s, example:%s, completion:%s, answer:%s}'
        % tuple(jd(v) for v in it) for it in d['items'])
    sec_label = SECTION_ES[d['section']]
    lv = d['level'].upper()
    s = HEAD.format(title=f'{d["short"]} — Juego {lv} | Word Play',
                    extra_css='<link rel="stylesheet" href="../../../../shared/game.css?v=v112">\n')
    s += '<body>\n' + HEADER + crumb(d, 'Juego') + nav('game.html', d['section'])
    s += (f'<div class="container">\n  <h1>{d["short"]} — Juego de Dominio</h1>\n'
          '  <div class="game-wrap">\n'
          '    <div id="gameStart" class="game-screen active">\n      <div class="game-start">\n'
          '        <h2>Juego de Dominio</h2>\n'
          f'        <p>{d["game_desc"]}</p>\n'
          '        <p style="font-size:0.8rem;color:var(--muted);margin-top:8px">Aciertos consecutivos del mismo concepto y rachas entre conceptos a&#241;aden puntos extra.</p>\n'
          '        <div class="game-stats-row">\n'
          '          <div class="game-stat"><div class="game-stat-val" id="gStartMastered">0</div><div class="game-stat-label">Dominados</div></div>\n'
          '          <div class="game-stat"><div class="game-stat-val">/ <span id="gStartTotal">0</span></div><div class="game-stat-label">Total</div></div>\n'
          '        </div>\n'
          '        <div id="gResumeSection" style="display:none;background:var(--cream-deep);border-radius:4px;padding:14px;margin-bottom:16px;">\n'
          '          <p style="font-size:0.9rem;margin-bottom:10px;">Tienes una partida guardada.</p>\n'
          '          <div class="game-btn-row">\n'
          '            <button id="gBtnResume" class="game-btn primary">Continuar</button>\n'
          '            <button id="gBtnNewFromResume" class="game-btn ghost small">Nueva partida</button>\n'
          '          </div>\n        </div>\n'
          '        <div class="game-btn-row"><button id="gBtnStart" class="game-btn primary">Empezar</button></div>\n'
          '      </div>\n'
          '      <div class="game-ref-panel" style="margin-top:20px;">\n'
          '        <div class="game-ref-head" id="gRefToggle">&#9660; Referencia — todas las palabras</div>\n'
          '        <div class="game-ref-body" id="gRefBody"><div id="gRefList"></div></div>\n'
          '      </div>\n    </div>\n'
          '    <div id="gamePlay" class="game-screen">\n      <div class="game-play"></div>\n    </div>\n'
          '    <div id="gameCompletion" class="game-screen">\n      <div class="game-completion">\n'
          '        <h2>&#161;Dominio alcanzado!</h2>\n        <p>Has completado todos los elementos de este cap&#237;tulo.</p>\n'
          '        <div class="game-stats-row" style="margin:20px 0;">\n'
          '          <div class="game-stat"><div class="game-stat-val" id="gFinalScore">0</div><div class="game-stat-label">Puntuaci&#243;n</div></div>\n'
          '          <div class="game-stat"><div class="game-stat-val" id="gFinalStreak">0</div><div class="game-stat-label">Mejor racha</div></div>\n'
          '          <div class="game-stat"><div class="game-stat-val" id="gFinalPct">0%</div><div class="game-stat-label">Dominados</div></div>\n'
          '        </div>\n        <div id="gMasteryMap"></div>\n'
          '        <div class="game-btn-row">\n'
          '          <button id="gBtnPlayAgain" class="game-btn primary">Jugar de nuevo</button>\n'
          '          <a href="worksheet.html" class="game-btn secondary">Ejercicios</a>\n'
          '        </div>\n      </div>\n    </div>\n  </div>\n</div>\n'
          '<div class="game-toast" id="gToast"></div>\n'
          f'<footer class="site-footer">Word Play &middot; Espa&#241;ol {lv} &middot; Juego</footer>\n'
          '<script>\n'
          f"window.GAME_DATA = {{\n  chapterId: {jd(slug)},\n  level: {jd(d['level'])},\n"
          f"  title: {jd(d['title'])},\n  storageKey: {jd('wordplay_game_es_' + d['level'] + '_' + slug)},\n"
          f'  items: [\n{items_js}\n  ]\n}};\n'
          '</script>\n'
          '<script src="../../../../shared/i18n.js?v=v124"></script>\n'
          '<script src="../../../../shared/store.js?v=v107"></script>\n'
          '<script src="../../../../shared/game.js?v=v111"></script>\n'
          '</body>\n</html>\n')
    return s


def render_printables(d, slug):
    lv = d['level'].upper()
    sec_label = SECTION_ES[d['section']]

    # Summary table rows
    summary_rows = ''.join(
        f'    <tr><td style="font-weight:700">{l}</td><td style="font-family:Georgia,serif;font-size:1rem">{f}</td><td style="color:#555">{e}</td></tr>\n'
        for l, f, e in d['summary'])

    # Traps table
    trap_rows = ''.join(
        f'    <tr><td style="color:#c0392b">{w}</td><td style="color:#1a7a4a;font-weight:700">{r}</td><td style="color:#555;font-size:.85rem">{n}</td></tr>\n'
        for w, r, n in d['traps'])

    # Exercises
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

    # Answer key
    key_e1 = ''.join(f'  <span style="margin-right:16px"><b>{i}.</b> {a}</span>'
                     for i, (_, _, a, _) in enumerate(e1qs, 1))
    key_e2 = ''.join(f'  <span style="margin-right:16px"><b>{i}.</b> {a}</span>'
                     for i, (_, a, _) in enumerate(e2qs, 1))
    key_e3 = ''.join(f'  <span style="margin-right:16px"><b>{i}.</b> {a}</span>'
                     for i, (_, _, a, _) in enumerate(e3qs, 1))

    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../../favicon.svg" type="image/svg+xml">
<title>{d["short"]} — Imprimibles | Word Play</title>
<link rel="stylesheet" href="../../../../shared/base.css?v=v124">
<link rel="stylesheet" href="../../../../shared/print.css?v=v102">
<script src="/shared/auth.js?v=1"></script>
<script src="../../../../shared/dark-init.js?v=v112"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner"><a href="index.html" class="back back-link" aria-label="Atr&#225;s"></a><a href="/" class="brand"><svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px"><rect width="32" height="32" rx="4" fill="currentColor"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>Word Play</a><button class="dark-toggle" aria-label="Modo oscuro" onclick="toggleDark()">&#9680; Oscuro</button></div></header>
<div class="section-page">
  <div class="breadcrumb">
    <a href="../../../../index.html">Inicio</a><span>&#8250;</span>
    <a href="../../../../espanol/index.html">Espa&#241;ol</a><span>&#8250;</span>
    <a href="../../index.html">{lv}</a><span>&#8250;</span>
    <a href="../index.html">{sec_label}</a><span>&#8250;</span>
    <a href="index.html">{d["short"]}</a><span>&#8250;</span>
    <strong>Imprimibles</strong>
  </div>
  <nav class="chapter-nav">
    <a href="slides.html" class="chapter-nav-btn">Lecci&#243;n</a>
    <a href="worksheet.html" class="chapter-nav-btn">Ejercicios</a>
    <a href="game.html" class="chapter-nav-btn">Juego</a>
    <a href="printables.html" class="chapter-nav-btn active">Imprimibles</a>
  </nav>
  <h1>{d["title"]} — Imprimibles</h1>
  <p style="color:var(--muted);font-family:var(--font-sans);font-size:.85rem;margin-bottom:24px">Referencia, ejercicios y clave de respuestas para imprimir.</p>
  <button class="print-btn" onclick="window.print()">Imprimir / Guardar PDF</button>

  <div class="print-section">
    <h2>Referencia: {d["short"]}</h2>
    <table style="width:100%;border-collapse:collapse;margin-top:12px">
      <thead><tr style="background:var(--amber);color:#1A1A1A">
        <th style="padding:8px;text-align:left">Concepto</th>
        <th style="padding:8px;text-align:left">Forma</th>
        <th style="padding:8px;text-align:left">Ejemplo</th>
      </tr></thead>
      <tbody>
{summary_rows}      </tbody>
    </table>
  </div>

  <div class="print-section" style="margin-top:32px">
    <h2>Errores comunes</h2>
    <table style="width:100%;border-collapse:collapse;margin-top:12px">
      <thead><tr style="background:#f0f0f0">
        <th style="padding:8px;text-align:left">Incorrecto</th>
        <th style="padding:8px;text-align:left">Correcto</th>
        <th style="padding:8px;text-align:left">Explicaci&#243;n</th>
      </tr></thead>
      <tbody>
{trap_rows}      </tbody>
    </table>
  </div>

  <div class="print-section" style="margin-top:32px">
    <h2>Ejercicio 1 — {e1t}</h2>
    <p style="color:var(--muted);font-size:.88rem;margin-bottom:12px">{e1i}</p>
{e1_qs}  </div>

  <div class="print-section" style="margin-top:32px">
    <h2>Ejercicio 2 — {e2t}</h2>
    <p style="color:var(--muted);font-size:.88rem;margin-bottom:12px">{e2i}</p>
{e2_qs}  </div>

  <div class="print-section" style="margin-top:32px">
    <h2>Ejercicio 3 — {e3t}</h2>
    <p style="color:var(--muted);font-size:.88rem;margin-bottom:12px">{e3i}</p>
{e3_qs}  </div>

  <div class="print-section" style="margin-top:32px;background:#f9f6f2;padding:20px;border-radius:6px;page-break-before:always">
    <h2>Clave de respuestas</h2>
    <p><strong>Ejercicio 1:</strong> {key_e1}</p>
    <p style="margin-top:12px"><strong>Ejercicio 2:</strong> {key_e2}</p>
    <p style="margin-top:12px"><strong>Ejercicio 3:</strong> {key_e3}</p>
  </div>
</div>
<footer class="site-footer">Word Play &middot; Espa&#241;ol {lv} &middot; Imprimibles</footer>
<script src="../../../../shared/print.js?v=v102"></script>
</body>
</html>
'''


def render_hub(d, slug):
    sec = SECTION_ES[d['section']]
    lv = d['level'].upper()
    has_print = d['section'] in ('grammar', 'writing')
    s = HEAD.format(title=f'{d["short"]} — {sec} {lv} | Word Play', extra_css='')
    s = s.replace('href="index.html" class="back', 'href="../index.html" class="back')
    s += '<body>\n' + HEADER.replace('href="index.html" class="back', 'href="../index.html" class="back')
    print_card = ''
    if has_print:
        print_card = ('    <a href="printables.html" class="activity-card" data-activity="print" style="--ac-color:#6B6B6B">\n'
                      '      <span class="ac-icon">&#128438;</span>\n'
                      '      <span class="ac-title">Imprimibles</span>\n'
                      '      <p class="ac-desc">Referencia, ejercicios y clave de respuestas para imprimir</p>\n'
                      '      <span class="ac-arrow">&#8594;</span>\n    </a>\n')
    s += ('<div class="section-page">\n'
          '  <div class="breadcrumb">\n'
          '    <a href="../../../../index.html">Inicio</a><span>&#8250;</span>\n'
          f'    <a href="../../index.html">{lv}</a><span>&#8250;</span>\n'
          f'    <a href="../index.html">{sec}</a><span>&#8250;</span>\n'
          f'    <strong>{d["short"]}</strong>\n  </div>\n'
          f'  <div class="chapter-num">{d["num"]} &middot; {sec}</div>\n'
          f'  <h1 class="chapter-h1">{d["short"]}</h1>\n'
          f'  <p class="chapter-subtitle">{d["subtitle"]}</p>\n'
          '  <div class="activity-grid">\n'
          '    <a href="slides.html" class="activity-card" data-activity="lesson" style="--ac-color:var(--amber)">\n'
          '      <span class="ac-icon">&#128214;</span>\n'
          '      <span class="ac-title">Lecci&#243;n</span>\n'
          '      <p class="ac-desc">Explicaciones con ejemplos y tabla de referencia</p>\n'
          '      <span class="ac-arrow">&#8594;</span>\n    </a>\n'
          '    <a href="worksheet.html" class="activity-card" data-activity="practice" style="--ac-color:var(--amber)">\n'
          '      <span class="ac-icon">&#9997;</span>\n'
          '      <span class="ac-title">Ejercicios</span>\n'
          '      <p class="ac-desc">Ejercicios interactivos con correcciones explicadas</p>\n'
          '      <span class="ac-arrow">&#8594;</span>\n    </a>\n'
          '    <a href="game.html" class="activity-card" data-activity="game" style="--ac-color:#2E7D52">\n'
          '      <span class="ac-icon">&#9670;</span>\n'
          '      <span class="ac-title">Juego de Dominio</span>\n'
          '      <p class="ac-desc">4 conceptos &times; 3 tipos de pregunta &mdash; llega a 100 puntos para ganar</p>\n'
          '      <span class="ac-arrow">&#8594;</span>\n    </a>\n'
          + print_card +
          '  </div>\n</div>\n'
          f'<footer class="site-footer">Word Play &middot; Espa&#241;ol {lv}</footer>\n'
          '</body>\n</html>\n')
    return s


def render(slug, d):
    section_dir = d['section']
    out_dir = os.path.join(ROOT, 'espanol', d['level'], section_dir, slug)
    os.makedirs(out_dir, exist_ok=True)
    open(os.path.join(out_dir, 'slides.html'), 'w', encoding='utf-8').write(render_slides(d, slug))
    open(os.path.join(out_dir, 'worksheet.html'), 'w', encoding='utf-8').write(render_worksheet(d, slug))
    open(os.path.join(out_dir, 'game.html'), 'w', encoding='utf-8').write(render_game(d, slug))
    open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8').write(render_hub(d, slug))
    if d['section'] in ('grammar', 'writing'):
        open(os.path.join(out_dir, 'printables.html'), 'w', encoding='utf-8').write(render_printables(d, slug))
    files = [os.path.join(out_dir, f) for f in
             ('slides.html', 'worksheet.html', 'game.html', 'index.html')]
    r = subprocess.run(['python3', os.path.join(ROOT, 'scripts/validate_inline_js.py')] + files,
                       capture_output=True, text=True)
    status = 'OK' if r.returncode == 0 else 'FAIL\n' + r.stdout
    print(f'{d["level"]}/{d["section"]}/{slug}: rendered, validate={status}')
    return r.returncode == 0


def normalize_ex_mc(ex):
    """Convert dict-format MC exercise to (title, instruct, questions) tuple.
    Handles question answers as either string or integer index."""
    if isinstance(ex, tuple):
        title, instruct, qs = ex
        normalized = []
        for q in qs:
            text, opts, a, expl = q
            if isinstance(a, int):
                a = opts[a]
            normalized.append((text, opts, a, expl))
        return (title, instruct, normalized)
    # dict format: dict(title=..., questions=[...])
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
    """Convert dict-format typed exercise to (title, instruct, questions) tuple."""
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
    """Convert dict-format items list to 7-tuple format."""
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
    """Normalize chapter dict to renderer-expected formats."""
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
