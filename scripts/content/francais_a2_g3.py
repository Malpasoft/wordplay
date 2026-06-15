"""Français A2 — Grammaire batch 3: G09–G12."""

CHAPTERS = {

# ── G09 Les Verbes Pronominaux ─────────────────────────────────────────────
'les-verbes-pronominaux': {
    'level':   'a2',
    'section': 'grammaire',
    'num':     'G09',
    'short':   'Les Verbes Pronominaux',
    'title':   'Les Verbes Pronominaux — Se Lever, Se Coucher…',
    'subtitle': 'Formation, conjugaison et usage des verbes réfléchis et réciproques',
    'slides': [
        ('Qu\'est-ce qu\'un verbe pronominal ?', None,
         '<p>Un verbe pronominal se conjugue avec un <b>pronom réfléchi</b> (me, te, se, nous, vous, se) qui renvoie au sujet :</p>'
         '<ul><li><b>Je me lève</b> à 7 h. (je me lève moi-même)</li>'
         '<li><b>Tu te brosses</b> les dents.</li>'
         '<li><b>Il s\'appelle</b> Thomas.</li></ul>'
         '<p>Catégories : réfléchis (action sur soi-même) · réciproques (action mutuelle) · idiomatiques (sens différent du verbe simple).</p>'),
        ('Conjugaison au présent', None,
         '<table><tr><th>Sujet</th><th>Pronom</th><th>se lever</th></tr>'
         '<tr><td>je</td><td><b>me</b></td><td>je me lève</td></tr>'
         '<tr><td>tu</td><td><b>te</b></td><td>tu te lèves</td></tr>'
         '<tr><td>il/elle</td><td><b>se</b></td><td>il/elle se lève</td></tr>'
         '<tr><td>nous</td><td><b>nous</b></td><td>nous nous levons</td></tr>'
         '<tr><td>vous</td><td><b>vous</b></td><td>vous vous levez</td></tr>'
         '<tr><td>ils/elles</td><td><b>se</b></td><td>ils/elles se lèvent</td></tr></table>'
         '<p>Élision : me/te/se → m\'/t\'/s\' devant voyelle : je <b>m\'</b>habille.</p>'),
        ('Verbes pronominaux courants', None,
         '<p><b>Routine quotidienne :</b></p>'
         '<ul><li>se lever · se coucher · se réveiller · s\'endormir</li>'
         '<li>se laver · se doucher · se brosser les dents · s\'habiller</li>'
         '<li>se maquiller · se raser · se coiffer</li></ul>'
         '<p><b>Autres courants :</b></p>'
         '<ul><li>s\'appeler · se trouver · s\'asseoir · se dépêcher</li>'
         '<li>se souvenir · s\'inquiéter · se sentir · se tromper</li></ul>'),
        ('Au passé composé — avec être', None,
         '<p>Tous les verbes pronominaux forment leur passé composé avec <b>être</b> :</p>'
         '<p>sujet + pronom réfléchi + être (conjugué) + participe passé</p>'
         '<ul><li>Je <b>me suis levé(e)</b> à 7 h.</li>'
         '<li>Elle <b>s\'est habillée</b> rapidement.</li>'
         '<li>Nous <b>nous sommes dépêchés</b>.</li></ul>'
         '<p>Le participe s\'accorde avec le <b>sujet</b> (sauf si COD après le verbe) :<br>'
         'Elle s\'est lavé <b>les mains</b>. (les mains = COD après → pas d\'accord)</p>'),
        ('La négation et les verbes réciproques', None,
         '<p><b>Négation :</b> ne encadre le pronom réfléchi + verbe :<br>'
         'Je <b>ne</b> me lève <b>pas</b> tard. / Elle <b>ne</b> s\'est <b>pas</b> coiffée.</p>'
         '<p><b>Réciproques</b> (action mutuelle entre deux sujets ou plus) :</p>'
         '<ul><li>Ils <b>se téléphonent</b> tous les soirs. (ils téléphonent l\'un à l\'autre)</li>'
         '<li>Nous <b>nous aimons</b> beaucoup.</li>'
         '<li>Elles <b>se connaissent</b> depuis dix ans.</li></ul>'),
    ],
    'traps': [
        ('Je me suis levé à 7 h.', 'Correct !', 'Se lever au passé composé → être + participe accordé (levé pour masc.).'),
        ('Elle s\'est lavé.', 'Elle s\'est lavée.', 'Pas de COD après le verbe → le participe s\'accorde avec le sujet (féminin) : lavée.'),
        ('Il se est rasé.', 'Il s\'est rasé.', 'Se + est → s\'est. Élision obligatoire devant voyelle.'),
        ('Nous nous sommes rencontré.', 'Nous nous sommes rencontrés.', 'Verbe réciproque + sujet masculin pluriel → accord : rencontrés.'),
        ('Je me lève pas.', 'Je ne me lève pas.', 'La négation encadre pronom + verbe : je ne me lève pas.'),
    ],
    'summary': [
        ('Pronoms', 'me/te/se/nous/vous/se (élision m\'/t\'/s\')', 'Je me lève. / Je m\'habille.'),
        ('Présent', 'pronom réfléchi + verbe conjugué', 'Tu te couches tôt.'),
        ('PC', 'être + participe accordé avec sujet', 'Elle s\'est levée. / Ils se sont levés.'),
        ('Accord', 'accord sauf si COD après le verbe', 'Elle s\'est lavé les mains. (les mains = COD)'),
        ('Négation', 'ne + pronom + verbe + pas', 'Je ne me souviens pas. / Il ne s\'est pas rasé.'),
        ('Réciproque', 'action mutuelle (nous/vous/ils)', 'Ils se téléphonent chaque soir.'),
    ],
    'ex1': ('Conjuguer au présent', 'Choisissez la forme correcte.',
        [
            ('Chaque matin, il ___ à 6 h. (se lever)', ['se lève', 'se lèvent', 's\'élève', 'lève'], 'se lève',
             'Se lever → il se lève (3e personne singulier, avec pronom réfléchi se).'),
            ('Nous ___ avant de partir. (se dépêcher)', ['nous dépêchons', 'nous nous dépêchons', 'se dépêchons', 'nous dépêchens'], 'nous nous dépêchons',
             'Verbe pronominal → sujet + pronom réfléchi + verbe : nous nous dépêchons.'),
            ('Elle ___ Marie. (s\'appeler)', ['s\'appelle', 'se appelle', 'appelle', 's\'apellent'], 's\'appelle',
             'S\'appeler → elle s\'appelle (élision : se → s\' devant voyelle).'),
            ('Ils ___ depuis l\'université. (se connaître)', ['se connaissent', 'se connaissent pas', 'connaissent', 'se connait'], 'se connaissent',
             'Se connaître → ils se connaissent (verbe réciproque, 3e pluriel).'),
        ]),
    'ex2': ('Mettre au passé composé', 'Donnez la forme correcte.',
        [
            ('Je ___ (se réveiller) à 8 h ce matin.', 'me suis réveillé(e)', 'Pronominal → être : je me suis réveillé(e). Accord selon le genre.'),
            ('Elle ___ (se doucher) rapidement.', 's\'est douchée', 'Féminin singulier → s\'est douchée (accord avec sujet).'),
            ('Nous ___ (se rencontrer) à Paris l\'an dernier.', 'nous sommes rencontrés / rencontrées', 'Réciproque → être : nous nous sommes rencontrés (accord avec sujet pluriel).'),
            ('Ils ___ (se coucher) très tard hier soir.', 'se sont couchés', 'Masculin pluriel → se sont couchés.'),
            ('Tu ___ (se tromper) de numéro.', 'tu t\'es trompé(e)', 'Se tromper → être : tu t\'es trompé(e).'),
        ]),
    'ex3': ('Identifier l\'erreur', 'Quelle phrase est incorrecte ?',
        [
            ('Laquelle est incorrecte ?',
             ['Je me lève à 7 h.', 'Elle s\'est habillée.', 'Il se est rasé.', 'Nous nous sommes levés.'],
             'Il se est rasé.',
             'Élision obligatoire : se + est → s\'est. La forme correcte est « il s\'est rasé ».'),
            ('Quel accord est faux ?',
             ['Elle s\'est levée.', 'Il s\'est levé.', 'Elles se sont lavé.', 'Ils se sont habillés.'],
             'Elles se sont lavé.',
             'Féminin pluriel → accord obligatoire : elles se sont lavées (sauf si COD après).'),
            ('Quelle négation est correcte ?',
             ['Je me ne lève pas.', 'Je ne me lève pas.', 'Je ne lève me pas.', 'Ne je me lève pas.'],
             'Je ne me lève pas.',
             'La négation encadre le bloc pronom réfléchi + verbe : je ne me lève pas.'),
        ]),
    'game_desc': 'Maîtrisez les verbes pronominaux en français !',
    'items': [
        ('pron-01', 'je me lève', 'I get up', 'présent', 'Je me lève à 7 h chaque matin.', 'Je ___ lève à 7 h chaque matin.', 'me'),
        ('pron-02', 's\'appelle', 'is called', 'présent', 'Elle s\'appelle Sophie.', 'Elle ___appelle Sophie.', 's\''),
        ('pron-03', 'nous nous levons', 'we get up', 'présent', 'Nous nous levons tôt le week-end.', 'Nous ___ levons tôt le week-end.', 'nous'),
        ('pron-04', 'je me suis levé(e)', 'I got up (PC)', 'passé', 'Je me suis levé à 6 h ce matin.', 'Je me ___ levé à 6 h ce matin.', 'suis'),
        ('pron-05', 'elle s\'est habillée', 'she got dressed (PC)', 'passé', 'Elle s\'est habillée rapidement.', 'Elle s\'est ___. (s\'habiller, f.)', 'habillée'),
        ('pron-06', 'ils se téléphonent', 'they call each other', 'réciproque', 'Ils se téléphonent tous les soirs.', 'Ils ___ téléphonent tous les soirs.', 'se'),
        ('pron-07', 'je ne me lève pas', 'I don\'t get up (neg.)', 'négation', 'Je ne me lève pas avant 8 h.', 'Je ne ___ lève pas avant 8 h.', 'me'),
        ('pron-08', 'se dépêcher', 'to hurry (up)', 'idiom.', 'Dépêche-toi, on est en retard !', 'Dépêche-___, on est en retard !', 'toi'),
    ],
},

# ── G10 Le Conditionnel Présent ────────────────────────────────────────────
'le-conditionnel': {
    'level':   'a2',
    'section': 'grammaire',
    'num':     'G10',
    'short':   'Le Conditionnel',
    'title':   'Le Conditionnel Présent — Politesse et Hypothèses',
    'subtitle': 'Former et utiliser le conditionnel pour la politesse et les phrases hypothétiques',
    'slides': [
        ('Qu\'est-ce que le conditionnel présent ?', None,
         '<p>Le conditionnel présent exprime :</p>'
         '<ul><li><b>La politesse</b> : Je <b>voudrais</b> un café. (plus poli que « je veux »)</li>'
         '<li><b>Une hypothèse</b> : Si j\'avais de l\'argent, j\'<b>achèterais</b> une maison.</li>'
         '<li><b>Un souhait</b> : J\'<b>aimerais</b> voyager en Asie.</li>'
         '<li><b>Un conseil</b> : Tu <b>devrais</b> dormir davantage.</li>'
         '<li><b>Le futur dans le passé</b> : Il a dit qu\'il <b>viendrait</b>.</li></ul>'),
        ('Formation', None,
         '<p>Base = <b>même radical que le futur simple</b> + terminaisons de l\'imparfait :</p>'
         '<table><tr><th>Sujet</th><th>Terminaison</th><th>Parler</th><th>Être (irrég.)</th></tr>'
         '<tr><td>je</td><td>-ais</td><td>parlerais</td><td>serais</td></tr>'
         '<tr><td>tu</td><td>-ais</td><td>parlerais</td><td>serais</td></tr>'
         '<tr><td>il/elle</td><td>-ait</td><td>parlerait</td><td>serait</td></tr>'
         '<tr><td>nous</td><td>-ions</td><td>parlerions</td><td>serions</td></tr>'
         '<tr><td>vous</td><td>-iez</td><td>parleriez</td><td>seriez</td></tr>'
         '<tr><td>ils/elles</td><td>-aient</td><td>parleraient</td><td>seraient</td></tr></table>'),
        ('Radicaux irréguliers', None,
         '<p>Mêmes radicaux irréguliers qu\'au futur simple :</p>'
         '<table><tr><th>Verbe</th><th>Radical</th><th>Conditionnel</th></tr>'
         '<tr><td>être</td><td>ser-</td><td>je serais</td></tr>'
         '<tr><td>avoir</td><td>aur-</td><td>tu aurais</td></tr>'
         '<tr><td>aller</td><td>ir-</td><td>il irait</td></tr>'
         '<tr><td>faire</td><td>fer-</td><td>nous ferions</td></tr>'
         '<tr><td>pouvoir</td><td>pourr-</td><td>vous pourriez</td></tr>'
         '<tr><td>vouloir</td><td>voudr-</td><td>ils voudraient</td></tr>'
         '<tr><td>venir</td><td>viendr-</td><td>elle viendrait</td></tr></table>'),
        ('La politesse au conditionnel', None,
         '<p>Le conditionnel est la forme polie par excellence :</p>'
         '<table><tr><th>Direct (présent)</th><th>Poli (conditionnel)</th></tr>'
         '<tr><td>Je veux un café.</td><td>Je <b>voudrais</b> un café.</td></tr>'
         '<tr><td>Pouvez-vous m\'aider ?</td><td><b>Pourriez</b>-vous m\'aider ?</td></tr>'
         '<tr><td>Vous devez partir.</td><td>Vous <b>devriez</b> partir.</td></tr>'
         '<tr><td>J\'ai besoin d\'aide.</td><td>J\'<b>aurais</b> besoin d\'aide.</td></tr></table>'),
        ('Si + imparfait → conditionnel', None,
         '<p>La structure hypothétique principale au niveau A2 :</p>'
         '<p><b>Si + imparfait, conditionnel présent</b></p>'
         '<ul><li>Si j\'<b>avais</b> le temps, je <b>voyagerais</b> plus.</li>'
         '<li>Si elle <b>habitait</b> à Paris, on <b>se verrait</b> souvent.</li>'
         '<li>Si tu <b>étudiais</b> plus, tu <b>réussirais</b>.</li></ul>'
         '<p>Attention : jamais <b>si + conditionnel</b>. La subordonnée avec « si » est toujours à l\'imparfait.</p>'),
    ],
    'traps': [
        ('Si j\'aurais de l\'argent, j\'achèterais…', 'Si j\'avais de l\'argent, j\'achèterais…', 'Jamais conditionnel après « si » hypothétique → imparfait.'),
        ('Je voudrais un café, s\'il vous plaît.', 'Correct !', 'Le conditionnel de vouloir est la formule polie standard pour commander.'),
        ('Tu devrais pas fumer.', 'Tu ne devrais pas fumer.', 'La négation encadre le verbe : tu ne devrais pas + infinitif.'),
        ('Il vendrais sa voiture.', 'Il vendrait sa voiture.', 'Vendre → conditionnel : vendrait (pas vendrais → vendrais = je/tu).'),
        ('Nous irerions en France.', 'Nous irions en France.', 'Aller → radical ir- → nous irions (pas irerions).'),
    ],
    'summary': [
        ('Formation', 'radical futur + terminaisons imparfait', 'parler → parlerais · finir → finirais'),
        ('Irrég.', 'être→ser- · avoir→aur- · aller→ir- · faire→fer-', 'je serais · tu aurais · il irait'),
        ('Politesse', 'voudrais · pourriez · devriez · aimerais', 'Je voudrais un café, s\'il vous plaît.'),
        ('Souhait', 'j\'aimerais · je voudrais + infinitif', 'J\'aimerais voyager en Asie.'),
        ('Hypothèse', 'si + imparfait → conditionnel', 'Si j\'avais du temps, je lirais plus.'),
        ('Erreur fréq.', 'Jamais si + conditionnel !', '✗ Si j\'aurais… ✓ Si j\'avais…'),
    ],
    'ex1': ('Choisir la bonne forme', 'Sélectionnez la réponse correcte.',
        [
            ('Je ___ un thé, s\'il vous plaît. (vouloir)', ['veux', 'voudrais', 'voudrai', 'voulu'], 'voudrais',
             'Vouloir au conditionnel pour la politesse → je voudrais.'),
            ('Si elle ___ le temps, elle lirait plus. (avoir)', ['aurait', 'a', 'avait', 'aura'], 'avait',
             'Si + imparfait (jamais conditionnel après si) → si elle avait.'),
            ('Tu ___ dormir davantage. (devoir)', ['dois', 'devras', 'devrais', 'devrait'], 'devrais',
             'Devoir au conditionnel pour un conseil : tu devrais.'),
            ('Si j\'habitais à Paris, je ___ souvent au musée. (aller)', ['irai', 'irais', 'allais', 'aille'], 'irais',
             'Hypothèse : si + imparfait → conditionnel : j\'irais.'),
        ]),
    'ex2': ('Conjuguer au conditionnel', 'Donnez la forme correcte.',
        [
            ('Il ___ (vouloir) parler avec toi.', 'voudrait', 'Vouloir → radical voudr- → il voudrait.'),
            ('Nous ___ (pouvoir) vous aider.', 'pourrions', 'Pouvoir → radical pourr- → nous pourrions.'),
            ('Si tu ___ (étudier) plus, tu réussirais.', 'étudiais', 'Si + imparfait → tu étudiais (pas conditionnel).'),
            ('Elle ___ (aimer) vivre à Rome.', 'aimerait', 'Aimer → aimer + -ait → elle aimerait.'),
            ('Vous ___ (devoir) appeler avant de venir.', 'devriez', 'Devoir → radical devr- → vous devriez.'),
        ]),
    'ex3': ('Identifier l\'erreur', 'Quelle phrase est incorrecte ?',
        [
            ('Laquelle est incorrecte ?',
             ['Je voudrais un café.', 'Si j\'avais du temps, je lirais.', 'Si j\'aurais du temps, je lirais.', 'Tu devrais partir.'],
             'Si j\'aurais du temps, je lirais.',
             'Jamais conditionnel après « si » hypothétique : si j\'avais (imparfait), je lirais (conditionnel).'),
            ('Quel conditionnel irrégulier est faux ?',
             ['je serais', 'tu aurais', 'il irait', 'nous faisserions'],
             'nous faisserions',
             'Faire → radical fer- → nous ferions. « Faisserions » n\'existe pas.'),
            ('Quelle phrase de politesse est la plus correcte ?',
             ['Je veux un café.', 'Je voudrais un café.', 'Je voudrai un café.', 'Je veuxdrais un café.'],
             'Je voudrais un café.',
             'Le conditionnel de vouloir (voudrais) est la forme polie standard.'),
        ]),
    'game_desc': 'Maîtrisez le conditionnel présent en français !',
    'items': [
        ('cond-01', 'je voudrais', 'I would like (polite)', 'politesse', 'Je voudrais un café, s\'il vous plaît.', 'Je ___ un café, s\'il vous plaît.', 'voudrais'),
        ('cond-02', 'tu devrais', 'you should (advice)', 'conseil', 'Tu devrais dormir plus tôt.', 'Tu ___ dormir plus tôt.', 'devrais'),
        ('cond-03', 'il irait', 'he would go', 'irrégulier', 'Il irait en vacances si c\'était moins cher.', 'Il ___ en vacances si c\'était moins cher.', 'irait'),
        ('cond-04', 'nous pourrions', 'we could', 'irrégulier', 'Nous pourrions vous aider demain.', 'Nous ___ vous aider demain.', 'pourrions'),
        ('cond-05', 'si + imparfait', 'if + imperfect (hypothesis)', 'syntaxe', 'Si j\'avais du temps, je voyagerais.', 'Si j\'___ du temps, je voyagerais.', 'avais'),
        ('cond-06', 'j\'aimerais', 'I would love to', 'souhait', 'J\'aimerais visiter le Japon un jour.', 'J\'___ visiter le Japon un jour.', 'aimerais'),
        ('cond-07', 'elle serait', 'she would be', 'irrégulier', 'Elle serait contente de te voir.', 'Elle ___ contente de te voir.', 'serait'),
        ('cond-08', 'pourriez-vous ?', 'could you? (polite)', 'politesse', 'Pourriez-vous répéter, s\'il vous plaît ?', '___ -vous répéter, s\'il vous plaît ?', 'Pourriez'),
    ],
},

# ── G11 Les Prépositions de Lieu ───────────────────────────────────────────
'les-prepositions-de-lieu': {
    'level':   'a2',
    'section': 'grammaire',
    'num':     'G11',
    'short':   'Les Prépositions de Lieu',
    'title':   'Les Prépositions de Lieu — Exprimer l\'Espace',
    'subtitle': 'Prépositions de localisation, directions et pays/villes en français',
    'slides': [
        ('Prépositions de localisation', None,
         '<p>Pour situer quelque chose dans l\'espace :</p>'
         '<table><tr><th>Préposition</th><th>Sens</th><th>Exemple</th></tr>'
         '<tr><td><b>dans</b></td><td>inside / in</td><td>Le chat est dans la boîte.</td></tr>'
         '<tr><td><b>sur</b></td><td>on / on top of</td><td>Le livre est sur la table.</td></tr>'
         '<tr><td><b>sous</b></td><td>under / beneath</td><td>Les chaussures sont sous le lit.</td></tr>'
         '<tr><td><b>devant</b></td><td>in front of</td><td>Il attend devant la porte.</td></tr>'
         '<tr><td><b>derrière</b></td><td>behind</td><td>Le jardin est derrière la maison.</td></tr>'
         '<tr><td><b>entre</b></td><td>between</td><td>La pharmacie est entre la boulangerie et la banque.</td></tr>'
         '<tr><td><b>à côté de</b></td><td>next to</td><td>L\'école est à côté de la mairie.</td></tr>'
         '<tr><td><b>en face de</b></td><td>opposite / facing</td><td>L\'hôtel est en face de la gare.</td></tr></table>'),
        ('À, en, au, aux — pays et villes', None,
         '<p>Pour dire où l\'on est ou où l\'on va :</p>'
         '<table><tr><th>Contexte</th><th>Prép.</th><th>Exemples</th></tr>'
         '<tr><td>Ville</td><td><b>à</b></td><td>à Paris · à Rome · à Tokyo</td></tr>'
         '<tr><td>Pays féminin ou voyelle</td><td><b>en</b></td><td>en France · en Italie · en Iran</td></tr>'
         '<tr><td>Pays masculin</td><td><b>au</b></td><td>au Mexique · au Japon · au Canada</td></tr>'
         '<tr><td>Pays pluriel</td><td><b>aux</b></td><td>aux États-Unis · aux Pays-Bas</td></tr>'
         '<tr><td>Région féminine</td><td><b>en</b></td><td>en Bretagne · en Provence</td></tr>'
         '<tr><td>Région masculine</td><td><b>dans le</b></td><td>dans le Midi · dans le Nord</td></tr></table>'),
        ('Venir de / rentrer de — origine', None,
         '<p>Pour exprimer l\'origine ou la provenance :</p>'
         '<table><tr><th>Contexte</th><th>Prép.</th><th>Exemple</th></tr>'
         '<tr><td>Ville</td><td><b>de</b></td><td>Je viens de Paris.</td></tr>'
         '<tr><td>Pays féminin</td><td><b>de</b></td><td>Elle revient de France.</td></tr>'
         '<tr><td>Pays masculin</td><td><b>du</b></td><td>Il arrive du Mexique.</td></tr>'
         '<tr><td>Pays pluriel</td><td><b>des</b></td><td>Ils rentrent des États-Unis.</td></tr></table>'),
        ('Prépositions de direction', None,
         '<p>Pour indiquer le mouvement ou la direction :</p>'
         '<ul><li><b>aller à / vers</b> : aller à gauche · aller vers la mer</li>'
         '<li><b>tourner à</b> : tourner à droite · à gauche</li>'
         '<li><b>continuer tout droit</b> : continuez tout droit</li>'
         '<li><b>traverser</b> : traversez le pont</li>'
         '<li><b>prendre</b> : prenez la première rue à droite</li>'
         '<li><b>jusqu\'à</b> : allez jusqu\'à la place</li>'
         '<li><b>en face de / à droite de / à gauche de</b></li></ul>'),
        ('Prépositions utiles supplémentaires', None,
         '<p>Autres prépositions de lieu fréquentes :</p>'
         '<table><tr><th>Préposition</th><th>Sens</th><th>Exemple</th></tr>'
         '<tr><td><b>près de</b></td><td>near / close to</td><td>J\'habite près de la gare.</td></tr>'
         '<tr><td><b>loin de</b></td><td>far from</td><td>C\'est loin de chez moi.</td></tr>'
         '<tr><td><b>au bord de</b></td><td>at the edge / by</td><td>Une maison au bord de la mer.</td></tr>'
         '<tr><td><b>au milieu de</b></td><td>in the middle of</td><td>La fontaine est au milieu de la place.</td></tr>'
         '<tr><td><b>au bout de</b></td><td>at the end of</td><td>La boulangerie est au bout de la rue.</td></tr></table>'),
    ],
    'traps': [
        ('Je vais en Paris.', 'Je vais à Paris.', 'Avec une ville → à. En s\'utilise avec des pays/régions féminins.'),
        ('Je vais au France.', 'Je vais en France.', 'France est un pays féminin → en France. Au = de + le, pour les pays masculins.'),
        ('Je viens de le Canada.', 'Je viens du Canada.', 'De + le = du. Je viens du Canada (pays masculin).'),
        ('Il habite dans Paris.', 'Il habite à Paris. / Il habite dans le 5e arrondissement.', 'À + ville. « Dans » ne s\'utilise qu\'avec un quartier ou arrondissement spécifique.'),
        ('La banque est en face la gare.', 'La banque est en face de la gare.', '« En face de » est une locution prépositionnelle : elle exige toujours « de ».'),
    ],
    'summary': [
        ('Localisation', 'dans/sur/sous/devant/derrière/entre/à côté de', 'Le livre est sur la table.'),
        ('Ville', 'à + ville', 'Je suis à Lyon. / Je vais à Madrid.'),
        ('Pays fém.', 'en + pays féminin ou voyelle', 'en France · en Espagne · en Iran'),
        ('Pays masc.', 'au + pays masculin', 'au Mexique · au Japon · au Canada'),
        ('Pays plur.', 'aux + pays pluriel', 'aux États-Unis · aux Pays-Bas'),
        ('Origine', 'de (ville/fém.) · du (masc.) · des (plur.)', 'Je viens de Paris. / Je viens du Japon.'),
    ],
    'ex1': ('Choisir la bonne préposition', 'Complétez avec la préposition correcte.',
        [
            ('Je vais ___ Madrid la semaine prochaine.', ['en', 'au', 'à', 'dans'], 'à',
             'Madrid est une ville → à : je vais à Madrid.'),
            ('Elle habite ___ Japon depuis deux ans.', ['à', 'en', 'aux', 'au'], 'au',
             'Japon est un pays masculin → au Japon.'),
            ('Ils reviennent ___ États-Unis demain.', ['de', 'du', 'des', 'd\''], 'des',
             'Les États-Unis est un pays pluriel → ils reviennent des États-Unis.'),
            ('La pharmacie est ___ côté de la banque.', ['en', 'à', 'au', 'dans'], 'à',
             'À côté de est la locution correcte : à côté de la banque.'),
        ]),
    'ex2': ('Compléter les phrases', 'Écrivez la préposition correcte.',
        [
            ('Je viens ___ France. (pays féminin)', 'de', 'Venir de + pays féminin : je viens de France.'),
            ('Le chat est ___ la table. (dessous)', 'sous', 'Sous = under / beneath.'),
            ('Il habite ___ Mexique.', 'au', 'Mexique = pays masculin → au Mexique.'),
            ('La gare est ___ face de l\'hôtel.', 'en', 'En face de = opposite.'),
            ('J\'arrive ___ Pays-Bas demain.', 'des', 'Les Pays-Bas = pays pluriel → des Pays-Bas.'),
        ]),
    'ex3': ('Identifier l\'erreur', 'Quelle phrase est incorrecte ?',
        [
            ('Laquelle est incorrecte ?',
             ['Je vais à Paris.', 'J\'habite en France.', 'Il vient au Mexique.', 'Elle est aux États-Unis.'],
             'Il vient au Mexique.',
             'Venir de + pays masculin → il vient du Mexique. « Au » s\'utilise pour aller au / être au, pas venir au.'),
            ('Quelle préposition est fausse ?',
             ['en France', 'au Japon', 'aux États-Unis', 'en Canada'],
             'en Canada',
             'Canada est masculin → au Canada (pas en Canada).'),
            ('Quelle localisation est correcte ?',
             ['Le livre est dans la table.', 'Le livre est sur la table.', 'Le livre est en la table.', 'Le livre est à la table.'],
             'Le livre est sur la table.',
             'Sur = on top of (surface). Dans = inside. « En la » et « à la » ne s\'utilisent pas avec table ici.'),
        ]),
    'game_desc': 'Maîtrisez les prépositions de lieu en français !',
    'items': [
        ('lieu-01', 'à Paris', 'in/to Paris (city)', 'ville', 'Je vais à Paris la semaine prochaine.', 'Je vais ___ Paris la semaine prochaine.', 'à'),
        ('lieu-02', 'en France', 'in/to France (fem. country)', 'pays', 'Elle habite en France depuis dix ans.', 'Elle habite ___ France depuis dix ans.', 'en'),
        ('lieu-03', 'au Japon', 'in/to Japan (masc. country)', 'pays', 'Il travaille au Japon.', 'Il travaille ___ Japon.', 'au'),
        ('lieu-04', 'aux États-Unis', 'in/to the USA (plural)', 'pays', 'Ils vivent aux États-Unis.', 'Ils vivent ___ États-Unis.', 'aux'),
        ('lieu-05', 'sous la table', 'under the table', 'localisation', 'Le chien est sous la table.', 'Le chien est ___ la table.', 'sous'),
        ('lieu-06', 'à côté de', 'next to', 'localisation', 'La pharmacie est à côté de la banque.', 'La pharmacie est à ___ de la banque.', 'côté'),
        ('lieu-07', 'en face de', 'opposite / facing', 'localisation', 'L\'hôtel est en face de la gare.', 'L\'hôtel est ___ face de la gare.', 'en'),
        ('lieu-08', 'près de', 'near / close to', 'localisation', 'J\'habite près de la gare.', 'J\'habite ___ de la gare.', 'près'),
    ],
},

# ── G12 Le Subjonctif — Introduction ──────────────────────────────────────
'le-subjonctif-intro': {
    'level':   'a2',
    'section': 'grammaire',
    'num':     'G12',
    'short':   'Le Subjonctif',
    'title':   'Le Subjonctif — Introduction',
    'subtitle': 'Reconnaître et former le subjonctif présent des verbes courants',
    'slides': [
        ('Qu\'est-ce que le subjonctif ?', None,
         '<p>Le subjonctif exprime une <b>subjectivité</b> : doute, émotion, volonté, nécessité :</p>'
         '<ul><li><b>Volonté</b> : Je veux qu\'il <b>vienne</b>.</li>'
         '<li><b>Émotion</b> : Je suis content que tu <b>sois</b> là.</li>'
         '<li><b>Nécessité</b> : Il faut que tu <b>fasses</b> tes devoirs.</li>'
         '<li><b>Doute</b> : Je ne crois pas qu\'il <b>ait</b> raison.</li></ul>'
         '<p>Repère : le subjonctif apparaît après <b>que</b> dans une proposition subordonnée, quand les deux sujets sont différents.</p>'),
        ('Formation — verbes réguliers', None,
         '<p>Base : <b>3e personne du pluriel du présent</b> (ils) — on enlève -ent, on ajoute :</p>'
         '<table><tr><th>Sujet</th><th>Terminaison</th><th>Parler → parl-</th><th>Finir → finiss-</th></tr>'
         '<tr><td>que je</td><td>-e</td><td>parle</td><td>finisse</td></tr>'
         '<tr><td>que tu</td><td>-es</td><td>parles</td><td>finisses</td></tr>'
         '<tr><td>qu\'il/elle</td><td>-e</td><td>parle</td><td>finisse</td></tr>'
         '<tr><td>que nous</td><td>-ions</td><td>parlions</td><td>finissions</td></tr>'
         '<tr><td>que vous</td><td>-iez</td><td>parliez</td><td>finissiez</td></tr>'
         '<tr><td>qu\'ils/elles</td><td>-ent</td><td>parlent</td><td>finissent</td></tr></table>'),
        ('Subjonctifs irréguliers courants', None,
         '<table><tr><th>Verbe</th><th>Subj. sing.</th><th>Subj. nous/vous</th></tr>'
         '<tr><td><b>être</b></td><td>sois · soit</td><td>soyons · soyez</td></tr>'
         '<tr><td><b>avoir</b></td><td>aie · ait</td><td>ayons · ayez</td></tr>'
         '<tr><td><b>aller</b></td><td>aille · ailles</td><td>allions · alliez</td></tr>'
         '<tr><td><b>faire</b></td><td>fasse · fasses</td><td>fassions · fassiez</td></tr>'
         '<tr><td><b>pouvoir</b></td><td>puisse · puisses</td><td>puissions · puissiez</td></tr>'
         '<tr><td><b>vouloir</b></td><td>veuille · veuilles</td><td>voulions · vouliez</td></tr>'
         '<tr><td><b>savoir</b></td><td>sache · saches</td><td>sachions · sachiez</td></tr></table>'),
        ('Déclencheurs du subjonctif', None,
         '<p>Le subjonctif est obligatoire après ces expressions :</p>'
         '<p><b>Volonté/souhait :</b> vouloir que · souhaiter que · aimer que · préférer que</p>'
         '<p><b>Nécessité :</b> il faut que · il est nécessaire que · il est important que</p>'
         '<p><b>Émotion :</b> être content/heureux/triste/surpris que · avoir peur que</p>'
         '<p><b>Doute :</b> douter que · ne pas croire que · ne pas penser que</p>'
         '<p><b>Conjonctions :</b> pour que · bien que · avant que · à condition que</p>'),
        ('Subjonctif ou infinitif ?', None,
         '<p>Si les deux verbes ont le <b>même sujet</b> → infinitif :<br>'
         'Je veux <b>partir</b>. (je veux → je pars : même sujet)</p>'
         '<p>Si les deux verbes ont des <b>sujets différents</b> → subjonctif :<br>'
         'Je veux qu\'il <b>parte</b>. (je veux → il part : sujets différents)</p>'
         '<p>Exemples :</p>'
         '<ul><li>Je préfère <b>rester</b>. (même sujet) ✓</li>'
         '<li>Je préfère que tu <b>restes</b>. (sujets différents) ✓</li>'
         '<li>Il est content de <b>partir</b>. (même sujet) ✓</li>'
         '<li>Il est content que vous <b>veniez</b>. (sujets différents) ✓</li></ul>'),
    ],
    'traps': [
        ('Il faut que tu viens.', 'Il faut que tu viennes.', 'Après « il faut que », le subjonctif est obligatoire : viennes (pas viens).'),
        ('Je suis content que tu viens.', 'Je suis content que tu viennes.', 'Émotion + que → subjonctif : tu viennes.'),
        ('Je veux partir.', 'Correct !', 'Même sujet → infinitif. Je veux partir = correct (pas je veux que je parte).'),
        ('Il faut qu\'il est là.', 'Il faut qu\'il soit là.', 'Être au subjonctif : soit (pas est). « Il faut que » déclenche toujours le subjonctif.'),
        ('Bien que il fait beau.', 'Bien que il fasse beau.', 'Bien que + subjonctif : fasse (pas fait).'),
    ],
    'summary': [
        ('Rôle', 'subjectivité : volonté, émotion, nécessité, doute', 'Il faut que tu viennes.'),
        ('Formation', 'base ils-présent + -e/-es/-e/-ions/-iez/-ent', 'parler → parl- → que je parle'),
        ('Irrég.', 'être→sois · avoir→aie · faire→fasse · aller→aille', 'il faut qu\'il soit là'),
        ('Déclencheurs', 'vouloir que · il faut que · être content que', 'Je veux qu\'il parte.'),
        ('Subj. vs inf.', 'même sujet → infinitif / sujets diff. → subjonctif', 'Je veux partir. / Je veux qu\'il parte.'),
        ('Conjonctions', 'pour que · bien que · avant que + subjonctif', 'Je pars avant qu\'il arrive.'),
    ],
    'ex1': ('Choisir la bonne forme', 'Subjonctif ou indicatif ?',
        [
            ('Il faut que tu ___ tes devoirs. (faire)', ['fais', 'fasse', 'fasses', 'fait'], 'fasses',
             'Il faut que + subjonctif → que tu fasses (faire irrégulier : fass-).'),
            ('Je suis content que vous ___ là. (être)', ['êtes', 'soyez', 'serez', 'soyons'], 'soyez',
             'Émotion + que → subjonctif → être irrégulier : que vous soyez.'),
            ('Elle veut que son fils ___ médecin. (devenir)', ['devient', 'devienne', 'deviendra', 'devenu'], 'devienne',
             'Volonté + que → subjonctif → devenir : base devien- → qu\'il devienne.'),
            ('Je veux ___ avec toi. (partir — même sujet)', ['que je parte', 'partir', 'parte', 'partirai'], 'partir',
             'Même sujet → infinitif : je veux partir.'),
        ]),
    'ex2': ('Conjuguer au subjonctif', 'Donnez la forme correcte.',
        [
            ('Il faut qu\'il ___ (être) là à 8 h.', 'soit', 'Être → subjonctif irrégulier : qu\'il soit.'),
            ('Je préfère que tu ___ (venir).', 'viennes', 'Venir → base vien- → que tu viennes.'),
            ('Elle veut que nous ___ (parler) français.', 'parlions', 'Parler → que nous parlions (base parl- + -ions).'),
            ('Il est important que vous ___ (faire) attention.', 'fassiez', 'Faire irrégulier : que vous fassiez.'),
            ('Je doute qu\'il ___ (avoir) raison.', 'ait', 'Avoir → subjonctif irrégulier : qu\'il ait.'),
        ]),
    'ex3': ('Identifier l\'erreur', 'Quelle phrase est incorrecte ?',
        [
            ('Laquelle est incorrecte ?',
             ['Il faut que tu parles.', 'Je veux partir.', 'Je veux que tu partir.', 'Elle veut qu\'il vienne.'],
             'Je veux que tu partir.',
             'Sujets différents + vouloir que → subjonctif : je veux que tu partes (pas infinitif).'),
            ('Quel subjonctif irrégulier est incorrect ?',
             ['que je sois', 'que tu aies', 'qu\'il fassit', 'que nous allions'],
             'qu\'il fassit',
             'Faire → subjonctif irrégulier : qu\'il fasse (pas fassit). La base est fass-, pas faiss-.'),
            ('Quelle phrase avec « il faut que » est correcte ?',
             ['Il faut que tu viens.', 'Il faut que tu viennes.', 'Il faut tu viennes.', 'Il faut que tu venais.'],
             'Il faut que tu viennes.',
             'Il faut que + subjonctif : venir → que tu viennes. C\'est la seule forme correcte.'),
        ]),
    'game_desc': 'Découvrez le subjonctif présent en français !',
    'items': [
        ('subj-01', 'il faut que', 'it is necessary that', 'déclencheur', 'Il faut que tu fasses tes devoirs.', 'Il faut que tu ___ tes devoirs. (faire)', 'fasses'),
        ('subj-02', 'que tu sois', 'that you are (être)', 'irrégulier', 'Je suis content que tu sois là.', 'Je suis content que tu ___ là. (être)', 'sois'),
        ('subj-03', 'qu\'il aille', 'that he goes (aller)', 'irrégulier', 'Je veux qu\'il aille à l\'école.', 'Je veux qu\'il ___ à l\'école. (aller)', 'aille'),
        ('subj-04', 'que vous fassiez', 'that you do (faire)', 'irrégulier', 'Il est important que vous fassiez attention.', 'Il est important que vous ___ attention. (faire)', 'fassiez'),
        ('subj-05', 'je veux partir', 'I want to leave (same subj.)', 'infinitif', 'Je veux partir demain matin.', 'Je veux ___. (même sujet → infinitif)', 'partir'),
        ('subj-06', 'pour que', 'so that (+ subjonctif)', 'conjonction', 'Je t\'explique pour que tu comprennes.', 'Je t\'explique ___ tu comprennes.', 'pour que'),
        ('subj-07', 'bien que', 'although (+ subjonctif)', 'conjonction', 'Bien qu\'il fasse froid, je sors.', 'Bien ___ il fasse froid, je sors.', 'qu\''),
        ('subj-08', 'qu\'il vienne', 'that he comes (venir)', 'régulier', 'Je préfère qu\'il vienne demain.', 'Je préfère qu\'il ___ demain. (venir)', 'vienne'),
    ],
},

}
