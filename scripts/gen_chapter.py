#!/usr/bin/env python3
"""
gen_chapter.py — Word Play chapter scaffold generator
Generates all 5 HTML files for a chapter from a JSON spec.

Usage:
  python3 scripts/gen_chapter.py scripts/chapter_specs/en-a2-grammar-superlatives.json
  python3 scripts/gen_chapter.py scripts/chapter_specs/en-a2-grammar-superlatives.json --dry-run

Spec JSON fields:
  lang:       "en" | "es"
  level:      "a1" | "a2" | "b1" | "b2" | "c1" | "c2"
  section:    "grammar" | "vocabulary" | "writing"
  num:        chapter/topic number (int)
  slug:       folder name, e.g. "superlatives"
  title:      display title, e.g. "Superlatives"
  subtitle:   sub-line, e.g. "the tallest · the most beautiful · the best"
  next_slug:  slug of the next chapter, null if last
  next_num:   number of the next chapter, null if last
  next_title: title of the next chapter, null if last
  game_items: (optional) list of 10 game item dicts for GAME_DATA; omit for placeholder items
"""

import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ─── Shared asset versions ─────────────────────────────────────────────────────
V = dict(base='v123', slides='v115', worksheet='v106', game='v110', print='v102',
         dark_init='v109', deck='v113', store='v105')

# ─── Level → repo path ─────────────────────────────────────────────────────────
LEVEL_PATH = {
    ('en','a1'):'a/a1', ('en','a2'):'a/a2', ('en','b1'):'b/b1',
    ('en','b2'):'b/b2', ('en','c1'):'c/c1', ('en','c2'):'c/c2',
    ('es','a1'):'es/a1',('es','a2'):'es/a2',('es','b1'):'es/b1',
    ('es','b2'):'es/b2',('es','c1'):'es/c1',('es','c2'):'es/c2',
}

# Progress storage level keys
PROG_KEY = {
    ('en','a1'):'a1', ('en','a2'):'a2', ('en','b1'):'b1',
    ('en','b2'):'b2', ('en','c1'):'c1', ('en','c2'):'c2',
    ('es','a1'):'es-a1',('es','a2'):'es-a2',('es','b1'):'es-b1',
    ('es','b2'):'es-b2',('es','c1'):'es-c1',('es','c2'):'es-c2',
}

def sec_folder(lang, section):
    if lang == 'es':
        # gramatica uses Spanish spelling; vocabulary/writing keep English (matches existing site structure)
        return {'grammar':'gramatica'}.get(section, section)
    return section

def sec_label(lang, section):
    en = {'grammar':'Grammar','vocabulary':'Vocabulary','writing':'Writing'}
    es = {'grammar':'Gramática','gramatica':'Gramática',
          'vocabulary':'Vocabulario','vocabulario':'Vocabulario',
          'writing':'Escritura','escritura':'Escritura'}
    return (es if lang=='es' else en).get(section, section.title())

# ─── UI string bundles ─────────────────────────────────────────────────────────
S = {
    'en': dict(
        footer='Word Play · Cambridge English A1&#8594;C2',
        dark='&#9680; Dark', home='Home',
        lesson='Lesson', review='Review', game='Game', printables='Printables',
        lesson_desc='Read the explanation with examples and notes',
        review_desc='Fill-in exercises and sentence building tasks',
        game_desc='Challenge yourself with the mastery game',
        print_desc='Download a printer-ready study sheet',
        start='Start', resume='Resume', start_fresh='Start fresh',
        all_mastered='All mastered!',
        items_stages='10 items · 4 stages each.',
        wrong_answer='A wrong answer drops you back one stage — never to zero.',
        next_ch='Next chapter &rarr;', redo='Redo practice worksheet',
        back_hub='&#8592; Back to hub',
        submit='Submit all', reset='Reset', try_again='Try again',
        reference='Reference &mdash; all words',
        practice_now='Practice now &rarr;',
        recap='Recap', mistakes='Common mistakes',
        mistakes_sub='Things learners often get wrong',
        by_ex='By exercise', ch_complete='Chapter {num} complete',
        score='Score', streak='Streak', wp='Word Play',
        play_game='Play mastery game &rarr;',
        ex_head='Exercise',
        ch_label=lambda num: f'Ch {num}',
    ),
    'es': dict(
        footer='Word Play · Cambridge Inglés A1&#8594;C2',
        dark='&#9680; Oscuro', home='Inicio',
        lesson='Lección', review='Repaso', game='Juego', printables='Imprimibles',
        lesson_desc='Lee la explicación con ejemplos y notas',
        review_desc='Ejercicios de relleno y construcción de frases',
        game_desc='Pon a prueba tu dominio con el juego',
        print_desc='Descarga una hoja de estudio lista para imprimir',
        start='Empezar', resume='Continuar', start_fresh='Empezar de nuevo',
        all_mastered='¡Todo dominado!',
        items_stages='10 elementos · 4 etapas cada uno.',
        wrong_answer='Una respuesta incorrecta te baja un nivel — nunca a cero.',
        next_ch='Siguiente capítulo &rarr;', redo='Repetir los ejercicios',
        back_hub='&#8592; Volver al inicio',
        submit='Enviar todo', reset='Reiniciar', try_again='Intentar de nuevo',
        reference='Referencia &mdash; todas las palabras',
        practice_now='Practicar ahora &rarr;',
        recap='Resumen', mistakes='Errores comunes',
        mistakes_sub='Errores típicos de hispanohablantes',
        by_ex='Por ejercicio', ch_complete='Capítulo {num} completado',
        score='Puntuación', streak='Racha', wp='Word Play',
        play_game='Jugar al juego de maestría &rarr;',
        ex_head='Ejercicio',
        ch_label=lambda num: f'Cap. {num}',
    ),
}

WP_SVG = '<svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px"><rect width="32" height="32" rx="4" fill="currentColor"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>'

# ─── Partials ─────────────────────────────────────────────────────────────────

def _header(lang, back_href):
    s = S[lang]
    return (f'<header class="site-header"><div class="site-header-inner">\n'
            f'  <a href="{back_href}" class="back back-link" aria-label="Back"></a>\n'
            f'  <a href="../../../../index.html" class="brand">{WP_SVG}{s["wp"]}</a>\n'
            f'  <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">{s["dark"]}</button>\n'
            f'</div></header>')

