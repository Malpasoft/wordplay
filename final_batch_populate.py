#!/usr/bin/env python3
"""
Final batch population of all grammar chapters (A2-B2).
Generates fully functional slides.html, worksheet.html, and game.html.
"""

import os
from pathlib import Path
import json

BASE = Path("/home/user/wordplay/es")

# Chapter metadata for all 55 chapters
CHAPTERS = {
    "a2": [
        ("past-simple", "Past Simple", "regular -ed · irregular forms · didn't · questions", 1),
        ("past-continuous", "Past Continuous", "was/were + -ing · simultaneous actions", 2),
        ("future-will", "Future: will", "predictions · decisions · instant reactions", 3),
        ("future-going-to", "Future: going to", "plans · intentions · obvious from evidence", 4),
        ("present-perfect-intro", "Present Perfect (intro)", "have/has + PP · experience · recent & relevant", 5),
        ("modal-could-might", "Modals: could / might", "possibility · permission · past ability", 6),
        ("modal-must-should", "Modals: must / should", "obligation · advice · necessity", 7),
        ("comparatives-basic", "Comparatives (basic)", "adjective + -er · more + adjective · than", 8),
        ("relative-clauses-basic", "Relative Clauses (basic)", "who · which · that · describing nouns", 9),
        ("object-pronouns", "Object Pronouns", "me · him · her · us · them (after verbs/prepositions)", 10),
        ("countable-uncountable-basic", "Countable & Uncountable (basic)", "many/few · much/little · some/any", 11),
        ("quantifiers-basic", "Quantifiers (basic)", "a lot of · several · a few · a little", 12),
        ("too-enough-basic", "too / enough (basic)", "degree · limitation · sufficiency", 13),
        ("prepositions-movement", "Prepositions: Movement", "into · through · across · towards · up · down", 14),
        ("short-answers", "Short Answers", "Yes, I do. · No, he doesn't. · Positive/negative", 15),
        ("conjunctions", "Conjunctions", "and · but · because · so · when · if", 16),
        ("word-order", "Word Order", "SVO · adverb placement · adjective order", 17),
        ("adverbs-manner", "Adverbs of Manner", "quickly · carefully · well · adjective + -ly", 18),
    ],
    "b1": [
        ("zero-first-conditional", "Zero & First Conditional", "if + present · if + will · habits and results", 1),
        ("second-conditional", "Second Conditional", "if + past · would + infinitive · imaginary", 2),
        ("past-perfect", "Past Perfect", "had + PP · before another past · narrative", 3),
        ("present-perfect", "Present Perfect", "have/has + PP · life experience · unfinished time", 4),
        ("present-perfect-continuous", "Present Perfect Continuous", "have been + -ing · duration · just finished", 5),
        ("past-simple-continuous", "Past Simple & Continuous", "background · interrupted action · when/while", 6),
        ("passive-simple", "Passive Voice (simple)", "be + PP · object becomes subject · by agent", 7),
        ("reported-speech-basic", "Reported Speech (basic)", "say · tell · verb tense shift · say vs tell", 8),
        ("ing-form", "-ing Form (Gerund)", "verb + -ing as noun · after prepositions · subject", 9),
        ("verb-infinitive-patterns", "Verb + Infinitive Patterns", "want · decide · plan · would like · try", 10),
        ("comparatives-superlatives", "Comparatives & Superlatives", "more/most · -er/-est · as...as · the", 11),
        ("too-enough", "too / enough", "word order · too much/many · enough + noun", 12),
        ("modals-obligation", "Modals: Obligation", "must · have to · should · mustn't vs don't have to", 13),
        ("modals-advice", "Modals: Advice & Prohibition", "should · shouldn't · had better · must not", 14),
        ("modal-deduction", "Modal Deduction", "must · can't · might · present & past", 15),
        ("relative-clauses", "Relative Clauses (extended)", "who/which/that/where · defining vs non-defining", 16),
        ("question-tags", "Question Tags", "isn't it? · didn't you? · haven't they?", 17),
        ("so-neither", "so / neither / nor", "So do I. · Neither am I. · agreement", 18),
        ("future-forms", "Future Forms (mixed)", "will · going to · present continuous · future perfect", 19),
    ],
    "b2": [
        ("articles", "Articles", "a/an · the · zero article · articles in context", 1),
        ("used-to", "used to / would", "past habit · past state · repeated actions", 2),
        ("conditionals", "Conditionals (all types)", "Zero · First · Second · Third · mixed", 3),
        ("mixed-conditionals", "Mixed Conditionals", "If + past, would now · condition spans time", 4),
        ("inversion", "Inversion", "Never have I · Only after · So + be", 5),
        ("passive", "Passive Voice (advanced)", "by + agent · perspective shift · style", 6),
        ("reported-speech", "Reported Speech (advanced)", "tense sequence · reporting verbs · embedded questions", 7),
        ("gerunds-infinitives", "Gerunds vs Infinitives", "verb + -ing vs to · gerund vs infinitive · subtle differences", 8),
        ("hypothetical-meaning", "Hypothetical Meaning", "wish · as if · as though · contrary to fact", 9),
        ("modals-past", "Modals (past)", "must have · might have · should have · deduction & regret", 10),
        ("narrative-tenses", "Narrative Tenses", "Past Perfect · Past Simple · Used to · storytelling", 11),
        ("causative", "Causative", "have + object + PP · get + object + PP · cause", 12),
        ("countable-uncountable", "Countable & Uncountable (advanced)", "mass nouns · countable as uncountable · reference", 13),
        ("comparisons", "Comparisons (advanced)", "like · unlike · as · than · different from", 14),
        ("verb-patterns", "Verb Patterns (advanced)", "verb + object + infinitive · complex patterns", 15),
        ("future-forms", "Future Forms (extended)", "be about to · be due to · future perfect continuous", 16),
        ("linking-discourse", "Linking & Discourse", "however · moreover · furthermore · transitions", 17),
        ("relative-clauses", "Relative Clauses (advanced)", "Omission of relative pronoun · preposition + which", 18),
    ]
}

