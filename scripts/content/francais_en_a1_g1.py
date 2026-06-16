"""francais-en A1 Grammar G01–G06 — French for English speakers"""

CHAPTERS = {
    "articles-and-gender": {
        "level": "a1",
        "section": "grammar",
        "num": "G01",
        "short": "Articles and Gender",
        "title": "Articles and Gender — Les Articles et le Genre",
        "subtitle": "Every French noun is masculine or feminine — and that changes everything",
        "slides": [
            ("The Big Difference: Grammatical Gender",
             "English has no grammatical gender. French does — every noun is either <em>masculine</em> or <em>feminine</em>, and the article (the/a) must match. This affects articles, adjectives, and pronouns throughout French.",
             '<table class="sum-table"><thead><tr><th>English</th><th>Masculine</th><th>Feminine</th></tr></thead><tbody>'
             '<tr><td>the</td><td><b>le</b> livre (the book)</td><td><b>la</b> table (the table)</td></tr>'
             '<tr><td>a / an</td><td><b>un</b> café (a coffee)</td><td><b>une</b> maison (a house)</td></tr>'
             '<tr><td>the (plural)</td><td colspan="2"><b>les</b> livres / les tables</td></tr>'
             '</tbody></table>'),
            ("Definite Articles: le, la, l', les",
             'Use <b>le</b> before masculine nouns, <b>la</b> before feminine nouns, <b>l\'</b> before any noun starting with a vowel or silent h, and <b>les</b> for all plural nouns.',
             '<ul class="slide-list"><li><b>le</b> garçon (the boy) — masc.</li>'
             '<li><b>la</b> fille (the girl) — fem.</li>'
             '<li><b>l\'</b>ami (the friend, m.) / <b>l\'</b>amie (the friend, f.) — vowel rule</li>'
             '<li><b>l\'</b>homme (the man) — silent h counts as a vowel</li>'
             '<li><b>les</b> garçons / <b>les</b> filles — plural (no gender distinction)</li></ul>'),
            ("Indefinite Articles: un, une, des",
             'English uses <em>a/an</em> for singular indefinite nouns and nothing (or <em>some</em>) for plural. French uses <b>un</b> (masc.), <b>une</b> (fem.), and <b>des</b> (plural).',
             '<ul class="slide-list"><li><b>un</b> chat — a cat (masc.)</li>'
             '<li><b>une</b> fleur — a flower (fem.)</li>'
             '<li><b>des</b> chats — (some) cats</li>'
             '<li><b>des</b> fleurs — (some) flowers</li></ul>'
             '<p>Note: <em>des</em> often translates as nothing in English: <b>des pommes</b> = "apples" (not "some apples").</p>'),
            ("How to Know the Gender",
             'Gender must be learned with each noun. But some endings are reliable clues:',
             '<table class="sum-table"><thead><tr><th>Usually Masculine</th><th>Usually Feminine</th></tr></thead><tbody>'
             '<tr><td>-age (le village)</td><td>-tion (la nation)</td></tr>'
             '<tr><td>-ment (le gouvernement)</td><td>-té (la liberté)</td></tr>'
             '<tr><td>-eau (le gâteau)</td><td>-ure (la voiture)</td></tr>'
             '<tr><td>-isme (le tourisme)</td><td>-eur (la couleur — mostly)</td></tr>'
             '</tbody></table>'
             '<p><strong>Tip:</strong> Always learn nouns with their article: not <em>chat</em> but <em>le chat</em>.</p>'),
            ("Contracted Articles: au, du, aux, des",
             '<em>de + le</em> and <em>à + le</em> always contract. <em>de la</em> and <em>à la</em> do NOT contract.',
             '<ul class="slide-list"><li><b>à + le</b> → <b>au</b>: Je vais au cinéma (I\'m going to the cinema)</li>'
             '<li><b>à + les</b> → <b>aux</b>: Je parle aux étudiants (I speak to the students)</li>'
             '<li><b>de + le</b> → <b>du</b>: le livre du professeur (the teacher\'s book)</li>'
             '<li><b>de + les</b> → <b>des</b>: le livre des enfants (the children\'s book)</li>'
             '<li>No contraction: <b>à la</b> gare, <b>de la</b> ville, <b>à l\'</b>hôtel</li></ul>'),
        ],
        "traps": [
            ("le problem", "le problème", "Borrowed words keep their French gender. <em>Problème</em> is masculine."),
            ("un/une with professions", "Il est médecin (no article)", "After <em>être</em> with professions, drop the article: <em>Elle est professeure</em>, not <em>une professeure</em>."),
            ("la people", "les gens", "<em>Gens</em> (people) is always plural. Never use <em>la people</em>."),
            ("le/la + vowel", "l'ami, l'école", "Before a vowel or silent h, both <em>le</em> and <em>la</em> become <em>l'</em>. You can't tell gender from <em>l'</em> alone — must memorise."),
        ],
        "summary": [
            ("Definite masc.", "le + noun", "le livre (the book)"),
            ("Definite fem.", "la + noun", "la table (the table)"),
            ("Definite (vowel)", "l' + noun", "l'ami (the friend)"),
            ("Definite plural", "les + noun", "les livres (the books)"),
            ("Indefinite masc.", "un + noun", "un chat (a cat)"),
            ("Indefinite fem.", "une + noun", "une maison (a house)"),
            ("Indefinite plural", "des + noun", "des chats (cats)"),
            ("Contraction à+le", "au", "Je vais au cinéma"),
        ],
        "ex1": (
            "Choosing the Right Article",
            "Choose the correct definite article (le, la, l', les) for each noun.",
            [
                ("___ chat (m.)", ["le", "la", "l'", "les"], "le", "Chat is masculine, so we use <em>le</em>."),
                ("___ école (f.)", ["le", "la", "l'", "les"], "l'", "École starts with a vowel, so <em>le/la</em> → <em>l'</em>."),
                ("___ hôtel (m.)", ["le", "la", "l'", "les"], "l'", "Hôtel has a silent h, so we use <em>l'</em> (treats silent h like a vowel)."),
                ("___ maisons (f. pl.)", ["le", "la", "l'", "les"], "les", "Plural nouns always take <em>les</em> regardless of gender."),
                ("___ livre (m.)", ["le", "la", "l'", "les"], "le", "Livre is masculine and starts with a consonant, so <em>le</em>."),
                ("___ amie (f.)", ["le", "la", "l'", "les"], "l'", "Amie starts with a vowel, so <em>la</em> → <em>l'</em>."),
            ]
        ),
        "ex2": (
            "Indefinite Articles",
            "Fill in the blank with un, une, or des.",
            [
                ("J'ai ___ chien. (I have a dog — m.)", "un", "Chien is masculine → <em>un</em>."),
                ("Elle mange ___ pomme. (She eats an apple — f.)", "une", "Pomme is feminine → <em>une</em>."),
                ("Nous avons ___ enfants. (We have children — pl.)", "des", "Plural → <em>des</em>."),
                ("C'est ___ appartement. (It's a flat — m.)", "un", "Appartement is masculine → <em>un</em>."),
                ("Il y a ___ fleurs. (There are flowers — pl.)", "des", "Plural → <em>des</em>."),
            ]
        ),
        "ex3": (
            "Contractions",
            "Choose the correct contracted or full form.",
            [
                ("Je vais ___ marché. (I'm going to the market — m.)", ["au", "à le", "à la", "du"], "au", "<em>à + le</em> → <em>au</em>. Never write <em>à le</em>."),
                ("Le livre ___ professeur. (The teacher's book — m.)", ["du", "de le", "de la", "des"], "du", "<em>de + le</em> → <em>du</em>."),
                ("Je parle ___ enfants. (I speak to the children — pl.)", ["aux", "à les", "au", "des"], "aux", "<em>à + les</em> → <em>aux</em>."),
                ("Elle vient ___ école. (She comes from school — f.)", ["de l'", "du", "de la", "des"], "de l'", "École starts with a vowel: <em>de l'école</em>. No contraction with feminine/vowel."),
                ("Les photos ___ vacances. (Holiday photos — f.pl.)", ["des", "du", "de la", "de les"], "des", "<em>de + les</em> → <em>des</em>."),
            ]
        ),
        "game_desc": "Master French articles and grammatical gender",
        "items": [
            ("le", "le", "definite article for masculine singular nouns", "masc. 'the'", "Le chat dort. (The cat sleeps.)", "le = definite article for masculine nouns", "le"),
            ("la", "la", "definite article for feminine singular nouns", "fem. 'the'", "La maison est grande. (The house is big.)", "la = definite article for feminine nouns", "la"),
            ("l-apos", "l'", "definite article before vowel or silent h", "elided 'the'", "L'ami arrive. (The friend is arriving.)", "l' = le/la before vowel or silent h", "l'"),
            ("les", "les", "definite article for all plural nouns", "plural 'the'", "Les livres sont ici. (The books are here.)", "les = definite article for plural nouns", "les"),
            ("un", "un", "indefinite article for masculine singular nouns", "masc. 'a'", "J'ai un chat. (I have a cat.)", "un = indefinite article for masculine nouns", "un"),
            ("une", "une", "indefinite article for feminine singular nouns", "fem. 'a'", "C'est une fleur. (It's a flower.)", "une = indefinite article for feminine nouns", "une"),
            ("des", "des", "indefinite article for all plural nouns", "plural (some)", "Il a des amis. (He has friends.)", "des = indefinite article for plural nouns", "des"),
            ("au", "au", "contraction of à + le before masculine nouns", "à + le", "Je vais au cinéma. (I'm going to the cinema.)", "au = à + le (contraction)", "au"),
        ],
    },

    "subject-pronouns-and-etre": {
        "level": "a1",
        "section": "grammar",
        "num": "G02",
        "short": "Subject Pronouns and Être",
        "title": "Subject Pronouns and Être — Les Pronoms Sujets et Être",
        "subtitle": "French has 8 subject pronouns and the verb être (to be) is irregular from the start",
        "slides": [
            ("The 8 Subject Pronouns",
             "French has more subject pronouns than English. The key additions are <em>tu</em> (informal you, singular) vs <em>vous</em> (formal or plural), and <em>ils/elles</em> (they — gender-matched).",
             '<table class="sum-table"><thead><tr><th>French</th><th>English</th><th>Notes</th></tr></thead><tbody>'
             '<tr><td><b>je</b></td><td>I</td><td>→ j\' before vowel</td></tr>'
             '<tr><td><b>tu</b></td><td>you (1 person, informal)</td><td>friends, family, children</td></tr>'
             '<tr><td><b>il / elle</b></td><td>he / she / it</td><td>also replaces masculine/feminine nouns</td></tr>'
             '<tr><td><b>nous</b></td><td>we</td><td>formal; spoken French often uses <em>on</em></td></tr>'
             '<tr><td><b>vous</b></td><td>you (formal OR plural)</td><td>singular polite or any group</td></tr>'
             '<tr><td><b>ils / elles</b></td><td>they</td><td>ils = mixed or all-male; elles = all-female</td></tr>'
             '</tbody></table>'),
            ("Tu vs Vous",
             'This distinction doesn\'t exist in modern English but is crucial in French.',
             '<ul class="slide-list">'
             '<li><b>tu</b> — talking to a friend, family member, child, pet, or equal in informal context</li>'
             '<li><b>vous</b> — talking to a stranger, someone older, an authority figure, your boss, or to any group of 2+ people</li>'
             '<li>Using <em>tu</em> with a stranger can be rude. Using <em>vous</em> with a close friend is stilted.</li>'
             '<li>Young people often use <em>tu</em> more widely. In doubt: use <em>vous</em>.</li></ul>'),
            ("Être — To Be (Irregular)",
             "This is the most important verb to memorise. It's irregular — no pattern to follow.",
             '<table class="sum-table"><thead><tr><th>Pronoun</th><th>Être</th><th>English</th></tr></thead><tbody>'
             '<tr><td>je</td><td><b>suis</b></td><td>I am</td></tr>'
             '<tr><td>tu</td><td><b>es</b></td><td>you are</td></tr>'
             '<tr><td>il/elle/on</td><td><b>est</b></td><td>he/she/it is</td></tr>'
             '<tr><td>nous</td><td><b>sommes</b></td><td>we are</td></tr>'
             '<tr><td>vous</td><td><b>êtes</b></td><td>you are</td></tr>'
             '<tr><td>ils/elles</td><td><b>sont</b></td><td>they are</td></tr>'
             '</tbody></table>'),
            ("Using Être: Descriptions and Identities",
             'Être expresses identity, nationality, profession, origin, and descriptions.',
             '<ul class="slide-list">'
             '<li><b>Je suis</b> étudiant(e). — I am a student.</li>'
             '<li><b>Tu es</b> français(e)? — Are you French?</li>'
             '<li><b>Il est</b> médecin. — He is a doctor.</li>'
             '<li><b>Elle est</b> grande. — She is tall.</li>'
             '<li><b>Nous sommes</b> de Paris. — We are from Paris.</li>'
             '<li><b>Vous êtes</b> professeur? — Are you a teacher? (polite)</li>'
             '<li><b>Ils sont</b> fatigués. — They are tired.</li></ul>'
             '<p>⚠️ No article before professions: <em>Il est médecin</em>, NOT <em>Il est un médecin</em>.</p>'),
            ("On — The Informal We",
             'In everyday spoken French, <em>on</em> is used more often than <em>nous</em> for "we". It uses the same verb form as <em>il/elle</em>.',
             '<ul class="slide-list">'
             '<li><b>On est</b> en retard. — We\'re late. (everyday)</li>'
             '<li><b>Nous sommes</b> en retard. — We are late. (formal/written)</li>'
             '<li>On also means "one" / "people in general": <em>On parle français ici.</em> (French is spoken here.)</li>'
             '<li>On + verb = il/elle form: <em>on est, on parle, on va</em></li></ul>'),
        ],
        "traps": [
            ("I is always capital", "je (lowercase unless first word)", "In French, <em>je</em> is only capitalised at the start of a sentence."),
            ("ils for mixed groups", "ils sont (not elles)", "If a group has even one male in it, use <em>ils</em>. Only an all-female group uses <em>elles</em>."),
            ("No article with professions + être", "Il est médecin", "After <em>être</em>, professions take no article: <em>Elle est infirmière</em>, not <em>une infirmière</em>."),
            ("vous = singular polite", "Vous êtes Madame Dupont?", "<em>Vous</em> can refer to just one person if you're being formal or polite."),
        ],
        "summary": [
            ("I", "je / j'", "Je suis étudiant."),
            ("you (informal)", "tu", "Tu es français?"),
            ("he/she/it", "il / elle", "Il est grand. Elle est petite."),
            ("we (formal)", "nous", "Nous sommes de Lyon."),
            ("we (informal)", "on + il/elle verb", "On est contents."),
            ("you (formal/plural)", "vous", "Vous êtes professeur?"),
            ("they (m./mixed)", "ils", "Ils sont fatigués."),
            ("they (f.)", "elles", "Elles sont contentes."),
        ],
        "ex1": (
            "Être Conjugation",
            "Choose the correct form of être.",
            [
                ("Je ___ étudiant.", ["suis", "es", "est", "êtes"], "suis", "<em>Je suis</em> — first person singular of être."),
                ("Tu ___ fatigué?", ["suis", "es", "est", "sont"], "es", "<em>Tu es</em> — second person singular informal."),
                ("Elle ___ de Paris.", ["suis", "êtes", "est", "sommes"], "est", "<em>Elle est</em> — third person singular."),
                ("Nous ___ contents.", ["êtes", "sont", "sommes", "est"], "sommes", "<em>Nous sommes</em> — first person plural."),
                ("Vous ___ professeur?", ["suis", "êtes", "sont", "sommes"], "êtes", "<em>Vous êtes</em> — second person formal/plural."),
                ("Ils ___ en retard.", ["est", "sommes", "êtes", "sont"], "sont", "<em>Ils sont</em> — third person plural."),
            ]
        ),
        "ex2": (
            "Translate Using Être",
            "Translate these sentences into French.",
            [
                ("I am a student. (male)", "Je suis étudiant.", "Je suis + profession (no article, no agreement for male)."),
                ("She is French.", "Elle est française.", "Elle est + nationality (feminine form: français → française)."),
                ("We are tired. (spoken)", "On est fatigués.", "Spoken 'we' = on + il/elle form of être."),
                ("Are you a doctor? (polite)", "Vous êtes médecin?", "Polite = vous; profession has no article after être."),
                ("They are from Spain. (mixed group)", "Ils sont d'Espagne.", "Mixed group = ils; de + vowel → d'."),
            ]
        ),
        "ex3": (
            "Tu or Vous?",
            "Which pronoun would you use in each situation?",
            [
                ("Talking to your friend Marie.", ["tu", "vous", "il", "elle"], "tu", "Friends → informal → tu."),
                ("Addressing your French teacher.", ["tu", "vous", "on", "ils"], "vous", "Teacher = authority figure → vous."),
                ("Talking to two classmates.", ["tu", "vous", "nous", "ils"], "vous", "Two people = plural → vous."),
                ("Talking to a child.", ["vous", "tu", "ils", "on"], "tu", "Children → informal → tu."),
                ("Asking a stranger for directions.", ["tu", "vous", "ils", "on"], "vous", "Stranger → polite → vous."),
            ]
        ),
        "game_desc": "Master French subject pronouns and the verb être",
        "items": [
            ("je", "je / j'", "first-person singular subject pronoun: I", "moi", "Je suis content. (I am happy.)", "je = I (first person singular)", "je"),
            ("tu", "tu", "informal second-person singular: you (one person, familiar)", "toi (informal)", "Tu es français? (Are you French?)", "tu = you (1 person, informal)", "tu"),
            ("il-elle", "il / elle", "third-person singular: he / she / it", "him/her", "Il est grand. Elle est petite. (He is tall. She is small.)", "il = he, elle = she/it", "il"),
            ("nous", "nous", "first-person plural subject pronoun: we (formal/written)", "on (informal)", "Nous sommes de Paris. (We are from Paris.)", "nous = we (formal/written)", "nous"),
            ("vous", "vous", "second-person plural or formal singular: you", "polite you", "Vous êtes professeur? (Are you a teacher?)", "vous = you (formal or plural)", "vous"),
            ("ils-elles", "ils / elles", "third-person plural: they (ils = mixed/male, elles = all-female)", "them", "Ils sont fatigués. Elles sont contentes.", "ils = they (m./mixed), elles = they (f.)", "ils"),
            ("on", "on", "informal first-person plural in speech: we; also means 'one' / 'people'", "spoken we", "On est en retard. (We're late.)", "on = we (spoken) or one", "on"),
            ("suis", "suis", "form of être for je: am", "je suis", "Je suis étudiant. (I am a student.)", "suis = am (je form of être)", "suis"),
        ],
    },

    "present-tense-er-verbs": {
        "level": "a1",
        "section": "grammar",
        "num": "G03",
        "short": "Present Tense: -er Verbs",
        "title": "Present Tense: -er Verbs — Le Présent des Verbes en -er",
        "subtitle": "About 90% of French verbs end in -er and follow this one pattern",
        "slides": [
            ("The -er Verb Pattern",
             "Most French verbs end in <em>-er</em> in the infinitive (to + verb). To conjugate, drop the <em>-er</em> and add the endings. The endings are the same for ALL regular -er verbs.",
             '<table class="sum-table"><thead><tr><th>Pronoun</th><th>Ending</th><th>Parler (to speak)</th></tr></thead><tbody>'
             '<tr><td>je</td><td>-e</td><td>je parl<b>e</b></td></tr>'
             '<tr><td>tu</td><td>-es</td><td>tu parl<b>es</b></td></tr>'
             '<tr><td>il/elle/on</td><td>-e</td><td>il/elle parl<b>e</b></td></tr>'
             '<tr><td>nous</td><td>-ons</td><td>nous parl<b>ons</b></td></tr>'
             '<tr><td>vous</td><td>-ez</td><td>vous parl<b>ez</b></td></tr>'
             '<tr><td>ils/elles</td><td>-ent</td><td>ils/elles parl<b>ent</b></td></tr>'
             '</tbody></table>'
             '<p>⚠️ The endings -e, -es, -ent are all <strong>silent</strong> in speech. Only <b>-ons</b> and <b>-ez</b> are pronounced differently.</p>'),
            ("No Do-Support in French",
             'English uses <em>do/does/did</em> in questions and negatives. French does NOT have this. One verb form covers it all.',
             '<table class="sum-table"><thead><tr><th>English</th><th>French</th></tr></thead><tbody>'
             '<tr><td>I speak French.</td><td>Je parle français.</td></tr>'
             '<tr><td>I <em>do</em> speak French.</td><td>Je parle français. (same)</td></tr>'
             '<tr><td>Do you speak French?</td><td>Tu parles français? (same verb)</td></tr>'
             '<tr><td>She doesn\'t speak French.</td><td>Elle <em>ne</em> parle <em>pas</em> français. (see negation)</td></tr>'
             '</tbody></table>'),
            ("Common -er Verbs",
             "These high-frequency verbs all follow the same -er pattern:",
             '<ul class="slide-list">'
             '<li><b>parler</b> — to speak: je parle, tu parles…</li>'
             '<li><b>manger</b> — to eat: je mange, tu manges… (nous mangeons — spelling change)</li>'
             '<li><b>habiter</b> — to live (somewhere): j\'habite à Paris</li>'
             '<li><b>travailler</b> — to work: elle travaille</li>'
             '<li><b>aimer</b> — to like/love: j\'aime le café</li>'
             '<li><b>écouter</b> — to listen: vous écoutez</li>'
             '<li><b>regarder</b> — to watch: ils regardent</li>'
             '<li><b>jouer</b> — to play: on joue au foot</li></ul>'),
            ("Spelling Changes: -ger and -cer Verbs",
             'Some -er verbs have minor spelling changes to preserve pronunciation before <em>-ons</em>.',
             '<ul class="slide-list">'
             '<li><b>manger</b> (to eat): nous mang<b>e</b>ons (not mangerons — to keep soft g sound)</li>'
             '<li><b>voyager</b> (to travel): nous voyag<b>e</b>ons</li>'
             '<li><b>commencer</b> (to start): nous commen<b>ç</b>ons (cedilla to keep /s/ sound)</li>'
             '<li><b>placer</b> (to place): nous pla<b>ç</b>ons</li>'
             '<li>Only the <em>nous</em> form is affected — all others conjugate normally.</li></ul>'),
            ("The Present Tense Covers Three English Uses",
             'One French present form does the work of three English constructions:',
             '<table class="sum-table"><thead><tr><th>English</th><th>French</th></tr></thead><tbody>'
             '<tr><td>I speak French. (simple)</td><td rowspan="3">Je parle français.</td></tr>'
             '<tr><td>I am speaking French. (continuous)</td></tr>'
             '<tr><td>I do speak French. (emphatic)</td></tr>'
             '</tbody></table>'
             '<p>There is no equivalent of "I am speaking" in French — use the same present tense.</p>'),
        ],
        "traps": [
            ("je parlons", "je parle", "Only nous takes -ons. Je always takes -e."),
            ("I am speaking = je suis parlant", "je parle", "There's no present continuous in French. Use the simple present for both."),
            ("ils parlent = 3 syllables", "ils parlent = 2 syllables (parlent is silent -ent)", "The -ent ending is completely silent: <em>parlent</em> sounds like <em>parl</em>."),
            ("nous mangons", "nous mangeons", "With -ger verbs, add an <em>e</em> before -ons to keep the soft g sound."),
        ],
        "summary": [
            ("je", "-e (silent)", "je parle"),
            ("tu", "-es (silent)", "tu parles"),
            ("il/elle/on", "-e (silent)", "il parle"),
            ("nous", "-ons", "nous parlons"),
            ("vous", "-ez", "vous parlez"),
            ("ils/elles", "-ent (silent)", "ils parlent"),
            ("-ger verbs", "nous + -eons", "nous mangeons"),
            ("No do-support", "same verb form", "Tu parles? = Do you speak?"),
        ],
        "ex1": (
            "Conjugate the Verb",
            "Choose the correct form of the -er verb.",
            [
                ("Elle ___ (parler) français.", ["parle", "parles", "parlons", "parlent"], "parle", "Elle → -e ending: elle parl<em>e</em>."),
                ("Nous ___ (manger) ensemble.", ["mange", "mangeons", "mangez", "mangent"], "mangeons", "Nous + -ger verb: mang<em>eons</em> (adds e to keep soft g)."),
                ("Vous ___ (travailler) ici?", ["travaillons", "travaillez", "travaille", "travaillent"], "travaillez", "Vous → -ez: vous travaill<em>ez</em>."),
                ("Ils ___ (écouter) de la musique.", ["écoutez", "écoute", "écoutons", "écoutent"], "écoutent", "Ils → -ent (silent): ils écout<em>ent</em>."),
                ("J'___ (habiter) à Lyon.", ["habites", "habite", "habitons", "habitez"], "habite", "Je → -e: j'habit<em>e</em>."),
                ("Tu ___ (aimer) le chocolat?", ["aime", "aimez", "aimes", "aimions"], "aimes", "Tu → -es: tu aim<em>es</em>."),
            ]
        ),
        "ex2": (
            "Translate Using the Present",
            "Translate these sentences into French.",
            [
                ("I live in Paris.", "J'habite à Paris.", "Je + habiter → j'habite (je before vowel = j')."),
                ("She works a lot.", "Elle travaille beaucoup.", "Elle + travailler → elle travaille."),
                ("We watch TV. (formal)", "Nous regardons la télé.", "Nous + regarder → nous regardons."),
                ("Do you speak English? (informal)", "Tu parles anglais?", "Questions in French: same word order with rising intonation, or add ? at the end."),
                ("They play football. (mixed group)", "Ils jouent au football.", "Ils + jouer → ils jouent; au = à + le."),
            ]
        ),
        "ex3": (
            "Identify the Error",
            "Which sentence has a grammar mistake?",
            [
                ("Which is correct?", ["Je parle français.", "Je parles français.", "J'parle français.", "Je suis parle français."], "Je parle français.", "Je takes -e; no apostrophe unless before vowel; no 'suis' with action verbs."),
                ("Which is correct?", ["Nous mangons ensemble.", "Nous mangeons ensemble.", "Nous mangent ensemble.", "Nous mangeez ensemble."], "Nous mangeons ensemble.", "Nous + -ger: add e before -ons → mangeons."),
                ("Which means 'she is working'?", ["Elle est travaille.", "Elle travaille.", "Elle travaillant.", "Elle va travaillez."], "Elle travaille.", "No present continuous in French — use simple present."),
                ("Which is correct for 'they listen'?", ["Ils écoutez.", "Ils écoute.", "Ils écoutent.", "Ils écoutons."], "Ils écoutent.", "Ils → -ent (silent): écoutent."),
                ("Which correctly asks 'do you eat here?' (informal)", ["Tu mange ici?", "Tu manges ici?", "Tu mangez ici?", "Tu mangeons ici?"], "Tu manges ici?", "Tu → -es: tu manges."),
            ]
        ),
        "game_desc": "Master the French -er verb conjugation pattern",
        "items": [
            ("parler", "parler", "to speak (regular -er verb)", "dire, s'exprimer", "Je parle français. (I speak French.)", "parler = to speak → je parle, tu parles…", "parler"),
            ("manger", "manger", "to eat (spelling change: nous mangeons)", "dîner, déjeuner", "Nous mangeons ensemble. (We eat together.)", "manger = to eat → nous mangeons (spelling change)", "manger"),
            ("habiter", "habiter", "to live somewhere; to reside", "vivre, résider", "J'habite à Paris. (I live in Paris.)", "habiter = to live → j'habite (vowel)", "habiter"),
            ("aimer", "aimer", "to like; to love", "adorer, apprécier", "J'aime le café. (I like coffee.)", "aimer = to like/love → j'aime, tu aimes…", "aimer"),
            ("travailler", "travailler", "to work", "bosser (informal)", "Elle travaille beaucoup. (She works a lot.)", "travailler = to work → je travaille", "travailler"),
            ("regarder", "regarder", "to watch; to look at", "observer, voir", "Ils regardent la télé. (They watch TV.)", "regarder = to watch → nous regardons", "regarder"),
            ("no-do-support", "no do-support", "French has no do/does in questions or negatives", "même forme verbale", "Tu parles? = Do you speak? (same verb)", "French: no do-support — same verb form", "no do-support"),
            ("ent-silent", "-ent (silent)", "the ils/elles ending is completely silent", "silent ending", "ils parlent → sounds like 'ils parl'", "-ent = ils/elles ending — completely silent", "-ent"),
        ],
    },

    "negation": {
        "level": "a1",
        "section": "grammar",
        "num": "G04",
        "short": "Negation",
        "title": "Negation — La Négation",
        "subtitle": "French wraps negation around the verb with ne...pas",
        "slides": [
            ("The Sandwich Structure: ne...pas",
             'English puts "not" after the first auxiliary verb: <em>I do <u>not</u> speak</em>. French wraps the verb in a two-part structure: <b>ne</b> before the verb and <b>pas</b> after.',
             '<table class="sum-table"><thead><tr><th>Positive</th><th>Negative</th></tr></thead><tbody>'
             '<tr><td>Je parle français.</td><td>Je <b>ne</b> parle <b>pas</b> français.</td></tr>'
             '<tr><td>Elle travaille.</td><td>Elle <b>ne</b> travaille <b>pas</b>.</td></tr>'
             '<tr><td>Nous sommes là.</td><td>Nous <b>ne</b> sommes <b>pas</b> là.</td></tr>'
             '<tr><td>Tu aimes le café.</td><td>Tu <b>n\'</b>aimes <b>pas</b> le café.</td></tr>'
             '</tbody></table>'),
            ("Ne becomes n' before a vowel",
             '<em>Ne</em> elides to <em>n\'</em> before a verb beginning with a vowel or silent h.',
             '<ul class="slide-list">'
             '<li>Je <b>n\'</b>aime pas les épinards. (I don\'t like spinach.)</li>'
             '<li>Il <b>n\'</b>est pas là. (He isn\'t there.)</li>'
             '<li>Nous <b>n\'</b>habitons pas à Paris. (We don\'t live in Paris.)</li>'
             '<li>Elle <b>n\'</b>a pas de voiture. (She doesn\'t have a car.)</li></ul>'),
            ("Ne...pas in Spoken French",
             'In everyday spoken French, <em>ne</em> is very often dropped, leaving only <em>pas</em>. Only <em>pas</em> remains audible.',
             '<ul class="slide-list">'
             '<li>Written: Je <em>ne</em> sais <em>pas</em>. → Spoken: Je sais <em>pas</em>.</li>'
             '<li>Written: C\'est <em>ne</em> pas bon. → WRONG. The verb goes between ne and pas.</li>'
             '<li>For writing and formal speech, always use both <em>ne</em> and <em>pas</em>.</li></ul>'),
            ("Other Negative Structures",
             'Beyond <em>ne...pas</em>, French has other two-part negatives:',
             '<table class="sum-table"><thead><tr><th>Structure</th><th>Meaning</th><th>Example</th></tr></thead><tbody>'
             '<tr><td>ne...jamais</td><td>never</td><td>Je ne mange jamais de viande.</td></tr>'
             '<tr><td>ne...rien</td><td>nothing / not anything</td><td>Il ne dit rien.</td></tr>'
             '<tr><td>ne...plus</td><td>no longer / not any more</td><td>Elle ne travaille plus.</td></tr>'
             '<tr><td>ne...personne</td><td>nobody / no one</td><td>Je ne vois personne.</td></tr>'
             '</tbody></table>'),
            ("Negation with Indefinite Articles",
             'After a negation, <em>un</em>, <em>une</em>, and <em>des</em> change to <em>de</em> (or <em>d\'</em> before a vowel). <em>Le</em>, <em>la</em>, <em>les</em> do NOT change.',
             '<ul class="slide-list">'
             '<li>J\'ai <em>un</em> chien. → Je n\'ai pas <em>de</em> chien. (I don\'t have a dog.)</li>'
             '<li>J\'ai <em>des</em> amis. → Je n\'ai pas <em>d\'</em>amis. (I don\'t have friends.)</li>'
             '<li>J\'aime <em>le</em> café. → Je n\'aime pas <em>le</em> café. (article stays the same)</li></ul>'),
        ],
        "traps": [
            ("Je pas parle français.", "Je ne parle pas français.", "Both ne AND pas are required in standard French. Ne goes before the verb, pas after."),
            ("Je ne parle pas du café", "Je ne parle pas de café", "After negation, un/une/des → de. But le/la/les stay: Je n'aime pas le café."),
            ("Il n'est jamais pas là.", "Il n'est jamais là.", "Don't combine two negatives (jamais + pas). Use only one negative word after ne."),
            ("Je ne sais pas. (dropping ne in writing)", "Je ne sais pas.", "Dropping ne is common in speech, but in writing always include ne...pas."),
        ],
        "summary": [
            ("Basic negation", "ne + verb + pas", "Je ne parle pas."),
            ("Before vowel", "n' + verb + pas", "Je n'aime pas."),
            ("Never", "ne + verb + jamais", "Il ne mange jamais."),
            ("No longer", "ne + verb + plus", "Elle ne travaille plus."),
            ("Nothing", "ne + verb + rien", "Il ne dit rien."),
            ("After negation", "un/une/des → de/d'", "Je n'ai pas de voiture."),
            ("le/la/les stay", "no change", "Je n'aime pas le café."),
            ("Spoken French", "drop ne (informal)", "Je sais pas. (spoken only)"),
        ],
        "ex1": (
            "Building the Negative",
            "Choose the correct negative sentence.",
            [
                ("I don't speak Spanish.", ["Je parle pas espagnol.", "Je ne parle pas espagnol.", "Je pas parle espagnol.", "Ne je parle pas espagnol."], "Je ne parle pas espagnol.", "ne before verb + pas after: Je ne parle pas."),
                ("She doesn't like coffee.", ["Elle n'aime pas le café.", "Elle ne aime pas le café.", "Elle aime pas le café.", "Elle pas aime le café."], "Elle n'aime pas le café.", "Before vowel: ne → n'. Le/la/les don't change after negation."),
                ("We are not at home.", ["Nous ne sommes pas à la maison.", "Nous sommes pas à la maison.", "Nous pas sommes à la maison.", "Nous ne pas sommes à la maison."], "Nous ne sommes pas à la maison.", "ne + sommes + pas. Remember: ne before the conjugated verb."),
                ("He never eats meat.", ["Il ne jamais mange de viande.", "Il jamais mange de viande.", "Il ne mange jamais de viande.", "Il ne mange pas jamais de viande."], "Il ne mange jamais de viande.", "ne + verb + jamais. Don't combine jamais + pas."),
                ("I don't have a car.", ["Je n'ai pas une voiture.", "Je n'ai pas de voiture.", "Je ne ai pas de voiture.", "Je pas ai de voiture."], "Je n'ai pas de voiture.", "After negation: un/une → de. n' before vowel (ai starts with a)."),
            ]
        ),
        "ex2": (
            "Make It Negative",
            "Rewrite the sentence in the negative.",
            [
                ("Je mange une pizza.", "Je ne mange pas de pizza.", "ne...pas wraps the verb; une → de after negation."),
                ("Elle aime les épinards.", "Elle n'aime pas les épinards.", "n' before vowel (aime); les stays — le/la/les don't change."),
                ("Nous habitons à Londres.", "Nous n'habitons pas à Londres.", "n' before vowel (habitons)."),
                ("Ils ont des enfants.", "Ils n'ont pas d'enfants.", "n' before vowel (ont); des → de/d' before vowel."),
                ("Tu travailles le dimanche.", "Tu ne travailles pas le dimanche.", "ne...pas; le stays."),
            ]
        ),
        "ex3": (
            "Which Negative?",
            "Choose the negative structure that matches the English.",
            [
                ("I no longer work here.", ["Je ne travaille pas ici.", "Je ne travaille plus ici.", "Je ne travaille jamais ici.", "Je ne travaille rien ici."], "Je ne travaille plus ici.", "No longer = ne...plus."),
                ("She never eats breakfast.", ["Elle ne mange pas de petit-déjeuner.", "Elle mange jamais de petit-déjeuner.", "Elle ne mange jamais de petit-déjeuner.", "Elle ne mange rien de petit-déjeuner."], "Elle ne mange jamais de petit-déjeuner.", "Never = ne...jamais."),
                ("He says nothing.", ["Il ne dit pas.", "Il ne dit rien.", "Il ne dit jamais.", "Il ne dit plus."], "Il ne dit rien.", "Nothing = ne...rien."),
                ("We don't have any friends.", ["Nous n'avons pas les amis.", "Nous n'avons pas d'amis.", "Nous n'avons jamais d'amis.", "Nous n'avons pas des amis."], "Nous n'avons pas d'amis.", "Not any → ne...pas; des → d' after negation before vowel."),
                ("I don't see anyone.", ["Je ne vois pas.", "Je ne vois rien.", "Je ne vois personne.", "Je ne vois jamais."], "Je ne vois personne.", "No one / not anyone = ne...personne."),
            ]
        ),
        "game_desc": "Master French negation with ne...pas and related structures",
        "items": [
            ("ne-pas", "ne...pas", "basic negation: not", "pas (spoken)", "Je ne parle pas anglais. (I don't speak English.)", "ne...pas = wrap around verb for 'not'", "ne...pas"),
            ("n-apos", "n'...pas", "ne elides to n' before a vowel or silent h", "ne before vowel", "Il n'est pas là. (He isn't there.)", "n'...pas = ne...pas before vowel", "n'"),
            ("ne-jamais", "ne...jamais", "never; not ever", "jamais seul", "Elle ne mange jamais de viande. (She never eats meat.)", "ne...jamais = never", "jamais"),
            ("ne-plus", "ne...plus", "no longer; not any more", "plus", "Il ne travaille plus. (He doesn't work any more.)", "ne...plus = no longer", "plus"),
            ("ne-rien", "ne...rien", "nothing; not anything", "rien", "Je ne dis rien. (I say nothing.)", "ne...rien = nothing", "rien"),
            ("ne-personne", "ne...personne", "nobody; no one; not anyone", "personne", "Il ne voit personne. (He sees nobody.)", "ne...personne = nobody", "personne"),
            ("de-after-neg", "de / d' after negation", "un/une/des change to de/d' after a negation", "article change", "Je n'ai pas de voiture. (I don't have a car.)", "after negation: un/une/des → de/d'", "de"),
            ("le-la-les-stay", "le/la/les stay", "definite articles do not change after negation", "no change", "Je n'aime pas le café. (I don't like coffee.)", "after negation: le/la/les unchanged", "le/la/les"),
        ],
    },

    "questions": {
        "level": "a1",
        "section": "grammar",
        "num": "G05",
        "short": "Asking Questions",
        "title": "Asking Questions — Poser des Questions",
        "subtitle": "French has three ways to form yes/no questions — choose the right one for the context",
        "slides": [
            ("Three Ways to Ask Yes/No Questions",
             "English only uses inversion (<em>Is she here?</em>) or a tag (<em>She's here, isn't she?</em>). French has three full methods, ordered from informal to formal.",
             '<table class="sum-table"><thead><tr><th>Method</th><th>How</th><th>Register</th></tr></thead><tbody>'
             '<tr><td>Rising intonation</td><td>Statement + ? (voice rises)</td><td>spoken, informal</td></tr>'
             '<tr><td>Est-ce que…</td><td>Add est-ce que before statement</td><td>spoken and written, neutral</td></tr>'
             '<tr><td>Inversion</td><td>Swap verb and subject pronoun</td><td>formal, written</td></tr>'
             '</tbody></table>'),
            ("Method 1: Rising Intonation",
             "Simply say the statement with a rising voice at the end. In writing, add a question mark.",
             '<ul class="slide-list">'
             '<li>Tu parles français<b>?</b> (Do you speak French?)</li>'
             '<li>Elle est là<b>?</b> (Is she there?)</li>'
             '<li>Vous aimez le café<b>?</b> (Do you like coffee?)</li>'
             '<li>Very common in everyday speech — never wrong informally.</li></ul>'),
            ("Method 2: Est-ce que",
             '<em>Est-ce que</em> (literally "is it that") goes at the start of the sentence. The word order after it stays the same (subject + verb).',
             '<ul class="slide-list">'
             '<li><b>Est-ce que</b> tu parles français? (Do you speak French?)</li>'
             '<li><b>Est-ce que</b> vous êtes professeur? (Are you a teacher?)</li>'
             '<li><b>Est-ce qu\'</b>elle est là? (Is she there?) — elision before vowel</li>'
             '<li>Works in speech and writing. A safe, neutral option.</li></ul>'),
            ("Method 3: Inversion",
             'Swap the subject pronoun and the conjugated verb, linked with a hyphen. Only used in formal writing and careful speech.',
             '<ul class="slide-list">'
             '<li>Tu parles → <b>Parles-tu</b> français? (Do you speak French?)</li>'
             '<li>Vous êtes → <b>Êtes-vous</b> professeur? (Are you a teacher?)</li>'
             '<li>Il parle → <b>Parle-t-il</b> français? (Does he speak French?) — add -t- for sound</li>'
             '<li>⚠️ If verb ends in a vowel and subject is il/elle/on, add -t-: parle-<b>t</b>-il</li></ul>'),
            ("Question Words (Mots Interrogatifs)",
             "For information questions, question words come at the start (like English):",
             '<table class="sum-table"><thead><tr><th>French</th><th>English</th><th>Example</th></tr></thead><tbody>'
             '<tr><td>Où</td><td>Where</td><td>Où habitez-vous?</td></tr>'
             '<tr><td>Quand</td><td>When</td><td>Quand est-ce qu\'il arrive?</td></tr>'
             '<tr><td>Pourquoi</td><td>Why</td><td>Pourquoi tu pars?</td></tr>'
             '<tr><td>Comment</td><td>How</td><td>Comment vous appelez-vous?</td></tr>'
             '<tr><td>Combien</td><td>How much/many</td><td>Combien ça coûte?</td></tr>'
             '<tr><td>Qui</td><td>Who</td><td>Qui est là?</td></tr>'
             '<tr><td>Qu\'est-ce que</td><td>What</td><td>Qu\'est-ce que tu fais?</td></tr>'
             '</tbody></table>'),
        ],
        "traps": [
            ("Do you speak = Est-ce que vous parlez (NOT Do est-ce que)", "Est-ce que vous parlez français?", "Don't translate 'do'. Est-ce que replaces the whole 'do you' construction."),
            ("Il parle-t-il?", "Parle-t-il?", "With inversion, remove the subject noun if there's a pronoun: 'Paul parle-t-il' (not 'il parle-t-il')."),
            ("Parle-il?", "Parle-t-il?", "When the verb ends in a vowel and subject is il/elle/on, insert -t-: parle-t-il, mange-t-elle."),
            ("Qu'est-ce que vs Qu'est-ce qui", "Qu'est-ce que je fais / Qu'est-ce qui se passe", "Qu'est-ce que = what (object); Qu'est-ce qui = what (subject, with no following subject)."),
        ],
        "summary": [
            ("Rising intonation", "Statement + ?", "Tu parles français?"),
            ("Est-ce que", "Est-ce que + statement", "Est-ce que tu parles français?"),
            ("Est-ce qu'", "Before vowel", "Est-ce qu'elle est là?"),
            ("Inversion", "Verb-pronoun", "Parlez-vous français?"),
            ("-t- insertion", "Vowel + il/elle/on", "Parle-t-il français?"),
            ("Where", "Où", "Où habitez-vous?"),
            ("When", "Quand", "Quand est-ce qu'il arrive?"),
            ("What (object)", "Qu'est-ce que", "Qu'est-ce que tu fais?"),
        ],
        "ex1": (
            "Identify the Question Method",
            "Which method is being used in each question?",
            [
                ("Est-ce que vous parlez anglais?", ["Rising intonation", "Est-ce que", "Inversion", "Question word"], "Est-ce que", "Est-ce que at the start = est-ce que method."),
                ("Parlez-vous anglais?", ["Rising intonation", "Est-ce que", "Inversion", "Question word"], "Inversion", "Verb before pronoun with hyphen = inversion."),
                ("Vous parlez anglais?", ["Rising intonation", "Est-ce que", "Inversion", "Question word"], "Rising intonation", "Same as a statement, ending with ? = rising intonation."),
                ("Où est-ce que vous habitez?", ["Rising intonation", "Est-ce que", "Inversion", "Question word"], "Question word", "Où + est-ce que = question word method."),
                ("Parle-t-il français?", ["Rising intonation", "Est-ce que", "Inversion", "Question word"], "Inversion", "Verb-t-pronoun = inversion with -t- inserted."),
            ]
        ),
        "ex2": (
            "Form the Question",
            "Rewrite as a question using est-ce que.",
            [
                ("Tu habites à Paris.", "Est-ce que tu habites à Paris?", "Add est-ce que before the statement."),
                ("Elle parle espagnol.", "Est-ce qu'elle parle espagnol?", "Elle starts with vowel: est-ce qu'elle."),
                ("Vous aimez le café.", "Est-ce que vous aimez le café?", "Est-ce que + statement unchanged."),
                ("Il est professeur.", "Est-ce qu'il est professeur?", "Il starts with vowel: est-ce qu'il."),
                ("Ils travaillent ici.", "Est-ce qu'ils travaillent ici?", "Ils starts with vowel: est-ce qu'ils."),
            ]
        ),
        "ex3": (
            "Add -t- or Not?",
            "Does this inversion question need a -t-?",
            [
                ("Parle-_-il français?", ["Parle-t-il", "Parle-il", "Parles-il", "Parlent-il"], "Parle-t-il", "Parle ends in -e (vowel) + il → insert -t-: Parle-t-il."),
                ("Mangent-_-ils souvent ici?", ["Mangent-t-ils", "Mangent-ils", "Mange-t-ils", "Mangez-ils"], "Mangent-ils", "Mangent ends in -t (consonant) → no extra -t- needed."),
                ("Aime-_-elle le sport?", ["Aime-t-elle", "Aime-elle", "Aimes-elle", "Aimez-elle"], "Aime-t-elle", "Aime ends in -e (vowel) + elle → -t-: Aime-t-elle."),
                ("Sont-_-ils prêts?", ["Sont-t-ils", "Sont-ils", "Sontez-ils", "Son-t-ils"], "Sont-ils", "Sont ends in -t → no additional -t-: Sont-ils."),
                ("A-_-il une voiture?", ["A-t-il", "A-il", "Avez-il", "Avoir-il"], "A-t-il", "A ends in -a (vowel) + il → -t-: A-t-il."),
            ]
        ),
        "game_desc": "Master the three ways to form questions in French",
        "items": [
            ("intonation", "rising intonation", "informal question: keep statement word order, raise voice at end", "informal ?", "Tu parles français? (Do you speak French?)", "rising intonation = statement + ? (spoken)", "Tu parles?"),
            ("est-ce-que", "est-ce que", "neutral question: add est-ce que before statement", "question prefix", "Est-ce que vous parlez anglais? (Do you speak English?)", "est-ce que = neutral question prefix", "est-ce que"),
            ("est-ce-qu", "est-ce qu'", "est-ce que elides before a vowel", "elision", "Est-ce qu'il est là? (Is he there?)", "est-ce qu' = est-ce que before vowel", "est-ce qu'"),
            ("inversion", "inversion", "formal question: swap verb and subject pronoun", "formal ?", "Parlez-vous français? (Do you speak French?)", "inversion = verb-pronoun (formal)", "Parlez-vous?"),
            ("t-insertion", "-t- insertion", "add -t- in inversion when verb ends in vowel + il/elle/on", "liaison -t-", "Parle-t-il? Mange-t-elle?", "-t- insertion = verb(vowel) + t + il/elle/on", "Parle-t-il"),
            ("ou", "où", "where", "question word", "Où habitez-vous? (Where do you live?)", "où = where", "où"),
            ("quand", "quand", "when", "question word", "Quand est-ce qu'il arrive? (When does he arrive?)", "quand = when", "quand"),
            ("qu-est-ce-que", "qu'est-ce que", "what (as object of question)", "what", "Qu'est-ce que tu fais? (What are you doing?)", "qu'est-ce que = what (object)", "qu'est-ce que"),
        ],
    },

    "adjective-agreement": {
        "level": "a1",
        "section": "grammar",
        "num": "G06",
        "short": "Adjective Agreement",
        "title": "Adjective Agreement — L'Accord des Adjectifs",
        "subtitle": "French adjectives agree with the noun they describe in gender and number",
        "slides": [
            ("Adjectives Must Agree",
             "In English, adjectives never change: <em>a tall man, a tall woman, tall men, tall women</em>. In French, adjectives must match the gender (m/f) and number (sing./plural) of the noun.",
             '<table class="sum-table"><thead><tr><th></th><th>Masculine</th><th>Feminine</th></tr></thead><tbody>'
             '<tr><td>Singular</td><td>un homme <b>grand</b></td><td>une femme <b>grande</b></td></tr>'
             '<tr><td>Plural</td><td>des hommes <b>grands</b></td><td>des femmes <b>grandes</b></td></tr>'
             '</tbody></table>'),
            ("The Four Forms",
             "Most adjectives follow this pattern. The masculine singular is the base form you find in a dictionary.",
             '<table class="sum-table"><thead><tr><th>M. singular</th><th>F. singular</th><th>M. plural</th><th>F. plural</th></tr></thead><tbody>'
             '<tr><td>grand</td><td>grand<b>e</b></td><td>grand<b>s</b></td><td>grand<b>es</b></td></tr>'
             '<tr><td>petit</td><td>petit<b>e</b></td><td>petit<b>s</b></td><td>petit<b>es</b></td></tr>'
             '<tr><td>intelligent</td><td>intelligent<b>e</b></td><td>intelligent<b>s</b></td><td>intelligent<b>es</b></td></tr>'
             '</tbody></table>'
             '<p>⚠️ The added -e often makes the final consonant audible: <em>grand</em> = silent d; <em>grande</em> = /d/ heard.</p>'),
            ("Adjectives Already Ending in -e",
             'If the masculine form already ends in -e, the feminine is identical. Only add -s for plural.',
             '<ul class="slide-list">'
             '<li>jeune → jeune (f. same) / jeunes (plural): <em>un jeune homme, une jeune femme</em></li>'
             '<li>facile → facile (f. same) / faciles: <em>un exercice facile, une leçon facile</em></li>'
             '<li>rouge → rouge / rouges: <em>un stylo rouge, une fleur rouge</em></li></ul>'),
            ("Irregular Adjectives",
             'Some common adjectives have irregular feminine forms:',
             '<table class="sum-table"><thead><tr><th>M. singular</th><th>F. singular</th><th>Meaning</th></tr></thead><tbody>'
             '<tr><td>beau</td><td>belle</td><td>beautiful</td></tr>'
             '<tr><td>nouveau</td><td>nouvelle</td><td>new</td></tr>'
             '<tr><td>vieux</td><td>vieille</td><td>old</td></tr>'
             '<tr><td>bon</td><td>bonne</td><td>good</td></tr>'
             '<tr><td>long</td><td>longue</td><td>long</td></tr>'
             '<tr><td>blanc</td><td>blanche</td><td>white</td></tr>'
             '</tbody></table>'),
            ("Position: After the Noun (Mostly)",
             'Most French adjectives come AFTER the noun — opposite to English. A small group of common adjectives comes before.',
             '<table class="sum-table"><thead><tr><th>After noun (most)</th><th>Before noun (BAGS)</th></tr></thead><tbody>'
             '<tr><td>une voiture <b>rouge</b></td><td><b>Beauty</b>: beau/belle, joli(e)</td></tr>'
             '<tr><td>un homme <b>intelligent</b></td><td><b>Age</b>: jeune, vieux/vieille, nouveau/nouvelle</td></tr>'
             '<tr><td>une femme <b>grande</b></td><td><b>Goodness</b>: bon/bonne, mauvais(e)</td></tr>'
             '<tr><td>des livres <b>intéressants</b></td><td><b>Size</b>: grand(e), petit(e), gros/grosse</td></tr>'
             '</tbody></table>'
             '<p><strong>BAGS</strong> = Beauty, Age, Goodness, Size — these go before the noun.</p>'),
        ],
        "traps": [
            ("une femme grand", "une femme grande", "All adjectives must agree with the noun. Femme is feminine → grande."),
            ("des hommes intelligents (silent s)", "des hommes intelligents /ɛ̃tɛliʒɑ̃/", "Plural -s on adjectives is silent unless followed by a vowel (liaison)."),
            ("un nouveau livre / un bel homme", "un nouveau livre / un bel homme", "Beau, nouveau, vieux have a special form (bel, nouvel, vieil) before a masculine noun starting with a vowel."),
            ("une voiture rouge grande", "une grande voiture rouge", "BAGS adjectives go before the noun; others after. Multiple adjectives: BAGS first, descriptive after."),
        ],
        "summary": [
            ("M. singular", "no change (base)", "grand, petit"),
            ("F. singular", "+e", "grande, petite"),
            ("M. plural", "+s", "grands, petits"),
            ("F. plural", "+es", "grandes, petites"),
            ("Already -e", "no change (+ s pl.)", "jeune → jeune, jeunes"),
            ("Irregular: beau", "belle (f.)", "une belle maison"),
            ("Position: after", "most adjectives", "une voiture rouge"),
            ("Position: before (BAGS)", "Beauty, Age, Goodness, Size", "un grand homme"),
        ],
        "ex1": (
            "Adjective Agreement",
            "Choose the correct form of the adjective.",
            [
                ("une femme ___ (grand)", ["grand", "grande", "grands", "grandes"], "grande", "Femme is feminine singular → grande (+e)."),
                ("des hommes ___ (intelligent)", ["intelligent", "intelligente", "intelligents", "intelligentes"], "intelligents", "Hommes is masculine plural → intelligents (+s)."),
                ("une leçon ___ (facile)", ["facile", "faciles", "facil", "facilement"], "facile", "Facile already ends in -e → no change for feminine. Leçon is singular."),
                ("un ___ livre (nouveau)", ["nouveau", "nouvelle", "nouveaux", "novel"], "nouveau", "Livre is masculine singular → nouveau. (BAGS — before noun)"),
                ("des fleurs ___ (blanc)", ["blanc", "blanche", "blancs", "blanches"], "blanches", "Fleurs is feminine plural → blanches (irregular: blanc → blanche → blanches)."),
                ("un homme ___ (beau)", ["beau", "belle", "bel", "beaux"], "beau", "Homme is masculine singular → beau (use bel only before vowel: un bel homme)."),
            ]
        ),
        "ex2": (
            "Build the Phrase",
            "Translate using the correct adjective form and position.",
            [
                ("a red car (f.)", "une voiture rouge", "Voiture (f.) + rouge after noun (colour adjective goes after)."),
                ("a tall woman (f.)", "une grande femme", "Grande (BAGS: size) goes before femme. Grande = feminine form of grand."),
                ("interesting books (m. pl.)", "des livres intéressants", "Intéressant goes after livre (not BAGS). Masculine plural: intéressants."),
                ("a beautiful house (f.)", "une belle maison", "Belle (f. of beau, BAGS: beauty) goes before maison."),
                ("old buildings (m. pl.)", "de vieux bâtiments", "Vieux (BAGS: age) before noun; masculine plural of vieux = vieux (same). Note: des → de before plural adjective."),
            ]
        ),
        "ex3": (
            "Before or After?",
            "Does the adjective go before or after the noun?",
            [
                ("un livre intéressant", ["Before: un intéressant livre", "After: un livre intéressant", "Either position is fine", "The adjective must go at the end of the sentence"], "After: un livre intéressant", "Intéressant is a descriptive adjective (not BAGS) → after the noun."),
                ("une belle femme", ["Before: une belle femme", "After: une femme belle", "Either position is fine", "No adjective needed"], "Before: une belle femme", "Beau/belle = Beauty (BAGS) → before the noun."),
                ("une maison rouge", ["Before: une rouge maison", "After: une maison rouge", "Either position is fine", "Rouge must follow the verb"], "After: une maison rouge", "Rouge = colour (not BAGS) → after the noun."),
                ("un jeune homme", ["Before: un jeune homme", "After: un homme jeune", "Either is correct in formal French", "After the verb"], "Before: un jeune homme", "Jeune = Age (BAGS) → before the noun."),
                ("un mauvais résultat", ["Before: un mauvais résultat", "After: un résultat mauvais", "Either is always correct", "Never use before or after"], "Before: un mauvais résultat", "Mauvais = Goodness/quality (BAGS) → before the noun."),
            ]
        ),
        "game_desc": "Master French adjective agreement in gender and number",
        "items": [
            ("grand-grande", "grand / grande", "tall / big (BAGS: size, before noun)", "haut/haute", "un grand homme, une grande femme", "grand (m.) → grande (f.) — BAGS: before noun", "grande"),
            ("petit-petite", "petit / petite", "small / little (BAGS: size)", "minuscule", "un petit chat, une petite maison", "petit (m.) → petite (f.) — BAGS: before noun", "petite"),
            ("beau-belle", "beau / belle", "beautiful / handsome (BAGS: beauty, before noun; bel before vowel)", "joli/jolie", "un beau jour, une belle maison, un bel homme", "beau (m.) → belle (f.) — BAGS: beauty", "belle"),
            ("nouveau-nouvelle", "nouveau / nouvelle", "new (BAGS: age, before noun; nouvel before vowel)", "récent/récente", "un nouveau livre, une nouvelle voiture", "nouveau (m.) → nouvelle (f.) — BAGS: age", "nouvelle"),
            ("vieux-vieille", "vieux / vieille", "old (BAGS: age, before noun; vieil before vowel)", "ancien/ancienne", "un vieux film, une vieille maison", "vieux (m.) → vieille (f.) — BAGS: age", "vieille"),
            ("bon-bonne", "bon / bonne", "good (BAGS: goodness, before noun)", "excellent", "un bon repas, une bonne idée", "bon (m.) → bonne (f.) — BAGS: goodness", "bonne"),
            ("rouge", "rouge", "red (colour adjective, after noun)", "écarlate, cramoisi", "une voiture rouge, des fleurs rouges", "rouge → rouge (f. same) — AFTER noun", "rouge"),
            ("bags", "BAGS", "rule for adjectives that go before the noun: Beauty, Age, Goodness, Size", "pre-nominal", "belle, jeune, bon, grand", "BAGS = Beauty Age Goodness Size → BEFORE noun", "BAGS"),
        ],
    },
}
