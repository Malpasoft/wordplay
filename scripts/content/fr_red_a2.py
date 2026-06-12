# -*- coding: utf-8 -*-
"""fr/ A2 rédaction — informal-email, description, postcard (3 chapitres)."""

CHAPTERS = {

'informal-email': dict(
  level='a2', section='redaction', num='Ch. 1', short='Email informel',
  title='Informal Email — Écrire à un ami',
  subtitle='Hi, contractions, questions au lecteur : le ton juste de l\'email amical',
  slides=[
    ('L\'email informel : la structure', None,
     '<p class="slide-explanation">L\'email à un ami suit un plan fixe : <b>salutation → accroche → nouvelles/réponses → questions → clôture</b>. Au niveau A2, on vise 60 à 80 mots bien organisés.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Hi Sam!</b></p>'
     '<p style="margin-top:8px">Thanks for your email! Great news about your new dog!</p>'
     '<p style="margin-top:8px">Last weekend I went to the mountains with my family. We walked a lot and I took some amazing photos. What about you? What did you do?</p>'
     '<p style="margin-top:8px"><b>Write back soon, Léa</b></p></div>'),
    ('Commencer : accuser réception et réagir', None,
     '<p class="slide-explanation">Un email amical répond presque toujours à un autre email. La première ligne <b>remercie</b> et <b>réagit</b> aux nouvelles de l\'ami — c\'est ce qui rend l\'email naturel.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Thanks for your email!</b> — Merci pour ton email !</p>'
     '<p style="margin-top:8px"><b>It was great to hear from you!</b> — Ça m\'a fait plaisir d\'avoir de tes nouvelles !</p>'
     '<p style="margin-top:8px"><b>Great news about your exam!</b> — Super nouvelle pour ton examen !</p></div>'
     '<p style="margin-top:16px">Ne commence jamais par « I write to you because... » — c\'est un calque du français qui sonne très scolaire.</p>'),
    ('Le ton informel : contractions et exclamations', None,
     '<p class="slide-explanation">L\'email amical utilise les <b>contractions</b> (I\'m, don\'t, can\'t), des <b>exclamations</b> et des mots simples. C\'est l\'inverse de la lettre formelle française !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I\'m</b> so happy! &nbsp;·&nbsp; It <b>was</b> amazing! &nbsp;·&nbsp; You <b>can\'t</b> imagine!</p>'
     '<p style="margin-top:8px"><b>Guess what?</b> — Devine quoi ? (pour annoncer une nouvelle)</p>'
     '<p style="margin-top:8px"><b>By the way...</b> — Au fait... (pour changer de sujet)</p></div>'
     '<p style="margin-top:16px">Évite les formules trop solennelles : pas de « I would like to inform you » entre amis !</p>'),
    ('Poser des questions à ton ami', None,
     '<p class="slide-explanation">Un bon email amical se termine par des <b>questions</b> : elles montrent ton intérêt et appellent la réponse. La consigne d\'examen en demande souvent explicitement.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>What about you?</b> — Et toi ?</p>'
     '<p style="margin-top:8px"><b>What did you do at the weekend?</b> — Qu\'as-tu fait ce week-end ?</p>'
     '<p style="margin-top:8px"><b>Can you come to my party?</b> — Tu peux venir à ma fête ?</p></div>'
     '<p style="margin-top:16px">Vérifie l\'ordre des mots interrogatifs (chapitre A1) : What DID you do? — l\'auxiliaire reste obligatoire, même entre amis.</p>'),
    ('Finir l\'email', None,
     '<p class="slide-explanation">La clôture amicale tient en deux lignes : une formule + ton prénom. Choisis selon le degré de proximité.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Write back soon!</b> — Réponds vite !</p>'
     '<p style="margin-top:8px"><b>See you soon! / Take care!</b> — À bientôt ! / Prends soin de toi !</p>'
     '<p style="margin-top:8px"><b>Love, Léa</b> — Bisous, Léa (entre amis proches ou famille)</p></div>'
     '<p style="margin-top:16px">« Love, » à la fin d\'un email n\'est pas une déclaration d\'amour — c\'est l\'équivalent de « bisous » entre proches.</p>'),
  ],
  traps=[
    ('I write to you because I want to tell you my holidays.', '<strong>Thanks for your email!</strong> Guess what? I went to Spain!', 'Pas d\'annonce solennelle : l\'email amical remercie, réagit et raconte directement.'),
    ('Dear Sir, can you come to my party?', '<strong>Hi Tom!</strong> Can you come to my party?', 'Dear Sir est réservé aux lettres formelles à un inconnu. Pour un ami : Hi + prénom.'),
    ('I am very happy because of to see you soon.', 'I\'m very happy <strong>to see</strong> you soon.', 'Happy + to + infinitif : happy TO SEE you. « Because of to » n\'existe pas.'),
    ('What you did at the weekend?', 'What <strong>did you do</strong> at the weekend?', 'La question garde son auxiliaire même dans un email informel : What DID you DO?'),
    ('Best regards, your friend Léa', '<strong>Write back soon! Léa</strong>', 'Best regards est une clôture professionnelle. Entre amis : Write back soon! / See you! / Love,'),
  ],
  summary=[
    ('Plan', 'salutation → réaction → nouvelles → questions → clôture', 'Hi Sam! ... Write back soon!'),
    ('Ouverture', 'Thanks for your email! · Great news!', 'It was great to hear from you!'),
    ('Ton', 'contractions + exclamations', 'I\'m so happy! Guess what?'),
    ('Changer de sujet', 'By the way...', 'By the way, how is your sister?'),
    ('Questions', 'What about you? · What did you do?', '2 questions avant de finir'),
    ('Clôture', 'Write back soon! · Take care! · Love,', 'Love, Léa'),
  ],
  ex1=('Le bon ton informel', 'Choisis la formule adaptée à un email entre amis.', [
    ('Pour commencer un email à ta copine Emma :', ['Hi Emma!', 'Dear Madam,', 'To Emma Smith,'], 'Hi Emma!',
     'Entre amis : Hi + prénom. Dear Madam est formel.'),
    ('Pour remercier de son email :', ['Thanks for your email!', 'I acknowledge receipt of your email.', 'Your email is arrived.'], 'Thanks for your email!',
     'La formule amicale standard : Thanks for your email!'),
    ('Pour annoncer une grande nouvelle :', ['Guess what? I won the competition!', 'I am writing to inform you that I won.', 'It is to be noted that I won.'], 'Guess what? I won the competition!',
     'Guess what? est l\'accroche informelle parfaite pour une nouvelle.'),
    ('Pour changer de sujet :', ['By the way, how is your brother?', 'Furthermore, regarding your brother...', 'In addition, your brother.'], 'By the way, how is your brother?',
     'By the way = au fait. Furthermore est trop formel pour un email amical.'),
    ('Pour demander de ses nouvelles :', ['What about you?', 'And about yourself, what?', 'What is your situation?'], 'What about you?',
     'What about you? = et toi ? — la relance amicale classique.'),
    ('Pour finir :', ['Write back soon!', 'Yours faithfully,', 'With my best considerations,'], 'Write back soon!',
     'Clôture amicale : Write back soon! Les autres sont des formules de lettre formelle.'),
  ]),
  ex2=('Complète l\'email', 'Écris le mot qui manque.', [
    ('Thanks ______ your email! (préposition)', 'for',
     'Thanks FOR your email — for introduit la raison du remerciement.'),
    ('It was great to hear ______ you! (préposition)', 'from',
     'Hear FROM somebody = avoir des nouvelles de quelqu\'un.'),
    ('______ what? I have a new bike! (devine)', 'Guess',
     'GUESS what? = devine quoi ?'),
    ('What ______ you do last weekend? (auxiliaire du passé)', 'did',
     'Question au past simple : What DID you do?'),
    ('Write ______ soon! (formule de clôture)', 'back',
     'Write BACK soon! = réponds-moi vite.'),
  ]),
  ex3=('L\'email réussi', 'Choisis la meilleure version.', [
    ('La meilleure première ligne après « Hi Leo! » :', ['Thanks for your email — great news about your team!', 'I write this email to answer your email.', 'Hello, here is my email.'], 'Thanks for your email — great news about your team!',
     'On remercie ET on réagit aux nouvelles : c\'est l\'ouverture naturelle.'),
    ('Raconter son week-end :', ['Last Saturday I went to the beach with my cousins.', 'The last saturday I have gone at the beach.', 'Last Saturday I go to beach.'], 'Last Saturday I went to the beach with my cousins.',
     'Past simple (went), majuscule à Saturday, the beach avec article.'),
    ('Inviter son ami :', ['Why don\'t you come to my house next Saturday?', 'You will come at my house the next saturday?', 'Come you to my house?'], 'Why don\'t you come to my house next Saturday?',
     'Why don\'t you...? est l\'invitation amicale type. Next Saturday sans article.'),
    ('Poser une question avant de finir :', ['What about you? Did you have a good weekend?', 'And you, the weekend, it was how?', 'How was about your weekend you?'], 'What about you? Did you have a good weekend?',
     'What about you? + question complète avec did : l\'enchaînement naturel.'),
    ('La clôture complète :', ['Write back soon! Love, Léa', 'Goodbye madam. Léa Dupont (Ms)', 'End of my email. Léa'], 'Write back soon! Love, Léa',
     'Formule amicale + prénom : Write back soon! Love, Léa.'),
  ]),
  game_desc='Chaque formule d\'email passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('thanks-for', 'Thanks for your email!', 'merci pour ton email — l\'ouverture standard', 'ouverture', '<b>Thanks for</b> your email!', 'Thanks ______ your email! (préposition)', 'for'),
    ('hear-from', 'to hear from you', 'avoir de tes nouvelles — hear + from', 'nouvelles', 'It was great to <b>hear from</b> you!', 'It was great to hear ______ you! (préposition)', 'from'),
    ('guess-what', 'Guess what?', 'devine quoi ? — annoncer une nouvelle', 'accroche', '<b>Guess what?</b> I have a new bike!', '______ what? I have a new bike! (devine)', 'guess'),
    ('by-the-way', 'by the way', 'au fait — changer de sujet en douceur', 'transition', '<b>By the way</b>, how is your sister?', 'By the ______, how is your sister? (au fait)', 'way'),
    ('what-about-you', 'What about you?', 'et toi ? — relancer son correspondant', 'relance', '<b>What about</b> you?', 'What ______ you? (et toi)', 'about'),
    ('why-dont-you', 'Why don\'t you...?', 'pourquoi ne... pas ? — l\'invitation amicale', 'invitation', '<b>Why don\'t you</b> come to my house?', 'Why ______ you come to my house? (négation)', 'don\'t'),
    ('write-back', 'Write back soon!', 'réponds vite — la clôture qui appelle une réponse', 'clôture', '<b>Write back</b> soon! Léa', 'Write ______ soon! Léa (réponds)', 'back'),
    ('love', 'Love, + prénom', 'bisous — la signature entre proches', 'signature', '<b>Love</b>, Léa', '______, Léa (bisous)', 'love'),
  ],
),

