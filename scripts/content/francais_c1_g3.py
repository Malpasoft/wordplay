"""francais C1 grammaire — G09–G12"""

CHAPTERS = {
    "le-discours-rapporte-avance": {
        "level": "c1",
        "section": "grammaire",
        "num": "G09",
        "short": "Le Discours Rapport&eacute; Avanc&eacute;",
        "title": "Le Discours Rapport&eacute; Avanc&eacute;",
        "subtitle": "Style indirect libre, verbes introducteurs nuanc&eacute;s, concordance stylistique",
        "slides": [
            ("Rappel : style direct, indirect, indirect libre",
             "<p>Trois modalités pour rapporter un discours&nbsp;:</p>"
             "<table><tr><th>Style</th><th>Marques</th><th>Exemple</th></tr>"
             "<tr><td><strong>Direct</strong></td><td>Guillemets, deux-points</td><td>Il dit&nbsp;: «&nbsp;Je pars.&nbsp;»</td></tr>"
             "<tr><td><strong>Indirect</strong></td><td>que + subordonnée</td><td>Il dit qu'il partait.</td></tr>"
             "<tr><td><strong>Indirect libre</strong></td><td>Ni guillemets ni que</td><td>Il partait. Qu'importait le reste.</td></tr></table>"
             "<p>Le style indirect libre est caractéristique de la prose littéraire moderne (Flaubert, Zola, Proust).</p>"),
            ("Le style indirect libre : caractéristiques",
             "<p>Le <strong>style indirect libre</strong> fond la voix du narrateur et celle du personnage&nbsp;:</p>"
             "<ul><li>Pas de verbe introducteur ni de conjonction</li>"
             "<li>Les temps verbaux sont ceux du discours indirect (imparfait, conditionnel)</li>"
             "<li>Les marques de la 1ère personne disparaissent (remplacées par 3e personne)</li>"
             "<li>Mais les exclamations, interrogations rhétoriques, interjections persistent</li></ul>"
             "<p><em>Exemple (Flaubert, Madame Bovary)&nbsp;:</em><br>"
             "<em>«&nbsp;Emma rentra chez elle. Pourquoi n'avait-elle pas osé parler ? Quelle lâcheté&nbsp;!&nbsp;»</em></p>"),
            ("Verbes introducteurs nuancés",
             "<p>Au-delà de <em>dire</em>, les verbes introducteurs précisent l'intention du locuteur&nbsp;:</p>"
             "<table><tr><th>Intention</th><th>Verbes</th></tr>"
             "<tr><td>Affirmer</td><td>affirmer, soutenir, prétendre, alléguer, avancer</td></tr>"
             "<tr><td>Nier</td><td>nier, démentir, contester, réfuter</td></tr>"
             "<tr><td>Demander</td><td>demander, interroger, s'enquérir, questionner</td></tr>"
             "<tr><td>Exiger</td><td>exiger, ordonner, sommer, enjoindre</td></tr>"
             "<tr><td>Promettre</td><td>promettre, s'engager à, jurer</td></tr>"
             "<tr><td>Suggérer</td><td>suggérer, proposer, préconiser, recommander</td></tr></table>"),
            ("Concordance des temps au discours indirect",
             "<p>Quand la principale est au passé, les temps changent dans la subordonnée&nbsp;:</p>"
             "<table><tr><th>Direct</th><th>Indirect (principale au passé)</th></tr>"
             "<tr><td>Présent</td><td>Imparfait</td></tr>"
             "<tr><td>Futur</td><td>Conditionnel</td></tr>"
             "<tr><td>Passé composé</td><td>Plus-que-parfait</td></tr>"
             "<tr><td>Impératif</td><td>de + infinitif</td></tr>"
             "<tr><td>demain</td><td>le lendemain</td></tr>"
             "<tr><td>hier</td><td>la veille</td></tr>"
             "<tr><td>ici</td><td>là / là-bas</td></tr></table>"),
            ("Guillemets et ponctuation du discours rapporté",
             "<p>La typographie française du discours direct&nbsp;:</p>"
             "<ul><li>Guillemets français&nbsp;: «&nbsp;texte&nbsp;» (avec espace fine insécable)</li>"
             "<li>Tiret cadratin (—) pour les répliques de dialogue</li>"
             "<li>Le verbe introducteur peut être placé avant, après ou au milieu de la citation</li></ul>"
             "<p>Exemples&nbsp;:</p>"
             "<ul><li><em>«&nbsp;Je pars demain&nbsp;», annonça-t-il.</em></li>"
             "<li><em>«&nbsp;Je pars&nbsp;», dit-il, «&nbsp;demain.&nbsp;»</em></li>"
             "<li><em>Il annonça&nbsp;: «&nbsp;Je pars demain.&nbsp;»</em></li></ul>"),
        ],
        "traps": [
            ("Confusion style indirect libre / style indirect", "le style indirect libre n'a pas de verbe introducteur ni de que. Si on ajoute <em>il pensait que</em>, ce devient du style indirect."),
            ("Concordance des temps oubliée", "oublier d'adapter les temps au discours indirect quand la principale est au passé — <em>*il dit qu'il partira</em> doit devenir <em>il dit qu'il partirait</em>."),
            ("Guillemets anglais en français", "utiliser les guillemets anglais (\"...\") au lieu des guillemets français («&nbsp;...&nbsp;»)&nbsp;— faute typographique en français formel."),
        ],
        "summary": [
            "Style direct (guillemets), indirect (que + sub.), indirect libre (ni guillemets ni que).",
            "Style indirect libre = voix du narrateur et du personnage fusionnées — imparfait/conditionnel.",
            "Verbes introducteurs nuancés&nbsp;: affirmer, soutenir, nier, exiger, suggérer…",
            "Concordance des temps au discours indirect quand principale au passé.",
        ],
        "ex1": {
            "q": "Dans 'Emma était heureuse. Comme la vie était belle soudain !', quel procédé narratif est utilisé ?",
            "opts": ["Style direct", "Style indirect", "Style indirect libre", "Narration omnisciente"],
            "ans": "Style indirect libre",
            "exp": "Il n'y a pas de guillemets ni de verbe introducteur avec <em>que</em>, mais le point de vue intérieur du personnage transparaît dans le texte du narrateur. C'est le style indirect libre.",
        },
        "ex2": {
            "q": "Mettez au discours indirect&nbsp;: Il a dit&nbsp;: «&nbsp;Je viendrai demain.&nbsp;»",
            "ans": "Il a dit qu'il viendrait le lendemain.",
            "exp": "Au discours indirect, après une principale au passé (<em>a dit</em>)&nbsp;: futur → conditionnel (<em>viendrai → viendrait</em>), <em>demain → le lendemain</em>.",
            "accept": ["il a dit qu'il viendrait", "il dit qu'il viendrait le lendemain"],
        },
        "ex3": {
            "q": "Quel verbe introducteur convient pour rapporter une affirmation contestée ?",
            "opts": ["affirmer", "prétendre", "ordonner", "promettre"],
            "ans": "prétendre",
            "exp": "<em>Prétendre</em> (ou <em>alléguer, soutenir</em>) rapporte une affirmation avec une nuance de doute ou de contestation. <em>Affirmer</em> est plus neutre.",
        },
        "game_desc": "Maîtrisez le discours rapporté et ses nuances stylistiques avancées",
        "items": [
            ("c1g09-sil", "le style indirect libre", "discours sans marqueur, mêlant voix du narrateur et personnage", "Flaubert · imparfait · fusion", "Emma rentrait chez elle. Était-elle donc condamnée ? — style indirect libre.", "SIL = fusion narrateur/personnage sans guillemets ni que", "discours rapporté sans marqueur, fusion des voix"),
            ("c1g09-verbe-intro", "le verbe introducteur nuancé", "verbe précisant l'intention du locuteur dans le discours rapporté", "soutenir · nier · exiger", "Il prétendit avoir été absent — prétendre suggère le doute.", "verbe introducteur = précise l'intention du locuteur", "verbe qui introduit et nuance le discours rapporté"),
            ("c1g09-pretendre", "prétendre", "rapporter une affirmation avec nuance de doute", "alléguer · soutenir · contesté", "Il prétend n'avoir rien vu — prétendre implique un doute sur la vérité.", "prétendre = affirmer avec nuance de doute", "rapporter une affirmation suspecte ou contestée"),
            ("c1g09-concordance", "la concordance au D.I.", "changement de temps au discours indirect (principale au passé)", "imparfait · conditionnel · PQP", "Il dit qu'il partirait = futur → conditionnel au discours indirect.", "concordance DI = adapter les temps au passé", "adaptation des temps dans le discours indirect"),
            ("c1g09-guillements", "les guillemets français", "«&nbsp;texte&nbsp;» avec espace insécable — typographie française", "«&nbsp;»&nbsp;· espace · typographie", "«&nbsp;Je pars&nbsp;» — guillemets français avec espace fine insécable obligatoire.", "guillemets fr. = «&nbsp;texte&nbsp;» avec espace", "guillemets et typographie du discours direct en français"),
            ("c1g09-tiret-dialogue", "le tiret cadratin dans le dialogue", "— pour introduire chaque réplique dans un dialogue littéraire", "— · dialogue · réplique", "— Vous partez ? demanda-t-il. — Oui, répondit-elle.", "tiret cadratin = marqueur de réplique dans dialogue", "ponctuation des dialogues littéraires en français"),
            ("c1g09-enjoindre", "enjoindre de + inf.", "verbe soutenu signifiant ordonner formellement", "ordre · formel · injonction", "Le juge lui enjoignit de se taire — enjoindre est un ordre formel.", "enjoindre = ordonner formellement (soutenu)", "verbe introducteur d'ordre formel au style indirect"),
            ("c1g09-demain-lendemain", "demain → le lendemain", "transformation des repères temporels au discours indirect", "temps · demain · veille", "Il dit qu'il viendrait le lendemain — demain devient le lendemain au D.I.", "demain → le lendemain au discours indirect", "changement des repères temporels au discours indirect"),
        ],
    },

    "la-stylistique": {
        "level": "c1",
        "section": "grammaire",
        "num": "G10",
        "short": "La Stylistique",
        "title": "La Stylistique",
        "subtitle": "Rythme, figures de style avanc&eacute;es et cohérence textuelle",
        "slides": [
            ("Figures de style au niveau C1",
             "<p>Figures de style avancées essentielles&nbsp;:</p>"
             "<table><tr><th>Figure</th><th>Définition</th><th>Exemple</th></tr>"
             "<tr><td>Oxymore</td><td>association de termes contradictoires</td><td><em>un silence éloquent</em></td></tr>"
             "<tr><td>Synecdoque</td><td>la partie pour le tout ou inversement</td><td><em>les voiles à l'horizon</em> (= les bateaux)</td></tr>"
             "<tr><td>Chiasme</td><td>inversion de la structure AB → BA</td><td><em>Il faut manger pour vivre, non vivre pour manger.</em></td></tr>"
             "<tr><td>Zeugme</td><td>un même verbe pour deux compléments incompatibles</td><td><em>Elle entra dans la pièce et dans ma vie.</em></td></tr>"
             "<tr><td>Prétérition</td><td>dire qu'on ne dira pas ce qu'on dit quand même</td><td><em>Je ne mentionnerai pas son passé douteux.</em></td></tr></table>"),
            ("Rythme et construction de la phrase",
             "<p>Le <strong>rythme</strong> est créé par la longueur et la structure des propositions&nbsp;:</p>"
             "<ul><li><strong>Phrase binaire</strong>&nbsp;: deux parties symétriques — <em>Il voulut partir ; il ne put le faire.</em></li>"
             "<li><strong>Phrase ternaire</strong>&nbsp;: trois éléments — <em>Il vit, il jugea, il agit.</em></li>"
             "<li><strong>Asyndète</strong>&nbsp;: suppression des conjonctions — <em>Je suis venu, j'ai vu, j'ai vaincu.</em></li>"
             "<li><strong>Polysyndète</strong>&nbsp;: répétition des conjonctions — <em>Et il cria, et il pleura, et il tomba.</em></li></ul>"),
            ("Cohérence et cohésion textuelles",
             "<p>Un texte cohérent maintient&nbsp;:</p>"
             "<ul><li><strong>Isotopie sémantique</strong>&nbsp;: champ lexical constant autour d'un thème</li>"
             "<li><strong>Anaphore pronominale</strong>&nbsp;: pronoms renvoyant clairement à un référent</li>"
             "<li><strong>Connecteurs logiques</strong>&nbsp;: articulent les idées (par conséquent, en revanche, néanmoins)</li>"
             "<li><strong>Thème/Rhème</strong>&nbsp;: information connue (thème) + nouvelle information (rhème)</li></ul>"
             "<p><em>Exemple</em>&nbsp;: <em>Le roman s'ouvre sur une scène de marché. <strong>Cette scène</strong> [thème repris] permet d'introduire les personnages principaux.</em></p>"),
            ("Le registre et le niveau de langue",
             "<p>Choisir le bon registre en C1&nbsp;:</p>"
             "<table><tr><th>Registre</th><th>Caractéristiques</th></tr>"
             "<tr><td>Soutenu/littéraire</td><td>subj. imparfait, passé simple, participes, vocabulaire riche</td></tr>"
             "<tr><td>Standard/courant</td><td>passé composé, subj. présent, vocabulaire usuel</td></tr>"
             "<tr><td>Familier</td><td>ne omis, troncations (sympa), argot</td></tr>"
             "<tr><td>Vulgaire</td><td>gros mots, verlan, ellipses extrêmes</td></tr></table>"
             "<p>En C1, on doit être capable d'<strong>identifier et de reproduire</strong> les registres soutenu et standard.</p>"),
            ("L'implicite et le sous-entendu",
             "<p>Le discours avancé repose souvent sur l'<strong>implicite</strong>&nbsp;:</p>"
             "<ul><li><strong>Présupposé</strong>&nbsp;: information implicitement admise avant l'énoncé.<br>"
             "<em>Elle a encore raté son examen</em> — présuppose qu'elle a déjà raté avant.</li>"
             "<li><strong>Sous-entendu</strong>&nbsp;: sens suggéré sans être dit.<br>"
             "<em>Il n'est pas exactement ponctuel</em> — suggère qu'il est souvent en retard.</li>"
             "<li><strong>Inférence</strong>&nbsp;: conclusion que le lecteur tire du texte.</li></ul>"
             "<p>En C1, analyser et produire des énoncés avec de l'implicite est une compétence clé.</p>"),
        ],
        "traps": [
            ("Oxymore confondu avec antithèse", "l'antithèse oppose deux idées dans deux propositions séparées ; l'oxymore les fusionne en une seule expression (<em>une obscure clarté</em>)."),
            ("Asyndète sans effet voulu", "supprimer les conjonctions sans raison stylistique crée de la confusion plutôt que du rythme."),
            ("Présupposé mal interprété", "confondre ce qui est dit (posé) et ce qui est implicitement admis (présupposé) — les deux ne peuvent être niés de la même façon."),
        ],
        "summary": [
            "Figures avancées&nbsp;: oxymore, chiasme, zeugme, synecdoque, prétérition.",
            "Rythme&nbsp;: phrases binaires/ternaires, asyndète (sans conjonctions), polysyndète.",
            "Cohérence textuelle&nbsp;: isotopie, anaphore, connecteurs, thème/rhème.",
            "Implicite&nbsp;: présupposé (admis), sous-entendu (suggéré), inférence.",
        ],
        "ex1": {
            "q": "Identifiez la figure de style&nbsp;: 'Il faut manger pour vivre et non vivre pour manger.'",
            "opts": ["Métaphore", "Chiasme", "Oxymore", "Anaphore"],
            "ans": "Chiasme",
            "exp": "Le chiasme inverse la structure AB → BA&nbsp;: A = manger, B = vivre → A'= vivre, B'= manger. La structure croisée est caractéristique du chiasme.",
        },
        "ex2": {
            "q": "Qu'est-ce qu'un présupposé ? Donnez un exemple en 1 phrase.",
            "ans": "Information implicitement admise avant l'énoncé, ex. : Elle a encore raté.",
            "exp": "'Elle a encore raté' présuppose qu'elle a déjà raté avant. Le présupposé est l'information admise sans être explicitée.",
            "accept": ["information implicite", "implicitement admis", "présupposé = information admise"],
        },
        "ex3": {
            "q": "Quelle est la différence entre asyndète et polysyndète ?",
            "opts": [
                "L'asyndète ajoute des conjonctions ; la polysyndète les supprime",
                "L'asyndète supprime les conjonctions ; la polysyndète les répète",
                "Elles sont synonymes",
                "L'asyndète est réservée à la poésie",
            ],
            "ans": "L'asyndète supprime les conjonctions ; la polysyndète les répète",
            "exp": "Asyndète&nbsp;: <em>Je suis venu, j'ai vu, j'ai vaincu</em> (pas de 'et'). Polysyndète&nbsp;: <em>Et il cria, et il pleura, et il tomba</em> (répétition de 'et').",
        },
        "game_desc": "Maîtrisez la stylistique et les figures de style avancées",
        "items": [
            ("c1g10-oxymore", "l'oxymore", "association de termes contradictoires dans une même expression", "contradiction · fusion · paradoxe", "Un silence éloquent — silence et éloquence sont contradictoires : oxymore.", "oxymore = termes contradictoires réunis", "association contradictoire dans une seule expression"),
            ("c1g10-chiasme", "le chiasme", "inversion de la structure AB → BA", "inversion · structure · miroir", "Manger pour vivre / vivre pour manger — structure inversée : chiasme.", "chiasme = AB → BA (structure inversée)", "inversion croisée de la structure syntaxique"),
            ("c1g10-zeugme", "le zeugme", "un verbe rattaché à deux compléments sémantiquement incompatibles", "incompatible · verbe unique · surprise", "Elle entra dans la pièce et dans ma vie — zeugme sur le verbe entrer.", "zeugme = un verbe pour deux compléments incompatibles", "construction inattendue liant deux compléments hétérogènes"),
            ("c1g10-pretention", "la prétérition", "dire qu'on ne dira pas ce qu'on dit quand même", "ironie · rhétorique · tactique", "Je ne mentionnerai pas son casier judiciaire — on vient pourtant de le mentionner.", "prétérition = dire ce qu'on prétend taire", "figure rhétorique consistant à mentionner ce qu'on prétend taire"),
            ("c1g10-asyndete", "l'asyndète", "suppression des conjonctions pour un rythme haletant", "rythme · vitesse · concision", "Je suis venu, j'ai vu, j'ai vaincu — asyndète créant un rythme rapide.", "asyndète = rythme rapide sans conjonctions", "suppression des conjonctions pour accélérer le rythme"),
            ("c1g10-presuppose", "le présupposé", "information implicitement admise dans un énoncé", "implicite · admis · non dit", "Elle a encore raté — présuppose qu'elle a déjà raté avant.", "présupposé = information admise implicitement", "information non dite mais supposée vraie dans l'énoncé"),
            ("c1g10-isotopie", "l'isotopie sémantique", "cohérence thématique par un champ lexical constant", "champ lexical · thème · cohérence", "Un texte sur la mer maintient un isotopie maritime dans son vocabulaire.", "isotopie = cohérence thématique lexicale", "unité sémantique d'un texte autour d'un champ lexical"),
            ("c1g10-theme-rheme", "thème et rhème", "thème = information connue ; rhème = information nouvelle", "information · progression · cohésion", "Le roman [thème connu] présente des personnages complexes [rhème nouveau].", "thème = connu ; rhème = nouveau dans la phrase", "organisation de l'information connue et nouvelle dans la phrase"),
        ],
    },

    "la-subordination-nominale": {
        "level": "c1",
        "section": "grammaire",
        "num": "G11",
        "short": "La Subordination Nominale",
        "title": "La Subordination Nominale",
        "subtitle": "Propositions en que, infinitives et interrogatives indirectes",
        "slides": [
            ("Complétives en que : indicatif ou subjonctif ?",
             "<p>Le mode de la complétive dépend du verbe de la principale&nbsp;:</p>"
             "<table><tr><th>Indicatif</th><th>Subjonctif</th></tr>"
             "<tr><td>Verbes d'opinion/déclaration&nbsp;: <em>croire, penser, dire, affirmer</em></td><td>Verbes de volonté&nbsp;: <em>vouloir, exiger, souhaiter</em></td></tr>"
             "<tr><td>Verbes de perception&nbsp;: <em>voir, entendre, remarquer</em></td><td>Verbes de sentiment&nbsp;: <em>regretter, craindre, s'étonner</em></td></tr>"
             "<tr><td>Verbes de certitude&nbsp;: <em>être sûr, être certain</em></td><td>Impersonnels&nbsp;: <em>il faut, il est possible, il est dommage</em></td></tr>"
             "<tr><td>La question &nbsp;: <em>est-il vrai que…?</em></td><td>Doute ou négation des précédents</td></tr></table>"),
            ("Complétive vs infinitive",
             "<p>Quand le sujet de la principale et de la subordonnée sont le MÊME, on emploie l'infinitif&nbsp;:</p>"
             "<ul><li>Sujet différent&nbsp;: <em>Je veux qu'<strong>il</strong> parte.</em> (complétive)</li>"
             "<li>Même sujet&nbsp;: <em>Je veux partir.</em> (infinitif)</li></ul>"
             "<p>Cette règle est absolue avec les verbes de volonté et de sentiment.</p>"
             "<p>Exceptions&nbsp;: <em>se douter que, espérer que</em> (+ subj. même sujet identique dans le cas de <em>espérer que</em>)</p>"),
            ("L'interrogative indirecte",
             "<p>L'interrogative indirecte remplace la question directe dans une subordonnée&nbsp;:</p>"
             "<table><tr><th>Directe</th><th>Indirecte</th></tr>"
             "<tr><td>Qui est là ?</td><td>Je demande <em>qui est là</em>.</td></tr>"
             "<tr><td>Qu'est-ce qui se passe ?</td><td>Je sais <em>ce qui se passe</em>.</td></tr>"
             "<tr><td>Où va-t-il ?</td><td>Je veux savoir <em>où il va</em>.</td></tr>"
             "<tr><td>Est-ce qu'il vient ?</td><td>Je me demande <em>s'il vient</em>.</td></tr></table>"
             "<p><strong>Règle&nbsp;:</strong> pas d'inversion du sujet dans l'interrogative indirecte.</p>"),
            ("Que explétif dans les complétives",
             "<p>Le <em>que</em> peut être répété dans une coordination de subordonnées&nbsp;:</p>"
             "<ul><li><em>Je pense <strong>qu'</strong>il viendra et <strong>qu'</strong>il restera.</em> (que répété)</li>"
             "<li><em>Je pense <strong>qu'</strong>il viendra et restera.</em> (ellipse — moins formel)</li></ul>"
             "<p>En style soutenu, on répète le <em>que</em> devant chaque subordonnée coordonnée.</p>"
             "<p>Attention&nbsp;: si les sujets sont différents, le <em>que</em> est obligatoire pour chaque subordonnée.</p>"),
            ("Substantivation des propositions",
             "<p>Une proposition entière peut être substantivée par un pronom neutre&nbsp;:</p>"
             "<ul><li><em>ce que</em>&nbsp;: <em>Ce qu'il a dit est faux.</em> (sujet)</li>"
             "<li><em>le fait que</em>&nbsp;: <em>Le fait qu'il soit là m'étonne.</em></li>"
             "<li><em>le fait de + inf.</em>&nbsp;: <em>Le fait de partir tôt a tout changé.</em></li></ul>"
             "<p>Ces constructions permettent de nominaliser une proposition et de l'utiliser comme sujet ou objet.</p>"),
        ],
        "traps": [
            ("Inversion dans l'interrogative indirecte", "ne jamais inverser le sujet dans une interrogative indirecte&nbsp;: <em>*je sais où va-t-il</em> est faux. L'ordre est toujours sujet-verbe&nbsp;: <em>je sais où il va</em>."),
            ("Subjonctif après je pense que", "<em>Je pense que</em> (affirmation) prend l'indicatif. <em>Je ne pense pas que</em> (négation) prend le subjonctif&nbsp;: la nuance dépend de la polarité."),
            ("Infinitif quand les sujets diffèrent", "employer l'infinitif quand les sujets sont différents est fautif&nbsp;: <em>*je veux il parte</em> → <em>je veux qu'il parte</em>.",),
        ],
        "summary": [
            "Complétives en que&nbsp;: indicatif (croire, savoir) ou subjonctif (vouloir, regretter, il faut).",
            "Même sujet → infinitif ; sujet différent → complétive en que.",
            "Interrogative indirecte&nbsp;: pas d'inversion du sujet après le verbe introducteur.",
            "que répété en style soutenu dans les subordonnées coordonnées.",
        ],
        "ex1": {
            "q": "Choisissez le mode correct&nbsp;: 'Je regrette que tu ___ (ne pas venir).'",
            "opts": ["n'es pas venu", "ne viennes pas", "ne viens pas", "sois venu"],
            "ans": "ne viennes pas",
            "exp": "<em>Regretter que</em> exprime un sentiment négatif → subjonctif. Au présent&nbsp;: <em>que tu ne viennes pas</em>. Le subjonctif présent suffit si l'action est simultanée.",
        },
        "ex2": {
            "q": "Transformez en interrogative indirecte&nbsp;: 'Où est-il allé ?'",
            "ans": "Je veux savoir où il est allé.",
            "exp": "Dans l'interrogative indirecte, on supprime l'inversion du sujet&nbsp;: <em>où est-il allé ?</em> → <em>où il est allé</em>. Le verbe introducteur (<em>je veux savoir</em>) introduit la subordonnée.",
            "accept": ["où il est allé", "je me demande où il est allé"],
        },
        "ex3": {
            "q": "Pourquoi dit-on 'je veux partir' et non 'je veux que je parte' ?",
            "opts": ["Par économie linguistique seulement", "Parce que quand le sujet est le même, on emploie l'infinitif", "Parce que 'partir' est un verbe intransitif", "Par convention arbitraire"],
            "ans": "Parce que quand le sujet est le même, on emploie l'infinitif",
            "exp": "La règle est syntaxique&nbsp;: même sujet dans la principale et la subordonnée → infinitif. Sujet différent → complétive en <em>que</em>.",
        },
        "game_desc": "Maîtrisez la subordination nominale et ses modes",
        "items": [
            ("c1g11-completive-ind", "la complétive à l'indicatif", "complétive après verbes d'opinion, déclaration, certitude", "croire · penser · indicatif", "Je pense qu'il viendra — verbe d'opinion → indicatif dans la complétive.", "complétive indic. = après croire, penser, savoir", "subordonnée nominale à l'indicatif après verbe d'opinion"),
            ("c1g11-completive-subj", "la complétive au subjonctif", "subjonctif après volonté, sentiment, impersonnels", "vouloir · regretter · il faut", "Je veux qu'il vienne — verbe de volonté → subjonctif dans la complétive.", "complétive subj. = après vouloir, regretter, il faut", "subordonnée nominale au subjonctif après volonté/sentiment"),
            ("c1g11-meme-sujet", "même sujet → infinitif", "remplacement de la complétive par l'infinitif quand les sujets sont identiques", "infinitif · même sujet · économie", "Je veux partir (même sujet) vs je veux qu'il parte (sujets différents).", "même sujet = toujours infinitif", "réduction de la complétive à l'infinitif avec sujet identique"),
            ("c1g11-inter-ind", "l'interrogative indirecte", "question intégrée à une phrase sans inversion du sujet", "si · où · ce qui", "Je sais où il va — pas d'inversion dans l'interrogative indirecte.", "inter. indirecte = question sans inversion", "question subordonnée sans inversion du sujet"),
            ("c1g11-pas-inversion", "pas d'inversion en inter. ind.", "l'ordre sujet-verbe est obligatoire dans l'interrogative indirecte", "erreur · inversion · indirect", "*Je sais où va-t-il — fautif. Correct : je sais où il va.", "inter. indirecte : toujours sujet-verbe", "absence d'inversion du sujet dans l'interrogative indirecte"),
            ("c1g11-le-fait-que", "le fait que + subjonctif", "nominalisation d'une proposition avec le fait que", "nominalisation · sujet · subjonctif", "Le fait qu'il soit là m'étonne — le fait que nominalise la proposition.", "le fait que = nominalisation + subjonctif", "nominalisation d'une proposition par le fait que"),
            ("c1g11-que-repete", "que répété (subordonnées coordonnées)", "répétition de que en style soutenu dans les coordinations", "soutenu · coordination · répétition", "Je sais qu'il viendra et qu'il restera — que répété en style formel.", "que répété = style soutenu dans les coordinations", "répétition du que devant chaque subordonnée coordonnée"),
            ("c1g11-ce-que", "ce que / ce qui (substantivation)", "pronoms neutres nominalisant une proposition", "ce qui · sujet · COD", "Ce qu'il dit est faux — ce que nominalise la proposition subordonnée.", "ce que / ce qui = pronoms de nominalisation", "nominalisation d'une proposition par ce que ou ce qui"),
        ],
    },

    "la-ponctuation-et-graphie": {
        "level": "c1",
        "section": "grammaire",
        "num": "G12",
        "short": "Ponctuation et Graphie Avanc&eacute;es",
        "title": "Ponctuation et Graphie Avanc&eacute;es",
        "subtitle": "Signes de ponctuation, accords complexes et orthographe soutenue",
        "slides": [
            ("La ponctuation française avancée",
             "<p>Signes de ponctuation avancés à maîtriser en C1&nbsp;:</p>"
             "<table><tr><th>Signe</th><th>Nom</th><th>Usage</th></tr>"
             "<tr><td>—</td><td>Tiret cadratin</td><td>Dialogues, insertions explicatives, ruptures</td></tr>"
             "<tr><td>–</td><td>Tiret demi-cadratin</td><td>Intervalles (2000–2010), listes</td></tr>"
             "<tr><td>«&nbsp;»</td><td>Guillemets français</td><td>Citations, discours direct, mots cités</td></tr>"
             "<tr><td>…</td><td>Points de suspension</td><td>Interruption, suggestion, liste non-exhaustive</td></tr>"
             "<tr><td>;</td><td>Point-virgule</td><td>Séparation d'idées liées, listes complexes</td></tr></table>"),
            ("Le point-virgule et la virgule",
             "<p>Le <strong>point-virgule</strong> sépare deux propositions indépendantes mais liées sémantiquement&nbsp;:</p>"
             "<ul><li><em>Il pleuvait ; nous décidâmes de rester.</em></li>"
             "<li><em>Il avait tout essayé ; rien n'avait fonctionné.</em></li></ul>"
             "<p>La <strong>virgule</strong>&nbsp;:</p>"
             "<ul><li>Isole les éléments d'une liste</li>"
             "<li>Encadre les appositions et les incises&nbsp;: <em>Paris, capitale de la France, est magnifique.</em></li>"
             "<li>Marque les propositions participiales et gérondives en tête de phrase</li>"
             "<li>Sépare les subordonnées circonstancielles antéposées</li></ul>"),
            ("Accords complexes",
             "<p>Accords à maîtriser en C1&nbsp;:</p>"
             "<ul><li><strong>PP avec avoir&nbsp;:</strong> s'accorde avec le COD si celui-ci précède le verbe&nbsp;: <em>Les lettres qu'il a <strong>écrites</strong>.</em></li>"
             "<li><strong>PP des verbes pronominaux&nbsp;:</strong> s'accorde avec le COD si celui-ci précède le verbe&nbsp;: <em>Elle s'est <strong>lavée</strong>.</em> / <em>Elle s'est lavé les mains.</em></li>"
             "<li><strong>Verbes impersonnels&nbsp;:</strong> PP toujours invariable&nbsp;: <em>les efforts qu'il a <strong>fallu</strong>.</em></li>"
             "<li><strong>Faire + inf.&nbsp;:</strong> PP toujours invariable&nbsp;: <em>la lettre qu'il a <strong>fait</strong> écrire.</em></li></ul>"),
            ("Orthographe des mots invariables avancée",
             "<p>Mots souvent mal orthographiés au niveau C1&nbsp;:</p>"
             "<table><tr><th>Forme correcte</th><th>Erreur fréquente</th><th>Remarque</th></tr>"
             "<tr><td><em>quoique</em> (bien que)</td><td><em>*quoi que</em></td><td>Un seul mot</td></tr>"
             "<tr><td><em>quoi que</em> (quelle que chose)</td><td><em>*quoique</em></td><td>Deux mots</td></tr>"
             "<tr><td><em>davantage</em></td><td><em>*d'avantage</em></td><td>Toujours un mot, sans cédille</td></tr>"
             "<tr><td><em>quelque</em> / <em>quel que</em></td><td>confusion fréquente</td><td><em>quelque</em> adj., <em>quel que</em> attribut</td></tr>"
             "<tr><td><em>peut-être</em></td><td><em>*peut être</em></td><td>Adverbe = avec trait d'union</td></tr></table>"),
            ("Majuscules et typographie française",
             "<p>Règles de majuscules spécifiques au français&nbsp;:</p>"
             "<ul><li>Les adjectifs de nationalité s'écrivent en minuscule&nbsp;: <em>un ami français</em> (≠ anglais)</li>"
             "<li>Les noms de nationalité s'écrivent en majuscule&nbsp;: <em>un Français</em></li>"
             "<li>Institutions&nbsp;: <em>l'Assemblée nationale, le Parlement, la République</em></li>"
             "<li>Titres d'œuvres&nbsp;: <em>Madame Bovary, Les Misérables</em></li></ul>"
             "<p>L'espace insécable avant les deux-points, le point-virgule, le point d'exclamation et le point d'interrogation est une règle typographique française.</p>"),
        ],
        "traps": [
            ("Quoique vs quoi que", "confondre <em>quoique</em> (= bien que, un mot, + subj.) avec <em>quoi que</em> (= quelle que soit la chose que, deux mots, + subj.)."),
            ("PP des pronominaux sans vérifier le COD", "l'accord du PP des verbes pronominaux dépend de la position du COD — <em>elle s'est lavée</em> (se = COD) vs <em>elle s'est lavé les mains</em> (les mains = COD, après le verbe, pas d'accord)."),
            ("Espace avant ponctuation haute", "en français, les signes &laquo;&nbsp;: ; ! ?&nbsp;&raquo; prennent une espace insécable avant eux — différent de l'anglais."),
        ],
        "summary": [
            "Tiret cadratin (dialogue), point-virgule (idées liées), guillemets français.",
            "PP avec avoir : accord avec le COD si antéposé.",
            "PP pronominaux&nbsp;: accord avec le COD si antéposé (se ≠ les mains).",
            "Homophones graphiques&nbsp;: quoique/quoi que, peut-être, davantage, quelque/quel que.",
        ],
        "ex1": {
            "q": "Quel est l'accord correct ? 'Les fleurs qu'elle a _____ (cueillir).'",
            "opts": ["cueilli", "cueillis", "cueillies", "cueillie"],
            "ans": "cueillies",
            "exp": "Le COD 'les fleurs' (féminin pluriel) est placé avant le verbe 'a cueillies' → le PP s'accorde en genre et nombre&nbsp;: <em>cueillies</em>.",
        },
        "ex2": {
            "q": "Choisissez la bonne orthographe&nbsp;: 'Il est venu ___ qu'il était fatigué.' (= bien que)",
            "ans": "quoique",
            "exp": "<em>Quoique</em> (un seul mot) = bien que. <em>Quoi que</em> (deux mots) = quelle que soit la chose que. Ici le sens est 'bien que' → <em>quoique</em>.",
            "accept": ["quoique"],
        },
        "ex3": {
            "q": "Dans 'Elle s'est lavé les mains', pourquoi le PP est-il invariable ?",
            "opts": ["Les verbes pronominaux sont toujours invariables", "Le COD 'les mains' est placé après le verbe", "S'est est un auxiliaire impersonnel", "Le sujet est féminin donc invariable"],
            "ans": "Le COD 'les mains' est placé après le verbe",
            "exp": "Le PP des verbes pronominaux s'accorde avec le COD si celui-ci précède le verbe. Ici 'les mains' est COD mais placé après → pas d'accord. Comparez&nbsp;: <em>Elle se les est lavées</em> (les mains, COD antéposé).",
        },
        "game_desc": "Maîtrisez la ponctuation française avancée et les accords complexes",
        "items": [
            ("c1g12-tiret-cadratin", "le tiret cadratin (—)", "tiret long pour les dialogues, insertions et ruptures syntaxiques", "dialogue · insertion · rupture", "— Je pars — dit-il — sans me retourner. Tiret cadratin dans le dialogue.", "tiret cadratin = — (long) pour dialogues et insertions", "tiret long pour les dialogues et insertions explicatives"),
            ("c1g12-guillemets-fr", "les guillemets français", "«&nbsp;» avec espace insécable — typographie française", "«&nbsp;» · citation · discours direct", "«&nbsp;Je pars&nbsp;» — guillemets français avec espace insécable.", "guillemets fr. = «&nbsp;» avec espaces insécables", "guillemets français avec espace insécable"),
            ("c1g12-pp-avoir", "PP avec avoir (accord)", "le PP s'accorde avec le COD si celui-ci précède le verbe", "COD · antéposé · accord", "Les lettres qu'il a écrites — COD féminin pluriel antéposé → accord.", "PP avoir = accord si COD avant le verbe", "accord du PP avec le COD antéposé dans avoir"),
            ("c1g12-pp-pronominal", "PP des pronominaux", "accord selon la position du COD : se lavée vs se lavé les mains", "COD · position · se", "Elle s'est lavée (se = COD) vs elle s'est lavé les mains (COD après).", "PP pronominal = accord si COD antéposé", "accord du PP pronominal selon la position du COD"),
            ("c1g12-quoique", "quoique vs quoi que", "quoique = bien que (1 mot) ; quoi que = quelle chose que (2 mots)", "bien que · confusion · homophones", "Quoique fatigué, il continua (bien que). Quoi qu'il fasse, il réussit (quelle chose).", "quoique = bien que ; quoi que = quelle chose", "distinction orthographique entre quoique et quoi que"),
            ("c1g12-peut-etre", "peut-être (adverbe)", "adverbe de doute toujours avec trait d'union", "trait d'union · adverbe · doute", "Il viendra peut-être — adverbe avec trait d'union obligatoire.", "peut-être = adverbe avec trait d'union", "orthographe de l'adverbe peut-être"),
            ("c1g12-point-virgule", "le point-virgule", "sépare deux propositions indépendantes mais liées sémantiquement", "séparation · idées liées · coordination", "Il pleuvait ; nous décidâmes de rester — idées liées par le point-virgule.", "point-virgule = propositions liées mais distinctes", "ponctuation séparant des idées indépendantes mais liées"),
            ("c1g12-majuscule-nat", "majuscule / minuscule nationalités", "nom de nationalité en maj. ; adjectif en minusc.", "Français · français · typographie", "Un Français (nom) parle français (adjectif) — majuscule vs minuscule.", "nationalité : nom = Majusc., adj. = minusc.", "règle des majuscules pour les noms et adjectifs de nationalité"),
        ],
    },
}
