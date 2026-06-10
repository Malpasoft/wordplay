#!/usr/bin/env python3
"""Add missing English grammar chapters: A2 indirect questions, B1 wish/passive."""
import json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPECS = os.path.join(ROOT, 'scripts/chapter_specs')
gen = os.path.join(ROOT, 'scripts/gen_chapter.py')
errors = []

NEW_CHAPTERS = [
    # (lang, level, section, num, slug, title, subtitle, next_slug, next_num, next_title)
    # A2 grammar: indirect questions (Ch 19)
    ('en', 'a2', 'grammar', 19, 'indirect-questions',
     'Indirect Questions',
     'Could you tell me where…? · I wonder if…  · polite question structure',
     None, None, None),

    # B1 grammar: wish / if only (Ch 20), passive variations (Ch 21)
    ('en', 'b1', 'grammar', 20, 'wish-if-only',
     'Wish and If Only',
     'I wish I had… · If only I could… · regret and hypothetical past',
     'passive-variations', 21, 'Passive Variations'),

    ('en', 'b1', 'grammar', 21, 'passive-variations',
     'Passive Variations',
     'Reporting passives · get passive · double object passive',
     None, None, None),
]

for lang, level, section, num, slug, title, subtitle, ns, nn, nt in NEW_CHAPTERS:
    sp = {"lang":lang,"level":level,"section":section,"num":num,"slug":slug,
          "title":title,"subtitle":subtitle,
          "next_slug":ns,"next_num":nn,"next_title":nt}
    fpath = os.path.join(SPECS, f"{lang}-{level}-{section}-{slug}.json")
    with open(fpath,'w') as f:
        json.dump(sp,f,indent=2)
    result = subprocess.run(['python3', gen, fpath], capture_output=True, text=True)
    if result.returncode != 0:
        errors.append(f"FAIL {lang}-{level}-{slug}: {result.stderr[:200]}")
    else:
        print(f"  ok  {lang}/{level}/{section}/{slug}/")

if errors:
    for e in errors: print(e)
    sys.exit(1)

# ─── Update A2 grammar index ───────────────────────────────────────────────────
a2_gi = os.path.join(ROOT, 'a/a2/grammar/index.html')
with open(a2_gi) as f:
    content = f.read()

new_card = (
    '\n    <a href="indirect-questions/index.html" class="ch-card ch-card--grammar" id="gpc_a2_indirect-questions">\n'
    '      <div class="ch-num">Ch 19</div>\n'
    '      <h2>Indirect Questions</h2>\n'
    '      <p class="ch-desc">Could you tell me where&#8230;? · I wonder if&#8230; · polite question structure</p>'
    '<span class="ch-cta">Study &rarr;</span>\n'
    '    </a>'
)
content = content.replace('  </div>\n</div>\n<footer', new_card + '\n  </div>\n</div>\n<footer')
with open(a2_gi,'w') as f:
    f.write(content)
print("  updated a/a2/grammar/index.html")

# ─── Update B1 grammar index ──────────────────────────────────────────────────
b1_gi = os.path.join(ROOT, 'b/b1/grammar/index.html')
with open(b1_gi) as f:
    content = f.read()

new_cards = (
    '\n    <a href="wish-if-only/index.html" class="ch-card ch-card--grammar" id="gpc_b1_wish-if-only">\n'
    '      <div class="ch-num">Ch 20</div>\n'
    '      <h2>Wish and If Only</h2>\n'
    '      <p class="ch-desc">I wish I had&#8230; · If only I could&#8230; · regret and hypothetical past</p>'
    '<span class="ch-cta">Study &rarr;</span>\n'
    '    </a>\n'
    '    <a href="passive-variations/index.html" class="ch-card ch-card--grammar" id="gpc_b1_passive-variations">\n'
    '      <div class="ch-num">Ch 21</div>\n'
    '      <h2>Passive Variations</h2>\n'
    '      <p class="ch-desc">Reporting passives · get passive · double object passive</p>'
    '<span class="ch-cta">Study &rarr;</span>\n'
    '    </a>'
)
content = content.replace('  </div>\n</div>\n<footer', new_cards + '\n  </div>\n</div>\n<footer')
with open(b1_gi,'w') as f:
    f.write(content)
print("  updated b/b1/grammar/index.html")

print("Done.")
