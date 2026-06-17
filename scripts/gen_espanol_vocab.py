#!/usr/bin/env python3
"""Generate espanol/ vocabulary chapters (monolingual Spanish course).

Per-chapter output: flashcards.html, slides.html, game.html, match.html, index.html
Content format: CHAPTERS = { slug: dict(level, num, short, words=[...]) }
  words: [(word, ipa, def_es, ex_es), ...] — 12 words; ex_es has target word in <b>

Usage:
  python3 scripts/gen_espanol_vocab.py scripts/content/espanol_a1_v1.py
"""
import importlib.util
import json
import os
import subprocess
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LEVEL_LABEL = {
    'a1': 'A1', 'a2': 'A2', 'b1': 'B1', 'b2': 'B2', 'c1': 'C1', 'c2': 'C2',
}
LEVEL_NAME = {
    'a1': 'A1 Principiante', 'a2': 'A2 Elemental',
    'b1': 'B1 Intermedio', 'b2': 'B2 Intermedio Alto',
    'c1': 'C1 Avanzado', 'c2': 'C2 Maestría',
}

HEAD = """\
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{rel}favicon.svg" type="image/svg+xml">
<title>{title}</title>
<link rel="stylesheet" href="{rel}shared/base.css?v=v125">
{extra_css}\
<script src="/shared/auth.js?v=1"></script>
<script src="{rel}shared/dark-init.js?v=v112"></script>
"""

HEADER_NAV = """\
<header class="site-header"><div class="site-header-inner">
  <a href="../index.html" class="back back-link" aria-label="Atr&#225;s"></a>
  <a href="/" class="brand"><svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px"><rect width="32" height="32" rx="4" fill="currentColor"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>Word Play</a>
  <button class="dark-toggle" aria-label="Modo oscuro" onclick="toggleDark()">&#9680; Oscuro</button>
</div></header>
"""


def jd(o):
    return json.dumps(o, ensure_ascii=False)