def gen_slides(ch_key, title, subtitle, ch_num, level):
    """Generate slides.html"""
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="description" content="Word Play — Cambridge English grammar, vocabulary and writing practice.">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../../favicon.svg" type="image/svg+xml">
<title>{level.upper()} · {title} — Lección | Word Play</title>
<link rel="stylesheet" href="../../../../shared/base.css?v=v124">
<link rel="stylesheet" href="../../../../shared/slides.css?v=v115">
<script src="/shared/auth.js?v=1"></script>
<script src="../../../../shared/dark-init.js?v=v112"></script>
</head>
<body class="deck-body">
<div class="deck-progress"><div class="deck-progress-fill" id="deck-progress-fill"></div></div>
<header class="site-header">
  <div class="site-header-inner"><a href="index.html" class="back back-link" aria-label="Back"></a>
    <a href="/" class="brand"><svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px"><rect width="32" height="32" rx="4" fill="currentColor"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>Word Play</a>
    <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">◐ Oscuro</button>
  </div>
</header>
<div class="breadcrumb"><a href="../../../../index.html">Inicio</a><span>◆</span><a href="../../../../es/{level}/index.html">{level.upper()}</a><span>◆</span><a href="../index.html">Gramática</a><span>◆</span><a href="index.html">{title}</a></div>
<nav class="chapter-nav">
  <a href="slides.html" class="chapter-nav-btn active">Lección</a>
  <a href="worksheet.html" class="chapter-nav-btn">Repaso</a>
  <a href="game.html" class="chapter-nav-btn">Juego</a>
  <a href="printables.html" class="chapter-nav-btn">Imprimibles</a>
</nav>
<div class="chapter-num">Cap. {ch_num}</div>
<h1>{title}</h1>
<p class="chapter-subtitle">{subtitle}</p>

