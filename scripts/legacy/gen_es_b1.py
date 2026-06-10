#!/usr/bin/env python3
"""Build complete Spanish B1 section: spec files, chapter pages, and index files."""
import json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPECS = os.path.join(ROOT, 'scripts/chapter_specs')
os.makedirs(SPECS, exist_ok=True)

# ─── B1 Grammar chapters ──────────────────────────────────────────────────────
GRAMMAR = [
    (1,  'comparatives-superlatives', 'Comparatives & Superlatives', 'the tallest · the most · the best · -er and -er'),
    (2,  'future-forms',              'Future Forms',                 'will · going to · Present Continuous — diferencias clave'),
    (3,  'ing-form',                  'The -ing Form',                'After verbs · after prepositions · meaning change'),
    (4,  'modal-deduction',           'Modals of Deduction',          'must be · can\'t be · might be · formas de pasado'),
    (5,  'modals-advice',             'Modals — Advice',              'should · ought to · had better — consejo y recomendación'),
    (6,  'modals-obligation',         'Modals — Obligation',          'must · have to · need to — obligación y prohibición'),
    (7,  'passive-simple',            'Passive Voice',                'is made · was built · will be sent — voz pasiva'),
    (8,  'past-simple-continuous',    'Past Simple & Continuous',     'narración · when vs while · verbos de estado'),
    (9,  'present-perfect',           'Present Perfect',              'for · since · how long · vs past simple'),
    (10, 'question-tags',             'Question Tags',                'isn\'t it? · didn\'t they? · entonación'),
    (11, 'relative-clauses',          'Relative Clauses',             'Reduced · prepositional · whom/which · cláusulas relativas'),
    (12, 'reported-speech-basic',     'Reported Speech',              'Tense backshift · say vs tell · cambios de palabras'),
    (13, 'second-conditional',        'Second Conditional',           'If + past + would — situaciones hipotéticas'),
    (14, 'so-neither',                'So and Neither',               'So do I · Neither can I — acuerdo y desacuerdo'),
    (15, 'too-enough',                'Too, Enough and Very',          'too much · adj + enough · very — grado y cantidad'),
    (16, 'verb-infinitive-patterns',  'Verb + Infinitive Patterns',   'want to · make bare · tell someone to'),
    (17, 'zero-first-conditional',    'Zero & First Conditional',     'If + present, + present/will — hábitos y posibilidades'),
    (18, 'past-perfect',              'Past Perfect',                  'had + PP · antes de otro evento pasado'),
    (19, 'present-perfect-continuous','Present Perfect Continuous',    'have been + -ing · for / since · vs present perfect'),
]

# ─── B1 Vocabulary topics ─────────────────────────────────────────────────────
VOCAB = [
    (1,  'adjective-preposition',   'Adjective + Preposition',       'interested in · good at · afraid of · responsible for'),
    (2,  'applied-grammar-verbs',   'Applied Grammar Verbs',         'suggest · recommend · deny · admit · regret · manage'),
    (3,  'collocations-make-do',    'Collocations: Make, Do, Have',  'make a decision · do research · have fun · take turns'),
    (4,  'education-school',        'Education and School',          'degree · tuition · curriculum · assignment · graduate'),
    (5,  'environment-nature',      'Environment and Nature',        'climate change · emissions · biodiversity · sustainable'),
    (6,  'phrasal-verbs-get-take',  'Phrasal Verbs: Get and Take',   'get on · get over · take off · take up · take over'),
    (7,  'phrasal-verbs-go-come',   'Phrasal Verbs: Go and Come',    'go on · go through · come across · come up with'),
    (8,  'sport-leisure',           'Sport and Leisure',             'tournament · referee · spectator · championship · training'),
    (9,  'technology-media',        'Technology and Media',          'artificial intelligence · software · network · digital media'),
    (10, 'travel-holidays',         'Travel and Holidays',           'itinerary · accommodation · resort · departure · customs'),
    (11, 'word-families-basic',     'Word Families',                 'noun/verb/adjective/adverb patterns · suffix & prefix'),
]

