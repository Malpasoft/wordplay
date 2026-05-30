#!/usr/bin/env python3
"""Build Spanish B2, C1, C2 sections: spec files, chapter pages, and index files."""
import json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPECS = os.path.join(ROOT, 'scripts/chapter_specs')
os.makedirs(SPECS, exist_ok=True)

BASE_V = 'v123'
DARK_V = 'v109'

# ─── Level data ───────────────────────────────────────────────────────────────
LEVELS = {
    'b2': {
        'label': 'B2 — Intermedio Alto',
        'hub_label': 'Intermedio Alto',
        'hub_sub': 'Intermedio Alto',
        'grammar_summary': 'Pasiva · Condicionales · Inversión · Gerundios · Discourse markers · 18 capítulos',
        'vocab_summary': 'Falsos amigos · Formación de palabras · Expresiones · FCE prep · 16 temas',
        'exam': 'FCE',
        'grammar': [
            (1,  'articles',              'Articles',                   'Generic vs specific · the with categories · zero article'),
            (2,  'causative',             'Causative Have / Get',       'have/get something done — voz causativa'),
            (3,  'comparisons',           'Comparisons',                'Comparatives · Superlatives · Double Comparatives · as...as'),
            (4,  'conditionals',          'Conditionals',               'Zero · First · Second · Third — los cuatro condicionales'),
            (5,  'countable-uncountable', 'Countable & Uncountable',    'Articles, quantifiers, FCE open cloze'),
            (6,  'future-forms',          'Future Forms',               'Will · going to · Present Continuous — diferencias y usos'),
            (7,  'gerunds-infinitives',   'Gerunds & Infinitives',      'Meaning change pairs · -ing vs to — sistema completo'),
            (8,  'hypothetical-meaning',  'Hypothetical Meaning',       'I wish · If only · Would rather · It\'s time'),
            (9,  'inversion',             'Inversion & Emphasis',       'Never/rarely/hardly + aux + subject — énfasis avanzado'),
            (10, 'linking-discourse',     'Linking & Discourse Markers','Despite/although · cause/result · contrast · addition'),
            (11, 'mixed-conditionals',    'Mixed Conditionals',         'Past if → present result · present if → past result'),
            (12, 'modals-past',           'Modals in the Past',         'Must have · could have · should have · might have'),
            (13, 'narrative-tenses',      'Narrative Tenses',           'Past simple/continuous/perfect/perfect continuous — narración'),
            (14, 'passive',              'The Passive',                 'It is said that… · He is thought to… · pasiva avanzada'),
            (15, 'relative-clauses',      'Relative Clauses',           'Reduced · prepositional · whom/which · whole-clause which'),
            (16, 'reported-speech',       'Reported Speech',            'Backshift · reporting verbs · estructuras mixtas'),
            (17, 'used-to',              'Be / Get Used To',            'used to do vs be used to doing — diferencia clave'),
            (18, 'verb-patterns',         'Verb Patterns',              'Verb + to · verb + -ing · verb + obj + (to/bare)'),
        ],
        'vocab': [
            (1,  'applied-grammar-prepositions','Applied Grammar Prepositions','in favour of · due to · regardless of · with regard to'),
            (2,  'collocations-adj-noun',       'Collocations: Adj + Noun',    'strong argument · heavy rain · tight schedule · high risk'),
            (3,  'collocations-verbs',          'Collocations: Verbs',         'make an effort · take action · give advice · break a record'),
            (4,  'environment-climate',         'Environment & Climate',        'climate change · emissions · biodiversity · renewable energy'),
            (5,  'expressions-idioms',          'Expressions & Idioms',        'hit the nail · under the weather · once in a blue moon'),
            (6,  'false-friends',               'False Friends',               'actually ≠ actualmente · embarrassed ≠ embarazada · library'),
            (7,  'health-lifestyle',            'Health & Lifestyle',          'symptoms · diagnosis · treatment · well-being · balanced diet'),
            (8,  'phrasal-verbs-look-bring',    'Phrasal Verbs: Look & Bring', 'look into · look up · bring about · bring forward'),
            (9,  'phrasal-verbs-put-set',       'Phrasal Verbs: Put & Set',    'put off · put up with · set up · set out · set back'),
            (10, 'phrasal-verbs-turn-run',      'Phrasal Verbs: Turn & Run',   'turn out · turn down · run out of · run into · run through'),
            (11, 'society-culture',             'Society & Culture',           'inequality · diversity · heritage · community · citizenship'),
            (12, 'technology-innovation',       'Technology & Innovation',     'artificial intelligence · algorithm · cybersecurity · platform'),
            (13, 'word-formation-adjectives',   'Word Formation: Adjectives',  '-ful · -less · -ive · -al · -able · suffixes and prefixes'),
            (14, 'word-formation-nouns',        'Word Formation: Nouns',       '-tion · -ment · -ness · -ity · -er — patrones de sustantivos'),
            (15, 'word-formation-prefixes',     'Word Formation: Prefixes',    'un- · mis- · re- · over- · dis- · pre- · under-'),
            (16, 'work-careers',                'Work & Careers',              'recruitment · promotion · redundancy · freelance · networking'),
        ],
    },
    'c1': {
        'label': 'C1 — Avanzado',
        'hub_label': 'Avanzado',
        'hub_sub': 'Avanzado',
        'grammar_summary': 'Inversión · Nominalización · Cláusulas · Hedging · Condicionales avanzados · 17 capítulos',
        'vocab_summary': 'Vocabulario académico · Colocaciones · Registro · Formación avanzada · 7 temas',
        'exam': 'CAE',
        'grammar': [
            (1,  'conditionals-advanced',     'Conditionals — Advanced',          'provided · as long as · unless · in case · should/were-to'),
            (2,  'passive-advanced',          'Passive — Advanced',               'get + PP · reporting verbs · double passive · full range'),
            (3,  'relative-clauses-advanced', 'Relative Clauses — Advanced',      'Participle clauses · whom/which · clause-which · reduction'),
            (4,  'reported-speech-advanced',  'Reported Speech — Advanced',       'Reporting verbs · prep + -ing · suggest patterns · formal'),
            (5,  'modal-verbs-advanced',      'Modal Verbs — Advanced',           'must have / can\'t have / should have + perfect infinitive'),
            (6,  'inversion-advanced',        'Inversion — Advanced',             'So/such · conditional inversion · locative · only constructs'),
            (7,  'cleft-sentences',           'Cleft Sentences',                  'It was X who · What I need is · the thing that · all I'),
            (8,  'ellipsis-substitution',     'Ellipsis & Substitution',          'one/ones · so/not · auxiliary ellipsis · to-infinitive'),
            (9,  'nominalisation',            'Nominalisation',                   'Verbs → nouns · academic and formal register · style'),
            (10, 'gerunds-infinitives-advanced','Gerunds & Infinitives — Advanced','Meaning pairs · need + -ing · perfect forms · perception'),
            (11, 'articles-advanced',         'Articles — Advanced',              'Generic patterns · fixed phrases · headlines · no article'),
            (12, 'quantifiers-advanced',      'Quantifiers — Advanced',           'vast majority · few/a few · both/either/neither/none'),
            (13, 'causative-advanced',        'Causative — Advanced',             'make/get/have · perception verbs · help + bare infinitive'),
            (14, 'hedging-language',          'Hedging Language',                 'Soften claims · academic register · cautious language'),
            (15, 'discourse-connectors',      'Discourse Connectors',             'Furthermore · nevertheless · conversely · subsequently'),
            (16, 'advanced-tenses',           'Advanced Tenses',                  'Future continuous · future perfect · future perfect continuous'),
            (17, 'subjunctive',               'Subjunctive',                      'I suggest he be · if I were · formal mandative subjunctive'),
        ],
        'vocab': [
            (1,  'academic-vocabulary',      'Academic Vocabulary',        'lexis · framework · methodology · hypothesis · implication'),
            (2,  'applied-grammar-register', 'Applied Grammar Register',   'formal vs informal · neutral register · code-switching'),
            (3,  'collocations-advanced',    'Collocations — Advanced',    'bear in mind · pay heed · cast doubt · come to fruition'),
            (4,  'idioms-fixed-expressions', 'Idioms & Fixed Expressions', 'cut corners · get to grips with · on the fence · par for the course'),
            (5,  'paraphrasing-synonyms',    'Paraphrasing & Synonyms',    'rephrase without repeating · near-synonyms · connotation'),
            (6,  'register-style',           'Register & Style',           'formal/neutral/informal registers · hedging · vague language'),
            (7,  'word-formation-advanced',  'Word Formation — Advanced',  'complex suffixes · negative prefixes · nominalisation patterns'),
        ],
    },
    'c2': {
        'label': 'C2 — Maestría',
        'hub_label': 'Maestría',
        'hub_sub': 'Maestría',
        'grammar_summary': 'Análisis de errores · Pasiva compleja · Condicionales · Gramática en el texto · 11 capítulos',
        'vocab_summary': 'Colocaciones académicas · Modismos · Vocabulario de corpus · Sofisticación léxica · 7 temas',
        'exam': 'CPE',
        'grammar': [
            (1,  'error-analysis',        'Error Analysis & Correction',  'Tense slip · agreement · false friends · registro'),
            (2,  'complex-passives',      'Complex Passives',             'Agentless · reporting + perf inf · double · full tense range'),
            (3,  'conditionals-mastery',  'Conditionals — Mastery',       'Full system · inversion · wish · it\'s time — dominio total'),
            (4,  'register-grammar',      'Register Switching',           'Continuum · formal markers · hedging · addressing styles'),
            (5,  'academic-grammar',      'Academic Grammar',             'Nominalisation · hedging · impersonal style · academic voice'),
            (6,  'stylistic-inversion',   'Stylistic Inversion',          'Triggers · fronting · register · subtle patterns'),
            (7,  'discourse-grammar',     'Discourse Grammar',            'Given/new · end-weight · end-focus · text cohesion'),
            (8,  'advanced-modality',     'Advanced Modality',            'Epistemic vs deontic · modal adverbs · past modals'),
            (9,  'grammar-in-text',       'Grammar in Context',           'Anaphora · substitution · ellipsis · conjunction'),
            (10, 'grammar-review-tenses', 'Tense Review — Advanced',      '12 combinations · style · backshift · aspect'),
            (11, 'advanced-clauses',      'Advanced Clause Structures',   'Participle · absolute · infinitive · correlative clauses'),
        ],
        'vocab': [
            (1,  'academic-collocations',       'Academic Collocations',       'conduct research · draw conclusions · shed light on'),
            (2,  'advanced-idioms',             'Advanced Idioms',             'rest on one\'s laurels · a stitch in time · bite the bullet'),
            (3,  'applied-grammar-collocation', 'Applied Grammar Collocation', 'preposition + noun · verb + adverb · adj + noun patterns'),
            (4,  'corpus-vocabulary',           'Corpus-informed Vocabulary',  'high-frequency academic words · collocations from corpora'),
            (5,  'discourse-vocabulary',        'Discourse Vocabulary',        'firstly · moreover · in contrast · to summarize · as a result'),
            (6,  'lexical-sophistication',      'Lexical Sophistication',      'precise word choice · connotation · register · nuance'),
            (7,  'nuanced-synonyms',            'Nuanced Synonyms',            'say vs claim · big vs substantial · get vs obtain · make vs create'),
        ],
    },
}