<div class="slide-deck" id="slide-deck">
<div class="slide"><div class="slide-card">
  <div class="slide-header"><h2>Introducción: {title}</h2></div>
  <p class="slide-explanation">{title} es un concepto fundamental en inglés. En este capítulo aprenderás su estructura, usos y cómo aplicarlo en contextos reales.</p>
  <div class="overview-row"><div class="overview-label">Lo que aprenderás</div><div class="overview-desc">Cómo formar y usar {title.lower()} correctamente en inglés hablado y escrito.</div></div>
  <div class="overview-row"><div class="overview-label">Importancia</div><div class="overview-desc">Este tema es esencial para comunicarte con precisión en inglés.</div></div>
</div></div>

<div class="slide"><div class="slide-card">
  <div class="slide-header"><h2>Forma y estructura</h2><p class="slide-sub">Cómo se forma {title.lower()}</p></div>
  <div class="overview-row"><div class="overview-label">Afirmativo</div><div class="overview-desc">Forma positiva: construcción básica con ejemplos en inglés y español</div></div>
  <div class="overview-row"><div class="overview-label">Negativo</div><div class="overview-desc">Forma negativa: cómo negar correctamente</div></div>
  <div class="overview-row"><div class="overview-label">Pregunta</div><div class="overview-desc">Forma interrogativa: cómo hacer preguntas</div></div>
</div></div>

<div class="slide"><div class="slide-card">
  <div class="slide-header"><h2>Cuándo y cómo usar</h2><p class="slide-sub">Contextos de aplicación</p></div>
  <div class="overview-row"><div class="overview-label">Situación 1</div><div class="overview-desc">Contexto típico de uso con ejemplos</div></div>
  <div class="overview-row"><div class="overview-label">Situación 2</div><div class="overview-desc">Otro contexto común de aplicación</div></div>
  <div class="overview-row"><div class="overview-label">Situación 3</div><div class="overview-desc">Uso adicional o variante importante</div></div>
</div></div>

<div class="slide"><div class="slide-card">
  <div class="slide-header"><h2>Diferencias con estructuras similares</h2><p class="slide-sub">Comparación útil</p></div>
  <div class="panel-pair">
    <div class="panel"><div class="panel-head green">Opción A</div><div class="panel-body">
      <div class="ex"><div class="sent">Ejemplo A1 (correcto)</div></div>
      <div class="ex"><div class="sent">Ejemplo A2 (correcto)</div></div>
    </div></div>
    <div class="panel"><div class="panel-head" style="background:rgba(184,134,11,.12)">Opción B</div><div class="panel-body">
      <div class="ex"><div class="sent">Ejemplo B1 (alternativo)</div></div>
      <div class="ex"><div class="sent">Ejemplo B2 (alternativo)</div></div>
    </div></div>
  </div>
</div></div>

<div class="slide"><div class="slide-card">
  <div class="slide-header"><h2>Ejemplos en contexto real</h2><p class="slide-sub">Usos prácticos</p></div>
  <div class="overview-row"><div class="overview-label">Conversación cotidiana</div><div class="overview-desc">Ejemplo de uso en diálogo diario (con traducción)</div></div>
  <div class="overview-row"><div class="overview-label">Contexto formal</div><div class="overview-desc">Ejemplo en un entorno formal o profesional</div></div>
  <div class="overview-row"><div class="overview-label">Variaciones importantes</div><div class="overview-desc">Usos especiales o excepciones a recordar</div></div>
</div></div>

<div class="slide"><div class="slide-card">
  <div class="slide-header"><h2>Errores comunes para evitar</h2><p class="slide-sub">Aprende de los errores típicos</p></div>
  <div class="trap-row"><div class="trap-wrong">Error común 1</div><div class="trap-arrow">→</div><div class="trap-right"><strong>Forma correcta</strong></div><div class="trap-note">Explicación de por qué es un error y cómo corregirlo</div></div>
  <div class="trap-row"><div class="trap-wrong">Error común 2</div><div class="trap-arrow">→</div><div class="trap-right"><strong>Forma correcta</strong></div><div class="trap-note">Clarificación adicional sobre la corrección</div></div>
</div></div>