def _breadcrumb(lang, level_label, level_href, section_href, section_name, title, is_leaf=True):
    s = S[lang]
    end = f'<strong>{title}</strong>' if is_leaf else f'<a href="index.html">{title}</a>'
    return (f'<div class="breadcrumb"><a href="../../../../index.html">{s["home"]}</a>'
            f'<span>&#8250;</span><a href="{level_href}">{level_label}</a>'
            f'<span>&#8250;</span><a href="{section_href}">{section_name}</a>'
            f'<span>&#8250;</span>{end}</div>')

def _chapter_nav(lang, active_page):
    s = S[lang]
    tabs = [('slides.html','lesson',s['lesson']),('worksheet.html','review',s['review']),
            ('game.html','game',s['game']),('printables.html','printables',s['printables'])]
    items = '\n'.join(
        f'  <a href="{href}" class="chapter-nav-btn{" active" if page==active_page else ""}">{label}</a>'
        for href, page, label in tabs)
    return f'<nav class="chapter-nav">\n{items}\n</nav>'

def _footer(lang):
    return f'<footer class="site-footer">{S[lang]["footer"]}</footer>'

# ─── File generators ──────────────────────────────────────────────────────────

def gen_index(sp, level_path, level_label, sec_name, sec_folder_name, prog_key, depth='../../../../'):
    s = S[sp['lang']]
    slug = sp['slug']
    num = sp['num']
    ch_label = s['ch_label'](num)
    title = sp['title']
    subtitle = sp['subtitle']
    level_href = f'{depth}{level_path}/index.html'
    section_href = '../index.html'

    # activity grid — vocab chapters don't have printables (use flashcards instead)
    is_vocab = sp['section'] in ('vocabulary', 'vocabulario')
    is_es = sp['lang'] == 'es'

    if is_vocab and is_es:
        activities = f'''  <a href="slides.html" class="activity-card" data-activity="lesson" style="--ac-color:#B8860B">
    <span class="ac-icon">&#128214;</span>
    <span class="ac-title">{s['lesson']}</span>
    <p class="ac-desc">{s['lesson_desc']}</p>
    <span class="ac-arrow">&#8594;</span>
  </a>
  <a href="flashcards.html" class="activity-card" data-activity="practice" style="--ac-color:#B8860B">
    <span class="ac-icon">&#9997;</span>
    <span class="ac-title">Tarjetas &amp; Emparejamiento</span>
    <p class="ac-desc">Estudia las tarjetas y luego empareja palabras con definiciones</p>
    <span class="ac-arrow">&#8594;</span>
  </a>
  <a href="game.html" class="activity-card" data-activity="game" style="--ac-color:#2E7D52">
    <span class="ac-icon">&#9889;</span>
    <span class="ac-title">{s['game']}</span>
    <p class="ac-desc">{s['game_desc']}</p>
    <span class="ac-arrow">&#8594;</span>
  </a>'''
    elif is_vocab:
        activities = f'''  <a href="slides.html" class="activity-card" data-activity="lesson">
    <span class="ac-title">{s['lesson']}</span>
    <p class="ac-desc">Study the vocabulary with explanations and examples</p>
    <span class="ac-arrow">&#8594;</span>
  </a>
  <a href="flashcards.html" class="activity-card" data-activity="practice">
    <span class="ac-title">Flashcards &amp; Match</span>
    <p class="ac-desc">Flip cards, then match words to definitions</p>
    <span class="ac-arrow">&#8594;</span>
  </a>
  <a href="game.html" class="activity-card" data-activity="game">
    <span class="ac-title">Mastery Game</span>
    <p class="ac-desc">4-stage game to lock words into long-term memory</p>
    <span class="ac-arrow">&#8594;</span>
  </a>'''
    else:
        activities = f'''  <a href="slides.html" class="activity-card" data-activity="lesson" style="--ac-color:#B8860B">
    <span class="ac-icon">&#128214;</span>
    <span class="ac-title">{s['lesson']}</span>
    <p class="ac-desc">{s['lesson_desc']}</p>
    <span class="ac-arrow">&#8594;</span>
  </a>
  <a href="worksheet.html" class="activity-card" data-activity="practice" style="--ac-color:#B8860B">
    <span class="ac-icon">&#9997;</span>
    <span class="ac-title">{s['review']}</span>
    <p class="ac-desc">{s['review_desc']}</p>
    <span class="ac-arrow">&#8594;</span>
  </a>
  <a href="game.html" class="activity-card" data-activity="game" style="--ac-color:#2E7D52">
    <span class="ac-icon">&#9889;</span>
    <span class="ac-title">{s['game']}</span>
    <p class="ac-desc">{s['game_desc']}</p>
    <span class="ac-arrow">&#8594;</span>
  </a>
  <a href="printables.html" class="activity-card" data-activity="print" style="--ac-color:#6B6B6B">
    <span class="ac-icon">&#128444;</span>
    <span class="ac-title">{s['printables']}</span>
    <p class="ac-desc">{s['print_desc']}</p>
    <span class="ac-arrow">&#8594;</span>
  </a>'''

    # Progress script — vocab vs grammar
    if is_vocab and is_es:
        prog_script = f'''(function(){{
  try {{
    var prog=JSON.parse(localStorage.getItem('wordplay_progress')||'{{}}');
    var lvl=prog['{prog_key}']||{{}};
    var defs=[
      ['slides.html', lvl['slides_{slug}']&&lvl['slides_{slug}'].done],
      ['flashcards.html', !!localStorage.getItem('wordplay_vocab_{prog_key}_{slug}_mastered')],
      ['game.html', lvl['wordplay_game_{prog_key}_{slug}']&&lvl['wordplay_game_{prog_key}_{slug}'].pct>=70]
    ];
    defs.forEach(function(d){{
      if(!d[1]) return;
      var card=document.querySelector('.activity-card[href="'+d[0]+'"]');
      if(card) card.setAttribute('data-done','1');
    }});
  }}catch(e){{}}
}})();'''
    elif is_vocab:
        prog_script = f'''(function(){{
  try {{
    var prog=JSON.parse(localStorage.getItem('wordplay_progress')||'{{}}');
    var lvl=prog['{prog_key}']||{{}};
    var defs=[
      ['slides.html', lvl['slides_{slug}']&&lvl['slides_{slug}'].done],
      ['flashcards.html', !!localStorage.getItem('wordplay_vocab_{prog_key}_{slug}_mastered')],
      ['game.html', lvl['wordplay_game_{prog_key}_{slug}']&&lvl['wordplay_game_{prog_key}_{slug}'].pct>=70]
    ];
    defs.forEach(function(d){{
      if(!d[1]) return;
      var card=document.querySelector('.activity-card[href="'+d[0]+'"]');
      if(card) card.setAttribute('data-done','1');
    }});
  }}catch(e){{}}
}})();'''
    else:
        prog_script = f'''(function(){{
  try {{
    var prog=JSON.parse(localStorage.getItem('wordplay_progress')||'{{}}');
    var lvl=prog['{prog_key}']||{{}};
    var defs=[
      ['slides.html', lvl['slides_{slug}']&&lvl['slides_{slug}'].done],
      ['worksheet.html', lvl['{slug}']&&lvl['{slug}'].pct>=70],
      ['game.html', lvl['wordplay_game_{slug}']&&lvl['wordplay_game_{slug}'].pct>=70],
      ['printables.html', false]
    ];
    defs.forEach(function(d){{
      if(!d[1]) return;
      var card=document.querySelector('.activity-card[href="'+d[0]+'"]');
      if(card) card.setAttribute('data-done','1');
    }});
  }}catch(e){{}}
}})();'''

    page_title = f'{title} — {sp["level"].upper()} {sec_label(sp["lang"], sp["section"])} | Word Play'

    return f'''<!DOCTYPE html>
<html lang="{sp['lang']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{depth}favicon.svg" type="image/svg+xml">
<title>{page_title}</title>
<link rel="stylesheet" href="{depth}shared/base.css?v={V['base']}">
<script src="{depth}shared/dark-init.js?v={V['dark_init']}"></script>
</head>
<body>
{_header(sp['lang'], '../index.html')}
<div class="section-page">
  {_breadcrumb(sp['lang'], sp['level'].upper(), level_href, section_href, sec_name, title)}
  <div class="chapter-num">{ch_label}</div>
  <h1 class="chapter-h1">{title}</h1>
  <p class="chapter-subtitle">{subtitle}</p>
  <div class="activity-grid">
{activities}
  </div>
</div>
{_footer(sp['lang'])}
<script src="{depth}shared/store.js?v={V['store']}"></script>
<script>
{prog_script}
</script>
</body>
</html>
'''


