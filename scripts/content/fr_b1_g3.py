# -*- coding: utf-8 -*-
"""fr/ B1 grammaire — lot 3 (4 chapitres)."""

CHAPTERS = {

'modal-deduction': dict(
  level='b1', section='grammaire', num='Ch. 11', short='Modals of Deduction',
  title='Modals of Deduction — Must, might, can’t',
  subtitle='Déduire : « ça doit être », « c’est peut-être », « impossible »',
  slides=[
    ('Trois degrés de certitude', None,
     '<p class="slide-explanation">Pour deviner à partir d’indices, l’anglais gradue la certitude avec trois modaux + be.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>must be</b> → quasi certain que c’est vrai : <b>She must be tired.</b> (Elle doit être fatiguée.)</p>'
     '<p style="margin-top:8px"><b>might/may/could be</b> → possible : <b>He might be at home.</b> (Il est peut-être chez lui.)</p>'
     '<p style="margin-top:8px"><b>can’t be</b> → quasi certain que c’est faux : <b>It can’t be true!</b> (C’est impossible !)</p></div>'),
    ('Must : la déduction logique', None,
     '<p class="slide-explanation">Ici must ne dit pas une obligation : il traduit notre « doit » de déduction (« il doit être fatigué »).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The lights are on — they must be at home.</b></p>'
     '<p style="margin-top:8px"><b>You’ve worked all day. You must be exhausted.</b></p></div>'),
    ('Le piège : le contraire de must est can’t', None,
     '<p class="slide-explanation">Pour la déduction négative (« ça ne peut pas être vrai »), l’anglais emploie <b>can’t</b>, jamais mustn’t.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>He ran a marathon — he can’t be unfit.</b> (Impossible qu’il soit en mauvaise forme.)</p>'
     '<p style="margin-top:8px">⚠ <b>mustn’t</b> = interdiction, pas déduction !</p></div>'),
    ('Might, may, could : le peut-être', None,
     '<p class="slide-explanation">Les trois expriment la possibilité, quasi interchangeables ici.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>She might be in a meeting.</b> · <b>He may be ill.</b> · <b>It could be a mistake.</b></p>'
     '<p style="margin-top:8px">Négation du peut-être : <b>might not / may not</b> (mais pas could not, qui bascule vers l’impossible).</p></div>'),
    ('Avec un verbe en -ing', None,
     '<p class="slide-explanation">Pour une action en cours déduite : modal + be + -ing.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>She’s not answering — she must be driving.</b> (Elle doit être en train de conduire.)</p>'
     '<p style="margin-top:8px"><b>They might be sleeping.</b></p></div>'),
  ],
  traps=[
    ('It mustn’t be true. (déduction)', 'It <strong>can’t</strong> be true.', 'Le contraire de must (déduction) est can’t — mustn’t exprime l’interdiction.'),
    ('She must to be tired.', 'She must <strong>be</strong> tired.', 'Modal + base verbale : must be, sans to.'),
    ('He can be at home now. (peut-être)', 'He <strong>might be</strong> at home now.', 'Pour « peut-être », on emploie might/may/could — can exprime une capacité générale.'),
    ('They must be tired? (intonation seule)', '<strong>They must be tired.</strong> / <strong>Must they be...?</strong> est rare', 'La déduction s’affirme ; pour demander, on dit Do you think they’re tired?'),
    ('Elle doit être en train de conduire → She must drive.', 'She must <strong>be driving</strong>.', 'Action en cours déduite → must be + -ing.'),
  ],
  summary=[
    ('Quasi sûr (vrai)', 'must be', 'They must be at home.'),
    ('Possible', 'might / may / could be', 'He might be ill.'),
    ('Quasi sûr (faux)', 'can’t be', 'It can’t be true.'),
    ('En cours', 'modal + be + -ing', 'She must be driving.'),
    ('Interdit ici', 'mustn’t (≠ déduction)', 'mustn’t = interdiction'),
  ],
  ex1=('Choisis le bon modal', 'Quel degré de certitude ?', [
    ('The lights are off — they ______ be out.', ['must', "can't", 'mustn’t'], 'must',
     'Indice fort (lumières éteintes) → déduction positive : they must be out.'),
    ('He ______ be French — he doesn’t speak a word of French!', ["can't", 'must', 'might'], "can't",
     'Déduction négative quasi certaine → can’t be.'),
    ('I’m not sure where she is. She ______ be at the gym.', ['might', 'must', "can't"], 'might',
     '« Je ne suis pas sûr » → simple possibilité : might be.'),
    ('You’ve been travelling all night — you ______ be exhausted.', ['must', 'might', "can't"], 'must',
     'Conclusion logique évidente → must be exhausted.'),
    ('She’s not answering her phone. She ______ be driving.', ['might', "mustn't", 'should'], 'might',
     'Explication possible → might be driving (modal + be + -ing).'),
    ('That ______ be John — John is in Canada!', ["can't", 'must', 'may'], "can't",
     'Impossible (il est au Canada) → can’t be John.'),
  ]),
  ex2=('Complète la déduction', 'Écris le modal (et be si demandé).', [
    ('Look at his house and his car — he ______ ______ rich. (quasi certain)', 'must be',
     'Déduction positive forte → must be rich.'),
    ('It ______ be true — I saw it with my own eyes! (impossible que ce soit faux... au contraire : c’est sûrement vrai → must)', 'must',
     'Ici on affirme la déduction positive : it must be true.'),
    ('They ______ be on holiday — I’m not sure. (peut-être)', 'might',
     'Possibilité incertaine → might (ou may/could).'),
    ('She ______ ______ sleeping — it’s 4 a.m. (doit être en train de)', 'must be',
     'Action en cours déduite → must be sleeping.'),
    ('He ______ be hungry — he has just eaten! (impossible)', "can't",
     'Déduction négative → can’t be hungry.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Tu dois être épuisé. »', ['You must be exhausted.', 'You have to be exhausted.', 'You should be exhausted.'], 'You must be exhausted.',
     '« Doit » de déduction → must be. Have to = obligation réelle.'),
    ('« C’est impossible, ça ne peut pas être vrai ! »', ["It can't be true!", "It mustn't be true!", "It shouldn't be true!"], "It can't be true!",
     'Déduction négative → can’t. Mustn’t serait une interdiction.'),
    ('« Elle est peut-être en réunion. »', ['She might be in a meeting.', 'She can be in a meeting.', 'She must be in a meeting.'], 'She might be in a meeting.',
     'Peut-être → might/may/could. Can exprime la capacité, pas la probabilité ponctuelle.'),
    ('« Ils doivent être en train de dîner. »', ['They must be having dinner.', 'They must have dinner.', 'They must to be having dinner.'], 'They must be having dinner.',
     'En train de + déduction → must be + -ing.'),
    ('« Ce n’est peut-être pas une erreur. »', ["It might not be a mistake.", "It can't be a mistake.", "It mustn't be a mistake."], 'It might not be a mistake.',
     'Possibilité négative → might not be.'),
  ]),
  game_desc='Chaque modal de déduction passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('must-be', 'must be', 'doit être — déduction quasi certaine', 'quasi certain (vrai)', 'She has a perfect score. She <b>must be</b> very talented.', 'She has a perfect score. She ______ ______ very talented.', 'must be'),
    ('cant-be', "can't be", 'ne peut pas être — déduction négative (jamais mustn’t)', 'quasi certain (faux)', "He ran a marathon. He <b>can't be</b> unfit.", 'He ran a marathon. He ______ be unfit.', "can't"),
    ('might-be', 'might be', 'est peut-être', 'possible', 'She <b>might be</b> at the gym.', 'She ______ be at the gym. (peut-être)', 'might'),
    ('may-be', 'may be', 'est peut-être — synonyme de might', 'possible (synonyme)', 'He <b>may be</b> ill.', 'He ______ be ill. (peut-être)', 'may'),
    ('could-be', 'could be', 'pourrait être — une possibilité parmi d’autres', 'autre possibilité', 'It <b>could be</b> a mistake.', 'It ______ be a mistake. (pourrait)', 'could'),
    ('must-be-ing', 'must be + -ing', 'doit être en train de', 'action en cours', 'She <b>must be driving</b>.', 'She must be ______ . (en train de conduire)', 'driving'),
    ('might-not', 'might not be', 'n’est peut-être pas', 'possibilité négative', 'It <b>might not be</b> true.', 'It might ______ be true. (peut-être pas)', 'not'),
    ('no-to-ded', 'modal + be (sans to)', 'jamais de to après le modal', 'règle de forme', 'She must <b>be</b> tired (jamais « must to be »).', 'She must ______ tired.', 'be'),
  ],
),

