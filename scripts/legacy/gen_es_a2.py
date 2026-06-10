#!/usr/bin/env python3
"""Build complete Spanish A2 section: spec files, chapter pages, and index files."""
import json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPECS = os.path.join(ROOT, 'scripts/chapter_specs')
os.makedirs(SPECS, exist_ok=True)

# ─── A2 Grammar chapters (in curriculum order) ───────────────────────────────
GRAMMAR = [
    (1,  'past-simple',              'Past Simple',               'regular -ed · irregular forms · didn\'t · questions'),
    (2,  'past-continuous',          'Past Continuous',           'was/were + -ing · while/when · stative verbs'),
    (3,  'present-perfect-intro',    'Present Perfect',           'have + PP · ever/never/just · vs past simple'),
    (4,  'future-going-to',          'Going to Future',           'planes · predicciones · voy a estudiar mañana'),
    (5,  'future-will',              'Future with Will',          'predicciones · decisiones espontáneas · promesas'),
    (6,  'modal-could-might',        'Could and Might',           'habilidad pasada · peticiones corteses · posibilidad'),
    (7,  'modal-must-should',        'Must and Should',           'obligación · prohibición · consejo · recomendación'),
    (8,  'comparatives-basic',       'Comparatives',             '-er than · more ... than · as ... as · irregular'),
    (9,  'countable-uncountable-basic','Countable & Uncountable', 'many/much · a few/a little · sustantivos difíciles'),
    (10, 'quantifiers-basic',        'Quantifiers',               'a lot of · enough · several · all · most · some/any'),
    (11, 'too-enough-basic',         'Too and Enough',            'too + adj · adj + enough · too many / too much'),
    (12, 'relative-clauses-basic',   'Relative Clauses',          'who · which · that · where · whose'),
    (13, 'word-order',               'Word Order',                'S+V+O · lugar antes de tiempo · posición del adverbio'),
    (14, 'object-pronouns',          'Object Pronouns',           'me · him · her · us · them · diferencia con español'),
    (15, 'short-answers',            'Short Answers',             'Yes I do · No she isn\'t · So do I · Neither do I'),
    (16, 'conjunctions',             'Conjunctions',              'because · although · so · however · while'),
    (17, 'adverbs-manner',           'Adverbs of Manner',         'adjetivo + -ly · well · fast · hard · posición'),
    (18, 'prepositions-movement',    'Prepositions of Movement',  'into · across · through · towards · around'),
]

# ─── A2 Vocabulary topics ─────────────────────────────────────────────────────
VOCAB = [
    (1,  'cooking',             'Cooking',              'cocinar · ingredientes · recetas · métodos de cocción'),
    (2,  'feelings-emotions',   'Feelings & Emotions',  'happy · sad · excited · nervous · angry · surprised'),
    (3,  'health-and-body',     'Health & Body',        'partes del cuerpo · enfermedades · síntomas · médico'),
    (4,  'music',               'Music',                'instrumentos · géneros · concierto · canción · cantante'),
    (5,  'problems-solutions',  'Problems & Solutions',  'problema · solución · sugerir · pedir ayuda · resolver'),
    (6,  'school-subjects',     'School Subjects',      'materias · asignatura · examen · nota · estudiar'),
    (7,  'shopping-and-money',  'Shopping & Money',     'comprar · precio · rebajas · pagar · cambio · tarjeta'),
    (8,  'sports',              'Sports',               'deporte · equipo · competición · ganar · perder · entrenamiento'),
    (9,  'technology-and-media','Technology & Media',   'smartphone · internet · redes sociales · aplicación · vídeo'),
    (10, 'transport-and-travel','Transport & Travel',   'avión · tren · autobús · reserva · billete · viaje'),
    (11, 'weather-detail',      'Weather',              'tiempo · lluvia · nieve · temperatura · previsión · estaciones'),
    (12, 'work-and-jobs',       'Work & Jobs',          'trabajo · jefe · sueldo · oficina · solicitud · contrato'),
]

# ─── Generate spec files ──────────────────────────────────────────────────────
print("Generating spec files...")
for i, (num, slug, title, subtitle) in enumerate(GRAMMAR):
    nxt = GRAMMAR[i+1] if i+1 < len(GRAMMAR) else None
    sp = {"lang":"es","level":"a2","section":"grammar","num":num,"slug":slug,
          "title":title,"subtitle":subtitle,
          "next_slug":nxt[1] if nxt else None,
          "next_num":nxt[0] if nxt else None,
          "next_title":nxt[2] if nxt else None}
    fname = f"es-a2-grammar-{slug}.json"
    with open(os.path.join(SPECS, fname),'w') as f:
        json.dump(sp,f,indent=2,ensure_ascii=False)