BASE_V = 'v123'
DARK_V = 'v109'

# ─── Generate spec files ──────────────────────────────────────────────────────
print("Generating spec files...")
for i, (num, slug, title, subtitle) in enumerate(GRAMMAR):
    nxt = GRAMMAR[i+1] if i+1 < len(GRAMMAR) else None
    sp = {"lang":"es","level":"b1","section":"grammar","num":num,"slug":slug,
          "title":title,"subtitle":subtitle,
          "next_slug":nxt[1] if nxt else None,
          "next_num":nxt[0] if nxt else None,
          "next_title":nxt[2] if nxt else None}
    with open(os.path.join(SPECS, f"es-b1-grammar-{slug}.json"),'w') as f:
        json.dump(sp,f,indent=2,ensure_ascii=False)

for i, (num, slug, title, subtitle) in enumerate(VOCAB):
    nxt = VOCAB[i+1] if i+1 < len(VOCAB) else None
    sp = {"lang":"es","level":"b1","section":"vocabulary","num":num,"slug":slug,
          "title":title,"subtitle":subtitle,
          "next_slug":nxt[1] if nxt else None,
          "next_num":nxt[0] if nxt else None,
          "next_title":nxt[2] if nxt else None}
    with open(os.path.join(SPECS, f"es-b1-vocabulary-{slug}.json"),'w') as f:
        json.dump(sp,f,indent=2,ensure_ascii=False)

print(f"  {len(GRAMMAR)} grammar + {len(VOCAB)} vocab spec files written.")

# ─── Run scaffold generator ───────────────────────────────────────────────────
gen = os.path.join(ROOT,'scripts/gen_chapter.py')
print("Running scaffold generator...")
errors = []
for fname in sorted(os.listdir(SPECS)):
    if fname.startswith('es-b1-'):
        result = subprocess.run(['python3', gen, os.path.join(SPECS,fname)],
                                capture_output=True, text=True)
        if result.returncode != 0:
            errors.append(f"  FAIL {fname}: {result.stderr[:200]}")
        else:
            print(f"  ok  {fname}")

if errors:
    for e in errors: print(e)
    sys.exit(1)

# ─── Create es/b1/gramatica/index.html ───────────────────────────────────────
print("\nCreating index files...")

def ch_card_grammar(num, slug, title, desc):
    return (f'    <a href="{slug}/index.html" class="ch-card ch-card--grammar" id="gpc_es-b1_{slug}">\n'
            f'      <div class="ch-num">Cap. {num}</div>\n'
            f'      <h2>{title}</h2>\n'
            f'      <p class="ch-desc">{desc}</p><span class="ch-cta">Estudiar &#8594;</span>\n'
            f'    </a>')

def badge_script(level, slug):
    return (f'(function(){{try{{var p=JSON.parse(localStorage.getItem(\'wordplay_progress\')||\'{{}}\'),(l=p[\'es-{level}\'||{{}}),c=document.getElementById(\'gpc_es-{level}_{slug}\');'
            f'if(!c)return;var b=[];if((l[\'{slug}\']||{{}}).pct>=70)b.push(\'Ejercicios\');'
            f'if((l[\'wordplay_game_es-{level}_{slug}\']||{{}}).pct>=70)b.push(\'Juego\');'
            f'if(b.length){{var d=document.createElement(\'div\');d.style.cssText=\'font-family:var(--font-sans);font-size:.65rem;font-weight:700;color:var(--amber);margin-top:6px;letter-spacing:.5px\';d.textContent=b.join(\' · \');c.querySelector(\'.ch-cta\').before(d);}}}}catch(e){{}}}})();')

grammar_cards = '\n'.join(ch_card_grammar(num,slug,title,sub) for num,slug,title,sub in GRAMMAR)
grammar_scripts = '\n'.join(badge_script('b1',slug) for _,slug,_,_ in GRAMMAR)

