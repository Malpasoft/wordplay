// ══════════════════════════════════════════════════════════════════
// WRITING GRADER v2 — Word Play
// Self-contained client-side writing assessment engine
//
// Config per worksheet:
// window.WRITING_CONFIG = {
//   taskType : 'essay'|'article'|'informal-letter'|'formal-letter'|
//              'formal-email'|'informal-email'|'story'|'report'|
//              'review'|'proposal'|'description'|'postcard'|
//              'note'|'profile'|'form'|'academic-essay'|'critical-review',
//   register : 'formal'|'semi-formal'|'informal'|'any',
//   minWords : number,
//   maxWords : number,
//   level    : 'a1'|'a2'|'b1'|'b2'|'c1'|'c2',  // optional, read from window.LEVEL
// }
// ══════════════════════════════════════════════════════════════════
(function() {
'use strict';

// ── LEVEL MAP ───────────────────────────────────────────────────
var LEVEL_NUM = {a1:1,a2:2,b1:3,b2:4,c1:5,c2:6};

// ── WORD LISTS ──────────────────────────────────────────────────
var CONTRACTIONS = ["can't","won't","don't","isn't","aren't","hasn't","haven't",
  "hadn't","didn't","wouldn't","couldn't","shouldn't","mustn't",
  "I'm","I've","I'd","I'll","it's","that's","there's",
  "we're","they're","you're","he's","she's","who's"];

var WEAK_WORDS = [
  {w:'very',      tip:'Replace "very + adj" with one strong word — "very important" → "crucial".'},
  {w:'really',    tip:'"Really" is weak in formal writing. Use a stronger adverb or restructure.'},
  {w:'a lot',     tip:'"A lot of" is informal. Prefer "many", "much", "a great deal of".'},
  {w:'got',       tip:'"Got" is informal. Try "received", "obtained", "became" or rephrase.'},
  {w:'nice',      tip:'"Nice" is vague — use "pleasant", "appealing", "impressive".'},
  {w:'good',      tip:'"Good" is overused — try "effective", "beneficial", "valuable".'},
  {w:'bad',       tip:'"Bad" is vague — try "harmful", "ineffective", "problematic".'},
  {w:'big',       tip:'"Big" is informal — prefer "significant", "substantial", "major".'},
  {w:'things',    tip:'"Things" is vague. Be specific about what you mean.'},
  {w:'stuff',     tip:'"Stuff" is informal — use "material", "content", or be specific.'},
  {w:'a bit',     tip:'"A bit" is informal. Use "slightly", "somewhat", or "rather".'},
  {w:'like',      tip:'Check "like" isn\'t used informally (e.g. "like, totally") — if so, remove it.'},
];

var GOOD_LINKERS = [
  'however','furthermore','moreover','in addition','additionally',
  'nevertheless','nonetheless','on the other hand','in contrast',
  'although','even though','despite','in spite of',
  'therefore','consequently','as a result','thus','hence',
  'for instance','for example','such as','in particular',
  'in conclusion','to conclude','in summary','to sum up',
  'firstly','secondly','thirdly','finally','lastly','to begin with',
  'in my opinion','in my view','from my perspective','it is worth noting',
  'it could be argued','it is clear that','one could argue',
  'having said that','with this in mind','in other words',
  'what is more','above all','by contrast','similarly',
];

var HIGHER_LINKERS = [
  'notwithstanding','insofar as','by the same token','it stands to reason',
  'to this end','in light of','given that','whilst','whereas',
  'to a great extent','arguably','undoubtedly','it is worth considering',
  'it could be contended','on reflection',
];

var INFORMAL_CASUAL = [
  'gonna','wanna','gotta','kinda','sorta','dunno','lemme','gimme',
  'ain\'t','y\'all','yep','nope','yeah','nah','ok','okay',
  'lots of','tons of','pretty much','kind of','sort of',
  'I think that','I feel like','I reckon','I guess','I suppose',
  'To be honest','Honestly','Basically','Literally',
  'amazing','awesome','terrible','horrible',
  'etc','and so on','you know','right?',
];

// ── TASK CHECKLISTS ─────────────────────────────────────────────
var TASK_CHECKS = {
  'essay': [
    {id:'intro',    label:'Introduction with clear topic statement',
     test: function(t) { return /\b(in this essay|this essay (will|aims|explores|examines)|the question of|it is (widely|often|generally)|nowadays|today|in (recent|modern|contemporary))/i.test(t); }},
    {id:'opinion',  label:'Opinion clearly stated',
     test: function(t) { return /\b(in my (opinion|view)|from my (perspective|point of view)|I (believe|would argue|consider|think that)|it (seems|appears) to me|personally)/i.test(t); }},
    {id:'linkers',  label:'Linking words used to connect ideas',
     test: function(t,linkers) { return linkers.length >= 2; }},
    {id:'conclusion',label:'Conclusion summarising your view',
     test: function(t) { return /\b(in conclusion|to conclude|to sum up|in summary|on balance|overall|finally|all in all|to (summarise|summarize))/i.test(t); }},
  ],
  'academic-essay': [
    {id:'intro',    label:'Formal introduction with thesis',
     test: function(t) { return /\b(this essay (will|aims|argues|contends|examines|explores)|the purpose of|the aim of|it (is|can be) argued|this paper)/i.test(t); }},
    {id:'argument', label:'Developed argument with evidence or reasoning',
     test: function(t) { return /\b(evidence suggests|research (shows|indicates)|studies (show|indicate)|it (has been|is) (shown|demonstrated|established|found))/i.test(t); }},
    {id:'counter',  label:'Counter-argument acknowledged',
     test: function(t) { return /\b(however|on the other hand|nevertheless|despite|critics (argue|claim)|some (argue|contend|suggest)|admittedly|it could be (argued|said))/i.test(t); }},
    {id:'conclusion',label:'Formal conclusion restating position',
     test: function(t) { return /\b(in conclusion|to conclude|in summary|on balance|this essay (has argued|has shown|has demonstrated)|to (summarise|summarize))/i.test(t); }},
  ],
  'informal-letter': [
    {id:'opening',  label:'Informal greeting (e.g. "Hi Maria,")',
     test: function(t) { return /^(hi|hello|dear|hey)\s/i.test(t.trim()); }},
    {id:'opener',   label:'Friendly opening sentence',
     test: function(t) { return /\b(how are you|hope you(\'re| are)|great to hear|lovely to hear|thanks for|thank you for)/i.test(t); }},
    {id:'content',  label:'All required points covered',
     test: function(t) { return t.trim().split(/\s+/).length >= 80; }},
    {id:'closing',  label:'Friendly closing phrase',
     test: function(t) { return /\b(write (soon|back)|take care|all my love|lots of love|best wishes|speak soon|looking forward|can\'t wait)/i.test(t); }},
  ],
  'formal-letter': [
    {id:'opening',  label:'Formal salutation (Dear Mr/Ms... or Dear Sir/Madam)',
     test: function(t) { return /^dear\s+(mr|mrs|ms|dr|sir|madam)/i.test(t.trim()); }},
    {id:'purpose',  label:'Purpose stated in first paragraph',
     test: function(t) { return /\b(I am writing (to|regarding|with regard to|in connection with|about)|The purpose of this letter)/i.test(t); }},
    {id:'formal',   label:'Formal language throughout',
     test: function(t,_,issues) { return !issues.some(function(i){return i.text.indexOf('informal')>-1 || i.text.indexOf('contraction')>-1; }); }},
    {id:'closing',  label:'Formal sign-off (Yours sincerely / Yours faithfully)',
     test: function(t) { return /\b(yours sincerely|yours faithfully|kind regards|best regards|with (kind|best) regards)/i.test(t); }},
  ],
  'formal-email': [
    {id:'opening',  label:'Formal greeting',
     test: function(t) { return /^dear\s/i.test(t.trim()) || /^(to whom it may concern|good morning|good afternoon)/i.test(t.trim()); }},
    {id:'purpose',  label:'Clear purpose in opening paragraph',
     test: function(t) { return /\b(I am writing|I am contacting|The purpose|I would like to)/i.test(t); }},
    {id:'closing',  label:'Appropriate sign-off',
     test: function(t) { return /\b(kind regards|best regards|yours sincerely|yours faithfully|many thanks|thank you for)/i.test(t); }},
  ],
  'informal-email': [
    {id:'opening',  label:'Friendly greeting',
     test: function(t) { return /^(hi|hey|hello|dear)\s/i.test(t.trim()); }},
    {id:'opener',   label:'Friendly opener or reference to previous contact',
     test: function(t) { return /\b(how are you|hope you|great to hear|thanks for getting|just wanted to|I\'ve been)/i.test(t); }},
    {id:'closing',  label:'Friendly closing',
     test: function(t) { return /\b(speak soon|write soon|take care|all the best|see you|talk later|looking forward)/i.test(t); }},
  ],
  'article': [
    {id:'title',    label:'Catchy title or heading',
     test: function(t) { var lines = t.trim().split('\n'); return lines[0] && lines[0].trim().length > 3 && lines[0].trim().length < 60 && lines[0].trim() === lines[0].trim().charAt(0).toUpperCase() + lines[0].trim().slice(1); }},
    {id:'hook',     label:'Engaging opening (question, fact, or bold statement)',
     test: function(t) { return /\?|Did you know|Have you ever|Imagine|Every year|[A-Z][a-z]+ is (one of|the most|a major|essential|vital)/.test(t.substring(0, 200)); }},
    {id:'opinion',  label:'Your opinion included',
     test: function(t) { return /\b(in my (opinion|view)|I (believe|think|would argue)|personally|from my experience)/i.test(t); }},
    {id:'conclusion',label:'Strong conclusion',
     test: function(t) { return /\b(in conclusion|to conclude|to sum up|overall|all in all|it is (clear|evident)|why not)/i.test(t); }},
  ],
  'story': [
    {id:'setting',  label:'Setting established (time and/or place)',
     test: function(t) { return /\b(one day|last (week|year|summer|night)|it was|in the|on a|at the|years ago|a long time)/i.test(t.substring(0,300)); }},
    {id:'pastcont', label:'Past continuous used for background',
     test: function(t) { return /\bwas\s+\w+ing\b|\bwere\s+\w+ing\b/i.test(t); }},
    {id:'dramatic', label:'Dramatic moment or climax',
     test: function(t) { return /\b(suddenly|all of a sudden|at that moment|without warning|to (his|her|their|my) surprise|unexpectedly|just then)/i.test(t); }},
    {id:'resolution',label:'Resolution or ending',
     test: function(t) { var end = t.slice(-300); return /\b(eventually|finally|in the end|at last|after (that|all|everything)|from (that day|then on))/i.test(end); }},
  ],
  'report': [
    {id:'heading',  label:'Clear heading or title',
     test: function(t) { var lines = t.trim().split('\n'); return lines[0] && /^[A-Z]/.test(lines[0].trim()) && lines[0].trim().length < 70; }},
    {id:'sections', label:'Organised in clear sections or paragraphs',
     test: function(t) { return t.trim().split(/\n\s*\n/).length >= 2 || /\b(introduction|findings|recommendation|conclusion|background|overview)/i.test(t); }},
    {id:'passive',  label:'Impersonal/passive constructions used',
     test: function(t) { return /\b(it (is|was|has been|would be)|there (is|are|was|were)|it (appears|seems|can be)|this report (aims|examines|presents))/i.test(t); }},
    {id:'recommendation',label:'Recommendation or conclusion included',
     test: function(t) { return /\b(it is (recommended|suggested|proposed)|in conclusion|to conclude|the following (is|are) recommended|we recommend|this report recommends)/i.test(t); }},
  ],
  'review': [
    {id:'intro',    label:'Introduction naming what is being reviewed',
     test: function(t) { return t.trim().split(/\s+/).length >= 30; }},
    {id:'positive', label:'Positive aspects mentioned',
     test: function(t) { return /\b(excellent|impressive|outstanding|enjoyable|well-written|fascinating|engaging|highly recommend|worth|best)/i.test(t); }},
    {id:'negative', label:'Negative aspects or balanced view',
     test: function(t) { return /\b(however|unfortunately|on the other hand|despite|although|drawback|weakness|disappointing|could (be|have been) better)/i.test(t); }},
    {id:'recommendation',label:'Clear recommendation to reader',
     test: function(t) { return /\b(I (would|highly) recommend|worth (reading|watching|visiting|seeing)|not worth|avoid|a must|don\'t miss)/i.test(t); }},
  ],
  'proposal': [
    {id:'purpose',  label:'Purpose of proposal stated clearly',
     test: function(t) { return /\b(the aim of|the purpose of|this proposal|I am writing to propose|the following proposal|we propose)/i.test(t); }},
    {id:'sections', label:'Organised in sections with headings',
     test: function(t) { return /\b(introduction|background|recommendations|benefits|conclusion|proposal|aims|objectives)/i.test(t); }},
    {id:'formal',   label:'Formal impersonal language',
     test: function(t) { return /\b(it is (proposed|recommended|suggested)|this would|the following|in order to|with a view to)/i.test(t); }},
    {id:'benefit',  label:'Benefits or justification given',
     test: function(t) { return /\b(benefit|advantage|improve|enhance|increase|would result in|would lead to|would enable)/i.test(t); }},
  ],
  'critical-review': [
    {id:'intro',    label:'Introduction situating the work',
     test: function(t) { return t.trim().split(/\s+/).length >= 40; }},
    {id:'analysis', label:'Critical analysis not just description',
     test: function(t) { return /\b(however|while|although|despite|the author (argues|claims|contends|suggests)|this (argument|claim|point|view) (is|can be|seems))/i.test(t); }},
    {id:'evidence', label:'Evidence or examples from the work cited',
     test: function(t) { return /\b(for example|for instance|as (shown|demonstrated|illustrated)|as the author (states|writes|notes)|in (chapter|section|paragraph))/i.test(t); }},
    {id:'evaluation',label:'Overall evaluation and judgement',
     test: function(t) { return /\b(on balance|overall|in conclusion|to conclude|ultimately|this work (is|represents|fails|succeeds|achieves))/i.test(t); }},
  ],
  'description': [
    {id:'adjectives',label:'Descriptive adjectives used',
     test: function(t) { var adjCount = (t.match(/\b(beautiful|tall|small|large|old|young|bright|dark|warm|cold|busy|quiet|loud|strange|wonderful|delicious|colourful|enormous|tiny|ancient|modern)/gi) || []).length; return adjCount >= 2; }},
    {id:'senses',   label:'Sensory details (sight, sound, smell, etc.)',
     test: function(t) { return /\b(look|see|hear|sound|smell|taste|feel|colour|bright|dark|loud|quiet|scent|aroma)/i.test(t); }},
    {id:'structure', label:'Organised structure (general to specific)',
     test: function(t) { return t.trim().split(/\s+/).length >= 50; }},
  ],
  'postcard': [
    {id:'greeting', label:'Greeting to the recipient',
     test: function(t) { return /^(hi|hello|dear|hey)\s/i.test(t.trim()); }},
    {id:'place',    label:'Location mentioned',
     test: function(t) { return /\b(here in|we are in|I am in|arrived in|staying in|visiting|I\'m in)\b/i.test(t); }},
    {id:'activity', label:'Activity or experience mentioned',
     test: function(t) { return /\b(we (are|have been|went|visited|tried|saw|ate|enjoyed)|I (am|have been|went|visited|tried|saw|ate|enjoyed))/i.test(t); }},
    {id:'closing',  label:'Friendly closing',
     test: function(t) { return /\b(wish you were here|see you soon|miss you|write soon|take care|love|best wishes)/i.test(t); }},
  ],
  'note': [
    {id:'greeting', label:'Greeting or recipient named',
     test: function(t) { return /^(hi|hello|dear|hey|\w+,)/i.test(t.trim()); }},
    {id:'message',  label:'Clear message communicated',
     test: function(t) { return t.trim().split(/\s+/).length >= 15; }},
    {id:'closing',  label:'Sign-off or name',
     test: function(t) { var end = t.trim().slice(-60); return /\b(bye|see you|take care|later|from|love|thanks|\w+)\.?\s*$/.test(end); }},
  ],
  'profile': [
    {id:'name',     label:'Name given',
     test: function(t) { return /\b(my name is|I am|I\'m)\s+\w+/i.test(t); }},
    {id:'origin',   label:'Origin or location mentioned',
     test: function(t) { return /\b(from|live in|living in|born in|grew up in)/i.test(t); }},
    {id:'activity', label:'Job, study, or hobby mentioned',
     test: function(t) { return /\b(work|study|job|school|hobby|free time|enjoy|like to|interested in)/i.test(t); }},
  ],
};

// ── VOCABULARY RANGE SCORING ─────────────────────────────────────
// Type-token ratio proxy: unique content words / total content words
// Adjusted for length (longer texts naturally have lower TTR)
var STOP_WORDS = new Set(['the','a','an','and','or','but','in','on','at','to','of',
  'for','with','is','are','was','were','be','been','have','has','had',
  'this','that','these','those','it','its','i','my','me','we','our',
  'you','your','he','his','she','her','they','their','as','by','if',
  'so','not','do','did','will','can','could','would','should','may',
  'might','just','also','then','than','when','which','who','what',
  'from','into','about','up','out','more','some','any','all','no',
  'one','two','three','very','much','many','most','other','such']);

function lexicalDiversity(text) {
  var words = text.toLowerCase().replace(/[^a-z\s]/g,' ').split(/\s+/).filter(
    function(w) { return w.length > 3 && !STOP_WORDS.has(w); }
  );
  if (words.length < 10) return 0;
  var unique = new Set(words);
  var rawTTR = unique.size / words.length;
  // Normalise: short texts have inflated TTR; adjust for length
  var adjusted = rawTTR * Math.min(1, Math.sqrt(words.length / 60));
  return Math.min(1, adjusted * 1.6); // 0–1 scale
}

// ── GRAMMAR PATTERN DETECTION ────────────────────────────────────
function detectGrammarPatterns(text, levelNum) {
  var issues = [];
  // Subject-verb: "he/she/it + base verb" (he go, she want)
  if (/\b(he|she|it)\s+(go|want|like|need|have|make|do|come|see|get|say|know|think|take|give|find|tell|feel|try|become|leave|call|keep|bring|begin|show|hear|let|seem|help|talk|turn|start|look|remain|lose|pay|meet|include|believe|hold|continue|serve|die|grow|stand|provide|cover|move|lead|drive|carry|expect|use|eat|walk|live|involve|appear|offer|read|spend|develop|work|play|run|require|fall|consider|produce|represent|result|act|hold)\b/i.test(text)) {
    issues.push({severity:'warn', text:'Possible subject-verb agreement error: use he/she/it + verb+s (e.g. "he goes", not "he go").'});
  }
  // Missing article before consonant-starting nouns (heuristic)
  if (levelNum <= 2 && /\b(I am|she is|he is|it is|they are|we are)\s+(teacher|student|doctor|nurse|engineer|manager|director)\b/i.test(text)) {
    issues.push({severity:'warn', text:'Check articles: "I am a teacher" — remember to use "a" or "an" before jobs and professions.'});
  }
  // Double negatives
  if (/\b(don't|doesn't|didn't|won't|can't|never|nobody|nothing|nowhere)\b.{0,40}\b(not|never|no one|nobody|nothing|nowhere)\b/i.test(text)) {
    issues.push({severity:'warn', text:'Possible double negative detected. In English, use only one negative per clause: "I didn\'t see anything" (not "I didn\'t see nothing").'});
  }
  return issues;
}

// ── CAMBRIDGE RUBRIC SCORING ─────────────────────────────────────
// Returns scores 0–5 for Content, Language, Organisation
// Based on Cambridge writing assessment criteria
function scoreRubric(text, config, analysis) {
  var levelNum = LEVEL_NUM[config.level || 'b1'] || 3;
  var wc = analysis.wordCount;
  var minW = config.minWords || 40;
  var maxW = config.maxWords || 200;

  // ── CONTENT (0–5) ─────────────────────────────────────────────
  // Did they attempt the task? Cover required points? Relevant ideas?
  var content = 0;
  if (wc >= minW * 0.4) content = 1;          // wrote something
  if (wc >= minW * 0.7) content = 2;          // reasonable attempt
  if (wc >= minW && analysis.checksPass >= 1) content = 3;  // on task
  if (wc >= minW && analysis.checksPass >= 2) content = 4;  // well-targeted
  if (wc >= minW && analysis.checksPass >= 3 && analysis.issues.filter(function(i){return i.severity==='error';}).length === 0) content = 5;

  // ── LANGUAGE (0–5) ────────────────────────────────────────────
  // Grammar accuracy, vocabulary range, register appropriateness
  var langDeductions = 0;
  langDeductions += analysis.issues.filter(function(i){return i.text.indexOf('contraction')>-1;}).length * 0.5;
  langDeductions += analysis.issues.filter(function(i){return i.text.indexOf('informal')>-1;}).length * 0.5;
  langDeductions += analysis.issues.filter(function(i){return i.text.indexOf('agreement')>-1 || i.text.indexOf('double negative')>-1;}).length * 1;
  var lexDiv = analysis.lexDiv;
  var langBase = 2 + Math.round(lexDiv * 2);          // 2–4 from vocab range
  if (analysis.tips.filter(function(t){return t.indexOf('weak')>-1||t.indexOf('vague')>-1;}).length >= 2) langBase--;
  var language = Math.max(0, Math.min(5, langBase - Math.floor(langDeductions)));

  // ── ORGANISATION (0–5) ────────────────────────────────────────
  // Structure, paragraphing, cohesion, linking
  var org = 1;
  if (analysis.paragraphs >= 2) org = 2;
  if (analysis.paragraphs >= 3) org = 3;
  if (analysis.linkersFound.length >= 2 && analysis.paragraphs >= 2) org = Math.min(5, org + 1);
  if (analysis.linkersFound.length >= 4 && analysis.paragraphs >= 3) org = Math.min(5, org + 1);
  // Higher-level linkers bonus
  var textLower = text.toLowerCase();
  var higherCount = HIGHER_LINKERS.filter(function(l){return textLower.indexOf(l)>-1;}).length;
  if (higherCount >= 2 && levelNum >= 4) org = Math.min(5, org + 1);

  // ── RANGE (0–5) ──────────────────────────────────────────────
  // Variety of vocabulary and structures relative to level
  var range = Math.round(analysis.lexDiv * 3) + 1; // 1–4 from lex diversity
  if (higherCount >= 1 && levelNum >= 4) range = Math.min(5, range + 1);
  if (analysis.linkersFound.length >= 5) range = Math.min(5, range + 1);

  var total = content + language + org + range;
  var pct = Math.round((total / 20) * 100);

  // Cambridge band descriptor
  var band;
  if      (pct >= 90) band = 'Distinction';
  else if (pct >= 75) band = 'Pass with Merit';
  else if (pct >= 60) band = 'Pass';
  else if (pct >= 45) band = 'Near miss';
  else                band = 'Needs more work';

  return { content:content, language:language, organisation:org, range:range,
           total:total, pct:pct, band:band };
}

// ── CORE ANALYSIS ─────────────────────────────────────────────────
function countWords(text) {
  var c = text.trim().replace(/\s+/g,' ');
  return c ? c.split(' ').length : 0;
}
function getSentences(text) {
  return text.split(/[.!?]+/).map(function(s){return s.trim();}).filter(function(s){return s.length>0;});
}
function findInText(text,phrase) {
  return new RegExp('\\b'+phrase.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\b','gi').test(text);
}
function countOccurrences(text,word) {
  var rx = new RegExp('\\b'+word.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\b','gi');
  return (text.match(rx)||[]).length;
}

function analyseText(text, config) {
  var issues = [], tips = [], positives = [];
  var wordCount = countWords(text);
  var sentences = getSentences(text);
  var textLower = text.toLowerCase();
  var register  = config.register || 'any';
  var isFormal  = (register === 'formal' || register === 'semi-formal');
  var levelStr  = config.level || (window.LEVEL) || 'b1';
  var levelNum  = LEVEL_NUM[levelStr] || 3;
  var minW = config.minWords || 40;
  var maxW = config.maxWords || 200;

  // ── 1. Word count ──────────────────────────────────────────────
  if (wordCount === 0) {
    issues.push({severity:'error', text:'No text written yet — start typing to get feedback.'});
  } else if (wordCount < minW) {
    issues.push({severity:'warn', text:'Too short: '+wordCount+' words (minimum '+minW+'). Write '+(minW-wordCount)+' more words.'});
  } else if (wordCount > maxW) {
    issues.push({severity:'warn', text:'Too long: '+wordCount+' words (maximum '+maxW+'). Cut '+(wordCount-maxW)+' words.'});
  } else {
    positives.push('Word count: '+wordCount+' words — within the '+minW+'–'+maxW+' target.');
  }

  // ── 2. Contractions in formal writing ─────────────────────────
  if (isFormal) {
    var contractionsFound = CONTRACTIONS.filter(function(c) {
      return text.indexOf(c) > -1 || text.indexOf(c.toLowerCase()) > -1;
    });
    if (contractionsFound.length > 0) {
      issues.push({severity:'warn', text:'Avoid contractions in formal writing: '+contractionsFound.slice(0,4).join(', ')+(contractionsFound.length>4?'…':'')+'. Write in full (e.g. "do not" instead of "don\'t").'});
    }
  }

  // ── 3. Informal vocabulary ────────────────────────────────────
  if (isFormal && levelNum >= 3) {
    var infFound = INFORMAL_CASUAL.filter(function(w){return findInText(text,w);});
    if (infFound.length > 0) {
      issues.push({severity:'warn', text:'Informal language: "'+infFound.slice(0,3).join('", "')+'"'+(infFound.length>3?'…':'')+'. Avoid casual words in formal writing.'});
    }
  }

  // ── 4. Weak/vague vocabulary ──────────────────────────────────
  if (levelNum >= 3) {
    WEAK_WORDS.forEach(function(item) {
      if (countOccurrences(text,item.w) >= 2) tips.push('"'+item.w+'" used repeatedly — '+item.tip);
    });
  }

  // ── 5. "Very" overuse ─────────────────────────────────────────
  var veryCount = countOccurrences(text,'very');
  if (veryCount >= 3) {
    tips.push('"very" appears '+veryCount+' times. Replace with stronger single words (e.g. "very big" → "enormous", "very important" → "crucial").');
  }

  // ── 6. Linking words ──────────────────────────────────────────
  var linkersFound = GOOD_LINKERS.filter(function(l){return textLower.indexOf(l)>-1;});
  var higherFound  = HIGHER_LINKERS.filter(function(l){return textLower.indexOf(l)>-1;});
  if (linkersFound.length >= 4 || higherFound.length >= 2) {
    positives.push('Strong use of cohesive devices: '+linkersFound.concat(higherFound).slice(0,5).join(', ')+'.');
  } else if (linkersFound.length >= 2) {
    positives.push('Good linking words: '+linkersFound.slice(0,4).join(', ')+'.');
  } else if (wordCount >= 60) {
    tips.push('Add linking words to connect ideas: "However", "Furthermore", "In addition", "As a result", "In conclusion".');
  }

  // ── 7. Sentence variety ───────────────────────────────────────
  if (sentences.length > 2) {
    var lengths = sentences.map(function(s){return s.split(/\s+/).length;});
    var avg = lengths.reduce(function(a,b){return a+b;},0)/lengths.length;
    if (lengths.every(function(l){return l<8;}) && wordCount>=60) {
      tips.push('All sentences are short (avg '+Math.round(avg)+' words). Combine some using "Although…", "While…", "Despite…" for variety.');
    } else if (lengths.every(function(l){return l>22;})) {
      tips.push('Some sentences are very long. Try breaking them up for clarity and readability.');
    } else if (wordCount>=80) {
      positives.push('Good sentence variety — mix of shorter and longer structures.');
    }
  }

  // ── 8. Paragraph structure ────────────────────────────────────
  var paragraphs = text.trim().split(/\n\s*\n/).filter(function(p){return p.trim().length>0;});
  var taskType = config.taskType||'';
  if (wordCount >= 80 && paragraphs.length < 2) {
    tips.push('Organise into paragraphs — separate your ideas with a blank line. For this task, aim for at least 3 paragraphs.');
  } else if (paragraphs.length >= 3 && wordCount >= 80) {
    positives.push('Well organised: '+paragraphs.length+' clear paragraphs.');
  }

  // ── 9. Repetition ─────────────────────────────────────────────
  var wordFreq = {};
  text.toLowerCase().replace(/[^a-z\s]/g,'').split(/\s+/).forEach(function(w){
    if (w.length>4 && !STOP_WORDS.has(w)) wordFreq[w]=(wordFreq[w]||0)+1;
  });
  var overused = Object.entries(wordFreq).filter(function(e){return e[1]>=4;}).sort(function(a,b){return b[1]-a[1];});
  if (overused.length>0) {
    tips.push('"'+overused[0][0]+'" appears '+overused[0][1]+' times — use synonyms to vary your vocabulary.');
  }

  // ── 10. Grammar patterns ──────────────────────────────────────
  var grammarIssues = detectGrammarPatterns(text, levelNum);
  issues = issues.concat(grammarIssues);

  // ── 11. Task checklist ────────────────────────────────────────
  var checks = TASK_CHECKS[taskType] || [];
  var checksPassed = [], checksFailed = [];
  checks.forEach(function(chk) {
    var passed = chk.test(text, linkersFound, issues);
    if (passed) checksPassed.push(chk.label);
    else checksFailed.push(chk.label);
  });
  if (checksPassed.length > 0) {
    positives.push('Task requirements met: '+checksPassed.join(' · ')+'.');
  }
  if (checksFailed.length > 0 && wordCount >= minW * 0.7) {
    issues.push({severity:'warn', text:'Missing task elements: '+checksFailed.join(' · ')+'.'});
  }

  // ── 12. Register-specific positives ──────────────────────────
  if (levelNum >= 4 && isFormal && linkersFound.length >= 3 && issues.filter(function(i){return i.text.indexOf('contraction')>-1||i.text.indexOf('informal')>-1;}).length===0) {
    positives.push('Appropriate formal register maintained throughout.');
  }

  var lexDiv = lexicalDiversity(text);
  if (wordCount >= 60) {
    if (lexDiv > 0.7) positives.push('Excellent vocabulary range — strong diversity of word choices.');
    else if (lexDiv > 0.5) positives.push('Good vocabulary variety.');
    else if (lexDiv < 0.3 && levelNum >= 3) tips.push('Limited vocabulary range — try to vary your word choices more. Use synonyms and avoid repeating the same words.');
  }

  return {
    wordCount   : wordCount,
    issues      : issues,
    tips        : tips,
    positives   : positives,
    linkersFound: linkersFound.concat(higherFound),
    paragraphs  : paragraphs.length,
    checksPass  : checksPassed.length,
    checksFail  : checksFailed.length,
    lexDiv      : lexDiv,
  };
}

// ── RENDER FEEDBACK ───────────────────────────────────────────────
function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g,function(c){
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];
  });
}

function renderFeedback(result, containerId, config, currentText) {
  currentText = currentText || '';
  var container = document.getElementById(containerId);
  if (!container) return;
  var html = '';
  var wc = result.wordCount;
  var cfg = config || {};
  var levelStr = cfg.level || (window.LEVEL) || 'b1';
  var levelNum = LEVEL_NUM[levelStr] || 3;

  // Rubric scores — only show if something written
  if (wc >= 10) {
    var rubric = scoreRubric(currentText, cfg, result);
    html += '<div class="wg-rubric">';
    html += '<div class="wg-rubric-title">Assessment · '+rubric.band+'</div>';
    html += '<div class="wg-rubric-grid">';
    var dims = [
      {label:'Content',      score:rubric.content},
      {label:'Language',     score:rubric.language},
      {label:'Organisation', score:rubric.organisation},
      {label:'Range',        score:rubric.range},
    ];
    dims.forEach(function(d) {
      var pct = d.score/5*100;
      var col = pct>=80?'var(--green)':pct>=60?'var(--amber)':'var(--red)';
      html += '<div class="wg-rubric-row">';
      html += '<div class="wg-rubric-label">'+d.label+'</div>';
      html += '<div class="wg-rubric-bar"><div class="wg-rubric-fill" style="width:'+pct+'%;background:'+col+'"></div></div>';
      html += '<div class="wg-rubric-score" style="color:'+col+'">'+d.score+'/5</div>';
      html += '</div>';
    });
    html += '</div>';
    html += '<div class="wg-rubric-total">Total: <strong>'+rubric.total+'/20</strong> · '+rubric.pct+'%</div>';
    html += '</div>';
  }

  // Positives
  if (result.positives.length > 0) {
    html += '<div class="wg-section wg-pos">';
    html += '<div class="wg-section-head">What is working well</div>';
    result.positives.forEach(function(p){html+='<div class="wg-item">'+escapeHtml(p)+'</div>';});
    html += '</div>';
  }

  // Issues
  if (result.issues.length > 0) {
    html += '<div class="wg-section wg-issues">';
    html += '<div class="wg-section-head">Issues to address</div>';
    result.issues.forEach(function(i){
      var cls = i.severity==='error'?'wg-error':'wg-warn';
      html += '<div class="wg-item '+cls+'">'+escapeHtml(i.text)+'</div>';
    });
    html += '</div>';
  }

  // Tips
  if (result.tips.length > 0) {
    html += '<div class="wg-section wg-tips">';
    html += '<div class="wg-section-head">Tips to improve</div>';
    result.tips.forEach(function(t){html+='<div class="wg-item">'+escapeHtml(t)+'</div>';});
    html += '</div>';
  }

  if (!html) {
    html = '<div class="wg-section"><div class="wg-item" style="color:var(--muted)">Write your answer to see feedback and your rubric score.</div></div>';
  }

  container.innerHTML = html;
}

// ── LIVE FEEDBACK ─────────────────────────────────────────────────
function initWritingGrader(textareaId, feedbackId, config) {
  var ta  = document.getElementById(textareaId);
  var cfg = config || window.WRITING_CONFIG || {};
  if (!ta) return;
  var container = document.getElementById(feedbackId);

  var timeout;
  ta.addEventListener('input', function() {
    clearTimeout(timeout);
    timeout = setTimeout(function() {
        var result = analyseText(ta.value, cfg);
      renderFeedback(result, feedbackId, cfg, ta.value);
    }, 700);
  });

  // Initial render
  renderFeedback(analyseText(ta.value, cfg), feedbackId, cfg, ta.value);
}

window.WritingGrader = { init:initWritingGrader, analyse:analyseText, render:renderFeedback, score:scoreRubric };
})();
