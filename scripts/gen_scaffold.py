#!/usr/bin/env python3
"""
Scaffold generator for new course tracks.
Creates placeholder HTML files for espanol-en/ and espanol/ tracks.
Run from repo root: python3 scripts/gen_scaffold.py

Placeholder files contain <!-- PLACEHOLDER --> so gen_coverage.py detects them as stubs.
All pages pass check_structure.py (breadcrumb, footer, favicon, base.css).
"""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WP_LOGO = '<svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px"><rect width="32" height="32" rx="4" fill="currentColor"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>'

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  wrote {path.replace(BASE+'/', '')}")

def depth_prefix(depth):
    return '../' * depth

# ─── espanol-en data ───────────────────────────────────────────────────────────

ESPANOL_EN_GRAMMAR_A1 = [
    ('ser-estar',           'Ser & Estar',             'The two "to be" verbs — permanent vs temporary'),
    ('present-tense',       'Present Tense',            'Regular -ar/-er/-ir verb conjugations'),
    ('articles',            'Articles',                 'el/la/los/las · un/una — definite & indefinite'),
    ('pronouns',            'Subject Pronouns',         'yo, tú, él, ella, nosotros, vosotros, ellos'),
    ('tener',               'Tener — to have',          'Possession, age, and fixed expressions'),
    ('numbers-time',        'Numbers & Time',           'Counting · telling the time · days & months'),
    ('demonstratives',      'Demonstratives',           'este / ese / aquel — this, that, those'),
    ('adjective-agreement', 'Adjective Agreement',      'Gender and number agreement with nouns'),
    ('question-words',      'Question Words',           'qué, cómo, dónde, cuándo, quién, cuánto'),
    ('negation',            'Negation',                 'no, nunca, tampoco — saying no in Spanish'),
    ('hay',                 'Hay',                      'There is / there are — hay + noun'),
    ('prepositions-place',  'Prepositions of Place',    'en, sobre, debajo, delante, detrás, entre'),
    ('prepositions-time',   'Prepositions of Time',     'a las, el, los, en, por, durante'),
    ('present-progressive', 'Present Progressive',      'estar + gerundio — I am doing / estoy haciendo'),
    ('gustar',              'Gustar',                   'me gusta / me gustan — expressing likes'),
    ('ser-estar-uses',      'Ser vs Estar in Depth',    'When to use each: identity, description, state'),
    ('ir-a-future',         'Ir a + Infinitive',        'voy a comer — talking about near future plans'),
    ('reflexive-verbs',     'Reflexive Verbs',          'levantarse, llamarse — actions you do to yourself'),
    ('regular-verbs-ar',    'Regular -ar Verbs',        'hablar, trabajar, escuchar — full paradigm'),
    ('regular-verbs-er-ir', 'Regular -er / -ir Verbs',  'comer, vivir, leer — contrasting the endings'),
    ('basic-commands',      'Basic Commands',           'Imperativo — ven aquí, escucha, abre el libro'),
    ('adverbs-frequency',   'Adverbs of Frequency',     'siempre, normalmente, a veces, nunca'),
    ('past-tense-regular',  'Past Tense — Regular',     'hablé, comí, viví — pretérito indefinido'),
    ('past-tense-irregular','Past Tense — Irregular',   'fui, tuve, hice — the most common irregulars'),
]

ESPANOL_EN_VOCAB_A1 = [
    ('numbers-and-time',   'Numbers & Time',       '1–100, days, months, seasons, telling the time'),
    ('colours',            'Colours',              'Basic colour vocabulary + shades'),
    ('family',             'Family',               'Parents, siblings, relatives and family verbs'),
    ('animals',            'Animals',              'Common animals — pets, farm and wild'),
    ('food-and-drink',     'Food & Drink',         'Common foods, drinks and restaurant vocabulary'),
    ('clothes',            'Clothes',              'Clothing items and getting dressed'),
    ('daily-routines',     'Daily Routines',       'Daily action verbs — morning, afternoon, evening'),
    ('places-in-town',     'Places in Town',       'la tienda, el banco, la farmacia, el mercado'),
    ('body',               'The Body',             'Head, torso, limbs — body part vocabulary'),
    ('house-and-home',     'House & Home',         'Rooms, furniture and household items'),
    ('adjectives-feelings','Adjectives & Feelings','cansado, feliz, triste, enfadado, aburrido'),
    ('jobs-and-occupations','Jobs & Occupations',  'médico, profesor, cocinero, dependiente'),
]

ESPANOL_EN_WRITING_A1 = [
    ('personal-introduction','Personal Introduction','Write a short introduction about yourself'),
    ('form-filling',         'Form Filling',         'Complete a form with personal details'),
    ('short-message',        'Short Message',        'Write a brief informal message or note'),
]

LEVELS = ['a1','a2','b1','b2','c1','c2']
LEVEL_NAMES = {'a1':'Beginner','a2':'Elementary','b1':'Intermediate',
               'b2':'Upper Intermediate','c1':'Advanced','c2':'Mastery'}
LEVEL_NAMES_ES = {'a1':'Principiante','a2':'Elemental','b1':'Intermedio',
                  'b2':'Intermedio Alto','c1':'Avanzado','c2':'Maestría'}

# ─── shared header/footer helpers ─────────────────────────────────────────────

def page_header(depth, lang='en', dark_label='Dark', back_href=None, back_label=None):
    pre = depth_prefix(depth)
    back = f'<a href="{back_href}" class="back back-link" aria-label="{back_label}"></a>' if back_href else '<span></span>'
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{pre}favicon.svg" type="image/svg+xml">
'''

def site_header(depth, dark_label='Dark', back_href='', back_label='Back'):
    pre = depth_prefix(depth)
    return f'''<header class="site-header"><div class="site-header-inner">
  <a href="{back_href}" class="back back-link" aria-label="{back_label}"></a>
  <a href="{pre}index.html" class="brand">{WP_LOGO}Word Play</a>
  <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">&#9680; {dark_label}</button>