'description': dict(
  level='a2', section='redaction', num='Ch. 2', short='La description',
  title='Description — Décrire une personne ou un lieu',
  subtitle='Adjectifs bien placés, have got, there is : le portrait et le décor',
  slides=[
    ('Décrire une personne : le plan', None,
     '<p class="slide-explanation">Le portrait A2 suit un ordre logique : <b>identité → physique → caractère → goûts</b>. Une ou deux phrases par bloc suffisent.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>My best friend is called Marco. He is tall and he has got short black hair and brown eyes. He is very funny and friendly. He loves basketball and video games.</p></div>'
     '<p style="margin-top:16px">Remarque les outils : <b>is called</b> (s\'appelle), <b>is + adjectif</b> (taille, caractère), <b>has got + nom</b> (cheveux, yeux).</p>'),
    ('Le physique : be ou have got ?', None,
     '<p class="slide-explanation">Deux verbes se partagent le physique : <b>be</b> pour la taille et l\'allure générale, <b>have got</b> pour les cheveux et les yeux.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>She <b>is tall / short / slim</b>. — Elle est grande / petite / mince.</p>'
     '<p style="margin-top:8px">She <b>has got long brown hair</b>. — Elle a les cheveux longs et bruns.</p>'
     '<p style="margin-top:8px">He <b>has got blue eyes</b>. — Il a les yeux bleus.</p></div>'
     '<p style="margin-top:16px">Ordre des adjectifs devant hair : longueur puis couleur — long brown hair (jamais « brown long hair »). Et hair est singulier : it IS, jamais « they are » !</p>'),
    ('Le caractère : les adjectifs justes', None,
     '<p class="slide-explanation">Pour le caractère, accumule deux ou trois adjectifs reliés par <b>and</b> ou nuancés par <b>very / quite / a bit</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>funny</b> (drôle) · <b>friendly</b> (sympa) · <b>kind</b> (gentil) · <b>shy</b> (timide)</p>'
     '<p style="margin-top:8px"><b>clever</b> (intelligent) · <b>lazy</b> (paresseux) · <b>hard-working</b> (travailleur)</p>'
     '<p style="margin-top:8px">He is <b>very kind</b> but <b>a bit shy</b>. — Il est très gentil mais un peu timide.</p></div>'
     '<p style="margin-top:16px">Faux ami : <b>sympathetic</b> ≠ sympa ! Sympathetic = compatissant. « Sympa » se dit friendly ou nice.</p>'),
    ('Décrire un lieu : there is / there are', None,
     '<p class="slide-explanation">Pour un lieu, la machine à décrire est <b>there is / there are</b> + les prépositions de lieu. Organise du général au particulier.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>My town is small but very pretty. <b>There is</b> a beautiful park near the river. <b>There are</b> lots of cafés in the centre. My favourite place is the old market.</p></div>'
     '<p style="margin-top:16px">Général (small, pretty) → éléments (there is/are) → ta touche personnelle (my favourite place). Trois mouvements, un paragraphe.</p>'),
    ('Enrichir : but, because, really', None,
     '<p class="slide-explanation">Une description A2 gagne des points avec des <b>liens logiques</b> et des <b>intensificateurs</b> — sans phrases compliquées.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>He is quiet <b>but</b> very funny with his friends. — Il est réservé mais très drôle avec ses amis.</p>'
     '<p style="margin-top:8px">I love this place <b>because</b> it is always sunny. — J\'adore cet endroit parce qu\'il y fait toujours beau.</p>'
     '<p style="margin-top:8px">She is <b>really</b> good at tennis. — Elle est vraiment douée au tennis.</p></div>'
     '<p style="margin-top:16px">Good AT + activité : good at tennis, good at maths — jamais « good in ».</p>'),
  ],
  traps=[
    ('She has the hairs long and brown.', 'She has got <strong>long brown hair</strong>.', 'Hair est singulier et les adjectifs se placent AVANT : long brown hair.'),
    ('My friend is very sympathetic.', 'My friend is very <strong>friendly</strong>.', 'Sympathetic = compatissant, pas « sympa » ! Sympa = friendly / nice.'),
    ('He is a boy very shy.', 'He is a very <strong>shy boy</strong>.', 'L\'adjectif avant le nom : a very SHY BOY.'),
    ('In my town, it has a big park.', 'In my town, <strong>there is</strong> a big park.', '« Il y a » = there is/are — jamais « it has ».'),
    ('She is good in maths.', 'She is good <strong>at</strong> maths.', 'Good AT + matière/activité : good at maths.'),
  ],
  summary=[
    ('Plan portrait', 'identité → physique → caractère → goûts', 'My best friend is called Marco...'),
    ('Taille/allure', 'be + adjectif', 'She is tall and slim.'),
    ('Cheveux/yeux', 'have got + adjectifs + nom', 'He has got short black hair.'),
    ('Caractère', 'very / quite / a bit + adjectif', 'very kind but a bit shy'),
    ('Plan lieu', 'général → there is/are → touche perso', 'My town is small. There is a park...'),
    ('Liens', 'but · because · really · good at', 'I love it because it\'s sunny.'),
  ],
  ex1=('Be ou have got ?', 'Choisis la bonne structure de description.', [
    ('Décrire la taille : « Elle est grande. »', ['She is tall.', 'She has tall.', 'She has got tall.'], 'She is tall.',
     'La taille avec be : she IS tall.'),
    ('Décrire les cheveux : « Il a les cheveux courts. »', ['He has got short hair.', 'He is short hair.', 'He has got short hairs.'], 'He has got short hair.',
     'Les cheveux avec have got + hair SINGULIER.'),
    ('Décrire les yeux : « Elle a les yeux verts. »', ['She has got green eyes.', 'She is green eyes.', 'She has got eyes greens.'], 'She has got green eyes.',
     'Have got + adjectif + nom : green eyes.'),
    ('Décrire le caractère : « Il est très drôle. »', ['He is very funny.', 'He has very funny.', 'He is very fun person.'], 'He is very funny.',
     'Caractère avec be : he IS funny.'),
    ('« Elle a les cheveux longs et blonds. »', ['She has got long blond hair.', 'She has got blond long hair.', 'She has got hairs long and blond.'], 'She has got long blond hair.',
     'Ordre : longueur puis couleur — LONG BLOND hair.'),
    ('« Mon ami est sympa. »', ['My friend is friendly.', 'My friend is sympathetic.', 'My friend is sympathic.'], 'My friend is friendly.',
     'Sympa = friendly. Sympathetic est un faux ami (= compatissant).'),
  ]),
  ex2=('Complète la description', 'Écris le mot qui manque.', [
    ('My town is small ______ very pretty. (mais)', 'but',
     'Le contraste : small BUT pretty.'),
    ('______ is a beautiful park near the river. (il y a, singulier)', 'There',
     'Il y a = THERE is a park.'),
    ('There ______ lots of cafés in the centre. (il y a, pluriel)', 'are',
     'Lots of cafés = pluriel → there ARE.'),
    ('She is really good ______ tennis. (préposition)', 'at',
     'Good AT + activité.'),
    ('I love this place ______ it is always sunny. (parce que)', 'because',
     'La cause : BECAUSE it is sunny.'),
  ]),
  ex3=('Le portrait réussi', 'Choisis la meilleure version.', [
    ('La phrase d\'ouverture du portrait :', ['My best friend is called Marco and he is thirteen.', 'My best friend calls himself Marco, thirteen years.', 'My best friend Marco has thirteen years.'], 'My best friend is called Marco and he is thirteen.',
     'Is called = s\'appelle, et l\'âge avec be : he IS thirteen.'),
    ('Le physique :', ['He is tall and he has got curly brown hair.', 'He is tall and he is curly brown hair.', 'He has tall and has got hair curly.'], 'He is tall and he has got curly brown hair.',
     'Be pour la taille, have got pour les cheveux, adjectifs avant le nom.'),
    ('Le caractère nuancé :', ['He is very friendly but a bit lazy.', 'He is much friendly but little lazy.', 'He is a friendly but lazy very.'], 'He is very friendly but a bit lazy.',
     'Very + adjectif, a bit + adjectif, reliés par but.'),
    ('La description de lieu :', ['There are two cinemas and a big library in my town.', 'It has two cinemas and a big library in my town.', 'In my town has two cinemas.'], 'There are two cinemas and a big library in my town.',
     'Il y a + pluriel = there ARE. Jamais « it has ».'),
    ('La touche personnelle finale :', ['My favourite place is the old market because it is so lively.', 'The place I prefer most better is the market.', 'My place favourite is the market because so lively.'], 'My favourite place is the old market because it is so lively.',
     'My favourite place is... because... : possessif + adjectif avant le nom + cause.'),
  ]),
  game_desc='Chaque outil de description passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('is-called', 'is called', 's\'appelle — présenter quelqu\'un', 'identité', 'My best friend <b>is called</b> Marco.', 'My best friend is ______ Marco. (s\'appelle)', 'called'),
    ('is-tall', 'she is tall', 'la taille avec be — is + adjectif', 'taille', 'She <b>is tall</b> and slim.', 'She ______ tall and slim. (est)', 'is'),
    ('has-got-hair', 'has got long brown hair', 'les cheveux avec have got — hair singulier', 'cheveux', 'He <b>has got</b> short black hair.', 'He has ______ short black hair. (possession)', 'got'),
    ('friendly', 'friendly', 'sympa — PAS sympathetic (faux ami)', 'caractère', 'My friend is very <b>friendly</b>.', 'My friend is very ______. (sympa)', 'friendly'),
    ('a-bit-shy', 'a bit shy', 'un peu timide — nuancer un adjectif', 'nuance', 'He is kind but <b>a bit</b> shy.', 'He is kind but a ______ shy. (un peu)', 'bit'),
    ('there-is-place', 'There is a park', 'il y a — décrire un lieu', 'lieu', '<b>There is</b> a beautiful park near the river.', '______ is a beautiful park near the river. (il y a)', 'there'),
    ('good-at', 'good at', 'doué en — good AT, jamais good in', 'good at', 'She is really good <b>at</b> tennis.', 'She is really good ______ tennis. (préposition)', 'at'),
    ('because', 'because', 'parce que — justifier ce qu\'on aime', 'cause', 'I love this place <b>because</b> it is sunny.', 'I love this place ______ it is sunny. (parce que)', 'because'),
  ],
),

