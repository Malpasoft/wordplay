"""Français A2 — Grammaire batch 2: G05–G08."""

CHAPTERS = {

# ── G05 Le Futur Simple ────────────────────────────────────────────────────
'le-futur-simple': {
    'level':   'a2',
    'section': 'grammaire',
    'num':     'G05',
    'short':   'Le Futur Simple',
    'title':   'Le Futur Simple — Parler de l\'Avenir',
    'subtitle': 'Formation du futur simple et distinction avec le futur proche',
    'slides': [
        ('Qu\'est-ce que le futur simple ?', None,
         '<p>Le futur simple exprime :</p>'
         '<ul><li>Une <b>action future</b> : Demain, il pleuvra.</li>'
         '<li>Une <b>prédiction</b> : Tu seras heureux.</li>'
         '<li>Une <b>promesse</b> : Je t\'appellerai ce soir.</li>'
         '<li>Une <b>instruction formelle</b> : Vous tournerez à gauche.</li></ul>'
         '<p>Différence avec le futur proche (<i>aller + inf.</i>) : le futur simple est souvent plus lointain ou plus formel. À l\'oral, le futur proche est plus fréquent.</p>'),
        ('Formation — verbes réguliers', None,
         '<p>Base = <b>infinitif</b> (les -RE perdent le -e final) + terminaisons :</p>'
         '<table><tr><th>Sujet</th><th>Terminaison</th><th>Parler</th><th>Finir</th><th>Vendre</th></tr>'
         '<tr><td>je</td><td>-ai</td><td>parlerai</td><td>finirai</td><td>vendrai</td></tr>'
         '<tr><td>tu</td><td>-as</td><td>parleras</td><td>finiras</td><td>vendras</td></tr>'
         '<tr><td>il/elle</td><td>-a</td><td>parlera</td><td>finira</td><td>vendra</td></tr>'
         '<tr><td>nous</td><td>-ons</td><td>parlerons</td><td>finirons</td><td>vendrons</td></tr>'
         '<tr><td>vous</td><td>-ez</td><td>parlerez</td><td>finirez</td><td>vendrez</td></tr>'
         '<tr><td>ils/elles</td><td>-ont</td><td>parleront</td><td>finiront</td><td>vendront</td></tr></table>'),
        ('Futurs irréguliers', None,
         '<p>Les principaux verbes avec un <b>radical irrégulier</b> (les terminaisons restent identiques) :</p>'
         '<table><tr><th>Infinitif</th><th>Radical</th><th>Exemple</th></tr>'
         '<tr><td>être</td><td>ser-</td><td>je serai</td></tr>'
         '<tr><td>avoir</td><td>aur-</td><td>tu auras</td></tr>'
         '<tr><td>aller</td><td>ir-</td><td>il ira</td></tr>'
         '<tr><td>faire</td><td>fer-</td><td>nous ferons</td></tr>'
         '<tr><td>pouvoir</td><td>pourr-</td><td>vous pourrez</td></tr>'
         '<tr><td>vouloir</td><td>voudr-</td><td>ils voudront</td></tr>'
         '<tr><td>venir</td><td>viendr-</td><td>elle viendra</td></tr>'
         '<tr><td>savoir</td><td>saur-</td><td>je saurai</td></tr></table>'),
        ('Futur simple vs. futur proche', None,
         '<table><tr><th>Futur proche (aller + inf.)</th><th>Futur simple</th></tr>'
         '<tr><td>Action imminente ou certaine</td><td>Action plus lointaine ou formelle</td></tr>'
         '<tr><td>Je vais manger maintenant.</td><td>Je mangerai chez toi vendredi.</td></tr>'
         '<tr><td>Plus fréquent à l\'oral</td><td>Plus fréquent à l\'écrit</td></tr>'
         '<tr><td>Je vais partir bientôt.</td><td>Un jour, je partirai pour Paris.</td></tr></table>'
         '<p>Les deux formes sont souvent interchangeables dans la conversation courante.</p>'),
        ('Marqueurs du futur', None,
         '<p>Ces marqueurs temporels accompagnent souvent le futur simple :</p>'
         '<ul><li><b>demain</b> · <b>après-demain</b></li>'
         '<li><b>la semaine prochaine</b> · <b>le mois prochain</b> · <b>l\'année prochaine</b></li>'
         '<li><b>dans + durée</b> : dans deux jours · dans un an</li>'
         '<li><b>un jour</b> · <b>bientôt</b> · <b>plus tard</b></li></ul>'
         '<p>Rappel : avec <b>quand</b> + futur (différence avec l\'anglais !)<br>'
         'Quand tu <b>arriveras</b>, appelle-moi. (pas <i>when you arrive</i>)</p>'),
    ],
    'traps': [
        ('Je vais parlerai demain.', 'Je parlerai demain. / Je vais parler demain.', 'Il ne faut pas mélanger futur proche et futur simple.'),
        ('Quand il arrive, je lui dirai.', 'Quand il arrivera, je lui dirai.', 'En français, « quand » + futur (pas présent) quand le verbe principal est au futur.'),
        ('Je serai allé demain.', 'J\'irai demain.', 'Le futur antérieur (serai allé) n\'est pas nécessaire ici. Utilisez le futur simple.'),
        ('Nous ferons pas de bruit.', 'Nous ne ferons pas de bruit.', 'La négation encadre le verbe conjugué : ne…pas autour de ferons.'),
        ('Il vendrera sa voiture.', 'Il vendra sa voiture.', 'Vendre → vendre (drop -e) → vendrai, vendras, vendra… Pas de -r- double.'),
    ],
    'summary': [
        ('Formation', 'infinitif (−e pour -RE) + -ai/-as/-a/-ons/-ez/-ont', 'parler→parlerai · vendre→vendrai'),
        ('Irrég.', 'être→ser- · avoir→aur- · aller→ir- · faire→fer-', 'je serai · tu auras · il ira'),
        ('Irrég.', 'pouvoir→pourr- · vouloir→voudr- · venir→viendr-', 'je pourrai · il voudra · elle viendra'),
        ('Vs proche', 'futur proche = immédiat/oral; simple = lointain/formel', 'Je vais partir. / Je partirai en juin.'),
        ('Quand', 'quand + futur (pas présent) si action future', 'Quand il arrivera, nous partirons.'),
        ('Marqueurs', 'demain · la semaine prochaine · dans + durée', 'Dans trois jours, je serai à Paris.'),
    ],
    'ex1': ('Choisir la bonne forme', 'Sélectionnez la forme correcte du futur simple.',
        [
            ('Demain, il ___ (faire) beau.', ['faisera', 'fera', 'ferait', 'fait'], 'fera',
             'Faire → radical fer- → il fera. Radical irrégulier, terminaison régulière.'),
            ('Nous ___ (partir) en vacances la semaine prochaine.', ['partirons', 'partierons', 'allons partir', 'partissons'], 'partirons',
             'Partir → partir (inf.) + -ons → partirons. Terminaisons régulières sur base infinitive.'),
            ('Quand tu ___ (arriver), appelle-moi.', ['arrives', 'es arrivé', 'arriveras', 'arrivais'], 'arriveras',
             'En français, « quand » + futur si l\'action principale est au futur : quand tu arriveras.'),
            ('Elle ___ (avoir) vingt ans l\'année prochaine.', ['aura', 'avra', 'sera', 'aurait'], 'aura',
             'Avoir → radical aur- → elle aura. Irrégulier.'),
        ]),
    'ex2': ('Conjuguer au futur simple', 'Donnez la forme correcte.',
        [
            ('Tu ___ (être) content de cette décision.', 'seras', 'Être → ser- → tu seras.'),
            ('Ils ___ (venir) nous voir samedi.', 'viendront', 'Venir → viendr- → ils viendront.'),
            ('Je ___ (pouvoir) t\'aider demain matin.', 'pourrai', 'Pouvoir → pourr- → je pourrai.'),
            ('Nous ___ (finir) ce projet dans deux semaines.', 'finirons', 'Finir → finir + -ons → finirons.'),
            ('Vous ___ (aller) à la réunion lundi ?', 'irez', 'Aller → ir- → vous irez.'),
        ]),
    'ex3': ('Identifier l\'erreur', 'Quelle phrase est incorrecte ?',
        [
            ('Laquelle est incorrecte ?',
             ['Je parlerai demain.', 'Elle fera ses devoirs.', 'Nous allons partirons.', 'Ils viendront lundi.'],
             'Nous allons partirons.',
             'On ne mélange pas futur proche et futur simple : soit « nous allons partir », soit « nous partirons ».'),
            ('Quel futur irrégulier est faux ?',
             ['il sera', 'tu auras', 'nous ferons', 'vous allirez'],
             'vous allirez',
             'Aller → ir- → vous irez (pas allirez).'),
            ('Quand + quel temps ?',
             ['Quand il arrivera, je serai là.', 'Quand tu viendras, on mangera.', 'Quand elle arrive, je lui dirai.', 'Quand nous partirons, il fera nuit.'],
             'Quand elle arrive, je lui dirai.',
             'Si l\'action principale est au futur, « quand » prend aussi le futur : quand elle arrivera.'),
        ]),
    'game_desc': 'Maîtrisez le futur simple en français !',
    'items': [
        ('fut-01', 'je parlerai', 'I will speak', 'régulier', 'Demain, je parlerai à mon chef.', 'Demain, je ___ à mon chef.', 'parlerai'),
        ('fut-02', 'il sera', 'he will be (être)', 'irrégulier', 'Il sera content de te voir.', 'Il ___ content de te voir.', 'sera'),
        ('fut-03', 'tu auras', 'you will have (avoir)', 'irrégulier', 'Tu auras les résultats demain.', 'Tu ___ les résultats demain.', 'auras'),
        ('fut-04', 'nous ferons', 'we will do (faire)', 'irrégulier', 'Nous ferons de notre mieux.', 'Nous ___ de notre mieux.', 'ferons'),
        ('fut-05', 'ils iront', 'they will go (aller)', 'irrégulier', 'Ils iront en France l\'été prochain.', 'Ils ___ en France l\'été prochain.', 'iront'),
        ('fut-06', 'elle pourra', 'she will be able to', 'irrégulier', 'Elle pourra venir samedi.', 'Elle ___ venir samedi.', 'pourra'),
        ('fut-07', 'quand + futur', 'when + future (FR rule)', 'syntaxe', 'Quand il arrivera, nous partirons.', 'Quand il ___, nous partirons.', 'arrivera'),
        ('fut-08', 'dans deux ans', 'in two years', 'marqueur', 'Dans deux ans, je serai ingénieur.', 'Dans deux ___, je serai ingénieur.', 'ans'),
    ],
},

# ── G06 Les Comparatifs ────────────────────────────────────────────────────
'les-comparatifs': {
    'level':   'a2',
    'section': 'grammaire',
    'num':     'G06',
    'short':   'Les Comparatifs',
    'title':   'Les Comparatifs et Superlatifs',
    'subtitle': 'Comparer des personnes, des objets et des actions en français',
    'slides': [
        ('Les trois degrés de comparaison', None,
         '<p>En français, on compare avec trois structures :</p>'
         '<table><tr><th>Degré</th><th>Adjectif/Adverbe</th><th>Nom</th><th>Verbe</th></tr>'
         '<tr><td><b>Supériorité</b></td><td>plus … que</td><td>plus de … que</td><td>plus que</td></tr>'
         '<tr><td><b>Égalité</b></td><td>aussi … que</td><td>autant de … que</td><td>autant que</td></tr>'
         '<tr><td><b>Infériorité</b></td><td>moins … que</td><td>moins de … que</td><td>moins que</td></tr></table>'
         '<p>L\'adjectif s\'accorde toujours avec le nom qu\'il qualifie.</p>'),
        ('Comparatifs avec adjectifs', None,
         '<p>Structure : <b>plus / aussi / moins + adjectif (accordé) + que</b></p>'
         '<ul><li>Paris est <b>plus grand que</b> Lyon.</li>'
         '<li>Cette robe est <b>aussi belle que</b> l\'autre.</li>'
         '<li>Mon appartement est <b>moins cher que</b> le tien.</li></ul>'
         '<p>L\'adjectif s\'accorde avec le sujet :<br>'
         'Marie est plus grande <b>qu\'</b>Emma. (élision devant voyelle)</p>'),
        ('Bon et mauvais — formes irrégulières', None,
         '<p>Deux adjectifs ont des comparatifs irréguliers :</p>'
         '<table><tr><th>Adjectif</th><th>Comparatif de supériorité</th></tr>'
         '<tr><td><b>bon(ne)</b></td><td><b>meilleur(e)</b> que (pas « plus bon »)</td></tr>'
         '<tr><td><b>mauvais(e)</b></td><td><b>pire</b> que (ou plus mauvais, courant)</td></tr></table>'
         '<p>Pour les adverbes :</p>'
         '<table><tr><th>Adverbe</th><th>Comparatif</th></tr>'
         '<tr><td><b>bien</b></td><td><b>mieux</b> que (pas « plus bien »)</td></tr>'
         '<tr><td><b>mal</b></td><td><b>pire</b> que / plus mal que</td></tr></table>'),
        ('Les superlatifs', None,
         '<p>Le superlatif = le/la/les + plus/moins + adjectif :</p>'
         '<ul><li>C\'est <b>le plus grand</b> bâtiment de la ville.</li>'
         '<li>C\'est <b>la moins chère</b> des options.</li>'
         '<li>Ce sont <b>les meilleurs</b> étudiants de la classe.</li></ul>'
         '<p>Rappel : <b>bon → le meilleur</b> (irrégulier), <b>bien → le mieux</b>.<br>'
         'Position : l\'adjectif garde sa position habituelle (avant ou après le nom).</p>'),
        ('Comparatifs de noms et verbes', None,
         '<p>Pour comparer des <b>noms</b> (quantités) :</p>'
         '<ul><li>Il a <b>plus de</b> travail <b>que</b> moi.</li>'
         '<li>Elle a <b>autant de</b> patience <b>que</b> son père.</li>'
         '<li>Il y a <b>moins de</b> bruit <b>qu\'</b>avant.</li></ul>'
         '<p>Pour comparer des <b>verbes</b> (actions) :</p>'
         '<ul><li>Il travaille <b>plus que</b> moi.</li>'
         '<li>Elle mange <b>autant que</b> son frère.</li>'
         '<li>Je dors <b>moins que</b> toi.</li></ul>'),
    ],
    'traps': [
        ('C\'est plus bon.', 'C\'est meilleur.', 'Bon → meilleur (irrégulier). « Plus bon » est incorrect.'),
        ('Elle parle plus bien que lui.', 'Elle parle mieux que lui.', 'Bien → mieux (irrégulier). « Plus bien » est incorrect.'),
        ('Il a plus de travail que moi.', 'Correct !', 'Plus de + nom pour les quantités. « Plus que » sans de serait incorrect avec un nom.'),
        ('C\'est le plus meilleur.', 'C\'est le meilleur.', '« Meilleur » est déjà un comparatif de supériorité. Le superlatif est : c\'est le meilleur.'),
        ('Elle est plus grande qu\'lui.', 'Elle est plus grande que lui.', 'Élision seulement devant voyelle : « qu\'elle » mais « que lui » (consonne).'),
    ],
    'summary': [
        ('Supériorité', 'plus + adj. + que / plus de + nom + que', 'Il est plus grand que toi.'),
        ('Égalité', 'aussi + adj. + que / autant de + nom + que', 'Elle est aussi intelligente que lui.'),
        ('Infériorité', 'moins + adj. + que / moins de + nom + que', 'C\'est moins cher qu\'avant.'),
        ('Irrég. adj.', 'bon → meilleur · mauvais → pire', 'C\'est meilleur que l\'autre.'),
        ('Irrég. adv.', 'bien → mieux · mal → pire/plus mal', 'Elle chante mieux que moi.'),
        ('Superlatif', 'le/la/les + plus/moins + adj.', 'C\'est la plus belle ville de France.'),
    ],
    'ex1': ('Choisir la bonne forme', 'Sélectionnez la réponse correcte.',
        [
            ('Ce restaurant est ___ que l\'autre.', ['plus bon', 'meilleur', 'mieux', 'plus meilleur'], 'meilleur',
             'Bon → meilleur (comparatif irrégulier). « Plus bon » est incorrect.'),
            ('Elle chante ___ que son frère.', ['plus bien', 'meilleure', 'mieux', 'mieux que'], 'mieux',
             'Bien → mieux (comparatif irrégulier de l\'adverbe).'),
            ('Il a ___ de travail que moi.', ['autant', 'plus', 'aussi', 'mieux'], 'plus',
             'Plus de + nom pour exprimer une plus grande quantité : plus de travail.'),
            ('C\'est ___ hôtel de la ville.', ['le plus grand', 'le plus grande', 'plus grand', 'le meilleur grand'], 'le plus grand',
             'Superlatif : le/la + plus + adjectif accordé → le plus grand hôtel.'),
        ]),
    'ex2': ('Compléter les phrases', 'Complétez avec la forme correcte.',
        [
            ('Paris est ___ grand ___ Lyon.', 'plus … que', 'Supériorité avec adjectif : plus + adj. + que.'),
            ('Ce film est aussi ___ que l\'autre.', 'bon → bon', 'Égalité : aussi + adjectif + que. Bon reste bon (pas meilleur pour l\'égalité).'),
            ('Elle parle ___ vite que toi.', 'moins', 'Infériorité : moins + adverbe + que.'),
            ('C\'est le ___ restaurant de la ville. (bon)', 'meilleur', 'Superlatif de bon : le meilleur (irrégulier).'),
            ('Il travaille ___ que son collègue. (comparatif de verbe, supériorité)', 'plus que', 'Plus que (sans de) pour comparer des actions/verbes.'),
        ]),
    'ex3': ('Identifier l\'erreur', 'Quelle phrase est incorrecte ?',
        [
            ('Laquelle est incorrecte ?',
             ['Il est plus grand que moi.', 'C\'est meilleur que l\'autre.', 'Elle chante plus bien que lui.', 'Ils ont moins de temps que nous.'],
             'Elle chante plus bien que lui.',
             'Bien → mieux (irrégulier). « Plus bien » n\'existe pas en français standard.'),
            ('Quelle phrase a une erreur ?',
             ['C\'est le meilleur film.', 'C\'est le plus bon film.', 'Elle est la moins chère.', 'Ils sont les plus rapides.'],
             'C\'est le plus bon film.',
             'Le superlatif de bon est le meilleur, pas le plus bon.'),
            ('Quel comparatif est correct ?',
             ['Il a plus travail que toi.', 'Il a plus de travail que toi.', 'Il a plus du travail que toi.', 'Il a le plus travail.'],
             'Il a plus de travail que toi.',
             'Plus de + nom pour les quantités. Pas d\'article entre plus de et le nom.'),
        ]),
    'game_desc': 'Maîtrisez les comparatifs et superlatifs en français !',
    'items': [
        ('comp-01', 'plus … que', 'more … than', 'supériorité', 'Il est plus grand que son frère.', 'Il est ___ grand que son frère.', 'plus'),
        ('comp-02', 'aussi … que', 'as … as', 'égalité', 'Elle est aussi intelligente que lui.', 'Elle est ___ intelligente que lui.', 'aussi'),
        ('comp-03', 'moins … que', 'less … than', 'infériorité', 'C\'est moins cher qu\'avant.', 'C\'est ___ cher qu\'avant.', 'moins'),
        ('comp-04', 'meilleur(e)', 'better (adj.)', 'irrégulier', 'Ce vin est meilleur que l\'autre.', 'Ce vin est ___ que l\'autre. (bon→)', 'meilleur'),
        ('comp-05', 'mieux', 'better (adv.)', 'irrégulier', 'Elle parle mieux que moi.', 'Elle parle ___ que moi. (bien→)', 'mieux'),
        ('comp-06', 'le meilleur', 'the best', 'superlatif', 'C\'est le meilleur restaurant de Paris.', 'C\'est le ___ restaurant de Paris.', 'meilleur'),
        ('comp-07', 'plus de … que', 'more … than (noun)', 'quantité', 'Il a plus de travail que moi.', 'Il a plus ___ travail que moi.', 'de'),
        ('comp-08', 'le plus grand', 'the tallest / biggest', 'superlatif', 'C\'est le plus grand pays d\'Europe.', 'C\'est le plus grand pays d\'___. (continent)', 'Europe'),
    ],
},

# ── G07 Les Pronoms Relatifs qui et que ────────────────────────────────────
'les-pronoms-relatifs': {
    'level':   'a2',
    'section': 'grammaire',
    'num':     'G07',
    'short':   'Les Pronoms Relatifs',
    'title':   'Les Pronoms Relatifs — qui, que, où',
    'subtitle': 'Relier deux phrases avec qui (sujet), que (objet) et où (lieu/temps)',
    'slides': [
        ('Qu\'est-ce qu\'un pronom relatif ?', None,
         '<p>Un pronom relatif relie deux phrases en évitant la répétition :</p>'
         '<ul><li>J\'ai un ami. Cet ami parle français.<br>'
         '→ J\'ai un ami <b>qui</b> parle français.</li>'
         '<li>C\'est le livre. J\'ai lu ce livre.<br>'
         '→ C\'est le livre <b>que</b> j\'ai lu.</li></ul>'
         '<p>Le pronom relatif représente un <b>antécédent</b> (le nom qui précède). Il relie une proposition relative à la proposition principale.</p>'),
        ('QUI — pronom sujet', None,
         '<p><b>Qui</b> remplace le <b>sujet</b> du verbe dans la relative :</p>'
         '<ul><li>L\'homme <b>qui</b> parle est mon professeur. (qui = l\'homme → sujet de « parle »)</li>'
         '<li>C\'est une ville <b>qui</b> est très belle.</li>'
         '<li>J\'ai des amis <b>qui</b> habitent à Lyon.</li></ul>'
         '<p>Après <b>qui</b>, le verbe s\'accorde avec l\'antécédent :<br>'
         'C\'est moi <b>qui</b> <i>suis</i> responsable. (pas « qui est »)</p>'),
        ('QUE — pronom objet', None,
         '<p><b>Que</b> remplace le <b>complément d\'objet direct</b> du verbe dans la relative :</p>'
         '<ul><li>Le film <b>que</b> j\'ai vu était super. (que = le film → COD de « ai vu »)</li>'
         '<li>La maison <b>que</b> tu as achetée est grande.</li>'
         '<li>C\'est le plat <b>que</b> je préfère.</li></ul>'
         '<p>Devant voyelle : <b>qu\'</b> — Le livre <b>qu\'</b>elle lit est passionnant.<br>'
         'Au passé composé avec avoir : accord avec <b>que</b> !</p>'),
        ('OÙ — pronom de lieu et de temps', None,
         '<p><b>Où</b> remplace un <b>complément de lieu ou de temps</b> :</p>'
         '<ul><li>La ville <b>où</b> j\'habite est très animée. (où = dans cette ville)</li>'
         '<li>C\'est le restaurant <b>où</b> on a dîné hier.</li>'
         '<li>Le jour <b>où</b> je suis arrivé, il pleuvait. (où = le jour)</li></ul>'
         '<p>Qui / que / où ne changent pas selon le genre ou le nombre de l\'antécédent.</p>'),
        ('Récapitulatif et erreurs fréquentes', None,
         '<table><tr><th>Pronom</th><th>Rôle</th><th>Exemple</th></tr>'
         '<tr><td><b>qui</b></td><td>sujet du verbe relatif</td><td>l\'homme qui parle</td></tr>'
         '<tr><td><b>que / qu\'</b></td><td>COD du verbe relatif</td><td>le film que j\'aime</td></tr>'
         '<tr><td><b>où</b></td><td>lieu ou temps</td><td>la ville où j\'habite</td></tr></table>'
         '<p>Test : remplacez par « il/elle » → <b>qui</b>. Remplacez par « le/la » → <b>que</b>.</p>'),
    ],
    'traps': [
        ('L\'homme que parle est sympa.', 'L\'homme qui parle est sympa.', '« Parle » n\'a pas d\'autre sujet → relatif sujet = qui.'),
        ('Le film qui j\'ai vu était bien.', 'Le film que j\'ai vu était bien.', '« J\'ai vu » a un sujet (je) → relatif objet = que.'),
        ('C\'est la ville où j\'habite dans.', 'C\'est la ville où j\'habite.', 'Où remplace déjà « dans la ville » — ne pas répéter la préposition.'),
        ('La maison que j\'ai acheté.', 'La maison que j\'ai achetée.', 'Avec avoir, le participe s\'accorde avec que (= la maison, féminin) : achetée.'),
        ('C\'est moi qui est responsable.', 'C\'est moi qui suis responsable.', 'Le verbe s\'accorde avec l\'antécédent de qui : moi → suis.'),
    ],
    'summary': [
        ('Qui', 'sujet du verbe relatif', 'L\'ami qui habite ici est sympa.'),
        ('Que/qu\'', 'COD du verbe relatif', 'Le livre que tu lis est excellent.'),
        ('Où', 'lieu ou moment', 'La ville où j\'habite · Le jour où il est parti'),
        ('Accord PC', 'participe s\'accorde avec que (COD avant)', 'La maison qu\'il a achetée.'),
        ('Test', 'sujet → qui / objet → que', 'L\'homme __ parle (sujet → qui)'),
        ('C\'est moi qui', 'verbe s\'accorde avec antécédent', 'C\'est toi qui as raison.'),
    ],
    'ex1': ('Choisir qui, que ou où', 'Complétez avec le bon pronom relatif.',
        [
            ('Le livre ___ tu m\'as conseillé est fantastique.', ['qui', 'que', 'où', 'qu\''], 'que',
             'Tu m\'as conseillé [le livre] — le livre est COD → que (ou qu\' devant voyelle).'),
            ('C\'est la ville ___ j\'ai grandi.', ['qui', 'que', 'où', 'qu\''], 'où',
             'J\'ai grandi dans cette ville → complément de lieu → où.'),
            ('J\'ai un collègue ___ parle quatre langues.', ['que', 'qu\'', 'où', 'qui'], 'qui',
             'Mon collègue parle quatre langues → sujet de « parle » → qui.'),
            ('Le jour ___ tu es arrivé, il neigeait.', ['qui', 'que', 'qu\'', 'où'], 'où',
             'Il neigeait ce jour-là → complément de temps → où.'),
        ]),
    'ex2': ('Relier les deux phrases', 'Combinez avec un pronom relatif.',
        [
            ('C\'est un film. Ce film m\'a beaucoup ému. → C\'est un film ___ m\'a beaucoup ému.', 'qui', 'Le film est sujet de « m\'a ému » → qui.'),
            ('C\'est le restaurant. Nous avons dîné dans ce restaurant. → C\'est le restaurant ___ nous avons dîné.', 'où', 'Complément de lieu → où.'),
            ('J\'ai lu le roman. Tu m\'as offert ce roman. → J\'ai lu le roman ___ tu m\'as offert.', 'que', 'Le roman est COD de « m\'as offert » → que.'),
            ('C\'est une étudiante. Elle travaille très bien. → C\'est une étudiante ___ travaille très bien.', 'qui', 'Elle est sujet de « travaille » → qui.'),
            ('C\'est la chanson. J\'ai écouté cette chanson hier. → C\'est la chanson ___ j\'ai écoutée hier.', 'que', 'La chanson est COD de « ai écoutée » → que (accord : écoutée).'),
        ]),
    'ex3': ('Identifier l\'erreur', 'Quelle phrase est incorrecte ?',
        [
            ('Laquelle est incorrecte ?',
             ['L\'ami qui m\'aide est sympa.', 'Le film que j\'ai vu était bien.', 'La ville où j\'habite est belle.', 'La fille qui j\'aime.'],
             'La fille qui j\'aime.',
             'J\'aime [la fille] — la fille est COD de « aime » → que : la fille que j\'aime.'),
            ('Quel accord est faux ?',
             ['La maison qu\'il a achetée.', 'Les films qu\'il a vus.', 'La chanson qu\'elle a chanté.', 'Le livre qu\'elle a lu.'],
             'La chanson qu\'elle a chanté.',
             'Que remplace « la chanson » (féminin) → accord du participe : chanté → chantée.'),
            ('Quelle phrase est correcte ?',
             ['C\'est moi qui est parti.', 'C\'est toi qui as raison.', 'C\'est lui qui sommes là.', 'C\'est elle qui avons fait ça.'],
             'C\'est toi qui as raison.',
             'Le verbe s\'accorde avec l\'antécédent de qui : toi → tu → as (2e personne singulier).'),
        ]),
    'game_desc': 'Maîtrisez les pronoms relatifs qui, que et où !',
    'items': [
        ('rel-01', 'qui (sujet)', 'who / that (subject)', 'sujet', 'J\'ai un ami qui parle français.', 'J\'ai un ami ___ parle français.', 'qui'),
        ('rel-02', 'que (objet)', 'that / which (object)', 'objet', 'C\'est le film que j\'ai vu.', 'C\'est le film ___ j\'ai vu.', 'que'),
        ('rel-03', 'qu\' (élision)', 'that (before vowel)', 'élision', 'Le livre qu\'elle lit est passionnant.', 'Le livre ___elle lit est passionnant.', 'qu\''),
        ('rel-04', 'où (lieu)', 'where (place)', 'lieu', 'La ville où j\'habite est animée.', 'La ville ___ j\'habite est animée.', 'où'),
        ('rel-05', 'où (temps)', 'when (time)', 'temps', 'Le jour où il est arrivé, il pleuvait.', 'Le jour ___ il est arrivé, il pleuvait.', 'où'),
        ('rel-06', 'accord avec que', 'agreement with que', 'accord', 'La maison qu\'il a achetée est belle.', 'La maison qu\'il a achetée → achetée car que = ___', 'maison'),
        ('rel-07', 'c\'est moi qui suis', 'it is I who am', 'accord', 'C\'est moi qui suis responsable.', 'C\'est moi qui ___ responsable.', 'suis'),
        ('rel-08', 'test sujet/objet', 'subject/object test', 'méthode', 'L\'homme qui parle est mon prof.', 'L\'homme ___ parle est mon prof. (sujet)', 'qui'),
    ],
},

# ── G08 Les Adverbes ───────────────────────────────────────────────────────
'les-adverbes': {
    'level':   'a2',
    'section': 'grammaire',
    'num':     'G08',
    'short':   'Les Adverbes',
    'title':   'Les Adverbes — Formation et Usage',
    'subtitle': 'Former les adverbes en -ment et les utiliser correctement',
    'slides': [
        ('Qu\'est-ce qu\'un adverbe ?', None,
         '<p>Un adverbe modifie un <b>verbe, un adjectif ou un autre adverbe</b>. Il est <b>invariable</b> (ne s\'accorde jamais) :</p>'
         '<ul><li>Elle parle <b>lentement</b>. (modifie le verbe)</li>'
         '<li>Il est <b>très</b> intelligent. (modifie l\'adjectif)</li>'
         '<li>Elle parle <b>vraiment</b> bien. (modifie un adverbe)</li></ul>'
         '<p>Catégories : manière (comment ?) · fréquence (combien ?) · temps (quand ?) · lieu (où ?) · quantité (combien ?)</p>'),
        ('Formation des adverbes en -ment', None,
         '<p>La majorité des adverbes de manière se forment à partir de l\'adjectif :</p>'
         '<table><tr><th>Règle</th><th>Adjectif</th><th>Adverbe</th></tr>'
         '<tr><td>fém. + -ment</td><td>lent → lente</td><td>lentement</td></tr>'
         '<tr><td>fém. + -ment</td><td>doux → douce</td><td>doucement</td></tr>'
         '<tr><td>masc. -e + -ment</td><td>rapide</td><td>rapidement</td></tr>'
         '<tr><td>-ant → -amment</td><td>courant</td><td>couramment</td></tr>'
         '<tr><td>-ent → -emment</td><td>récent</td><td>récemment</td></tr></table>'
         '<p>Exceptions : <b>vrai → vraiment</b> · <b>gentil → gentiment</b> · <b>bref → brièvement</b></p>'),
        ('Adverbes fréquents (à mémoriser)', None,
         '<p><b>Manière :</b> bien · mal · vite · fort · ensemble · surtout · seulement</p>'
         '<p><b>Fréquence :</b> toujours · souvent · parfois · rarement · jamais · encore</p>'
         '<p><b>Temps :</b> maintenant · déjà · bientôt · hier · demain · tard · tôt</p>'
         '<p><b>Quantité :</b> très · beaucoup · peu · assez · trop · vraiment · plutôt</p>'
         '<p><b>Lieu :</b> ici · là · partout · ailleurs · dehors · dedans</p>'),
        ('Position de l\'adverbe', None,
         '<p>Position habituelle :</p>'
         '<ul><li>Après le <b>verbe</b> au temps simple : Elle parle <b>bien</b>.</li>'
         '<li>Après l\'<b>auxiliaire</b> au temps composé : Il a <b>bien</b> travaillé.</li>'
         '<li>Avant l\'<b>adjectif</b> ou l\'adverbe modifié : très <b>grand</b> · vraiment <b>bien</b>.</li>'
         '<li>Exceptions — adverbes longs souvent en fin de phrase : Il est parti <b>rapidement</b>.</li></ul>'
         '<p>Adverbes de fréquence : entre sujet et verbe à la négation : Il ne va <b>jamais</b> au cinéma.</p>'),
        ('Ne … jamais, ne … plus, ne … pas encore', None,
         '<p>Les adverbes négatifs encadrent le verbe (ou l\'auxiliaire) :</p>'
         '<table><tr><th>Expression</th><th>Sens</th><th>Exemple</th></tr>'
         '<tr><td><b>ne … jamais</b></td><td>never</td><td>Je ne mange jamais de sucre.</td></tr>'
         '<tr><td><b>ne … plus</b></td><td>no longer / not anymore</td><td>Il ne travaille plus ici.</td></tr>'
         '<tr><td><b>ne … pas encore</b></td><td>not yet</td><td>Elle n\'est pas encore arrivée.</td></tr>'
         '<tr><td><b>ne … toujours pas</b></td><td>still not</td><td>Il n\'a toujours pas répondu.</td></tr></table>'),
    ],
    'traps': [
        ('Elle a vite mangé.', 'Elle a mangé vite. / Elle a vite mangé.', 'Vite peut se placer avant ou après le participe. Les deux sont acceptés.'),
        ('Il parle très couramment.', 'Il parle couramment. / très couramment.', '« Couramment » est déjà un adverbe de degré élevé, mais « très couramment » est possible et correct.'),
        ('Elle est patientement.', 'Elle est patiente.', 'Après être, on utilise un adjectif (accordé), pas un adverbe.'),
        ('Il ne mange toujours pas.', 'Il ne mange toujours pas. / Il ne mange plus.', '« Ne…toujours pas » = still not (il n\'a pas encore changé). « Ne…plus » = no longer.'),
        ('C\'est vraiement beau.', 'C\'est vraiment beau.', 'Vrai → vraiment (exception : pas « vraiement »).'),
    ],
    'summary': [
        ('Formation', 'adj. fém. + -ment (règle générale)', 'lent→lente→lentement · doux→douce→doucement'),
        ('-ant/-ent', '-ant→-amment · -ent→-emment', 'courant→couramment · récent→récemment'),
        ('Irrég.', 'bien · mal · vite · vraiment · gentiment', 'Il parle bien. · Elle mange vite.'),
        ('Position', 'après verbe simple / après auxiliaire PC', 'Elle parle bien. / Il a bien travaillé.'),
        ('Négatifs', 'ne…jamais · ne…plus · ne…pas encore', 'Je ne mange jamais de viande.'),
        ('Invariable', 'l\'adverbe ne s\'accorde jamais', 'Elles parlent lentement. (pas lentements)'),
    ],
    'ex1': ('Choisir l\'adverbe correct', 'Sélectionnez la réponse correcte.',
        [
            ('Quelle est la forme adverbiale de « rapide » ?', ['rapidement', 'rapidment', 'rapidement', 'rapide-ment'], 'rapidement',
             'Rapide se termine par -e → on ajoute directement -ment : rapidement.'),
            ('Quel adverbe est formé à partir de « récent » ?', ['récentment', 'récemment', 'récentement', 'récemement'], 'récemment',
             '-ent → -emment : récent → récemment (attention à l\'orthographe !).'),
            ('Il ne travaille ___ ici. (no longer)', ['jamais', 'pas', 'plus', 'encore'], 'plus',
             'Ne … plus = no longer / not anymore.'),
            ('Elle n\'est pas ___ arrivée. (not yet)', ['jamais', 'encore', 'plus', 'toujours'], 'encore',
             'Ne … pas encore = not yet.'),
        ]),
    'ex2': ('Former les adverbes', 'Donnez la forme adverbiale.',
        [
            ('lent → lente → ___', 'lentement', 'Adjectif féminin + -ment : lente → lentement.'),
            ('doux → douce → ___', 'doucement', 'Adjectif féminin + -ment : douce → doucement.'),
            ('courant → ___', 'couramment', '-ant → -amment : courant → couramment.'),
            ('gentil → ___', 'gentiment', 'Exception : gentil → gentiment (pas gentillement).'),
            ('vrai → ___', 'vraiment', 'Exception : vrai → vraiment (pas vraiment avec e intercalaire).'),
        ]),
    'ex3': ('Identifier l\'erreur', 'Quelle phrase est incorrecte ?',
        [
            ('Laquelle est incorrecte ?',
             ['Elle parle lentement.', 'Il a bien travaillé.', 'Elles sont patientement.', 'Il mange trop vite.'],
             'Elles sont patientement.',
             'Après être, on utilise un adjectif (accordé), pas un adverbe : elles sont patientes.'),
            ('Quelle formation est incorrecte ?',
             ['courant → couramment', 'récent → récemment', 'patient → patientement', 'lent → lentement'],
             'patient → patientement',
             'Patient (-ent) → -emment : la forme correcte est patiemment, pas patientement.'),
            ('Quel adverbe est invariable ?',
             ['Elle parle lentements.', 'Ils marchent rapidement.', 'Elles chantent doucement.', 'Il parle couramment.'],
             'Elle parle lentements.',
             'Les adverbes sont invariables : on ne met jamais de -s à un adverbe.'),
        ]),
    'game_desc': 'Maîtrisez la formation et l\'usage des adverbes en français !',
    'items': [
        ('adv-01', 'lentement', 'slowly', 'manière', 'Elle parle lentement et clairement.', 'Elle parle ___ et clairement.', 'lentement'),
        ('adv-02', 'rapidement', 'quickly', 'manière', 'Il a répondu rapidement à mon message.', 'Il a répondu ___ à mon message.', 'rapidement'),
        ('adv-03', 'couramment', 'fluently (-ant→-amment)', 'formation', 'Elle parle couramment le français.', 'Elle parle ___ le français.', 'couramment'),
        ('adv-04', 'récemment', 'recently (-ent→-emment)', 'formation', 'Il a récemment changé de travail.', 'Il a ___ changé de travail.', 'récemment'),
        ('adv-05', 'ne … jamais', 'never', 'négation', 'Je ne mange jamais de sucre.', 'Je ne mange ___ de sucre.', 'jamais'),
        ('adv-06', 'ne … plus', 'no longer', 'négation', 'Il ne travaille plus ici.', 'Il ne travaille ___ ici.', 'plus'),
        ('adv-07', 'vraiment', 'truly / really (irreg.)', 'formation', 'C\'est vraiment beau !', 'C\'est ___ beau !', 'vraiment'),
        ('adv-08', 'ne … pas encore', 'not yet', 'négation', 'Elle n\'est pas encore arrivée.', 'Elle n\'est pas ___ arrivée.', 'encore'),
    ],
},

}