</div></header>
'''

# ─── espanol-en track hub ──────────────────────────────────────────────────────

def gen_espanol_en_hub():
    pre = depth_prefix(1)
    path = os.path.join(BASE, 'espanol-en', 'index.html')
    content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<title>Word Play — Spanish Course for English Speakers</title>
<link rel="stylesheet" href="../shared/base.css?v=v123">
<script src="../shared/dark-init.js?v=v109"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="../index.html" class="back back-link">Back to English</a>
  <a href="../index.html" class="brand">{WP_LOGO}Word Play</a>
  <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">&#9680; Dark</button>
</div></header>

<div class="section-page" style="max-width:800px;margin:0 auto;padding:40px 20px">
  <div style="text-align:center;margin-bottom:40px">
    <div style="font-family:var(--font-sans);font-size:.65rem;font-weight:800;letter-spacing:2.5px;text-transform:uppercase;color:var(--amber);margin-bottom:12px">FOR ENGLISH SPEAKERS</div>
    <h1 style="font-family:Georgia,serif;font-size:2.8rem;font-weight:700;color:var(--ink);margin:0 0 12px;line-height:1.1">Learn Spanish</h1>
    <p style="color:var(--muted);font-size:1rem;margin:0 0 32px;line-height:1.6">Complete Spanish course (A1 to C2) designed for native English speakers. Grammar explained in English, with interference notes, false friends, and full DELE exam preparation.</p>
  </div>

  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px;margin-bottom:40px">
    <a href="a1/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">LEVEL A1</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">Beginner</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">Grammar &middot; Vocabulary &middot; Writing &middot; 24 chapters</div>
    </a>
    <a href="a2/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">LEVEL A2</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">Elementary</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">Coming soon &mdash; stub chapters</div>
    </a>
    <a href="b1/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">LEVEL B1</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">Intermediate</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">Coming soon &mdash; stub chapters</div>
    </a>
    <a href="b2/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">LEVEL B2</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">Upper Intermediate</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">Coming soon &mdash; stub chapters</div>
    </a>
    <a href="c1/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">LEVEL C1</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">Advanced</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">Coming soon &mdash; stub chapters</div>
    </a>
    <a href="c2/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">LEVEL C2</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">Mastery</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">Coming soon &mdash; stub chapters</div>
    </a>
    <a href="exams/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">EXAMS</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">DELE Exam Prep</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">A1 &middot; A2 &middot; B1 &middot; B2 &middot; C1 &middot; C2</div>
    </a>
  </div>

  <div style="background:var(--cream-deep);border-radius:10px;padding:28px;margin-bottom:32px">
    <h2 style="font-family:Georgia,serif;font-size:1.3rem;font-weight:700;color:var(--ink);margin:0 0 12px">What&#8217;s included?</h2>
    <p style="color:var(--muted);font-size:.88rem;line-height:1.6;margin:0 0 12px">Full Spanish course for English speakers, with English-language scaffolding:</p>
    <p style="color:var(--ink);font-size:.88rem;line-height:1.8;margin:0">
      Grammar explanations <strong>in English</strong> alongside the Spanish.<br>
      <strong>False friends</strong> (embarazada &#8800; embarrassed, actualmente &#8800; actually).<br>
      English interference notes — where English habits trip up Spanish learners.<br>
      <strong>Ser vs Estar</strong>, subjunctive, por vs para — the classic sticking points.<br>
      Pronunciation contrasts: sounds that don&#8217;t exist in English.<br>
      Preparation for <strong>DELE</strong> (A1&#8211;C2, Instituto Cervantes).
    </p>
  </div>

  <div style="text-align:center;padding:20px 0">
    <p style="color:var(--muted);font-size:.85rem;margin-bottom:16px">Want the English course instead?</p>
    <a href="../index.html" style="display:inline-block;padding:13px 32px;background:var(--amber);color:#1A1A1A;font-family:var(--font-sans);font-size:.8rem;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;border-radius:5px">Go to English Course</a>
  </div>
</div>

<footer class="site-footer">Word Play &middot; Spanish A1&#8211;C2 &middot; For English Speakers</footer>
</body>
</html>'''
    write(path, content)

# ─── espanol-en level hub ──────────────────────────────────────────────────────

