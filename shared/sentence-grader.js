/* ══════════════════════════════════════════════════════════════════
   SENTENCE GRADER — Word Play
   
   Grades open production sentences by detecting required grammatical
   patterns using regex. No AI, no API — deterministic structure
   detection. Each task defines what patterns must be present and
   gives specific feedback when they are absent.
   
   USAGE (in worksheet HTML):
   <textarea class="sentence-grader"
     data-task="it-cleft"
     data-points="3"
     id="prod_q1"
     placeholder="Write your sentence here...">
   </textarea>
   <div id="prod_q1_feedback" class="sg-feedback"></div>
   
   window.SentenceGrader.grade(textareaEl, feedbackEl) → {score, max, passed}
   window.SentenceGrader.autoAttach() — attach to all .sentence-grader elements
   ══════════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  // ── Pattern library ──────────────────────────────────────────────
  // Each task: { checks: [{name, pattern, weight, tip}], forbidden: [{pattern, tip}], minWords }
  // score = sum of matched check weights (max = sum of all weights)
  // A check passes if pattern.test(text.toLowerCase().trim())

  var TASKS = {

    // ── C1 Grammar ────────────────────────────────────────────────

    'it-cleft': {
      label: 'It-cleft sentence',
      example: 'It was the lack of funding that caused the delay.',
      checks: [
        { name: 'It + be', pattern: /\bit\s+(was|is|were|has been|had been)\b/i, weight: 2,
          tip: 'Start with "It was/is..." — the it-cleft structure requires this opening.' },
        { name: 'that/who', pattern: /\b(that|who)\b/, weight: 2,
          tip: 'You need "that" (for things) or "who" (for people) after the focused element.' },
        { name: 'Focused element present', pattern: /it\s+(was|is|were)\s+.{3,40}\s+(that|who)\b/i, weight: 1,
          tip: 'The structure is: It was [FOCUS] that/who [REST]. Make sure there is a focused element between "was" and "that/who".' },
      ],
      forbidden: [
        { pattern: /^because\b/i, tip: '"Because" is not an it-cleft. Use: "It was ... that ..."' },
      ],
      minWords: 6,
    },

    'wh-cleft': {
      label: 'Wh-cleft (pseudo-cleft)',
      example: 'What I need is more time.',
      checks: [
        { name: 'What + clause', pattern: /\bwhat\s+\w+\s+(need|want|like|enjoy|find|think|believe|hope|mean|do|did|am|is|was)\b/i, weight: 2,
          tip: 'Start with "What I/we/you/he/she + verb" — that is the pseudo-cleft structure.' },
        { name: 'Linking be', pattern: /\bis\b|\bwas\b|\bare\b/, weight: 1,
          tip: 'After the "what-clause" you need a form of "be": "What I need IS a holiday."' },
      ],
      minWords: 5,
    },

    'negative-inversion': {
      label: 'Negative inversion',
      example: 'Never have I seen such dedication.',
      checks: [
        { name: 'Negative adverbial', pattern: /^(never|not only|rarely|seldom|at no time|under no circumstances|no sooner|little did|hardly|scarcely|only when|only after|only then|not until|not since)\b/i, weight: 2,
          tip: 'Start with a negative adverbial: Never / Not only / Rarely / Seldom / At no time / Under no circumstances...' },
        { name: 'Auxiliary inversion', pattern: /^(never|not only|rarely|seldom|at no time|under no circumstances|no sooner|little|hardly|scarcely|only\s+\w+|not\s+\w+)\s+(have|has|had|did|do|does|is|are|was|were|can|could|would|will|shall|should|must|might|may)\s+\w/i, weight: 2,
          tip: 'After the negative adverbial, the auxiliary must come BEFORE the subject: "Never HAVE I seen..." not "Never I have seen..."' },
      ],
      forbidden: [
        { pattern: /^(never|rarely)\s+(i|he|she|we|they|it|you)\s+(have|has|had|did|do|does)\b/i,
          tip: 'You have the right adverbial but the word order is wrong. Put the auxiliary before the subject: "Never HAVE I..." not "Never I have..."' },
      ],
      minWords: 6,
    },

    'so-such-inversion': {
      label: 'So/such inversion',
      example: 'So complex was the problem that no one could solve it.',
      checks: [
        { name: 'So/Such opener', pattern: /^(so|such)\b/i, weight: 2,
          tip: 'Start with "So" (+ adjective/adverb) or "Such" (+ noun phrase).' },
        { name: 'Verb before subject', pattern: /^so\s+\w+\s+(was|were|is|are|has been|had been)\s+\w/i, weight: 2,
          tip: 'After "So + adjective", invert: "So complex WAS the problem..." — verb before subject.' },
        { name: 'that clause', pattern: /\bthat\b/, weight: 1,
          tip: 'Complete the structure with a "that" clause showing the consequence.' },
      ],
      minWords: 8,
    },

    'nominalisation': {
      label: 'Nominalisation',
      example: 'The rapid deterioration of water quality raised serious concerns.',
      checks: [
        { name: 'No main clause verb as action', pattern: /\b(investigation|development|achievement|implementation|introduction|establishment|deterioration|improvement|increase|decrease|reduction|expansion|production|destruction|construction|analysis|assessment|evaluation|examination|consideration|recommendation|conclusion|suggestion|decision|discovery|observation|recognition|realisation|understanding|management|application|organisation|regulation|participation|contribution|distribution|transformation|formation|information|situation|condition|relation|solution|operation|education|communication|administration|demonstration|preparation|presentation|publication|calculation|estimation|indication|limitation|reservation|variation|cooperation|generation|investigation|implementation)\b/i, weight: 3,
          tip: 'Your sentence should contain a nominalised form (a noun derived from a verb, e.g. "investigation" not "investigated"). Look for -tion, -ment, -ance, -ity endings.' },
        { name: 'Formal structure (no contractions)', pattern: /^((?!can't|won't|don't|isn't|aren't|it's|that's|there's|we're|they're|you're).)*$/i, weight: 1,
          tip: 'Nominalised sentences are formal — no contractions.' },
      ],
      minWords: 7,
    },

    'hedging': {
      label: 'Hedging language',
      example: 'There is evidence to suggest that social media may contribute to anxiety.',
      checks: [
        { name: 'Hedging device present', pattern: /\b(may|might|could|would appear|seems to|appears to|tends to|is thought to|is believed to|it could be argued|there is evidence|evidence suggests|arguably|presumably|reportedly|apparently|it seems|it would seem|it is possible that|it has been suggested)\b/i, weight: 3,
          tip: 'Use a hedging device: "may", "might", "could", "appears to", "it could be argued that", "there is evidence to suggest that".' },
        { name: 'Not absolute claim', pattern: /^((?!is\s+(definitely|certainly|obviously|clearly|undoubtedly)|always causes|proves that|proves it).)*$/i, weight: 1,
          tip: 'Avoid absolute claims like "definitely", "always", "proves". Hedge the statement.' },
      ],
      minWords: 8,
    },

    'subjunctive': {
      label: 'Present subjunctive',
      example: 'It is essential that every student be present at the meeting.',
      checks: [
        { name: 'Subjunctive trigger', pattern: /\b(essential|vital|important|necessary|critical|imperative|recommended|suggested|proposed|required|demanded|insisted|requested|urged|advised|stipulated)\s+that\b/i, weight: 2,
          tip: 'Use a subjunctive trigger: "It is essential/vital/important/necessary that..."' },
        { name: 'Base form (not 3rd person -s)', pattern: /that\s+\w+\s+(be|have|do|go|make|take|give|come|know|find|leave|keep|bring|get)\b/i, weight: 2,
          tip: 'After "that", use the BASE form of the verb (no -s for third person): "...that he BE present" not "that he IS present".' },
        { name: 'No modal after that', pattern: /that\s+\w+\s+(should|must|will|would|can|could|may|might)\b/i, weight: -1,
          tip: 'The subjunctive does NOT use a modal: "It is essential that he be..." not "...that he should be". Remove the modal.' },
      ],
      minWords: 7,
    },

    'ellipsis': {
      label: 'Ellipsis',
      example: 'She wanted to stay, but she knew she had to.',
      checks: [
        { name: 'Truncated clause present', pattern: /\b(had to|have to|will|would|could|should|did so|does so|do so|to\s*[,.]|to\b\s*$)/i, weight: 3,
          tip: 'Use ellipsis: leave out the repeated part of the second clause. "She had to [leave]." — the understood word is omitted.' },
        { name: 'Two clauses connected', pattern: /,\s*(but|and|though|although|even though|whereas)|;\s*\w/i, weight: 1,
          tip: 'Ellipsis connects two clauses. Use a coordinating conjunction or semicolon.' },
      ],
      minWords: 5,
    },

    'passive-reporting': {
      label: 'Passive reporting structure',
      example: 'The company is said to have made significant losses last year.',
      checks: [
        { name: 'Passive reporting verb', pattern: /\b(is|are|was|were)\s+(said|thought|believed|claimed|reported|alleged|considered|assumed|known|understood|expected|supposed)\s+to\b/i, weight: 3,
          tip: 'Use structure 2: Subject + is/are said/thought/believed/reported + to + infinitive.' },
        { name: 'To-infinitive after verb', pattern: /(said|thought|believed|reported|alleged|claimed|considered)\s+to\s+(have|be|do|make|take|give|come|go|find|know|get|leave|keep)\b/i, weight: 1,
          tip: 'After "is said/reported", use "to" + base form OR "to have" + past participle for past reference.' },
      ],
      minWords: 6,
    },

    'it-cleft-passive': {
      label: 'It-cleft with passive reporting',
      example: 'It has been reported that the company is facing bankruptcy.',
      checks: [
        { name: 'It + passive', pattern: /\bit\s+(has been|was|is|have been|had been)\s+(said|reported|claimed|alleged|thought|believed|found|noted|established|confirmed|demonstrated|suggested|argued|proposed)\b/i, weight: 3,
          tip: 'Use structure 1: "It + passive reporting verb + that clause". E.g. "It was reported that..."' },
        { name: 'That clause follows', pattern: /\b(said|reported|claimed|alleged|thought|believed|found|noted|established|confirmed|demonstrated|suggested|argued)\s+that\b/i, weight: 1,
          tip: 'Complete the structure with "that" + a full clause.' },
      ],
      minWords: 8,
    },

    'conditional-inverted': {
      label: 'Inverted conditional',
      example: 'Had I known about the delay, I would have left earlier.',
      checks: [
        { name: 'Inverted opening', pattern: /^(had\s+\w|were\s+\w|should\s+\w)/i, weight: 3,
          tip: 'Start with the inverted form: "Had I/she/they...", "Were I/she...", "Should you/it..." — NO "if" in an inverted conditional.' },
        { name: 'Main clause with would', pattern: /,\s*\w[^,]*\bwould\b/i, weight: 2,
          tip: 'The main clause needs "would" (or "could/might"): "Had I known, I WOULD HAVE called."' },
      ],
      forbidden: [
        { pattern: /^if\b/i, tip: 'Inverted conditionals do NOT start with "if". Remove it and invert instead: "If I had known" → "Had I known".' },
      ],
      minWords: 8,
    },

    'discourse-connector': {
      label: 'Discourse connector',
      example: 'The results were promising. Notwithstanding this, further trials are needed.',
      checks: [
        { name: 'C1-level connector present', pattern: /\b(notwithstanding|nevertheless|nonetheless|moreover|furthermore|in addition|by contrast|conversely|consequently|accordingly|hitherto|thereby|insofar as|inasmuch as|by the same token|it follows that|in light of|to this end|be that as it may|that said|for all that|having said that)\b/i, weight: 3,
          tip: 'Use a C1-level discourse connector. Examples: "Notwithstanding", "Nevertheless", "Furthermore", "Consequently", "That said", "By contrast".' },
        { name: 'Two connected ideas', pattern: /[.;,]\s*\w|^\w.+[.;]\s*\w/i, weight: 1,
          tip: 'The connector should link two related ideas. Make sure there are two distinct statements.' },
      ],
      forbidden: [
        { pattern: /^(also|and also|but|so)\b/i, tip: '"Also", "but", "so" are not C1-level connectors. Use a more sophisticated device.' },
      ],
      minWords: 10,
    },

    // ── C2 Grammar ────────────────────────────────────────────────

    'stylistic-inversion': {
      label: 'Stylistic inversion',
      example: 'So profound was the impact that the entire industry was transformed.',
      checks: [
        { name: 'So/Such opener OR negative adverbial', pattern: /^(so\s+\w+\s+(was|were|is|are)|such\s+(was|were|is|are)|never|not only|rarely|seldom|gone was|only then|little)/i, weight: 3,
          tip: 'Use "So + adjective + was/were", "Such was/were + NP", or a negative adverbial opener.' },
        { name: 'Subject after verb', pattern: /(was|were|is|are|had|has|did|do|does|can|could|would|will|shall|should)\s+(the|a|an|its|their|his|her|this|that|my|our|your|\w+\b)/i, weight: 1,
          tip: 'Ensure the verb comes before the subject in the inverted clause.' },
      ],
      minWords: 8,
    },

    'non-finite-clause': {
      label: 'Non-finite participial clause',
      example: 'Having considered all the evidence, the committee reached a unanimous decision.',
      checks: [
        { name: 'Participial opener', pattern: /^(having\s+\w+ed|being\s+\w+ed?|\w+ing\s+\w|exhausted by|surprised by|given that|considering|despite having|after having)\b/i, weight: 3,
          tip: 'Start with a non-finite participial clause: "Having + past participle...", "-ing clause...", or "Past participle + by..."' },
        { name: 'Main clause follows', pattern: /,\s*the\s+\w|,\s*(she|he|it|they|we|I)\s+\w/i, weight: 1,
          tip: 'The participial clause must be followed by a main clause, separated by a comma.' },
      ],
      forbidden: [
        { pattern: /^after\s+(i|he|she|they|we|it)\s+had\b/i, tip: 'You\'re using a finite clause ("After I had..."). A non-finite version would be "Having..." or "After having...".' },
      ],
      minWords: 8,
    },

    'comment-clause': {
      label: 'Comment clause',
      example: 'The results, strictly speaking, do not support the original hypothesis.',
      checks: [
        { name: 'Comment clause present', pattern: /\b(strictly speaking|broadly speaking|generally speaking|relatively speaking|as far as i can tell|as it happens|as i see it|needless to say|it goes without saying|as is well known|as has been noted|to put it simply|to be fair|frankly speaking|interestingly enough|as expected|as predicted)\b/i, weight: 3,
          tip: 'Insert a comment clause: "strictly speaking", "broadly speaking", "as far as I can tell", "needless to say", "as is well known".' },
        { name: 'Set off with commas', pattern: /,\s*(strictly|broadly|generally|relatively|as far|as it|as i|needless|it goes|as is|frankly|interestingly|as expected)[^,]+,/i, weight: 1,
          tip: 'Comment clauses should be set off with commas: "The data, strictly speaking, is inconclusive."' },
      ],
      minWords: 7,
    },


    // ── B1 Grammar ────────────────────────────────────────────────

    'simple-passive': {
      label: 'Simple passive voice',
      example: 'The windows are cleaned every Friday.',
      checks: [
        { name: 'be + past participle', pattern: /\b(is|are|was|were|has been|have been|had been)\s+(\w+ed|written|made|built|found|given|seen|taken|broken|chosen|driven|eaten|grown|known|shown|spoken|stolen|thrown|worn|been|begun|come|done|gone|held|kept|left|let|met|paid|read|run|sat|sent|set|shut|sold|spent|stood|told|thought|taught|brought|bought|caught|felt|fought|got|had|heard|hurt|laid|led|lost|meant|met|put|quit|rid|said|sang|sank|sat|slept|slid|spat|spread|swam|swung|woke|won|wound|wept)\b/i, weight: 3,
          tip: 'Passive voice needs "be + past participle": is/are/was/were/has been + done/made/written etc.' },
        { name: 'No by-agent required but natural', pattern: /.+/, weight: 1,
          tip: 'Add a by-agent ("by someone") or a time expression to make the sentence complete.' },
      ],
      minWords: 4,
    },

    'reported-speech-stmt': {
      label: 'Reported speech (statement)',
      example: 'She said that she was very tired.',
      checks: [
        { name: 'Reporting verb', pattern: /\b(said|told|explained|mentioned|admitted|claimed|insisted|added|replied|announced|confirmed|denied)\b/i, weight: 2,
          tip: 'Use a reporting verb: said, told, explained, mentioned...' },
        { name: 'That clause or backshift', pattern: /(said|told|explained|mentioned)\s+(me\s+)?(that\s+)?\w+\s+(was|were|had|would|could|might)\b/i, weight: 2,
          tip: 'After "said/told", backshift the tense: "is" → "was", "will" → "would", "can" → "could".' },
      ],
      forbidden: [
        { pattern: /said\s+me\b/i, tip: '"said me" is wrong. Use "told me" (with indirect object) or "said to me". said + that-clause (no indirect object).' },
      ],
      minWords: 6,
    },

    'comparative-sentence': {
      label: 'Comparative sentence',
      example: 'This city is much more expensive than I expected.',
      checks: [
        { name: 'Comparative adjective or adverb', pattern: /\b(\w+er\b|more\s+\w+|less\s+\w+|as\s+\w+\s+as|not\s+as\s+\w+\s+as)\b/i, weight: 2,
          tip: 'Use a comparative form: adjective+er, "more + adjective", "less + adjective", or "as ... as".' },
        { name: 'Than / as comparison', pattern: /\bthan\b|\bas\s+\w+\s+as\b/i, weight: 2,
          tip: 'Complete the comparison with "than" (for -er/more/less) or "as ... as" for equal comparison.' },
      ],
      minWords: 5,
    },

    // ── B2 Grammar ────────────────────────────────────────────────

    'mixed-conditional': {
      label: 'Mixed conditional',
      example: 'If I had taken that job, I would be living in New York now.',
      checks: [
        { name: 'Past perfect in if-clause', pattern: /if\s+\w+\s+had\s+(not\s+)?\w+(ed|en|t|n)\b/i, weight: 3,
          tip: 'Mixed conditional: "If + past perfect" for the past cause. E.g. "If I had taken..."' },
        { name: 'Would + bare infinitive in main clause', pattern: /,\s*\w+\s+would\s+(be\s+\w+ing|be\s+\w+|have\s+\w+|still\s+\w+|\w+)\b/i, weight: 2,
          tip: 'Main clause: "would + infinitive" for the present result. E.g. "...I would be living in New York now."' },
        { name: 'Present time marker', pattern: /\b(now|still|today|at the moment|currently|these days|at present)\b/i, weight: 1,
          tip: 'Add a present time marker (now, still, today) to make the mixed time frames clear.' },
      ],
      minWords: 10,
    },

    'third-conditional': {
      label: 'Third conditional',
      example: 'If she had arrived earlier, she would have met him.',
      checks: [
        { name: 'If + past perfect', pattern: /if\s+\w+\s+had\s+(not\s+)?\w+(ed|en|t|n)\b/i, weight: 2,
          tip: 'Third conditional: "If + past perfect" (If she had arrived...)' },
        { name: 'Would have + past participle', pattern: /would\s+have\s+\w+(ed|en|t|n)\b/i, weight: 2,
          tip: 'Main clause: "would have + past participle" (would have met).' },
      ],
      minWords: 8,
    },

    'narrative-tense': {
      label: 'Narrative tense sequence',
      example: 'She had been waiting for two hours when he finally arrived.',
      checks: [
        { name: 'Past perfect/continuous for background', pattern: /\b(had\s+been\s+\w+ing|had\s+\w+(ed|en|t)|was\s+\w+ing|were\s+\w+ing)\b/i, weight: 2,
          tip: 'Use past perfect or past continuous for the background event (action happening before or during the main event).' },
        { name: 'Past simple for main event', pattern: /\b(when|until|as\s+soon\s+as|the\s+moment)\b.+\b\w+(ed|t)\b/i, weight: 2,
          tip: 'Use past simple for the main event: "...when he arrived", "...until she came".' },
      ],
      minWords: 8,
    },
  };

  // ── Core grading function ────────────────────────────────────────
  function grade(textarea, feedbackEl, taskKey) {
    var task = TASKS[taskKey];
    if (!task) {
      if (feedbackEl) feedbackEl.innerHTML = '<span style="color:var(--muted);font-size:.82rem">No task definition for: ' + taskKey + '</span>';
      return { score: 0, max: 0, passed: false };
    }

    var text = (textarea.value || '').trim();
    var words = text.split(/\s+/).filter(Boolean).length;

    var score = 0;
    var maxScore = task.checks.reduce(function(s, c) { return s + Math.max(0, c.weight); }, 0);
    var feedback = [];
    var passed = false;

    // ── Word count check ─────────────────────────────────────────
    if (!text || words < (task.minWords || 5)) {
      if (feedbackEl) {
        feedbackEl.innerHTML = renderFeedback([{type:'warn', msg: 'Write a complete sentence (at least ' + (task.minWords || 5) + ' words) to receive feedback.'}], 0, maxScore, task);
      }
      return { score: 0, max: maxScore, passed: false };
    }

    // ── Forbidden patterns ────────────────────────────────────────
    var forbiddenHits = [];
    (task.forbidden || []).forEach(function(f) {
      if (f.pattern.test(text)) {
        forbiddenHits.push({ type: 'error', msg: f.tip });
      }
    });

    // ── Required checks ───────────────────────────────────────────
    var checkResults = [];
    task.checks.forEach(function(check) {
      var ok = check.pattern.test(text);
      if (check.weight < 0) {
        // Negative check: passing the pattern is BAD
        if (ok) {
          checkResults.push({ ok: false, check: check });
          score += check.weight; // reduces score
          feedback.push({ type: 'error', msg: check.tip });
        }
      } else {
        if (ok) {
          score += check.weight;
          checkResults.push({ ok: true, check: check });
        } else {
          checkResults.push({ ok: false, check: check });
          feedback.push({ type: 'warn', msg: check.tip });
        }
      }
    });

    score = Math.max(0, score);
    passed = score >= Math.ceil(maxScore * 0.6); // 60% = passing

    // ── Build feedback display ────────────────────────────────────
    var allFeedback = forbiddenHits.concat(feedback);

    if (feedbackEl) {
      feedbackEl.innerHTML = renderFeedback(allFeedback, score, maxScore, task);
    }

    return { score: score, max: maxScore, passed: passed, text: text };
  }

  function renderFeedback(items, score, maxScore, task) {
    var pct = maxScore > 0 ? Math.round((score / maxScore) * 100) : 0;
    var col = pct >= 80 ? 'var(--green)' : pct >= 50 ? 'var(--amber)' : 'var(--red)';

    var html = '<div class="sg-panel">';

    // Score badge
    html += '<div class="sg-score-row">';
    html += '<span class="sg-label">Structure check</span>';
    html += '<span class="sg-badge" style="background:' + col + '">' + score + ' / ' + maxScore + '</span>';
    html += '</div>';

    // Feedback items
    if (items.length === 0 && pct >= 80) {
      html += '<div class="sg-item sg-pass">\u2713 The required ' + task.label + ' structure is present. Well done.</div>';
    } else if (items.length === 0 && pct >= 50) {
      html += '<div class="sg-item sg-warn">\u26a0 Structure partially detected. Check the example below.</div>';
    }

    items.forEach(function(item) {
      var icon = item.type === 'error' ? '\u2717' : '\u26a0';
      var cls = item.type === 'error' ? 'sg-error' : 'sg-warn-item';
      html += '<div class="sg-item ' + cls + '">' + icon + ' ' + item.msg + '</div>';
    });

    // Always show the example
    if (task.example) {
      html += '<div class="sg-example"><span class="sg-example-label">Model structure: </span>' + task.example + '</div>';
    }

    html += '</div>';
    return html;
  }

  // ── Auto-attach to all .sentence-grader textareas ───────────────
  function autoAttach() {
    document.querySelectorAll('textarea.sentence-grader').forEach(function(ta) {
      var taskKey = ta.dataset.task;
      var feedbackId = ta.id + '_feedback';
      var feedbackEl = document.getElementById(feedbackId);
      if (!feedbackEl) {
        feedbackEl = document.createElement('div');
        feedbackEl.id = feedbackId;
        feedbackEl.className = 'sg-feedback';
        ta.parentNode.insertBefore(feedbackEl, ta.nextSibling);
      }

      var timeout;
      ta.addEventListener('input', function() {
        clearTimeout(timeout);
        timeout = setTimeout(function() {
          grade(ta, feedbackEl, taskKey);
        }, 700);
      });

      ta.addEventListener('blur', function() {
        clearTimeout(timeout);
        if (ta.value.trim().length > 10) {
          grade(ta, feedbackEl, taskKey);
        }
      });
    });
  }

  // ── CSS ──────────────────────────────────────────────────────────
  var style = document.createElement('style');
  style.textContent = [
    '.sg-panel{border:1px solid var(--hairline);border-radius:6px;overflow:hidden;margin-top:8px;font-family:var(--font-sans)}',
    '.sg-score-row{display:flex;justify-content:space-between;align-items:center;padding:8px 12px;background:var(--cream-deep);border-bottom:1px solid var(--hairline)}',
    '.sg-label{font-size:.65rem;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:var(--muted)}',
    '.sg-badge{font-size:.75rem;font-weight:700;padding:3px 10px;border-radius:10px;color:white}',
    '.sg-item{padding:7px 12px;font-size:.82rem;line-height:1.5;border-bottom:1px solid var(--hairline)}',
    '.sg-item:last-child{border-bottom:0}',
    '.sg-pass{color:var(--green)}',
    '.sg-warn-item{color:var(--amber)}',
    '.sg-error{color:var(--red)}',
    '.sg-example{padding:8px 12px;font-size:.82rem;color:var(--muted);font-style:italic;background:rgba(184,134,11,.04)}',
    '.sg-example-label{font-style:normal;font-weight:700;color:var(--amber)}',
    'textarea.sentence-grader{width:100%;padding:10px 12px;font-family:Georgia,serif;font-size:.9rem;border:1.5px solid var(--hairline);border-radius:4px;background:var(--paper);color:var(--ink);resize:vertical;line-height:1.55;min-height:56px}',
    'textarea.sentence-grader:focus{border-color:var(--amber);outline:none}',
  ].join('');
  document.head.appendChild(style);

  // ── Public API ──────────────────────────────────────────────────
  window.SentenceGrader = { grade: grade, autoAttach: autoAttach, TASKS: TASKS };

  // Auto-attach on DOMContentLoaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', autoAttach);
  } else {
    autoAttach();
  }

})();