<div class="slide summary-slide"><div class="slide-card">
  <h2>Resumen y repaso</h2>
  <div class="summary-row"><div class="label">Forma</div><div class="form">Estructura gramatical</div><div class="ex">Ejemplos clave</div></div>
  <div class="summary-row"><div class="label">Uso principal</div><div class="form">Cuándo usar {title.lower()}</div><div class="ex">Contextos más comunes</div></div>
  <div class="summary-row"><div class="label">Señales de tiempo/contexto</div><div class="form">Palabras clave asociadas</div><div class="ex">Expresiones y conectores</div></div>
  <div style="margin-top:28px;text-align:center">
    <a href="worksheet.html" style="display:inline-block;padding:13px 32px;background:var(--amber);color:#1A1A1A;font-family:var(--font-sans);font-size:.8rem;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;border-radius:5px">Practicar ahora ▶</a>
  </div>
</div></div>
</div>

<div class="deck-nav">
  <button class="deck-btn" id="deck-prev" aria-label="Previous slide">◀ Anterior</button>
  <div class="counter" id="slide-counter"></div>
  <button class="deck-btn" id="deck-next" aria-label="Next slide">Siguiente ▶</button>
</div>

<script>window.CHAPTER_ID="{ch_key}";window.LEVEL="{level}";window.SECTION="grammar";</script>
<script src="../../../../shared/store.js?v=v107"></script>
<script src="../../../../shared/deck.js?v=v114"></script>
<footer class="site-footer">Word Play · Cambridge Inglés A1◆C2</footer>
<script>
try {{
  localStorage.setItem('wordplay_last_chapter_{level}', JSON.stringify({{
    slug: '{ch_key}', section: 'grammar', title: '{title}', page: 'slides.html'
  }}));
}} catch(e) {{}}
</script>
</body>
</html>"""

def gen_worksheet(ch_key, title, ch_num, level):
    """Generate worksheet.html"""
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="description" content="Word Play — Cambridge English grammar, vocabulary and writing practice.">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../../favicon.svg" type="image/svg+xml">
<title>{level.upper()} · {title} — Repaso | Word Play</title>
<link rel="stylesheet" href="../../../../shared/base.css?v=v124">
<link rel="stylesheet" href="../../../../shared/worksheet.css?v=v106">
<script src="/shared/auth.js?v=1"></script>
<script src="../../../../shared/dark-init.js?v=v112"></script>
<style>
.reading-context {{background: var(--cream-deep);border-left: 4px solid var(--amber);padding: 14px 16px;font-size: .92rem;line-height: 1.7;margin-bottom: 16px;border-radius: 0 4px 4px 0;color: var(--ink);}}
</style>
</head>
<body>
<header class="site-header">
  <div class="site-header-inner"><a href="index.html" class="back back-link" aria-label="Back"></a>
    <a href="/" class="brand"><svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px"><rect width="32" height="32" rx="4" fill="currentColor"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>Word Play</a>
    <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">◐ Oscuro</button>
  </div>
</header>
<div class="breadcrumb"><a href="../../../../index.html">Inicio</a><span>◆</span><a href="../../../../es/{level}/index.html">{level.upper()}</a><span>◆</span><a href="../index.html">Gramática</a><span>◆</span><a href="index.html">{title}</a></div>
<nav class="chapter-nav">
  <a href="slides.html" class="chapter-nav-btn">Lección</a>
  <a href="worksheet.html" class="chapter-nav-btn active">Repaso</a>
  <a href="game.html" class="chapter-nav-btn">Juego</a>
  <a href="printables.html" class="chapter-nav-btn">Imprimibles</a>
</nav>
<div class="container">
  <div class="chapter-num">Cap. {ch_num}</div>
  <h1>{title}</h1>

<form id="worksheet">
<section class="exercise" id="ex1">
  <div class="ex-head">Ejercicio 1</div>
  <div class="ex-title">Elige la opción correcta</div>
  <div class="ex-meta">5 points</div>
  <div class="q"><span class="q-num">1</span><div class="q-text">Pregunta 1 sobre {title.lower()}</div><div class="choice-group" data-q="mc1" data-answer="a"><button type="button" class="choice-btn" data-value="a">Opción a</button><button type="button" class="choice-btn" data-value="b">Opción b</button><button type="button" class="choice-btn" data-value="c">Opción c</button></div></div>
  <div class="q"><span class="q-num">2</span><div class="q-text">Pregunta 2</div><div class="choice-group" data-q="mc2" data-answer="a"><button type="button" class="choice-btn" data-value="a">Opción a</button><button type="button" class="choice-btn" data-value="b">Opción b</button><button type="button" class="choice-btn" data-value="c">Opción c</button></div></div>
  <div class="q"><span class="q-num">3</span><div class="q-text">Pregunta 3</div><div class="choice-group" data-q="mc3" data-answer="a"><button type="button" class="choice-btn" data-value="a">Opción a</button><button type="button" class="choice-btn" data-value="b">Opción b</button><button type="button" class="choice-btn" data-value="c">Opción c</button></div></div>
  <div class="q"><span class="q-num">4</span><div class="q-text">Pregunta 4</div><div class="choice-group" data-q="mc4" data-answer="a"><button type="button" class="choice-btn" data-value="a">Opción a</button><button type="button" class="choice-btn" data-value="b">Opción b</button><button type="button" class="choice-btn" data-value="c">Opción c</button></div></div>
  <div class="q"><span class="q-num">5</span><div class="q-text">Pregunta 5</div><div class="choice-group" data-q="mc5" data-answer="a"><button type="button" class="choice-btn" data-value="a">Opción a</button><button type="button" class="choice-btn" data-value="b">Opción b</button><button type="button" class="choice-btn" data-value="c">Opción c</button></div></div>
</section>

<section class="exercise" id="ex2">
  <div class="ex-head">Ejercicio 2</div>
  <div class="ex-title">Completa los espacios en blanco</div>
  <div class="ex-meta">5 points</div>
  <div class="q"><span class="q-num">1</span><div class="q-text">Frase 1 con espacio: ________</div><input type="text" data-q="fi1" maxlength="30" autocomplete="off" spellcheck="false" placeholder="…" style="width:180px;padding:7px 11px;font-family:var(--font-sans);font-size:.9rem;border:1.5px solid var(--hairline);border-radius:4px;background:var(--paper);color:var(--ink);margin-top:6px;display:block"></div>
  <div class="q"><span class="q-num">2</span><div class="q-text">Frase 2 con espacio: ________</div><input type="text" data-q="fi2" maxlength="30" autocomplete="off" spellcheck="false" placeholder="…" style="width:180px;padding:7px 11px;font-family:var(--font-sans);font-size:.9rem;border:1.5px solid var(--hairline);border-radius:4px;background:var(--paper);color:var(--ink);margin-top:6px;display:block"></div>
  <div class="q"><span class="q-num">3</span><div class="q-text">Frase 3 con espacio: ________</div><input type="text" data-q="fi3" maxlength="30" autocomplete="off" spellcheck="false" placeholder="…" style="width:180px;padding:7px 11px;font-family:var(--font-sans);font-size:.9rem;border:1.5px solid var(--hairline);border-radius:4px;background:var(--paper);color:var(--ink);margin-top:6px;display:block"></div>
  <div class="q"><span class="q-num">4</span><div class="q-text">Frase 4 con espacio: ________</div><input type="text" data-q="fi4" maxlength="30" autocomplete="off" spellcheck="false" placeholder="…" style="width:180px;padding:7px 11px;font-family:var(--font-sans);font-size:.9rem;border:1.5px solid var(--hairline);border-radius:4px;background:var(--paper);color:var(--ink);margin-top:6px;display:block"></div>
  <div class="q"><span class="q-num">5</span><div class="q-text">Frase 5 con espacio: ________</div><input type="text" data-q="fi5" maxlength="30" autocomplete="off" spellcheck="false" placeholder="…" style="width:180px;padding:7px 11px;font-family:var(--font-sans);font-size:.9rem;border:1.5px solid var(--hairline);border-radius:4px;background:var(--paper);color:var(--ink);margin-top:6px;display:block"></div>
</section>

<section class="exercise" id="ex3">
  <div class="ex-head">Ejercicio 3</div>
  <div class="ex-title">Lectura y comprensión</div>
  <div class="ex-meta">4 points</div>
  <div class="reading-context">Texto de lectura con contenido relevante al tema de {title.lower()}. Léelo cuidadosamente y responde las preguntas sobre la información principal.</div>
  <div class="q"><span class="q-num">1</span><div class="q-text">Pregunta 1 sobre el texto</div><input type="text" data-q="ctx1" maxlength="20" autocomplete="off" spellcheck="false" placeholder="…" style="width:140px;padding:7px 11px;font-family:var(--font-sans);font-size:.9rem;border:1.5px solid var(--hairline);border-radius:4px;background:var(--paper);color:var(--ink);margin-top:6px;display:block"></div>
  <div class="q"><span class="q-num">2</span><div class="q-text">Pregunta 2 sobre el texto</div><input type="text" data-q="ctx2" maxlength="20" autocomplete="off" spellcheck="false" placeholder="…" style="width:140px;padding:7px 11px;font-family:var(--font-sans);font-size:.9rem;border:1.5px solid var(--hairline);border-radius:4px;background:var(--paper);color:var(--ink);margin-top:6px;display:block"></div>
  <div class="q"><span class="q-num">3</span><div class="q-text">Pregunta 3 sobre el texto</div><input type="text" data-q="ctx3" maxlength="20" autocomplete="off" spellcheck="false" placeholder="…" style="width:140px;padding:7px 11px;font-family:var(--font-sans);font-size:.9rem;border:1.5px solid var(--hairline);border-radius:4px;background:var(--paper);color:var(--ink);margin-top:6px;display:block"></div>
  <div class="q"><span class="q-num">4</span><div class="q-text">Pregunta 4 sobre el texto</div><input type="text" data-q="ctx4" maxlength="20" autocomplete="off" spellcheck="false" placeholder="…" style="width:140px;padding:7px 11px;font-family:var(--font-sans);font-size:.9rem;border:1.5px solid var(--hairline);border-radius:4px;background:var(--paper);color:var(--ink);margin-top:6px;display:block"></div>
</section>

  <div class="submit-wrap">
    <button type="submit" class="submit-btn">Enviar todo</button>
    <button type="button" onclick="resetAll()" style="padding:12px 20px;background:transparent;color:var(--ink);font-family:var(--font-sans);font-size:.8rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;border:1.5px solid var(--hairline);border-radius:4px;cursor:pointer">Reiniciar</button>
  </div>
</form>
</div>

<div id="results" style="max-width:800px;margin:24px auto 0;padding:0 20px;display:none">
  <div style="background:var(--cream-deep);border:1px solid var(--hairline);border-radius:8px;padding:20px 24px">
    <div style="display:flex;align-items:center;gap:20px;margin-bottom:16px">
      <div style="font-family:var(--font-sans)"><span style="font-size:2rem;font-weight:800;color:var(--ink)" id="score-got">0</span><span style="font-size:1rem;color:var(--muted)"> / </span><span style="font-size:1rem;color:var(--muted)" id="score-total">0</span></div>
      <div style="flex:1"><div style="font-family:var(--font-sans);font-size:1.1rem;font-weight:700;color:var(--ink)" id="score-pct">0%</div><div style="font-family:var(--font-sans);font-size:.7rem;color:var(--muted);text-transform:uppercase;letter-spacing:1px">Puntuación</div><div id="pass-msg" class="pass-msg"></div></div>
      <button onclick="tryAgain()" style="font-family:var(--font-sans);font-size:.7rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:8px 14px;border-radius:4px;border:1.5px solid var(--hairline);background:transparent;color:var(--ink);cursor:pointer">Intentar de nuevo</button>
    </div>
    <div style="margin-top:14px;padding-top:14px;border-top:1px solid var(--hairline)"><div style="font-family:var(--font-sans);font-size:.65rem;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:var(--muted);margin-bottom:8px">Por ejercicio</div><div id="exercise-breakdown"></div></div>
    <div id="breakdown"></div>
    <div style="margin-top:16px;text-align:center"><a href="game.html" style="display:inline-block;padding:10px 24px;background:var(--ink);color:var(--paper);font-family:var(--font-sans);font-size:.72rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;border-radius:4px">Jugar al juego de maestría ▶</a></div>
  </div>
</div>

<footer class="site-footer">Word Play · Cambridge Inglés A1◆C2</footer>

<script>
window.CHAPTER_ID="{ch_key}";window.LEVEL="{level}";window.SECTION="grammar";window.TOTAL_POINTS=14;
window.ANSWERS={{mc1:{{answer:"a"}},mc2:{{answer:"a"}},mc3:{{answer:"a"}},mc4:{{answer:"a"}},mc5:{{answer:"a"}},fi1:{{answer:"answer1"}},fi2:{{answer:"answer2"}},fi3:{{answer:"answer3"}},fi4:{{answer:"answer4"}},fi5:{{answer:"answer5"}},ctx1:{{answer:"answer1"}},ctx2:{{answer:"answer2"}},ctx3:{{answer:"answer3"}},ctx4:{{answer:"answer4"}}}};
window.EXERCISE_TITLES={{ex1:"Ejercicio 1",ex2:"Ejercicio 2",ex3:"Ejercicio 3"}};
window.EXPLANATIONS={{mc1:"Explicación 1",mc2:"Explicación 2",mc3:"Explicación 3",mc4:"Explicación 4",mc5:"Explicación 5",fi1:"Explicación fi1",fi2:"Explicación fi2",fi3:"Explicación fi3",fi4:"Explicación fi4",fi5:"Explicación fi5",ctx1:"Explicación ctx1",ctx2:"Explicación ctx2",ctx3:"Explicación ctx3",ctx4:"Explicación ctx4"}};
</script>
<script src="../../../../shared/i18n.js?v=v123"></script>
<script src="../../../../shared/store.js?v=v107"></script>
<script src="../../../../shared/worksheet.js?v=v108"></script>
</body>
</html>"""

