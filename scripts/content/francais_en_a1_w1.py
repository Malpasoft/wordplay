"""
francais-en A1 Writing W01–W04  (French for English Speakers)
Generator: gen_francais_en.py
"""

CHAPTERS = {

    # ------------------------------------------------------------------ W01
    "self-introduction": {
        "level": "a1", "section": "writing", "num": "W01",
        "short": "Self-Introduction",
        "title": "Writing a Self-Introduction",
        "subtitle": "Introduce yourself in French — name, age, nationality, family, hobbies",
        "slides": [
            ("What to Include in a French Introduction",
             "A simple A1 self-introduction covers five things.",
             "1. <strong>Name</strong> — <em>Je m'appelle…</em><br>"
             "2. <strong>Age</strong> — <em>J'ai … ans.</em><br>"
             "3. <strong>Nationality / origin</strong> — <em>Je suis… / Je viens de…</em><br>"
             "4. <strong>Family</strong> — <em>J'ai… / Je suis fils/fille unique.</em><br>"
             "5. <strong>Hobbies</strong> — <em>J'aime… / Je fais…</em>"),
            ("Name and Age",
             "Always use <em>je m'appelle</em> for your name and <em>avoir</em> for age.",
             "<em>Je m'appelle Lucas. J'ai dix-huit ans.</em><br>"
             "Remember: in French you <em>have</em> an age, not <em>be</em> one.<br>"
             "Wrong: ~~Je suis dix-huit ans.~~ ✗<br>"
             "Right: <em>J'ai dix-huit ans.</em> ✓"),
            ("Nationality and Origin",
             "Use <em>être</em> for nationality. Nationalities <strong>agree in gender</strong>.",
             "<em>Je suis anglais.</em> (m.) / <em>Je suis anglaise.</em> (f.)<br>"
             "<em>Je suis espagnol / espagnole.</em><br>"
             "<em>Je viens de Londres.</em> — I come from London.<br>"
             "<em>Je viens d'Australie.</em> — I come from Australia."),
            ("Family and Living Situation",
             "Keep it simple with <em>avoir</em> + family members.",
             "<em>J'ai un frère et une sœur.</em><br>"
             "<em>Je suis fils unique.</em> (m.) / <em>Je suis fille unique.</em> (f.)<br>"
             "<em>J'habite à Bristol avec ma famille.</em><br>"
             "<em>Je vis dans un appartement.</em>"),
            ("Hobbies and Likes",
             "Use <em>j'aime + noun/infinitive</em> or <em>je fais de…</em>.",
             "<em>J'aime la musique et les films.</em><br>"
             "<em>Je joue au football le week-end.</em><br>"
             "<em>J'adore lire et regarder des séries.</em><br>"
             "<em>Je fais de la natation.</em> — I swim."),
            ("Putting It Together — Model Text",
             "Here is a complete 60-word self-introduction at A1 level.",
             "<em>Bonjour ! Je m'appelle Emma. J'ai seize ans et je suis anglaise. Je viens de Manchester. J'ai deux frères — ils s'appellent Tom et Jack. J'habite dans une grande maison avec ma famille. J'aime la musique, les animaux et le sport. Je joue au tennis le samedi. Enchanté(e) de vous rencontrer !</em>"),
        ],
        "traps": [
            ("I am 18 years old", "J'ai dix-huit ans", "Avoir for age — never être."),
            ("I am English (female)", "Je suis anglaise", "Nationality adjectives agree in gender."),
            ("I live in Paris", "J'habite à Paris", "Habiter + à + city."),
            ("I like to read", "J'aime lire", "Aimer + infinitive (no 'to' needed)."),
        ],
        "summary": [
            ("name", "Je m'appelle…", "Je m'appelle Sophie."),
            ("age", "J'ai … ans.", "J'ai vingt ans."),
            ("nationality (m/f)", "Je suis anglais / anglaise.", "Je suis français / française."),
            ("origin", "Je viens de + city/country", "Je viens de Londres."),
            ("family", "J'ai … frère(s)/sœur(s).", "J'ai un frère et deux sœurs."),
            ("home", "J'habite à… / Je vis dans…", "J'habite à Paris."),
            ("hobbies", "J'aime + noun / infinitive", "J'aime le foot et la lecture."),
            ("joining up", "et, aussi, mais", "J'aime la musique mais je n'aime pas le sport."),
        ],
        "ex1": ("Exercise 1 — Choose the correct form",
                "Select the right option for each gap.",
                [
                    ("___ Marie. (My name is)", ["Je m'appelle", "Je suis", "J'ai", "J'habite"], "Je m'appelle",
                     "Je m'appelle = my name is; not je suis."),
                    ("___ vingt ans. (I am 20)", ["J'ai", "Je suis", "Je m'appelle", "J'habite"], "J'ai",
                     "Avoir for age in French."),
                    ("Je suis ___ (female, from England)", ["anglais", "anglaise", "l'anglais", "england"], "anglaise",
                     "Nationality adjective — feminine form anglaise."),
                    ("Je viens ___ Paris. (I come from Paris)", ["à", "de", "en", "au"], "de",
                     "Venir de + city."),
                    ("J'aime ___ football. (I like football)", ["le", "du", "au", "de"], "le",
                     "Aimer + le/la/les + sport."),
                ]),
        "ex2": ("Exercise 2 — Translate into French",
                "Type the French sentence.",
                [
                    ("My name is Sam.", "Je m'appelle Sam.", "Je m'appelle for name."),
                    ("I am 19 years old.", "J'ai dix-neuf ans.", "Avoir for age."),
                    ("I live in London.", "J'habite à Londres.", "Habiter + à + city."),
                    ("I have two sisters.", "J'ai deux sœurs.", "Avoir for family."),
                    ("I like music and sport.", "J'aime la musique et le sport.", "Aimer + article."),
                ]),
        "ex3": ("Exercise 3 — Error correction",
                "Pick the correct sentence.",
                [
                    ("'I am 16 years old' in French:", ["Je suis seize ans.", "J'ai seize ans.", "Je me suis seize ans.", "J'ai seize."], "J'ai seize ans.",
                     "Avoir for age — never être; include ans."),
                    ("'She is Spanish (female)' in French:", ["Elle est espagnol.", "Elle est espagnole.", "Elle est espagnols.", "Elle a espagnole."], "Elle est espagnole.",
                     "Nationality adjective in feminine form."),
                    ("'I come from Ireland' in French:", ["Je viens à Irlande.", "Je viens en Irlande.", "Je viens d'Irlande.", "Je suis d'Irlande."], "Je viens d'Irlande.",
                     "Venir de + country; d' before vowel."),
                    ("'I like to swim' in French:", ["J'aime à nager.", "J'aime de nager.", "J'aime nager.", "J'aime le nager."], "J'aime nager.",
                     "Aimer + infinitive directly — no preposition needed."),
                ]),
        "game_desc": "Practise the building blocks of a French self-introduction.",
        "items": [
            ("wi1", "Je m'appelle…", "My name is…", "name", "Je m'appelle Lucie, j'ai dix-huit ans.", "Complète: ___ Thomas. (my name is)", "Je m'appelle"),
            ("wi2", "J'ai … ans.", "I am … years old.", "age", "J'ai vingt et un ans et je suis étudiant.", "Complète: J'___ vingt ans. (I am 20)", "ai"),
            ("wi3", "Je suis + nationalité", "I am (nationality)", "nationality", "Je suis française. Je viens de Lyon.", "Complète: Je ___ anglais. (I am)", "suis"),
            ("wi4", "Je viens de…", "I come from…", "origin", "Je viens de Dublin, en Irlande.", "Complète: Je ___ de Manchester. (I come)", "viens"),
            ("wi5", "J'habite à…", "I live in…", "live", "J'habite à Paris depuis cinq ans.", "Complète: J'___ à Rome. (I live)", "habite"),
            ("wi6", "J'ai un/une/des…", "I have a… / I have…", "family", "J'ai un frère et deux sœurs.", "Complète: J'___ un frère. (I have)", "ai"),
            ("wi7", "J'aime…", "I like…", "like", "J'aime la musique et le sport.", "Complète: J'___ le football. (I like)", "aime"),
            ("wi8", "Je joue au / Je fais de…", "I play… / I do…", "hobby", "Je joue au tennis et je fais de la natation.", "Complète: Je ___ au football. (I play)", "joue"),
        ],
    },

    # ------------------------------------------------------------------ W02
    "describing-a-person": {
        "level": "a1", "section": "writing", "num": "W02",
        "short": "Describing a Person",
        "title": "Describing a Person",
        "subtitle": "Physical appearance, personality, and clothing",
        "slides": [
            ("Physical Appearance — Hair",
             "Use <em>avoir</em> to describe someone's physical features in French.",
             "<em>Il a les cheveux bruns.</em> — He has brown hair.<br>"
             "<em>Elle a les cheveux longs et blonds.</em> — She has long blonde hair.<br>"
             "<em>Il est chauve.</em> — He is bald.<br>"
             "Adjectives come <strong>after</strong> the noun (les cheveux <em>courts</em>)."),
            ("Physical Appearance — Eyes and Height",
             "Eyes: <em>avoir les yeux…</em> Height: <em>être grand(e) / petit(e)</em>.",
             "<em>Elle a les yeux verts.</em> — She has green eyes.<br>"
             "<em>Il a les yeux bleus et bruns.</em> — He has blue-brown eyes.<br>"
             "<em>Il est grand et mince.</em> — He is tall and slim.<br>"
             "<em>Elle est petite et mince.</em> — She is short and slim."),
            ("Personality Adjectives",
             "Personality adjectives follow <em>être</em> and must agree in gender/number.",
             "<em>Il est sympa / sympathique.</em> — He is nice.<br>"
             "<em>Elle est drôle.</em> — She is funny.<br>"
             "<em>Il est timide.</em> — He is shy.<br>"
             "<em>Elle est intelligente et travailleuse.</em> — She is intelligent and hard-working.<br>"
             "<em>Il est bavard.</em> — He is talkative."),
            ("Describing Clothes and Style",
             "Use <em>porter</em> to say what someone is wearing.",
             "<em>Il porte un jean bleu et un tee-shirt blanc.</em><br>"
             "<em>Elle porte une robe rouge et des chaussures noires.</em><br>"
             "Tip: colour adjectives go <strong>after</strong> the noun (un tee-shirt <em>rouge</em>)."),
            ("Putting It Together — Model Description",
             "A complete A1 description of a person.",
             "<em>Mon ami s'appelle Théo. Il a dix-sept ans. Il est grand et mince, avec les cheveux bruns et courts. Il a les yeux noirs. Il est sympa et drôle. Il aime le sport et la musique. Aujourd'hui, il porte un pull vert et un jean gris.</em>"),
            ("Avoiding Common Mistakes",
             "Three key traps when describing people.",
             "1. <strong>avoir not être for physical features:</strong><br>"
             "   <em>Il a les cheveux noirs.</em> ✓ (NOT ~~Il est les cheveux noirs~~) ✗<br>"
             "2. <strong>Adjective agreement:</strong><br>"
             "   <em>Elle est intelligente.</em> ✓ (NOT ~~Elle est intelligent~~) ✗<br>"
             "3. <strong>Adjective position after noun:</strong><br>"
             "   <em>un tee-shirt rouge</em> ✓ (NOT ~~un rouge tee-shirt~~) ✗"),
        ],
        "traps": [
            ("He has brown hair", "Il a les cheveux bruns", "Use avoir, not être, for physical features."),
            ("She is nice (personality)", "Elle est sympa / sympathique", "Personality = être + adjective."),
            ("a red shirt", "un tee-shirt rouge", "Colour adjectives come after the noun."),
            ("She is intelligent (female)", "Elle est intelligente", "Adjective must agree in gender."),
        ],
        "summary": [
            ("hair", "avoir les cheveux + adj.", "Il a les cheveux bruns et courts."),
            ("eyes", "avoir les yeux + colour", "Elle a les yeux bleus."),
            ("height/build", "être + grand/petit/mince", "Il est grand et mince."),
            ("personality", "être + adj. (agreed)", "Elle est sympa et intelligente."),
            ("clothes", "porter + article + noun + colour", "Il porte un jean bleu."),
            ("adj. agreement", "masc. / fém. (-e) / pl. (-s)", "Il est content / Elle est contente."),
            ("adj. position", "after noun (except BAGS)", "une robe rouge · un grand homme"),
            ("linking", "et, mais, aussi, avec", "Il est sympa mais un peu timide."),
        ],
        "ex1": ("Exercise 1 — Choose the correct form",
                "Select the right answer.",
                [
                    ("Elle ___ les yeux verts. (She has green eyes)", ["a", "est", "ai", "avons"], "a",
                     "avoir for physical features — elle → a."),
                    ("Il est ___. (He is tall — masculine)", ["grande", "grands", "grand", "grandes"], "grand",
                     "Masculine singular → grand."),
                    ("Elle est ___. (She is nice)", ["sympa", "sympas", "sympathiques", "sympathique"], "sympathique",
                     "Feminine singular — sympa or sympathique are both correct."),
                    ("Il porte un tee-shirt ___. (colour after noun)", ["rouge tee-shirt", "rouge", "rouges", "de rouge"], "rouge",
                     "Colour adjective after the noun."),
                    ("Elle est intelligente et ___. (hard-working, f.)", ["travailleur", "travailleuse", "travailleuses", "travailleurs"], "travailleuse",
                     "Feminine form of travailleur → travailleuse."),
                ]),
        "ex2": ("Exercise 2 — Translate into French",
                "Type the French sentence.",
                [
                    ("She has blue eyes.", "Elle a les yeux bleus.", "Avoir for eyes; bleus agrees (plural masc.)."),
                    ("He is tall and slim.", "Il est grand et mince.", "Être for height/build."),
                    ("She is funny.", "Elle est drôle.", "Drôle is invariable (same form m/f)."),
                    ("He is wearing a blue shirt.", "Il porte une chemise bleue.", "Porter; chemise is feminine → bleue."),
                    ("She has long brown hair.", "Elle a les cheveux longs et bruns.", "Avoir; adjectives after noun, agree plural."),
                ]),
        "ex3": ("Exercise 3 — Spot the mistake",
                "Pick the correct sentence.",
                [
                    ("'He has black hair':", ["Il est les cheveux noirs.", "Il a les cheveux noirs.", "Il a cheveux noirs.", "Il a le cheveux noirs."], "Il a les cheveux noirs.",
                     "Avoir (not être); les cheveux (always plural with article)."),
                    ("'She is intelligent' (female):", ["Elle est intelligent.", "Elle est intelligente.", "Elle a intelligente.", "Elle est intelligents."], "Elle est intelligente.",
                     "Être + adjective; feminine → intelligente."),
                    ("'a green dress' in French:", ["une verte robe", "une robe vertes", "une robe verte", "un robe vert"], "une robe verte",
                     "Noun before colour; robe is feminine → verte."),
                    ("'He is wearing white shoes':", ["Il porte des chaussures blanches.", "Il porte des chaussures blanc.", "Il porte des blanches chaussures.", "Il a des chaussures blanches."], "Il porte des chaussures blanches.",
                     "Porter for wearing; chaussures is feminine plural → blanches."),
                ]),
        "game_desc": "Practise describing people's appearance, personality, and clothing in French.",
        "items": [
            ("wd1", "avoir les cheveux…", "to have … hair", "hair", "Il a les cheveux bruns et courts.", "Complète: Elle a les ___ longs. (hair)", "cheveux"),
            ("wd2", "avoir les yeux…", "to have … eyes", "eyes", "Elle a les yeux bleus et le sourire facile.", "Complète: Il a les ___ verts. (eyes)", "yeux"),
            ("wd3", "être grand(e) / petit(e)", "to be tall / short", "tall", "Il est grand et sportif.", "Complète: Elle est ___. (tall, f.)", "grande"),
            ("wd4", "être sympa / sympathique", "to be nice", "nice", "Il est sympa et toujours de bonne humeur.", "Complète: Elle est ___. (nice, invariable)", "sympa"),
            ("wd5", "être drôle", "to be funny", "funny", "Il est drôle — il fait rire tout le monde.", "Complète: Elle est ___ et sympa. (funny)", "drôle"),
            ("wd6", "porter un/une…", "to be wearing a…", "wearing", "Elle porte une robe rouge et des sandales.", "Complète: Il ___ un jean bleu. (is wearing)", "porte"),
            ("wd7", "adj. agreement (f.)", "add -e for feminine", "feminine", "Elle est intelligente et travailleuse.", "Complète: Elle est travaille___. (feminine suffix)", "use"),
            ("wd8", "adj. after noun", "colour after noun", "after", "Elle porte une robe verte. Il a un sac bleu.", "Complète: une chemise ___. (white, f.)", "blanche"),
        ],
    },

    # ------------------------------------------------------------------ W03
    "my-daily-routine": {
        "level": "a1", "section": "writing", "num": "W03",
        "short": "My Daily Routine",
        "title": "My Daily Routine",
        "subtitle": "Describing daily activities with time expressions",
        "slides": [
            ("Reflexive Verbs — Daily Routines",
             "Many daily routine verbs are <strong>reflexive</strong> in French — they include a reflexive pronoun (me, te, se…).",
             "<em>se lever</em> — to get up<br>"
             "<em>se laver</em> — to wash<br>"
             "<em>se brosser les dents</em> — to brush teeth<br>"
             "<em>se coucher</em> — to go to bed<br>"
             "<em>Je me lève à 7h.</em> — I get up at 7."),
            ("Time Expressions",
             "Use these to organise your routine chronologically.",
             "<em>le matin</em> — in the morning<br>"
             "<em>l'après-midi</em> — in the afternoon<br>"
             "<em>le soir</em> — in the evening<br>"
             "<em>à… heures</em> — at… o'clock<br>"
             "<em>d'abord</em> — first<br>"
             "<em>ensuite / puis</em> — then / next<br>"
             "<em>enfin</em> — finally"),
            ("Regular Routine Verbs",
             "These non-reflexive verbs are also common in routines.",
             "<em>prendre le petit-déjeuner</em> — to have breakfast<br>"
             "<em>aller au collège / lycée / travail</em> — to go to school / work<br>"
             "<em>déjeuner</em> — to have lunch<br>"
             "<em>rentrer à la maison</em> — to go home<br>"
             "<em>dîner</em> — to have dinner<br>"
             "<em>regarder la télé</em> — to watch TV"),
            ("Structuring Your Text",
             "A simple four-part plan for a daily routine paragraph.",
             "1. <strong>Morning</strong> — getting up, breakfast, leaving<br>"
             "2. <strong>School / Work</strong> — schedule, lunch<br>"
             "3. <strong>Afternoon / Evening</strong> — activities, sport, homework<br>"
             "4. <strong>Night</strong> — dinner, wind-down, bedtime"),
            ("Model Routine — 80 Words",
             "A complete A1 daily routine text.",
             "<em>Le matin, je me lève à sept heures. Je me douche et je prends le petit-déjeuner — du pain grillé avec du café. Ensuite, je vais au lycée à pied. Je déjeune à la cantine à midi. L'après-midi, j'ai cours jusqu'à dix-sept heures. Le soir, je rentre à la maison, je fais mes devoirs et je dîne avec ma famille. Enfin, je me couche vers vingt-deux heures. Je lis un peu avant de dormir.</em>"),
            ("Quick Summary",
             "Key patterns for your routine text.",
             "• Reflexive verbs: <em>je me lève / je me couche</em>.<br>"
             "• Time markers: d'abord → ensuite → enfin.<br>"
             "• Link clauses with <em>et, puis, après</em>.<br>"
             "• Say what time things happen: <em>à 7h, vers 22h</em>."),
        ],
        "traps": [
            ("I get up at 7", "Je me lève à sept heures", "Reflexive verb — je me lève."),
            ("then / next", "ensuite / puis", "Both mean 'then'; avoid using 'après' as a standalone connector."),
            ("I go to school", "je vais au collège / lycée", "Aller + au + masculine place."),
            ("I brush my teeth", "Je me brosse les dents", "Reflexive + definite article les (not my)."),
        ],
        "summary": [
            ("getting up", "je me lève", "Je me lève à sept heures."),
            ("washing", "je me douche / je me lave", "Je me douche à sept heures et demie."),
            ("breakfast", "je prends le petit-déjeuner", "Je prends le petit-déjeuner à huit heures."),
            ("going to school", "je vais au lycée / collège", "Je vais au lycée en bus."),
            ("lunch", "je déjeune", "Je déjeune à la cantine à midi."),
            ("coming home", "je rentre à la maison", "Je rentre à la maison à 17h."),
            ("dinner", "je dîne", "Je dîne avec ma famille à 20h."),
            ("going to bed", "je me couche", "Je me couche à 22h30."),
        ],
        "ex1": ("Exercise 1 — Choose the correct verb",
                "Select the right form.",
                [
                    ("Je ___ à 7h. (I get up)", ["me lève", "me lever", "me couche", "suis levé"], "me lève",
                     "Se lever conjugated: je me lève."),
                    ("Je ___ le petit-déjeuner. (I have breakfast)", ["prends", "prenons", "prend", "prendre"], "prends",
                     "Prendre: je → prends."),
                    ("D'abord, puis, ___. (sequence)", ["avant", "enfin", "après", "déjà"], "enfin",
                     "D'abord → puis → enfin (first → then → finally)."),
                    ("Je me couche ___ 22h. (at/around)", ["à", "vers", "de", "en"], "vers",
                     "Vers = around/approximately (a time)."),
                    ("Je ___ à la maison à 17h. (I go home)", ["rentre", "vais", "retourne", "arrive"], "rentre",
                     "Rentrer à la maison = to go home."),
                ]),
        "ex2": ("Exercise 2 — Translate into French",
                "Type the French sentence.",
                [
                    ("I get up at 6:30.", "Je me lève à six heures et demie.", "Se lever; et demie."),
                    ("I have breakfast at 7.", "Je prends le petit-déjeuner à sept heures.", "Prendre le petit-déjeuner."),
                    ("Then I go to school.", "Ensuite, je vais au collège / lycée.", "Ensuite + aller au."),
                    ("I have dinner with my family.", "Je dîne avec ma famille.", "Dîner + avec."),
                    ("I go to bed at 10pm.", "Je me couche à vingt-deux heures.", "Se coucher; 22h."),
                ]),
        "ex3": ("Exercise 3 — Sequence the routine",
                "Which order is correct?",
                [
                    ("Which sequence is logical?",
                     ["Je me couche → Je me lève → Je prends le petit-déjeuner.",
                      "Je me lève → Je prends le petit-déjeuner → Je vais au lycée.",
                      "Je dîne → Je me lève → Je rentre à la maison.",
                      "Je vais au lycée → Je me lève → Je prends le petit-déjeuner."],
                     "Je me lève → Je prends le petit-déjeuner → Je vais au lycée.",
                     "Logical morning order: get up → breakfast → go to school."),
                    ("Which sentence uses the reflexive correctly?",
                     ["Je lève à 7h.", "Je me lève à 7h.", "Je me lever à 7h.", "Je me lèves à 7h."],
                     "Je me lève à 7h.",
                     "Je me lève — reflexive pronoun me + correct conjugation."),
                    ("Which time expression means 'finally'?",
                     ["d'abord", "ensuite", "puis", "enfin"],
                     "enfin",
                     "Enfin = finally; d'abord = first; ensuite/puis = then."),
                    ("'I brush my teeth' in French:",
                     ["Je brosse mes dents.", "Je me brosse les dents.", "Je me brosse mes dents.", "Je brosses les dents."],
                     "Je me brosse les dents.",
                     "Reflexive verb + les (definite article, not possessive)."),
                ]),
        "game_desc": "Practise French daily routine verbs and time expressions.",
        "items": [
            ("rout1", "je me lève", "I get up", "get up", "Je me lève à sept heures tous les jours.", "Complète: Je me ___ tôt. (get up)", "lève"),
            ("rout2", "je me douche", "I have a shower", "shower", "Je me douche après le sport.", "Complète: Je me ___ le matin. (shower)", "douche"),
            ("rout3", "je prends le petit-déjeuner", "I have breakfast", "breakfast", "Je prends le petit-déjeuner à huit heures.", "Complète: Je ___ le petit-déjeuner. (have)", "prends"),
            ("rout4", "je vais au lycée", "I go to school", "school", "Je vais au lycée en bus.", "Complète: Je vais au ___ à pied. (school)", "lycée"),
            ("rout5", "je déjeune", "I have lunch", "lunch", "Je déjeune à la cantine à midi.", "Complète: Je ___ à midi. (have lunch)", "déjeune"),
            ("rout6", "je rentre", "I go home / return", "go home", "Je rentre à la maison à dix-sept heures.", "Complète: Je ___ à la maison. (go home)", "rentre"),
            ("rout7", "je dîne", "I have dinner", "dinner", "Je dîne avec ma famille à vingt heures.", "Complète: Je ___ à 20h. (dine)", "dîne"),
            ("rout8", "je me couche", "I go to bed", "bed", "Je me couche à vingt-deux heures.", "Complète: Je me ___ tard. (go to bed)", "couche"),
        ],
    },

    # ------------------------------------------------------------------ W04
    "a-postcard": {
        "level": "a1", "section": "writing", "num": "W04",
        "short": "Writing a Postcard",
        "title": "Writing a Postcard",
        "subtitle": "Short informal messages — holidays, greetings, news",
        "slides": [
            ("Postcard Structure",
             "A French postcard has four sections. Keep it short — 50-80 words.",
             "1. <strong>Opening</strong> — <em>Cher Pierre, / Chère Marie,</em><br>"
             "2. <strong>Where you are & weather</strong> — <em>Je suis à… / Il fait…</em><br>"
             "3. <strong>What you're doing</strong> — present tense<br>"
             "4. <strong>Closing</strong> — <em>Grosses bises, / À bientôt,</em>"),
            ("Opening a Postcard",
             "Use the right form of 'Dear' depending on who you're writing to.",
             "<em>Cher + masculine name</em> → <em>Cher Paul,</em><br>"
             "<em>Chère + feminine name</em> → <em>Chère Marie,</em><br>"
             "<em>Chers amis,</em> → Dear friends (mixed/plural)<br>"
             "Alternative: <em>Salut !<br>Hello !<br>Bonjour !</em>"),
            ("Location and Weather",
             "Use present tense — describe where you are and what the weather is like.",
             "<em>Je suis à Nice, dans le sud de la France.</em><br>"
             "<em>Il fait très beau et très chaud.</em><br>"
             "<em>Nous sommes à la montagne, en Savoie.</em><br>"
             "<em>Il y a beaucoup de soleil.</em>"),
            ("Activities and Opinions",
             "Present tense verbs — what you are doing and how you feel about it.",
             "<em>Je visite les monuments et les musées.</em><br>"
             "<em>Nous mangeons bien — la cuisine est délicieuse !</em><br>"
             "<em>Je me repose à la plage chaque matin.</em><br>"
             "<em>C'est fantastique ! J'adore les vacances.</em>"),
            ("Closing a Postcard",
             "French closings for informal letters and postcards.",
             "<em>Grosses bises</em> — big kisses (very informal, family/close friends)<br>"
             "<em>Bisous</em> — kisses (informal)<br>"
             "<em>Amitiés</em> — kind regards (slightly more formal friends)<br>"
             "<em>À bientôt !</em> — see you soon<br>"
             "<em>À la prochaine !</em> — until next time"),
            ("Model Postcard — 70 Words",
             "A complete example at A1 level.",
             "<em>Cher Tom,</em><br><br>"
             "<em>Je suis à Marseille, dans le sud de la France ! Il fait beau et très chaud — trente degrés ! Je visite le Vieux-Port et je mange de la bouillabaisse. L'hôtel est confortable et la ville est magnifique. Nous allons à la plage demain matin.</em><br><br>"
             "<em>Grosses bises,<br>Sophie</em>"),
        ],
        "traps": [
            ("Dear Marie (female)", "Chère Marie", "Cher is masculine; chère is feminine."),
            ("I am in Paris", "Je suis à Paris", "Être + à + city."),
            ("the weather is nice", "il fait beau", "Faire for weather expressions."),
            ("kisses / love (close friends)", "Grosses bises / Bisous", "Never use 'amour' as a closing to friends."),
        ],
        "summary": [
            ("dear (m./f.)", "Cher / Chère + name", "Cher Paul, / Chère Marie,"),
            ("location", "Je suis à / Nous sommes à", "Je suis à Paris."),
            ("weather", "Il fait beau/chaud/froid / Il pleut", "Il fait 30 degrés !"),
            ("activities", "present tense verbs", "Je visite / je mange / nous allons"),
            ("opinions", "C'est + adj. / J'adore…", "C'est fantastique ! J'adore la plage."),
            ("close (informal)", "Grosses bises / Bisous", "Grosses bises, Emma"),
            ("close (semi-formal)", "Amitiés / À bientôt", "À bientôt, Sophie"),
            ("word count", "50-80 words for A1", "4 short paragraphs"),
        ],
        "ex1": ("Exercise 1 — Choose the correct opening",
                "Select the right form.",
                [
                    ("Writing to your female friend Léa:", ["Cher Léa,", "Chère Léa,", "Chers Léa,", "Chères Léa,"], "Chère Léa,",
                     "Léa is a female name → Chère."),
                    ("Writing to your male friend Paul:", ["Chère Paul,", "Cher Paul,", "Chers Paul,", "Salut Paul"], "Cher Paul,",
                     "Paul is male → Cher."),
                    ("'The weather is lovely' in French:", ["Il est beau.", "Le temps est beau.", "Il fait beau.", "C'est beau le temps."], "Il fait beau.",
                     "Il fait + weather adjective."),
                    ("'I am in Lyon' in French:", ["Je suis en Lyon.", "J'habite à Lyon.", "Je suis à Lyon.", "Je vais à Lyon."], "Je suis à Lyon.",
                     "Être + à + city for current location."),
                    ("Best closing for a postcard to a close friend:", ["Cordialement,", "Sincèrement,", "Grosses bises,", "Veuillez agréer…"], "Grosses bises,",
                     "Grosses bises is warm and informal — perfect for friends."),
                ]),
        "ex2": ("Exercise 2 — Translate into French",
                "Type the French phrase.",
                [
                    ("Dear Sophie,", "Chère Sophie,", "Sophie is a female name → Chère."),
                    ("I am in Rome.", "Je suis à Rome.", "Être + à + city."),
                    ("The weather is hot.", "Il fait chaud.", "Il fait + adjective."),
                    ("I visit the museums.", "Je visite les musées.", "Visiter + les."),
                    ("Big kisses, Emma.", "Grosses bises, Emma.", "Standard postcard closing."),
                ]),
        "ex3": ("Exercise 3 — Order the postcard",
                "Which structure is correct for a postcard?",
                [
                    ("Correct postcard order:",
                     ["Opening → Closing → Activities → Location",
                      "Closing → Opening → Weather → Activities",
                      "Opening → Location & weather → Activities → Closing",
                      "Activities → Location → Closing → Opening"],
                     "Opening → Location & weather → Activities → Closing",
                     "Standard postcard structure: open → set scene → tell news → close."),
                    ("Which sentence gives a location correctly?",
                     ["Je suis en Paris.", "Je suis au Paris.", "Je suis à Paris.", "Je suis Paris."],
                     "Je suis à Paris.",
                     "Cities → être + à."),
                    ("Which closing is NOT appropriate for a close friend?",
                     ["Grosses bises,", "Bisous,", "À bientôt,", "Veuillez agréer, Monsieur, l'expression de mes sentiments distingués,"],
                     "Veuillez agréer, Monsieur, l'expression de mes sentiments distingués,",
                     "That formula is very formal business French — not for postcards."),
                    ("'The food is delicious !' in French:",
                     ["La cuisine est délicieuse !", "Le cuisine est délicieux !", "La nourriture est délicieuse !", "Both A and C are correct"],
                     "Both A and C are correct",
                     "La cuisine and la nourriture both mean 'food' — both are correct."),
                ]),
        "game_desc": "Practise the language of informal postcards and holiday messages.",
        "items": [
            ("pc1", "Cher / Chère", "Dear (m. / f.)", "dear", "Chère Marie, je t'écris de Rome !", "Complète: ___ Paul, (dear, m.)", "Cher"),
            ("pc2", "Je suis à…", "I am in… (city)", "in", "Je suis à Nice — il fait très beau !", "Complète: Je ___ à Paris. (I am)", "suis"),
            ("pc3", "il fait beau/chaud", "the weather is nice/hot", "weather", "Il fait beau et très chaud — 32 degrés !", "Complète: Il fait ___ ici. (nice weather)", "beau"),
            ("pc4", "je visite", "I visit", "visit", "Je visite le Louvre et la Tour Eiffel.", "Complète: Je ___ les monuments. (I visit)", "visite"),
            ("pc5", "C'est fantastique !", "It's fantastic!", "fantastic", "La ville est magnifique — c'est fantastique !", "Complète: C'est ___! (fantastic)", "fantastique"),
            ("pc6", "je mange bien", "I eat well", "food", "Je mange bien — la cuisine est délicieuse !", "Complète: Je ___ bien ici. (I eat)", "mange"),
            ("pc7", "Grosses bises", "big kisses (close)", "kisses", "Grosses bises et à bientôt !", "Complète: ___ bises, (closing)", "Grosses"),
            ("pc8", "À bientôt !", "See you soon!", "soon", "À bientôt — je rentre dimanche !", "Complète: À ___ ! (see you soon)", "bientôt"),
        ],
    },
}
