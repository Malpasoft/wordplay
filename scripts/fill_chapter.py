#!/usr/bin/env python3
"""Fill a scaffolded chapter (slides/worksheet/game) with real content.

Replaces the placeholder regions produced by gen_chapter.py with authored
educational content from a chapter data dict. Regions are matched by stable
anchors, never by line number, so re-running is idempotent on filled files
only if anchors still exist (run once on a fresh scaffold).

Data dict shape (per chapter):
  slides:       [{title, sub, html}] x5   (html = inner slide-card body)
  mistakes:     [{wrong, right, note}] x4
  summary_rows: [{label, form, ex}] x5
  mc:           [{q, opts[3], answer, explanation}] x5
  fi:           [{prompt, answer, explanation}] x5
  ctx:          [{sentence, answer, explanation}] x4
  game_items:   [{id, term, meaning, synonym, example, completion, answer}] x10
"""
import json, re, os, sys

# ── Spanish UI strings for exercise headers ──────────────────────────────────
EX1_TITLE = "Elige la opción correcta"
EX1_INSTR = "Selecciona la respuesta correcta para cada frase."
EX2_TITLE = "Completa los huecos"
EX2_INSTR = "Escribe el verbo en la forma correcta del Present Continuous / going to."
EX3_TITLE = "En contexto"
EX3_INSTR = "Lee y completa cada frase con la forma correcta."
EX3_LEAD  = "Lee con atención y escribe la forma correcta en cada hueco."


def accept_variants(answer):
    """Auto-generate acceptable alternative spellings (contraction expansions)."""
    alts = set()
    a = answer
    for c, full in (("isn't", "is not"), ("aren't", "are not"),
                    ("don't", "do not"), ("doesn't", "does not"),
                    ("can't", "cannot")):
        if c in a:
            alts.add(a.replace(c, full))
    return sorted(alts)


# ── slides.html ──────────────────────────────────────────────────────────────
def build_slides(d):
    out = ['<div class="slide-deck" id="slide-deck">\n']
    for i, s in enumerate(d["slides"], 1):
        sub = f'<p class="slide-sub">{s["sub"]}</p>' if s.get("sub") else ''
        out.append(
            f'\n<!-- Slide {i} -->\n'
            f'<div class="slide"><div class="slide-card">\n'
            f'  <div class="slide-header"><h2>{s["title"]}</h2>{sub}</div>\n'
            f'  {s["html"]}\n'
            f'</div></div>\n'
        )
    # Slide 6: common mistakes
    traps = ''.join(
        f'\n  <div class="trap-row">'
        f'<div class="trap-wrong">{m["wrong"]}</div>'
        f'<div class="trap-arrow">&rarr;</div>'
        f'<div class="trap-right">{m["right"]}</div>'
        f'<div class="trap-note">{m["note"]}</div>'
        f'</div>'
        for m in d["mistakes"]
    )
    out.append(
        '\n<!-- Slide 6: Common mistakes -->\n'
        '<div class="slide"><div class="slide-card">\n'
        '  <div class="slide-header"><h2>Errores comunes</h2>'
        '<p class="slide-sub">Errores típicos de hispanohablantes</p></div>'
        f'{traps}\n'
        '</div></div>\n'
    )
    # Slide 7: recap
    rows = ''.join(
        f'\n  <div class="summary-row"><div class="label">{r["label"]}</div>'
        f'<div class="form">{r["form"]}</div><div class="ex">{r["ex"]}</div></div>'
        for r in d["summary_rows"]
    )
    out.append(
        '\n<!-- Slide 7: Recap -->\n'
        '<div class="slide summary-slide"><div class="slide-card">\n'
        '  <h2>Resumen</h2>'
        f'{rows}\n'
        '  <div style="margin-top:28px;text-align:center">\n'
        '    <a href="worksheet.html" style="display:inline-block;padding:13px 32px;'
        'background:var(--amber);color:#1A1A1A;font-family:var(--font-sans);font-size:.8rem;'
        'font-weight:800;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;'
        'border-radius:5px">Practicar ahora &rarr;</a>\n'
        '  </div>\n'
        '</div></div>\n'
    )
    out.append('</div><!-- .slide-deck -->')
    return ''.join(out)


