"""francais-en B1 Grammar G01–G12 — French for English speakers"""

CHAPTERS = {
    "subjonctif-introduction": {
        "level": "b1",
        "section": "grammar",
        "num": "G01",
        "short": "Introduction to the Subjunctive",
        "title": "Introduction to the Subjunctive — Le Subjonctif",
        "subtitle": "A mood expressing wishes, necessity and doubt — triggered by specific verbs and expressions",
        "slides": [
            ("What Is the Subjunctive?",
             "The subjunctive is a mood, not a tense. It expresses wishes, doubt, necessity, emotion, and subjective attitudes. It appears in subordinate clauses introduced by <em>que</em> after specific trigger verbs or expressions.",
             '<table class="sum-table"><thead><tr><th>Indicative (fact)</th><th>Subjunctive (wish/doubt)</th></tr></thead><tbody>'
             '<tr><td>Il est là. (He is there — fact.)</td><td>Je veux qu\'il <b>soit</b> là. (I want him to be there.)</td></tr>'
             '<tr><td>Elle vient. (She is coming.)</td><td>Il faut qu\'elle <b>vienne</b>. (She must come.)</td></tr>'
             '<tr><td>Tu sais la réponse.</td><td>Je doute que tu <b>saches</b> la réponse.</td></tr>'
             '</tbody></table>'
             '<p><strong>Key rule:</strong> Two different subjects → use <em>que</em> + subjunctive. Same subject → use the infinitive: <em>Je veux partir.</em> (not: Je veux que je parte.)</p>'),
            ("Formation: Regular Verbs",
             "Take the <em>ils/elles</em> form of the present tense, drop <em>-ent</em>, and add the subjunctive endings: <b>-e, -es, -e, -ions, -iez, -ent</b>.",
             '<table class="sum-table"><thead><tr><th>Pronoun</th><th>parler (ils parlent → parl-)</th><th>finir (ils finissent → finiss-)</th><th>partir (ils partent → part-)</th></tr></thead><tbody>'
             '<tr><td>que je</td><td>parl<b>e</b></td><td>finiss<b>e</b></td><td>part<b>e</b></td></tr>'
             '<tr><td>que tu</td><td>parl<b>es</b></td><td>finiss<b>es</b></td><td>part<b>es</b></td></tr>'
             '<tr><td>qu\'il/elle</td><td>parl<b>e</b></td><td>finiss<b>e</b></td><td>part<b>e</b></td></tr>'
             '<tr><td>que nous</td><td>parl<b>ions</b></td><td>finiss<b>ions</b></td><td>part<b>ions</b></td></tr>'
             '<tr><td>que vous</td><td>parl<b>iez</b></td><td>finiss<b>iez</b></td><td>part<b>iez</b></td></tr>'
             '<tr><td>qu\'ils/elles</td><td>parl<b>ent</b></td><td>finiss<b>ent</b></td><td>part<b>ent</b></td></tr>'
             '</tbody></table>'
             '<p>Note: the <em>-ions/-iez</em> forms look like imparfait but sound different. <em>Nous parlions</em> (imparfait) vs <em>que nous parlions</em> (subjonctif) — context distinguishes them.</p>'),
            ("Irregular Stems: Être and Avoir",
             "The two most important irregular subjunctives are <em>être</em> and <em>avoir</em>. Their stems are completely irregular and must be memorised.",
             '<table class="sum-table"><thead><tr><th>Pronoun</th><th>être (soi- / soy-)</th><th>avoir (ai- / ay-)</th></tr></thead><tbody>'
             '<tr><td>que je</td><td>sois</td><td>aie</td></tr>'
             '<tr><td>que tu</td><td>sois</td><td>aies</td></tr>'
             '<tr><td>qu\'il/elle</td><td>soit</td><td>ait</td></tr>'
             '<tr><td>que nous</td><td>soyons</td><td>ayons</td></tr>'
             '<tr><td>que vous</td><td>soyez</td><td>ayez</td></tr>'
             '<tr><td>qu\'ils/elles</td><td>soient</td><td>aient</td></tr>'
             '</tbody></table>'
             '<p>Examples: <em>Il faut que tu <b>sois</b> à l\'heure.</em> (You must be on time.) — <em>Je veux que vous <b>ayez</b> les résultats.</em> (I want you to have the results.)</p>'),
            ("Key Trigger Expressions",
             "The subjunctive is required after these common triggers:",
             '<table class="sum-table"><thead><tr><th>Expression</th><th>Meaning</th><th>Example</th></tr></thead><tbody>'
             '<tr><td><b>vouloir que</b></td><td>to want (someone) to</td><td>Je veux qu\'il <b>vienne</b>.</td></tr>'
             '<tr><td><b>il faut que</b></td><td>it is necessary that / must</td><td>Il faut que tu <b>partes</b> maintenant.</td></tr>'
             '<tr><td><b>il est important que</b></td><td>it is important that</td><td>Il est important qu\'elle <b>sache</b> la vérité.</td></tr>'
             '<tr><td><b>souhaiter que</b></td><td>to wish that</td><td>Je souhaite qu\'il <b>réussisse</b>.</td></tr>'
             '<tr><td><b>préférer que</b></td><td>to prefer that</td><td>Elle préfère que nous <b>attendions</b>.</td></tr>'
             '<tr><td><b>avoir peur que</b></td><td>to be afraid that</td><td>J\'ai peur qu\'il <b>soit</b> en retard.</td></tr>'
             '<tr><td><b>douter que</b></td><td>to doubt that</td><td>Je doute qu\'ils <b>aient</b> raison.</td></tr>'
             '</tbody></table>'),
            ("Same Subject vs Different Subjects",
             "The subjunctive is only used when the subject of the main clause is different from the subject of the subordinate clause. With the same subject, use an infinitive.",
             '<table class="sum-table"><thead><tr><th>Different subjects → subjunctive</th><th>Same subject → infinitive</th></tr></thead><tbody>'
             '<tr><td>Je veux qu\'il <b>parte</b>. (I want him to leave.)</td><td>Je veux <b>partir</b>. (I want to leave.)</td></tr>'
             '<tr><td>Elle préfère que tu <b>restes</b>.</td><td>Elle préfère <b>rester</b>.</td></tr>'
             '<tr><td>Il faut que vous <b>soyez</b> là.</td><td>Il faut <b>être</b> là.</td></tr>'
             '</tbody></table>'
             '<p><strong>Quick check:</strong> two different people involved? → use <em>que</em> + subjunctive. Only one person? → use the infinitive.</p>'),
        ],
        "traps": [
            ("Je veux que je parte tôt.", "Je veux partir tôt.", "Same subject (both 'I') → use infinitive, not subjunctive. Subjunctive requires two different subjects."),
            ("Il faut que tu pars.", "Il faut que tu partes.", "After il faut que, use the subjunctive: partir → que tu partes (not pars, which is indicative)."),
            ("que nous soyions (être)", "que nous soyons", "Être is fully irregular in the subjunctive: soyons (not soyions). The stem is soy- for nous/vous forms."),
            ("que vous ayiez (avoir)", "que vous ayez", "Avoir subjunctive: ayez (not ayiez). The stem is ay- for nous/vous: ayons, ayez."),
        ],
        "summary": [
            ("Formation", "ils present – ent + -e/-es/-e/-ions/-iez/-ent", "parler → qu'il parle"),
            ("être (subj.)", "sois, sois, soit, soyons, soyez, soient", "qu'il soit là"),
            ("avoir (subj.)", "aie, aies, ait, ayons, ayez, aient", "qu'elle ait raison"),
            ("vouloir que", "want (s.o.) to", "Je veux qu'il vienne."),
            ("il faut que", "must / necessary that", "Il faut que tu partes."),
            ("douter que", "to doubt that", "Je doute qu'il soit prêt."),
            ("Two subjects", "→ que + subjunctive", "Je veux qu'elle parte."),
            ("Same subject", "→ infinitive", "Je veux partir."),
        ],
        "ex1": (
            "Choosing the Subjunctive",
            "Choose the correct subjunctive form to complete the sentence.",
            [
                ("Il faut que tu ___ (partir) avant midi.", ["pars", "partes", "parte", "partais"], "partes", "Partir: ils partent → stem: part-. Tu + -es: partes. Il faut que triggers subjunctive."),
                ("Je veux qu\'elle ___ (finir) ce travail.", ["finit", "finisse", "finit", "finira"], "finisse", "Finir: ils finissent → stem: finiss-. Elle + -e: finisse. Vouloir que triggers subjunctive."),
                ("Il est important que vous ___ (être) à l\'heure.", ["êtes", "soyez", "étiez", "serez"], "soyez", "Être is irregular in subjunctive: vous → soyez."),
                ("Elle préfère que nous ___ (attendre).", ["attendons", "attendrions", "attendions", "attendent"], "attendions", "Attendre: ils attendent → stem: attend-. Nous + -ions: attendions."),
                ("J\'ai peur qu\'il ___ (avoir) des problèmes.", ["a", "ait", "avait", "aura"], "ait", "Avoir is irregular in subjunctive: il → ait."),
                ("Je doute qu\'ils ___ (savoir) la réponse.", ["savent", "sachent", "savaient", "sauraient"], "sachent", "Savoir: ils sachent (irregular subjunctive). Douter que triggers subjunctive."),
            ]
        ),
        "ex2": (
            "Subjunctive or Infinitive?",
            "Write the verb in the correct form — infinitive or subjunctive.",
            [
                ("Je veux ___ (partir) à 8h. (I want to leave at 8.)", "partir", "Same subject (je/je) → infinitive: partir."),
                ("Je veux qu\'elle ___ (partir) à 8h. (I want her to leave at 8.)", "parte", "Different subjects (je/elle) → subjunctive: que elle parte."),
                ("Il faut ___ (être) prudent. (One must be careful.)", "être", "Il faut + infinitive when no specific subject named: il faut être."),
                ("Il faut que tu ___ (être) prudent.", "sois", "Specific subject (tu) → il faut que + subjunctive: sois (irregular)."),
                ("Nous préférons ___ (rester) ici. (We prefer to stay here.)", "rester", "Same subject (nous/nous) → infinitive: rester."),
            ]
        ),
        "ex3": (
            "Irregular Subjunctives",
            "Choose the correct irregular subjunctive form.",
            [
                ("il ___ (être)", ["soit", "est", "était", "serait"], "soit", "Être subjunctive: il → soit. Fully irregular stem: soi-."),
                ("nous ___ (avoir)", ["avons", "aurions", "ayons", "ayions"], "ayons", "Avoir subjunctive: nous → ayons. Irregular stem: ay-."),
                ("tu ___ (être)", ["es", "étais", "sois", "serais"], "sois", "Être subjunctive: tu → sois (same as je form)."),
                ("elles ___ (avoir)", ["ont", "aient", "auraient", "avaient"], "aient", "Avoir subjunctive: elles → aient."),
            ]
        ),
        "game_desc": "Master the French subjunctive — formation, irregular verbs, and triggers",
        "items": [
            ("subj-form", "ils – ent + endings", "subjunctive stem: drop -ent from ils/elles present", "subj. stem rule", "parler → ils parlent → parl- → qu'il parle", "subjunctive: ils form minus -ent, add -e/-es/-e/-ions/-iez/-ent", "parle"),
            ("subj-soit", "soit", "subjunctive of être (il/elle form) — must be memorised", "be (subj.)", "Il faut qu'il soit là. (He must be there.)", "être subjunctive: sois/sois/soit/soyons/soyez/soient", "soit"),
            ("subj-ait", "ait", "subjunctive of avoir (il/elle form) — must be memorised", "have (subj.)", "Je doute qu'elle ait raison. (I doubt she is right.)", "avoir subjunctive: aie/aies/ait/ayons/ayez/aient", "ait"),
            ("vouloir-que", "vouloir que", "trigger: to want (someone) to — requires subjunctive", "want s.o. to", "Je veux qu'il parte maintenant.", "vouloir que + subjunctive", "parte"),
            ("il-faut-que", "il faut que", "trigger: it is necessary that / must — requires subjunctive", "must (subj.)", "Il faut que tu sois à l'heure.", "il faut que + subjunctive", "sois"),
            ("douter-que", "douter que", "trigger: to doubt that — requires subjunctive", "doubt that", "Je doute qu'ils sachent la réponse.", "douter que + subjunctive", "sachent"),
            ("two-subjects", "2 subjects → subj.", "different subjects in main and subordinate clause → subjunctive", "2 subjects", "Je veux qu'elle parte. (not: Je veux qu'elle part.)", "2 different subjects → que + subjunctive", "parte"),
            ("same-subject", "1 subject → infin.", "same subject in both clauses → infinitive (not subjunctive)", "1 subject", "Je veux partir. (not: Je veux que je parte.)", "same subject → infinitive", "partir"),
        ],
    },

    "conditional": {
        "level": "b1",
        "section": "grammar",
        "num": "G02",
        "short": "Conditionnel présent",
        "title": "Conditionnel présent — The Conditional",
        "subtitle": "Express politeness, hypothetical situations, and conditions with si + imparfait",
        "slides": [
            ("Formation: Future Stem + Imparfait Endings",
             "The conditional uses the same stems as the future simple (usually the full infinitive for regular verbs) plus the endings of the imparfait: <b>-ais, -ais, -ait, -ions, -iez, -aient</b>.",
             '<table class="sum-table"><thead><tr><th>Pronoun</th><th>parler (stem: parler-)</th><th>finir (stem: finir-)</th><th>attendre (stem: attendr-)</th></tr></thead><tbody>'
             '<tr><td>je</td><td>parler<b>ais</b></td><td>finir<b>ais</b></td><td>attendr<b>ais</b></td></tr>'
             '<tr><td>tu</td><td>parler<b>ais</b></td><td>finir<b>ais</b></td><td>attendr<b>ais</b></td></tr>'
             '<tr><td>il/elle</td><td>parler<b>ait</b></td><td>finir<b>ait</b></td><td>attendr<b>ait</b></td></tr>'
             '<tr><td>nous</td><td>parler<b>ions</b></td><td>finir<b>ions</b></td><td>attendr<b>ions</b></td></tr>'
             '<tr><td>vous</td><td>parler<b>iez</b></td><td>finir<b>iez</b></td><td>attendr<b>iez</b></td></tr>'
             '<tr><td>ils/elles</td><td>parler<b>aient</b></td><td>finir<b>aient</b></td><td>attendr<b>aient</b></td></tr>'
             '</tbody></table>'
             '<p><em>Note on -re verbs:</em> drop the final <em>-e</em> before adding endings: attendre → attendr- → j\'attendrais.</p>'),
            ("Irregular Stems — Same as Future",
             "The irregular conditional stems are identical to the irregular future stems. These must be memorised:",
             '<table class="sum-table"><thead><tr><th>Infinitive</th><th>Cond./Future stem</th><th>Conditional (il form)</th></tr></thead><tbody>'
             '<tr><td>être</td><td>ser-</td><td>il <b>serait</b></td></tr>'
             '<tr><td>avoir</td><td>aur-</td><td>il <b>aurait</b></td></tr>'
             '<tr><td>aller</td><td>ir-</td><td>il <b>irait</b></td></tr>'
             '<tr><td>faire</td><td>fer-</td><td>il <b>ferait</b></td></tr>'
             '<tr><td>pouvoir</td><td>pourr-</td><td>il <b>pourrait</b></td></tr>'
             '<tr><td>vouloir</td><td>voudr-</td><td>il <b>voudrait</b></td></tr>'
             '<tr><td>venir</td><td>viendr-</td><td>il <b>viendrait</b></td></tr>'
             '<tr><td>savoir</td><td>saur-</td><td>il <b>saurait</b></td></tr>'
             '<tr><td>devoir</td><td>devr-</td><td>il <b>devrait</b></td></tr>'
             '</tbody></table>'),
            ("Use 1: Polite Requests and Suggestions",
             "The conditional softens requests, making them more polite. It is essential for formal and social contexts:",
             '<ul class="slide-list">'
             '<li><b>Je voudrais</b> un café, s\'il vous plaît. (I would like a coffee.) — much more polite than: Je veux un café.</li>'
             '<li><b>Pourriez-vous</b> répéter? (Could you repeat that?) — polite form of pouvoir</li>'
             '<li><b>Tu devrais</b> parler à ton professeur. (You should talk to your teacher.) — devoir conditional = should</li>'
             '<li><b>On pourrait</b> aller au cinéma ce soir. (We could go to the cinema tonight.) — suggestion</li>'
             '<li><b>Auriez-vous</b> l\'heure? (Would you have the time?) — formal request</li></ul>'),
            ("Use 2: Si + Imparfait + Conditionnel",
             "For hypothetical situations in the present or future (things that are unlikely or imaginary), use: <b>si + imparfait</b> in the condition, <b>conditionnel</b> in the result.",
             '<table class="sum-table"><thead><tr><th>Si clause (imparfait)</th><th>Result clause (conditionnel)</th></tr></thead><tbody>'
             '<tr><td>Si j\'avais de l\'argent,</td><td>j\'achèterais une voiture.</td></tr>'
             '<tr><td>(If I had money,)</td><td>(I would buy a car.)</td></tr>'
             '<tr><td>Si elle était là,</td><td>elle t\'aiderait.</td></tr>'
             '<tr><td>(If she were here,)</td><td>(she would help you.)</td></tr>'
             '<tr><td>Si vous vouliez,</td><td>vous pourriez partir plus tôt.</td></tr>'
             '<tr><td>(If you wanted to,)</td><td>(you could leave earlier.)</td></tr>'
             '</tbody></table>'
             '<p><strong>Rule:</strong> Never put the conditional in the <em>si</em> clause. Si is always followed by imparfait (for hypothetical), never by conditional.</p>'),
            ("Use 3: Unconfirmed Information (Journalistic Conditional)",
             "In French journalism and formal speech, the conditional is used to report unverified information — translating as 'reportedly' or 'allegedly':",
             '<ul class="slide-list">'
             '<li>Le président <b>serait</b> en visite à Paris. (The president is reportedly visiting Paris.)</li>'
             '<li>L\'accident <b>aurait</b> fait trois blessés. (The accident reportedly left three injured.)</li>'
             '<li>Ce médicament <b>pourrait</b> guérir la maladie. (This drug could allegedly cure the disease.)</li></ul>'
             '<p>This use signals that the speaker is not personally vouching for the truth of the statement — it is attributed information.</p>'),
        ],
        "traps": [
            ("Si j'aurais de l'argent…", "Si j'avais de l'argent…", "Never use the conditional after si in a hypothetical clause. Si + imparfait (not conditional)."),
            ("je voudrais → je voudrait", "je voudrais", "The ending for je is -ais (not -ait). Je voudrais (I would like). Il voudrait (he would like)."),
            ("attendrais (wrong stem: attenderais)", "j'attendrais", "For -re verbs, drop the final -e: attendre → attendr-. Add -ais: j'attendrais (not attenderais)."),
            ("devrais = I must (present)", "devrais = I should (conditional)", "Je dois = I must (present). Je devrais = I should (conditional). They are different tenses with different meanings."),
        ],
        "summary": [
            ("Stem", "future stem (infin. for regular)", "parler- / finir- / attendr-"),
            ("Endings", "-ais/-ais/-ait/-ions/-iez/-aient", "je parlerais, il parlerait"),
            ("être → serait", "irregular stem: ser-", "Il serait content."),
            ("avoir → aurait", "irregular stem: aur-", "Elle aurait raison."),
            ("aller → irait", "irregular stem: ir-", "On irait au cinéma."),
            ("Politeness", "je voudrais / tu devrais", "Je voudrais un café."),
            ("Si + hypothetical", "si + imparfait + conditionnel", "Si j'avais le temps, j'irais."),
            ("Journalistic", "reportedly / allegedly", "Il serait à Paris."),
        ],
        "ex1": (
            "Forming the Conditional",
            "Choose the correct conditional form.",
            [
                ("Si j\'avais le temps, je ___ (voyager) plus.", ["voyagerai", "voyagerais", "voyagerais", "voyagiais"], "voyagerais", "Hypothetical: si + imparfait → conditional. Voyager: stem voyager- + -ais: je voyagerais."),
                ("Elle ___ (vouloir) un café, s\'il vous plaît.", ["veut", "voulait", "voudrait", "voudra"], "voudrait", "Polite request: vouloir → irregular stem voudr- + -ait: voudrait."),
                ("Si vous ___ (avoir) un problème, appelez-moi.", ["avez", "auriez", "aurez", "aviez"], "aviez", "Si clause (hypothetical) → imparfait, not conditional: si vous aviez (avoir imparfait)."),
                ("Tu ___ (devoir) te reposer davantage.", ["dois", "devais", "devrais", "devras"], "devrais", "Advice/should: devoir → irregular stem devr- + -ais: tu devrais."),
                ("Ils ___ (pouvoir) venir demain.", ["peuvent", "pourraient", "pourront", "pouvaient"], "pourraient", "Hypothetical possibility: pouvoir → pourr- + -aient: pourraient."),
            ]
        ),
        "ex2": (
            "Translate into French",
            "Write the sentence in French using the conditional.",
            [
                ("I would like to reserve a table for two.", "Je voudrais réserver une table pour deux personnes.", "Polite request: vouloir → je voudrais. Réserver = to reserve. Pour deux personnes = for two people."),
                ("If he studied more, he would pass.", "S'il étudiait plus, il réussirait.", "Si + imparfait (étudiait) + conditional (réussirait). Réussir → réussir- + -ait."),
                ("You should call your mother. (informal)", "Tu devrais appeler ta mère.", "Devoir conditional: tu devrais = you should."),
                ("Could you open the window? (formal)", "Pourriez-vous ouvrir la fenêtre?", "Polite question: pouvoir → pourriez. Inversion: pourriez-vous."),
                ("We could go to the beach this weekend.", "On pourrait aller à la plage ce week-end.", "Suggestion: pouvoir → on pourrait."),
            ]
        ),
        "ex3": (
            "Si Clauses — Imparfait or Conditional?",
            "Choose the correct tense for each blank in the si clause structure.",
            [
                ("Si elle ___ (être) là, je serais content.", ["serait", "était", "est", "sera"], "était", "Si clause (hypothetical) → imparfait: était. Never use conditional after si."),
                ("Si tu pouvais, tu ___ (aider) ton ami.", ["aideras", "aides", "aiderais", "aidais"], "aiderais", "Result clause (after si + imparfait) → conditional: tu aiderais."),
                ("Si nous avions le temps, nous ___ (faire) une promenade.", ["ferions", "faisions", "ferons", "faisions"], "ferions", "Result clause → conditional: faire → fer- + -ions: ferions."),
                ("Si j\'___ (aller) à Paris, je visiterais le Louvre.", ["irais", "allais", "irai", "vais"], "allais", "Si clause → imparfait: aller → j'allais (not conditional)."),
            ]
        ),
        "game_desc": "Master the French conditional — formation, irregular stems, and si clauses",
        "items": [
            ("cond-stem", "futur stem + endings", "conditional = future stem + imparfait endings (-ais/-ais/-ait/-ions/-iez/-aient)", "stem + endings", "parler → je parlerais, tu parlerais, il parlerait", "conditional: future stem + -ais/-ais/-ait/-ions/-iez/-aient", "parlerais"),
            ("serait", "serait", "conditional of être (il/elle form) — irregular stem: ser-", "would be", "Si j'étais riche, je serais heureux.", "être → ser- → il serait", "serait"),
            ("aurait", "aurait", "conditional of avoir (il/elle form) — irregular stem: aur-", "would have", "Il aurait raison si tu l'écoutais.", "avoir → aur- → il aurait", "aurait"),
            ("voudrais", "voudrais", "conditional of vouloir (je form) — polite request", "would like", "Je voudrais un thé, s'il vous plaît.", "vouloir → voudr- → je voudrais (polite)", "voudrais"),
            ("devrais", "devrais", "conditional of devoir — means 'should' (advice)", "should", "Tu devrais dormir plus. (You should sleep more.)", "devoir → devr- → tu devrais = you should", "devrais"),
            ("pourrait", "pourrait", "conditional of pouvoir — could / might", "could", "On pourrait aller au cinéma. (We could go to the cinema.)", "pouvoir → pourr- → il pourrait = could", "pourrait"),
            ("si-imparfait", "si + imparfait", "hypothetical si clause: always imparfait (never conditional)", "if (hypothetical)", "Si j'avais de l'argent, j'achèterais une voiture.", "si + imparfait (NEVER conditional) + result: conditional", "avais"),
            ("irait", "irait", "conditional of aller — irregular stem: ir-", "would go", "Elle irait en France si elle pouvait.", "aller → ir- → il irait = would go", "irait"),
        ],
    },

    "plus-que-parfait": {
        "level": "b1",
        "section": "grammar",
        "num": "G03",
        "short": "Plus-que-parfait",
        "title": "Plus-que-parfait — The Pluperfect",
        "subtitle": "Express an action that happened before another past action",
        "slides": [
            ("What Is the Plus-que-parfait?",
             "The plus-que-parfait (pluperfect) describes an action that was completed BEFORE another past action. In English: 'had done', 'had arrived', 'had eaten'.",
             '<table class="sum-table"><thead><tr><th>Earlier action (PQP)</th><th>Later action (PC or imparfait)</th></tr></thead><tbody>'
             '<tr><td>Quand je suis arrivé,</td><td>elle <b>était déjà partie</b>.</td></tr>'
             '<tr><td>(When I arrived,)</td><td>(she had already left.)</td></tr>'
             '<tr><td>Il n\'a pas pu entrer</td><td>parce qu\'il <b>avait oublié</b> ses clés.</td></tr>'
             '<tr><td>(He couldn\'t get in)</td><td>(because he had forgotten his keys.)</td></tr>'
             '</tbody></table>'),
            ("Formation: Avoir/Être in Imparfait + Past Participle",
             "The plus-que-parfait is formed with the auxiliary (<em>avoir</em> or <em>être</em>) in the <b>imparfait</b> + the past participle. The same verbs that use être in the passé composé use être in the PQP.",
             '<table class="sum-table"><thead><tr><th>Pronoun</th><th>manger (avoir aux.)</th><th>aller (être aux.)</th></tr></thead><tbody>'
             '<tr><td>j\'</td><td>j\'<b>avais mangé</b></td><td>j\'<b>étais allé(e)</b></td></tr>'
             '<tr><td>tu</td><td>tu <b>avais mangé</b></td><td>tu <b>étais allé(e)</b></td></tr>'
             '<tr><td>il/elle</td><td>il <b>avait mangé</b></td><td>elle <b>était allée</b></td></tr>'
             '<tr><td>nous</td><td>nous <b>avions mangé</b></td><td>nous <b>étions allés</b></td></tr>'
             '<tr><td>vous</td><td>vous <b>aviez mangé</b></td><td>vous <b>étiez allés</b></td></tr>'
             '<tr><td>ils/elles</td><td>ils <b>avaient mangé</b></td><td>elles <b>étaient allées</b></td></tr>'
             '</tbody></table>'
             '<p>All the same agreement rules apply: être verbs agree with subject; avoir verbs do not agree with subject.</p>'),
            ("Time Markers That Signal the PQP",
             "Certain words and structures typically appear with the plus-que-parfait to show one action came before another:",
             '<table class="sum-table"><thead><tr><th>Expression</th><th>Meaning</th><th>Example</th></tr></thead><tbody>'
             '<tr><td><b>quand / lorsque</b></td><td>when</td><td>Quand il est arrivé, elle <b>était déjà partie</b>.</td></tr>'
             '<tr><td><b>après que</b></td><td>after</td><td>Après qu\'il <b>avait mangé</b>, il s\'est couché.</td></tr>'
             '<tr><td><b>avant que (+ subj.)</b></td><td>before (subj.)</td><td>avant qu\'il <b>parte</b> (subjunctive, not PQP)</td></tr>'
             '<tr><td><b>déjà</b></td><td>already</td><td>Elle <b>avait déjà</b> vu ce film.</td></tr>'
             '<tr><td><b>parce que / car</b></td><td>because</td><td>Il était fatigué parce qu\'il <b>avait travaillé</b> toute la nuit.</td></tr>'
             '<tr><td><b>une fois que</b></td><td>once</td><td>Une fois qu\'il <b>était parti</b>, j\'ai pu dormir.</td></tr>'
             '</tbody></table>'),
            ("PQP in Context: Storytelling",
             "In a narrative, the PQP is used alongside the passé composé and imparfait to show the sequence of events. The PQP indicates the furthest-back action.",
             '<ul class="slide-list">'
             '<li>Hier, je suis allé chercher mes billets, mais je <b>les avais déjà perdus</b>. (Yesterday I went to get my tickets, but I had already lost them.)</li>'
             '<li>Elle était fatiguée parce qu\'elle <b>s\'était couchée</b> très tard. (She was tired because she had gone to bed very late.)</li>'
             '<li>Quand nous sommes arrivés au restaurant, ils <b>avaient déjà commandé</b>. (When we arrived at the restaurant, they had already ordered.)</li>'
             '<li>Il ne savait pas que tu <b>avais essayé</b> de le contacter. (He didn\'t know you had tried to contact him.)</li></ul>'),
        ],
        "traps": [
            ("j'avais été là → for 'I had gone there'", "j'étais allé(e) là", "Aller takes être as auxiliary: j'étais allé (PQP). Avoir + été is the PQP of être itself (j'avais été = I had been)."),
            ("elle avait partée", "elle était partie", "Partir uses être, not avoir. PQP: elle était partie. With être, the participle agrees: partie (f.)."),
            ("Après qu'il a mangé, il s'est couché. (trying PQP)", "Après qu'il avait mangé, il s'est couché.", "After après que, use PQP to emphasise the completed earlier action before the next past action."),
            ("nous avions allés", "nous étions allés", "Aller = être auxiliary. PQP: nous étions allés. Never avions allés."),
        ],
        "summary": [
            ("Formula", "avoir/être (imparfait) + past participle", "j'avais mangé / j'étais allé"),
            ("avoir aux.", "most verbs", "j'avais fini, il avait dit"),
            ("être aux.", "movement + reflexive verbs", "elle était partie, il s'était levé"),
            ("Agreement", "être: agrees with subject", "elles étaient arrivées"),
            ("quand + PQP", "when (before another past action)", "Quand il est arrivé, j'avais fini."),
            ("déjà + PQP", "already", "Elle avait déjà mangé."),
            ("parce que + PQP", "because (earlier cause)", "Il était triste parce qu'elle était partie."),
            ("Timeline", "PQP → PC/imparfait", "PQP = earlier; PC/imparfait = later"),
        ],
        "ex1": (
            "Forming the Plus-que-parfait",
            "Choose the correct plus-que-parfait form.",
            [
                ("Quand il est arrivé, elle ___ (partir) déjà.", ["a déjà partie", "était déjà partie", "avait déjà parti", "était déjà partis"], "était déjà partie", "Partir uses être. PQP: elle était partie. Feminine subject → partie."),
                ("Je ne savais pas qu\'ils ___ (manger) avant moi.", ["ont mangé", "avaient mangé", "mangeaient", "avaient mangés"], "avaient mangé", "Manger uses avoir. PQP: ils avaient mangé. No agreement with avoir."),
                ("Elle était fatiguée parce qu\'elle ___ (se coucher) tard.", ["s'est couchée", "s'était couchée", "avait couchée", "était couchée"], "s'était couchée", "Reflexive: se coucher → être aux. PQP: s'était couchée (f. agreement)."),
                ("Il n\'a pas pu entrer car il ___ (oublier) ses clés.", ["avait oublié", "a oublié", "oubliait", "avait oubliés"], "avait oublié", "Oublier → avoir aux. PQP: il avait oublié. No agreement."),
                ("Nous ___ (voir) ce film avant de lire le livre.", ["avons vu", "avions vu", "étions vu", "avions vus"], "avions vu", "Voir → avoir aux. PQP: nous avions vu. No agreement."),
            ]
        ),
        "ex2": (
            "Translate into French",
            "Write the sentence in French using the plus-que-parfait.",
            [
                ("She had already left when I arrived.", "Elle était déjà partie quand je suis arrivé.", "Partir → être aux. PQP: était partie. Quand = when; arriver PC: je suis arrivé."),
                ("He hadn't eaten since the morning.", "Il n'avait pas mangé depuis le matin.", "Manger → avoir aux. PQP negative: il n'avait pas mangé. Depuis = since."),
                ("They (f.) had visited Paris before the trip.", "Elles avaient visité Paris avant le voyage.", "Visiter → avoir aux. PQP: elles avaient visité. No agreement with avoir."),
                ("We had already seen that film.", "Nous avions déjà vu ce film.", "Voir → avoir aux. PQP: nous avions vu. Déjà = already."),
                ("I was tired because I had worked all night.", "J'étais fatigué(e) parce que j'avais travaillé toute la nuit.", "State: imparfait (étais). Earlier cause: PQP (avais travaillé). Toute la nuit = all night."),
            ]
        ),
        "ex3": (
            "PQP or Passé Composé?",
            "Choose the tense that fits the timeline.",
            [
                ("Quand je suis arrivé, Marie ___ (partir) déjà.", ["est partie", "était déjà partie", "partait", "a déjà parti"], "était déjà partie", "Marie's leaving happened BEFORE the arrival → PQP: était partie."),
                ("Hier, j\'___ (appeler) Paul et il m\'a rappelé.", ["avais appelé", "ai appelé", "avais appeler", "appelais"], "ai appelé", "Single completed sequence (same timeline): passé composé: j'ai appelé."),
                ("Il était triste parce qu\'il ___ (perdre) son travail.", ["perd", "avait perdu", "perdait", "a perdu"], "avait perdu", "Losing the job happened BEFORE his sadness → PQP: avait perdu."),
                ("Elle n\'a pas pu venir parce qu\'elle ___ (tomber) malade.", ["tombait", "est tombée", "était tombée", "tombe"], "était tombée", "Falling ill happened BEFORE the inability to come → PQP: était tombée."),
            ]
        ),
        "game_desc": "Master the plus-que-parfait — the tense for actions before other past actions",
        "items": [
            ("pqp-formula", "avoir/être (imparfait) + PP", "pluperfect: auxiliary in imparfait + past participle", "had done", "j'avais mangé / j'étais allé(e)", "PQP = avoir/être (imparfait) + participe passé", "avais mangé"),
            ("pqp-avoir", "avais / avait", "imparfait of avoir as auxiliary in PQP", "had (aux.)", "Il avait oublié ses clés. (He had forgotten his keys.)", "avoir PQP: j'avais / tu avais / il avait…", "avait"),
            ("pqp-etre", "étais / était", "imparfait of être as auxiliary in PQP (movement + reflexive verbs)", "had (aux.)", "Elle était déjà partie. (She had already left.)", "être PQP: j'étais / tu étais / il était…", "était"),
            ("pqp-deja", "déjà + PQP", "already — common with PQP to show prior completion", "already", "Quand il est arrivé, elle avait déjà mangé.", "déjà + PQP = already done before another past action", "avait déjà"),
            ("pqp-quand", "quand + séquence", "when — introduces the later action; PQP in the other clause", "when (sequence)", "Quand je suis arrivé, elle était partie.", "quand (PC) + PQP = sequence in past", "était partie"),
            ("pqp-parce-que", "parce que + PQP", "because — PQP gives the earlier cause of a past state", "because (past)", "Il était fatigué parce qu'il avait travaillé toute la nuit.", "cause before state → PQP after parce que", "avait travaillé"),
            ("pqp-agree-etre", "accord avec être", "PQP with être: participle agrees with subject in gender/number", "agreement", "Elles étaient arrivées tôt. (They had arrived early.)", "être aux. in PQP → agreement same as PC", "étaient arrivées"),
            ("pqp-timeline", "PQP → PC/imparfait", "PQP is the furthest-back action; PC/imparfait is the next layer", "timeline", "Elle était partie quand il est arrivé. (She had left when he arrived.)", "PQP = before; PC = after in past timeline", "était partie"),
        ],
    },

    "passive-voice": {
        "level": "b1",
        "section": "grammar",
        "num": "G04",
        "short": "Voix passive",
        "title": "Voix passive — The Passive Voice",
        "subtitle": "Move the focus from the doer to the receiver of an action using être + past participle",
        "slides": [
            ("What Is the Passive Voice?",
             "In an active sentence, the subject does the action. In a passive sentence, the subject receives the action. The doer (agent) may or may not be mentioned.",
             '<table class="sum-table"><thead><tr><th>Active</th><th>Passive</th></tr></thead><tbody>'
             '<tr><td>Le chef prépare le repas.</td><td>Le repas <b>est préparé</b> par le chef.</td></tr>'
             '<tr><td>(The chef prepares the meal.)</td><td>(The meal is prepared by the chef.)</td></tr>'
             '<tr><td>Les étudiants ont fait l\'exercice.</td><td>L\'exercice <b>a été fait</b> par les étudiants.</td></tr>'
             '<tr><td>(The students did the exercise.)</td><td>(The exercise was done by the students.)</td></tr>'
             '</tbody></table>'
             '<p>The passive moves the object of the active sentence to subject position. The verb changes to <em>être</em> + past participle.</p>'),
            ("Formation: Être + Past Participle (Agreed)",
             "The passive is formed with <b>être conjugated in any tense</b> + the past participle. The past participle <b>always agrees</b> with the subject of the passive sentence.",
             '<table class="sum-table"><thead><tr><th>Tense</th><th>Formula</th><th>Example</th></tr></thead><tbody>'
             '<tr><td>Present</td><td>est/sont + PP</td><td>La lettre <b>est écrite</b>.</td></tr>'
             '<tr><td>Passé composé</td><td>a été / ont été + PP</td><td>La lettre <b>a été écrite</b>.</td></tr>'
             '<tr><td>Imparfait</td><td>était / étaient + PP</td><td>La lettre <b>était écrite</b>.</td></tr>'
             '<tr><td>Future</td><td>sera / seront + PP</td><td>La lettre <b>sera écrite</b>.</td></tr>'
             '<tr><td>Conditional</td><td>serait / seraient + PP</td><td>La lettre <b>serait écrite</b>.</td></tr>'
             '</tbody></table>'
             '<p><em>La lettre</em> is feminine → écrit<b>e</b>. <em>Les lettres</em> → écrit<b>es</b>. Agreement is mandatory.</p>'),
            ("The Agent: Par or De?",
             "The agent (the doer of the action) is usually introduced by <b>par</b>. A few verbs of state or feeling use <b>de</b>:",
             '<table class="sum-table"><thead><tr><th>par (by — active agent)</th><th>de (by — state/feeling)</th></tr></thead><tbody>'
             '<tr><td>La décision a été prise <b>par</b> le directeur.</td><td>Elle est <b>aimée de</b> tout le monde.</td></tr>'
             '<tr><td>(The decision was taken by the director.)</td><td>(She is loved by everyone.)</td></tr>'
             '<tr><td>Le livre a été écrit <b>par</b> Camus.</td><td>Il est <b>respecté de</b> ses collègues.</td></tr>'
             '<tr><td>(The book was written by Camus.)</td><td>(He is respected by his colleagues.)</td></tr>'
             '</tbody></table>'
             '<p>In most cases, use <em>par</em>. Use <em>de</em> mainly with verbs expressing emotions or habitual states: <em>aimer, respecter, admirer, accompagner, entourer</em>.</p>'),
            ("Avoiding the Passive: On",
             "French often prefers to avoid the passive by using <b>on</b> as an impersonal subject (similar to 'one', 'they', 'people', or a passive in English).",
             '<table class="sum-table"><thead><tr><th>Passive</th><th>With on (preferred in speech)</th></tr></thead><tbody>'
             '<tr><td>Le français est parlé ici.</td><td><b>On</b> parle français ici.</td></tr>'
             '<tr><td>(French is spoken here.)</td><td></td></tr>'
             '<tr><td>Les portes ont été ouvertes.</td><td><b>On</b> a ouvert les portes.</td></tr>'
             '<tr><td>(The doors were opened.)</td><td></td></tr>'
             '<tr><td>Des fautes ont été faites.</td><td><b>On</b> a fait des fautes.</td></tr>'
             '</tbody></table>'
             '<p>In spoken and informal French, <em>on</em> is very commonly used instead of the passive, especially when the agent is unknown or unimportant.</p>'),
            ("Converting Active to Passive",
             "Steps to convert an active sentence to passive: (1) make the active object into the passive subject; (2) conjugate être in the same tense as the original verb; (3) add past participle, agreed with new subject; (4) add <em>par + agent</em> if needed.",
             '<table class="sum-table"><thead><tr><th>Step</th><th>Active</th><th>Passive</th></tr></thead><tbody>'
             '<tr><td>Original</td><td>Les enfants mangent le gâteau.</td><td>→</td></tr>'
             '<tr><td>New subject</td><td>(le gâteau becomes subject)</td><td>Le gâteau ___</td></tr>'
             '<tr><td>Être + tense</td><td>(manger = présent)</td><td>Le gâteau est ___</td></tr>'
             '<tr><td>Past participle (agreed)</td><td>(gâteau = m.sg.)</td><td>Le gâteau est mangé ___</td></tr>'
             '<tr><td>Agent</td><td>(les enfants = agent)</td><td>Le gâteau est mangé <b>par les enfants</b>.</td></tr>'
             '</tbody></table>'),
        ],
        "traps": [
            ("La lettre est écrit par Paul.", "La lettre est écrite par Paul.", "The past participle in the passive agrees with the subject. La lettre is feminine → écrite (not écrit)."),
            ("Le livre a été écrit de Paul.", "Le livre a été écrit par Paul.", "Use par for an active agent doing a specific action. De is used only for states/emotions (aimer de, respecter de)."),
            ("Ils sont mangés (passive confusion with être verbs)", "Ils ont mangé. / Le repas est mangé.", "Être + past participle can be passive OR the passé composé of an être verb. Context clarifies: <em>Ils sont allés</em> (PC of aller) vs <em>Le repas est mangé</em> (passive)."),
            ("On parles français ici.", "On parle français ici.", "On takes the third-person singular (il/elle) form: on parle, on mange, on fait. Never add -s."),
        ],
        "summary": [
            ("Formula", "être (any tense) + past participle", "La lettre est écrite."),
            ("Agreement", "PP agrees with passive subject", "Les lettres sont écrites."),
            ("Agent", "par + agent (active doer)", "écrit par le professeur"),
            ("par vs de", "par (action); de (state/emotion)", "aimée de tous"),
            ("PC passive", "a été + PP", "Le film a été tourné à Paris."),
            ("Imparfait passive", "était + PP", "La porte était ouverte."),
            ("Avoid: on", "on = informal alternative", "On parle français ici."),
            ("Converting", "object → subject; verb → être + PP", "Les enfants mangent le gâteau → Le gâteau est mangé."),
        ],
        "ex1": (
            "Forming the Passive",
            "Choose the correct passive construction.",
            [
                ("La maison ___ (construire) par des architectes. (present)", ["est construite", "est construit", "a construite", "est construite"], "est construite", "Construire passive present: est + construite. La maison is feminine → construite."),
                ("Le film ___ (tourner) en 1999. (PC)", ["a été tourné", "a été tournée", "est tourné", "était tourné"], "a été tourné", "Passive PC: a été + past participle. Le film is masculine → tourné."),
                ("Les résultats ___ (annoncer) demain. (future)", ["seront annoncés", "sont annoncés", "ont été annoncés", "seraient annoncés"], "seront annoncés", "Passive future: seront + annoncés. Les résultats = masculine plural → annoncés."),
                ("La lettre ___ (écrire) par Marie. (imparfait)", ["était écrite", "était écrit", "a été écrite", "sera écrite"], "était écrite", "Passive imparfait: était + écrite. La lettre = feminine → écrite."),
                ("Ces peintures ___ (faire) par Picasso.", ["ont été faites", "ont été fait", "sont faites", "ont fait"], "ont été faites", "Passive PC: ont été + faites. Ces peintures = feminine plural → faites."),
                ("Le problème ___ (résoudre) par l\'équipe.", ["a été résolu", "a été résolue", "est résolue", "avait résolu"], "a été résolu", "Résoudre → résolu. Le problème = masculine → résolu (no agreement with avoir in passive formula)."),
            ]
        ),
        "ex2": (
            "Convert Active to Passive",
            "Rewrite the sentence in the passive voice.",
            [
                ("Le professeur corrige les examens.", "Les examens sont corrigés par le professeur.", "Examens → subject. Corriger (présent) → sont corrigés. Examens = m.pl. → corrigés. Agent: par le professeur."),
                ("Marie a écrit cette lettre.", "Cette lettre a été écrite par Marie.", "Lettre → subject (f.sg.). Écrire PC → a été écrite. Feminine → écrite. Agent: par Marie."),
                ("On parle anglais dans ce bureau.", "L'anglais est parlé dans ce bureau.", "On = impersonal → omit agent. Anglais → subject (m.sg.). Parler → est parlé."),
                ("Les médecins respectent ce chirurgien.", "Ce chirurgien est respecté des médecins.", "Respecter (état/emotion) → can use de. Chirurgien (m.sg.) → respecté. Par or de both acceptable here; de preferred for respect."),
                ("L\'architecte construira le pont l\'année prochaine.", "Le pont sera construit par l'architecte l'année prochaine.", "Pont → subject (m.sg.). Construire (future) → sera construit. Agent: par l'architecte."),
            ]
        ),
        "ex3": (
            "Par or De? On or Passive?",
            "Choose the correct option.",
            [
                ("Le président est ___ de tous les citoyens. (admired)", ["admiré", "admired", "adorer", "admire"], "admiré", "Admirer is a state/emotion verb → de tous les citoyens. Le président est admiré de tous."),
                ("Ce livre a été écrit ___ un auteur célèbre.", ["de", "par", "avec", "à"], "par", "Active, specific agent doing an action → par. Écrit par un auteur."),
                ("___ parle espagnol dans ce quartier. (They speak Spanish here.)", ["On", "Il", "Elles", "Nous"], "On", "Impersonal subject to avoid passive in spoken French: on parle espagnol."),
                ("Les portes ___ fermées à 18h. (are closed daily)", ["ont été", "sont", "seront", "ont"], "sont", "Regular daily state: present passive: les portes sont fermées. No specific past event here."),
            ]
        ),
        "game_desc": "Master the French passive voice — formation, agreement, par vs de, and on alternative",
        "items": [
            ("passive-form", "être + participe (accordé)", "passive = être (any tense) + past participle agreeing with subject", "être + PP", "La lettre est écrite par Paul.", "passive: être (conjugated) + PP agreeing with subject", "est écrite"),
            ("passive-agree", "accord obligatoire", "past participle in passive ALWAYS agrees with the passive subject", "agreement", "Les lettres sont écrites. / Les livres sont écrits.", "PP agrees with passive subject in gender/number", "écrites"),
            ("passive-par", "par (agent actif)", "agent introduced by par for active, specific doers", "by (agent)", "Le film a été réalisé par Spielberg.", "agent = par + doer (specific action)", "par"),
            ("passive-de", "de (état/émotion)", "agent introduced by de for states, emotions, habitual relationships", "by (state)", "Elle est aimée de tous. (She is loved by all.)", "de used with: aimer, respecter, admirer, entourer…", "de"),
            ("passive-pc", "a été + PP", "passive passé composé: avoir + été + past participle (agreed)", "was done (PC)", "Le pont a été construit en 1902.", "passive PC: a/ont été + PP (agreed)", "a été construit"),
            ("passive-on", "on (alternative)", "on + active verb = informal/spoken alternative to the passive", "they / people", "On parle français ici. = Le français est parlé ici.", "on = avoids passive (informal/spoken)", "on parle"),
            ("passive-convert", "objet → sujet", "converting: active object becomes passive subject; verb → être + PP", "convert rule", "Elle écrit la lettre. → La lettre est écrite (par elle).", "active object → passive subject + être + PP", "est écrite"),
            ("passive-agreement-f", "accord féminin", "feminine passive subject: add -e to the past participle", "fem. agreement", "La porte est fermée. / Les portes sont fermées.", "feminine subject → -e on past participle in passive", "fermée"),
        ],
    },

    "relative-pronouns": {
        "level": "b1",
        "section": "grammar",
        "num": "G05",
        "short": "relative-pronouns",
        "title": "Relative Pronouns — Les Pronoms Relatifs",
        "subtitle": "Link clauses using qui, que, dont, où and lequel",
        "slides": [
            ("Qui and Que — Subject vs Object",
             "<b>Qui</b> replaces the subject of the relative clause. <b>Que</b> (qu' before vowel) replaces the direct object.",
             '<table class="sum-table"><thead><tr><th>Pronoun</th><th>Role</th><th>Example</th></tr></thead><tbody>'
             '<tr><td><b>qui</b></td><td>subject</td><td>Le prof <b>qui</b> parle vite. (The teacher who speaks fast.)</td></tr>'
             '<tr><td><b>que</b></td><td>direct object</td><td>Le film <b>que</b> j\'ai vu. (The film that I saw.)</td></tr>'
             '</tbody></table>'
             '<p><strong>Tip:</strong> If the noun is the one doing the action in the clause → <em>qui</em>. If it receives the action → <em>que</em>.</p>'),
            ("Dont — De + Noun",
             "<b>Dont</b> replaces <em>de + noun</em>. It is used with verbs and expressions that take <em>de</em>: parler de, avoir besoin de, se souvenir de, être fier de.",
             '<ul class="slide-list">'
             '<li>C\'est le livre <b>dont</b> je t\'ai parlé. (the book I told you about → parler de)</li>'
             '<li>Voilà l\'outil <b>dont</b> j\'ai besoin. (the tool I need → avoir besoin de)</li>'
             '<li>C\'est un événement <b>dont</b> je me souviens. (remember → se souvenir de)</li>'
             '<li><em>Dont</em> can also express possession: La femme <b>dont</b> le fils est médecin. (whose son is a doctor)</li></ul>'),
            ("Où — Place and Time",
             "<b>Où</b> replaces a place or a time expression. It can mean where, when, or in which.",
             '<table class="sum-table"><thead><tr><th>Usage</th><th>Example</th></tr></thead><tbody>'
             '<tr><td>Place</td><td>La ville <b>où</b> j\'habite. (The city where I live.)</td></tr>'
             '<tr><td>Time</td><td>Le jour <b>où</b> il est arrivé. (The day when he arrived.)</td></tr>'
             '<tr><td>Situation</td><td>À l\'époque <b>où</b> tout était différent. (At the time when everything was different.)</td></tr>'
             '</tbody></table>'),
            ("Lequel — After Prepositions",
             "<b>Lequel/laquelle/lesquels/lesquelles</b> is used after prepositions (other than de, which uses <em>dont</em>) to refer to things.",
             '<table class="sum-table"><thead><tr><th>Form</th><th>Use</th><th>Example</th></tr></thead><tbody>'
             '<tr><td>lequel</td><td>masc. sing.</td><td>Le stylo <b>avec lequel</b> j\'écris.</td></tr>'
             '<tr><td>laquelle</td><td>fem. sing.</td><td>La table <b>sur laquelle</b> il travaille.</td></tr>'
             '<tr><td>lesquels</td><td>masc. pl.</td><td>Les livres <b>parmi lesquels</b> j\'ai choisi.</td></tr>'
             '<tr><td>auquel</td><td>à + lequel</td><td>Le projet <b>auquel</b> je participe.</td></tr>'
             '</tbody></table>'),
        ],
        "traps": [
            ("Le film que j'ai vu il était bon.", "Le film que j'ai vu était bon.", "Don't repeat the noun/pronoun after que. The relative clause replaces it."),
            ("La personne qui j'aime.", "La personne que j'aime.", "Aimer takes a direct object → que, not qui. Qui is for subjects only."),
            ("Le sujet dont je parle de.", "Le sujet dont je parle.", "Dont already contains de — never add de again after dont."),
            ("La ville où j'habite là.", "La ville où j'habite.", "Où already expresses location — no need for là."),
        ],
        "summary": [
            ("qui", "subject of clause", "Le prof qui parle vite."),
            ("que / qu'", "direct object of clause", "Le film que j'ai vu."),
            ("dont", "replaces de + noun", "Le livre dont j'ai besoin."),
            ("dont", "possession (whose)", "La femme dont le fils est médecin."),
            ("où", "place or time", "La ville où j'habite. / Le jour où il est arrivé."),
            ("lequel / laquelle", "after preposition (thing)", "Le stylo avec lequel j'écris."),
            ("auquel / à laquelle", "à + lequel/laquelle", "Le projet auquel je participe."),
            ("duquel / de laquelle", "de + lequel (not people)", "Le mur au-dessus duquel il a sauté."),
        ],
        "ex1": (
            "Qui, Que or Dont?",
            "Choose the correct relative pronoun.",
            [
                ("C'est la femme ___ travaille à la mairie.", ["qui", "que", "dont", "où"], "qui", "She is doing the working → subject → qui."),
                ("Le film ___ nous avons regardé était super.", ["qui", "que", "dont", "où"], "que", "We watched it → direct object → que."),
                ("C'est le problème ___ je t'ai parlé.", ["qui", "que", "dont", "où"], "dont", "Parler de quelque chose → dont."),
                ("L'hôtel ___ nous avons séjourné était luxueux.", ["qui", "que", "dont", "où"], "où", "Place of staying → où."),
                ("Le document ___ j'ai besoin n'est pas là.", ["qui", "que", "dont", "où"], "dont", "Avoir besoin de → dont."),
                ("La fille ___ chante est ma cousine.", ["qui", "que", "dont", "où"], "qui", "She is singing → subject → qui."),
            ]
        ),
        "ex2": (
            "Complete with the Correct Relative Pronoun",
            "Fill in qui, que, dont, où, or the correct form of lequel.",
            [
                ("C'est l'ami ___ je fais confiance. (faire confiance à)", "auquel", "Faire confiance à → à + lequel → auquel."),
                ("La raison ___ il est parti reste mystérieuse.", "pour laquelle", "Pour + laquelle (feminine raison) after preposition pour."),
                ("C'est le quartier ___ j'ai grandi.", "où", "Place of growing up → où."),
                ("Le professeur ___ les étudiants admirent est brillant.", "que", "Students admire him → direct object → que."),
                ("Le projet ___ nous travaillons avance bien.", "sur lequel", "Travailler sur quelque chose → sur + lequel."),
            ]
        ),
        "ex3": (
            "Join the Sentences",
            "Choose the correctly joined sentence.",
            [
                ("J'ai un ami. Il parle six langues.", ["J'ai un ami que parle six langues.", "J'ai un ami qui parle six langues.", "J'ai un ami dont parle six langues.", "J'ai un ami où parle six langues."], "J'ai un ami qui parle six langues.", "He speaks languages → he is the subject → qui."),
                ("C'est le livre. J'en ai besoin. (avoir besoin de)", ["C'est le livre que j'ai besoin.", "C'est le livre qui j'ai besoin.", "C'est le livre dont j'ai besoin.", "C'est le livre où j'ai besoin."], "C'est le livre dont j'ai besoin.", "Avoir besoin de → dont replaces de + le livre."),
                ("Voilà le café. Nous nous sommes rencontrés là.", ["Voilà le café que nous nous sommes rencontrés.", "Voilà le café qui nous nous sommes rencontrés.", "Voilà le café dont nous nous sommes rencontrés.", "Voilà le café où nous nous sommes rencontrés."], "Voilà le café où nous nous sommes rencontrés.", "Place of meeting → où."),
                ("C'est un outil. Je me sers de cet outil.", ["C'est un outil que je me sers.", "C'est un outil dont je me sers.", "C'est un outil qui je me sers.", "C'est un outil où je me sers."], "C'est un outil dont je me sers.", "Se servir de → dont."),
                ("Le stylo est à moi. Tu écris avec ce stylo.", ["Le stylo que tu écris est à moi.", "Le stylo avec qui tu écris est à moi.", "Le stylo avec lequel tu écris est à moi.", "Le stylo dont tu écris est à moi."], "Le stylo avec lequel tu écris est à moi.", "Écrire avec + thing → avec lequel."),
            ]
        ),
        "game_desc": "Master French relative pronouns qui, que, dont, où and lequel",
        "items": [
            ("qui-subj", "qui", "subject relative pronoun — replaces the subject of the relative clause", "who / that (subj.)", "Le prof qui parle vite est mon préféré.", "qui = subject pronoun (doing the action in the clause)", "qui"),
            ("que-obj", "que / qu'", "object relative pronoun — replaces the direct object", "that / whom (obj.)", "Le film que j'ai vu était excellent.", "que = direct object (receiving the action)", "que"),
            ("dont-de", "dont", "replaces de + noun — used with verbs taking de", "of which / whose", "C'est le livre dont j'ai besoin.", "dont = de + noun (parler de, avoir besoin de, se souvenir de...)", "dont"),
            ("dont-poss", "dont (possession)", "dont expresses whose — replaces de + possessor", "whose", "La femme dont le fils est médecin.", "dont = whose (possession)", "dont"),
            ("ou-place", "où (place)", "replaces a place expression — where", "where", "La ville où j'habite est belle.", "où = place (where)", "où"),
            ("ou-time", "où (time)", "replaces a time expression — when/on which", "when (time)", "Le jour où il est arrivé était pluvieux.", "où = time (when)", "où"),
            ("lequel-prep", "lequel / laquelle", "replaces thing after a preposition (not de)", "which (after prep.)", "Le stylo avec lequel j'écris est rouge.", "lequel = thing after preposition (not de)", "lequel"),
            ("auquel", "auquel / à laquelle", "à + lequel/laquelle — for verbs taking à + thing", "to which", "Le projet auquel je participe est intéressant.", "auquel = à + lequel (verb + à + thing)", "auquel"),
        ],
    },

    "indirect-speech": {
        "level": "b1",
        "section": "grammar",
        "num": "G06",
        "short": "indirect-speech",
        "title": "Indirect Speech — Le Discours Indirect",
        "subtitle": "Report what someone said using tense shifts and adapted pronouns",
        "slides": [
            ("Reporting Statements — Que + Clause",
             "Statements are reported with <b>dire que</b>, <b>affirmer que</b>, <b>expliquer que</b>, etc. Pronouns and tense shift when the reporting verb is in the past.",
             '<table class="sum-table"><thead><tr><th>Direct</th><th>Indirect (past reporting verb)</th></tr></thead><tbody>'
             '<tr><td>«Je suis fatigué.»</td><td>Il a dit qu\'il <b>était</b> fatigué. (présent → imparfait)</td></tr>'
             '<tr><td>«J\'ai fini.»</td><td>Elle a dit qu\'elle <b>avait fini</b>. (PC → PQP)</td></tr>'
             '<tr><td>«Je partirai demain.»</td><td>Il a dit qu\'il <b>partirait</b> le lendemain. (futur → conditionnel)</td></tr>'
             '</tbody></table>'),
            ("Reporting Yes/No Questions — Si",
             "Yes/no questions become <b>si + clause</b> (word order returns to normal — no inversion).",
             '<ul class="slide-list">'
             '<li>«Tu viens?» → Elle a demandé <b>si</b> je venais.</li>'
             '<li>«Est-ce qu\'il a mangé?» → Il a demandé <b>si</b> elle avait mangé.</li>'
             '<li>Note: <em>si</em> becomes <em>s\'</em> before il/ils: Il a demandé <b>s\'</b>il était prêt.</li></ul>'),
            ("Reporting Wh-Questions",
             "Wh-questions keep their interrogative word but drop inversion.",
             '<table class="sum-table"><thead><tr><th>Direct question</th><th>Indirect (reported)</th></tr></thead><tbody>'
             '<tr><td>«Où habites-tu?»</td><td>Il a demandé <b>où</b> j\'habitais.</td></tr>'
             '<tr><td>«Quand est-il arrivé?»</td><td>Elle a voulu savoir <b>quand</b> il était arrivé.</td></tr>'
             '<tr><td>«Pourquoi tu pleures?»</td><td>Elle a demandé <b>pourquoi</b> je pleurais.</td></tr>'
             '<tr><td>«Qu\'est-ce que tu veux?»</td><td>Il a demandé <b>ce que</b> je voulais.</td></tr>'
             '</tbody></table>'),
            ("Reporting Commands — De + Infinitif",
             "Commands are reported with <b>de + infinitif</b>. Negation: de ne pas + infinitif.",
             '<ul class="slide-list">'
             '<li>«Ferme la porte!» → Elle m\'a dit <b>de fermer</b> la porte.</li>'
             '<li>«Ne pars pas!» → Il m\'a demandé <b>de ne pas partir</b>.</li>'
             '<li>«Soyez patients!» → Le prof nous a demandé <b>d\'être</b> patients.</li></ul>'),
            ("Time Expression Changes",
             "When reporting in the past, time words shift to remain logically consistent.",
             '<table class="sum-table"><thead><tr><th>Direct</th><th>Indirect</th></tr></thead><tbody>'
             '<tr><td>aujourd\'hui</td><td>ce jour-là</td></tr>'
             '<tr><td>hier</td><td>la veille</td></tr>'
             '<tr><td>demain</td><td>le lendemain</td></tr>'
             '<tr><td>maintenant</td><td>à ce moment-là</td></tr>'
             '<tr><td>ici</td><td>là</td></tr>'
             '</tbody></table>'),
        ],
        "traps": [
            ("Il a dit qu'il est fatigué. (present reporting verb → can keep présent)", "Il a dit qu'il était fatigué. (past reporting verb → imparfait)", "When the reporting verb is in the past, the tense of the reported clause must shift back."),
            ("Elle a demandé est-ce qu'il vient.", "Elle a demandé s'il venait.", "In indirect speech, no inversion and no est-ce que — use si + normal word order."),
            ("Il a demandé qu'est-ce que tu veux.", "Il a demandé ce que tu voulais.", "Qu'est-ce que → ce que in indirect speech. Drop the est-ce que structure."),
            ("Elle m'a dit fermer la porte.", "Elle m'a dit de fermer la porte.", "Commands in indirect speech need de + infinitif, not just the infinitive alone."),
        ],
        "summary": [
            ("statement", "dire que + clause", "Il a dit qu'il était fatigué."),
            ("présent → imparfait", "tense shift 1", "«Je viens.» → Il a dit qu'il venait."),
            ("PC → PQP", "tense shift 2", "«J'ai fini.» → Elle a dit qu'elle avait fini."),
            ("futur → conditionnel", "tense shift 3", "«Je partirai.» → Il a dit qu'il partirait."),
            ("yes/no question", "si + clause (no inversion)", "Il a demandé si elle venait."),
            ("wh-question", "interrogative word + clause", "Elle a demandé où j'habitais."),
            ("qu'est-ce que", "→ ce que", "Il a demandé ce que tu voulais."),
            ("command", "de + infinitif", "Elle m'a dit de fermer la porte."),
        ],
        "ex1": (
            "Choose the Correct Reported Form",
            "Select the correct indirect speech version.",
            [
                ("«Je suis content.» → Il a dit...", ["qu'il est content.", "qu'il était content.", "qu'il soit content.", "qu'il sera content."], "qu'il était content.", "Statement in past → présent shifts to imparfait: est → était."),
                ("«Est-ce que tu viens?» → Elle a demandé...", ["si je viens.", "si je venais.", "si je sois venu.", "si je viendrais."], "si je venais.", "Yes/no question with past reporting verb → si + imparfait."),
                ("«Viens ici!» → Il m'a dit...", ["de venir ici.", "de venir là.", "venir là.", "que je viens là."], "de venir là.", "Command → de + infinitif. Ici → là in indirect speech."),
                ("«Qu'est-ce que tu veux?» → Elle a voulu savoir...", ["qu'est-ce que je voulais.", "ce que je voulais.", "ce que je veux.", "que je voulais."], "ce que je voulais.", "Qu'est-ce que → ce que + imparfait in indirect past."),
                ("«J'ai fini mon travail.» → Elle a dit...", ["qu'elle a fini son travail.", "qu'elle avait fini son travail.", "qu'elle finissait son travail.", "qu'elle finirait son travail."], "qu'elle avait fini son travail.", "PC in direct → PQP in indirect (past reporting verb)."),
            ]
        ),
        "ex2": (
            "Rewrite in Indirect Speech",
            "Convert each direct quotation into indirect speech with a past reporting verb.",
            [
                ("«Je pars demain.» Il a dit que...", "il partait le lendemain.", "Partir (présent) → partait (imparfait). Demain → le lendemain."),
                ("«Est-ce qu'elle a téléphoné?» Il a demandé...", "si elle avait téléphoné.", "Yes/no → si. PC → PQP: a téléphoné → avait téléphoné."),
                ("«Où habitez-vous?» Elle a demandé...", "où ils habitaient.", "Wh-question: où stays. Inversion dropped. Présent → imparfait."),
                ("«Ne touche pas ça!» Elle m'a dit...", "de ne pas toucher ça.", "Command → de ne pas + infinitif."),
                ("«Je reviendrai.» Il a promis...", "qu'il reviendrait.", "Futur → conditionnel présent in indirect past."),
            ]
        ),
        "ex3": (
            "Direct or Indirect?",
            "Identify the correctly formed sentence.",
            [
                ("Reporting: «Je suis là.» (past)", ["Il a dit qu'il est là.", "Il a dit qu'il était là.", "Il a dit qu'il soit là.", "Il a dit qu'il sera là."], "Il a dit qu'il était là.", "Past reporting verb → présent shifts to imparfait."),
                ("Reporting: «Viens!» (past)", ["Elle m'a dit venir.", "Elle m'a dit que je vienne.", "Elle m'a dit de venir.", "Elle m'a dit si je viens."], "Elle m'a dit de venir.", "Command → de + infinitif."),
                ("Time word: «Je pars aujourd'hui.» (reported)", ["qu'il partait aujourd'hui.", "qu'il partait ce jour-là.", "qu'il partait hier.", "qu'il partait maintenant."], "qu'il partait ce jour-là.", "Aujourd'hui → ce jour-là in past indirect speech."),
                ("Reporting yes/no: «Est-ce qu'il dort?»", ["Elle a demandé est-ce qu'il dort.", "Elle a demandé s'il dormait.", "Elle a demandé qu'il dorme.", "Elle a demandé si il dort."], "Elle a demandé s'il dormait.", "Yes/no: si + clause (no inversion). Si il → s'il. Présent → imparfait."),
                ("Reporting wh: «Qu'est-ce que tu fais?»", ["Il a demandé qu'est-ce que tu faisais.", "Il a demandé ce que je faisais.", "Il a demandé ce que tu fais.", "Il a demandé si tu faisais."], "Il a demandé ce que je faisais.", "Qu'est-ce que → ce que. Pronoun tu → je (perspective shift). Imparfait."),
            ]
        ),
        "game_desc": "Master French indirect speech — tense shifts, si clauses, and command forms",
        "items": [
            ("dire-que", "dire que + clause", "reporting statements: dire/affirmer/expliquer + que + reported clause", "that (statements)", "Il a dit qu'il était fatigué.", "dire que = reporting a statement", "que"),
            ("pres-imp", "présent → imparfait", "tense shift 1: direct présent becomes imparfait in past indirect speech", "shift 1", "«Je viens.» → Il a dit qu'il venait.", "présent shifts to ___ in past indirect speech", "imparfait"),
            ("pc-pqp", "PC → plus-que-parfait", "tense shift 2: direct PC becomes PQP in past indirect speech", "shift 2", "«J'ai fini.» → Elle a dit qu'elle avait fini.", "PC shifts to ___ in past indirect speech", "plus-que-parfait"),
            ("fut-cond", "futur → conditionnel", "tense shift 3: direct future becomes conditionnel in past indirect speech", "shift 3", "«Je partirai.» → Il a dit qu'il partirait.", "futur shifts to ___ in past indirect speech", "conditionnel"),
            ("si-yon", "si + clause", "yes/no questions become si + clause (no inversion, no est-ce que)", "if / whether", "Il a demandé si elle venait.", "yes/no question → ___ + clause (no inversion)", "si"),
            ("ce-que", "ce que", "qu'est-ce que becomes ce que in indirect speech", "what (object)", "Il a demandé ce que je voulais.", "qu'est-ce que → ___ in indirect speech", "ce que"),
            ("cmd-de", "de + infinitif", "commands become de + infinitif in indirect speech", "to do (command)", "Elle m'a dit de fermer la porte.", "command → de + ___ in indirect speech", "infinitif"),
            ("demain-lend", "demain → le lendemain", "time word shift: demain (tomorrow) → le lendemain (the next day)", "time shift", "«Je pars demain.» → Il a dit qu'il partait le lendemain.", "demain → ___ in past indirect speech", "le lendemain"),
        ],
    },

    "causative-faire": {
        "level": "b1",
        "section": "grammar",
        "num": "G07",
        "short": "causative-faire",
        "title": "Causative Faire — Faire + Infinitif",
        "subtitle": "Express having something done or making someone do something with faire + infinitif",
        "slides": [
            ("What is the Causative?",
             "The causative construction uses <b>faire + infinitif</b> to mean <em>have something done</em> or <em>make someone do something</em>. The subject causes the action but doesn't do it themselves.",
             '<ul class="slide-list">'
             '<li>Je <b>fais réparer</b> ma voiture. (I\'m having my car repaired.) — someone else repairs it</li>'
             '<li>Le prof <b>fait travailler</b> les étudiants. (The teacher makes the students work.)</li>'
             '<li>Elle <b>fait construire</b> une maison. (She\'s having a house built.)</li>'
             '<li>Compare: Je répare ma voiture. (I repair it myself.)</li></ul>'),
            ("Two Objects: Direct and Indirect",
             "When the causative has only one object (the thing done), use a direct object. When there are two objects (the thing AND the person doing it), the person takes an indirect object (à or par).",
             '<table class="sum-table"><thead><tr><th>Pattern</th><th>Example</th></tr></thead><tbody>'
             '<tr><td>faire + inf + [thing] (1 object)</td><td>Il fait <b>laver la voiture</b>. (He has the car washed.)</td></tr>'
             '<tr><td>faire + inf + [thing] + par [person]</td><td>Il fait laver la voiture <b>par le mécanicien</b>.</td></tr>'
             '<tr><td>faire + inf + [person] (no thing)</td><td>Elle fait <b>travailler les élèves</b>. (She makes the pupils work.)</td></tr>'
             '</tbody></table>'),
            ("Se faire + Infinitif",
             "<b>Se faire + infinitif</b> means to have something done to oneself — the subject is both the causer and the recipient.",
             '<ul class="slide-list">'
             '<li>Je <b>me suis fait couper</b> les cheveux. (I had my hair cut.) — at the hairdresser</li>'
             '<li>Elle <b>s\'est fait voler</b> son sac. (She had her bag stolen.) — it happened to her</li>'
             '<li>Il <b>se fait aider</b> par ses collègues. (He gets help from his colleagues.)</li>'
             '<li>Note: In PC, se faire never varies for agreement (it is always se fait...).</li></ul>'),
            ("Pronoun Placement in Causative",
             "Object pronouns go BEFORE <em>faire</em>, not before the infinitive.",
             '<table class="sum-table"><thead><tr><th>Full form</th><th>With pronoun</th></tr></thead><tbody>'
             '<tr><td>Je fais réparer la voiture.</td><td>Je <b>la</b> fais réparer.</td></tr>'
             '<tr><td>Elle fait travailler les élèves.</td><td>Elle <b>les</b> fait travailler.</td></tr>'
             '<tr><td>Il a fait construire une maison.</td><td>Il <b>en</b> a fait construire une.</td></tr>'
             '</tbody></table>'),
        ],
        "traps": [
            ("Je fais réparer à mon ami la voiture.", "Je fais réparer la voiture par mon ami.", "When the causee (person doing it) is introduced, use par — not à — when there is also a direct object."),
            ("Je me suis faite couper les cheveux. (f.)", "Je me suis fait couper les cheveux.", "Se faire is invariable in the passé composé — no agreement with the subject."),
            ("Je fais réparer la à mon mécanicien.", "Je la fais réparer par mon mécanicien.", "Pronoun goes before faire, not before the infinitive."),
            ("Laisser vs faire — même sens", "Laisser = allow/let; faire = make/have (stronger)", "Laisser + inf = let (permission). Faire + inf = make/have (cause). Elle laisse les enfants jouer. ≠ Elle fait travailler les enfants."),
        ],
        "summary": [
            ("faire + inf", "have sth done / make sb do", "Je fais réparer ma voiture."),
            ("faire + inf + par [person]", "have done by someone", "Il fait laver la voiture par le mécanicien."),
            ("faire + inf + [person]", "make someone do", "Elle fait travailler les étudiants."),
            ("se faire + inf", "have sth done to oneself", "Je me suis fait couper les cheveux."),
            ("pronoun placement", "before faire, not infinitive", "Je la fais réparer."),
            ("se faire (PC)", "invariable — no agreement", "Elle s'est fait voler son sac."),
            ("laisser vs faire", "let vs make/have", "Elle laisse les élèves sortir. / Elle fait travailler les élèves."),
            ("faire faire", "have done (general)", "Il fait faire les courses par sa femme."),
        ],
        "ex1": (
            "Causative or Not?",
            "Choose the sentence that correctly uses the causative.",
            [
                ("Having your car repaired (by a mechanic)", ["Je répare ma voiture.", "Je fais réparer ma voiture.", "Je me répare la voiture.", "Ma voiture se répare."], "Je fais réparer ma voiture.", "Faire + inf = have it done (by someone else). Je répare = I do it myself."),
                ("Making the students work", ["Elle travaille les étudiants.", "Elle fait travailler les étudiants.", "Elle fait les étudiants travailler.", "Elle laisse travailler les étudiants."], "Elle fait travailler les étudiants.", "Faire + inf directly. Object after infinitive: faire travailler [les étudiants]."),
                ("She had her bag stolen", ["Elle a volé son sac.", "Elle a fait voler son sac.", "Elle s'est fait voler son sac.", "Elle se fait voler son sac."], "Elle s'est fait voler son sac.", "Se faire + inf = have something done to oneself (happened to her)."),
                ("I'm having a house built by an architect", ["Je construis une maison par un architecte.", "Je fais construire une maison par un architecte.", "Je fais un architecte construire une maison.", "Je me fais construire une maison."], "Je fais construire une maison par un architecte.", "Faire + inf + thing + par + person."),
                ("He lets the children play", ["Il fait jouer les enfants.", "Il laisse les enfants jouer.", "Il fait les enfants jouer.", "Il se laisse les enfants jouer."], "Il laisse les enfants jouer.", "Laisser = let/allow. Faire = make/have. Permission → laisser."),
            ]
        ),
        "ex2": (
            "Pronoun Replacement",
            "Replace the object with the correct pronoun.",
            [
                ("Je fais réparer la voiture. → Je ___ fais réparer.", "la", "La voiture (f. sing.) → la. Pronoun before faire."),
                ("Elle fait travailler les élèves. → Elle ___ fait travailler.", "les", "Les élèves (pl.) → les. Before faire."),
                ("Il a fait construire cette maison. → Il ___ a fait construire.", "la", "Cette maison (f.) → la. Before fait."),
                ("Je me suis fait couper les cheveux. → Je me les ___ fait couper.", "suis", "Me les suis fait couper — pronoun stays before faire (past: suis fait)."),
                ("Nous faisons laver la voiture par le mécanicien. → Nous ___ faisons laver par le mécanicien.", "la", "La voiture → la. Before faisons."),
            ]
        ),
        "ex3": (
            "Translate Using the Causative",
            "Choose the correct French causative sentence.",
            [
                ("I had my hair cut.", ["J'ai coupé mes cheveux.", "Je me suis fait couper les cheveux.", "Je me suis faite couper les cheveux.", "J'ai fait couper mes cheveux moi."], "Je me suis fait couper les cheveux.", "Se faire + inf (no agreement in PC). Les cheveux, not mes cheveux with se faire."),
                ("She makes her students write every day.", ["Elle écrit ses étudiants tous les jours.", "Elle laisse ses étudiants écrire tous les jours.", "Elle fait écrire ses étudiants tous les jours.", "Elle fait ses étudiants écrire tous les jours."], "Elle fait écrire ses étudiants tous les jours.", "Faire + inf + object (person). Object after the infinitive."),
                ("He's having his house painted by a professional.", ["Il peint sa maison par un professionnel.", "Il fait peindre sa maison par un professionnel.", "Il fait peindre par un professionnel sa maison.", "Il se fait peindre sa maison."], "Il fait peindre sa maison par un professionnel.", "Faire + inf + thing + par + person."),
                ("I'll have the report sent tonight.", ["Je vais envoyer le rapport ce soir.", "Je vais me faire envoyer le rapport ce soir.", "Je vais faire envoyer le rapport ce soir.", "Je vais faire le rapport envoyer ce soir."], "Je vais faire envoyer le rapport ce soir.", "Aller + faire + inf + object. Object after infinitive."),
                ("They had their car repaired.", ["Ils ont réparé leur voiture.", "Ils se sont fait réparer leur voiture.", "Ils ont fait réparer leur voiture.", "Ils ont fait leur voiture réparer."], "Ils ont fait réparer leur voiture.", "Faire (PC: ont fait) + inf + object (la voiture). No se faire here — they commissioned the repair."),
            ]
        ),
        "game_desc": "Master the French causative construction faire + infinitif",
        "items": [
            ("faire-inf", "faire + infinitif", "causative: have something done / make someone do something", "have done", "Je fais réparer ma voiture. (I'm having my car repaired.)", "causative: faire + ___ = have done", "infinitif"),
            ("faire-par", "faire + inf + par", "have done by: introduce the agent with par when there is also a direct object", "by (agent)", "Il fait laver la voiture par le mécanicien.", "faire + inf + [thing] + par + [person who does it]", "par"),
            ("se-faire", "se faire + inf", "have something done to oneself — subject is recipient", "have done to self", "Je me suis fait couper les cheveux.", "se faire + inf = have ___ done to oneself", "se faire"),
            ("se-faire-inv", "se faire (invariable)", "se faire is invariable in the PC — no agreement with subject", "no agreement", "Elle s'est fait voler son sac. (not volée)", "se faire PC: always ___ (no gender/number agreement)", "invariable"),
            ("pron-before", "pronom avant faire", "object pronouns go BEFORE faire, not before the infinitive", "pronoun placement", "Je la fais réparer. (not Je fais la réparer.)", "pronoun goes ___ faire (not before infinitive)", "avant"),
            ("laisser", "laisser + inf", "let/allow someone to do — permission (contrast: faire = make/cause)", "let / allow", "Elle laisse les enfants jouer dehors.", "laisser + inf = ___ someone do (permission)", "laisser"),
            ("obj-after", "objet après l'infinitif", "in causative, the object comes after the infinitive (unlike regular verbs)", "object after inf.", "Elle fait travailler les étudiants. (not Elle fait les étudiants travailler.)", "causative: object comes ___ the infinitive", "après"),
            ("faire-faire", "faire faire", "have something done (general): double faire structure is perfectly correct", "have done", "Il fait faire les courses. (He has the shopping done.)", "faire + ___ + [task] = have the task done", "faire"),
        ],
    },

    "gerondif": {
        "level": "b1",
        "section": "grammar",
        "num": "G08",
        "short": "gerondif",
        "title": "The Gerundive — En + Participe Présent",
        "subtitle": "Express simultaneous actions, manner, and conditions with en + -ant",
        "slides": [
            ("Formation",
             "The gerundive is formed with <b>en</b> + the <b>present participle</b>. The present participle is formed from the <em>nous</em> form of the present tense: drop <em>-ons</em>, add <em>-ant</em>.",
             '<table class="sum-table"><thead><tr><th>Verb</th><th>Nous form</th><th>Participe</th><th>Gérondif</th></tr></thead><tbody>'
             '<tr><td>parler</td><td>parlons</td><td>parlant</td><td>en parlant</td></tr>'
             '<tr><td>finir</td><td>finissons</td><td>finissant</td><td>en finissant</td></tr>'
             '<tr><td>faire</td><td>faisons</td><td>faisant</td><td>en faisant</td></tr>'
             '<tr><td>avoir</td><td>avons</td><td>ayant</td><td>en ayant</td></tr>'
             '<tr><td>être</td><td>sommes</td><td>étant</td><td>en étant</td></tr>'
             '</tbody></table>'),
            ("Uses: Simultaneous Action and Manner",
             "The gerundive most commonly expresses two actions happening at the same time by the SAME subject, or the manner in which something is done.",
             '<ul class="slide-list">'
             '<li><b>Simultaneous:</b> Il chante <b>en travaillant</b>. (He sings while working.)</li>'
             '<li><b>Manner:</b> Elle a répondu <b>en souriant</b>. (She answered smiling / with a smile.)</li>'
             '<li><b>Manner:</b> J\'ai appris le français <b>en regardant</b> des films. (by watching films)</li>'
             '<li>Key rule: the subject of the gerundive MUST be the same as the main clause subject.</li></ul>'),
            ("Uses: Condition and Concession",
             "The gerundive can also express a condition (if/by doing) or concession with <b>tout en</b> (even though / while at the same time).",
             '<ul class="slide-list">'
             '<li><b>Condition:</b> <b>En travaillant</b> dur, tu réussiras. (By working hard, you will succeed.)</li>'
             '<li><b>Condition:</b> <b>En partant</b> tôt, nous éviterons les embouteillages.</li>'
             '<li><b>Concession (tout en):</b> <b>Tout en comprenant</b> ton point de vue, je ne suis pas d\'accord. (While understanding your POV, I disagree.)</li>'
             '<li><em>Tout en</em> emphasises a contrast or paradox between the two actions.</li></ul>'),
        ],
        "traps": [
            ("En mangeant, il a regardé la télé et son chien a aboyé.", "En mangeant, il a regardé la télé. (same subject)", "The subject of the gérondif MUST match the main clause subject. His dog is a different subject."),
            ("Il a répondu souriant. (missing en)", "Il a répondu en souriant.", "The gerundive always requires en before the present participle."),
            ("En ayant travaillé dur... (past participle)", "En travaillant dur...", "The gérondif uses the present participle (-ant), not the past participle. There is no passé gérondif in standard B1 usage."),
            ("Etant = being (invariable)", "étant (no agreement)", "The present participle used in a gérondif is invariable — no gender/number agreement."),
        ],
        "summary": [
            ("formation", "nous form − ons + ant", "parlons → parlant → en parlant"),
            ("irregular", "être / avoir / savoir", "étant / ayant / sachant"),
            ("simultaneous", "while doing", "Il travaille en écoutant de la musique."),
            ("manner", "by doing / how", "J'ai appris en pratiquant."),
            ("condition", "by doing (if)", "En partant tôt, tu éviteras les bouchons."),
            ("tout en", "even though / while", "Tout en comprenant, je ne suis pas d'accord."),
            ("same subject rule", "subject must match main clause", "En arrivant, il a vu Marie. (il = he for both)"),
            ("invariable", "no gender/number agreement", "Elle a répondu en souriant. (not souriante)"),
        ],
        "ex1": (
            "Form the Gérondif",
            "Choose the correct gérondif form.",
            [
                ("travailler → en ___", ["en travaillant", "en travaillé", "en travailler", "en travaillant-s"], "en travaillant", "Nous travaillons → travaillant → en travaillant."),
                ("faire → en ___", ["en faisant", "en faisisant", "en faisant-s", "en faire"], "en faisant", "Nous faisons → faisant → en faisant (irregular nous form)."),
                ("être → en ___", ["en étant", "en êtreant", "en sommeant", "en être"], "en étant", "Être is irregular: étant (not sommeant). En étant."),
                ("savoir → en ___", ["en savant", "en sachant", "en savoirant", "en savons"], "en sachant", "Savoir is irregular: sachant → en sachant."),
                ("finir → en ___", ["en finant", "en finissant", "en finissont", "en finir"], "en finissant", "Nous finissons → finissant → en finissant."),
            ]
        ),
        "ex2": (
            "Translate Using the Gérondif",
            "Express in French using en + participe présent.",
            [
                ("She learned Spanish by watching TV.", "Elle a appris l'espagnol en regardant la télé.", "En regardant = by watching. Both actions: she (same subject)."),
                ("He arrived singing.", "Il est arrivé en chantant.", "En chantant = while/while singing. Same subject: il."),
                ("By working hard, you will succeed.", "En travaillant dur, tu réussiras.", "Gérondif at start = condition. En travaillant = by working."),
                ("While understanding the issue, I disagree.", "Tout en comprenant le problème, je ne suis pas d'accord.", "Tout en + gérondif = concession (even though)."),
                ("She answered smiling.", "Elle a répondu en souriant.", "En souriant = smiling / with a smile. Manner."),
            ]
        ),
        "ex3": (
            "Identify the Correct Sentence",
            "Choose the sentence with the correct use of the gérondif.",
            [
                ("He reads while listening to music.", ["En écoutant de la musique, le livre tombe.", "Il lit en écoutant de la musique.", "En écoutant, son livre tombe.", "Il lit et son livre en écoutant."], "Il lit en écoutant de la musique.", "Same subject (il) for both: il lit / il écoute. Correct."),
                ("By leaving early, we'll avoid traffic.", ["En partant tôt, nous éviterons les embouteillages.", "En partant tôt, les embouteillages seront évités.", "Tout en partant tôt, les embouteillages.", "Nous partons tôt en embouteillages."], "En partant tôt, nous éviterons les embouteillages.", "Condition: en + gérondif. Same subject: nous."),
                ("She answered without smiling.", ["Elle a répondu sans sourire.", "Elle a répondu en ne souriant pas.", "Elle a répondu sans en souriant.", "Elle a répondu en souriant pas."], "Elle a répondu sans sourire.", "Negation with gérondif: sans + infinitif (not en ne...pas in B1 contexts). Both are grammatical but sans + inf is the clean B1 form."),
                ("While agreeing, he said nothing.", ["Tout en agréant, il n'a rien dit.", "En agréant, il n'a rien dit.", "Tout en acceptant, il n'a rien dit.", "En acceptant, il rien dit."], "Tout en acceptant, il n'a rien dit.", "Concession/paradox → tout en + gérondif. Accepter (to agree/accept) → acceptant."),
                ("He learned by making mistakes.", ["Il a appris en fait des erreurs.", "Il a appris en faisant des erreurs.", "Il a appris faisant des erreurs.", "Il a appris en fait erreurs."], "Il a appris en faisant des erreurs.", "En faisant = by making. Faire → faisant."),
            ]
        ),
        "game_desc": "Master the French gérondif — en + participe présent for simultaneous actions and manner",
        "items": [
            ("gerondif-form", "en + -ant", "gérondif = en + present participle (nous form minus -ons + ant)", "while / by doing", "Il travaille en écoutant de la musique.", "gérondif = en + present participle (___ + ant)", "-ant"),
            ("simultaneous", "en + -ant (simultaneous)", "two actions at the same time by the same subject", "while doing", "Elle écoute la radio en conduisant.", "simultaneous action: ___ + gérondif = while doing", "en"),
            ("manner", "en + -ant (manner)", "how something is done — by doing / doing", "by doing", "J'ai appris le français en regardant des films.", "manner: en + gérondif = ___ doing", "by"),
            ("condition", "en + -ant (condition)", "by doing X, Y will happen — if/by doing", "if / by doing", "En partant tôt, tu éviteras les bouchons.", "condition: en + gérondif → by ___ this, that happens", "doing"),
            ("tout-en", "tout en + -ant", "concession/paradox — even though / while at the same time", "even though", "Tout en comprenant, je ne suis pas d'accord.", "tout en + gérondif = ___ though doing", "even"),
            ("same-subject", "même sujet obligatoire", "the subject of the gérondif MUST match the main clause subject", "same subject", "En arrivant, il a vu Marie. (il does both)", "gérondif rule: ___ subject as main verb required", "same"),
            ("invariable", "invariable (pas d'accord)", "the present participle in a gérondif does not agree in gender/number", "no agreement", "Elle a répondu en souriant. (not souriante)", "gérondif is ___ (no gender/number change)", "invariable"),
            ("etre-avoir-irr", "étant / ayant / sachant", "irregular present participles: être → étant, avoir → ayant, savoir → sachant", "irregular", "En étant patient, on réussit.", "être → ___, avoir → ayant, savoir → sachant", "étant"),
        ],
    },

    "si-clauses": {
        "level": "b1",
        "section": "grammar",
        "num": "G09",
        "short": "si-clauses",
        "title": "Si Clauses — Phrases Conditionnelles",
        "subtitle": "Express real, hypothetical, and impossible conditions with the three si-clause patterns",
        "slides": [
            ("Type 1 — Real / Possible Condition",
             "<b>Si + présent → présent / futur / impératif</b>. Used for conditions that are real or likely.",
             '<table class="sum-table"><thead><tr><th>Si clause (condition)</th><th>Main clause (result)</th></tr></thead><tbody>'
             '<tr><td>Si tu travailles,</td><td>tu réussiras. (If you work, you will succeed.)</td></tr>'
             '<tr><td>Si elle a faim,</td><td>elle mange quelque chose. (If she\'s hungry, she eats.)</td></tr>'
             '<tr><td>Si vous avez des questions,</td><td>posez-les! (If you have questions, ask them!)</td></tr>'
             '</tbody></table>'
             '<p>Rule: Never use futur or conditionnel after <em>si</em>.</p>'),
            ("Type 2 — Hypothetical / Unlikely Condition",
             "<b>Si + imparfait → conditionnel présent</b>. Used for hypothetical or unlikely situations (often translations of 'would').",
             '<table class="sum-table"><thead><tr><th>Si clause (imparfait)</th><th>Main clause (conditionnel)</th></tr></thead><tbody>'
             '<tr><td>Si j\'avais de l\'argent,</td><td>j\'achèterais une voiture. (If I had money, I would buy a car.)</td></tr>'
             '<tr><td>Si elle venait,</td><td>ce serait super. (If she came, it would be great.)</td></tr>'
             '<tr><td>Si tu travaillais plus,</td><td>tu réussirais. (If you worked more, you would succeed.)</td></tr>'
             '</tbody></table>'),
            ("Type 3 — Impossible / Past Regret",
             "<b>Si + plus-que-parfait → conditionnel passé</b>. Refers to the past — what would have happened if things had been different.",
             '<table class="sum-table"><thead><tr><th>Si clause (PQP)</th><th>Main clause (cond. passé)</th></tr></thead><tbody>'
             '<tr><td>Si j\'avais travaillé,</td><td>j\'aurais réussi. (If I had worked, I would have succeeded.)</td></tr>'
             '<tr><td>Si elle était venue,</td><td>ça aurait été super.</td></tr>'
             '<tr><td>Si tu n\'avais pas menti,</td><td>tout aurait été différent.</td></tr>'
             '</tbody></table>'),
            ("The Golden Rule — Never Futur/Conditionnel After Si",
             "In ALL three types, the <em>si</em> clause NEVER contains a future or conditional tense. This is one of the most common errors in French.",
             '<ul class="slide-list">'
             '<li>WRONG: Si tu <em>viendras</em> (futur after si) ✗</li>'
             '<li>WRONG: Si tu <em>viendrais</em> (conditionnel after si) ✗</li>'
             '<li>RIGHT (Type 1): Si tu viens, je serai content. ✓</li>'
             '<li>RIGHT (Type 2): Si tu venais, je serais content. ✓</li>'
             '<li>RIGHT (Type 3): Si tu étais venu, j\'aurais été content. ✓</li>'
             '<li>The result clause takes futur/conditionnel — not the si clause.</li></ul>'),
        ],
        "traps": [
            ("Si tu viendras / Si tu viendrais...", "Si tu viens / Si tu venais...", "NEVER futur or conditionnel after si. Type 1: si + présent. Type 2: si + imparfait."),
            ("Si j'aurais su... (conditionnel passé after si)", "Si j'avais su...", "NEVER conditionnel passé after si. Type 3 uses si + plus-que-parfait."),
            ("If I was rich (English was → imparfait in French)", "Si j'étais riche, j'achèterais...", "English 'if I was' = hypothetical → French si + imparfait → conditionnel présent (Type 2)."),
            ("Inverting the clauses", "Both orders are correct", "The result clause can come first: J'achèterais une voiture si j'avais de l'argent. The tenses are the same either way."),
        ],
        "summary": [
            ("Type 1 (real)", "si + présent → futur/présent/impératif", "Si tu travailles, tu réussiras."),
            ("Type 2 (hypothetical)", "si + imparfait → conditionnel présent", "Si j'avais de l'argent, j'achèterais une voiture."),
            ("Type 3 (past regret)", "si + PQP → conditionnel passé", "Si j'avais étudié, j'aurais réussi."),
            ("golden rule", "never futur/conditionnel after si", "Si tu viendras ✗ → Si tu viens ✓"),
            ("result clause position", "can be first or second", "J'achèterais X si j'avais Y. / Si j'avais Y, j'achèterais X."),
            ("Type 2 signal word", "'would' in English result clause", "'I would' = conditionnel présent in result"),
            ("Type 3 signal word", "'would have' in English result", "'I would have' = conditionnel passé in result"),
            ("mixed types", "Type 2 + Type 3 possible", "Si tu avais étudié, tu réussirais maintenant."),
        ],
        "ex1": (
            "Which Type of Si Clause?",
            "Identify the type and choose the correct tense in the main clause.",
            [
                ("Si tu viens demain, je ___ content. (real — tomorrow)", ["suis", "serais", "serai", "sois"], "serai", "Type 1 (real/possible): si + présent → futur. Je serai content."),
                ("Si j'avais plus de temps, je ___ davantage. (hypothetical)", ["lis", "lirais", "lirai", "aie lu"], "lirais", "Type 2 (hypothetical): si + imparfait → conditionnel présent. Je lirais."),
                ("Si tu m'avais appelé, je ___ venu. (past impossible)", ["suis", "serais", "serai", "serais"], "serais", "Type 3: si + PQP → conditionnel passé. Je serais venu."),
                ("Si elle est fatiguée, elle ___ se reposer. (general truth)", ["devra", "devrait", "devra", "doit"], "doit", "Type 1 (general/factual): si + présent → présent. Elle doit se reposer."),
                ("Si vous ___ plus tôt, vous n'auriez pas raté le train. (past regret)", ["êtes partis", "partiez", "étiez partis", "partirez"], "étiez partis", "Type 3: si + PQP (être verbe → étiez partis). Result: conditionnel passé."),
            ]
        ),
        "ex2": (
            "Complete the Si Clause",
            "Fill in the correct tense.",
            [
                ("Si je ___ (avoir) plus d'argent, j'achèterais une maison.", "avais", "Type 2: si + imparfait. Avoir → avais."),
                ("Si tu ___ (étudier) hier soir, tu aurais réussi.", "avais étudié", "Type 3: si + PQP. Avoir + étudié = avais étudié."),
                ("Si elle ___ (venir) à la fête, ce sera super.", "vient", "Type 1: si + présent. Venir → vient."),
                ("Si nous ___ (partir) plus tôt, on éviterait les embouteillages.", "partions", "Type 2: si + imparfait. Partir → partions."),
                ("Si tu m'___ (appeler), j'aurais su.", "avais appelé", "Type 3: si + PQP. Avoir + appelé = avais appelé."),
            ]
        ),
        "ex3": (
            "Spot the Error",
            "Choose the correctly formed conditional sentence.",
            [
                ("Type 1 — real condition", ["Si tu viendras, ce sera bien.", "Si tu viens, ce sera bien.", "Si tu viendrais, ce sera bien.", "Si tu venais, ce sera bien."], "Si tu viens, ce sera bien.", "Type 1: si + présent → futur. Never futur after si."),
                ("Type 2 — hypothetical", ["Si j'aurais de l'argent, j'achèterais.", "Si j'avais de l'argent, j'achèterai.", "Si j'avais de l'argent, j'achèterais.", "Si j'aille avoir de l'argent, j'achèterais."], "Si j'avais de l'argent, j'achèterais.", "Type 2: si + imparfait → conditionnel présent. Avais (not aurais or aurai)."),
                ("Type 3 — past regret", ["Si tu étais venu, j'aurai été content.", "Si tu venais, j'aurais été content.", "Si tu étais venu, j'aurais été content.", "Si tu seras venu, j'aurais été content."], "Si tu étais venu, j'aurais été content.", "Type 3: si + PQP → conditionnel passé. Étais venu → j'aurais été content."),
                ("Result clause first", ["Je viendrais si tu me demanderas.", "Je viendrais si tu me demanderais.", "Je viendrais si tu me demandes.", "Je viendrais si tu me demandais."], "Je viendrais si tu me demandais.", "Type 2 result clause first. Si + imparfait (demandais) → conditionnel (viendrais)."),
                ("General truth", ["Si l'eau gèlerait à 0°C, elle devient de la glace.", "Si l'eau gèle à 0°C, elle devient de la glace.", "Si l'eau gelait à 0°C, elle devient de la glace.", "Si l'eau gèle à 0°C, elle devenait de la glace."], "Si l'eau gèle à 0°C, elle devient de la glace.", "General/scientific truth: si + présent → présent."),
            ]
        ),
        "game_desc": "Master the three French si-clause types — real, hypothetical, and past regret",
        "items": [
            ("type1", "si + présent → futur", "Type 1: real/possible condition — present in si clause, future in result", "real condition", "Si tu viens, je serai content.", "Type 1: si + ___ → futur/présent (real condition)", "présent"),
            ("type2", "si + imparfait → conditionnel", "Type 2: hypothetical — imparfait in si clause, conditionnel présent in result", "hypothetical", "Si j'avais de l'argent, j'achèterais une voiture.", "Type 2: si + ___ → conditionnel présent (hypothetical)", "imparfait"),
            ("type3", "si + PQP → cond. passé", "Type 3: past impossible — plus-que-parfait in si clause, conditionnel passé in result", "past regret", "Si j'avais étudié, j'aurais réussi.", "Type 3: si + ___ → conditionnel passé (past regret)", "plus-que-parfait"),
            ("golden-rule", "jamais futur/cond. après si", "NEVER futur or conditionnel tense after si — in any type", "no futur after si", "Si tu viendras ✗ → Si tu viens ✓", "NEVER futur or ___ after si", "conditionnel"),
            ("would", "'would' → conditionnel présent", "English 'I would do' = conditionnel présent in Type 2 result", "would = conditionnel", "Si j'étais riche, j'achèterais... ('I would buy')", "'would' in result = conditionnel ___", "présent"),
            ("would-have", "'would have' → cond. passé", "English 'I would have done' = conditionnel passé in Type 3 result", "would have", "Si j'avais su, j'aurais dit... ('I would have said')", "'would have' in result = conditionnel ___", "passé"),
            ("inversion", "ordre interchangeable", "the si clause and result clause can swap positions — tenses stay the same", "clause order", "Si j'avais de l'argent, j'achèterais X. = J'achèterais X si j'avais de l'argent.", "si clause and result clause order is ___", "interchangeable"),
            ("mixed", "Type 2 + Type 3 mélangés", "mixed conditional: si + PQP (past) → conditionnel présent (present result)", "mixed conditional", "Si tu avais étudié, tu réussirais maintenant.", "mixed: si + PQP → conditionnel ___ (present result of past cause)", "présent"),
        ],
    },

    "negation-advanced": {
        "level": "b1",
        "section": "grammar",
        "num": "G10",
        "short": "negation-advanced",
        "title": "Advanced Negation — La Négation Avancée",
        "subtitle": "Go beyond ne…pas with ne…que, ni…ni, ne…jamais plus and more",
        "slides": [
            ("Ne…Que — Only / Restriction",
             "<b>Ne…que</b> expresses restriction: only. It is not a true negation — it limits rather than negates.",
             '<ul class="slide-list">'
             '<li>Je ne mange <b>que</b> des légumes. (I only eat vegetables.) → Only vegetables, nothing else.</li>'
             '<li>Il n\'a <b>qu\'</b>un euro. (He only has one euro.)</li>'
             '<li><em>Que</em> is placed directly BEFORE the restricted element (the noun/adj/adverb), not at the end.</li>'
             '<li>Alternative: <em>seulement</em> (Je mange seulement des légumes.) — interchangeable but <em>ne…que</em> is more formal.</li></ul>'),
            ("Ni…Ni — Neither…Nor",
             "<b>Ni…ni</b> replaces both elements in a negation. Articles are dropped after ni…ni. The verb is preceded by ne.",
             '<ul class="slide-list">'
             '<li>Je n\'aime <b>ni</b> le café <b>ni</b> le thé. (I like neither coffee nor tea.)</li>'
             '<li>Il n\'a <b>ni</b> argent <b>ni</b> travail. (He has neither money nor work.) — no article after ni</li>'
             '<li>With compound tenses: ne is before the auxiliary, ni…ni after: Elle n\'a <b>ni</b> mangé <b>ni</b> dormi.</li>'
             '<li>Ni can negate verbs: Il ne boit ni ne fume. (He neither drinks nor smokes.)</li></ul>'),
            ("Ne…Jamais Plus / Ne…Plus Jamais — Never Again",
             "<b>Ne…jamais plus</b> and <b>ne…plus jamais</b> both mean <em>never again</em>. Both are acceptable; plus jamais is slightly more emphatic.",
             '<ul class="slide-list">'
             '<li>Je ne ferai <b>jamais plus</b> cette erreur. (I will never make this mistake again.)</li>'
             '<li>Il ne m\'a <b>plus jamais</b> téléphoné. (He never called me again.)</li>'
             '<li><b>Ne…plus</b> alone = no longer / not anymore: Je ne fume <b>plus</b>. (I don\'t smoke anymore.)</li>'
             '<li><b>Ne…jamais</b> alone = never: Je ne mens <b>jamais</b>. (I never lie.)</li></ul>'),
            ("Negation in Compound Tenses and with Infinitives",
             "In compound tenses, most negative elements wrap around the auxiliary. With infinitives, ne pas (and most others) come BEFORE the infinitive together.",
             '<table class="sum-table"><thead><tr><th>Type</th><th>Compound tense</th><th>Infinitive</th></tr></thead><tbody>'
             '<tr><td>ne…pas</td><td>Il n\'a pas mangé.</td><td>Il préfère ne pas manger.</td></tr>'
             '<tr><td>ne…jamais</td><td>Il n\'a jamais mangé.</td><td>Il préfère ne jamais manger.</td></tr>'
             '<tr><td>ne…plus</td><td>Il n\'a plus mangé.</td><td>Il préfère ne plus manger.</td></tr>'
             '<tr><td>ne…que</td><td>Il n\'a mangé qu\'une pomme.</td><td>—</td></tr>'
             '</tbody></table>'),
        ],
        "traps": [
            ("Je mange seulement que des légumes.", "Je ne mange que des légumes. / Je mange seulement des légumes.", "Ne…que and seulement are alternatives — never combine them."),
            ("Je n'aime ni le café ni le thé. (with articles)", "Je n'aime ni café ni thé. (no articles after ni…ni)", "Drop the definite/indefinite article after ni in most cases."),
            ("Il n'a pas jamais menti. (double negation)", "Il n'a jamais menti.", "Never stack ne…pas and ne…jamais. Choose one negation. Pas jamais is a double negative."),
            ("Ne que position: Je mange que des légumes.", "Je ne mange que des légumes.", "Ne…que still requires ne before the verb — que alone is not sufficient."),
        ],
        "summary": [
            ("ne…que", "only / restriction", "Je ne mange que des légumes."),
            ("ne…plus", "no longer / not anymore", "Je ne fume plus."),
            ("ne…jamais", "never", "Je ne mens jamais."),
            ("ne…jamais plus", "never again", "Je ne le ferai jamais plus."),
            ("ni…ni", "neither…nor (no article)", "Je n'aime ni café ni thé."),
            ("ne…rien", "nothing", "Je n'ai rien dit."),
            ("ne…personne", "nobody", "Je n'ai vu personne."),
            ("neg. + infinitive", "ne pas before infinitive together", "Il préfère ne pas venir."),
        ],
        "ex1": (
            "Choose the Correct Negation",
            "Select the right negative structure.",
            [
                ("I only speak French. (restriction)", ["Je ne parle pas français.", "Je ne parle que français.", "Je ne parle jamais français.", "Je ne parle plus français."], "Je ne parle que français.", "Ne…que = only/restriction. Que before the restricted element (français)."),
                ("She no longer lives here.", ["Elle n'a pas vécu ici.", "Elle n'habite jamais ici.", "Elle n'habite plus ici.", "Elle ne vit que ici."], "Elle n'habite plus ici.", "Ne…plus = no longer/not anymore."),
                ("He likes neither coffee nor tea.", ["Il n'aime ni le café ni le thé.", "Il n'aime pas le café ni le thé.", "Il n'aime ni café ni thé.", "Il ne boit ni le café ni le thé."], "Il n'aime ni café ni thé.", "Ni…ni drops the definite articles: ni café ni thé."),
                ("I will never lie again.", ["Je ne mens jamais.", "Je ne mentirai plus.", "Je ne mentirai jamais plus.", "Je ne mens plus jamais."], "Je ne mentirai jamais plus.", "Never again = ne…jamais plus (future: je mentirai)."),
                ("She has said nothing.", ["Elle n'a pas dit rien.", "Elle n'a rien dit.", "Elle ne dit rien.", "Elle n'a dit que rien."], "Elle n'a rien dit.", "Ne…rien in compound tense: ne + auxiliary + rien + past participle."),
            ]
        ),
        "ex2": (
            "Translate the Negation",
            "Fill in the correct negative element.",
            [
                ("I only have five euros. (restriction)", "Je n'ai que cinq euros.", "Ne…que + amount. Que placed before cinq euros."),
                ("He no longer works here.", "Il ne travaille plus ici.", "Ne…plus = no longer."),
                ("They like neither jazz nor classical music.", "Ils n'aiment ni le jazz ni la musique classique.", "Ni…ni. Articles can stay with music genres treated as specific (stylistic choice — both with and without are used)."),
                ("I prefer not to go.", "Je préfère ne pas y aller.", "Negation before infinitive: ne pas before the infinitive together."),
                ("She has never seen him again.", "Elle ne l'a plus jamais vu.", "Ne…plus jamais = never again (past)."),
            ]
        ),
        "ex3": (
            "Spot the Error",
            "Choose the correctly negated sentence.",
            [
                ("Only restriction", ["Je mange seulement que des fruits.", "Je ne mange seulement des fruits.", "Je ne mange que des fruits.", "Je mange que des fruits."], "Je ne mange que des fruits.", "Ne…que: need ne before verb, que before restricted element. Never seulement que together."),
                ("Neither…nor", ["Il n'aime ni le café ni le thé.", "Il n'aime pas le café ni le thé.", "Il aime ni café ni thé.", "Il n'aime ni café et ni thé."], "Il n'aime ni le café ni le thé.", "Ni…ni wraps the verb with ne. Articles can be kept with aimer (taste/preference). Never ni…et ni."),
                ("Never again", ["Je ne le ferai pas encore.", "Je ne le ferai jamais plus.", "Je ne le ferai plus pas.", "Je ne le ferai jamais."], "Je ne le ferai jamais plus.", "Never again = jamais plus or plus jamais with ne. Ne…jamais alone = never (not again specifically)."),
                ("Compound tense rien", ["Il n'a pas dit rien.", "Il n'a rien dit.", "Il ne rien a dit.", "Il a ne rien dit."], "Il n'a rien dit.", "Rien: ne + auxiliary + rien + past participle. Never ne…pas…rien (double)."),
                ("Negation + infinitive", ["Il préfère ne pas partir.", "Il préfère pas ne partir.", "Il ne préfère pas partir.", "Il préfère ne partir pas."], "Il préfère ne pas partir.", "Ne pas together before the infinitive: ne pas partir."),
            ]
        ),
        "game_desc": "Master advanced French negation — ne…que, ni…ni, ne…plus jamais and more",
        "items": [
            ("ne-que", "ne…que", "restriction: only — not a real negation, limits rather than negates", "only", "Je ne mange que des légumes. (I only eat vegetables.)", "ne…___ = only (restriction)", "que"),
            ("ne-plus", "ne…plus", "no longer / not anymore — the action has stopped", "no longer", "Je ne fume plus. (I don't smoke anymore.)", "ne…___ = no longer / not anymore", "plus"),
            ("ne-jamais", "ne…jamais", "never — the action has never happened / will never happen", "never", "Je ne mens jamais. (I never lie.)", "ne…___ = never", "jamais"),
            ("jamais-plus", "ne…jamais plus / ne…plus jamais", "never again — combination of jamais and plus", "never again", "Je ne ferai jamais plus cette erreur.", "never again = ne…jamais ___ / ne…plus jamais", "plus"),
            ("ni-ni", "ni…ni (+ ne)", "neither…nor — articles often dropped; ne before verb", "neither…nor", "Il n'aime ni café ni thé.", "neither/nor = ___ … ni (+ ne before verb)", "ni"),
            ("ne-rien", "ne…rien", "nothing — rien wraps around auxiliary in compound tenses", "nothing", "Il n'a rien dit. (He said nothing.)", "ne…___ = nothing", "rien"),
            ("ne-personne", "ne…personne", "nobody / no one — personne goes AFTER the past participle", "nobody", "Il n'a vu personne. (He saw nobody.)", "ne…___ = nobody (after past participle in PC)", "personne"),
            ("neg-inf", "ne pas + infinitif", "negation before infinitive: ne pas / ne jamais / ne plus all go BEFORE the infinitive together", "neg. infinitive", "Il préfère ne pas venir.", "negation + infinitive: ___ pas / jamais / plus before inf.", "ne"),
        ],
    },

    "subjunctive-expressions": {
        "level": "b1",
        "section": "grammar",
        "num": "G11",
        "short": "subjunctive-expressions",
        "title": "Subjunctive Expressions — Expressions avec le Subjonctif",
        "subtitle": "Master the key verbs, adjectives, and conjunctions that trigger the subjunctive",
        "slides": [
            ("Verbs of Will, Wish, and Preference",
             "Verbs expressing wish, will, or preference trigger the subjunctive in the subordinate clause when the subject changes.",
             '<table class="sum-table"><thead><tr><th>Trigger verb</th><th>Example</th></tr></thead><tbody>'
             '<tr><td>vouloir que</td><td>Je veux <b>qu\'il vienne</b>. (I want him to come.)</td></tr>'
             '<tr><td>souhaiter que</td><td>Elle souhaite <b>que tu réussisses</b>. (She wishes you succeed.)</td></tr>'
             '<tr><td>préférer que</td><td>Je préfère <b>qu\'on parte</b> tôt.</td></tr>'
             '<tr><td>aimer que</td><td>Il aime <b>que tu sois</b> là.</td></tr>'
             '</tbody></table>'
             '<p>Same subject → infinitive: Je veux partir. (not Je veux que je parte.)</p>'),
            ("Verbs of Emotion and Doubt",
             "Verbs expressing emotion, fear, doubt, or denial also require the subjunctive.",
             '<table class="sum-table"><thead><tr><th>Trigger</th><th>Example</th></tr></thead><tbody>'
             '<tr><td>avoir peur que</td><td>J\'ai peur <b>qu\'il soit</b> malade.</td></tr>'
             '<tr><td>être content(e) que</td><td>Je suis content <b>que tu viennes</b>.</td></tr>'
             '<tr><td>regretter que</td><td>Elle regrette <b>qu\'il ne puisse</b> pas venir.</td></tr>'
             '<tr><td>douter que</td><td>Je doute <b>qu\'il sache</b> la réponse.</td></tr>'
             '<tr><td>ne pas croire que</td><td>Je ne crois pas <b>qu\'elle ait</b> raison.</td></tr>'
             '</tbody></table>'),
            ("Impersonal Expressions",
             "Many impersonal expressions with <em>il est / c\'est + adjective + que</em> trigger the subjunctive.",
             '<ul class="slide-list">'
             '<li><b>Il faut que</b> tu partes maintenant. (You must leave now.)</li>'
             '<li><b>Il est important que</b> vous soyez à l\'heure.</li>'
             '<li><b>Il est possible que</b> ce soit vrai.</li>'
             '<li><b>Il est dommage que</b> tu ne puisses pas venir.</li>'
             '<li><b>Il vaut mieux que</b> tu le fasses toi-même.</li>'
             '<li><b>C\'est normal que</b> tu sois fatigué.</li></ul>'),
            ("Conjunctions That Trigger the Subjunctive",
             "Several conjunctions always take the subjunctive. Key ones to master at B1:",
             '<table class="sum-table"><thead><tr><th>Conjunction</th><th>Meaning</th><th>Example</th></tr></thead><tbody>'
             '<tr><td>bien que / quoique</td><td>although</td><td>Bien qu\'il <b>soit</b> tard, je reste.</td></tr>'
             '<tr><td>pour que / afin que</td><td>so that</td><td>Je parle lentement pour qu\'il <b>comprenne</b>.</td></tr>'
             '<tr><td>avant que</td><td>before</td><td>Pars avant qu\'il <b>arrive</b>.</td></tr>'
             '<tr><td>à moins que</td><td>unless</td><td>Je viens, à moins que tu ne <b>préfères</b> être seul.</td></tr>'
             '<tr><td>jusqu\'à ce que</td><td>until</td><td>Attends jusqu\'à ce qu\'il <b>revienne</b>.</td></tr>'
             '</tbody></table>'),
        ],
        "traps": [
            ("Je veux que je parte. (same subject)", "Je veux partir.", "Same subject → infinitive, not subjunctive. Different subject → que + subjonctif."),
            ("Je pense qu'il soit là. (penser = belief, affirmative)", "Je pense qu'il est là.", "Affirmative penser/croire/espérer take the indicative. Only negative/interrogative penser/croire trigger subjunctive."),
            ("Bien qu'il est tard...", "Bien qu'il soit tard...", "Bien que ALWAYS takes the subjunctive. Never indicative after bien que."),
            ("après que + subjonctif", "après que + indicatif", "Après que takes the INDICATIVE (it's already done). Contrast: avant que takes the subjunctive."),
        ],
        "summary": [
            ("will/wish", "vouloir / souhaiter / préférer + que", "Je veux qu'il vienne."),
            ("emotion", "être content / avoir peur / regretter + que", "Je suis content que tu sois là."),
            ("doubt", "douter / ne pas croire + que", "Je doute qu'il sache."),
            ("il faut que", "obligation (impersonal)", "Il faut que tu partes."),
            ("bien que / quoique", "although + subj.", "Bien qu'il soit tard, je reste."),
            ("pour que / afin que", "so that + subj.", "Je parle lentement pour qu'il comprenne."),
            ("avant que", "before + subj.", "Pars avant qu'il arrive."),
            ("même sujet → infinitif", "same subject → no que + subj.", "Je veux partir. (not que je parte)"),
        ],
        "ex1": (
            "Indicative or Subjunctive?",
            "Choose the correct mood.",
            [
                ("Je pense qu'il ___ raison. (affirmative penser)", ["ait", "a", "aura", "avait"], "a", "Affirmative penser + que → indicative. Je pense qu'il a raison."),
                ("Il faut que tu ___ à l'heure. (obligation)", ["sois", "es", "seras", "étais"], "sois", "Il faut que → always subjunctive. Être → sois."),
                ("Elle est contente que tu ___. (emotion)", ["viens", "viennes", "viendras", "venais"], "viennes", "Être content que → subjunctive. Venir → viennes."),
                ("Je suis sûr qu'il ___. (certainty)", ["est", "soit", "sera", "ait été"], "est", "Être sûr que → certainty → indicative. Il est. (not soit)"),
                ("Bien qu'il ___ fatigué, il travaille.", ["est", "soit", "sera", "était"], "soit", "Bien que → always subjunctive. Être → soit."),
            ]
        ),
        "ex2": (
            "Fill in the Subjunctive",
            "Give the correct subjunctive form.",
            [
                ("Je veux que vous ___ (venir) ce soir.", "veniez", "Vouloir que → subjunctive. Venir → vous veniez."),
                ("Il est possible que ce ___ (être) vrai.", "soit", "Il est possible que → subjunctive. Être → soit."),
                ("J'ai peur qu'il ne ___ (pouvoir) pas venir.", "puisse", "Avoir peur que → subjunctive. Pouvoir → puisse."),
                ("Parle fort pour qu'il t'___ (entendre).", "entende", "Pour que → subjunctive. Entendre → entende."),
                ("Je doute qu'elle ___ (savoir) la réponse.", "sache", "Douter que → subjunctive. Savoir → sache."),
            ]
        ),
        "ex3": (
            "Choose the Correct Sentence",
            "Which sentence correctly uses the subjunctive rule?",
            [
                ("I want to leave. (same subject)", ["Je veux que je parte.", "Je veux partir.", "Je veux que partir.", "Je veux que je pars."], "Je veux partir.", "Same subject (je) → infinitive. Je veux partir. No que + subjonctif."),
                ("Although she's tired, she continues.", ["Bien qu'elle est fatiguée, elle continue.", "Bien qu'elle soit fatiguée, elle continue.", "Quoique elle soit fatiguée, elle continue.", "Malgré qu'elle soit fatiguée, elle continue."], "Bien qu'elle soit fatiguée, elle continue.", "Bien que → always subjunctive. Quoique is valid but requires que inside: quoiqu'elle soit. Malgré que is informal/disputed."),
                ("I'm leaving before he arrives.", ["Je pars avant que je n'arrive.", "Je pars après qu'il arrive.", "Je pars avant qu'il arrive.", "Je pars avant qu'il est arrivé."], "Je pars avant qu'il arrive.", "Avant que → subjunctive. Different subjects (je / il). Arriver → arrive."),
                ("I don't think she knows.", ["Je ne pense pas qu'elle sait.", "Je ne pense pas qu'elle sache.", "Je ne pense pas qu'elle soit.", "Je ne pense pas qu'elle saura."], "Je ne pense pas qu'elle sache.", "Negative penser + que → subjunctive. Savoir → sache."),
                ("You must be on time.", ["Il est important que tu es à l'heure.", "Il faut que tu sois à l'heure.", "Il faut être à l'heure à toi.", "Il faut que tu es à l'heure."], "Il faut que tu sois à l'heure.", "Il faut que → subjunctive. Être → sois."),
            ]
        ),
        "game_desc": "Master the French expressions and conjunctions that trigger the subjunctive",
        "items": [
            ("vouloir-que", "vouloir que + subj.", "trigger: will/desire — vouloir que (different subject)", "want that", "Je veux qu'il vienne ce soir.", "vouloir que → ___ (different subject)", "subjonctif"),
            ("emotion-que", "être content/triste que + subj.", "trigger: emotion — être content/triste/surpris/fier que", "emotion trigger", "Je suis content que tu sois là.", "être content que → ___", "subjonctif"),
            ("il-faut-que", "il faut que + subj.", "obligation: il faut que / il est nécessaire que → subjunctive", "must / necessary", "Il faut que tu partes maintenant.", "il faut que → ___", "subjonctif"),
            ("bien-que", "bien que + subj.", "although — always subjunctive (never indicative after bien que)", "although", "Bien qu'il soit tard, je reste.", "bien que → ___ (always)", "subjonctif"),
            ("pour-que", "pour que / afin que + subj.", "so that — always subjunctive", "so that", "Je parle lentement pour qu'il comprenne.", "pour que → ___", "subjonctif"),
            ("avant-que", "avant que + subj.", "before — always subjunctive (contrast: après que → indicative)", "before", "Pars avant qu'il arrive.", "avant que → ___ (contrast: après que → indicatif)", "subjonctif"),
            ("meme-sujet", "même sujet → infinitif", "if both clauses share the subject, use infinitive — not que + subjonctif", "same subject rule", "Je veux partir. (not que je parte)", "same subject → ___ (not que + subjonctif)", "infinitif"),
            ("douter-que", "douter / ne pas croire + subj.", "doubt: douter que / ne pas croire que → subjunctive", "doubt trigger", "Je doute qu'il sache la réponse.", "douter que → ___", "subjonctif"),
        ],
    },

    "faux-amis-b1": {
        "level": "b1",
        "section": "grammar",
        "num": "G12",
        "short": "faux-amis-b1",
        "title": "Faux Amis B1 — False Friends",
        "subtitle": "Avoid B1-level false cognates that trap intermediate learners",
        "slides": [
            ("Verbs That Look Familiar but Aren't",
             "Several common French verbs look like English words but have very different meanings at B1 level.",
             '<table class="sum-table"><thead><tr><th>French word</th><th>Looks like</th><th>Actual meaning</th><th>True equivalent</th></tr></thead><tbody>'
             '<tr><td><b>assister à</b></td><td>assist</td><td>to attend (a show/meeting)</td><td>aider (to help/assist)</td></tr>'
             '<tr><td><b>attendre</b></td><td>attend</td><td>to wait (for)</td><td>assister à (to attend)</td></tr>'
             '<tr><td><b>rester</b></td><td>rest</td><td>to stay / remain</td><td>se reposer (to rest)</td></tr>'
             '<tr><td><b>quitter</b></td><td>quit</td><td>to leave (a place/person)</td><td>abandonner / démissionner (to quit a job)</td></tr>'
             '</tbody></table>'),
            ("Nouns That Deceive",
             "These nouns are particularly tricky because they are very similar to English but mean something different.",
             '<table class="sum-table"><thead><tr><th>French word</th><th>Looks like</th><th>Actual meaning</th><th>True equivalent</th></tr></thead><tbody>'
             '<tr><td><b>une librairie</b></td><td>library</td><td>a bookshop</td><td>une bibliothèque (library)</td></tr>'
             '<tr><td><b>un journaliste</b></td><td>journalist ✓</td><td>journalist (correct!)</td><td>—</td></tr>'
             '<tr><td><b>une location</b></td><td>location</td><td>a rental / letting</td><td>un endroit / un lieu (location)</td></tr>'
             '<tr><td><b>un car</b></td><td>car</td><td>a coach / long-distance bus</td><td>une voiture (car)</td></tr>'
             '<tr><td><b>un médecin</b></td><td>medicine</td><td>a doctor</td><td>la médecine (medicine/field)</td></tr>'
             '</tbody></table>'),
            ("Adjectives and Adverbs",
             "These adjectives and adverbs cause consistent errors at B1 level.",
             '<table class="sum-table"><thead><tr><th>French word</th><th>Looks like</th><th>Actual meaning</th><th>True equivalent</th></tr></thead><tbody>'
             '<tr><td><b>actuel / actuellement</b></td><td>actual / actually</td><td>current / currently</td><td>en réalité / vraiment (actually)</td></tr>'
             '<tr><td><b>éventuellement</b></td><td>eventually</td><td>possibly / perhaps</td><td>finalement / à la fin (eventually)</td></tr>'
             '<tr><td><b>sensible</b></td><td>sensible</td><td>sensitive / emotional</td><td>raisonnable / sensé (sensible)</td></tr>'
             '<tr><td><b>large</b></td><td>large</td><td>wide / broad</td><td>grand / gros (large/big)</td></tr>'
             '</tbody></table>'),
            ("False Friends in Context",
             "Seeing false friends in context helps cement the correct meaning.",
             '<ul class="slide-list">'
             '<li>J\'ai <b>assisté à</b> la conférence. (I attended the conference.) ✓ — not I assisted at...</li>'
             '<li>J\'attends le bus depuis 20 minutes. (I\'ve been waiting for the bus for 20 min.) ✓</li>'
             '<li>La <b>location</b> de cet appartement coûte 900€. (The rental of this flat costs €900.) ✓</li>'
             '<li>La situation <b>actuelle</b> est difficile. (The current situation is difficult.) ✓</li>'
             '<li>Elle est très <b>sensible</b> — elle pleure facilement. (She is very sensitive.) ✓</li>'
             '<li>Cette rue est très <b>large</b>. (This street is very wide.) ✓</li></ul>'),
        ],
        "traps": [
            ("J'ai assisté à Marie pendant la réunion. (helped her)", "J'ai aidé Marie pendant la réunion.", "Assister à = to attend. To help someone = aider quelqu'un."),
            ("Je vais à la librairie emprunter un livre. (borrow)", "Je vais à la bibliothèque emprunter un livre.", "Librairie = bookshop (to buy). Bibliothèque = library (to borrow)."),
            ("La situation actuelle est la vérité. (actually)", "En réalité / En fait, c'est la vérité.", "Actuel = current (not actual). Actually = en réalité / en fait."),
            ("Je partirai éventuellement. (eventually)", "Je partirai finalement. / Je finirai par partir.", "Éventuellement = possibly / perhaps (not eventually). Eventually = finalement / à la fin."),
        ],
        "summary": [
            ("assister à", "to attend (not assist)", "J'ai assisté à la conférence."),
            ("attendre", "to wait for (not attend)", "J'attends le bus."),
            ("rester", "to stay (not rest)", "Je reste ici ce soir."),
            ("une librairie", "bookshop (not library)", "J'achète mes livres à la librairie."),
            ("une location", "a rental (not location)", "La location de l'appartement est chère."),
            ("actuel/actuellement", "current/currently (not actual/actually)", "La situation actuelle est difficile."),
            ("éventuellement", "possibly (not eventually)", "Il viendra éventuellement. (maybe he'll come)"),
            ("sensible", "sensitive (not sensible)", "Elle est très sensible — elle pleure facilement."),
        ],
        "ex1": (
            "What Does It Actually Mean?",
            "Choose the correct meaning of the French word.",
            [
                ("assister à une réunion", ["to assist at a meeting", "to attend a meeting", "to organise a meeting", "to miss a meeting"], "to attend a meeting", "Assister à = to attend/be present at. NOT to assist/help."),
                ("une librairie", ["a library", "a library card", "a bookshop", "a reading room"], "a bookshop", "Librairie = bookshop (to buy books). Bibliothèque = library (to borrow books)."),
                ("actuellement", ["actually", "in actuality", "at the moment / currently", "really"], "at the moment / currently", "Actuellement = currently / at the moment. NOT actually (= en réalité)."),
                ("éventuellement", ["eventually", "gradually", "possibly / perhaps", "normally"], "possibly / perhaps", "Éventuellement = possibly. Eventually = finalement / à la fin."),
                ("sensible", ["sensible / reasonable", "sensitive / emotional", "sensational", "insensible"], "sensitive / emotional", "Sensible in French = easily affected emotionally. Sensible (English) = raisonnable."),
            ]
        ),
        "ex2": (
            "Choose the Right Word",
            "Select the correct French word for the English meaning.",
            [
                ("I attended the concert. (verb)", "J'ai assisté au concert.", "Assister à (+ au = à + le). Attended = assisté à."),
                ("She's very sensible about money. (reasonable)", "Elle est très raisonnable avec l'argent.", "Sensible (English, reasonable) = raisonnable in French. Sensible in French = sensitive."),
                ("I'm going to the library to borrow a book.", "Je vais à la bibliothèque emprunter un livre.", "Library (to borrow) = bibliothèque. Librairie = bookshop (to buy)."),
                ("The current president is popular.", "Le président actuel est populaire.", "Current = actuel. Actual (English, real) = réel / vrai."),
                ("He'll possibly come later.", "Il viendra éventuellement.", "Possibly = éventuellement. Eventually (in the end) = finalement."),
            ]
        ),
        "ex3": (
            "Spot the Faux Ami Error",
            "Choose the sentence that CORRECTLY avoids the false friend.",
            [
                ("I'm waiting for the train.", ["J'attends le train. ✓", "J'assiste au train.", "J'aide le train.", "J'attend le train."], "J'attends le train. ✓", "Attendre = to wait for. Assister à = to attend. J'attends is correct."),
                ("I need to rest.", ["Je dois rester.", "Je dois me reposer.", "Je dois assister.", "Je dois attendre."], "Je dois me reposer.", "Rest = se reposer. Rester = to stay/remain."),
                ("The rental is 800 euros.", ["L'emplacement est 800 euros.", "La localisation est 800 euros.", "La location est 800 euros.", "Le lieu est 800 euros."], "La location est 800 euros.", "Rental = une location. Location (place) = un endroit / un lieu."),
                ("This road is very wide.", ["Cette route est très large. ✓", "Cette route est très grosse.", "Cette route est très grande.", "Cette route est très large grande."], "Cette route est très large. ✓", "Large in French = wide/broad. Large in English = big → grand/gros. Here large IS correct (it means wide)."),
                ("I took the coach (long-distance bus).", ["J'ai pris la voiture.", "J'ai pris le car.", "J'ai pris le taxi.", "J'ai pris la moto."], "J'ai pris le car.", "Un car = coach/long-distance bus. Une voiture = car."),
            ]
        ),
        "game_desc": "Avoid B1-level French false friends — assister à, librairie, actuel, éventuellement and more",
        "items": [
            ("assister-a", "assister à", "to attend (NOT to assist) — always followed by à + event", "attend", "J'ai assisté à la conférence hier.", "assister à = to ___ (not to assist)", "attend"),
            ("attendre", "attendre", "to wait for (NOT to attend) — takes direct object", "wait for", "J'attends le bus depuis 20 minutes.", "attendre = to ___ for (not to attend)", "wait"),
            ("librairie", "une librairie", "bookshop where you BUY books (NOT a library)", "bookshop", "Je vais à la librairie acheter ce roman.", "une librairie = ___ (not library)", "bookshop"),
            ("bibliotheque", "une bibliothèque", "a library where you BORROW books (contrast: librairie = bookshop)", "library", "J'emprunte des livres à la bibliothèque.", "une bibliothèque = ___ (not bookshop)", "library"),
            ("actuel", "actuel / actuellement", "current / currently — NOT actual / actually", "current", "La situation actuelle est préoccupante.", "actuel = ___ (not 'actual')", "current"),
            ("eventuellement", "éventuellement", "possibly / perhaps — NOT eventually (= finalement)", "possibly", "Il viendra éventuellement. (He might come.)", "éventuellement = ___ (not 'eventually')", "possibly"),
            ("sensible", "sensible", "sensitive / emotional — NOT sensible (English, = reasonable → raisonnable)", "sensitive", "Elle est très sensible et pleure facilement.", "sensible (French) = ___ (not 'sensible')", "sensitive"),
            ("location", "une location", "a rental / a letting — NOT a location (= un endroit / un lieu)", "rental", "La location de cet appartement coûte 900€.", "une location = ___ (not 'location')", "rental"),
        ],
    },
}
