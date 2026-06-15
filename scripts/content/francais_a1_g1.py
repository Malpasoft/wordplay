"""French A1 Grammar — Batch 1: articles, être, pronoms sujets, négation."""

CHAPTERS = {
    'les-articles': {
        'level': 'a1',
        'section': 'grammaire',
        'num': 'G01',
        'short': 'Les Articles',
        'title': 'Les Articles — Définis et Indéfinis',
        'subtitle': "Apprends à utiliser le, la, l', les, un, une et des en français",
        'slides': [
            ("Qu'est-ce qu'un article ?", None,
             '<p class="slide-explanation">En français, chaque nom a un <b>genre</b> (masculin ou féminin) et un <b>nombre</b> (singulier ou pluriel). L\'article s\'accorde avec le nom.</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Un chat</b> dort. &rarr; un chat quelconque (inconnu)</p>'
             '<p style="margin-top:8px"><b>Le chat</b> de Marie dort. &rarr; ce chat précis (connu)</p>'
             '</div>'
             '<p style="margin-top:16px">Il existe deux types : les <b>articles définis</b> (le, la, l\', les) et les <b>articles indéfinis</b> (un, une, des).</p>'),
            ("Les articles définis", "Le, la, l', les",
             '<p class="slide-explanation">On utilise les articles définis pour parler de quelque chose de <b>connu ou spécifique</b> :</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse"><tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Genre</th><th style="padding:8px;text-align:left">Singulier</th><th style="padding:8px;text-align:left">Pluriel</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Masculin</td><td style="padding:8px"><b>le</b> livre</td><td style="padding:8px" rowspan="2"><b>les</b> livres, les tables</td></tr>'
             '<tr><td style="padding:8px">Féminin</td><td style="padding:8px"><b>la</b> table</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Devant voyelle / h muet</td><td style="padding:8px" colspan="2"><b>l\'</b>ami, l\'heure</td></tr>'
             '</table>'
             '<p>Exemples : <b>le chien, la maison, l\'école, les enfants</b>.</p>'),
            ("Les articles indéfinis", "Un, une, des",
             '<p class="slide-explanation">On utilise les articles indéfinis pour présenter quelque chose de <b>nouveau ou non identifié</b> :</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse"><tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Genre</th><th style="padding:8px;text-align:left">Singulier</th><th style="padding:8px;text-align:left">Pluriel</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Masculin</td><td style="padding:8px"><b>un</b> livre</td><td style="padding:8px" rowspan="2"><b>des</b> livres, des tables</td></tr>'
             '<tr><td style="padding:8px">Féminin</td><td style="padding:8px"><b>une</b> table</td></tr>'
             '</table>'
             '<p style="margin-top:12px">Exemples : <b>un chien, une maison, des enfants</b>. Je vois <b>un chat</b> dans la rue. Il y a <b>des fleurs</b> dans le jardin.</p>'),
            ("L'élision : le et la devant voyelle", None,
             '<p class="slide-explanation">Le et la <b>s\'élident</b> (perdent leur voyelle) devant un mot commençant par une voyelle ou un <b>h muet</b> :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><s>le ami</s> &rarr; <b>l\'ami</b></p>'
             '<p style="margin-top:8px"><s>la école</s> &rarr; <b>l\'école</b></p>'
             '<p style="margin-top:8px"><s>le hôpital</s> &rarr; <b>l\'hôpital</b> (h muet)</p>'
             '<p style="margin-top:8px"><b>le hibou</b> &rarr; pas d\'élision (h aspiré)</p>'
             '</div>'
             '<p>Au pluriel : pas d\'élision mais liaison orale — <b>les amis</b> [lez ami], <b>les écoles</b> [lez ekɔl].</p>'),
        ],
        'traps': [
            ("le ami", "l'ami", "Le s'élide devant une voyelle : le + ami = l'ami."),
            ("J'ai un informations.", "J'ai des informations.", "Informations est toujours pluriel : utilise des."),
            ("Je suis une professeure.", "Je suis professeure.", "Après être, le métier s'emploie sans article indéfini (sauf avec adjectif)."),
            ("un eau", "une eau", "Eau est féminin : une eau (ou l'eau avec l'article défini)."),
            ("des bon livres", "de bons livres", "Devant un adjectif pluriel, des devient de."),
        ],
        'summary': [
            ("le / la / l'", "défini singulier", "le chat, la table, l'ami"),
            ("les", "défini pluriel", "les chats, les tables"),
            ("un / une", "indéfini singulier", "un chien, une fleur"),
            ("des", "indéfini pluriel", "des chiens, des fleurs"),
            ("l' (élision)", "le/la devant voyelle ou h muet", "l'ami, l'école, l'hôpital"),
        ],
        'ex1': (
            "Articles définis ou indéfinis ?",
            "Choisis le bon article pour compléter chaque phrase.",
            [
                ("Je vois _____ chien dans le parc.", ["le", "un", "une", "des"], "un",
                 "On parle d'un chien non identifié : article indéfini un."),
                ("_____ Tour Eiffel est à Paris.", ["Une", "La", "Le", "L'"], "La",
                 "Tour est féminin. C'est un monument connu et spécifique : article défini la."),
                ("Elle a _____ amie à Lyon.", ["le", "un", "une", "des"], "une",
                 "Amie est féminin. C'est une amie non spécifiée : article indéfini une."),
                ("_____ enfants jouent dans le jardin.", ["Le", "Un", "Des", "Les"], "Les",
                 "On parle d'enfants spécifiques du contexte : article défini pluriel les."),
                ("Il mange _____ pomme.", ["le", "la", "une", "un"], "une",
                 "Pomme est féminin. C'est une pomme non spécifiée : article indéfini une."),
            ]
        ),
        'ex2': (
            "L'élision",
            "Réécris l'article et le nom avec élision si nécessaire (ex. : le ami → l'ami).",
            [
                ("le + arbre", "l'arbre", "Arbre commence par a : le → l'."),
                ("la + école", "l'école", "École commence par é : la → l'."),
                ("le + hibou", "le hibou", "Hibou a un h aspiré : pas d'élision."),
                ("la + université", "l'université", "Université commence par u : la → l'."),
                ("le + homme", "l'homme", "Homme a un h muet : le → l'."),
            ]
        ),
        'ex3': (
            "Genre des noms",
            "Choisis l'article défini correct selon le genre du nom.",
            [
                ("_____ voiture est rouge.", ["Le", "La", "L'", "Les"], "La",
                 "Voiture est féminin : la voiture."),
                ("_____ avion est en retard.", ["Le", "La", "L'", "Les"], "L'",
                 "Avion commence par a : élision → l'avion."),
                ("Il y a _____ arbres dans le parc.", ["le", "la", "l'", "les"], "les",
                 "Arbres est pluriel : les arbres."),
                ("_____ eau est froide.", ["Le", "La", "L'", "Les"], "L'",
                 "Eau est féminin et commence par e : l'eau."),
                ("C'est _____ beau film.", ["le", "la", "un", "une"], "un",
                 "Film est masculin. C'est un film non spécifié : un beau film."),
            ]
        ),
        'game_desc': "Entraîne-toi sur les articles définis et indéfinis du français.",
        'items': [
            ('art-01', 'le', 'article défini masculin singulier', 'déf. masc. sg.',
             'Le livre est sur la table.', '______ livre est sur la table.', 'Le'),
            ('art-02', 'la', 'article défini féminin singulier', 'déf. fém. sg.',
             'La maison est grande.', '______ maison est grande.', 'La'),
            ("art-03", "l'", "article défini devant voyelle ou h muet (élision)", "l' (élision)",
             "L'ami de Pierre est sympa.", "______ ami de Pierre est sympa.", "L'"),
            ('art-04', 'les', 'article défini pluriel (masc. et fém.)', 'déf. pl.',
             'Les enfants jouent dehors.', '______ enfants jouent dehors.', 'Les'),
            ('art-05', 'un', 'article indéfini masculin singulier', 'indéf. masc. sg.',
             "J'ai un chien.", "J'ai ______ chien.", 'un'),
            ('art-06', 'une', 'article indéfini féminin singulier', 'indéf. fém. sg.',
             'Elle mange une pomme.', 'Elle mange ______ pomme.', 'une'),
            ('art-07', 'des', 'article indéfini pluriel', 'indéf. pl.',
             'Nous avons des amis à Paris.', 'Nous avons ______ amis à Paris.', 'des'),
            ('art-08', 'de', "article indéfini pluriel devant adjectif (des → de)", "des → de + adj.",
             'Ce sont de bons livres.', 'Ce sont ______ bons livres.', 'de'),
        ],
    },

    'le-verbe-etre': {
        'level': 'a1',
        'section': 'grammaire',
        'num': 'G02',
        'short': 'Le Verbe Être',
        'title': 'Le Verbe Être — Conjugaison et Emplois',
        'subtitle': "Maîtrise la conjugaison du verbe être au présent de l'indicatif",
        'slides': [
            ("Le verbe être au présent", "Conjugaison complète",
             '<p class="slide-explanation">Le verbe <b>être</b> est l\'un des verbes les plus importants du français. Sa conjugaison est irrégulière :</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse"><tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronom</th><th style="padding:8px;text-align:left">Être</th><th style="padding:8px;text-align:left">Exemple</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">je</td><td style="padding:8px"><b>suis</b></td><td style="padding:8px">Je suis étudiant.</td></tr>'
             '<tr><td style="padding:8px">tu</td><td style="padding:8px"><b>es</b></td><td style="padding:8px">Tu es français ?</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">il / elle / on</td><td style="padding:8px"><b>est</b></td><td style="padding:8px">Elle est médecin.</td></tr>'
             '<tr><td style="padding:8px">nous</td><td style="padding:8px"><b>sommes</b></td><td style="padding:8px">Nous sommes amis.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">vous</td><td style="padding:8px"><b>êtes</b></td><td style="padding:8px">Vous êtes prêts ?</td></tr>'
             '<tr><td style="padding:8px">ils / elles</td><td style="padding:8px"><b>sont</b></td><td style="padding:8px">Ils sont à Paris.</td></tr>'
             '</table>'),
            ("Utilisations principales de être", None,
             '<p class="slide-explanation">On utilise <b>être</b> pour exprimer :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>1. L\'identité et la nationalité :</b> Je suis français. Elle s\'appelle Marie.</p>'
             '<p style="margin-top:8px"><b>2. La profession :</b> Il est professeur. Nous sommes médecins.</p>'
             '<p style="margin-top:8px"><b>3. La description (adjectif) :</b> La maison est grande. Tu es gentil.</p>'
             '<p style="margin-top:8px"><b>4. L\'origine et la localisation :</b> Je suis de Lyon. Il est en France.</p>'
             '<p style="margin-top:8px"><b>5. L\'heure :</b> Il est deux heures. Il est midi.</p>'
             '</div>'),
            ("Être + adjectif : l'accord", None,
             '<p class="slide-explanation">Quand on utilise être avec un adjectif, l\'adjectif <b>s\'accorde</b> en genre et en nombre avec le sujet :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>Paul est grand. &rarr; Marie est grand<b>e</b>.</p>'
             '<p style="margin-top:8px">Paul est content. &rarr; Marie est content<b>e</b>.</p>'
             '<p style="margin-top:8px">Les garçons sont grand<b>s</b>. &rarr; Les filles sont grand<b>es</b>.</p>'
             '</div>'
             '<p style="margin-top:12px">La forme de base (masculin singulier) est la forme du dictionnaire.</p>'),
            ("C'est vs Il/Elle est", None,
             '<p class="slide-explanation">Deux structures très courantes avec être :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>C\'est</b> + article + nom : C\'est un médecin. C\'est la maison de Paul.</p>'
             '<p style="margin-top:8px"><b>Il/Elle est</b> + nom de métier (sans article) : Il est médecin.</p>'
             '<p style="margin-top:12px"><b>C\'est</b> + adjectif (sens général) : C\'est beau ! C\'est difficile.</p>'
             '<p style="margin-top:8px"><b>Il/Elle est</b> + adjectif (pour une personne précise) : Il est intelligent. Elle est belle.</p>'
             '</div>'),
        ],
        'traps': [
            ("Je suis bien.", "Je vais bien.", "Pour la santé, on utilise aller, pas être : Je vais bien."),
            ("C'est un médecin. / Il est un médecin.", "C'est un médecin. / Il est médecin.", "Après il/elle est, le métier va sans article. Après c'est, on met l'article."),
            ("Je suis de accord.", "Je suis d'accord.", "De + accord : la préposition de s'élide devant la voyelle → d'accord."),
            ("Vous êtes un professeur ?", "Vous êtes professeur ?", "Après être, le métier s'emploie sans article."),
            ("Il est deux heures et demie.", "Il est deux heures et demie. ✓", "Cette phrase est correcte : il est + heure. Pas d'erreur ici."),
        ],
        'summary': [
            ("je suis", "1re pers. sing.", "Je suis étudiant."),
            ("tu es", "2e pers. sing.", "Tu es prêt ?"),
            ("il/elle/on est", "3e pers. sing.", "Elle est médecin."),
            ("nous sommes", "1re pers. pl.", "Nous sommes amis."),
            ("vous êtes", "2e pers. pl.", "Vous êtes en retard."),
            ("ils/elles sont", "3e pers. pl.", "Ils sont à Paris."),
        ],
        'ex1': (
            "Conjugaison du verbe être",
            "Choisis la forme correcte du verbe être.",
            [
                ("Je _____ étudiant.", ["suis", "es", "est", "sommes"], "suis",
                 "Je → première personne singulier : je suis."),
                ("Tu _____ français ?", ["suis", "es", "est", "êtes"], "es",
                 "Tu → deuxième personne singulier : tu es."),
                ("Elle _____ médecin.", ["suis", "es", "est", "sont"], "est",
                 "Elle → troisième personne singulier : elle est."),
                ("Nous _____ en retard.", ["sommes", "êtes", "sont", "suis"], "sommes",
                 "Nous → première personne pluriel : nous sommes."),
                ("Ils _____ à Paris.", ["est", "êtes", "sommes", "sont"], "sont",
                 "Ils → troisième personne pluriel : ils sont."),
            ]
        ),
        'ex2': (
            "Phrases avec être",
            "Conjugue le verbe être à la bonne forme.",
            [
                ("Vous _____ prêts ?", "êtes", "Vous → deuxième personne pluriel : vous êtes."),
                ("On _____ contents.", "est", "On se conjugue comme il/elle : on est."),
                ("Elles _____ italiennes.", "sont", "Elles → troisième personne pluriel : elles sont."),
                ("Je _____ de Paris.", "suis", "Je → première personne singulier : je suis."),
                ("Il _____ midi.", "est", "L'heure avec il est : il est midi."),
            ]
        ),
        'ex3': (
            "Être + adjectif",
            "Choisis la forme correcte.",
            [
                ("La maison _____ grande.", ["suis", "êtes", "est", "sont"], "est",
                 "La maison → troisième personne singulier : est."),
                ("C'est _____ médecin.", ["un", "une", "de", "à"], "un",
                 "C'est + article + nom : c'est un médecin (médecin est masculin)."),
                ("Il _____ professeur.", ["suis", "es", "est", "êtes"], "est",
                 "Il → troisième personne singulier : il est. Sans article après être + métier."),
                ("Les élèves _____ contents.", ["sommes", "suis", "êtes", "sont"], "sont",
                 "Les élèves → troisième personne pluriel : sont."),
                ("Nous _____ contents de vous voir.", ["sommes", "suis", "êtes", "sont"], "sommes",
                 "Nous → première personne pluriel : nous sommes."),
            ]
        ),
        'game_desc': "Maîtrise la conjugaison et les emplois du verbe être en français.",
        'items': [
            ('etre-01', 'je suis', 'verbe être à la 1re personne singulier', '1sg',
             'Je suis étudiant à Paris.', 'Je ______ étudiant à Paris.', 'suis'),
            ('etre-02', 'tu es', 'verbe être à la 2e personne singulier', '2sg',
             'Tu es prêt pour le cours ?', 'Tu ______ prêt pour le cours ?', 'es'),
            ('etre-03', 'il/elle est', 'verbe être à la 3e personne singulier', '3sg',
             'Elle est professeure de français.', 'Elle ______ professeure de français.', 'est'),
            ('etre-04', 'nous sommes', 'verbe être à la 1re personne pluriel', '1pl',
             'Nous sommes en vacances.', 'Nous ______ en vacances.', 'sommes'),
            ('etre-05', 'vous êtes', 'verbe être à la 2e personne pluriel', '2pl',
             'Vous êtes en retard.', 'Vous ______ en retard.', 'êtes'),
            ('etre-06', 'ils/elles sont', 'verbe être à la 3e personne pluriel', '3pl',
             'Ils sont fatigués après le voyage.', 'Ils ______ fatigués après le voyage.', 'sont'),
            ("etre-07", "c'est", "présentatif : c'est + article + nom", "présentatif",
             "C'est un bon restaurant.", "C'______ un bon restaurant.", "est"),
            ('etre-08', 'être + adjectif', "l'adjectif s'accorde avec le sujet", "accord adj.",
             'Les élèves sont contents.', 'Les élèves ______ contents.', 'sont'),
        ],
    },

    'les-pronoms-sujets': {
        'level': 'a1',
        'section': 'grammaire',
        'num': 'G03',
        'short': 'Les Pronoms Sujets',
        'title': 'Les Pronoms Sujets — Je, Tu, Il, Elle...',
        'subtitle': "Apprends les huit pronoms sujets du français et leurs emplois",
        'slides': [
            ("Les huit pronoms sujets", None,
             '<p class="slide-explanation">En français, le <b>pronom sujet est obligatoire</b> avant le verbe. Il y a huit pronoms sujets :</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse"><tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronom</th><th style="padding:8px;text-align:left">Sens</th><th style="padding:8px;text-align:left">Exemple</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>je</b></td><td style="padding:8px">I — 1re sg.</td><td style="padding:8px">Je parle.</td></tr>'
             '<tr><td style="padding:8px"><b>tu</b></td><td style="padding:8px">you (familier) — 2e sg.</td><td style="padding:8px">Tu parles.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>il / elle / on</b></td><td style="padding:8px">he / she / one — 3e sg.</td><td style="padding:8px">Il parle. On parle.</td></tr>'
             '<tr><td style="padding:8px"><b>nous</b></td><td style="padding:8px">we — 1re pl.</td><td style="padding:8px">Nous parlons.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>vous</b></td><td style="padding:8px">you plural / formal — 2e pl.</td><td style="padding:8px">Vous parlez.</td></tr>'
             '<tr><td style="padding:8px"><b>ils / elles</b></td><td style="padding:8px">they masc. / fém. — 3e pl.</td><td style="padding:8px">Ils parlent. Elles parlent.</td></tr>'
             '</table>'),
            ("Tu vs Vous — tutoiement et vouvoiement", None,
             '<p class="slide-explanation">Le français distingue le registre familier et formel :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Tu</b> (tutoiement) : famille, amis, enfants, collègues proches.</p>'
             '<p style="margin-top:8px"><b>Vous</b> (vouvoiement) : inconnus, supérieurs hiérarchiques, personnes âgées.</p>'
             '<p style="margin-top:12px">Tu veux un café ? (à un ami)</p>'
             '<p>Vous voulez un café, madame ? (formel)</p>'
             '</div>'
             '<p>Vous est aussi le pluriel de tu : <b>Vous</b> deux, venez ici !</p>'),
            ("On — le pronom indéfini", None,
             '<p class="slide-explanation"><b>On</b> est très fréquent en français parlé. Il peut signifier :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>1. Nous (informel) :</b> On va au cinéma ce soir. (= Nous allons au cinéma.)</p>'
             '<p style="margin-top:8px"><b>2. Les gens en général :</b> En France, on mange à midi.</p>'
             '<p style="margin-top:8px"><b>3. Quelqu\'un (indéfini) :</b> On a téléphoné pour toi.</p>'
             '</div>'
             '<p>On se conjugue toujours comme <b>il / elle</b> (3e personne singulier).</p>'),
            ("Ils vs Elles — le genre du groupe", None,
             '<p class="slide-explanation">Pour les groupes mixtes, le français utilise le <b>masculin pluriel</b> :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>Marie + Pierre &rarr; <b>Ils</b> sont amis. (groupe mixte = masc. pluriel)</p>'
             '<p style="margin-top:8px">Marie + Julie &rarr; <b>Elles</b> sont amies. (groupe tout féminin)</p>'
             '<p style="margin-top:8px">Pierre + Paul &rarr; <b>Ils</b> sont amis. (groupe tout masculin)</p>'
             '</div>'
             '<p>Un seul homme dans un groupe féminin &rarr; <b>ils</b>. C\'est la règle du masculin générique.</p>'),
        ],
        'traps': [
            ("Parle français.", "Je parle français.", "Le pronom sujet est obligatoire en français. On ne peut pas l'omettre."),
            ("On sont contents.", "On est content.", "On se conjugue toujours à la 3e personne singulier : on est."),
            ("Il et elle sont amis.", "Ils sont amis.", "Pour remplacer un groupe mixte, utilise ils."),
            ("Tu veux du café, monsieur ?", "Vous voulez du café, monsieur ?", "Avec un inconnu ou un supérieur, on vouvoie : vous."),
            ("Nous, on est différent.", "Nous, on est différents. ✓", "Cette phrase est correcte à l'oral. On = nous, mais l'adjectif peut s'accorder au pluriel."),
        ],
        'summary': [
            ("je", "1re pers. sg.", "Je parle français."),
            ("tu / vous (poli)", "2e pers. sg. (fam. / formel)", "Tu viens ? / Vous venez ?"),
            ("il / elle / on", "3e pers. sg.", "Il est là. On mange."),
            ("nous", "1re pers. pl.", "Nous sommes prêts."),
            ("vous", "2e pers. pl. ou politesse", "Vous parlez bien."),
            ("ils / elles", "3e pers. pl. masc. / fém.", "Ils jouent. Elles chantent."),
        ],
        'ex1': (
            "Quel pronom ?",
            "Choisis le bon pronom sujet.",
            [
                ("_____ suis étudiant.", ["Je", "Tu", "Il", "Nous"], "Je",
                 "La forme suis correspond à je : je suis."),
                ("_____ es français ?", ["Je", "Tu", "Il", "Vous"], "Tu",
                 "La forme es correspond à tu : tu es."),
                ("Marie et Paul... _____ sont amis.", ["Ils", "Elles", "On", "Nous"], "Ils",
                 "Groupe mixte (masc. + fém.) → pronom ils."),
                ("_____ allons au marché.", ["Vous", "Ils", "Nous", "On"], "Nous",
                 "La forme allons correspond à nous : nous allons."),
                ("Marie et Julie... _____ parlent ensemble.", ["Ils", "Elles", "On", "Tu"], "Elles",
                 "Groupe tout féminin → pronom elles."),
            ]
        ),
        'ex2': (
            "Tu ou Vous ?",
            "Écris tu ou vous selon la situation.",
            [
                ("Tu parles à ton meilleur ami.", "tu", "Ami proche = tutoiement : tu."),
                ("Tu parles à ton patron.", "vous", "Supérieur hiérarchique = vouvoiement : vous."),
                ("Tu parles à un inconnu dans la rue.", "vous", "Inconnu = vouvoiement : vous."),
                ("Tu parles à ta petite sœur.", "tu", "Membre de la famille = tutoiement : tu."),
                ("Tu parles à deux collègues.", "vous", "Plusieurs personnes = vous (pluriel)."),
            ]
        ),
        'ex3': (
            "On — quel sens ?",
            "Quel est le sens de 'on' dans chaque phrase ?",
            [
                ("On va au cinéma ce soir.", ["nous", "quelqu'un", "les gens", "vous"], "nous",
                 "On va au cinéma = Nous allons au cinéma (informel)."),
                ("En France, on mange à midi.", ["nous", "quelqu'un", "les gens", "vous"], "les gens",
                 "On parle d'une habitude culturelle générale."),
                ("On a téléphoné pour toi.", ["nous", "quelqu'un", "les gens", "vous"], "quelqu'un",
                 "On = une personne non identifiée qui a téléphoné."),
                ("On est fatigués ce soir.", ["nous", "quelqu'un", "les gens", "vous"], "nous",
                 "On est fatigués = Nous sommes fatigués (registre informel)."),
                ("Ici, on parle anglais.", ["nous", "quelqu'un", "les gens", "vous"], "les gens",
                 "On parle d'une pratique générale dans cet endroit."),
            ]
        ),
        'game_desc': "Entraîne-toi sur les pronoms sujets du français.",
        'items': [
            ('pron-01', 'je', 'pronom sujet 1re personne singulier', '1re sg.',
             'Je parle français.', '______ parle français.', 'Je'),
            ('pron-02', 'tu', 'pronom sujet 2e personne singulier (familier)', '2e sg. fam.',
             'Tu es étudiant.', '______ es étudiant.', 'Tu'),
            ('pron-03', 'il', 'pronom sujet masculin 3e personne singulier', '3e sg. masc.',
             'Il habite à Bordeaux.', '______ habite à Bordeaux.', 'Il'),
            ('pron-04', 'elle', 'pronom sujet féminin 3e personne singulier', '3e sg. fém.',
             'Elle travaille à Lyon.', '______ travaille à Lyon.', 'Elle'),
            ('pron-05', 'on', 'pronom indéfini = nous (informel) ou les gens en général', 'indéf.',
             'On va au cinéma ce soir.', '______ va au cinéma ce soir.', 'On'),
            ('pron-06', 'nous', 'pronom sujet 1re personne pluriel', '1re pl.',
             'Nous sommes en vacances.', '______ sommes en vacances.', 'Nous'),
            ('pron-07', 'vous', 'pronom sujet 2e personne pluriel ou politesse', '2e pl. / pol.',
             'Vous parlez très bien français.', '______ parlez très bien français.', 'Vous'),
            ('pron-08', 'ils / elles', 'pronom sujet 3e personne pluriel (masc. / fém.)', '3e pl.',
             'Elles chantent dans la chorale.', '______ chantent dans la chorale.', 'Elles'),
        ],
    },

    'la-negation': {
        'level': 'a1',
        'section': 'grammaire',
        'num': 'G04',
        'short': 'La Négation',
        'title': 'La Négation — Ne...Pas et Autres Formes',
        'subtitle': "Apprends à former des phrases négatives en français",
        'slides': [
            ("La négation de base : ne...pas", None,
             '<p class="slide-explanation">En français, la négation de base se forme avec <b>ne...pas</b>. Le verbe est entouré de <b>ne</b> (avant) et <b>pas</b> (après) :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>Je <b>ne</b> parle <b>pas</b> espagnol.</p>'
             '<p style="margin-top:8px">Il <b>ne</b> mange <b>pas</b> de viande.</p>'
             '<p style="margin-top:8px">Nous <b>ne</b> sommes <b>pas</b> en retard.</p>'
             '</div>'
             '<p style="margin-top:16px"><b>Structure :</b> SUJET + <b>ne</b> + VERBE + <b>pas</b> + (complément)</p>'),
            ("L'élision de ne devant une voyelle", None,
             '<p class="slide-explanation">La particule <b>ne</b> s\'élide en <b>n\'</b> devant un verbe commençant par une voyelle ou un h muet :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>Je <b>n\'</b>ai pas de voiture. (ne + ai &rarr; n\'ai)</p>'
             '<p style="margin-top:8px">Elle <b>n\'</b>est pas là. (ne + est &rarr; n\'est)</p>'
             '<p style="margin-top:8px">Il <b>n\'</b>habite pas ici. (ne + habite &rarr; n\'habite)</p>'
             '</div>'
             '<p style="margin-top:12px">Le <b>pas</b> reste toujours après le verbe, sans élision.</p>'),
            ("Articles après la négation", None,
             '<p class="slide-explanation">Après une négation, les articles <b>un, une, des, du, de la, de l\'</b> deviennent <b>de</b> (ou <b>d\'</b>) :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>J\'ai <b>un</b> chien. &rarr; Je n\'ai <b>pas de</b> chien.</p>'
             '<p style="margin-top:8px">Il boit <b>du</b> café. &rarr; Il ne boit <b>pas de</b> café.</p>'
             '<p style="margin-top:8px">Elle mange <b>des</b> légumes. &rarr; Elle ne mange <b>pas de</b> légumes.</p>'
             '</div>'
             '<p style="margin-top:12px">Exception : les articles <b>définis</b> (le, la, les) ne changent <b>pas</b> après la négation.</p>'),
            ("Autres formes de négation", None,
             '<p class="slide-explanation">D\'autres expressions négatives permettent de nuancer :</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse"><tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Expression</th><th style="padding:8px;text-align:left">Sens</th><th style="padding:8px;text-align:left">Exemple</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>ne...plus</b></td><td style="padding:8px">not anymore</td><td style="padding:8px">Je ne fume plus.</td></tr>'
             '<tr><td style="padding:8px"><b>ne...jamais</b></td><td style="padding:8px">never</td><td style="padding:8px">Il ne ment jamais.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>ne...rien</b></td><td style="padding:8px">nothing</td><td style="padding:8px">Elle ne dit rien.</td></tr>'
             '<tr><td style="padding:8px"><b>ne...personne</b></td><td style="padding:8px">nobody</td><td style="padding:8px">Je ne vois personne.</td></tr>'
             '</table>'),
        ],
        'traps': [
            ("Je ne sais pas rien.", "Je ne sais rien.", "En français, on ne cumule pas deux négations : ne...pas + rien est impossible. Utilise ne...rien."),
            ("Il parle pas.", "Il ne parle pas.", "Dans l'écrit formel, ne est obligatoire. À l'oral familier, on l'omet souvent."),
            ("Je n'ai pas un chien.", "Je n'ai pas de chien.", "Après ne...pas, un/une/des/du/de la deviennent de."),
            ("Elle ne mange jamais pas.", "Elle ne mange jamais.", "Ne...jamais et ne...pas ne se combinent pas."),
            ("Ne pas il vient.", "Il ne vient pas.", "Structure obligatoire : sujet + ne + verbe + pas. Ne vient toujours avant le verbe."),
        ],
        'summary': [
            ("ne...pas", "négation de base", "Je ne parle pas."),
            ("n'...pas", "élision de ne devant voyelle", "Il n'est pas là."),
            ("pas de", "article indéfini → de après négation", "Je n'ai pas de chien."),
            ("ne...plus", "not anymore", "Je ne fume plus."),
            ("ne...jamais", "never", "Elle ne ment jamais."),
            ("ne...rien", "nothing", "Il ne dit rien."),
        ],
        'ex1': (
            "Mettre à la forme négative",
            "Choisis la négation correcte.",
            [
                ("Je parle espagnol. &rarr; Je _____ espagnol.", ["ne parle pas", "parle ne pas", "pas parle", "ne pas parle"], "ne parle pas",
                 "Structure ne + verbe + pas : je ne parle pas espagnol."),
                ("Tu es en retard. &rarr; Tu _____ en retard.", ["n'es pas", "ne es pas", "es ne pas", "pas es"], "n'es pas",
                 "Ne s'élide devant une voyelle : tu n'es pas en retard."),
                ("Il mange de la viande. &rarr; Il _____ de viande.", ["ne mange pas", "mange pas", "ne pas mange", "ne mange"], "ne mange pas",
                 "Structure ne + verbe + pas. Et de la viande → de viande après négation."),
                ("Nous avons des enfants. &rarr; Nous _____ d'enfants.", ["n'avons pas", "ne avons pas", "avons pas", "pas avons"], "n'avons pas",
                 "Ne s'élide devant avons : nous n'avons pas. Et des → d' après négation."),
                ("Elle fume. &rarr; Elle _____ plus.", ["ne fume", "ne fume pas", "fume ne", "pas fume"], "ne fume",
                 "Ne...plus : elle ne fume plus. Ne fume (sans pas) car on utilise plus."),
            ]
        ),
        'ex2': (
            "Articles après la négation",
            "Complète avec l'article correct après la négation (de, d' ou le/la/les).",
            [
                ("Je n'ai pas _____ chat.", "de", "Un chat → pas de chat (un → de après négation)."),
                ("Il ne boit pas _____ café.", "de", "Du café → de café (du → de après négation)."),
                ("Nous n'avons pas _____ amis ici.", "d'", "Des amis → d'amis (des → de → d' devant voyelle)."),
                ("Elle ne mange pas _____ salade.", "de", "De la salade → de salade (de la → de après négation)."),
                ("Je ne lis pas _____ journal.", "le", "Le journal → le journal : les articles définis ne changent pas après la négation."),
            ]
        ),
        'ex3': (
            "Quelle négation ?",
            "Choisis la forme négative qui correspond au sens indiqué.",
            [
                ("Il ne travaille _____ depuis janvier. (not anymore)", ["pas", "jamais", "plus", "rien"], "plus",
                 "Not anymore = ne...plus : il ne travaille plus depuis janvier."),
                ("Je ne mange _____ de sucre. (never)", ["pas", "plus", "jamais", "rien"], "jamais",
                 "Never = ne...jamais : je ne mange jamais de sucre."),
                ("Elle ne dit _____. (nothing)", ["pas", "plus", "jamais", "rien"], "rien",
                 "Nothing = ne...rien : elle ne dit rien."),
                ("Nous ne voyons _____ dans le noir. (nothing)", ["pas", "jamais", "rien", "plus"], "rien",
                 "Nothing = ne...rien : nous ne voyons rien dans le noir."),
                ("Tu ne fais _____ de sport ? (not anymore)", ["pas", "plus", "jamais", "rien"], "plus",
                 "Not anymore = ne...plus : tu ne fais plus de sport ?"),
            ]
        ),
        'game_desc': "Entraîne-toi sur la négation en français : ne...pas et ses variantes.",
        'items': [
            ('neg-01', 'ne...pas', 'forme de base de la négation', 'négation simple',
             'Je ne parle pas espagnol.', 'Je ______ parle pas espagnol.', 'ne'),
            ("neg-02", "n'...pas", "élision de ne devant une voyelle ou h muet", "n' (élision)",
             "Il n'est pas là.", "Il ______ est pas là.", "n'"),
            ('neg-03', 'pas de', "article indéfini/partitif → de après la négation", "de après nég.",
             "Je n'ai pas de voiture.", "Je n'ai pas ______ voiture.", 'de'),
            ('neg-04', 'ne...plus', 'not anymore / no longer', 'plus',
             'Elle ne fume plus.', 'Elle ne fume ______.', 'plus'),
            ('neg-05', 'ne...jamais', 'never', 'jamais',
             'Il ne ment jamais.', 'Il ne ment ______.', 'jamais'),
            ('neg-06', 'ne...rien', 'nothing / not anything', 'rien',
             'Je ne dis rien.', 'Je ne dis ______.', 'rien'),
            ('neg-07', 'ne...personne', 'nobody / not anyone', 'personne',
             'Elle ne voit personne.', 'Elle ne voit ______.', 'personne'),
            ('neg-08', 'ne...que', "restriction : only / nothing but", "seulement",
             'Je ne parle que français.', 'Je ne parle ______ français.', 'que'),
        ],
    },
}