def fill_slides(path, d):
    html = open(path, encoding="utf-8").read()
    new = build_slides(d)
    html2, n = re.subn(
        r'<div class="slide-deck" id="slide-deck">.*?</div><!-- \.slide-deck -->',
        lambda m: new, html, count=1, flags=re.S)
    assert n == 1, f"slide-deck region not found in {path}"
    open(path, "w", encoding="utf-8").write(html2)


# ── worksheet.html ───────────────────────────────────────────────────────────
def build_ex1(d):
    qs = []
    for i, q in enumerate(d["mc"], 1):
        btns = ''.join(
            f'<button type="button" class="choice-btn" data-value="{o}">{o}</button>'
            for o in q["opts"])
        qs.append(
            f'  <div class="q"><span class="q-num">{i}</span>\n'
            f'    <div class="q-text">{q["q"]}</div>\n'
            f'    <div class="choice-group" data-q="mc{i}" data-answer="{q["answer"]}">{btns}</div>\n'
            f'  </div>')
    return (
        '<section class="exercise" id="ex1">\n'
        '  <div class="ex-head">Ejercicio 1</div>\n'
        f'  <div class="ex-title">{EX1_TITLE}</div>\n'
        '  <div class="ex-meta">5 points</div>\n'
        f'  <div class="ex-instruct">{EX1_INSTR}</div>\n'
        + '\n'.join(qs) + '\n'
        '</section>')


INPUT_STYLE = ('width:180px;padding:7px 11px;font-family:var(--font-sans);font-size:.9rem;'
               'border:1.5px solid var(--hairline);border-radius:4px;background:var(--paper);'
               'color:var(--ink);margin-top:6px;display:block')
CTX_INPUT_STYLE = INPUT_STYLE.replace('width:180px', 'width:140px')


def build_ex2(d):
    qs = []
    for i, q in enumerate(d["fi"], 1):
        qs.append(
            f'  <div class="q"><span class="q-num">{i}</span>\n'
            f'    <div class="q-text">{q["prompt"]}</div>\n'
            f'    <input type="text" data-q="fi{i}" maxlength="30" autocomplete="off" '
            f'spellcheck="false" placeholder="…" style="{INPUT_STYLE}">\n'
            f'  </div>')
    return (
        '<section class="exercise" id="ex2">\n'
        '  <div class="ex-head">Ejercicio 2</div>\n'
        f'  <div class="ex-title">{EX2_TITLE}</div>\n'
        '  <div class="ex-meta">5 points</div>\n'
        f'  <div class="ex-instruct">{EX2_INSTR}</div>\n'
        + '\n'.join(qs) + '\n'
        '</section>')


def build_ex3(d):
    qs = []
    for i, q in enumerate(d["ctx"], 1):
        qs.append(
            f'  <div class="q"><span class="q-num">{i}</span>\n'
            f'    <div class="q-text">{q["sentence"]}</div>\n'
            f'    <input type="text" data-q="ctx{i}" maxlength="20" autocomplete="off" '
            f'spellcheck="false" placeholder="…" style="{CTX_INPUT_STYLE}">\n'
            f'  </div>')
    return (
        '<section class="exercise" id="ex3">\n'
        '  <div class="ex-head">Ejercicio 3</div>\n'
        f'  <div class="ex-title">{EX3_TITLE}</div>\n'
        '  <div class="ex-meta">4 points</div>\n'
        f'  <div class="ex-instruct">{EX3_INSTR}</div>\n'
        f'  <div class="reading-context">{EX3_LEAD}</div>\n'
        + '\n'.join(qs) + '\n'
        '</section>')