def gen_slides(sp, level_path, level_label, sec_name, prog_key, depth='../../../../'):
    s = S[sp['lang']]
    slug = sp['slug']
    num = sp['num']
    ch_label = s['ch_label'](num)
    title = sp['title']
    subtitle = sp['subtitle']
    lang = sp['lang']
    level_href = f'{depth}{level_path}/index.html'
    section_href = '../index.html'
    level_upper = sp['level'].upper()

    page_title = f'{level_upper} · {title} — {s["lesson"]} | Word Play'

    # 7 placeholder slides
    slides_html = f'''
<!-- ── Slide 1: Introduction ─────────────────────────────── -->
<div class="slide"><div class="slide-card">
  <div class="slide-header"><h2><!-- SLIDE 1 TITLE --></h2></div>
  <p class="slide-explanation"><!-- SLIDE 1 EXPLANATION --></p>
  <!-- ADD: overview-row, example-card, watch-out blocks as needed -->
</div></div>

<!-- ── Slide 2: Core concept ─────────────────────────────── -->
<div class="slide"><div class="slide-card">
  <div class="slide-header"><h2><!-- SLIDE 2 TITLE --></h2><p class="slide-sub"><!-- sub-heading --></p></div>
  <!-- ADD: overview-row table / formula-block / panel-pair -->
</div></div>

<!-- ── Slide 3: Forms / Structure ───────────────────────── -->
<div class="slide"><div class="slide-card">
  <div class="slide-header"><h2><!-- SLIDE 3 TITLE --></h2><p class="slide-sub"><!-- sub-heading --></p></div>
  <!-- ADD: examples-row / panel-pair correct vs wrong -->
</div></div>

<!-- ── Slide 4: Usage / Context ─────────────────────────── -->
<div class="slide"><div class="slide-card">
  <div class="slide-header"><h2><!-- SLIDE 4 TITLE --></h2><p class="slide-sub"><!-- sub-heading --></p></div>
  <!-- ADD: overview-row pairs showing when / why to use -->
</div></div>

<!-- ── Slide 5: Contrastive / Exceptions ────────────────── -->
<div class="slide"><div class="slide-card">
  <div class="slide-header"><h2><!-- SLIDE 5 TITLE --></h2><p class="slide-sub"><!-- sub-heading --></p></div>
  <!-- ADD: bi-block (ES) or watch-out + panel-pair (EN) -->
</div></div>

<!-- ── Slide 6: Common mistakes ─────────────────────────── -->
<div class="slide"><div class="slide-card">
  <div class="slide-header"><h2>{s['mistakes']}</h2><p class="slide-sub">{s['mistakes_sub']}</p></div>
  <!-- ADD: trap-row elements  -->
  <!-- Example:
  <div class="trap-row">
    <div class="trap-wrong">Wrong sentence.</div>
    <div class="trap-arrow">→</div>
    <div class="trap-right">Correct sentence.</div>
    <div class="trap-note">Explanation.</div>
  </div>
  -->
</div></div>

<!-- ── Slide 7: Recap ───────────────────────────────────── -->
<div class="slide summary-slide"><div class="slide-card">
  <h2>{s['recap']}</h2>
  <!-- ADD: summary-row elements -->
  <!-- Example:
  <div class="summary-row"><div class="label">Label</div><div class="form">Form</div><div class="ex">Example</div></div>
  -->
  <div style="margin-top:28px;text-align:center">
    <a href="worksheet.html" style="display:inline-block;padding:13px 32px;background:var(--amber);color:#1A1A1A;font-family:var(--font-sans);font-size:.8rem;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;border-radius:5px">{s['practice_now']}</a>
  </div>
</div></div>'''

    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="description" content="Word Play — Cambridge English grammar, vocabulary and writing practice.">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{depth}favicon.svg" type="image/svg+xml">