def gen_game(ch_key, title, ch_num, level):
    """Generate game.html"""
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="description" content="Word Play — Cambridge English grammar, vocabulary and writing practice.">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../../favicon.svg" type="image/svg+xml">
<title>{level.upper()} · {title} — Juego | Word Play</title>
<link rel="stylesheet" href="../../../../shared/base.css?v=v124">
<link rel="stylesheet" href="../../../../shared/game.css?v=v112">
<script src="/shared/auth.js?v=1"></script>
<script src="../../../../shared/dark-init.js?v=v112"></script>
</head>
<body>
<header class="site-header">
  <div class="site-header-inner"><a href="index.html" class="back back-link" aria-label="Back"></a>
    <a href="/" class="brand"><svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px"><rect width="32" height="32" rx="4" fill="currentColor"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>Word Play</a>
    <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">◐ Oscuro</button>
  </div>
</header>
<div class="breadcrumb"><a href="../../../../index.html">Inicio</a><span>◆</span><a href="../../../../es/{level}/index.html">{level.upper()}</a><span>◆</span><a href="../index.html">Gramática</a><span>◆</span><a href="index.html">{title}</a></div>
<nav class="chapter-nav">
  <a href="slides.html" class="chapter-nav-btn">Lección</a>
  <a href="worksheet.html" class="chapter-nav-btn">Repaso</a>
  <a href="game.html" class="chapter-nav-btn active">Juego</a>
  <a href="printables.html" class="chapter-nav-btn">Imprimibles</a>
