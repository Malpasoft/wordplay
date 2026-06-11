# -*- coding: utf-8 -*-
"""Frenchify fr/ B1-B2 vocabulaire chapters.

- Replaces English defs with French glosses (scripts/content/fr_vocab_defs.py)
  in flashcards.html and match.html WORDS arrays (via node for safe JS parsing).
- Swaps Spanish-track false-friends entries for francophone ones (REPLACE map).
- Converts page chrome (titles, nav, breadcrumbs, buttons, instructions) to French.

Usage: python3 scripts/frenchify_fr_vocab.py
"""
import json, os, re, subprocess, sys, tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'content'))
from fr_vocab_defs import DEFS, REPLACE

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

NODE_REWRITE = r'''
const fs = require("fs"), path = require("path");
const [,, file, defsJson] = process.argv;
const cfg = JSON.parse(fs.readFileSync(defsJson, "utf8"));
function extract(text) {
  const m = text.match(/(var WORDS\s*=\s*|window\.VOCAB_DATA\s*=\s*)([\s\S]*?);\s*\n/);
  if (!m) return null;
  let v = eval("(" + m[2] + ")");
  return { m, v, words: Array.isArray(v) ? v : v.WORDS, isData: !Array.isArray(v) };
}
let t = fs.readFileSync(file, "utf8");
const ext = extract(t);
if (!ext) { console.error("NO WORDS: " + file); process.exit(2); }
const { m, isData } = ext;
let v = ext.v, words = ext.words;
// match.html entries carry only word/def: map defs by word from the
// already-frenchified sibling flashcards.html
if (path.basename(file) === "match.html") {
  const fc = extract(fs.readFileSync(path.join(path.dirname(file), "flashcards.html"), "utf8"));
  const byWord = {};
  for (const w of fc.words) byWord[w.word] = w.def;
  words = words.map(w => {
    if (byWord[w.word]) return Object.assign({}, w, { def: byWord[w.word] });
    console.error("  match: no fr def for " + w.word);
    return w;
  });
  v = words;
  const ser = JSON.stringify(v);
  t = t.slice(0, m.index) + m[1] + ser + ";\n" + t.slice(m.index + m[0].length);
  fs.writeFileSync(file, t);
  process.exit(0);
}
words = words.map(w => {
  const rep = cfg.replace[w.word] || cfg.replace[w.id];
  if (rep) {
    // match.html entries may only carry word/def
    const out = Object.assign({}, w);
    if ("id" in out) out.id = rep.id;
    out.word = rep.word;
    out.def = rep.def;
    if ("ex" in out) out.ex = rep.ex;
    if ("ipa" in out) out.ipa = rep.ipa;
    return out;
  }
  const fr = cfg.defs[w.id] || cfg.defs[w.word];
  if (fr) { const out = Object.assign({}, w); out.def = fr; return out; }
  console.error("  no fr def: " + (w.id || w.word) + " in " + file);
  return w;
});
if (isData) v.WORDS = words; else v = words;
const ser = JSON.stringify(v);
t = t.slice(0, m.index) + m[1] + ser + ";\n" + t.slice(m.index + m[0].length);
fs.writeFileSync(file, t);
'''