for i, (num, slug, title, subtitle) in enumerate(VOCAB):
    nxt = VOCAB[i+1] if i+1 < len(VOCAB) else None
    sp = {"lang":"es","level":"a2","section":"vocabulary","num":num,"slug":slug,
          "title":title,"subtitle":subtitle,
          "next_slug":nxt[1] if nxt else None,
          "next_num":nxt[0] if nxt else None,
          "next_title":nxt[2] if nxt else None}
    fname = f"es-a2-vocabulary-{slug}.json"
    with open(os.path.join(SPECS, fname),'w') as f:
        json.dump(sp,f,indent=2,ensure_ascii=False)

print(f"  {len(GRAMMAR)} grammar + {len(VOCAB)} vocab spec files written.")

# ─── Run gen_chapter.py for each spec ────────────────────────────────────────
gen = os.path.join(ROOT,'scripts/gen_chapter.py')
print("Running scaffold generator...")
errors = []
for fname in sorted(os.listdir(SPECS)):
    if fname.startswith('es-a2-'):
        result = subprocess.run(['python3', gen, os.path.join(SPECS,fname)],
                                capture_output=True, text=True)
        if result.returncode != 0:
            errors.append(f"  FAIL {fname}: {result.stderr[:200]}")
        else:
            print(f"  ok  {fname}")

if errors:
    print("ERRORS:")
    for e in errors:
        print(e)
    sys.exit(1)

# ─── Create es/a2/gramatica/index.html ───────────────────────────────────────
print("\nCreating section index files...")

BASE_V = 'v123'
DARK_V = 'v109'

def ch_card_grammar(num, slug, title, desc):
    return (f'    <a href="{slug}/index.html" class="ch-card ch-card--grammar" id="gpc_es-a2_{slug}">\n'
            f'      <div class="ch-num">Cap. {num}</div>\n'
            f'      <h2>{title}</h2>\n'
            f'      <p class="ch-desc">{desc}</p><span class="ch-cta">Estudiar &#8594;</span>\n'
            f'    </a>')

def badge_script(slug):
    return (f'(function() {{\n'
            f'  try {{\n'
            f'    var p=JSON.parse(localStorage.getItem(\'wordplay_progress\')||\'{{}}\'),(l=p[\'es-a2\']||{{}}),c=document.getElementById(\'gpc_es-a2_{slug}\');\n'
            f'    if(!c)return;\n'
            f'    var b=[];\n'
            f'    if((l[\'{slug}\']||{{}}).pct>=70)b.push(\'Ejercicios\');\n'
            f'    if((l[\'wordplay_game_es-a2_{slug}\']||{{}}).pct>=70)b.push(\'Juego\');\n'
            f'    if(b.length){{var d=document.createElement(\'div\');d.style.cssText=\'font-family:var(--font-sans);font-size:.65rem;font-weight:700;color:var(--amber);margin-top:6px;letter-spacing:.5px\';d.textContent=b.join(\' · \');c.querySelector(\'.ch-cta\').before(d);}}\n'
            f'  }}catch(e){{}}\n'
            f'}})();')

grammar_cards = '\n'.join(ch_card_grammar(num,slug,title,subtitle) for num,slug,title,subtitle in GRAMMAR)
grammar_scripts = '\n\n'.join(badge_script(slug) for _,slug,_,_ in GRAMMAR)

gramatica_idx = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../favicon.svg" type="image/svg+xml">
<title>A2 Gramática — Word Play para hispanohablantes</title>
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
    <a href="../index.html">A2</a><span>›</span>
    <strong>Gramática</strong>
  </div>
  <div class="eyebrow">A2 · GRAMÁTICA · PARA HISPANOHABLANTES</div>
  <h1>Gramática A2</h1>
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

os.makedirs(os.path.join(ROOT,'es/a2/gramatica'), exist_ok=True)
with open(os.path.join(ROOT,'es/a2/gramatica/index.html'),'w') as f:
    f.write(gramatica_idx)
print("  created es/a2/gramatica/index.html")

# ─── Create es/a2/vocabulary/index.html ──────────────────────────────────────
def vocab_card(num, slug, title, desc):
    return (f'    <a href="{slug}/index.html" class="ch-card ch-card--vocab" id="vpc_a2_{slug}">\n'
            f'      <div class="ch-num">V{num}</div>\n'
            f'      <h2>{title}</h2>\n'
            f'      <p class="ch-desc">{desc}</p><span class="ch-cta">Estudiar &#8594;</span>\n'
            f'    </a>')

vocab_cards = '\n'.join(vocab_card(num,slug,title,subtitle) for num,slug,title,subtitle in VOCAB)