def gen_espanol_en_level(level):
    name = LEVEL_NAMES[level]
    sections_html = ''
    if level == 'a1':
        sections_html = f'''    <a href="grammar/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:8px">GRAMMAR</div>
      <div style="font-family:Georgia,serif;font-size:1.3rem;font-weight:700;color:white;margin-bottom:6px">Spanish Grammar {level.upper()}</div>
      <div style="font-family:var(--font-sans);font-size:.78rem;color:rgba(255,255,255,.55);line-height:1.5;margin-bottom:16px">Ser/Estar &middot; Present &middot; Past &middot; 24 chapters</div>
      <div style="font-family:var(--font-sans);font-size:.7rem;font-weight:700;color:var(--amber);letter-spacing:.5px">Study &#8594;</div>
    </a>
    <a href="vocabulary/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:8px">VOCABULARY</div>
      <div style="font-family:Georgia,serif;font-size:1.3rem;font-weight:700;color:white;margin-bottom:6px">Spanish Vocabulary {level.upper()}</div>
      <div style="font-family:var(--font-sans);font-size:.78rem;color:rgba(255,255,255,.55);line-height:1.5;margin-bottom:16px">Animals &middot; Food &middot; Family &middot; 12 topics</div>
      <div style="font-family:var(--font-sans);font-size:.7rem;font-weight:700;color:var(--amber);letter-spacing:.5px">Study &#8594;</div>
    </a>
    <a href="writing/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:8px">WRITING</div>
      <div style="font-family:Georgia,serif;font-size:1.3rem;font-weight:700;color:white;margin-bottom:6px">Spanish Writing {level.upper()}</div>
      <div style="font-family:var(--font-sans);font-size:.78rem;color:rgba(255,255,255,.55);line-height:1.5;margin-bottom:16px">3 tasks &middot; Introduction &middot; Form &middot; Message</div>
      <div style="font-family:var(--font-sans);font-size:.7rem;font-weight:700;color:var(--amber);letter-spacing:.5px">Study &#8594;</div>
    </a>'''
    else:
        sections_html = f'''    <div class="sect-card" style="opacity:.55;cursor:default">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:8px">COMING SOON</div>
      <div style="font-family:Georgia,serif;font-size:1.3rem;font-weight:700;color:white;margin-bottom:6px">{level.upper()} Content</div>
      <div style="font-family:var(--font-sans);font-size:.78rem;color:rgba(255,255,255,.55);line-height:1.5;margin-bottom:16px">Grammar &middot; Vocabulary &middot; Writing &mdash; being built</div>
      <div style="font-family:var(--font-sans);font-size:.7rem;font-weight:700;color:var(--amber);letter-spacing:.5px"><!-- PLACEHOLDER --></div>
    </div>'''

    path = os.path.join(BASE, 'espanol-en', level, 'index.html')
    content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<title>{level.upper()} {name} — Word Play Spanish for English Speakers</title>
<link rel="stylesheet" href="../../shared/base.css?v=v123">
<script src="../../shared/dark-init.js?v=v109"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="../index.html" class="back back-link" aria-label="Back"></a>
  <a href="../../index.html" class="brand">{WP_LOGO}Word Play</a>
  <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">&#9680; Dark</button>
</div></header>
<div class="section-page">
  <div class="breadcrumb">
    <a href="../../index.html">Home</a><span>&#8250;</span>
    <a href="../index.html">Spanish for English Speakers</a><span>&#8250;</span>
    <strong>{level.upper()} {name}</strong>
  </div>
  <div class="eyebrow">LEVEL {level.upper()} &middot; SPANISH FOR ENGLISH SPEAKERS</div>
  <h1>{level.upper()} &mdash; {name}</h1>
  <p class="section-desc">Spanish grammar &middot; Vocabulary &middot; Writing &mdash; all explained in English</p>
  <div class="ch-grid">
{sections_html}
  </div>
</div>
<footer class="site-footer">Word Play &middot; Spanish {level.upper()}&#8211;C2 &middot; For English Speakers</footer>
</body>
</html>'''
    write(path, content)

# ─── espanol-en section indexes ───────────────────────────────────────────────

def gen_espanol_en_grammar_index():
    cards = ''
    for i, (slug, title, desc) in enumerate(ESPANOL_EN_GRAMMAR_A1, 1):
        cards += f'''    <a href="{slug}/index.html" class="ch-card ch-card--grammar" id="gpc_espanol-en-a1_{slug}">
      <div class="ch-num">Ch. {i}</div>
      <h2>{title}</h2>
      <p class="ch-desc">{desc}</p><span class="ch-cta">Study &#8594;</span>
    </a>
'''
    path = os.path.join(BASE, 'espanol-en', 'a1', 'grammar', 'index.html')
    content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../favicon.svg" type="image/svg+xml">
<title>A1 Spanish Grammar — Word Play for English Speakers</title>
<link rel="stylesheet" href="../../../shared/base.css?v=v123">
<script src="../../../shared/dark-init.js?v=v109"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="../index.html" class="back back-link" aria-label="Back"></a>
  <a href="../../../index.html" class="brand">{WP_LOGO}Word Play</a>
  <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">&#9680; Dark</button>
</div></header>
<div class="section-page">
  <div class="breadcrumb">
    <a href="../../../index.html">Home</a><span>&#8250;</span>
    <a href="../../index.html">Spanish for English Speakers</a><span>&#8250;</span>
    <a href="../index.html">A1</a><span>&#8250;</span>
    <strong>Grammar</strong>
  </div>
  <div class="eyebrow">A1 &middot; GRAMMAR &middot; FOR ENGLISH SPEAKERS</div>
  <h1>Spanish Grammar A1</h1>
  <p class="section-desc">English explanations &middot; Interference notes &middot; English-Spanish comparison</p>
  <div class="ch-grid">
{cards}  </div>
</div>
<footer class="site-footer">Word Play &middot; Spanish A1&#8211;C2 &middot; For English Speakers</footer>
</body>
</html>'''
    write(path, content)

def gen_espanol_en_vocab_index():
    cards = ''
    for i, (slug, title, desc) in enumerate(ESPANOL_EN_VOCAB_A1, 1):
        cards += f'''    <a href="{slug}/index.html" class="ch-card ch-card--vocab" id="vpc_espanol-en-a1_{slug}">
      <div class="ch-num">V{i}</div>
      <h2>{title}</h2>
      <p class="ch-desc">{desc}</p><span class="ch-cta">Study &#8594;</span>
    </a>
'''
    path = os.path.join(BASE, 'espanol-en', 'a1', 'vocabulary', 'index.html')
    content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../favicon.svg" type="image/svg+xml">