'postcard': dict(
  level='a2', section='redaction', num='Ch. 3', short='La carte postale',
  title='Postcard — Écrire une carte de vacances',
  subtitle='Having a great time! Le mélange des temps qui raconte les vacances',
  slides=[
    ('La carte postale : courte et vivante', None,
     '<p class="slide-explanation">La carte postale est un mini-récit de vacances : 40 à 60 mots, ton enthousiaste, et un <b>mélange de temps</b> bien précis — présent pour l\'ambiance, passé pour les activités.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Dear Emma,</b></p>'
     '<p style="margin-top:8px">Greetings from Spain! We\'re having a great time. The weather is hot and sunny. Yesterday we visited a castle and swam in the sea. Tomorrow we\'re going to the mountains.</p>'
     '<p style="margin-top:8px"><b>Wish you were here! Love, Léa</b></p></div>'),
    ('Les formules de la carte postale', None,
     '<p class="slide-explanation">La carte a ses expressions rituelles, à placer telles quelles — les examinateurs les attendent.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Greetings from Spain!</b> — Bonjour d\'Espagne !</p>'
     '<p style="margin-top:8px"><b>We\'re having a great time!</b> — On passe un super moment !</p>'
     '<p style="margin-top:8px"><b>Wish you were here!</b> — J\'aimerais que tu sois là !</p></div>'
     '<p style="margin-top:16px">« We\'re having a great time » utilise have au continuous — exception au verbe d\'état, car ici have = passer (un moment), pas posséder.</p>'),
    ('Le présent : ambiance et météo', None,
     '<p class="slide-explanation">Pour décrire le cadre (météo, hôtel, ambiance), on utilise le <b>présent</b> — simple pour les états, continuous pour ce qui se passe en ce moment.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>The weather <b>is</b> hot and sunny. — Il fait chaud et beau.</p>'
     '<p style="margin-top:8px">The hotel <b>is</b> right on the beach. — L\'hôtel est juste sur la plage.</p>'
     '<p style="margin-top:8px">I\'<b>m sitting</b> by the pool right now. — Je suis assis au bord de la piscine en ce moment.</p></div>'
     '<p style="margin-top:16px">La météo se dit avec be : the weather IS hot / it IS sunny — jamais « it makes hot » (calque de « il fait chaud »).</p>'),
    ('Le passé : ce qu\'on a fait', None,
     '<p class="slide-explanation">Les activités déjà faites passent au <b>past simple</b> — avec yesterday, last night, this morning.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Yesterday we <b>visited</b> the old town. — Hier on a visité la vieille ville.</p>'
     '<p style="margin-top:8px">We <b>swam</b> in the sea and <b>ate</b> delicious tapas. — On a nagé dans la mer et mangé de délicieuses tapas.</p>'
     '<p style="margin-top:8px">Last night we <b>went</b> to a concert. — Hier soir on est allés à un concert.</p></div>'
     '<p style="margin-top:16px">Révise tes irréguliers A1 : went, saw, ate, swam — la carte postale en est pleine !</p>'),
    ('Le futur : la suite du programme', None,
     '<p class="slide-explanation">Pour la suite des vacances, on utilise <b>be going to</b> ou le present continuous à valeur de futur — avec tomorrow, next week.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Tomorrow we\'<b>re going to visit</b> the islands. — Demain on va visiter les îles.</p>'
     '<p style="margin-top:8px">We\'<b>re coming home</b> on Saturday. — On rentre samedi.</p>'
     '<p style="margin-top:8px"><b>See you next week!</b> — À la semaine prochaine !</p></div>'
     '<p style="margin-top:16px">Le trio gagnant de la carte : présent (cadre) + passé (souvenirs) + futur (programme). Les trois temps en 50 mots !</p>'),
  ],
  traps=[
    ('It makes very hot here.', 'It <strong>is</strong> very hot here.', 'La météo avec be : it IS hot. « Il fait chaud » ne se traduit jamais par make.'),
    ('We have visited a castle yesterday.', 'We <strong>visited</strong> a castle yesterday.', 'Avec yesterday (moment passé précis), le past simple est obligatoire : we VISITED.'),
    ('We pass a great time.', 'We\'re <strong>having</strong> a great time.', '« Passer un bon moment » = have a great time — jamais pass.'),
    ('I wish you are here.', 'Wish you <strong>were</strong> here!', 'La formule consacrée utilise were : Wish you WERE here!'),
    ('Tomorrow we visited the islands.', 'Tomorrow we\'re <strong>going to visit</strong> the islands.', 'Tomorrow = futur → going to. Le past simple est réservé à ce qui est déjà arrivé.'),
  ],
  summary=[
    ('Format', '40-60 mots · Dear... → Love,', 'Dear Emma, ... Love, Léa'),
    ('Rituels', 'Greetings from...! · Wish you were here!', 'Greetings from Spain!'),
    ('Ambiance', 'présent : the weather is...', 'The weather is hot and sunny.'),
    ('Souvenirs', 'past simple + yesterday/last night', 'Yesterday we visited a castle.'),
    ('Programme', 'going to + tomorrow/next week', 'Tomorrow we\'re going to the beach.'),
    ('Enthousiasme', 'amazing · delicious · having a great time', 'We\'re having a great time!'),
  ],
  ex1=('Le bon temps pour chaque phrase', 'Présent, passé ou futur ?', [
    ('La météo, maintenant : The weather ______ beautiful.', ['is', 'was', 'makes'], 'is',
     'Le cadre actuel → présent : the weather IS beautiful.'),
    ('Hier : Yesterday we ______ the old town.', ['visited', 'visit', 'are visiting'], 'visited',
     'Yesterday → past simple : we VISITED.'),
    ('Demain : Tomorrow we ______ to the mountains.', ['are going', 'went', 'go yesterday'], 'are going',
     'Tomorrow → futur : we ARE GOING to the mountains.'),
    ('L\'ambiance : We ______ a great time!', ['are having', 'are passing', 'make'], 'are having',
     'Have a great time, au continuous : we\'re HAVING a great time.'),
    ('Hier soir : Last night we ______ to a flamenco show.', ['went', 'go', 'are going'], 'went',
     'Last night → past simple irrégulier : we WENT.'),
    ('La formule finale : Wish you ______ here!', ['were', 'are', 'will be'], 'were',
     'La formule fixe : Wish you WERE here!'),
  ]),
  ex2=('Complète la carte', 'Écris le mot qui manque.', [
    ('______ from Italy! (la formule d\'ouverture)', 'Greetings',
     'GREETINGS from + pays = bonjour de... !'),
    ('The weather ______ hot and sunny. (verbe)', 'is',
     'La météo avec be : the weather IS hot.'),
    ('Yesterday we ______ in the sea. (nager, au passé)', 'swam',
     'Swim → SWAM au past simple.'),
    ('We ate some ______ pizza! (délicieuse)', 'delicious',
     'L\'enthousiasme de la carte : DELICIOUS pizza.'),
    ('We\'re coming ______ on Saturday. (à la maison)', 'home',
     'Come HOME — sans préposition, comme go home.'),
  ]),
  ex3=('La carte postale complète', 'Choisis la meilleure version.', [
    ('L\'ouverture :', ['Greetings from Portugal! We\'re having a wonderful time.', 'I write you from Portugal where I am.', 'This is a postcard from Portugal.'], 'Greetings from Portugal! We\'re having a wonderful time.',
     'Formule rituelle + enthousiasme : l\'ouverture parfaite de carte postale.'),
    ('La météo :', ['It\'s sunny and really hot.', 'It makes sun and very hot.', 'The weather makes hot.'], 'It\'s sunny and really hot.',
     'Météo avec be : it IS sunny. Jamais make.'),
    ('Les activités d\'hier :', ['Yesterday we visited the castle and took lots of photos.', 'Yesterday we visit the castle and take photos.', 'Yesterday we have visited the castle.'], 'Yesterday we visited the castle and took lots of photos.',
     'Yesterday → past simple : visited, took.'),
    ('Le programme de demain :', ['Tomorrow we\'re going to explore the islands.', 'Tomorrow we explored the islands.', 'Tomorrow we go explored islands.'], 'Tomorrow we\'re going to explore the islands.',
     'Tomorrow → going to + base verbale : going to EXPLORE.'),
    ('La clôture :', ['Wish you were here! Love, Tom', 'I wish you are here. Sincerely, Mr Tom', 'You should be here. The end. Tom'], 'Wish you were here! Love, Tom',
     'La formule consacrée + signature amicale : Wish you were here! Love, Tom.'),
  ]),
  game_desc='Chaque formule de carte postale passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('greetings', 'Greetings from Spain!', 'bonjour d\'Espagne — l\'ouverture rituelle', 'ouverture', '<b>Greetings</b> from Spain!', '______ from Spain! (bonjour de)', 'greetings'),
    ('having-great-time', 'having a great time', 'passer un super moment — have, pas pass', 'l\'ambiance', 'We\'re <b>having</b> a great time!', 'We\'re ______ a great time! (passons)', 'having'),
    ('weather-is', 'the weather is hot', 'il fait chaud — la météo avec be', 'météo', 'The weather <b>is</b> hot and sunny.', 'The weather ______ hot and sunny. (il fait)', 'is'),
    ('yesterday-visited', 'yesterday we visited', 'hier on a visité — past simple', 'souvenirs', 'Yesterday we <b>visited</b> a castle.', 'Yesterday we ______ a castle. (avons visité)', 'visited'),
    ('swam', 'we swam', 'on a nagé — l\'irrégulier swim → swam', 'irrégulier', 'We <b>swam</b> in the sea.', 'We ______ in the sea. (avons nagé)', 'swam'),
    ('tomorrow-going', 'tomorrow we\'re going to...', 'demain on va... — le programme au futur', 'programme', 'Tomorrow we\'re <b>going to</b> visit the islands.', 'Tomorrow we\'re ______ to visit the islands. (futur)', 'going'),
    ('wish-you-were', 'Wish you were here!', 'j\'aimerais que tu sois là — la formule consacrée', 'formule', '<b>Wish you were</b> here!', 'Wish you ______ here! (sois)', 'were'),
    ('love-signature', 'Love, + prénom', 'bisous — la signature de la carte', 'signature', '<b>Love</b>, Léa', '______, Léa (bisous)', 'love'),
  ],
),

}