def deacc(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def strip_b(s):
    return s.replace('<b>', '').replace('</b>', '')


def blank_ex(ex):
    i = ex.index('<b>')
    j = ex.index('</b>')
    return ex[:i] + '_____' + ex[j + 4:]


def rel_path(level):
    return '../../../../'


def crumb(level, lv_label, short, current):
    return (
        f'<div class="breadcrumb">\n'
        f'  <a href="{rel_path(level)}index.html">Inicio</a><span>&#8250;</span>\n'
        f'  <a href="{rel_path(level)}espanol/index.html">Espa&#241;ol</a><span>&#8250;</span>\n'
        f'  <a href="{rel_path(level)}espanol/{level}/index.html">{lv_label}</a><span>&#8250;</span>\n'
        f'  <a href="../index.html">Vocabulario</a><span>&#8250;</span>\n'
        f'  <strong>{short}</strong>\n'
        f'</div>\n'
    )


def chapter_nav(active):
    pages = [
        ('flashcards.html', 'Tarjetas'),
        ('slides.html', 'Lecci&#243;n'),
        ('game.html', 'Juego'),
        ('match.html', 'Relacionar'),
    ]
    links = ''.join(
        f'<a href="{p}" class="chapter-nav-btn{" active" if p == active else ""}">{label}</a>'
        for p, label in pages
    )
    return f'<nav class="chapter-nav">{links}</nav>\n'


VOCAB_CSS = """\
<style>
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
</style>
"""

MATCH_CSS = """\
<style>
.match-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:20px}
.match-col{display:flex;flex-direction:column;gap:8px}
.match-item{padding:12px 14px;border:1.5px solid var(--hairline);border-radius:6px;cursor:pointer;font-size:.9rem;color:var(--ink);transition:border-color .15s,background .15s;user-select:none;min-height:48px;display:flex;align-items:center}
.match-item.selected{border-color:var(--amber);background:rgba(184,134,11,.08)}
.match-item.correct{border-color:var(--green,#2E7D52);background:rgba(46,125,82,.08);pointer-events:none;color:var(--muted)}
.match-item.wrong{border-color:var(--red,#C03A2B);background:rgba(192,57,43,.08)}
.match-status{font-family:var(--font-sans);font-size:.85rem;color:var(--muted);text-align:center;margin-bottom:16px}
.heart-row{display:flex;gap:6px;justify-content:center;margin-bottom:12px}
.heart-svg{width:22px;height:22px}
.mastery-badge{display:inline-block;padding:8px 18px;background:rgba(184,134,11,.12);color:var(--amber);font-family:var(--font-sans);font-size:.78rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;border-radius:4px;margin-bottom:16px}
</style>
"""


def render_flashcards(d, slug):
    level, lv = d['level'], LEVEL_LABEL[d['level']]
    short, num = d['short'], d['num']
    words = d['words']
    rel = rel_path(level)
    words_js = jd([{'word': w, 'ipa': ipa, 'def': df, 'ex': ex}
                   for w, ipa, df, ex in words])
    storage_key = f'wordplay_vocab_mastered_es_{level}_{slug}'
    s = HEAD.format(
        rel=rel,
        title=f'{short} — Tarjetas | Espa&#241;ol {lv} | Word Play',
        extra_css=VOCAB_CSS,
    )
    s += f'<script src="{rel}shared/store.js?v=v107"></script>\n</head>\n'
    s += '<body>\n' + HEADER_NAV
    s += '<div class="container">\n'
    s += crumb(level, lv, short, 'Tarjetas')
    s += f'<div class="chapter-num">{num}</div>\n<h1>{short}</h1>\n'
    s += chapter_nav('flashcards.html')
    s += f'<div id="masteryBadge" style="margin:12px 0;display:none"><span class="mastery-badge">&#10003; Tema dominado</span></div>\n'
    s += f'<p style="font-family:var(--font-sans);font-size:.75rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:var(--muted);margin-bottom:16px">{len(words)} palabras &middot; pulsa la tarjeta para ver la definici&#243;n</p>\n'
    s += '<div class="fc-nav"><button class="fc-btn" onclick="prevCard()">&#8592; Anterior</button>'
    s += '<span class="fc-counter" id="fcCounter">1 / ' + str(len(words)) + '</span>'
    s += '<button class="fc-btn primary" onclick="nextCard()">Siguiente &#8594;</button></div>\n'
    s += '<div class="fc-wrap"><div class="fc" id="fcCard" onclick="flipCard()">'
    s += '<div class="fc-face fc-front"><div class="fc-word" id="fcWord"></div>'
    s += '<div class="fc-ipa" id="fcIpa"></div>'
    s += '<div class="fc-hint">Pulsa para ver la definici&#243;n</div></div>'
    s += '<div class="fc-face fc-back">'
    s += '<div class="fc-def" id="fcDef"></div>'
    s += '<div class="fc-ex" id="fcEx"></div>'
    s += '<button class="fc-audio" onclick="event.stopPropagation();speakWord()">&#9654; Escuchar</button>'
    s += '</div></div></div>\n'
    s += f"""<script>
var WORDS = {words_js};
var STORAGE_KEY = {jd(storage_key)};
var idx = 0, seen = new Set();
function showCard() {{
  var w = WORDS[idx];
  document.getElementById('fcWord').textContent = w.word;
  document.getElementById('fcIpa').textContent = w.ipa ? '[' + w.ipa + ']' : '';
  document.getElementById('fcDef').textContent = w.def;
  document.getElementById('fcEx').innerHTML = w.ex;
  document.getElementById('fcCard').classList.remove('flipped');
  document.getElementById('fcCounter').textContent = (idx+1) + ' / ' + WORDS.length;
  seen.add(idx);
  if (seen.size === WORDS.length) {{
    var sk = (window.store || localStorage);
    var prog = JSON.parse(sk.getItem('wordplay_progress') || '{{}}');
    prog[{jd(level)}] = prog[{jd(level)}] || {{}};
    prog[{jd(level)}][STORAGE_KEY] = {{done:true, date:new Date().toISOString().slice(0,10)}};
    sk.setItem('wordplay_progress', JSON.stringify(prog));
    document.getElementById('masteryBadge').style.display = '';
  }}
}}
function flipCard() {{ document.getElementById('fcCard').classList.toggle('flipped'); }}
function nextCard() {{ idx = (idx + 1) % WORDS.length; showCard(); }}
function prevCard() {{ idx = (idx - 1 + WORDS.length) % WORDS.length; showCard(); }}
function speakWord() {{
  var u = new SpeechSynthesisUtterance(WORDS[idx].word);
  u.lang = 'es-ES'; u.rate = 0.85;
  window.speechSynthesis.cancel();
  window.speechSynthesis.speak(u);
}}
document.addEventListener('keydown', function(e) {{
  if (e.key === 'ArrowRight' || e.key === ' ') nextCard();
  if (e.key === 'ArrowLeft') prevCard();
  if (e.key === 'Enter') flipCard();
}});
showCard();
(function checkMastery() {{
  var sk = (window.store || localStorage);
  var prog = JSON.parse(sk.getItem('wordplay_progress') || '{{}}');
  if (prog[{jd(level)}] && prog[{jd(level)}][STORAGE_KEY] && prog[{jd(level)}][STORAGE_KEY].done)
    document.getElementById('masteryBadge').style.display = '';
}})();
</script>
"""
    s += '</div>\n<footer class="site-footer">Word Play &middot; Espa&#241;ol {lv} &middot; Vocabulario</footer>\n</body>\n</html>\n'
    return s.replace('{lv}', lv)


def render_slides(d, slug):
    level, lv = d['level'], LEVEL_LABEL[d['level']]
    short, num = d['short'], d['num']
    words = d['words']
    rel = rel_path(level)
    half = (len(words) + 1) // 2
    def word_rows(chunk):
        return ''.join(
            f'<div class="summary-row"><div class="label"><b>{w}</b></div>'
            f'<div class="form">[{ipa}]</div><div class="ex">{df} &mdash; <em>{strip_b(ex)}</em></div></div>'
            for w, ipa, df, ex in chunk
        )
    s = HEAD.format(
        rel=rel,
        title=f'{short} — Lecci&#243;n | Espa&#241;ol {lv} | Word Play',
        extra_css=f'<link rel="stylesheet" href="{rel}shared/slides.css?v=v115">\n',
    )
    s += f'<script src="{rel}shared/store.js?v=v107"></script>\n'
    s += f'<script src="{rel}shared/deck.js?v=v114"></script>\n</head>\n'
    s += '<body class="deck-body">\n' + HEADER_NAV
    s += '<div class="container">\n'
    s += crumb(level, lv, short, 'Lecci&#243;n')
    s += f'<div class="chapter-num">{num}</div>\n<h1>{short}</h1>\n'
    s += chapter_nav('slides.html')
    s += f'<div id="deck">\n'
    s += (
        f'<div class="slide"><div class="slide-card">'
        f'<div class="slide-header"><h2>Bienvenido a {short}</h2></div>'
        f'<p class="slide-explanation">En este tema aprender&#225;s {len(words)} palabras esenciales en espa&#241;ol. '
        f'Cada tarjeta incluye la definici&#243;n y un ejemplo en contexto.</p>'
        f'<div class="overview-row"><div class="overview-label">C&#243;mo estudiar</div>'
        f'<div class="overview-desc">Lee los dos grupos de palabras, luego practica con las tarjetas '
        f'interactivas, el juego de relacionar y el juego de maest&#237;a.</div></div>'
        f'</div></div>\n'
    )
    s += (
        f'<div class="slide"><div class="slide-card">'
        f'<div class="slide-header"><h2>Palabras 1&#8211;{half}</h2></div>'
        f'<div class="slide-summary">{word_rows(words[:half])}</div>'
        f'</div></div>\n'
    )
    s += (
        f'<div class="slide"><div class="slide-card">'
        f'<div class="slide-header"><h2>Palabras {half+1}&#8211;{len(words)}</h2></div>'
        f'<div class="slide-summary">{word_rows(words[half:])}</div>'
        f'</div></div>\n'
    )
    s += '</div>\n'
    s += f'<script>\nwindow.LEVEL={jd(level)};\nwindow.CHAPTER_ID={jd(slug)};\n'
    s += f'window.SECTION="vocabulary";\n</script>\n'
    s += '</div>\n<footer class="site-footer">Word Play &middot; Espa&#241;ol {lv} &middot; Vocabulario</footer>\n</body>\n</html>\n'
    return s.replace('{lv}', lv)


def render_game(d, slug):
    level, lv = d['level'], LEVEL_LABEL[d['level']]
    short, num = d['short'], d['num']
    words = d['words']
    rel = rel_path(level)
    items_js = []
    for w, ipa, df, ex in words[:8]:
        wid = deacc(w.replace(' ', '-').replace('/', '-'))
        wid = ''.join(c for c in wid if c.isalnum() or c == '-')
        acc_list = [deacc(w)] if deacc(w) != w else []
        acc_str = f', accept:{jd(acc_list)}' if acc_list else ''
        items_js.append(
            f'    {{id:{jd(wid)}, term:{jd(w)}, meaning:{jd(df)}, '
            f'synonym:{jd("Espa&#241;ol para: " + df)}, '
            f'example:{jd(ex)}, completion:{jd(blank_ex(ex))}, answer:{jd(w)}{acc_str}}}'
        )
    s = HEAD.format(
        rel=rel,
        title=f'{short} — Juego | Espa&#241;ol {lv} | Word Play',
        extra_css=(
            f'<link rel="stylesheet" href="{rel}shared/game.css?v=v112">\n'
        ),
    )
    s += f'<script src="{rel}shared/i18n.js?v=v124"></script>\n'
    s += f'<script src="{rel}shared/store.js?v=v107"></script>\n'
    s += f'<script src="{rel}shared/game.js?v=v112"></script>\n</head>\n'
    s += '<body>\n' + HEADER_NAV
    s += '<div class="container">\n'
    s += crumb(level, lv, short, 'Juego')
    s += f'<div class="chapter-num">{num}</div>\n<h1>{short}</h1>\n'
    s += chapter_nav('game.html')
    s += ('  <div class="game-wrap">\n'
          '    <div id="gameStart" class="game-screen active">\n      <div class="game-start">\n'
          '        <h2>Juego de Dominio</h2>\n'
          '        <p>4 palabras clave &middot; 3 rondas cada una &middot; llega a 100 puntos para ganar.</p>\n'
          '        <p style="font-size:0.8rem;color:var(--muted);margin-top:8px">Aciertos consecutivos de la misma palabra y rachas entre palabras a&#241;aden puntos extra.</p>\n'
          '        <div class="game-stats-row">\n'
          '          <div class="game-stat"><div class="game-stat-val" id="gStartMastered">0</div><div class="game-stat-label">Dominadas</div></div>\n'
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
          '        <h2>&#161;Dominio alcanzado!</h2>\n        <p>Has completado todas las palabras de este cap&#237;tulo.</p>\n'
          '        <div class="game-stats-row" style="margin:20px 0;">\n'
          '          <div class="game-stat"><div class="game-stat-val" id="gFinalScore">0</div><div class="game-stat-label">Puntuaci&#243;n</div></div>\n'
          '          <div class="game-stat"><div class="game-stat-val" id="gFinalStreak">0</div><div class="game-stat-label">Mejor racha</div></div>\n'
          '          <div class="game-stat"><div class="game-stat-val" id="gFinalPct">0%</div><div class="game-stat-label">Dominadas</div></div>\n'
          '        </div>\n        <div id="gMasteryMap"></div>\n'
          '        <div class="game-btn-row">\n'
          '          <button id="gBtnPlayAgain" class="game-btn primary">Jugar de nuevo</button>\n'
          '          <a href="flashcards.html" class="game-btn secondary">Tarjetas</a>\n'
          '        </div>\n      </div>\n    </div>\n  </div>\n'
          '<div class="game-toast" id="gToast"></div>\n')
    items_block = ',\n'.join(items_js)
    s += f"""<script>
window.GAME_DATA = {{
  chapterId: {jd(slug)},
  level: {jd(level)},
  title: {jd(short)},
  storageKey: {jd(f'wordplay_game_es_{level}_{slug}')},
  section: 'vocabulary',
  items: [
{items_block}
  ]
}};
</script>
"""
    s += '</div>\n<footer class="site-footer">Word Play &middot; Espa&#241;ol {lv} &middot; Vocabulario</footer>\n</body>\n</html>\n'
    return s.replace('{lv}', lv)


def render_match(d, slug):
    level, lv = d['level'], LEVEL_LABEL[d['level']]
    short, num = d['short'], d['num']
    words = d['words']
    rel = rel_path(level)
    storage_key = f'wordplay_match_es_{level}_{slug}'
    pairs_js = jd([[w, df] for w, _, df, _ in words[:8]])
    s = HEAD.format(
        rel=rel,
        title=f'{short} — Relacionar | Espa&#241;ol {lv} | Word Play',
        extra_css=MATCH_CSS,
    )
    s += f'<script src="{rel}shared/store.js?v=v107"></script>\n</head>\n'
    s += '<body>\n' + HEADER_NAV
    s += '<div class="container">\n'
    s += crumb(level, lv, short, 'Relacionar')
    s += f'<div class="chapter-num">{num}</div>\n<h1>{short}</h1>\n'
    s += chapter_nav('match.html')
    s += '<div id="masteryBadge" style="margin:12px 0;display:none"><span class="mastery-badge">&#10003; Tema dominado</span></div>\n'
    s += '<div class="match-status" id="matchStatus">Relaciona cada palabra con su definici&#243;n</div>\n'
    s += '<div class="heart-row" id="heartRow"></div>\n'
    s += '<div class="match-grid"><div class="match-col" id="colWords"></div><div class="match-col" id="colDefs"></div></div>\n'
    s += '<div style="text-align:center;margin-top:12px"><button class="fc-btn" onclick="restart()">Reiniciar</button></div>\n'
    s += f"""<script>
var PAIRS = {pairs_js};
var STORAGE_KEY = {jd(storage_key)};
var LEVEL = {jd(level)};
var lives = 3, matched = 0, needTwo = 0, selected = null;
var rounds = []; /* each word needs 2 correct matches */
function shuffle(a) {{ for(var i=a.length-1;i>0;i--){{ var j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]; }} return a; }}
function heartSVG(filled) {{
  return '<svg class="heart-svg" viewBox="0 0 24 24"><path fill="' + (filled?'var(--amber)':'var(--hairline)') + '" d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>';
}}
function updateHearts() {{
  document.getElementById('heartRow').innerHTML = heartSVG(lives>=1)+heartSVG(lives>=2)+heartSVG(lives>=3);
}}
function buildRound() {{
  var words = shuffle(PAIRS.map(function(p,i){{return {{idx:i,text:p[0],type:'w'}};}}));
  var defs = shuffle(PAIRS.map(function(p,i){{return {{idx:i,text:p[1],type:'d'}};}}));
  document.getElementById('colWords').innerHTML = words.map(function(w){{
    return '<div class="match-item" data-idx="'+w.idx+'" data-type="w" onclick="pick(this)">'+w.text+'</div>';
  }}).join('');
  document.getElementById('colDefs').innerHTML = defs.map(function(d){{
    return '<div class="match-item" data-idx="'+d.idx+'" data-type="d" onclick="pick(this)">'+d.text+'</div>';
  }}).join('');
  matched = 0; selected = null;
  document.getElementById('matchStatus').textContent = 'Relaciona cada palabra con su definición';
}}
function pick(el) {{
  if (el.classList.contains('correct') || el.classList.contains('wrong')) return;
  if (selected && selected === el) {{ el.classList.remove('selected'); selected = null; return; }}
  if (!selected) {{ el.classList.add('selected'); selected = el; return; }}
  if (selected.dataset.type === el.dataset.type) {{
    selected.classList.remove('selected'); selected.classList.add('selected');
    el.classList.add('selected'); selected.classList.remove('selected'); selected = el;
    return;
  }}
  var a = selected, b = el;
  if (a.dataset.idx === b.dataset.idx) {{
    a.classList.remove('selected'); a.classList.add('correct');
    b.classList.add('correct'); matched++; selected = null;
    if (matched === PAIRS.length) {{ needTwo++; if (needTwo >= 2) finish(); else {{ setTimeout(buildRound,600); }} }}
  }} else {{
    a.classList.add('wrong'); b.classList.add('wrong');
    lives = Math.max(0, lives - 1); updateHearts();
    setTimeout(function(){{ a.classList.remove('wrong','selected'); b.classList.remove('wrong'); selected=null; }}, 700);
    if (lives === 0) {{ document.getElementById('matchStatus').textContent = 'Sin vidas. Reinicia para intentarlo de nuevo.'; }}
  }}
}}
function finish() {{
  var sk = (window.store || localStorage);
  var prog = JSON.parse(sk.getItem('wordplay_progress') || '{{}}');
  prog[LEVEL] = prog[LEVEL] || {{}};
  prog[LEVEL][STORAGE_KEY] = {{done:true, date:new Date().toISOString().slice(0,10)}};
  sk.setItem('wordplay_progress', JSON.stringify(prog));
  document.getElementById('masteryBadge').style.display = '';
  document.getElementById('matchStatus').textContent = '¡Tema dominado!';
}}
function restart() {{ lives=3; needTwo=0; updateHearts(); buildRound(); document.getElementById('masteryBadge').style.display='none'; }}
(function init() {{
  updateHearts(); buildRound();
  var sk=(window.store||localStorage);
  var prog=JSON.parse(sk.getItem('wordplay_progress')||'{{}}');
  if(prog[LEVEL]&&prog[LEVEL][STORAGE_KEY]&&prog[LEVEL][STORAGE_KEY].done)
    document.getElementById('masteryBadge').style.display='';
}})();
</script>
"""
    s += '</div>\n<footer class="site-footer">Word Play &middot; Espa&#241;ol {lv} &middot; Vocabulario</footer>\n</body>\n</html>\n'
    return s.replace('{lv}', lv)


def render_index(d, slug):
    level, lv = d['level'], LEVEL_LABEL[d['level']]
    short, num = d['short'], d['num']
    words = d['words']
    rel = rel_path(level)
    s = HEAD.format(
        rel=rel,
        title=f'{short} | Vocabulario {lv} | Word Play',
        extra_css='',
    )
    s += f'<script src="{rel}shared/store.js?v=v107"></script>\n</head>\n'
    s += '<body>\n' + HEADER_NAV
    s += '<div class="container">\n'
    s += crumb(level, lv, short, short)
    s += f'<div class="chapter-num">{num}</div>\n<h1>{short}</h1>\n'
    s += f'<p class="chapter-subtitle">{len(words)} palabras esenciales con definici&#243;n y ejemplo en espa&#241;ol</p>\n'
    s += '<div class="act-grid">\n'
    acts = [
        ('flashcards.html', 'Tarjetas', 'Estudia las palabras con tarjetas interactivas', 'lesson', 'var(--amber)'),
        ('slides.html', 'Lecci&#243;n', 'Lista completa de palabras con definiciones', 'lesson', 'var(--amber)'),
        ('game.html', 'Juego de Maest&#237;a', 'Juego interactivo para dominar las palabras', 'game', '#2E7D52'),
        ('match.html', 'Relacionar', 'Relaciona palabras con sus definiciones', 'game', '#2E7D52'),
    ]
    for href, title, desc, kind, color in acts:
        s += (
            f'<a href="{href}" class="act-card" style="--ac-color:{color}">\n'
            f'  <div class="act-title">{title}</div>\n'
            f'  <div class="act-desc">{desc}</div>\n'
            f'  <span class="act-cta">Ir &#8594;</span>\n'
            f'</a>\n'
        )
    s += '</div>\n'
    s += f"""<script>
(function() {{
  var sk=(window.store||localStorage);
  var prog=JSON.parse(sk.getItem('wordplay_progress')||'{{}}');
  var lv=prog[{jd(level)}]||{{}};
  var fk='wordplay_vocab_mastered_es_{level}_{slug}';
  var gk='wordplay_game_es_{level}_{slug}';
  var mk='wordplay_match_es_{level}_{slug}';
  if(lv[fk]&&lv[fk].done) document.querySelector('[href="flashcards.html"]').classList.add('done');
  if(lv[gk]&&lv[gk].pct>=100) document.querySelector('[href="game.html"]').classList.add('done');
  if(lv[mk]&&lv[mk].done) document.querySelector('[href="match.html"]').classList.add('done');
}})();
</script>
"""
    s += '</div>\n<footer class="site-footer">Word Play &middot; Espa&#241;ol {lv} &middot; Vocabulario</footer>\n</body>\n</html>\n'
    return s.replace('{lv}', lv)


def render(slug, d):
    level = d['level']
    out_dir = os.path.join(ROOT, 'espanol', level, 'vocabulary', slug)
    os.makedirs(out_dir, exist_ok=True)
    open(os.path.join(out_dir, 'flashcards.html'), 'w', encoding='utf-8').write(render_flashcards(d, slug))
    open(os.path.join(out_dir, 'slides.html'), 'w', encoding='utf-8').write(render_slides(d, slug))
    open(os.path.join(out_dir, 'game.html'), 'w', encoding='utf-8').write(render_game(d, slug))
    open(os.path.join(out_dir, 'match.html'), 'w', encoding='utf-8').write(render_match(d, slug))
    open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8').write(render_index(d, slug))
    files = [os.path.join(out_dir, f) for f in
             ('flashcards.html', 'slides.html', 'game.html', 'match.html', 'index.html')]
    r = subprocess.run(['python3', os.path.join(ROOT, 'scripts/validate_inline_js.py')] + files,
                       capture_output=True, text=True)
    status = 'OK' if r.returncode == 0 else 'FAIL\n' + r.stdout
    print(f'espanol/{level}/vocabulary/{slug}: rendered, validate={status}')
    return r.returncode == 0


def main():
    mod_path = sys.argv[1]
    spec = importlib.util.spec_from_file_location('content', mod_path)
    if spec is None:
        print(f'ERROR: cannot load {mod_path}', file=sys.stderr)
        sys.exit(1)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    ok = True
    for slug, d in mod.CHAPTERS.items():
        ok = render(slug, d) and ok
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