LEVEL_NAMES = {'b2': 'Intermedio Alto', 'c1': 'Avanzado', 'c2': 'Maestría'}

def build_level(level_code, data):
    grammar = data['grammar']
    vocab = data['vocab']
    label = data['label']

    # ── Spec files ──
    print(f"\n=== Building Spanish {level_code.upper()} ({len(grammar)} grammar + {len(vocab)} vocab) ===")
    for i, (num, slug, title, subtitle) in enumerate(grammar):
        nxt = grammar[i+1] if i+1 < len(grammar) else None
        sp = {"lang":"es","level":level_code,"section":"grammar","num":num,"slug":slug,
              "title":title,"subtitle":subtitle,
              "next_slug":nxt[1] if nxt else None,"next_num":nxt[0] if nxt else None,
              "next_title":nxt[2] if nxt else None}
        with open(os.path.join(SPECS, f"es-{level_code}-grammar-{slug}.json"),'w') as f:
            json.dump(sp,f,indent=2,ensure_ascii=False)

    for i, (num, slug, title, subtitle) in enumerate(vocab):
        nxt = vocab[i+1] if i+1 < len(vocab) else None
        sp = {"lang":"es","level":level_code,"section":"vocabulary","num":num,"slug":slug,
              "title":title,"subtitle":subtitle,
              "next_slug":nxt[1] if nxt else None,"next_num":nxt[0] if nxt else None,
              "next_title":nxt[2] if nxt else None}
        with open(os.path.join(SPECS, f"es-{level_code}-vocabulary-{slug}.json"),'w') as f:
            json.dump(sp,f,indent=2,ensure_ascii=False)
    print(f"  spec files written.")

    # ── Run generator ──
    gen = os.path.join(ROOT,'scripts/gen_chapter.py')
    errors = []
    for fname in sorted(os.listdir(SPECS)):
        if fname.startswith(f'es-{level_code}-'):
            result = subprocess.run(['python3', gen, os.path.join(SPECS,fname)],
                                    capture_output=True, text=True)
            if result.returncode != 0:
                errors.append(f"  FAIL {fname}: {result.stderr[:200]}")
            else:
                print(f"  ok  {fname}")
    if errors:
        for e in errors: print(e)
        return False

    # ── gramatica/index.html ──
    depth = 3  # es/{level}/gramatica/SLUG → ../../../../
    def ch_card(num, slug, title, desc):
        return (f'    <a href="{slug}/index.html" class="ch-card ch-card--grammar" id="gpc_es-{level_code}_{slug}">\n'
                f'      <div class="ch-num">Cap. {num}</div>\n'
                f'      <h2>{title}</h2>\n'
                f'      <p class="ch-desc">{desc}</p><span class="ch-cta">Estudiar &#8594;</span>\n'
                f'    </a>')

    grammar_cards = '\n'.join(ch_card(n,s,t,sub) for n,s,t,sub in grammar)
    grammar_scripts = '\n'.join(
        f'(function(){{try{{var p=JSON.parse(localStorage.getItem(\'wordplay_progress\')||\'{{}}\'),(l=p[\'es-{level_code}\'||{{}}),c=document.getElementById(\'gpc_es-{level_code}_{s}\');'
        f'if(!c)return;var b=[];if((l[\'{s}\']||{{}}).pct>=70)b.push(\'Ejercicios\');'
        f'if((l[\'wordplay_game_es-{level_code}_{s}\']||{{}}).pct>=70)b.push(\'Juego\');'
        f'if(b.length){{var d=document.createElement(\'div\');d.style.cssText=\'font-family:var(--font-sans);font-size:.65rem;font-weight:700;color:var(--amber);margin-top:6px;letter-spacing:.5px\';d.textContent=b.join(\' · \');c.querySelector(\'.ch-cta\').before(d);}}}}catch(e){{}}}})();'
        for _,s,_,_ in grammar
    )

    lv_upper = level_code.upper()
    gram_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../favicon.svg" type="image/svg+xml">
