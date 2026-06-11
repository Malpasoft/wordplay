# -*- coding: utf-8 -*-
"""Fill es/ grammar and writing game.html stubs from their worksheet ANSWERS.

For each game.html with <!-- TERM placeholder items in an es/ grammar or
writing chapter, this script:
  1. Reads sibling worksheet.html for questions, ANSWERS, EXPLANATIONS
  2. Derives GAME_DATA items where:
       term       = the correct answer (key grammar form)
       meaning    = EXPLANATIONS[qid] (Spanish rule explanation)
       synonym    = exercise title / hint
       example    = question text with answer <b>bolded</b>
       completion = question text with _____ blank
       answer     = answer.toLowerCase()
  3. Replaces only the items:[...] array in game.html

Usage: python3 scripts/gen_es_grammar_games.py
"""
import glob, json, os, re, subprocess, sys, tempfile

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

NODE = r'''
const fs = require("fs");
const [,, gamePath, wsPath] = process.argv;
const ws = fs.readFileSync(wsPath, "utf8");

// Extract ANSWERS
const am = ws.match(/window\.ANSWERS\s*=\s*(\{[\s\S]*?\})\s*;/);
if (!am) { console.error("NO ANSWERS " + wsPath); process.exit(2); }
const ANSWERS = eval("(" + am[1] + ")");

// Extract EXPLANATIONS (optional)
let EXPS = {};
const em = ws.match(/window\.EXPLANATIONS\s*=\s*(\{[\s\S]*?\})\s*;/);
if (em) { try { EXPS = eval("(" + em[1] + ")"); } catch(e){} }

// Extract EXERCISE_TITLES (optional)
let EX_TITLES = {};
const etm = ws.match(/window\.EXERCISE_TITLES\s*=\s*(\{[^}]*\})\s*;/);
if (etm) { try { EX_TITLES = eval("(" + etm[1] + ")"); } catch(e){} }

// Extract questions: <div class="q">...<div class="q-text">TEXT</div>...data-q="QID"
// Also handle choice-group data-answer
const Q_RE = /<div class="q"[^>]*>[\s\S]*?<div class="q-text">([\s\S]*?)<\/div>([\s\S]*?)(?=<div class="q"[^>]*>|<\/section>|<div class="submit)/g;
const questions = [];
let qm;
while ((qm = Q_RE.exec(ws)) !== null) {
  const qtext = qm[1].replace(/<[^>]+>/g, "").replace(/\s+/g, " ").trim();
  const qblock = qm[2];
  // Find qid from data-q attribute
  const qidM = qblock.match(/data-q="([^"]+)"/);
  const answerM = qblock.match(/data-answer="([^"]*)"/);
  const qid = qidM ? qidM[1] : null;
  const mcAnswer = answerM ? answerM[1] : null;
  if (!qid) continue;
  const answer = (mcAnswer !== null ? mcAnswer : (ANSWERS[qid] ? ANSWERS[qid].answer : ""));
  if (!answer) continue;
  questions.push({ qid, qtext, answer, mcAnswer });
}

if (questions.length < 4) {
  console.error("TOO FEW QUESTIONS " + wsPath + " (found " + questions.length + ")");
  process.exit(2);
}

function slugify(s) { return s.toLowerCase().replace(/[^a-z0-9]+/g,"_").replace(/^_|_$/g,""); }

function makeExample(qtext, answer) {
  // Bold the answer in the question text if it appears
  // For MC questions, often the answer is a word inserted into ______
  const blank = /_{3,}/.test(qtext);
  if (blank) {
    // Replace blank with bolded answer
    return qtext.replace(/_{3,}/, "<b>" + answer + "</b>");
  }
  // If no blank, just return text with answer appended
  return qtext + " <b>" + answer + "</b>";
}

function makeCompletion(qtext, answer) {
  const blank = /_{3,}/.test(qtext);
  if (blank) return qtext; // already has blank
  return qtext + " _____";
}

// Take up to 10 items
const maxItems = Math.min(questions.length, 10);
const items = [];
for (let i = 0; i < maxItems; i++) {
  const q = questions[i];
  const exNum = q.qid.match(/^(e\d+)/) ? q.qid.match(/^(e\d+)/)[1] : "ex1";
  const exTitle = EX_TITLES[exNum] || EX_TITLES["ex1"] || "";
  const exp = EXPS[q.qid] ? EXPS[q.qid].replace(/<[^>]+>/g,"") : "";
  items.push({
    id: "item" + (i+1),
    term: q.answer,
    meaning: exp || (exTitle ? exTitle + ": " + q.answer : q.answer),
    synonym: exTitle || "",
    example: makeExample(q.qtext, q.answer),
    completion: makeCompletion(q.qtext, q.answer),
    answer: q.answer.toLowerCase().replace(/[^a-z0-9'\-\s]/g,"").trim()
  });
}

if (items.length < 4) {
  console.error("TOO FEW ITEMS " + wsPath);
  process.exit(2);
}

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

    # Find all grammar/writing game.html with placeholder items across all tracks
    games = sorted(
        glob.glob(os.path.join(ROOT, 'es', '*', 'gramatica', '*', 'game.html')) +
        glob.glob(os.path.join(ROOT, 'es', '*', 'writing', '*', 'game.html')) +
        glob.glob(os.path.join(ROOT, 'a', '*', 'grammar', '*', 'game.html')) +
        glob.glob(os.path.join(ROOT, 'b', '*', 'grammar', '*', 'game.html')) +
        glob.glob(os.path.join(ROOT, 'c', '*', 'grammar', '*', 'game.html')) +
        glob.glob(os.path.join(ROOT, 'a', '*', 'writing', '*', 'game.html')) +
        glob.glob(os.path.join(ROOT, 'b', '*', 'writing', '*', 'game.html')) +
        glob.glob(os.path.join(ROOT, 'c', '*', 'writing', '*', 'game.html'))
    )

    for g in games:
        with open(g, encoding='utf-8') as f:
            t = f.read()
        if '<!-- TERM' not in t:
            continue
        ws = os.path.join(os.path.dirname(g), 'worksheet.html')
        if not os.path.exists(ws):
            print('NO WORKSHEET', g)
            fails += 1
            continue
        r = subprocess.run(['node', js.name, g, ws], capture_output=True, text=True)
        out = (r.stdout + r.stderr).strip()
        print(out)
        if r.returncode != 0:
            fails += 1

    os.unlink(js.name)
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
