"""
francais-en A2 Writing W01–W04  (French for English Speakers)
Generator: gen_francais_en.py
"""

CHAPTERS = {

    # ------------------------------------------------------------------ W01
    "informal-email": {
        "level": "a2", "section": "writing", "num": "W01",
        "short": "Informal Email",
        "title": "Writing an Informal Email",
        "subtitle": "Catching up, sharing news, and making plans",
        "slides": [
            ("Email Structure at A2",
             "A French informal email has five components.",
             "1. <strong>Subject line</strong> — <em>Objet :</em><br>"
             "2. <strong>Opening</strong> — <em>Salut Thomas, / Bonjour Marie,</em><br>"
             "3. <strong>Reason for writing</strong> — <em>Je t'écris pour…</em><br>"
             "4. <strong>Main content</strong> — news, question, plan<br>"
             "5. <strong>Closing</strong> — <em>À bientôt, / Bisous,</em>"),
            ("Opening an Informal Email",
             "Use tu form for friends. The opening sets the tone.",
             "<em>Salut Lucas !</em> (very informal)<br>"
             "<em>Bonjour Marie,</em> (slightly warmer)<br>"
             "<em>Coucou !</em> (very casual, close friends)<br>"
             "Ask how they are: <em>Comment vas-tu ? / Ça va ?</em>"),
            ("Sharing Past News",
             "Use the <strong>passé composé</strong> to say what you did.",
             "<em>Ce week-end, je suis allé(e) à la mer.</em><br>"
             "<em>Nous avons mangé dans un super restaurant.</em><br>"
             "<em>J'ai rencontré quelqu'un d'intéressant !</em><br>"
             "Time markers: <em>hier, ce week-end, la semaine dernière, samedi</em>"),
            ("Making Plans / Future",
             "Use the futur proche or future simple for plans.",
             "<em>On va aller au cinéma samedi soir.</em><br>"
             "<em>Est-ce que tu peux venir ?</em> — Can you come?<br>"
             "<em>Je serai là à 19h.</em> — I'll be there at 7pm.<br>"
             "<em>On se retrouve où ?</em> — Where shall we meet?"),
            ("Closing an Informal Email",
             "End warmly and invite a reply.",
             "<em>Donne-moi des nouvelles !</em> — Give me your news!<br>"
             "<em>Réponds-moi vite !</em> — Reply quickly!<br>"
             "<em>À bientôt !</em> / <em>À la prochaine !</em><br>"
             "<em>Bisous,</em> / <em>Gros bisous,</em> / <em>Amicalement,</em>"),
            ("Model Email — 90 Words",
             "Complete example at A2 level.",
             "<em>Objet : Week-end au lac</em><br><br>"
             "<em>Salut Emma !<br><br>"
             "Comment vas-tu ? Moi, je suis un peu fatigué(e) mais très content(e) !<br><br>"
             "Ce week-end, je suis allé(e) au lac avec ma famille. On a nagé et on a fait du bateau. Le temps était magnifique — du soleil et 28 degrés ! Le soir, nous avons mangé dans un restaurant au bord de l'eau. C'était vraiment sympa !<br><br>"
             "Et toi, qu'est-ce que tu as fait ? On se retrouve samedi prochain ?<br><br>"
             "Bisous,<br>Sophie</em>"),
        ],
        "traps": [
            ("Yesterday I went (informal email)", "Hier, je suis allé(e)", "Passé composé for past events; aller uses être."),
            ("Can you come?", "Est-ce que tu peux venir ?", "Tu form with friends; peux (not peut)."),
            ("The weather was nice", "Le temps était beau / magnifique", "Imparfait for description in the past."),
            ("Give me your news (informal)", "Donne-moi des nouvelles !", "Imperative tu form; des nouvelles."),
        ],
        "summary": [
            ("opening", "Salut / Bonjour + name", "Salut Emma ! · Bonjour Lucas,"),
            ("ask how they are", "Comment vas-tu ? / Ça va ?", "Comment vas-tu ? Moi, je vais bien !"),
            ("past events", "PC — j'ai / je suis + PP", "Je suis allé(e) au cinéma hier."),
            ("descriptions in past", "imparfait — c'était, il faisait", "C'était super ! Il faisait beau."),
            ("future plans", "futur proche — je vais + inf.", "On va aller au restaurant samedi."),
            ("invite to reply", "Réponds-moi / Donne-moi des nouvelles", "Réponds-moi vite !"),
            ("closing", "Bisous / À bientôt / Amicalement", "À bientôt ! Bisous, Sophie"),
            ("tu vs vous", "tu for friends", "Qu'est-ce que tu as fait ?"),
        ],
        "ex1": ("Exercise 1 — Choose the right form",
                "Select the correct answer for each gap.",
                [
                    ("Opening to your friend Léa:", ["Chère Madame Léa,", "Salut Léa !", "Veuillez agréer, Léa,", "À l'attention de Léa"], "Salut Léa !",
                     "Informal email to a friend → Salut + first name."),
                    ("'Last weekend I went to Paris' in PC:", ["La semaine dernière j'allais à Paris.", "Le week-end dernier, je suis allé(e) à Paris.", "Hier, j'ai été à Paris.", "La semaine dernière, j'ai allé à Paris."], "Le week-end dernier, je suis allé(e) à Paris.",
                     "PC: aller uses être → je suis allé(e)."),
                    ("The description 'the weather was great':", ["Le temps a été beau.", "Il a fait beau.", "C'était magnifique.", "Both B and C are correct"], "Both B and C are correct",
                     "Both PC and imparfait describe past weather — both natural here."),
                    ("Closing for a close friend:", ["Cordialement,", "À bientôt ! Bisous,", "Veuillez agréer…", "Sincèrement,"], "À bientôt ! Bisous,",
                     "Bisous is warm and casual — right for close friends."),
                    ("'Can you come on Saturday?'", ["Est-ce que vous pouvez venir samedi ?", "Est-ce que tu peux venir samedi ?", "Pouvez-vous venir samedi ?", "Peux-vous venir samedi ?"], "Est-ce que tu peux venir samedi ?",
                     "Friend → tu form; peux-tu OR est-ce que tu peux."),
                ]),
        "ex2": ("Exercise 2 — Translate into French",
                "Type the French phrase.",
                [
                    ("Hi Emma!", "Salut Emma !", "Informal opening."),
                    ("Last weekend I went to the beach.", "Le week-end dernier, je suis allé(e) à la plage.", "PC: aller → être."),
                    ("It was fantastic!", "C'était fantastique !", "Imparfait for description."),
                    ("See you soon!", "À bientôt !", "Casual closing."),
                    ("Give me your news!", "Donne-moi des nouvelles !", "Imperative tu form."),
                ]),
        "ex3": ("Exercise 3 — Spot the mistake",
                "Pick the correct sentence.",
                [
                    ("'I went to the cinema last week' in PC:", ["Je suis allé au cinéma la semaine dernière.", "J'ai allé au cinéma la semaine dernière.", "Je suis allé le cinéma la semaine dernière.", "J'ai été au cinéma la semaine dernière."], "Je suis allé au cinéma la semaine dernière.",
                     "Aller uses être in PC; au cinéma."),
                    ("Which closing is correct for a friend?", ["Veuillez agréer mes salutations.", "Bisous, Marc", "Cordialement,", "Je vous prie d'agréer…"], "Bisous, Marc",
                     "Bisous is appropriate for informal emails to friends."),
                    ("'The film was great':", ["Le film a été super.", "Le film était super.", "Le film est été super.", "Le film a super."], "Le film était super.",
                     "Imparfait for descriptions in the past."),
                    ("'Can you come?' to a friend:", ["Est-ce que vous pouvez venir ?", "Est-ce que tu peux venir ?", "Est-ce que tu peut venir ?", "Pouvez-vous venir ?"], "Est-ce que tu peux venir ?",
                     "Friend → tu; pouvoir: tu → peux."),
                ]),
        "game_desc": "Practise informal email conventions — past events, plans, and closings.",
        "items": [
            ("em1", "Salut + name !", "Hi [name]! (informal opening)", "hi", "Salut Thomas ! Comment vas-tu ?", "Complète: ___ Emma ! (opening)", "Salut"),
            ("em2", "je suis allé(e)", "I went (PC, aller+être)", "I went", "Je suis allé(e) au cinéma samedi.", "Complète: Je ___ allé au lac. (went)", "suis"),
            ("em3", "c'était", "it was (imparfait description)", "it was", "C'était fantastique — un super week-end !", "Complète: C'___ super ! (it was)", "était"),
            ("em4", "on va + inf.", "we're going to (near future)", "plan", "On va aller au restaurant samedi soir.", "Complète: On va ___ au cinéma. (go)", "aller"),
            ("em5", "est-ce que tu peux ?", "can you? (informal)", "can you", "Est-ce que tu peux venir samedi soir ?", "Complète: Tu ___ venir ? (can, tu)", "peux"),
            ("em6", "la semaine dernière", "last week", "last week", "La semaine dernière, j'ai vu un film super.", "Complète: ___ dernière, j'ai visité Paris. (last week)", "la semaine"),
            ("em7", "Donne-moi des nouvelles !", "Give me your news!", "your news", "Donne-moi des nouvelles — j'attends ta réponse !", "Complète: Donne-moi des ___! (news)", "nouvelles"),
            ("em8", "À bientôt / Bisous", "See you soon / Kisses", "closing", "À bientôt ! Bisous, Sophie", "Complète: À ___! (see you soon)", "bientôt"),
        ],
    },

    # ------------------------------------------------------------------ W02
    "telling-a-story": {
        "level": "a2", "section": "writing", "num": "W02",
        "short": "Telling a Story",
        "title": "Telling a Story in the Past",
        "subtitle": "Combining passé composé and imparfait",
        "slides": [
            ("Two Past Tenses — Two Jobs",
             "The key to narrating in French: use the right tense for the right job.",
             "<strong>Passé composé</strong> → actions that move the story forward:<br>"
             "<em>Elle est entrée, elle a regardé la salle et elle s'est assise.</em><br><br>"
             "<strong>Imparfait</strong> → background, descriptions, feelings, habits:<br>"
             "<em>Il faisait beau. La musique jouait. Elle était nerveuse.</em>"),
            ("PC: Moving the Plot",
             "Use the passé composé (PC) for events that happened once and advance the narrative.",
             "Signal words: <em>soudain, tout à coup, d'abord, puis, ensuite, enfin</em><br>"
             "<em>D'abord, il est sorti de la maison.</em> — First, he left the house.<br>"
             "<em>Puis il a vu une voiture bizarre.</em> — Then he saw a strange car.<br>"
             "<em>Soudain, la voiture a démarré.</em> — Suddenly, the car started."),
            ("Imparfait: Setting the Scene",
             "Use the imparfait for background, simultaneous actions, and descriptions.",
             "Signal words: <em>pendant que, alors que, quand, d'habitude, souvent, chaque…</em><br>"
             "<em>Il pleuvait et il faisait froid.</em> — It was raining and it was cold.<br>"
             "<em>Les enfants jouaient dans la rue.</em> — The children were playing in the street.<br>"
             "<em>Elle lisait pendant que lui regardait la télé.</em> — She was reading while he watched TV."),
            ("Linking Words for Stories",
             "Good narration uses connectors to sequence and contrast events.",
             "<em>d'abord</em> — first · <em>ensuite / puis</em> — then<br>"
             "<em>enfin / finalement</em> — finally<br>"
             "<em>soudain / tout à coup</em> — suddenly<br>"
             "<em>pendant que</em> — while · <em>quand</em> — when<br>"
             "<em>mais</em> — but · <em>cependant</em> — however"),
            ("Model Story — 90 Words",
             "Complete past narrative at A2 level.",
             "<em>Hier, je me promenais dans le parc quand j'ai entendu un cri. Il faisait beau et les enfants jouaient. D'abord, j'ai regardé autour de moi mais je n'ai rien vu. Soudain, un petit garçon a couru vers moi. Il pleurait et il cherchait sa mère. Je l'ai aidé et nous avons trouvé sa mère près de l'entrée. Elle était soulagée ! Le garçon a souri et m'a dit merci. C'était une belle fin !</em>"),
            ("Quick Summary",
             "PC vs. imparfait in a nutshell.",
             "• <strong>PC</strong> = action (moves story forward): il a couru, j'ai vu<br>"
             "• <strong>Imparfait</strong> = description/background: il faisait beau, elle pleurait<br>"
             "• <strong>PC inside imparfait</strong>: <em>Je lisais quand il est entré.</em><br>"
             "• Use connectors: d'abord → puis → soudain → enfin."),
        ],
        "traps": [
            ("It was raining (background)", "Il pleuvait", "Background description → imparfait."),
            ("suddenly he ran (plot action)", "tout à coup, il a couru", "Plot action → passé composé."),
            ("she was reading (ongoing)", "elle lisait", "Ongoing background action → imparfait."),
            ("I heard a noise (sudden event)", "j'ai entendu un bruit", "One-off event → passé composé."),
        ],
        "summary": [
            ("PC use", "completed / one-off actions", "Il a crié. Elle est partie."),
            ("imparfait use", "background / description", "Il faisait beau. Elle était triste."),
            ("PC inside imparfait", "je + imparfait + quand + PC", "Je dormais quand il a sonné."),
            ("d'abord", "first", "D'abord, je me suis levé."),
            ("ensuite / puis", "then / next", "Ensuite, j'ai pris le petit-déjeuner."),
            ("soudain / tout à coup", "suddenly", "Soudain, il a crié."),
            ("enfin / finalement", "finally / at last", "Enfin, nous avons trouvé la solution."),
            ("pendant que", "while (two simultaneous)", "Elle lisait pendant qu'il cuisinait."),
        ],
        "ex1": ("Exercise 1 — PC or imparfait?",
                "Select the correct tense form.",
                [
                    ("It was raining. → background description:", ["Il a plu.", "Il pleuvait.", "Il pleure.", "Il pleut."], "Il pleuvait.",
                     "Background description → imparfait."),
                    ("Suddenly she screamed. → plot action:", ["Soudain elle criait.", "Soudain elle a crié.", "Soudain elle crie.", "Soudain elle crierait."], "Soudain elle a crié.",
                     "Sudden plot action → passé composé."),
                    ("The children were playing (when...) → background:", ["Les enfants ont joué.", "Les enfants jouaient.", "Les enfants jouent.", "Les enfants ont été jouant."], "Les enfants jouaient.",
                     "Ongoing background activity → imparfait."),
                    ("Then I left. → plot:", ["Ensuite je partais.", "Ensuite j'ai parti.", "Ensuite je suis parti.", "Ensuite je partis."], "Ensuite je suis parti.",
                     "Plot action → PC; partir uses être."),
                    ("She was tired (description):", ["Elle a été fatiguée.", "Elle était fatiguée.", "Elle est fatiguée.", "Elle fut fatiguée."], "Elle était fatiguée.",
                     "Description/state → imparfait."),
                ]),
        "ex2": ("Exercise 2 — Translate into French",
                "Type the French sentence.",
                [
                    ("It was sunny.", "Il faisait beau. / Il y avait du soleil.", "Background → imparfait."),
                    ("Suddenly he ran.", "Soudain, il a couru.", "Sudden plot action → PC."),
                    ("I was reading when she arrived.", "Je lisais quand elle est arrivée.", "Ongoing (imparfait) + sudden event (PC)."),
                    ("First, he left the house.", "D'abord, il est sorti de la maison.", "Plot → PC; sortir uses être."),
                    ("It was a great day!", "C'était une super journée !", "Description/assessment → imparfait."),
                ]),
        "ex3": ("Exercise 3 — Spot the mistake",
                "Which sentence is correct?",
                [
                    ("Background: 'The music was playing':", ["La musique a joué.", "La musique jouait.", "La musique joue.", "La musique avait joué."], "La musique jouait.",
                     "Background sound → imparfait."),
                    ("Plot: 'Suddenly the door opened':", ["Soudain la porte s'ouvrait.", "Soudain la porte s'est ouverte.", "Soudain la porte a ouvert.", "Soudain la porte ouvrait."], "Soudain la porte s'est ouverte.",
                     "Sudden plot action → PC; s'ouvrir is reflexive → être."),
                    ("'I was sleeping when he called':", ["Je dormais quand il a appelé.", "J'ai dormi quand il a appelé.", "Je dormais quand il appelait.", "J'ai dormi quand il appelait."], "Je dormais quand il a appelé.",
                     "Ongoing (imparfait) + sudden interruption (PC)."),
                    ("Which connects two simultaneous actions?", ["d'abord", "soudain", "pendant que", "enfin"], "pendant que",
                     "Pendant que = while; connects two ongoing actions."),
                ]),
        "game_desc": "Practise telling stories in French — PC for plot, imparfait for background.",
        "items": [
            ("st1", "PC = action", "passé composé for plot events", "plot", "Il est entré et il a pris son café.", "Complète: Soudain il ___ couru. (a, has run)", "a"),
            ("st2", "imparfait = background", "imparfait for descriptions", "background", "Il faisait beau et les oiseaux chantaient.", "Complète: Il ___ beau. (was, faire)", "faisait"),
            ("st3", "je dormais quand…", "I was sleeping when… (imp.+PC)", "when", "Je dormais quand le téléphone a sonné.", "Complète: Je ___ quand il est entré. (was sleeping)", "dormais"),
            ("st4", "soudain", "suddenly (PC follows)", "suddenly", "Soudain, elle a entendu un bruit.", "Complète: ___, il a crié. (suddenly)", "Soudain"),
            ("st5", "d'abord … puis … enfin", "first … then … finally", "sequence", "D'abord j'ai mangé, puis j'ai travaillé, enfin je me suis couché.", "Complète: ___ j'ai mangé. (first)", "D'abord"),
            ("st6", "pendant que", "while (simultaneous)", "while", "Elle lisait pendant qu'il cuisinait.", "Complète: Il travaillait ___ elle dormait. (while)", "pendant que"),
            ("st7", "c'était", "it was (imparfait description)", "it was", "C'était une belle journée à la mer.", "Complète: C'___ génial ! (it was)", "était"),
            ("st8", "tout à coup", "all of a sudden", "suddenly", "Tout à coup, il a commencé à pleuvoir.", "Complète: ___ à coup, elle a crié. (all of)", "tout"),
        ],
    },

    # ------------------------------------------------------------------ W03
    "describing-a-place": {
        "level": "a2", "section": "writing", "num": "W03",
        "short": "Describing a Place",
        "title": "Describing a Place",
        "subtitle": "Describing a city, region, or tourist site",
        "slides": [
            ("How to Structure a Place Description",
             "A good A2 place description covers four angles.",
             "1. <strong>Location and overview</strong> — where, how big, general feel<br>"
             "2. <strong>Key features</strong> — monuments, nature, industry, history<br>"
             "3. <strong>What to do / see there</strong> — activities, sights<br>"
             "4. <strong>Your opinion</strong> — why you recommend it"),
            ("Location and Size Vocabulary",
             "Set the scene with position, size, and general character.",
             "<em>se trouver / être situé(e) à</em> — to be located at/in<br>"
             "<em>au nord/sud/est/ouest de</em> — in the north/south/east/west of<br>"
             "<em>au bord de la mer / de la rivière</em> — by the sea / river<br>"
             "<em>une grande / petite ville</em> — a large / small city<br>"
             "<em>une région</em> — a region · <em>le quartier</em> — the neighbourhood"),
            ("Key Features Vocabulary",
             "Describe what makes the place distinctive.",
             "<em>un monument historique</em> — a historic monument<br>"
             "<em>un château</em> — a castle / château<br>"
             "<em>une cathédrale</em> — a cathedral<br>"
             "<em>un paysage</em> — a landscape / scenery<br>"
             "<em>le patrimoine</em> — heritage<br>"
             "<em>la cuisine locale</em> — local food<br>"
             "<em>connu(e) pour</em> — famous for"),
            ("Activities and Recommendations",
             "What can visitors do?",
             "<em>visiter</em> — to visit · <em>se promener</em> — to walk around<br>"
             "<em>faire une excursion</em> — to go on a trip<br>"
             "<em>goûter</em> — to taste · <em>admirer</em> — to admire<br>"
             "<em>je vous recommande de…</em> — I recommend that you…<br>"
             "<em>il ne faut pas manquer</em> — you must not miss"),
            ("Expressing Opinions",
             "Include your personal view to make the text more engaging.",
             "<em>Je trouve que…</em> — I think that…<br>"
             "<em>À mon avis,…</em> — In my opinion,…<br>"
             "<em>Ce qui me plaît, c'est…</em> — What I like is…<br>"
             "<em>Le point fort est…</em> — The strong point is…<br>"
             "<em>Je recommande vivement…</em> — I highly recommend…"),
            ("Model Text — 100 Words",
             "A complete place description at A2 level.",
             "<em>Barcelone est une grande ville côtière du nord-est de l'Espagne. Elle est connue pour son architecture unique, notamment les œuvres de Gaudí comme la Sagrada Família. On peut aussi se promener sur la Rambla et admirer la vue depuis le Parc Güell.<br><br>"
             "Barcelone offre une cuisine délicieuse — les tapas, les fruits de mer et la paella sont à goûter absolument. La ville a un excellent réseau de métro, ce qui la rend facile à visiter.<br><br>"
             "À mon avis, c'est l'une des plus belles villes d'Europe. Je vous recommande vivement de la visiter !</em>"),
        ],
        "traps": [
            ("famous for", "connue pour", "Connue agrees (f. if referring to ville, connue; m. if ville is not stated: connu pour)."),
            ("you must not miss", "il ne faut pas manquer", "Il faut + infinitive; negation ne faut pas."),
            ("I recommend that you visit", "je vous recommande de visiter", "Recommander de + infinitive (not que + subjunctive at A2)."),
            ("in the north of", "au nord de", "Direction: au nord/sud/est/ouest + de."),
        ],
        "summary": [
            ("location", "se trouver à / être situé(e) à", "Lyon se trouve au sud-est de la France."),
            ("compass", "au nord/sud/est/ouest de", "au nord de Paris · au sud de l'Espagne"),
            ("famous for", "connu(e) pour + noun/inf.", "connu pour son architecture"),
            ("recommend", "je recommande de + inf.", "Je recommande de visiter le château."),
            ("must not miss", "il ne faut pas manquer", "Il ne faut pas manquer la cathédrale."),
            ("opinion", "À mon avis, / Je trouve que", "À mon avis, c'est magnifique."),
            ("activity", "on peut + inf.", "On peut se promener et visiter des musées."),
            ("description", "il y a / c'est un(e)", "Il y a un magnifique marché couvert."),
        ],
        "ex1": ("Exercise 1 — Choose the right expression",
                "Select the correct form.",
                [
                    ("Lyon ___ au sud-est de la France. (is located)", ["est situé", "se trouve", "est", "Both A and B are correct"], "Both A and B are correct",
                     "Both est situé and se trouve are correct for 'is located'."),
                    ("Paris est ___ pour la Tour Eiffel. (famous)", ["fameux", "connu", "connue", "connus"], "connue",
                     "La ville de Paris (f.) → connue pour."),
                    ("___ mon avis, c'est magnifique.", ["En", "À", "De", "Selon"], "À",
                     "À mon avis = in my opinion."),
                    ("Il ne faut pas ___ le Louvre. (miss)", ["manque", "manquer", "manqué", "manquez"], "manquer",
                     "Il ne faut pas + infinitive."),
                    ("'In the north of France':", ["dans le nord de la France", "au nord de la France", "en nord de la France", "Both A and B are correct"], "Both A and B are correct",
                     "Both au nord and dans le nord are used — au nord is more formal."),
                ]),
        "ex2": ("Exercise 2 — Translate into French",
                "Type the French phrase.",
                [
                    ("Paris is located in the north of France.", "Paris se trouve au nord de la France.", "Se trouver + au nord de."),
                    ("It is famous for its castles.", "Il/Elle est connu(e) pour ses châteaux.", "Connu + pour + noun."),
                    ("In my opinion, it's magnificent.", "À mon avis, c'est magnifique.", "À mon avis + c'est."),
                    ("You must not miss the cathedral.", "Il ne faut pas manquer la cathédrale.", "Il ne faut pas + infinitive."),
                    ("I recommend visiting the market.", "Je recommande de visiter le marché.", "Recommander de + infinitive."),
                ]),
        "ex3": ("Exercise 3 — Spot the mistake",
                "Which sentence is correct?",
                [
                    ("'Lyon is located south-east of Paris':", ["Lyon se trouve au sud-est de Paris.", "Lyon se trouve en sud-est de Paris.", "Lyon est situé du sud-est de Paris.", "Lyon se situe dans le sud-est Paris."], "Lyon se trouve au sud-est de Paris.",
                     "Direction: au + compass point + de + city."),
                    ("'The city is famous for its food':", ["La ville est connue pour sa cuisine.", "La ville est connu pour sa cuisine.", "La ville est fameux pour sa cuisine.", "La ville est connues pour sa cuisine."], "La ville est connue pour sa cuisine.",
                     "Ville is feminine → connue (agreed)."),
                    ("'I recommend visiting the museum':", ["Je recommande visiter le musée.", "Je recommande de visiter le musée.", "Je recommande que vous visitez le musée.", "Je vous recommande visiter le musée."], "Je recommande de visiter le musée.",
                     "Recommander de + infinitive."),
                    ("'What I like is the food':", ["Ce que j'aime, c'est la cuisine.", "Ce que j'aime, c'est la nourriture.", "Ce que j'aime c'est la cuisine.", "Both A and B are correct"], "Both A and B are correct",
                     "La cuisine and la nourriture both mean food — both correct."),
                ]),
        "game_desc": "Practise describing places — location, features, activities, opinions.",
        "items": [
            ("pl1", "se trouver à / être situé(e) à", "to be located at/in", "located", "Lyon se trouve au sud-est de la France.", "Complète: Paris ___ situé en France. (is)", "est"),
            ("pl2", "au nord/sud de", "in the north/south of", "compass", "La Bretagne se trouve à l'ouest de la France.", "Complète: Il est ___ nord de Paris. (to the)", "au"),
            ("pl3", "connu(e) pour", "famous for", "famous", "La région est connue pour ses vins.", "Complète: C'est ___ pour son histoire. (famous, masc.)", "connu"),
            ("pl4", "il y a", "there is / there are", "there is", "Il y a un château médiéval et une cathédrale.", "Complète: Il ___ un musée. (there is)", "y a"),
            ("pl5", "on peut + inf.", "you can / one can", "can visit", "On peut visiter le château et se promener.", "Complète: On ___ visiter. (can)", "peut"),
            ("pl6", "il ne faut pas manquer", "you must not miss", "don't miss", "Il ne faut pas manquer la vieille ville.", "Complète: Il ne faut pas ___. (miss)", "manquer"),
            ("pl7", "à mon avis", "in my opinion", "opinion", "À mon avis, c'est une ville magnifique.", "Complète: ___ mon avis, c'est super. (à)", "À"),
            ("pl8", "je recommande de", "I recommend (doing)", "recommend", "Je recommande de visiter la cathédrale.", "Complète: Je ___ de visiter. (recommend)", "recommande"),
        ],
    },

    # ------------------------------------------------------------------ W04
    "comparing-two-options": {
        "level": "a2", "section": "writing", "num": "W04",
        "short": "Comparing Options",
        "title": "Comparing Two Options",
        "subtitle": "Giving advantages, disadvantages, and a recommendation",
        "slides": [
            ("Structure: For/Against + Recommendation",
             "A comparison task at A2 has three parts.",
             "1. <strong>Option A</strong> — advantages and disadvantages<br>"
             "2. <strong>Option B</strong> — advantages and disadvantages<br>"
             "3. <strong>Recommendation</strong> — your choice and why"),
            ("Introducing Each Option",
             "Signal each option clearly with a transition.",
             "<em>D'un côté,…</em> — On one hand,…<br>"
             "<em>De l'autre côté,…</em> — On the other hand,…<br>"
             "<em>En ce qui concerne A,…</em> — As for A,…<br>"
             "<em>Quant à B,…</em> — As for B,…"),
            ("Advantages and Disadvantages",
             "Key phrases for pros and cons.",
             "<strong>Advantages:</strong><br>"
             "<em>L'avantage de… c'est que…</em><br>"
             "<em>… est plus pratique / moins cher / meilleur pour…</em><br>"
             "<strong>Disadvantages:</strong><br>"
             "<em>L'inconvénient de… c'est que…</em><br>"
             "<em>Par contre, / En revanche,…</em> — On the other hand / However,…<br>"
             "<em>… est plus cher / moins commode / moins rapide</em>"),
            ("Comparatives in Context",
             "Use comparative and superlative structures.",
             "<em>Le train est plus rapide que le bus.</em><br>"
             "<em>La voiture est moins écologique que le vélo.</em><br>"
             "<em>C'est la solution la plus économique.</em><br>"
             "<em>Il coûte autant que l'option B.</em> — It costs as much as option B."),
            ("Making a Recommendation",
             "End with a clear, justified recommendation.",
             "<em>Je recommande… parce que…</em><br>"
             "<em>À mon avis, la meilleure option est…</em><br>"
             "<em>En conclusion, je préfère… car…</em><br>"
             "<em>Pour ces raisons, je choisis…</em>"),
            ("Model Text — 110 Words",
             "Comparing two holiday options: city break vs. beach holiday.",
             "<em>D'un côté, un séjour à la mer a de nombreux avantages. On peut se détendre, nager et profiter du soleil. C'est une option idéale pour se reposer. Par contre, le bord de mer peut être très animé en été et les hôtels sont souvent plus chers.<br><br>"
             "De l'autre côté, une escapade en ville est plus culturelle. On peut visiter des musées, des monuments et de bons restaurants. Les prix sont souvent moins élevés hors saison. En revanche, on ne peut pas se baigner et ça peut être fatigant.<br><br>"
             "À mon avis, la meilleure option est la ville, car c'est plus varié et moins cher.</em>"),
        ],
        "traps": [
            ("on one hand", "d'un côté", "D'un côté / de l'autre côté — for/against structure."),
            ("on the other hand", "par contre / en revanche", "Par contre and en revanche are interchangeable here."),
            ("more expensive", "plus cher", "Cher (masc.) → plus cher; never 'plus chère' for general cost."),
            ("the best option", "la meilleure option", "Meilleure (f.) — irregular superlative of bonne."),
        ],
        "summary": [
            ("introduce option", "D'un côté / En ce qui concerne A", "D'un côté, le train est rapide."),
            ("contrast", "De l'autre côté / Par contre / En revanche", "Par contre, c'est plus cher."),
            ("advantage", "L'avantage de…, c'est que…", "L'avantage du bus, c'est que c'est moins cher."),
            ("disadvantage", "L'inconvénient de…, c'est que…", "L'inconvénient, c'est que c'est long."),
            ("comparison", "plus/moins/aussi + adj. + que", "Le train est plus rapide que le bus."),
            ("superlative", "le/la + plus/moins + adj.", "C'est la solution la plus écologique."),
            ("recommendation", "Je recommande… / À mon avis…", "À mon avis, la meilleure option est…"),
            ("conclusion", "En conclusion / Pour ces raisons", "En conclusion, je préfère le train."),
        ],
        "ex1": ("Exercise 1 — Choose the right connector",
                "Select the best transition.",
                [
                    ("You are introducing the second option:", ["D'abord,", "De l'autre côté,", "Soudain,", "Autrefois,"], "De l'autre côté,",
                     "De l'autre côté = on the other hand — introduces second option."),
                    ("You are giving a disadvantage:", ["L'avantage, c'est que…", "Par contre, / En revanche,…", "D'un côté,…", "En conclusion,…"], "Par contre, / En revanche,…",
                     "Par contre / En revanche introduce a contrast/disadvantage."),
                    ("Comparing: 'The train is faster than the bus':", ["Le train est plus vite que le bus.", "Le train est plus rapide que le bus.", "Le train est le plus rapide.", "Le train est aussi rapide que le bus."], "Le train est plus rapide que le bus.",
                     "Plus + adjective + que; rapide (not vite, which is an adverb)."),
                    ("Making a recommendation:", ["Je recommande le train parce que…", "À mon avis, le train est meilleur.", "En conclusion, je préfère le train.", "All of the above are correct"], "All of the above are correct",
                     "All three formulas are valid for recommending."),
                    ("'the most economical solution' (f.):", ["la plus économique solution", "la solution la plus économique", "la solution plus économique", "la meilleuse solution"], "la solution la plus économique",
                     "Adj. after noun: noun + la/le + plus + adj."),
                ]),
        "ex2": ("Exercise 2 — Translate into French",
                "Type the French sentence.",
                [
                    ("On one hand, it's cheaper.", "D'un côté, c'est moins cher.", "D'un côté + comparatif."),
                    ("On the other hand, it's slower.", "De l'autre côté / Par contre, c'est plus lent.", "De l'autre côté / par contre."),
                    ("The advantage is that it's quick.", "L'avantage, c'est que c'est rapide.", "L'avantage, c'est que + clause."),
                    ("In my opinion, the best option is the train.", "À mon avis, la meilleure option est le train.", "Meilleure = fem. superlative of bonne."),
                    ("In conclusion, I prefer the bike.", "En conclusion, je préfère le vélo.", "En conclusion + je préfère."),
                ]),
        "ex3": ("Exercise 3 — Spot the mistake",
                "Pick the correct sentence.",
                [
                    ("'The best option' (f.):", ["la meilleure option", "la meilleur option", "la plus bonne option", "la mieux option"], "la meilleure option",
                     "Superlative of bonne → la meilleure (feminine)."),
                    ("'The train is faster than the car':", ["Le train est plus vite que la voiture.", "Le train est plus rapide que la voiture.", "Le train est le plus rapide que la voiture.", "Le train est autant rapide que la voiture."], "Le train est plus rapide que la voiture.",
                     "Rapide is the adjective (more rapid); vite is an adverb."),
                    ("'On the other hand, it's more expensive':", ["D'un côté, c'est plus cher.", "Par contre, c'est plus cher.", "En revanche, c'est plus cher.", "Both B and C are correct"], "Both B and C are correct",
                     "Par contre and en revanche are interchangeable in this context."),
                    ("'I recommend this option because it's cheaper':", ["Je recommande cette option parce que c'est moins cher.", "Je recommande cette option car c'est moins cher.", "Je recommande cette option puisque c'est moins cher.", "All are correct"], "All are correct",
                     "Parce que, car, and puisque all introduce a reason."),
                ]),
        "game_desc": "Practise comparing options with advantages, disadvantages, and recommendations.",
        "items": [
            ("cmp1", "d'un côté", "on one hand", "one hand", "D'un côté, le bus est moins cher.", "Complète: ___ côté, c'est rapide. (on one)", "d'un"),
            ("cmp2", "de l'autre côté / par contre", "on the other hand / however", "other hand", "Par contre, c'est plus lent et moins confortable.", "Complète: ___ contre, c'est cher. (however)", "par"),
            ("cmp3", "l'avantage, c'est que", "the advantage is that", "advantage", "L'avantage du train, c'est que c'est rapide.", "Complète: L'___, c'est que c'est gratuit. (advantage)", "avantage"),
            ("cmp4", "l'inconvénient, c'est que", "the disadvantage is that", "disadvantage", "L'inconvénient, c'est que c'est trop loin.", "Complète: L'___, c'est que c'est cher. (disadvantage)", "inconvénient"),
            ("cmp5", "plus…que", "more … than", "faster than", "Le train est plus rapide que le bus.", "Complète: C'est plus ___ que l'autre. (cheap: bon marché)", "bon marché"),
            ("cmp6", "la meilleure option", "the best option (f.)", "best", "À mon avis, la meilleure option est le vélo.", "Complète: La ___ option est le train. (best, f.)", "meilleure"),
            ("cmp7", "en conclusion / pour ces raisons", "in conclusion / for these reasons", "conclusion", "En conclusion, je préfère la voiture.", "Complète: ___ conclusion, je préfère. (in)", "en"),
            ("cmp8", "je recommande… parce que", "I recommend… because", "recommend", "Je recommande le vélo parce que c'est écologique.", "Complète: Je ___ le train. (recommend)", "recommande"),
        ],
    },
}