<title>A1 Spanish Vocabulary — Word Play for English Speakers</title>
<link rel="stylesheet" href="../../../shared/base.css?v=v123">
<script src="../../../shared/dark-init.js?v=v109"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="../index.html" class="back back-link" aria-label="Back"></a>
  <a href="../../../index.html" class="brand">{WP_LOGO}Word Play</a>
  <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">&#9680; Dark</button>
</div></header>
<div class="section-page">
  <div class="breadcrumb">
    <a href="../../../index.html">Home</a><span>&#8250;</span>
    <a href="../../index.html">Spanish for English Speakers</a><span>&#8250;</span>
    <a href="../index.html">A1</a><span>&#8250;</span>
    <strong>Vocabulary</strong>
  </div>
  <div class="eyebrow">A1 &middot; VOCABULARY</div>
  <h1>Spanish Vocabulary A1</h1>
  <p class="section-desc">12 topics &middot; Flashcards &middot; Lesson &middot; Game</p>
  <div class="ch-grid">
{cards}  </div>
</div>
<footer class="site-footer">Word Play &middot; Spanish A1&#8211;C2 &middot; For English Speakers</footer>
</body>
</html>'''
    write(path, content)

def gen_espanol_en_writing_index():
    cards = ''
    for i, (slug, title, desc) in enumerate(ESPANOL_EN_WRITING_A1, 1):
        cards += f'''    <a href="{slug}/index.html" class="ch-card ch-card--writing" id="wpc_espanol-en-a1_{slug}">
      <div class="ch-num">W{i}</div>
      <h2>{title}</h2>
      <p class="ch-desc">{desc}</p><span class="ch-cta">Study &#8594;</span>
    </a>
'''
    path = os.path.join(BASE, 'espanol-en', 'a1', 'writing', 'index.html')
    content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../favicon.svg" type="image/svg+xml">
<title>A1 Spanish Writing — Word Play for English Speakers</title>
<link rel="stylesheet" href="../../../shared/base.css?v=v123">
<script src="../../../shared/dark-init.js?v=v109"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="../index.html" class="back back-link" aria-label="Back"></a>
  <a href="../../../index.html" class="brand">{WP_LOGO}Word Play</a>
  <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">&#9680; Dark</button>
</div></header>
<div class="section-page">
  <div class="breadcrumb">
    <a href="../../../index.html">Home</a><span>&#8250;</span>
    <a href="../../index.html">Spanish for English Speakers</a><span>&#8250;</span>
    <a href="../index.html">A1</a><span>&#8250;</span>
    <strong>Writing</strong>
  </div>
  <div class="eyebrow">A1 &middot; WRITING</div>
  <h1>Spanish Writing A1</h1>
  <p class="section-desc">3 tasks &middot; Worksheet &middot; Game &middot; Printable</p>
  <div class="ch-grid">
{cards}  </div>
</div>
<footer class="site-footer">Word Play &middot; Spanish A1&#8211;C2 &middot; For English Speakers</footer>
</body>
</html>'''
    write(path, content)

# ─── espanol-en chapter files ──────────────────────────────────────────────────

def placeholder_slide(title, track, level, section, slug, depth=4):
    pre = depth_prefix(depth)
    # Lesson slides must CTA to the next activity (pedagogy_check):
    # vocab → game.html, grammar/writing → worksheet.html
    if section == 'vocabulary':
        next_activity, next_label = 'game.html', 'Mastery Game'
    else:
        next_activity, next_label = 'worksheet.html', 'Practice'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{pre}favicon.svg" type="image/svg+xml">
<title>{title} — {level.upper()} {section.title()} | Word Play</title>
<link rel="stylesheet" href="{pre}shared/base.css?v=v123">
<link rel="stylesheet" href="{pre}shared/slides.css?v=v115">
<script src="{pre}shared/dark-init.js?v=v109"></script>
</head>
<body class="deck-body">
<div class="deck-progress"><div class="deck-progress-fill" id="deck-progress-fill"></div></div>
<header class="site-header"><div class="site-header-inner">
  <a href="index.html" class="back back-link" aria-label="Back"></a>
  <a href="{pre}index.html" class="brand">{WP_LOGO}Word Play</a>
  <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">&#9680; Dark</button>
</div></header>
<div class="breadcrumb">
  <a href="{pre}index.html">Home</a><span>&#8250;</span>
  <a href="{pre}{track}/index.html">Spanish</a><span>&#8250;</span>
  <a href="{pre}{track}/{level}/index.html">{level.upper()}</a><span>&#8250;</span>
  <a href="../index.html">{section.title()}</a><span>&#8250;</span>
  <a href="index.html">{title}</a><span>&#8250;</span>
  <strong>Lesson</strong>
</div>
<!-- PLACEHOLDER -->
<div class="slide active" style="padding:40px;text-align:center">
  <h1 style="font-family:Georgia,serif;color:var(--ink)">{title}</h1>
  <p style="color:var(--muted)">Content coming soon &mdash; use AI Prompts to bootstrap this chapter.</p>
  <p style="margin-top:24px"><a href="{next_activity}" style="display:inline-block;padding:11px 24px;background:var(--amber);color:#fff;font-family:var(--font-sans);font-size:.78rem;font-weight:700;letter-spacing:.5px;text-decoration:none;border-radius:6px">{next_label} &#8594;</a></p>
