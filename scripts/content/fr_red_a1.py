# -*- coding: utf-8 -*-
"""fr/ A1 rédaction — short-note, form-filling, personal-profile (3 chapitres)."""

CHAPTERS = {

'short-note': dict(
  level='a1', section='redaction', num='Ch. 1', short='Message court',
  title='Short Note — Écrire un petit message',
  subtitle='Invitations, remerciements, infos pratiques : 25 mots qui font mouche',
  slides=[
    ('Le message court : simple et direct', None,
     '<p class="slide-explanation">Au niveau A1, on écrit des messages de 20 à 30 mots : inviter un ami, remercier, donner une info. La règle d\'or : des <b>phrases courtes</b>, une idée par phrase, et tout ce que le lecteur doit savoir.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Hi Tom!</b></p>'
     '<p style="margin-top:8px">It\'s my birthday on Saturday. Can you come to my party? It starts at 6 pm at my house.</p>'
     '<p style="margin-top:8px"><b>See you soon, Léa</b></p></div>'
     '<p style="margin-top:16px">Trois informations : quoi (party), quand (Saturday, 6 pm), où (my house). Rien de plus, rien de moins.</p>'),
    ('Commencer et finir le message', None,
     '<p class="slide-explanation">Un message commence par une <b>salutation</b> et se termine par une <b>formule de clôture</b> + ton prénom. Voici les classiques du niveau A1.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Pour commencer :</b> Hi Tom! · Hello Anna! · Dear Sam,</p>'
     '<p style="margin-top:8px"><b>Pour finir :</b> See you soon! · Thanks! · Love, · Bye for now,</p></div>'
     '<p style="margin-top:16px">« Dear » n\'est pas réservé aux lettres formelles : Dear Sam est tout à fait normal pour un ami. Mais pas de « Mr » + prénom !</p>'),
    ('Les trois questions du message', None,
     '<p class="slide-explanation">Avant d\'écrire, vérifie que ton message répond aux questions posées par la consigne — en général trois : <b>what? when? where?</b> (quoi, quand, où). À l\'examen, chaque réponse manquante coûte des points.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>What?</b> — a football match, a party, a picnic...</p>'
     '<p style="margin-top:8px"><b>When?</b> — on Saturday, at 4 o\'clock, tomorrow...</p>'
     '<p style="margin-top:8px"><b>Where?</b> — at my house, in the park, at school...</p></div>'
     '<p style="margin-top:16px">Astuce : souligne les questions dans la consigne et coche-les une à une après avoir écrit.</p>'),
    ('Inviter, remercier, proposer', None,
     '<p class="slide-explanation">Trois intentions, trois structures toutes prêtes à réutiliser.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Inviter :</b> Can you come to...? / Do you want to come to...?</p>'
     '<p style="margin-top:8px"><b>Remercier :</b> Thank you for... (+ nom ou -ing) — Thank you for the present!</p>'
     '<p style="margin-top:8px"><b>Proposer :</b> Let\'s meet at 5. / See you at the park!</p></div>'
     '<p style="margin-top:16px">Piège : « merci pour » + verbe → thank you for + -ing : Thank you for invitING me (jamais « for invite me »).</p>'),
    ('Les pièges du francophone dans les messages', None,
     '<p class="slide-explanation">Quelques automatismes français à désactiver quand tu écris un message en anglais.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>« Rendez-vous à 6 h » → <b>See you at 6.</b> (pas de « rendez-vous » !)</p>'
     '<p style="margin-top:8px">« Je t\'invite à ma fête » → <b>Can you come to my party?</b></p>'
     '<p style="margin-top:8px">« Réponds-moi vite » → <b>Write back soon!</b></p></div>'
     '<p style="margin-top:16px">Et n\'oublie pas la majuscule aux jours : <b>Saturday</b>, <b>Monday</b> — toujours, même au milieu d\'une phrase.</p>'),
  ],
  traps=[
    ('Thank you for invite me.', 'Thank you for <strong>inviting</strong> me.', 'Après thank you for, le verbe prend -ing : for invitING me.'),
    ('Rendez-vous at 6 pm.', '<strong>See you at</strong> 6 pm.', '« Rendez-vous » ne se dit pas en anglais courant : on écrit See you at 6 / Let\'s meet at 6.'),
    ('Can you come saturday?', 'Can you come <strong>on Saturday</strong>?', 'Deux corrections : majuscule au jour (Saturday) et préposition on devant le jour.'),
    ('I invite you at my party.', 'Can you come <strong>to</strong> my party?', 'On invite avec come TO : come to my party. Et la tournure question est plus naturelle qu\'« I invite you ».'),
    ('Mr Tom, can you come?', '<strong>Hi Tom!</strong> Can you come?', 'Jamais Mr + prénom. Pour un ami : Hi Tom! ou Dear Tom,.'),
  ],
  summary=[
    ('Structure', 'salutation + message + clôture + prénom', 'Hi Tom! ... See you soon, Léa'),
    ('Salutations', 'Hi... ! · Hello... ! · Dear... ,', 'Hi Anna!'),
    ('Clôtures', 'See you soon! · Thanks! · Love,', 'Bye for now, Sam'),
    ('Les 3 questions', 'what? when? where?', 'party · Saturday 6 pm · my house'),
    ('Inviter', 'Can you come to...?', 'Can you come to my party?'),
    ('Remercier', 'Thank you for + nom / -ing', 'Thank you for inviting me!'),
  ],
  ex1=('Choisis la bonne formule', 'Salutations, clôtures et invitations.', [
    ('Pour commencer un message à ton ami Tom :', ['Hi Tom!', 'Mr Tom,', 'Dear Mr Tom sir,'], 'Hi Tom!',
     'Pour un ami : Hi Tom! — jamais Mr + prénom.'),
    ('Pour inviter : « Peux-tu venir à ma fête ? »', ['Can you come to my party?', 'Can you come at my party?', 'You come my party?'], 'Can you come to my party?',
     'Come TO my party : la destination prend to.'),
    ('Pour finir un message à un ami :', ['See you soon!', 'Yours faithfully,', 'Goodbye forever.'], 'See you soon!',
     'See you soon! est la clôture amicale classique. Yours faithfully est très formel.'),
    ('Pour remercier d\'un cadeau :', ['Thank you for the present!', 'Thank you for present!', 'Thanks the present!'], 'Thank you for the present!',
     'Thank you for + THE present : l\'article est nécessaire.'),
    ('Pour donner l\'heure du rendez-vous :', ['It starts at 6 pm.', 'It starts to 6 pm.', 'Rendez-vous 6 pm.'], 'It starts at 6 pm.',
     'L\'heure prend at : AT 6 pm.'),
    ('Pour demander une réponse :', ['Write back soon!', 'Answer me fast!', 'Respond quickly me!'], 'Write back soon!',
     'La formule naturelle est Write back soon! (réponds-moi vite).'),
  ]),
  ex2=('Complète le message', 'Écris le mot qui manque.', [
    ('Hi Anna! It\'s my birthday ______ Saturday. (préposition)', 'on',
     'Les jours prennent on : ON Saturday.'),
    ('The party starts ______ 5 o\'clock. (préposition)', 'at',
     'Les heures prennent at : AT 5 o\'clock.'),
    ('Can you ______ to my house? (venir)', 'come',
     'L\'invitation : Can you COME to...?'),
    ('Thank you for ______ me to your party! (inviter, avec -ing)', 'inviting',
     'Thank you for + -ing : for INVITING me.'),
    ('See ______ soon! (formule de clôture)', 'you',
     'SEE YOU soon! — la clôture amicale la plus courante.'),
  ]),
  ex3=('Le message complet', 'Choisis la meilleure version.', [
    ('Quelle invitation contient quoi + quand + où ?', ['Party at my house on Saturday at 6! Can you come?', 'I have a party. It is great. I like parties.', 'Can you come? It will be fun! See you!'], 'Party at my house on Saturday at 6! Can you come?',
     'Les trois infos y sont : quoi (party), où (my house), quand (Saturday, 6). Les autres versions oublient des informations.'),
    ('Quel remerciement est correct ?', ['Thank you for the lovely present!', 'Thank you for buy me a present!', 'Merci for the present!'], 'Thank you for the lovely present!',
     'Thank you for + nom. « For buy » est faux (il faudrait for buying) et pas de mélange français-anglais.'),
    ('Quelle clôture pour un message à un ami ?', ['Bye for now, Léa', 'Yours sincerely, Ms Léa Dupont', 'The end. Léa'], 'Bye for now, Léa',
     'Registre amical : Bye for now + prénom. Yours sincerely est pour les lettres formelles.'),
    ('Comment proposer un rendez-vous ?', ['Let\'s meet at the park at 4.', 'Rendez-vous at the park 4 hours.', 'We have rendez-vous at park.'], 'Let\'s meet at the park at 4.',
     'Let\'s meet + lieu + heure. « Rendez-vous » n\'existe pas dans ce sens en anglais courant.'),
    ('Quel message refuse poliment ?', ['Sorry, I can\'t come. Thank you for inviting me!', 'No.', 'I don\'t want to come to your boring party.'], 'Sorry, I can\'t come. Thank you for inviting me!',
     'On s\'excuse (sorry, I can\'t) et on remercie quand même : c\'est la politesse anglaise attendue.'),
  ]),
  game_desc='Chaque formule de message passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('hi', 'Hi Tom!', 'salut + prénom — la salutation amicale', 'salutation', '<b>Hi Tom!</b> It\'s my birthday on Saturday.', '______ Tom! It\'s my birthday on Saturday. (salut)', 'hi'),
    ('can-you-come', 'Can you come to...?', 'peux-tu venir à... ? — la formule d\'invitation', 'invitation', '<b>Can you come to</b> my party?', 'Can you ______ to my party? (venir)', 'come'),
    ('on-saturday', 'on Saturday', 'samedi — on + jour, avec majuscule', 'le jour', 'The party is <b>on Saturday</b>.', 'The party is ______ Saturday. (préposition)', 'on'),
    ('at-6', 'at 6 pm', 'à 18 h — at + heure', 'l\'heure', 'It starts <b>at</b> 6 pm.', 'It starts ______ 6 pm. (à)', 'at'),
    ('thank-you-for', 'Thank you for + -ing', 'merci de... — le verbe prend -ing', 'remerciement', '<b>Thank you for inviting</b> me!', 'Thank you for ______ me! (inviter)', 'inviting'),
    ('see-you', 'See you soon!', 'à bientôt — la clôture amicale', 'clôture', '<b>See you soon!</b> Léa', '______ you soon! Léa (à bientôt)', 'see'),
    ('lets-meet', 'Let\'s meet at...', 'retrouvons-nous à... — proposer un rendez-vous', 'rendez-vous', '<b>Let\'s meet</b> at the park at 4.', 'Let\'s ______ at the park at 4. (se retrouver)', 'meet'),
    ('write-back', 'Write back soon!', 'réponds-moi vite — demander une réponse', 'réponse', '<b>Write back</b> soon!', 'Write ______ soon! (réponds)', 'back'),
  ],
),

