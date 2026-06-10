#!/usr/bin/env python3
"""Render fr/ (English course for French speakers) grammar & redaction chapters.

French-mediated course: UI chrome and pedagogical explanations in French,
target content (examples, questions, answers) in English. Pages set
<html lang="fr"> so shared/i18n.js (v124+) serves French engine strings.

Content modules expose CHAPTERS = { slug: {...} } with:
  level     'b1' | 'b2'
  section   'grammaire' | 'redaction'
  num       'Ch. 5'
  short     'Future Forms'                        (crumb / hub)
  title     'Future Forms — Le futur en anglais'  (page h1)
  subtitle  French one-liner
  slides    [ (h2, sub_or_None, inner_html_fr) ]  4-6 slides, French prose,
            English examples in <b>
  traps     [ (wrong, right, note_fr) x4-5 ]      francophone-specific errors
  summary   [ (label_fr, form, ex) x5-6 ]
  ex1/ex3   (title_fr, instruct_fr, [ (qtext, [opts], answer, expl_fr) ])  MC
  ex2       (title_fr, instruct_fr, [ (qtext, answer, expl_fr) ])          typed
  game_desc French start-screen sentence
  items     [ (id, term, meaning_fr, synonym_fr, example, completion, answer) x8 ]

Usage: python3 scripts/gen_fr.py scripts/content/fr_b1_g1.py
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

HEADER = '''<header class="site-header"><div class="site-header-inner"><a href="index.html" class="back back-link" aria-label="Retour"></a><a href="/" class="brand"><svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px"><rect width="32" height="32" rx="4" fill="currentColor"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>Word Play</a><button class="dark-toggle" aria-label="Mode sombre" onclick="toggleDark()">&#9680; Sombre</button></div></header>
'''

SECTION_FR = {'grammaire': 'Grammaire', 'redaction': 'Rédaction', 'vocabulaire': 'Vocabulaire'}


def crumb(d, page_fr):
    sec = SECTION_FR[d['section']]
    return (f'<div class="breadcrumb">\n'
            f'  <a href="../../../../index.html">Accueil</a><span>&#8250;</span>\n'
            f'  <a href="../../../../fr/index.html">Anglais pour francophones</a><span>&#8250;</span>\n'
            f'  <a href="../../index.html">{d["level"].upper()}</a><span>&#8250;</span>\n'
            f'  <a href="../index.html">{sec}</a><span>&#8250;</span>\n'
            f'  <a href="index.html">{d["short"]}</a><span>&#8250;</span>\n'
            f'  <strong>{page_fr}</strong>\n</div>\n')


def nav(active):
    items = [('slides.html', 'Leçon'), ('worksheet.html', 'Exercices'), ('game.html', 'Jeu')]
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
        out.append(f'\n<!-- Slide {i} -->\n<div class="slide"><div class="slide-card">\n'
                   f'  <div class="slide-header"><h2>{h2}</h2>{subh}</div>\n  {inner}\n</div></div>\n')
    traps = ''.join(
        f'\n  <div class="trap-row"><div class="trap-wrong">{w}</div>'
        f'<div class="trap-arrow">→</div><div class="trap-right">{r}</div>'
        f'<div class="trap-note">{n}</div></div>'
        for w, r, n in d['traps'])
    out.append('\n<!-- Erreurs typiques -->\n<div class="slide"><div class="slide-card">\n'
               '  <div class="slide-header"><h2>Erreurs typiques</h2>'
               '<p class="slide-sub">Les pièges classiques pour les francophones</p></div>\n'
               '  <p class="slide-explanation">Voici les erreurs que les francophones font le plus souvent sur ce point.</p>'
               f'{traps}\n</div></div>\n')
    rows = ''.join(
        f'\n  <div class="summary-row"><div class="label">{l}</div>'
        f'<div class="form">{f}</div><div class="ex">{e}</div></div>'
        for l, f, e in d['summary'])
    out.append('\n<!-- Récapitulatif -->\n<div class="slide summary-slide"><div class="slide-card">\n'
               f'  <div class="slide-header"><h2>Récapitulatif : {d["short"]}</h2></div>{rows}\n'
               '  <div style="margin-top:28px;text-align:center"><a href="worksheet.html" '
               'style="display:inline-block;padding:13px 32px;background:var(--amber);color:#1A1A1A;'
               'font-family:var(--font-sans);font-size:.8rem;font-weight:800;letter-spacing:1.5px;'
               'text-transform:uppercase;text-decoration:none;border-radius:5px">Aux exercices →</a></div>\n'
               '</div></div>\n')
    return ''.join(out)


def render_slides(d, slug):
    sec_label = 'Grammaire' if d['section'] == 'grammaire' else 'Rédaction'
    s = HEAD.format(title=f'{d["short"]} — {sec_label} {d["level"].upper()} | Word Play',
                    extra_css='<link rel="stylesheet" href="../../../../shared/slides.css?v=v115">\n')
    s += ('<body class="deck-body">\n'
          '<div class="deck-progress"><div class="deck-progress-fill" id="deck-progress-fill"></div></div>\n')
    s += HEADER + crumb(d, 'Leçon') + nav('slides.html')
    s += (f'<div class="chapter-num">{d["num"]} &middot; {sec_label}</div>\n'
          f'<h1>{d["title"]}</h1>\n<p class="chapter-subtitle">{d["subtitle"]}</p>\n'
          f'<div class="slide-deck" id="slide-deck">\n{build_slides_html(d)}\n</div>\n'
          '<div class="deck-nav"><button class="deck-btn" id="deck-prev" aria-label="Diapositive précédente">&#9664; Préc.</button>'
          '<div class="counter" id="slide-counter"></div>'
          '<button class="deck-btn" id="deck-next" aria-label="Diapositive suivante">Suiv. &#9654;</button></div>\n'
          f'<script>window.CHAPTER_ID={jd(slug)};window.LEVEL={jd(d["level"])};'
          f'window.SECTION={jd("grammar" if d["section"] == "grammaire" else "writing")};</script>\n'
          '<script src="../../../../shared/i18n.js?v=v124"></script>\n'
          '<script src="../../../../shared/store.js?v=v107"></script>\n'
          '<script src="../../../../shared/deck.js?v=v114"></script>\n'
          f'<footer class="site-footer">Word Play &middot; Anglais {d["level"].upper()} &middot; Leçon</footer>\n'
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
                    f'aria-label="Réponse e2q{i}"></div></div>\n')
    form.append(f'</section>\n\n<section class="exercise" id="ex3">\n<div class="ex-head">Exercice 3</div>\n'
                f'<div class="ex-title">{e3t}</div>\n<div class="ex-meta">{len(e3qs)} points</div>\n'
                f'<div class="ex-instruct">{e3i}</div>\n')
    for i, (q, opts, a, _) in enumerate(e3qs, 1):
        form.append(mc_q(i, q, opts, a, f'e3q{i}'))
    form.append('<div class="submit-wrap"><button type="submit" class="submit-btn">Vérifier les réponses</button></div>\n'
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

    sec_label = 'Grammaire' if d['section'] == 'grammaire' else 'Rédaction'
    s = HEAD.format(title=f'{d["short"]} — Exercices {d["level"].upper()} | Word Play',
                    extra_css='<link rel="stylesheet" href="../../../../shared/worksheet.css?v=v106">\n'
                              '<link rel="stylesheet" href="../../../../shared/game.css?v=v112">\n')
    s += '<body>\n' + HEADER + crumb(d, 'Exercices') + nav('worksheet.html')
    s += (f'<h1>{d["title"]}</h1>\n'
          f'<p class="intro-meta">Complète les exercices puis vérifie tes réponses. Total : {total} points.</p>\n'
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
          f'<footer class="site-footer">Word Play &middot; Anglais {d["level"].upper()} &middot; Exercices</footer>\n'
          '</body>\n</html>\n')
    return s


def render_game(d, slug):
    items = ',\n'.join(
        '    {id:%s, term:%s, meaning:%s, synonym:%s, example:%s, completion:%s, answer:%s}'
        % tuple(jd(v) for v in it) for it in d['items'])
    sec_label = 'Grammaire' if d['section'] == 'grammaire' else 'Rédaction'
    s = HEAD.format(title=f'{d["short"]} — Jeu {d["level"].upper()} | Word Play',
                    extra_css='<link rel="stylesheet" href="../../../../shared/game.css?v=v112">\n')
    s += '<body>\n' + HEADER + crumb(d, 'Jeu') + nav('game.html')
    s += (f'<div class="container">\n  <h1>{d["short"]} — Jeu de Maîtrise</h1>\n'
          '  <div class="game-wrap">\n'
          '    <div id="gameStart" class="game-screen active">\n      <div class="game-start">\n'
          '        <h2>Jeu de Maîtrise</h2>\n'
          f'        <p>{d["game_desc"]}</p>\n'
          '        <div class="game-stats-row">\n'
          '          <div class="game-stat"><div class="game-stat-val" id="gStartMastered">0</div><div class="game-stat-label">Maîtrisés</div></div>\n'
          '          <div class="game-stat"><div class="game-stat-val">/ <span id="gStartTotal">0</span></div><div class="game-stat-label">Total</div></div>\n'
          '        </div>\n'
          '        <div id="gResumeSection" style="display:none;background:var(--cream-deep);border-radius:4px;padding:14px;margin-bottom:16px;">\n'
          '          <p style="font-size:0.9rem;margin-bottom:10px;">Tu as une partie sauvegardée.</p>\n'
          '          <div class="game-btn-row">\n'
          '            <button id="gBtnResume" class="game-btn primary">Reprendre</button>\n'
          '            <button id="gBtnNewFromResume" class="game-btn ghost small">Nouvelle partie</button>\n'
          '          </div>\n        </div>\n'
          '        <div class="game-btn-row"><button id="gBtnStart" class="game-btn primary">Commencer</button></div>\n'
          '      </div>\n'
          '      <div class="game-ref-panel" style="margin-top:20px;">\n'
          '        <div class="game-ref-head" id="gRefToggle">&#9660; Tous les éléments — référence</div>\n'
          '        <div class="game-ref-body" id="gRefBody"><div id="gRefList"></div></div>\n'
          '      </div>\n    </div>\n'
          '    <div id="gamePlay" class="game-screen">\n      <div class="game-play"></div>\n    </div>\n'
          '    <div id="gameCompletion" class="game-screen">\n      <div class="game-completion">\n'
          '        <h2>Maîtrisé !</h2>\n        <p>Tu as terminé tous les éléments de ce chapitre.</p>\n'
          '        <div class="game-stats-row" style="margin:20px 0;">\n'
          '          <div class="game-stat"><div class="game-stat-val" id="gFinalScore">0</div><div class="game-stat-label">Score</div></div>\n'
          '          <div class="game-stat"><div class="game-stat-val" id="gFinalStreak">0</div><div class="game-stat-label">Meilleure série</div></div>\n'
          '          <div class="game-stat"><div class="game-stat-val" id="gFinalPct">0%</div><div class="game-stat-label">Maîtrisés</div></div>\n'
          '        </div>\n        <div id="gMasteryMap"></div>\n'
          '        <div class="game-btn-row">\n'
          '          <button id="gBtnPlayAgain" class="game-btn primary">Rejouer</button>\n'
          '          <a href="worksheet.html" class="game-btn secondary">Exercices</a>\n'
          '        </div>\n      </div>\n    </div>\n  </div>\n</div>\n'
          '<div class="game-toast" id="gToast"></div>\n'
          f'<footer class="site-footer">Word Play &middot; Anglais {d["level"].upper()} &middot; Jeu</footer>\n'
          '<script>\n'
          f"window.GAME_DATA = {{\n  chapterId: {jd(slug)},\n  level: {jd(d['level'])},\n"
          f"  title: {jd(d['title'])},\n  storageKey: 'wordplay_game_{d['level']}_{slug}',\n"
          f'  items: [\n{items}\n  ]\n}};\n'
          '</script>\n'
          '<script src="../../../../shared/i18n.js?v=v124"></script>\n'
          '<script src="../../../../shared/store.js?v=v107"></script>\n'
          '<script src="../../../../shared/game.js?v=v111"></script>\n'
          '</body>\n</html>\n')
    return s


def render_hub(d, slug):
    sec = SECTION_FR[d['section']]
    s = HEAD.format(title=f'{d["short"]} — {sec} {d["level"].upper()} | Word Play', extra_css='')
    s = s.replace('href="index.html" class="back', 'href="../index.html" class="back')
    s += '<body>\n' + HEADER.replace('href="index.html" class="back', 'href="../index.html" class="back')
    s += ('<div class="section-page">\n'
          '  <div class="breadcrumb">\n'
          '    <a href="../../../../index.html">Accueil</a><span>&#8250;</span>\n'
          f'    <a href="../../index.html">{d["level"].upper()}</a><span>&#8250;</span>\n'
          f'    <a href="../index.html">{sec}</a><span>&#8250;</span>\n'
          f'    <strong>{d["short"]}</strong>\n  </div>\n'
          f'  <div class="chapter-num">{d["num"]} &middot; {sec}</div>\n'
          f'  <h1 class="chapter-h1">{d["short"]}</h1>\n'
          '  <div class="activity-grid">\n'
          '    <a href="slides.html" class="activity-card" data-activity="lesson">\n'
          '      <span class="ac-title">Leçon</span>\n'
          '      <p class="ac-desc">Explications en français avec exemples en anglais</p>\n'
          '      <span class="ac-arrow">&#8594;</span>\n    </a>\n'
          '    <a href="worksheet.html" class="activity-card" data-activity="practice">\n'
          '      <span class="ac-title">Exercices</span>\n'
          '      <p class="ac-desc">Exercices interactifs avec corrections expliquées</p>\n'
          '      <span class="ac-arrow">&#8594;</span>\n    </a>\n'
          '    <a href="game.html" class="activity-card" data-activity="game">\n'
          '      <span class="ac-title">Jeu de Maîtrise</span>\n'
          '      <p class="ac-desc">Trois manches par concept pour tout mémoriser</p>\n'
          '      <span class="ac-arrow">&#8594;</span>\n    </a>\n'
          '  </div>\n</div>\n'
          f'<footer class="site-footer">Word Play &middot; Anglais {d["level"].upper()}</footer>\n'
          '</body>\n</html>\n')
    return s


def render(slug, d):
    out_dir = os.path.join(ROOT, 'fr', d['level'], d['section'], slug)
    os.makedirs(out_dir, exist_ok=True)
    open(os.path.join(out_dir, 'slides.html'), 'w', encoding='utf-8').write(render_slides(d, slug))
    open(os.path.join(out_dir, 'worksheet.html'), 'w', encoding='utf-8').write(render_worksheet(d, slug))
    open(os.path.join(out_dir, 'game.html'), 'w', encoding='utf-8').write(render_game(d, slug))
    open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8').write(render_hub(d, slug))
    r = subprocess.run(['python3', os.path.join(ROOT, 'scripts/validate_inline_js.py')]
                       + [os.path.join(out_dir, f) for f in
                          ('slides.html', 'worksheet.html', 'game.html', 'index.html')],
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