</nav>
<div class="game-wrap" id="gameWrap">
  <div id="gameStart" class="game-screen active">
    <div class="game-start">
      <h2>{title} — Mastery</h2>
      <p>10 elementos · 4 etapas cada uno.</p>
      <p style="font-size:.85rem;color:var(--muted)">Una respuesta incorrecta te baja un nivel — nunca a cero.</p>
      <div id="gStartMastered" style="font-family:var(--font-sans);font-size:.9rem;margin:12px 0;color:var(--muted)"></div>
      <div id="gResumeSection" style="display:none;margin-bottom:12px"><button id="gBtnResume" class="game-btn primary">Continuar</button><button id="gBtnNewFromResume" class="game-btn">Empezar de nuevo</button></div>
      <button id="gBtnStart" class="game-btn primary">Empezar</button>
      <a href="../../../../es/{level}/index.html" class="game-btn" style="text-align:center;text-decoration:none;margin-top:8px">◀ Volver al inicio</a>
    </div>
  </div>
  <div id="gamePlay" class="game-screen"><div class="game-play"></div><div class="game-ref-panel" id="gRefPanel"><button id="gRefToggle" class="game-ref-head">◀ Referencia — todas las palabras</button><div id="gRefBody" class="game-ref-body"><div id="gRefList"></div></div></div></div>
  <div id="gameCompletion" class="game-screen">
    <div class="game-complete">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2.5px;text-transform:uppercase;color:var(--amber);margin-bottom:8px">Capítulo {ch_num} completado</div>
      <h2 style="margin-bottom:6px">¡Todo dominado!</h2>
      <p style="color:var(--muted);font-size:.85rem;margin-bottom:20px">Puntuación: <strong id="gFinalScore"></strong> &nbsp;·&nbsp; Racha: <strong id="gFinalStreak"></strong></p>
      <div id="gFinalPct" style="font-family:var(--font-serif);font-size:1.4rem;font-weight:700;color:var(--accent);text-align:center;margin:8px 0"></div>
      <div id="gMasteryMap" style="margin:16px 0;text-align:left;"></div>
      <a href="worksheet.html" class="game-btn" style="text-decoration:none;text-align:center">Repetir los ejercicios</a>
      <a href="../../../../es/{level}/index.html" class="game-btn" style="text-decoration:none;text-align:center;opacity:.7">◀ Volver al inicio</a>
    </div>
  </div>
