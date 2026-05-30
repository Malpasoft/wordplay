#!/usr/bin/env python3
"""Add missing English vocabulary topics for C1 and C2."""
import json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPECS = os.path.join(ROOT, 'scripts/chapter_specs')
gen = os.path.join(ROOT, 'scripts/gen_chapter.py')
BASE_V = 'v123'
DARK_V = 'v109'

# ─── New C1 vocabulary (7 more → 14 total, proper CAE coverage) ───────────────
C1_VOCAB = [
    (8,  'abstract-nouns',       'Abstract Nouns',        'concept · phenomenon · tendency · perception · assumption'),
    (9,  'academic-verbs',       'Academic Verbs',        'argue · suggest · demonstrate · highlight · indicate · conclude'),
    (10, 'attitudes-opinions',   'Attitudes & Opinions',  'controversial · skeptical · compelling · contentious · persuasive'),
    (11, 'cause-effect',         'Cause and Effect',      'consequently · therefore · stems from · brings about · leads to'),
    (12, 'contrast-concession',  'Contrast & Concession', 'despite · nevertheless · whereas · albeit · notwithstanding'),
    (13, 'formal-synonyms',      'Formal Synonyms',       'commence · endeavour · facilitate · obtain · regarding · sufficient'),
    (14, 'topic-vocabulary-arts','Arts & Culture',        'aesthetic · portrayal · genre · narrative · interpretation · critique'),
]

# ─── New C2 vocabulary (5 more → 12 total, proper CPE coverage) ──────────────
C2_VOCAB = [
    (8,  'connotation-register', 'Connotation & Register',  'derogatory · euphemism · loaded language · understatement · irony'),
    (9,  'literary-devices',     'Literary Devices',        'metaphor · simile · allusion · personification · paradox · irony'),
    (10, 'persuasive-language',  'Persuasive Language',     'rhetoric · ethos · pathos · logos · assertion · refutation'),
    (11, 'precision-vocabulary', 'Precision Vocabulary',    'distinguish tiny meaning differences · marginal · negligible · substantial'),
    (12, 'spoken-written-modes', 'Spoken vs Written Modes', 'hedging · vagueness in speech · written formality · mode continuum'),
]

errors = []
new_c1 = []
new_c2 = []

for i, (num, slug, title, subtitle) in enumerate(C1_VOCAB):
    nxt = C1_VOCAB[i+1] if i+1 < len(C1_VOCAB) else None
    sp = {"lang":"en","level":"c1","section":"vocabulary","num":num,"slug":slug,
          "title":title,"subtitle":subtitle,
          "next_slug":nxt[1] if nxt else None,"next_num":nxt[0] if nxt else None,
          "next_title":nxt[2] if nxt else None}
    fpath = os.path.join(SPECS, f"en-c1-vocabulary-{slug}.json")
    with open(fpath,'w') as f:
        json.dump(sp,f,indent=2)
    result = subprocess.run(['python3', gen, fpath], capture_output=True, text=True)
    if result.returncode != 0:
        errors.append(f"FAIL c1-vocab-{slug}: {result.stderr[:200]}")
    else:
        new_c1.append((num, slug, title, subtitle))
        print(f"  ok  en/c1/vocabulary/{slug}/")

for i, (num, slug, title, subtitle) in enumerate(C2_VOCAB):
    nxt = C2_VOCAB[i+1] if i+1 < len(C2_VOCAB) else None
    sp = {"lang":"en","level":"c2","section":"vocabulary","num":num,"slug":slug,
          "title":title,"subtitle":subtitle,
          "next_slug":nxt[1] if nxt else None,"next_num":nxt[0] if nxt else None,
          "next_title":nxt[2] if nxt else None}
    fpath = os.path.join(SPECS, f"en-c2-vocabulary-{slug}.json")
    with open(fpath,'w') as f:
        json.dump(sp,f,indent=2)
    result = subprocess.run(['python3', gen, fpath], capture_output=True, text=True)
    if result.returncode != 0:
        errors.append(f"FAIL c2-vocab-{slug}: {result.stderr[:200]}")
    else:
        new_c2.append((num, slug, title, subtitle))
        print(f"  ok  en/c2/vocabulary/{slug}/")

if errors:
    for e in errors: print(e)
    sys.exit(1)

# ─── Update C1 vocabulary/index.html ─────────────────────────────────────────
c1_vi = os.path.join(ROOT, 'c/c1/vocabulary/index.html')
with open(c1_vi) as f:
    content = f.read()

for num, slug, title, subtitle in new_c1:
    card = (
        f'\n    <a href="{slug}/index.html" class="ch-card ch-card--vocab" id="vpc_c1_{slug}">\n'
        f'      <div class="ch-num">V{num}</div>\n'
        f'      <h2>{title}</h2>\n'
        f'      <p class="ch-desc">{subtitle}</p><span class="ch-cta">Study &rarr;</span>\n'
        f'    </a>'
    )
    content = content.replace('  </div>\n</div>\n<footer', card + '\n  </div>\n</div>\n<footer')

# Update section-desc count
content = content.replace('7 topics', '14 topics')
with open(c1_vi,'w') as f:
    f.write(content)
print(f"  updated c/c1/vocabulary/index.html (+{len(new_c1)} topics → 14)")

# ─── Update C2 vocabulary/index.html ─────────────────────────────────────────
c2_vi = os.path.join(ROOT, 'c/c2/vocabulary/index.html')
with open(c2_vi) as f:
    content = f.read()

for num, slug, title, subtitle in new_c2:
    card = (
        f'\n    <a href="{slug}/index.html" class="ch-card ch-card--vocab" id="vpc_c2_{slug}">\n'
        f'      <div class="ch-num">V{num}</div>\n'
        f'      <h2>{title}</h2>\n'
        f'      <p class="ch-desc">{subtitle}</p><span class="ch-cta">Study &rarr;</span>\n'
        f'    </a>'
    )
    content = content.replace('  </div>\n</div>\n<footer', card + '\n  </div>\n</div>\n<footer')

content = content.replace('7 topics', '12 topics')
with open(c2_vi,'w') as f:
    f.write(content)
print(f"  updated c/c2/vocabulary/index.html (+{len(new_c2)} topics → 12)")

print("Done.")