<title>{page_title}</title>
<link rel="stylesheet" href="{depth}shared/base.css?v={V['base']}">
<link rel="stylesheet" href="{depth}shared/slides.css?v={V['slides']}">
<script src="{depth}shared/dark-init.js?v={V['dark_init']}"></script>
</head>
<body class="deck-body">
<div class="deck-progress"><div class="deck-progress-fill" id="deck-progress-fill"></div></div>
<header class="site-header">
  <div class="site-header-inner"><a href="index.html" class="back back-link" aria-label="Back"></a>
    <a href="{depth}index.html" class="brand">{WP_SVG}{s['wp']}</a>
    <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">{s['dark']}</button>
  </div>
</header>
{_breadcrumb(lang, sp['level'].upper(), level_href, section_href, sec_name, title, is_leaf=False)}
{_chapter_nav(lang, 'lesson')}
<div class="chapter-num">{ch_label}</div>
<h1>{title}</h1>
<p class="chapter-subtitle">{subtitle}</p>

<div class="slide-deck" id="slide-deck">
{slides_html}
</div><!-- .slide-deck -->

<div class="deck-nav">
  <button class="deck-btn" id="deck-prev" aria-label="Previous slide">&#9664; Prev</button>
  <div class="counter" id="slide-counter"></div>
  <button class="deck-btn" id="deck-next" aria-label="Next slide">Next &#9654;</button>
</div>

<script>window.CHAPTER_ID="{slug}";window.LEVEL="{sp['level']}";window.SECTION="{sp['section']}";</script>
<script src="{depth}shared/store.js?v={V['store']}"></script>
<script src="{depth}shared/deck.js?v={V['deck']}"></script>
{_footer(lang)}
<script>
try {{
  localStorage.setItem('wordplay_last_chapter_{sp['level']}', JSON.stringify({{
    slug: '{slug}', section: '{sp['section']}', title: '{title}', page: 'slides.html'
  }}));
}} catch(e) {{}}
</script>
</body>
</html>
'''


def gen_worksheet(sp, level_path, level_label, sec_name, prog_key, depth='../../../../'):
    s = S[sp['lang']]
    slug = sp['slug']
    num = sp['num']
    ch_label = s['ch_label'](num)
    title = sp['title']
    subtitle = sp['subtitle']
    lang = sp['lang']
    level_href = f'{depth}{level_path}/index.html'
    section_href = '../index.html'
    level_upper = sp['level'].upper()

    page_title = f'{level_upper} · {title} — {s["review"]} | Word Play'

    # 3 placeholder exercises with proper data-q keys
    exercises_html = f'''<!-- ── Ex 1: Multiple choice ─────────────────────────────── -->
<section class="exercise" id="ex1">
  <div class="ex-head">{s['ex_head']} 1</div>
  <div class="ex-title"><!-- Exercise 1 title --></div>
  <div class="ex-meta">5 points</div>
  <div class="ex-instruct"><!-- Instructions --></div>
  <div class="q"><span class="q-num">1</span>
    <div class="q-text"><!-- Question 1 --></div>
    <div class="choice-group" data-q="mc1" data-answer="<!-- ANSWER -->"><button type="button" class="choice-btn" data-value="<!-- opt1 -->"><!-- opt1 --></button><button type="button" class="choice-btn" data-value="<!-- opt2 -->"><!-- opt2 --></button><button type="button" class="choice-btn" data-value="<!-- opt3 -->"><!-- opt3 --></button></div>
  </div>
  <div class="q"><span class="q-num">2</span>
    <div class="q-text"><!-- Question 2 --></div>
    <div class="choice-group" data-q="mc2" data-answer="<!-- ANSWER -->"><button type="button" class="choice-btn" data-value="<!-- opt1 -->"><!-- opt1 --></button><button type="button" class="choice-btn" data-value="<!-- opt2 -->"><!-- opt2 --></button><button type="button" class="choice-btn" data-value="<!-- opt3 -->"><!-- opt3 --></button></div>
  </div>
  <div class="q"><span class="q-num">3</span>
    <div class="q-text"><!-- Question 3 --></div>
    <div class="choice-group" data-q="mc3" data-answer="<!-- ANSWER -->"><button type="button" class="choice-btn" data-value="<!-- opt1 -->"><!-- opt1 --></button><button type="button" class="choice-btn" data-value="<!-- opt2 -->"><!-- opt2 --></button><button type="button" class="choice-btn" data-value="<!-- opt3 -->"><!-- opt3 --></button></div>
  </div>
  <div class="q"><span class="q-num">4</span>
    <div class="q-text"><!-- Question 4 --></div>
    <div class="choice-group" data-q="mc4" data-answer="<!-- ANSWER -->"><button type="button" class="choice-btn" data-value="<!-- opt1 -->"><!-- opt1 --></button><button type="button" class="choice-btn" data-value="<!-- opt2 -->"><!-- opt2 --></button><button type="button" class="choice-btn" data-value="<!-- opt3 -->"><!-- opt3 --></button></div>
  </div>
  <div class="q"><span class="q-num">5</span>
    <div class="q-text"><!-- Question 5 --></div>
    <div class="choice-group" data-q="mc5" data-answer="<!-- ANSWER -->"><button type="button" class="choice-btn" data-value="<!-- opt1 -->"><!-- opt1 --></button><button type="button" class="choice-btn" data-value="<!-- opt2 -->"><!-- opt2 --></button><button type="button" class="choice-btn" data-value="<!-- opt3 -->"><!-- opt3 --></button></div>
  </div>
</section>