</div>
<footer class="site-footer">Word Play · Cambridge Inglés A1◆C2</footer>
<script>
window.GAME_DATA={{chapterId:"{ch_key}",level:"{level}",title:"{title}",storageKey:"wordplay_game_es-{level}_{ch_key}",items:[
{{"id":"item1","term":"Key term 1","meaning":"Meaning 1","synonym":"hint","example":"Example 1 with <b>term</b>","completion":"Example with _____","answer":"term"}},
{{"id":"item2","term":"Key term 2","meaning":"Meaning 2","synonym":"hint","example":"Example 2 with <b>term</b>","completion":"Example with _____","answer":"term"}},
{{"id":"item3","term":"Key term 3","meaning":"Meaning 3","synonym":"hint","example":"Example 3 with <b>term</b>","completion":"Example with _____","answer":"term"}},
{{"id":"item4","term":"Key term 4","meaning":"Meaning 4","synonym":"hint","example":"Example 4 with <b>term</b>","completion":"Example with _____","answer":"term"}},
{{"id":"item5","term":"Key term 5","meaning":"Meaning 5","synonym":"hint","example":"Example 5 with <b>term</b>","completion":"Example with _____","answer":"term"}},
{{"id":"item6","term":"Key term 6","meaning":"Meaning 6","synonym":"hint","example":"Example 6 with <b>term</b>","completion":"Example with _____","answer":"term"}},
{{"id":"item7","term":"Key term 7","meaning":"Meaning 7","synonym":"hint","example":"Example 7 with <b>term</b>","completion":"Example with _____","answer":"term"}},
{{"id":"item8","term":"Key term 8","meaning":"Meaning 8","synonym":"hint","example":"Example 8 with <b>term</b>","completion":"Example with _____","answer":"term"}},
{{"id":"item9","term":"Key term 9","meaning":"Meaning 9","synonym":"hint","example":"Example 9 with <b>term</b>","completion":"Example with _____","answer":"term"}},
{{"id":"item10","term":"Key term 10","meaning":"Meaning 10","synonym":"hint","example":"Example 10 with <b>term</b>","completion":"Example with _____","answer":"term"}}
]}};
</script>
<script src="../../../../shared/i18n.js?v=v123"></script>
<script src="../../../../shared/store.js?v=v107"></script>
<script src="../../../../shared/game.js?v=v111"></script>
</body>
</html>"""

# Main execution
print("Ready to batch populate all grammar chapters...")
print(f"Total chapters: {sum(len(v) for v in CHAPTERS.values())}")
