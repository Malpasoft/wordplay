#!/usr/bin/env python3
"""Generate spec JSON files for all missing Spanish A1 chapters."""
import json, os

OUT = os.path.join(os.path.dirname(__file__), 'chapter_specs')
os.makedirs(OUT, exist_ok=True)

# ─── Missing Spanish A1 Grammar chapters ──────────────────────────────────────
# Existing: articulos, can, demostrativos, have-got, plurales, preposiciones,
#           present-simple, pronombres, there-is-there-are, to-be  (10 chapters)
# We add chapters 11-24 (14 chapters)

GRAMMAR = [
    # (num, slug, title, subtitle)
    (11, 'present-continuous',    'Present Continuous',     'estoy hablando · está comiendo · estamos aprendiendo'),
    (12, 'can-cant',              'Can and Can\'t',          'puedo · no puedo · ¿puedes?'),
    (13, 'imperatives',           'Imperatives',             'abre · no hables · escucha · ven aquí'),
    (14, 'adjectives-basic',      'Basic Adjectives',        'grande · pequeño · rápido · difícil'),
    (15, 'possessive-adjectives', 'Possessive Adjectives',   'my · your · his · her · our · their'),
    (16, 'possessives',           'Possessives',             'mine · yours · his · hers · ours · theirs'),
    (17, 'question-words',        'Question Words',          'what · where · when · who · why · how'),
    (18, 'prepositions-place',    'Prepositions of Place',   'in · on · under · next to · behind · in front of'),
    (19, 'prepositions-time',     'Prepositions of Time',    'at · on · in · before · after · during'),
    (20, 'some-any',              'Some and Any',            'some friends · any money · some milk · any ideas'),
    (21, 'going-to-future',       'Going to Future',         'voy a estudiar · vas a venir · va a llover'),
    (22, 'adverbs-frequency',     'Adverbs of Frequency',    'always · usually · sometimes · rarely · never'),
    (23, 'simple-past-regular',   'Simple Past Regular',     'I worked · she played · they listened'),
    (24, 'simple-past-irregular', 'Simple Past Irregular',   'went · saw · ate · had · came · said'),
]

for i, (num, slug, title, subtitle) in enumerate(GRAMMAR):
    next_entry = GRAMMAR[i + 1] if i + 1 < len(GRAMMAR) else None
    sp = {
        "lang": "es",
        "level": "a1",
        "section": "grammar",
        "num": num,
        "slug": slug,
        "title": title,
        "subtitle": subtitle,
        "next_slug": next_entry[1] if next_entry else None,
        "next_num": next_entry[0] if next_entry else None,
        "next_title": next_entry[2] if next_entry else None,
    }
    fname = f"es-a1-grammar-{slug}.json"
    with open(os.path.join(OUT, fname), 'w') as f:
        json.dump(sp, f, indent=2, ensure_ascii=False)
    print(f"  wrote {fname}")

# ─── Missing Spanish A1 Vocabulary chapters ───────────────────────────────────
# Existing: animals, colours, daily-routines, family, food-and-drink, numbers-and-time  (6 topics)
# We add topics 7-12 (6 topics)

VOCAB = [
    # (num, slug, title, subtitle)
    (7,  'clothes',        'Clothes',         'shirt · trousers · dress · coat · shoes · hat'),
    (8,  'hobbies',        'Hobbies',         'reading · sport · music · cooking · games · travel'),
    (9,  'house-and-rooms','House and Rooms',  'kitchen · bedroom · bathroom · living room · garden'),
    (10, 'jobs',           'Jobs',            'teacher · doctor · engineer · driver · chef · nurse'),
    (11, 'places-in-town', 'Places in Town',  'school · hospital · bank · station · park · market'),
    (12, 'weather',        'Weather',         'sunny · cloudy · raining · cold · hot · windy'),
]

for i, (num, slug, title, subtitle) in enumerate(VOCAB):
    next_entry = VOCAB[i + 1] if i + 1 < len(VOCAB) else None
    sp = {
        "lang": "es",
        "level": "a1",
        "section": "vocabulary",
        "num": num,
        "slug": slug,
        "title": title,
        "subtitle": subtitle,
        "next_slug": next_entry[1] if next_entry else None,
        "next_num": next_entry[0] if next_entry else None,
        "next_title": next_entry[2] if next_entry else None,
    }
    fname = f"es-a1-vocabulary-{slug}.json"
    with open(os.path.join(OUT, fname), 'w') as f:
        json.dump(sp, f, indent=2, ensure_ascii=False)
    print(f"  wrote {fname}")

print(f"\nDone. {len(GRAMMAR)} grammar + {len(VOCAB)} vocab = {len(GRAMMAR)+len(VOCAB)} spec files.")
