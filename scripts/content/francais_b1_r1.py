"""
francais/b1 — Rédaction B1 — batch 1 (R01–R04)
"""

CHAPTERS = {

"exprimer-une-opinion": {
    "level": "b1",
    "section": "redaction",
    "num": "R01",
    "short": "Exprimer une Opinion",
    "title": "Exprimer une Opinion",
    "subtitle": "Donner son avis, nuancer et justifier",
    "slides": [
        ("Introduire son opinion",
         "À la première personne : <em>Je pense que, Je crois que, J'estime que, À mon avis, Selon moi, Pour ma part</em>.<br>"
         "Nuancé : <em>Il me semble que + indicatif, Il me semble difficile de + infinitif</em>."),
        ("Approuver et désapprouver",
         "<strong>Approuver :</strong> Je suis pour, Je suis favorable à, J'approuve, Je soutiens.<br>"
         "<strong>Désapprouver :</strong> Je suis contre, Je m'oppose à, Je désapprouve, Je rejette.<br>"
         "Neutre : Je ne suis ni pour ni contre."),
        ("Nuancer son opinion",
         "<em>Certes… mais, Il est vrai que… cependant, D'un côté… de l'autre, Bien que + subjonctif, Même si + indicatif</em>.<br>"
         "Exprimer une réserve : <em>À condition que, À moins que + subjonctif</em>."),
        ("Justifier son opinion",
         "Car, parce que, puisque, étant donné que, vu que, compte tenu de.<br>"
         "Exemple : <em>Je pense que cette mesure est efficace <strong>car</strong> elle a déjà prouvé ses résultats.</em>"),
        ("Structure d'un paragraphe d'opinion",
         "1. <strong>Affirmation</strong> : Énoncez votre opinion clairement.<br>"
         "2. <strong>Justification</strong> : Donnez la raison principale.<br>"
         "3. <strong>Exemple</strong> : Illustrez avec un exemple concret.<br>"
         "4. <strong>Nuance</strong> (facultatif) : Reconnaissez les limites de votre position."),
        ("Registre : formel vs familier",
         "Formel : <em>Il me semble, J'estime, À mon sens, Je considère que</em>.<br>"
         "Courant : <em>Je pense, Je crois, À mon avis</em>.<br>"
         "Familier (à éviter à l'écrit) : <em>Pour moi c'est clair, Je trouve que c'est nul</em>."),
    ],
    "traps": [
        ("Je pense + subjonctif", "Je pense que + indicatif (affirmation positive). Je ne pense pas que + subjonctif (doute/négation). *Je pense qu'il soit là → Je pense qu'il est là."),
        ("À mon avis + que", "À mon avis est suivi directement de la proposition sans 'que' : *À mon avis que c'est bien → À mon avis, c'est bien."),
        ("Bien que + indicatif", "Bien que déclenche toujours le subjonctif. *Bien qu'il est fatigué → Bien qu'il soit fatigué."),
        ("Certes seul", "'Certes' (= admittedly) doit être suivi d'une opposition : Certes c'est cher, mais ça en vaut la peine. Certes seul est incomplet."),
    ],
    "summary": [
        "Introduire : <strong>à mon avis, je pense que, j'estime que</strong> + indicatif.",
        "Nuancer : <strong>certes… mais, d'un côté… de l'autre, bien que</strong> + subjonctif.",
        "Justifier : <strong>car, parce que, puisque, étant donné que</strong>.",
        "Formel : <strong>j'estime, je considère, il me semble</strong>.",
        "Structure : affirmation → justification → exemple → nuance.",
    ],
    "ex1": {
        "q": "Quelle phrase introduit une opinion de façon formelle ?",
        "opts": [
            "À mon sens, cette politique est inefficace.",
            "Pour moi c'est nul.",
            "Moi je pense que c'est bien.",
            "C'est clair que ça marche pas.",
        ],
        "ans": "À mon sens, cette politique est inefficace.",
        "exp": "'À mon sens' est un marqueur d'opinion formel, suivi d'un vocabulaire soutenu. Les autres relèvent du registre familier ou oral.",
    },
    "ex2": {
        "q": "Complétez : 'Je soutiens cette mesure ___ elle réduit les inégalités.'",
        "ans": "car",
        "exp": "Connecteur de cause introduisant la justification : car / parce que / puisque. 'Car' ne peut pas se placer en début de phrase.",
        "accept": ["car", "parce que", "puisque", "étant donné que", "vu que"],
    },
    "ex3": {
        "q": "Quelle phrase nuance correctement une opinion ?",
        "opts": [
            "Certes ce projet coûte cher, mais il créera des emplois.",
            "Bien qu'il est utile, je suis contre.",
            "D'un côté c'est bien, d'autre côté c'est mal.",
            "Même si + elle part, je reste.",
        ],
        "ans": "Certes ce projet coûte cher, mais il créera des emplois.",
        "exp": "'Certes… mais' est la structure de concession correcte. 'Bien qu'il est' → faut le subjonctif (soit). 'D'autre côté' → de l'autre côté. 'Même si + elle part' est mal construit syntaxiquement.",
    },
    "game_desc": "Exprimer une opinion — marqueurs et structure",
    "items": [
        ("op-avis", "À mon avis", "Introduire une opinion de façon neutre", "exprimer son point de vue", "À mon avis, cette loi est juste.", "à mon avis = je pense que", "exprimer son point de vue"),
        ("op-estime", "J'estime que", "Introduire une opinion de façon formelle et soutenue", "opinion formelle", "J'estime que cette décision est mauvaise.", "j'estime = opinion formelle", "opinion formelle"),
        ("op-certes", "Certes… mais", "Concéder un point avant d'opposer son argument principal", "admettre un fait puis opposer", "Certes c'est cher, mais c'est efficace.", "certes + mais = concession", "admettre un fait puis opposer"),
        ("op-bien-que", "Bien que + subjonctif", "Exprimer une concession avec changement de mode", "concession → subjonctif", "Bien qu'il soit difficile, je l'approuve.", "bien que = concession + subjonctif", "concession → subjonctif"),
        ("op-car", "Car", "Connecteur de justification placé en milieu de phrase", "justifier une opinion", "Je soutiens cela car c'est efficace.", "car = parce que (milieu de phrase)", "justifier une opinion"),
        ("op-pour", "Je suis pour / contre", "Exprimer son soutien ou son opposition à une idée", "soutenir ou s'opposer", "Je suis pour cette réforme.", "pour/contre = soutien ou opposition", "soutenir ou s'opposer"),
        ("op-nuance", "D'un côté… de l'autre", "Présenter deux aspects d'une question", "deux facettes d'un argument", "D'un côté c'est utile, de l'autre c'est coûteux.", "d'un côté... de l'autre = deux aspects", "deux facettes d'un argument"),
        ("op-justifier", "Étant donné que", "Connecteur de cause formel pour justifier une opinion", "cause formelle", "Étant donné que les preuves manquent, je doute.", "étant donné que = cause formelle", "cause formelle"),
    ],
},

"argumenter-pour-et-contre": {
    "level": "b1",
    "section": "redaction",
    "num": "R02",
    "short": "Argumenter Pour et Contre",
    "title": "Argumenter Pour et Contre",
    "subtitle": "Structure d'un texte argumentatif équilibré",
    "slides": [
        ("Structure du texte pour/contre",
         "1. <strong>Introduction</strong> : Présenter le sujet et annoncer le plan.<br>"
         "2. <strong>Arguments pour</strong> : 2–3 arguments avec exemples.<br>"
         "3. <strong>Arguments contre</strong> : 2–3 arguments avec exemples.<br>"
         "4. <strong>Conclusion</strong> : Synthèse et prise de position personnelle."),
        ("Introduire le sujet",
         "<em>De nos jours, … est un sujet qui suscite beaucoup de débats.</em><br>"
         "<em>La question de … divise l'opinion publique.</em><br>"
         "<em>Nous allons examiner les arguments pour et contre …</em><br>"
         "<em>Dans quelle mesure … est-il/elle bénéfique ?</em>"),
        ("Présenter les arguments pour",
         "Premièrement / D'abord / En premier lieu… · Deuxièmement / Ensuite / De plus…<br>"
         "<em>L'un des principaux avantages est que…</em><br>"
         "<em>Il convient de souligner que…</em><br>"
         "<em>Force est de constater que…</em>"),
        ("Présenter les arguments contre",
         "Cependant / Néanmoins / Toutefois / En revanche…<br>"
         "<em>L'un des inconvénients majeurs est que…</em><br>"
         "<em>Il faut également noter que…</em><br>"
         "<em>On peut cependant objecter que…</em>"),
        ("Illustrer avec des exemples",
         "Par exemple · C'est le cas de · Ainsi · Tel est le cas lorsque…<br>"
         "Chiffres et statistiques : <em>Selon les études, … Pour cent des personnes…</em><br>"
         "Citations : <em>Comme le dit l'expert X, …</em>"),
        ("Conclure et prendre position",
         "<em>En définitive / En conclusion / Pour conclure / En somme…</em><br>"
         "<em>Après avoir examiné les différents aspects…</em><br>"
         "<em>Il ressort de cette analyse que…</em><br>"
         "Prise de position : <em>Je considère que… / Il me semble que… / Il est indéniable que…</em>"),
    ],
    "traps": [
        ("Plan en deux parties sans conclusion", "Un texte pour/contre doit toujours avoir une conclusion avec prise de position. Sans elle, le texte reste incomplet."),
        ("Connecteurs répétés", "Evitez de répéter toujours 'et', 'mais', 'donc'. Variez : d'abord/ensuite, cependant/néanmoins, ainsi/par exemple."),
        ("Exemples sans argument", "Un exemple seul n'est pas un argument. Structure : argument → exemple → analyse de l'exemple."),
        ("Introduction = copier-coller du sujet", "L'introduction doit reformuler et contextualiser le sujet, pas le recopier mot pour mot."),
    ],
    "summary": [
        "Structure : <strong>intro → arguments pour → arguments contre → conclusion</strong>.",
        "Intro : <em>De nos jours… · La question de… divise l'opinion</em>.",
        "Arguments pour : <strong>premièrement, de plus, l'un des avantages est que</strong>.",
        "Arguments contre : <strong>cependant, néanmoins, l'un des inconvénients est que</strong>.",
        "Conclusion : <strong>en définitive, il ressort que</strong> + prise de position.",
    ],
    "ex1": {
        "q": "Quel connecteur introduit un argument contraire ?",
        "opts": [
            "Cependant",
            "De plus",
            "Premièrement",
            "Par exemple",
        ],
        "ans": "Cependant",
        "exp": "'Cependant' introduit une opposition ou un argument contre. 'De plus' ajoute un argument dans le même sens. 'Premièrement' commence une liste. 'Par exemple' illustre.",
    },
    "ex2": {
        "q": "Comment introduire le sujet d'une dissertation ? Complétez : '___ jours, le télétravail est un sujet qui suscite beaucoup de débats.'",
        "ans": "De nos",
        "exp": "L'expression 'De nos jours' (= nowadays) introduit classiquement le contexte d'un texte argumentatif.",
        "accept": ["De nos", "de nos", "De nos jours,"],
    },
    "ex3": {
        "q": "Quelle phrase convient à une conclusion ?",
        "opts": [
            "En définitive, il ressort que les avantages l'emportent sur les inconvénients.",
            "Premièrement, c'est un sujet important.",
            "Par exemple, beaucoup de gens pensent cela.",
            "Cependant, il y a des avantages.",
        ],
        "ans": "En définitive, il ressort que les avantages l'emportent sur les inconvénients.",
        "exp": "'En définitive' marque la conclusion et 'il ressort que' synthétise l'analyse — structure typique d'une conclusion. 'Premièrement' appartient au développement. 'Par exemple' illustre. 'Cependant' introduit une opposition.",
    },
    "game_desc": "Argumenter pour et contre — structure et connecteurs",
    "items": [
        ("arg-intro", "Introduction argumentative", "Contextualiser le sujet et annoncer le plan", "présenter le thème et le plan", "De nos jours, la question divise l'opinion.", "intro = contexte + plan annoncé", "présenter le thème et le plan"),
        ("arg-premierement", "Premièrement / D'abord", "Connecteur pour présenter le premier argument", "introduire le premier point", "Premièrement, les coûts sont réduits.", "premièrement = premier argument", "introduire le premier point"),
        ("arg-de-plus", "De plus / En outre", "Connecteur pour ajouter un argument dans le même sens", "ajouter un argument positif", "De plus, cela crée des emplois.", "de plus = ajouter un argument", "ajouter un argument positif"),
        ("arg-cependant", "Cependant / Néanmoins", "Connecteur pour introduire un argument opposé", "présenter le contre-argument", "Cependant, les risques sont réels.", "cependant = mais (soutenu)", "présenter le contre-argument"),
        ("arg-avantage", "L'un des avantages est que", "Formule pour introduire un bénéfice", "présenter un point positif", "L'un des avantages est que c'est gratuit.", "avantage = point positif", "présenter un point positif"),
        ("arg-inconvenient", "L'un des inconvénients est que", "Formule pour introduire un problème", "présenter un point négatif", "L'un des inconvénients est que c'est long.", "inconvénient = point négatif", "présenter un point négatif"),
        ("arg-exemple", "Par exemple / Ainsi", "Connecteur pour illustrer un argument avec un exemple", "donner un exemple concret", "Ainsi, en France, le taux a baissé.", "par exemple / ainsi = illustrer", "donner un exemple concret"),
        ("arg-conclusion", "En définitive / En somme", "Connecteur pour introduire la conclusion générale", "conclure l'analyse", "En définitive, les avantages l'emportent.", "en définitive = conclusion finale", "conclure l'analyse"),
    ],
},

"ecrire-une-lettre-de-reclamation": {
    "level": "b1",
    "section": "redaction",
    "num": "R03",
    "short": "Lettre de Réclamation",
    "title": "Écrire une Lettre de Réclamation",
    "subtitle": "Structure, formules et ton formel",
    "slides": [
        ("Structure d'une lettre formelle",
         "[Vos coordonnées] · [Lieu, date] · [Coordonnées du destinataire]<br>"
         "Objet : Réclamation concernant…<br>"
         "Madame, Monsieur,<br>"
         "[Corps de la lettre en paragraphes]<br>"
         "Dans l'attente de votre réponse, veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées."),
        ("Exposer le problème",
         "<em>Je me permets de vous contacter au sujet de…</em><br>"
         "<em>J'ai l'honneur de vous signaler que…</em><br>"
         "<em>Suite à [l'achat / la commande / la livraison] du [date], je constate que…</em><br>"
         "<em>Je regrette de devoir vous informer que…</em>"),
        ("Décrire les faits",
         "Utilisez des dates précises et des numéros de référence.<br>"
         "<em>Le [date], j'ai commandé [produit] (référence n° …).</em><br>"
         "<em>Lors de la livraison, j'ai constaté que [description du problème].</em><br>"
         "<em>Malgré ma demande du [date], je n'ai pas reçu de réponse.</em>"),
        ("Formuler une demande",
         "<em>Je vous serais reconnaissant(e) de bien vouloir…</em><br>"
         "<em>Je vous prie de procéder au remboursement / remplacement / réparation.</em><br>"
         "<em>J'attends de votre part une réponse rapide.</em><br>"
         "<em>Dans le cas contraire, je me verrai dans l'obligation de…</em>"),
        ("Formules de politesse",
         "Simple : <em>Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées.</em><br>"
         "Plus court : <em>Dans l'attente de vous lire, je vous adresse mes cordiales salutations.</em><br>"
         "Jamais : <em>Cordialement</em> seul dans une lettre de réclamation (trop désinvolte)."),
        ("Ton et vocabulaire formel",
         "Toujours utiliser <em>vous</em>. Pas de <em>tu</em> même si vous connaissez la personne.<br>"
         "Éviter : <em>c'est nul, vous avez mal fait, c'est inacceptable !</em><br>"
         "Préférer : <em>Je suis dans l'obligation de vous signaler… / Cela ne correspond pas à…</em>"),
    ],
    "traps": [
        ("Madame/Monsieur avec virgule", "En français, la formule d'appel prend une virgule : 'Madame,' ou 'Monsieur,' — jamais de point d'exclamation."),
        ("Cordialement dans une réclamation", "'Cordialement' convient aux courriels professionnels courants mais pas à une lettre de réclamation formelle où on utilisera 'mes salutations distinguées'."),
        ("'Je vous serais reconnaissant de' + indicatif", "Après 'je vous serais reconnaissant(e) de', on met l'infinitif : *de vous répondre, pas *que vous répondez."),
        ("Oublier l'objet", "Une lettre de réclamation doit toujours avoir une ligne 'Objet :' qui résume le sujet en quelques mots."),
    ],
    "summary": [
        "Structure : <strong>coordonnées · objet · Madame, Monsieur · corps · formule de politesse</strong>.",
        "Exposer : <em>je me permets de vous contacter au sujet de…</em>",
        "Demander : <em>je vous serais reconnaissant(e) de bien vouloir + infinitif</em>.",
        "Formule finale : <strong>veuillez agréer… mes salutations distinguées</strong>.",
        "Ton <strong>formel</strong> : jamais d'exclamations ni d'émotions vives.",
    ],
    "ex1": {
        "q": "Quelle est la formule correcte pour exposer un problème dans une lettre de réclamation ?",
        "opts": [
            "Je me permets de vous contacter au sujet de ma commande défectueuse.",
            "Bonjour, votre produit est cassé !",
            "Cher Monsieur, vous avez mal fait votre travail.",
            "Salut, j'ai un problème.",
        ],
        "ans": "Je me permets de vous contacter au sujet de ma commande défectueuse.",
        "exp": "'Je me permets de vous contacter' est la formule formelle standard pour exposer un problème. Les autres appartiennent à un registre familier ou trop agressif.",
    },
    "ex2": {
        "q": "Complétez : 'Je vous ___ reconnaissant(e) de bien vouloir procéder au remboursement.'",
        "ans": "serais",
        "exp": "La formule complète est 'je vous serais reconnaissant(e) de + infinitif'. Le conditionnel 'serais' marque la politesse.",
        "accept": ["serais", "je vous serais"],
    },
    "ex3": {
        "q": "Quelle formule de clôture est correcte pour une lettre de réclamation ?",
        "opts": [
            "Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées.",
            "Cordialement.",
            "À bientôt !",
            "Bien à vous.",
        ],
        "ans": "Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées.",
        "exp": "La formule complète avec 'veuillez agréer… mes salutations distinguées' est la clôture formelle standard d'une lettre de réclamation. 'Cordialement' est pour les courriels courants; 'À bientôt' et 'Bien à vous' sont trop familiers.",
    },
    "game_desc": "Lettre de réclamation — structure et formules formelles",
    "items": [
        ("rec-objet", "L'Objet", "Ligne résumant le sujet de la lettre avant le corps", "résumé du sujet en quelques mots", "Objet : Réclamation commande n°1234.", "Objet = résumé de la lettre", "résumé du sujet en quelques mots"),
        ("rec-appel", "Madame, Monsieur", "Formule d'appel neutre quand on ne connaît pas le nom du destinataire", "appel formel sans nom", "Madame, Monsieur,", "Madame, Monsieur = appel formel", "appel formel sans nom"),
        ("rec-exposer", "Je me permets de vous contacter", "Formule pour introduire poliment le problème", "introduire le problème poliment", "Je me permets de vous contacter au sujet de…", "formule d'introduction formelle", "introduire le problème poliment"),
        ("rec-constater", "Je constate que / j'ai constaté que", "Formule neutre pour décrire le problème observé", "décrire le problème observément", "J'ai constaté que le produit était endommagé.", "constater = décrire le problème", "décrire le problème observément"),
        ("rec-demande", "Je vous serais reconnaissant(e) de", "Formule de demande polie au conditionnel + infinitif", "demande polie formelle", "Je vous serais reconnaissante de procéder au remboursement.", "je vous serais reconnaissant(e) de + inf.", "demande polie formelle"),
        ("rec-attente", "Dans l'attente de votre réponse", "Formule qui précède la clôture de la lettre", "transition vers la formule finale", "Dans l'attente de votre réponse, je vous…", "dans l'attente = avant la clôture", "transition vers la formule finale"),
        ("rec-cloture", "Veuillez agréer mes salutations distinguées", "Formule de politesse finale d'une lettre formelle", "formule de clôture formelle", "Veuillez agréer, Madame, l'expression de mes salutations distinguées.", "formule finale formelle", "formule de clôture formelle"),
        ("rec-ton", "Ton formel dans une réclamation", "Rester poli et factuel même en cas de mécontentement", "calme et factuel, pas agressif", "Je regrette de devoir signaler ce problème.", "ton = formel et factuel", "calme et factuel, pas agressif"),
    ],
},

"rediger-un-texte-informatif": {
    "level": "b1",
    "section": "redaction",
    "num": "R04",
    "short": "Texte Informatif",
    "title": "Rédiger un Texte Informatif",
    "subtitle": "Présenter des faits, expliquer et synthétiser",
    "slides": [
        ("Qu'est-ce qu'un texte informatif ?",
         "Un texte informatif <strong>présente des faits objectifs</strong> sans exprimer d'opinion personnelle.<br>"
         "Types : article de presse, rapport, compte rendu, fiche d'information, biographie.<br>"
         "Ton : neutre, impersonnel, factuel."),
        ("Organiser l'information",
         "Utilisez des <strong>titres et sous-titres</strong> si le format le permet.<br>"
         "Paragraphes courts avec <strong>une idée par paragraphe</strong>.<br>"
         "Ordre logique : du général au particulier, ou chronologique.<br>"
         "Données précises : chiffres, dates, sources."),
        ("Introduire les faits",
         "<em>Il est important de noter que… · Selon [source], … · D'après les statistiques, …</em><br>"
         "<em>Les recherches montrent que… · Il ressort des données que…</em><br>"
         "Impersonnel : <em>On constate que… · Il apparaît que… · Force est de constater que…</em>"),
        ("Expliquer et développer",
         "<em>En effet, … · C'est-à-dire que… · Autrement dit…</em> (reformuler)<br>"
         "<em>Cela s'explique par… · La raison en est que…</em> (expliquer)<br>"
         "<em>Il convient de distinguer… · Il faut préciser que…</em> (nuancer)"),
        ("Citer des sources",
         "<em>Selon le rapport de l'OMS (2024), …</em><br>"
         "<em>Comme l'indique l'étude publiée par…</em><br>"
         "<em>D'après les chiffres du ministère de la Santé…</em><br>"
         "Éviter <em>on dit que</em> (trop vague) → préférer une source précise."),
        ("Conclure un texte informatif",
         "<em>En conclusion… · Pour résumer… · En récapitulant…</em><br>"
         "<em>Il ressort de ces éléments que…</em><br>"
         "Un texte informatif ne prend <strong>pas de position</strong> — il synthétise sans juger.<br>"
         "Si une perspective est attendue, l'annoncer clairement."),
    ],
    "traps": [
        ("Opinion dans un texte informatif", "Un texte informatif ne contient pas 'je pense que' ni 'd'après moi'. Utiliser les formes impersonnelles : on observe, il ressort, les données montrent."),
        ("Selon moi vs Selon les données", "'Selon moi' = opinion personnelle. 'Selon les données / selon l'étude' = référence objective. Dans un texte informatif, utiliser uniquement la seconde."),
        ("En effet ≠ En fait", "'En effet' confirme ce qui précède. 'En fait' (= actually) corrige ou nuance. Ne pas les confondre."),
        ("Chiffres sans source", "Dans un texte informatif sérieux, chaque donnée chiffrée doit être attribuée à une source ou accompagnée d'une réserve : 'selon les estimations'."),
    ],
    "summary": [
        "Ton <strong>neutre et impersonnel</strong> : on constate, il ressort, selon les données.",
        "Structure : <strong>introduction → développement par paragraphes → conclusion</strong>.",
        "Expliquer : <em>en effet, c'est-à-dire, cela s'explique par</em>.",
        "Citer : <strong>selon [source], d'après les chiffres de</strong>.",
        "Pas d'opinion personnelle — synthétiser sans juger.",
    ],
    "ex1": {
        "q": "Quelle formule convient à un texte informatif impersonnel ?",
        "opts": [
            "Il ressort des données que la consommation a augmenté.",
            "Je pense que la consommation a augmenté.",
            "À mon avis, la consommation a augmenté.",
            "D'après moi, la consommation a augmenté.",
        ],
        "ans": "Il ressort des données que la consommation a augmenté.",
        "exp": "'Il ressort des données que' est impersonnel et objectif — idéal pour un texte informatif. Les autres formules ('je pense', 'à mon avis', 'd'après moi') expriment une opinion personnelle et ne conviennent pas à ce genre.",
    },
    "ex2": {
        "q": "Complétez : '___ le rapport de l'OMS, le taux de vaccination a progressé.'",
        "ans": "Selon",
        "exp": "'Selon [source]' est la formule standard pour citer une référence dans un texte informatif. 'D'après' est également acceptable.",
        "accept": ["Selon", "D'après", "D'apres"],
    },
    "ex3": {
        "q": "Quelle est la différence entre 'en effet' et 'en fait' ?",
        "opts": [
            "'En effet' confirme ; 'en fait' corrige ou nuance.",
            "'En effet' corrige ; 'en fait' confirme.",
            "Les deux signifient la même chose.",
            "'En effet' est oral ; 'en fait' est écrit.",
        ],
        "ans": "'En effet' confirme ; 'en fait' corrige ou nuance.",
        "exp": "'En effet' (= indeed) confirme ce qui vient d'être dit. 'En fait' (= actually / in fact) introduit une correction ou une nuance. Les deux s'utilisent à l'écrit et à l'oral.",
    },
    "game_desc": "Texte informatif — ton neutre et citation de sources",
    "items": [
        ("info-ton", "Ton impersonnel", "Utiliser des formes impersonnelles pour garder l'objectivité", "neutre et factuel, sans 'je'", "On constate que les prix ont augmenté.", "ton informatif = impersonnel", "neutre et factuel, sans 'je'"),
        ("info-selon", "Selon [source]", "Citer une source pour appuyer un fait", "attribuer un fait à une source", "Selon l'OMS, le taux a baissé.", "selon = citer une source", "attribuer un fait à une source"),
        ("info-il-ressort", "Il ressort que", "Formule pour synthétiser les résultats d'une analyse", "synthétiser objectivement", "Il ressort des données que la situation s'améliore.", "il ressort que = synthèse objective", "synthétiser objectivement"),
        ("info-en-effet", "En effet", "Confirmer ou développer ce qui précède", "confirmer un point", "Il fait froid. En effet, les températures sont négatives.", "en effet = confirmer, développer", "confirmer un point"),
        ("info-en-fait", "En fait", "Corriger ou nuancer ce qui précède", "corriger une idée", "On croit que c'est simple. En fait, c'est complexe.", "en fait = corriger ou nuancer", "corriger une idée"),
        ("info-cest-a-dire", "C'est-à-dire", "Reformuler une idée pour la rendre plus claire", "reformuler clairement", "Il est bilingue, c'est-à-dire qu'il parle deux langues.", "c'est-à-dire = reformuler", "reformuler clairement"),
        ("info-structure", "Structure informative", "Introduction → développement (un fait par paragraphe) → conclusion", "organiser un texte objectif", "Intro générale → faits détaillés → synthèse.", "structure = intro + faits + synthèse", "organiser un texte objectif"),
        ("info-sans-opinion", "Pas d'opinion", "Un texte informatif ne contient pas de 'je pense' ni 'd'après moi'", "objectif = sans avis personnel", "Éviter : je pense / à mon avis dans un rapport.", "informatif = sans opinion personnelle", "objectif = sans avis personnel"),
    ],
},

}