'passive-simple': dict(
  level='b1', section='grammaire', num='Ch. 12', short='Passive (Simple)',
  title='Passive — Le passif au présent et au prétérit',
  subtitle='Be + participe passé : quand l’action compte plus que l’acteur',
  slides=[
    ('Le principe : comme en français', None,
     '<p class="slide-explanation">Le passif anglais se construit comme le nôtre : <b>be + participe passé</b>. On l’emploie quand l’auteur de l’action est inconnu ou sans importance.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>This cheese is made in France.</b> (Ce fromage est fabriqué en France.)</p>'
     '<p style="margin-top:8px"><b>My bike was stolen yesterday.</b> (Mon vélo a été volé hier.)</p></div>'),
    ('Présent et prétérit passifs', None,
     '<p class="slide-explanation">Le temps se porte sur be : <b>am/is/are</b> + participe (présent), <b>was/were</b> + participe (prétérit).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>English is spoken here.</b> · <b>These cars are made in Japan.</b></p>'
     '<p style="margin-top:8px"><b>The bridge was built in 1890.</b> · <b>The letters were sent on Monday.</b></p></div>'),
    ('By : préciser l’auteur', None,
     '<p class="slide-explanation">Si l’auteur compte, on l’ajoute avec <b>by</b> (= par).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Hamlet was written by Shakespeare.</b></p>'
     '<p style="margin-top:8px"><b>The photo was taken by my sister.</b></p></div>'),
    ('Là où le français dit « on »', None,
     '<p class="slide-explanation">Le passif anglais traduit souvent notre « on » : « on parle anglais ici » → <b>English is spoken here.</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>« On m’a invité. » → <b>I was invited.</b></p>'
     '<p style="margin-top:8px">« On construit un nouveau pont. » → <b>A new bridge is being built.</b> (aperçu du continu)</p></div>'
     '<p style="margin-top:16px">Réflexe à prendre : avant de traduire « on » par « one » ou « we », pensez au passif.</p>'),
    ('Questions et négations', None,
     '<p class="slide-explanation">On manipule be comme d’habitude.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Was the house built in the 60s?</b> · <b>When was it built?</b></p>'
     '<p style="margin-top:8px"><b>The email wasn’t sent.</b> (L’e-mail n’a pas été envoyé.)</p></div>'),
  ],
  traps=[
    ('My bike was stole yesterday.', 'My bike was <strong>stolen</strong> yesterday.', 'Le passif exige le participe passé (3e colonne) : steal–stole–stolen.'),
    ('This cheese is make in France.', 'This cheese is <strong>made</strong> in France.', 'Be + participe passé : made, pas la base verbale.'),
    ('The book was written from Dickens.', 'The book was written <strong>by</strong> Dickens.', '« Par » = by au passif, jamais from.'),
    ('On parle anglais ici → One speaks English here.', '<strong>English is spoken here.</strong>', 'Le « on » français se rend le plus souvent par le passif.'),
    ('The letters was sent on Monday.', 'The letters <strong>were</strong> sent on Monday.', 'Be s’accorde avec le sujet : letters → were.'),
  ],
  summary=[
    ('Présent passif', 'am/is/are + participe', 'English is spoken here.'),
    ('Prétérit passif', 'was/were + participe', 'The bridge was built in 1890.'),
    ('Par...', 'by + auteur', 'written by Shakespeare'),
    ('« On »', '→ passif', 'I was invited. (on m’a invité)'),
    ('Question', 'Was/Were + sujet + participe ?', 'When was it built?'),
  ],
  ex1=('Choisis la forme passive correcte', 'Attention à l’accord de be et au participe.', [
    ('These watches ______ in Switzerland.', ['are made', 'are make', 'is made'], 'are made',
     'Sujet pluriel + présent passif → are made.'),
    ('The castle ______ in the 12th century.', ['was built', 'was build', 'is built'], 'was built',
     'Date passée → was + participe : was built.'),
    ('The Mona Lisa ______ by Leonardo da Vinci.', ['was painted', 'was paint', 'painted'], 'was painted',
     'Passif passé + auteur : was painted by...'),
    ('Portuguese ______ in Brazil.', ['is spoken', 'is speak', 'speaks'], 'is spoken',
     '« On parle portugais au Brésil » → is spoken.'),
    ('My keys ______ somewhere in the park.', ['were lost', 'was lost', 'were lose'], 'were lost',
     'Keys est pluriel → were lost.'),
    ('When ______ this photo ______ ?', ['was / taken', 'did / taken', 'was / took'], 'was / taken',
     'Question passive : When was this photo taken?'),
  ]),
  ex2=('Mets au passif', 'Écris la forme passive demandée.', [
    ('They make this cheese in Normandy. → This cheese ______ ______ in Normandy.', 'is made',
     'Présent passif : is made (le on/they disparaît).'),
    ('Somebody stole my bike. → My bike ______ ______ . ', 'was stolen',
     'Prétérit passif : was stolen.'),
    ('They built these houses in 1950. → These houses ______ built in 1950. (be)', 'were',
     'Sujet pluriel au passé → were built.'),
    ('Shakespeare wrote Hamlet. → Hamlet was written ______ Shakespeare. (par)', 'by',
     'L’auteur s’introduit avec by.'),
    ('On m’a invité à la fête. → I ______ invited to the party.', 'was',
     '« On m’a invité » → I was invited : le passif remplace « on ».'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« On parle français au Québec. »', ['French is spoken in Quebec.', 'One speaks French in Quebec.', 'They speaks French in Quebec.'], 'French is spoken in Quebec.',
     '« On » + verbe → passif anglais : is spoken.'),
    ('« Mon portefeuille a été volé. »', ['My wallet was stolen.', 'My wallet was stole.', 'My wallet stole.'], 'My wallet was stolen.',
     'Was + participe passé irrégulier : stolen.'),
    ('« Ce roman a été écrit par une amie. »', ['This novel was written by a friend.', 'This novel was written from a friend.', 'This novel wrote by a friend.'], 'This novel was written by a friend.',
     'Passif + by pour l’auteur.'),
    ('« Le dîner est servi à 20 h. »', ['Dinner is served at 8 p.m.', 'Dinner is serve at 8 p.m.', 'Dinner serves at 8 p.m.'], 'Dinner is served at 8 p.m.',
     'Présent passif : is served.'),
    ('« Les résultats n’ont pas été publiés. »', ["The results weren't published.", "The results wasn't published.", "The results didn't published."], "The results weren't published.",
     'Négation du passif passé, sujet pluriel → weren’t published.'),
  ]),
  game_desc='Chaque forme passive passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('is-made', 'is made', 'est fabriqué — présent passif singulier', 'présent passif', 'This cheese <b>is made</b> in France.', 'This cheese ______ ______ in France.', 'is made'),
    ('are-made', 'are made', 'sont fabriqués — présent passif pluriel', 'présent passif pluriel', 'These cars <b>are made</b> in Japan.', 'These cars ______ made in Japan.', 'are'),
    ('was-built', 'was built', 'a été construit — prétérit passif', 'prétérit passif', 'The bridge <b>was built</b> in 1890.', 'The bridge ______ ______ in 1890.', 'was built'),
    ('were-sent', 'were sent', 'ont été envoyés — prétérit passif pluriel', 'pluriel passé', 'The letters <b>were sent</b> on Monday.', 'The letters ______ sent on Monday.', 'were'),
    ('by', 'by + auteur', 'par — introduit l’auteur de l’action', 'complément d’agent', 'Hamlet was written <b>by</b> Shakespeare.', 'Hamlet was written ______ Shakespeare. (par)', 'by'),
    ('is-spoken', 'is spoken', 'se parle / on parle — le « on » français au passif', 'traduire « on »', 'English <b>is spoken</b> here.', 'English ______ ______ here. (on parle)', 'is spoken'),
    ('was-stolen', 'was stolen', 'a été volé — participe irrégulier stolen', 'participe irrégulier', 'My bike <b>was stolen</b> yesterday.', 'My bike was ______ yesterday. (volé)', 'stolen'),
    ('wasnt-sent', "wasn't sent", 'n’a pas été envoyé — négation du passif', 'négation', 'The email <b>wasn’t sent</b>.', 'The email ______ sent. (n’a pas été)', "wasn't"),
  ],
),