<title>{lv_upper} Gramática — Word Play para hispanohablantes</title>
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
    <a href="../index.html">{lv_upper}</a><span>›</span>
    <strong>Gramática</strong>
  </div>
  <div class="eyebrow">{lv_upper} · GRAMÁTICA · PARA HISPANOHABLANTES</div>
  <h1>Gramática {lv_upper}</h1>
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

    os.makedirs(os.path.join(ROOT, f'es/{level_code}/gramatica'), exist_ok=True)
    with open(os.path.join(ROOT, f'es/{level_code}/gramatica/index.html'),'w') as f:
        f.write(gram_html)
    print(f"  created es/{level_code}/gramatica/index.html")

    # ── vocabulary/index.html ──
    def vc_card(num, slug, title, desc):
        return (f'    <a href="{slug}/index.html" class="ch-card ch-card--vocab" id="vpc_{level_code}_{slug}">\n'
                f'      <div class="ch-num">V{num}</div>\n'
                f'      <h2>{title}</h2>\n'
                f'      <p class="ch-desc">{desc}</p><span class="ch-cta">Estudiar &#8594;</span>\n'
                f'    </a>')

    vocab_cards = '\n'.join(vc_card(n,s,t,sub) for n,s,t,sub in vocab)

    vocab_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../favicon.svg" type="image/svg+xml">
