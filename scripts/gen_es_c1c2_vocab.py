#!/usr/bin/env python3
"""Mirror the English C1/C2 vocab expansion to the Spanish track."""
import json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPECS = os.path.join(ROOT, 'scripts/chapter_specs')
gen = os.path.join(ROOT, 'scripts/gen_chapter.py')

NEW_VOCAB = {
    'c1': [
        (8,  'abstract-nouns',       'Abstract Nouns',        'concept · phenomenon · tendency · perception · assumption'),
        (9,  'academic-verbs',       'Academic Verbs',        'argue · suggest · demonstrate · highlight · indicate · conclude'),
        (10, 'attitudes-opinions',   'Attitudes & Opinions',  'controversial · sceptical · compelling · contentious · persuasive'),
        (11, 'cause-effect',         'Cause and Effect',      'consequently · therefore · stems from · brings about · leads to'),
        (12, 'contrast-concession',  'Contrast & Concession', 'despite · nevertheless · whereas · albeit · notwithstanding'),
        (13, 'formal-synonyms',      'Formal Synonyms',       'commence · endeavour · facilitate · obtain · regarding · sufficient'),
        (14, 'topic-vocabulary-arts','Arts & Culture',        'aesthetic · portrayal · genre · narrative · interpretation · critique'),
    ],
    'c2': [
        (8,  'connotation-register', 'Connotation & Register',  'derogatory · euphemism · loaded language · understatement · irony'),
        (9,  'literary-devices',     'Literary Devices',        'metaphor · simile · allusion · personification · paradox · irony'),
        (10, 'persuasive-language',  'Persuasive Language',     'rhetoric · ethos · pathos · logos · assertion · refutation'),
        (11, 'precision-vocabulary', 'Precision Vocabulary',    'marginal · negligible · substantial · nuanced · ambiguous · vague'),
        (12, 'spoken-written-modes', 'Spoken vs Written Modes', 'hedging · vagueness in speech · written formality · mode continuum'),
    ],
}

errors = []
added = {'c1': [], 'c2': []}

for level_code, vocab in NEW_VOCAB.items():
    for i, (num, slug, title, subtitle) in enumerate(vocab):
        nxt = vocab[i+1] if i+1 < len(vocab) else None
        sp = {"lang":"es","level":level_code,"section":"vocabulary","num":num,"slug":slug,
              "title":title,"subtitle":subtitle,
              "next_slug":nxt[1] if nxt else None,"next_num":nxt[0] if nxt else None,
              "next_title":nxt[2] if nxt else None}
        fpath = os.path.join(SPECS, f"es-{level_code}-vocabulary-{slug}.json")
        with open(fpath,'w') as f:
            json.dump(sp,f,indent=2,ensure_ascii=False)
        result = subprocess.run(['python3', gen, fpath], capture_output=True, text=True)
        if result.returncode != 0:
            errors.append(f"FAIL es-{level_code}-vocab-{slug}: {result.stderr[:200]}")
        else:
            added[level_code].append((num, slug, title, subtitle))
            print(f"  ok  es/{level_code}/vocabulary/{slug}/")

if errors:
    for e in errors: print(e)
    sys.exit(1)

# ─── Update vocabulary index files ───────────────────────────────────────────
for level_code, new_topics in added.items():
    vi = os.path.join(ROOT, f'es/{level_code}/vocabulary/index.html')
    with open(vi) as f:
        content = f.read()
    for num, slug, title, subtitle in new_topics:
        card = (
            f'\n    <a href="{slug}/index.html" class="ch-card ch-card--vocab" id="vpc_{level_code}_{slug}">\n'
            f'      <div class="ch-num">V{num}</div>\n'
            f'      <h2>{title}</h2>\n'
            f'      <p class="ch-desc">{subtitle}</p><span class="ch-cta">Estudiar &#8594;</span>\n'
            f'    </a>'
        )
        content = content.replace('  </div>\n</div>\n<footer', card + '\n  </div>\n</div>\n<footer')
    old_count = '7 temas'
    new_count = f'{7 + len(new_topics)} temas'
    content = content.replace(old_count, new_count)
    with open(vi,'w') as f:
        f.write(content)
    print(f"  updated es/{level_code}/vocabulary/index.html (+{len(new_topics)} → {7+len(new_topics)} topics)")

print("Done.")
