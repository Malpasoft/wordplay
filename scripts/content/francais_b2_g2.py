"""
francais/b2 — Grammaire B2 — batch 2 (G05–G08)
"""

CHAPTERS = {

"la-nominalisation": {
    "level": "b2",
    "section": "grammaire",
    "num": "G05",
    "short": "La Nominalisation",
    "title": "La Nominalisation",
    "subtitle": "Transformer un verbe ou un adjectif en nom",
    "slides": [
        ("Qu'est-ce que la nominalisation ?",
         "Transformer un verbe ou un adjectif en <strong>groupe nominal</strong>.<br>"
         "Utile dans les textes formels pour alléger et varier le style.<br>"
         "<em>On a décidé que… → La décision de…</em>"),
        ("Suffixes de nominalisation (verbe → nom)",
         "<strong>-tion / -sion :</strong> décider → la décision · construire → la construction<br>"
         "<strong>-ment :</strong> développer → le développement · traiter → le traitement<br>"
         "<strong>-age :</strong> recycler → le recyclage · marier → le mariage<br>"
         "<strong>-ure :</strong> ouvrir → l'ouverture · fermer → la fermeture<br>"
         "<strong>-ée / -ie :</strong> entrer → l'entrée · sortir → la sortie"),
        ("Nominalisation d'adjectifs",
         "<strong>-ité :</strong> égal → l'égalité · rapide → la rapidité · capable → la capacité<br>"
         "<strong>-esse :</strong> triste → la tristesse · riche → la richesse<br>"
         "<strong>-eur :</strong> peur → la peur (déjà nom) · blanc → la blancheur<br>"
         "<strong>-ance / -ence :</strong> tolérant → la tolérance · différent → la différence"),
        ("Nominalisation dans les textes formels",
         "Dans les textes officiels et académiques, on préfère souvent le groupe nominal :<br>"
         "<em>Il a proposé qu'on améliore le système.</em><br>"
         "→ <em>Sa proposition d'amélioration du système a été acceptée.</em><br>"
         "Avantage : concision et style impersonnel."),
        ("Dénominalisation : pièges de traduction",
         "Le français nominalise plus que l'anglais. Ne pas surestimer la traduction directe :<br>"
         "<em>to decide → décider / la décision</em><br>"
         "<em>to develop → développer / le développement</em><br>"
         "Choisir entre verbe et nom selon le registre et la cohérence du texte."),
        ("Exercice de style : paraphrase nominale",
         "On a construit une nouvelle école. → La construction d'une nouvelle école.<br>"
         "Les enfants sont arrivés à l'heure. → L'arrivée des enfants à l'heure.<br>"
         "Le gouvernement a décidé d'agir. → La décision du gouvernement d'agir."),
    ],
    "traps": [
        ("Suffixe incorrect", "Ne pas inventer des nominalisations. *Décidement n'existe pas (≠ décision). Mémoriser les suffixes courants et les formes correctes."),
        ("Genre du nom nominalisé", "Les noms en -tion et -sion sont féminins. Les noms en -ment sont masculins. Vérifier le genre avec le dictionnaire pour les formes moins courantes."),
        ("Nominalisation excessive", "Trop de nominalisations rendent le texte lourd. Alterner verbes et noms pour un style équilibré. Les textes administratifs abusent souvent de la nominalisation."),
        ("Perte d'information dans la nominalisation", "La nominalisation peut supprimer le sujet de l'action. 'Le gouvernement a décidé' → 'la décision a été prise' : on ne sait plus qui a décidé."),
    ],
    "summary": [
        "Verbe → nom : <strong>-tion/-sion, -ment, -age, -ure, -ée</strong>.",
        "Adjectif → nom : <strong>-ité, -esse, -eur, -ance/-ence</strong>.",
        "Nominalisation = style <strong>formel et concis</strong>.",
        "Noms en <strong>-tion/-sion → féminins</strong>; noms en <strong>-ment → masculins</strong>.",
        "Alterner verbes et noms pour éviter un style <strong>lourd</strong>.",
    ],
    "ex1": {
        "q": "Quel est le nom correspondant au verbe 'développer' ?",
        "opts": ["le développement", "la développation", "le développage", "la développence"],
        "ans": "le développement",
        "exp": "'Développer' → 'le développement' (suffixe -ment, masculin). Les autres formes sont incorrectes : *développation, *développage, *développence n'existent pas en français.",
    },
    "ex2": {
        "q": "Nominalisez : 'Le gouvernement a décidé d'agir.' → La ___ du gouvernement d'agir.",
        "ans": "décision",
        "exp": "Décider → la décision (suffixe -sion, féminin). La décision du gouvernement d'agir.",
        "accept": ["décision", "la décision"],
    },
    "ex3": {
        "q": "Quel suffixe forme des noms féminins ?",
        "opts": ["-tion", "-ment", "-age", "-isme"],
        "ans": "-tion",
        "exp": "Les noms en -tion/-sion sont féminins : la décision, la construction, la satisfaction. Les noms en -ment sont masculins. Les noms en -age sont souvent masculins. Le suffixe -isme donne des noms masculins.",
    },
    "game_desc": "Nominalisation — verbes et adjectifs en noms",
    "items": [
        ("nom-tion", "Suffixe -tion/-sion", "Transforme un verbe en nom féminin", "verbe → nom féminin en -tion", "décider → la décision", "-tion = nom féminin de verbe", "verbe → nom féminin en -tion"),
        ("nom-ment", "Suffixe -ment", "Transforme un verbe en nom masculin", "verbe → nom masculin en -ment", "développer → le développement", "-ment = nom masculin de verbe", "verbe → nom masculin en -ment"),
        ("nom-age", "Suffixe -age", "Transforme un verbe en nom souvent masculin", "verbe → nom en -age", "recycler → le recyclage", "-age = nom de verbe (masc.)", "verbe → nom souvent masculin"),
        ("nom-ite", "Suffixe -ité", "Transforme un adjectif en nom féminin", "adjectif → nom féminin en -ité", "égal → l'égalité", "-ité = nom féminin d'adjectif", "adjectif → nom féminin en -ité"),
        ("nom-esse", "Suffixe -esse", "Transforme un adjectif en nom féminin", "adjectif → nom en -esse", "triste → la tristesse", "-esse = nom féminin d'adjectif", "adjectif → nom féminin"),
        ("nom-formel", "Style formel", "La nominalisation est préférée dans les textes officiels", "nominalisation = style soutenu", "La décision d'agir a été prise.", "nominalisation = formel et concis", "nominalisation = style soutenu"),
        ("nom-genre", "Genre du nom nominalisé", "-tion/-sion → féminin; -ment → masculin", "vérifier le genre", "la construction (f.) / le développement (m.)", "genre selon le suffixe", "vérifier le genre"),
        ("nom-piege", "Perte du sujet", "La nominalisation peut masquer qui fait l'action", "nominalisation peut supprimer le sujet", "'La décision a été prise' : qui ?", "nominalisation cache l'agent", "nominalisation peut masquer qui fait l'action"),
    ],
},

"les-nuances-du-conditionnel": {
    "level": "b2",
    "section": "grammaire",
    "num": "G06",
    "short": "Les Nuances du Conditionnel",
    "title": "Les Nuances du Conditionnel",
    "subtitle": "Politesse, hypothèse, information non vérifiée et futur dans le passé",
    "slides": [
        ("Conditionnel présent : rappel et nuances",
         "Formation : infinitif (radical futur) + terminaisons de l'imparfait (-ais, -ais, -ait, -ions, -iez, -aient).<br>"
         "Emplois : <em>condition (si + imparfait → cond.)</em>, <em>politesse</em>, <em>désir</em>, <em>suggestion</em>, <em>info non vérifiée</em>."),
        ("Politesse et demandes atténuées",
         "<em>Pourriez-vous m'aider ?</em> (plus poli que 'pouvez-vous')<br>"
         "<em>Je voudrais un café.</em> (commande polie)<br>"
         "<em>Auriez-vous une minute ?</em><br>"
         "<em>Cela vous dérangerait-il de…</em>"),
        ("Futur dans le passé",
         "Après un verbe au passé, le futur devient conditionnel :<br>"
         "<em>Il a dit qu'il <strong>viendrait</strong>.</em> (il a dit : 'je viendrai')<br>"
         "<em>Elle pensait qu'il <strong>réussirait</strong>.</em><br>"
         "Structure du discours indirect au passé : futur → conditionnel."),
        ("Information non vérifiée : conditionnel journalistique",
         "Dans les médias, le conditionnel marque une information non confirmée :<br>"
         "<em>Le premier ministre <strong>aurait démissionné</strong>.</em> (non confirmé)<br>"
         "<em>Des victimes <strong>seraient</strong> encore dans les décombres.</em><br>"
         "Ce conditionnel exprime la prudence journalistique."),
        ("Conditionnel présent vs passé",
         "Conditionnel présent : action hypothétique actuelle ou future.<br>"
         "Conditionnel passé : action hypothétique passée / regret / reproche.<br>"
         "<em>Si j'avais le temps, je <strong>viendrais</strong>.</em> (présent : impossibilité actuelle)<br>"
         "<em>Si j'avais eu le temps, je <strong>serais venu</strong>.</em> (passé : regret)"),
        ("Expressions conditionnelles variées",
         "Si + imparfait → cond. présent · Si + PQP → cond. passé<br>"
         "<em>À ta place, je…</em> (conseil au cond.)<br>"
         "<em>Au cas où + conditionnel</em> : <em>Au cas où il viendrait, prévenez-moi.</em><br>"
         "<em>Sauf si, à condition que + subjonctif.</em>"),
    ],
    "traps": [
        ("Si + conditionnel : jamais !", "Après 'si' conditionnel, on n'utilise jamais le conditionnel (ni le futur). Si j'avais le temps → cond. présent. Si j'avais eu le temps → cond. passé. *Si j'aurais = fautif."),
        ("Au cas où + conditionnel", "'Au cas où' déclenche le conditionnel (pas l'indicatif ni le subjonctif). Au cas où il viendrait (cond.) — pas *vient ni *vienne."),
        ("Futur dans le passé : cond. présent ou passé ?", "Futur simple dans le discours direct → conditionnel présent dans le discours indirect au passé. Futur antérieur → conditionnel passé."),
        ("Conditionnel journalistique : attribution claire", "Quand on rapporte une information non confirmée, le conditionnel seul ne suffit pas : préciser la source ou le contexte. 'Il démissionnerait.' sans source peut être trompeur."),
    ],
    "summary": [
        "<strong>Politesse :</strong> pourriez-vous, je voudrais, auriez-vous…",
        "<strong>Futur dans le passé :</strong> futur → conditionnel après verbe au passé.",
        "<strong>Info non vérifiée :</strong> il aurait dit, elle serait, ils auraient…",
        "<strong>Si + imparfait</strong> → cond. présent; <strong>Si + PQP</strong> → cond. passé.",
        "<strong>Au cas où</strong> + conditionnel (pas subjonctif, pas indicatif).",
    ],
    "ex1": {
        "q": "Il a promis qu'il ___ (revenir) le lendemain.",
        "opts": ["reviendrait", "reviendra", "soit revenu", "revient"],
        "ans": "reviendrait",
        "exp": "Discours indirect au passé (a promis = passé) : futur → conditionnel présent. 'Reviendra' serait le futur direct. 'Soit revenu' est subjonctif passé. 'Revient' est présent.",
    },
    "ex2": {
        "q": "Formulez une demande polie : 'Vous pouvez me passer le sel ?' → ___",
        "ans": "pourriez-vous me passer le sel",
        "exp": "Conditionnel de politesse : pouvoir → pourriez. 'Pourriez-vous me passer le sel ?' est la formulation polie standard.",
        "accept": ["pourriez-vous me passer le sel", "pourriez-vous me passer le sel ?", "pourriez vous me passer le sel"],
    },
    "ex3": {
        "q": "Quelle phrase utilise le conditionnel journalistique ?",
        "opts": [
            "Selon les témoins, l'auteur serait encore en fuite.",
            "Si tu venais, je serais content.",
            "Je voudrais un café, s'il vous plaît.",
            "Au cas où il viendrait, prévenez-moi.",
        ],
        "ans": "Selon les témoins, l'auteur serait encore en fuite.",
        "exp": "'Serait encore en fuite' avec 'selon les témoins' = conditionnel journalistique pour marquer une information non vérifiée. Les autres emplois sont : condition (si tu venais), politesse (je voudrais), précaution (au cas où).",
    },
    "game_desc": "Nuances du conditionnel — politesse, presse, futur passé",
    "items": [
        ("cond-politesse", "Conditionnel de politesse", "Atténuer une demande ou une suggestion", "demande polie = conditionnel", "Pourriez-vous m'aider ?", "conditionnel = demande polie", "demande polie = conditionnel"),
        ("cond-futur-passe", "Futur dans le passé", "Futur dans le discours direct → conditionnel dans le discours indirect au passé", "futur → conditionnel après verbe passé", "Il a dit qu'il viendrait.", "futur passé = conditionnel", "futur → conditionnel après verbe passé"),
        ("cond-journalistique", "Conditionnel journalistique", "Marquer une information non confirmée dans les médias", "info non vérifiée = conditionnel", "Le ministre aurait démissionné.", "conditionnel = info non confirmée", "info non vérifiée = conditionnel"),
        ("cond-si-imparfait", "Si + imparfait → cond. présent", "Condition hypothétique actuelle ou future", "si + imparfait = hypothèse actuelle", "Si j'avais le temps, je viendrais.", "si + imparfait = cond. présent", "condition hypothétique actuelle ou future"),
        ("cond-si-pqp", "Si + PQP → cond. passé", "Condition hypothétique passée — regret", "si + PQP = hypothèse passée", "Si j'avais su, j'aurais agi.", "si + PQP = cond. passé", "condition hypothétique passée — regret"),
        ("cond-au-cas-ou", "Au cas où + conditionnel", "Précaution : dans l'éventualité où quelque chose arriverait", "au cas où + conditionnel", "Au cas où il viendrait, appelle-moi.", "au cas où = conditionnel obligatoire", "au cas où + conditionnel"),
        ("cond-a-ta-place", "À ta place, je…", "Conseil formulé au conditionnel", "conseil poli = conditionnel", "À ta place, je parlerais à ton chef.", "à ta place + conditionnel = conseil", "conseil formulé au conditionnel"),
        ("cond-jamais-si", "Si ≠ conditionnel", "Après si conditionnel, jamais de conditionnel ni de futur", "si + imparfait/PQP, pas de conditionnel", "*Si j'aurais → Si j'avais (+ cond. hors si)", "si + conditionnel = toujours fautif", "après si conditionnel, jamais de conditionnel"),
    ],
},

"les-tournures-impersonnelles-avancees": {
    "level": "b2",
    "section": "grammaire",
    "num": "G07",
    "short": "Tournures Impersonnelles Avancées",
    "title": "Tournures Impersonnelles Avancées",
    "subtitle": "Il convient de, il est à noter, force est de constater",
    "slides": [
        ("Pourquoi les tournures impersonnelles ?",
         "Dans les textes formels, académiques et professionnels, les tournures impersonnelles :<br>"
         "- <strong>évitent le 'je'</strong> (style plus objectif)<br>"
         "- <strong>atténuent l'assertion</strong> (moins direct)<br>"
         "- <strong>marquent la certitude ou le doute</strong> de façon nuancée"),
        ("Tournures de nécessité formelles",
         "<em>Il convient de</em> + inf. : <em>Il convient de préciser que…</em><br>"
         "<em>Il importe de</em> + inf. : <em>Il importe de noter que…</em><br>"
         "<em>Il s'avère nécessaire de</em> + inf.<br>"
         "<em>Il est indispensable de / Il est impératif de</em> + inf."),
        ("Tournures de constatation",
         "<em>Il est à noter que</em> + indicatif : <em>Il est à noter que les résultats sont positifs.</em><br>"
         "<em>Force est de constater que</em> + indicatif : <em>Force est de constater que la situation s'améliore.</em><br>"
         "<em>Il ressort de cette analyse que</em> + indicatif.<br>"
         "<em>Il apparaît clairement que</em> + indicatif."),
        ("Tournures de probabilité et d'opinion nuancée",
         "<em>Il est probable que</em> + indicatif (forte probabilité)<br>"
         "<em>Il est possible que</em> + subjonctif (simple possibilité)<br>"
         "<em>Il semble que</em> + subjonctif (impression)<br>"
         "<em>Il paraît que</em> + indicatif (info entendue)<br>"
         "<em>On pourrait arguer que</em> + indicatif"),
        ("Tournures de conclusion",
         "<em>En définitive, il ressort que</em>…<br>"
         "<em>Il en découle que</em>…<br>"
         "<em>On peut en conclure que</em>…<br>"
         "<em>Tout bien considéré, il convient de reconnaître que</em>…"),
        ("Registre et usage",
         "Ces tournures sont propres au <strong>registre soutenu</strong>.<br>"
         "À l'oral quotidien, on dira : 'On voit que…' plutôt que 'Force est de constater que…'.<br>"
         "Dans les essais, rapports, articles de presse, lettres officielles : indispensables.<br>"
         "À éviter dans les textes créatifs ou les courriels informels."),
    ],
    "traps": [
        ("Il semble que + indicatif", "'Il semble que' exige le subjonctif, pas l'indicatif. *Il semble qu'il est là → Il semble qu'il soit là."),
        ("Il est probable vs Il est possible", "'Il est probable que' + indicatif (haute probabilité). 'Il est possible que' + subjonctif (basse probabilité / incertitude). Même structure, modes différents."),
        ("Force est de constater = impersonnel fixe", "'Force est de constater que' est une expression figée — on ne la modifie pas : *Force était de constater (fréquent mais non standard à l'écrit). À l'écrit formel : rester au présent."),
        ("Il convient de ≠ il convient que", "Il convient de + infinitif (sans sujet précis). Il convient que + subjonctif (si un sujet est précisé : Il convient que vous répondiez)."),
    ],
    "summary": [
        "<strong>Nécessité :</strong> il convient de, il importe de, il est indispensable de + inf.",
        "<strong>Constatation :</strong> il est à noter que, force est de constater que + indicatif.",
        "<strong>Probabilité :</strong> il est probable que + ind.; il est possible que + subj.",
        "<strong>Conclusion :</strong> il en découle que, on peut en conclure que.",
        "Registre <strong>soutenu</strong> — réservé aux textes formels.",
    ],
    "ex1": {
        "q": "Quelle tournure exprime la nécessité de façon formelle ?",
        "opts": [
            "Il convient de préciser ce point.",
            "On doit préciser ce point.",
            "Faut préciser ce point.",
            "C'est nécessaire de préciser.",
        ],
        "ans": "Il convient de préciser ce point.",
        "exp": "'Il convient de + infinitif' est la formule formelle de nécessité. 'On doit' est neutre. 'Faut' est familier. 'C'est nécessaire de' est courant mais pas soutenu.",
    },
    "ex2": {
        "q": "Complétez : 'Force est de ___ que la situation s'est améliorée.'",
        "ans": "constater",
        "exp": "'Force est de constater que' est une expression figée suivie de l'indicatif pour exprimer une constatation incontournable.",
        "accept": ["constater", "Force est de constater"],
    },
    "ex3": {
        "q": "Quelle phrase est correcte ?",
        "opts": [
            "Il est possible qu'il soit absent.",
            "Il est probable qu'il soit absent.",
            "Il semble qu'il est absent.",
            "Il paraît qu'il soit absent.",
        ],
        "ans": "Il est possible qu'il soit absent.",
        "exp": "'Il est possible que' + subjonctif (soit). 'Il est probable que' + indicatif (est, pas soit). 'Il semble que' + subjonctif (soit, pas est). 'Il paraît que' + indicatif (est, pas soit).",
    },
    "game_desc": "Tournures impersonnelles — style formel et soutenu",
    "items": [
        ("imp-convient", "Il convient de", "Exprimer une nécessité formelle avec infinitif", "nécessité formelle = il convient de + inf.", "Il convient de souligner ce point.", "il convient de + inf. = nécessité formelle", "nécessité formelle = il convient de + inf."),
        ("imp-noter", "Il est à noter que", "Attirer l'attention sur un fait important", "souligner un fait = il est à noter", "Il est à noter que les résultats sont positifs.", "il est à noter = signaler un fait", "attirer l'attention sur un fait important"),
        ("imp-force", "Force est de constater que", "Reconnaître une évidence incontournable", "évidence incontournable = force est de constater", "Force est de constater que la situation est grave.", "force est de constater = évidence imposée", "reconnaître une évidence incontournable"),
        ("imp-probable", "Il est probable que + ind.", "Exprimer une forte probabilité à l'impersonnel", "forte probabilité = probable + indicatif", "Il est probable qu'il viendra.", "probable + indicatif", "forte probabilité = probable + indicatif"),
        ("imp-possible", "Il est possible que + subj.", "Exprimer une simple possibilité à l'impersonnel", "simple possibilité = possible + subjonctif", "Il est possible qu'il vienne.", "possible + subjonctif", "simple possibilité = possible + subjonctif"),
        ("imp-semble", "Il semble que + subj.", "Exprimer une impression incertaine", "impression incertaine = il semble que + subj.", "Il semble qu'il soit absent.", "il semble que + subjonctif", "impression incertaine"),
        ("imp-decoule", "Il en découle que", "Exprimer la conséquence logique d'une analyse", "conséquence logique = il en découle que", "Il en découle que des réformes sont nécessaires.", "il en découle que = conséquence formelle", "conséquence logique d'une analyse"),
        ("imp-registre", "Registre soutenu", "Ces tournures appartiennent au style formel écrit", "style formel = tournures impersonnelles", "Force est de constater → essai/rapport.", "impersonnel = registre soutenu", "style formel = tournures impersonnelles"),
    ],
},

"la-concordance-des-temps-avancee": {
    "level": "b2",
    "section": "grammaire",
    "num": "G08",
    "short": "Concordance des Temps Avancée",
    "title": "Concordance des Temps Avancée",
    "subtitle": "Subordonnées temporelles, hypothétiques et concessives",
    "slides": [
        ("Rappel : concordance de base",
         "Verbe principal au présent → subordonnée au même temps qu'en français direct.<br>"
         "Verbe principal au passé → décalage des temps :<br>"
         "présent → imparfait · PC → PQP · futur → conditionnel présent · futur ant. → cond. passé"),
        ("Subordonnées temporelles au futur",
         "Après <em>quand, lorsque, dès que, aussitôt que, une fois que</em> + action future :<br>"
         "→ <strong>Futur simple</strong> ou <strong>futur antérieur</strong> (pas présent !).<br>"
         "<em>Quand il <strong>arrivera</strong>, appelle-moi.</em><br>"
         "<em>Dès qu'il <strong>aura fini</strong>, il te rejoindra.</em>"),
        ("Subordonnées hypothétiques : si + temps",
         "Si + présent → principale au présent/futur/impératif.<br>"
         "Si + imparfait → principale au conditionnel présent (hypothèse actuelle).<br>"
         "Si + PQP → principale au conditionnel passé (hypothèse passée / regret).<br>"
         "<em>Si tu venais, nous pourrions parler.</em>"),
        ("Subordonnées temporelles au passé",
         "Avant que + subjonctif : <em>Avant qu'il parte, j'ai parlé.</em><br>"
         "Après que + indicatif : <em>Après qu'il est parti, j'ai réfléchi.</em> (passé composé)<br>"
         "Jusqu'à ce que + subjonctif : <em>J'attendrai jusqu'à ce qu'il vienne.</em><br>"
         "Pendant que + indicatif : temps simultané."),
        ("Subordonnées concessives",
         "Bien que / Quoique + subjonctif.<br>"
         "Même si + indicatif (à tous les temps).<br>"
         "Quel(le)(s) que + subjonctif : <em>Quelle que soit votre opinion, écoutez.</em><br>"
         "Si + adjectif + que + subjonctif : <em>Si difficile que ce soit, continuez.</em>"),
        ("Tableau récapitulatif",
         "quand + futur → futur simple · quand + passé → imparfait/PQP<br>"
         "bien que → subjonctif toujours · même si → indicatif toujours<br>"
         "avant que → subjonctif · après que → indicatif<br>"
         "jusqu'à ce que → subjonctif · pendant que → indicatif"),
    ],
    "traps": [
        ("Après que + subjonctif", "Erreur fréquente. 'Après que' prend l'indicatif (pas le subjonctif) en français standard. *Après qu'il soit parti → Après qu'il est parti."),
        ("Quand + présent pour le futur", "En français, les conjonctions temporelles futures (quand, dès que…) exigent le futur. *Quand il vient demain → Quand il viendra demain."),
        ("Même si ≠ bien que pour le mode", "'Même si' + indicatif. 'Bien que' + subjonctif. Ne pas les échanger. *Même si tu sois là → Même si tu es là. *Bien que tu es là → Bien qu'il soit là."),
        ("Quel que soit : accord", "'Quel que soit/soient' s'accorde avec le nom suivant. Quelle que soit la raison (féminin). Quels que soient les résultats (masculin pluriel)."),
    ],
    "summary": [
        "Après <strong>quand/dès que</strong> + futur → futur simple ou futur antérieur.",
        "Si + imparfait → <strong>conditionnel présent</strong>; Si + PQP → <strong>conditionnel passé</strong>.",
        "<strong>Avant que</strong> + subjonctif; <strong>après que</strong> + indicatif.",
        "<strong>Bien que</strong> + subjonctif; <strong>même si</strong> + indicatif.",
        "<strong>Jusqu'à ce que</strong> + subjonctif; <strong>pendant que</strong> + indicatif.",
    ],
    "ex1": {
        "q": "Dès qu'il ___ (terminer) son rapport, il partira en vacances.",
        "opts": ["aura terminé", "terminera", "avait terminé", "aurait terminé"],
        "ans": "aura terminé",
        "exp": "Dès que + action accomplie avant le départ → futur antérieur (aura terminé). 'Terminera' marquerait deux actions simultanées. 'Avait terminé' est PQP (passé). 'Aurait terminé' est conditionnel passé.",
    },
    "ex2": {
        "q": "Choisissez le bon mode : 'J'attendrai jusqu'à ce qu'il ___ (venir).'",
        "ans": "vienne",
        "exp": "'Jusqu'à ce que' déclenche toujours le subjonctif. Venir → il vienne (subjonctif présent).",
        "accept": ["vienne", "il vienne"],
    },
    "ex3": {
        "q": "Quelle phrase est correcte ?",
        "opts": [
            "Après qu'il est parti, j'ai réfléchi.",
            "Après qu'il soit parti, j'ai réfléchi.",
            "Bien que même si tu es là, ça change.",
            "Avant qu'il est arrivé, j'avais préparé.",
        ],
        "ans": "Après qu'il est parti, j'ai réfléchi.",
        "exp": "'Après que' + indicatif → est parti (correct). 'Après qu'il soit' est fautif (subjonctif après après que). 'Bien que même si' est une combinaison incorrecte. 'Avant que' + subjonctif → avant qu'il soit arrivé (pas 'est arrivé').",
    },
    "game_desc": "Concordance des temps — subordonnées et modes",
    "items": [
        ("conc-quand-futur", "Quand + futur", "Après quand/dès que + action future → futur simple ou antérieur", "quand + futur = futur (pas présent)", "Quand il arrivera, appelle-moi.", "quand + futur = futur obligatoire", "quand + futur = futur (pas présent)"),
        ("conc-si-imp", "Si + imparfait", "Hypothèse actuelle : si + imparfait → conditionnel présent", "si + imparfait → cond. présent", "Si tu venais, je serais content.", "si + imparfait = cond. présent", "hypothèse actuelle"),
        ("conc-si-pqp", "Si + PQP", "Hypothèse passée : si + PQP → conditionnel passé", "si + PQP → cond. passé", "Si tu étais venu, j'aurais été content.", "si + PQP = cond. passé", "hypothèse passée"),
        ("conc-avant-que", "Avant que + subjonctif", "La subordonnée avec 'avant que' prend toujours le subjonctif", "avant que + subjonctif", "Avant qu'il parte, parle-lui.", "avant que = subjonctif obligatoire", "avant que + subjonctif"),
        ("conc-apres-que", "Après que + indicatif", "La subordonnée avec 'après que' prend l'indicatif (pas le subjonctif)", "après que + indicatif (pas subj.)", "Après qu'il est parti, j'ai réfléchi.", "après que = indicatif (erreur fréquente)", "après que + indicatif (pas le subjonctif)"),
        ("conc-bien-que", "Bien que + subjonctif", "La concession avec 'bien que' exige toujours le subjonctif", "bien que = subjonctif obligatoire", "Bien qu'il soit fatigué, il travaille.", "bien que = subjonctif", "bien que + subjonctif"),
        ("conc-meme-si", "Même si + indicatif", "La concession avec 'même si' prend l'indicatif", "même si = indicatif (pas subjonctif)", "Même s'il est fatigué, il travaille.", "même si = indicatif", "même si + indicatif"),
        ("conc-jusqua", "Jusqu'à ce que + subjonctif", "Durée jusqu'à un événement futur → subjonctif obligatoire", "jusqu'à ce que = subjonctif", "J'attendrai jusqu'à ce qu'il arrive.", "jusqu'à ce que = subjonctif", "durée jusqu'à un événement futur → subjonctif"),
    ],
},

}
