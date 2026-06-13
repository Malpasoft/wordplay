# -*- coding: utf-8 -*-
"""Generate grammar printables.html from worksheet + slides data.

Covers:
  es/a1/gramatica/*           (lang=es, 10 missing)
  espanol-en/a1/grammar/*     (lang=en, all 22)
  espanol-en/a2/grammar/*     (lang=en, all 22)
  fr/b1/grammaire/*           (lang=fr, all 22)
  fr/b2/grammaire/*           (lang=fr, all 17)

For each chapter missing printables.html:
  1. Parse worksheet.html: exercises, questions, answers
  2. Parse slides.html: summary-slide rows (lesson reference)
  3. Generate printables.html with real content (3 sections)
  4. Add printables activity card to chapter index.html
  5. Add Imprimibles/Printables nav btn to sibling pages

Usage: python3 scripts/gen_printables.py [--sample] [--track TRACK]
  --sample   process 3 chapters only
  --track    es | esen | fr
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── Language config ───────────────────────────────────────────────────────────
LANG = {
    'es': {
        'html_lang': 'es',
        'dark_btn': '&#9680; Oscuro',
        'nav': ['Lección', 'Repaso', 'Juego', 'Imprimibles'],
        'nav_hrefs': ['slides.html', 'worksheet.html', 'game.html', 'printables.html'],
        'hub_title_suffix': ' — Imprimibles',
        'card_labels': ['LECCIÓN', 'REPASO', 'RESPUESTAS'],
        'card_titles': ['Referencia', 'Ejercicios', 'Clave de Respuestas'],
        'card_descs': [
            'Reglas gramaticales y ejemplos',
            'Ejercicios de práctica para imprimir',
            'Respuestas correctas para corregir'
        ],
        'hub_print_all': 'Imprimir todo',
        'view_btn': 'Ver',
        'print_btn': 'Imprimir',
        'section_lesson_h2': 'Referencia gramatical',
        'section_ws_suffix': ' — Ejercicios',
        'section_key_suffix': ' — Respuestas',
        'footer': 'Word Play · Cambridge Inglés A1&#8594;C2',
        'title_prefix': 'A1 · ',
        'col_headers': ['Forma', 'Ejemplo'],
        'activity_card': (
            '  <a href="printables.html" class="activity-card" data-activity="print" style="--ac-color:#6B6B6B">\n'
            '    <span class="ac-title">Imprimibles</span>\n'
            '    <p class="ac-desc">Ficha de referencia, ejercicios para imprimir y clave de respuestas</p>\n'
            '    <span class="ac-arrow">&#8594;</span>\n'
            '  </a>\n'
        ),
        'nav_btn_label': 'Imprimibles',
        'answer_key_intro': 'Respuestas',
    },
    'en': {
        'html_lang': 'en',
        'dark_btn': '&#9680; Dark',
        'nav': ['Lesson', 'Review', 'Game', 'Printables'],
        'nav_hrefs': ['slides.html', 'worksheet.html', 'game.html', 'printables.html'],
        'hub_title_suffix': ' — Printables',
        'card_labels': ['LESSON', 'REVIEW', 'ANSWER KEY'],
        'card_titles': ['Lesson Reference', 'Review Exercises', 'Answer Key'],
        'card_descs': [
            'Grammar rules and examples for self-study',
            'Fill-in and gap-fill practice tasks',
            'Correct answers for all exercises'
        ],
        'hub_print_all': 'Print all',
        'view_btn': 'View',
        'print_btn': 'Print',
        'section_lesson_h2': 'Grammar Reference',
        'section_ws_suffix': ' — Exercises',
        'section_key_suffix': ' — Answer Key',
        'footer': 'Word Play · Spanish for English Speakers',
        'title_prefix': '',
        'col_headers': ['Form', 'Example'],
        'activity_card': (
            '  <a href="printables.html" class="activity-card" data-activity="print" style="--ac-color:#6B6B6B">\n'
            '    <span class="ac-title">Printables</span>\n'
            '    <p class="ac-desc">Reference card, printable exercises and answer key</p>\n'
            '    <span class="ac-arrow">&#8594;</span>\n'
            '  </a>\n'
        ),
        'nav_btn_label': 'Printables',
        'answer_key_intro': 'Answers',
    },
    'fr': {
        'html_lang': 'fr',
        'dark_btn': '&#9680; Sombre',
        'nav': ['Leçon', 'Exercices', 'Jeu', 'Imprimables'],
        'nav_hrefs': ['slides.html', 'worksheet.html', 'game.html', 'printables.html'],
        'hub_title_suffix': ' — Imprimables',
        'card_labels': ['LEÇON', 'EXERCICES', 'CORRIGÉ'],
        'card_titles': ['Référence de cours', 'Exercices', 'Corrigé'],
        'card_descs': [
            'Règles de grammaire et exemples',
            "Exercices à compléter à l'écrit",
            'Réponses correctes pour la correction'
        ],
        'hub_print_all': 'Tout imprimer',
        'view_btn': 'Voir',
        'print_btn': 'Imprimer',
        'section_lesson_h2': 'Référence grammaticale',
        'section_ws_suffix': ' — Exercices',
        'section_key_suffix': ' — Corrigé',
        'footer': 'Word Play · Cambridge Anglais B1&#8594;B2',
        'title_prefix': '',
        'col_headers': ['Forme', 'Exemple'],
        'activity_card': (
            '  <a href="printables.html" class="activity-card" data-activity="print" style="--ac-color:#6B6B6B">\n'
            '    <span class="ac-title">Imprimables</span>\n'
            '    <p class="ac-desc">Fiche de référence, exercices à imprimer et corrigé</p>\n'
            '    <span class="ac-arrow">&#8594;</span>\n'
            '  </a>\n'
        ),
        'nav_btn_label': 'Imprimables',
        'answer_key_intro': 'Réponses',
    },
}

# ── Tracks to process ─────────────────────────────────────────────────────────
TRACKS = [
    ('es',      os.path.join(ROOT, 'es',          'a1', 'gramatica')),
    ('en',      os.path.join(ROOT, 'espanol-en',  'a1', 'grammar')),
    ('en',      os.path.join(ROOT, 'espanol-en',  'a2', 'grammar')),
    ('en',      os.path.join(ROOT, 'espanol-en',  'b1', 'grammar')),
    ('en',      os.path.join(ROOT, 'espanol-en',  'b2', 'grammar')),
    ('fr',      os.path.join(ROOT, 'fr',          'a1', 'grammaire')),
    ('fr',      os.path.join(ROOT, 'fr',          'a2', 'grammaire')),
    ('fr',      os.path.join(ROOT, 'fr',          'b1', 'grammaire')),
    ('fr',      os.path.join(ROOT, 'fr',          'b2', 'grammaire')),
    ('fr',      os.path.join(ROOT, 'fr',          'b1', 'redaction')),
    ('fr',      os.path.join(ROOT, 'fr',          'b2', 'redaction')),
]

# Also process es/a2, a1 (full tracks if needed by caller)
ALL_TRACKS = TRACKS + [
    ('es',  os.path.join(ROOT, 'es', 'a2', 'gramatica')),
    ('es',  os.path.join(ROOT, 'es', 'b1', 'gramatica')),
    ('es',  os.path.join(ROOT, 'es', 'b2', 'gramatica')),
]

# ── Regex helpers ─────────────────────────────────────────────────────────────
H1_RE = re.compile(r'<h1[^>]*>(.*?)</h1>', re.S)
TAG_RE = re.compile(r'<[^>]+>')
EX_SECTION_RE = re.compile(r'<section[^>]+class="exercise"[^>]+id="(ex\d+)"[^>]*>(.*?)</section>', re.S)
Q_RE = re.compile(r'<div class="q"[^>]*>.*?<div class="q-num">(\d+)</div>\s*<div class="q-text">(.*?)</div>(.*?)</div>', re.S)
CHOICE_GROUP_RE = re.compile(r'<div class="choice-group"[^>]*data-q="([^"]+)"[^>]*data-answer="([^"]*)"')
CHOICE_BTN_RE = re.compile(r'<button[^>]*class="choice-btn"[^>]*data-value="([^"]*)"')
ANSWERS_RE = re.compile(r'window\.ANSWERS\s*=\s*(\{[\s\S]*?\})\s*;')
EX_TITLES_RE = re.compile(r'window\.EXERCISE_TITLES\s*=\s*(\{[^}]*\})\s*;')
SUMMARY_SLIDE_RE = re.compile(r'class="[^"]*summary-slide[^"]*"[^>]*>(.*?)(?=</div>\s*</div>|<div class="slide|$)', re.S)
SUMMARY_ROW_INNER_RE = re.compile(r'<div class="summary-row">(.*?)(?=<div class="summary-row">|</div>\s*</div>)', re.S)
SUMMARY_LABEL_RE = re.compile(r'<div class="label">(.*?)</div>', re.S)
SUMMARY_FORM_RE = re.compile(r'<div class="form">(.*?)</div>', re.S)
SUMMARY_EX_RE = re.compile(r'<div class="ex">(.*?)</div>', re.S)
NAV_RE = re.compile(r'<nav class="chapter-nav">(.*?)</nav>', re.S)
ACTIVITY_CARDS_RE = re.compile(r'(</div>\s*</div>\s*<footer)', re.S)


def strip_tags(s):
    return TAG_RE.sub('', s).strip()


def parse_worksheet_old(html):
    """Parse old-style espanol-en/a1 worksheets (inline q divs, no ANSWERS JS).

    Pattern: <div style="..."><div style="font-weight:700">N. question text</div>
    <select name="qN"> / <input name="qN">
    <div id="eN"><b>Answer:</b> answer text</div>
    """
    title = ''
    m = H1_RE.search(html)
    if m:
        title = strip_tags(m.group(1)).replace(' — Practice', '').replace(' — Review', '')

    questions = []
    # Find question blocks: numbered divs with Answer reveal
    q_blocks = re.findall(
        r'<div[^>]*>\s*<div[^>]*style="font-weight:700[^"]*">\s*(\d+)\.\s*(.*?)</div>'
        r'(.*?)'
        r'<div id="e\1"[^>]*>\s*<b>Answer:</b>\s*(.*?)</p>',
        html, re.S
    )
    if not q_blocks:
        # fallback: simpler pattern
        q_blocks = re.findall(
            r'<div[^>]*style="font-weight:700[^"]*">\s*(\d+)\.\s*(.*?)</div>'
            r'.*?<b>Answer:</b>\s*(.*?)<',
            html, re.S
        )
        for qnum, qtext, answer in q_blocks:
            questions.append({'num': qnum, 'text': strip_tags(qtext).strip(),
                              'choices': [], 'qid': f'q{qnum}',
                              'answer': strip_tags(answer).strip()})
    else:
        for qnum, qtext, qbody, answer in q_blocks:
            choices = re.findall(r'<option value="[^"]*">([^<]+)</option>', qbody)
            choices = [c for c in choices if not c.startswith('--')]
            questions.append({'num': qnum, 'text': strip_tags(qtext).strip(),
                              'choices': choices, 'qid': f'q{qnum}',
                              'answer': strip_tags(answer).strip()})

    if not questions:
        return title, [], {}

    # Wrap in single exercise
    exercises = [{'id': 'ex1', 'title': 'Practice', 'instruct': '', 'questions': questions}]
    return title, exercises, {}


def parse_worksheet(html):
    """Return (title, exercises, text_answers) where:
    exercises = [{'id': 'ex1', 'title': '...', 'questions': [{'num':1,'text':'...','choices':[],'qid':'...','answer':'...'}]}]
    text_answers = {'e2q1': 'older', ...}  (for non-MC)
    """
    title = ''
    m = H1_RE.search(html)
    if m:
        title = strip_tags(m.group(1))

    # Parse EXERCISE_TITLES
    ex_titles = {}
    et = EX_TITLES_RE.search(html)
    if et:
        try:
            ex_titles = json.loads(et.group(1))
        except Exception:
            raw = et.group(1)
            for k, v in re.findall(r'(\w+):"([^"]*)"', raw):
                ex_titles[k] = v

    # Parse ANSWERS (text input answers)
    text_answers = {}
    am = ANSWERS_RE.search(html)
    if am:
        try:
            raw = json.loads(am.group(1))
            for k, v in raw.items():
                text_answers[k] = v.get('answer', '') if isinstance(v, dict) else str(v)
        except Exception:
            pass

    # Parse exercises
    exercises = []
    for ex_id, ex_body in EX_SECTION_RE.findall(html):
        # Get title from ex-title div
        title_m = re.search(r'<div class="ex-title">(.*?)</div>', ex_body)
        ex_title = strip_tags(title_m.group(1)) if title_m else ex_titles.get(ex_id, ex_id)
        instruct_m = re.search(r'<div class="ex-instruct">(.*?)</div>', ex_body)
        instruct = strip_tags(instruct_m.group(1)) if instruct_m else ''

        # Parse questions in this section
        questions = []
        # Find all q divs in order
        for qm in re.finditer(r'<div class="q"[^>]*>(.*?)</div\s*>', ex_body, re.S):
            qblock = qm.group(1)
            num_m = re.search(r'<span class="q-num">(\d+)</span>', qblock)
            text_m = re.search(r'<div class="q-text">(.*?)</div>', qblock, re.S)
            if not text_m:
                continue
            num = num_m.group(1) if num_m else '?'
            qtext = strip_tags(text_m.group(1))
            # Check for choice-group (MC)
            cg = CHOICE_GROUP_RE.search(qblock)
            choices = []
            answer = ''
            qid = ''
            if cg:
                qid = cg.group(1)
                answer = cg.group(2)
                choices = CHOICE_BTN_RE.findall(qblock)
            else:
                # text input
                inp = re.search(r'data-q="([^"]+)"', qblock)
                if inp:
                    qid = inp.group(1)
                    answer = text_answers.get(qid, '')
                else:
                    # may be in ANSWERS via a different key pattern
                    qid = f'{ex_id}q{num}'
                    answer = text_answers.get(qid, '')
            questions.append({'num': num, 'text': qtext, 'choices': choices,
                              'qid': qid, 'answer': answer})

        exercises.append({'id': ex_id, 'title': ex_title, 'instruct': instruct,
                          'questions': questions})

    return title, exercises, text_answers


def parse_summary(html):
    """Extract summary-slide rows from slides.html."""
    rows = []
    # Extract all label/form/ex groups by finding all three divs consecutively
    labels = SUMMARY_LABEL_RE.findall(html)
    forms = SUMMARY_FORM_RE.findall(html)
    exs = SUMMARY_EX_RE.findall(html)
    n = min(len(labels), len(forms))
    for i in range(n):
        rows.append({
            'label': strip_tags(labels[i]),
            'form': strip_tags(forms[i]),
            'ex': strip_tags(exs[i]) if i < len(exs) else '',
        })
    return rows


def build_printable(slug, title, level_label, depth, lang, summary_rows, exercises):
    lc = LANG[lang]
    prefix = '../' * depth
    # Determine level display (e.g. "A1 · ")
    lvl_eyebrow = level_label + ' · ' if level_label else ''

    # ── Hub section ───────────────────────────────────────────────
    cards_html = ''
    for i in range(3):
        cards_html += f'''    <div class="ph-hub-card">
      <div class="ph-hub-card-label">{lc['card_labels'][i]}</div>
      <div class="ph-hub-card-title">{lc['card_titles'][i]}</div>
      <div class="ph-hub-card-desc">{lc['card_descs'][i]}</div>
      <div class="ph-hub-btn-row">
        <a href="#ph-{['lesson','worksheet','key'][i]}" class="ph-hub-btn ph-hub-btn-view">{lc['view_btn']}</a>
        <button onclick="wpPrint('{['lesson','worksheet','key'][i]}')" class="ph-hub-btn ph-hub-btn-print">{lc['print_btn']}</button>
      </div>
    </div>\n'''

    # ── Lesson reference section ───────────────────────────────────
    if summary_rows:
        rows_html = ''.join(
            f'<tr><td>{r["label"]}</td><td><strong>{r["form"]}</strong></td><td><em>{r["ex"]}</em></td></tr>\n'
            for r in summary_rows if r['label'] or r['form']
        )
        lesson_body = f'''<h1>{title}</h1>
<h2>{lc['section_lesson_h2']}</h2>
<table style="width:100%;border-collapse:collapse;font-size:.88rem;margin:8px 0 0">
<thead><tr style="border-bottom:2px solid #ccc">
  <th style="text-align:left;padding:6px 8px;font-size:.7rem;text-transform:uppercase;letter-spacing:1px;color:#777"></th>
  <th style="text-align:left;padding:6px 8px;font-size:.7rem;text-transform:uppercase;letter-spacing:1px;color:#777">{lc['col_headers'][0]}</th>
  <th style="text-align:left;padding:6px 8px;font-size:.7rem;text-transform:uppercase;letter-spacing:1px;color:#777">{lc['col_headers'][1]}</th>
</tr></thead>
<tbody>\n{rows_html}</tbody>
</table>'''
    else:
        lesson_body = f'<h1>{title}</h1>\n<h2>{lc["section_lesson_h2"]}</h2>'

    # ── Worksheet section ─────────────────────────────────────────
    ws_body = f'<h1>{title}{lc["section_ws_suffix"]}</h1>\n'
    key_body = f'<h1>{title}{lc["section_key_suffix"]}</h1>\n'

    for exn, ex in enumerate(exercises, 1):
        ws_body += f'<h2>{ex["title"]}</h2>\n'
        if ex['instruct']:
            ws_body += f'<p style="font-size:.82rem;color:#666;margin-bottom:8px">{ex["instruct"]}</p>\n'
        ws_body += '<ol style="padding-left:1.2em;margin:0 0 16px">\n'

        key_body += f'<h2>{ex["title"]}</h2>\n<ol style="padding-left:1.2em;margin:0 0 16px">\n'

        for q in ex['questions']:
            text = q['text']
            if q['choices']:
                choices_str = ' / '.join(q['choices'])
                ws_body += (
                    f'<li style="padding:6px 0;border-bottom:1px solid #eee;font-size:.9rem">'
                    f'{text}<br>'
                    f'<span style="font-size:.75rem;color:#999">({choices_str})</span>'
                    f'<span style="display:inline-block;min-width:100px;border-bottom:1px solid #666;margin-left:8px">&nbsp;</span>'
                    f'</li>\n'
                )
            else:
                ws_body += (
                    f'<li style="padding:8px 0;border-bottom:1px solid #eee;font-size:.9rem">'
                    f'{text}<br>'
                    f'<span style="display:block;border-bottom:1px solid #666;min-height:20px;margin-top:4px"></span>'
                    f'</li>\n'
                )
            ans = q['answer'] or '—'
            key_body += (
                f'<li style="padding:4px 0;font-size:.9rem">'
                f'<strong>{ans}</strong>'
                f'</li>\n'
            )
        ws_body += '</ol>\n'
        key_body += '</ol>\n'

    # ── Nav ───────────────────────────────────────────────────────
    nav_items = ''
    for label, href in zip(lc['nav'], lc['nav_hrefs']):
        active = ' active' if href == 'printables.html' else ''
        nav_items += f'  <a href="{href}" class="chapter-nav-btn{active}">{label}</a>\n'

    return f'''<!DOCTYPE html>
<html lang="{lc['html_lang']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml">
<title>{lvl_eyebrow}{title}{lc['hub_title_suffix']} | Word Play</title>
<link rel="stylesheet" href="{prefix}shared/base.css?v=v124">
<link rel="stylesheet" href="{prefix}shared/print.css?v=v102">
<script src="/shared/auth.js?v=1"></script>
<script src="{prefix}shared/dark-init.js?v=v112"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="index.html" class="back back-link" aria-label="Back"></a>
  <a href="/" class="brand"><svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px"><rect width="32" height="32" rx="4" fill="currentColor"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>Word Play</a>
  <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">{lc['dark_btn']}</button>
</div></header>
<nav class="chapter-nav">
{nav_items}</nav>
<div class="ph-hub">
  <h1 class="ph-hub-title">{title}</h1>
  <div class="ph-hub-grid">
{cards_html}  </div>
  <div class="ph-hub-actions">
    <button onclick="wpPrint('all')" class="ph-hub-btn ph-hub-btn-print">{lc['hub_print_all']}</button>
  </div>
</div>

<div id="ph-lesson" class="ph-section">
{lesson_body}
</div>

<div id="ph-worksheet" class="ph-section">
{ws_body}
</div>

<div id="ph-key" class="ph-section">
{key_body}
</div>

<footer class="site-footer">{lc['footer']}</footer>
<script src="{prefix}shared/print.js?v=v102"></script>
</body>
</html>
'''


def add_nav_btn(html, lang):
    """Add Printables nav button to chapter-nav if not already there."""
    label = LANG[lang]['nav_btn_label']
    if f'href="printables.html"' in html:
        return html, False
    new = NAV_RE.sub(
        lambda m: m.group(0).rstrip('</nav>').rstrip() + f'\n  <a href="printables.html" class="chapter-nav-btn">{label}</a>\n</nav>',
        html, count=1
    )
    return new, new != html


def add_hub_card(html, lang):
    """Insert printables activity-card into chapter index.html after the game card."""
    if 'href="printables.html"' in html:
        return html, False
    card = LANG[lang]['activity_card']
    # Insert after game.html card closure
    game_card_end = '</a>\n  </div>'
    # Try to find game activity card and insert after it
    game_anchor = 'href="game.html" class="activity-card"'
    i = html.find(game_anchor)
    if i == -1:
        return html, False
    j = html.find('</a>', i)
    if j == -1:
        return html, False
    j += len('</a>')
    return html[:j] + '\n' + card + html[j:], True


def get_level_label(path):
    """Extract level label from path (e.g. 'A1', 'B1')."""
    parts = path.replace(ROOT, '').strip(os.sep).split(os.sep)
    for p in parts:
        if re.match(r'^[ab]\d$', p, re.I):
            return p.upper()
    return ''


def get_depth(path):
    """Return number of ../ hops from chapter dir to ROOT."""
    rel = os.path.relpath(ROOT, path)
    return rel.count('..') + rel.count(os.sep) + 1 if rel != '.' else 0


def chapters_for_track(section_dir):
    if not os.path.isdir(section_dir):
        return []
    return [
        os.path.join(section_dir, d)
        for d in sorted(os.listdir(section_dir))
        if os.path.isdir(os.path.join(section_dir, d))
    ]


def main():
    sample = '--sample' in sys.argv
    track_filter = None
    if '--track' in sys.argv:
        i = sys.argv.index('--track')
        if i + 1 < len(sys.argv):
            track_filter = sys.argv[i + 1]

    done, skipped = [], []

    for lang, section_dir in TRACKS:
        if track_filter:
            if track_filter == 'es' and lang != 'es':
                continue
            if track_filter == 'esen' and lang != 'en':
                continue
            if track_filter == 'fr' and lang != 'fr':
                continue

        for ch in chapters_for_track(section_dir):
            rel = os.path.relpath(ch, ROOT)
            target = os.path.join(ch, 'printables.html')

            # Skip if already has real content (not a stub)
            if os.path.exists(target):
                content = open(target, encoding='utf-8').read()
                if '<!-- LESSON REFERENCE CONTENT -->' not in content and 'LESSON REFERENCE CONTENT' not in content:
                    continue  # already populated
                # it's a stub — overwrite

            ws_path = os.path.join(ch, 'worksheet.html')
            sl_path = os.path.join(ch, 'slides.html')

            if not os.path.exists(ws_path):
                skipped.append(f'{rel} (no worksheet.html)')
                continue

            ws_html = open(ws_path, encoding='utf-8').read()
            title, exercises, _ = parse_worksheet(ws_html)
            if not exercises:
                title, exercises, _ = parse_worksheet_old(ws_html)

            if not title or not exercises:
                skipped.append(f'{rel} (no parseable exercises)')
                continue

            summary_rows = []
            if os.path.exists(sl_path):
                sl_html = open(sl_path, encoding='utf-8').read()
                summary_rows = parse_summary(sl_html)

            level_label = get_level_label(ch)
            depth = len(os.path.relpath(ch, ROOT).split(os.sep))

            html = build_printable(
                slug=os.path.basename(ch),
                title=title,
                level_label=level_label,
                depth=depth,
                lang=lang,
                summary_rows=summary_rows,
                exercises=exercises,
            )

            with open(target, 'w', encoding='utf-8') as f:
                f.write(html)

            # Update sibling nav buttons
            for sib in ('slides.html', 'worksheet.html', 'game.html'):
                p = os.path.join(ch, sib)
                if not os.path.exists(p):
                    continue
                s, changed = add_nav_btn(open(p, encoding='utf-8').read(), lang)
                if changed:
                    open(p, 'w', encoding='utf-8').write(s)

            # Update chapter hub
            hub_p = os.path.join(ch, 'index.html')
            if os.path.exists(hub_p):
                hub, changed = add_hub_card(open(hub_p, encoding='utf-8').read(), lang)
                if changed:
                    open(hub_p, 'w', encoding='utf-8').write(hub)

            done.append(rel)
            print(f'OK  {rel}  ({len(exercises)} exercises, {len(summary_rows)} summary rows)')
            if sample and len(done) >= 3:
                print('[sample mode — stopping]')
                return

    print(f'\n{len(done)} printables generated')
    if skipped:
        print('Skipped:')
        for s in skipped:
            print(' -', s)


if __name__ == '__main__':
    main()