<title>Vocabulario {lv_upper} — Word Play</title>
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
    <strong>Vocabulario</strong>
  </div>
  <div class="eyebrow">{lv_upper} · VOCABULARIO</div>
  <h1>Vocabulario {lv_upper}</h1>
  <p class="section-desc">{len(vocab)} temas · Tarjetas · Lección · Juego</p>
  <div class="ch-grid">
{vocab_cards}
  </div>
</div>
<footer class="site-footer">Word Play · Inglés Cambridge A1&#8594;C2 · Para hispanohablantes</footer>
</body>
</html>"""

    os.makedirs(os.path.join(ROOT, f'es/{level_code}/vocabulary'), exist_ok=True)
    with open(os.path.join(ROOT, f'es/{level_code}/vocabulary/index.html'),'w') as f:
        f.write(vocab_html)
    print(f"  created es/{level_code}/vocabulary/index.html")

    # ── level hub ──
    hub_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<title>{lv_upper} {data['hub_label']} — Word Play para hispanohablantes</title>
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
    <strong>{label}</strong>
  </div>
  <div class="eyebrow">NIVEL {lv_upper} · PARA HISPANOHABLANTES</div>
  <h1>{label}</h1>
  <p class="section-desc">Gramática · Vocabulario — con explicaciones en español y comparaciones entre los dos idiomas</p>
  <div class="ch-grid">
    <a href="gramatica/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:8px">GRAMÁTICA</div>
      <div style="font-family:Georgia,serif;font-size:1.3rem;font-weight:700;color:white;margin-bottom:6px">Gramática {lv_upper}</div>
      <div style="font-family:var(--font-sans);font-size:.78rem;color:rgba(255,255,255,.55);line-height:1.5;margin-bottom:16px">{data['grammar_summary']}</div>
      <div style="font-family:var(--font-sans);font-size:.7rem;font-weight:700;color:var(--amber);letter-spacing:.5px">Estudiar &#8594;</div>
    </a>
    <a href="vocabulary/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:8px">VOCABULARIO</div>
      <div style="font-family:Georgia,serif;font-size:1.3rem;font-weight:700;color:white;margin-bottom:6px">Vocabulario {lv_upper}</div>
      <div style="font-family:var(--font-sans);font-size:.78rem;color:rgba(255,255,255,.55);line-height:1.5;margin-bottom:16px">{data['vocab_summary']}</div>
      <div style="font-family:var(--font-sans);font-size:.7rem;font-weight:700;color:var(--amber);letter-spacing:.5px">Estudiar &#8594;</div>
    </a>
  </div>
</div>
<footer class="site-footer">Word Play · Inglés Cambridge A1&#8594;C2 · Para hispanohablantes</footer>
</body>
</html>"""

    os.makedirs(os.path.join(ROOT, f'es/{level_code}'), exist_ok=True)
    with open(os.path.join(ROOT, f'es/{level_code}/index.html'),'w') as f:
        f.write(hub_html)
    print(f"  created es/{level_code}/index.html")

    return True