<!-- ── Ex 2: Fill-in ──────────────────────────────────────── -->
<section class="exercise" id="ex2">
  <div class="ex-head">{s['ex_head']} 2</div>
  <div class="ex-title"><!-- Exercise 2 title --></div>
  <div class="ex-meta">5 points</div>
  <div class="ex-instruct"><!-- Instructions --></div>
  <div class="q"><span class="q-num">1</span>
    <div class="q-text"><!-- Sentence with gap --></div>
    <input type="text" data-q="fi1" maxlength="30" autocomplete="off" spellcheck="false" placeholder="…" style="width:180px;padding:7px 11px;font-family:var(--font-sans);font-size:.9rem;border:1.5px solid var(--hairline);border-radius:4px;background:var(--paper);color:var(--ink);margin-top:6px;display:block">
  </div>
  <div class="q"><span class="q-num">2</span>
    <div class="q-text"><!-- Sentence with gap --></div>
    <input type="text" data-q="fi2" maxlength="30" autocomplete="off" spellcheck="false" placeholder="…" style="width:180px;padding:7px 11px;font-family:var(--font-sans);font-size:.9rem;border:1.5px solid var(--hairline);border-radius:4px;background:var(--paper);color:var(--ink);margin-top:6px;display:block">
  </div>
  <div class="q"><span class="q-num">3</span>
    <div class="q-text"><!-- Sentence with gap --></div>
    <input type="text" data-q="fi3" maxlength="30" autocomplete="off" spellcheck="false" placeholder="…" style="width:180px;padding:7px 11px;font-family:var(--font-sans);font-size:.9rem;border:1.5px solid var(--hairline);border-radius:4px;background:var(--paper);color:var(--ink);margin-top:6px;display:block">
  </div>
  <div class="q"><span class="q-num">4</span>
    <div class="q-text"><!-- Sentence with gap --></div>
    <input type="text" data-q="fi4" maxlength="30" autocomplete="off" spellcheck="false" placeholder="…" style="width:180px;padding:7px 11px;font-family:var(--font-sans);font-size:.9rem;border:1.5px solid var(--hairline);border-radius:4px;background:var(--paper);color:var(--ink);margin-top:6px;display:block">
  </div>
  <div class="q"><span class="q-num">5</span>
    <div class="q-text"><!-- Sentence with gap --></div>
    <input type="text" data-q="fi5" maxlength="30" autocomplete="off" spellcheck="false" placeholder="…" style="width:180px;padding:7px 11px;font-family:var(--font-sans);font-size:.9rem;border:1.5px solid var(--hairline);border-radius:4px;background:var(--paper);color:var(--ink);margin-top:6px;display:block">
  </div>
</section>

<!-- ── Ex 3: In context ───────────────────────────────────── -->
<section class="exercise" id="ex3">
  <div class="ex-head">{s['ex_head']} 3</div>
  <div class="ex-title"><!-- Exercise 3 title --></div>
  <div class="ex-meta">4 points</div>
  <div class="ex-instruct"><!-- Instructions --></div>
  <div class="reading-context"><!-- Context passage --></div>
  <div class="q"><span class="q-num">1</span>
    <div class="q-text"><!-- Q1 --></div>
    <input type="text" data-q="ctx1" maxlength="20" autocomplete="off" spellcheck="false" placeholder="…" style="width:140px;padding:7px 11px;font-family:var(--font-sans);font-size:.9rem;border:1.5px solid var(--hairline);border-radius:4px;background:var(--paper);color:var(--ink);margin-top:6px;display:block">
  </div>
  <div class="q"><span class="q-num">2</span>
    <div class="q-text"><!-- Q2 --></div>
    <input type="text" data-q="ctx2" maxlength="20" autocomplete="off" spellcheck="false" placeholder="…" style="width:140px;padding:7px 11px;font-family:var(--font-sans);font-size:.9rem;border:1.5px solid var(--hairline);border-radius:4px;background:var(--paper);color:var(--ink);margin-top:6px;display:block">
  </div>
  <div class="q"><span class="q-num">3</span>
    <div class="q-text"><!-- Q3 --></div>
    <input type="text" data-q="ctx3" maxlength="20" autocomplete="off" spellcheck="false" placeholder="…" style="width:140px;padding:7px 11px;font-family:var(--font-sans);font-size:.9rem;border:1.5px solid var(--hairline);border-radius:4px;background:var(--paper);color:var(--ink);margin-top:6px;display:block">
  </div>
  <div class="q"><span class="q-num">4</span>
    <div class="q-text"><!-- Q4 --></div>
    <input type="text" data-q="ctx4" maxlength="20" autocomplete="off" spellcheck="false" placeholder="…" style="width:140px;padding:7px 11px;font-family:var(--font-sans);font-size:.9rem;border:1.5px solid var(--hairline);border-radius:4px;background:var(--paper);color:var(--ink);margin-top:6px;display:block">
  </div>
