#!/usr/bin/env python3
"""Render espanol-en/a2 writing chapters.

Reuses the grammar renderer (slides/worksheet/game from the past-simple
template) with section fixed to writing, then adds a printables.html built
from the A1 personal-introduction printables skeleton, and a Printables
card on the hub. Content modules add three extra keys per chapter:
  ref_rows  [(label, text)]  useful-language reference rows
  task      hand-writing task statement (English, with Spanish targets)
  model     model answer text (Spanish)

Usage: python3 scripts/gen_esen_a2_writing.py scripts/content/esen_a2_w.py
"""
import importlib.util
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import gen_esen_a2 as G  # noqa: E402

OUT = os.path.join(ROOT, 'espanol-en/a2/writing')
PRINT_TPL = os.path.join(ROOT, 'espanol-en/a1/writing/personal-introduction/printables.html')

PRINTABLES_CARD = '''    <a href="printables.html" class="activity-card" data-activity="print">
      <span class="ac-title">Printables</span>
      <p class="ac-desc">Reference card, hand-writing task and model answer</p>
      <span class="ac-arrow">&#8594;</span>
    </a>
'''


def build_printables(d):
    s = open(PRINT_TPL, encoding='utf-8').read()
    s = s.replace('Personal Introduction', d['short'])
    s = s.replace('Spanish A1', 'Spanish A2')
    rows = '\n'.join(
        f'<div class="ref-row"><span class="ref-label">{l}</span><span>{t}</span></div>'
        for l, t in d['ref_rows'])
    i = s.index('<h2>Useful language</h2>')
    j = s.index('<div class="footer">', i)
    s = s[:i] + '<h2>Useful language</h2>\n' + rows + '\n\n' + s[j:]
    i = s.index('<h2>Task</h2>')
    j = s.index('<div class="writing-lines">', i)
    s = (s[:i] + '<h2>Task</h2>\n<p style="font-size:10pt;margin-bottom:8pt">'
         + d['task'] + '</p>\n' + s[j:])
    i = s.index('<div class="model-text">')
    j = s.index('</div>', i)
    s = s[:i] + '<div class="model-text">' + d['model'] + s[j:]
    return s


def main():
    spec = importlib.util.spec_from_file_location('content', sys.argv[1])
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    G.OUT_BASE = OUT
    ok = True
    for slug, d in mod.CHAPTERS.items():
        out_dir = os.path.join(OUT, slug)
        ok = G.render(slug, d) and ok
        for f in ('slides.html', 'worksheet.html', 'game.html', 'index.html'):
            p = os.path.join(out_dir, f)
            s = open(p, encoding='utf-8').read()
            s = s.replace('<a href="../index.html">Grammar</a>', '<a href="../index.html">Writing</a>')
            s = s.replace("window.SECTION = 'grammar'", "window.SECTION = 'writing'")
            s = s.replace('window.SECTION="grammar"', 'window.SECTION="writing"')
            s = s.replace('&middot; Grammar</div>', '&middot; Writing task</div>')
            if f == 'index.html' and 'printables.html' not in s:
                anchor = '<a href="game.html" class="activity-card"'
                i = s.index(anchor)
                j = s.index('</a>', i) + len('</a>\n')
                s = s[:j] + PRINTABLES_CARD + s[j:]
            open(p, 'w', encoding='utf-8').write(s)
        open(os.path.join(out_dir, 'printables.html'), 'w', encoding='utf-8').write(build_printables(d))
        r = subprocess.run(['python3', os.path.join(ROOT, 'scripts/validate_inline_js.py'),
                            os.path.join(out_dir, 'printables.html')],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(f'{slug}: printables JS FAIL\n{r.stdout}')
            ok = False
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
