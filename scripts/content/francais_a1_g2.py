"""French A1 Grammar — Batch 2: présent -ER, avoir, il y a, adjectifs."""

CHAPTERS = {
    'le-present-er': {
        'level': 'a1',
        'section': 'grammaire',
        'num': 'G05',
        'short': 'Le Présent en -ER',
        'title': 'Le Présent des Verbes en -ER',
        'subtitle': "Conjugue les verbes réguliers en -ER au présent de l'indicatif",
        'slides': [
            ("Les verbes en -ER : la règle", None,
             '<p class="slide-explanation">Les verbes en <b>-ER</b> sont les plus nombreux en français. Ils se conjuguent selon un modèle régulier. On retire le <b>-ER</b> de l\'infinitif pour obtenir le radical, puis on ajoute les terminaisons :</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse"><tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronom</th><th style="padding:8px;text-align:left">Terminaison</th><th style="padding:8px;text-align:left">Exemple : parler</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">je</td><td style="padding:8px"><b>-e</b></td><td style="padding:8px">je parl<b>e</b></td></tr>'
             '<tr><td style="padding:8px">tu</td><td style="padding:8px"><b>-es</b></td><td style="padding:8px">tu parl<b>es</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">il / elle / on</td><td style="padding:8px"><b>-e</b></td><td style="padding:8px">il parl<b>e</b></td></tr>'
             '<tr><td style="padding:8px">nous</td><td style="padding:8px"><b>-ons</b></td><td style="padding:8px">nous parl<b>ons</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">vous</td><td style="padding:8px"><b>-ez</b></td><td style="padding:8px">vous parl<b>ez</b></td></tr>'
             '<tr><td style="padding:8px">ils / elles</td><td style="padding:8px"><b>-ent</b></td><td style="padding:8px">ils parl<b>ent</b></td></tr>'
             '</table>'),
            ("Verbes courants en -ER", None,
             '<p class="slide-explanation">Voici les verbes en -ER les plus utilisés en français A1 :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px;display:grid;grid-template-columns:1fr 1fr;gap:8px">'
             '<div><b>parler</b> — to speak</div><div><b>aimer</b> — to like/love</div>'
             '<div><b>habiter</b> — to live</div><div><b>travailler</b> — to work</div>'
             '<div><b>écouter</b> — to listen</div><div><b>regarder</b> — to watch</div>'
             '<div><b>manger</b> — to eat</div><div><b>chercher</b> — to look for</div>'
             '<div><b>donner</b> — to give</div><div><b>arriver</b> — to arrive</div>'
             '</div>'
             '<p style="margin-top:12px">Exemples : <b>J\'aime</b> le café. <b>Nous habitons</b> à Paris. <b>Il travaille</b> beaucoup.</p>'),
            ("Particularités orthographiques", None,
             '<p class="slide-explanation">Quelques verbes en -ER ont des petites irrégularités orthographiques :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>manger</b> : nous mang<b>e</b>ons (on garde le e pour conserver le son [ʒ])</p>'
             '<p style="margin-top:8px"><b>commencer</b> : nous commenc<b>ons</b> (c→ç pour conserver le son [s])</p>'
             '<p style="margin-top:8px"><b>s\'appeler</b> : je m\'appell<b>e</b>, tu t\'appell<b>es</b> (doublement du l)</p>'
             '<p style="margin-top:8px"><b>préférer</b> : je préf<b>è</b>re (é→è devant syllabe muette)</p>'
             '</div>'
             '<p>Ces changements sont réguliers et suivent des règles phonétiques.</p>'),
            ("Emplois du présent", None,
             '<p class="slide-explanation">Le présent de l\'indicatif exprime :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>1. Une action en cours :</b> Je lis un livre en ce moment.</p>'
             '<p style="margin-top:8px"><b>2. Une habitude :</b> Il mange à midi tous les jours.</p>'
             '<p style="margin-top:8px"><b>3. Une vérité générale :</b> L\'eau bout à 100 degrés.</p>'
             '<p style="margin-top:8px"><b>4. Un futur proche (avec marqueur) :</b> Demain, elle arrive à 8h.</p>'
             '</div>'),
        ],
        'traps': [
            ("ils parlent (ils parle)", "ils parlent", "La terminaison -ent de la 3e personne du pluriel est muette : on ne la prononce pas."),
            ("nous mangeons (nous mangons)", "nous mangeons", "Manger garde le e avant -ons pour préserver le son [ʒ] : nous mangeons."),
            ("je parles", "je parle", "À la 1re personne singulier, la terminaison est -e (sans s) : je parle."),
            ("vous parlez (vous parlais)", "vous parlez", "Le présent de vous est -ez, pas une terminaison du passé."),
            ("il travail", "il travaille", "L'infinitif travailler → radical travaill- → il travaille (avec -e final muet)."),
        ],
        'summary': [
            ("je / il / elle", "-e (muet)", "je parle, il arrive"),
            ("tu", "-es (muet)", "tu parles, tu aimes"),
            ("nous", "-ons", "nous parlons, nous mangeons"),
            ("vous", "-ez", "vous parlez, vous regardez"),
            ("ils / elles", "-ent (muet)", "ils parlent, elles écoutent"),
            ("radical", "infinitif sans -ER", "parler → parl-"),
        ],
        'ex1': (
            "Conjugaison au présent",
            "Choisis la forme correcte du verbe en -ER.",
            [
                ("Je _____ français. (parler)", ["parle", "parles", "parlons", "parlent"], "parle",
                 "Je → terminaison -e : je parle."),
                ("Tu _____ à Paris ? (habiter)", ["habite", "habites", "habitons", "habitez"], "habites",
                 "Tu → terminaison -es : tu habites."),
                ("Elle _____ le piano. (jouer)", ["joue", "joues", "jouons", "jouent"], "joue",
                 "Elle → terminaison -e : elle joue."),
                ("Nous _____ à midi. (manger)", ["mangeons", "mangons", "mangez", "mangent"], "mangeons",
                 "Nous + manger → mangeons (on garde le e : nous mangeons)."),
                ("Ils _____ la télé. (regarder)", ["regarde", "regardes", "regardons", "regardent"], "regardent",
                 "Ils → terminaison -ent : ils regardent."),
            ]
        ),
        'ex2': (
            "Conjuguer au présent",
            "Écris la bonne forme du verbe entre parenthèses.",
            [
                ("Vous _____ bien l'anglais. (parler)", "parlez", "Vous → terminaison -ez : vous parlez."),
                ("On _____ un café ? (chercher)", "cherche", "On → terminaison -e : on cherche."),
                ("Elles _____ en Espagne. (habiter)", "habitent", "Elles → terminaison -ent : elles habitent."),
                ("Tu _____ la musique ? (écouter)", "écoutes", "Tu → terminaison -es : tu écoutes."),
                ("Il _____ beaucoup. (travailler)", "travaille", "Il → terminaison -e : il travaille."),
            ]
        ),
        'ex3': (
            "Radical + terminaison",
            "Choisis la bonne forme.",
            [
                ("Je _____ le français. (aimer)", ["aime", "aimes", "aimons", "aimez"], "aime",
                 "Je → -e : j'aime (avec élision de je devant voyelle)."),
                ("Nous _____ en ville. (arriver)", ["arrive", "arrivons", "arrivez", "arrivent"], "arrivons",
                 "Nous → -ons : nous arrivons."),
                ("Vous _____ du café ? (vouloir — irrég.)", ["voulez", "voulons", "veulent", "veux"], "voulez",
                 "Vouloir est irrégulier mais vous → -ez reste : vous voulez."),
                ("Tu _____ comment ? (s'appeler)", ["appelles", "t'appelles", "appele", "appelles"], "t'appelles",
                 "S'appeler est pronominal : tu t'appelles. Et doublement du l."),
                ("Ils _____ de la musique. (écouter)", ["écoute", "écoutes", "écoutons", "écoutent"], "écoutent",
                 "Ils → -ent : ils écoutent."),
            ]
        ),
        'game_desc': "Entraîne-toi sur la conjugaison des verbes réguliers en -ER au présent.",
        'items': [
            ('er-01', 'je parle', 'verbe en -ER à la 1re personne singulier', '1sg -e',
             'Je parle français tous les jours.', 'Je ______ français tous les jours.', 'parle'),
            ('er-02', 'tu parles', 'verbe en -ER à la 2e personne singulier', '2sg -es',
             'Tu parles très vite !', 'Tu ______ très vite !', 'parles'),
            ('er-03', 'il parle', 'verbe en -ER à la 3e personne singulier', '3sg -e',
             'Il parle à son ami au téléphone.', 'Il ______ à son ami au téléphone.', 'parle'),
            ('er-04', 'nous parlons', 'verbe en -ER à la 1re personne pluriel', '1pl -ons',
             'Nous parlons de notre voyage.', 'Nous ______ de notre voyage.', 'parlons'),
            ('er-05', 'vous parlez', 'verbe en -ER à la 2e personne pluriel', '2pl -ez',
             'Vous parlez trop vite pour moi.', 'Vous ______ trop vite pour moi.', 'parlez'),
            ('er-06', 'ils parlent', 'verbe en -ER à la 3e personne pluriel (-ent muet)', '3pl -ent',
             'Ils parlent ensemble dans le couloir.', 'Ils ______ ensemble dans le couloir.', 'parlent'),
            ('er-07', 'nous mangeons', 'manger : nous mangeons (e conservé)', 'orthographe',
             'Nous mangeons à midi.', 'Nous ______ à midi.', 'mangeons'),
            ('er-08', "j'aime", "élision de je devant voyelle + conjugaison -e", "élision + -e",
             "J'aime beaucoup le cinéma.", "J'______ beaucoup le cinéma.", 'aime'),
        ],
    },

    'le-verbe-avoir': {
        'level': 'a1',
        'section': 'grammaire',
        'num': 'G06',
        'short': 'Le Verbe Avoir',
        'title': 'Le Verbe Avoir — Conjugaison et Emplois',
        'subtitle': "Maîtrise le verbe avoir : possession, âge et expressions idiomatiques",
        'slides': [
            ("Le verbe avoir au présent", "Conjugaison complète",
             '<p class="slide-explanation">Le verbe <b>avoir</b> est irrégulier. Sa conjugaison au présent :</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse"><tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronom</th><th style="padding:8px;text-align:left">Avoir</th><th style="padding:8px;text-align:left">Exemple</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">je</td><td style="padding:8px"><b>ai</b></td><td style="padding:8px">J\'ai un chat.</td></tr>'
             '<tr><td style="padding:8px">tu</td><td style="padding:8px"><b>as</b></td><td style="padding:8px">Tu as quel âge ?</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">il / elle / on</td><td style="padding:8px"><b>a</b></td><td style="padding:8px">Elle a une sœur.</td></tr>'
             '<tr><td style="padding:8px">nous</td><td style="padding:8px"><b>avons</b></td><td style="padding:8px">Nous avons deux enfants.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">vous</td><td style="padding:8px"><b>avez</b></td><td style="padding:8px">Vous avez l\'heure ?</td></tr>'
             '<tr><td style="padding:8px">ils / elles</td><td style="padding:8px"><b>ont</b></td><td style="padding:8px">Ils ont un grand appartement.</td></tr>'
             '</table>'),
            ("Emplois principaux de avoir", None,
             '<p class="slide-explanation">On utilise <b>avoir</b> pour exprimer :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>1. La possession :</b> J\'ai une voiture. Tu as un stylo ?</p>'
             '<p style="margin-top:8px"><b>2. L\'âge :</b> Elle a 25 ans. Quel âge avez-vous ?</p>'
             '<p style="margin-top:8px"><b>3. La famille :</b> Il a deux frères. Nous avons une fille.</p>'
             '<p style="margin-top:8px"><b>4. Auxiliaire du passé composé :</b> J\'ai mangé. Elle a parlé.</p>'
             '</div>'),
            ("Expressions avec avoir", None,
             '<p class="slide-explanation">En français, de nombreuses sensations physiques s\'expriment avec <b>avoir</b> (et non avec être) :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px;display:grid;grid-template-columns:1fr 1fr;gap:8px">'
             '<div><b>avoir faim</b> — to be hungry</div><div>J\'ai faim !</div>'
             '<div><b>avoir soif</b> — to be thirsty</div><div>Tu as soif ?</div>'
             '<div><b>avoir froid</b> — to be cold</div><div>Elle a froid.</div>'
             '<div><b>avoir chaud</b> — to be hot</div><div>Nous avons chaud.</div>'
             '<div><b>avoir sommeil</b> — to be sleepy</div><div>Il a sommeil.</div>'
             '<div><b>avoir peur</b> — to be afraid</div><div>Ils ont peur.</div>'
             '</div>'),
            ("Avoir vs Être", None,
             '<p class="slide-explanation">Attention aux différences avec l\'anglais :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Âge :</b> I am 20 years old. &rarr; J\'<b>ai</b> 20 ans. (avoir, pas être)</p>'
             '<p style="margin-top:8px"><b>Faim, soif, froid, chaud... :</b> I am hungry. &rarr; J\'<b>ai</b> faim. (avoir)</p>'
             '<p style="margin-top:8px"><b>Raison :</b> You are right. &rarr; Tu <b>as</b> raison. (avoir)</p>'
             '<p style="margin-top:8px"><b>Mais description :</b> I am tall. &rarr; Je <b>suis</b> grand. (être)</p>'
             '</div>'),
        ],
        'traps': [
            ("Je suis 20 ans.", "J'ai 20 ans.", "L'âge s'exprime avec avoir en français : j'ai 20 ans."),
            ("Je suis faim.", "J'ai faim.", "La faim, la soif, le froid, le chaud s'expriment avec avoir, pas être."),
            ("il a (il est)", "il a ✓", "Ne pas confondre il a (avoir) et il est (être). Ils sonnent différemment."),
            ("Vous avez raison ? (Vous êtes raison ?)", "Vous avez raison.", "Avoir raison = to be right. En français, c'est avoir, pas être."),
            ("ils a", "ils ont", "La 3e personne pluriel de avoir est ont, pas a."),
        ],
        'summary': [
            ("j'ai", "1re pers. sing.", "J'ai un chien."),
            ("tu as", "2e pers. sing.", "Tu as soif ?"),
            ("il/elle a", "3e pers. sing.", "Elle a 25 ans."),
            ("nous avons", "1re pers. pl.", "Nous avons deux enfants."),
            ("vous avez", "2e pers. pl.", "Vous avez l'heure ?"),
            ("ils/elles ont", "3e pers. pl.", "Ils ont faim."),
        ],
        'ex1': (
            "Conjugaison du verbe avoir",
            "Choisis la forme correcte du verbe avoir.",
            [
                ("J'_____ un chat.", ["ai", "as", "a", "avons"], "ai",
                 "Je → j'ai (élision de je devant a)."),
                ("Tu _____ quel âge ?", ["ai", "as", "a", "ont"], "as",
                 "Tu → tu as."),
                ("Il _____ une grande maison.", ["ai", "as", "a", "ont"], "a",
                 "Il → il a."),
                ("Nous _____ deux billets.", ["avons", "avez", "ont", "as"], "avons",
                 "Nous → nous avons."),
                ("Ils _____ faim.", ["a", "as", "avez", "ont"], "ont",
                 "Ils → ils ont."),
            ]
        ),
        'ex2': (
            "Avoir ou Être ?",
            "Complète avec la bonne forme de avoir ou être.",
            [
                ("Elle _____ 30 ans.", "a", "L'âge = avoir : elle a 30 ans."),
                ("Ils _____ fatigués.", "sont", "Adjectif décrivant un état = être : ils sont fatigués."),
                ("Tu _____ soif ?", "as", "La soif = avoir : tu as soif ?"),
                ("Nous _____ en retard.", "sommes", "Localisation/état = être : nous sommes en retard."),
                ("J'_____ raison.", "ai", "Avoir raison = to be right : j'ai raison."),
            ]
        ),
        'ex3': (
            "Expressions avec avoir",
            "Choisis la bonne expression.",
            [
                ("Il fait très chaud. &rarr; J'_____.", ["ai chaud", "suis chaud", "ai froid", "suis chaud"], "ai chaud",
                 "Avoir chaud = to feel hot : j'ai chaud."),
                ("Il n'a pas mangé depuis ce matin. &rarr; Il _____.", ["a faim", "est faim", "a soif", "est affamé"], "a faim",
                 "Avoir faim = to be hungry : il a faim."),
                ("Elle n'a pas dormi. &rarr; Elle _____.", ["a sommeil", "est sommeil", "a fatigué", "est endormi"], "a sommeil",
                 "Avoir sommeil = to be sleepy : elle a sommeil."),
                ("Vous _____ raison, c'est correct.", ["avez", "êtes", "avons", "ont"], "avez",
                 "Avoir raison = to be right : vous avez raison."),
                ("Les enfants ont peur du noir. Ils _____ peur.", ["ont", "sont", "avons", "êtes"], "ont",
                 "Avoir peur = to be afraid : ils ont peur."),
            ]
        ),
        'game_desc': "Entraîne-toi sur la conjugaison et les emplois du verbe avoir.",
        'items': [
            ("av-01", "j'ai", "verbe avoir à la 1re personne singulier", "1sg",
             "J'ai un vélo rouge.", "J'______ un vélo rouge.", "ai"),
            ('av-02', 'tu as', 'verbe avoir à la 2e personne singulier', '2sg',
             'Tu as quel âge ?', 'Tu ______ quel âge ?', 'as'),
            ('av-03', 'il/elle a', 'verbe avoir à la 3e personne singulier', '3sg',
             'Elle a une belle maison.', 'Elle ______ une belle maison.', 'a'),
            ('av-04', 'nous avons', 'verbe avoir à la 1re personne pluriel', '1pl',
             'Nous avons deux chats.', 'Nous ______ deux chats.', 'avons'),
            ('av-05', 'vous avez', 'verbe avoir à la 2e personne pluriel', '2pl',
             'Vous avez l\'heure, s\'il vous plaît ?', 'Vous ______ l\'heure, s\'il vous plaît ?', 'avez'),
            ('av-06', 'ils/elles ont', 'verbe avoir à la 3e personne pluriel', '3pl',
             'Ils ont beaucoup de travail.', 'Ils ______ beaucoup de travail.', 'ont'),
            ('av-07', 'avoir faim', 'expression avec avoir : to be hungry', 'faim',
             "Je n'ai pas mangé — j'ai faim !", "Je n'ai pas mangé — j'______ faim !", 'ai'),
            ('av-08', 'avoir + âge', "l'âge s'exprime avec avoir en français", "âge = avoir",
             'Elle a 25 ans.', 'Elle ______ 25 ans.', 'a'),
        ],
    },

    'il-y-a': {
        'level': 'a1',
        'section': 'grammaire',
        'num': 'G07',
        'short': 'Il y a',
        'title': 'Il y a — Exprimer l\'Existence',
        'subtitle': "Apprends à utiliser il y a, il n'y a pas et il y a + durée",
        'slides': [
            ("Il y a — there is / there are", None,
             '<p class="slide-explanation"><b>Il y a</b> est une expression invariable qui signifie <b>there is</b> ou <b>there are</b>. Elle s\'utilise pour signaler l\'existence ou la présence de quelque chose :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Il y a</b> un chat dans le jardin. (there is a cat)</p>'
             '<p style="margin-top:8px"><b>Il y a</b> des étudiants dans la classe. (there are students)</p>'
             '<p style="margin-top:8px"><b>Il y a</b> une table et deux chaises. (there is... and...)</p>'
             '</div>'
             '<p style="margin-top:12px">Il y a est <b>invariable</b> : il ne change pas selon le nombre (singulier ou pluriel).</p>'),
            ("Il n'y a pas — there is/are no", None,
             '<p class="slide-explanation">La forme négative est <b>il n\'y a pas</b> (there is/are no) :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>Il y a un café ici. &rarr; Il <b>n\'y a pas</b> de café ici.</p>'
             '<p style="margin-top:8px">Il y a des enfants. &rarr; Il <b>n\'y a pas</b> d\'enfants.</p>'
             '</div>'
             '<p style="margin-top:12px">Attention : après <b>il n\'y a pas</b>, l\'article change : un/une/des &rarr; <b>de</b> (règle générale de la négation).</p>'),
            ("Il y a vs C'est / Ce sont", None,
             '<p class="slide-explanation">Ne pas confondre <b>il y a</b> et <b>c\'est / ce sont</b> :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Il y a</b> un musée dans cette ville. (existence, présence)</p>'
             '<p style="margin-top:8px"><b>C\'est</b> le musée du Louvre. (identification d\'un élément connu)</p>'
             '<p style="margin-top:12px"><b>Il y a</b> des étudiants ici. (présence)</p>'
             '<p style="margin-top:8px"><b>Ce sont</b> les étudiants de M. Dupont. (identification)</p>'
             '</div>'),
            ("Il y a + durée", None,
             '<p class="slide-explanation"><b>Il y a</b> + durée exprime le temps écoulé depuis une action passée (= <b>ago</b> en anglais) :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>Je suis arrivé <b>il y a</b> deux heures. (I arrived two hours ago)</p>'
             '<p style="margin-top:8px">Nous nous sommes rencontrés <b>il y a</b> cinq ans. (five years ago)</p>'
             '<p style="margin-top:8px">Il a mangé <b>il y a</b> une heure. (one hour ago)</p>'
             '</div>'
             '<p style="margin-top:12px">Structure : <b>il y a</b> + nombre + unité de temps (heure(s), jour(s), an(s)...)</p>'),
        ],
        'traps': [
            ("Il y ont des gens.", "Il y a des gens.", "Il y a est invariable : il ne change pas au pluriel."),
            ("Il n'y a pas des livres.", "Il n'y a pas de livres.", "Après il n'y a pas, des → de : il n'y a pas de livres."),
            ("Il y a ago deux ans.", "Il y a deux ans.", "Il y a + durée = ago. On ne traduit pas ago séparément."),
            ("C'est un café ici.", "Il y a un café ici.", "Pour signaler l'existence/présence, utilise il y a, pas c'est."),
            ("Y a des gens.", "Il y a des gens.", "À l'oral familier, on dit y a, mais à l'écrit il faut il y a complet."),
        ],
        'summary': [
            ("il y a", "there is / there are", "Il y a un parc ici."),
            ("il n'y a pas de", "there is/are no", "Il n'y a pas de café."),
            ("il y a + durée", "ago", "Il y a deux ans."),
            ("invariable", "sing. et plur. = il y a", "Il y a un chat. Il y a des chats."),
            ("négation : de", "un/des → de après négation", "Il n'y a pas d'eau."),
        ],
        'ex1': (
            "Il y a ou il n'y a pas ?",
            "Choisis la forme correcte.",
            [
                ("_____ un cinéma dans mon quartier.", ["Il y a", "Il n'y a pas de", "C'est", "Ce sont"], "Il y a",
                 "On signale l'existence d'un cinéma : il y a un cinéma."),
                ("_____ de parking gratuit ici.", ["Il y a", "Il n'y a pas", "C'est", "Il y a des"], "Il n'y a pas",
                 "Forme négative : il n'y a pas de parking (pas + de)."),
                ("_____ combien d'étudiants dans ta classe ?", ["Il y a", "C'est", "Ce sont", "Il n'y a pas"], "Il y a",
                 "Pour demander combien : il y a combien de... ?"),
                ("_____ une boulangerie et une pharmacie.", ["Il y a", "Ce sont", "C'est", "Il n'y a pas"], "Il y a",
                 "On signale la présence de deux commerces : il y a..."),
                ("_____ d'eau dans le désert.", ["Il y a de l'", "Il n'y a pas", "C'est de l'", "Il y a"], "Il n'y a pas",
                 "Forme négative : il n'y a pas d'eau (de l'eau → d'eau)."),
            ]
        ),
        'ex2': (
            "Il y a + durée",
            "Traduis en français avec il y a.",
            [
                ("two years ago", "il y a deux ans", "Ago = il y a : il y a deux ans."),
                ("five minutes ago", "il y a cinq minutes", "Ago = il y a : il y a cinq minutes."),
                ("one week ago", "il y a une semaine", "Ago = il y a : il y a une semaine."),
                ("three hours ago", "il y a trois heures", "Ago = il y a : il y a trois heures."),
                ("ten years ago", "il y a dix ans", "Ago = il y a : il y a dix ans."),
            ]
        ),
        'ex3': (
            "Il y a vs C'est",
            "Choisis entre il y a et c'est / ce sont.",
            [
                ("_____ une nouvelle élève dans la classe.", ["Il y a", "C'est", "Ce sont", "Il n'y a pas"], "Il y a",
                 "On signale la présence d'une nouvelle élève : il y a."),
                ("_____ Marie, notre nouvelle collègue.", ["Il y a", "C'est", "Ce sont", "Il n'y a pas"], "C'est",
                 "On identifie une personne précise : c'est Marie."),
                ("_____ mes amis là-bas.", ["Il y a", "C'est", "Ce sont", "Il n'y a pas"], "Ce sont",
                 "On identifie un groupe pluriel : ce sont mes amis."),
                ("_____ beaucoup de monde au marché.", ["Il y a", "C'est", "Ce sont", "Il n'y a pas"], "Il y a",
                 "On signale la présence d'une foule : il y a beaucoup de monde."),
                ("_____ une bonne idée !", ["Il y a", "C'est", "Ce sont", "Il y a des"], "C'est",
                 "On évalue une idée : c'est une bonne idée."),
            ]
        ),
        'game_desc': "Entraîne-toi sur il y a, il n'y a pas et il y a + durée.",
        'items': [
            ('iya-01', 'il y a', 'expression invariable = there is / there are', 'existence',
             'Il y a un parc près de chez moi.', 'Il ______ un parc près de chez moi.', 'y a'),
            ("iya-02", "il n'y a pas de", "forme négative de il y a", "négatif",
             "Il n'y a pas de parking ici.", "Il n'______ pas de parking ici.", "y a"),
            ('iya-03', 'il y a (invariable)', 'il y a ne change pas au pluriel', 'invariable',
             'Il y a des enfants dans le parc.', 'Il ______ des enfants dans le parc.', 'y a'),
            ('iya-04', 'il y a + durée', 'il y a + durée = ago', 'ago',
             'Je suis arrivé il y a deux heures.', 'Je suis arrivé il y a deux ______.', 'heures'),
            ('iya-05', "il n'y a pas d'", "il n'y a pas de devant voyelle", "élision",
             "Il n'y a pas d'eau.", "Il n'y a pas ______ eau.", "d'"),
            ('iya-06', 'combien', "il y a combien de... ? pour demander la quantité", 'quantité',
             'Il y a combien d\'étudiants ?', 'Il y a ______ d\'étudiants ?', 'combien'),
            ('iya-07', "c'est", "c'est pour identifier (≠ il y a pour la présence)", "identifier",
             "C'est le musée du Louvre.", "______ le musée du Louvre.", "C'est"),
            ('iya-08', 'y a (oral)', "à l'oral familier : y a (sans il)", "registre",
             'Il y a quelqu\'un ?', '______ quelqu\'un ?', 'Il y a'),
        ],
    },

    'les-adjectifs': {
        'level': 'a1',
        'section': 'grammaire',
        'num': 'G08',
        'short': 'Les Adjectifs',
        'title': 'Les Adjectifs — Accord et Position',
        'subtitle': "Apprends à accorder les adjectifs en genre et en nombre en français",
        'slides': [
            ("L'accord de l'adjectif", None,
             '<p class="slide-explanation">En français, les adjectifs <b>s\'accordent</b> en <b>genre</b> (masculin/féminin) et en <b>nombre</b> (singulier/pluriel) avec le nom qu\'ils qualifient :</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse"><tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left"></th><th style="padding:8px;text-align:left">Masculin</th><th style="padding:8px;text-align:left">Féminin</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Singulier</b></td><td style="padding:8px">grand</td><td style="padding:8px">grand<b>e</b></td></tr>'
             '<tr><td style="padding:8px"><b>Pluriel</b></td><td style="padding:8px">grand<b>s</b></td><td style="padding:8px">grand<b>es</b></td></tr>'
             '</table>'
             '<p>Le masculin singulier est la forme de base (forme du dictionnaire).</p>'),
            ("Formations du féminin", None,
             '<p class="slide-explanation">On forme généralement le féminin en ajoutant <b>-e</b> au masculin. Quelques règles importantes :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Règle générale :</b> petit &rarr; petit<b>e</b> | grand &rarr; grand<b>e</b></p>'
             '<p style="margin-top:8px"><b>Déjà en -e :</b> rouge &rarr; rouge (pas de changement)</p>'
             '<p style="margin-top:8px"><b>-eux → -euse :</b> heureux &rarr; heureus<b>e</b></p>'
             '<p style="margin-top:8px"><b>-er → -ère :</b> léger &rarr; légèr<b>e</b></p>'
             '<p style="margin-top:8px"><b>Irréguliers :</b> beau &rarr; bell<b>e</b> | vieux &rarr; vieill<b>e</b> | nouveau &rarr; nouvell<b>e</b></p>'
             '</div>'),
            ("La position de l'adjectif", None,
             '<p class="slide-explanation">En français, la plupart des adjectifs se placent <b>après</b> le nom. Mais quelques adjectifs courants se placent <b>avant</b> le nom :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Après (normal) :</b> une voiture rouge, un livre intéressant, un homme intelligent</p>'
             '<p style="margin-top:12px"><b>Avant (BAGS) :</b> Beauty, Age, Good/Bad, Size</p>'
             '<p style="margin-top:8px">beau, joli | vieux, jeune, nouveau | bon, mauvais | grand, petit, gros, long</p>'
             '<p style="margin-top:8px">Exemples : un <b>beau</b> livre, une <b>petite</b> maison, un <b>bon</b> repas</p>'
             '</div>'),
            ("Adjectifs courants", None,
             '<p class="slide-explanation">Voici les adjectifs les plus utiles en A1 :</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px;display:grid;grid-template-columns:1fr 1fr;gap:8px">'
             '<div><b>grand(e)</b> — big/tall</div><div><b>petit(e)</b> — small/short</div>'
             '<div><b>bon(ne)</b> — good</div><div><b>mauvais(e)</b> — bad</div>'
             '<div><b>beau/belle</b> — beautiful</div><div><b>vieux/vieille</b> — old</div>'
             '<div><b>nouveau/nouvelle</b> — new</div><div><b>jeune</b> — young</div>'
             '<div><b>heureux/heureuse</b> — happy</div><div><b>content(e)</b> — pleased</div>'
             '<div><b>rouge</b> — red</div><div><b>blanc/blanche</b> — white</div>'
             '</div>'),
        ],
        'traps': [
            ("une rouge voiture", "une voiture rouge", "En français, la plupart des adjectifs se placent APRÈS le nom."),
            ("Elle est grand.", "Elle est grande.", "L'adjectif s'accorde : sujet féminin → adjectif féminin (grand → grande)."),
            ("des grands maisons", "de grandes maisons", "Après des + adjectif avant le nom, des → de."),
            ("Il est vieux. (vieux = vieux)", "Il est vieux. ✓", "Vieux est correct au masculin singulier. Féminin : vieille."),
            ("un bel homme (beau)", "un bel homme ✓", "Beau devient bel devant un nom masculin commençant par une voyelle : un bel homme."),
        ],
        'summary': [
            ("masc. sg.", "forme de base", "grand, petit, bon"),
            ("fém. sg.", "masc. + -e", "grande, petite, bonne"),
            ("masc. pl.", "masc. + -s", "grands, petits, bons"),
            ("fém. pl.", "masc. + -es", "grandes, petites, bonnes"),
            ("position", "généralement après le nom", "un livre intéressant"),
            ("BAGS avant", "beau, âge, bon/mauvais, size", "un beau livre, une petite maison"),
        ],
        'ex1': (
            "Accord de l'adjectif",
            "Choisis la forme correcte de l'adjectif.",
            [
                ("C'est une _____ fille. (petit)", ["petit", "petite", "petits", "petites"], "petite",
                 "Fille est féminin singulier : petite."),
                ("Ce sont des _____ garçons. (grand)", ["grand", "grande", "grands", "grandes"], "grands",
                 "Garçons est masculin pluriel : grands."),
                ("Elle est _____. (heureux)", ["heureux", "heureuse", "heureux", "heureuses"], "heureuse",
                 "Elle est féminin : heureux → heureuse (-eux → -euse)."),
                ("C'est une _____ idée. (bon)", ["bon", "bonne", "bonnes", "bons"], "bonne",
                 "Idée est féminin : bon → bonne (doublement du n)."),
                ("Les maisons sont _____. (blanc)", ["blanc", "blanche", "blancs", "blanches"], "blanches",
                 "Maisons est féminin pluriel : blanc → blanches."),
            ]
        ),
        'ex2': (
            "Féminin de l'adjectif",
            "Donne le féminin de l'adjectif.",
            [
                ("grand", "grande", "Grand → grande (ajout de -e)."),
                ("heureux", "heureuse", "Heureux → heureuse (-eux → -euse)."),
                ("beau", "belle", "Beau → belle (irrégulier)."),
                ("léger", "légère", "Léger → légère (-er → -ère)."),
                ("vieux", "vieille", "Vieux → vieille (irrégulier)."),
            ]
        ),
        'ex3': (
            "Position de l'adjectif",
            "L'adjectif va avant ou après le nom ?",
            [
                ("C'est une _____ maison. (petit)", ["petite maison", "maison petite", "maison petits", "petits maison"], "petite maison",
                 "Petit appartient aux adjectifs BAGS (size) : il se place avant le nom."),
                ("J'ai un sac _____. (rouge)", ["rouge sac", "rouge", "sacs rouge", "sac rouge"], "sac rouge",
                 "Rouge est un adjectif de couleur : il se place après le nom."),
                ("C'est un _____ film. (bon)", ["bon film", "film bon", "films bon", "bons film"], "bon film",
                 "Bon appartient aux adjectifs BAGS (good/bad) : il se place avant le nom."),
                ("Il a les yeux _____. (bleu)", ["bleus yeux", "bleu yeux", "yeux bleus", "yeux bleu"], "yeux bleus",
                 "Bleu est un adjectif de couleur : il se place après le nom, accordé au pluriel."),
                ("Voilà une _____ personne. (beau)", ["belle personne", "personne belle", "beau personne", "belle personnes"], "belle personne",
                 "Beau appartient aux adjectifs BAGS et est irrégulier au féminin : belle. Il se place avant le nom."),
            ]
        ),
        'game_desc': "Entraîne-toi sur l'accord et la position des adjectifs en français.",
        'items': [
            ('adj-01', 'grand / grande', 'accord féminin de grand : + e', 'fém. + e',
             'C\'est une grande maison.', 'C\'est une ______ maison.', 'grande'),
            ('adj-02', 'petit / petite', 'accord féminin de petit : + e', 'fém. + e',
             'Elle a une petite voiture.', 'Elle a une ______ voiture.', 'petite'),
            ('adj-03', 'heureux / heureuse', 'accord féminin : -eux → -euse', 'fém. -euse',
             'Elle est heureuse aujourd\'hui.', 'Elle est ______ aujourd\'hui.', 'heureuse'),
            ('adj-04', 'beau / belle', 'adjectif irrégulier : beau → belle au féminin', 'irrég.',
             'C\'est une belle journée.', 'C\'est une ______ journée.', 'belle'),
            ('adj-05', 'vieux / vieille', 'adjectif irrégulier : vieux → vieille au féminin', 'irrég.',
             'C\'est une vieille église.', 'C\'est une ______ église.', 'vieille'),
            ('adj-06', 'bon / bonne', 'accord féminin : bon → bonne (doublement du n)', 'fém. nn',
             'C\'est une bonne idée.', 'C\'est une ______ idée.', 'bonne'),
            ('adj-07', 'position avant', "adjectifs BAGS : avant le nom", "BAGS = avant",
             'C\'est un petit appartement.', 'C\'est un ______ appartement.', 'petit'),
            ('adj-08', 'position après', "adjectifs de couleur et description : après le nom", "couleur = après",
             'J\'ai une voiture rouge.', 'J\'ai une voiture ______.', 'rouge'),
        ],
    },
}
