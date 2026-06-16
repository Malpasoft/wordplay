"""francais B2 rédaction — R01–R04"""

CHAPTERS = {
    "la-dissertation": {
        "level": "b2",
        "section": "redaction",
        "num": "R01",
        "short": "La Dissertation",
        "title": "La Dissertation",
        "subtitle": "Argumenter en trois parties — th&egrave;se, antith&egrave;se, synth&egrave;se",
        "slides": [
            ("Qu'est-ce que la dissertation ?",
             "<p>La dissertation est un exercice d'argumentation structur&eacute; en <strong>trois parties</strong> qui explore une question complexe sous plusieurs angles.</p>"
             "<ul><li>Partie 1 : Th&egrave;se &mdash; d&eacute;fendre une position</li>"
             "<li>Partie 2 : Antith&egrave;se &mdash; nuancer ou contredire</li>"
             "<li>Partie 3 : Synth&egrave;se &mdash; d&eacute;passer la contradiction</li></ul>"
             "<p>Chaque partie comprend 2 &agrave; 3 paragraphes avec un argument + un exemple + une transition.</p>"),
            ("L'introduction en 4 temps",
             "<p>Une introduction efficace suit toujours le m&ecirc;me sch&eacute;ma&nbsp;:</p>"
             "<ol><li><strong>L'accroche</strong> &mdash; citation, fait marquant, question rhétorique</li>"
             "<li><strong>La contextualisation</strong> &mdash; situer le sujet dans son contexte</li>"
             "<li><strong>La probl&eacute;matique</strong> &mdash; reformuler le sujet en question ouverte</li>"
             "<li><strong>L'annonce du plan</strong> &mdash; annoncer les trois parties clairement</li></ol>"
             "<p><em>Astuce&nbsp;:</em> La probl&eacute;matique n'est jamais une simple question rhétorique ; elle doit soulever un v&eacute;ritable enjeu intellectuel.</p>"),
            ("Le paragraphe argumentatif (AAEX)",
             "<p>Chaque paragraphe de d&eacute;veloppement suit la structure <strong>AAEX</strong>&nbsp;:</p>"
             "<ul><li><strong>A</strong>ffirmation &mdash; pr&eacute;senter l'id&eacute;e directrice</li>"
             "<li><strong>A</strong>rgument &mdash; expliquer le raisonnement</li>"
             "<li><strong>EX</strong>emple &mdash; illustrer par un exemple concret (auteur, statistique, fait historique)</li></ul>"
             "<p>Terminer par une <strong>phrase de transition</strong> vers l'argument suivant.</p>"
             "<p><em>Exemple&nbsp;:</em> &laquo;&nbsp;Cependant, cette position soulève une limite importante…&nbsp;&raquo;</p>"),
            ("Connecteurs essentiels pour disserter",
             "<table><tr><th>Fonction</th><th>Exemples</th></tr>"
             "<tr><td>Addition</td><td>de plus, en outre, qui plus est, par ailleurs</td></tr>"
             "<tr><td>Opposition</td><td>or, n&eacute;anmoins, en revanche, toutefois, cependant</td></tr>"
             "<tr><td>Concession</td><td>certes… mais, il est vrai que… pourtant, bien que + subj.</td></tr>"
             "<tr><td>Illustration</td><td>ainsi, &agrave; titre d'exemple, c'est le cas de</td></tr>"
             "<tr><td>Synth&egrave;se</td><td>en d&eacute;finitive, il ressort que, au bout du compte</td></tr></table>"),
            ("La conclusion en 2 temps",
             "<p>La conclusion doit&nbsp;:</p>"
             "<ol><li><strong>R&eacute;capitulation</strong> &mdash; rappeler bri&egrave;vement les grandes &eacute;tapes du raisonnement</li>"
             "<li><strong>R&eacute;ponse &agrave; la probl&eacute;matique</strong> &mdash; apporter une r&eacute;ponse nuanc&eacute;e &agrave; la question de d&eacute;part</li></ol>"
             "<p>En option : une <strong>ouverture</strong> sur une question connexe ou une perspective &eacute;largie.</p>"
             "<p><em>&Agrave; &eacute;viter&nbsp;:</em> introduire de nouveaux arguments dans la conclusion, redire mot pour mot l'introduction.</p>"),
        ],
        "traps": [
            ("Plan dit 'catalogue'", "aligner des arguments sans les articuler entre eux ; la th&egrave;se et l'antith&egrave;se doivent s'opposer r&eacute;ellement, et la synth&egrave;se doit d&eacute;passer la contradiction."),
            ("Paraphrase du sujet", "reformuler le sujet sans l'analyser ; la probl&eacute;matique doit poser un vrai enjeu intellectuel, pas simplement rep&eacute;ter la question en d'autres mots."),
            ("Exemples sans analyse", "citer un exemple et passer &agrave; autre chose ; chaque exemple doit &ecirc;tre explicit&eacute; pour montrer en quoi il confirme l'argument."),
            ("Conclusion nouvelle", "introduire un argument neuf en conclusion ; la conclusion synth&eacute;tise, elle ne d&eacute;veloppe pas de nouvelles id&eacute;es."),
        ],
        "summary": [
            "Introduction : accroche + contextualisation + probl&eacute;matique + annonce du plan.",
            "D&eacute;veloppement : 3 parties (th&egrave;se / antith&egrave;se / synth&egrave;se), chacune avec paragraphes AAEX.",
            "Connecteurs logiques pour relier les id&eacute;es et fluidifier la lecture.",
            "Conclusion : r&eacute;capitulation + r&eacute;ponse &agrave; la probl&eacute;matique + ouverture facultative.",
        ],
        "ex1": {
            "q": "Quelle structure suit la dissertation fran&ccedil;aise traditionnelle ?",
            "opts": [
                "Introduction — d&eacute;veloppement libre — conclusion",
                "Th&egrave;se — antith&egrave;se — synth&egrave;se",
                "Probl&egrave;me — solution — &eacute;valuation",
                "Narration — description — argumentation",
            ],
            "ans": "Th&egrave;se — antith&egrave;se — synth&egrave;se",
            "exp": "La dissertation suit la structure dialectique : th&egrave;se (d&eacute;fendre une position), antith&egrave;se (nuancer), synth&egrave;se (d&eacute;passer la contradiction).",
        },
        "ex2": {
            "q": "Compl&eacute;tez : Un paragraphe argumentatif comprend une affirmation, un argument, un _____ et une transition.",
            "ans": "exemple",
            "exp": "La structure AAEX exige : Affirmation, Argument, EXemple concret, puis une transition vers le point suivant.",
            "accept": ["exemple concret", "ex.", "illustration"],
        },
        "ex3": {
            "q": "Quel connecteur est le plus adapt&eacute; pour introduire une nuance dans une antith&egrave;se ?",
            "opts": [
                "De plus",
                "N&eacute;anmoins",
                "Ainsi",
                "En outre",
            ],
            "ans": "N&eacute;anmoins",
            "exp": "'N&eacute;anmoins' (ainsi que 'cependant', 'toutefois', 'or') sert &agrave; introduire une opposition ou une nuance, typique de l'antith&egrave;se. 'De plus' et 'en outre' ajoutent ; 'ainsi' illustre.",
        },
        "game_desc": "Ma&icirc;trisez la structure et les techniques de la dissertation fran&ccedil;aise",
        "items": [
            ("diss-these", "la th&egrave;se", "premi&egrave;re partie d&eacute;fendant une position", "argument principal · affirmation · d&eacute;fense", "La th&egrave;se pr&eacute;sente la position principale que l'on va d&eacute;fendre.", "th&egrave;se = position principale &agrave; d&eacute;fendre", "position principale &agrave; d&eacute;fendre"),
            ("diss-antithese", "l'antith&egrave;se", "deuxi&egrave;me partie qui nuance ou contredit la th&egrave;se", "opposition · nuance · contre-argument", "L'antith&egrave;se ne r&eacute;fute pas la th&egrave;se, elle l'enrichit par une perspective oppos&eacute;e.", "antith&egrave;se = position oppos&eacute;e qui nuance", "deuxi&egrave;me partie qui nuance ou contredit la th&egrave;se"),
            ("diss-synthese", "la synth&egrave;se", "troisi&egrave;me partie qui d&eacute;passe la contradiction", "d&eacute;passement · conciliation · r&eacute;ponse", "La synth&egrave;se ne choisit pas un camp : elle d&eacute;passe la contradiction pour proposer une vision nouvelle.", "synth&egrave;se = d&eacute;passer th&egrave;se et antith&egrave;se", "troisi&egrave;me partie qui d&eacute;passe la contradiction"),
            ("diss-problematique", "la probl&eacute;matique", "question intellectuelle centrale qui structure la dissertation", "enjeu · question · analyse", "La probl&eacute;matique doit soulever un v&eacute;ritable enjeu, pas simplement recopier le sujet.", "probl&eacute;matique = question centrale &agrave; explorer", "question intellectuelle centrale qui structure la dissertation"),
            ("diss-accroche", "l'accroche", "&eacute;l&eacute;ment d'introduction qui capte l'attention du lecteur", "citation · fait · question rh&eacute;torique", "Une bonne accroche cr&eacute;e d'embl&eacute;e un int&eacute;r&ecirc;t pour le sujet.", "accroche = d&eacute;but qui capte l'attention", "&eacute;l&eacute;ment d'introduction qui capte l'attention"),
            ("diss-transition", "la transition", "phrase reliant deux parties ou deux arguments", "lien · articulation · progression", "Les transitions fluidifient la lecture et montrent la logique du raisonnement.", "transition = lien entre deux parties", "phrase reliant deux parties ou deux arguments"),
            ("diss-ouverture", "l'ouverture", "question &eacute;largie en fin de conclusion", "perspective · horizon · question connexe", "L'ouverture invite le lecteur &agrave; prolonger la r&eacute;flexion au-del&agrave; du sujet.", "ouverture = question &eacute;largie en conclusion", "question &eacute;largie en fin de conclusion"),
            ("diss-AAEX", "la structure AAEX", "Affirmation + Argument + EXemple pour chaque paragraphe", "paragraphe · exemple · argument", "Appliquer la structure AAEX garantit la rigueur de chaque paragraphe argumentatif.", "AAEX = Affirmation + Argument + Exemple", "Affirmation + Argument + EXemple pour chaque paragraphe"),
        ],
    },

    "la-synthese-de-documents": {
        "level": "b2",
        "section": "redaction",
        "num": "R02",
        "short": "La Synth&egrave;se de Documents",
        "title": "La Synth&egrave;se de Documents",
        "subtitle": "Confronter, articuler et pr&eacute;senter plusieurs sources",
        "slides": [
            ("Qu'est-ce que la synth&egrave;se ?",
             "<p>La synth&egrave;se de documents consiste &agrave; <strong>mettre en relation</strong> plusieurs textes autour d'une probl&eacute;matique commune, sans donner votre avis personnel.</p>"
             "<ul><li>Lire et analyser chaque document</li>"
             "<li>D&eacute;gager les id&eacute;es essentielles</li>"
             "<li>Organiser les convergences et les divergences</li>"
             "<li>R&eacute;diger de mani&egrave;re neutre et objective</li></ul>"
             "<p><em>La synth&egrave;se n'est pas un r&eacute;sum&eacute; des documents un par un — c'est une confrontation organis&eacute;e.</em></p>"),
            ("&Eacute;tapes de la m&eacute;thode",
             "<ol><li><strong>Lire</strong> chaque document et noter le th&egrave;me, l'auteur, la source, la date</li>"
             "<li><strong>D&eacute;gager</strong> les id&eacute;es principales (max. 3 par document)</li>"
             "<li><strong>Croiser</strong> les id&eacute;es : convergences, divergences, compl&eacute;mentarit&eacute;s</li>"
             "<li><strong>Trouver un plan</strong> th&eacute;matique (pas document par document)</li>"
             "<li><strong>R&eacute;diger</strong> en citant les sources avec des formules de renvoi</li></ol>"
             "<p>Plan type : 2 ou 3 parties th&eacute;matiques, chacune avec 2&ndash;3 paragraphes.</p>"),
            ("Formules de renvoi aux sources",
             "<p>Il faut toujours attribuer les id&eacute;es &agrave; leurs sources&nbsp;:</p>"
             "<table><tr><th>Formule</th><th>Usage</th></tr>"
             "<tr><td>Selon le document 1…</td><td>r&eacute;f&eacute;rence directe</td></tr>"
             "<tr><td>Comme le souligne l'auteur de…</td><td>mise en valeur</td></tr>"
             "<tr><td>Le texte B abonde dans ce sens…</td><td>convergence</td></tr>"
             "<tr><td>En revanche, le document 3 avance que…</td><td>divergence</td></tr>"
             "<tr><td>Les documents 1 et 2 s'accordent pour…</td><td>convergence multiple</td></tr></table>"),
            ("Neutralit&eacute; et objectivit&eacute;",
             "<p>La synth&egrave;se doit rester <strong>impersonnelle</strong>&nbsp;:</p>"
             "<ul><li><strong>&Agrave; &eacute;viter&nbsp;:</strong> je pense, &agrave; mon avis, il me semble</li>"
             "<li><strong>&Agrave; utiliser&nbsp;:</strong> il appara&icirc;t que, on peut constater, les documents montrent</li></ul>"
             "<p>Ne pas prendre parti entre les documents m&ecirc;me si leurs th&egrave;ses s'opposent.</p>"
             "<p><em>Exception&nbsp;:</em> si la consigne demande explicitement une prise de position.</p>"),
            ("Plan th&eacute;matique vs plan par document",
             "<p><strong>Plan th&eacute;matique</strong> (correct)&nbsp;: organiser les id&eacute;es en sous-th&egrave;mes transversaux</p>"
             "<p>Exemple&nbsp;:</p>"
             "<ul><li>I. Les avantages de la mondialisation (docs 1, 2, 3)</li>"
             "<li>II. Les limites et critiques (docs 2, 3, 4)</li>"
             "<li>III. Les alternatives propos&eacute;es (docs 1, 4)</li></ul>"
             "<p><strong>Plan par document</strong> (incorrect)&nbsp;: Document 1 dit… Document 2 dit… Document 3 dit… &rarr; ce n'est pas une synth&egrave;se, c'est une suite de r&eacute;sum&eacute;s.</p>"),
        ],
        "traps": [
            ("Plan document par document", "r&eacute;sumer chaque texte dans un paragraphe s&eacute;par&eacute; ; un plan th&eacute;matique croise les id&eacute;es de tous les documents."),
            ("Avis personnel", "exprimer votre opinion personnelle avec 'je pense' ; la synth&egrave;se requiert une posture neutre et objective sauf mention contraire."),
            ("Omission d'un document", "oublier de mentionner un des documents fournis ; toutes les sources doivent appara&icirc;tre dans la synth&egrave;se."),
            ("Citation mot pour mot", "recopier de longs passages des documents ; utilisez la paraphrase et les formules de renvoi."),
        ],
        "summary": [
            "La synth&egrave;se confronte plusieurs sources sans donner d'avis personnel.",
            "Plan th&eacute;matique obligatoire : jamais document par document.",
            "Formules de renvoi pour attribuer chaque id&eacute;e &agrave; sa source.",
            "Neutralit&eacute; et objectivit&eacute; du ton tout au long de la r&eacute;daction.",
        ],
        "ex1": {
            "q": "Quelle est la principale diff&eacute;rence entre une synth&egrave;se et un r&eacute;sum&eacute; de documents ?",
            "opts": [
                "La synth&egrave;se est plus courte que le r&eacute;sum&eacute;",
                "La synth&egrave;se donne votre opinion personnelle",
                "La synth&egrave;se croise les id&eacute;es de plusieurs textes de mani&egrave;re th&eacute;matique",
                "La synth&egrave;se suit les documents dans leur ordre de pr&eacute;sentation",
            ],
            "ans": "La synth&egrave;se croise les id&eacute;es de plusieurs textes de mani&egrave;re th&eacute;matique",
            "exp": "La synth&egrave;se organise les id&eacute;es selon des th&egrave;mes transversaux, en mettant en relation les convergences et divergences entre documents — pas en les r&eacute;sumant un par un.",
        },
        "ex2": {
            "q": "Reformulez cette phrase pour une synth&egrave;se (remplacez 'je pense') : 'Je pense que les deux documents s'accordent sur l'importance de l'&eacute;ducation.'",
            "ans": "Les deux documents s'accordent sur l'importance de l'éducation",
            "exp": "La synth&egrave;se exige une posture objective. 'Je pense' est personnel. Utiliser : 'il appara&icirc;t que', 'les documents montrent', 'on peut constater'.",
            "accept": ["il apparaît que les deux documents s'accordent", "les documents montrent", "on peut constater que"],
        },
        "ex3": {
            "q": "Quelle formule convient pour signaler une divergence entre deux documents ?",
            "opts": [
                "Les documents 1 et 2 s'accordent pour…",
                "En revanche, le document 2 avance que…",
                "Selon les deux textes…",
                "De m&ecirc;me, le texte B souligne…",
            ],
            "ans": "En revanche, le document 2 avance que…",
            "exp": "'En revanche' marque une opposition. 'S'accordent pour' et 'de m&ecirc;me' signalent des convergences ; 'selon les deux textes' ne marque pas de divergence.",
        },
        "game_desc": "Ma&icirc;trisez la m&eacute;thode de la synth&egrave;se de documents",
        "items": [
            ("synt-plan-thematique", "le plan th&eacute;matique", "organisation par th&egrave;mes transversaux, pas document par document", "th&egrave;mes · croisement · organisation", "Un plan th&eacute;matique montre les liens entre les sources mieux qu'un plan par document.", "plan th&eacute;matique = organisation par th&egrave;mes transversaux", "organisation par th&egrave;mes transversaux"),
            ("synt-convergence", "la convergence", "accord ou point commun entre plusieurs documents", "accord · point commun · s'accordent", "La convergence montre que plusieurs sources partagent la m&ecirc;me id&eacute;e.", "convergence = accord entre documents", "accord ou point commun entre plusieurs documents"),
            ("synt-divergence", "la divergence", "d&eacute;saccord ou point de diff&eacute;rence entre des documents", "opposition · diff&eacute;rence · en revanche", "La divergence enrichit la synth&egrave;se en montrant les tensions entre les sources.", "divergence = d&eacute;saccord entre documents", "d&eacute;saccord ou point de diff&eacute;rence entre des documents"),
            ("synt-neutralite", "la neutralit&eacute;", "absence d'opinion personnelle dans la synth&egrave;se", "objectivit&eacute; · impersonnel · sans avis", "La neutralit&eacute; exige d'&eacute;viter les formules &agrave; la premi&egrave;re personne.", "neutralit&eacute; = &eacute;criture sans avis personnel", "absence d'opinion personnelle dans la synth&egrave;se"),
            ("synt-paraphrase", "la paraphrase", "reformulation d'une id&eacute;e avec ses propres mots", "reformulation · ses mots · pr&eacute;cis", "La paraphrase &eacute;vite la copie directe tout en restant fid&egrave;le &agrave; l'id&eacute;e.", "paraphrase = reformuler avec ses propres mots", "reformulation d'une id&eacute;e avec ses propres mots"),
            ("synt-formule-renvoi", "la formule de renvoi", "expression attributant une id&eacute;e &agrave; sa source", "selon · comme le souligne · d'apr&egrave;s", "Utiliser des formules de renvoi est obligatoire pour attribuer chaque id&eacute;e &agrave; son document.", "formule de renvoi = attribuer une id&eacute;e &agrave; sa source", "expression attributant une id&eacute;e &agrave; sa source"),
            ("synt-problematique", "la probl&eacute;matique commune", "question centrale partag&eacute;e par tous les documents", "fil directeur · enjeu · question", "La probl&eacute;matique commune guide la lecture et l'organisation de la synth&egrave;se.", "probl&eacute;matique commune = fil conducteur de la synth&egrave;se", "question centrale partag&eacute;e par tous les documents"),
            ("synt-complementarite", "la compl&eacute;mentarit&eacute;", "situation o&ugrave; les documents s'enrichissent mutuellement", "compl&egrave;te · enrichit · abonde", "La compl&eacute;mentarit&eacute; montre comment les sources apportent des &eacute;clairages diff&eacute;rents.", "compl&eacute;mentarit&eacute; = les documents s'enrichissent mutuellement", "situation o&ugrave; les documents s'enrichissent mutuellement"),
        ],
    },

    "le-compte-rendu": {
        "level": "b2",
        "section": "redaction",
        "num": "R03",
        "short": "Le Compte Rendu",
        "title": "Le Compte Rendu",
        "subtitle": "Rapporter fid&egrave;lement des informations — r&eacute;union, article, &eacute;v&eacute;nement",
        "slides": [
            ("Qu'est-ce qu'un compte rendu ?",
             "<p>Le compte rendu est un document fonctionnel qui <strong>rapporte fid&egrave;lement</strong> le contenu d'un &eacute;v&eacute;nement (r&eacute;union, conf&eacute;rence, article, livre) sans interpr&eacute;tation personnelle.</p>"
             "<ul><li><strong>Compte rendu de r&eacute;union</strong> : decisions prises, points abord&eacute;s, participants</li>"
             "<li><strong>Compte rendu de lecture</strong> : th&egrave;ses, structure, exemples d'un texte</li>"
             "<li><strong>Compte rendu de conf&eacute;rence</strong> : interventions, questions, conclusions</li></ul>"
             "<p>Le ton est factuel, clair et neutre.</p>"),
            ("Structure du compte rendu",
             "<p>Un compte rendu bien organis&eacute; contient&nbsp;:</p>"
             "<ol><li><strong>En-t&ecirc;te</strong> : nature du document, date, lieu, participants</li>"
             "<li><strong>Objet / contexte</strong> : de quoi s'agit-il ? dans quel cadre ?</li>"
             "<li><strong>Corps</strong> : points trait&eacute;s dans l'ordre chronologique ou th&eacute;matique</li>"
             "<li><strong>Conclusions et suites</strong> : d&eacute;cisions, actions pr&eacute;vues, prochaine &eacute;tape</li></ol>"
             "<p>Les d&eacute;cisions ou points importants peuvent &ecirc;tre <strong>mis en valeur</strong> par des puces ou du gras.</p>"),
            ("Reformuler sans trahir",
             "<p>Un bon compte rendu ne recopie pas mot pour mot — il r&eacute;sume fid&egrave;lement&nbsp;:</p>"
             "<table><tr><th>Original</th><th>Reformulation</th></tr>"
             "<tr><td>M. Martin a dit : 'Nous devons absolument réduire les coûts.'</td><td>M. Martin a insisté sur la nécessité de réduire les coûts.</td></tr>"
             "<tr><td>Personne n'était d'accord sur la date.</td><td>La date n'a pas fait l'objet d'un consensus.</td></tr>"
             "<tr><td>On a finalement décidé de reporter la réunion.</td><td>Il a été décidé de reporter la réunion.</td></tr></table>"),
            ("Registre et ton du compte rendu",
             "<p>Le compte rendu est toujours &eacute;crit en <strong>registre formel</strong>&nbsp;:</p>"
             "<ul><li>Troisi&egrave;me personne &mdash; pas de 'je' ni de 'on' informel</li>"
             "<li>Tournures impersonnelles : <em>il a &eacute;t&eacute; d&eacute;cid&eacute; de, il est apparu que</em></li>"
             "<li>Verbes de rapportage : <em>souligner, insister sur, pr&eacute;coniser, proposer, conclure</em></li>"
             "<li>Pas d'adjectifs &eacute;valuatifs ('excellent', 'catastrophique') sauf citation</li></ul>"),
            ("Verbes de rapportage utiles",
             "<table><tr><th>Intention</th><th>Verbes</th></tr>"
             "<tr><td>Annoncer</td><td>annoncer, indiquer, pr&eacute;ciser, informer</td></tr>"
             "<tr><td>Argumenter</td><td>souligner, insister sur, avancer, d&eacute;fendre</td></tr>"
             "<tr><td>Proposer</td><td>sugg&eacute;rer, pr&eacute;coniser, recommander, proposer</td></tr>"
             "<tr><td>Conclure</td><td>conclure, estimer, consid&eacute;rer, juger</td></tr>"
             "<tr><td>S'opposer</td><td>contester, r&eacute;futer, nuancer, objecter</td></tr></table>"),
        ],
        "traps": [
            ("Opinions personnelles", "exprimer votre jugement sur les d&eacute;cisions rapport&eacute;es ; le compte rendu est factuel et neutre."),
            ("Copier mot pour mot", "recopier les paroles exactes sans reformuler ; utilisez les verbes de rapportage et le style indirect."),
            ("Omission des suites", "ne pas mentionner les d&eacute;cisions prises et les actions pr&eacute;vues ; ce sont des &eacute;l&eacute;ments essentiels."),
            ("D&eacute;sordre chronologique", "m&eacute;langer l'ordre des &eacute;v&eacute;nements ; suivre l'ordre logique ou chronologique."),
        ],
        "summary": [
            "Le compte rendu rapporte fid&egrave;lement sans interpr&eacute;tation personnelle.",
            "Structure : en-t&ecirc;te + objet + corps + conclusions/suites.",
            "Ton formel, troisi&egrave;me personne, tournures impersonnelles.",
            "Verbes de rapportage vari&eacute;s (souligner, pr&eacute;coniser, conclure).",
        ],
        "ex1": {
            "q": "Quel est le ton principal d'un compte rendu de r&eacute;union ?",
            "opts": [
                "Subjectif et personnel",
                "Factuel, neutre et formel",
                "Narratif et descriptif",
                "Argumentatif et persuasif",
            ],
            "ans": "Factuel, neutre et formel",
            "exp": "Le compte rendu rapporte les faits objectivement en registre formel. Les opinions personnelles et le registre familier n'y ont pas leur place.",
        },
        "ex2": {
            "q": "Reformulez cette phrase en style indirect formel : 'Il faut changer notre strat&eacute;gie.' (dit par Mme Dubois)",
            "ans": "Mme Dubois a souligné la nécessité de changer de stratégie",
            "exp": "Le style indirect formel utilise un verbe de rapportage (souligner, insister, pr&eacute;coniser) suivi d'une reformulation nominale ou infinitive.",
            "accept": ["Mme Dubois a insisté sur la nécessité", "Mme Dubois a préconisé", "Mme Dubois a estimé qu'il fallait"],
        },
        "ex3": {
            "q": "Quel &eacute;l&eacute;ment figure dans l'en-t&ecirc;te d'un compte rendu de r&eacute;union ?",
            "opts": [
                "Les arguments d&eacute;taill&eacute;s de chaque participant",
                "La liste des participants, la date et le lieu",
                "Une introduction avec accroche",
                "Les opinions personnelles du r&eacute;dacteur",
            ],
            "ans": "La liste des participants, la date et le lieu",
            "exp": "L'en-t&ecirc;te d'un compte rendu donne les informations contextuelles : nature de la r&eacute;union, date, lieu, participants pr&eacute;sents et excus&eacute;s.",
        },
        "game_desc": "Ma&icirc;trisez la r&eacute;daction du compte rendu formel",
        "items": [
            ("cr-en-tete", "l'en-t&ecirc;te", "informations contextuelles en d&eacute;but de compte rendu", "date · lieu · participants", "L'en-t&ecirc;te permet d'identifier imm&eacute;diatement le contexte du compte rendu.", "en-t&ecirc;te = contexte initial du compte rendu", "informations contextuelles en d&eacute;but de compte rendu"),
            ("cr-verbatim", "le verbatim", "transcription mot pour mot d'une prise de parole", "&agrave; &eacute;viter · citation · textuellement", "Le verbatim int&eacute;gral est inappropri&eacute; dans un compte rendu — on r&eacute;sume.", "verbatim = reproduction mot pour mot (&agrave; &eacute;viter)", "transcription mot pour mot d'une prise de parole"),
            ("cr-rapportage", "le verbe de rapportage", "verbe qui introduit une parole ou une id&eacute;e rapport&eacute;e", "souligner · pr&eacute;coniser · estimer", "Les verbes de rapportage vari&eacute;s rendent le compte rendu plus pr&eacute;cis.", "verbe de rapportage = introduit une parole rapport&eacute;e", "verbe qui introduit une parole ou une id&eacute;e rapport&eacute;e"),
            ("cr-impersonnel", "la tournure impersonnelle", "construction &eacute;vitant le sujet personnel dans le compte rendu", "il a &eacute;t&eacute; d&eacute;cid&eacute; · il est apparu", "Les tournures impersonnelles renforcent la neutralit&eacute; du document.", "tournure impersonnelle = &eacute;vite le 'je' ou le 'on'", "construction &eacute;vitant le sujet personnel"),
            ("cr-suites", "les suites", "d&eacute;cisions et actions pr&eacute;vues mentionn&eacute;es en conclusion", "d&eacute;cisions · actions · suite &agrave; donner", "La section 'suites' est essentielle dans un compte rendu de r&eacute;union.", "suites = d&eacute;cisions prises et actions &agrave; venir", "d&eacute;cisions et actions pr&eacute;vues mentionn&eacute;es en conclusion"),
            ("cr-reformulation", "la reformulation", "exprimer une id&eacute;e avec ses propres mots sans la trahir", "fid&egrave;le · ses mots · style indirect", "Une bonne reformulation reste fid&egrave;le au sens tout en &eacute;vitant la copie.", "reformulation = exprimer en d'autres mots", "exprimer une id&eacute;e avec ses propres mots sans la trahir"),
            ("cr-neutralite", "la neutralit&eacute;", "absence de jugement ou d'opinion dans le compte rendu", "objectif · factuel · sans &eacute;valuation", "La neutralit&eacute; distingue le compte rendu du commentaire ou de la critique.", "neutralit&eacute; = absence de jugement personnel", "absence de jugement ou d'opinion dans le compte rendu"),
            ("cr-chronologie", "la chronologie", "ordre temporel des &eacute;v&eacute;nements dans le compte rendu", "ordre · temps · d&eacute;roulement", "Suivre la chronologie facilite la lecture et la compr&eacute;hension du compte rendu.", "chronologie = ordre temporel des &eacute;v&eacute;nements", "ordre temporel des &eacute;v&eacute;nements dans le compte rendu"),
        ],
    },

    "le-texte-litteraire": {
        "level": "b2",
        "section": "redaction",
        "num": "R04",
        "short": "Le Texte Litt&eacute;raire",
        "title": "Le Texte Litt&eacute;raire",
        "subtitle": "Narration, description et registres litt&eacute;raires en fran&ccedil;ais avanc&eacute;",
        "slides": [
            ("Les genres litt&eacute;raires &agrave; conna&icirc;tre",
             "<p>Le texte litt&eacute;raire peut appartenir &agrave; diff&eacute;rents <strong>genres</strong>&nbsp;:</p>"
             "<ul><li><strong>Narratif</strong> : raconte une histoire (roman, nouvelle, conte)</li>"
             "<li><strong>Descriptif</strong> : peint un lieu, un personnage, une ambiance</li>"
             "<li><strong>Lyrique</strong> : exprime des &eacute;motions intimes (po&eacute;sie)</li>"
             "<li><strong>Argumentatif</strong> : d&eacute;fend une th&egrave;se (essai, pamphlet)</li>"
             "<li><strong>Satirique</strong> : critique par l'humour ou l'ironie</li></ul>"
             "<p>Un texte litt&eacute;raire m&ecirc;le souvent plusieurs registres.</p>"),
            ("Les temps de la narration",
             "<p>En fran&ccedil;ais litt&eacute;raire, la <strong>narration au pass&eacute;</strong> utilise&nbsp;:</p>"
             "<ul><li><strong>Pass&eacute; simple</strong> : action principale, fait ponctuel ('<em>il entra</em>')</li>"
             "<li><strong>Imparfait</strong> : description, habitude, arri&egrave;re-plan ('<em>il faisait froid</em>')</li>"
             "<li><strong>Plus-que-parfait</strong> : ant&eacute;riorit&eacute; par rapport au pass&eacute; ('<em>il avait oubli&eacute;</em>')</li></ul>"
             "<p>La <strong>narration au pr&eacute;sent</strong> (pr&eacute;sent de narration) donne un effet d'imm&eacute;diatisme.</p>"),
            ("Figures de style essentielles",
             "<table><tr><th>Figure</th><th>D&eacute;finition</th><th>Exemple</th></tr>"
             "<tr><td>M&eacute;taphore</td><td>identification directe</td><td><em>La vie est un voyage</em></td></tr>"
             "<tr><td>Comparaison</td><td>avec 'comme' ou 'tel'</td><td><em>Doux comme la soie</em></td></tr>"
             "<tr><td>Personnification</td><td>attribuer des qualit&eacute;s humaines</td><td><em>Le vent murmurait</em></td></tr>"
             "<tr><td>Hyperbole</td><td>exag&eacute;ration expressive</td><td><em>J'ai mille fois essayé</em></td></tr>"
             "<tr><td>Anaphore</td><td>r&eacute;p&eacute;tition en d&eacute;but</td><td><em>Il courait. Il courait. Il courait.</em></td></tr></table>"),
            ("La description efficace",
             "<p>Une bonne description litt&eacute;raire mobilise les <strong>cinq sens</strong>&nbsp;:</p>"
             "<ul><li>Vue : couleurs, formes, lumi&egrave;re, ombre</li>"
             "<li>Ou&iuml;e : sons, silences, rythmes</li>"
             "<li>Odorat : parfums, odeurs</li>"
             "<li>Toucher : textures, temp&eacute;ratures</li>"
             "<li>Go&ucirc;t : saveurs (si pertinent)</li></ul>"
             "<p>Privil&eacute;gier les <strong>d&eacute;tails significatifs</strong> plut&ocirc;t qu'une liste exhaustive.</p>"
             "<p><em>Technique&nbsp;:</em> ancrer la description dans la perception d'un personnage pour l'animer.</p>"),
            ("Rythme et style en litt&eacute;rature",
             "<p>Le style litt&eacute;raire se travaille sur la <strong>phrase</strong>&nbsp;:</p>"
             "<ul><li><strong>Phrase courte</strong> : rythme haletant, urgence, choc</li>"
             "<li><strong>Phrase longue</strong> : ampleur, m&eacute;ditation, d&eacute;tail</li>"
             "<li><strong>Alternance</strong> : varier les longueurs cr&eacute;e du dynamisme</li></ul>"
             "<p>Soigner les <strong>transitions narratives</strong>&nbsp;:</p>"
             "<ul><li>Saut de sc&egrave;ne : <em>Le lendemain, il se trouva face &agrave;…</em></li>"
             "<li>Flash-back : <em>Trois ans plus t&ocirc;t, tout avait commenc&eacute; quand…</em></li>"
             "<li>Changement de point de vue : <em>De l'autre c&ocirc;t&eacute; de la rue, Marie observait…</em></li></ul>"),
        ],
        "traps": [
            ("Pass&eacute; compos&eacute; dans la narration litt&eacute;raire", "utiliser le pass&eacute; compos&eacute; dans un texte litt&eacute;raire au lieu du pass&eacute; simple ; les grands textes fran&ccedil;ais utilisent le pass&eacute; simple pour les actions narratives."),
            ("Description sans ancrage sensoriel", "lister des &eacute;l&eacute;ments visuels sans faire appel aux autres sens ; une description riche mobilise vue, ou&iuml;e, odorat, toucher."),
            ("Figures de style plaqu&eacute;es", "ins&eacute;rer des m&eacute;taphores sans lien avec le propos ; les figures de style doivent servir le sens et l'&eacute;motion."),
            ("Dialogues mal ponctus", "oublier le tiret cadratin (—) pour les r&eacute;pliques et le guillemet fran&ccedil;ais (&laquo; &raquo;) pour l'introduction du dialogue."),
        ],
        "summary": [
            "Genres litt&eacute;raires : narratif, descriptif, lyrique, argumentatif, satirique.",
            "Narration au pass&eacute; : pass&eacute; simple (actions), imparfait (description), plus-que-parfait (ant&eacute;riorit&eacute;).",
            "Figures de style au service du sens et de l'&eacute;motion.",
            "Description sensorielle et style vari&eacute; (alternance courtes/longues phrases).",
        ],
        "ex1": {
            "q": "Quel temps verbal est utilis&eacute; pour les actions principales dans la narration litt&eacute;raire fran&ccedil;aise ?",
            "opts": [
                "Le pass&eacute; compos&eacute;",
                "L'imparfait",
                "Le pass&eacute; simple",
                "Le plus-que-parfait",
            ],
            "ans": "Le pass&eacute; simple",
            "exp": "Dans la narration litt&eacute;raire fran&ccedil;aise, le pass&eacute; simple exprime les actions ponctuelles qui font avancer le r&eacute;cit. L'imparfait est r&eacute;serv&eacute; aux descriptions et aux habitudes.",
        },
        "ex2": {
            "q": "Identifiez la figure de style : 'Le soleil s'endormit derri&egrave;re la colline.'",
            "ans": "personnification",
            "exp": "Attribuer une action humaine (s'endormir) &agrave; un &eacute;l&eacute;ment non humain (le soleil) est une personnification.",
            "accept": ["une personnification", "c'est une personnification"],
        },
        "ex3": {
            "q": "Quelle technique de description litt&eacute;raire est recommand&eacute;e pour rendre une sc&egrave;ne vivante ?",
            "opts": [
                "Lister tous les &eacute;l&eacute;ments visuels de la sc&egrave;ne",
                "Mobiliser les cinq sens et ancrer dans la perception d'un personnage",
                "Utiliser uniquement des adjectifs pr&eacute;cis",
                "Citer des sources historiques",
            ],
            "ans": "Mobiliser les cinq sens et ancrer dans la perception d'un personnage",
            "exp": "Une description vivante sollicite plusieurs sens (vue, ou&iuml;e, odorat, toucher) et est ancr&eacute;e dans le point de vue d'un personnage pour cr&eacute;er de l'immersion.",
        },
        "game_desc": "Ma&icirc;trisez la narration, la description et les figures de style litt&eacute;raires",
        "items": [
            ("litt-passe-simple", "le pass&eacute; simple", "temps narratif des actions ponctuelles en litt&eacute;rature", "narration · action · ponctuel", "Il entra sans frapper — le pass&eacute; simple donne un rythme net aux actions.", "pass&eacute; simple = temps des actions narratives", "temps narratif des actions ponctuelles en litt&eacute;rature"),
            ("litt-imparfait-narr", "l'imparfait narratif", "temps de la description et de l'arri&egrave;re-plan", "description · habitude · fond", "L'imparfait peint le d&eacute;cor et les &eacute;tats pendant que le pass&eacute; simple fait avancer l'action.", "imparfait = description et arri&egrave;re-plan", "temps de la description et de l'arri&egrave;re-plan"),
            ("litt-personnification", "la personnification", "attribuer des qualit&eacute;s humaines &agrave; un &eacute;l&eacute;ment non humain", "humain · nature · objet", "La personnification anime le r&eacute;cit en donnant vie aux &eacute;l&eacute;ments du d&eacute;cor.", "personnification = attribuer des actions humaines &agrave; la nature", "attribuer des qualit&eacute;s humaines &agrave; un &eacute;l&eacute;ment non humain"),
            ("litt-hyperbole", "l'hyperbole", "exag&eacute;ration expressive pour intensifier un effet", "exag&eacute;ration · intensit&eacute; · effet", "L'hyperbole cr&eacute;e un effet d'intensit&eacute; ou d'humour selon le contexte.", "hyperbole = exag&eacute;ration expressive", "exag&eacute;ration expressive pour intensifier un effet"),
            ("litt-anaphore", "l'anaphore", "r&eacute;p&eacute;tition d'un mot ou groupe en d&eacute;but de proposition", "r&eacute;p&eacute;tition · rythme · insistance", "L'anaphore cr&eacute;e un effet de martelage et renforce l'&eacute;motion dans le texte.", "anaphore = r&eacute;p&eacute;tition en d&eacute;but de proposition", "r&eacute;p&eacute;tition d'un mot ou groupe en d&eacute;but de proposition"),
            ("litt-sens", "l'ancrage sensoriel", "d&eacute;crire par les cinq sens pour immerger le lecteur", "vue · ou&iuml;e · odorat · toucher", "Un ancrage sensoriel r&eacute;ussi fait vivre la sc&egrave;ne plut&ocirc;t que de simplement la raconter.", "ancrage sensoriel = description par les cinq sens", "d&eacute;crire par les cinq sens pour immerger le lecteur"),
            ("litt-dialogue", "le dialogue litt&eacute;raire", "r&eacute;pliques entre personnages avec ponctuation fran&ccedil;aise", "tiret · guillemet · r&eacute;plique", "Le dialogue litt&eacute;raire utilise le tiret cadratin (—) pour chaque prise de parole.", "dialogue litt&eacute;raire = &eacute;changes avec ponctuation fran&ccedil;aise", "r&eacute;pliques entre personnages avec ponctuation fran&ccedil;aise"),
            ("litt-genre", "le registre litt&eacute;raire", "ton g&eacute;n&eacute;ral d'un texte (lyrique, satirique, &eacute;pique…)", "ton · g&eacute;nre · &eacute;motion", "Identifier le registre aide &agrave; adapter son style lors de l'&eacute;criture.", "registre litt&eacute;raire = ton g&eacute;n&eacute;ral du texte", "ton g&eacute;n&eacute;ral d'un texte (lyrique, satirique, &eacute;pique…)"),
        ],
    },
}
