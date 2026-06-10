#!/usr/bin/env python3
"""Update es/a1 grammar and vocabulary index.html files with new chapter cards."""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ─── Grammar index ─────────────────────────────────────────────────────────────
GRAMMAR_NEW = [
    (11, 'present-continuous',    'Present Continuous',        'estoy hablando · está comiendo · estamos aprendiendo'),
    (12, 'can-cant',              'Can and Can\'t',             'puedo · no puedo · ¿puedes? — posibilidad y habilidad'),
    (13, 'imperatives',           'Imperatives',               'abre · no hables · escucha — órdenes e instrucciones'),
    (14, 'adjectives-basic',      'Basic Adjectives',          'big · small · fast · old — posición y concordancia'),
    (15, 'possessive-adjectives', 'Possessive Adjectives',     'my · your · his · her · our · their — adjetivos posesivos'),
    (16, 'possessives',           'Possessives',               'mine · yours · his · hers · ours · theirs — pronombres posesivos'),
    (17, 'question-words',        'Question Words',            'what · where · when · who · why · how — hacer preguntas'),
    (18, 'prepositions-place',    'Prepositions of Place',     'in · on · under · next to · behind · in front of'),
    (19, 'prepositions-time',     'Prepositions of Time',      'at noon · on Monday · in July — cuándo en inglés'),
    (20, 'some-any',              'Some and Any',              'some friends · any money — cantidad indefinida'),
    (21, 'going-to-future',       'Going to Future',           'voy a estudiar · vas a venir — futuro próximo'),
    (22, 'adverbs-frequency',     'Adverbs of Frequency',      'always · usually · sometimes · rarely · never'),
    (23, 'simple-past-regular',   'Simple Past Regular',       'I worked · she played · they listened — verbo + -ed'),
    (24, 'simple-past-irregular', 'Simple Past Irregular',     'went · saw · ate · had · came — verbos irregulares'),
]

grammar_cards = []
grammar_scripts = []

for num, slug, title, desc in GRAMMAR_NEW:
    grammar_cards.append(
        f'    <a href="{slug}/index.html" class="ch-card ch-card--grammar" id="gpc_es-a1_{slug}">\n'
        f'      <div class="ch-num">Cap. {num}</div>\n'
        f'      <h2>{title}</h2>\n'
        f'      <p class="ch-desc">{desc}</p><span class="ch-cta">Estudiar &#8594;</span>\n'
        f'    </a>'
    )
    grammar_scripts.append(
        f'(function() {{\n'
        f'  try {{\n'
        f'    var prog = JSON.parse(localStorage.getItem(\'wordplay_progress\') || \'{{}}\');\n'
        f'    var lvl = prog[\'es-a1\'] || {{}};\n'
        f'    var card = document.getElementById(\'gpc_es-a1_{slug}\');\n'
        f'    if (!card) return;\n'
        f'    var ws = lvl[\'{slug}\'];\n'
        f'    var gm = lvl[\'wordplay_game_es-a1_{slug}\'];\n'
        f'    var badges = [];\n'
        f'    if (ws && ws.pct >= 70) badges.push(\'Ejercicios\');\n'
        f'    if (gm && gm.pct >= 70) badges.push(\'Juego\');\n'
        f'    if (badges.length) {{\n'
        f'      var b = document.createElement(\'div\');\n'
        f'      b.style.cssText = \'font-family:var(--font-sans);font-size:.65rem;font-weight:700;color:var(--amber);margin-top:6px;letter-spacing:.5px\';\n'
        f'      b.textContent = badges.join(\' · \');\n'
        f'      card.querySelector(\'.ch-cta\').before(b);\n'
        f'    }}\n'
        f'  }} catch(e) {{}}\n'
        f'}})();'
    )

# Read and update grammar index
grammar_path = os.path.join(ROOT, 'es/a1/gramatica/index.html')
with open(grammar_path) as f:
    content = f.read()

# Insert new cards before closing </div> of ch-grid
new_cards_block = '\n' + '\n'.join(grammar_cards) + '\n  '
content = content.replace('  </div>\n</div>\n<footer',
                          new_cards_block + '</div>\n</div>\n<footer')

# Insert new scripts before closing </script>
new_scripts_block = '\n\n' + '\n\n'.join(grammar_scripts) + '\n'
content = content.replace('\n</script>\n</body>', new_scripts_block + '</script>\n</body>')

with open(grammar_path, 'w') as f:
    f.write(content)
print(f"Updated {grammar_path}: +{len(GRAMMAR_NEW)} cards")

# ─── Vocabulary index ──────────────────────────────────────────────────────────
VOCAB_NEW = [
    (7,  'clothes',         'Ropa',            'camisa · pantalón · vestido · abrigo · zapatos · sombrero'),
    (8,  'hobbies',         'Pasatiempos',     'lectura · deporte · música · cocina · juegos · viajes'),
    (9,  'house-and-rooms', 'Casa y Habitaciones', 'cocina · dormitorio · baño · salón · jardín'),
    (10, 'jobs',            'Profesiones',     'profesor · médico · ingeniero · conductor · chef · enfermero'),
    (11, 'places-in-town',  'Lugares en la Ciudad', 'colegio · hospital · banco · estación · parque · mercado'),
    (12, 'weather',         'El Tiempo',       'soleado · nublado · lloviendo · frío · calor · ventoso'),
]

vocab_cards = []
for num, slug, title, desc in VOCAB_NEW:
    vocab_cards.append(
        f'    <a href="{slug}/index.html" class="ch-card ch-card--vocab" id="vpc_a1_{slug}">\n'
        f'      <div class="ch-num">V{num}</div>\n'
        f'      <h2>{title}</h2>\n'
        f'      <p class="ch-desc">{desc}</p><span class="ch-cta">Estudiar &#8594;</span>\n'
        f'    </a>'
    )

# Read and update vocab index
vocab_path = os.path.join(ROOT, 'es/a1/vocabulary/index.html')
with open(vocab_path) as f:
    content = f.read()

# Update section-desc count
content = content.replace('12 temas · Tarjetas · Lección · Juego', '12 temas · Tarjetas · Lección · Juego')

# Insert new cards before closing </div> of ch-grid
new_vocab_block = '\n' + '\n'.join(vocab_cards) + '\n  '
content = content.replace('  </div>\n</div>\n<footer',
                          new_vocab_block + '</div>\n</div>\n<footer')

with open(vocab_path, 'w') as f:
    f.write(content)
print(f"Updated {vocab_path}: +{len(VOCAB_NEW)} cards")
print("Done.")
