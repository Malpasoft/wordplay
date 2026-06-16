"""
francais/b2 — Grammaire B2 — batch 1 (G01–G04)
"""

CHAPTERS = {

"le-subjonctif-passe": {
    "level": "b2",
    "section": "grammaire",
    "num": "G01",
    "short": "Le Subjonctif Passé",
    "title": "Le Subjonctif Passé",
    "subtitle": "Action antérieure dans une proposition subjonctive",
    "slides": [
        ("Formation",
         "Auxiliaire (être/avoir) au subjonctif présent + participe passé.<br>"
         "j'aie mangé · tu aies fini · il ait compris · nous ayons vu<br>"
         "je sois parti(e) · tu sois arrivé(e) · il soit allé · nous soyons venus"),
        ("Emploi : antériorité dans le subjonctif",
         "Le subjonctif passé exprime une action <em>déjà accomplie</em> au moment de la principale.<br>"
         "Je suis content qu'il <em>soit venu</em>. (= il est venu AVANT que je sois content)<br>"
         "Elle regrette que tu <em>aies raté</em> cette occasion."),
        ("Comparer : subjonctif présent vs passé",
         "Présent → action simultanée ou future par rapport à la principale :<br>"
         "<em>Je doute qu'il <strong>vienne</strong>.</em> (maintenant ou plus tard)<br>"
         "Passé → action antérieure :<br>"
         "<em>Je doute qu'il <strong>soit venu</strong>.</em> (dans le passé)"),
        ("Déclencheurs : même liste que le subjonctif présent",
         "Émotion : <em>Je suis content(e) qu'il ait réussi.</em><br>"
         "Doute : <em>Il est douteux qu'elle ait dit ça.</em><br>"
         "Bien que + subjonctif passé : <em>Bien qu'il ait plu, nous sommes sortis.</em>"),
        ("Accord du participe passé au subjonctif passé",
         "Mêmes règles qu'au passé composé :<br>"
         "Avec être → accord sujet : <em>Je suis désolé qu'elle soit partie.</em><br>"
         "Avec avoir + COD antéposé → accord COD : <em>Les lettres qu'il ait écrites.</em>"),
        ("Subjonctif passé vs Conditionnel passé",
         "Ne pas confondre :<br>"
         "Subj. passé : <em>qu'il <strong>ait</strong> mangé</em> (auxiliaire au subjonctif)<br>"
         "Cond. passé : <em>il <strong>aurait</strong> mangé</em> (auxiliaire au conditionnel)<br>"
         "Ces deux formes sont parfois phonétiquement proches — attention à l'écrit."),
    ],
    "traps": [
        ("Ait vs Aurait", "'Qu'il ait mangé' = subjonctif passé (dans une proposition subordonnée). 'Il aurait mangé' = conditionnel passé (hypothèse). Contexte syntaxique différent."),
        ("Accord au subjonctif passé", "Les mêmes accords qu'au PC s'appliquent. Avec être → accord sujet. *Qu'elle soit parti → qu'elle soit partie."),
        ("Subjonctif passé avec bien que", "'Bien que + subjonctif passé' pour un fait passé : Bien qu'il ait plu, nous sommes sortis. 'Bien que + subjonctif présent' pour un fait actuel."),
        ("Ne pas utiliser le subjonctif passé si la principale est au présent et l'action est future", "Si la subordonnée exprime une action encore à venir, utiliser le subjonctif présent : Je doute qu'il vienne demain (pas : soit venu demain)."),
    ],
    "summary": [
        "Formation : auxiliaire au <strong>subjonctif présent</strong> + participe passé.",
        "Exprime une action <strong>antérieure</strong> dans une proposition subjonctive.",
        "Mêmes <strong>déclencheurs</strong> que le subjonctif présent.",
        "Accord <strong>identique au PC</strong> (être → sujet; avoir + COD antéposé → COD).",
        "Bien que + subjonctif passé = fait passé concédé.",
    ],
    "ex1": {
        "q": "Je suis surpris qu'il ___ (partir) sans dire au revoir.",
        "opts": ["soit parti", "est parti", "aurait parti", "serait parti"],
        "ans": "soit parti",
        "exp": "Émotion (être surpris) + deux sujets différents → subjonctif. Action passée (il est parti avant) → subjonctif passé. 'Partir' prend être → soit parti. 'Est parti' est indicatif; 'aurait parti' et 'serait parti' sont incorrects.",
    },
    "ex2": {
        "q": "Mettez au subjonctif passé : 'Elle (finir) son travail.'",
        "ans": "qu'elle ait fini son travail",
        "exp": "Finir → participe passé 'fini'; auxiliaire avoir au subjonctif présent → ait. Subjonctif passé : qu'elle ait fini.",
        "accept": ["qu'elle ait fini son travail", "elle ait fini son travail", "ait fini"],
    },
    "ex3": {
        "q": "Quelle phrase utilise correctement le subjonctif passé ?",
        "opts": [
            "Bien qu'il ait plu, la fête a continué.",
            "Bien qu'il soit pleuvoir hier, on est sortis.",
            "Bien qu'il a plu, la fête a continué.",
            "Bien qu'il pleuvait, la fête a continué.",
        ],
        "ans": "Bien qu'il ait plu, la fête a continué.",
        "exp": "'Bien que' déclenche le subjonctif. Pour un fait passé, subjonctif passé : ait plu. 'Soit pleuvoir' est impossible. 'A plu' est indicatif. 'Pleuvait' est imparfait — jamais après bien que.",
    },
    "game_desc": "Subjonctif passé — formation et antériorité",
    "items": [
        ("sp-form", "Formation subjonctif passé", "Auxiliaire au subjonctif présent + participe passé", "subj. présent de l'auxiliaire + participe passé", "Je suis content qu'il ait réussi.", "subj. présent + participe passé", "subj. présent de l'auxiliaire + participe passé"),
        ("sp-aie", "Avoir au subj. présent", "que j'aie, tu aies, il ait, nous ayons, vous ayez, ils aient", "aie / ait / ayons au subjonctif", "qu'il ait compris", "aie/ait/ayons = avoir au subjonctif", "aie / ait / ayons au subjonctif"),
        ("sp-sois", "Être au subj. présent", "que je sois, tu sois, il soit, nous soyons, vous soyez, ils soient", "sois / soit / soyons au subjonctif", "qu'elle soit partie", "sois/soit/soyons = être au subjonctif", "sois / soit / soyons au subjonctif"),
        ("sp-anteriorite", "Antériorité au subjonctif", "Le subjonctif passé exprime une action accomplie avant la principale", "action avant la principale = subj. passé", "Je regrette qu'il soit parti.", "subj. passé = avant la principale", "action avant la principale = subj. passé"),
        ("sp-vs-present", "Subj. présent vs passé", "Présent = simultané/futur; passé = antérieur à la principale", "présent: simultan; passé: antérieur", "qu'il vienne (futur) / qu'il soit venu (passé)", "choisir selon l'antériorité", "présent: simultan; passé: antérieur"),
        ("sp-bien-que", "Bien que + subj. passé", "Concession portant sur un fait passé accompli", "bien que + fait passé = subj. passé", "Bien qu'il ait plu, nous sommes sortis.", "bien que + passé = subj. passé", "bien que + fait passé = subj. passé"),
        ("sp-accord", "Accord au subj. passé", "Même règle d'accord qu'au passé composé", "accord identique au PC", "Je suis content qu'elle soit venue.", "accord subj. passé = accord PC", "accord identique au PC"),
        ("sp-vs-cond", "Subj. passé vs cond. passé", "Ait mangé (subj.) ≠ aurait mangé (cond.): contexte différent", "ait (subj.) vs aurait (cond.)", "qu'il ait fini (subj.) / il aurait fini (cond.)", "ait = subjonctif; aurait = conditionnel", "ait (subj.) vs aurait (cond.)"),
    ],
},

"le-gerondif-et-le-participe-present": {
    "level": "b2",
    "section": "grammaire",
    "num": "G02",
    "short": "Le Gérondif et le Participe Présent",
    "title": "Le Gérondif et le Participe Présent",
    "subtitle": "En + -ant : simultanéité, manière et condition",
    "slides": [
        ("Formation du participe présent",
         "Radical de la 1re personne du pluriel (nous) + <strong>-ant</strong>.<br>"
         "nous parlons → parlant · nous finissons → finissant · nous prenons → prenant<br>"
         "Irréguliers : être → <em>étant</em> · avoir → <em>ayant</em> · savoir → <em>sachant</em>"),
        ("Le gérondif : en + participe présent",
         "Gérondif = <strong>en</strong> + participe présent.<br>"
         "<em>en parlant, en finissant, en prenant</em><br>"
         "Le sujet du gérondif est <strong>toujours le même</strong> que celui du verbe principal."),
        ("Emplois du gérondif",
         "<strong>1. Simultanéité :</strong> <em>Il chante <u>en travaillant</u>.</em> (deux actions en même temps)<br>"
         "<strong>2. Manière :</strong> <em>Elle a réussi <u>en travaillant dur</u>.</em> (comment ?)<br>"
         "<strong>3. Condition :</strong> <em><u>En partant tôt</u>, tu éviteras les embouteillages.</em> (si tu pars tôt)<br>"
         "<strong>4. Cause :</strong> <em><u>En arrivant en retard</u>, il a raté le début.</em>"),
        ("Participe présent vs Gérondif",
         "Participe présent (sans <em>en</em>) = <strong>adjectif verbal ou relative courte</strong> :<br>"
         "<em>un enfant <u>souriant</u></em> (adj.) · <em>les étudiants <u>travaillant</u> ici</em> (rel.)<br>"
         "Gérondif (avec <em>en</em>) = <strong>adverbe de manière/temps/condition</strong> :<br>"
         "<em>Il est sorti <u>en courant</u>.</em>"),
        ("Participe présent composé",
         "Ayant + participe passé = action antérieure au participe présent.<br>"
         "<em><u>Ayant terminé</u> son travail, il est sorti.</em> (= Après avoir terminé)<br>"
         "Étant + participe passé (être) : <em><u>Étant arrivée</u> tôt, elle a eu une bonne place.</em>"),
        ("Accord : pas d'accord pour le gérondif",
         "Le gérondif est invariable : il ne s'accorde jamais.<br>"
         "Le participe présent employé comme adjectif s'accorde en genre et nombre :<br>"
         "<em>une histoire <u>intéressante</u></em> (adjectif verbal accordé)<br>"
         "vs <em>une histoire <u>intéressant</u> les jeunes</em> (participe présent invariable)"),
    ],
    "traps": [
        ("Sujets différents interdit au gérondif", "Le sujet du gérondif doit être le même que celui du verbe principal. *'En travaillant, la tâche est finie' est incorrect : 'la tâche' ne travaille pas."),
        ("Accord du participe présent/adjectif verbal", "Participe présent invariable : une histoire intéressant les enfants. Adjectif verbal accordé : une histoire intéressante. La différence : avec complément = participe; sans = adjectif."),
        ("En + participe passé", "On ne dit pas *'en ayant fini' dans les emplois courants. Utiliser 'après avoir fini' ou le participe passé composé 'ayant fini'."),
        ("Irréguliers à mémoriser", "être → étant; avoir → ayant; savoir → sachant. Pas *étantant, *avantant, *saventant."),
    ],
    "summary": [
        "Participe présent : radical nous + <strong>-ant</strong> (invariable comme verbe).",
        "Gérondif : <strong>en</strong> + participe présent — même sujet que le verbe principal.",
        "Emplois du gérondif : <strong>simultanéité, manière, condition, cause</strong>.",
        "Participe présent employé comme adj. verbal → <strong>s'accorde</strong>.",
        "Participe présent composé : <strong>ayant/étant</strong> + participe passé.",
    ],
    "ex1": {
        "q": "Il a appris le français ___ (regarder) des films.",
        "opts": ["en regardant", "regardant", "qu'il regardait", "pour regarder"],
        "ans": "en regardant",
        "exp": "Le gérondif (en + participe présent) exprime la manière : comment a-t-il appris ? 'En regardant' = manière/moyen. 'Regardant' seul serait un participe présent (relatif). 'Pour regarder' exprime le but.",
    },
    "ex2": {
        "q": "Transformez : 'Après avoir fini son repas, elle a appelé.' → Participe présent composé.",
        "ans": "ayant fini son repas, elle a appelé",
        "exp": "Le participe passé composé (ayant + PP) remplace 'après avoir fini' pour exprimer l'antériorité. 'Ayant fini' = action accomplie avant l'action principale.",
        "accept": ["ayant fini son repas, elle a appelé", "Ayant fini son repas, elle a appelé", "ayant fini son repas"],
    },
    "ex3": {
        "q": "Quelle phrase est correcte ?",
        "opts": [
            "En travaillant dur, tu réussiras.",
            "En travaillant dur, le succès viendra.",
            "En ayant fini, je suis sorti.",
            "Étant content, il sourissait.",
        ],
        "ans": "En travaillant dur, tu réussiras.",
        "exp": "Sujet du gérondif et du verbe principal identique (tu) → correct. 'Le succès viendra' : 'le succès' ne travaille pas — sujets différents. 'En ayant fini' est incorrect. 'Sourissait' est une forme fautive : il souriait.",
    },
    "game_desc": "Gérondif et participe présent — formation et emplois",
    "items": [
        ("ger-form", "Formation participe présent", "Radical de nous + -ant", "nous + -ant", "nous parlons → parlant", "radical nous + -ant", "nous + -ant"),
        ("ger-gerondif", "Le gérondif", "En + participe présent — même sujet que le verbe principal", "en + participe présent", "Il travaille en écoutant de la musique.", "gérondif = en + participe présent", "en + participe présent"),
        ("ger-simultaneite", "Simultanéité", "Deux actions qui se produisent en même temps", "deux actions simultanées", "Elle chante en cuisinant.", "gérondif = simultaneité", "deux actions simultanées"),
        ("ger-maniere", "Manière", "Gérondif exprimant comment une action est accomplie", "comment = gérondif", "Il a réussi en travaillant dur.", "gérondif = manière (comment)", "comment = gérondif"),
        ("ger-condition", "Condition", "Gérondif exprimant une condition (= si...)", "si + action = gérondif", "En partant tôt, tu éviteras le trafic.", "gérondif = condition (si)", "si + action = gérondif"),
        ("ger-adj-verbal", "Adjectif verbal accordé", "Participe présent employé comme adjectif → s'accorde", "adjectif verbal = accordé", "une histoire intéressante (adj.) vs intéressant les enfants (participe)", "adj. verbal s'accorde; participe ne s'accorde pas", "adjectif verbal = accordé"),
        ("ger-compose", "Participe présent composé", "Ayant/Étant + participe passé = action antérieure", "ayant + PP = avant l'action principale", "Ayant fini, il est parti.", "ayant + PP = antériorité", "ayant + PP = avant l'action principale"),
        ("ger-irreguliers", "Irréguliers du participe présent", "être → étant; avoir → ayant; savoir → sachant", "trois irréguliers à mémoriser", "étant, ayant, sachant", "étant / ayant / sachant", "trois irréguliers à mémoriser"),
    ],
},

"la-mise-en-relief": {
    "level": "b2",
    "section": "grammaire",
    "num": "G03",
    "short": "La Mise en Relief",
    "title": "La Mise en Relief",
    "subtitle": "C'est… qui/que, présentatifs et structures emphatiques",
    "slides": [
        ("C'est… qui / C'est… que",
         "<em>C'est</em> + élément mis en valeur + <em>qui</em> (sujet) / <em>que</em> (objet) + reste de la phrase.<br>"
         "Sujet : <em>C'est Marie <strong>qui</strong> a téléphoné.</em> (et non pas quelqu'un d'autre)<br>"
         "Objet : <em>C'est ce livre <strong>que</strong> je veux.</em> (et non pas un autre)"),
        ("C'est… que avec d'autres éléments",
         "Lieu : <em>C'est à Paris <strong>que</strong> j'habite.</em><br>"
         "Temps : <em>C'est hier <strong>que</strong> j'ai compris.</em><br>"
         "Manière : <em>C'est ainsi <strong>que</strong> ça s'est passé.</em><br>"
         "→ Pour tout élément autre que le sujet, on utilise <em>que</em>."),
        ("Ce qui / Ce que emphatique",
         "<em>Ce qui m'intéresse, c'est la culture.</em> (sujet mis en relief)<br>"
         "<em>Ce que j'aime, c'est la musique.</em> (objet mis en relief)<br>"
         "<em>Ce dont j'ai besoin, c'est du repos.</em> (avec de)<br>"
         "Structure : Ce qui/que/dont + proposition + c'est + élément mis en valeur."),
        ("Voilà / C'est pour insister",
         "<em>Voilà</em> + nom : pour présenter ou souligner quelque chose.<br>"
         "<em>Voilà pourquoi je suis parti.</em> (= C'est la raison pour laquelle)<br>"
         "<em>C'est ainsi / C'est donc / C'est bien</em> : renforcer la cohérence du discours."),
        ("Inversion emphatique et répétition pronominale",
         "Dislocation gauche : <em>Ce film, je l'adore.</em> (le nom repris par pronom)<br>"
         "Dislocation droite : <em>Je l'adore, ce film.</em><br>"
         "Ces structures sont très courantes à l'oral et dans les textes expressifs."),
        ("Ne… que : restriction emphatique",
         "<em>Ne… que</em> = seulement. Encadre le verbe :<br>"
         "<em>Il ne fait <strong>que</strong> travailler.</em> (= Il fait seulement ça)<br>"
         "<em>Je n'ai <strong>que</strong> dix euros.</em> (= seulement dix)<br>"
         "≠ <em>Il ne travaille pas</em> (négation totale)"),
    ],
    "traps": [
        ("Qui vs que après c'est", "C'est + [sujet du verbe suivant] + qui. C'est + [objet ou circonstanciel] + que. *C'est Marie que a téléphoné → C'est Marie qui a téléphoné (Marie est sujet du verbe qui suit)."),
        ("Ce qui vs Ce que", "Ce qui = sujet du verbe de la subordonnée. Ce que = objet direct du verbe. Ce dont = avec un verbe + de. *Ce qui j'aime → Ce que j'aime (aimer qqch = objet direct)."),
        ("Ne… que ≠ négation", "Ne…que est restrictif (= seulement), pas négatif. Je n'ai que deux euros (j'en ai deux). Je n'ai pas deux euros (j'en ai zéro ou plus/moins)."),
        ("Dislocation : accord du pronom", "Dans la dislocation, le pronom doit s'accorder avec le nom disloqué. Ce film, je l'adore (masculin sg → l'). Ces films, je les adore (pluriel → les)."),
    ],
    "summary": [
        "<strong>C'est… qui</strong> (sujet) / <strong>C'est… que</strong> (objet/circonstanciel).",
        "<strong>Ce qui / Ce que / Ce dont</strong> + proposition + c'est + élément mis en relief.",
        "Dislocation : <em>Ce film, je l'adore</em> / <em>Je l'adore, ce film</em>.",
        "<strong>Ne… que</strong> = restriction (seulement) — pas une négation.",
        "Voilà pourquoi / C'est ainsi que — cohérence et emphase.",
    ],
    "ex1": {
        "q": "Reformulez : 'Paul a téléphoné.' → C'est ___ a téléphoné.",
        "opts": ["Paul qui", "Paul que", "Paul dont", "Paul lequel"],
        "ans": "Paul qui",
        "exp": "Paul est le sujet du verbe 'a téléphoné' → C'est Paul qui a téléphoné. 'Que' s'utilise pour l'objet ou les circonstanciels. 'Dont' remplace de + nom.",
    },
    "ex2": {
        "q": "Complétez : '___ j'aime dans cette ville, c'est son architecture.'",
        "ans": "Ce que",
        "exp": "'Aimer' = verbe avec objet direct. La mise en relief d'un objet direct → Ce que. Ce qui = pour le sujet. Ce dont = pour les verbes avec de.",
        "accept": ["Ce que", "ce que"],
    },
    "ex3": {
        "q": "Quelle phrase utilise correctement 'ne… que' ?",
        "opts": [
            "Je n'ai que cinq minutes.",
            "Je ne que lis des romans.",
            "Il ne travaille que pas.",
            "Elle ne mange que pas de viande.",
        ],
        "ans": "Je n'ai que cinq minutes.",
        "exp": "'Ne…que' encadre le verbe et porte sur l'élément qui suit 'que'. Je n'ai que cinq minutes = j'ai seulement cinq minutes. 'Je ne que lis' et 'ne travaille que pas' sont syntaxiquement incorrects.",
    },
    "game_desc": "Mise en relief — c'est… qui/que et structures emphatiques",
    "items": [
        ("mer-cest-qui", "C'est… qui", "Mettre en relief le sujet d'un verbe", "emphase sur le sujet", "C'est Marie qui a appelé.", "c'est + sujet + qui", "emphase sur le sujet"),
        ("mer-cest-que", "C'est… que", "Mettre en relief l'objet, le lieu, le temps ou la manière", "emphase sur objet ou circonstanciel", "C'est ce livre que je veux.", "c'est + objet/circonstanciel + que", "emphase sur objet ou circonstanciel"),
        ("mer-ce-qui", "Ce qui… c'est", "Mettre en relief un élément qui est sujet dans la subordonnée", "sujet mis en relief = ce qui", "Ce qui m'intéresse, c'est la grammaire.", "ce qui = sujet mis en relief", "sujet mis en relief = ce qui"),
        ("mer-ce-que", "Ce que… c'est", "Mettre en relief un objet direct dans la subordonnée", "objet direct mis en relief = ce que", "Ce que j'aime, c'est voyager.", "ce que = objet mis en relief", "objet direct mis en relief = ce que"),
        ("mer-dislocation", "Dislocation", "Déplacer un nom en début ou fin de phrase, repris par un pronom", "nom + pronom ou pronom + nom", "Ce film, je l'adore.", "dislocation = nom déplacé + pronom", "nom + pronom ou pronom + nom"),
        ("mer-ne-que", "Ne… que", "Restriction : exprimer 'seulement' avec ne et que autour du verbe", "ne + verbe + que = seulement", "Je n'ai que dix euros.", "ne…que = seulement (pas négatif)", "ne + verbe + que = seulement"),
        ("mer-voila", "Voilà pourquoi", "Formule de cohérence pour expliquer la raison d'une situation", "résumer la raison = voilà pourquoi", "Voilà pourquoi je suis parti.", "voilà pourquoi = c'est la raison", "résumer la raison = voilà pourquoi"),
        ("mer-ce-dont", "Ce dont… c'est", "Mettre en relief un élément introduit par 'de'", "verbe + de → ce dont", "Ce dont j'ai besoin, c'est du sommeil.", "ce dont = avec verbe + de", "verbe + de → ce dont"),
    ],
},

"les-propositions-infinitives": {
    "level": "b2",
    "section": "grammaire",
    "num": "G04",
    "short": "Les Propositions Infinitives",
    "title": "Les Propositions Infinitives",
    "subtitle": "Infinitif comme substitut de proposition subordonnée",
    "slides": [
        ("Infinitif après verbes de perception",
         "Voir, entendre, sentir, regarder, écouter + <strong>nom + infinitif</strong> (COD de la perception).<br>"
         "<em>J'entends les oiseaux <strong>chanter</strong>.</em><br>"
         "<em>Je vois les enfants <strong>jouer</strong>.</em><br>"
         "Le nom est à la fois COD du verbe principal et sujet logique de l'infinitif."),
        ("Infinitif après faire, laisser, envoyer",
         "<em>Faire</em> + infinitif = faire réaliser par quelqu'un d'autre (causatif) :<br>"
         "<em>Je fais <strong>réparer</strong> ma voiture.</em> (par un mécanicien)<br>"
         "<em>Elle fait <strong>travailler</strong> ses étudiants.</em><br>"
         "<em>Laisser</em> + inf. = permettre : <em>Il laisse les enfants <strong>jouer</strong>.</em>"),
        ("Place des pronoms avec faire + infinitif",
         "Le COD se place <strong>avant le verbe faire</strong>, pas avant l'infinitif :<br>"
         "<em>Je la fais réparer.</em> (= je fais réparer la voiture; 'la' = la voiture)<br>"
         "<em>Il les fait travailler.</em><br>"
         "Exception : <em>se faire + infinitif</em> = subir : <em>Je me suis fait voler mon sac.</em>"),
        ("Infinitif passé : après avoir / après être",
         "<em>Après avoir + PP</em> = action antérieure au verbe principal (même sujet) :<br>"
         "<em>Après avoir mangé, il est sorti.</em><br>"
         "<em>Après être parti, elle a appelé.</em><br>"
         "Ne jamais utiliser <em>après que + subjonctif</em> — l'indicatif s'impose après après que."),
        ("Pour + infinitif : but et cause négative",
         "But : <em>Il travaille dur <strong>pour réussir</strong>.</em><br>"
         "Cause négative (reproche) : <em>Il a été puni <strong>pour avoir triché</strong>.</em><br>"
         "Simultanéité avec le verbe principal : infinitif présent.<br>"
         "Antériorité : infinitif passé (pour avoir + PP)."),
        ("Sans, avant de, afin de + infinitif",
         "<em>Sans</em> + inf. : <em>Il est parti <strong>sans dire</strong> au revoir.</em><br>"
         "<em>Avant de</em> + inf. : <em>Réfléchissez <strong>avant de répondre</strong>.</em><br>"
         "<em>Afin de</em> + inf. : but formel. <em>Elle a étudié <strong>afin de réussir</strong>.</em><br>"
         "Ces prépositions précèdent toujours l'infinitif (pas une proposition finie)."),
    ],
    "traps": [
        ("Après que + subjonctif", "'Après que' prend l'indicatif en français standard, pas le subjonctif. *Après qu'il soit parti → Après qu'il est parti / After leaving → Après être parti (même sujet)."),
        ("Faire + infinitif : ordre du COD", "Le pronom va avant faire, pas avant l'infinitif. *Je fais la réparer → Je la fais réparer."),
        ("Après avoir vs Après que", "'Après avoir + PP' = même sujet que le verbe principal (infinitif passé). 'Après que' = sujets différents (indicatif). Après être parti (même sujet) / Après qu'il est parti (sujets différents)."),
        ("Pour avoir + PP = cause passée", "'Pour avoir triché' = parce qu'il a triché (cause passée). Ne pas confondre avec le but 'pour tricher' (but présent/futur)."),
    ],
    "summary": [
        "Verbes de <strong>perception</strong> + nom + infinitif (voir, entendre, sentir).",
        "<strong>Faire</strong> + infinitif = causatif (faire faire par qqn d'autre).",
        "Pronoms avant <strong>faire</strong>, pas avant l'infinitif.",
        "<strong>Après avoir/être</strong> + PP = antériorité (même sujet).",
        "<strong>Sans, avant de, afin de, pour</strong> + infinitif (présent ou passé).",
    ],
    "ex1": {
        "q": "Réécrivez avec le pronom : 'Je fais réparer ma voiture.' → Je ___ réparer.",
        "opts": ["la fais", "fais la", "fais la la", "me fais"],
        "ans": "la fais",
        "exp": "Le COD (la voiture → la) se place avant le verbe 'faire', pas avant l'infinitif : Je la fais réparer. 'Fais la' inverse l'ordre correct.",
    },
    "ex2": {
        "q": "Transformez : 'Il a dîné. Ensuite, il s'est couché.' → Après ___",
        "ans": "après avoir dîné, il s'est couché",
        "exp": "Même sujet → infinitif passé 'après avoir + PP'. Dîner → dîné. 'Après avoir dîné, il s'est couché.'",
        "accept": ["après avoir dîné, il s'est couché", "Après avoir dîné, il s'est couché", "avoir dîné"],
    },
    "ex3": {
        "q": "Quelle phrase est correcte ?",
        "opts": [
            "J'entends les oiseaux chanter.",
            "J'entends les oiseaux chantent.",
            "J'entends que les oiseaux chantent.",
            "J'entends les oiseaux de chanter.",
        ],
        "ans": "J'entends les oiseaux chanter.",
        "exp": "Verbe de perception (entendre) + COD (les oiseaux) + infinitif (chanter) = structure correcte. 'Chantent' = verbe conjugué (construction incorrecte sans que). 'Que les oiseaux chantent' est possible mais la construction directe est préférée. 'De chanter' n'existe pas après entendre.",
    },
    "game_desc": "Propositions infinitives — faire, laisser, percevoir",
    "items": [
        ("inf-perception", "Verbe de perception + inf.", "Voir, entendre, sentir + COD + infinitif", "perception + nom + infinitif", "Je vois les enfants jouer.", "voir/entendre + nom + infinitif", "perception + nom + infinitif"),
        ("inf-faire-caus", "Faire + infinitif (causatif)", "Faire réaliser une action par quelqu'un d'autre", "faire faire par qqn", "Je fais réparer ma voiture.", "faire + inf. = faire faire par qqn", "faire faire par qqn"),
        ("inf-laisser", "Laisser + infinitif", "Permettre à quelqu'un de faire quelque chose", "laisser = permettre à qqn de", "Il laisse les enfants jouer.", "laisser + inf. = permettre", "laisser = permettre à qqn de"),
        ("inf-pronom-faire", "Pronom + faire + inf.", "Le pronom COD se place avant faire, pas avant l'infinitif", "pronom avant faire", "Je la fais réparer.", "COD avant faire, pas avant inf.", "pronom avant faire"),
        ("inf-apres-avoir", "Après avoir + PP", "Infinitif passé pour une action antérieure (même sujet)", "après + inf. passé = antériorité", "Après avoir mangé, il est sorti.", "après avoir + PP = antériorité", "après + inf. passé = antériorité"),
        ("inf-pour-passe", "Pour avoir + PP", "Exprimer la cause passée (parce qu'il a fait qqch)", "pour + inf. passé = cause passée", "Il a été puni pour avoir triché.", "pour avoir + PP = cause passée", "pour + inf. passé = cause passée"),
        ("inf-avant-de", "Avant de + infinitif", "Action non encore faite au moment du verbe principal", "avant de + inf. = non encore fait", "Réfléchis avant de répondre.", "avant de + infinitif", "action non encore faite au moment du verbe principal"),
        ("inf-sans", "Sans + infinitif", "Absence d'une action concomitante", "sans + inf. = sans faire qqch", "Il est parti sans dire au revoir.", "sans + infinitif = without doing", "absence d'une action concomitante"),
    ],
},

}