# ─── Build all three levels ───────────────────────────────────────────────────
for level_code, data in LEVELS.items():
    ok = build_level(level_code, data)
    if not ok:
        print(f"ERROR building {level_code}, aborting.")
        sys.exit(1)

# ─── Update es/index.html: activate B2-C2 ────────────────────────────────────
es_idx_path = os.path.join(ROOT,'es/index.html')
with open(es_idx_path) as f:
    content = f.read()

old = '''    <div style="background:#1A1A1A;border-radius:10px;padding:22px 20px;opacity:.5">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">NIVELES B2 — C2</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">Avanzado</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.45)">Proximamente</div>
    </div>'''

new = '''    <a href="b2/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">NIVEL B2</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">Intermedio Alto</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">FCE prep · 18 gramática · 16 vocabulario</div>
    </a>
    <a href="c1/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">NIVEL C1</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">Avanzado</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">CAE prep · 17 gramática · 7 vocabulario</div>
    </a>
    <a href="c2/index.html" class="sect-card">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">NIVEL C2</div>
      <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin-bottom:4px">Maestría</div>
      <div style="font-family:var(--font-sans);font-size:.75rem;color:rgba(255,255,255,.65)">CPE prep · 11 gramática · 7 vocabulario</div>
    </a>'''

if old in content:
    content = content.replace(old, new)
    with open(es_idx_path,'w') as f:
        f.write(content)
    print("\n  updated es/index.html: B2, C1, C2 now active")
else:
    print("\n  WARNING: could not find B2-C2 placeholder in es/index.html")

print("\nAll done. Spanish B2, C1, C2 fully scaffolded.")