</div>
<footer class="site-footer">Word Play &middot; Spanish {level.upper()} &middot; {section.title()}</footer>
<script src="{pre}shared/deck.js?v=v113"></script>
</body>
</html>'''

def placeholder_worksheet(title, track, level, section, slug, depth=4):
    pre = depth_prefix(depth)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{pre}favicon.svg" type="image/svg+xml">
<title>{title} — Practice | Word Play</title>
<link rel="stylesheet" href="{pre}shared/base.css?v=v123">
<script src="{pre}shared/dark-init.js?v=v109"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="index.html" class="back back-link" aria-label="Back"></a>
  <a href="{pre}index.html" class="brand">{WP_LOGO}Word Play</a>
  <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">&#9680; Dark</button>
</div></header>
<div class="section-page">
  <div class="breadcrumb">
    <a href="{pre}index.html">Home</a><span>&#8250;</span>
    <a href="{pre}{track}/{level}/index.html">{level.upper()}</a><span>&#8250;</span>
    <a href="../index.html">{section.title()}</a><span>&#8250;</span>
    <a href="index.html">{title}</a><span>&#8250;</span>
    <strong>Practice</strong>
  </div>
  <!-- PLACEHOLDER -->
  <h1>{title} &mdash; Practice</h1>
  <p style="color:var(--muted)">Worksheet content coming soon.</p>
</div>
<footer class="site-footer">Word Play &middot; Spanish {level.upper()} &middot; Practice</footer>
<script src="{pre}shared/worksheet.js?v=v106"></script>
</body>
</html>'''

def placeholder_flashcards(title, track, level, slug, depth=4):
    pre = depth_prefix(depth)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{pre}favicon.svg" type="image/svg+xml">
<title>{title} — Flashcards | Word Play</title>
<link rel="stylesheet" href="{pre}shared/base.css?v=v123">
<script src="{pre}shared/dark-init.js?v=v109"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="index.html" class="back back-link" aria-label="Back"></a>
  <a href="{pre}index.html" class="brand">{WP_LOGO}Word Play</a>
  <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">&#9680; Dark</button>
</div></header>
<div class="section-page">
  <div class="breadcrumb">
    <a href="{pre}index.html">Home</a><span>&#8250;</span>
    <a href="{pre}{track}/{level}/index.html">{level.upper()}</a><span>&#8250;</span>
    <a href="../index.html">Vocabulary</a><span>&#8250;</span>
    <a href="index.html">{title}</a><span>&#8250;</span>
    <strong>Flashcards</strong>
  </div>
  <!-- PLACEHOLDER -->
  <h1>{title} &mdash; Flashcards</h1>
  <p style="color:var(--muted)">Flashcard content coming soon.</p>
</div>
<footer class="site-footer">Word Play &middot; Spanish {level.upper()} &middot; Vocabulary</footer>
</body>
</html>'''

def placeholder_game(title, track, level, section, slug, depth=4):
    pre = depth_prefix(depth)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{pre}favicon.svg" type="image/svg+xml">
<title>{title} — Mastery Game | Word Play</title>
<link rel="stylesheet" href="{pre}shared/base.css?v=v123">
<script src="{pre}shared/dark-init.js?v=v109"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="index.html" class="back back-link" aria-label="Back"></a>
  <a href="{pre}index.html" class="brand">{WP_LOGO}Word Play</a>
  <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">&#9680; Dark</button>
</div></header>
<div class="section-page">
  <div class="breadcrumb">
    <a href="{pre}index.html">Home</a><span>&#8250;</span>
    <a href="{pre}{track}/{level}/index.html">{level.upper()}</a><span>&#8250;</span>
    <a href="../index.html">{section.title()}</a><span>&#8250;</span>
    <a href="index.html">{title}</a><span>&#8250;</span>
    <strong>Mastery Game</strong>
  </div>
  <!-- PLACEHOLDER -->
  <h1>{title} &mdash; Mastery Game</h1>
  <p style="color:var(--muted)">Game content coming soon.</p>
</div>
<footer class="site-footer">Word Play &middot; Spanish {level.upper()} &middot; Game</footer>
<script src="{pre}shared/game.js?v=v110"></script>
</body>
</html>'''

def placeholder_printables(title, track, level, slug, depth=4):
    pre = depth_prefix(depth)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{pre}favicon.svg" type="image/svg+xml">
<title>{title} — Printables | Word Play</title>
<link rel="stylesheet" href="{pre}shared/base.css?v=v123">
<script src="{pre}shared/dark-init.js?v=v109"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="index.html" class="back back-link" aria-label="Back"></a>
  <a href="{pre}index.html" class="brand">{WP_LOGO}Word Play</a>
  <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">&#9680; Dark</button>
</div></header>
<div class="section-page">
  <div class="breadcrumb">
    <a href="{pre}index.html">Home</a><span>&#8250;</span>
    <a href="{pre}{track}/{level}/index.html">{level.upper()}</a><span>&#8250;</span>
    <a href="../index.html">Writing</a><span>&#8250;</span>
    <a href="index.html">{title}</a><span>&#8250;</span>
    <strong>Printables</strong>
  </div>
  <!-- PLACEHOLDER -->
  <h1>{title} &mdash; Printables</h1>
  <p style="color:var(--muted)">Printable content coming soon.</p>
