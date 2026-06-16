"""
francais/b2 — Grammaire B2 — batch 3 (G09–G12)
"""

CHAPTERS = {

"les-connecteurs-avances": {
    "level": "b2",
    "section": "grammaire",
    "num": "G09",
    "short": "Les Connecteurs Avancés",
    "title": "Les Connecteurs Avancés",
    "subtitle": "Cohésion textuelle, nuance et registre soutenu",
    "slides": [
        ("Connecteurs de cause avancés",
         "<em>Vu que / Étant donné que / Compte tenu de</em> + nom/proposition : cause factuelle.<br>"
         "<em>D'autant que / D'autant plus que</em> : renforcer une cause.<br>"
         "<em>Faute de</em> + nom/inf. : cause par manque.<br>"
         "<em>Il est vrai que… mais</em> : concéder pour mieux réfuter."),
        ("Connecteurs de conséquence avancés",
         "<em>Si bien que</em> + indicatif : <em>Il a trop travaillé, si bien qu'il est épuisé.</em><br>"
         "<em>De sorte que</em> + indicatif : <em>Il a expliqué clairement, de sorte qu'on a compris.</em><br>"
         "<em>Au point que / À tel point que</em> + indicatif : intensité.<br>"
         "<em>C'est pourquoi / C'est la raison pour laquelle</em> : transition formelle."),
        ("Connecteurs de concession avancés",
         "<em>Quoi que</em> + subjonctif : <em>Quoi qu'il fasse, c'est bien.</em><br>"
         "<em>Quel(le)(s) que soit/soient</em> + subjonctif : <em>Quelle que soit la raison…</em><br>"
         "<em>Si + adj. + que + subjonctif</em> : <em>Si difficile que soit la tâche…</em><br>"
         "<em>Pour autant</em> (= cependant) : <em>Il est tard ; pour autant, je reste.</em>"),
        ("Connecteurs de restriction et d'addition",
         "<em>Certes… mais</em> · <em>Non seulement… mais encore</em> · <em>Bien plus</em> (= de plus, de surcroît)<br>"
         "<em>Outre cela / Outre le fait que</em> : addition formelle.<br>"
         "<em>Hormis / À l'exception de</em> : restriction/exclusion formelle.<br>"
         "<em>Sans compter que</em> : ajouter un fait supplémentaire."),
        ("Connecteurs de reformulation",
         "<em>C'est-à-dire que / Autrement dit / En d'autres termes</em> : reformuler.<br>"
         "<em>En effet</em> (= confirmer ce qui précède) · <em>En fait</em> (= corriger/nuancer).<br>"
         "<em>À savoir</em> : introduire une précision ou liste.<br>"
         "<em>Soit</em> (formel) : <em>Soit n personnes, soit… .</em>"),
        ("Connecteurs de transition et de structuration",
         "<em>D'une part… d'autre part</em> · <em>D'un côté… de l'autre</em>.<br>"
         "<em>Dans un premier temps… dans un second temps</em>.<br>"
         "<em>En ce qui concerne / Pour ce qui est de / Quant à</em> : changement de thème.<br>"
         "<em>Ceci dit / Cela étant</em> : transition concessive."),
    ],
    "traps": [
        ("Si bien que vs Si + adj + que", "'Si bien que' (= conséquence) + indicatif. 'Si difficile que' (= concession) + subjonctif. Ne pas les confondre."),
        ("Quoi que vs Quoique", "'Quoi que' = quelle que soit la chose que (+ subjonctif). 'Quoique' = bien que (+ subjonctif). Deux mots séparés : relativement libre; un seul mot : synonyme de bien que."),
        ("D'autant que vs D'autant plus que", "'D'autant que' = renforcer une cause (neutre). 'D'autant plus que' = renforcer avec emphase. 'D'autant moins que' = affaiblir la cause."),
        ("Outre que vs En plus de", "'Outre que' + proposition. 'Outre + nom'. 'En plus de + nom/infinitif'. Ne pas mélanger les structures."),
    ],
    "summary": [
        "<strong>Cause renforcée :</strong> d'autant que, étant donné que, faute de.",
        "<strong>Conséquence :</strong> si bien que, au point que, c'est la raison pour laquelle.",
        "<strong>Concession :</strong> quoi que, quel que soit, si + adj. + que + subj.",
        "<strong>Transition :</strong> d'une part…d'autre part, en ce qui concerne, quant à.",
        "<strong>Reformulation :</strong> c'est-à-dire, autrement dit, à savoir.",
    ],
    "ex1": {
        "q": "Quel connecteur exprime la conséquence avec intensité ?",
        "opts": [
            "Au point qu'il n'a pas pu dormir.",
            "Bien que le travail soit dur.",
            "Quoi qu'il arrive.",
            "D'autant que c'est important.",
        ],
        "ans": "Au point qu'il n'a pas pu dormir.",
        "exp": "'Au point que' exprime une conséquence marquant un degré élevé. 'Bien que' = concession. 'Quoi qu'il arrive' = concession généralisée. 'D'autant que' = renforcement de cause.",
    },
    "ex2": {
        "q": "Complétez : '___ soit sa décision, nous la respecterons.' (quelle que)",
        "ans": "Quelle que",
        "exp": "'Quel que soit' s'accorde avec le nom suivant. 'Décision' est féminin → Quelle que soit sa décision. Suivi du subjonctif.",
        "accept": ["Quelle que", "quelle que"],
    },
    "ex3": {
        "q": "Quelle phrase utilise correctement 'si bien que' ?",
        "opts": [
            "Il a trop travaillé, si bien qu'il est épuisé.",
            "Si bien qu'il travaille, il est épuisé.",
            "Si bien que difficile, il continue.",
            "Il est épuisé, si bien qu'il travaille.",
        ],
        "ans": "Il a trop travaillé, si bien qu'il est épuisé.",
        "exp": "'Si bien que' introduit la conséquence de ce qui précède : cause → si bien que → conséquence. 'Si bien qu'il travaille' ne fonctionne pas comme introduction. 'Si bien que difficile' est une erreur de construction.",
    },
    "game_desc": "Connecteurs avancés — cohésion et registre soutenu",
    "items": [
        ("con-au-point", "Au point que", "Conséquence marquant un degré élevé", "conséquence intense = au point que", "Il a tellement travaillé au point qu'il est épuisé.", "au point que = conséquence intense", "conséquence marquant un degré élevé"),
        ("con-si-bien", "Si bien que", "Conséquence logique d'une situation", "conséquence logique = si bien que + ind.", "Il a expliqué clairement, si bien qu'on a compris.", "si bien que = conséquence", "conséquence logique d'une situation"),
        ("con-quoi-que", "Quoi que + subjonctif", "Concession généralisée : quelle que soit la chose que", "quoi que = quelle que soit la chose + subj.", "Quoi qu'il fasse, je l'admire.", "quoi que + subjonctif = concession totale", "concession généralisée"),
        ("con-quel-que", "Quel que soit + subjonctif", "Concession sur un nom : quelle que soit + nom + subjonctif de être", "quel que soit + accord + subj.", "Quelle que soit la raison, je comprends.", "quel que soit = accordé + subjonctif", "concession sur un nom accordé"),
        ("con-d-autant", "D'autant que", "Renforcer une cause déjà évoquée", "renforcer la cause = d'autant que", "Je suis fatigué, d'autant que je n'ai pas dormi.", "d'autant que = cause renforcée", "renforcer une cause déjà évoquée"),
        ("con-cest-pourquoi", "C'est la raison pour laquelle", "Transition formelle de conséquence", "conséquence formelle = c'est la raison pour laquelle", "C'est la raison pour laquelle j'ai démissionné.", "c'est la raison pour laquelle = donc formel", "transition formelle de conséquence"),
        ("con-quant-a", "Quant à", "Changer de thème ou introduire un aspect particulier", "changer de thème = quant à", "Quant à moi, je reste neutre.", "quant à = pour ce qui est de", "changer de thème ou introduire un aspect"),
        ("con-autrement-dit", "Autrement dit", "Reformuler ce qui vient d'être dit pour clarifier", "reformuler = autrement dit", "Il est parti. Autrement dit, c'est fini.", "autrement dit = en d'autres termes", "reformuler pour clarifier"),
    ],
},

"le-style-indirect-avance": {
    "level": "b2",
    "section": "grammaire",
    "num": "G10",
    "short": "Le Style Indirect Avancé",
    "title": "Le Style Indirect Avancé",
    "subtitle": "Discours rapporté complexe, nuances et registre",
    "slides": [
        ("Rappel : les grandes règles",
         "Verbe intro au présent → temps inchangés.<br>"
         "Verbe intro au passé → présent → imparfait; PC → PQP; futur → conditionnel.<br>"
         "Les déictiques changent : ici → là; maintenant → alors; demain → le lendemain."),
        ("Style indirect libre",
         "Le style indirect libre mêle narration et discours sans verbe introducteur ni guillemets.<br>"
         "<em>Il sortit. Quelle journée ! Il n'en pouvait plus. Mais demain serait mieux.</em><br>"
         "Utilisé dans la littérature pour accéder aux pensées du personnage sans rupture narrative."),
        ("Rapporter des questions complexes",
         "Questions avec <em>si</em> (oui/non) · <em>ce que, ce qui, ce dont</em> · mots interrogatifs.<br>"
         "<em>Elle lui a demandé ce qu'il voulait faire de sa vie.</em><br>"
         "<em>Il a voulu savoir d'où elle venait et depuis combien de temps elle vivait là.</em><br>"
         "Pas d'inversion, jamais de point d'interrogation."),
        ("Rapporter des actes de parole variés",
         "Promettre : <em>Il a promis de venir.</em><br>"
         "Refuser : <em>Elle a refusé de participer.</em><br>"
         "Suggérer : <em>Il a suggéré qu'on parte ensemble.</em> (+ subjonctif)<br>"
         "Ordonner : <em>Il leur a ordonné de se taire.</em> (de + infinitif)<br>"
         "Nier : <em>Elle a nié avoir dit cela.</em>"),
        ("Concordance dans les subordonnées enchâssées",
         "Quand plusieurs propositions sont imbriquées, les décalages s'accumulent :<br>"
         "<em>Il a dit qu'elle avait pensé qu'il serait venu.</em><br>"
         "→ 'il serait venu' = il viendra (futur dans l'indirect au passé → conditionnel)<br>"
         "→ 'elle avait pensé' = elle pensait (passé) → PQP après un autre PQP = PQP."),
        ("Verbes introducteurs nuancés",
         "affirmer, soutenir, prétendre (assertif) · nier, démentir (négation)<br>"
         "admettre, reconnaître, concéder (concession) · insister sur, souligner (emphase)<br>"
         "ajouter, préciser, mentionner (addition) · s'interroger sur (doute)<br>"
         "Choisir le verbe introducteur pour nuancer le rapport fidèlement."),
    ],
    "traps": [
        ("Point d'interrogation dans l'indirect", "Au style indirect, la question devient une proposition déclarative. *Il a demandé où tu allais ? → Il a demandé où tu allais. (pas de point d'interrogation)"),
        ("Inversion dans l'indirect", "On ne conserve pas l'inversion sujet-verbe au style indirect. *Il a demandé où habitait-elle → Il a demandé où elle habitait."),
        ("Style indirect libre : temps et personne", "Dans le style indirect libre, les temps restent au passé et les pronoms à la 3e personne — mais les interrogations et exclamations sont conservées. C'est un entre-deux narratif/discursif."),
        ("Nier avoir + PP", "'Nier avoir + PP' est correct pour rapporter un démenti passé. 'Nier que + subjonctif' est aussi possible. Ne pas confondre avec 'nier de + inf.' (incorrect)."),
    ],
    "summary": [
        "<strong>Style indirect libre :</strong> narration + pensée sans guillemets ni introducteur.",
        "Questions complexes → <strong>ce que, ce qui, ce dont</strong>, mots interrogatifs (pas d'inversion).",
        "Verbes variés : <strong>promettre, refuser, suggérer, nier, admettre</strong>.",
        "Concordance enchâssée : les décalages <strong>s'accumulent</strong> selon la profondeur.",
        "Verbes introducteurs nuancés pour <strong>transcrire fidèlement l'intention</strong>.",
    ],
    "ex1": {
        "q": "Transformez : 'Qu'est-ce que tu veux faire ?' → Elle lui a demandé ___",
        "opts": [
            "ce qu'il voulait faire.",
            "qu'est-ce qu'il voulait faire.",
            "ce qu'il veut faire ?",
            "qu'il voulait quoi faire.",
        ],
        "ans": "ce qu'il voulait faire.",
        "exp": "'Qu'est-ce que' (objet direct) → 'ce que' au style indirect. Verbe au passé → présent (veut) devient imparfait (voulait). Pas d'inversion, pas de point d'interrogation.",
    },
    "ex2": {
        "q": "Quel verbe introducteur convient pour rapporter un démenti ?",
        "ans": "nier",
        "exp": "Nier = refuser de reconnaître la vérité d'une assertion. Elle a nié avoir dit cela. Autres verbes de démenti : démentir, contester, réfuter.",
        "accept": ["nier", "démentir", "contester", "réfuter"],
    },
    "ex3": {
        "q": "Quel exemple illustre le style indirect libre ?",
        "opts": [
            "Il se demandait. Après tout, la vie était courte. Pourquoi ne pas partir ?",
            "Il a dit : 'Je pars demain.'",
            "Il a dit qu'il partirait le lendemain.",
            "Il lui demanda s'il devait partir.",
        ],
        "ans": "Il se demandait. Après tout, la vie était courte. Pourquoi ne pas partir ?",
        "exp": "Le style indirect libre mêle narration (il se demandait, la vie était courte) et discours intérieur (Pourquoi ne pas partir?) sans guillemets ni verbe introducteur explicite. Les autres exemples sont : discours direct, style indirect classique, discours indirect avec verbe.",
    },
    "game_desc": "Style indirect avancé — complexe, libre et nuancé",
    "items": [
        ("sia-libre", "Style indirect libre", "Narration mêlant pensée du personnage sans verbe introducteur", "discours sans guillemets ni introducteur", "Elle était heureuse. Enfin la paix.", "style indirect libre = entre narration et discours", "narration mêlant pensée sans verbe introducteur"),
        ("sia-ce-que", "Ce que dans l'indirect", "Que/Qu'est-ce que → ce que au style indirect", "que → ce que dans l'indirect", "Il a demandé ce qu'elle voulait.", "ce que = objet dans l'indirect", "que → ce que au style indirect"),
        ("sia-verbes", "Verbes introducteurs variés", "Choisir le bon verbe pour transcrire l'acte de parole", "verbe introducteur = intention de l'acte", "Il a promis de revenir / Elle a nié.", "choisir le verbe selon l'intention", "verbe introducteur = intention de l'acte"),
        ("sia-nier", "Nier avoir + PP", "Rapporter un démenti portant sur une action passée", "démenti passé = nier avoir + PP", "Elle a nié avoir dit cela.", "nier avoir + PP = démenti passé", "démenti portant sur une action passée"),
        ("sia-pas-inversion", "Pas d'inversion dans l'indirect", "L'inversion sujet-verbe disparaît au style indirect", "style indirect = ordre SVO, pas d'inversion", "Il a demandé où elle habitait.", "indirect = pas d'inversion", "l'inversion sujet-verbe disparaît"),
        ("sia-pas-point-interro", "Pas de ? dans l'indirect", "La question indirecte ne prend pas de point d'interrogation", "indirect = pas de point d'interrogation", "Il a demandé si elle viendrait.", "indirect = pas de ?", "la question indirecte = phrase déclarative"),
        ("sia-enchasse", "Concordance enchâssée", "Les décalages temporels s'accumulent dans les subordonnées imbriquées", "plusieurs niveaux de décalage temporel", "Il a dit qu'elle avait pensé qu'il serait venu.", "enchâssement = décalages accumulés", "décalages temporels accumulés"),
        ("sia-suggerer", "Suggérer + subjonctif", "Suggérer que + subjonctif pour rapporter une proposition indirecte", "suggérer que + subjonctif", "Il a suggéré qu'on parte ensemble.", "suggérer que = subjonctif", "suggérer que + subjonctif"),
    ],
},

"les-registres-de-langue": {
    "level": "b2",
    "section": "grammaire",
    "num": "G11",
    "short": "Les Registres de Langue",
    "title": "Les Registres de Langue",
    "subtitle": "Soutenu, courant, familier et argot",
    "slides": [
        ("Les quatre registres",
         "<strong>Soutenu (ou littéraire) :</strong> textes officiels, littérature, discours formels.<br>"
         "<strong>Courant (ou standard) :</strong> conversation ordinaire, journaux, courriels professionnels.<br>"
         "<strong>Familier :</strong> conversations entre amis, SMS, style décontracté.<br>"
         "<strong>Argotique ou populaire :</strong> très informel, parfois limité à certains groupes."),
        ("Marqueurs du registre soutenu",
         "Vocabulaire : <em>demeure (maison), époux (mari), s'en aller (partir), naguère (récemment)</em>.<br>"
         "Grammaire : inversion sujet-verbe dans les questions, subjonctif imparfait, passé simple.<br>"
         "Formules : <em>Veuillez, Je vous prie de, Il convient de, À cet égard.</em>"),
        ("Marqueurs du registre courant",
         "Vocabulaire : <em>maison, mari, partir, récemment</em>.<br>"
         "Questions : <em>Est-ce que tu viens ?</em> ou <em>Tu viens ?</em> (pas d'inversion)<br>"
         "Formules : <em>Bonjour, Je voudrais, S'il vous plaît, Cordialement.</em>"),
        ("Marqueurs du registre familier",
         "Vocabulaire : <em>boulot (travail), bouffe (nourriture), bosser (travailler), sympa, super</em>.<br>"
         "Grammaire : suppression du ne de négation (<em>Je sais pas</em>), <em>on</em> pour <em>nous</em>.<br>"
         "Questions : <em>T'as vu ? T'as un stylo ?</em> (suppression du sujet)"),
        ("Choisir le bon registre",
         "Adapte le registre à la situation : <strong>destinataire, contexte, support</strong>.<br>"
         "Lettre de candidature → soutenu. Courriel au collègue → courant. SMS à un ami → familier.<br>"
         "Erreur courante : mélanger les registres dans un même texte."),
        ("Registres et grammaire : quelques différences",
         "Interrogation : <em>Vient-il ?</em> (soutenu) · <em>Est-ce qu'il vient ?</em> (courant) · <em>Il vient ?</em> (familier)<br>"
         "Négation : <em>Je ne sais pas</em> (courant) · <em>Je sais pas</em> (familier)<br>"
         "Pronom : <em>nous</em> (courant/soutenu) · <em>on</em> (familier/courant)<br>"
         "Futur : <em>je partirai</em> (courant/soutenu) · <em>je vais partir</em> (familier/courant)"),
    ],
    "traps": [
        ("Ne de négation à l'oral", "À l'oral familier, le 'ne' est souvent omis. À l'écrit, même dans un registre courant, conserver ne…pas. *J'sais pas (oral) → Je ne sais pas (écrit courant)."),
        ("On vs Nous", "'On' peut remplacer 'nous' à l'oral familier et courant. À l'écrit formel, préférer 'nous'. Les deux sont grammaticalement corrects dans un contexte approprié."),
        ("Vocabulaire soutenu ≠ plus correct", "Le registre soutenu n'est pas 'plus correct' — il est adapté à certains contextes. Utiliser 'époux' dans un SMS serait bizarre. L'adéquation au contexte prime."),
        ("Inversion dans les questions", "L'inversion sujet-verbe (Vient-il ?) est formelle. À l'oral courant, on utilise 'est-ce que' ou la question intonative. Forcer l'inversion à l'oral sonne pédant."),
    ],
    "summary": [
        "<strong>Soutenu :</strong> inversion, subjonctif imparfait, vocabulaire littéraire.",
        "<strong>Courant :</strong> est-ce que, ne…pas, nous, vocabulaire standard.",
        "<strong>Familier :</strong> omission du ne, on pour nous, verlan, contractions.",
        "Adapter le registre au <strong>destinataire, contexte et support</strong>.",
        "Éviter de <strong>mélanger les registres</strong> dans un même texte.",
    ],
    "ex1": {
        "q": "Quelle question appartient au registre soutenu ?",
        "opts": [
            "Venez-vous à la réunion ?",
            "Est-ce que vous venez à la réunion ?",
            "Vous venez à la réunion ?",
            "T'viens à la réunion ?",
        ],
        "ans": "Venez-vous à la réunion ?",
        "exp": "L'inversion sujet-verbe (Venez-vous) marque le registre soutenu. 'Est-ce que vous venez' est courant. 'Vous venez ?' est familier/courant. 'T'viens' est très familier.",
    },
    "ex2": {
        "q": "Quel mot est du registre familier pour 'travail' ?",
        "ans": "boulot",
        "exp": "Boulot = travail (registre familier). Équivalents : boulot, taf, job (plus courant).",
        "accept": ["boulot", "taf", "job"],
    },
    "ex3": {
        "q": "Dans quel contexte est-il correct d'omettre le 'ne' de négation ?",
        "opts": [
            "Dans une conversation orale informelle.",
            "Dans une lettre de candidature.",
            "Dans un article de journal.",
            "Dans un rapport officiel.",
        ],
        "ans": "Dans une conversation orale informelle.",
        "exp": "L'omission du 'ne' (Je sais pas) est acceptable à l'oral familier et informel. Dans les contextes écrits formels (lettre, rapport, article), le 'ne' est obligatoire.",
    },
    "game_desc": "Registres de langue — soutenu, courant, familier",
    "items": [
        ("reg-soutenu", "Registre soutenu", "Textes officiels, discours formels, littérature", "soutenu = formel et élaboré", "Veuillez agréer mes salutations distinguées.", "soutenu = officiel, littéraire", "textes officiels et discours formels"),
        ("reg-courant", "Registre courant", "Conversation ordinaire, courriels pro, journaux", "courant = standard, quotidien", "Je voudrais vous parler.", "courant = standard quotidien", "conversation ordinaire et textes standard"),
        ("reg-familier", "Registre familier", "Conversations entre amis, SMS, style décontracté", "familier = informel entre proches", "T'as vu ce film ?", "familier = entre amis, décontracté", "conversations informelles entre proches"),
        ("reg-boulot", "Boulot / Bosser", "Vocabulaire familier pour travail/travailler", "vocabulaire familier du travail", "J'ai trop bossé aujourd'hui.", "boulot = travail (familier)", "vocabulaire familier pour travail"),
        ("reg-ne-omis", "Omission du ne", "À l'oral familier, le ne de négation est souvent omis", "ne omis = oral familier", "Je sais pas. (familier) / Je ne sais pas. (courant)", "ne omis = oral informel", "ne omis à l'oral familier"),
        ("reg-on-nous", "On pour nous", "'On' remplace 'nous' à l'oral courant et familier", "on = nous à l'oral", "On y va ? (familier/courant)", "on = nous à l'oral", "on remplace nous à l'oral"),
        ("reg-inversion", "Inversion soutenue", "L'inversion sujet-verbe dans les questions est formelle", "inversion = registre soutenu", "Vient-il demain ?", "inversion = soutenu", "inversion dans les questions = formel"),
        ("reg-adapter", "Adapter le registre", "Choisir le registre approprié selon le destinataire et le contexte", "registre = adapté au contexte", "Lettre formelle ≠ SMS à un ami.", "adapter le registre = compétence clé", "registre approprié selon contexte"),
    ],
},

"la-syntaxe-avancee": {
    "level": "b2",
    "section": "grammaire",
    "num": "G12",
    "short": "La Syntaxe Avancée",
    "title": "La Syntaxe Avancée",
    "subtitle": "Constructions complexes, ellipses et cohésion textuelle",
    "slides": [
        ("Ellipses et économie de langue",
         "L'ellipse supprime un élément récupérable du contexte :<br>"
         "<em>Tu viens ? — Oui, je viens.</em> → <em>Oui.</em> (ellipse du verbe)<br>"
         "<em>Paul a travaillé toute la nuit et Marie aussi.</em> (ellipse de 'a travaillé toute la nuit')<br>"
         "Très courante à l'oral et dans les textes courts."),
        ("Propositions participiales et absolues",
         "Participiale : participe présent ou passé avec un sujet propre :<br>"
         "<em>Le soleil se couchant, ils rentrèrent.</em><br>"
         "Absolue : groupe nominal + participe, souvent détaché :<br>"
         "<em>La réunion terminée, chacun reprit son travail.</em>"),
        ("Anaphore et cohésion référentielle",
         "<strong>Anaphore</strong> = reprise d'un élément déjà mentionné.<br>"
         "Pronoms (il, elle, le, y, en), groupes nominaux (ce dernier, celui-ci, ledit).<br>"
         "Éviter les ambiguïtés : s'assurer que l'antécédent est clair.<br>"
         "<em>Paul a vu Marc. Il lui a dit bonjour.</em> → Qui est 'il' ? Risque d'ambiguïté."),
        ("Prolepse et structures détachées",
         "Prolepse = anticipation d'un élément repris par un pronom :<br>"
         "<em>Ce problème, je le connais bien.</em> (reprise par 'le')<br>"
         "Apposition : <em>Paris, <u>capitale de la France</u>, accueille des millions de touristes.</em><br>"
         "Incises : <em>Il est venu, <u>comme prévu</u>, à l'heure.</em>"),
        ("Subordination multiple",
         "Plusieurs propositions subordonnées peuvent s'enchaîner :<br>"
         "<em>Je pense que ce projet, bien qu'il soit ambitieux, pourrait réussir si nous obtenons les fonds.</em><br>"
         "Veiller à la concordance des temps et à la clarté de la structure."),
        ("Cohésion textuelle : outils avancés",
         "<strong>Connecteurs</strong> (d'abord/ensuite/enfin) · <strong>Anaphores</strong> (il, ce dernier) · <strong>Hyperonymes</strong> (animal pour chat) · <strong>Synonymes</strong> (problème/difficulté/enjeu).<br>"
         "La variété lexicale et la reprise pronominale assurent la cohésion sans répétition."),
    ],
    "traps": [
        ("Proposition participiale : sujet différent", "Le sujet de la participiale doit être différent de celui de la principale pour former une structure absolue. Si le sujet est le même, utiliser le participe seul : 'Arrivé chez lui, il s'est assis.' (pas 'Lui arrivé, il s'est assis.')"),
        ("Ambiguïté des anaphores", "Quand un pronom peut référer à plusieurs antécédents, reformuler pour éviter l'ambiguïté. 'Il lui a dit' avec deux personnes mentionnées → préciser le nom."),
        ("Ellipse et registre", "L'ellipse est naturelle à l'oral et dans certains styles. Dans les textes formels et académiques, préférer des phrases complètes sauf quand la reprise est très claire."),
        ("Ledit / ladite : usage formel", "'Ledit contrat, ladite disposition' sont des termes juridiques/administratifs. Éviter dans les textes courants où 'ce contrat, cette disposition' suffisent."),
    ],
    "summary": [
        "<strong>Ellipse :</strong> suppression d'un élément récupérable du contexte.",
        "<strong>Participiale absolue :</strong> la réunion terminée, chacun repartit.",
        "<strong>Anaphore :</strong> reprise pronominale ou nominale sans ambiguïté.",
        "<strong>Prolepse :</strong> anticipation + reprise pronominale (Ce livre, je l'aime).",
        "Cohésion : connecteurs + anaphores + synonymes + <strong>hyperonymes</strong>.",
    ],
    "ex1": {
        "q": "Quelle construction utilise une participiale absolue ?",
        "opts": [
            "La réunion terminée, chacun repartit chez soi.",
            "Terminant la réunion, il est parti.",
            "Quand la réunion a fini, il est parti.",
            "Il est parti après la réunion.",
        ],
        "ans": "La réunion terminée, chacun repartit chez soi.",
        "exp": "La participiale absolue : groupe nominal (la réunion) + participe passé (terminée), détaché, avec son propre sujet logique. 'Terminant la réunion' est un gérondif (même sujet). 'Quand' introduit une temporelle. 'Après' introduit un groupe prépositionnel.",
    },
    "ex2": {
        "q": "Identifiez l'ellipse : 'Paul a réussi son examen et Marie aussi.'",
        "ans": "a réussi son examen",
        "exp": "Dans 'Marie aussi', on sous-entend 'a réussi son examen' — c'est l'élément ellipsé, récupérable grâce au contexte.",
        "accept": ["a réussi son examen", "a réussi", "réussi son examen"],
    },
    "ex3": {
        "q": "Quelle phrase utilise une anaphore claire ?",
        "opts": [
            "Marie a rencontré Sophie. Elle lui a souri.",
            "Paul a vu Marc. Il lui a dit bonjour.",
            "J'ai acheté un livre. Il est cher.",
            "Elle est venue. Elle est repartie.",
        ],
        "ans": "J'ai acheté un livre. Il est cher.",
        "exp": "'Il' réfère clairement à 'un livre' (seul antécédent possible). Les autres phrases ont des antécédents ambigus : 'Elle' et 'lui' dans les deux premières phrases pourraient référer à l'une ou l'autre personne. La quatrième répète 'elle' avec une ambiguïté sur le référent.",
    },
    "game_desc": "Syntaxe avancée — ellipse, anaphore et cohésion",
    "items": [
        ("syn-ellipse", "Ellipse", "Suppression d'un élément récupérable du contexte linguistique", "omission récupérable", "Tu viens ? — Oui. (ellipse de 'je viens')", "ellipse = omission récupérable", "suppression d'un élément récupérable"),
        ("syn-participiale", "Participiale absolue", "Groupe nominal + participe avec sujet propre, détaché de la principale", "sujet propre + participe = absolue", "La réunion terminée, il est parti.", "participiale absolue = sujet propre + participe", "groupe nominal + participe détaché"),
        ("syn-anaphore", "Anaphore", "Reprise d'un élément déjà mentionné par un pronom ou un groupe nominal", "reprise d'un élément = anaphore", "Paul est arrivé. Il s'est assis.", "anaphore = reprise sans répétition", "reprise d'un élément déjà mentionné"),
        ("syn-prolepse", "Prolepse", "Anticipation d'un nom repris ensuite par un pronom", "nom anticipé + reprise pronominale", "Ce film, je l'adore.", "prolepse = anticipation + pronom", "anticipation d'un nom repris par pronom"),
        ("syn-apposition", "Apposition", "Groupe nominal détaché précisant ou explicitant un autre nom", "nom + apposition explicative", "Paris, capitale de la France, est magnifique.", "apposition = précision détachée", "groupe nominal explicatif détaché"),
        ("syn-coherence", "Cohésion textuelle", "Maintenir la clarté et l'unité d'un texte par des outils variés", "connecteurs + anaphores + synonymes", "D'abord… ensuite… enfin… ce problème… cette difficulté.", "cohésion = outils de liaison", "maintenir clarté et unité du texte"),
        ("syn-ambiguite", "Ambiguïté des pronoms", "Un pronom ambigu peut référer à plusieurs antécédents — à éviter", "pronom ambigu = reformuler", "Il lui a dit bonjour. (qui est il ?)", "ambiguïté = reformuler pour clarifier", "pronom ambigu à éviter"),
        ("syn-synonyme", "Synonymes et hyperonymes", "Varier le vocabulaire de reprise pour éviter les répétitions", "synonyme/hyperonyme pour éviter répétition", "chat → animal domestique → il.", "synonyme et hyperonyme = cohésion", "varier le vocabulaire de reprise"),
    ],
},

}