'passive-variations': dict(
  level='b1', section='grammaire', num='Ch. 13', short='Passive (Variations)',
  title='Passive Variations — Autres temps du passif',
  subtitle='Present perfect, futur, modaux et continu au passif',
  slides=[
    ('Le mécanisme universel', None,
     '<p class="slide-explanation">Quel que soit le temps, le passif = (temps porté par be ou l’auxiliaire) + <b>participe passé</b>. Il suffit de savoir conjuguer be.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>has been + participe</b> · <b>will be + participe</b> · <b>must be + participe</b> · <b>is being + participe</b></p></div>'),
    ('Present perfect passif', None,
     '<p class="slide-explanation"><b>Has/have been + participe</b> : résultat présent d’une action subie.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The road has been closed.</b> (La route a été fermée — elle l’est toujours.)</p>'
     '<p style="margin-top:8px"><b>Three people have been arrested.</b></p></div>'),
    ('Futur et modaux', None,
     '<p class="slide-explanation"><b>Will be + participe</b> pour le futur ; <b>can/must/should be + participe</b> avec les modaux.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The results will be published tomorrow.</b></p>'
     '<p style="margin-top:8px"><b>This form must be signed.</b> (Ce formulaire doit être signé.)</p>'
     '<p style="margin-top:8px"><b>It can be done in an hour.</b></p></div>'),
    ('Le passif continu', None,
     '<p class="slide-explanation"><b>Is/are being + participe</b> : action subie en cours — notre « est en train d’être ».</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The bridge is being repaired.</b> (Le pont est en cours de réparation.)</p>'
     '<p style="margin-top:8px"><b>Your order is being prepared.</b></p></div>'),
    ('Choisir actif ou passif', None,
     '<p class="slide-explanation">Le passif met en avant ce qui subit ; l’actif met en avant qui agit. L’anglais courant préfère l’actif quand l’acteur est connu.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Naturel : <b>My sister took this photo.</b></p>'
     '<p style="margin-top:8px">Passif justifié : <b>This photo was taken in 1990.</b> (peu importe par qui)</p></div>'),
  ],
  traps=[
    ('The road has been close.', 'The road has been <strong>closed</strong>.', 'Toujours le participe passé : closed.'),
    ('The results will published tomorrow.', 'The results will <strong>be</strong> published tomorrow.', 'Le be est obligatoire : will be published.'),
    ('This form must be sign.', 'This form must be <strong>signed</strong>.', 'Modal + be + participe passé : signed.'),
    ('The bridge is repairing. (en cours de réparation)', 'The bridge <strong>is being repaired</strong>.', 'Action subie en cours → is being + participe.'),
    ('It has being done.', 'It has <strong>been</strong> done.', 'Present perfect passif = has been + participe (being appartient au continu).'),
  ],
  summary=[
    ('Present perfect', 'has/have been + participe', 'The road has been closed.'),
    ('Futur', 'will be + participe', 'It will be published.'),
    ('Modal', 'must/can be + participe', 'This form must be signed.'),
    ('Continu', 'is/are being + participe', 'The bridge is being repaired.'),
    ('Choix', 'actif si l’acteur compte', 'My sister took this photo.'),
  ],
  ex1=('Choisis la forme passive', 'Quel temps de be ?', [
    ('The new hospital ______ next year.', ['will be opened', 'will opened', 'will being opened'], 'will be opened',
     'Futur passif : will be + participe.'),
    ('Your application ______ — we’ll reply soon.', ['has been received', 'has being received', 'has received'], 'has been received',
     'Present perfect passif : has been received.'),
    ('The lift ______ at the moment — take the stairs.', ['is being repaired', 'is repairing', 'is repaired now always'], 'is being repaired',
     'Action en cours subie → is being repaired.'),
    ('Helmets ______ on the building site.', ['must be worn', 'must wear', 'must be wear'], 'must be worn',
     'Modal passif : must be + worn (participe de wear).'),
    ('Two new schools ______ since 2020.', ['have been built', 'has been built', 'have being built'], 'have been built',
     'Sujet pluriel + present perfect passif : have been built.'),
    ('This document can ______ online.', ['be downloaded', 'download', 'be download'], 'be downloaded',
     'Can + be + participe : can be downloaded.'),
  ]),
  ex2=('Complète le passif', 'Écris la forme demandée.', [
    ('The email will ______ sent tomorrow. (be)', 'be',
     'Will be sent — le be ne disparaît jamais.'),
    ('The room is ______ cleaned right now. (en cours)', 'being',
     'Passif continu : is being cleaned.'),
    ('The match has ______ cancelled. (perfect passif)', 'been',
     'Has been cancelled : le match a été annulé.'),
    ('All answers must be ______ in English. (write → participe)', 'written',
     'Participe passé irrégulier : written.'),
    ('Dinner will be ______ at eight. (serve → participe)', 'served',
     'Will be served : sera servi.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« La route a été fermée. » (et l’est encore)', ['The road has been closed.', 'The road was closing.', 'The road has closed itself.'], 'The road has been closed.',
     'Résultat présent → present perfect passif.'),
    ('« Le pont est en cours de réparation. »', ['The bridge is being repaired.', 'The bridge is repairing.', 'The bridge repairs.'], 'The bridge is being repaired.',
     'En cours + subi → is being repaired.'),
    ('« Les résultats seront publiés demain. »', ['The results will be published tomorrow.', 'The results will publish tomorrow.', 'The results are published tomorrow by will.'], 'The results will be published tomorrow.',
     'Futur passif : will be published.'),
    ('« Ce formulaire doit être signé. »', ['This form must be signed.', 'This form must sign.', 'This form must to be signed.'], 'This form must be signed.',
     'Modal passif : must be signed, sans to.'),
    ('« Votre commande est en train d’être préparée. »', ['Your order is being prepared.', 'Your order is been prepared.', 'Your order is preparing.'], 'Your order is being prepared.',
     'Is being + participe — been appartient au perfect.'),
  ]),
  game_desc='Chaque variation du passif passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('has-been', 'has been + participe', 'a été — present perfect passif', 'perfect passif', 'The road <b>has been closed</b>.', 'The road has ______ closed.', 'been'),
    ('will-be', 'will be + participe', 'sera — futur passif', 'futur passif', 'The results <b>will be published</b> tomorrow.', 'The results will ______ published tomorrow.', 'be'),
    ('must-be-pp', 'must be + participe', 'doit être — modal passif', 'modal passif', 'This form <b>must be signed</b>.', 'This form must be ______ . (signé)', 'signed'),
    ('is-being', 'is being + participe', 'est en train d’être — passif continu', 'passif continu', 'The bridge <b>is being repaired</b>.', 'The bridge is ______ repaired.', 'being'),
    ('can-be', 'can be + participe', 'peut être fait', 'possibilité passive', 'It <b>can be done</b> in an hour.', 'It can ______ done in an hour.', 'be'),
    ('have-been-pl', 'have been + participe', 'ont été — perfect passif pluriel', 'pluriel', 'Three people <b>have been arrested</b>.', 'Three people ______ been arrested.', 'have'),
    ('worn', 'worn', 'porté — participe irrégulier de wear', 'participe irrégulier', 'Helmets must be <b>worn</b> on site.', 'Helmets must be ______ on site. (portés)', 'worn'),
    ('active-choice', 'actif préféré', 'si l’acteur est connu, l’anglais préfère l’actif', 'actif vs passif', '<b>My sister took</b> this photo.', 'My sister ______ this photo. (a pris)', 'took'),
  ],
),