</div>
<footer class="site-footer">Word Play &middot; Spanish {level.upper()} &middot; Writing</footer>
</body>
</html>'''

def chapter_index(slug, title, desc, track, level, section, chapter_num, depth=4):
    pre = depth_prefix(depth)
    if section == 'grammar':
        num_label = f'Chapter {chapter_num} &middot; Grammar'
        activities = f'''    <a href="slides.html" class="activity-card" data-activity="lesson">
      <span class="ac-title">Lesson</span>
      <p class="ac-desc">Full explanation with examples and English comparisons</p>
      <span class="ac-arrow">&#8594;</span>
    </a>
    <a href="worksheet.html" class="activity-card" data-activity="practice">
      <span class="ac-title">Practice</span>
      <p class="ac-desc">Interactive exercises with immediate feedback</p>
      <span class="ac-arrow">&#8594;</span>
    </a>
    <a href="game.html" class="activity-card" data-activity="game">
      <span class="ac-title">Mastery Game</span>
      <p class="ac-desc">4-stage game to lock the grammar into memory</p>
      <span class="ac-arrow">&#8594;</span>
    </a>'''
    elif section == 'vocabulary':
        num_label = f'V{chapter_num} &middot; 10 words'
        activities = f'''    <a href="slides.html" class="activity-card" data-activity="lesson">
      <span class="ac-title">Lesson</span>
      <p class="ac-desc">Study the words with translations and example sentences</p>
      <span class="ac-arrow">&#8594;</span>
    </a>
    <a href="flashcards.html" class="activity-card" data-activity="practice">
      <span class="ac-title">Flashcards &amp; Match</span>
      <p class="ac-desc">Flip cards, then match words with definitions</p>
      <span class="ac-arrow">&#8594;</span>
    </a>
    <a href="game.html" class="activity-card" data-activity="game">
      <span class="ac-title">Mastery Game</span>
      <p class="ac-desc">4-stage game to lock the vocabulary into memory</p>
      <span class="ac-arrow">&#8594;</span>
    </a>'''
    else:  # writing
        num_label = f'W{chapter_num} &middot; Writing task'
        activities = f'''    <a href="slides.html" class="activity-card" data-activity="lesson">
      <span class="ac-title">Model Text</span>
      <p class="ac-desc">Read a model answer and analyse the structure</p>
      <span class="ac-arrow">&#8594;</span>
    </a>
    <a href="worksheet.html" class="activity-card" data-activity="practice">
      <span class="ac-title">Practice</span>
      <p class="ac-desc">Guided writing exercises with sentence starters</p>
      <span class="ac-arrow">&#8594;</span>
    </a>
    <a href="game.html" class="activity-card" data-activity="game">
      <span class="ac-title">Mastery Game</span>
      <p class="ac-desc">Vocabulary and phrases from this writing type</p>
      <span class="ac-arrow">&#8594;</span>
    </a>
    <a href="printables.html" class="activity-card" data-activity="print">
      <span class="ac-title">Printable</span>
      <p class="ac-desc">Print-ready version for classroom use</p>
      <span class="ac-arrow">&#8594;</span>
    </a>'''

    section_title = {'grammar':'Grammar','vocabulary':'Vocabulary','writing':'Writing'}[section]
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{pre}favicon.svg" type="image/svg+xml">
<title>{title} &mdash; {section_title} {level.upper()} | Word Play</title>
<link rel="stylesheet" href="{pre}shared/base.css?v=v123">
<script src="{pre}shared/dark-init.js?v=v109"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="../index.html" class="back back-link" aria-label="Back"></a>
  <a href="{pre}index.html" class="brand">{WP_LOGO}Word Play</a>
  <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">&#9680; Dark</button>
</div></header>
<div class="section-page">
  <div class="breadcrumb">
    <a href="{pre}index.html">Home</a><span>&#8250;</span>
    <a href="{pre}{track}/{level}/index.html">{level.upper()}</a><span>&#8250;</span>
    <a href="../index.html">{section_title}</a><span>&#8250;</span>
    <strong>{title}</strong>
  </div>
  <div class="chapter-num">{num_label}</div>
  <h1 class="chapter-h1">{title}</h1>
  <div class="activity-grid">
{activities}
  </div>
</div>
<footer class="site-footer">Word Play &middot; Spanish {level.upper()} &middot; {section_title}</footer>
<script src="{pre}shared/store.js?v=v105"></script>
</body>
</html>'''

def gen_espanol_en_grammar_chapters():
    for i, (slug, title, desc) in enumerate(ESPANOL_EN_GRAMMAR_A1, 1):
        base_path = os.path.join(BASE, 'espanol-en', 'a1', 'grammar', slug)
        write(os.path.join(base_path, 'index.html'),
              chapter_index(slug, title, desc, 'espanol-en', 'a1', 'grammar', i))
        write(os.path.join(base_path, 'slides.html'),
              placeholder_slide(title, 'espanol-en', 'a1', 'grammar', slug))
        write(os.path.join(base_path, 'worksheet.html'),
              placeholder_worksheet(title, 'espanol-en', 'a1', 'grammar', slug))
        write(os.path.join(base_path, 'game.html'),
              placeholder_game(title, 'espanol-en', 'a1', 'grammar', slug))

def gen_espanol_en_vocab_chapters():
    for i, (slug, title, desc) in enumerate(ESPANOL_EN_VOCAB_A1, 1):
        base_path = os.path.join(BASE, 'espanol-en', 'a1', 'vocabulary', slug)
        write(os.path.join(base_path, 'index.html'),
              chapter_index(slug, title, desc, 'espanol-en', 'a1', 'vocabulary', i))
        write(os.path.join(base_path, 'slides.html'),
              placeholder_slide(title, 'espanol-en', 'a1', 'vocabulary', slug))
        write(os.path.join(base_path, 'flashcards.html'),
              placeholder_flashcards(title, 'espanol-en', 'a1', slug))
        write(os.path.join(base_path, 'game.html'),
              placeholder_game(title, 'espanol-en', 'a1', 'vocabulary', slug))

