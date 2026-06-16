"""francais C1 grammaire — G05–G08"""

CHAPTERS = {
    "la-phrase-complexe": {
        "level": "c1",
        "section": "grammaire",
        "num": "G05",
        "short": "La Phrase Complexe",
        "title": "La Phrase Complexe",
        "subtitle": "Subordination, enchâssement et ellipse au niveau C1",
        "slides": [
            ("Types de propositions subordonnées",
             "<p>La phrase complexe repose sur l'enchâssement de <strong>propositions subordonnées</strong>&nbsp;:</p>"
             "<table><tr><th>Type</th><th>Introductr.</th><th>Exemple</th></tr>"
             "<tr><td>Relative</td><td>qui, que, dont, où…</td><td><em>L'homme dont je parle</em></td></tr>"
             "<tr><td>Complétive (COD)</td><td>que + ind./subj.</td><td><em>Je crois qu'il viendra</em></td></tr>"
             "<tr><td>Interrogative ind.</td><td>si, ce qui, ce que…</td><td><em>Je sais ce qu'il veut</em></td></tr>"
             "<tr><td>Circonstancielle</td><td>quand, bien que…</td><td><em>Bien qu'il soit tard</em></td></tr>"
             "<tr><td>Infinitive</td><td>verbe de perc.</td><td><em>Je le vois partir</em></td></tr></table>"),
            ("L'enchâssement et les propositions imbriquées",
             "<p>Les subordonnées peuvent s'<strong>imbriquer</strong> (une dans l'autre)&nbsp;:</p>"
             "<p><em>Je sais que celui qui aura fini son travail pourra partir plus tôt.</em></p>"
             "<p>Analyse&nbsp;:</p>"
             "<ul><li>Principale : <em>Je sais</em></li>"
             "<li>Subord. complétive : <em>que…pourra partir plus tôt</em></li>"
             "<li>Relative enchâssée : <em>qui aura fini son travail</em></li></ul>"
             "<p>Dans ces constructions, garder la <strong>concordance des temps</strong> est crucial.</p>"),
            ("L'ellipse dans la phrase complexe",
             "<p>L'<strong>ellipse</strong> supprime un élément récupérable du contexte pour alléger le style&nbsp;:</p>"
             "<ul><li>Ellipse du sujet et verbe&nbsp;: <em>Il parla longuement et clairement.</em> (= et il parla clairement)</li>"
             "<li>Ellipse de que&nbsp;: <em>Il dit avoir compris.</em> (= il dit qu'il avait compris)</li>"
             "<li>Ellipse du verbe dans les comparatives&nbsp;: <em>Elle court plus vite que lui.</em> (= que lui ne court)</li></ul>"
             "<p>L'ellipse est valorisée dans les écrits soignés pour éviter la lourdeur.</p>"),
            ("Propositions relatives de liaison",
             "<p>Les <strong>relatives de liaison</strong> (ou relative continuative) enchainent deux idées sans subordination logique explicite&nbsp;:</p>"
             "<ul><li><em>Il nous a parlé longuement, ce qui m'a surpris.</em></li>"
             "<li><em>Elle est partie, après quoi on a pu discuter.</em></li>"
             "<li><em>Il a réussi, dont nous nous réjouissons.</em></li></ul>"
             "<p>Ces relatives réfèrent à l'ensemble de la proposition précédente, pas à un nom antécédent précis.</p>"),
            ("La subordination concessive avancée",
             "<p>Structures concessives de niveau C1&nbsp;:</p>"
             "<table><tr><th>Locution</th><th>Mode</th><th>Nuance</th></tr>"
             "<tr><td><em>si… que</em></td><td>Indicatif</td><td>quelle que soit la mesure</td></tr>"
             "<tr><td><em>quelque… que</em></td><td>Subjonctif</td><td>quelle que soit la qualité</td></tr>"
             "<tr><td><em>quoi que</em></td><td>Subjonctif</td><td>quelle que soit la chose</td></tr>"
             "<tr><td><em>pour… que</em></td><td>Subjonctif</td><td>même si (très)</td></tr>"
             "<tr><td><em>avoir beau + inf.</em></td><td>—</td><td>bien que / même si</td></tr></table>"
             "<p><em>Si fatigué qu'il fût, il continua.</em> / <em>Quoi qu'il fasse, il échoue.</em></p>"),
        ],
        "traps": [
            ("Confusion quoi que / quoique", "<em>quoi que</em> (deux mots = quelle que soit la chose que) vs <em>quoique</em> (un mot = bien que). <em>Quoi qu'il fasse</em> ≠ <em>quoiqu'il fasse</em>."),
            ("Mode après si… que concessif", "<em>si… que</em> avec valeur concessive se construit avec l'indicatif ou le subjonctif selon le sens ; ne pas confondre avec <em>si… que</em> de conséquence."),
            ("Enchâssement sans concordance", "ne pas adapter les temps dans les subordonnées imbriquées — chaque niveau d'enchâssement doit respecter la concordance."),
        ],
        "summary": [
            "Types de subordonnées&nbsp;: relative, complétive, interrogative indirecte, circonstancielle, infinitive.",
            "Enchâssement (imbrication) nécessite une concordance rigoureuse des temps.",
            "Ellipse&nbsp;: supprimer un élément récupérable pour alléger le style.",
            "Concessives avancées&nbsp;: <em>si… que, quelque… que, quoi que, pour… que, avoir beau</em>.",
        ],
        "ex1": {
            "q": "Dans 'Ce qu'il dit m'étonne', la proposition 'ce qu'il dit' est&nbsp;:",
            "opts": ["Une proposition relative", "Une interrogative indirecte", "Une complétive sujet", "Une circonstancielle de cause"],
            "ans": "Une complétive sujet",
            "exp": "'Ce qu'il dit' est une complétive pronominale qui fonctionne comme sujet de <em>étonne</em>. Elle n'est pas introduite par si (interrogative ind.) ni ne renvoie à un antécédent (relative).",
        },
        "ex2": {
            "q": "Choisissez la bonne forme&nbsp;: '___ il fasse, il ne réussira pas.' (= quelle que soit la chose qu'il fasse)",
            "ans": "Quoi que",
            "exp": "<em>Quoi que</em> (deux mots) = quelle que soit la chose que. S'emploie avec le subjonctif et exprime une concession portant sur une action. <em>Quoique</em> (un mot) = bien que.",
            "accept": ["quoi que", "Quoi que"],
        },
        "ex3": {
            "q": "Quel est le rôle de 'ce qui' dans 'Elle est arrivée en retard, ce qui a tout compliqué' ?",
            "opts": ["Pronom relatif renvoyant à 'elle'", "Relative de liaison renvoyant à l'ensemble de la proposition", "Conjonction de coordination", "Interrogatif indirect"],
            "ans": "Relative de liaison renvoyant à l'ensemble de la proposition",
            "exp": "La relative de liaison <em>ce qui</em> renvoie à l'ensemble de la proposition précédente ('elle est arrivée en retard'), pas à un nom antécédent précis.",
        },
        "game_desc": "Maîtrisez la phrase complexe et ses constructions avancées",
        "items": [
            ("c1g05-subordination", "la subordination", "dépendance d'une proposition par rapport à la principale", "principale · subordonnée · dépendance", "La phrase complexe repose sur la subordination de propositions dépendantes.", "subordination = proposition dépendant de la principale", "dépendance d'une proposition par rapport à la principale"),
            ("c1g05-enchassement", "l'enchâssement", "imbrication d'une subordonnée dans une autre subordonnée", "imbrication · relative · complétive", "Je sais que celui qui viendra gagnera — deux niveaux d'enchâssement.", "enchâssement = subordonnée dans une subordonnée", "imbrication de propositions subordonnées"),
            ("c1g05-ellipse", "l'ellipse", "suppression d'un élément récupérable du contexte", "économie · style · implicite", "Il parla longuement et clairement — ellipse du sujet et verbe répétés.", "ellipse = suppression d'un élément récupérable", "suppression d'un élément implicitement compris"),
            ("c1g05-relative-liaison", "la relative de liaison", "relative renvoyant à toute une proposition antérieure", "ce qui · ce que · dont", "Elle est partie, ce qui m'a surpris — ce qui renvoie à toute la proposition.", "relative de liaison = réfère à toute la proposition", "relative dont l'antécédent est une proposition entière"),
            ("c1g05-quoi-que", "quoi que (+ subj.)", "concessive signifiant 'quelle que soit la chose que'", "concession · subjonctif · quoi que", "Quoi qu'il fasse, il échoue — quoi que introduit une concession totale.", "quoi que = quelle que soit la chose que (subj.)", "concession totale portant sur une action"),
            ("c1g05-avoir-beau", "avoir beau + inf.", "construction concessive signifiant 'même si, bien que'", "concession · beau · infructueux", "Il a beau travailler, il n'avance pas — avoir beau = effort sans résultat.", "avoir beau = même si, bien que", "concession exprimant un effort infructueux"),
            ("c1g05-quelque-que", "quelque… que (+ subj.)", "concessive portant sur une qualité ou quantité", "quelle que soit · qualité · subjonctif", "Quelque fatigué qu'il soit, il continue — concession sur la qualité.", "quelque… que = quelle que soit la qualité", "concession portant sur la qualité ou l'intensité"),
            ("c1g05-pour-que", "pour… que (+ subj.)", "concessive signifiant 'même si (très)'", "même si · intensité · subjonctif", "Pour intelligente qu'elle soit, elle peut se tromper — concession d'intensité.", "pour… que = même si très (subj.)", "concession d'intensité avec pour… que"),
        ],
    },

    "le-conditionnel-avance": {
        "level": "c1",
        "section": "grammaire",
        "num": "G06",
        "short": "Le Conditionnel Avanc&eacute;",
        "title": "Le Conditionnel Avanc&eacute;",
        "subtitle": "Hypoth&egrave;se, irr&eacute;el, conditionnel pass&eacute; — concordance des temps",
        "slides": [
            ("Rappel : les trois systèmes hypothétiques",
             "<p>Trois niveaux de réalité dans les propositions conditionnelles&nbsp;:</p>"
             "<table><tr><th>Type</th><th>Si + …</th><th>Principale</th><th>Réalité</th></tr>"
             "<tr><td>Réel</td><td>présent</td><td>futur/présent</td><td>possible</td></tr>"
             "<tr><td>Irréel du présent</td><td>imparfait</td><td>conditionnel présent</td><td>hypothétique</td></tr>"
             "<tr><td>Irréel du passé</td><td>plus-que-parfait</td><td>conditionnel passé</td><td>impossible</td></tr></table>"
             "<p><em>Si j'avais su, je serais venu.</em> (irréel du passé — c'est trop tard)</p>"),
            ("Conditionnel passé 2e forme",
             "<p>Le <strong>conditionnel passé 2e forme</strong> est identique au subjonctif plus-que-parfait. C'est un tour litt&eacute;raire&nbsp;:</p>"
             "<ul><li>Standard&nbsp;: <em>Il aurait voulu partir.</em></li>"
             "<li>Litt&eacute;raire&nbsp;: <em>Il eût voulu partir.</em></li></ul>"
             "<p>Il s'emploie&nbsp;:</p>"
             "<ul><li>Dans les apodoses conditionnelles litt&eacute;raires</li>"
             "<li>Comme conditionnel pass&eacute; de politesse soutenu&nbsp;:<br><em>J'eusse préféré une réponse plus claire.</em></li></ul>"),
            ("Structures conditionnelles sans 'si'",
             "<p>D'autres structures introduisent la condition sans <em>si</em>&nbsp;:</p>"
             "<table><tr><th>Structure</th><th>Exemple</th></tr>"
             "<tr><td>À condition que + subj.</td><td><em>Je viendrai à condition qu'il fasse beau.</em></td></tr>"
             "<tr><td>Pourvu que + subj.</td><td><em>Pourvu qu'il arrive à temps.</em></td></tr>"
             "<tr><td>Au cas où + cond.</td><td><em>Au cas où il viendrait, préviens-moi.</em></td></tr>"
             "<tr><td>Participe passé</td><td><em>Prévenu à temps, il aurait pu éviter ça.</em></td></tr>"
             "<tr><td>Inversion du sujet</td><td><em>Fût-il venu, cela n'aurait rien changé.</em> (litt.)</td></tr></table>"),
            ("Conditionnel d'information non vérifiée",
             "<p>Le conditionnel s'emploie pour marquer une <strong>information non confirmée</strong> (presse, rumeur)&nbsp;:</p>"
             "<ul><li><em>Le ministre aurait démissionné.</em> (conditionnel journalistique)</li>"
             "<li><em>L'entreprise serait en difficulté financière.</em></li>"
             "<li><em>Selon nos sources, il y aurait eu des négociations secrètes.</em></li></ul>"
             "<p>Ce conditionnel dit <em>épistémique</em> marque la distanciation du locuteur face à l'information.</p>"),
            ("Conditionnel à valeur temporelle (futur dans le passé)",
             "<p>Le conditionnel exprime un <strong>futur vu depuis le passé</strong> (discours indirect, concordance)&nbsp;:</p>"
             "<ul><li>Direct&nbsp;: <em>Il dit : 'Je viendrai demain.'</em></li>"
             "<li>Indirect&nbsp;: <em>Il dit qu'il viendrait le lendemain.</em></li></ul>"
             "<p>Conditionnel passé = futur antérieur dans le passé&nbsp;:</p>"
             "<ul><li>Direct&nbsp;: <em>Il dit : 'J'aurai fini à 17h.'</em></li>"
             "<li>Indirect&nbsp;: <em>Il dit qu'il aurait fini à 17h.</em></li></ul>"),
        ],
        "traps": [
            ("Si + conditionnel", "utiliser le conditionnel dans la proposition en <em>si</em>&nbsp;: <em>*Si il viendrait</em> est faux. Après <em>si</em> hypothétique, toujours indicatif (présent, imparfait, plus-que-parfait)."),
            ("Conditionnel passé 2e forme confondu avec subjonctif plus-que-parfait", "ces deux formes sont identiques mais leurs rôles diffèrent selon le contexte — dans une apodose, c'est un conditionnel passé; dans une subordonnée après que, c'est un subjonctif."),
            ("Au cas où + indicatif", "<em>Au cas où</em> exige le conditionnel, pas l'indicatif ni le subjonctif : <em>au cas où il viendrait</em> (pas <em>*vient</em> ni <em>*vienne</em>)."),
        ],
        "summary": [
            "Trois systèmes conditionnels : réel (si + présent / futur), irréel présent (si + imparfait / conditionnel), irréel passé (si + PQP / conditionnel passé).",
            "Conditionnel passé 2e forme = subjonctif plus-que-parfait — litt&eacute;raire.",
            "Structures sans si&nbsp;: <em>à condition que, pourvu que, au cas où</em>.",
            "Conditionnel épistémique (presse) et futur dans le passé (discours indirect).",
        ],
        "ex1": {
            "q": "Quelle est la construction correcte pour l'irréel du passé ?",
            "opts": ["Si il viendrait, j'aurais été content", "Si il venait, j'aurais été content", "Si il était venu, j'aurais été content", "Si il sera venu, j'aurai été content"],
            "ans": "Si il était venu, j'aurais été content",
            "exp": "L'irréel du passé = si + plus-que-parfait / conditionnel passé. <em>Si il était venu</em> (PQP) → <em>j'aurais été content</em> (conditionnel passé). Le conditionnel après <em>si</em> est toujours fautif.",
        },
        "ex2": {
            "q": "Reformulez en style indirect&nbsp;: 'Il annonce : Je serai là demain.'",
            "ans": "Il annonce qu'il serait là le lendemain.",
            "exp": "Au discours indirect, le futur de la principale devient conditionnel présent (futur dans le passé)&nbsp;: <em>sera</em> → <em>serait</em>. <em>Demain</em> → <em>le lendemain</em>.",
            "accept": ["il annonce qu'il serait là", "qu'il serait là le lendemain"],
        },
        "ex3": {
            "q": "Dans 'Selon ses collègues, il aurait quitté l'entreprise', le conditionnel exprime&nbsp;:",
            "opts": ["Une hypothèse irréelle", "Une information non vérifiée (conditionnel épistémique)", "Un futur dans le passé", "Une politesse"],
            "ans": "Une information non vérifiée (conditionnel épistémique)",
            "exp": "Le conditionnel journalistique ou épistémique marque que l'information est rapportée mais non confirmée. C'est très courant dans la presse et les rumeurs.",
        },
        "game_desc": "Maîtrisez le conditionnel et ses emplois avancés",
        "items": [
            ("c1g06-irreel-passe", "l'irréel du passé", "si + plus-que-parfait / conditionnel passé — impossible à réaliser", "plus-que-parfait · trop tard · passé", "Si j'avais su, je serais venu — irréel du passé, l'occasion est passée.", "irréel du passé = si + PQP / conditionnel passé", "hypothèse sur le passé impossible à réaliser"),
            ("c1g06-cond-2e", "le conditionnel passé 2e forme", "= subjonctif plus-que-parfait — style littéraire", "eût · litt&eacute;raire · soutenu", "Il eût voulu partir = il aurait voulu partir — style litt&eacute;raire soutenu.", "cond. passé 2e = eût/eussent + PP (litt.)", "conditionnel passé en style littéraire"),
            ("c1g06-au-cas-ou", "au cas où + conditionnel", "conditionnel dans la subordonnée après au cas où", "éventualité · conditionnel · précaution", "Au cas où il viendrait, préviens-moi — conditionnel obligatoire après au cas où.", "au cas où = toujours + conditionnel", "structure conditionnelle avec au cas où"),
            ("c1g06-epistemique", "le conditionnel épistémique", "conditionnel de l'information non vérifiée", "presse · rumeur · distanciation", "Le ministre aurait démissionné — conditionnel journalistique de prudence.", "conditionnel épistémique = info non confirmée", "conditionnel marquant une information non vérifiée"),
            ("c1g06-futur-passe", "le futur dans le passé", "conditionnel exprimant le futur vu depuis le passé", "discours indirect · futur · was going to", "Il dit qu'il viendrait — conditionnel = futur dans le passé au discours indirect.", "futur dans le passé = conditionnel en discours indirect", "futur vu depuis un moment passé"),
            ("c1g06-pourvu-que", "pourvu que + subjonctif", "condition-souhait : à condition que / espérons que", "espoir · subjonctif · souhait", "Pourvu qu'il réussisse ! — pourvu que exprime l'espoir et la condition.", "pourvu que = j'espère que + subjonctif", "condition-souhait introduite par pourvu que"),
            ("c1g06-inversion-cond", "inversion conditionnelle (litt.)", "condition exprimée par inversion : Fût-il venu...", "inversion · litt&eacute;raire · si omis", "Fût-il venu, rien n'aurait changé = S'il était venu — inversion littéraire.", "inversion = condition sans si (litt.)", "condition littéraire par inversion du sujet"),
            ("c1g06-si-interdit", "si + conditionnel (erreur)", "le conditionnel après si hypothétique est toujours fautif", "erreur · si · indicatif", "*Si il viendrait est faux — après si, toujours l'indicatif (imparfait, PQP).", "après si : jamais de conditionnel", "erreur classique : conditionnel après si"),
        ],
    },

    "les-temps-litteraires": {
        "level": "c1",
        "section": "grammaire",
        "num": "G07",
        "short": "Les Temps Litt&eacute;raires",
        "title": "Les Temps Litt&eacute;raires",
        "subtitle": "Pass&eacute; simple, pass&eacute; ant&eacute;rieur et leurs valeurs stylistiques",
        "slides": [
            ("Le passé simple : formation",
             "<p>Le <strong>passé simple</strong> se forme sur le radical de l'infinitif avec des terminaisons spécifiques&nbsp;:</p>"
             "<table><tr><th>Groupe</th><th>Terminaisons</th><th>Exemple</th></tr>"
             "<tr><td>-er</td><td>-ai, -as, -a, -âmes, -âtes, -èrent</td><td>il parla</td></tr>"
             "<tr><td>-ir/-re</td><td>-is, -is, -it, -îmes, -îtes, -irent</td><td>il finit</td></tr>"
             "<tr><td>Irrég.</td><td>-us, -us, -ut, -ûmes, -ûtes, -urent</td><td>il eut, il fut</td></tr></table>"
             "<p>Verbes irréguliers essentiels&nbsp;: <em>être → fut, avoir → eut, faire → fit, venir → vint, voir → vit, prendre → prit.</em></p>"),
            ("Valeurs du passé simple",
             "<p>Le passé simple exprime&nbsp;:</p>"
             "<ul><li><strong>Action ponctuelle et accomplie</strong> dans une narration au passé&nbsp;: <em>Il entra et s'assit.</em></li>"
             "<li><strong>Action de courte durée</strong> dans un contexte de description à l'imparfait&nbsp;: <em>Il faisait beau ; soudain, l'orage éclata.</em></li>"
             "<li><strong>Succession d'actions</strong>&nbsp;: <em>Il se leva, s'habilla et sortit.</em></li></ul>"
             "<p>Il s'oppose à l'imparfait (fond descriptif, durée, habitude) et au passé composé (registre oral/journalistique).</p>"),
            ("Le passé antérieur",
             "<p>Le <strong>passé antérieur</strong> = auxiliaire au passé simple + participe passé.</p>"
             "<p>Il exprime l'<strong>antériorité immédiate</strong> par rapport au passé simple.</p>"
             "<ul><li><em>Quand il eut fini, il sortit.</em></li>"
             "<li><em>Dès qu'elle fut arrivée, la réunion commença.</em></li>"
             "<li><em>À peine eut-il prononcé ces mots qu'un murmure s'éleva.</em></li></ul>"
             "<p>Il s'emploie surtout après <em>quand, dès que, aussitôt que, lorsque, à peine… que.</em></p>"),
            ("Style et effet du passé simple",
             "<p>Le passé simple produit des effets stylistiques importants&nbsp;:</p>"
             "<ul><li><strong>Distance narrative</strong>&nbsp;: le passé simple crée une distance entre le narrateur et les événements</li>"
             "<li><strong>Rythme</strong>&nbsp;: la succession de passés simples crée un rythme haletant</li>"
             "<li><strong>Solennité</strong>&nbsp;: le passé simple donne une tonalité soutenue et classique</li></ul>"
             "<p>Comparez&nbsp;:</p>"
             "<ul><li>PS&nbsp;: <em>Il entra, vit la scène, et tomba à genoux.</em> (dynamique, solennité)</li>"
             "<li>PC&nbsp;: <em>Il est entré, a vu la scène, et est tombé à genoux.</em> (plus proche, oral)</li></ul>"),
            ("Passé simple vs passé composé",
             "<table><tr><th></th><th>Passé simple</th><th>Passé composé</th></tr>"
             "<tr><td>Registre</td><td>Littéraire, soutenu, écrit</td><td>Oral, journalistique, courant</td></tr>"
             "<tr><td>Relation avec présent</td><td>Aucun lien</td><td>Résultat encore pertinent</td></tr>"
             "<tr><td>Usage</td><td>Roman, conte, histoire</td><td>Conversation, presse</td></tr>"
             "<tr><td>Exemple</td><td><em>Napoléon mourut en 1821.</em></td><td><em>Il est mort hier.</em></td></tr></table>"
             "<p>En France, le passé composé remplace le passé simple à l'oral. En français belge et suisse, le passé simple est parfois encore utilisé à l'oral.</p>"),
        ],
        "traps": [
            ("Passé simple à la première personne", "la 1ère et 2ème personne du passé simple sont rarissimes à l'oral mais existent en littérature&nbsp;: <em>je parlai, tu parlas, nous parlâmes.</em>"),
            ("Passé antérieur confondu avec plus-que-parfait", "le passé antérieur (auxiliaire au passé simple) est différent du plus-que-parfait (auxiliaire à l'imparfait). L'un exprime l'antériorité immédiate dans la narration littéraire, l'autre l'antériorité générale."),
            ("Passé simple des verbes irréguliers", "les formes irrégulières sont nombreuses&nbsp;: <em>il fut, il eut, il fit, il vint, il vit, il prit, il dit, il alla.</em>"),
        ],
        "summary": [
            "Passé simple = action ponctuelle accomplie dans la narration littéraire.",
            "S'oppose à l'imparfait (fond) et au passé composé (registre oral).",
            "Passé antérieur = auxiliaire (PS) + PP — antériorité immédiate après <em>quand, dès que, à peine</em>.",
            "Produit distance narrative, rythme et solennité dans le style soutenu.",
        ],
        "ex1": {
            "q": "Dans une narration littéraire, quel temps exprime le fond descriptif pendant lequel une action se produit ?",
            "opts": ["Le passé simple", "L'imparfait", "Le passé antérieur", "Le présent"],
            "ans": "L'imparfait",
            "exp": "L'imparfait exprime le fond, la description et la durée dans la narration littéraire. Le passé simple exprime les actions ponctuelles qui font avancer le récit.",
        },
        "ex2": {
            "q": "Donnez le passé antérieur de 'finir' à la 3e personne du singulier.",
            "ans": "il eut fini",
            "exp": "Passé antérieur = auxiliaire au passé simple + PP. <em>Avoir</em> → passé simple <em>il eut</em> + PP <em>fini</em> → <em>il eut fini</em>.",
            "accept": ["eut fini", "il eut fini"],
        },
        "ex3": {
            "q": "Pourquoi le passé simple est-il absent de la langue orale standard en France ?",
            "opts": ["Il est trop difficile à conjuguer", "Il est remplacé par le passé composé en registre oral", "Il a été officiellement supprimé", "Il n'existe que dans les textes médiévaux"],
            "ans": "Il est remplacé par le passé composé en registre oral",
            "exp": "En français oral standard (France), le passé composé remplace le passé simple. Le passé simple reste vivant à l'écrit littéraire et dans certaines variétés du français (belge, suisse).",
        },
        "game_desc": "Maîtrisez les temps littéraires et leurs valeurs stylistiques",
        "items": [
            ("c1g07-ps-ponctuel", "le passé simple ponctuel", "action accomplie et délimitée dans la narration littéraire", "ponctuel · accompli · littéraire", "Il entra, vit et s'assit — trois actions ponctuelles au passé simple.", "passé simple = action ponctuelle dans le récit", "action accomplie et délimitée dans la narration littéraire"),
            ("c1g07-imparfait-fond", "l'imparfait de fond", "imparfait exprimant le décor et la durée dans un récit", "description · durée · décor", "Il faisait beau quand l'orage éclata — imparfait = fond, passé simple = action.", "imparfait de fond = décor et durée du récit", "imparfait exprimant le fond descriptif d'un récit"),
            ("c1g07-passe-anterieur", "le passé antérieur", "auxiliaire (PS) + PP — antériorité immédiate dans le récit", "quand · dès que · antériorité", "Quand il eut fini, il sortit — passé antérieur avant le passé simple.", "passé antérieur = eut/fut + PP", "antériorité immédiate par rapport au passé simple"),
            ("c1g07-ps-rythme", "le rythme du passé simple", "succession de PS créant un effet de rapidité narrative", "rythme · dynamisme · enchaînement", "Il se leva, s'habilla et sortit — succession de PS crée un rythme rapide.", "succession de PS = rythme narratif rapide", "effet stylistique de rapidité par les passés simples"),
            ("c1g07-ps-irreguliers", "les passés simples irréguliers", "formes à mémoriser : fut, eut, fit, vint, vit, prit", "irrégulier · mémoriser · essentiel", "Il fut, il eut, il fit, il vint — irréguliers incontournables du passé simple.", "passé simple irrég. = fut/eut/fit/vint/vit/prit", "formes irrégulières essentielles du passé simple"),
            ("c1g07-a-peine", "à peine… que (+ PA)", "construction d'antériorité immédiate avec le passé antérieur", "à peine · inversé · antérieur", "À peine eut-il parlé qu'un murmure s'éleva — antériorité immédiate.", "à peine + PA = action aussitôt suivie d'une autre", "antériorité immédiate après à peine… que"),
            ("c1g07-ps-vs-pc", "passé simple vs passé composé", "distinction registre littéraire vs oral/journalistique", "registre · littéraire · oral", "Napoléon mourut (PS, historique) vs Il est mort hier (PC, oral).", "PS = littéraire ; PC = oral/journalistique", "opposition de registre entre passé simple et composé"),
            ("c1g07-distance-narr", "la distance narrative", "effet de recul créé par le passé simple dans un récit", "distance · narrateur · solennité", "Le passé simple crée une distance entre le narrateur et les faits racontés.", "passé simple = distance narrative et solennité", "effet de recul et de solennité du passé simple"),
        ],
    },

    "la-modalite-avancee": {
        "level": "c1",
        "section": "grammaire",
        "num": "G08",
        "short": "La Modalit&eacute; Avanc&eacute;e",
        "title": "La Modalit&eacute; Avanc&eacute;e",
        "subtitle": "Devoir, pouvoir, falloir — modalit&eacute; &eacute;pist&eacute;mique et d&eacute;ontique",
        "slides": [
            ("Modalité épistémique vs déontique",
             "<p>Les verbes modaux (<em>devoir, pouvoir, falloir</em>) ont deux grandes valeurs&nbsp;:</p>"
             "<table><tr><th>Modalité</th><th>Définition</th><th>Exemple</th></tr>"
             "<tr><td><strong>Épistémique</strong></td><td>probabilité, déduction</td><td><em>Il doit être là.</em> (= probablement)</td></tr>"
             "<tr><td><strong>Déontique</strong></td><td>obligation, permission, interdiction</td><td><em>Tu dois partir.</em> (= obligation)</td></tr></table>"
             "<p>Le contexte détermine la lecture. Souvent ambiguë&nbsp;: <em>Il peut partir</em> = il est peut-être parti (épistémique) ou il a la permission (déontique).</p>"),
            ("Devoir : tous ses sens",
             "<p><strong>Devoir</strong> au présent et aux temps composés&nbsp;:</p>"
             "<table><tr><th>Temps/mode</th><th>Valeur</th><th>Exemple</th></tr>"
             "<tr><td>Présent</td><td>obligation présente</td><td><em>Je dois partir.</em></td></tr>"
             "<tr><td>Présent épist.</td><td>probabilité présente</td><td><em>Il doit être à la maison.</em></td></tr>"
             "<tr><td>Conditionnel</td><td>conseil, reproche atténué</td><td><em>Tu devrais te reposer.</em></td></tr>"
             "<tr><td>Conditionnel passé</td><td>regret, reproche sur le passé</td><td><em>Tu aurais dû partir plus tôt.</em></td></tr>"
             "<tr><td>Passé composé épist.</td><td>déduction sur le passé</td><td><em>Il a dû oublier.</em></td></tr></table>"),
            ("Pouvoir : nuances épistémiques et déontiques",
             "<p><strong>Pouvoir</strong> au présent et aux temps composés&nbsp;:</p>"
             "<table><tr><th>Valeur</th><th>Exemple</th></tr>"
             "<tr><td>Capacité</td><td><em>Je peux courir vite.</em></td></tr>"
             "<tr><td>Permission</td><td><em>Tu peux partir.</em></td></tr>"
             "<tr><td>Possibilité épist.</td><td><em>Il peut se tromper.</em> (= peut-être)</td></tr>"
             "<tr><td>Éventualité</td><td><em>Cela pourrait arriver.</em></td></tr>"
             "<tr><td>Regret/reproche (passé)</td><td><em>Tu aurais pu me prévenir.</em></td></tr></table>"),
            ("Il faut, il est nécessaire, il est indispensable",
             "<p>Gradation des expressions d'obligation&nbsp;:</p>"
             "<table><tr><th>Expression</th><th>Force</th></tr>"
             "<tr><td><em>Il est indispensable de / que</em></td><td>Obligation absolue</td></tr>"
             "<tr><td><em>Il faut / il est nécessaire de</em></td><td>Obligation forte</td></tr>"
             "<tr><td><em>Il convient de / il importe de</em></td><td>Obligation modérée (soutenu)</td></tr>"
             "<tr><td><em>Il serait bon de / il serait utile de</em></td><td>Suggestion</td></tr>"
             "<tr><td><em>Il est permis de / on peut</em></td><td>Permission</td></tr></table>"),
            ("Modalité dans le discours académique",
             "<p>Dans l'écriture académique et formelle, la modalité épistémique est essentielle pour nuancer les affirmations&nbsp;:</p>"
             "<ul><li><em>Cette analyse semble montrer que…</em> (probabilité)</li>"
             "<li><em>On pourrait avancer que…</em> (hypothèse prudente)</li>"
             "<li><em>Il est probable que… / Il est possible que…</em></li>"
             "<li><em>Les données tendent à suggérer que…</em></li>"
             "<li><em>Tout laisse à penser que…</em></li></ul>"
             "<p>Ces expressions permettent de présenter des conclusions sans les affirmer avec une certitude excessive.</p>"),
        ],
        "traps": [
            ("Devoir épistémique confondu avec obligation", "<em>Il doit avoir oublié</em> = il a probablement oublié (épistémique), pas <em>il est obligé d'avoir oublié</em>."),
            ("Conditionnel passé de pouvoir mal interprété", "<em>Il aurait pu partir</em> peut signifier&nbsp;: (1) il avait la capacité mais ne l'a pas fait, (2) il est possible qu'il soit parti — contexte décisif."),
            ("Il faut que + indicatif", "<em>Il faut que</em> exige toujours le subjonctif&nbsp;: <em>il faut qu'il <strong>vienne</strong></em> (pas <em>*il vient</em>)."),
        ],
        "summary": [
            "Modalité épistémique (probabilité/déduction) vs déontique (obligation/permission).",
            "Devoir&nbsp;: obligation (présent), probabilité (présent épist.), conseil (cond.), reproche/regret (cond. passé).",
            "Pouvoir&nbsp;: capacité, permission, possibilité épistémique, reproche passé.",
            "Gradation obligation&nbsp;: indispensable > nécessaire > il convient > il serait bon.",
        ],
        "ex1": {
            "q": "Dans 'Il doit être en réunion', <em>doit</em> exprime&nbsp;:",
            "opts": ["Une obligation", "Une déduction/probabilité (épistémique)", "Un reproche", "Une permission"],
            "ans": "Une déduction/probabilité (épistémique)",
            "exp": "Ici, <em>doit</em> = probablement (déduction sur un état présent). On peut paraphraser&nbsp;: <em>il est sans doute en réunion</em>. Ce n'est pas une obligation car personne ne lui impose d'être en réunion.",
        },
        "ex2": {
            "q": "Traduisez ce reproche en fr.: 'You should have called me.' (impliquant un regret sur le passé)",
            "ans": "Tu aurais dû m'appeler.",
            "exp": "Le reproche ou regret portant sur une action passée non réalisée = <em>devoir</em> au conditionnel passé (<em>aurais dû</em>) + infinitif.",
            "accept": ["vous auriez dû m'appeler", "tu aurais dû m'appeler"],
        },
        "ex3": {
            "q": "Quelle expression marque l'obligation la plus forte&nbsp;?",
            "opts": ["Il serait bon de partir", "Il convient de partir", "Il est indispensable de partir", "On peut partir"],
            "ans": "Il est indispensable de partir",
            "exp": "<em>Indispensable</em> marque l'obligation absolue. La gradation décroissante est&nbsp;: indispensable > nécessaire/faut > convient/importe > serait bon > peut.",
        },
        "game_desc": "Maîtrisez la modalité épistémique et déontique en français avancé",
        "items": [
            ("c1g08-epistemique", "la modalité épistémique", "probabilité et déduction exprimées par les modaux", "probabilité · déduction · peut-être", "Il doit être parti = il est probablement parti (déduction épistémique).", "épistémique = probabilité et déduction", "modalité de probabilité et déduction"),
            ("c1g08-deontique", "la modalité déontique", "obligation et permission exprimées par les modaux", "obligation · permission · devoir", "Tu dois partir maintenant = obligation déontique.", "déontique = obligation et permission", "modalité d'obligation et de permission"),
            ("c1g08-devoir-regret", "devoir conditionnel passé", "aurait dû + inf. — reproche ou regret sur le passé", "regret · reproche · passé", "Tu aurais dû me prévenir — reproche sur une action passée non faite.", "devoir cond. passé = reproche/regret passé", "reproche ou regret sur une action passée non réalisée"),
            ("c1g08-pouvoir-repr", "pouvoir conditionnel passé", "aurait pu + inf. — capacité non exercée ou possibilité passée", "capacité · passé · reproche", "Tu aurais pu appeler — tu avais la possibilité mais tu ne l'as pas fait.", "pourvoir cond. passé = capacité non exercée", "possibilité ou capacité passée non réalisée"),
            ("c1g08-il-faut", "il faut que + subjonctif", "obligation impersonnelle exigeant le subjonctif", "obligation · falloir · subjonctif", "Il faut qu'il vienne — obligation impersonnelle avec subjonctif obligatoire.", "il faut que = obligation + subjonctif", "obligation impersonnelle construite avec le subjonctif"),
            ("c1g08-il-convient", "il convient de + infinitif", "expression d'obligation modérée en registre soutenu", "soutenu · obligation · politesse", "Il convient de respecter les règles — obligation soutenue et nuancée.", "il convient de = obligation modérée soutenue", "obligation modérée en registre formel"),
            ("c1g08-modal-acad", "modalité académique", "expressions de probabilité prudente dans l'écrit formel", "probabilité · nuance · académique", "Cette analyse semble montrer que… — modalité épistémique prudente.", "modalité académique = probabilité nuancée à l'écrit", "expressions de probabilité prudente dans le discours académique"),
            ("c1g08-gradation", "la gradation de l'obligation", "du plus fort au plus faible : indispensable → il serait bon", "nécessaire · indispensable · conseil", "Indispensable > nécessaire > il convient > il serait bon — gradation décroissante.", "gradation obligation = indispensable à il serait bon", "hiérarchie des expressions d'obligation en français"),
        ],
    },
}
