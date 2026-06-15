"""Français A2 — Rédaction batch 1: R01–R04."""

CHAPTERS = {

# ── R01 Raconter un Événement Passé ───────────────────────────────────────
'raconter-un-evenement': {
    'level':   'a2',
    'section': 'redaction',
    'num':     'R01',
    'short':   'Raconter un Événement',
    'title':   'Raconter un Événement Passé',
    'subtitle': 'Utiliser le passé composé et l\'imparfait pour raconter une histoire',
    'slides': [
        ('La structure d\'un récit', None,
         '<p>Pour raconter un événement passé, on utilise deux temps :</p>'
         '<ul><li><b>Passé composé</b> : les actions principales, ce qui s\'est passé</li>'
         '<li><b>Imparfait</b> : le contexte, la description, les habitudes</li></ul>'
         '<p>Structure d\'un bon récit :</p>'
         '<ol><li><b>Contexte</b> : quand, où, qui (imparfait)</li>'
         '<li><b>Événement principal</b> (passé composé)</li>'
         '<li><b>Réaction / suite</b> (passé composé)</li>'
         '<li><b>Conclusion / leçon</b></li></ol>'),
        ('Connecteurs de récit', None,
         '<p>Ces mots structurent et enrichissent votre récit :</p>'
         '<table><tr><th>Rôle</th><th>Connecteurs</th></tr>'
         '<tr><td><b>Début</b></td><td>Un jour… · L\'année dernière… · Il y a trois ans…</td></tr>'
         '<tr><td><b>Suite</b></td><td>Ensuite · Puis · Après · Alors</td></tr>'
         '<tr><td><b>Simultané</b></td><td>En même temps · Pendant ce temps</td></tr>'
         '<tr><td><b>Soudain</b></td><td>Tout à coup · Soudain · Brusquement</td></tr>'
         '<tr><td><b>Fin</b></td><td>Finalement · En fin de compte · Pour finir</td></tr>'
         '<tr><td><b>Cause</b></td><td>Parce que · Car · À cause de</td></tr></table>'),
        ('PC et imparfait dans le récit', None,
         '<p>La règle d\'or :</p>'
         '<p><b>Imparfait = décor</b> (ce qui durait, ce qui était habituel, la description)</p>'
         '<p><b>Passé composé = action</b> (ce qui s\'est passé, ce qui a changé)</p>'
         '<blockquote><p>Il <b>faisait</b> beau. (décor : imparfait)<br>'
         'Nous <b>nous promenions</b> dans le parc. (décor : imparfait)<br>'
         'Soudain, il <b>a commencé</b> à pleuvoir. (événement : PC)<br>'
         'Nous <b>avons couru</b> vers la voiture. (action : PC)</p></blockquote>'),
        ('Exprimer la durée et le moment', None,
         '<p>Pour préciser quand :</p>'
         '<ul><li><b>il y a + durée</b> : Il y a deux ans, je suis allé en France.</li>'
         '<li><b>pendant + durée</b> : J\'ai vécu en France pendant un an.</li>'
         '<li><b>depuis + durée</b> : Je parle français depuis trois ans. (présent → toujours vrai)</li>'
         '<li><b>en + durée</b> : J\'ai lu ce livre en deux jours. (durée pour accomplir qqch)</li></ul>'
         '<p>Piège : <b>depuis</b> → présent / <b>pendant</b> → passé composé</p>'),
        ('Modèle de récit', None,
         '<blockquote><p><b>Une journée inoubliable</b><br><br>'
         'L\'été dernier, je suis parti(e) en vacances en Bretagne avec ma famille.<br>'
         'Il <b>faisait</b> très beau et nous <b>étions</b> très contents.<br>'
         'Un jour, nous <b>avons décidé</b> de faire une randonnée en bord de mer.<br>'
         'Nous <b>marchions</b> depuis deux heures quand, tout à coup, nous <b>avons vu</b> un phoque !<br>'
         'C\'<b>était</b> incroyable. Nous <b>avons pris</b> beaucoup de photos.<br>'
         'Ce jour-là restera l\'un des meilleurs souvenirs de mes vacances.</p></blockquote>'),
    ],
    'traps': [
        ('Hier, je travaillais.', 'Hier, j\'ai travaillé.', '« Hier » marque une action terminée → passé composé.'),
        ('Il y a deux ans, j\'habitais en France pendant six mois.', 'Il y a deux ans, j\'ai habité en France pendant six mois.', '« Pendant » + durée terminée → passé composé.'),
        ('Je parle français depuis trois ans.', 'Correct !', 'Depuis + présent : l\'action dure encore. Pas de passé composé.'),
        ('Tout à coup, il pleuvait.', 'Tout à coup, il a plu.', 'Tout à coup = événement soudain → passé composé.'),
        ('Ensuite, je suis aller au cinéma.', 'Ensuite, je suis allé(e) au cinéma.', 'Aller → allé(e) (participe, avec accord si féminin). Pas « aller ».'),
    ],
    'summary': [
        ('Structure', 'contexte (imp.) → action (PC) → suite (PC) → conclusion', 'Il faisait beau. J\'ai décidé de sortir.'),
        ('Imparfait', 'décor, description, habitude, durée de fond', 'Il pleuvait. Je me sentais fatigué.'),
        ('Passé composé', 'action unique, événement, rupture', 'Soudain, il a appelé.'),
        ('Connecteurs', 'ensuite · puis · alors · tout à coup · finalement', 'Puis il a commencé à pleuvoir.'),
        ('Il y a', 'il y a + durée (point dans le passé)', 'Il y a deux ans, je suis parti.'),
        ('Pendant vs depuis', 'pendant + PC (terminé) / depuis + présent (continue)', 'J\'ai travaillé pendant 3 ans. / Je travaille depuis 3 ans.'),
    ],
    'ex1': ('Choisir le bon temps', 'Passé composé ou imparfait ?',
        [
            ('Quand j\'___ (être) enfant, j\'adorais la natation.', ['ai été', 'étais', 'suis', 'serai'], 'étais',
             'État / habitude dans le passé → imparfait : j\'étais.'),
            ('Soudain, le téléphone ___ (sonner).', ['sonnait', 'a sonné', 'sonne', 'sonnera'], 'a sonné',
             'Soudain = événement ponctuel → passé composé : a sonné.'),
            ('J\'___ (vivre) en Espagne pendant deux ans.', ['vivais', 'ai vécu', 'vis', 'vivrai'], 'ai vécu',
             'Pendant + durée terminée → passé composé : j\'ai vécu.'),
            ('Il ___ (pleuvoir) depuis le matin quand nous sommes sortis.', ['a plu', 'pleuvait', 'pleut', 'pluvait'], 'pleuvait',
             'Action en cours (décor) au moment d\'un autre événement → imparfait : il pleuvait.'),
        ]),
    'ex2': ('Compléter le récit', 'Mettez les verbes au bon temps.',
        [
            ('L\'année dernière, je ___ (visiter) Paris pour la première fois.', 'ai visité', 'Action terminée dans le passé → passé composé.'),
            ('Il ___ (faire) froid et il y ___ (avoir) beaucoup de monde dans les rues.', 'faisait … avait', 'Description du contexte → imparfait.'),
            ('Tout à coup, je ___ (voir) la Tour Eiffel !', 'ai vu', 'Événement soudain → passé composé.'),
            ('Je parle français ___ deux ans. (depuis/pendant)', 'depuis', 'Depuis + présent : l\'action continue.'),
            ('J\'ai étudié l\'espagnol ___ trois ans à l\'université. (depuis/pendant)', 'pendant', 'Pendant + passé : durée terminée.'),
        ]),
    'ex3': ('Identifier l\'erreur', 'Quelle phrase est incorrecte ?',
        [
            ('Laquelle est incorrecte ?',
             ['Hier, j\'ai travaillé.', 'Il faisait beau ce matin-là.', 'Soudain, il pleuvait.', 'J\'ai vécu ici pendant cinq ans.'],
             'Soudain, il pleuvait.',
             '« Soudain » = événement ponctuel → passé composé : soudain, il a plu.'),
            ('Quelle phrase avec « depuis » est correcte ?',
             ['J\'ai habité ici depuis cinq ans.', 'J\'habite ici depuis cinq ans.', 'J\'habitais ici depuis cinq ans maintenant.', 'J\'ai habitué ici depuis cinq ans.'],
             'J\'habite ici depuis cinq ans.',
             'Depuis + présent pour une action qui continue : j\'habite ici depuis cinq ans.'),
            ('Quel connecteur est mal placé ?',
             ['D\'abord, nous avons pris le train.', 'Ensuite, nous avons visité le musée.', 'Finalement, nous sommes rentrés.', 'Soudain, nous avons mangé une pizza.'],
             'Soudain, nous avons mangé une pizza.',
             '« Soudain / tout à coup » marque un événement inattendu et brusque. Manger une pizza n\'est pas un événement soudain. Utilisez « puis » ou « ensuite ».'),
        ]),
    'game_desc': 'Maîtrisez l\'art de raconter en français !',
    'items': [
        ('rec-01', 'imparfait = décor', 'imperfect = background', 'récit', 'Il faisait beau et nous étions contents.', 'Il ___ beau et nous étions contents. (décor)', 'faisait'),
        ('rec-02', 'PC = action', 'passé composé = event', 'récit', 'Soudain, il a commencé à pleuvoir.', 'Soudain, il a ___ à pleuvoir. (événement)', 'commencé'),
        ('rec-03', 'tout à coup', 'suddenly', 'connecteur', 'Tout à coup, le chien a aboyé.', '___ à coup, le chien a aboyé.', 'Tout'),
        ('rec-04', 'finalement', 'finally / in the end', 'connecteur', 'Finalement, nous avons trouvé un taxi.', '___, nous avons trouvé un taxi.', 'Finalement'),
        ('rec-05', 'il y a + durée', 'ago', 'temps', 'Il y a deux ans, je suis allé en Italie.', 'Il y a deux ___, je suis allé en Italie.', 'ans'),
        ('rec-06', 'pendant', 'for (completed duration)', 'durée', 'J\'ai travaillé là-bas pendant trois ans.', 'J\'ai travaillé là-bas ___ trois ans.', 'pendant'),
        ('rec-07', 'depuis', 'since / for (ongoing)', 'durée', 'J\'habite ici depuis cinq ans.', 'J\'habite ici ___ cinq ans.', 'depuis'),
        ('rec-08', 'ensuite', 'then / next', 'connecteur', 'Ensuite, nous avons visité le musée.', '___, nous avons visité le musée.', 'Ensuite'),
    ],
},

# ── R02 Décrire un Lieu ────────────────────────────────────────────────────
'decrire-un-lieu': {
    'level':   'a2',
    'section': 'redaction',
    'num':     'R02',
    'short':   'Décrire un Lieu',
    'title':   'Décrire un Lieu — Ville, Quartier, Maison',
    'subtitle': 'Écrire une description de lieu précise et vivante en français',
    'slides': [
        ('Décrire un lieu — structure', None,
         '<p>Une bonne description de lieu répond à ces questions :</p>'
         '<ul><li><b>Où ?</b> Localisation et situation géographique</li>'
         '<li><b>Comment ?</b> Apparence générale, ambiance</li>'
         '<li><b>Qu\'est-ce qu\'il y a ?</b> Ce qu\'on y trouve</li>'
         '<li><b>J\'aime / Je n\'aime pas</b> : votre opinion</li></ul>'
         '<p>Conseil : commencez par le général, puis zoomez sur les détails.</p>'),
        ('Localiser et situer', None,
         '<p>Pour situer le lieu :</p>'
         '<ul><li><b>Se trouver</b> : La ville se trouve dans le sud de la France.</li>'
         '<li><b>Être situé(e)</b> : L\'appartement est situé au troisième étage.</li>'
         '<li><b>Se trouver à + distance</b> : Le château se trouve à 5 km du village.</li>'
         '<li><b>Non loin de</b> : C\'est non loin de la gare.</li>'
         '<li><b>Au bord de</b> : C\'est une maison au bord de la mer.</li>'
         '<li><b>En plein centre</b> : Mon quartier est en plein centre-ville.</li></ul>'),
        ('Décrire l\'apparence et l\'ambiance', None,
         '<p>Adjectifs utiles pour décrire :</p>'
         '<p><b>Taille :</b> grand(e) · petit(e) · immense · minuscule · spacieux/spacieuse</p>'
         '<p><b>Aspect :</b> moderne · ancien(ne) · pittoresque · animé(e) · tranquille · bruyant(e)</p>'
         '<p><b>Ambiance :</b> agréable · sympathique · chaleureux/chaleureuse · accueillant(e)</p>'
         '<p>Structure : <b>C\'est un(e)… + adj.</b> ou <b>Il/Elle est… + adj.</b></p>'
         '<p>C\'est une ville <b>animée et moderne</b>, avec une <b>belle</b> architecture.</p>'),
        ('Il y a / on trouve / on peut', None,
         '<p>Pour décrire ce qu\'on trouve dans un lieu :</p>'
         '<ul><li><b>Il y a</b> + nom : Il y a un grand parc au centre.</li>'
         '<li><b>On trouve</b> + nom : On y trouve de nombreux restaurants.</li>'
         '<li><b>On peut</b> + infinitif : On peut visiter le musée gratuitement.</li>'
         '<li><b>Il n\'y a pas de</b> + nom : Il n\'y a pas de supermarché dans le village.</li></ul>'),
        ('Modèle de description', None,
         '<blockquote><p><b>Mon quartier</b><br><br>'
         'J\'habite dans le quartier de la Croix-Rousse, à Lyon, en France.<br>'
         'C\'est un quartier <b>animé et pittoresque</b>, situé sur une colline.<br>'
         'Il y a de nombreux cafés, restaurants et petits commerces.<br>'
         'On peut aussi visiter un marché le dimanche matin.<br>'
         'J\'aime beaucoup ce quartier parce qu\'il est <b>très vivant</b> mais aussi <b>calme</b> la nuit.<br>'
         'Le seul inconvénient, c\'est qu\'il y a beaucoup de touristes en été.</p></blockquote>'),
    ],
    'traps': [
        ('Ma ville est grande et animé.', 'Ma ville est grande et animée.', 'Ville est féminin → animée (avec -e).'),
        ('Il y a un musée dans mon ville.', 'Il y a un musée dans ma ville.', 'Ville est féminin → ma ville (pas mon).'),
        ('C\'est une ville très vivante et qui est moderne aussi.', 'C\'est une ville très vivante et moderne.', 'Simplifiez : deux adjectifs côte à côte, pas besoin de « qui est ».'),
        ('Mon appartement se situe dans le quatrième étage.', 'Mon appartement se situe au quatrième étage.', 'Au + étage (pas dans le étage). « Au » = à + le.'),
        ('J\'habite à le centre-ville.', 'J\'habite au centre-ville. / J\'habite en centre-ville.', 'À + le = au : j\'habite au centre-ville.'),
    ],
    'summary': [
        ('Localisation', 'se trouver / être situé(e) / au bord de / en plein centre', 'La ville se trouve dans le nord.'),
        ('Apparence', 'C\'est un(e) + adj. / Il est + adj.', 'C\'est un quartier animé et moderne.'),
        ('Contenu', 'Il y a / on trouve / on peut', 'Il y a un grand marché le dimanche.'),
        ('Accord', 'adjectifs accordés avec le nom décrit', 'une ville animée / un quartier tranquille'),
        ('Opinion', 'J\'aime… parce que / Le seul inconvénient…', 'J\'aime ce quartier parce qu\'il est calme.'),
        ('Étage', 'au + ordinal + étage', 'Mon appartement est au troisième étage.'),
    ],
    'ex1': ('Choisir le bon mot', 'Sélectionnez la réponse correcte.',
        [
            ('Mon quartier est très ___. (vivant, plein d\'activité)', ['animé', 'animée', 'ennuyeux', 'bruyante'], 'animé',
             'Quartier est masculin → animé (sans -e).'),
            ('La ville ___ dans le sud de la France.', ['est situées', 'se trouve', 'trouve', 'située'], 'se trouve',
             'Pour localiser : la ville se trouve + lieu. Ou : est située (mais pas « se situe » sans pronom).'),
            ('Il y a ___ restaurants dans mon quartier.', ['le', 'de', 'des', 'de la'], 'des',
             'Il y a + des + nom pluriel : il y a des restaurants.'),
            ('J\'habite ___ deuxième étage.', ['dans le', 'au', 'en', 'à le'], 'au',
             'À + le = au : j\'habite au deuxième étage.'),
        ]),
    'ex2': ('Compléter la description', 'Remplissez les espaces.',
        [
            ('C\'est une ville ___ et ___. (grand / animé, accordés)', 'grande et animée', 'Ville est féminin → grande (f.) et animée (f.).'),
            ('La maison ___ au bord de la mer.', 'se trouve / est située', 'Se trouver ou être situé(e) : la maison se trouve au bord de la mer.'),
            ('___ un grand parc à côté de chez moi.', 'Il y a', 'Il y a + nom : il y a un grand parc.'),
            ('On ___ visiter le château gratuitement.', 'peut', 'On peut + infinitif pour décrire une possibilité.'),
            ('J\'aime ce quartier ___ il est calme et verdoyant.', 'parce que / car', 'Pour exprimer la cause : parce que / car.'),
        ]),
    'ex3': ('Identifier l\'erreur', 'Quelle phrase est incorrecte ?',
        [
            ('Laquelle est incorrecte ?',
             ['C\'est une ville animée.', 'Mon quartier est tranquille.', 'Il y a un beau parc.', 'La plage est grande et magnifique.'],
             'La plage est grande et magnifique.',
             'En fait toutes ces phrases sont correctes. Reformulation correcte : quelle phrase a un accord erroné ?'),
            ('Quel accord est faux ?',
             ['une ville animée', 'un quartier tranquille', 'une maison moderne', 'un appartement spacieuse'],
             'un appartement spacieuse',
             'Appartement est masculin → spacieux (pas spacieuse, qui est féminin).'),
            ('Quelle localisation est correcte ?',
             ['J\'habite dans le troisième étage.', 'J\'habite au troisième étage.', 'J\'habite en le troisième étage.', 'J\'habite à le troisième étage.'],
             'J\'habite au troisième étage.',
             'Au + numéro ordinal + étage : au troisième étage. « Dans le » et « à le » sont incorrects.'),
        ]),
    'game_desc': 'Maîtrisez la description de lieux en français !',
    'items': [
        ('lieu-01', 'se trouver',   'to be located',  'localisation', 'La ville se trouve dans le sud.',      'La ville ___ dans le sud.',           'se trouve'),
        ('lieu-02', 'animé(e)',     'lively',         'adjectif',     'C\'est un quartier animé et vivant.',  'C\'est un quartier ___ et vivant.',   'animé'),
        ('lieu-03', 'il y a',       'there is/are',   'structure',    'Il y a un grand parc au centre.',      '___ un grand parc au centre.',        'Il y a'),
        ('lieu-04', 'on peut',      'one can',        'structure',    'On peut visiter le musée gratuitement.','___ visiter le musée gratuitement.',  'On peut'),
        ('lieu-05', 'au troisième étage','on the 3rd floor','lieu',  'Mon appartement est au troisième étage.','Mon appartement est ___ troisième étage.','au'),
        ('lieu-06', 'pittoresque',  'picturesque',    'adjectif',     'C\'est un village pittoresque et calme.','C\'est un village ___ et calme.',    'pittoresque'),
        ('lieu-07', 'parce que',    'because',        'opinion',      'J\'aime ce quartier parce qu\'il est calme.','J\'aime ce quartier ___ qu\'il est calme.','parce'),
        ('lieu-08', 'au bord de',   'at the edge of / by','localisation','Une maison au bord de la mer.',    'Une maison ___ bord de la mer.',      'au'),
    ],
},

# ── R03 Écrire une Carte Postale ───────────────────────────────────────────
'ecrire-une-carte-postale': {
    'level':   'a2',
    'section': 'redaction',
    'num':     'R03',
    'short':   'La Carte Postale',
    'title':   'Écrire une Carte Postale — En Vacances',
    'subtitle': 'Rédiger une carte postale de vacances en français : lieu, activités, temps',
    'slides': [
        ('La structure d\'une carte postale', None,
         '<p>Une carte postale de vacances a une structure très codifiée :</p>'
         '<ol><li><b>Lieu et date</b> : [ville], le [date]</li>'
         '<li><b>Salutation</b> : Cher Thomas, / Chère Marie, / Bonjour !</li>'
         '<li><b>Lieu</b> : Je suis à… / Nous sommes à…</li>'
         '<li><b>Météo</b> : Il fait beau / chaud / beau temps</li>'
         '<li><b>Activités</b> : Nous avons visité… / On fait…</li>'
         '<li><b>Appréciation</b> : C\'est magnifique ! / On adore !</li>'
         '<li><b>Clôture</b> : À bientôt ! / Grosses bises !</li>'
         '<li><b>Signature</b></li></ol>'),
        ('Décrire les vacances', None,
         '<p>Expressions utiles pour décrire vos vacances :</p>'
         '<p><b>Lieu :</b></p>'
         '<ul><li>Je suis en vacances à… / en… / au…</li>'
         '<li>Nous passons une semaine à…</li>'
         '<li>C\'est un endroit magnifique / superbe / incroyable.</li></ul>'
         '<p><b>Activités :</b></p>'
         '<ul><li>Nous avons visité + monument (PC)</li>'
         '<li>On fait de la randonnée / de la natation.</li>'
         '<li>Hier, nous sommes allés…</li></ul>'),
        ('La météo et les sensations', None,
         '<p>Pour parler du temps et de ses sensations :</p>'
         '<p><b>Météo :</b> Il fait beau / chaud / froid. · Il y a du soleil. · Le temps est magnifique.</p>'
         '<p><b>Sensations :</b></p>'
         '<ul><li>Je me sens vraiment bien / détendu(e) / reposé(e).</li>'
         '<li>Nous sommes ravis / contents / enchantés.</li>'
         '<li>C\'est une expérience inoubliable !</li>'
         '<li>La nourriture est délicieuse / excellente.</li></ul>'),
        ('Parler des projets', None,
         '<p>Pour mentionner ce qu\'on va faire :</p>'
         '<ul><li><b>Futur proche :</b> Demain, on va visiter le château.</li>'
         '<li><b>Futur simple :</b> Après-demain, nous irons à la plage.</li>'
         '<li>On a prévu de + infinitif : On a prévu de faire une excursion.</li></ul>'
         '<p>Clôtures affectueuses :</p>'
         '<ul><li>Grosses bises ! / Bisous à tous !</li>'
         '<li>À très bientôt ! / On pense à vous !</li>'
         '<li>Je vous embrasse très fort !</li></ul>'),
        ('Modèle de carte postale', None,
         '<blockquote><p>Barcelone, le 15 juillet 2026<br><br>'
         'Chère Marie,<br><br>'
         'Je suis en vacances à Barcelone depuis trois jours et c\'est absolument magnifique !<br>'
         'Il fait très beau et chaud. Hier, nous avons visité la Sagrada Família — c\'était impressionnant !<br>'
         'La cuisine espagnole est délicieuse.<br>'
         'Demain, on va aller sur la plage de la Barceloneta.<br>'
         'Tu me manques !<br><br>'
         'Grosses bises,<br>'
         'Emma</p></blockquote>'),
    ],
    'traps': [
        ('Je suis à les vacances.', 'Je suis en vacances.', '« En vacances » est une expression fixe — pas d\'article, pas de préposition différente.'),
        ('On a visité la Sagrada Família hier.', 'Hier, on a visité la Sagrada Família.', 'Stylistiquement, les marqueurs de temps se placent en début de phrase dans les cartes postales.'),
        ('Le temps est beau.', 'Il fait beau. / Le temps est beau.', 'Les deux sont correctes ! « Il fait beau » est plus naturel et courant à l\'oral.'),
        ('Cher Marie,', 'Chère Marie,', 'Marie est féminin → chère (avec -e).'),
        ('À bientôt Thomas !', 'À bientôt, Thomas !', 'Une virgule sépare la formule de congé du prénom.'),
    ],
    'summary': [
        ('Structure', 'ville + date → salut → lieu+météo → activités → projets → clôture', 'Paris, le 10 juin. Chère Léa, Je suis à Paris…'),
        ('Lieu', 'je suis en vacances à/en/au + lieu', 'Je suis à Rome. / Nous sommes en Italie.'),
        ('Météo', 'Il fait beau/chaud. / Le temps est magnifique.', 'Il fait très chaud ici !'),
        ('Activités', 'PC pour hier / futur proche pour demain', 'Hier, on a visité… / Demain, on va aller…'),
        ('En vacances', 'expression fixe : en vacances (sans article)', 'Je suis en vacances depuis lundi.'),
        ('Clôture', 'Grosses bises ! / Bisous à tous ! / Je vous embrasse.', 'Grosses bises, Emma'),
    ],
    'ex1': ('Choisir la bonne option', 'Sélectionnez la réponse correcte.',
        [
            ('Je suis ___ vacances à Nice.', ['à les', 'aux', 'en', 'de'], 'en',
             '« En vacances » est une expression figée. Pas d\'article.'),
            ('___ Thomas, (salutation, masculin)', ['Cher', 'Chère', 'Chéri', 'Bien cher'], 'Cher',
             'Thomas est masculin → Cher Thomas, (sans -e).'),
            ('Hier, nous ___ la tour Eiffel.', ['visitons', 'avons visité', 'allons visiter', 'visiitions'], 'avons visité',
             '« Hier » = action terminée → passé composé : nous avons visité.'),
            ('Demain, on ___ à la plage.', ['est allé', 'allait', 'va aller', 'allons'], 'va aller',
             '« Demain » = futur → futur proche : on va aller.'),
        ]),
    'ex2': ('Compléter la carte postale', 'Remplissez les espaces.',
        [
            ('___ Marie, (salutation, féminin)', 'Chère', 'Féminin → Chère (avec -e).'),
            ('Je suis ___ vacances à Rome depuis lundi.', 'en', '« En vacances » : expression figée sans article.'),
            ('Il ___ très beau et chaud. (météo)', 'fait', 'Il fait beau / chaud.'),
            ('Hier, nous ___ le Colisée. (visiter, PC)', 'avons visité', 'Hier → passé composé.'),
            ('___ bises, Emma ! (clôture affectueuse)', 'Grosses', 'Grosses bises ! est la clôture la plus commune.'),
        ]),
    'ex3': ('Identifier l\'erreur', 'Quelle phrase est incorrecte ?',
        [
            ('Laquelle est incorrecte ?',
             ['Je suis en vacances.', 'Cher Thomas,', 'Chère Marie,', 'Cher Lucie,'],
             'Cher Lucie,',
             'Lucie est féminin → Chère Lucie, (avec -e).'),
            ('Quel temps verbal est faux ?',
             ['Hier, on a visité le musée.', 'Il y a deux jours, nous sommes allés à la plage.', 'Demain, on va faire une randonnée.', 'Hier, on allait au marché.'],
             'Hier, on allait au marché.',
             '« Hier » avec une action terminée → passé composé : hier, on est allé(s) au marché.'),
            ('Quelle clôture est la plus appropriée pour une carte postale à un ami ?',
             ['Veuillez agréer mes salutations distinguées.', 'Cordialement,', 'Grosses bises !', 'Bien à vous,'],
             'Grosses bises !',
             'Pour une carte postale à un ami, « Grosses bises ! » est la formule la plus naturelle et affectueuse.'),
        ]),
    'game_desc': 'Maîtrisez la rédaction d\'une carte postale en français !',
    'items': [
        ('cp-01', 'en vacances',    'on holiday',     'expression', 'Je suis en vacances depuis lundi.',       'Je suis ___ vacances depuis lundi.',      'en'),
        ('cp-02', 'chère Marie',    'dear Marie (f.)', 'salutation', 'Chère Marie, je t\'écris de Venise !',    '___ Marie, je t\'écris de Venise !',      'Chère'),
        ('cp-03', 'il fait beau',   'the weather is nice','météo', 'Il fait beau et chaud ici !',               'Il ___ beau et chaud ici !',              'fait'),
        ('cp-04', 'on a visité',    'we visited (PC)', 'activité',  'Hier, on a visité le Louvre.',             'Hier, on ___ le Louvre.',                 'a visité'),
        ('cp-05', 'on va aller',    'we are going to go','projet',  'Demain, on va aller à la plage.',          'Demain, on ___ à la plage.',              'va aller'),
        ('cp-06', 'c\'est magnifique','it\'s magnificent','appréciation','C\'est magnifique, tu dois venir !',  'C\'est ___, tu dois venir !',             'magnifique'),
        ('cp-07', 'grosses bises',  'big kisses (closing)','clôture','Grosses bises, Emma !',                   '___ bises, Emma !',                       'Grosses'),
        ('cp-08', 'tu me manques',  'I miss you',     'sentiment',  'Tu me manques beaucoup !',                  'Tu ___ manques beaucoup !',               'me'),
    ],
},

# ── R04 Écrire un Courriel Formel ─────────────────────────────────────────
'ecrire-un-courriel-formel': {
    'level':   'a2',
    'section': 'redaction',
    'num':     'R04',
    'short':   'Le Courriel Formel',
    'title':   'Écrire un Courriel Formel',
    'subtitle': 'Réserver, demander des informations et faire une réclamation par courriel',
    'slides': [
        ('La structure du courriel formel', None,
         '<p>Un courriel formel a des conventions strictes :</p>'
         '<ol><li><b>Objet</b> : Court et précis — « Réservation chambre n° 12 »</li>'
         '<li><b>Salutation</b> : Madame, / Monsieur, / Madame, Monsieur,</li>'
         '<li><b>Formule d\'introduction</b> : Je me permets de vous écrire au sujet de…</li>'
         '<li><b>Corps</b> : L\'information principale — clair et bref</li>'
         '<li><b>Demande / action</b> : Je vous serais reconnaissant(e) de bien vouloir…</li>'
         '<li><b>Formule de politesse</b> : Veuillez agréer…</li>'
         '<li><b>Signature</b> : Prénom NOM</li></ol>'),
        ('Formules d\'introduction', None,
         '<p>Selon la situation :</p>'
         '<ul><li><b>Réservation :</b> Je souhaite réserver… / Je voudrais réserver…</li>'
         '<li><b>Demande d\'information :</b> Je vous contacte afin d\'obtenir des informations sur…</li>'
         '<li><b>Réclamation :</b> Suite à ma commande du…, je me permets de vous signaler…</li>'
         '<li><b>Candidature :</b> Je vous adresse ma candidature pour le poste de…</li></ul>'
         '<p>Le conditionnel (voudrais, souhaiterais) est plus poli que le présent (veux).</p>'),
        ('Faire une demande polie', None,
         '<p>Tournures polies pour faire une demande :</p>'
         '<ul><li><b>Pourriez-vous</b> + infinitif ? (très poli)</li>'
         '<li><b>Je vous serais reconnaissant(e) de</b> + infinitif (très formel)</li>'
         '<li><b>Je vous demande de bien vouloir</b> + infinitif (formel)</li>'
         '<li><b>Il serait possible de</b> + infinitif ? (poli)</li></ul>'
         '<p>Exemple : Pourriez-vous m\'envoyer votre catalogue ?<br>'
         'Je vous serais reconnaissante de bien vouloir me confirmer la réservation.</p>'),
        ('Formules de politesse finales', None,
         '<p>La formule de clôture formelle est longue mais codifiée :</p>'
         '<p><b>Standard :</b><br>'
         'Veuillez agréer, Madame / Monsieur, l\'expression de mes salutations distinguées.</p>'
         '<p><b>Simplifié (acceptable) :</b><br>'
         'Dans l\'attente de votre réponse, je vous adresse mes cordiales salutations.</p>'
         '<p><b>Très simple (emails professionnels courants) :</b><br>'
         'Cordialement,<br>Prénom NOM</p>'
         '<p>À l\'A2, « Cordialement » ou « Dans l\'attente de votre réponse, cordialement » suffisent.</p>'),
        ('Modèle : réserver un hôtel', None,
         '<blockquote><p><b>Objet :</b> Réservation chambre double — 20 au 23 août 2026<br><br>'
         'Madame, Monsieur,<br><br>'
         'Je vous contacte afin de réserver une chambre double pour trois nuits, du 20 au 23 août 2026.<br>'
         'Je voyagerai avec une personne. Pourriez-vous me confirmer la disponibilité et le tarif par nuit ?<br>'
         'Si possible, je souhaiterais une chambre avec vue sur la mer.<br><br>'
         'Dans l\'attente de votre réponse, je vous adresse mes cordiales salutations.<br><br>'
         'Marie DUPONT<br>'
         'marie.dupont@email.fr</p></blockquote>'),
    ],
    'traps': [
        ('Cher Monsieur,', 'Monsieur,', 'Dans un courriel formel en français, on n\'utilise pas « Cher/Chère » avec un inconnu. Juste « Madame, » ou « Monsieur, ».'),
        ('Je veux réserver une chambre.', 'Je souhaite réserver / Je voudrais réserver une chambre.', 'Dans un courriel formel, « je veux » est trop direct. Utilisez le conditionnel ou « souhaiter ».'),
        ('Cordialement, Marie', 'Cordialement,\nMarie DUPONT', 'La signature formelle inclut nom + prénom. Et la clôture est sur une ligne séparée.'),
        ('En attendant votre réponse, cordialement.', 'Dans l\'attente de votre réponse, je vous adresse mes cordiales salutations.', 'La formule complète est plus correcte à l\'écrit formel.'),
        ('Je vous enverrai mes coordonnées.', 'Correct !', 'Le futur simple est acceptable dans un courriel formel pour s\'engager à une action.'),
    ],
    'summary': [
        ('Structure', 'Objet → salut → intro → corps → demande → clôture → signature', 'Madame, / Je souhaite réserver… / Cordialement,'),
        ('Salutation', 'Madame, / Monsieur, (pas Cher/Chère)', 'Madame, Monsieur, (si inconnu)'),
        ('Politesse', 'conditionnel → voudrais · souhaiterais · pourriez-vous', 'Je voudrais réserver… / Pourriez-vous…'),
        ('Demande', 'Pourriez-vous / Je vous serais reconnaissant(e) de', 'Pourriez-vous me confirmer ?'),
        ('Clôture', 'Cordialement, / Dans l\'attente de votre réponse,', 'Cordialement, Marie DUPONT'),
        ('Objet', 'court, précis, sans article', 'Objet : Réservation chambre — 20 août'),
    ],
    'ex1': ('Choisir la bonne formule', 'Sélectionnez la réponse correcte.',
        [
            ('Quelle salutation est correcte dans un courriel formel à un inconnu ?', ['Cher Monsieur,', 'Monsieur,', 'Bonjour,', 'Salut,'], 'Monsieur,',
             'En français formel, la salutation est simplement « Madame, » ou « Monsieur, » sans « Cher/Chère ».'),
            ('Comment formuler une demande polie au conditionnel ?', ['Je veux une chambre.', 'Je voudrais réserver une chambre.', 'Donne-moi une chambre.', 'Je voulais une chambre.'], 'Je voudrais réserver une chambre.',
             'Le conditionnel (voudrais) rend la demande plus polie que le présent (veux).'),
            ('Quelle clôture est adaptée à un courriel professionnel simple ?', ['Grosses bises,', 'À bientôt !', 'Cordialement,', 'Salut,'], 'Cordialement,',
             '« Cordialement, » est la clôture standard pour un courriel professionnel ou formel.'),
            ('Quelle formule de demande est la plus polie ?', ['Je veux que vous répondiez.', 'Répondez-moi.', 'Pourriez-vous me répondre ?', 'Répondez s\'il vous plaît.'], 'Pourriez-vous me répondre ?',
             'Le conditionnel interrogatif (Pourriez-vous…) est la formule de demande la plus polie.'),
        ]),
    'ex2': ('Compléter le courriel', 'Remplissez les espaces.',
        [
            ('___, Monsieur, (salutation formelle)', 'Madame', 'Madame, Monsieur, quand on ne connaît pas le genre du destinataire.'),
            ('Je ___ réserver une chambre double. (vouloir, conditionnel)', 'voudrais', 'Vouloir au conditionnel : je voudrais.'),
            ('___ -vous me confirmer la disponibilité ? (pouvoir, conditionnel)', 'Pourriez', 'Pouvoir au conditionnel interrogatif : pourriez-vous ?'),
            ('Dans l\'___ de votre réponse, cordialement.', 'attente', 'La formule : Dans l\'attente de votre réponse, cordialement.'),
            ('___, Marie DUPONT (clôture simple)', 'Cordialement', '« Cordialement, » est la clôture formelle standard.'),
        ]),
    'ex3': ('Identifier l\'erreur', 'Quelle phrase est incorrecte ?',
        [
            ('Laquelle est incorrecte pour un courriel formel ?',
             ['Madame,', 'Je voudrais réserver une chambre.', 'Cher Monsieur,', 'Cordialement,'],
             'Cher Monsieur,',
             'En français formel avec un inconnu, on dit simplement « Monsieur, » (pas « Cher Monsieur, »).'),
            ('Quelle formule de demande est incorrecte ?',
             ['Pourriez-vous m\'envoyer votre catalogue ?', 'Je vous serais reconnaissant de bien vouloir répondre.', 'Donne-moi le catalogue.', 'Auriez-vous la gentillesse de me répondre ?'],
             'Donne-moi le catalogue.',
             'L\'impératif direct est trop brusque dans un courriel formel. Utilisez le conditionnel.'),
            ('Quelle clôture est trop familière pour un courriel formel ?',
             ['Cordialement,', 'Dans l\'attente de votre réponse, cordiales salutations.', 'Grosses bises,', 'Veuillez agréer mes salutations.'],
             'Grosses bises,',
             '« Grosses bises » est une formule très familière, réservée aux amis proches ou à la famille.'),
        ]),
    'game_desc': 'Maîtrisez l\'écriture du courriel formel en français !',
    'items': [
        ('form-01', 'Madame, Monsieur,','Dear Sir/Madam (formal)','salutation','Madame, Monsieur, je vous contacte…','___, je vous contacte… (formel)',   'Madame'),
        ('form-02', 'je voudrais',    'I would like (polite)',   'politesse', 'Je voudrais réserver une chambre.', 'Je ___ réserver une chambre.',      'voudrais'),
        ('form-03', 'pourriez-vous ?','could you? (formal req.)','demande',   'Pourriez-vous me confirmer la date ?','___ -vous me confirmer la date ?', 'Pourriez'),
        ('form-04', 'je souhaite',    'I wish to / I would like','politesse', 'Je souhaite obtenir des informations.','Je ___ obtenir des informations.', 'souhaite'),
        ('form-05', 'cordialement',   'kind regards (closing)',  'clôture',   'Cordialement, Marie DUPONT',         '___, Marie DUPONT',                 'Cordialement'),
        ('form-06', 'dans l\'attente','awaiting (your reply)',   'clôture',   'Dans l\'attente de votre réponse,',  '___ l\'attente de votre réponse,',  'Dans'),
        ('form-07', 'l\'objet',       'the subject (email)',     'structure', 'Objet : Réservation chambre double', '___ : Réservation chambre double',   'Objet'),
        ('form-08', 'je vous serais reconnaissant(e)','I would be grateful','demande','Je vous serais reconnaissante de répondre.','Je vous ___ reconnaissante de répondre.','serais'),
    ],
},

}