def gen_espanol_en_writing_chapters():
    for i, (slug, title, desc) in enumerate(ESPANOL_EN_WRITING_A1, 1):
        base_path = os.path.join(BASE, 'espanol-en', 'a1', 'writing', slug)
        write(os.path.join(base_path, 'index.html'),
              chapter_index(slug, title, desc, 'espanol-en', 'a1', 'writing', i))
        write(os.path.join(base_path, 'slides.html'),
              placeholder_slide(title, 'espanol-en', 'a1', 'writing', slug))
        write(os.path.join(base_path, 'worksheet.html'),
              placeholder_worksheet(title, 'espanol-en', 'a1', 'writing', slug))
        write(os.path.join(base_path, 'game.html'),
              placeholder_game(title, 'espanol-en', 'a1', 'writing', slug))
        write(os.path.join(base_path, 'printables.html'),
              placeholder_printables(title, 'espanol-en', 'a1', slug))

# ─── espanol-en exams hub ──────────────────────────────────────────────────────

def gen_espanol_en_exams():
    path = os.path.join(BASE, 'espanol-en', 'exams', 'index.html')
    content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<title>DELE Exam Preparation — Word Play Spanish</title>
<link rel="stylesheet" href="../../shared/base.css?v=v123">
<script src="../../shared/dark-init.js?v=v109"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="../index.html" class="back back-link" aria-label="Back"></a>
  <a href="../../index.html" class="brand">{WP_LOGO}Word Play</a>
  <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">&#9680; Dark</button>
</div></header>
<div class="section-page">
  <div class="breadcrumb">
    <a href="../../index.html">Home</a><span>&#8250;</span>
    <a href="../index.html">Spanish for English Speakers</a><span>&#8250;</span>
    <strong>DELE Exam Prep</strong>
  </div>
  <div class="eyebrow">DELE &middot; EXAM PREPARATION</div>
  <h1>DELE Exam Preparation</h1>
  <p class="section-desc">Instituto Cervantes official Spanish proficiency examinations &mdash; A1 to C2</p>
  <div class="ch-grid">
    <div class="sect-card" style="opacity:.55;cursor:default">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">DELE A1</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">DELE A1</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)"><!-- PLACEHOLDER --> Coming soon</div>
    </div>
    <div class="sect-card" style="opacity:.55;cursor:default">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">DELE A2</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">DELE A2</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">Coming soon</div>
    </div>
    <div class="sect-card" style="opacity:.55;cursor:default">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">DELE B1</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">DELE B1</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">Coming soon</div>
    </div>
    <div class="sect-card" style="opacity:.55;cursor:default">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">DELE B2</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">DELE B2</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">Coming soon &mdash; Niamh&#8217;s target exam</div>
    </div>
    <div class="sect-card" style="opacity:.55;cursor:default">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">DELE C1</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">DELE C1</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">Coming soon</div>
    </div>
    <div class="sect-card" style="opacity:.55;cursor:default">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">DELE C2</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">DELE C2</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">Coming soon</div>
    </div>
  </div>
</div>
<footer class="site-footer">Word Play &middot; DELE Exam Prep &middot; For English Speakers</footer>
</body>
</html>'''
    write(path, content)

# ─── espanol/ track (universal Spanish) ───────────────────────────────────────

def gen_espanol_hub():
    path = os.path.join(BASE, 'espanol', 'index.html')
    content = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<title>Word Play — Curso de Espa&#241;ol A1&#8211;C2</title>
<link rel="stylesheet" href="../shared/base.css?v=v123">
<script src="../shared/dark-init.js?v=v109"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="../index.html" class="back back-link">English</a>
  <a href="../index.html" class="brand">{WP_LOGO}Word Play</a>
  <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">&#9680; Dark</button>
</div></header>

<div class="section-page" style="max-width:800px;margin:0 auto;padding:40px 20px">
  <div style="text-align:center;margin-bottom:40px">
    <div style="font-family:var(--font-sans);font-size:.65rem;font-weight:800;letter-spacing:2.5px;text-transform:uppercase;color:var(--amber);margin-bottom:12px">CURSO UNIVERSAL</div>
    <h1 style="font-family:Georgia,serif;font-size:2.8rem;font-weight:700;color:var(--ink);margin:0 0 12px;line-height:1.1">Aprende Espa&#241;ol</h1>
    <p style="color:var(--muted);font-size:1rem;margin:0 0 32px;line-height:1.6">Curso completo de espa&#241;ol CEFR (A1 a C2) para cualquier estudiante, con preparaci&#243;n para los ex&#225;menes DELE del Instituto Cervantes.</p>
  </div>

  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px;margin-bottom:40px">
    <a href="a1/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">NIVEL A1</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">Principiante</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)"><!-- PLACEHOLDER --> En construcci&#243;n</div>
    </a>
    <a href="a2/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">NIVEL A2</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">Elemental</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">En construcci&#243;n</div>
    </a>
    <a href="b1/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">NIVEL B1</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">Intermedio</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">En construcci&#243;n</div>
    </a>
    <a href="b2/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">NIVEL B2</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">Intermedio Alto</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">En construcci&#243;n</div>
    </a>
    <a href="c1/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">NIVEL C1</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">Avanzado</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">En construcci&#243;n</div>
    </a>
    <a href="c2/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">NIVEL C2</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">Maestr&#237;a</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">En construcci&#243;n</div>
    </a>
    <a href="exams/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">EX&#193;MENES</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">Preparaci&#243;n DELE</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">A1 &middot; A2 &middot; B1 &middot; B2 &middot; C1 &middot; C2</div>
    </a>
  </div>

  <div style="text-align:center;padding:20px 0">
    <p style="color:var(--muted);font-size:.85rem;margin-bottom:16px">&#191;Hablas ingl&#233;s? Hay una versi&#243;n con explicaciones en ingl&#233;s:</p>
    <a href="../espanol-en/index.html" style="display:inline-block;padding:13px 32px;background:var(--amber);color:#1A1A1A;font-family:var(--font-sans);font-size:.8rem;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;border-radius:5px">Espa&#241;ol para anglohablantes</a>
  </div>
</div>

<footer class="site-footer">Word Play &middot; Espa&#241;ol A1&#8211;C2 &middot; Instituto Cervantes DELE</footer>
</body>
</html>'''
    write(path, content)

