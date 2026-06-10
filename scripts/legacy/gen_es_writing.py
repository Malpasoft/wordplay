#!/usr/bin/env python3
"""Build Spanish writing sections for all 6 levels (es/a1 through es/c2)."""
import json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPECS = os.path.join(ROOT, 'scripts/chapter_specs')
BASE_V = 'v123'
DARK_V = 'v109'

# ─── Writing curriculum per level ────────────────────────────────────────────
# Mirrors English writing chapters with Spanish-native focus
WRITING = {
    'a1': [
        (1, 'form-filling',    'Form Filling',      'Rellenar un formulario con información personal correcta'),
        (2, 'personal-profile','Personal Profile',   'Escribir sobre ti mismo · información básica · oraciones simples'),
        (3, 'short-note',      'Short Note',         'Escribir una nota corta · mensaje informal · saludos simples'),
    ],
    'a2': [
        (1, 'description',    'Personal Description','Describir personas y lugares · adjetivos · presente simple'),
        (2, 'informal-email', 'Informal Email',      'Email a un amigo · registro informal · saludos y despedidas'),
        (3, 'postcard',       'Postcard',            'Tarjeta postal · mensaje breve · lugar que visitas · tiempo verbal'),
    ],
    'b1': [
        (1, 'article',         'Article',            'Artículo PET · gancho inicial · secciones · conciencia del lector'),
        (2, 'informal-letter', 'Informal Letter',    'Carta informal · registro · tono amistoso · fórmulas de cierre'),
        (3, 'story',           'Story',              'Narración · tiempos de pasado · conectores · tensión narrativa'),
    ],
    'b2': [
        (1, 'article',       'Article',         'Artículo FCE · gancho inicial · subtítulos · conciencia del lector'),
        (2, 'essay',         'Essay',           'Ensayo argumentativo · registro formal · estructura clara · 140–190 palabras'),
        (3, 'formal-email',  'Formal Email',    'Email formal · saludo correcto · registro · frases formales · cierre'),
        (4, 'report',        'Report',          'Informe FCE · secciones · tono impersonal · recomendaciones'),
        (5, 'review',        'Review',          'Reseña FCE · opinión fundamentada · evaluación equilibrada · recomendación'),
    ],
    'c1': [
        (1, 'article',        'Article',        'Artículo CAE · apertura atractiva · subtítulos · 220–260 palabras'),
        (2, 'essay',          'Essay',          'Ensayo CAE · argumento equilibrado · registro formal · 220–260 palabras'),
        (3, 'formal-letter',  'Formal Letter',  'Carta formal CAE · solicitud · queja · consulta · registro estricto'),
        (4, 'proposal',       'Proposal',       'Propuesta CAE · secciones con título · recomendaciones · tono persuasivo'),
        (5, 'report',         'Report',         'Informe CAE · secciones · tono impersonal · hallazgos y conclusiones'),
        (6, 'review',         'Review',         'Reseña CAE · evaluación sostenida · vocabulario preciso · semiFormal'),
    ],
    'c2': [
        (1, 'academic-essay',    'Academic Essay',    'Ensayo CPE · escritura discursiva · 180–220 palabras · registro formal'),
        (2, 'critical-review',   'Critical Review',   'Reseña crítica CPE · evaluación sostenida · vocabulario preciso'),
        (3, 'formal-letter',     'Formal Letter',     'Carta formal CPE · registro correcto · convenciones de apertura y cierre'),
        (4, 'proposal',          'Proposal',          'Propuesta CPE · secciones estructuradas · recomendaciones · tono persuasivo'),
        (5, 'report',            'Report',            'Informe CPE · registro impersonal · encabezados · hallazgos y conclusiones'),
        (6, 'review',            'Review',            'Reseña CPE · lenguaje evaluativo · recomendación · 220–260 palabras'),
    ],
}

gen = os.path.join(ROOT, 'scripts/gen_chapter.py')
errors = []
all_spec_files = []

# ─── Generate spec files and chapter pages ───────────────────────────────────
for level_code, chapters in WRITING.items():
    print(f"\nBuilding es/{level_code} writing ({len(chapters)} chapters)...")
    for i, (num, slug, title, subtitle) in enumerate(chapters):
        nxt = chapters[i+1] if i+1 < len(chapters) else None
        sp = {"lang":"es","level":level_code,"section":"writing","num":num,"slug":slug,
              "title":title,"subtitle":subtitle,
              "next_slug":nxt[1] if nxt else None,"next_num":nxt[0] if nxt else None,
              "next_title":nxt[2] if nxt else None}
        fpath = os.path.join(SPECS, f"es-{level_code}-writing-{slug}.json")
        with open(fpath,'w') as f:
            json.dump(sp,f,indent=2,ensure_ascii=False)
        all_spec_files.append(fpath)

        result = subprocess.run(['python3', gen, fpath], capture_output=True, text=True)
        if result.returncode != 0:
            errors.append(f"  FAIL es-{level_code}-writing-{slug}: {result.stderr[:200]}")
        else:
            print(f"  ok  es/{level_code}/writing/{slug}/")