gramatica_idx = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../favicon.svg" type="image/svg+xml">
<title>B1 Gramática — Word Play para hispanohablantes</title>
<link rel="stylesheet" href="../../../shared/base.css?v={BASE_V}">
<script src="../../../shared/dark-init.js?v={DARK_V}"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="../index.html" class="back back-link" aria-label="Atrás"></a>
  <a href="../../../index.html" class="brand"><svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px"><rect width="32" height="32" rx="4" fill="currentColor"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>Word Play</a>
  <button class="dark-toggle" aria-label="Cambiar modo oscuro" onclick="toggleDark()">&#9680; Oscuro</button>
</div></header>
<div class="section-page">
  <div class="breadcrumb">
    <a href="../../../index.html">Inicio</a><span>›</span>
    <a href="../../index.html">Para hispanohablantes</a><span>›</span>
    <a href="../index.html">B1</a><span>›</span>
    <strong>Gramática</strong>
  </div>
  <div class="eyebrow">B1 · GRAMÁTICA · PARA HISPANOHABLANTES</div>
  <h1>Gramática B1</h1>
  <p class="section-desc">Explicaciones en español · Errores de interferencia · Comparación inglés-español</p>
  <div class="ch-grid">
{grammar_cards}
  </div>
</div>
<footer class="site-footer">Word Play · Inglés Cambridge A1&#8594;C2 · Para hispanohablantes</footer>
<script>
{grammar_scripts}
</script>
</body>
</html>"""

os.makedirs(os.path.join(ROOT,'es/b1/gramatica'), exist_ok=True)
with open(os.path.join(ROOT,'es/b1/gramatica/index.html'),'w') as f:
    f.write(gramatica_idx)
print("  created es/b1/gramatica/index.html")

# ─── Create es/b1/vocabulary/index.html ──────────────────────────────────────
def vocab_card(num, slug, title, desc):
    return (f'    <a href="{slug}/index.html" class="ch-card ch-card--vocab" id="vpc_b1_{slug}">\n'
            f'      <div class="ch-num">V{num}</div>\n'
            f'      <h2>{title}</h2>\n'
            f'      <p class="ch-desc">{desc}</p><span class="ch-cta">Estudiar &#8594;</span>\n'
            f'    </a>')

vocab_cards = '\n'.join(vocab_card(num,slug,title,sub) for num,slug,title,sub in VOCAB)

vocab_idx = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../favicon.svg" type="image/svg+xml">
<title>Vocabulario B1 — Word Play</title>
<link rel="stylesheet" href="../../../shared/base.css?v={BASE_V}">
<script src="../../../shared/dark-init.js?v={DARK_V}"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="../index.html" class="back back-link" aria-label="Atrás"></a>
  <a href="../../../index.html" class="brand"><svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px"><rect width="32" height="32" rx="4" fill="currentColor"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>Word Play</a>
  <button class="dark-toggle" aria-label="Cambiar modo oscuro" onclick="toggleDark()">&#9680; Oscuro</button>
</div></header>
<div class="section-page">
  <div class="breadcrumb">
    <a href="../../../index.html">Inicio</a><span>&#8250;</span>
    <a href="../../index.html">Para hispanohablantes</a><span>&#8250;</span>
    <a href="../index.html">B1</a><span>&#8250;</span>
    <strong>Vocabulario</strong>
  </div>
  <div class="eyebrow">B1 · VOCABULARIO</div>
  <h1>Vocabulario B1</h1>
  <p class="section-desc">11 temas · Tarjetas · Lección · Juego</p>
  <div class="ch-grid">
{vocab_cards}
  </div>
</div>
<footer class="site-footer">Word Play · Inglés Cambridge A1&#8594;C2 · Para hispanohablantes</footer>
</body>
</html>"""

os.makedirs(os.path.join(ROOT,'es/b1/vocabulary'), exist_ok=True)
with open(os.path.join(ROOT,'es/b1/vocabulary/index.html'),'w') as f:
    f.write(vocab_idx)
