"""
francais-en A1 Grammar G07–G12  (French for English Speakers)
Generator: gen_francais_en.py
"""

CHAPTERS = {

    # ------------------------------------------------------------------ G07
    "possessives": {
        "level": "a1", "section": "grammar", "num": "G07",
        "short": "Possessive Adjectives",
        "title": "Possessive Adjectives",
        "subtitle": "mon, ma, mes — my, your, his, her…",
        "slides": [
            ("What Are Possessive Adjectives?",
             "Possessive adjectives tell you <em>who owns something</em>. In English: <strong>my, your, his, her, its, our, your, their</strong>. In French they must <strong>agree with the noun</strong>, not with the owner.",
             "English: <em>his sister / her sister</em> — both use 'sister'. French changes the adjective."),
            ("The French Possessives — Singular",
             "Each person has <strong>three forms</strong>: masc. singular · fem. singular · plural.<br><br>"
             "<table><tr><th>Person</th><th>Masc. sg</th><th>Fem. sg</th><th>Plural</th></tr>"
             "<tr><td>my</td><td>mon</td><td>ma</td><td>mes</td></tr>"
             "<tr><td>your (tu)</td><td>ton</td><td>ta</td><td>tes</td></tr>"
             "<tr><td>his/her/its</td><td>son</td><td>sa</td><td>ses</td></tr></table>",
             "<em>mon frère</em> (my brother) · <em>ma sœur</em> (my sister) · <em>mes parents</em> (my parents)"),
            ("The French Possessives — Plural Subjects",
             "<table><tr><th>Person</th><th>Masc. sg</th><th>Fem. sg</th><th>Plural</th></tr>"
             "<tr><td>our</td><td>notre</td><td>notre</td><td>nos</td></tr>"
             "<tr><td>your (vous)</td><td>votre</td><td>votre</td><td>vos</td></tr>"
             "<tr><td>their</td><td>leur</td><td>leur</td><td>leurs</td></tr></table>",
             "<em>notre maison</em> · <em>nos enfants</em> · <em>leur voiture</em> · <em>leurs amis</em>"),
            ("The Vowel Trap: mon/ton/son Before Feminine Nouns",
             "When a feminine noun begins with a <strong>vowel or silent h</strong>, use the <strong>masculine form</strong> — mon/ton/son — for easier pronunciation.",
             "<em>mon amie</em> (my female friend) — NOT ~~ma amie~~<br><em>ton école</em> (your school, feminine) — NOT ~~ta école~~<br><em>son histoire</em> (his/her story) — NOT ~~sa histoire~~"),
            ("His or Her? Context, Not Pronoun",
             "French <em>son/sa/ses</em> means <strong>his, her, or its</strong> — the form depends on the <em>noun</em>, not on the owner's gender.",
             "<em>son frère</em> = his brother OR her brother<br><em>sa mère</em> = his mother OR her mother<br>Only context tells you whether the owner is male or female."),
            ("Quick Summary",
             "• Possessives agree with the <strong>noun</strong>, not the owner.<br>"
             "• Use <strong>mon/ton/son</strong> before any noun starting with a vowel or silent h.<br>"
             "• son/sa/ses = his OR her — context decides.<br>"
             "• notre/votre/leur have only two forms (sg/pl).",
             "<em>mon livre</em> (m) · <em>ma robe</em> (f) · <em>mes affaires</em> (pl) · <em>mon ami(e)</em> (vowel)"),
        ],
        "traps": [
            ("his sister", "sa sœur", "son/sa/ses agree with the noun — not the gender of the owner."),
            ("my female friend", "mon amie", "Feminine noun starting with vowel → use mon, not ma."),
            ("their house", "leur maison", "leur (singular noun) — no -s; leurs amis (plural)."),
            ("her school", "son école", "Feminine vowel-initial noun → son, not sa."),
        ],
        "summary": [
            ("my", "mon / ma / mes", "mon frère · ma sœur · mes livres"),
            ("your (tu)", "ton / ta / tes", "ton chat · ta mère · tes amis"),
            ("his/her/its", "son / sa / ses", "son fils · sa fille · ses enfants"),
            ("our", "notre / nos", "notre maison · nos parents"),
            ("your (vous)", "votre / vos", "votre voiture · vos clés"),
            ("their", "leur / leurs", "leur chien · leurs enfants"),
            ("vowel rule", "mon/ton/son (not ma/ta/sa)", "mon amie · ton école · son histoire"),
            ("his or her?", "son/sa/ses (context decides)", "son frère = his OR her brother"),
        ],
        "ex1": ("Exercise 1 — Choose the correct possessive",
                "Select the right form.",
                [
                    ("___ livre (my, masculine)", ["mon", "ma", "mes", "son"], "mon", "Masculine singular → mon."),
                    ("___ sœur (your, tu, feminine)", ["ton", "ta", "tes", "sa"], "ta", "Feminine singular with tu → ta."),
                    ("___ amis (their, plural)", ["leur", "leurs", "ses", "vos"], "leurs", "Plural noun → leurs."),
                    ("___ école (his, vowel-initial feminine)", ["son", "sa", "ses", "mon"], "son", "Feminine vowel-initial noun → son, not sa."),
                    ("___ maison (our, feminine)", ["notre", "nos", "leur", "votre"], "notre", "Singular feminine noun → notre."),
                    ("___ parents (my, plural)", ["mon", "ma", "mes", "ses"], "mes", "Plural noun with my → mes."),
                ]),
        "ex2": ("Exercise 2 — Translate into French",
                "Type the French sentence.",
                [
                    ("my brother", "mon frère", "Masculine singular → mon."),
                    ("her books", "ses livres", "Plural → ses (his/her)."),
                    ("our school", "notre école", "Singular → notre; école starts with vowel but votre/notre don't change."),
                    ("your (tu) mother", "ta mère", "Feminine singular → ta."),
                    ("their children", "leurs enfants", "Plural → leurs."),
                ]),
        "ex3": ("Exercise 3 — Error correction",
                "Which sentence is correct?",
                [
                    ("Choose the correct version.", ["ma amie", "mon amie", "mes amie", "son amies"], "mon amie",
                     "Vowel-initial feminine noun → mon, not ma."),
                    ("Choose the correct version.", ["leur voitures", "leurs voiture", "leurs voitures", "leur voiture"], "leurs voitures",
                     "Plural noun → leurs; voiture also needs plural."),
                    ("His sister in French:", ["son sœur", "sa sœur", "ses sœur", "leur sœur"], "sa sœur",
                     "Feminine noun sœur → sa; son is for masculine or vowel-initial."),
                    ("My opinion (opinion = feminine):", ["mon opinion", "ma opinion", "mes opinion", "son opinion"], "mon opinion",
                     "Vowel-initial noun → mon even though opinion is feminine."),
                ]),
        "game_desc": "Practice possessive adjectives — mon/ma/mes, ton/ta/tes, son/sa/ses and more.",
        "items": [
            ("poss1", "mon / ma / mes", "my (masc / fem / plural)", "my", "Mon frère, ma sœur, mes livres.", "C'est ___ livre. (my, masc.)", "mon"),
            ("poss2", "ton / ta / tes", "your (tu form, masc / fem / plural)", "your", "Ton chien, ta voiture, tes amis.", "C'est ___ école. (your, tu, vowel)", "ton"),
            ("poss3", "son / sa / ses", "his / her / its (masc / fem / plural)", "his/her", "Son frère, sa mère, ses parents.", "C'est ___ amie. (her, vowel-initial)", "son"),
            ("poss4", "notre / nos", "our (sg / plural)", "our", "Notre maison, nos enfants.", "C'est ___ professeur. (our, masc.)", "notre"),
            ("poss5", "votre / vos", "your (vous form, sg / plural)", "your (formal)", "Votre voiture, vos clés.", "C'est ___ sac. (your, vous, masc.)", "votre"),
            ("poss6", "leur / leurs", "their (sg / plural)", "their", "Leur chien, leurs amis.", "C'est ___ maison. (their, fem. sg)", "leur"),
            ("poss7", "mon amie", "my female friend (vowel rule)", "vowel rule", "Mon amie Marie est sympa.", "Complète: ___ histoire est longue. (her)", "son"),
            ("poss8", "ses livres", "his/her books (plural)", "books", "Il range ses livres dans son sac.", "Complète: Ce sont ___ enfants. (their, plural)", "leurs"),
        ],
    },

    # ------------------------------------------------------------------ G08
    "avoir": {
        "level": "a1", "section": "grammar", "num": "G08",
        "short": "The Verb Avoir (to have)",
        "title": "The Verb <em>Avoir</em> — To Have",
        "subtitle": "j'ai, tu as, il a… and key expressions",
        "slides": [
            ("Avoir — Present Tense",
             "The verb <em>avoir</em> (to have) is <strong>irregular</strong> and very common. Memorise these six forms.",
             "<table><tr><th>Pronoun</th><th>Avoir</th><th>Meaning</th></tr>"
             "<tr><td>je</td><td>ai</td><td>I have</td></tr>"
             "<tr><td>tu</td><td>as</td><td>you have</td></tr>"
             "<tr><td>il/elle/on</td><td>a</td><td>he/she/one has</td></tr>"
             "<tr><td>nous</td><td>avons</td><td>we have</td></tr>"
             "<tr><td>vous</td><td>avez</td><td>you have</td></tr>"
             "<tr><td>ils/elles</td><td>ont</td><td>they have</td></tr></table>"),
            ("Avoir with Un/Une — Indefinite Article",
             "To say you have something, use <em>avoir</em> + <strong>un/une/des</strong>.",
             "<em>J'ai un chien.</em> (I have a dog.)<br><em>Elle a une sœur.</em> (She has a sister.)<br><em>Ils ont des livres.</em> (They have books.)"),
            ("Avoir — Negative: de/d'",
             "In a negative sentence, <strong>un/une/des</strong> changes to <strong>de/d'</strong> (before vowel).",
             "<em>J'ai un chat.</em> → <em>Je n'ai pas de chat.</em><br><em>Il a des amis.</em> → <em>Il n'a pas d'amis.</em><br>Rule: ne…pas → noun gets <em>de/d'</em>, never <em>un/une/des</em>."),
            ("Key Avoir Expressions — Age & Feelings",
             "French uses <em>avoir</em> (have) where English uses <em>be</em> for many feelings and states.",
             "<em>avoir … ans</em> — to be … years old<br>"
             "<em>avoir faim</em> — to be hungry<br>"
             "<em>avoir soif</em> — to be thirsty<br>"
             "<em>avoir chaud</em> — to be hot<br>"
             "<em>avoir froid</em> — to be cold<br>"
             "<em>avoir sommeil</em> — to be sleepy"),
            ("More Avoir Expressions",
             "More fixed phrases with avoir:",
             "<em>avoir peur (de)</em> — to be afraid (of)<br>"
             "<em>avoir envie (de)</em> — to feel like, to want<br>"
             "<em>avoir besoin (de)</em> — to need<br>"
             "<em>avoir raison</em> — to be right<br>"
             "<em>avoir tort</em> — to be wrong<br>"
             "<em>avoir de la chance</em> — to be lucky"),
            ("Quick Summary",
             "• 6 forms: <em>ai, as, a, avons, avez, ont</em>.<br>"
             "• After <em>ne…pas</em>: un/une/des → <strong>de/d'</strong>.<br>"
             "• Dozens of idiomatic expressions use <em>avoir</em> where English uses <em>be</em>.",
             "<em>Quel âge as-tu ?</em> — How old are you?<br><em>J'ai dix-huit ans.</em> — I'm eighteen."),
        ],
        "traps": [
            ("I am 20 years old", "J'ai vingt ans", "French uses avoir for age, not être."),
            ("I am hungry", "J'ai faim", "Avoir faim — literal: 'I have hunger'."),
            ("I don't have a car", "Je n'ai pas de voiture", "un/une/des → de/d' after negation."),
            ("they have", "ils ont", "Irregular — not ils avons or ils avent."),
        ],
        "summary": [
            ("je", "j'ai", "j'ai faim · j'ai un chat"),
            ("tu", "as", "tu as quel âge ?"),
            ("il / elle / on", "a", "il a froid · elle a soif"),
            ("nous", "avons", "nous avons raison"),
            ("vous", "avez", "vous avez de la chance"),
            ("ils / elles", "ont", "ils ont peur · elles ont chaud"),
            ("after negation", "un/une/des → de/d'", "je n'ai pas de chien"),
            ("age / hunger…", "avoir (not être)", "j'ai 20 ans · j'ai faim"),
        ],
        "ex1": ("Exercise 1 — Choose the correct form",
                "Select the right form of avoir.",
                [
                    ("Nous ___ une voiture.", ["avons", "ont", "a", "ai"], "avons", "Nous → avons."),
                    ("Ils ___ de la chance.", ["ont", "a", "avons", "avez"], "ont", "Ils → ont."),
                    ("Tu ___ faim?", ["as", "ai", "a", "ont"], "as", "Tu → as."),
                    ("Elle ___ deux sœurs.", ["a", "ai", "ont", "avez"], "a", "Il/elle → a."),
                    ("Vous ___ raison.", ["avez", "avons", "a", "ont"], "avez", "Vous → avez."),
                ]),
        "ex2": ("Exercise 2 — Translate into French",
                "Type the French sentence.",
                [
                    ("I am hungry.", "J'ai faim.", "Avoir faim — not être faim."),
                    ("She is 25 years old.", "Elle a vingt-cinq ans.", "Avoir for age."),
                    ("We don't have a dog.", "Nous n'avons pas de chien.", "un/une/des → de/d' after negation."),
                    ("They (m) are cold.", "Ils ont froid.", "Avoir froid."),
                    ("Do you need help? (tu)", "Tu as besoin d'aide?", "Avoir besoin de."),
                ]),
        "ex3": ("Exercise 3 — Spot the mistake",
                "Which sentence is correct?",
                [
                    ("'I have 16 years old' in French:", ["Je suis seize ans.", "J'ai seize ans.", "Je ai seize ans.", "J'avons seize ans."], "J'ai seize ans.",
                     "Avoir for age; je + ai → j'ai."),
                    ("'They don't have friends' in French:", ["Ils n'ont pas des amis.", "Ils n'ont pas amis.", "Ils n'ont pas d'amis.", "Ils ont pas amis."], "Ils n'ont pas d'amis.",
                     "des → d' after ne…pas; vowel-initial noun needs d'."),
                    ("'She is thirsty' in French:", ["Elle est soif.", "Elle a soif.", "Elle avez soif.", "Elle ont soif."], "Elle a soif.",
                     "Il/elle → a; avoir soif."),
                    ("'We are right' in French:", ["Nous sommes raison.", "Nous avons raison.", "Nous a raison.", "Nous avez raison."], "Nous avons raison.",
                     "Avoir raison; nous → avons."),
                ]),
        "game_desc": "Master the verb avoir and its essential idiomatic expressions.",
        "items": [
            ("av1", "j'ai", "I have", "I have", "J'ai un frère et une sœur.", "Complète: ___ besoin d'aide. (I)", "j'ai"),
            ("av2", "tu as / vous avez", "you have (sg/pl)", "you have", "Tu as quel âge ? — Vous avez raison.", "Complète: Tu ___ faim ? (tu)", "as"),
            ("av3", "il / elle a", "he / she has", "he has", "Il a une grande famille. Elle a froid.", "Complète: Elle ___ soif. (she)", "a"),
            ("av4", "nous avons", "we have", "we have", "Nous avons deux chats à la maison.", "Complète: Nous ___ de la chance. (we)", "avons"),
            ("av5", "ils / elles ont", "they have", "they have", "Ils ont trois enfants. Elles ont faim.", "Complète: Ils ___ peur. (they)", "ont"),
            ("av6", "avoir faim / soif", "to be hungry / thirsty", "hungry", "J'ai faim. Tu as soif après le sport.", "Complète: J'___ faim. (I)", "ai"),
            ("av7", "avoir … ans", "to be … years old", "years old", "Elle a vingt ans. Ils ont seize ans.", "Complète: Il ___ trente ans. (he)", "a"),
            ("av8", "ne pas avoir de", "not to have (no article)", "no article", "Je n'ai pas de chien. Nous n'avons pas d'argent.", "Complète: Il n'a pas ___ voiture. (de/d')", "de"),
        ],
    },

    # ------------------------------------------------------------------ G09
    "aller-futur": {
        "level": "a1", "section": "grammar", "num": "G09",
        "short": "Aller + Infinitive (Near Future)",
        "title": "Aller + Infinitive — Near Future",
        "subtitle": "je vais manger, tu vas partir…",
        "slides": [
            ("The Futur Proche — Going to…",
             "To talk about plans or events in the near future, French uses <strong>aller + infinitive</strong>. This is exactly like English <em>going to</em>.",
             "<em>Je vais manger.</em> — I'm going to eat.<br><em>Elle va partir.</em> — She's going to leave.<br><em>Nous allons voyager.</em> — We're going to travel."),
            ("Conjugation of Aller — Present",
             "You need <em>aller</em> in the <strong>present tense</strong> first.",
             "<table><tr><th>Pronoun</th><th>Aller</th></tr>"
             "<tr><td>je</td><td>vais</td></tr>"
             "<tr><td>tu</td><td>vas</td></tr>"
             "<tr><td>il/elle/on</td><td>va</td></tr>"
             "<tr><td>nous</td><td>allons</td></tr>"
             "<tr><td>vous</td><td>allez</td></tr>"
             "<tr><td>ils/elles</td><td>vont</td></tr></table>"),
            ("Futur Proche — Affirmative",
             "Formula: <strong>subject + aller (present) + infinitive</strong>.",
             "<em>Tu vas étudier ce soir ?</em> — Are you going to study tonight?<br>"
             "<em>Ils vont regarder un film.</em> — They're going to watch a film.<br>"
             "<em>Nous allons sortir.</em> — We're going to go out."),
            ("Futur Proche — Negative",
             "Place <strong>ne…pas around aller</strong>, NOT around the infinitive.",
             "<em>Je ne vais pas manger.</em> — I'm not going to eat.<br>"
             "<em>Elle ne va pas venir.</em> — She's not going to come.<br>"
             "Wrong: ~~Je vais ne pas manger.~~ ✗"),
            ("Aller as 'To Go'",
             "<em>Aller</em> also means <em>to go</em>. Use it with <strong>à/au/aux/en</strong> to say where you are going.",
             "<em>Je vais à l'école.</em> — I go to school.<br>"
             "<em>Nous allons au cinéma.</em> — We're going to the cinema.<br>"
             "<em>Ils vont en France.</em> — They're going to France.<br>"
             "Also: <em>Ça va ?</em> — How are you? / <em>Je vais bien.</em> — I'm fine."),
            ("Quick Summary",
             "• Futur proche = <strong>aller (present) + infinitive</strong>.<br>"
             "• Negative: <strong>ne + aller + pas + infinitive</strong>.<br>"
             "• Aller also = <em>to go</em> (to a place).<br>"
             "• <em>Ça va / Je vais bien</em> = everyday greeting.",
             "<em>je vais · tu vas · il va · nous allons · vous allez · ils vont</em>"),
        ],
        "traps": [
            ("I'm not going to sleep", "Je ne vais pas dormir", "ne…pas wraps aller, not the infinitive."),
            ("they are going to come", "ils vont venir", "Irregular: ils → vont."),
            ("How are you?", "Ça va ?", "Literally 'It goes?' — idiomatic greeting."),
            ("we go to the cinema", "nous allons au cinéma", "à + le → au; aller + destination."),
        ],
        "summary": [
            ("je / tu / il-elle-on", "vais / vas / va", "je vais, tu vas, elle va"),
            ("nous / vous / ils-elles", "allons / allez / vont", "nous allons, vous allez, ils vont"),
            ("futur proche", "aller + infinitive", "je vais manger · elle va partir"),
            ("negative futur proche", "ne + aller + pas + inf.", "je ne vais pas dormir"),
            ("to go to a city", "aller à + city", "je vais à Paris"),
            ("to go to a country", "aller au/en/aux", "au Japon · en France · aux États-Unis"),
            ("greeting", "Ça va ?", "Ça va ? — Oui, je vais bien."),
            ("to go / going to", "both uses", "je vais au cinéma · je vais regarder"),
        ],
        "ex1": ("Exercise 1 — Choose the right form of aller",
                "Select the correct form.",
                [
                    ("Nous ___ voyager cet été.", ["allons", "vont", "va", "vas"], "allons", "Nous → allons."),
                    ("Tu ___ étudier ce soir ?", ["vas", "vais", "va", "allez"], "vas", "Tu → vas."),
                    ("Ils ___ regarder un film.", ["vont", "va", "allez", "allons"], "vont", "Ils → vont."),
                    ("Elle ___ partir demain.", ["va", "vais", "vas", "vont"], "va", "Il/elle → va."),
                    ("Vous ___ manger au restaurant ?", ["allez", "allons", "vont", "vas"], "allez", "Vous → allez."),
                ]),
        "ex2": ("Exercise 2 — Translate into French",
                "Type the French sentence.",
                [
                    ("I'm going to eat.", "Je vais manger.", "je + vais + infinitive."),
                    ("She's not going to come.", "Elle ne va pas venir.", "ne + va + pas + infinitive."),
                    ("Are you (tu) going to study?", "Tu vas étudier ?", "tu + vas + infinitive."),
                    ("We're going to the cinema.", "Nous allons au cinéma.", "aller + au (à+le)."),
                    ("They (f) are going to travel.", "Elles vont voyager.", "elles + vont + infinitive."),
                ]),
        "ex3": ("Exercise 3 — Spot the mistake",
                "Which sentence is correct?",
                [
                    ("'I'm not going to sleep' in French:", ["Je vais ne pas dormir.", "Je ne vais pas dormir.", "Je ne vas pas dormir.", "Je vais dormir pas."], "Je ne vais pas dormir.",
                     "ne…pas wraps aller; je → vais."),
                    ("'They are going to arrive' in French:", ["Ils allons arriver.", "Ils va arriver.", "Ils vont arriver.", "Ils aller arriver."], "Ils vont arriver.",
                     "Ils → vont; add infinitive."),
                    ("How do you say 'How are you?' casually:", ["Comment vas-tu ?", "Ça va ?", "Tu vas bien ?", "All correct"], "All correct",
                     "All three are valid casual ways to ask. Ça va? is most common."),
                    ("'We go to France' in French:", ["Nous allons à France.", "Nous allons en France.", "Nous allez en France.", "Nous allons France."], "Nous allons en France.",
                     "Countries (feminine) → en; nous → allons."),
                ]),
        "game_desc": "Master aller in the present and futur proche — going to do things.",
        "items": [
            ("al1", "je vais", "I go / I am going", "I go", "Je vais à l'école. Je vais manger.", "Complète: Je ___ partir. (I)", "vais"),
            ("al2", "tu vas / vous allez", "you go / you are going", "you go", "Tu vas bien ? Vous allez en France ?", "Complète: Tu ___ étudier ? (tu)", "vas"),
            ("al3", "il / elle va", "he / she goes", "she goes", "Il va au cinéma. Elle va travailler.", "Complète: Elle ___ venir. (she)", "va"),
            ("al4", "nous allons", "we go / we are going", "we go", "Nous allons au marché ce matin.", "Complète: Nous ___ voyager. (we)", "allons"),
            ("al5", "ils / elles vont", "they go / are going", "they go", "Ils vont regarder un film ce soir.", "Complète: Ils ___ arriver. (they)", "vont"),
            ("al6", "aller + infinitif", "futur proche (going to…)", "going to", "Elle va partir demain matin tôt.", "Complète: Tu vas ___ ce soir. (étudier)", "étudier"),
            ("al7", "ne pas aller + infinitif", "not going to (negative futur proche)", "not going to", "Je ne vais pas manger ce soir.", "Complète: Il ne ___ pas venir. (va)", "va"),
            ("al8", "Ça va ?", "How are you? / I'm fine", "fine", "Ça va ? — Oui, ça va bien, merci !", "Complète: ___ va ? (Ça)", "Ça"),
        ],
    },

    # ------------------------------------------------------------------ G10
    "prepositions-places": {
        "level": "a1", "section": "grammar", "num": "G10",
        "short": "Prepositions with Countries & Cities",
        "title": "Prepositions with Countries & Cities",
        "subtitle": "en France · au Mexique · aux États-Unis · à Paris",
        "slides": [
            ("Cities — Always à",
             "To say you are in or going to a <strong>city</strong>, use <strong>à</strong>.",
             "<em>Je suis à Paris.</em> — I'm in Paris.<br><em>Elle va à Barcelone.</em> — She's going to Barcelona.<br><em>Ils habitent à Londres.</em> — They live in London.<br>No article needed — just à + city name."),
            ("Feminine Countries — en",
             "Most countries ending in <strong>-e</strong> are feminine → use <strong>en</strong>.",
             "<em>en France · en Espagne · en Italie · en Allemagne</em><br>"
             "<em>en Chine · en Corée · en Australie · en Colombie</em><br>"
             "<em>Je vais en France.</em> — I'm going to France.<br>"
             "Exception: <em>le Mexique, le Mozambique, le Zimbabwe</em> → these end in -e but are masculine."),
            ("Masculine Countries — au / aux",
             "Masculine countries (not ending in -e, mostly) use <strong>au</strong>. Plural country names use <strong>aux</strong>.",
             "<em>au Portugal · au Maroc · au Japon · au Canada</em><br>"
             "<em>aux États-Unis · aux Pays-Bas · aux Philippines</em><br>"
             "<em>Il travaille au Japon.</em> — He works in Japan.<br>"
             "<em>Ils habitent aux États-Unis.</em> — They live in the United States."),
            ("Coming From — de/du/des/d'",
             "To say where you come from, use <strong>de</strong> for cities; <strong>du/de la/des/d'</strong> for countries.",
             "<em>Je viens de Paris.</em> — I come from Paris.<br>"
             "<em>Elle vient de France.</em> — She comes from France. (fem. country)<br>"
             "<em>Il vient du Japon.</em> — He comes from Japan. (de + le → du)<br>"
             "<em>Ils viennent des États-Unis.</em> — They come from the US. (de + les → des)"),
            ("Summary Table",
             "Quick reference for prepositions of place and origin.",
             "<table><tr><th>Case</th><th>In/To</th><th>From</th><th>Example</th></tr>"
             "<tr><td>City</td><td>à</td><td>de</td><td>à Paris / de Paris</td></tr>"
             "<tr><td>Fem. country</td><td>en</td><td>de</td><td>en France / de France</td></tr>"
             "<tr><td>Masc. country</td><td>au</td><td>du</td><td>au Japon / du Japon</td></tr>"
             "<tr><td>Plural country</td><td>aux</td><td>des</td><td>aux États-Unis / des États-Unis</td></tr></table>"),
            ("Quick Summary",
             "• <strong>à</strong> → all cities.<br>"
             "• <strong>en</strong> → feminine countries (most -e endings).<br>"
             "• <strong>au</strong> → masculine countries; <strong>aux</strong> → plural countries.<br>"
             "• <strong>de/du/des</strong> → origin, matching gender/number.",
             "<em>Je vis à Madrid. Je vais au Mexique. Elle vient de Chine.</em>"),
        ],
        "traps": [
            ("in Japan", "au Japon", "Japon is masculine → au, not en."),
            ("from the United States", "des États-Unis", "Plural → aux/des."),
            ("in Mexico", "au Mexique", "Ends in -e but masculine → au, not en."),
            ("from France", "de France", "Feminine country → de, not du."),
        ],
        "summary": [
            ("in/to + city", "à", "à Paris · à Tokyo · à Rome"),
            ("in/to + fem. country", "en", "en France · en Espagne · en Chine"),
            ("in/to + masc. country", "au", "au Japon · au Canada · au Maroc"),
            ("in/to + plural country", "aux", "aux États-Unis · aux Pays-Bas"),
            ("from + city", "de", "de Paris · de Londres · de Rome"),
            ("from + fem. country", "de", "de France · d'Italie · de Chine"),
            ("from + masc. country", "du", "du Japon · du Canada · du Maroc"),
            ("from + plural country", "des", "des États-Unis · des Pays-Bas"),
        ],
        "ex1": ("Exercise 1 — Choose the right preposition",
                "Select in/to.",
                [
                    ("___ Espagne (feminine country)", ["en", "au", "à", "aux"], "en", "Espagne is feminine → en."),
                    ("___ Tokyo (city)", ["à", "en", "au", "aux"], "à", "All cities → à."),
                    ("___ Canada (masculine country)", ["au", "en", "à", "aux"], "au", "Canada is masculine → au."),
                    ("___ États-Unis (plural country)", ["aux", "au", "en", "à"], "aux", "Plural → aux."),
                    ("___ Portugal (masculine country)", ["au", "en", "à", "aux"], "au", "Portugal is masculine → au."),
                    ("___ Chine (feminine country)", ["en", "au", "à", "aux"], "en", "Chine is feminine → en."),
                ]),
        "ex2": ("Exercise 2 — Translate into French",
                "Type the French sentence.",
                [
                    ("I live in London.", "Je vis à Londres.", "City → à."),
                    ("She's going to Japan.", "Elle va au Japon.", "Masculine → au."),
                    ("He comes from France.", "Il vient de France.", "Feminine country origin → de."),
                    ("They live in the United States.", "Ils vivent aux États-Unis.", "Plural → aux."),
                    ("I come from Mexico.", "Je viens du Mexique.", "Masculine → du."),
                ]),
        "ex3": ("Exercise 3 — Spot the mistake",
                "Which sentence is correct?",
                [
                    ("'She lives in Spain':", ["Elle vit au Espagne.", "Elle vit en Espagne.", "Elle vit à Espagne.", "Elle vit des Espagne."], "Elle vit en Espagne.",
                     "Spain (Espagne) is feminine → en."),
                    ("'He comes from Japan':", ["Il vient de Japon.", "Il vient du Japon.", "Il vient en Japon.", "Il vient au Japon."], "Il vient du Japon.",
                     "Origin from masculine country → du (de + le)."),
                    ("'I'm going to Paris':", ["Je vais en Paris.", "Je vais au Paris.", "Je vais à Paris.", "Je vais Paris."], "Je vais à Paris.",
                     "All cities → à; no article."),
                    ("'They come from the United States':", ["Ils viennent de États-Unis.", "Ils viennent du États-Unis.", "Ils viennent des États-Unis.", "Ils viennent aux États-Unis."], "Ils viennent des États-Unis.",
                     "Plural country origin → des (de + les)."),
                ]),
        "game_desc": "Practice prepositions with cities, countries, and origins.",
        "items": [
            ("pp1", "à + ville", "in / to + city", "to city", "Je vais à Rome. Elle habite à Berlin.", "Complète: Il vit ___ Tokyo. (city)", "à"),
            ("pp2", "en + pays féminin", "in / to + feminine country", "in France", "Elle voyage en Italie. Je vis en France.", "Complète: Tu vas ___ Espagne. (feminine)", "en"),
            ("pp3", "au + pays masculin", "in / to + masculine country", "in Japan", "Il travaille au Japon. Je vais au Maroc.", "Complète: Elle va ___ Canada. (masculine)", "au"),
            ("pp4", "aux + pays pluriel", "in / to + plural country", "in the US", "Ils habitent aux États-Unis.", "Complète: Nous allons ___ Pays-Bas. (plural)", "aux"),
            ("pp5", "de + ville", "from + city", "from Paris", "Je viens de Paris. Elle vient de Rome.", "Complète: Il vient ___ Berlin. (city)", "de"),
            ("pp6", "de + pays féminin", "from + feminine country", "from France", "Elle vient de France. Il revient d'Italie.", "Complète: Je viens ___ Espagne. (feminine)", "de"),
            ("pp7", "du + pays masculin", "from + masculine country", "from Japan", "Il vient du Japon. Elle revient du Maroc.", "Complète: Il vient ___ Mexique. (masculine)", "du"),
            ("pp8", "des + pays pluriel", "from + plural country", "from the US", "Ils viennent des États-Unis.", "Complète: Elle vient ___ Pays-Bas. (plural)", "des"),
        ],
    },

    # ------------------------------------------------------------------ G11
    "numbers-time": {
        "level": "a1", "section": "grammar", "num": "G11",
        "short": "Numbers & Telling the Time",
        "title": "Numbers & Telling the Time",
        "subtitle": "0–100, heure, demi, quart…",
        "slides": [
            ("Cardinal Numbers 0–20",
             "Learn these first — higher numbers build on them.",
             "0 zéro · 1 un · 2 deux · 3 trois · 4 quatre · 5 cinq<br>"
             "6 six · 7 sept · 8 huit · 9 neuf · 10 dix<br>"
             "11 onze · 12 douze · 13 treize · 14 quatorze · 15 quinze<br>"
             "16 seize · 17 dix-sept · 18 dix-huit · 19 dix-neuf · 20 vingt"),
            ("Numbers 21–100",
             "Pattern: <em>vingt et un, vingt-deux… trente… quarante… cinquante…</em><br>Note the <em>et un</em> at 21, 31, 41, 51, 61 — but <strong>NOT</strong> at 71 onwards.",
             "21 vingt et un · 22 vingt-deux<br>"
             "30 trente · 31 trente et un<br>"
             "40 quarante · 50 cinquante · 60 soixante<br>"
             "70 soixante-dix · 71 soixante et onze · 72 soixante-douze<br>"
             "80 quatre-vingts · 81 quatre-vingt-un<br>"
             "90 quatre-vingt-dix · 91 quatre-vingt-onze · 100 cent"),
            ("The 70s, 80s, 90s — French Math",
             "French counts differently from 70 onwards — literally 'sixty-ten' (70), 'four-twenties' (80), 'four-twenty-ten' (90).",
             "70 = soixante-dix (60+10)<br>"
             "71 = soixante et onze (60+11)<br>"
             "72 = soixante-douze (60+12)<br>"
             "80 = quatre-vingts (4×20) — drops -s in compounds<br>"
             "81 = quatre-vingt-un<br>"
             "90 = quatre-vingt-dix (4×20+10)<br>"
             "91 = quatre-vingt-onze"),
            ("Telling the Time — Quelle heure est-il?",
             "Ask: <em>Quelle heure est-il ?</em> / <em>Il est quelle heure ?</em><br>Answer: <em>Il est + [number] + heure(s)</em>.",
             "<em>Il est une heure.</em> — It's 1 o'clock.<br>"
             "<em>Il est deux heures.</em> — It's 2 o'clock.<br>"
             "<em>Il est midi.</em> — It's noon.<br>"
             "<em>Il est minuit.</em> — It's midnight."),
            ("Minutes, Quarter, Half",
             "Add minutes directly, or use quarter/half expressions.",
             "<em>Il est trois heures dix.</em> — It's 3:10.<br>"
             "<em>Il est trois heures et quart.</em> — It's quarter past 3.<br>"
             "<em>Il est trois heures et demie.</em> — It's half past 3.<br>"
             "<em>Il est quatre heures moins le quart.</em> — It's quarter to 4.<br>"
             "<em>Il est quatre heures moins dix.</em> — It's 3:50 (ten to four)."),
            ("Quick Summary",
             "• 70–79: soixante + (10–19).<br>"
             "• 80–89: quatre-vingt + (1–9) — no -s except bare 80.<br>"
             "• 90–99: quatre-vingt + (10–19).<br>"
             "• Time: <em>Il est X heure(s)</em>; midi; minuit.<br>"
             "• et quart / et demie / moins le quart.",
             "<em>Il est dix-sept heures trente.</em> (17:30 = 5:30 pm)"),
        ],
        "traps": [
            ("80", "quatre-vingts", "80 = 4×20; drops -s in compounds (81 = quatre-vingt-un)."),
            ("71", "soixante et onze", "70s = 60 + teens; 71 uses et like other -1 forms (until 61)."),
            ("It's half past 3", "Il est trois heures et demie", "et demie after heures (feminine)."),
            ("It's quarter to 4", "Il est quatre heures moins le quart", "moins le quart = minus a quarter."),
        ],
        "summary": [
            ("0–69", "regular", "un, deux…vingt, trente, quarante…soixante"),
            ("70–79", "soixante-dix…", "soixante-dix, soixante et onze…soixante-dix-neuf"),
            ("80–89", "quatre-vingts…", "quatre-vingts, quatre-vingt-un…quatre-vingt-neuf"),
            ("90–99", "quatre-vingt-dix…", "quatre-vingt-dix, quatre-vingt-onze…"),
            ("time", "Il est + N + heure(s)", "Il est deux heures."),
            ("quarter past", "et quart", "Il est trois heures et quart."),
            ("half past", "et demie", "Il est trois heures et demie."),
            ("quarter to", "moins le quart", "Il est quatre heures moins le quart."),
        ],
        "ex1": ("Exercise 1 — Number quiz",
                "Choose the correct French number.",
                [
                    ("70 in French:", ["soixante-dix", "septante", "soixante-dixième", "quatre-vingt-dix"], "soixante-dix", "70 = soixante-dix (used in France)."),
                    ("80 in French:", ["octante", "quatre-vingts", "quatre-vingt", "huitante"], "quatre-vingts", "80 = quatre-vingts (note the -s on the bare form)."),
                    ("91 in French:", ["quatre-vingt-onze", "quatre-vingt-et-un", "nonante et un", "soixante-onze"], "quatre-vingt-onze", "91 = quatre-vingt-onze (no et)."),
                    ("72 in French:", ["soixante-douze", "soixante-et-douze", "septante-deux", "soixante-dixième"], "soixante-douze", "72 = soixante-douze."),
                    ("45 in French:", ["quarante-cinq", "quarante et cinq", "quatre-vingt-cinq", "cinquante-cinq"], "quarante-cinq", "45 = quarante-cinq."),
                ]),
        "ex2": ("Exercise 2 — Time expressions",
                "Type the French phrase.",
                [
                    ("It's 3 o'clock.", "Il est trois heures.", "Il est + number + heures."),
                    ("It's quarter past 2.", "Il est deux heures et quart.", "et quart after heures."),
                    ("It's half past 9.", "Il est neuf heures et demie.", "et demie after heures."),
                    ("It's quarter to 6.", "Il est six heures moins le quart.", "moins le quart."),
                    ("It's noon.", "Il est midi.", "Special word for noon."),
                ]),
        "ex3": ("Exercise 3 — Choose the time expression",
                "Pick the correct phrase.",
                [
                    ("3:15 in French:", ["Il est trois heures et quart.", "Il est trois heures quart.", "Il est trois et quart heures.", "Il est quatre heures moins quart."], "Il est trois heures et quart.",
                     "et quart placed after heures."),
                    ("3:30:", ["Il est trois heures demi.", "Il est trois heures et demie.", "Il est trois et demie.", "Il est trois heures demi-heure."], "Il est trois heures et demie.",
                     "et demie (feminine, agrees with heure)."),
                    ("3:50:", ["Il est trois heures cinquante.", "Il est quatre heures moins dix.", "Both are correct", "Il est moins dix."], "Both are correct",
                     "3:50 = quatre heures moins dix OR trois heures cinquante — both valid."),
                    ("How do you ask the time?", ["Quelle heure est-il ?", "Qu'est-ce que l'heure ?", "Quel heure est-il ?", "Quelle est l'heure actuelle ?"], "Quelle heure est-il ?",
                     "Standard question; note quelle (feminine, agrees with heure)."),
                ]),
        "game_desc": "Practice French numbers 0–100 and telling the time.",
        "items": [
            ("nm1", "soixante-dix", "70 (sixty-ten)", "seventy", "Il y a soixante-dix pages dans ce livre.", "Complète: Elle a soixante-___ ans. (10)", "dix"),
            ("nm2", "quatre-vingts", "80 (four-twenties)", "eighty", "Ma grand-mère a quatre-vingts ans.", "Complète: Quatre-___ euros. (bare 80)", "vingts"),
            ("nm3", "quatre-vingt-dix", "90 (four-twenty-ten)", "ninety", "Le score final est quatre-vingt-dix points.", "Complète: Quatre-vingt-___ euros. (90)", "dix"),
            ("nm4", "Il est… heures", "It is… o'clock", "o'clock", "Il est deux heures de l'après-midi.", "Complète: Il est trois ___. (o'clock pl.)", "heures"),
            ("nm5", "et quart", "quarter past", "quarter past", "Il est dix heures et quart du matin.", "Complète: Il est cinq heures et ___. (15 min)", "quart"),
            ("nm6", "et demie", "half past", "half past", "Il est huit heures et demie.", "Complète: Il est midi et ___. (30 min)", "demie"),
            ("nm7", "moins le quart", "quarter to", "quarter to", "Il est six heures moins le quart.", "Complète: Il est sept heures moins le ___. (quarter)", "quart"),
            ("nm8", "midi / minuit", "noon / midnight", "noon", "On mange à midi. Le train part à minuit.", "Complète: Il est ___. (12:00 midday)", "midi"),
        ],
    },

    # ------------------------------------------------------------------ G12
    "faux-amis-a1": {
        "level": "a1", "section": "grammar", "num": "G12",
        "short": "Faux Amis (False Friends) — A1",
        "title": "Faux Amis — False Friends at A1",
        "subtitle": "Words that look English but mean something different",
        "slides": [
            ("What Are Faux Amis?",
             "<strong>Faux amis</strong> (false friends) are French words that look or sound like English words but have a <em>different meaning</em>. They are one of the biggest traps for English speakers.",
             "<em>librairie</em> looks like 'library' — but it means <strong>bookshop</strong>.<br><em>library</em> in French = <em>bibliothèque</em>.<br>Knowing the faux amis saves you from embarrassing mistakes."),
            ("Everyday Faux Amis — Part 1",
             "High-frequency traps you will meet at A1.",
             "<em>actuellement</em> — currently / at the moment (NOT 'actually')<br>"
             "<em>actually</em> = <em>en fait / vraiment</em><br><br>"
             "<em>assister à</em> — to attend (a meeting, event) (NOT 'to assist')<br>"
             "<em>to assist</em> = <em>aider</em><br><br>"
             "<em>attendre</em> — to wait (for) (NOT 'to attend')<br>"
             "<em>to attend</em> = <em>assister à</em>"),
            ("Everyday Faux Amis — Part 2",
             "More A1-level traps.",
             "<em>blesser</em> — to injure / to hurt (NOT 'to bless')<br>"
             "<em>to bless</em> = <em>bénir</em><br><br>"
             "<em>caméra</em> — video/film camera (NOT a photo camera)<br>"
             "<em>photo camera</em> = <em>appareil photo</em><br><br>"
             "<em>cave</em> — wine cellar / basement (NOT 'a cave')<br>"
             "<em>a cave</em> = <em>une grotte</em>"),
            ("Everyday Faux Amis — Part 3",
             "More essential pairs.",
             "<em>commander</em> — to order (food/goods) (NOT 'to command an army')<br>"
             "<em>to command (troops)</em> = <em>diriger / ordonner</em><br><br>"
             "<em>étudiant</em> — university student (NOT any student)<br>"
             "<em>a school pupil</em> = <em>un élève</em><br><br>"
             "<em>librairie</em> — bookshop (NOT 'library')<br>"
             "<em>library</em> = <em>bibliothèque</em>"),
            ("Everyday Faux Amis — Part 4",
             "Final set of A1 faux amis.",
             "<em>location</em> — rental (of a car, flat…) (NOT 'a location')<br>"
             "<em>a location (place)</em> = <em>un endroit / un lieu</em><br><br>"
             "<em>monnaie</em> — coins / small change (NOT 'money')<br>"
             "<em>money</em> = <em>argent</em><br><br>"
             "<em>rester</em> — to stay / to remain (NOT 'to rest')<br>"
             "<em>to rest</em> = <em>se reposer</em>"),
            ("Quick Summary",
             "Don't translate by appearance — check meaning!",
             "<table style='font-size:.85em'>"
             "<tr><th>Faux ami</th><th>French meaning</th><th>English word it looks like</th><th>Correct French</th></tr>"
             "<tr><td>actuellement</td><td>currently</td><td>actually</td><td>en fait</td></tr>"
             "<tr><td>attendre</td><td>to wait</td><td>to attend</td><td>assister à</td></tr>"
             "<tr><td>librairie</td><td>bookshop</td><td>library</td><td>bibliothèque</td></tr>"
             "<tr><td>location</td><td>rental</td><td>location</td><td>endroit / lieu</td></tr>"
             "<tr><td>rester</td><td>to stay</td><td>to rest</td><td>se reposer</td></tr>"
             "</table>"),
        ],
        "traps": [
            ("I'm waiting for the bus", "J'attends le bus", "attendre = to wait, NOT attend."),
            ("the library", "la bibliothèque", "librairie = bookshop; library = bibliothèque."),
            ("car rental", "location de voiture", "location = rental in French — not a place."),
            ("actually / in fact", "en fait / vraiment", "actuellement = currently, not actually."),
        ],
        "summary": [
            ("actuellement", "currently", "en fait / vraiment = actually"),
            ("attendre", "to wait", "assister à = to attend"),
            ("assister à", "to attend", "aider = to assist"),
            ("blesser", "to injure", "bénir = to bless"),
            ("librairie", "bookshop", "bibliothèque = library"),
            ("location", "rental", "endroit / lieu = location/place"),
            ("monnaie", "coins / change", "argent = money"),
            ("rester", "to stay", "se reposer = to rest"),
        ],
        "ex1": ("Exercise 1 — What does it mean?",
                "Choose the correct English meaning.",
                [
                    ("actuellement", ["actually", "currently", "at first", "actually not"], "currently",
                     "actuellement = currently / at the moment; 'actually' = en fait."),
                    ("attendre", ["to attend", "to wait", "to listen", "to tend"], "to wait",
                     "attendre = to wait; 'to attend' = assister à."),
                    ("librairie", ["library", "bookshop", "laboratory", "library card"], "bookshop",
                     "librairie = bookshop; 'library' = bibliothèque."),
                    ("location", ["location/place", "rental", "locomotion", "local area"], "rental",
                     "location = rental; 'location/place' = endroit/lieu."),
                    ("rester", ["to rest", "to stay/remain", "to resist", "to restore"], "to stay/remain",
                     "rester = to stay; 'to rest' = se reposer."),
                ]),
        "ex2": ("Exercise 2 — Translate correctly",
                "Type the correct French word or phrase.",
                [
                    ("the library (not a bookshop)", "la bibliothèque", "librairie = bookshop; bibliothèque = library."),
                    ("I'm waiting for the train.", "J'attends le train.", "attendre = to wait."),
                    ("car rental", "location de voiture", "location = rental in French."),
                    ("she is currently in Paris", "elle est actuellement à Paris", "actuellement = currently."),
                    ("I need to rest.", "J'ai besoin de me reposer.", "se reposer = to rest."),
                ]),
        "ex3": ("Exercise 3 — Choose the right word",
                "Pick the correct option.",
                [
                    ("'I attend the meeting' in French:", ["J'attends la réunion.", "J'assiste à la réunion.", "Je reste à la réunion.", "J'aide la réunion."], "J'assiste à la réunion.",
                     "to attend = assister à; attendre = to wait."),
                    ("'She hurt herself' in French:", ["Elle s'est bénie.", "Elle s'est blessée.", "Elle s'est assistée.", "Elle s'est commandée."], "Elle s'est blessée.",
                     "blesser = to injure/hurt; bénir = to bless."),
                    ("'I need some money' in French:", ["J'ai besoin de monnaie.", "J'ai besoin d'argent.", "J'ai besoin de location.", "J'ai besoin de cave."], "J'ai besoin d'argent.",
                     "argent = money; monnaie = coins/change."),
                    ("'I'm staying here' in French:", ["Je reste ici.", "Je me repose ici.", "J'attends ici.", "Je commande ici."], "Je reste ici.",
                     "rester = to stay; se reposer = to rest."),
                ]),
        "game_desc": "Test your knowledge of French false friends — words that look English but aren't.",
        "items": [
            ("fa1", "actuellement", "currently / at the moment", "currently", "Actuellement, je travaille à Paris.", "actuellement = currently (NOT ___)", "actually"),
            ("fa2", "attendre", "to wait (for)", "to wait", "J'attends le bus depuis dix minutes.", "attendre = to wait (NOT to ___)", "attend"),
            ("fa3", "librairie", "bookshop", "bookshop", "J'achète ce roman à la librairie.", "librairie = bookshop (NOT ___)", "library"),
            ("fa4", "bibliothèque", "library", "library", "J'emprunte des livres à la bibliothèque.", "bibliothèque = library (NOT ___)", "bookshop"),
            ("fa5", "location", "rental", "rental", "La location de voitures est moins chère ici.", "location = rental (NOT a place; place = ___)", "endroit"),
            ("fa6", "blesser", "to injure / to hurt", "to injure", "Il s'est blessé au foot. Pas grave.", "blesser = to injure (NOT to ___)", "bless"),
            ("fa7", "rester", "to stay / to remain", "to stay", "Je reste à la maison ce soir.", "rester = to stay (NOT to ___)", "rest"),
            ("fa8", "assister à", "to attend (an event)", "to attend", "J'assiste à la conférence demain.", "assister à = to attend (NOT to ___)", "assist"),
        ],
    },
}
