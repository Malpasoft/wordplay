"""
francais-en A2 Grammar G07–G12  (French for English Speakers)
Generator: gen_francais_en.py
"""

CHAPTERS = {

    # ------------------------------------------------------------------ G07
    "partitive-articles": {
        "level": "a2", "section": "grammar", "num": "G07",
        "short": "Partitive Articles",
        "title": "Partitive Articles — du, de la, de l', des",
        "subtitle": "Expressing 'some' — uncountable quantities in French",
        "slides": [
            ("What Are Partitive Articles?",
             "Partitive articles express an <strong>unspecified quantity</strong> of something — 'some bread', 'some water'. English often omits them; French requires them.",
             "<em>Je mange du pain.</em> — I eat (some) bread.<br>"
             "<em>Elle boit de l'eau.</em> — She drinks (some) water.<br>"
             "<em>Il achète des légumes.</em> — He buys (some) vegetables.<br>"
             "English often omits 'some'; French never does for uncountable nouns."),
            ("The Three Forms",
             "The partitive article has three forms, chosen by gender/starting sound.",
             "<table><tr><th>Noun type</th><th>Partitive</th><th>Example</th></tr>"
             "<tr><td>Masculine</td><td>du (= de + le)</td><td>du café, du lait</td></tr>"
             "<tr><td>Feminine</td><td>de la</td><td>de la viande, de la farine</td></tr>"
             "<tr><td>Vowel / silent h</td><td>de l'</td><td>de l'eau, de l'huile</td></tr>"
             "<tr><td>Plural (countable)</td><td>des</td><td>des oranges, des tomates</td></tr></table>"),
            ("After Negation — Always de/d'",
             "After <em>ne…pas</em>, the partitive (and indefinite articles un/une/des) all become <strong>de/d'</strong>.",
             "<em>J'achète du pain.</em> → <em>Je n'achète pas de pain.</em><br>"
             "<em>Elle mange de la salade.</em> → <em>Elle ne mange pas de salade.</em><br>"
             "<em>Il a des amis.</em> → <em>Il n'a pas d'amis.</em><br>"
             "Rule: after negation, de/d' replaces du, de la, de l', des, un, une."),
            ("Partitive vs. Definite Article",
             "Use the <strong>definite article</strong> (le/la/les) for general statements or preferences; use the <strong>partitive</strong> for quantities.",
             "<em>J'aime le café.</em> — I like coffee (in general).<br>"
             "<em>Je prends du café.</em> — I'm having (some) coffee.<br>"
             "<em>Les légumes sont bons pour la santé.</em> — Vegetables are good for health (general).<br>"
             "<em>Je mange des légumes.</em> — I'm eating (some) vegetables."),
            ("Quick Summary",
             "Key rules for partitive articles at a glance.",
             "• du (masc.) / de la (fem.) / de l' (vowel/h) / des (plural).<br>"
             "• After negation: all → de/d'.<br>"
             "• General truth / preference → le/la/les (not partitive).<br>"
             "• Expressions of quantity take de/d' too: <em>un verre de vin, beaucoup de pain.</em>"),
        ],
        "traps": [
            ("I like wine (general)", "J'aime le vin", "General preference → le/la/les, not du/de la."),
            ("I'm drinking wine (now)", "Je bois du vin", "Partitive for quantity being consumed."),
            ("I don't eat meat", "Je ne mange pas de viande", "After negation: de la → de."),
            ("a glass of water", "un verre d'eau", "Expressions of quantity take de/d'."),
        ],
        "summary": [
            ("masc. noun", "du", "du café, du lait, du pain"),
            ("fem. noun", "de la", "de la viande, de la farine, de la bière"),
            ("vowel/h noun", "de l'", "de l'eau, de l'huile, de l'argent"),
            ("plural", "des", "des fruits, des légumes, des œufs"),
            ("after negation", "de / d'", "pas de pain, pas d'eau, pas de viande"),
            ("after quantity", "de / d'", "un verre de vin, beaucoup de lait"),
            ("general / preference", "le / la / les", "J'aime le fromage. Les légumes sont sains."),
            ("with numbers", "no article", "deux kilos de farine, trois litres d'eau"),
        ],
        "ex1": ("Exercise 1 — Choose the correct partitive",
                "Select the right article.",
                [
                    ("Je bois ___ café le matin.", ["du", "de la", "de l'", "des"], "du",
                     "Café is masculine → du."),
                    ("Elle mange ___ viande deux fois par semaine.", ["du", "de la", "de l'", "des"], "de la",
                     "Viande is feminine → de la."),
                    ("Il boit ___ eau après le sport.", ["du", "de la", "de l'", "des"], "de l'",
                     "Eau starts with a vowel → de l'."),
                    ("Nous achetons ___ légumes au marché.", ["du", "de la", "de l'", "des"], "des",
                     "Légumes is plural → des."),
                    ("Je n'achète pas ___ pain aujourd'hui.", ["du", "de", "de la", "des"], "de",
                     "After negation: du/de la/des → de."),
                    ("J'ai besoin ___ argent.", ["du", "de l'", "de la", "des"], "de l'",
                     "Argent starts with a vowel → de l'."),
                ]),
        "ex2": ("Exercise 2 — Translate into French",
                "Type the French sentence.",
                [
                    ("I'm eating some cheese.", "Je mange du fromage.", "Fromage is masculine → du."),
                    ("She drinks some milk.", "Elle boit du lait.", "Lait is masculine → du."),
                    ("We don't eat meat.", "Nous ne mangeons pas de viande.", "After negation → de."),
                    ("I like cheese (in general).", "J'aime le fromage.", "General preference → le."),
                    ("I need some water.", "J'ai besoin d'eau.", "After besoin de + vowel → d'."),
                ]),
        "ex3": ("Exercise 3 — General or partitive?",
                "Pick the correct form.",
                [
                    ("'I like wine' (general preference):", ["Je bois du vin.", "J'aime le vin.", "J'aime du vin.", "Je prends le vin."], "J'aime le vin.",
                     "General preference → aimer + le/la/les."),
                    ("'She is drinking some water' (right now):", ["Elle aime l'eau.", "Elle boit de l'eau.", "Elle boit du eau.", "Elle boit l'eau."], "Elle boit de l'eau.",
                     "Partitive for a quantity being drunk → de l' before vowel."),
                    ("'He doesn't eat any bread':", ["Il ne mange pas du pain.", "Il ne mange pas de pain.", "Il ne mange pas le pain.", "Il ne mange pas des pains."], "Il ne mange pas de pain.",
                     "After ne…pas: du → de."),
                    ("'a glass of orange juice':", ["un verre du jus d'orange", "un verre de jus d'orange", "un verre de le jus d'orange", "un verre des jus"], "un verre de jus d'orange",
                     "After quantity expression → de/d' (no article after un verre de)."),
                ]),
        "game_desc": "Practice partitive articles — du, de la, de l', des — and their negation.",
        "items": [
            ("part1", "du", "some (masc. noun)", "some", "Je mange du pain et du fromage.", "Complète: Je bois ___ café. (some, masc.)", "du"),
            ("part2", "de la", "some (fem. noun)", "some fem.", "Elle mange de la viande le dimanche.", "Complète: Il boit de ___ bière. (fem.)", "la"),
            ("part3", "de l'", "some (vowel/h noun)", "some vowel", "Je bois de l'eau minérale.", "Complète: Elle mange de ___ huile. (vowel)", "l'"),
            ("part4", "des", "some (plural)", "some plural", "Nous achetons des fruits au marché.", "Complète: Il mange ___ légumes. (plural)", "des"),
            ("part5", "ne…pas de", "no / not any (after negation)", "not any", "Je ne mange pas de viande — je suis végétarien.", "Complète: Il ne boit pas ___ café. (neg.)", "de"),
            ("part6", "aimer + le/la/les", "to like (general)", "to like", "J'aime le café, mais je préfère le thé.", "Complète: Elle aime ___ fromage. (general pref.)", "le"),
            ("part7", "un verre de", "a glass of", "glass of", "Je voudrais un verre de vin rouge.", "Complète: un verre ___ eau. (of)", "d'"),
            ("part8", "beaucoup de", "a lot of (no article)", "lots of", "Il y a beaucoup de monde au marché.", "Complète: beaucoup ___ pain. (of)", "de"),
        ],
    },

    # ------------------------------------------------------------------ G08
    "reflexive-verbs": {
        "level": "a2", "section": "grammar", "num": "G08",
        "short": "Reflexive Verbs",
        "title": "Reflexive Verbs — se laver, se lever…",
        "subtitle": "Verbs where the subject acts on itself",
        "slides": [
            ("What Are Reflexive Verbs?",
             "Reflexive verbs have a <strong>reflexive pronoun</strong> (me, te, se, nous, vous, se) that refers back to the subject — the subject does the action to itself.",
             "<em>Je me lave.</em> — I wash myself.<br>"
             "<em>Tu te lèves tôt.</em> — You get up early.<br>"
             "<em>Elle se couche à 22h.</em> — She goes to bed at 10pm.<br>"
             "The reflexive pronoun must match the subject."),
            ("Reflexive Pronoun Conjugation Table",
             "The pronouns change with each subject.",
             "<table><tr><th>Subject</th><th>Reflexive</th><th>Example</th></tr>"
             "<tr><td>je</td><td>me / m'</td><td>je me lève</td></tr>"
             "<tr><td>tu</td><td>te / t'</td><td>tu te laves</td></tr>"
             "<tr><td>il/elle/on</td><td>se / s'</td><td>il se couche</td></tr>"
             "<tr><td>nous</td><td>nous</td><td>nous nous levons</td></tr>"
             "<tr><td>vous</td><td>vous</td><td>vous vous rasez</td></tr>"
             "<tr><td>ils/elles</td><td>se / s'</td><td>elles s'habillent</td></tr></table>"),
            ("Common Reflexive Verbs",
             "Many daily routine verbs are reflexive in French.",
             "<em>se lever</em> — to get up<br>"
             "<em>se laver</em> — to wash (oneself)<br>"
             "<em>se doucher</em> — to have a shower<br>"
             "<em>se brosser les dents</em> — to brush one's teeth<br>"
             "<em>se coucher</em> — to go to bed<br>"
             "<em>s'appeler</em> — to be called<br>"
             "<em>se dépêcher</em> — to hurry"),
            ("Reflexive Verbs — Negative and Question",
             "In the negative, <em>ne</em> comes before the reflexive pronoun; <em>pas</em> after the verb.",
             "<em>Je ne me lève pas tôt.</em> — I don't get up early.<br>"
             "<em>Il ne se douche pas le soir.</em> — He doesn't shower in the evening.<br>"
             "In a question with inversion, the pronoun stays with the verb:<br>"
             "<em>Te lèves-tu tôt ?</em> — Do you get up early?"),
            ("Reflexive Verbs in Passé Composé",
             "Reflexive verbs always use <strong>être</strong> in the passé composé, and the past participle agrees with the subject.",
             "<em>Je me suis levé(e) tôt.</em> — I got up early.<br>"
             "<em>Elle s'est lavée.</em> — She washed herself. (agree: f. singular)<br>"
             "<em>Ils se sont couchés tard.</em> — They went to bed late. (agree: m. plural)<br>"
             "Structure: subject + reflexive pronoun + être (conjugated) + past participle (agreed)."),
        ],
        "traps": [
            ("nous nous levons", "We get up — both 'nous' needed", "Subject 'nous' + reflexive 'nous' — both required."),
            ("she washed (herself)", "elle s'est lavée", "Agreement in PC: s' = elle → add -e to lavée."),
            ("they (m) got up", "ils se sont levés", "Agreement in PC: ils → add -s to levés."),
            ("I don't get up early", "Je ne me lève pas tôt", "ne before reflexive pronoun, pas after verb."),
        ],
        "summary": [
            ("je", "me / m'", "je me lève, je m'appelle"),
            ("tu", "te / t'", "tu te laves, tu t'habilles"),
            ("il / elle / on", "se / s'", "il se couche, elle s'appelle"),
            ("nous", "nous", "nous nous levons, nous nous dépêchons"),
            ("vous", "vous", "vous vous rasez, vous vous couchez"),
            ("ils / elles", "se / s'", "ils se lèvent, elles s'habillent"),
            ("PC: auxiliary", "être (always)", "Je me suis levé(e). Elle s'est couchée."),
            ("PC: agreement", "PP agrees with subject", "Elles se sont levées. Ils se sont couchés."),
        ],
        "ex1": ("Exercise 1 — Choose the correct reflexive form",
                "Select the right pronoun/form.",
                [
                    ("Nous ___ levons à 7h.", ["nous nous", "me", "se", "vous vous"], "nous nous",
                     "Subject nous + reflexive nous."),
                    ("Tu ___ douches le matin ou le soir ?", ["te", "me", "se", "vous"], "te",
                     "Tu → reflexive te."),
                    ("Elle ___ est couchée tard hier.", ["s'", "me", "se", "t'"], "s'",
                     "PC reflexive with être; s' before vowel."),
                    ("Ils ___ sont levés tôt.", ["se", "s'", "me", "te"], "se",
                     "PC: ils se sont levés."),
                    ("Je ne ___ lève pas avant 9h.", ["me", "se", "te", "nous"], "me",
                     "Je → reflexive me."),
                ]),
        "ex2": ("Exercise 2 — Translate into French",
                "Type the French sentence.",
                [
                    ("I get up at 6.", "Je me lève à six heures.", "je me lève."),
                    ("She showers every morning.", "Elle se douche chaque matin.", "elle se douche."),
                    ("They (m) went to bed late.", "Ils se sont couchés tard.", "PC: se + être; -s agreement."),
                    ("We hurry!", "Nous nous dépêchons !", "nous nous dépêchons."),
                    ("He didn't wash (himself).", "Il ne s'est pas lavé.", "PC neg: ne + s'est + pas + lavé."),
                ]),
        "ex3": ("Exercise 3 — Spot the error",
                "Which sentence is correct?",
                [
                    ("'She got up early' in French:", ["Elle s'a levée tôt.", "Elle s'est levée tôt.", "Elle se lève tôt hier.", "Elle se s'est levée tôt."], "Elle s'est levée tôt.",
                     "PC: s'est + levée (être auxiliary, agree f.)."),
                    ("'I don't get up early':", ["Je me ne lève pas tôt.", "Je ne me lève pas tôt.", "Je ne lève pas me tôt.", "Je ne me lèves pas tôt."], "Je ne me lève pas tôt.",
                     "Order: ne + reflexive + verb + pas."),
                    ("'We washed ourselves' in the PC:", ["Nous avons nous lavés.", "Nous nous sommes lavés.", "Nous nous avons lavé.", "Nous se sommes lavés."], "Nous nous sommes lavés.",
                     "PC: nous nous sommes + lavés (agree m. plural)."),
                    ("Which reflexive verb means 'to hurry'?", ["se lever", "se dépêcher", "se coucher", "se laver"], "se dépêcher",
                     "Se dépêcher = to hurry."),
                ]),
        "game_desc": "Master French reflexive verbs — daily routine, PC, and negation.",
        "items": [
            ("ref1", "se lever", "to get up", "get up", "Je me lève à sept heures chaque matin.", "Complète: Je me ___ tôt. (get up)", "lève"),
            ("ref2", "se laver", "to wash (oneself)", "wash", "Il se lave les mains avant de manger.", "Complète: Tu te ___ le matin. (wash)", "laves"),
            ("ref3", "se coucher", "to go to bed", "go to bed", "Elle se couche à vingt-deux heures.", "Complète: Je me ___ à 23h. (go to bed)", "couche"),
            ("ref4", "s'appeler", "to be called / named", "be called", "Je m'appelle Marc. Comment tu t'appelles ?", "Complète: Elle s'___ Sophie. (is called)", "appelle"),
            ("ref5", "se doucher", "to have a shower", "shower", "Il se douche après le sport.", "Complète: Tu te ___ le soir ? (shower)", "douches"),
            ("ref6", "se dépêcher", "to hurry", "hurry", "Dépêchez-vous ! Le train part dans cinq minutes !", "Complète: Je me ___ ! (hurry)", "dépêche"),
            ("ref7", "PC: s'est + PP", "she got up / washed (PC)", "she got up", "Elle s'est levée tôt et s'est habillée vite.", "Complète: Elle s'est ___. (got up, f.)", "levée"),
            ("ref8", "ne se…pas", "reflexive negation", "not wash", "Je ne me lève pas tôt le week-end.", "Complète: Il ne se ___ pas. (doesn't get up)", "lève"),
        ],
    },

    # ------------------------------------------------------------------ G09
    "future-simple": {
        "level": "a2", "section": "grammar", "num": "G09",
        "short": "Future Simple",
        "title": "Future Simple — je parlerai, tu finiras…",
        "subtitle": "Talking about future events — will do",
        "slides": [
            ("What Is the Future Simple?",
             "The future simple expresses what <strong>will happen</strong>. It is formed differently from the near future (aller + infinitive) — it uses a one-word tense.",
             "<em>Je parlerai français.</em> — I will speak French.<br>"
             "<em>Elle finira ses devoirs.</em> — She will finish her homework.<br>"
             "<em>Nous partirons demain.</em> — We will leave tomorrow.<br>"
             "Use it for decisions, predictions, and formal promises."),
            ("Formation — Regular Verbs",
             "For -er and -ir verbs: add endings to the <strong>infinitive</strong>. For -re verbs: drop the -e first.",
             "<table><tr><th>Subject</th><th>Ending</th><th>parler</th><th>finir</th><th>vendre</th></tr>"
             "<tr><td>je</td><td>-ai</td><td>parlerai</td><td>finirai</td><td>vendrai</td></tr>"
             "<tr><td>tu</td><td>-as</td><td>parleras</td><td>finiras</td><td>vendras</td></tr>"
             "<tr><td>il/elle</td><td>-a</td><td>parlera</td><td>finira</td><td>vendra</td></tr>"
             "<tr><td>nous</td><td>-ons</td><td>parlerons</td><td>finirons</td><td>vendrons</td></tr>"
             "<tr><td>vous</td><td>-ez</td><td>parlerez</td><td>finirez</td><td>vendrez</td></tr>"
             "<tr><td>ils</td><td>-ont</td><td>parleront</td><td>finiront</td><td>vendront</td></tr></table>"),
            ("Irregular Future Stems",
             "Many common verbs have irregular stems but use the same endings.",
             "<em>être → ser-</em> : je serai (I will be)<br>"
             "<em>avoir → aur-</em> : j'aurai (I will have)<br>"
             "<em>aller → ir-</em> : j'irai (I will go)<br>"
             "<em>faire → fer-</em> : je ferai (I will do/make)<br>"
             "<em>pouvoir → pourr-</em> : je pourrai (I will be able)<br>"
             "<em>venir → viendr-</em> : je viendrai (I will come)<br>"
             "<em>voir → verr-</em> : je verrai (I will see)"),
            ("Future Simple vs. Futur Proche",
             "Both refer to the future, but they feel different.",
             "<strong>Futur proche (aller + inf.)</strong> — near future, planned, certain:<br>"
             "<em>Je vais partir demain.</em> — I'm going to leave tomorrow. (planned)<br><br>"
             "<strong>Future simple</strong> — more open, predictions, formal promises:<br>"
             "<em>Je partirai demain.</em> — I will leave tomorrow.<br>"
             "At A2 level, both are often interchangeable in speech."),
            ("Quick Summary",
             "Future simple at a glance.",
             "• Regular: infinitive + -ai/-as/-a/-ons/-ez/-ont.<br>"
             "• -re verbs: drop -e before adding endings.<br>"
             "• Key irregulars: ser- / aur- / ir- / fer- / pourr- / viendr- / verr-.<br>"
             "• With <em>si</em> clause: present + future (not future + future):<br>"
             "  <em>Si tu travailles, tu réussiras.</em> (If you work, you'll succeed.)"),
        ],
        "traps": [
            ("If you work, you will succeed", "Si tu travailles, tu réussiras", "si + present, main clause + future (not si + future)."),
            ("I will go", "j'irai", "aller is irregular: ir- + ai → j'irai."),
            ("she will be", "elle sera", "être is irregular: ser- + a → sera."),
            ("we will do", "nous ferons", "faire is irregular: fer- + ons → ferons."),
        ],
        "summary": [
            ("je", "-ai", "je parlerai · je serai · j'irai"),
            ("tu", "-as", "tu finiras · tu auras · tu feras"),
            ("il / elle", "-a", "il vendra · elle sera · il pourra"),
            ("nous", "-ons", "nous parlerons · nous irons"),
            ("vous", "-ez", "vous finirez · vous verrez"),
            ("ils / elles", "-ont", "ils parleront · elles auront"),
            ("irregular stems", "ser- / aur- / ir- / fer- / pourr-", "sera · aura · ira · fera · pourra"),
            ("si + present", "→ future in main clause", "Si tu viens, on mangera ensemble."),
        ],
        "ex1": ("Exercise 1 — Choose the correct future form",
                "Select the right verb form.",
                [
                    ("Demain, il ___ beau. (il fait → future)", ["fera", "ferait", "feras", "faira"], "fera",
                     "Faire is irregular: fer- + a → fera."),
                    ("Nous ___ en France l'année prochaine.", ["irons", "allerons", "aillons", "irrons"], "irons",
                     "Aller is irregular: ir- + ons → irons."),
                    ("Tu ___ le résultat demain.", ["sauras", "saurais", "sauras", "savoir"], "sauras",
                     "Savoir is irregular: saur- + as → sauras."),
                    ("Ils ___ à la réunion.", ["viendront", "vienneront", "venront", "veniront"], "viendront",
                     "Venir is irregular: viendr- + ont → viendront."),
                    ("Si tu travailles, tu ___.", ["réussiras", "réussis", "réussirais", "réussiras"], "réussiras",
                     "si + present → future in result clause."),
                ]),
        "ex2": ("Exercise 2 — Translate into French",
                "Type the French sentence.",
                [
                    ("I will speak French.", "Je parlerai français.", "parler: parler + ai."),
                    ("She will finish tomorrow.", "Elle finira demain.", "finir: finir + a."),
                    ("We will be there.", "Nous serons là.", "être irregular: ser- + ons."),
                    ("They (m) will come.", "Ils viendront.", "venir irregular: viendr- + ont."),
                    ("If you study, you will pass.", "Si tu étudies, tu réussiras.", "si + present + future."),
                ]),
        "ex3": ("Exercise 3 — Spot the mistake",
                "Which sentence is correct?",
                [
                    ("'She will have' in French:", ["Elle aura.", "Elle avera.", "Elle aurait.", "Elle avoir."], "Elle aura.",
                     "Avoir irregular: aur- + a → aura."),
                    ("'If he works, he will succeed':", ["Si il travaillera, il réussira.", "Si il travaille, il réussira.", "Si il travaille, il réussirait.", "Si il travaillera, il réussit."], "Si il travaille, il réussira.",
                     "si + present + future (never si + future)."),
                    ("'We will go to Paris':", ["Nous allerons à Paris.", "Nous irons à Paris.", "Nous irrons à Paris.", "Nous allions à Paris."], "Nous irons à Paris.",
                     "Aller irregular: ir- + ons → irons."),
                    ("'They will be able to come':", ["Ils pourraient venir.", "Ils pourront venir.", "Ils pouveront venir.", "Ils peuvent venir."], "Ils pourront venir.",
                     "Pouvoir irregular: pourr- + ont → pourront."),
                ]),
        "game_desc": "Master the French future simple — regular endings and irregular stems.",
        "items": [
            ("fut1", "je parlerai", "I will speak", "will speak", "Demain, je parlerai au directeur.", "Complète: Je ___ demain. (will speak)", "parlerai"),
            ("fut2", "tu finiras", "you will finish", "will finish", "Tu finiras tes devoirs avant le dîner.", "Complète: Tu ___ à 18h. (will finish)", "finiras"),
            ("fut3", "il / elle sera", "he / she will be", "will be", "Elle sera médecin dans dix ans.", "Complète: Il ___ là. (will be)", "sera"),
            ("fut4", "nous irons", "we will go", "will go", "Nous irons en France l'été prochain.", "Complète: Nous ___ à Paris. (will go)", "irons"),
            ("fut5", "ils feront", "they will do / make", "will do", "Ils feront un voyage en Espagne.", "Complète: Ils ___ leurs devoirs. (will do)", "feront"),
            ("fut6", "j'aurai", "I will have", "will have", "J'aurai plus de temps la semaine prochaine.", "Complète: J'___ le temps. (will have)", "aurai"),
            ("fut7", "elle viendra", "she will come", "will come", "Elle viendra à la fête samedi.", "Complète: Il ___ demain. (will come)", "viendra"),
            ("fut8", "si + présent → futur", "if…, …will", "if clause", "Si tu travailles, tu réussiras.", "Complète: Si elle vient, on ___ ensemble. (will eat, manger)", "mangera"),
        ],
    },

    # ------------------------------------------------------------------ G10
    "comparative-superlative": {
        "level": "a2", "section": "grammar", "num": "G10",
        "short": "Comparative & Superlative",
        "title": "Comparative & Superlative",
        "subtitle": "plus…que, moins…que, le plus/moins…",
        "slides": [
            ("The Comparative",
             "To compare two things in French, use <strong>plus…que</strong> (more than), <strong>moins…que</strong> (less than), or <strong>aussi…que</strong> (as…as).",
             "<em>Paris est plus grand que Lyon.</em> — Paris is bigger than Lyon.<br>"
             "<em>Ce film est moins intéressant que l'autre.</em> — This film is less interesting.<br>"
             "<em>Elle est aussi intelligente que lui.</em> — She is as intelligent as him.<br>"
             "The adjective agrees with the noun it describes."),
            ("Comparative — Irregular Forms",
             "Some adjectives have irregular comparative forms.",
             "<em>bon(ne)</em> → <em>meilleur(e)</em> (NOT ~~plus bon~~)<br>"
             "<em>mauvais(e)</em> → <em>pire</em> OR <em>plus mauvais(e)</em><br>"
             "<em>petit(e)</em> → <em>plus petit(e)</em> OR <em>moindre</em> (lesser, abstract)<br><br>"
             "<em>Ce restaurant est meilleur que l'autre.</em><br>"
             "<em>Cette situation est pire qu'avant.</em>"),
            ("The Superlative — Most / Least",
             "Use <strong>le/la/les + plus/moins + adjective</strong> for the superlative.",
             "<em>C'est le film le plus intéressant.</em> — It's the most interesting film.<br>"
             "<em>Elle est la plus grande de la classe.</em> — She is the tallest in the class.<br>"
             "<em>C'est le moins cher.</em> — It's the cheapest (least expensive).<br>"
             "The article (le/la/les) agrees with the noun."),
            ("Superlative — Irregular and Position",
             "Adjectives that normally come before the noun keep that position in the superlative.",
             "<em>le meilleur restaurant</em> — the best restaurant (meilleur before noun)<br>"
             "<em>la pire décision</em> — the worst decision<br>"
             "For adjectives that follow the noun:<br>"
             "<em>l'étudiante la plus intelligente</em> — the most intelligent student<br>"
             "(the article repeats after the noun)"),
            ("Quick Summary",
             "Comparison patterns at a glance.",
             "• Comparative: <em>plus/moins/aussi + adj. + que</em>.<br>"
             "• Superlative: <em>le/la/les + plus/moins + adj.</em><br>"
             "• bon → <strong>meilleur</strong>; mauvais → <strong>pire</strong>.<br>"
             "• After <em>le plus / la plus</em>, use <em>de</em> for 'in a group':<br>"
             "  <em>le plus grand de la classe</em> — the tallest in the class."),
        ],
        "traps": [
            ("better (adj.)", "meilleur(e)", "Never 'plus bon' — use meilleur."),
            ("the most interesting film", "le film le plus intéressant", "Article + noun + le + plus + adj. when adj. follows noun."),
            ("the best restaurant", "le meilleur restaurant", "Meilleur goes before noun like bon."),
            ("the tallest in the class", "le plus grand de la classe", "Use de after superlative, not dans."),
        ],
        "summary": [
            ("more than", "plus + adj. + que", "Il est plus grand que moi."),
            ("less than", "moins + adj. + que", "C'est moins cher que ça."),
            ("as … as", "aussi + adj. + que", "Elle est aussi forte que lui."),
            ("the most", "le/la/les + plus + adj.", "C'est le plus beau."),
            ("the least", "le/la/les + moins + adj.", "C'est le moins cher."),
            ("good → better", "bon → meilleur(e)", "Ce vin est meilleur que l'autre."),
            ("bad → worse", "mauvais → pire", "Cette situation est pire qu'avant."),
            ("superlative + group", "le plus + de", "le plus grand de la classe"),
        ],
        "ex1": ("Exercise 1 — Choose the correct comparative",
                "Select the right form.",
                [
                    ("Ce livre est ___ intéressant que l'autre. (more)", ["plus", "moins", "aussi", "meilleur"], "plus",
                     "More than → plus + adj. + que."),
                    ("Ce vin est ___. (better — irregular)", ["plus bon", "meilleur", "mieux", "bon"], "meilleur",
                     "Better (adj.) → meilleur; mieux is for adverbs/verbs."),
                    ("Elle est ___ grande que son frère. (as)", ["aussi", "plus", "moins", "autant"], "aussi",
                     "As … as → aussi + adj. + que."),
                    ("C'est le film ___ intéressant de l'année. (most)", ["plus", "le plus", "la plus", "mieux"], "le plus",
                     "Superlative: le + plus + adj."),
                    ("C'est la situation ___. (worst)", ["la plus mauvaise", "la pire", "la moins bonne", "Both A and B are correct"], "Both A and B are correct",
                     "La pire and la plus mauvaise are both correct for 'the worst'."),
                ]),
        "ex2": ("Exercise 2 — Translate into French",
                "Type the French sentence.",
                [
                    ("She is taller than him.", "Elle est plus grande que lui.", "plus + grande (agreed f.) + que."),
                    ("This restaurant is the best.", "Ce restaurant est le meilleur.", "Meilleur is the irregular superlative."),
                    ("He is as clever as she is.", "Il est aussi intelligent qu'elle.", "aussi + adj. + que; qu' before vowel."),
                    ("It's the cheapest in the shop.", "C'est le moins cher du magasin.", "moins + cher; de + le → du."),
                    ("This film is worse than that one.", "Ce film est pire que celui-là.", "pire = worse (irregular)."),
                ]),
        "ex3": ("Exercise 3 — Spot the mistake",
                "Pick the correct sentence.",
                [
                    ("'This wine is better':", ["Ce vin est plus bon.", "Ce vin est meilleur.", "Ce vin est plus bien.", "Ce vin est mieux."], "Ce vin est meilleur.",
                     "Better for an adjective → meilleur (never plus bon)."),
                    ("'the most intelligent student (f.)':", ["l'étudiante plus intelligente", "l'étudiante la plus intelligente", "la plus intelligente étudiante", "l'étudiante le plus intelligente"], "l'étudiante la plus intelligente",
                     "Adj. that follows noun: noun + la (agrees f.) + plus + adj."),
                    ("'He is less patient than she is':", ["Il est moins patient qu'elle.", "Il est moins patient que elle.", "Il est plus patient qu'elle.", "Il est le moins patient qu'elle."], "Il est moins patient qu'elle.",
                     "que → qu' before vowel; moins + adj. + qu'elle."),
                    ("'the tallest in the class':", ["le plus grand dans la classe", "le plus grand de la classe", "le grand de la classe", "plus grand que la classe"], "le plus grand de la classe",
                     "After superlative, use de (not dans) for 'in a group'."),
                ]),
        "game_desc": "Practice comparative and superlative forms in French.",
        "items": [
            ("comp1", "plus…que", "more … than", "bigger than", "Paris est plus grand que Lyon.", "Complète: Il est plus ___ que moi. (tall: grand)", "grand"),
            ("comp2", "moins…que", "less … than", "cheaper than", "C'est moins cher que dans l'autre magasin.", "Complète: Il est moins ___ qu'elle. (patient)", "patient"),
            ("comp3", "aussi…que", "as … as", "as fast as", "Elle court aussi vite que son frère.", "Complète: Il est aussi ___ qu'elle. (clever: intelligent)", "intelligent"),
            ("comp4", "meilleur(e)", "better (adj.)", "better", "Ce restaurant est meilleur que l'autre.", "Complète: Ce vin est ___. (better)", "meilleur"),
            ("comp5", "pire", "worse (adj.)", "worse", "Cette situation est pire qu'avant.", "Complète: C'est ___. (worse)", "pire"),
            ("comp6", "le/la plus + adj.", "the most + adj.", "the most", "C'est le film le plus intéressant.", "Complète: C'est la plus ___. (tall: grande)", "grande"),
            ("comp7", "le/la moins + adj.", "the least + adj.", "the least", "C'est le moins cher de tous.", "Complète: C'est le moins ___. (expensive: cher)", "cher"),
            ("comp8", "le plus + de", "superlative in a group", "tallest in", "Il est le plus grand de la classe.", "Complète: le plus grand ___ la famille. (in)", "de"),
        ],
    },

    # ------------------------------------------------------------------ G11
    "tout-meme-quelques": {
        "level": "a2", "section": "grammar", "num": "G11",
        "short": "Tout, Même, Quelques",
        "title": "Quantifiers — tout, même, quelques, chaque",
        "subtitle": "All, every, even, same, a few — common A2 quantifiers",
        "slides": [
            ("Tout — All / Every",
             "<em>Tout</em> is one of the most versatile French words. As an adjective, it agrees in gender and number.",
             "<table><tr><th></th><th>Masc. sg</th><th>Fem. sg</th><th>Masc. pl</th><th>Fem. pl</th></tr>"
             "<tr><td>tout</td><td>tout</td><td>toute</td><td>tous</td><td>toutes</td></tr></table>"
             "<em>tout le monde</em> — everyone (invariable)<br>"
             "<em>toute la famille</em> — the whole family<br>"
             "<em>tous les jours</em> — every day<br>"
             "<em>toutes les semaines</em> — every week"),
            ("Même — Same / Even",
             "<em>Même</em> has two uses: as an <strong>adjective</strong> (same) or as an <strong>adverb</strong> (even).",
             "<strong>Adjective (same) — before noun:</strong><br>"
             "<em>le même livre</em> — the same book<br>"
             "<em>la même chose</em> — the same thing<br><br>"
             "<strong>Adverb (even) — invariable:</strong><br>"
             "<em>Il travaille même le week-end.</em> — He works even on weekends.<br>"
             "<em>Elle ne mange même pas.</em> — She doesn't even eat."),
            ("Quelques — A Few",
             "<em>Quelques</em> is always plural and means <em>a few / some</em>.",
             "<em>J'ai quelques amis ici.</em> — I have a few friends here.<br>"
             "<em>Nous resterons quelques jours.</em> — We'll stay for a few days.<br>"
             "<em>Il reste quelques places.</em> — There are a few seats left.<br>"
             "Always plural — never use with singular nouns."),
            ("Chaque — Each / Every",
             "<em>Chaque</em> is always singular and means <em>each / every</em>. Always followed by a singular noun, no article needed.",
             "<em>chaque jour</em> — each/every day<br>"
             "<em>chaque élève</em> — each pupil<br>"
             "<em>chaque semaine</em> — every week<br>"
             "Contrast: <em>chaque jour</em> (each day, no article) vs. <em>tous les jours</em> (every day, with article)."),
            ("Quick Summary",
             "Quantifier quick reference.",
             "• <em>tout</em> agrees: tout/toute/tous/toutes.<br>"
             "• <em>tout le monde</em> = everyone (invariable, singular verb).<br>"
             "• <em>même</em> as adj. = same (before noun); as adverb = even (invariable).<br>"
             "• <em>quelques</em> = a few (always plural).<br>"
             "• <em>chaque</em> = each/every (always singular, no article)."),
        ],
        "traps": [
            ("every day", "tous les jours", "Tous + les + day (masculine plural); chaque jour also correct."),
            ("everyone", "tout le monde", "Invariable phrase — uses singular verb: tout le monde est là."),
            ("the same thing", "la même chose", "Même before noun = same; agrees with article."),
            ("a few days", "quelques jours", "Quelques = a few; always plural."),
        ],
        "summary": [
            ("tout (m.sg)", "tout le / tout mon", "tout le monde · tout mon temps"),
            ("toute (f.sg)", "toute la / toute ma", "toute la famille · toute la nuit"),
            ("tous (m.pl)", "tous les", "tous les jours · tous mes amis"),
            ("toutes (f.pl)", "toutes les", "toutes les semaines · toutes mes notes"),
            ("même (adj.)", "same (before noun)", "le même livre · la même chose"),
            ("même (adv.)", "even (invariable)", "Il travaille même le samedi."),
            ("quelques", "a few (always plural)", "quelques jours · quelques amis"),
            ("chaque", "each/every (always singular)", "chaque jour · chaque élève"),
        ],
        "ex1": ("Exercise 1 — Choose the right quantifier",
                "Select the correct form.",
                [
                    ("___ le monde était là. (everyone)", ["Tout", "Toute", "Tous", "Toutes"], "Tout",
                     "Tout le monde — invariable phrase."),
                    ("Elle travaille ___ les jours. (every)", ["tout", "toute", "tous", "chaque"], "tous",
                     "Tous les jours — masculine plural."),
                    ("J'ai ___ amis ici. (a few)", ["quelque", "quelques", "chaque", "tout"], "quelques",
                     "Quelques = a few, always plural."),
                    ("___ élève doit rendre son devoir. (each)", ["Chaque", "Quelques", "Tous les", "Tout"], "Chaque",
                     "Chaque = each, always singular."),
                    ("C'est le ___ problème. (same)", ["mêmes", "même", "tout", "quelques"], "même",
                     "Même before noun = same."),
                ]),
        "ex2": ("Exercise 2 — Translate into French",
                "Type the French phrase.",
                [
                    ("every week", "toutes les semaines", "Semaines is feminine plural → toutes les."),
                    ("everyone is here", "tout le monde est là", "Invariable — singular verb."),
                    ("a few days", "quelques jours", "Quelques — always plural."),
                    ("each student", "chaque étudiant", "Chaque — always singular, no article."),
                    ("the same book", "le même livre", "Même before noun = same."),
                ]),
        "ex3": ("Exercise 3 — Spot the mistake",
                "Which sentence is correct?",
                [
                    ("'Every day' in French:", ["tout les jours", "tous les jours", "toutes les jours", "chaque les jours"], "tous les jours",
                     "Jour is masculine plural → tous les jours."),
                    ("'Everyone is happy':", ["Tout le monde sont contents.", "Tout le monde est content.", "Tous le monde est content.", "Tout les mondes est content."], "Tout le monde est content.",
                     "Tout le monde = invariable phrase + singular verb."),
                    ("'I have a few ideas':", ["J'ai quelque idées.", "J'ai quelques idées.", "J'ai chaque idée.", "J'ai tout idées."], "J'ai quelques idées.",
                     "Quelques — always plural (-s)."),
                    ("'She even works on Sundays':", ["Elle même travaille le dimanche.", "Elle travaille même le dimanche.", "Elle travaille le même dimanche.", "Elle travaille le dimanche même."], "Elle travaille même le dimanche.",
                     "Même as adverb (even) — placed before the thing being emphasized."),
                ]),
        "game_desc": "Master tout, même, quelques, and chaque in context.",
        "items": [
            ("qt1", "tout le monde", "everyone", "everyone", "Tout le monde est prêt pour la réunion.", "Complète: ___ le monde est là. (everyone)", "Tout"),
            ("qt2", "tous les jours", "every day", "daily", "Je fais du sport tous les jours.", "Complète: ___ les jours. (every)", "tous"),
            ("qt3", "toute la famille", "the whole family", "whole family", "Toute la famille est réunie pour Noël.", "Complète: ___ la nuit. (the whole)", "toute"),
            ("qt4", "même (same)", "same (adj.)", "same", "On a lu le même livre en cours.", "Complète: C'est la ___ chose. (same)", "même"),
            ("qt5", "même (even)", "even (adverb)", "even", "Il travaille même le week-end.", "Complète: Elle ___ travaille le dimanche. (even)", "même"),
            ("qt6", "quelques", "a few", "a few", "J'ai quelques questions à te poser.", "Complète: ___ jours plus tard. (a few)", "quelques"),
            ("qt7", "chaque", "each / every (singular)", "each", "Chaque élève doit faire ses devoirs.", "Complète: ___ semaine. (each)", "chaque"),
            ("qt8", "toutes les semaines", "every week (f.pl.)", "every week", "Elle appelle ses parents toutes les semaines.", "Complète: ___ les semaines. (every, f.)", "toutes"),
        ],
    },

    # ------------------------------------------------------------------ G12
    "faux-amis-a2": {
        "level": "a2", "section": "grammar", "num": "G12",
        "short": "Faux Amis — A2",
        "title": "Faux Amis — False Friends at A2",
        "subtitle": "More words that look English but mean something different",
        "slides": [
            ("False Friends You'll Meet at A2",
             "At A2 you read more French and hit a new set of <em>faux amis</em>. These are trickier because they appear in everyday contexts.",
             "<em>assister à</em> — to attend ≠ to assist<br>"
             "<em>sensible</em> — sensitive ≠ sensible<br>"
             "<em>sympathique</em> — friendly/nice ≠ sympathetic<br>"
             "Don't trust looks — always check meaning in context."),
            ("Faux Amis Cluster 1 — Feelings and Character",
             "False friends about people and personalities.",
             "<em>sensible</em> — sensitive (NOT sensible — use <em>raisonnable / sensé</em>)<br>"
             "<em>sympathique</em> — friendly / nice (NOT sympathetic — use <em>compatissant</em>)<br>"
             "<em>décevoir</em> — to disappoint (NOT to deceive — use <em>tromper</em>)<br>"
             "<em>blesser</em> — to injure (NOT to bless — use <em>bénir</em>)"),
            ("Faux Amis Cluster 2 — Places and Objects",
             "False friends in everyday environments.",
             "<em>la pièce</em> — room OR coin (NOT piece/bit — use <em>morceau</em>)<br>"
             "<em>le collège</em> — secondary school (NOT college/university — use <em>université</em>)<br>"
             "<em>le lycée</em> — sixth-form / high school (NOT lycée)<br>"
             "<em>le journal</em> — newspaper / diary (NOT journal as diary always — both OK)"),
            ("Faux Amis Cluster 3 — Actions",
             "Verbs that trap English speakers.",
             "<em>demander</em> — to ask (NOT to demand — use <em>exiger</em>)<br>"
             "<em>introduire</em> — to insert / put in (NOT to introduce a person — use <em>présenter</em>)<br>"
             "<em>prétendre</em> — to claim / to maintain (NOT to pretend — use <em>faire semblant</em>)<br>"
             "<em>réaliser</em> — to carry out / to achieve (NOT to realise mentally — use <em>se rendre compte</em>)"),
            ("Faux Amis Cluster 4 — Everyday Mix",
             "Mixed set of common A2 traps.",
             "<em>éventuellement</em> — possibly / perhaps (NOT eventually — use <em>finalement</em>)<br>"
             "<em>large</em> — wide (NOT large as size — use <em>grand</em>)<br>"
             "<em>sensé</em> — sensible / rational (NOT sensitive — use <em>sensible</em>)<br>"
             "<em>urgent</em> — (same meaning — NOT an error, but note: <em>les urgences</em> = A&amp;E in hospital)<br>"
             "<em>les chips</em> — crisps (NOT chips as in chips = <em>les frites</em>)"),
            ("Quick Summary Table",
             "A2 faux amis at a glance.",
             "<table style='font-size:.82em'><tr><th>Faux ami</th><th>French meaning</th><th>Looks like</th><th>Correct French</th></tr>"
             "<tr><td>sensible</td><td>sensitive</td><td>sensible</td><td>raisonnable</td></tr>"
             "<tr><td>sympathique</td><td>friendly/nice</td><td>sympathetic</td><td>compatissant</td></tr>"
             "<tr><td>décevoir</td><td>to disappoint</td><td>to deceive</td><td>tromper</td></tr>"
             "<tr><td>demander</td><td>to ask</td><td>to demand</td><td>exiger</td></tr>"
             "<tr><td>éventuellement</td><td>possibly</td><td>eventually</td><td>finalement</td></tr>"
             "<tr><td>large</td><td>wide</td><td>large (big)</td><td>grand</td></tr>"
             "<tr><td>prétendre</td><td>to claim</td><td>to pretend</td><td>faire semblant</td></tr>"
             "<tr><td>réaliser</td><td>to carry out</td><td>to realise</td><td>se rendre compte</td></tr>"
             "</table>"),
        ],
        "traps": [
            ("She is very sensitive", "Elle est très sensible", "sensible in French = sensitive, not sensible."),
            ("He is friendly / nice", "Il est sympathique", "sympathique = nice/friendly, not sympathetic."),
            ("I'll ask the teacher", "Je demanderai au professeur", "demander = to ask (not demand)."),
            ("eventually", "finalement", "éventuellement = possibly; eventually = finalement."),
        ],
        "summary": [
            ("sensible", "sensitive (not 'sensible')", "Elle est sensible à la critique."),
            ("raisonnable", "sensible/reasonable", "Sois raisonnable !"),
            ("sympathique", "friendly/nice (not sympathetic)", "Il est très sympathique."),
            ("décevoir", "to disappoint (not deceive)", "Ce film m'a déçu."),
            ("demander", "to ask (not demand)", "Je lui ai demandé l'heure."),
            ("éventuellement", "possibly (not eventually)", "Je pourrai éventuellement venir."),
            ("large", "wide (not large/big)", "La rue est très large."),
            ("prétendre", "to claim (not pretend)", "Il prétend être médecin."),
        ],
        "ex1": ("Exercise 1 — What does it mean?",
                "Choose the correct English translation.",
                [
                    ("sensible (French)", ["sensible", "sensitive", "reasonable", "Both B and C — depends on context"],
                     "sensitive", "sensible in French = sensitive; reasonable = raisonnable."),
                    ("éventuellement", ["eventually", "possibly / perhaps", "frequently", "never"],
                     "possibly / perhaps", "éventuellement = possibly; eventually = finalement."),
                    ("demander", ["to demand", "to ask", "to require", "to need"],
                     "to ask", "demander = to ask; to demand = exiger."),
                    ("large", ["large (big)", "wide", "long", "heavy"],
                     "wide", "large in French = wide; big = grand."),
                    ("prétendre", ["to pretend", "to claim / maintain", "to tend", "to intend"],
                     "to claim / maintain", "prétendre = to claim; to pretend = faire semblant."),
                ]),
        "ex2": ("Exercise 2 — Translate correctly",
                "Type the correct French word or phrase.",
                [
                    ("eventually (at the end)", "finalement", "éventuellement = possibly; eventually = finalement."),
                    ("He asks for help.", "Il demande de l'aide.", "demander = to ask."),
                    ("She is very sensitive.", "Elle est très sensible.", "sensible = sensitive in French."),
                    ("to realise (mentally)", "se rendre compte", "réaliser = to carry out; realise mentally = se rendre compte."),
                    ("a wide street", "une rue large", "large = wide; adj. after noun."),
                ]),
        "ex3": ("Exercise 3 — Choose correctly",
                "Pick the right option.",
                [
                    ("'He is friendly' in French:", ["Il est sympathétique.", "Il est sympathique.", "Il est sensible.", "Il est compatible."],
                     "Il est sympathique.", "sympathique = friendly/nice."),
                    ("'She disappointed me':", ["Elle m'a décevée.", "Elle m'a déçue.", "Elle m'a trompée.", "Elle m'a déçu."],
                     "Elle m'a déçue.", "décevoir PC: déçu + -e for fem. direct object (me)."),
                    ("'He claims to be a doctor':", ["Il prétend être médecin.", "Il fait semblant d'être médecin.", "Il réalise être médecin.", "Both A and B correct."],
                     "Il prétend être médecin.", "prétendre = to claim."),
                    ("'The road is wide':", ["La route est grande.", "La route est large.", "La route est large et grande.", "Both A and B correct."],
                     "La route est large.", "large = wide; grande = big/tall."),
                ]),
        "game_desc": "Test your knowledge of A2-level false friends — words that look English but aren't.",
        "items": [
            ("fa1", "sensible", "sensitive (not sensible)", "sensitive", "Elle est très sensible aux critiques.", "sensible = sensitive (NOT ___)", "sensible (en)"),
            ("fa2", "sympathique", "friendly / nice (not sympathetic)", "friendly", "Il est sympathique et toujours de bonne humeur.", "sympathique = nice (NOT ___)", "sympathetic"),
            ("fa3", "décevoir", "to disappoint (not deceive)", "to disappoint", "Ce film m'a vraiment déçu.", "décevoir = to disappoint (NOT to ___)", "deceive"),
            ("fa4", "demander", "to ask (not demand)", "to ask", "Je lui ai demandé son numéro.", "demander = to ask (NOT to ___)", "demand"),
            ("fa5", "éventuellement", "possibly (not eventually)", "possibly", "Je pourrai éventuellement venir.", "éventuellement = possibly (NOT ___)", "eventually"),
            ("fa6", "large", "wide (not large/big)", "wide", "La rue est très large à cet endroit.", "large = wide (NOT ___)", "large/big"),
            ("fa7", "prétendre", "to claim (not pretend)", "to claim", "Il prétend avoir raison, mais je ne crois pas.", "prétendre = to claim (NOT to ___)", "pretend"),
            ("fa8", "réaliser", "to carry out / achieve (not realise)", "to achieve", "Elle a réalisé son rêve.", "réaliser = to achieve (NOT to ___)", "realise"),
        ],
    },
}