print("  created es/b1/vocabulary/index.html")

# ─── Create es/b1/index.html ──────────────────────────────────────────────────
b1_hub = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<title>B1 Intermedio — Word Play para hispanohablantes</title>
<link rel="stylesheet" href="../../shared/base.css?v={BASE_V}">
<script src="../../shared/dark-init.js?v={DARK_V}"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="../index.html" class="back back-link" aria-label="Atrás"></a>
  <a href="../../index.html" class="brand"><svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px"><rect width="32" height="32" rx="4" fill="currentColor"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>Word Play</a>
  <button class="dark-toggle" aria-label="Cambiar modo oscuro" onclick="toggleDark()">&#9680; Oscuro</button>
</div></header>
<div class="section-page">
  <div class="breadcrumb">
    <a href="../../index.html">Inicio</a><span>›</span>
    <a href="../index.html">Para hispanohablantes</a><span>›</span>
    <strong>B1 Intermedio</strong>
  </div>
  <div class="eyebrow">NIVEL B1 · PARA HISPANOHABLANTES</div>
  <h1>B1 — Intermedio</h1>
  <p class="section-desc">Gramática · Vocabulario — con explicaciones en español y comparaciones entre los dos idiomas</p>
  <div class="ch-grid">
    <a href="gramatica/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:8px">GRAMÁTICA</div>
      <div style="font-family:Georgia,serif;font-size:1.3rem;font-weight:700;color:white;margin-bottom:6px">Gramática B1</div>
      <div style="font-family:var(--font-sans);font-size:.78rem;color:rgba(255,255,255,.55);line-height:1.5;margin-bottom:16px">Pasado · Pasiva · Condicionales · Discurso indirecto · 19 capítulos</div>
      <div style="font-family:var(--font-sans);font-size:.7rem;font-weight:700;color:var(--amber);letter-spacing:.5px">Estudiar &#8594;</div>
    </a>
    <a href="vocabulary/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:8px">VOCABULARIO</div>
      <div style="font-family:Georgia,serif;font-size:1.3rem;font-weight:700;color:white;margin-bottom:6px">Vocabulario B1</div>
      <div style="font-family:var(--font-sans);font-size:.78rem;color:rgba(255,255,255,.55);line-height:1.5;margin-bottom:16px">Medio ambiente · Phrasal verbs · Colocaciones · 11 temas</div>
      <div style="font-family:var(--font-sans);font-size:.7rem;font-weight:700;color:var(--amber);letter-spacing:.5px">Estudiar &#8594;</div>
    </a>
  </div>
</div>
<footer class="site-footer">Word Play · Inglés Cambridge A1&#8594;C2 · Para hispanohablantes</footer>
</body>
</html>"""

os.makedirs(os.path.join(ROOT,'es/b1'), exist_ok=True)
with open(os.path.join(ROOT,'es/b1/index.html'),'w') as f:
    f.write(b1_hub)
print("  created es/b1/index.html")

# ─── Update es/index.html: activate B1 ───────────────────────────────────────
es_idx_path = os.path.join(ROOT,'es/index.html')
with open(es_idx_path) as f:
    content = f.read()

old = '''    <div style="background:#1A1A1A;border-radius:10px;padding:22px 20px;opacity:.5">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">NIVEL B1</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">Intermedio</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.45)">Proximamente</div>
    </div>'''

new = '''    <a href="b1/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">NIVEL B1</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">Intermedio</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">Gramática · 19 capítulos disponibles</div>
    </a>'''

if old in content:
    content = content.replace(old, new)
    with open(es_idx_path,'w') as f:
        f.write(content)
    print("  updated es/index.html: B1 now active")
else:
    print("  WARNING: could not find B1 placeholder in es/index.html")

print(f"\nDone. Spanish B1 fully scaffolded: {len(GRAMMAR)} grammar + {len(VOCAB)} vocab chapters.")