def gen_espanol_level(level):
    name = LEVEL_NAMES_ES[level]
    path = os.path.join(BASE, 'espanol', level, 'index.html')
    content = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<title>{level.upper()} {name} &mdash; Espa&#241;ol | Word Play</title>
<link rel="stylesheet" href="../../shared/base.css?v=v123">
<script src="../../shared/dark-init.js?v=v109"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="../index.html" class="back back-link" aria-label="Atr&#225;s"></a>
  <a href="../../index.html" class="brand">{WP_LOGO}Word Play</a>
  <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">&#9680; Dark</button>
</div></header>
<div class="section-page">
  <div class="breadcrumb">
    <a href="../../index.html">Inicio</a><span>&#8250;</span>
    <a href="../index.html">Espa&#241;ol</a><span>&#8250;</span>
    <strong>{level.upper()} {name}</strong>
  </div>
  <div class="eyebrow">NIVEL {level.upper()} &middot; ESPA&#209;OL</div>
  <h1>{level.upper()} &mdash; {name}</h1>
  <p class="section-desc"><!-- PLACEHOLDER --> Contenido en construcci&#243;n &mdash; pr&#243;ximamente</p>
  <div class="ch-grid">
    <div class="sect-card" style="opacity:.55;cursor:default">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:8px">GRAM&#193;TICA</div>
      <div style="font-family:Georgia,serif;font-size:1.3rem;font-weight:700;color:white;margin-bottom:6px">Gram&#225;tica {level.upper()}</div>
      <div style="font-family:var(--font-sans);font-size:.78rem;color:rgba(255,255,255,.55);line-height:1.5;margin-bottom:16px">En construcci&#243;n</div>
    </div>
    <div class="sect-card" style="opacity:.55;cursor:default">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:8px">VOCABULARIO</div>
      <div style="font-family:Georgia,serif;font-size:1.3rem;font-weight:700;color:white;margin-bottom:6px">Vocabulario {level.upper()}</div>
      <div style="font-family:var(--font-sans);font-size:.78rem;color:rgba(255,255,255,.55);line-height:1.5;margin-bottom:16px">En construcci&#243;n</div>
    </div>
  </div>
</div>
<footer class="site-footer">Word Play &middot; Espa&#241;ol {level.upper()}&#8211;C2</footer>
</body>
</html>'''
    write(path, content)

def gen_espanol_exams():
    path = os.path.join(BASE, 'espanol', 'exams', 'index.html')
    content = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<title>Preparaci&#243;n DELE &mdash; Word Play Espa&#241;ol</title>
<link rel="stylesheet" href="../../shared/base.css?v=v123">
<script src="../../shared/dark-init.js?v=v109"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="../index.html" class="back back-link" aria-label="Atr&#225;s"></a>
  <a href="../../index.html" class="brand">{WP_LOGO}Word Play</a>
  <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">&#9680; Dark</button>
</div></header>
<div class="section-page">
  <div class="breadcrumb">
    <a href="../../index.html">Inicio</a><span>&#8250;</span>
    <a href="../index.html">Espa&#241;ol</a><span>&#8250;</span>
    <strong>Ex&#225;menes DELE</strong>
  </div>
  <div class="eyebrow">DELE &middot; PREPARACI&#211;N</div>
  <h1>Preparaci&#243;n DELE</h1>
  <p class="section-desc">Ex&#225;menes oficiales del Instituto Cervantes &mdash; A1 a C2</p>
  <div class="ch-grid">
    <div class="sect-card" style="opacity:.55;cursor:default">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">DELE A1</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">DELE A1</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)"><!-- PLACEHOLDER --> Pr&#243;ximamente</div>
    </div>
    <div class="sect-card" style="opacity:.55;cursor:default">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">DELE A2</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">DELE A2</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">Pr&#243;ximamente</div>
    </div>
    <div class="sect-card" style="opacity:.55;cursor:default">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">DELE B1</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">DELE B1</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">Pr&#243;ximamente</div>
    </div>
    <div class="sect-card" style="opacity:.55;cursor:default">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">DELE B2</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">DELE B2</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">Pr&#243;ximamente</div>
    </div>
    <div class="sect-card" style="opacity:.55;cursor:default">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">DELE C1</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">DELE C1</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">Pr&#243;ximamente</div>
    </div>
    <div class="sect-card" style="opacity:.55;cursor:default">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">DELE C2</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">DELE C2</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">Pr&#243;ximamente</div>
    </div>
  </div>
</div>
<footer class="site-footer">Word Play &middot; DELE &middot; Instituto Cervantes</footer>
</body>
</html>'''
    write(path, content)

# ─── main ──────────────────────────────────────────────────────────────────────

def main():
    print("=== Generating espanol-en/ scaffold ===")
    gen_espanol_en_hub()
    for level in LEVELS:
        gen_espanol_en_level(level)
    gen_espanol_en_grammar_index()
    gen_espanol_en_vocab_index()
    gen_espanol_en_writing_index()
    gen_espanol_en_grammar_chapters()
    gen_espanol_en_vocab_chapters()
    gen_espanol_en_writing_chapters()
    gen_espanol_en_exams()

    print("\n=== Generating espanol/ scaffold ===")
    gen_espanol_hub()
    for level in LEVELS:
        gen_espanol_level(level)
    gen_espanol_exams()

    print("\nDone. Run python3 scripts/gen_coverage.py then python3 scripts/check_structure.py")

if __name__ == '__main__':
    main()