def build_answers(d):
    lines = []
    for i, q in enumerate(d["mc"], 1):
        lines.append(f'  mc{i}:{{answer:{json.dumps(q["answer"])}}}')
    for i, q in enumerate(d["fi"], 1):
        acc = accept_variants(q["answer"])
        ax = f',accept:{json.dumps(acc)}' if acc else ''
        lines.append(f'  fi{i}:{{answer:{json.dumps(q["answer"])}{ax}}}')
    for i, q in enumerate(d["ctx"], 1):
        acc = accept_variants(q["answer"])
        ax = f',accept:{json.dumps(acc)}' if acc else ''
        lines.append(f'  ctx{i}:{{answer:{json.dumps(q["answer"])}{ax}}}')
    return 'window.ANSWERS = {\n' + ',\n'.join(lines) + '\n};'


def build_explanations(d):
    lines = []
    for i, q in enumerate(d["mc"], 1):
        lines.append(f'  "mc{i}":{json.dumps(q["explanation"])}')
    for i, q in enumerate(d["fi"], 1):
        lines.append(f'  "fi{i}":{json.dumps(q["explanation"])}')
    for i, q in enumerate(d["ctx"], 1):
        lines.append(f'  "ctx{i}":{json.dumps(q["explanation"])}')
    return 'window.EXPLANATIONS = {\n' + ',\n'.join(lines) + '\n};'


def fill_worksheet(path, d):
    html = open(path, encoding="utf-8").read()

    def sub_section(html, sid, new):
        pat = r'<section class="exercise" id="%s">.*?</section>' % sid
        out, n = re.subn(pat, lambda m: new, html, count=1, flags=re.S)
        assert n == 1, f"{sid} not found in {path}"
        return out

    html = sub_section(html, "ex1", build_ex1(d))
    html = sub_section(html, "ex2", build_ex2(d))
    html = sub_section(html, "ex3", build_ex3(d))

    html, n = re.subn(r'window\.ANSWERS = \{.*?\};',
                      lambda m: build_answers(d), html, count=1, flags=re.S)
    assert n == 1, "ANSWERS block not found"
    html, n = re.subn(r'window\.EXPLANATIONS = \{.*?\};',
                      lambda m: build_explanations(d), html, count=1, flags=re.S)
    assert n == 1, "EXPLANATIONS block not found"
    open(path, "w", encoding="utf-8").write(html)


# ── game.html ────────────────────────────────────────────────────────────────
def build_game_items(d):
    rows = []
    for n, it in enumerate(d["game_items"], 1):
        rows.append('  ' + json.dumps({
            "id": f"item{n}", "term": it["term"], "meaning": it["meaning"],
            "synonym": it["synonym"], "example": it["example"],
            "completion": it["completion"], "answer": it["answer"],
        }, ensure_ascii=False))
    return 'items:[\n' + ',\n'.join(rows) + '\n]'


def fill_game(path, d):
    html = open(path, encoding="utf-8").read()
    html2, n = re.subn(r'items:\[.*?\]\};',
                       lambda m: build_game_items(d) + '};', html, count=1, flags=re.S)
    assert n == 1, f"items array not found in {path}"
    open(path, "w", encoding="utf-8").write(html2)


def fill_chapter(chapter_dir, data):
    fill_slides(os.path.join(chapter_dir, "slides.html"), data)
    fill_worksheet(os.path.join(chapter_dir, "worksheet.html"), data)
    fill_game(os.path.join(chapter_dir, "game.html"), data)


if __name__ == "__main__":
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, os.path.join(ROOT, "scripts/content"))
    from es_a1_g_batch1 import CHAPTERS as B1
    from es_a1_g_batch2 import CHAPTERS as B2
    ALL = {**B1, **B2}
    base = os.path.join(ROOT, "es/a1/gramatica")
    for slug, data in ALL.items():
        cdir = os.path.join(base, slug)
        if not os.path.isdir(cdir):
            print(f"  SKIP {slug} (dir missing)"); continue
        fill_chapter(cdir, data)
        print(f"  filled es/a1/gramatica/{slug}/")
    print("Done.")
