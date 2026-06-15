"""French A1 Grammar — Batch 3: présent irrégulier, questions, prépositions, nombres."""

CHAPTERS = {
    'le-present-irregulier': {
        'level': 'a1',
        'section': 'grammaire',
        'num': 'G09',
        'short': 'Le Présent Irrégulier',
        'title': 'Le Présent Irrégulier — Aller, Faire, Pouvoir, Vouloir',
        'subtitle': "Maîtrise les verbes irréguliers essentiels du français A1",
        'slides': [
            ("Le verbe aller", "to go",
             '<p class="slide-explanation">Le verbe <b>aller</b> est très irrégulier. Sa conjugaison au présent :</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse"><tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronom</th><th style="padding:8px;text-align:left">Aller</th><th style="padding:8px;text-align:left">Exemple</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">je</td><td style="padding:8px"><b>vais</b></td><td style="padding:8px">Je vais bien.</td></tr>'
             '<tr><td style="padding:8px">tu</td><td style="padding:8px"><b>vas</b></td><td style="padding:8px">Tu vas au marché ?</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">il / elle / on</td><td style="padding:8px"><b>va</b></td><td style="padding:8px">Elle va à l\'école.</td></tr>'
             '<tr><td style="padding:8px">nous</td><td style="padding:8px"><b>allons</b></td><td style="padding:8px">Nous allons au cinéma.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">vous</td><td style="padding:8px"><b>allez</b></td><td style="padding:8px">Vous allez bien ?</td></tr>'
             '<tr><td style="padding:8px">ils / elles</td><td style="padding:8px"><b>vont</b></td><td style="padding:8px">Ils vont en France.</td></tr>'
             '</table>'
             '<p style="margin-top:10px">Aller + infinitif = futur proche : Je <b>vais manger</b>. Elle <b>va partir</b>.</p>'),
            ("Le verbe faire", "to do / to make",
             '<p class="slide-explanation">Le verbe <b>faire</b> est irrégulier et très fréquent :</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse"><tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronom</th><th style="padding:8px;text-align:left">Faire</th><th style="padding:8px;text-align:left">Exemple</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">je</td><td style="padding:8px"><b>fais</b></td><td style="padding:8px">Je fais du sport.</td></tr>'
             '<tr><td style="padding:8px">tu</td><td style="padding:8px"><b>fais</b></td><td style="padding:8px">Tu fais quoi ?</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">il / elle / on</td><td style="padding:8px"><b>fait</b></td><td style="padding:8px">Il fait beau.</td></tr>'
             '<tr><td style="padding:8px">nous</td><td style="padding:8px"><b>faisons</b></td><td style="padding:8px">Nous faisons la cuisine.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">vous</td><td style="padding:8px"><b>faites</b></td><td style="padding:8px">Vous faites du vélo ?</td></tr>'
             '<tr><td style="padding:8px">ils / elles</td><td style="padding:8px"><b>font</b></td><td style="padding:8px">Ils font leurs devoirs.</td></tr>'
             '</table>'),
            ("Pouvoir et Vouloir", "can / want to",
             '<p class="slide-explanation">Ces deux verbes modaux sont très utiles :</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse"><tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronom</th><th style="padding:8px;text-align:left">Pouvoir</th><th style="padding:8px;text-align:left">Vouloir</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">je</td><td style="padding:8px"><b>peux</b></td><td style="padding:8px"><b>veux</b></td></tr>'
             '<tr><td style="padding:8px">tu</td><td style="padding:8px"><b>peux</b></td><td style="padding:8px"><b>veux</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">il / elle</td><td style="padding:8px"><b>peut</b></td><td style="padding:8px"><b>veut</b></td></tr>'
             '<tr><td style="padding:8px">nous</td><td style="padding:8px"><b>pouvons</b></td><td style="padding:8px"><b>voulons</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">vous</td><td style="padding:8px"><b>pouvez</b></td><td style="padding:8px"><b>voulez</b></td></tr>'
             '<tr><td style="padding:8px">ils / elles</td><td style="padding:8px"><b>peuvent</b></td><td style="padding:8px"><b>veulent</b></td></tr>'
             '</table>'
             '<p style="margin-top:10px">Ils sont suivis d\'un <b>infinitif</b> : Je peux <b>venir</b>. Elle veut <b>partir</b>.</p>'),
            ("Le futur proche avec aller", None,
             '<p class="slide-explanation">On utilise <b>aller + infinitif</b> pour exprimer un futur immédiat ou planifié :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>Je <b>vais manger</b> dans cinq minutes. (I\'m going to eat)</p>'
             '<p style="margin-top:8px">Elle <b>va partir</b> demain. (She\'s going to leave)</p>'
             '<p style="margin-top:8px">Nous <b>allons visiter</b> Paris. (We\'re going to visit)</p>'
             '<p style="margin-top:8px">Ils <b>vont arriver</b> bientôt. (They\'re going to arrive)</p>'
             '</div>'
             '<p>C\'est la façon la plus courante d\'exprimer le futur en français parlé.</p>'),
        ],
        'traps': [
            ("vous faisez", "vous faites", "Faire est irrégulier : vous faites (pas faisez)."),
            ("Je vas bien.", "Je vais bien.", "Aller : je vais (pas je vas)."),
            ("ils peuvent (ils peuves)", "ils peuvent", "Pouvoir : ils peuvent (irrégulier)."),
            ("Je veux manger. / Je veux de manger.", "Je veux manger.", "Vouloir + infinitif sans préposition : je veux manger (pas de manger)."),
            ("Il va à faire du sport.", "Il va faire du sport.", "Futur proche : aller + infinitif sans préposition : il va faire."),
        ],
        'summary': [
            ("je vais / tu vas / il va", "aller singulier", "Je vais bien."),
            ("nous allons / vous allez / ils vont", "aller pluriel", "Ils vont en France."),
            ("je/tu fais / il fait / ils font", "faire présent", "Il fait beau."),
            ("je/tu peux / il peut / ils peuvent", "pouvoir présent", "Je peux venir."),
            ("je/tu veux / il veut / ils veulent", "vouloir présent", "Elle veut partir."),
            ("aller + infinitif", "futur proche", "Je vais manger."),
        ],
        'ex1': (
            "Conjugaison des verbes irréguliers",
            "Choisis la forme correcte.",
            [
                ("Tu _____ au cinéma ? (aller)", ["vais", "vas", "va", "allons"], "vas",
                 "Aller : tu vas."),
                ("Il _____ ses devoirs. (faire)", ["fais", "faites", "fait", "font"], "fait",
                 "Faire : il fait."),
                ("Vous _____ du sport ? (faire)", ["fait", "fais", "faites", "font"], "faites",
                 "Faire : vous faites (irrégulier)."),
                ("Je _____ venir ce soir. (pouvoir)", ["peux", "peut", "pouvez", "peuvent"], "peux",
                 "Pouvoir : je peux."),
                ("Ils _____ partir maintenant. (vouloir)", ["veut", "voulons", "veulent", "voulez"], "veulent",
                 "Vouloir : ils veulent."),
            ]
        ),
        'ex2': (
            "Futur proche",
            "Forme le futur proche avec aller + infinitif.",
            [
                ("Je / manger (demain)", "je vais manger", "Futur proche : je + vais + manger."),
                ("Elle / partir (ce soir)", "elle va partir", "Futur proche : elle + va + partir."),
                ("Nous / visiter (Paris)", "nous allons visiter", "Futur proche : nous + allons + visiter."),
                ("Ils / arriver (bientôt)", "ils vont arriver", "Futur proche : ils + vont + arriver."),
                ("Tu / faire (quoi ?)", "tu vas faire", "Futur proche : tu + vas + faire."),
            ]
        ),
        'ex3': (
            "Pouvoir ou Vouloir ?",
            "Choisis le bon verbe selon le contexte.",
            [
                ("J'ai la permission. &rarr; Je _____ venir.", ["peux", "veux", "vais", "fais"], "peux",
                 "Permission = pouvoir : je peux venir."),
                ("C'est mon désir. &rarr; Je _____ un café.", ["peux", "veux", "vais", "fais"], "veux",
                 "Désir = vouloir : je veux un café."),
                ("Il n'a pas la capacité. &rarr; Il ne _____ pas nager.", ["peut", "veut", "va", "fait"], "peut",
                 "Capacité = pouvoir : il ne peut pas nager."),
                ("Nous avons envie. &rarr; Nous _____ aller au restaurant.", ["pouvons", "voulons", "allons", "faisons"], "voulons",
                 "Envie = vouloir : nous voulons aller au restaurant."),
                ("Il fait beau. &rarr; On _____ faire du vélo.", ["peut", "veut", "va", "fait"], "peut",
                 "Possibilité = pouvoir : on peut faire du vélo."),
            ]
        ),
        'game_desc': "Maîtrise les verbes irréguliers essentiels : aller, faire, pouvoir, vouloir.",
        'items': [
            ('irr-01', 'je vais', 'aller à la 1re personne singulier', '1sg aller',
             'Je vais au marché ce matin.', 'Je ______ au marché ce matin.', 'vais'),
            ('irr-02', 'il va', 'aller à la 3e personne singulier', '3sg aller',
             'Il va à l\'école en vélo.', 'Il ______ à l\'école en vélo.', 'va'),
            ('irr-03', 'ils vont', 'aller à la 3e personne pluriel', '3pl aller',
             'Ils vont en vacances demain.', 'Ils ______ en vacances demain.', 'vont'),
            ('irr-04', 'je fais', 'faire à la 1re personne singulier', '1sg faire',
             'Je fais du sport le matin.', 'Je ______ du sport le matin.', 'fais'),
            ('irr-05', 'vous faites', 'faire à la 2e personne pluriel (irrégulier)', '2pl faire',
             'Vous faites quoi ce soir ?', 'Vous ______ quoi ce soir ?', 'faites'),
            ('irr-06', 'je peux', 'pouvoir à la 1re personne singulier', '1sg pouvoir',
             'Je peux t\'aider si tu veux.', 'Je ______ t\'aider si tu veux.', 'peux'),
            ('irr-07', 'je veux', 'vouloir à la 1re personne singulier', '1sg vouloir',
             'Je veux un café, s\'il vous plaît.', 'Je ______ un café, s\'il vous plaît.', 'veux'),
            ('irr-08', 'futur proche', 'aller + infinitif = futur immédiat', 'aller + inf.',
             'Je vais manger dans cinq minutes.', 'Je vais ______ dans cinq minutes.', 'manger'),
        ],
    },

    'les-questions': {
        'level': 'a1',
        'section': 'grammaire',
        'num': 'G10',
        'short': 'Les Questions',
        'title': 'Les Questions — Comment Interroger en Français',
        'subtitle': "Trois façons de poser une question et les mots interrogatifs essentiels",
        'slides': [
            ("Trois façons de poser une question", None,
             '<p class="slide-explanation">En français, il y a <b>trois façons</b> de former une question :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>1. Intonation montante (oral) :</b> Tu parles français <b>?</b></p>'
             '<p style="margin-top:8px"><b>2. Est-ce que (neutre) :</b> <b>Est-ce que</b> tu parles français ?</p>'
             '<p style="margin-top:8px"><b>3. Inversion (formel) :</b> Parles-<b>tu</b> français ?</p>'
             '</div>'
             '<p style="margin-top:12px">À l\'A1, les deux premières structures sont les plus importantes. L\'inversion est plus formelle.</p>'),
            ("Les mots interrogatifs", None,
             '<p class="slide-explanation">Les mots interrogatifs (question words) :</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse"><tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Mot</th><th style="padding:8px;text-align:left">Sens</th><th style="padding:8px;text-align:left">Exemple</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>qui</b></td><td style="padding:8px">who</td><td style="padding:8px">Qui est là ?</td></tr>'
             '<tr><td style="padding:8px"><b>que / qu\'</b></td><td style="padding:8px">what</td><td style="padding:8px">Qu\'est-ce que tu fais ?</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>où</b></td><td style="padding:8px">where</td><td style="padding:8px">Où habites-tu ?</td></tr>'
             '<tr><td style="padding:8px"><b>quand</b></td><td style="padding:8px">when</td><td style="padding:8px">Quand arrives-tu ?</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>comment</b></td><td style="padding:8px">how</td><td style="padding:8px">Comment tu t\'appelles ?</td></tr>'
             '<tr><td style="padding:8px"><b>pourquoi</b></td><td style="padding:8px">why</td><td style="padding:8px">Pourquoi tu ris ?</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>combien (de)</b></td><td style="padding:8px">how much / many</td><td style="padding:8px">Combien ça coûte ?</td></tr>'
             '<tr><td style="padding:8px"><b>quel(le)</b></td><td style="padding:8px">which / what</td><td style="padding:8px">Quel âge as-tu ?</td></tr>'
             '</table>'),
            ("Qu'est-ce que vs Qui est-ce qui", None,
             '<p class="slide-explanation">Les deux expressions les plus courantes pour les questions :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Qu\'est-ce que</b> + sujet + verbe &rarr; demande l\'objet d\'une action</p>'
             '<p>Qu\'est-ce que tu <b>manges</b> ? (What are you eating?)</p>'
             '<p style="margin-top:12px"><b>Qui est-ce qui</b> + verbe &rarr; demande le sujet (une personne)</p>'
             '<p>Qui est-ce qui <b>parle</b> ? (Who is speaking?)</p>'
             '<p style="margin-top:12px">À l\'oral : on dit souvent simplement <b>C\'est qui ?</b> ou <b>Tu fais quoi ?</b></p>'
             '</div>'),
            ("Quel / Quelle", None,
             '<p class="slide-explanation"><b>Quel</b> s\'accorde avec le nom qui suit :</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse"><tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left"></th><th style="padding:8px;text-align:left">Masculin</th><th style="padding:8px;text-align:left">Féminin</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Singulier</td><td style="padding:8px"><b>quel</b> âge</td><td style="padding:8px"><b>quelle</b> heure</td></tr>'
             '<tr><td style="padding:8px">Pluriel</td><td style="padding:8px"><b>quels</b> films</td><td style="padding:8px"><b>quelles</b> langues</td></tr>'
             '</table>'
             '<p style="margin-top:12px">Exemples : <b>Quel</b> âge as-tu ? &mdash; <b>Quelle</b> heure est-il ? &mdash; <b>Quelles</b> langues tu parles ?</p>'),
        ],
        'traps': [
            ("Comment t'appelles tu ?", "Comment tu t'appelles ?", "À l'oral familier, on dit comment tu t'appelles ? À l'écrit formel : Comment t'appelles-tu ?"),
            ("Où est-ce que tu habites-tu ?", "Où est-ce que tu habites ?", "Ne mélange pas est-ce que et l'inversion (-tu) dans la même question."),
            ("Quel heure est-il ?", "Quelle heure est-il ?", "Heure est féminin : quelle heure (pas quel heure)."),
            ("Pourquoi tu ne viens pas ?", "Pourquoi tu ne viens pas ? ✓", "Cette structure (intonation) est correcte à l'oral. À l'écrit : Pourquoi ne viens-tu pas ?"),
            ("Combien coûte ça ? (Combien ça coûte-t-il ?)", "Combien ça coûte ?", "À l'oral : combien ça coûte ? (intonation). Le -t-il est formel/écrit."),
        ],
        'summary': [
            ("intonation ?", "question orale simple", "Tu viens ?"),
            ("est-ce que", "question neutre", "Est-ce que tu viens ?"),
            ("inversion", "formel/écrit", "Viens-tu ?"),
            ("qui / que / où", "who / what / where", "Qui est là ? Où vas-tu ?"),
            ("quand / comment / pourquoi", "when / how / why", "Quand arrives-tu ?"),
            ("quel(le)(s)", "which / what (accordé)", "Quel âge ? Quelle heure ?"),
        ],
        'ex1': (
            "Quel mot interrogatif ?",
            "Choisis le bon mot interrogatif.",
            [
                ("_____ habites-tu ? (where)", ["Qui", "Où", "Quand", "Comment"], "Où",
                 "Where = où : Où habites-tu ?"),
                ("_____ est-ce que tu fais ? (what)", ["Qui", "Où", "Qu'", "Quand"], "Qu'",
                 "What = que/qu' : Qu'est-ce que tu fais ?"),
                ("_____ parle ? (who)", ["Qui", "Que", "Quand", "Comment"], "Qui",
                 "Who = qui : Qui parle ?"),
                ("_____ tu t'appelles ? (how)", ["Où", "Quand", "Comment", "Pourquoi"], "Comment",
                 "How = comment : Comment tu t'appelles ?"),
                ("_____ ça coûte ? (how much)", ["Pourquoi", "Combien", "Quand", "Quel"], "Combien",
                 "How much = combien : Combien ça coûte ?"),
            ]
        ),
        'ex2': (
            "Quel ou Quelle ?",
            "Écris la bonne forme de quel.",
            [
                ("_____ âge as-tu ?", "Quel", "Âge est masculin : quel âge."),
                ("_____ heure est-il ?", "Quelle", "Heure est féminin : quelle heure."),
                ("_____ langues tu parles ?", "Quelles", "Langues est féminin pluriel : quelles langues."),
                ("_____ est ton prénom ?", "Quel", "Prénom est masculin : quel prénom."),
                ("_____ films tu aimes ?", "Quels", "Films est masculin pluriel : quels films."),
            ]
        ),
        'ex3': (
            "Forme la question",
            "Choisis la question correcte pour la réponse donnée.",
            [
                ("Réponse : Je m'appelle Marie.", ["Comment tu t'appelles ?", "Où tu habites ?", "Qui est là ?", "Quand tu pars ?"], "Comment tu t'appelles ?",
                 "La réponse donne un prénom → question avec comment (comment tu t'appelles ?)."),
                ("Réponse : J'habite à Lyon.", ["Comment tu t'appelles ?", "Où tu habites ?", "Quand tu arrives ?", "Pourquoi tu pars ?"], "Où tu habites ?",
                 "La réponse donne un lieu → question avec où."),
                ("Réponse : J'ai 22 ans.", ["Où tu habites ?", "Quel âge as-tu ?", "Quand tu pars ?", "Comment tu vas ?"], "Quel âge as-tu ?",
                 "La réponse donne un âge → quel âge."),
                ("Réponse : Parce que j'aime la culture.", ["Combien ça coûte ?", "Quand tu pars ?", "Pourquoi tu apprends le français ?", "Qui est là ?"], "Pourquoi tu apprends le français ?",
                 "La réponse commence par parce que → question avec pourquoi."),
                ("Réponse : Je pars demain.", ["Qui parle ?", "Où vas-tu ?", "Quand tu pars ?", "Comment tu t'appelles ?"], "Quand tu pars ?",
                 "La réponse donne un temps → question avec quand."),
            ]
        ),
        'game_desc': "Entraîne-toi sur les mots interrogatifs et les formes de questions en français.",
        'items': [
            ('q-01', 'où', 'mot interrogatif : where', 'where',
             'Où habites-tu ?', '______ habites-tu ?', 'Où'),
            ('q-02', 'quand', 'mot interrogatif : when', 'when',
             'Quand arrives-tu ?', '______ arrives-tu ?', 'Quand'),
            ('q-03', 'comment', 'mot interrogatif : how', 'how',
             'Comment tu t\'appelles ?', '______ tu t\'appelles ?', 'Comment'),
            ('q-04', 'pourquoi', 'mot interrogatif : why', 'why',
             'Pourquoi tu ris ?', '______ tu ris ?', 'Pourquoi'),
            ('q-05', 'combien', 'mot interrogatif : how much / how many', 'how much',
             'Combien ça coûte ?', '______ ça coûte ?', 'Combien'),
            ('q-06', 'quel / quelle', 'adjectif interrogatif accordé avec le nom', 'which',
             'Quel âge as-tu ?', '______ âge as-tu ?', 'Quel'),
            ('q-07', 'est-ce que', 'structure neutre pour former une question', 'est-ce que',
             'Est-ce que tu parles français ?', '______ tu parles français ?', 'Est-ce que'),
            ('q-08', "qu'est-ce que", "demander l'objet d'une action", "what (objet)",
             "Qu'est-ce que tu manges ?", "______ tu manges ?", "Qu'est-ce que"),
        ],
    },

    'les-prepositions': {
        'level': 'a1',
        'section': 'grammaire',
        'num': 'G11',
        'short': 'Les Prépositions',
        'title': 'Les Prépositions — En, À, De, Dans, Sur...',
        'subtitle': "Apprends les prépositions essentielles pour situer et relier des éléments",
        'slides': [
            ("Les prépositions de lieu", None,
             '<p class="slide-explanation">Les prépositions de lieu indiquent la <b>position</b> ou la <b>direction</b> :</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse"><tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Préposition</th><th style="padding:8px;text-align:left">Sens</th><th style="padding:8px;text-align:left">Exemple</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>dans</b></td><td style="padding:8px">in (inside)</td><td style="padding:8px">dans la boîte</td></tr>'
             '<tr><td style="padding:8px"><b>sur</b></td><td style="padding:8px">on</td><td style="padding:8px">sur la table</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>sous</b></td><td style="padding:8px">under</td><td style="padding:8px">sous le lit</td></tr>'
             '<tr><td style="padding:8px"><b>devant</b></td><td style="padding:8px">in front of</td><td style="padding:8px">devant la maison</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>derrière</b></td><td style="padding:8px">behind</td><td style="padding:8px">derrière le rideau</td></tr>'
             '<tr><td style="padding:8px"><b>entre</b></td><td style="padding:8px">between</td><td style="padding:8px">entre les deux</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>à côté de</b></td><td style="padding:8px">next to</td><td style="padding:8px">à côté de l\'école</td></tr>'
             '</table>'),
            ("À et En — pays et villes", None,
             '<p class="slide-explanation"><b>À</b> et <b>en</b> s\'utilisent avec les pays et les villes, mais pas de la même façon :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>À</b> + ville : Je suis <b>à</b> Paris. Elle va <b>à</b> Lyon.</p>'
             '<p style="margin-top:8px"><b>En</b> + pays féminin : Je suis <b>en</b> France. Il habite <b>en</b> Espagne.</p>'
             '<p style="margin-top:8px"><b>Au</b> + pays masculin : Je vais <b>au</b> Portugal. Elle est <b>au</b> Mexique.</p>'
             '<p style="margin-top:8px"><b>Aux</b> + pays pluriel : Nous allons <b>aux</b> États-Unis.</p>'
             '</div>'
             '<p>La plupart des pays en <b>-e</b> sont féminins (France, Espagne, Chine...).</p>'),
            ("De — origine et possession", None,
             '<p class="slide-explanation"><b>De</b> est une préposition très fréquente :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Origine :</b> Je suis <b>de</b> Lyon. Elle vient <b>de</b> Paris.</p>'
             '<p style="margin-top:8px"><b>Possession :</b> le livre <b>de</b> Marie, la maison <b>du</b> prof (de + le = du)</p>'
             '<p style="margin-top:8px"><b>Matière :</b> une table <b>en</b> bois, un sac <b>en</b> cuir</p>'
             '<p style="margin-top:8px"><b>De + pays féminin :</b> Je viens <b>de</b> France. Il vient <b>d\'</b>Espagne.</p>'
             '<p style="margin-top:8px"><b>Du + pays masculin :</b> Je viens <b>du</b> Japon.</p>'
             '</div>'),
            ("Contractions : au et du", None,
             '<p class="slide-explanation">En français, <b>à + le = au</b> et <b>de + le = du</b>. Ces contractions sont obligatoires :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>à + le marché &rarr; <b>au</b> marché ✓ (pas à le marché)</p>'
             '<p style="margin-top:8px">de + le prof &rarr; le livre <b>du</b> prof ✓ (pas de le prof)</p>'
             '<p style="margin-top:8px">à + la gare &rarr; <b>à la</b> gare ✓ (pas de contraction)</p>'
             '<p style="margin-top:8px">de + la gare &rarr; <b>de la</b> gare ✓ (pas de contraction)</p>'
             '<p style="margin-top:8px">à + l\'école &rarr; <b>à l\'</b>école ✓ (pas de contraction)</p>'
             '</div>'),
        ],
        'traps': [
            ("Je suis à France.", "Je suis en France.", "Avec les pays féminins, on utilise en (pas à) : en France."),
            ("Je viens de le marché.", "Je viens du marché.", "De + le = du (contraction obligatoire)."),
            ("Je vais à le parc.", "Je vais au parc.", "À + le = au (contraction obligatoire)."),
            ("Le livre de la Marie.", "Le livre de Marie.", "Pas d'article devant un prénom : le livre de Marie."),
            ("Il est en Portugal.", "Il est au Portugal.", "Portugal est masculin : au Portugal (pas en Portugal)."),
        ],
        'summary': [
            ("à + ville", "location in a city", "à Paris, à Lyon"),
            ("en + pays féminin", "in a feminine country", "en France, en Espagne"),
            ("au + pays masculin", "in a masculine country", "au Japon, au Mexique"),
            ("à + le = au", "contraction obligatoire", "au marché, au parc"),
            ("de + le = du", "contraction obligatoire", "du prof, du Japon"),
            ("dans / sur / sous", "in / on / under", "dans la boîte, sur la table"),
        ],
        'ex1': (
            "Quelle préposition ?",
            "Choisis la bonne préposition.",
            [
                ("Le chat est _____ la table.", ["sur", "sous", "dans", "devant"], "sur",
                 "Sur = on : le chat est sur la table."),
                ("Je vais _____ Paris ce week-end.", ["en", "au", "à", "de"], "à",
                 "Avec une ville, on utilise à : je vais à Paris."),
                ("Elle habite _____ France.", ["à", "au", "de", "en"], "en",
                 "France est un pays féminin : en France."),
                ("Le livre est _____ la boîte.", ["sur", "sous", "dans", "devant"], "dans",
                 "Dans = in (inside) : le livre est dans la boîte."),
                ("Il vient _____ Japon.", ["de", "du", "en", "au"], "du",
                 "Japon est masculin : venir du Japon (de + le = du)."),
            ]
        ),
        'ex2': (
            "Au, du, à la, de la ?",
            "Complète avec la bonne forme.",
            [
                ("Je vais _____ marché.", "au", "À + le marché = au marché."),
                ("Le sac _____ professeur est sur la chaise.", "du", "De + le professeur = du professeur."),
                ("Elle arrive _____ gare dans une heure.", "à la", "Gare est féminin : à la gare (pas de contraction)."),
                ("Je viens _____ bibliothèque.", "de la", "Bibliothèque est féminin : de la bibliothèque."),
                ("Il va _____ cinéma ce soir.", "au", "À + le cinéma = au cinéma."),
            ]
        ),
        'ex3': (
            "Prépositions de lieu",
            "Choisis la bonne préposition de lieu.",
            [
                ("Le stylo est _____ le livre. (under)", ["sur", "sous", "dans", "devant"], "sous",
                 "Under = sous : le stylo est sous le livre."),
                ("Le supermarché est _____ la boulangerie. (next to)", ["devant", "derrière", "à côté de", "entre"], "à côté de",
                 "Next to = à côté de."),
                ("La pharmacie est _____ la mairie et la poste. (between)", ["à côté de", "devant", "entre", "derrière"], "entre",
                 "Between = entre : entre la mairie et la poste."),
                ("Il y a une voiture _____ la maison. (in front of)", ["derrière", "devant", "sur", "dans"], "devant",
                 "In front of = devant : devant la maison."),
                ("Les clés sont _____ le tiroir. (in)", ["sur", "sous", "dans", "devant"], "dans",
                 "In (inside) = dans : dans le tiroir."),
            ]
        ),
        'game_desc': "Entraîne-toi sur les prépositions essentielles du français.",
        'items': [
            ('prep-01', 'à', 'préposition de lieu pour les villes', 'ville',
             'Je suis à Paris.', 'Je suis ______ Paris.', 'à'),
            ('prep-02', 'en', 'préposition pour les pays féminins', 'pays fém.',
             'Elle habite en France.', 'Elle habite ______ France.', 'en'),
            ('prep-03', 'au', 'à + le (contraction) — pays masculins', 'à + le',
             'Il va au Japon.', 'Il va ______ Japon.', 'au'),
            ('prep-04', 'du', 'de + le (contraction)', 'de + le',
             'Le livre du professeur est là.', 'Le livre ______ professeur est là.', 'du'),
            ('prep-05', 'dans', 'in (à l\'intérieur)', 'in',
             'Le chat est dans la boîte.', 'Le chat est ______ la boîte.', 'dans'),
            ('prep-06', 'sur', 'on (en contact avec une surface)', 'on',
             'Le verre est sur la table.', 'Le verre est ______ la table.', 'sur'),
            ('prep-07', 'sous', 'under (en dessous)', 'under',
             'Le chien dort sous le lit.', 'Le chien dort ______ le lit.', 'sous'),
            ('prep-08', 'de', 'origine ou possession', 'from / of',
             'Je viens de Lyon.', 'Je viens ______ Lyon.', 'de'),
        ],
    },

    'les-nombres': {
        'level': 'a1',
        'section': 'grammaire',
        'num': 'G12',
        'short': 'Les Nombres',
        'title': 'Les Nombres — Cardinaux et Ordinaux',
        'subtitle': "Apprends à compter et à utiliser les nombres en français",
        'slides': [
            ("Les nombres de 0 à 20", None,
             '<p class="slide-explanation">Les nombres de <b>0 à 20</b> sont à mémoriser :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;font-size:.88rem">'
             '<div><b>0</b> zéro</div><div><b>1</b> un</div><div><b>2</b> deux</div>'
             '<div><b>3</b> trois</div><div><b>4</b> quatre</div><div><b>5</b> cinq</div>'
             '<div><b>6</b> six</div><div><b>7</b> sept</div><div><b>8</b> huit</div>'
             '<div><b>9</b> neuf</div><div><b>10</b> dix</div><div><b>11</b> onze</div>'
             '<div><b>12</b> douze</div><div><b>13</b> treize</div><div><b>14</b> quatorze</div>'
             '<div><b>15</b> quinze</div><div><b>16</b> seize</div><div><b>17</b> dix-sept</div>'
             '<div><b>18</b> dix-huit</div><div><b>19</b> dix-neuf</div><div><b>20</b> vingt</div>'
             '</div>'),
            ("Les dizaines : 20 à 100", None,
             '<p class="slide-explanation">Les dizaines en français — attention à 70, 80 et 90 !</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse"><tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Nombre</th><th style="padding:8px;text-align:left">Français</th><th style="padding:8px;text-align:left">Logique</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">20</td><td style="padding:8px"><b>vingt</b></td><td style="padding:8px">—</td></tr>'
             '<tr><td style="padding:8px">30</td><td style="padding:8px"><b>trente</b></td><td style="padding:8px">—</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">40</td><td style="padding:8px"><b>quarante</b></td><td style="padding:8px">—</td></tr>'
             '<tr><td style="padding:8px">50</td><td style="padding:8px"><b>cinquante</b></td><td style="padding:8px">—</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">60</td><td style="padding:8px"><b>soixante</b></td><td style="padding:8px">—</td></tr>'
             '<tr><td style="padding:8px">70</td><td style="padding:8px"><b>soixante-dix</b></td><td style="padding:8px">60 + 10</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">80</td><td style="padding:8px"><b>quatre-vingts</b></td><td style="padding:8px">4 × 20</td></tr>'
             '<tr><td style="padding:8px">90</td><td style="padding:8px"><b>quatre-vingt-dix</b></td><td style="padding:8px">4 × 20 + 10</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">100</td><td style="padding:8px"><b>cent</b></td><td style="padding:8px">—</td></tr>'
             '</table>'),
            ("Les nombres composés : 21 à 99", None,
             '<p class="slide-explanation">Pour les nombres entre les dizaines, on ajoute un trait d\'union :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>21</b> : vingt et <b>un</b> (avec "et")</p>'
             '<p style="margin-top:8px"><b>22</b> : vingt-<b>deux</b> (avec trait d\'union)</p>'
             '<p style="margin-top:8px"><b>71</b> : soixante et <b>onze</b></p>'
             '<p style="margin-top:8px"><b>72</b> : soixante-<b>douze</b></p>'
             '<p style="margin-top:8px"><b>81</b> : quatre-vingt-<b>un</b></p>'
             '<p style="margin-top:8px"><b>91</b> : quatre-vingt-<b>onze</b></p>'
             '</div>'
             '<p>Note : 80 = quatre-vingt<b>s</b> (avec s), mais 81 = quatre-vingt-un (sans s).</p>'),
            ("Les nombres ordinaux", None,
             '<p class="slide-explanation">Les nombres ordinaux (1er, 2e, 3e...) :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px;display:grid;grid-template-columns:1fr 1fr;gap:8px">'
             '<div><b>1er/1re</b> premier / première</div><div><b>2e</b> deuxième</div>'
             '<div><b>3e</b> troisième</div><div><b>4e</b> quatrième</div>'
             '<div><b>5e</b> cinquième</div><div><b>6e</b> sixième</div>'
             '<div><b>7e</b> septième</div><div><b>10e</b> dixième</div>'
             '</div>'
             '<p style="margin-top:12px">Règle générale : nombre cardinal + <b>-ième</b> (deuxième, troisième...).</p>'
             '<p>Exception : 1er premier / 1re première.</p>'),
        ],
        'traps': [
            ("septante", "soixante-dix", "En France, 70 = soixante-dix (pas septante, qui est utilisé en Belgique et Suisse)."),
            ("huitante / octante", "quatre-vingts", "En France, 80 = quatre-vingts (pas huitante ni octante)."),
            ("quatre-vingt-un (quatre-vingts un)", "quatre-vingt-un", "Devant un autre nombre, quatre-vingts perd son -s : quatre-vingt-un."),
            ("vingt-et-deux", "vingt-deux", "Et ne s'utilise qu'avec les unités 1 : vingt et un, trente et un, etc. Pour les autres : vingt-deux."),
            ("le deuxième étage (2ème)", "le deuxième étage ✓", "Cette phrase est correcte. 2ème et 2e sont tous les deux acceptés en abréviation."),
        ],
        'summary': [
            ("1–16", "formes propres", "un, deux, trois... seize"),
            ("17–19", "dix + unité", "dix-sept, dix-huit, dix-neuf"),
            ("70", "soixante-dix", "60 + 10"),
            ("80", "quatre-vingts", "4 × 20"),
            ("90", "quatre-vingt-dix", "4 × 20 + 10"),
            ("ordinaux", "cardinal + -ième", "deuxième, troisième..."),
        ],
        'ex1': (
            "Comment dit-on ?",
            "Choisis le bon nombre en lettres.",
            [
                ("17 en français", ["dix-sept", "septième", "dix-suite", "sèptante"], "dix-sept",
                 "17 = dix-sept (10 + 7)."),
                ("70 en français", ["septante", "soixante-dix", "soixante-douze", "quatre-vingts"], "soixante-dix",
                 "70 = soixante-dix (60 + 10). En France, pas septante."),
                ("80 en français", ["huitante", "soixante-vingt", "quatre-vingts", "octante"], "quatre-vingts",
                 "80 = quatre-vingts (4 × 20). Avec -s car pas de nombre après."),
                ("90 en français", ["nonante", "quatre-vingt-dix", "soixante-trente", "quatre-vingts-dix"], "quatre-vingt-dix",
                 "90 = quatre-vingt-dix (4 × 20 + 10). Sans -s car suivi de dix."),
                ("21 en français", ["vingt-un", "vingt et un", "vingt-et-un", "vingt et une"], "vingt et un",
                 "21 = vingt et un. On écrit et sans trait d'union pour les -un."),
            ]
        ),
        'ex2': (
            "Les ordinaux",
            "Donne l'ordinal en lettres.",
            [
                ("1er (masculin)", "premier", "1er masculin = premier."),
                ("2e", "deuxième", "2e = deuxième."),
                ("3e", "troisième", "3e = troisième."),
                ("5e", "cinquième", "5e = cinquième."),
                ("1re (féminin)", "première", "1re féminin = première."),
            ]
        ),
        'ex3': (
            "Calcul et nombres",
            "Choisis le bon résultat.",
            [
                ("20 + 15 = ?", ["trente-cinq", "vingt-cinq", "quarante", "soixante"], "trente-cinq",
                 "20 + 15 = 35 = trente-cinq."),
                ("60 + 11 = ?", ["soixante-onze", "soixante-et-onze", "soixante-onze", "septante-et-un"], "soixante-onze",
                 "60 + 11 = 71 = soixante et onze."),
                ("4 × 20 + 5 = ?", ["quatre-vingt-cinq", "soixante-quinze", "quatre-vingt-quatre", "quatre-vingts-cinq"], "quatre-vingt-cinq",
                 "4 × 20 + 5 = 85 = quatre-vingt-cinq (sans -s car suivi d'un nombre)."),
                ("50 + 13 = ?", ["soixante-cinq", "soixante-trois", "cinquante-treize", "soixante-treize"], "soixante-treize",
                 "50 + 13 = 63 = soixante-trois. Attention : 73 = soixante-treize."),
                ("100 en français ?", ["cent", "cents", "cen", "centième"], "cent",
                 "100 = cent (sans -s car il n'est pas multiplié)."),
            ]
        ),
        'game_desc': "Entraîne-toi sur les nombres cardinaux et ordinaux en français.",
        'items': [
            ('nb-01', 'soixante-dix', '70 en français (60 + 10)', '70',
             'Il a soixante-dix ans.', 'Il a ______ ans.', 'soixante-dix'),
            ('nb-02', 'quatre-vingts', '80 en français (4 × 20)', '80',
             'Il y a quatre-vingts élèves dans l\'école.', 'Il y a ______ élèves dans l\'école.', 'quatre-vingts'),
            ('nb-03', 'quatre-vingt-dix', '90 en français (4 × 20 + 10)', '90',
             'Elle a quatre-vingt-dix ans.', 'Elle a ______ ans.', 'quatre-vingt-dix'),
            ('nb-04', 'vingt et un', '21 en français', '21',
             'Il y a vingt et un jours.', 'Il y a ______ jours.', 'vingt et un'),
            ('nb-05', 'soixante et onze', '71 en français (60 + 11)', '71',
             'Mon grand-père a soixante et onze ans.', 'Mon grand-père a ______ ans.', 'soixante et onze'),
            ('nb-06', 'premier / première', 'ordinal 1er/1re', '1er',
             'C\'est le premier jour du mois.', 'C\'est le ______ jour du mois.', 'premier'),
            ('nb-07', 'deuxième', 'ordinal 2e', '2e',
             'Elle habite au deuxième étage.', 'Elle habite au ______ étage.', 'deuxième'),
            ('nb-08', 'cent', '100 en français', '100',
             'Il y a cent personnes dans la salle.', 'Il y a ______ personnes dans la salle.', 'cent'),
        ],
    },
}
