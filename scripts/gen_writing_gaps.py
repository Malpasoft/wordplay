#!/usr/bin/env python3
"""Add missing writing chapters for C1 and C2 English."""
import json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPECS = os.path.join(ROOT, 'scripts/chapter_specs')

# ─── C1 writing: add article (was missing) ────────────────────────────────────
C1_WRITING = [
    (6, 'article', 'Article', 'CAE article · engaging opener · subheadings · 220–260 words'),
]

# ─── C2 writing: add 4 missing task types ─────────────────────────────────────
C2_WRITING = [
    (3, 'formal-letter', 'Formal Letter',  'CPE formal letter · correct register · opening/closing conventions'),
    (4, 'proposal',      'Proposal',        'CPE proposal · structured sections · recommendations · persuasive tone'),
    (5, 'report',        'Report',          'CPE report · impersonal register · headings · findings and conclusions'),
    (6, 'review',        'Review',          'CPE review · evaluative language · recommendation · 220–260 words'),
]

gen = os.path.join(ROOT, 'scripts/gen_chapter.py')
errors = []

for num, slug, title, subtitle in C1_WRITING:
    sp = {"lang":"en","level":"c1","section":"writing","num":num,"slug":slug,
          "title":title,"subtitle":subtitle,"next_slug":None,"next_num":None,"next_title":None}
    fpath = os.path.join(SPECS, f"en-c1-writing-{slug}.json")
    with open(fpath,'w') as f:
        json.dump(sp,f,indent=2)
    result = subprocess.run(['python3', gen, fpath], capture_output=True, text=True)
    if result.returncode != 0:
        errors.append(f"FAIL en-c1-writing-{slug}: {result.stderr[:200]}")
    else:
        print(f"  ok  en-c1-writing-{slug}")

for num, slug, title, subtitle in C2_WRITING:
    sp = {"lang":"en","level":"c2","section":"writing","num":num,"slug":slug,
          "title":title,"subtitle":subtitle,"next_slug":None,"next_num":None,"next_title":None}
    fpath = os.path.join(SPECS, f"en-c2-writing-{slug}.json")
    with open(fpath,'w') as f:
        json.dump(sp,f,indent=2)
    result = subprocess.run(['python3', gen, fpath], capture_output=True, text=True)
    if result.returncode != 0:
        errors.append(f"FAIL en-c2-writing-{slug}: {result.stderr[:200]}")
    else:
        print(f"  ok  en-c2-writing-{slug}")

if errors:
    for e in errors: print(e)
    sys.exit(1)

# ─── Update c1/writing/index.html ─────────────────────────────────────────────
c1_wi = os.path.join(ROOT, 'c/c1/writing/index.html')
with open(c1_wi) as f:
    content = f.read()

new_card = (
    '\n    <a href="article/index.html" class="ch-card ch-card--writing" id="wpc_c1_article">\n'
    '      <div class="ch-num">Ch 6</div>\n'
    '      <h2>Article</h2>\n'
    '      <p class="ch-desc">CAE article · engaging opener · subheadings · 220&#8211;260 words</p>'
    '<span class="ch-cta">Study &rarr;</span>\n'
    '    </a>'
)
content = content.replace('  </div>\n</div>\n<footer', new_card + '\n  </div>\n</div>\n<footer')
with open(c1_wi,'w') as f:
    f.write(content)
print(f"  updated c/c1/writing/index.html")

# ─── Update c2/writing/index.html ─────────────────────────────────────────────
c2_wi = os.path.join(ROOT, 'c/c2/writing/index.html')
with open(c2_wi) as f:
    content = f.read()

new_cards = ''
for num, slug, title, subtitle in C2_WRITING:
    new_cards += (
        f'\n    <a href="{slug}/index.html" class="ch-card ch-card--writing" id="wpc_c2_{slug}">\n'
        f'      <div class="ch-num">Ch {num}</div>\n'
        f'      <h2>{title}</h2>\n'
        f'      <p class="ch-desc">{subtitle}</p><span class="ch-cta">Study &rarr;</span>\n'
        f'    </a>'
    )
content = content.replace('  </div>\n</div>\n<footer', new_cards + '\n  </div>\n</div>\n<footer')
with open(c2_wi,'w') as f:
    f.write(content)
print(f"  updated c/c2/writing/index.html")

print("Done.")
