"""Français A1 — Rédaction batch 1: R01–R04."""

CHAPTERS = {

# ── R01 Se Présenter ───────────────────────────────────────────────────────
'se-presenter': {
    'level':   'a1',
    'section': 'redaction',
    'num':     'R01',
    'short':   'Se Présenter',
    'title':   'Se Présenter — Dire Qui On Est',
    'subtitle': 'Écrire une courte présentation : nom, âge, nationalité, profession',
    'slides': [
        ('La présentation personnelle', None,
         '<p>En français, une présentation de base répond à cinq questions :</p>'
         '<ul><li><b>Qui ?</b> Je m\'appelle…</li>'
         '<li><b>Âge ?</b> J\'ai… ans.</li>'
         '<li><b>Origine ?</b> Je suis… (nationalité)</li>'
         '<li><b>Lieu ?</b> J\'habite à…</li>'
         '<li><b>Travail ?</b> Je suis… / Je travaille comme…</li></ul>'
         '<p>Ces cinq éléments forment le bloc de base de toute présentation écrite au niveau A1.</p>'),
        ('Nom et origine', None,
         '<p>Pour le nom : <b>Je m\'appelle</b> + prénom + nom.<br>'
         'Pour l\'origine : <b>Je suis</b> + nationalité (adjectif accordé).</p>'
         '<table><tr><th>Masculin</th><th>Féminin</th></tr>'
         '<tr><td>Je suis français</td><td>Je suis française</td></tr>'
         '<tr><td>Je suis espagnol</td><td>Je suis espagnole</td></tr>'
         '<tr><td>Je suis anglais</td><td>Je suis anglaise</td></tr>'
         '<tr><td>Je suis américain</td><td>Je suis américaine</td></tr></table>'
         '<p>Attention : les nationalités ne prennent <b>pas de majuscule</b> en français.</p>'),
        ('L\'âge et le lieu', None,
         '<p>Pour l\'âge : <b>J\'ai</b> + nombre + <b>ans</b>. (Jamais <i>Je suis 25 ans</i> !)</p>'
         '<p>Pour le lieu : <b>J\'habite à</b> + ville / <b>J\'habite en</b> + pays féminin / '
         '<b>J\'habite au</b> + pays masculin.</p>'
         '<ul><li>J\'habite <b>à</b> Paris.</li>'
         '<li>J\'habite <b>en</b> France.</li>'
         '<li>J\'habite <b>au</b> Mexique.</li>'
         '<li>J\'habite <b>aux</b> États-Unis.</li></ul>'),
        ('La profession', None,
         '<p>Pour la profession : <b>Je suis</b> + métier (sans article !).<br>'
         'Ou : <b>Je travaille comme</b> + métier.</p>'
         '<ul><li>Je suis <b>professeur</b>. ✓</li>'
         '<li>Je suis <b>un professeur</b>. ✗ (sans article)</li>'
         '<li>Je suis <b>étudiant(e)</b>.</li>'
         '<li>Je suis <b>médecin</b>.</li>'
         '<li>Je travaille comme <b>ingénieur</b>.</li></ul>'),
        ('Modèle de présentation', None,
         '<p>Voici un exemple complet à adapter :</p>'
         '<blockquote><p><b>Bonjour ! Je m\'appelle Sophie Dupont.</b><br>'
         'J\'ai vingt-huit ans. Je suis française.<br>'
         'J\'habite à Lyon, en France.<br>'
         'Je suis professeure de mathématiques.<br>'
         'J\'aime lire et voyager.<br>'
         'Enchanté(e) !</p></blockquote>'
         '<p>Structure : salutation → nom → âge → nationalité → lieu → profession → loisirs → formule de clôture.</p>'),
    ],
    'traps': [
        ('J\'ai vingt ans old.', 'J\'ai vingt ans.', 'Ne jamais ajouter « old » — en français, ans suffit.'),
        ('Je suis 30 ans.', 'J\'ai 30 ans.', 'L\'âge s\'exprime avec avoir, pas être.'),
        ('Je suis un étudiant.', 'Je suis étudiant.', 'Après « je suis + profession », pas d\'article.'),
        ('Je suis Français.', 'Je suis français.', 'Les nationalités sont en minuscule en français.'),
        ('J\'habite en Paris.', 'J\'habite à Paris.', 'Avec une ville, on utilise à, pas en.'),
    ],
    'summary': [
        ('Nom', 'Je m\'appelle + prénom/nom', 'Je m\'appelle Marie Lefebvre.'),
        ('Âge', 'J\'ai + nombre + ans', 'J\'ai vingt-trois ans.'),
        ('Nationalité', 'Je suis + adj. accordé (minuscule)', 'Je suis espagnole.'),
        ('Lieu', 'J\'habite à/en/au/aux + lieu', 'J\'habite à Barcelone, en Espagne.'),
        ('Profession', 'Je suis + métier (sans article)', 'Je suis ingénieur.'),
        ('Clôture', 'Enchanté(e) ! / Ravi(e) de vous rencontrer.', 'Enchanté !'),
    ],
    'ex1': ('Choisir la bonne formule', 'Choisissez la réponse correcte.',
        [
            ('Comment dit-on son âge en français ?',
             ['Je suis 25 ans.', 'J\'ai 25 ans.', 'J\'ai 25 years.', 'Je suis vingt-cinq years old.'],
             'J\'ai 25 ans.',
             'L\'âge s\'exprime avec avoir + nombre + ans. Jamais « être » pour l\'âge.'),
            ('Quelle phrase est correcte ?',
             ['Je suis un médecin.', 'Je suis médecin.', 'Je suis la médecin.', 'J\'ai médecin.'],
             'Je suis médecin.',
             'Après être + profession, on n\'utilise pas d\'article en français.'),
            ('Comment s\'appelle la règle pour les nationalités ?',
             ['Majuscule toujours', 'Minuscule toujours', 'Majuscule pour les femmes', 'Majuscule si pays connu'],
             'Minuscule toujours',
             'En français, les adjectifs de nationalité prennent toujours la minuscule : je suis français, espagnol, anglais…'),
            ('J\'habite ___ Londres.',
             ['en', 'au', 'à', 'aux'],
             'à',
             'On dit à + ville : à Paris, à Londres, à Madrid. En/au/aux s\'utilisent avec des pays.'),
        ]),
    'ex2': ('Compléter la présentation', 'Complétez avec le mot manquant.',
        [
            ('Je ___ appelle Thomas.', 'm\'', 'Le verbe s\'appeler se construit avec le pronom réfléchi : je m\'appelle.'),
            ('J\'___ vingt ans.', 'ai', 'L\'âge s\'exprime avec avoir : j\'ai… ans.'),
            ('Je suis ___. (France / masculin)', 'français', 'La nationalité est un adjectif accordé en genre, toujours en minuscule.'),
            ('J\'habite ___ Madrid.', 'à', 'À + ville. En/au/aux + pays.'),
            ('Je suis ___. (profession : enseigner)', 'professeur', 'Être + profession sans article.'),
        ]),
    'ex3': ('Identifier l\'erreur', 'Quelle phrase contient une erreur ?',
        [
            ('Trouvez l\'erreur dans la présentation.',
             ['Je m\'appelle Ana. J\'ai dix-neuf ans.', 'Je suis Espagnole et j\'habite à Madrid.', 'Je suis étudiante en économie.', 'J\'aime la musique et le sport.'],
             'Je suis Espagnole et j\'habite à Madrid.',
             'Les nationalités prennent la minuscule : espagnole, pas Espagnole.'),
            ('Quelle phrase est incorrecte ?',
             ['J\'ai trente ans.', 'Je suis professeur.', 'J\'habite à Berlin.', 'Je suis un architecte.'],
             'Je suis un architecte.',
             'Après être + profession, pas d\'article : je suis architecte.'),
            ('Quel lieu nécessite « en » ?',
             ['à Paris', 'au Mexique', 'en France', 'aux États-Unis'],
             'en France',
             'En + pays féminin (France, Espagne, Italie…). À + ville, au + pays masculin, aux + pays pluriel.'),
        ]),
    'game_desc': 'Testez votre maîtrise des formules de présentation en français !',
    'items': [
        ('pres-01', 'Je m\'appelle', 'my name is', 'se nommer', 'Je m\'appelle Sophie Dupont.', 'Je ___ appelle Sophie Dupont.', 'm\''),
        ('pres-02', 'J\'ai … ans', 'I am … years old', 'âge', 'J\'ai vingt-huit ans.', 'J\'___ vingt-huit ans.', 'ai'),
        ('pres-03', 'je suis + nationalité', 'I am + nationality', 'origine', 'Je suis française.', 'Je ___ française.', 'suis'),
        ('pres-04', 'j\'habite à', 'I live in (city)', 'lieu', 'J\'habite à Lyon.', 'J\'habite ___ Lyon.', 'à'),
        ('pres-05', 'je suis + métier', 'I am a + profession', 'profession', 'Je suis professeure.', 'Je suis ___. (enseigner)', 'professeure'),
        ('pres-06', 'enchanté(e)', 'pleased to meet you', 'formule', 'Enchanté ! Ravi de vous rencontrer.', '___ ! Ravi de vous rencontrer.', 'Enchanté'),
        ('pres-07', 'j\'habite en', 'I live in (country f.)', 'lieu', 'J\'habite en France.', 'J\'habite ___ France.', 'en'),
        ('pres-08', 'j\'habite au', 'I live in (country m.)', 'lieu', 'J\'habite au Mexique.', 'J\'habite ___ Mexique.', 'au'),
    ],
},

# ── R02 Décrire une Personne ───────────────────────────────────────────────
'decrire-une-personne': {
    'level':   'a1',
    'section': 'redaction',
    'num':     'R02',
    'short':   'Décrire une Personne',
    'title':   'Décrire une Personne — Apparence et Caractère',
    'subtitle': 'Rédiger une description physique et de caractère au niveau A1',
    'slides': [
        ('Décrire l\'apparence', None,
         '<p>Pour décrire quelqu\'un physiquement, on utilise le verbe <b>avoir</b> pour les traits physiques et <b>être</b> pour la taille et le caractère.</p>'
         '<ul><li><b>Il/Elle a</b> les yeux bleus / marron / verts.</li>'
         '<li><b>Il/Elle a</b> les cheveux courts / longs / frisés / raides.</li>'
         '<li><b>Il/Elle a</b> les cheveux blonds / bruns / roux / noirs.</li>'
         '<li><b>Il/Elle est</b> grand(e) / petit(e) / de taille moyenne.</li></ul>'),
        ('Les cheveux et les yeux', None,
         '<table><tr><th>Cheveux — forme</th><th>Cheveux — couleur</th><th>Yeux — couleur</th></tr>'
         '<tr><td>courts</td><td>blonds</td><td>bleus</td></tr>'
         '<tr><td>longs</td><td>bruns</td><td>verts</td></tr>'
         '<tr><td>frisés</td><td>roux</td><td>marron (inv.)</td></tr>'
         '<tr><td>raides</td><td>noirs</td><td>gris</td></tr>'
         '<tr><td>mi-longs</td><td>gris / blancs</td><td>noisette</td></tr></table>'
         '<p>Rappel : <b>marron</b> est invariable (pas de marrons).</p>'),
        ('Le caractère', None,
         '<p>Pour le caractère, on utilise <b>être</b> + adjectif accordé :</p>'
         '<ul><li>Il/Elle est <b>sympa(thique)</b> / <b>gentil(le)</b>.</li>'
         '<li>Il/Elle est <b>drôle</b> / <b>sérieux(-euse)</b>.</li>'
         '<li>Il/Elle est <b>timide</b> / <b>bavard(e)</b>.</li>'
         '<li>Il/Elle est <b>généreux(-euse)</b> / <b>égoïste</b>.</li>'
         '<li>Il/Elle est <b>patient(e)</b> / <b>impatient(e)</b>.</li></ul>'
         '<p>L\'adjectif <b>s\'accorde</b> toujours avec la personne décrite.</p>'),
        ('L\'accord des adjectifs', None,
         '<p>Les adjectifs s\'accordent en <b>genre</b> (masculin/féminin) et en <b>nombre</b> (singulier/pluriel).</p>'
         '<table><tr><th></th><th>Masc. sing.</th><th>Fém. sing.</th></tr>'
         '<tr><td>grand</td><td>Il est <b>grand</b></td><td>Elle est <b>grande</b></td></tr>'
         '<tr><td>brun</td><td>Il est <b>brun</b></td><td>Elle est <b>brune</b></td></tr>'
         '<tr><td>sérieux</td><td>Il est <b>sérieux</b></td><td>Elle est <b>sérieuse</b></td></tr>'
         '<tr><td>gentil</td><td>Il est <b>gentil</b></td><td>Elle est <b>gentille</b></td></tr></table>'),
        ('Modèle de description', None,
         '<p>Voici un exemple complet :</p>'
         '<blockquote><p><b>Mon ami s\'appelle Lucas.</b><br>'
         'Il a trente ans. Il est grand et mince.<br>'
         'Il a les cheveux bruns et courts.<br>'
         'Il a les yeux verts.<br>'
         'Il est sympa et très drôle.<br>'
         'Il aime le football et la musique.</p></blockquote>'
         '<p>Ordre conseillé : nom → âge → taille → cheveux → yeux → caractère → loisirs.</p>'),
    ],
    'traps': [
        ('Elle a grand.', 'Elle est grande.', 'La taille s\'exprime avec être, pas avoir.'),
        ('Il a les yeux marrons.', 'Il a les yeux marron.', 'Marron est invariable en français : pas de -s au pluriel.'),
        ('Elle est une gentille.', 'Elle est gentille.', 'Après être + adjectif de caractère, pas d\'article.'),
        ('Il a les cheveux le brun.', 'Il a les cheveux bruns.', 'La couleur des cheveux est un adjectif, pas un nom avec article.'),
        ('Elle est sérieux.', 'Elle est sérieuse.', 'L\'adjectif s\'accorde avec le sujet : sérieux (m.) → sérieuse (f.).'),
    ],
    'summary': [
        ('Taille', 'être + grand(e) / petit(e) / de taille moyenne', 'Il est grand et mince.'),
        ('Cheveux', 'avoir les cheveux + couleur + forme', 'Elle a les cheveux longs et blonds.'),
        ('Yeux', 'avoir les yeux + couleur', 'Il a les yeux marron. (invariable)'),
        ('Caractère', 'être + adjectif accordé', 'Elle est sympa et généreuse.'),
        ('Accord adj.', 'masc. → fém. : +e / -eux→-euse / -il→-ille', 'sérieux → sérieuse · gentil → gentille'),
        ('Ordre', 'nom → âge → taille → cheveux → yeux → caractère', 'Mon ami Lucas a 30 ans. Il est grand…'),
    ],
    'ex1': ('Choisir la bonne description', 'Choisissez la réponse correcte.',
        [
            ('Comment décrit-on la taille en français ?',
             ['Il a grand.', 'Il est grand.', 'Il fait grand.', 'Il a de la grandeur.'],
             'Il est grand.',
             'La taille s\'exprime avec être + adjectif : il est grand, elle est petite.'),
            ('Laquelle est correcte ?',
             ['Elle a les yeux marrons.', 'Elle a les yeux marron.', 'Elle est les yeux marron.', 'Elle a yeux marron.'],
             'Elle a les yeux marron.',
             'Marron est invariable (pas de -s). Les yeux s\'expriment avec avoir.'),
            ('Comment dit-on qu\'elle est sympa ?',
             ['Elle a sympa.', 'Elle est sympa.', 'Elle fait sympa.', 'Elle a de la sympa.'],
             'Elle est sympa.',
             'Les adjectifs de caractère s\'utilisent avec être.'),
            ('Quelle est la forme féminine de « sérieux » ?',
             ['sérieuse', 'sérieusse', 'sérieuxe', 'sérieux'],
             'sérieuse',
             'Les adjectifs en -eux forment leur féminin en -euse : sérieux → sérieuse.'),
        ]),
    'ex2': ('Compléter la description', 'Complétez avec le mot manquant.',
        [
            ('Il ___ les cheveux blonds.', 'a', 'Les caractéristiques physiques (cheveux, yeux) s\'expriment avec avoir.'),
            ('Elle ___ grande et mince.', 'est', 'La taille et le caractère s\'expriment avec être.'),
            ('Il a les yeux ___. (couleur invariable)', 'marron', 'Marron est invariable : pas de -s même au pluriel.'),
            ('Elle est ___. (féminin de « gentil »)', 'gentille', 'Gentil → gentille au féminin (doublement du -l).'),
            ('Il a les cheveux courts et ___. (couleur : brun au pluriel)', 'bruns', 'L\'adjectif de couleur s\'accorde en genre et en nombre avec le nom.'),
        ]),
    'ex3': ('Identifier l\'erreur', 'Quelle phrase contient une erreur ?',
        [
            ('Choisissez la phrase correcte.',
             ['Il est grand.', 'Elle a les yeux bleus.', 'Il a les cheveux roux.', 'Elle a petite.'],
             'Elle a petite.',
             'La taille s\'exprime avec être, pas avoir : elle est petite.'),
            ('Trouvez l\'erreur.',
             ['Il est sympa et drôle.', 'Elle est sérieuse.', 'Il est un gentil.', 'Elle est timide.'],
             'Il est un gentil.',
             'Après être + adjectif, on n\'utilise pas d\'article : il est gentil.'),
            ('Quelle description est incorrecte ?',
             ['Elle a les yeux verts.', 'Il a les cheveux bruns.', 'Elle a les yeux marron.', 'Il a les cheveux le noir.'],
             'Il a les cheveux le noir.',
             'La couleur des cheveux est un adjectif, pas un groupe nominal avec article : il a les cheveux noirs.'),
        ]),
    'game_desc': 'Maîtrisez les formules pour décrire une personne en français !',
    'items': [
        ('desc-01', 'il/elle est grand(e)', 'he/she is tall', 'taille', 'Il est grand et mince.', 'Il ___ grand et mince.', 'est'),
        ('desc-02', 'il/elle a les yeux', 'he/she has … eyes', 'yeux', 'Elle a les yeux bleus.', 'Elle a les ___ bleus.', 'yeux'),
        ('desc-03', 'il/elle a les cheveux', 'he/she has … hair', 'cheveux', 'Il a les cheveux courts et bruns.', 'Il a les ___ courts et bruns.', 'cheveux'),
        ('desc-04', 'marron (invariable)', 'brown (invariable)', 'couleur', 'Elle a les yeux marron.', 'Elle a les yeux ___. (brun/inv.)', 'marron'),
        ('desc-05', 'sérieux → sérieuse', 'serious (f.)', 'accord', 'Elle est sérieuse et patiente.', 'Elle est ___ et patiente. (sérieux/f.)', 'sérieuse'),
        ('desc-06', 'gentil → gentille', 'kind (f.)', 'accord', 'Elle est très gentille.', 'Elle est très ___. (gentil/f.)', 'gentille'),
        ('desc-07', 'de taille moyenne', 'of medium height', 'taille', 'Il est de taille moyenne.', 'Il est de taille ___.',  'moyenne'),
        ('desc-08', 'bavard(e)', 'talkative', 'caractère', 'Il est très bavard en classe.', 'Il est très ___ en classe.', 'bavard'),
    ],
},

# ── R03 Écrire un Message Simple ───────────────────────────────────────────
'ecrire-un-message': {
    'level':   'a1',
    'section': 'redaction',
    'num':     'R03',
    'short':   'Écrire un Message',
    'title':   'Écrire un Message Simple — SMS et Courriel',
    'subtitle': 'Rédiger un court message, un SMS ou un courriel informel au niveau A1',
    'slides': [
        ('La structure d\'un message', None,
         '<p>Tout message écrit en français, même court, a une structure de base :</p>'
         '<ol><li><b>Salutation :</b> Bonjour, / Salut, / Chère Marie, / Cher Thomas,</li>'
         '<li><b>Corps du message :</b> l\'information principale</li>'
         '<li><b>Formule de clôture :</b> À bientôt, / Bises, / Cordialement,</li>'
         '<li><b>Signature :</b> ton prénom</li></ol>'
         '<p>Un message A1 peut avoir seulement 3–5 phrases, mais doit toujours avoir ces quatre parties.</p>'),
        ('Les salutations et formules de clôture', None,
         '<table><tr><th>Contexte</th><th>Salutation</th><th>Clôture</th></tr>'
         '<tr><td>Ami(e)</td><td>Salut, / Coucou,</td><td>Bises, / À bientôt,</td></tr>'
         '<tr><td>Famille</td><td>Bonjour, / Chère Maman,</td><td>Bisous, / Je t\'embrasse,</td></tr>'
         '<tr><td>Formel</td><td>Bonjour Madame, / Cher Monsieur,</td><td>Cordialement, / Bien à vous,</td></tr></table>'
         '<p>Pour un SMS entre amis, la salutation peut être très courte ou absente.</p>'),
        ('Donner des informations pratiques', None,
         '<p>Un message A1 donne souvent des informations pratiques. Utilisez :</p>'
         '<ul><li><b>Lieu :</b> Je suis à… / On se retrouve à…</li>'
         '<li><b>Heure :</b> À… heures / À quelle heure ?</li>'
         '<li><b>Date :</b> Le… / Mardi prochain / Ce week-end</li>'
         '<li><b>Invitation :</b> Tu veux venir ? / On peut se voir ?</li>'
         '<li><b>Confirmation :</b> D\'accord ! / C\'est parfait. / Je ne peux pas.</li></ul>'),
        ('Exprimer ses besoins et demandes', None,
         '<p>Pour demander quelque chose poliment :</p>'
         '<ul><li><b>Est-ce que tu peux…</b> + infinitif ? (informel)</li>'
         '<li><b>Pouvez-vous…</b> + infinitif ? (formel)</li>'
         '<li><b>J\'ai besoin de…</b> + nom</li>'
         '<li><b>Je voudrais…</b> + infinitif / nom</li>'
         '<li><b>S\'il te plaît</b> (informel) / <b>S\'il vous plaît</b> (formel)</li></ul>'),
        ('Modèle de message', None,
         '<p>Voici un exemple de message à un(e) ami(e) :</p>'
         '<blockquote><p>Salut Léa,<br><br>'
         'Comment tu vas ? Moi, ça va bien.<br>'
         'Tu veux aller au cinéma samedi soir ?<br>'
         'Il y a un film super à 20 h.<br>'
         'Réponds-moi vite !<br><br>'
         'Bises,<br>Emma</p></blockquote>'
         '<p>5 phrases suffisent : salutation → nouvelle → invitation → détail → clôture.</p>'),
    ],
    'traps': [
        ('Chère Marie, … Amicalement,', 'Chère Marie, … Bises,', '« Amicalement » est semi-formel. Avec une amie, on écrit « Bises » ou « À bientôt ».'),
        ('Bonjour, je voudrais… Bises,', 'Bonjour Monsieur, je voudrais… Cordialement,', 'Dans un message formel, la clôture doit aussi être formelle. « Bises » est trop familier.'),
        ('On se retrouve à le café.', 'On se retrouve au café.', 'À + le = au. Contraction obligatoire.'),
        ('Je veux venir demain ?', 'Tu veux venir demain ?', 'Pour inviter, on demande à l\'autre : « Tu veux… ? » pas « Je veux… ? »'),
        ('À bientôt. Tom', 'À bientôt,\nTom', 'La formule de clôture est suivie d\'une virgule, puis la signature est sur une nouvelle ligne.'),
    ],
    'summary': [
        ('Structure', 'Salutation → corps → clôture → signature', 'Salut, / … / À bientôt, / Emma'),
        ('Ami(e)', 'Salut, / Coucou, → Bises, / À bientôt,', 'Salut Léa, … Bises, Emma'),
        ('Formel', 'Bonjour Madame, → Cordialement,', 'Bonjour Monsieur, … Cordialement, M. Dupont'),
        ('Invitation', 'Tu veux + infinitif ?', 'Tu veux venir au cinéma samedi ?'),
        ('Demande', 'Est-ce que tu peux + infinitif ?', 'Est-ce que tu peux m\'appeler ?'),
        ('Lieu', 'On se retrouve à/au/en…', 'On se retrouve au café à 18 h.'),
    ],
    'ex1': ('Choisir la bonne formule', 'Choisissez la réponse correcte.',
        [
            ('Quelle clôture convient à un message à un ami ?',
             ['Cordialement,', 'Bien à vous,', 'Bises,', 'Veuillez agréer mes salutations.'],
             'Bises,',
             '« Bises » est la formule amicale standard. « Cordialement » et « Bien à vous » sont formels.'),
            ('On se retrouve ___ café.',
             ['à le', 'au', 'en', 'du'],
             'au',
             'À + le = au (contraction). On dit « au café », pas « à le café ».'),
            ('Comment inviter un ami au cinéma ?',
             ['Je veux aller au cinéma.', 'Tu veux aller au cinéma ?', 'Vous allez au cinéma.', 'Il va au cinéma.'],
             'Tu veux aller au cinéma ?',
             'Pour inviter, on pose la question à l\'autre avec « Tu veux… ? »'),
            ('Quelle est la formule de clôture formelle ?',
             ['Bises,', 'À bientôt,', 'Bisous,', 'Cordialement,'],
             'Cordialement,',
             '« Cordialement » est la clôture standard dans un contexte professionnel ou formel.'),
        ]),
    'ex2': ('Compléter le message', 'Complétez avec le mot manquant.',
        [
            ('___ Élodie,\n(salutation amicale)', 'Salut', 'Pour un message à une amie, on commence par « Salut » ou « Coucou ».'),
            ('On se retrouve ___ café à 17 h.', 'au', 'À + le café → au café. Contraction obligatoire.'),
            ('___ veux venir à ma fête ?', 'Tu', 'Pour inviter : tu veux + infinitif ?'),
            ('Je ne ___ pas venir samedi.', 'peux', 'Pour refuser poliment : je ne peux pas + infinitif.'),
            ('___,\nThomas\n(clôture amicale)', 'À bientôt', '« À bientôt » est une formule de clôture amicale courante.'),
        ]),
    'ex3': ('Identifier l\'erreur', 'Quelle phrase contient une erreur ?',
        [
            ('Quel élément manque dans ce message : « Salut, Je viens à 18 h. Tom » ?',
             ['La salutation', 'Le corps du message', 'La formule de clôture', 'La signature'],
             'La formule de clôture',
             'Il manque une formule de clôture entre le corps et la signature (ex. : À bientôt,).'),
            ('Quel message contient une erreur de registre ?',
             ['Salut Léa, Tu veux venir ? Bises, Emma', 'Bonjour Madame, Je voudrais… Cordialement,', 'Salut Marc, … Cordialement, Paul', 'Coucou, On se retrouve à 18 h ? À bientôt,'],
             'Salut Marc, … Cordialement, Paul',
             '« Salut » (familier) et « Cordialement » (formel) ne vont pas ensemble. Il faut garder le même registre.'),
            ('Trouvez l\'erreur dans cette phrase.',
             ['On se retrouve au café.', 'Je voudrais un café, s\'il vous plaît.', 'On se retrouve à le parc.', 'Tu veux venir à la fête ?'],
             'On se retrouve à le parc.',
             'À + le = au. La contraction est obligatoire : au parc, pas à le parc.'),
        ]),
    'game_desc': 'Maîtrisez les formules pour écrire des messages en français !',
    'items': [
        ('msg-01', 'Salut,', 'Hi, (informal opening)', 'salutation', 'Salut Léa, comment tu vas ?', '___ Léa, comment tu vas ?', 'Salut'),
        ('msg-02', 'Bises,', 'Love / Kisses (closing)', 'clôture', 'À bientôt ! Bises, Emma', 'À bientôt ! ___, Emma', 'Bises'),
        ('msg-03', 'Cordialement,', 'Kind regards (formal)', 'clôture', 'Je reste à votre disposition. Cordialement,', 'Je reste à votre disposition. ___,', 'Cordialement'),
        ('msg-04', 'au café', 'at the café', 'lieu', 'On se retrouve au café à 18 h.', 'On se retrouve ___ café à 18 h.', 'au'),
        ('msg-05', 'tu veux ?', 'do you want? (invite)', 'invitation', 'Tu veux venir au cinéma samedi ?', '___ veux venir au cinéma samedi ?', 'Tu'),
        ('msg-06', 'je ne peux pas', 'I can\'t', 'refus', 'Désolé, je ne peux pas venir vendredi.', 'Désolé, je ne ___ pas venir vendredi.', 'peux'),
        ('msg-07', 'À bientôt,', 'See you soon, (closing)', 'clôture', 'À bientôt, Thomas', '___ bientôt, Thomas', 'À'),
        ('msg-08', 'je voudrais', 'I would like', 'demande', 'Je voudrais réserver une table pour deux.', 'Je ___ réserver une table pour deux.', 'voudrais'),
    ],
},

# ── R04 Remplir un Formulaire ──────────────────────────────────────────────
'remplir-un-formulaire': {
    'level':   'a1',
    'section': 'redaction',
    'num':     'R04',
    'short':   'Remplir un Formulaire',
    'title':   'Remplir un Formulaire — Les Informations Personnelles',
    'subtitle': 'Comprendre et remplir un formulaire simple en français',
    'slides': [
        ('Les champs du formulaire', None,
         '<p>Un formulaire en français demande souvent les informations suivantes :</p>'
         '<table><tr><th>Champ</th><th>Ce qu\'on écrit</th></tr>'
         '<tr><td><b>Nom</b></td><td>votre nom de famille</td></tr>'
         '<tr><td><b>Prénom</b></td><td>votre prénom</td></tr>'
         '<tr><td><b>Date de naissance</b></td><td>JJ/MM/AAAA (ex. : 15/03/1998)</td></tr>'
         '<tr><td><b>Lieu de naissance</b></td><td>la ville où vous êtes né(e)</td></tr>'
         '<tr><td><b>Nationalité</b></td><td>français(e), espagnol(e)…</td></tr>'
         '<tr><td><b>Adresse</b></td><td>numéro + rue + code postal + ville</td></tr>'
         '<tr><td><b>Courriel / E-mail</b></td><td>votre adresse électronique</td></tr>'
         '<tr><td><b>Téléphone</b></td><td>votre numéro de téléphone</td></tr></table>'),
        ('Nom et prénom — attention !', None,
         '<p>En France, dans les formulaires officiels :</p>'
         '<ul><li><b>Nom</b> = nom de famille (family name). Souvent en <b>MAJUSCULES</b>.</li>'
         '<li><b>Prénom</b> = first name. Avec majuscule initiale seulement.</li>'
         '<li>L\'ordre est : Nom DUPONT, Prénom Marie.</li>'
         '<li>C\'est l\'inverse de l\'ordre habituel en anglais !</li></ul>'
         '<p>Sur un formulaire d\'hôtel ou d\'inscription, il est courant de voir :<br>'
         '<b>NOM :</b> MARTIN &nbsp;&nbsp; <b>PRÉNOM :</b> Lucas</p>'),
        ('La date en français', None,
         '<p>La date s\'écrit dans l\'ordre <b>JJ/MM/AAAA</b> (jour / mois / année) :</p>'
         '<ul><li>15/03/1998 = le 15 mars 1998</li>'
         '<li>01/07/2002 = le 1er juillet 2002</li></ul>'
         '<p>Les mois en français :</p>'
         '<p>janvier · février · mars · avril · mai · juin<br>'
         'juillet · août · septembre · octobre · novembre · décembre</p>'
         '<p>Attention : les mois prennent la <b>minuscule</b> en français.</p>'),
        ('L\'adresse postale', None,
         '<p>Format d\'une adresse française :</p>'
         '<blockquote><p>Marie DUPONT<br>'
         '12, rue des Fleurs<br>'
         '75008 Paris<br>'
         'France</p></blockquote>'
         '<p>Composantes :</p>'
         '<ul><li><b>Numéro</b> + type de voie (rue, avenue, boulevard, place…) + nom</li>'
         '<li><b>Code postal</b> (5 chiffres en France) + ville</li>'
         '<li>Le code postal précède toujours le nom de la ville.</li></ul>'),
        ('Vocabulaire du formulaire', None,
         '<p>Autres champs fréquents :</p>'
         '<table><tr><th>Terme</th><th>Signification</th></tr>'
         '<tr><td><b>Sexe / Genre</b></td><td>M (masculin) / F (féminin)</td></tr>'
         '<tr><td><b>Situation de famille</b></td><td>célibataire / marié(e) / divorcé(e)</td></tr>'
         '<tr><td><b>Profession</b></td><td>votre métier</td></tr>'
         '<tr><td><b>Signature</b></td><td>votre signature manuscrite</td></tr>'
         '<tr><td><b>Date et lieu</b></td><td>Fait à Paris, le 15 juin 2026</td></tr>'
         '<tr><td><b>Cocher la case</b></td><td>☑ (tick / check the box)</td></tr></table>'),
    ],
    'traps': [
        ('Nom : Marie / Prénom : Dupont', 'Nom : Dupont / Prénom : Marie', 'Sur un formulaire français, Nom = famille (Dupont), Prénom = premier prénom (Marie).'),
        ('Date : 03/15/1998', 'Date : 15/03/1998', 'En France, l\'ordre est JJ/MM/AAAA, pas MM/DD/YYYY comme en anglais américain.'),
        ('Nationalité : Français', 'Nationalité : français(e)', 'La nationalité prend la minuscule en français, même sur un formulaire.'),
        ('Adresse : Paris 75008', 'Adresse : 75008 Paris', 'Le code postal (5 chiffres) précède le nom de la ville en France.'),
        ('Mois : Janvier', 'Mois : janvier', 'Les noms de mois prennent la minuscule en français.'),
    ],
    'summary': [
        ('Nom / Prénom', 'Nom = famille (MAJUSC.) / Prénom = first name', 'NOM : DUPONT · PRÉNOM : Marie'),
        ('Date', 'JJ/MM/AAAA — mois en minuscule', '15/03/1998 = le 15 mars 1998'),
        ('Adresse', 'numéro + rue + code postal + ville', '12, rue des Fleurs · 75008 Paris'),
        ('Nationalité', 'minuscule, accordé en genre', 'français / française'),
        ('Situation', 'célibataire / marié(e) / divorcé(e)', 'Situation de famille : célibataire'),
        ('Signature', 'Fait à + ville, le + date', 'Fait à Lyon, le 15 juin 2026'),
    ],
    'ex1': ('Comprendre le formulaire', 'Choisissez la réponse correcte.',
        [
            ('Sur un formulaire français, « Nom » signifie :',
             ['votre prénom', 'votre nom de famille', 'votre surnom', 'votre nationalité'],
             'votre nom de famille',
             'En France, Nom = nom de famille, et Prénom = first name. L\'ordre est inverse à l\'usage anglais.'),
            ('Comment s\'écrit la date 3 juillet 2001 sur un formulaire français ?',
             ['07/03/2001', '03/07/2001', '2001/07/03', '3-JUL-2001'],
             '03/07/2001',
             'L\'ordre français est JJ/MM/AAAA : jour d\'abord, puis mois, puis année.'),
            ('Quel est l\'ordre correct d\'une adresse française ?',
             ['Ville + code postal + rue', 'Code postal + ville + rue', 'Rue + code postal + ville', 'Rue + ville'],
             'Rue + code postal + ville',
             'Format : 12, rue des Fleurs / 75008 Paris. La rue est sur la première ligne, code postal + ville sur la deuxième.'),
            ('Comment écrire la nationalité sur un formulaire ?',
             ['Français', 'français', 'FRANÇAIS', 'FR'],
             'français',
             'Les nationalités prennent la minuscule en français, même sur un formulaire officiel.'),
        ]),
    'ex2': ('Remplir les champs', 'Complétez avec le mot manquant.',
        [
            ('___ : MARTIN (votre nom de famille en majuscules)', 'Nom', 'Le champ « Nom » correspond au nom de famille.'),
            ('___ : Thomas (votre premier prénom)', 'Prénom', 'Le champ « Prénom » correspond au first name.'),
            ('Date de naissance : ___/06/2000 (le 8 juin)', '08', 'La date s\'écrit JJ/MM/AAAA. Le jour 8 s\'écrit 08.'),
            ('___ de famille : célibataire', 'Situation', 'Le champ « Situation de famille » indique célibataire, marié(e), etc.'),
            ('Fait à Paris, le 15 ___ 2026', 'juin', 'Les noms de mois s\'écrivent en minuscule en français : juin, pas Juin.'),
        ]),
    'ex3': ('Identifier l\'erreur', 'Quelle réponse contient une erreur ?',
        [
            ('Quel formulaire est correctement rempli ?',
             ['NOM : PETIT · PRÉNOM : Julie', 'Date : 25/12/1995', 'Code postal : 69001 Lyon', 'Nationalité : Espagnol'],
             'Nationalité : Espagnol',
             'Les nationalités prennent la minuscule : espagnol, pas Espagnol.'),
            ('Quelle date est au format français ?',
             ['12/31/1990', '31/12/1990', '1990-31-12', '31.DEC.1990'],
             '31/12/1990',
             'Le format français est JJ/MM/AAAA. Le 31 décembre 1990 s\'écrit 31/12/1990.'),
            ('Quelle adresse est au format français ?',
             ['5, avenue Victor Hugo · 13001 Marseille', 'Marseille 13001 · avenue Victor Hugo 5', '13001 · avenue Victor Hugo · 5', 'avenue Victor Hugo, 5, Marseille'],
             'Marseille 13001 · avenue Victor Hugo 5',
             'Le format correct : numéro + rue sur la première ligne, code postal + ville sur la deuxième. La ville ne vient pas avant le code postal.'),
        ]),
    'game_desc': 'Maîtrisez le vocabulaire des formulaires en français !',
    'items': [
        ('form-01', 'le nom',         'the surname / family name', 'formulaire', 'NOM : DUPONT (nom de famille)',          'NOM : DUPONT (___ de famille)',      'nom'),
        ('form-02', 'le prénom',      'the first name',            'formulaire', 'PRÉNOM : Marie (premier prénom)',        '___ : Marie (premier prénom)',        'Prénom'),
        ('form-03', 'la date JJ/MM/AAAA', 'date DD/MM/YYYY',      'date',       'Date de naissance : 15/03/1998',         'Date de naissance : 15/___ /1998',   '03'),
        ('form-04', 'le code postal', 'the postcode',              'adresse',    '75008 Paris (code postal + ville)',      '___ Paris (code postal + ville)',     '75008'),
        ('form-05', 'célibataire',    'single',                    'situation',  'Situation de famille : célibataire',     'Situation de famille : ___',          'célibataire'),
        ('form-06', 'la signature',   'the signature',             'formulaire', 'Fait à Lyon, le 15 juin 2026 + signature', 'Fait à Lyon, le 15 juin 2026 + ___', 'signature'),
        ('form-07', 'le courriel',    'the email address',         'contact',    'Courriel : marie.dupont@email.fr',       '___ : marie.dupont@email.fr',         'Courriel'),
        ('form-08', 'la nationalité', 'the nationality (lower c.)','identité',   'Nationalité : française (minuscule)',    'Nationalité : française (___)',       'minuscule'),
    ],
},

}