if errors:
    for e in errors: print(e)
    sys.exit(1)

# ─── Create writing/index.html for each level ─────────────────────────────────
def write_section_index(level_code, chapters, lv_upper):
    def ch_card(num, slug, title, desc):
        return (f'    <a href="{slug}/index.html" class="ch-card ch-card--writing" id="wpc_es-{level_code}_{slug}">\n'
                f'      <div class="ch-num">Cap. {num}</div>\n'
                f'      <h2>{title}</h2>\n'
                f'      <p class="ch-desc">{desc}</p><span class="ch-cta">Estudiar &#8594;</span>\n'
                f'    </a>')

    cards = '\n'.join(ch_card(n,s,t,sub) for n,s,t,sub in chapters)

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../favicon.svg" type="image/svg+xml">
<title>Escritura {lv_upper} — Word Play para hispanohablantes</title>
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
    <a href="../index.html">{lv_upper}</a><span>&#8250;</span>
    <strong>Escritura</strong>
  </div>
  <div class="eyebrow">{lv_upper} · ESCRITURA</div>
  <h1>Escritura {lv_upper}</h1>
  <p class="section-desc">{len(chapters)} tipos de texto · Lección · Ejercicios · Imprimibles</p>
  <div class="ch-grid">
{cards}
  </div>
</div>
<footer class="site-footer">Word Play · Inglés Cambridge A1&#8594;C2 · Para hispanohablantes</footer>
</body>
</html>"""

    os.makedirs(os.path.join(ROOT, f'es/{level_code}/writing'), exist_ok=True)
    path = os.path.join(ROOT, f'es/{level_code}/writing/index.html')
    with open(path,'w') as f:
        f.write(html)
    print(f"  created es/{level_code}/writing/index.html")

LEVEL_LABELS = {'a1':'A1','a2':'A2','b1':'B1','b2':'B2','c1':'C1','c2':'C2'}
for level_code, chapters in WRITING.items():
    write_section_index(level_code, chapters, LEVEL_LABELS[level_code])

# ─── Update level hub index.html to add writing card ─────────────────────────
WRITING_SUMMARIES = {
    'a1': ('3 tipos · Formulario · Perfil personal · Nota corta', 'Notas y formularios básicos'),
    'a2': ('3 tipos · Descripción · Email informal · Postal', 'Emails y mensajes simples'),
    'b1': ('3 tipos · Artículo · Carta informal · Historia', 'Textos PET — carta, artículo y narración'),
    'b2': ('5 tipos · Artículo · Ensayo · Email formal · Informe · Reseña', 'Textos FCE — registros formal e informal'),
    'c1': ('6 tipos · Ensayo · Carta formal · Propuesta · Informe · Reseña · Artículo', 'Textos CAE — registro avanzado'),
    'c2': ('6 tipos · Ensayo académico · Reseña crítica · Propuesta · Informe', 'Textos CPE — dominio del registro y estilo'),
}

for level_code, (summary, brief) in WRITING_SUMMARIES.items():
    hub_path = os.path.join(ROOT, f'es/{level_code}/index.html')
    with open(hub_path) as f:
        content = f.read()

    writing_card = (
        f'\n    <a href="writing/index.html" class="sect-card">\n'
        f'      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:8px">ESCRITURA</div>\n'
        f'      <div style="font-family:Georgia,serif;font-size:1.3rem;font-weight:700;color:white;margin-bottom:6px">Escritura {LEVEL_LABELS[level_code]}</div>\n'
        f'      <div style="font-family:var(--font-sans);font-size:.78rem;color:rgba(255,255,255,.55);line-height:1.5;margin-bottom:16px">{summary}</div>\n'
        f'      <div style="font-family:var(--font-sans);font-size:.7rem;font-weight:700;color:var(--amber);letter-spacing:.5px">Estudiar &#8594;</div>\n'
        f'    </a>'
    )

    # Insert writing card after the vocabulary card (before closing </div> of ch-grid)
    content = content.replace('\n  </div>\n</div>\n<footer', writing_card + '\n  </div>\n</div>\n<footer')

    with open(hub_path,'w') as f:
        f.write(content)
    print(f"  updated es/{level_code}/index.html: writing card added")

print(f"\nDone. Writing sections created for all 6 Spanish levels.")
