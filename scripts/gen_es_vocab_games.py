# -*- coding: utf-8 -*-
"""Fill es/ vocabulary game.html stubs from their completed flashcards.

Each es/ vocab flashcards.html has WORDS = [{word, ipa, definition (Spanish),
example (English)}]. The sibling game.html stubs carry placeholder items
(`<!-- TERM 1 -->`). This script derives real GAME_DATA items:

  term       = English word
  meaning    = Spanish definition (the track's language)
  synonym    = IPA (hint slot, same convention as fr/ vocab games)
  example    = English example with the term bolded
  completion = example with the term blanked, else "definition = ____"
  answer     = the word (lowercased)

Only the items:[...] array is replaced; chapterId/storageKey/nav stay intact.
Usage: python3 scripts/gen_es_vocab_games.py
"""
import glob, json, os, re, subprocess, sys, tempfile

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

NODE = r'''
const fs = require("fs");
const [,, gamePath, fcPath] = process.argv;
const fc = fs.readFileSync(fcPath, "utf8");
const wm = fc.match(/(?:var WORDS|window\.VOCAB_DATA)\s*=\s*([\s\S]*?])\s*;/);
if (!wm) { console.error("NO WORDS " + fcPath); process.exit(2); }
let wv = eval("(" + wm[1] + ")");
const words = Array.isArray(wv) ? wv : wv.WORDS;

function slugify(w){ return w.toLowerCase().replace(/[^a-z0-9]+/g,"_").replace(/^_|_$/g,""); }
function boldTerm(ex, w){
  const re = new RegExp("(" + w.replace(/[.*+?^${}()|[\]\\]/g,"\\$&") + "\\w*)", "i");
  return re.test(ex) ? ex.replace(re, "<b>$1</b>") : null;
}
function blankTerm(ex, w){
  const re = new RegExp(w.replace(/[.*+?^${}()|[\]\\]/g,"\\$&") + "\\w*", "i");
  return re.test(ex) ? ex.replace(re, "_____") : null;
}
const items = words.slice(0, 12).map(w => {
  const word = w.word, def = w.definition || w.def || "";
  const ex = w.example || w.ex || "";
  const bolded = boldTerm(ex, word);
  const blanked = blankTerm(ex, word);
  return {
    id: slugify(word),
    term: word,
    meaning: def,
    synonym: w.ipa || "",
    example: bolded || ex || (word + " — " + def),
    completion: blanked || (def + " = _____"),
    answer: word.toLowerCase()
  };
});
if (items.length < 4) { console.error("TOO FEW " + fcPath); process.exit(2); }

let g = fs.readFileSync(gamePath, "utf8");
const gm = g.match(/(window\.GAME_DATA\s*=\s*\{[\s\S]*?items\s*:\s*)\[[\s\S]*?\](\s*\};)/);
if (!gm) { console.error("NO GAME_DATA " + gamePath); process.exit(2); }
const ser = "[\n  " + items.map(i => JSON.stringify(i)).join(",\n  ") + "\n]";
g = g.slice(0, gm.index) + gm[1] + ser + gm[2] + g.slice(gm.index + gm[0].length);
fs.writeFileSync(gamePath, g);
console.log("OK " + gamePath + " (" + items.length + " items)");
'''


def main():
    js = tempfile.NamedTemporaryFile('w', suffix='.js', delete=False)
    js.write(NODE)
    js.close()
    fails = 0
    games = sorted(glob.glob(os.path.join(ROOT, 'es', '*', 'vocabulary', '*', 'game.html')))
    for g in games:
        with open(g, encoding='utf-8') as f:
            t = f.read()
        if '<!-- TERM' not in t:
            continue
        fc = os.path.join(os.path.dirname(g), 'flashcards.html')
        if not os.path.exists(fc):
            print('NO FLASHCARDS', g)
            fails += 1
            continue
        r = subprocess.run(['node', js.name, g, fc], capture_output=True, text=True)
        out = (r.stdout + r.stderr).strip()
        print(out)
        if r.returncode != 0:
            fails += 1
    os.unlink(js.name)
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