</section>'''

    answers_placeholder = '''{
  mc1:{answer:"<!-- ANSWER -->"},
  mc2:{answer:"<!-- ANSWER -->"},
  mc3:{answer:"<!-- ANSWER -->"},
  mc4:{answer:"<!-- ANSWER -->"},
  mc5:{answer:"<!-- ANSWER -->"},
  fi1:{answer:"<!-- ANSWER -->"},
  fi2:{answer:"<!-- ANSWER -->"},
  fi3:{answer:"<!-- ANSWER -->"},
  fi4:{answer:"<!-- ANSWER -->"},
  fi5:{answer:"<!-- ANSWER -->"},
  ctx1:{answer:"<!-- ANSWER -->"},
  ctx2:{answer:"<!-- ANSWER -->"},
  ctx3:{answer:"<!-- ANSWER -->"},
  ctx4:{answer:"<!-- ANSWER -->"}
}'''

    explanations_placeholder = '''{
  "mc1":"<!-- EXPLANATION 1 -->",
  "mc2":"<!-- EXPLANATION 2 -->",
  "mc3":"<!-- EXPLANATION 3 -->",
  "mc4":"<!-- EXPLANATION 4 -->",
  "mc5":"<!-- EXPLANATION 5 -->",
  "fi1":"<!-- EXPLANATION fi1 -->",
  "fi2":"<!-- EXPLANATION fi2 -->",
  "fi3":"<!-- EXPLANATION fi3 -->",
  "fi4":"<!-- EXPLANATION fi4 -->",
  "fi5":"<!-- EXPLANATION fi5 -->",
  "ctx1":"<!-- EXPLANATION ctx1 -->",
  "ctx2":"<!-- EXPLANATION ctx2 -->",
  "ctx3":"<!-- EXPLANATION ctx3 -->",
  "ctx4":"<!-- EXPLANATION ctx4 -->"
}'''

    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="description" content="Word Play — Cambridge English grammar, vocabulary and writing practice.">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{depth}favicon.svg" type="image/svg+xml">
<title>{page_title}</title>
<link rel="stylesheet" href="{depth}shared/base.css?v={V['base']}">
<link rel="stylesheet" href="{depth}shared/worksheet.css?v={V['worksheet']}">
<script src="{depth}shared/dark-init.js?v={V['dark_init']}"></script>
<style>
.reading-context {{
  background: var(--cream-deep);
  border-left: 4px solid var(--amber);
  padding: 14px 16px;
  font-size: .92rem;
  line-height: 1.7;
  margin-bottom: 16px;
  border-radius: 0 4px 4px 0;
  color: var(--ink);
}}
</style>
</head>
<body>
<header class="site-header">
  <div class="site-header-inner"><a href="index.html" class="back back-link" aria-label="Back"></a>
    <a href="{depth}index.html" class="brand">{WP_SVG}{s['wp']}</a>
    <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">{s['dark']}</button>
  </div>
</header>
{_breadcrumb(lang, sp['level'].upper(), level_href, section_href, sec_name, title, is_leaf=False)}
{_chapter_nav(lang, 'review')}
<div class="container">
  <div class="chapter-num">{ch_label}</div>
  <h1>{title}</h1>
  <p class="chapter-subtitle">{subtitle}</p>

<form id="worksheet">

{exercises_html}

  <div class="submit-wrap">
    <button type="submit" class="submit-btn">{s['submit']}</button>
    <button type="button" onclick="resetAll()" style="padding:12px 20px;background:transparent;color:var(--ink);font-family:var(--font-sans);font-size:.8rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;border:1.5px solid var(--hairline);border-radius:4px;cursor:pointer">{s['reset']}</button>
  </div>

</form>

</div><!-- .container -->

<div id="results" style="max-width:800px;margin:24px auto 0;padding:0 20px;display:none">
  <div style="background:var(--cream-deep);border:1px solid var(--hairline);border-radius:8px;padding:20px 24px">
    <div style="display:flex;align-items:center;gap:20px;margin-bottom:16px">
      <div style="font-family:var(--font-sans)">
        <span style="font-size:2rem;font-weight:800;color:var(--ink)" id="score-got">0</span>
        <span style="font-size:1rem;color:var(--muted)"> / </span>
        <span style="font-size:1rem;color:var(--muted)" id="score-total">0</span>
      </div>
      <div style="flex:1">
        <div style="font-family:var(--font-sans);font-size:1.1rem;font-weight:700;color:var(--ink)" id="score-pct">0%</div>
        <div style="font-family:var(--font-sans);font-size:.7rem;color:var(--muted);text-transform:uppercase;letter-spacing:1px">{s['score']}</div>
        <div id="pass-msg" class="pass-msg"></div>
      </div>
      <button onclick="tryAgain()" style="font-family:var(--font-sans);font-size:.7rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:8px 14px;border-radius:4px;border:1.5px solid var(--hairline);background:transparent;color:var(--ink);cursor:pointer">{s['try_again']}</button>
    </div>
    <div style="margin-top:14px;padding-top:14px;border-top:1px solid var(--hairline)">
      <div style="font-family:var(--font-sans);font-size:.65rem;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:var(--muted);margin-bottom:8px">{s['by_ex']}</div>
      <div id="exercise-breakdown"></div>
    </div>
    <div id="breakdown"></div>
    <div style="margin-top:16px;text-align:center">
      <a href="game.html" style="display:inline-block;padding:10px 24px;background:var(--ink);color:var(--paper);font-family:var(--font-sans);font-size:.72rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;border-radius:4px">{s['play_game']}</a>
    </div>
  </div>
</div>

{_footer(lang)}

<script>
window.CHAPTER_ID = "{slug}";
window.LEVEL = "{sp['level']}";
window.SECTION = "{sp['section']}";
window.TOTAL_POINTS = 14;
window.ANSWERS = {answers_placeholder};
window.EXERCISE_TITLES = {{
  ex1:"{s['ex_head']} 1",
  ex2:"{s['ex_head']} 2",
  ex3:"{s['ex_head']} 3"
}};
</script>
<script>
window.EXPLANATIONS = {explanations_placeholder};
</script>
<script src="{depth}shared/store.js?v={V['store']}"></script>
<script src="{depth}shared/worksheet.js?v={V['worksheet']}"></script>
</body>
</html>
'''


def gen_game(sp, level_path, level_label, sec_name, prog_key, depth='../../../../'):
    s = S[sp['lang']]
    slug = sp['slug']
    num = sp['num']
    title = sp['title']
    lang = sp['lang']
    level_href = f'{depth}{level_path}/index.html'
    section_href = '../index.html'
    level_upper = sp['level'].upper()
    page_title = f'{level_upper} · {title} — {s["game"]} | Word Play'
    level_path_full = LEVEL_PATH[(lang, sp['level'])]

    # Next chapter link
    next_slug = sp.get('next_slug')
    next_title = sp.get('next_title', '')
    next_num = sp.get('next_num', '')
    if next_slug:
        next_btn = f'<a href="../{next_slug}/slides.html" class="game-btn primary" style="text-decoration:none;text-align:center">{s["next_ch"]} {s["ch_label"](next_num)} {next_title}</a>'
    else:
        next_btn = f'<a href="{depth}{level_path_full}/index.html" class="game-btn primary" style="text-decoration:none;text-align:center">{s["back_hub"]}</a>'

    # Game items — use spec items if provided, else 10 placeholders
    game_items = sp.get('game_items', None)
    if game_items:
        items_json = json.dumps(game_items, ensure_ascii=False, indent=2)
    else:
        items_json = '''[
  {"id":"item1","term":"<!-- TERM 1 -->","meaning":"<!-- MEANING 1 -->","synonym":"<!-- hint -->","example":"<!-- Example with <b>term</b> -->","completion":"<!-- Example with _____ -->","answer":"<!-- answer -->"},
  {"id":"item2","term":"<!-- TERM 2 -->","meaning":"<!-- MEANING 2 -->","synonym":"<!-- hint -->","example":"<!-- Example with <b>term</b> -->","completion":"<!-- Example with _____ -->","answer":"<!-- answer -->"},
  {"id":"item3","term":"<!-- TERM 3 -->","meaning":"<!-- MEANING 3 -->","synonym":"<!-- hint -->","example":"<!-- Example with <b>term</b> -->","completion":"<!-- Example with _____ -->","answer":"<!-- answer -->"},
  {"id":"item4","term":"<!-- TERM 4 -->","meaning":"<!-- MEANING 4 -->","synonym":"<!-- hint -->","example":"<!-- Example with <b>term</b> -->","completion":"<!-- Example with _____ -->","answer":"<!-- answer -->"},
  {"id":"item5","term":"<!-- TERM 5 -->","meaning":"<!-- MEANING 5 -->","synonym":"<!-- hint -->","example":"<!-- Example with <b>term</b> -->","completion":"<!-- Example with _____ -->","answer":"<!-- answer -->"},
  {"id":"item6","term":"<!-- TERM 6 -->","meaning":"<!-- MEANING 6 -->","synonym":"<!-- hint -->","example":"<!-- Example with <b>term</b> -->","completion":"<!-- Example with _____ -->","answer":"<!-- answer -->"},
  {"id":"item7","term":"<!-- TERM 7 -->","meaning":"<!-- MEANING 7 -->","synonym":"<!-- hint -->","example":"<!-- Example with <b>term</b> -->","completion":"<!-- Example with _____ -->","answer":"<!-- answer -->"},
  {"id":"item8","term":"<!-- TERM 8 -->","meaning":"<!-- MEANING 8 -->","synonym":"<!-- hint -->","example":"<!-- Example with <b>term</b> -->","completion":"<!-- Example with _____ -->","answer":"<!-- answer -->"},
  {"id":"item9","term":"<!-- TERM 9 -->","meaning":"<!-- MEANING 9 -->","synonym":"<!-- hint -->","example":"<!-- Example with <b>term</b> -->","completion":"<!-- Example with _____ -->","answer":"<!-- answer -->"},
  {"id":"item10","term":"<!-- TERM 10 -->","meaning":"<!-- MEANING 10 -->","synonym":"<!-- hint -->","example":"<!-- Example with <b>term</b> -->","completion":"<!-- Example with _____ -->","answer":"<!-- answer -->"}
]'''

    ch_complete_label = s['ch_complete'].format(num=num)
    storage_key = f'wordplay_game_{prog_key}_{slug}' if lang == 'es' else f'wordplay_game_{slug}'

    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="description" content="Word Play — Cambridge English grammar, vocabulary and writing practice.">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{depth}favicon.svg" type="image/svg+xml">