'form-filling': dict(
  level='a1', section='redaction', num='Ch. 2', short='Le formulaire',
  title='Form Filling — Remplir un formulaire',
  subtitle='Surname, date of birth, nationality : décoder les champs sans se tromper',
  slides=[
    ('Le vocabulaire du formulaire', None,
     '<p class="slide-explanation">Les formulaires anglais utilisent des mots précis qu\'il faut reconnaître au premier coup d\'œil. Le piège principal : <b>surname</b> ne veut pas dire « surnom » !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>First name</b> = prénom &nbsp;·&nbsp; <b>Surname / Last name</b> = nom de famille</p>'
     '<p style="margin-top:8px"><b>Date of birth (DOB)</b> = date de naissance &nbsp;·&nbsp; <b>Age</b> = âge</p>'
     '<p style="margin-top:8px"><b>Address</b> = adresse &nbsp;·&nbsp; <b>Postcode</b> = code postal</p></div>'
     '<p style="margin-top:16px"><b>Surname</b> est un faux ami : c\'est le nom de famille (Dupont), pas un surnom. « Surnom » se dit nickname.</p>'),
    ('Nationality : avec une majuscule', None,
     '<p class="slide-explanation">Le champ <b>nationality</b> attend un adjectif de nationalité — toujours avec une <b>majuscule</b> en anglais.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Nationality: <b>French</b> &nbsp;·&nbsp; Country: <b>France</b></p>'
     '<p style="margin-top:8px">Languages: <b>French, English</b></p>'
     '<p style="margin-top:8px;color:var(--muted)">(jamais « french » en minuscule — c\'est une faute comptée à l\'examen)</p></div>'
     '<p style="margin-top:16px">Distingue bien : <b>country</b> = le pays (France), <b>nationality</b> = l\'adjectif (French).</p>'),
    ('La date à l\'anglaise', None,
     '<p class="slide-explanation">Les dates britanniques s\'écrivent <b>jour/mois/année</b> comme en France — mais on les dit et écrit souvent avec le mois en toutes lettres. Attention aussi aux mois avec majuscule !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Date of birth: <b>12 March 2014</b> ou <b>12/03/2014</b></p>'
     '<p style="margin-top:8px">Les mois prennent une majuscule : <b>January, February, March...</b></p></div>'
     '<p style="margin-top:16px">Piège américain : aux États-Unis, 03/12/2014 = 12 mars. Sur un formulaire britannique, écris le mois en lettres pour éviter toute confusion.</p>'),
    ('Écrire en capitales : BLOCK CAPITALS', None,
     '<p class="slide-explanation">Beaucoup de formulaires demandent d\'écrire en <b>BLOCK CAPITALS</b> (lettres majuscules). Et la consigne <b>please tick</b> signifie « cochez ».</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Please write in BLOCK CAPITALS: <b>DUPONT</b></p>'
     '<p style="margin-top:8px">Please tick: Male ☐ Female ☐ — cochez la case</p>'
     '<p style="margin-top:8px"><b>Signature</b> = signature · <b>Date</b> = date du jour (pas ta naissance !)</p></div>'
     '<p style="margin-top:16px">Lis chaque champ deux fois : le champ « Date » en bas d\'un formulaire = la date d\'aujourd\'hui, pas ta date de naissance.</p>'),
    ('Les réponses courtes : pas de phrases !', None,
     '<p class="slide-explanation">Dans un formulaire, on répond par des <b>mots ou groupes de mots</b>, jamais par des phrases complètes. C\'est l\'inverse de la rédaction !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Occupation: <b>student</b> (et non « I am a student »)</p>'
     '<p style="margin-top:8px">Hobbies: <b>football, music, reading</b></p>'
     '<p style="margin-top:8px">Reason for visit: <b>holiday</b></p></div>'
     '<p style="margin-top:16px">Économie de mots : le formulaire veut des données, pas du style. Garde tes phrases pour le personal profile (chapitre 3) !</p>'),
  ],
  traps=[
    ('Surname: Léo (mon surnom)', 'Surname: <strong>DUPONT</strong> (nom de famille)', 'Surname = nom de famille, pas surnom ! « Surnom » se dit nickname en anglais.'),
    ('Nationality: france', 'Nationality: <strong>French</strong>', 'Deux fautes : nationality attend l\'adjectif (French, pas France) et il prend une majuscule.'),
    ('Date of birth: 2014', 'Date of birth: <strong>12 March 2014</strong>', 'DOB = la date complète (jour, mois, année), pas seulement l\'année.'),
    ('Occupation: I am a student.', 'Occupation: <strong>student</strong>', 'Dans un formulaire, on écrit des mots, pas des phrases : student suffit.'),
    ('Date: 12 March 2014 (en bas du formulaire)', 'Date: <strong>la date d\'aujourd\'hui</strong>', 'Le champ Date en bas d\'un formulaire = la date du jour de signature, pas ta date de naissance.'),
  ],
  summary=[
    ('Identité', 'first name = prénom · surname = nom', 'First name: Léa · Surname: DUPONT'),
    ('Naissance', 'date of birth (DOB) = jour + mois + année', '12 March 2014'),
    ('Nationalité', 'adjectif avec majuscule', 'Nationality: French'),
    ('Pays', 'country = le nom du pays', 'Country: France'),
    ('Consignes', 'BLOCK CAPITALS = majuscules · tick = cocher', 'DUPONT · Male ☑'),
    ('Style', 'des mots, pas des phrases', 'Occupation: student'),
  ],
  ex1=('Décode le formulaire', 'Que faut-il écrire dans chaque champ ?', [
    ('Champ « Surname » — tu t\'appelles Léa Dupont :', ['Dupont', 'Léa', 'Lulu (mon surnom)'], 'Dupont',
     'Surname = nom de famille : Dupont. Faux ami — pas le surnom !'),
    ('Champ « First name » — tu t\'appelles Léa Dupont :', ['Léa', 'Dupont', 'Mademoiselle'], 'Léa',
     'First name = prénom : Léa.'),
    ('Champ « Nationality » — tu es française :', ['French', 'France', 'french'], 'French',
     'Nationality = adjectif avec majuscule : French.'),
    ('Champ « Country » :', ['France', 'French', 'Frenchland'], 'France',
     'Country = le nom du pays : France.'),
    ('Champ « Occupation » — tu es étudiant :', ['student', 'I am a student.', 'Yes'], 'student',
     'Un mot suffit : student. Pas de phrase dans un formulaire.'),
    ('Consigne « Please write in BLOCK CAPITALS » :', ['DUPONT', 'dupont', 'Dupont'], 'DUPONT',
     'BLOCK CAPITALS = tout en majuscules : DUPONT.'),
  ]),
  ex2=('Le vocabulaire du formulaire', 'Écris le mot anglais demandé.', [
    ('« nom de famille » (un mot, commence par s) → ______', 'surname',
     'SURNAME = nom de famille. À ne pas confondre avec nickname (surnom).'),
    ('« date de naissance » (trois mots) → date ______ ______', 'of birth',
     'Date OF BIRTH, souvent abrégé DOB.'),
    ('« cocher » (la consigne « please... », un mot) → ______', 'tick',
     'Please TICK = cochez la case.'),
    ('« code postal » (un mot) → ______', 'postcode',
     'POSTCODE = code postal (anglais britannique).'),
    ('« prénom » (deux mots) → ______ name', 'first',
     'FIRST name = prénom. Last name / surname = nom de famille.'),
  ]),
  ex3=('Remplis sans te tromper', 'Choisis la bonne réponse pour chaque champ.', [
    ('« Date of birth » pour quelqu\'un né le 5 mai 2013 :', ['5 May 2013', 'May 2013', '2013, the 5 of may'], '5 May 2013',
     'Jour + Mois (majuscule) + année : 5 May 2013.'),
    ('« Languages » — tu parles français et un peu anglais :', ['French, English', 'france, england', 'I speak French and a little English.'], 'French, English',
     'Liste de mots avec majuscules — pas de phrase complète.'),
    ('« Address » :', ['12 rue des Lilas, 69003 Lyon, France', 'I live in Lyon.', 'lyon'], '12 rue des Lilas, 69003 Lyon, France',
     'L\'adresse complète, en données — pas une phrase.'),
    ('« Hobbies » :', ['football, music', 'I like football very much and also music.', 'yes'], 'football, music',
     'Des mots-clés séparés par des virgules.'),
    ('Le champ « Signature » :', ['ta signature manuscrite', 'ton nom en majuscules', 'ta date de naissance'], 'ta signature manuscrite',
     'Signature = la signature, différente du nom en capitales demandé ailleurs.'),
  ]),
  game_desc='Chaque champ de formulaire passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('surname', 'surname', 'nom de famille — FAUX AMI, pas « surnom »', 'last name', 'Write your <b>surname</b> in BLOCK CAPITALS.', 'Write your ______ in BLOCK CAPITALS. (nom de famille)', 'surname'),
    ('first-name', 'first name', 'prénom — la première partie du nom', 'prénom', 'Her <b>first name</b> is Léa.', 'Her ______ name is Léa. (prénom)', 'first'),
    ('dob', 'date of birth', 'date de naissance — jour, mois, année', 'DOB', 'My <b>date of birth</b> is 12 March 2014.', 'My date of ______ is 12 March 2014. (naissance)', 'birth'),
    ('nationality', 'nationality: French', 'nationalité — adjectif avec majuscule', 'adjectif', 'Nationality: <b>French</b>.', 'Nationality: ______. (français, avec majuscule)', 'french'),
    ('postcode', 'postcode', 'code postal — dans l\'adresse britannique', 'code postal', 'The <b>postcode</b> is 69003.', 'The ______ is 69003. (code postal)', 'postcode'),
    ('tick', 'please tick', 'cochez — la consigne des cases', 'cocher', '<b>Please tick</b>: Male or Female.', 'Please ______: Male or Female. (cochez)', 'tick'),
    ('block-capitals', 'BLOCK CAPITALS', 'en majuscules — la consigne d\'écriture', 'majuscules', 'Write in <b>BLOCK CAPITALS</b>: DUPONT.', 'Write in BLOCK ______: DUPONT. (majuscules)', 'capitals'),
    ('occupation', 'occupation: student', 'profession — un mot, pas une phrase', 'métier', 'Occupation: <b>student</b>.', 'Occupation: ______. (étudiant, un mot)', 'student'),
  ],
),

