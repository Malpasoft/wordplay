// ══════════════════════════════════════════════════════════════════
// store.js — FCEStore — progress storage for Word Play
// ══════════════════════════════════════════════════════════════════
//
// WHAT THIS FILE DOES
// All progress reading and writing goes through this module.
// localStorage key: 'wordplay_progress'
// Structure: { a1: { "slug": { score, total, pct, date } }, a2: {...}, ... }
//
// USAGE
//   FCEStore.saveResult(chapterId, score, total)    — saves worksheet score
//   FCEStore.saveGameResult(chapterId, mastered, total) — saves game mastery
//   FCEStore.getLevel(level)                        — returns { grammar:{}, vocab:{} }
//   FCEStore.CHAPTERS                               — chapter registry object
//
// IMPORTANT: window.LEVEL must be set on every page before calling saveResult.
// Without it, progress saves to the wrong level key.
//
// CHAPTER REGISTRATION
// All chapter slugs are registered in CHAPTERS at the bottom of this file.
// When adding a new chapter, add its slug there too.
// ══════════════════════════════════════════════════════════════════

(function() {
  var KEY = 'wordplay_progress';
  // One-time migration from old storage key
  try {
    var oldData = localStorage.getItem('playLearnProgress');
    if (oldData && !localStorage.getItem('wordplay_progress')) {
      localStorage.setItem('wordplay_progress', oldData);
    }
  } catch(e) {}


  function load() {
    try { return JSON.parse(localStorage.getItem(KEY)) || {}; }
    catch(e) { return {}; }
  }
  function save(data) {
    try {
      localStorage.setItem(KEY, JSON.stringify(data));
    } catch(e) {
      console.warn('[WordPlay] localStorage save failed:', e.message);
    }
  }

  // Update streak — uses local date (en-CA locale = YYYY-MM-DD) so streaks
  // work correctly for students in any timezone, not just UTC.
  function updateStreak(data) {
    var today = new Date().toLocaleDateString('en-CA');
    if (data.lastDay === today) return;
    if (data.lastDay) {
      var last = new Date(data.lastDay);
      var now = new Date(today);
      var diff = Math.round((now - last) / 86400000);
      data.streak = diff === 1 ? (data.streak || 0) + 1 : 1;
    } else {
      data.streak = 1;
    }
    data.lastDay = today;
  }

  function touchStreak() {
    var data = load();
    updateStreak(data);
    save(data);
    schedulePush();
  }

  var XP_LEVELS = [
    { label: 'Beginner',           min: 0    },
    { label: 'Elementary',         min: 100  },
    { label: 'Pre-Intermediate',   min: 250  },
    { label: 'Intermediate',       min: 500  },
    { label: 'Upper-Intermediate', min: 1000 },
    { label: 'Advanced',           min: 2000 },
  ];

  window.FCEStore = {
    touchStreak: touchStreak,
    // Save a worksheet result
    saveResult: function(chapterId, score, total, perExercise) {
      var data = load();
      // Use window.LEVEL hint if provided, else find via registry
      var level, info;
      if (window.LEVEL && CHAPTERS[window.LEVEL]) {
        level = window.LEVEL;
      } else {
        info = findChapter(chapterId);
        if (!info) return;
        level = info.level;
      }
      if (!data[level]) data[level] = {};
      data[level][chapterId] = {
        score: score,
        total: total,
        pct: Math.round((score / total) * 100),
        perExercise: perExercise || null,
        date: new Date().toISOString(),
        lastDate: new Date().toISOString()
      };
      updateStreak(data);
      save(data);
      schedulePush();
    },

    // Save a game result
    saveGameResult: function(chapterId, mastered, total) {
      var data = load();
      var level, info;
      if (window.LEVEL && CHAPTERS[window.LEVEL]) {
        level = window.LEVEL;
      } else {
        info = findChapter(chapterId);
        if (!info) return;
        level = info.level;
      }
      if (!data[level]) data[level] = {};
      var key = 'wordplay_game_' + chapterId;
      data[level][key] = {
        mastered: mastered,
        total: total,
        pct: Math.round((mastered / total) * 100),
        date: new Date().toISOString()
      };
      updateStreak(data);
      save(data);
      schedulePush();
    },

    // XP system
    addXP: function(n) {
      var data = load();
      data.xp = (data.xp || 0) + Math.max(0, n || 0);
      save(data);
      schedulePush();
      return data.xp;
    },
    getXP: function() {
      try { return (JSON.parse(localStorage.getItem(KEY) || '{}').xp) || 0; } catch(e) { return 0; }
    },
    getXPLevel: function() {
      var xp = FCEStore.getXP();
      var level = XP_LEVELS[0];
      for (var i = 0; i < XP_LEVELS.length; i++) {
        if (xp >= XP_LEVELS[i].min) level = XP_LEVELS[i];
        else break;
      }
      var nextIdx = XP_LEVELS.indexOf(level) + 1;
      var next    = nextIdx < XP_LEVELS.length ? XP_LEVELS[nextIdx] : null;
      var pct     = next ? Math.min(100, Math.round(((xp - level.min) / (next.min - level.min)) * 100)) : 100;
      return { label: level.label, xp: xp, min: level.min, max: next ? next.min : null, pct: pct };
    },

    // Get all data for a level
    getLevel: function(level) {
      var data = load();
      var results = data[level] || {};
      return {
        results: results,
        chapters: CHAPTERS[level] || {},
        streak: data.streak || 0
      };
    },

    // Get weakest chapters for a level+section
    getWeakest: function(level, section) {
      var data = load();
      var results = data[level] || {};
      var chs = (CHAPTERS[level] || {})[section] || [];
      return chs
        .filter(function(ch) { return results[ch.slug]; })
        .sort(function(a,b) { return results[a.slug].pct - results[b.slug].pct; });
    },

    // Push local progress to D1 (reliable: keepalive survives navigation).
    pushToD1: function() { return doPush(); },

    // Pull cloud progress and DEEP-MERGE into local — never loses a chapter.
    mergeFromD1: function() {
      var token = getAuthToken ? getAuthToken() : null;
      var user  = getCurrentUser ? getCurrentUser() : null;
      if (!token || !user) return Promise.resolve(null);

      return fetch('/api/progress/' + user.user_id, {
        headers: { 'Authorization': 'Bearer ' + token }
      })
        .then(function(res) {
          if (!res.ok) throw new Error('Fetch failed: ' + res.status);
          return res.json();
        })
        .then(function(data) {
          var merged = mergeProgress(load(), data.progress || {});
          save(merged);
          // Push merged back once so the cloud converges with anything
          // that existed only on this device. No data is discarded either way.
          doPush();
          return merged;
        })
        .catch(function(err) {
          console.warn('[WordPlay] D1 merge failed, using local progress:', err.message);
          return load();
        });
    }
  };

  // ── Cloud sync internals ─────────────────────────────────────────
  // Deep-merge two progress objects without losing data:
  //  · level maps → union of chapters, keep the later-dated (then higher-pct) entry
  //  · xp / streak → keep the maximum
  //  · lastDay     → keep the later date
  function pickEntry(x, y) {
    if (!x) return y;
    if (!y) return x;
    var dx = Date.parse(x.lastDate || x.date || 0) || 0;
    var dy = Date.parse(y.lastDate || y.date || 0) || 0;
    if (dx !== dy) return dx > dy ? x : y;
    return (y.pct || 0) > (x.pct || 0) ? y : x;
  }

  function mergeProgress(a, b) {
    a = a || {}; b = b || {};
    var out = {};
    var keys = {};
    Object.keys(a).forEach(function(k){ keys[k] = 1; });
    Object.keys(b).forEach(function(k){ keys[k] = 1; });

    Object.keys(keys).forEach(function(k) {
      var av = a[k], bv = b[k];
      if (k === 'updated_at') return;                 // recomputed below
      if (k === 'xp')      { out.xp = Math.max(av || 0, bv || 0); return; }
      if (k === 'streak')  { out.streak = Math.max(av || 0, bv || 0); return; }
      if (k === 'lastDay') { out.lastDay = (av || '') > (bv || '') ? av : bv; return; }

      // Level maps (objects of chapter entries)
      if (av && bv && typeof av === 'object' && typeof bv === 'object') {
        var level = {};
        var chs = {};
        Object.keys(av).forEach(function(c){ chs[c] = 1; });
        Object.keys(bv).forEach(function(c){ chs[c] = 1; });
        Object.keys(chs).forEach(function(c){ level[c] = pickEntry(av[c], bv[c]); });
        out[k] = level;
        return;
      }
      out[k] = (bv !== undefined ? bv : av);
    });

    out.updated_at = Date.now();
    return out;
  }

  // Reliable push: keepalive lets the request finish even if the page is
  // navigating away, so we don't need an (unreliable) beforeunload fetch.
  function doPush() {
    var token = getAuthToken ? getAuthToken() : null;
    var user  = getCurrentUser ? getCurrentUser() : null;
    if (!token || !user) return Promise.resolve(null);

    var data = load();
    data.updated_at = Date.now();

    return fetch('/api/progress/' + user.user_id, {
      method: 'POST',
      keepalive: true,
      headers: {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    }).catch(function(err) {
      console.warn('[WordPlay] D1 push failed, will retry on next save:', err.message);
      return null;
    });
  }

  // Debounced push — called after every local write so progress reaches the
  // cloud a couple of seconds after a student finishes, while still on-page.
  var _pushTimer = null;
  function schedulePush() {
    if (!getCurrentUser || !getCurrentUser()) return;
    if (_pushTimer) clearTimeout(_pushTimer);
    _pushTimer = setTimeout(function(){ _pushTimer = null; doPush(); }, 1500);
  }

  // Final best-effort flush when the page is hidden/closed (keepalive fetch).
  if (typeof window !== 'undefined') {
    window.addEventListener('pagehide', function(){
      if (_pushTimer) { clearTimeout(_pushTimer); _pushTimer = null; doPush(); }
    });
  }

  // ── Flat slug index for O(1) chapter lookup ──────────────────────
  // Built once at load time from CHAPTERS; replaces O(n·m) scan.
  // Format: { 'slug': { level: 'a1', section: 'grammar' }, ... }
  var slugIndex = {};

  function buildSlugIndex(chapters) {
    slugIndex = {};
    for (var level in chapters) {
      for (var section in chapters[level]) {
        var chs = chapters[level][section];
        for (var i = 0; i < chs.length; i++) {
          slugIndex[chs[i].slug] = { level: level, section: section };
        }
      }
    }
  }

  function findChapter(slug) {
    // O(1) lookup via pre-built index
    return slugIndex[slug] || null;
  }

  var CHAPTERS = {
    'a1': {
      'grammar': [
        {slug:'to-be',label:'Verb to be'},
        {slug:'present-simple',label:'Present Simple'},
        {slug:'have-got',label:'Have got'},
        {slug:'pronouns',label:'Pronouns'},
        {slug:'possessive-adjectives',label:'Possessive Adjectives'},
        {slug:'articles-basic',label:'A, An, The'},
        {slug:'nouns-plural',label:'Plural Nouns'},
        {slug:'adjectives-basic',label:'Adjectives'},
        {slug:'there-is-there-are',label:'There is / There are'},
        {slug:'present-continuous',label:'Present Continuous'},
        {slug:'can-cant',label:'Can and Can\'t'},
        {slug:'imperatives',label:'Imperatives'},
        {slug:'adverbs-frequency',label:'Adverbs of Frequency'},
        {slug:'prepositions-place',label:'Prepositions of Place (in/on/at)'},
        {slug:'prepositions-time',label:'Prepositions of Time'},
        {slug:'question-words',label:'Question Words'},
        {slug:'some-any',label:'Some and Any'},
        {slug:'simple-past-regular',label:'Simple Past — Regular'},
        {slug:'simple-past-irregular',label:'Simple Past — Irregular'},
        {slug:'going-to-future',label:'Going to — Future'},
        {slug:'demonstratives',label:'Demonstratives'},
        {slug:'prepositions-of-place',label:'Prepositions of Place (position)'},
        {slug:'can-basic',label:'Can — ability'},
        {slug:'possessives',label:'Possessive Adjectives (review)'}
      ],
      'vocabulary': [
        {slug:'family',label:'Family'},
        {slug:'food',label:'Food and Drink'},
        {slug:'daily-routine',label:'Daily Routine'},
        {slug:'clothes',label:'Clothes'},
        {slug:'weather',label:'Weather'},
        {slug:'places-in-town',label:'Places in Town'}
      ],
      'writing': [
        {slug:'personal-profile',label:'Personal Profile'},
        {slug:'short-note',label:'Short Note or Message'},
        {slug:'form-filling',label:'Form Filling'},
      ],
    },
    'a2': {
      'grammar': [
        {slug:'past-simple',label:'Past Simple'},
        {slug:'past-continuous',label:'Past Continuous'},
        {slug:'present-perfect-intro',label:'Present Perfect — Introduction'},
        {slug:'future-going-to',label:'Future — going to'},
        {slug:'future-will',label:'Future — will'},
        {slug:'modal-could-might',label:'Modals: could, might'},
        {slug:'modal-must-should',label:'Modals: must, should'},
        {slug:'comparatives-basic',label:'Comparatives'},
        {slug:'countable-uncountable-basic',label:'Countable & Uncountable'},
        {slug:'quantifiers-basic',label:'Quantifiers'},
        {slug:'too-enough-basic',label:'Too & Enough'},
        {slug:'relative-clauses-basic',label:'Relative Clauses'},
        {slug:'word-order',label:'Word Order'},
        {slug:'object-pronouns',label:'Object Pronouns'},
        {slug:'short-answers',label:'Short Answers'},
        {slug:'conjunctions',label:'Conjunctions'},
        {slug:'adverbs-manner',label:'Adverbs of Manner'},
        {slug:'prepositions-movement',label:'Prepositions of Movement'}
      ],
      'vocabulary': [
        {slug:'school-subjects',label:'School Subjects'},
        {slug:'work-and-jobs',label:'Work and Jobs'},
        {slug:'transport-and-travel',label:'Transport and Travel'},
        {slug:'health-and-body',label:'Health and Body'},
        {slug:'shopping-and-money',label:'Shopping and Money'},
        {slug:'technology-and-media',label:'Technology and Media'},
      ],
      'writing': [
        {slug:'informal-email',label:'Informal Email'},
        {slug:'postcard',label:'Postcard'},
        {slug:'description',label:'Personal Description'},
      ],
    },
    'b1': {
      'grammar': [
        {slug:'comparatives-superlatives',label:'Comparatives & Superlatives'},
        {slug:'future-forms',label:'Future Forms'},
        {slug:'ing-form',label:'The -ing Form'},
        {slug:'modal-deduction',label:'Modals of Deduction'},
        {slug:'modals-advice',label:'Modals — Advice'},
        {slug:'modals-obligation',label:'Modals — Obligation'},
        {slug:'passive-simple',label:'Passive Voice'},
        {slug:'past-simple-continuous',label:'Past Simple & Continuous'},
        {slug:'present-perfect',label:'Present Perfect'},
        {slug:'question-tags',label:'Question Tags'},
        {slug:'relative-clauses',label:'Relative Clauses'},
        {slug:'reported-speech-basic',label:'Reported Speech — basic'},
        {slug:'second-conditional',label:'Second Conditional'},
        {slug:'so-neither',label:'So and Neither'},
        {slug:'too-enough',label:'Too, Enough and Very'},
        {slug:'verb-infinitive-patterns',label:'Verb + Infinitive Patterns'},
        {slug:'zero-first-conditional',label:'Zero & First Conditional'}
      ],
      'vocabulary': [
        {slug:'adjective-preposition',label:'Adjective + Preposition'},
        {slug:'collocations-make-do',label:'Collocations — Make, Do, Have, Take'},
        {slug:'education-school',label:'Education and School'},
        {slug:'environment-nature',label:'Environment and Nature'},
        {slug:'phrasal-verbs-get-take',label:'Phrasal Verbs — Get and Take'},
        {slug:'phrasal-verbs-go-come',label:'Phrasal Verbs — Go and Come'},
        {slug:'sport-leisure',label:'Sport and Leisure'},
        {slug:'technology-media',label:'Technology and Media'},
        {slug:'travel-holidays',label:'Travel and Holidays'},
        {slug:'word-families-basic',label:'Word Families — basic'}
      ],
      'writing': [
        {slug:'article',label:'Article'},
        {slug:'informal-letter',label:'Informal Letter'},
        {slug:'story',label:'Story'}
      ],
    },
    'b2': {
      'grammar': [
        {slug:'articles',label:'Articles'},
        {slug:'causative',label:'Causative Have / Get'},
        {slug:'comparisons',label:'Comparisons'},
        {slug:'conditionals',label:'Conditionals'},
        {slug:'countable-uncountable',label:'Countable & Uncountable'},
        {slug:'future-forms',label:'Future Forms'},
        {slug:'gerunds-infinitives',label:'Gerunds & Infinitives'},
        {slug:'hypothetical-meaning',label:'Hypothetical Meaning'},
        {slug:'inversion',label:'Inversion & Emphasis'},
        {slug:'linking-discourse',label:'Linking & Discourse Markers'},
        {slug:'mixed-conditionals',label:'Mixed Conditionals'},
        {slug:'modals-past',label:'Modals in the Past'},
        {slug:'narrative-tenses',label:'Narrative Tenses'},
        {slug:'passive',label:'The Passive'},
        {slug:'relative-clauses',label:'Relative Clauses'},
        {slug:'reported-speech',label:'Reported Speech'},
        {slug:'used-to',label:'Be / Get Used To'},
        {slug:'verb-patterns',label:'Verb Patterns'}
      ],
      'vocabulary': [
        {slug:'collocations-adj-noun',label:'Collocations — Adj + Noun'},
        {slug:'collocations-verbs',label:'Collocations — Verbs'},
        {slug:'environment-climate',label:'Environment and Climate'},
        {slug:'expressions-idioms',label:'Expressions and Idioms'},
        {slug:'false-friends',label:'False Friends & Confusables'},
        {slug:'health-lifestyle',label:'Health and Lifestyle'},
        {slug:'phrasal-verbs-look-bring',label:'Phrasal Verbs — Look and Bring'},
        {slug:'phrasal-verbs-put-set',label:'Phrasal Verbs — Put and Set'},
        {slug:'phrasal-verbs-turn-run',label:'Phrasal Verbs — Turn and Run'},
        {slug:'society-culture',label:'Society and Culture'},
        {slug:'technology-innovation',label:'Technology and Innovation'},
        {slug:'word-formation-adjectives',label:'Word Formation — Adjectives'},
        {slug:'word-formation-nouns',label:'Word Formation — Nouns'},
        {slug:'word-formation-prefixes',label:'Word Formation — Prefixes'},
        {slug:'work-careers',label:'Work and Careers'}
      ],
      'writing': [
        {slug:'article',label:'Article'},
        {slug:'essay',label:'The Essay'},
        {slug:'formal-email',label:'Formal Email / Letter'},
        {slug:'report',label:'The Report'},
        {slug:'review',label:'The Review'}
      ],
    },
    // C1/C2 fully live — all chapters, vocabulary, and writing registered
    'c1': {
      'grammar': [
        {slug:'conditionals-advanced',label:'Conditionals — Advanced'},
        {slug:'passive-advanced',label:'Passive — Advanced'},
        {slug:'relative-clauses-advanced',label:'Relative Clauses — Advanced'},
        {slug:'reported-speech-advanced',label:'Reported Speech — Advanced'},
        {slug:'modal-verbs-advanced',label:'Modal Verbs — Advanced'},
        {slug:'inversion-advanced',label:'Inversion — Advanced'},
        {slug:'cleft-sentences',label:'Cleft Sentences'},
        {slug:'ellipsis-substitution',label:'Ellipsis & Substitution'},
        {slug:'nominalisation',label:'Nominalisation'},
        {slug:'gerunds-infinitives-advanced',label:'Gerunds & Infinitives — Advanced'},
        {slug:'articles-advanced',label:'Articles — Advanced'},
        {slug:'quantifiers-advanced',label:'Quantifiers — Advanced'},
        {slug:'causative-advanced',label:'Causative — Advanced'},
        {slug:'hedging-language',label:'Hedging Language'},
        {slug:'discourse-connectors',label:'Discourse Connectors'},
        {slug:'advanced-tenses',label:'Advanced Tenses'},
        {slug:'subjunctive',label:'Subjunctive'},
      ],
      'vocabulary': [],
      'writing': [
        {slug:'essay',label:'Essay'},
        {slug:'formal-letter',label:'Formal Letter'},
        {slug:'proposal',label:'Proposal'},
        {slug:'report',label:'Report'},
        {slug:'review',label:'Review'},
      ],
    },
    'c2': {
      'grammar': [
        {slug:'error-analysis',label:'Error Analysis & Correction'},
        {slug:'complex-passives',label:'Complex Passives'},
        {slug:'conditionals-mastery',label:'Conditionals — Mastery'},
        {slug:'register-grammar',label:'Register Switching'},
        {slug:'academic-grammar',label:'Academic Grammar'},
        {slug:'stylistic-inversion',label:'Stylistic Inversion'},
        {slug:'discourse-grammar',label:'Discourse Grammar'},
        {slug:'advanced-modality',label:'Advanced Modality'},
        {slug:'grammar-in-text',label:'Grammar in Context'},
        {slug:'grammar-review-tenses',label:'Tense Review — Advanced'},
        {slug:'advanced-clauses',label:'Advanced Clause Structures'},
      ],
      'vocabulary': [
        {slug:'lexical-sophistication',label:'Lexical Sophistication'},
        {slug:'advanced-idioms',label:'Advanced Idioms'},
        {slug:'academic-collocations',label:'Academic Collocations'},
        {slug:'nuanced-synonyms',label:'Nuanced Synonyms'},
        {slug:'discourse-vocabulary',label:'Discourse Vocabulary'},
        {slug:'corpus-vocabulary',label:'Corpus Vocabulary'},
        {slug:'applied-grammar-collocation',label:'Applied Grammar & Collocation'},
      ],
      'writing': [
        {slug:'academic-essay',label:'Academic Essay'},
        {slug:'critical-review',label:'Critical Review'},
      ],
    },
  };

  // ── Build flat index for O(1) lookups ────────────────────────────
  buildSlugIndex(CHAPTERS);

  window.FCEStore.CHAPTERS = CHAPTERS;
})();