vocab_idx = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../favicon.svg" type="image/svg+xml">
<title>Vocabulario A2 — Word Play</title>
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
    <a href="../index.html">A2</a><span>&#8250;</span>
    <strong>Vocabulario</strong>
  </div>
  <div class="eyebrow">A2 · VOCABULARIO</div>
  <h1>Vocabulario A2</h1>
  <p class="section-desc">12 temas · Tarjetas · Lección · Juego</p>
  <div class="ch-grid">
{vocab_cards}
  </div>
</div>
<footer class="site-footer">Word Play · Inglés Cambridge A1&#8594;C2 · Para hispanohablantes</footer>
</body>
</html>"""

os.makedirs(os.path.join(ROOT,'es/a2/vocabulary'), exist_ok=True)
with open(os.path.join(ROOT,'es/a2/vocabulary/index.html'),'w') as f:
    f.write(vocab_idx)
print("  created es/a2/vocabulary/index.html")

# ─── Create es/a2/index.html (level hub) ─────────────────────────────────────
a2_hub = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<title>A2 Elemental — Word Play para hispanohablantes</title>
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
    <strong>A2 Elemental</strong>
  </div>
  <div class="eyebrow">NIVEL A2 · PARA HISPANOHABLANTES</div>
  <h1>A2 — Elemental</h1>
  <p class="section-desc">Gramática · Vocabulario — con explicaciones en español y comparaciones entre los dos idiomas</p>
  <div class="ch-grid">
    <a href="gramatica/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:8px">GRAMÁTICA</div>
      <div style="font-family:Georgia,serif;font-size:1.3rem;font-weight:700;color:white;margin-bottom:6px">Gramática A2</div>
      <div style="font-family:var(--font-sans);font-size:.78rem;color:rgba(255,255,255,.55);line-height:1.5;margin-bottom:16px">Past Simple · Present Perfect · Modales · Relativos · 18 capítulos</div>
      <div style="font-family:var(--font-sans);font-size:.7rem;font-weight:700;color:var(--amber);letter-spacing:.5px">Estudiar &#8594;</div>
    </a>
    <a href="vocabulary/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:8px">VOCABULARIO</div>
      <div style="font-family:Georgia,serif;font-size:1.3rem;font-weight:700;color:white;margin-bottom:6px">Vocabulario A2</div>
      <div style="font-family:var(--font-sans);font-size:.78rem;color:rgba(255,255,255,.55);line-height:1.5;margin-bottom:16px">Cocina · Emociones · Trabajo · Tecnología · 12 temas</div>
      <div style="font-family:var(--font-sans);font-size:.7rem;font-weight:700;color:var(--amber);letter-spacing:.5px">Estudiar &#8594;</div>
    </a>
  </div>
</div>
<footer class="site-footer">Word Play · Inglés Cambridge A1&#8594;C2 · Para hispanohablantes</footer>
</body>
</html>"""

os.makedirs(os.path.join(ROOT,'es/a2'), exist_ok=True)
with open(os.path.join(ROOT,'es/a2/index.html'),'w') as f:
    f.write(a2_hub)
print("  created es/a2/index.html")

# ─── Update es/index.html: activate A2 link ───────────────────────────────────
es_idx_path = os.path.join(ROOT,'es/index.html')
with open(es_idx_path) as f:
    content = f.read()

old = '''    <div style="background:#1A1A1A;border-radius:10px;padding:22px 20px;opacity:.5">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">NIVEL A2</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">Elemental</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.45)">Proximamente</div>
    </div>'''

new = '''    <a href="a2/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">NIVEL A2</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">Elemental</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">Gramática · 18 capítulos disponibles</div>
    </a>'''

if old in content:
    content = content.replace(old, new)
    with open(es_idx_path,'w') as f:
        f.write(content)
    print("  updated es/index.html: A2 now active")
else:
    print("  WARNING: could not find A2 placeholder in es/index.html — manual update needed")

# ─── Fix es/a1/index.html chapter counts ─────────────────────────────────────
a1_hub_path = os.path.join(ROOT,'es/a1/index.html')
with open(a1_hub_path) as f:
    content = f.read()

content = content.replace('To be · Present Simple · Can · Preposiciones · 10 capítulos',
                          'To be · Can · Present Simple · Pasado Simple · 24 capítulos')
content = content.replace('Colores · Animales · Familia · Números · 4 temas',
                          'Animales · Colores · Familia · Ropa · Trabajo · 12 temas')

with open(a1_hub_path,'w') as f:
    f.write(content)
print("  updated es/a1/index.html: chapter counts corrected")

print("\nDone. Spanish A2 fully scaffolded.")