# (pattern, replacement) applied to every html file in the chapter dirs.
CHROME = [
    ('<html lang="en">', '<html lang="fr">'),
    ('>Home</a>', '>Accueil</a>'),
    ('>Vocabulary</a>', '>Vocabulaire</a>'),
    ('aria-label="Back"', 'aria-label="Retour"'),
    ('aria-label="Toggle dark mode"', 'aria-label="Basculer mode sombre"'),
    ('aria-label="Next slide"', 'aria-label="Diapositive suivante"'),
    ('aria-label="Previous slide"', 'aria-label="Diapositive précédente"'),
    ('>Lesson<', '>Leçon<'),
    ('>Game<', '>Jeu<'),
    ('>Worksheet<', '>Exercices<'),
    ('>Practice<', '>Exercices<'),
    ('>Words<', '>Mots<'),
    ('>Check Answers<', '>Vérifier les réponses<'),
    ('>Check all your answers before submitting.<', '>Vérifie toutes tes réponses avant de valider.<'),
    ('>Play again<', '>Rejouer<'),
    ('>Try again<', '>Réessayer<'),
    ('>Match Master!<', '>Association parfaite !<'),
    ('>Match game<', '>Jeu d&rsquo;association<'),
    ('Match each word to its definition &mdash; 3 lives, match every word twice to win',
     'Associe chaque mot à sa définition &mdash; 3 vies, chaque mot doit être associé deux fois'),
    ('>Match each word to its definition<', '>Associe chaque mot à sa définition<'),
    ('Match each word to its definition. You have 3 lives',
     'Associe chaque mot à sa définition. Tu as 3 vies'),
    ('>Match the definition<', '>Associe les définitions<'),
    ('>Choose the correct word<', '>Choisis le bon mot<'),
    ('>Complete the sentences<', '>Complète les phrases<'),
    ('>Open writing<', '>Production écrite<'),
    ('>Exercise 1<', '>Exercice 1<'), ('>Exercise 2<', '>Exercice 2<'),
    ('>Exercise 3<', '>Exercice 3<'), ('>Exercise 4<', '>Exercice 4<'),
    ('ex1:"Exercise 1', 'ex1:"Exercice 1'), ('ex2:"Exercise 2', 'ex2:"Exercice 2'),
    ('ex3:"Exercise 3', 'ex3:"Exercice 3'), ('ex4:"Exercise 4', 'ex4:"Exercice 4'),
    ('B1 Vocab ·', 'B1 Vocabulaire ·'), ('B2 Vocab ·', 'B2 Vocabulaire ·'),
    ('— B1 Vocabulary Practice |', '— Exercices de vocabulaire B1 |'),
    ('— B2 Vocabulary Practice |', '— Exercices de vocabulaire B2 |'),
    ('— B1 Vocabulary Game |', '— Jeu de vocabulaire B1 |'),
    ('— B2 Vocabulary Game |', '— Jeu de vocabulaire B2 |'),
    ('— B1 Vocabulary |', '— Vocabulaire B1 |'),
    ('— B2 Vocabulary |', '— Vocabulaire B2 |'),
    ('— Match Game |', '— Jeu d’association |'),
    ('— Flashcards |', '— Flashcards |'),
    ('Exercises practising', 'Exercices sur'),
    ('. Total:', ' &middot; Total :'),
    ('Vocabulary from the B1 word bank is used throughout.', 'Le vocabulaire de la banque de mots B1 est utilisé tout au long.'),
    ('Vocabulary from the B2 word bank is used throughout.', 'Le vocabulaire de la banque de mots B2 est utilisé tout au long.'),
    (' points</strong>', ' points</strong>'),
    ('tap card to reveal', 'touche la carte pour révéler'),
    ('words · ', 'mots · '),
]


def chrome_pass(path):
    with open(path, encoding='utf-8') as f:
        t = f.read()
    for a, b in CHROME:
        t = t.replace(a, b)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(t)


def main():
    node_script = tempfile.NamedTemporaryFile('w', suffix='.js', delete=False)
    node_script.write(NODE_REWRITE)
    node_script.close()
    failures = 0
    for level in ('b1', 'b2'):
        base = os.path.join(ROOT, 'fr', level, 'vocabulaire')
        for slug in sorted(os.listdir(base)):
            d = os.path.join(base, slug)
            if not os.path.isdir(d):
                continue
            defs = DEFS.get(slug, {})
            rep = REPLACE.get(slug, {})
            if defs:
                cfg = tempfile.NamedTemporaryFile('w', suffix='.json', delete=False)
                json.dump({'defs': defs, 'replace': rep}, cfg)
                cfg.close()
                for fn in ('flashcards.html', 'match.html'):
                    p = os.path.join(d, fn)
                    if not os.path.exists(p):
                        continue
                    r = subprocess.run(['node', node_script.name, p, cfg.name],
                                       capture_output=True, text=True)
                    if r.returncode != 0 or r.stderr.strip():
                        print(f"{level}/{slug}/{fn}: {r.stderr.strip() or 'rewrite failed'}")
                        failures += r.returncode != 0
                os.unlink(cfg.name)
            for fn in os.listdir(d):
                if fn.endswith('.html'):
                    chrome_pass(os.path.join(d, fn))
            print(f"{level}/{slug}: OK")
    os.unlink(node_script.name)
    sys.exit(1 if failures else 0)


if __name__ == '__main__':
    main()
