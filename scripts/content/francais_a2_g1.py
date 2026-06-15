"""Français A2 — Grammaire batch 1: G01–G04."""

CHAPTERS = {

# ── G01 Le Passé Composé ───────────────────────────────────────────────────
'le-passe-compose': {
    'level':   'a2',
    'section': 'grammaire',
    'num':     'G01',
    'short':   'Le Passé Composé',
    'title':   'Le Passé Composé — Parler du Passé',
    'subtitle': 'Formation avec avoir et être — accord du participe passé',
    'slides': [
        ('Qu\'est-ce que le passé composé ?', None,
         '<p>Le passé composé exprime une <b>action terminée</b> dans le passé :</p>'
         '<ul><li>J\'ai mangé une pizza hier soir.</li>'
         '<li>Nous avons fini le travail.</li>'
         '<li>Elle est arrivée à midi.</li></ul>'
         '<p>Formation : <b>auxiliaire</b> (avoir ou être au présent) + <b>participe passé</b>.</p>'
         '<p>C\'est le temps du passé le plus fréquent à l\'oral et à l\'écrit en français courant.</p>'),
        ('Avec l\'auxiliaire avoir', None,
         '<p>La grande majorité des verbes se conjuguent avec <b>avoir</b> :</p>'
         '<table><tr><th>Sujet</th><th>Avoir</th><th>Participe</th></tr>'
         '<tr><td>j\'</td><td>ai</td><td rowspan="6">mangé / fini / vendu</td></tr>'
         '<tr><td>tu</td><td>as</td></tr>'
         '<tr><td>il/elle</td><td>a</td></tr>'
         '<tr><td>nous</td><td>avons</td></tr>'
         '<tr><td>vous</td><td>avez</td></tr>'
         '<tr><td>ils/elles</td><td>ont</td></tr></table>'
         '<p>Formation du participe : -ER → -é · -IR → -i · -RE → -u</p>'),
        ('Avec l\'auxiliaire être', None,
         '<p>Une quinzaine de verbes de <b>mouvement et d\'état</b> utilisent être :<br>'
         '(moyen mnémotechnique : DR&nbsp;MRS&nbsp;VANDERTRAMP)</p>'
         '<p><b>aller</b> (allé) · <b>venir</b> (venu) · <b>arriver</b> (arrivé) · <b>partir</b> (parti)<br>'
         '<b>entrer</b> (entré) · <b>sortir</b> (sorti) · <b>monter</b> (monté) · <b>descendre</b> (descendu)<br>'
         '<b>naître</b> (né) · <b>mourir</b> (mort) · <b>rester</b> (resté) · <b>tomber</b> (tombé)<br>'
         '<b>retourner</b> (retourné) · <b>passer</b> (passé)</p>'
         '<p>+ tous les verbes <b>pronominaux</b> : se lever → je me suis levé(e).</p>'),
        ('L\'accord du participe passé', None,
         '<p>Avec <b>être</b> : le participe s\'accorde avec le <b>sujet</b> :</p>'
         '<ul><li>Il est arrivé. / Elle est arrivée. (+e)</li>'
         '<li>Ils sont arrivés. / Elles sont arrivées. (+es)</li></ul>'
         '<p>Avec <b>avoir</b> : le participe est <b>invariable</b> sauf si le COD est placé avant le verbe :</p>'
         '<ul><li>Elle a mangé une pomme. (COD après → pas d\'accord)</li>'
         '<li>La pomme qu\'elle a mangée. (COD avant → accord)</li></ul>'
         '<p>À l\'oral, l\'accord avec avoir est souvent inaudible.</p>'),
        ('Participes passés irréguliers', None,
         '<table><tr><th>Infinitif</th><th>Participe</th><th>Infinitif</th><th>Participe</th></tr>'
         '<tr><td>être</td><td><b>été</b></td><td>avoir</td><td><b>eu</b></td></tr>'
         '<tr><td>faire</td><td><b>fait</b></td><td>prendre</td><td><b>pris</b></td></tr>'
         '<tr><td>venir</td><td><b>venu</b></td><td>pouvoir</td><td><b>pu</b></td></tr>'
         '<tr><td>voir</td><td><b>vu</b></td><td>vouloir</td><td><b>voulu</b></td></tr>'
         '<tr><td>savoir</td><td><b>su</b></td><td>lire</td><td><b>lu</b></td></tr>'
         '<tr><td>écrire</td><td><b>écrit</b></td><td>dire</td><td><b>dit</b></td></tr></table>'),
    ],
    'traps': [
        ('Je suis mangé.', 'J\'ai mangé.', '« Manger » est un verbe ordinaire ; il prend avoir, pas être.'),
        ('Elle est arrivé.', 'Elle est arrivée.', 'Avec être, le participe s\'accorde avec le sujet : arrivée (féminin).'),
        ('Il a été allé.', 'Il est allé.', '« Aller » se conjugue avec être, pas avoir + être.'),
        ('Nous avons vendu la maison hier.', 'Correct !', 'Vendre → vendu. Avec avoir, le participe est invariable quand le COD suit.'),
        ('Ils ont pris la décision.', 'Ils ont pris la décision.', 'Prendre → pris (irrégulier). Correct ! Pas « prisd » ni « prendu ».'),
    ],
    'summary': [
        ('Formation', 'avoir / être (présent) + participe passé', 'J\'ai mangé. · Elle est partie.'),
        ('Avec avoir', 'majorité des verbes ; participe invariable', 'Il a fait ses devoirs.'),
        ('Avec être', 'verbes de mouvement/état + pronominaux', 'Elle est arrivée. · Il s\'est levé.'),
        ('Accord (être)', 'participe s\'accorde avec le sujet', 'Elles sont parties. (+es)'),
        ('PP irrég.', 'être→été · avoir→eu · faire→fait · prendre→pris', 'J\'ai eu · tu as fait · il a pris'),
        ('Usage', 'action terminée dans le passé', 'Hier, j\'ai travaillé jusqu\'à 18 h.'),
    ],
    'ex1': ('Choisir l\'auxiliaire', 'Choisissez avoir ou être.',
        [
            ('Elle ___ arrivée à 8 h.', ['a', 'est', 'avait', 'était'], 'est',
             'Arriver est un verbe de mouvement qui se conjugue avec être. Le participe s\'accorde : arrivée (f.).'),
            ('Nous ___ mangé au restaurant.', ['sommes', 'avons', 'étions', 'avions'], 'avons',
             'Manger est un verbe ordinaire qui se conjugue avec avoir.'),
            ('Ils ___ partis de bonne heure.', ['ont', 'sont', 'avaient', 'étaient'], 'sont',
             'Partir (verbe de mouvement) → être. Accord : partis (masculin pluriel).'),
            ('Tu ___ vu ce film ?', ['es', 'as', 'étais', 'avais'], 'as',
             'Voir → vu. Verbe ordinaire → avoir.'),
        ]),
    'ex2': ('Mettre au passé composé', 'Écrivez la forme correcte du participe passé.',
        [
            ('Elle a ___ (manger) une salade.', 'mangé', '-ER → -é : manger → mangé.'),
            ('Nous avons ___ (finir) le projet.', 'fini', '-IR → -i : finir → fini.'),
            ('Il a ___ (prendre) le train.', 'pris', 'Prendre → pris (irrégulier).'),
            ('Elles sont ___ (arriver) hier soir.', 'arrivées', 'Avec être, accord avec le sujet féminin pluriel : arrivées.'),
            ('J\'ai ___ (faire) mes devoirs.', 'fait', 'Faire → fait (irrégulier).'),
        ]),
    'ex3': ('Trouver l\'erreur', 'Quelle phrase est incorrecte ?',
        [
            ('Laquelle est incorrecte ?',
             ['J\'ai mangé.', 'Elle est arrivée.', 'Nous avons fini.', 'Il est mangé.'],
             'Il est mangé.',
             'Manger prend avoir, pas être : il a mangé.'),
            ('Quelle phrase a un mauvais accord ?',
             ['Elle est partie.', 'Ils sont arrivés.', 'Elles sont arrivé.', 'Il est allé.'],
             'Elles sont arrivé.',
             'Avec être, le participe s\'accorde avec le sujet : elles sont arrivées (+es).'),
            ('Quel participe est incorrect ?',
             ['fait', 'pris', 'vu', 'prendu'],
             'prendu',
             'Prendre → pris (irrégulier). « Prendu » n\'existe pas.'),
        ]),
    'game_desc': 'Maîtrisez le passé composé en français !',
    'items': [
        ('pc-01', 'avoir + participe', 'to have + past participle', 'auxiliaire', 'J\'ai mangé une pizza hier.', 'J\'___ mangé une pizza hier.', 'ai'),
        ('pc-02', 'être + participe', 'to be + past participle', 'auxiliaire', 'Elle est arrivée à midi.', 'Elle ___ arrivée à midi.', 'est'),
        ('pc-03', 'manger → mangé', 'eat → eaten (-ER)', 'participe', 'Nous avons mangé au restaurant.', 'Nous avons ___ au restaurant.', 'mangé'),
        ('pc-04', 'finir → fini', 'finish → finished (-IR)', 'participe', 'Ils ont fini le travail.', 'Ils ont ___ le travail.', 'fini'),
        ('pc-05', 'faire → fait', 'do/make → done (irreg.)', 'participe', 'Tu as fait tes devoirs ?', 'Tu as ___ tes devoirs ?', 'fait'),
        ('pc-06', 'prendre → pris', 'take → taken (irreg.)', 'participe', 'Elle a pris le bus ce matin.', 'Elle a ___ le bus ce matin.', 'pris'),
        ('pc-07', 'accord avec être', 'agreement with être', 'accord', 'Elles sont arrivées en retard.', 'Elles sont arrivée___. (pluriel)', 's'),
        ('pc-08', 'partir → parti', 'leave → left (être)', 'participe', 'Il est parti tôt ce matin.', 'Il est ___ tôt ce matin.', 'parti'),
    ],
},

# ── G02 L'Imparfait ────────────────────────────────────────────────────────
'l-imparfait': {
    'level':   'a2',
    'section': 'grammaire',
    'num':     'G02',
    'short':   'L\'Imparfait',
    'title':   'L\'Imparfait — Descriptions et Habitudes du Passé',
    'subtitle': 'Formation de l\'imparfait et distinction avec le passé composé',
    'slides': [
        ('Qu\'est-ce que l\'imparfait ?', None,
         '<p>L\'imparfait exprime :</p>'
         '<ul><li>Une <b>description dans le passé</b> : Il faisait beau. · Elle était fatiguée.</li>'
         '<li>Une <b>habitude passée</b> : Quand j\'étais enfant, je jouais au foot.</li>'
         '<li>Une <b>action en cours</b> quand une autre arrive : Je dormais quand le téléphone a sonné.</li>'
         '<li>Une <b>situation de fond</b> (décor) d\'un récit.</li></ul>'
         '<p>L\'imparfait n\'est jamais utilisé pour une action unique et terminée — c\'est le rôle du passé composé.</p>'),
        ('Formation de l\'imparfait', None,
         '<p>Base : <b>1re personne du pluriel du présent</b> (nous) — on enlève -ons, on ajoute les terminaisons :</p>'
         '<table><tr><th>Sujet</th><th>Terminaison</th><th>Parler</th><th>Finir</th></tr>'
         '<tr><td>je</td><td>-ais</td><td>parlais</td><td>finissais</td></tr>'
         '<tr><td>tu</td><td>-ais</td><td>parlais</td><td>finissais</td></tr>'
         '<tr><td>il/elle</td><td>-ait</td><td>parlait</td><td>finissait</td></tr>'
         '<tr><td>nous</td><td>-ions</td><td>parlions</td><td>finissions</td></tr>'
         '<tr><td>vous</td><td>-iez</td><td>parliez</td><td>finissiez</td></tr>'
         '<tr><td>ils/elles</td><td>-aient</td><td>parlaient</td><td>finissaient</td></tr></table>'),
        ('Exception : être', None,
         '<p>Le seul verbe vraiment irrégulier à l\'imparfait est <b>être</b> :<br>'
         'base = <b>ét-</b> (pas étions)</p>'
         '<table><tr><th>Sujet</th><th>Être</th></tr>'
         '<tr><td>j\'</td><td>étais</td></tr>'
         '<tr><td>tu</td><td>étais</td></tr>'
         '<tr><td>il/elle</td><td>était</td></tr>'
         '<tr><td>nous</td><td>étions</td></tr>'
         '<tr><td>vous</td><td>étiez</td></tr>'
         '<tr><td>ils/elles</td><td>étaient</td></tr></table>'
         '<p>Tous les autres verbes suivent la règle régulière.</p>'),
        ('Passé composé vs. imparfait', None,
         '<p>La distinction clé :</p>'
         '<table><tr><th>Passé composé</th><th>Imparfait</th></tr>'
         '<tr><td>Action terminée, unique</td><td>Description, habitude, fond</td></tr>'
         '<tr><td>Rupture, événement</td><td>Durée, continuité</td></tr>'
         '<tr><td>Hier, j\'ai travaillé 8 h.</td><td>Avant, je travaillais à Paris.</td></tr>'
         '<tr><td>Il a sonné à la porte.</td><td>Il faisait nuit.</td></tr></table>'
         '<p>Dans un récit : <b>imparfait = décor</b>, <b>passé composé = action</b>.</p>'),
        ('Marqueurs temporels', None,
         '<p>Certains marqueurs aident à choisir le temps :</p>'
         '<table><tr><th>Imparfait</th><th>Passé composé</th></tr>'
         '<tr><td>quand j\'étais enfant</td><td>hier, avant-hier</td></tr>'
         '<tr><td>tous les jours, souvent</td><td>une fois, soudain</td></tr>'
         '<tr><td>d\'habitude, autrefois</td><td>ce matin, la semaine dernière</td></tr>'
         '<tr><td>toujours, jamais (habitude)</td><td>tout à coup, puis</td></tr></table>'),
    ],
    'traps': [
        ('Hier, je travaillais.', 'Hier, j\'ai travaillé.', '« Hier » signale une action unique/terminée → passé composé.'),
        ('Quand j\'étais enfant, j\'ai joué au foot tous les jours.', 'Quand j\'étais enfant, je jouais au foot tous les jours.', '« Tous les jours » = habitude → imparfait.'),
        ('Il a été fatigué.', 'Il était fatigué.', 'Un état ou une description dans le passé s\'exprime à l\'imparfait.'),
        ('Je dormissais.', 'Je dormais.', 'Dormir : nous dormons → base dorm- → je dormais. Pas de -iss- à l\'imparfait.'),
        ('Soudain, il pleuvait.', 'Soudain, il a plu.', '« Soudain » (tout à coup) = événement ponctuel → passé composé.'),
    ],
    'summary': [
        ('Rôle', 'description, habitude, fond du récit', 'Il faisait beau. · Je jouais au foot.'),
        ('Formation', 'base nous-présent + -ais/-ais/-ait/-ions/-iez/-aient', 'parler → parl- → je parlais'),
        ('Exception', 'être → étais/étais/était/étions/étiez/étaient', 'J\'étais fatigué.'),
        ('vs. PC', 'imparfait = fond / PC = action', 'Je dormais quand il est arrivé.'),
        ('Marqueurs', 'toujours, souvent, d\'habitude → imparfait', 'D\'habitude, il prenait le bus.'),
        ('Marqueurs PC', 'hier, soudain, une fois → passé composé', 'Hier, j\'ai vu un film.'),
    ],
    'ex1': ('Choisir le bon temps', 'Passé composé ou imparfait ?',
        [
            ('D\'habitude, elle ___ (prendre) le train.', ['a pris', 'prenait', 'prend', 'prendra'], 'prenait',
             '« D\'habitude » indique une habitude passée → imparfait : elle prenait.'),
            ('Hier, il ___ (pleuvoir) toute la journée.', ['pleuvait', 'a plu', 'pluvait', 'plu'], 'a plu',
             '« Hier toute la journée » = action/situation terminée → passé composé : il a plu.'),
            ('Quand j\'étais petit, j\'___ (adorer) les glaces.', ['ai adoré', 'adorais', 'adore', 'adoré'], 'adorais',
             '« Quand j\'étais petit » = habitude/état passé → imparfait : j\'adorais.'),
            ('Soudain, le téléphone ___ (sonner).', ['sonnait', 'a sonné', 'sonne', 'sonnera'], 'a sonné',
             '« Soudain » = événement ponctuel → passé composé : a sonné.'),
        ]),
    'ex2': ('Conjuguer à l\'imparfait', 'Donnez la forme correcte.',
        [
            ('Quand il ___ (être) enfant, il habitait à Nice.', 'était', 'Être à l\'imparfait : j\'étais, tu étais, il était… Base irrégulière ét-.'),
            ('Nous ___ (manger) souvent des pâtes.', 'mangions', 'Manger → nous mangeons → base mange- → nous mangions.'),
            ('Elle ___ (finir) toujours ses devoirs avant le dîner.', 'finissait', 'Finir → nous finissons → base finiss- → elle finissait.'),
            ('Ils ___ (parler) français à la maison.', 'parlaient', 'Parler → nous parlons → base parl- → ils parlaient.'),
            ('Tu ___ (avoir) les cheveux longs autrefois.', 'avais', 'Avoir → nous avons → base av- → tu avais.'),
        ]),
    'ex3': ('Identifier l\'erreur', 'Quelle phrase est incorrecte ?',
        [
            ('Laquelle est incorrecte ?',
             ['Je jouais au foot quand j\'étais enfant.', 'Hier, j\'ai travaillé.', 'Soudain, il pleuvait.', 'D\'habitude, elle prenait le bus.'],
             'Soudain, il pleuvait.',
             '« Soudain » indique un événement ponctuel → passé composé : soudain, il a plu.'),
            ('Quelle forme est mal conjuguée ?',
             ['je parlais', 'tu finissais', 'il dormissait', 'nous mangions'],
             'il dormissait',
             'Dormir → nous dormons → base dorm- → il dormait. Pas de -iss- à l\'imparfait pour les -ir réguliers issus de dormir.'),
            ('Quel marqueur ne va PAS avec l\'imparfait ?',
             ['d\'habitude', 'toujours', 'soudain', 'souvent'],
             'soudain',
             '« Soudain / tout à coup » marque un événement ponctuel → passé composé.'),
        ]),
    'game_desc': 'Maîtrisez l\'imparfait et son usage en français !',
    'items': [
        ('imp-01', 'je parlais', 'I was speaking / used to speak', 'formation', 'Avant, je parlais souvent avec lui.', 'Avant, je ___ souvent avec lui.', 'parlais'),
        ('imp-02', 'il était', 'he was (être irreg.)', 'être', 'Il était fatigué après le travail.', 'Il ___ fatigué après le travail.', 'était'),
        ('imp-03', 'd\'habitude', 'usually / as a rule', 'marqueur', 'D\'habitude, elle prenait le métro.', 'D\'___, elle prenait le métro.', 'habitude'),
        ('imp-04', 'nous mangions', 'we used to eat (-ger)', 'orthographe', 'Nous mangions souvent des crêpes.', 'Nous ___ souvent des crêpes.', 'mangions'),
        ('imp-05', 'imparfait = fond', 'imperfect = background', 'récit', 'Je dormais quand il est arrivé.', 'Je ___ quand il est arrivé. (fond)', 'dormais'),
        ('imp-06', 'PC = action', 'passé composé = event', 'récit', 'Soudain, le téléphone a sonné.', 'Soudain, le téléphone a ___. (événement)', 'sonné'),
        ('imp-07', 'ils finissaient', 'they used to finish', 'formation', 'Ils finissaient toujours à 17 h.', 'Ils ___ toujours à 17 h.', 'finissaient'),
        ('imp-08', 'quand j\'étais enfant', 'when I was a child', 'marqueur', 'Quand j\'étais enfant, j\'adorais la natation.', 'Quand j\'étais ___, j\'adorais la natation.', 'enfant'),
    ],
},

# ── G03 Les Articles Partitifs ─────────────────────────────────────────────
'les-articles-partitifs': {
    'level':   'a2',
    'section': 'grammaire',
    'num':     'G03',
    'short':   'Les Articles Partitifs',
    'title':   'Les Articles Partitifs — Du, De la, Des',
    'subtitle': 'Exprimer une quantité non définie avec du, de la, de l\'et des',
    'slides': [
        ('Les articles partitifs', None,
         '<p>Les articles partitifs expriment une <b>quantité indéfinie</b> de quelque chose :</p>'
         '<table><tr><th>Genre / Nombre</th><th>Article</th><th>Exemple</th></tr>'
         '<tr><td>Masculin</td><td><b>du</b></td><td>du pain · du fromage</td></tr>'
         '<tr><td>Féminin</td><td><b>de la</b></td><td>de la viande · de la musique</td></tr>'
         '<tr><td>Voyelle / h muet</td><td><b>de l\'</b></td><td>de l\'eau · de l\'huile</td></tr>'
         '<tr><td>Pluriel</td><td><b>des</b></td><td>des légumes · des amis</td></tr></table>'
         '<p>Traduction anglaise : « some » ou aucun article — I eat bread. / Je mange du pain.</p>'),
        ('Différence avec les articles définis et indéfinis', None,
         '<p>Comparaison des trois types d\'articles :</p>'
         '<table><tr><th>Défini</th><th>Indéfini</th><th>Partitif</th></tr>'
         '<tr><td>le pain</td><td>un pain</td><td>du pain</td></tr>'
         '<tr><td><i>the bread (précis)</i></td><td><i>a loaf of bread</i></td><td><i>some bread</i></td></tr></table>'
         '<ul><li><b>Défini</b> : chose précise ou connue → J\'aime <b>le</b> café.</li>'
         '<li><b>Indéfini</b> : une unité → Je veux <b>un</b> café.</li>'
         '<li><b>Partitif</b> : une quantité → Je bois <b>du</b> café.</li></ul>'),
        ('La négation : de / d\'', None,
         '<p>Après une négation (<b>ne…pas</b>), tous les articles partitifs et indéfinis deviennent <b>de</b> (ou <b>d\'</b> devant voyelle) :</p>'
         '<table><tr><th>Affirmatif</th><th>Négatif</th></tr>'
         '<tr><td>Je mange du pain.</td><td>Je ne mange <b>pas de</b> pain.</td></tr>'
         '<tr><td>Elle boit de la limonade.</td><td>Elle ne boit <b>pas de</b> limonade.</td></tr>'
         '<tr><td>Il mange des légumes.</td><td>Il ne mange <b>pas de</b> légumes.</td></tr>'
         '<tr><td>J\'ai un chien.</td><td>Je n\'ai <b>pas de</b> chien.</td></tr></table>'
         '<p>Exception : avec le verbe <b>être</b>, l\'article reste : Ce n\'est pas <b>du</b> vin, c\'est du jus.</p>'),
        ('Expressions de quantité', None,
         '<p>Après une expression de quantité, on utilise aussi <b>de</b> (sans article) :</p>'
         '<ul><li>un verre <b>de</b> vin · une tasse <b>de</b> café</li>'
         '<li>un kilo <b>de</b> farine · un litre <b>d\'</b>eau</li>'
         '<li>beaucoup <b>de</b> travail · assez <b>de</b> temps</li>'
         '<li>trop <b>de</b> sucre · peu <b>de</b> sel</li>'
         '<li>un peu <b>de</b> musique · combien <b>de</b> personnes ?</li></ul>'),
        ('Récapitulatif et pièges', None,
         '<p>Résumé des choix :</p>'
         '<ul><li>Généralité / goût : <b>article défini</b> — J\'aime <b>le</b> chocolat.</li>'
         '<li>Unité comptable : <b>article indéfini</b> — Je veux <b>une</b> pomme.</li>'
         '<li>Quantité non définie : <b>partitif</b> — Je prends <b>du</b> sucre.</li>'
         '<li>Négation : <b>de</b> — Je ne veux <b>pas de</b> sucre.</li>'
         '<li>Après quantité : <b>de</b> — beaucoup <b>de</b> sucre.</li></ul>'),
    ],
    'traps': [
        ('Je mange de la pain.', 'Je mange du pain.', 'Pain est masculin → du pain (de + le = du).'),
        ('Je ne mange pas du pain.', 'Je ne mange pas de pain.', 'Après la négation, du/de la/des → de.'),
        ('Il boit beaucoup du café.', 'Il boit beaucoup de café.', 'Après une expression de quantité (beaucoup), on utilise de sans article.'),
        ('J\'aime du chocolat.', 'J\'aime le chocolat.', 'Pour exprimer un goût général, on utilise l\'article défini, pas le partitif.'),
        ('Elle mange des viande.', 'Elle mange de la viande.', 'Viande est un nom indénombrable féminin → de la viande (pas des).'),
    ],
    'summary': [
        ('Du', 'masc. singulier + indénombrable', 'du pain · du fromage · du café'),
        ('De la', 'fém. singulier + indénombrable', 'de la viande · de la farine'),
        ('De l\'', 'devant voyelle ou h muet', 'de l\'eau · de l\'huile · de l\'air'),
        ('Des', 'pluriel (indéfini)', 'des légumes · des pommes · des amis'),
        ('Négation', 'pas de / pas d\' (toujours)', 'Je ne mange pas de pain.'),
        ('Après quantité', 'de / d\' sans article', 'un verre de vin · beaucoup de travail'),
    ],
    'ex1': ('Choisir l\'article partitif', 'Complétez avec du, de la, de l\' ou des.',
        [
            ('Je bois ___ eau chaque matin.', ['du', 'de la', 'de l\'', 'des'], 'de l\'',
             'Eau est féminin et commence par une voyelle → de l\'eau.'),
            ('Elle mange ___ fromage tous les jours.', ['de la', 'du', 'de l\'', 'des'], 'du',
             'Fromage est masculin singulier → du fromage.'),
            ('Il fait ___ sport le week-end.', ['de la', 'du', 'de l\'', 'des'], 'du',
             'Sport est masculin singulier → du sport.'),
            ('Ils ont mangé ___ légumes ce soir.', ['du', 'de la', 'de l\'', 'des'], 'des',
             'Légumes est au pluriel → des légumes.'),
        ]),
    'ex2': ('Mettre à la forme négative', 'Transformez en négatif.',
        [
            ('Je mange du pain. → Je ne mange pas ___ pain.', 'de', 'Après la négation, du/de la/des → de.'),
            ('Elle boit de la limonade. → Elle ne boit pas ___ limonade.', 'de', 'Après ne…pas, de la → de.'),
            ('Il a des amis à Paris. → Il n\'a pas ___ amis à Paris.', 'd\'', 'Pas de + voyelle → pas d\'. Des → d\'.'),
            ('Je prends du sucre. → Je ne prends pas ___ sucre.', 'de', 'Du → de après la négation.'),
            ('Il y a de l\'eau. → Il n\'y a pas ___ eau.', 'd\'', 'Pas de + voyelle → pas d\'.'),
        ]),
    'ex3': ('Identifier l\'erreur', 'Quelle phrase est incorrecte ?',
        [
            ('Laquelle est incorrecte ?',
             ['Je mange du pain.', 'Elle boit de la limonade.', 'J\'ai mangé de la viandes.', 'Il prend de l\'eau.'],
             'J\'ai mangé de la viandes.',
             'Viande est un nom indénombrable → de la viande (singulier, sans -s).'),
            ('Quel article est faux ?',
             ['J\'aime le chocolat.', 'Je mange du chocolat.', 'Je ne mange pas de chocolat.', 'Je mange du chocolats.'],
             'Je mange du chocolats.',
             'Chocolat est indénombrable masculin → du chocolat (singulier, sans -s).'),
            ('Quelle phrase après la négation est correcte ?',
             ['Je ne mange pas de pain.', 'Je ne mange pas du pain.', 'Je ne mange pas de la viande.', 'Je ne mange pas des légumes.'],
             'Je ne mange pas de pain.',
             'Après ne…pas, tous les articles partitifs → de. Seule « pas de pain » est correct.'),
        ]),
    'game_desc': 'Maîtrisez les articles partitifs du, de la, des en français !',
    'items': [
        ('part-01', 'du pain', 'some bread (masc.)', 'partitif', 'Je mange du pain le matin.', 'Je mange ___ pain le matin.', 'du'),
        ('part-02', 'de la musique', 'some music (fém.)', 'partitif', 'Elle écoute de la musique.', 'Elle écoute ___ musique.', 'de la'),
        ('part-03', 'de l\'eau', 'some water (vowel)', 'partitif', 'Je bois de l\'eau chaque jour.', 'Je bois ___ eau chaque jour.', 'de l\''),
        ('part-04', 'des légumes', 'some vegetables (pl.)', 'partitif', 'On mange des légumes ce soir.', 'On mange ___ légumes ce soir.', 'des'),
        ('part-05', 'pas de pain', 'no bread (neg.)', 'négation', 'Je ne mange pas de pain.', 'Je ne mange pas ___ pain.', 'de'),
        ('part-06', 'beaucoup de', 'a lot of (quantity)', 'quantité', 'Il y a beaucoup de monde ici.', 'Il y a beaucoup ___ monde ici.', 'de'),
        ('part-07', 'j\'aime le café', 'I like coffee (general)', 'goût', 'J\'aime le café mais je ne bois pas de café le soir.', 'J\'aime ___ café. (goût général)', 'le'),
        ('part-08', 'un verre de', 'a glass of (quantity)', 'quantité', 'Je prends un verre de vin avec le repas.', 'Je prends un verre ___ vin.', 'de'),
    ],
},

# ── G04 Les Pronoms COD et COI ─────────────────────────────────────────────
'les-pronoms-cod-coi': {
    'level':   'a2',
    'section': 'grammaire',
    'num':     'G04',
    'short':   'Les Pronoms COD/COI',
    'title':   'Les Pronoms Compléments — COD et COI',
    'subtitle': 'Remplacer le complément d\'objet direct et indirect pour éviter la répétition',
    'slides': [
        ('Les pronoms COD', None,
         '<p>Les pronoms COD remplacent un <b>complément d\'objet direct</b> (sans préposition) :</p>'
         '<table><tr><th>Personne</th><th>COD</th><th>Exemple</th></tr>'
         '<tr><td>1re sing.</td><td><b>me / m\'</b></td><td>Il me regarde.</td></tr>'
         '<tr><td>2e sing.</td><td><b>te / t\'</b></td><td>Je te vois.</td></tr>'
         '<tr><td>3e sing. m.</td><td><b>le / l\'</b></td><td>Je le connais. / Je l\'aime.</td></tr>'
         '<tr><td>3e sing. f.</td><td><b>la / l\'</b></td><td>Je la vois. / Je l\'aime.</td></tr>'
         '<tr><td>1re pl.</td><td><b>nous</b></td><td>Il nous invite.</td></tr>'
         '<tr><td>2e pl.</td><td><b>vous</b></td><td>Je vous comprends.</td></tr>'
         '<tr><td>3e pl.</td><td><b>les</b></td><td>Je les connais.</td></tr></table>'),
        ('Les pronoms COI', None,
         '<p>Les pronoms COI remplacent un <b>complément d\'objet indirect</b> (introduit par <i>à</i>) :</p>'
         '<table><tr><th>Personne</th><th>COI</th><th>Exemple</th></tr>'
         '<tr><td>1re sing.</td><td><b>me / m\'</b></td><td>Il me parle. (il parle à moi)</td></tr>'
         '<tr><td>2e sing.</td><td><b>te / t\'</b></td><td>Je te réponds.</td></tr>'
         '<tr><td>3e sing.</td><td><b>lui</b></td><td>Je lui téléphone. (à lui/elle)</td></tr>'
         '<tr><td>1re pl.</td><td><b>nous</b></td><td>Il nous écrit.</td></tr>'
         '<tr><td>2e pl.</td><td><b>vous</b></td><td>Je vous réponds.</td></tr>'
         '<tr><td>3e pl.</td><td><b>leur</b></td><td>Je leur envoie un message.</td></tr></table>'),
        ('Position du pronom', None,
         '<p>Le pronom se place <b>avant le verbe</b> (ou avant l\'auxiliaire au passé composé) :</p>'
         '<ul><li>Je <b>le</b> mange. (présent)</li>'
         '<li>Je <b>l\'</b>ai mangé. (passé composé)</li>'
         '<li>Je vais <b>le</b> manger. (futur proche)</li>'
         '<li>Mange-<b>le</b> ! (impératif affirmatif — exception !)</li>'
         '<li>Ne <b>le</b> mange pas ! (impératif négatif — avant le verbe)</li></ul>'),
        ('COD ou COI ?', None,
         '<p>Comment savoir si c\'est COD ou COI :</p>'
         '<ul><li><b>COD :</b> le verbe est suivi directement du nom — aimer <b>quelqu\'un</b>, voir <b>quelqu\'un</b></li>'
         '<li><b>COI :</b> le verbe est suivi de <i>à</i> + nom — parler <b>à quelqu\'un</b>, téléphoner <b>à quelqu\'un</b></li></ul>'
         '<table><tr><th>Verbes + COD (le/la/les)</th><th>Verbes + COI (lui/leur)</th></tr>'
         '<tr><td>voir, aimer, connaître, inviter</td><td>parler à, téléphoner à, écrire à</td></tr>'
         '<tr><td>prendre, manger, lire, regarder</td><td>répondre à, donner à, dire à</td></tr></table>'),
        ('Récapitulatif et exemples', None,
         '<p>Comparaison COD / COI avec les mêmes verbes :</p>'
         '<ul><li>J\'appelle Marie. → Je <b>l\'</b>appelle. (COD : appeler qqn)</li>'
         '<li>Je parle à Marie. → Je <b>lui</b> parle. (COI : parler à qqn)</li>'
         '<li>J\'invite mes amis. → Je <b>les</b> invite. (COD pl.)</li>'
         '<li>J\'écris à mes amis. → Je <b>leur</b> écris. (COI pl.)</li>'
         '<li>Il me voit. (COD) / Il me parle. (COI) — me/te/nous/vous sont identiques !</li></ul>'),
    ],
    'traps': [
        ('Je lui vois.', 'Je le/la vois.', '« Voir » prend un COD (sans préposition) → le/la, pas lui.'),
        ('Je les téléphone.', 'Je leur téléphone.', '« Téléphoner à » prend un COI → leur (pluriel), pas les.'),
        ('Je l\'ai le mangé.', 'Je l\'ai mangé.', 'Un seul pronom COD suffit : je l\'ai mangé, pas je l\'ai le mangé.'),
        ('Mange-le pas !', 'Ne le mange pas !', 'À l\'impératif négatif, le pronom se replace avant le verbe : ne le mange pas.'),
        ('Je lui connais.', 'Je le/la connais.', '« Connaître » prend un COD → le/la, pas lui.'),
    ],
    'summary': [
        ('COD sing.', 'me/te/le/la/l\' — devant verbe', 'Je le vois. / Je l\'aime.'),
        ('COD pl.', 'nous/vous/les — devant verbe', 'Je les connais.'),
        ('COI sing.', 'me/te/lui — verbe + à qqn', 'Je lui téléphone. (à lui/elle)'),
        ('COI pl.', 'nous/vous/leur — verbe + à qqn', 'Je leur écris. (à eux/elles)'),
        ('Position', 'avant le verbe (ou auxiliaire)', 'Je l\'ai vu. / Je vais le faire.'),
        ('Impératif +', 'après le verbe avec tiret', 'Regarde-le ! / Dis-lui !'),
    ],
    'ex1': ('Choisir le bon pronom', 'COD ou COI ?',
        [
            ('Je vois Marie. → Je ___ vois.', ['lui', 'la', 'leur', 'les'], 'la',
             'Voir + qqn = COD (sans à) → la (féminin singulier).'),
            ('Je parle à mes amis. → Je ___ parle.', ['les', 'le', 'leur', 'lui'], 'leur',
             'Parler à + qqn = COI → leur (pluriel).'),
            ('Il invite ses collègues. → Il ___ invite.', ['leur', 'lui', 'les', 'le'], 'les',
             'Inviter + qqn = COD → les (pluriel).'),
            ('Elle écrit à son frère. → Elle ___ écrit.', ['le', 'la', 'les', 'lui'], 'lui',
             'Écrire à + qqn = COI → lui (singulier).'),
        ]),
    'ex2': ('Remplacer par un pronom', 'Réécrivez en remplaçant le complément souligné.',
        [
            ('Je mange la pizza. → Je ___ mange.', 'la', 'Pizza est féminin singulier COD → la.'),
            ('Il appelle ses parents. → Il ___ appelle.', 'les', 'Parents est pluriel COD → les.'),
            ('Elle téléphone à sa mère. → Elle ___ téléphone.', 'lui', 'Téléphoner à + qqn = COI singulier → lui.'),
            ('Nous envoyons un message à nos amis. → Nous ___ envoyons un message.', 'leur', 'Envoyer à + qqn = COI pluriel → leur.'),
            ('Tu vois le film ? → Tu ___ vois ?', 'le', 'Film est masculin singulier COD → le.'),
        ]),
    'ex3': ('Identifier l\'erreur', 'Quelle phrase est incorrecte ?',
        [
            ('Laquelle est incorrecte ?',
             ['Je le vois.', 'Je lui parle.', 'Je lui vois.', 'Je leur écris.'],
             'Je lui vois.',
             'Voir + COD → le/la, pas lui. Lui est pour le COI (parler à qqn).'),
            ('Quelle phrase a une erreur de position ?',
             ['Je le mange.', 'Je l\'ai mangé.', 'Mange-le !', 'Je le mange pas.'],
             'Je le mange pas.',
             'À la forme négative, le pronom reste avant le verbe mais la négation encadre l\'ensemble : je ne le mange pas.'),
            ('Quel pronom est faux ?',
             ['Je les invite. (amis, pl.)', 'Je lui téléphone. (à Marie)', 'Je les téléphone. (à mes amis)', 'Je lui écris. (à Thomas)'],
             'Je les téléphone. (à mes amis)',
             'Téléphoner à + qqn = COI → leur (pluriel), pas les.'),
        ]),
    'game_desc': 'Maîtrisez les pronoms COD et COI en français !',
    'items': [
        ('cod-01', 'le / la', 'him / her (COD 3rd sing.)', 'COD', 'Je le vois tous les jours.', 'Je ___ vois tous les jours. (m.)', 'le'),
        ('cod-02', 'les', 'them (COD 3rd pl.)', 'COD', 'Je les connais bien.', 'Je ___ connais bien. (pl.)', 'les'),
        ('coi-01', 'lui', 'to him/her (COI 3rd sing.)', 'COI', 'Je lui téléphone ce soir.', 'Je ___ téléphone ce soir. (à elle)', 'lui'),
        ('coi-02', 'leur', 'to them (COI 3rd pl.)', 'COI', 'Je leur envoie un message.', 'Je ___ envoie un message. (à eux)', 'leur'),
        ('cod-03', 'l\'', 'him/her before vowel (COD)', 'élision', 'Je l\'aime beaucoup.', 'Je ___aime beaucoup. (élision)', 'l\''),
        ('pos-01', 'avant le verbe', 'before the verb', 'position', 'Je le vois. / Je l\'ai vu.', 'Je ___ vois. (pronom COD)', 'le'),
        ('imp-01', 'impératif+', 'after verb (imperative +)', 'position', 'Regarde-le ! / Dis-lui !', 'Regarde-___! (impératif affirmatif)', 'le'),
        ('coi-03', 'me / te', 'me / you (COD and COI)', 'identique', 'Il me voit. (COD) / Il me parle. (COI)', 'Il ___ parle. (COI, à moi)', 'me'),
    ],
},

}