'reported-speech-basic': dict(
  level='b1', section='grammaire', num='Ch. 14', short='Reported Speech',
  title='Reported Speech — Le discours indirect',
  subtitle='Said, told et le recul des temps',
  slides=[
    ('Le principe : un cran en arrière', None,
     '<p class="slide-explanation">Pour rapporter des paroles, l’anglais recule les temps d’un cran — comme la concordance française (« il a dit qu’il était fatigué »).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>“I <b>am</b> tired.” → He said he <b>was</b> tired.</p>'
     '<p style="margin-top:8px">“I <b>work</b> here.” → She said she <b>worked</b> there.</p>'
     '<p style="margin-top:8px">“I <b>will</b> call you.” → He said he <b>would</b> call me.</p></div>'),
    ('Say ou tell ?', None,
     '<p class="slide-explanation">LE piège francophone : « dire à quelqu’un » = <b>tell someone</b> (sans to !), say se contente des paroles.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>She said (that) she was busy.</b> — pas de destinataire</p>'
     '<p style="margin-top:8px"><b>She told me (that) she was busy.</b> — destinataire obligatoire après tell</p></div>'
     '<p style="margin-top:16px">« Elle m’a dit que... » → She told me that... (jamais « said me »).</p>'),
    ('La carte des reculs', None,
     '<p class="slide-explanation">Présent → prétérit · prétérit / present perfect → past perfect · will → would · can → could · must → had to.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>“I <b>have finished</b>.” → She said she <b>had finished</b>.</p>'
     '<p style="margin-top:8px">“I <b>can</b> help.” → He said he <b>could</b> help.</p></div>'),
    ('Les petits mots qui changent', None,
     '<p class="slide-explanation">Les repères se décalent aussi : today → that day, tomorrow → the next day, here → there, this → that.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>“I’ll see you <b>tomorrow</b>.” → She said she would see me <b>the next day</b>.</p></div>'),
    ('Rapporter les questions', None,
     '<p class="slide-explanation">Question rapportée = ordre affirmatif, sans do/did. Yes/no → <b>if</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>“Where do you live?” → He asked me <b>where I lived</b>.</p>'
     '<p style="margin-top:8px">“Are you OK?” → She asked <b>if I was</b> OK.</p></div>'),
  ],
  traps=[
    ('She said me that she was busy.', 'She <strong>told me</strong> that she was busy.', '« Dire à quelqu’un » = tell someone — say ne prend pas de destinataire direct.'),
    ('He told that he was tired.', 'He <strong>said</strong> that he was tired. / He told <strong>me</strong>...', 'Tell exige un destinataire ; sans destinataire, c’est say.'),
    ('He asked me where did I live.', 'He asked me where <strong>I lived</strong>.', 'Question rapportée → ordre affirmatif, sans did.'),
    ('She said she will call me. (hier)', 'She said she <strong>would</strong> call me.', 'Recul des temps : will → would.'),
    ('He told to me the truth.', 'He told <strong>me</strong> the truth.', 'Tell + destinataire directement, sans to.'),
  ],
  summary=[
    ('Dire (sans dest.)', 'say (that)...', 'She said she was busy.'),
    ('Dire à qqn', 'tell + personne', 'She told me she was busy.'),
    ('Recul', 'présent→prétérit, will→would', 'He said he would come.'),
    ('Repères', 'tomorrow → the next day', 'the next day, there, that'),
    ('Questions', 'asked + ordre affirmatif / if', 'He asked where I lived.'),
  ],
  ex1=('Say, tell et le recul des temps', 'Choisis la forme correcte.', [
    ('She ______ me she was leaving.', ['told', 'said', 'said to'], 'told',
     'Destinataire (me) → told me. « Said me » est l’erreur classique.'),
    ('He ______ that he was hungry.', ['said', 'told', 'asked to'], 'said',
     'Pas de destinataire → said that...'),
    ('“I can swim.” → She said she ______ swim.', ['could', 'can', 'would'], 'could',
     'Recul : can → could.'),
    ('“I will help you.” → He said he ______ help me.', ['would', 'will', 'had'], 'would',
     'Recul : will → would.'),
    ('“Where do you work?” → She asked me where I ______ .', ['worked', 'did work', 'work'], 'worked',
     'Question rapportée : ordre affirmatif + recul → where I worked.'),
    ('“Are you French?” → He asked ______ I was French.', ['if', 'that', 'what'], 'if',
     'Question fermée rapportée → if (ou whether).'),
  ]),
  ex2=('Rapporte les paroles', 'Écris le mot manquant.', [
    ('“I am tired.” → She said she ______ tired.', 'was',
     'Présent → prétérit : she was tired.'),
    ('“I have finished.” → He said he ______ finished.', 'had',
     'Present perfect → past perfect : had finished.'),
    ('Elle m’a dit la vérité. → She ______ me the truth.', 'told',
     'Dire quelque chose à quelqu’un → tell someone something.'),
    ('“I’ll see you tomorrow.” → She said she would see me the ______ day.', 'next',
     'Tomorrow → the next day dans le discours rapporté.'),
    ('“Do you like jazz?” → He asked me ______ I liked jazz.', 'if',
     'Yes/no question → if : he asked me if I liked jazz.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Elle m’a dit qu’elle était occupée. »', ['She told me she was busy.', 'She said me she was busy.', 'She told that she was busy.'], 'She told me she was busy.',
     'Dire à quelqu’un → tell + personne, et recul am → was.'),
    ('« Il a dit qu’il appellerait demain. »', ['He said he would call the next day.', 'He said he will call tomorrow.', 'He told he would call tomorrow.'], 'He said he would call the next day.',
     'Will → would et tomorrow → the next day.'),
    ('« Elle m’a demandé où j’habitais. »', ['She asked me where I lived.', 'She asked me where did I live.', 'She asked me where I live?'], 'She asked me where I lived.',
     'Question rapportée : ordre affirmatif + prétérit.'),
    ('« Il m’a demandé si j’étais prêt. »', ['He asked me if I was ready.', 'He asked me that I was ready.', 'He said me if I was ready.'], 'He asked me if I was ready.',
     'Question fermée → if ; asked + destinataire.'),
    ('« Dis-lui que je suis là. »', ["Tell him I'm here.", "Say him I'm here.", "Tell to him I'm here."], "Tell him I'm here.",
     'Tell + personne directement : tell him.'),
  ]),
  game_desc='Chaque mécanisme du discours indirect passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('told-me', 'told me', 'm’a dit — tell exige un destinataire', 'dire à quelqu’un', 'She <b>told me</b> she was busy.', 'She ______ me she was busy. (a dit)', 'told'),
    ('said-that', 'said (that)', 'a dit que — sans destinataire', 'dire (sans destinataire)', 'He <b>said</b> that he was tired.', 'He ______ that he was tired.', 'said'),
    ('was-backshift', 'am → was', 'le recul du présent au prétérit', 'recul des temps', '“I am tired.” → She said she <b>was</b> tired.', '“I am tired.” → She said she ______ tired.', 'was'),
    ('would-backshift', 'will → would', 'le recul de will', 'recul de will', 'He said he <b>would</b> call me.', 'He said he ______ call me.', 'would'),
    ('could-backshift', 'can → could', 'le recul de can', 'recul de can', 'She said she <b>could</b> help.', 'She said she ______ help.', 'could'),
    ('had-finished', 'have → had + participe', 'perfect → past perfect', 'recul du perfect', 'He said he <b>had finished</b>.', 'He said he ______ finished.', 'had'),
    ('asked-if', 'asked if', 'a demandé si — la question fermée rapportée', 'question rapportée', 'She <b>asked if</b> I was OK.', 'She asked ______ I was OK. (si)', 'if'),
    ('next-day', 'the next day', 'le lendemain — tomorrow rapporté', 'repère décalé', 'She said she would come <b>the next day</b>.', 'She said she would come the ______ day. (lendemain)', 'next'),
  ],
),
}
