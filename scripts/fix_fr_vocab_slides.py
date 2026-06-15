#!/usr/bin/env python3
"""
Rebuild fr/ vocab slides.html files to use the bilingual bi-block layout
(Français → English) instead of English-only overview-desc format.

Extracts WORDS from each chapter's flashcards.html, then rebuilds the
slide-deck section in the matching slides.html.
"""
import json, re, glob, os

SLIDES_CSS_ADDON = """.bi-block{border-left:3px solid var(--amber);padding:8px 0 8px 14px;margin:10px 0}
.bi-row{display:flex;align-items:baseline;gap:8px;padding:4px 0}
.bi-fr{flex:1;color:var(--muted);font-size:.86rem;font-style:italic}
.bi-sep{color:var(--amber);font-weight:700;font-size:.9rem;min-width:16px;text-align:center}
.bi-en{flex:1;color:var(--ink);font-size:.86rem}
.fr-label,.en-label{font-family:var(--font-sans);font-size:.58rem;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:var(--muted);margin-bottom:4px}"""

def extract_words(fc_path):
    with open(fc_path, encoding='utf-8') as f:
        content = f.read()
    m = re.search(r'var WORDS\s*=\s*(\[.*?\]);', content, re.DOTALL)
    if not m:
        return None
    return json.loads(m.group(1))

def fr_word(def_str):
    """Extract French word from 'chien — ...' format."""
    if ' — ' in def_str:
        return def_str.split(' — ')[0].strip()
    if ' - ' in def_str:
        return def_str.split(' - ')[0].strip()
    return def_str.strip()

def build_slide_deck(words):
    """Build the full <div id="slide-deck">...</div> with bilingual bi-block layout."""
    chunk_size = 4
    slides_html = '<div id="slide-deck">'

    for i in range(0, len(words), chunk_size):
        chunk = words[i:i+chunk_size]
        start = i + 1
        end = i + len(chunk)
        label = f"Mots {start}–{end}" if len(chunk) > 1 else f"Mot {start}"

        slide = f'<div class="slide"><div class="slide-card">'
        slide += f'<div class="slide-header"><h2>{label}</h2></div>'
        slide += '<div class="bi-block">'
        slide += '<div style="display:flex;gap:8px;margin-bottom:6px">'
        slide += '<div style="flex:1" class="fr-label">Français</div>'
        slide += '<div style="width:20px"></div>'
        slide += '<div style="flex:1" class="en-label">English</div>'
        slide += '</div>'

        for w in chunk:
            fr = fr_word(w.get('def', ''))
            en = w['word']
            ipa = w.get('ipa', '')
            ipa_html = f' <span style="color:var(--muted);font-size:.78rem">{ipa}</span>' if ipa else ''
            slide += '<div class="bi-row">'
            slide += f'<div class="bi-fr">{fr}</div>'
            slide += '<div class="bi-sep">→</div>'
            slide += f'<div class="bi-en"><strong>{en}</strong>{ipa_html}</div>'
            slide += '</div>'

        slide += '</div>'  # end bi-block

        # Examples section
        examples = [w.get('ex', '') for w in chunk if w.get('ex')]
        if examples:
            slide += '<div style="margin-top:14px;padding-top:10px;border-top:1px solid var(--hairline)">'
            slide += '<div style="font-family:var(--font-sans);font-size:.65rem;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--muted);margin-bottom:6px">Exemples</div>'
            for ex in examples:
                slide += f'<div style="font-size:.87rem;color:var(--muted);padding:3px 0;font-style:italic">"{ex}"</div>'
            slide += '</div>'

        slide += '</div></div>'  # end slide-card, slide
        slides_html += slide

    slides_html += '</div>'
    return slides_html

def process_slides(slides_path, words):
    with open(slides_path, encoding='utf-8') as f:
        content = f.read()

    # Replace slide-deck block
    new_deck = build_slide_deck(words)
    content = re.sub(
        r'<div id="slide-deck">.*?</div>\s*(?=\s*<div class="deck-nav">)',
        new_deck + '\n  ',
        content, flags=re.DOTALL
    )

    # Fix Prev button
    content = content.replace('>&#9664; Prev<', '>&#9664; Préc<')

    # Inject CSS if not already present
    if 'bi-block' not in content:
        content = content.replace('</style>', SLIDES_CSS_ADDON + '\n</style>', 1)

    # Remove overview-row CSS if present (no longer needed)
    content = re.sub(r'\.overview-row\{[^}]*\}\s*', '', content)
    content = re.sub(r'\.overview-label\{[^}]*\}\s*', '', content)
    content = re.sub(r'\.overview-desc\{[^}]*\}\s*', '', content)

    with open(slides_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    slides_files = glob.glob('fr/*/vocabulaire/*/slides.html')
    updated = 0
    skipped = 0

    for slides_path in sorted(slides_files):
        if 'overview-row' not in open(slides_path, encoding='utf-8').read():
            skipped += 1
            continue

        chapter_dir = os.path.dirname(slides_path)
        fc_path = os.path.join(chapter_dir, 'flashcards.html')

        if not os.path.exists(fc_path):
            print(f'  SKIP (no flashcards): {slides_path}')
            continue

        words = extract_words(fc_path)
        if not words:
            print(f'  SKIP (no WORDS): {slides_path}')
            continue

        process_slides(slides_path, words)
        print(f'  OK  {slides_path}')
        updated += 1

    print(f'\nUpdated {updated}, skipped {skipped} (already bilingual)')

if __name__ == '__main__':
    main()