'personal-profile': dict(
  level='a1', section='redaction', num='Ch. 3', short='Se présenter',
  title='Personal Profile — Se présenter par écrit',
  subtitle='Nom, âge, famille, goûts : ton premier paragraphe en anglais',
  slides=[
    ('Le plan du personal profile', None,
     '<p class="slide-explanation">Se présenter par écrit suit toujours le même plan en quatre temps : <b>identité → famille/ville → goûts → routine</b>. Avec une phrase par élément, tu obtiens un paragraphe parfait de niveau A1.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>My name is Léa and I am twelve years old. I live in Lyon with my parents and my brother. I love music and I play tennis every Saturday. On Sundays, I visit my grandparents.</p></div>'
     '<p style="margin-top:16px">Quatre phrases, quatre informations — c\'est exactement ce qu\'attend un correcteur A1.</p>'),
    ('L\'identité : name et age', None,
     '<p class="slide-explanation">Les deux premières phrases de toute présentation. Attention au piège de l\'âge : en anglais, on <b>est</b> son âge, on ne l\'« a » pas !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>My name is</b> Léa. / <b>I\'m</b> Léa.</p>'
     '<p style="margin-top:8px"><b>I am twelve (years old).</b> — J\'ai douze ans.</p>'
     '<p style="margin-top:8px;color:var(--muted)">(jamais « I have twelve years » — c\'est LA faute de francophone)</p></div>'
     '<p style="margin-top:16px">On peut écrire I am twelve ou I am twelve years old — mais jamais « I have twelve years ».</p>'),
    ('Famille et ville : live with, have got', None,
     '<p class="slide-explanation">Pour la famille et le lieu, deux structures suffisent : <b>I live in</b> + ville et <b>I have got</b> (ou I have) + famille.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I live in</b> Lyon, <b>in</b> France. — J\'habite à Lyon, en France.</p>'
     '<p style="margin-top:8px"><b>I have got</b> one brother and two sisters. — J\'ai un frère et deux sœurs.</p>'
     '<p style="margin-top:8px"><b>I live with</b> my parents. — J\'habite avec mes parents.</p></div>'
     '<p style="margin-top:16px">Rappel du chapitre 24 : les villes prennent IN — I live in Lyon (jamais « at Lyon »).</p>'),
    ('Les goûts : like + -ing', None,
     '<p class="slide-explanation">Pour parler de ce que tu aimes : <b>like / love / don\'t like</b> + nom ou + verbe en <b>-ing</b>. Le -ing après like est le réflexe à installer dès maintenant.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>love music</b> and I <b>like reading</b>. — J\'adore la musique et j\'aime lire.</p>'
     '<p style="margin-top:8px">I <b>like playing</b> football. — J\'aime jouer au foot.</p>'
     '<p style="margin-top:8px">I <b>don\'t like getting</b> up early. — Je n\'aime pas me lever tôt.</p></div>'
     '<p style="margin-top:16px">Mes favoris : <b>My favourite subject is</b> English. / <b>My favourite colour is</b> blue. (favourite avec u en anglais britannique !)</p>'),
    ('La routine : present simple + fréquence', None,
     '<p class="slide-explanation">Termine ta présentation avec une ou deux habitudes — c\'est l\'occasion de replacer le present simple et les adverbes de fréquence des chapitres 12 et 17.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>play</b> tennis <b>every Saturday</b>. — Je joue au tennis tous les samedis.</p>'
     '<p style="margin-top:8px">I <b>usually do</b> my homework after school. — Je fais d\'habitude mes devoirs après l\'école.</p>'
     '<p style="margin-top:8px">My sister <b>often watches</b> TV in the evening. — Ma sœur regarde souvent la télé le soir.</p></div>'
     '<p style="margin-top:16px">N\'oublie pas le -s de la troisième personne quand tu présentes ta famille : my brother playS, my mother workS.</p>'),
  ],
  traps=[
    ('I have twelve years.', 'I <strong>am twelve</strong> (years old).', 'L\'âge se dit avec be : I AM twelve. « I have twelve years » est le calque français classique.'),
    ('I like play football.', 'I like <strong>playing</strong> football.', 'Après like, le verbe prend -ing : I like playING.'),
    ('I live at Lyon.', 'I live <strong>in</strong> Lyon.', 'Les villes prennent in : I live IN Lyon.'),
    ('My brother play tennis.', 'My brother <strong>plays</strong> tennis.', 'Troisième personne → -s : my brother playS. Ne l\'oublie pas en présentant ta famille !'),
    ('I am agree with my parents.', 'I <strong>agree</strong> with my parents.', 'Agree est un verbe : I agree (sans am). « Je suis d\'accord » ne se traduit pas mot à mot.'),
  ],
  summary=[
    ('Plan', 'identité → famille/ville → goûts → routine', '4 phrases = 1 profil complet'),
    ('Nom', 'My name is... / I\'m...', 'My name is Léa.'),
    ('Âge', 'I am + nombre (years old)', 'I am twelve years old.'),
    ('Ville et famille', 'I live in + ville · I have got + famille', 'I live in Lyon. I have got one brother.'),
    ('Goûts', 'like/love + nom ou + -ing', 'I like playing football.'),
    ('Routine', 'present simple + fréquence', 'I play tennis every Saturday.'),
  ],
  ex1=('Construis ta présentation', 'Choisis la phrase correcte.', [
    ('Dire ton âge :', ['I am twelve years old.', 'I have twelve years.', 'I have twelve years old.'], 'I am twelve years old.',
     'L\'âge avec be : I AM twelve. Jamais avec have.'),
    ('Dire où tu habites :', ['I live in Lyon.', 'I live at Lyon.', 'I live to Lyon.'], 'I live in Lyon.',
     'Ville → IN : I live in Lyon.'),
    ('Parler de ta famille :', ['I have got two sisters.', 'I have got two sister.', 'I am two sisters.'], 'I have got two sisters.',
     'I have got + pluriel : two sisterS.'),
    ('Dire ce que tu aimes faire :', ['I like reading.', 'I like read.', 'I like to reading.'], 'I like reading.',
     'Like + -ing : I like readING.'),
    ('Parler de ta matière préférée :', ['My favourite subject is English.', 'My subject favourite is English.', 'My favourite subject is english.'], 'My favourite subject is English.',
     'Favourite AVANT subject, et English avec majuscule.'),
    ('Présenter ton frère :', ['My brother plays football.', 'My brother play football.', 'My brother playing football.'], 'My brother plays football.',
     'Troisième personne → -s : my brother playS.'),
  ]),
  ex2=('Complète le profil', 'Écris le mot qui manque.', [
    ('My name ______ Léa. (verbe)', 'is',
     'My name IS Léa — troisième personne.'),
    ('I ______ eleven years old. (verbe — pas have !)', 'am',
     'L\'âge avec be : I AM eleven.'),
    ('I live ______ Paris with my family. (préposition)', 'in',
     'Ville → IN Paris.'),
    ('I love ______ to music. (écouter, avec -ing)', 'listening',
     'Love + -ing : I love LISTENING to music.'),
    ('I play basketball ______ Saturday. (chaque)', 'every',
     'La routine : EVERY Saturday — sans préposition devant every.'),
  ]),
  ex3=('Le profil complet', 'Choisis la meilleure version.', [
    ('Quelle première phrase ?', ['My name is Tom and I am ten years old.', 'I am Tom and I have ten years.', 'My name Tom, ten years.'], 'My name is Tom and I am ten years old.',
     'Identité + âge avec be, reliés par and : la phrase d\'ouverture parfaite.'),
    ('Quelle phrase sur la famille ?', ['I live in Nice with my parents and my little sister.', 'I live at Nice with my parents and my sister little.', 'I am living Nice with parents.'], 'I live in Nice with my parents and my little sister.',
     'Live IN + ville, adjectif AVANT le nom (little sister).'),
    ('Quelle phrase sur les goûts ?', ['I love swimming and I like playing video games.', 'I love swim and like play video games.', 'I am loving swimming and playing.'], 'I love swimming and I like playing video games.',
     'Love/like + -ing, et love reste au present simple (jamais « am loving »).'),
    ('Quelle phrase de routine ?', ['I usually do my homework after school.', 'I do usually my homework after school.', 'Usually I am do my homework.'], 'I usually do my homework after school.',
     'Adverbe de fréquence AVANT le verbe : I USUALLY do.'),
    ('Quelle phrase finale ?', ['In the future, I want to be a doctor.', 'In the future, I want be doctor.', 'In future I am doctor.'], 'In the future, I want to be a doctor.',
     'Want TO be + A doctor : l\'infinitif complet et l\'article devant la profession.'),
  ]),
  game_desc='Chaque élément du profil passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('my-name-is', 'My name is...', 'je m\'appelle... — la phrase d\'ouverture', 'identité', '<b>My name is</b> Léa.', 'My ______ is Léa. (nom)', 'name'),
    ('i-am-twelve', 'I am twelve', 'j\'ai douze ans — l\'âge avec BE, jamais have', 'l\'âge', '<b>I am</b> twelve years old.', 'I ______ twelve years old. (verbe)', 'am'),
    ('i-live-in', 'I live in + ville', 'j\'habite à — in devant les villes', 'la ville', 'I <b>live in</b> Lyon.', 'I live ______ Lyon. (préposition)', 'in'),
    ('have-got', 'I have got + famille', 'j\'ai un frère / une sœur — la possession', 'la famille', 'I <b>have got</b> one brother.', 'I have ______ one brother. (possession)', 'got'),
    ('like-ing', 'I like + -ing', 'j\'aime faire — le verbe prend -ing', 'les goûts', 'I like <b>playing</b> football.', 'I like ______ football. (jouer)', 'playing'),
    ('favourite', 'my favourite...', 'mon/ma préféré(e) — avec u britannique', 'préférence', 'My <b>favourite</b> subject is English.', 'My ______ subject is English. (préféré)', 'favourite'),
    ('every-saturday', 'every Saturday', 'tous les samedis — la routine', 'routine', 'I play tennis <b>every</b> Saturday.', 'I play tennis ______ Saturday. (tous les)', 'every'),
    ('third-person', 'my brother plays', 'le -s de la 3e personne — en présentant la famille', '3e personne', 'My brother <b>plays</b> tennis.', 'My brother ______ tennis. (joue)', 'plays'),
  ],
),

}