<title>{page_title}</title>
<link rel="stylesheet" href="{depth}shared/base.css?v={V['base']}">
<link rel="stylesheet" href="{depth}shared/game.css?v={V['game']}">
<script src="{depth}shared/dark-init.js?v={V['dark_init']}"></script>
</head>
<body>
<header class="site-header">
  <div class="site-header-inner"><a href="index.html" class="back back-link" aria-label="Back"></a>
    <a href="{depth}index.html" class="brand">{WP_SVG}{s['wp']}</a>
    <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">{s['dark']}</button>
  </div>
</header>
{_breadcrumb(lang, sp['level'].upper(), level_href, section_href, sec_name, title, is_leaf=False)}
{_chapter_nav(lang, 'game')}
<div class="game-wrap" id="gameWrap">
  <div id="gameStart" class="game-screen active">
    <div class="game-start">
      <h2>{title} — Mastery</h2>
      <p>{s['items_stages']}</p>
      <p style="font-size:.85rem;color:var(--muted)">{s['wrong_answer']}</p>
      <div id="gStartMastered" style="font-family:var(--font-sans);font-size:.9rem;margin:12px 0;color:var(--muted)"></div>
      <div id="gResumeSection" style="display:none;margin-bottom:12px">
        <button id="gBtnResume" class="game-btn primary">{s['resume']}</button>
        <button id="gBtnNewFromResume" class="game-btn">{s['start_fresh']}</button>
      </div>
      <button id="gBtnStart" class="game-btn primary">{s['start']}</button>
      <a href="{depth}{level_path_full}/index.html" class="game-btn" style="text-align:center;text-decoration:none;margin-top:8px">{s['back_hub']}</a>
    </div>
  </div>
  <div id="gamePlay" class="game-screen"><div class="game-play"></div>
  <div class="game-ref-panel" id="gRefPanel">
    <button id="gRefToggle" class="game-ref-head">&#9660; {s['reference']}</button>
    <div id="gRefBody" class="game-ref-body"><div id="gRefList"></div></div>
  </div></div>
  <div id="gameCompletion" class="game-screen">
    <div class="game-complete">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2.5px;text-transform:uppercase;color:var(--amber);margin-bottom:8px">{ch_complete_label}</div>
      <h2 style="margin-bottom:6px">{s['all_mastered']}</h2>
      <p style="color:var(--muted);font-size:.85rem;margin-bottom:20px">{s['score']}: <strong id="gFinalScore"></strong> &nbsp;&middot;&nbsp; {s['streak']}: <strong id="gFinalStreak"></strong></p>
      <div id="gFinalPct" style="font-family:var(--font-serif);font-size:1.4rem;font-weight:700;color:var(--accent);text-align:center;margin:8px 0"></div>
      <div id="gMasteryMap" style="margin:16px 0;text-align:left;"></div>
      {next_btn}
      <a href="worksheet.html" class="game-btn" style="text-decoration:none;text-align:center">{s['redo']}</a>
      <a href="{depth}{level_path_full}/index.html" class="game-btn" style="text-decoration:none;text-align:center;opacity:.7">{s['back_hub']}</a>
    </div>
  </div>
</div>
{_footer(lang)}
<script>
window.GAME_DATA={{chapterId:"{slug}",level:"{sp['level']}",title:"{title}",storageKey:"{storage_key}",items:{items_json}}};
</script>
<script src="{depth}shared/store.js?v={V['store']}"></script>
<script src="{depth}shared/game.js?v={V['game']}"></script>
</body>
</html>
'''


def gen_printables(sp, level_path, level_label, sec_name, prog_key, depth='../../../../'):
    s = S[sp['lang']]
    slug = sp['slug']
    title = sp['title']
    lang = sp['lang']
    level_upper = sp['level'].upper()
    page_title = f'{level_upper} · {title} — {s["printables"]} | Word Play'

    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{depth}favicon.svg" type="image/svg+xml">
<title>{page_title}</title>
<link rel="stylesheet" href="{depth}shared/base.css?v={V['base']}">
<link rel="stylesheet" href="{depth}shared/print.css?v={V['print']}">
<script src="{depth}shared/dark-init.js?v={V['dark_init']}"></script>
</head>
<body>
{_header(lang, 'index.html')}
{_chapter_nav(lang, 'printables')}
<div class="ph-hub">
  <h1 class="ph-hub-title">{title}</h1>
  <div class="ph-hub-grid">
    <div class="ph-hub-card">
      <div class="ph-hub-card-label">LESSON</div>
      <div class="ph-hub-card-title">Reference Card</div>
      <div class="ph-hub-card-desc">Grammar rules and examples for self-study</div>
      <div class="ph-hub-btn-row">
        <a href="#ph-lesson" class="ph-hub-btn ph-hub-btn-view">View</a>
        <button onclick="wpPrint('lesson')" class="ph-hub-btn ph-hub-btn-print">Print</button>
      </div>
    </div>
    <div class="ph-hub-card">
      <div class="ph-hub-card-label">REVIEW</div>
      <div class="ph-hub-card-title">Exercises</div>
      <div class="ph-hub-card-desc">Fill-in and gap-fill practice tasks</div>
      <div class="ph-hub-btn-row">
        <a href="#ph-worksheet" class="ph-hub-btn ph-hub-btn-view">View</a>
        <button onclick="wpPrint('worksheet')" class="ph-hub-btn ph-hub-btn-print">Print</button>
      </div>
    </div>
    <div class="ph-hub-card">
      <div class="ph-hub-card-label">ANSWER KEY</div>
      <div class="ph-hub-card-title">For marking</div>
      <div class="ph-hub-card-desc">Correct answers for all exercises</div>
      <div class="ph-hub-btn-row">
        <a href="#ph-key" class="ph-hub-btn ph-hub-btn-view">View</a>
        <button onclick="wpPrint('key')" class="ph-hub-btn ph-hub-btn-print">Print</button>
      </div>
    </div>
  </div>
  <div class="ph-hub-actions">
    <button onclick="wpPrint('all')" class="ph-hub-btn ph-hub-btn-print">Print all</button>
  </div>
</div>

<div id="ph-lesson" class="ph-section">
  <h1>{title}</h1>
  <h2><!-- LESSON REFERENCE CONTENT --></h2>
  <!-- Add reference tables, rules, examples here -->
</div>

<div id="ph-worksheet" class="ph-section">
  <h1>{title} — Exercises</h1>
  <!-- Add print-friendly exercises here -->
</div>

<div id="ph-key" class="ph-section">
  <h1>{title} — Answer Key</h1>
  <!-- Add answer key here -->
</div>

{_footer(lang)}
<script src="{depth}shared/print.js?v={V['print']}"></script>
</body>
</html>
'''


# ─── Main ─────────────────────────────────────────────────────────────────────

def build(sp, dry_run=False):
    lang = sp['lang']
    level = sp['level']
    section = sp['section']
    slug = sp['slug']

    lp = LEVEL_PATH[(lang, level)]
    prog_key = PROG_KEY[(lang, level)]
    sf = sec_folder(lang, section)
    sl = sec_label(lang, section)
    level_label = level.upper()
    out_dir = os.path.join(ROOT, lp, sf, slug)

    print(f'Target: {os.path.relpath(out_dir, ROOT)}/')
    if dry_run:
        for f in ['index.html','slides.html','worksheet.html','game.html','printables.html']:
            is_vocab = section in ('vocabulary','vocabulario')
            if is_vocab:
                files = ['index.html','slides.html','flashcards.html','game.html']
                if lang == 'en': files.append('printables.html')
            else:
                files = ['index.html','slides.html','worksheet.html','game.html','printables.html']
        for f in files:
            print(f'  Would create: {f}')
        return

    os.makedirs(out_dir, exist_ok=True)

    level_href_path = f'../../../../{lp}/index.html'
    section_href = '../index.html'

    is_vocab = section in ('vocabulary', 'vocabulario')
    is_es_vocab = is_vocab and lang == 'es'

    # Always generate index, slides, game
    files = {
        'index.html':    gen_index(sp, lp, level_label, sl, sf, prog_key),
        'slides.html':   gen_slides(sp, lp, level_label, sl, prog_key),
        'game.html':     gen_game(sp, lp, level_label, sl, prog_key),
    }

    if is_vocab:
        # Vocab: flashcards instead of worksheet; no printables for ES
        files['flashcards.html'] = _placeholder_flashcards(sp, lp, sl, prog_key)
        if not is_es_vocab:
            files['printables.html'] = gen_printables(sp, lp, level_label, sl, prog_key)
    else:
        files['worksheet.html'] = gen_worksheet(sp, lp, level_label, sl, prog_key)
        files['printables.html'] = gen_printables(sp, lp, level_label, sl, prog_key)

    for fname, content in files.items():
        path = os.path.join(out_dir, fname)
        if os.path.exists(path):
            print(f'  SKIP (exists): {fname}')
            continue
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  Created: {fname}')


def _placeholder_flashcards(sp, level_path, sec_name, prog_key, depth='../../../../'):
    """Minimal flashcards placeholder — will be replaced by actual content later."""
    s = S[sp['lang']]
    slug = sp['slug']
    title = sp['title']
    lang = sp['lang']
    level_upper = sp['level'].upper()
    lp = LEVEL_PATH[(lang, sp['level'])]
    level_href = f'{depth}{lp}/index.html'
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{depth}favicon.svg" type="image/svg+xml">
<title>{level_upper} · {title} — Flashcards | Word Play</title>
<link rel="stylesheet" href="{depth}shared/base.css?v={V['base']}">
<script src="{depth}shared/dark-init.js?v={V['dark_init']}"></script>
</head>
<body>
{_header(lang, 'index.html')}
<div class="container">
  <div class="chapter-num">{s["ch_label"](sp["num"])}</div>
  <h1>{title}</h1>
  <p class="chapter-subtitle">{sp["subtitle"]}</p>
  <p style="color:var(--muted);font-size:.9rem;padding:40px 0;text-align:center"><!-- FLASHCARDS CONTENT PLACEHOLDER --></p>
</div>
{_footer(lang)}
<script src="{depth}shared/store.js?v={V['store']}"></script>
</body>
</html>
'''


if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)

    dry_run = '--dry-run' in args
    spec_files = [a for a in args if not a.startswith('--')]

    for spec_file in spec_files:
        if not os.path.exists(spec_file):
            print(f'Error: spec file not found: {spec_file}')
            sys.exit(1)
        with open(spec_file, encoding='utf-8') as f:
            sp = json.load(f)
        print(f"\n=== Generating: {sp['lang']}/{sp['level']}/{sp['section']}/{sp['slug']} ===")
        build(sp, dry_run=dry_run)

    print('\nDone.')
