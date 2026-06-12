# -*- coding: utf-8 -*-
"""fr/ A1 grammaire — lot 5 (chapitres 21-24). Explications en français, anglais cible."""

CHAPTERS = {

'simple-past-regular': dict(
  level='a1', section='grammaire', num='Ch. 21', short='Le passé régulier',
  title='Le past simple régulier — I worked, she didn\'t play',
  subtitle='Raconter le passé avec les verbes en -ed, et l\'auxiliaire did',
  slides=[
    ('Le past simple : un seul passé pour tout', None,
     '<p class="slide-explanation">Bonne nouvelle : là où le français hésite entre passé composé et imparfait, l\'anglais courant utilise un seul temps, le <b>past simple</b>. Pour les verbes réguliers, on ajoute simplement <b>-ed</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>worked</b> yesterday. — J\'ai travaillé hier.</p>'
     '<p style="margin-top:8px">She <b>played</b> tennis last Saturday. — Elle a joué au tennis samedi dernier.</p>'
     '<p style="margin-top:8px">We <b>watched</b> a film. — Nous avons regardé un film.</p></div>'
     '<p style="margin-top:16px">Encore mieux : la forme est <b>la même pour toutes les personnes</b>. I worked, she worked, they worked — pas de -s, pas d\'accord !</p>'),
    ('L\'orthographe du -ed', None,
     '<p class="slide-explanation">Quelques ajustements d\'orthographe à connaître quand on ajoute -ed.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>verbe en -e → <b>+d</b> : live → <b>lived</b> · dance → <b>danced</b></p>'
     '<p style="margin-top:8px">consonne + y → <b>-ied</b> : study → <b>studied</b> · try → <b>tried</b></p>'
     '<p style="margin-top:8px">voyelle courte + consonne → consonne doublée : stop → <b>stopped</b> · plan → <b>planned</b></p></div>'
     '<p style="margin-top:16px">Mais play → <b>played</b> (voyelle + y : le y reste) et visit → <b>visited</b> (pas de doublement).</p>'),
    ('La négation : didn\'t + base verbale', None,
     '<p class="slide-explanation">Au passé, l\'auxiliaire est <b>did</b> (le passé de do). La négation : <b>didn\'t + base verbale</b>. Le verbe perd son -ed — la marque du passé est déjà dans didn\'t !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>didn\'t work</b> yesterday. — Je n\'ai pas travaillé hier.</p>'
     '<p style="margin-top:8px">She <b>didn\'t play</b> tennis. — Elle n\'a pas joué au tennis.</p>'
     '<p style="margin-top:8px;color:var(--muted)">(et non « she didn\'t playED » — un seul marqueur de passé par phrase !)</p></div>'
     '<p style="margin-top:16px">Même logique qu\'au présent avec doesn\'t : l\'auxiliaire porte la marque, le verbe reste nu.</p>'),
    ('La question : Did + sujet + base verbale', None,
     '<p class="slide-explanation">Pour les questions au passé : <b>Did</b> + sujet + base verbale. Une seule forme pour toutes les personnes — encore plus simple que le présent !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Did you watch</b> the match? — As-tu regardé le match ?</p>'
     '<p style="margin-top:8px"><b>Did she visit</b> Paris? — A-t-elle visité Paris ?</p>'
     '<p style="margin-top:8px">Réponses : <b>Yes, I did.</b> / <b>No, she didn\'t.</b></p></div>'
     '<p style="margin-top:16px">Le verbe reste à la base : Did you WATCH? — jamais « Did you watched? ».</p>'),
    ('Les expressions de temps du passé', None,
     '<p class="slide-explanation">Le past simple s\'accompagne d\'expressions qui datent l\'action. Ce sont elles qui déclenchent le passé dans une phrase.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>yesterday</b> (hier) &nbsp;·&nbsp; <b>last night</b> (hier soir) &nbsp;·&nbsp; <b>last week</b> (la semaine dernière)</p>'
     '<p style="margin-top:8px"><b>two days ago</b> (il y a deux jours) &nbsp;·&nbsp; <b>in 2020</b> (en 2020)</p>'
     '<p style="margin-top:8px">I visited London <b>two years ago</b>. — J\'ai visité Londres il y a deux ans.</p></div>'
     '<p style="margin-top:16px">Piège : « il y a deux jours » = two days <b>ago</b> — ago se place APRÈS la durée, pas avant.</p>'),
  ],
  traps=[
    ('She didn\'t played tennis.', 'She didn\'t <strong>play</strong> tennis.', 'Après didn\'t, base verbale : didn\'t PLAY. Le passé est déjà marqué par didn\'t.'),
    ('Did you watched the film?', 'Did you <strong>watch</strong> the film?', 'Après did, base verbale : Did you WATCH? Un seul marqueur de passé par phrase.'),
    ('I have worked yesterday.', 'I <strong>worked</strong> yesterday.', 'Avec une date passée précise (yesterday), l\'anglais utilise le past simple, pas have + participe. « J\'ai travaillé hier » → I WORKED yesterday.'),
    ('He studyed for the exam.', 'He <strong>studied</strong> for the exam.', 'Consonne + y → -ied : study → studIED.'),
    ('I visited London ago two years.', 'I visited London two years <strong>ago</strong>.', 'Ago se place APRÈS la durée : two years AGO (≠ « il y a » qui se place avant).'),
  ],
  summary=[
    ('Affirmation', 'verbe + -ed (toutes personnes)', 'I worked. / She played.'),
    ('Orthographe', 'live → lived · study → studied · stop → stopped', 'lived / studied / stopped'),
    ('Négation', 'didn\'t + base verbale', 'She didn\'t play tennis.'),
    ('Question', 'Did + sujet + base verbale?', 'Did you watch the match?'),
    ('Réponse courte', 'Yes, I did. / No, I didn\'t.', 'Did she call? Yes, she did.'),
    ('Temps du passé', 'yesterday · last week · two days ago', 'I visited London two years ago.'),
  ],
  ex1=('Mets le verbe au past simple', 'Attention à l\'orthographe du -ed.', [
    ('I ______ football yesterday. (play)', ['played', 'plaied', 'playd'], 'played',
     'Voyelle + y → le y reste : playED.'),
    ('She ______ English last year. (study)', ['studied', 'studyed', 'studed'], 'studied',
     'Consonne + y → -ied : studIED.'),
    ('We ______ in Paris in 2020. (live)', ['lived', 'liveed', 'livd'], 'lived',
     'Verbe en -e → on ajoute juste -d : livED.'),
    ('The bus ______ at the station. (stop)', ['stopped', 'stoped', 'stopt'], 'stopped',
     'Voyelle courte + consonne → doublement : stoPPed.'),
    ('They ______ a great film last night. (watch)', ['watched', 'watchd', 'watcht'], 'watched',
     'Cas simple : watch + ED = watched.'),
    ('He ______ his grandmother two days ago. (visit)', ['visited', 'visitted', 'visit'], 'visited',
     'Pas de doublement sur visit : visitED.'),
  ]),
  ex2=('Négation et question au passé', 'Utilise did / didn\'t + base verbale.', [
    ('« Je n\'ai pas travaillé hier. » → I ______ work yesterday. (un mot)', 'didn\'t',
     'Négation au passé : DIDN\'T + base verbale work.'),
    ('« As-tu regardé le match ? » → ______ you watch the match? (un mot)', 'Did',
     'Question au passé : DID + sujet + base verbale.'),
    ('« Elle n\'a pas aimé le film. » → She didn\'t ______ the film. (un mot)', 'like',
     'Après didn\'t → base verbale LIKE (sans -d).'),
    ('« Oui, j\'ai appelé. » (réponse à Did you call?) → Yes, I ______. (un mot)', 'did',
     'Réponse courte : Yes, I DID — on reprend l\'auxiliaire.'),
    ('« Avez-vous visité le musée ? » → Did you ______ the museum? (un mot)', 'visit',
     'Après did → base verbale VISIT (sans -ed).'),
  ]),
  ex3=('Trouve la phrase correcte', 'Un seul marqueur de passé par phrase !', [
    ('« Elle a dansé toute la nuit. »', ['She danced all night.', 'She danceed all night.', 'She did danced all night.'], 'She danced all night.',
     'Dance + d = danced. Pas de did dans une affirmation.'),
    ('« Nous n\'avons pas regardé la télé. »', ['We didn\'t watch TV.', 'We didn\'t watched TV.', 'We don\'t watched TV.'], 'We didn\'t watch TV.',
     'Didn\'t + base verbale : didn\'t WATCH.'),
    ('« A-t-il téléphoné hier soir ? »', ['Did he call last night?', 'Did he called last night?', 'Does he called last night?'], 'Did he call last night?',
     'Did + base verbale : Did he CALL?'),
    ('« J\'ai habité à Lyon il y a trois ans. »', ['I lived in Lyon three years ago.', 'I lived in Lyon ago three years.', 'I have lived in Lyon three years ago.'], 'I lived in Lyon three years ago.',
     'Past simple + durée + AGO : three years ago.'),
    ('« Ils ont étudié pour l\'examen. »', ['They studied for the exam.', 'They studyed for the exam.', 'They did studied for the exam.'], 'They studied for the exam.',
     'Study → studIED (consonne + y).'),
  ]),
  game_desc='Chaque forme du past simple régulier passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('worked', 'worked', 'travaillé — verbe + -ed, toutes personnes', '-ed', 'I <b>worked</b> late yesterday.', 'I ______ late yesterday. (ai travaillé)', 'worked'),
    ('lived', 'lived', 'habité — verbe en -e : on ajoute juste -d', '+d', 'We <b>lived</b> in Paris in 2020.', 'We ______ in Paris in 2020. (habitions)', 'lived'),
    ('studied', 'studied', 'étudié — consonne + y → -ied', '-ied', 'She <b>studied</b> English last year.', 'She ______ English last year. (a étudié)', 'studied'),
    ('stopped', 'stopped', 'arrêté — consonne doublée après voyelle courte', 'doublement', 'The bus <b>stopped</b> at the station.', 'The bus ______ at the station. (s\'est arrêté)', 'stopped'),
    ('didnt-play', 'didn\'t play', 'négation — didn\'t + base verbale sans -ed', 'négation', 'She <b>didn\'t play</b> tennis.', 'She didn\'t ______ tennis. (jouer)', 'play'),
    ('did-you', 'Did you...?', 'question — did + sujet + base verbale', 'question', '<b>Did</b> you watch the match?', '______ you watch the match? (auxiliaire)', 'did'),
    ('yesterday', 'yesterday', 'hier — déclencheur du past simple', 'hier', 'I worked <b>yesterday</b>.', 'I worked ______. (hier)', 'yesterday'),
    ('ago', 'two years ago', 'il y a deux ans — ago APRÈS la durée', 'il y a', 'I visited London two years <b>ago</b>.', 'I visited London two years ______. (il y a)', 'ago'),
  ],
),

'simple-past-irregular': dict(
  level='a1', section='grammaire', num='Ch. 22', short='Le passé irrégulier',
  title='Le past simple irrégulier — went, saw, ate, had',
  subtitle='Les verbes irréguliers les plus fréquents, à apprendre par cœur',
  slides=[
    ('Les irréguliers : pas de -ed, des formes à mémoriser', None,
     '<p class="slide-explanation">Les verbes les plus fréquents de l\'anglais sont <b>irréguliers</b> : leur passé ne prend pas -ed, il change de forme. Pas de règle — il faut les apprendre, comme les conjugaisons françaises.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>go → <b>went</b> (aller) &nbsp;·&nbsp; see → <b>saw</b> (voir) &nbsp;·&nbsp; eat → <b>ate</b> (manger)</p>'
     '<p style="margin-top:8px">have → <b>had</b> (avoir) &nbsp;·&nbsp; do → <b>did</b> (faire) &nbsp;·&nbsp; make → <b>made</b> (faire/fabriquer)</p></div>'
     '<p style="margin-top:16px">La bonne nouvelle reste : <b>une seule forme pour toutes les personnes</b>. I went, she went, they went.</p>'),
    ('Les 12 irréguliers indispensables', None,
     '<p class="slide-explanation">Voici les irréguliers qu\'il faut absolument connaître au niveau A1 — ils couvrent l\'essentiel de la conversation.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>be → <b>was/were</b> &nbsp;·&nbsp; go → <b>went</b> &nbsp;·&nbsp; have → <b>had</b> &nbsp;·&nbsp; do → <b>did</b></p>'
     '<p style="margin-top:8px">see → <b>saw</b> &nbsp;·&nbsp; eat → <b>ate</b> &nbsp;·&nbsp; drink → <b>drank</b> &nbsp;·&nbsp; take → <b>took</b></p>'
     '<p style="margin-top:8px">come → <b>came</b> &nbsp;·&nbsp; buy → <b>bought</b> &nbsp;·&nbsp; get → <b>got</b> &nbsp;·&nbsp; say → <b>said</b></p></div>'
     '<p style="margin-top:16px">Astuce : apprends-les par trois chaque jour, avec une phrase exemple pour chacun.</p>'),
    ('Was et were : le passé de to be', None,
     '<p class="slide-explanation">To be est le seul verbe avec DEUX formes au passé : <b>was</b> (I, he, she, it) et <b>were</b> (you, we, they).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>was</b> tired last night. — J\'étais fatigué hier soir.</p>'
     '<p style="margin-top:8px">They <b>were</b> at the cinema. — Ils étaient au cinéma.</p>'
     '<p style="margin-top:8px"><b>Were you</b> at home? — Étais-tu à la maison ? · No, I <b>wasn\'t</b>.</p></div>'
     '<p style="margin-top:16px">Comme au présent, be se passe de did : négation avec wasn\'t/weren\'t, question par inversion.</p>'),
    ('Négation et question : did pour tous', None,
     '<p class="slide-explanation">Énorme avantage : au négatif et à la question, <b>tous les verbes (sauf be) utilisent did</b> — et le verbe revient à la base. L\'irrégularité disparaît !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I went → I <b>didn\'t go</b> (et non « didn\'t went »)</p>'
     '<p style="margin-top:8px">She saw the film → <b>Did she see</b> the film? (et non « Did she saw »)</p>'
     '<p style="margin-top:8px">They ate pizza → They <b>didn\'t eat</b> pizza.</p></div>'
     '<p style="margin-top:16px">Retiens : la forme irrégulière (went, saw, ate) ne s\'utilise QUE dans les phrases affirmatives.</p>'),
    ('Raconter sa journée au passé', None,
     '<p class="slide-explanation">Avec une dizaine d\'irréguliers, tu peux déjà raconter ta journée — c\'est l\'exercice de production classique du niveau A1.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Yesterday I <b>got</b> up at 7. I <b>had</b> breakfast and I <b>went</b> to school.</p>'
     '<p style="margin-top:8px">At lunchtime I <b>ate</b> a sandwich and <b>drank</b> some juice.</p>'
     '<p style="margin-top:8px">After school I <b>saw</b> my friends and we <b>did</b> our homework.</p></div>'
     '<p style="margin-top:16px">Remarque la chaîne : got up, had, went, ate, drank, saw, did — sept irréguliers dans un récit tout simple.</p>'),
  ],
  traps=[
    ('I didn\'t went to school.', 'I didn\'t <strong>go</strong> to school.', 'Après didn\'t, base verbale : didn\'t GO. La forme irrégulière went ne s\'utilise qu\'à l\'affirmatif.'),
    ('Did you saw the film?', 'Did you <strong>see</strong> the film?', 'Après did, base verbale : Did you SEE? Jamais deux marqueurs de passé.'),
    ('I goed to the beach.', 'I <strong>went</strong> to the beach.', 'Go est irrégulier : pas de -ed. Go → WENT.'),
    ('They was at the cinema.', 'They <strong>were</strong> at the cinema.', 'They → WERE. Was est réservé à I/he/she/it.'),
    ('She maked a cake.', 'She <strong>made</strong> a cake.', 'Make est irrégulier : make → MADE (pas « maked »).'),
  ],
  summary=[
    ('Le principe', 'forme spéciale, pas de -ed', 'go → went · see → saw · eat → ate'),
    ('Be au passé', 'was (I/he/she/it) · were (you/we/they)', 'I was tired. / They were here.'),
    ('Négation', 'didn\'t + base verbale', 'I didn\'t go to school.'),
    ('Question', 'Did + sujet + base verbale?', 'Did you see the film?'),
    ('Affirmatif seul', 'went/saw/ate uniquement à l\'affirmatif', 'I went. MAIS I didn\'t go.'),
    ('Les indispensables', 'went · had · did · saw · ate · came · took · bought', 'Yesterday I went to school.'),
  ],
  ex1=('Choisis la forme irrégulière', 'Pas de -ed sur ces verbes !', [
    ('Yesterday I ______ to the cinema. (go)', ['went', 'goed', 'gone'], 'went',
     'Go → WENT. « Goed » n\'existe pas.'),
    ('She ______ a beautiful bird in the garden. (see)', ['saw', 'seed', 'seen'], 'saw',
     'See → SAW au past simple.'),
    ('We ______ pizza for dinner. (eat)', ['ate', 'eated', 'eaten'], 'ate',
     'Eat → ATE.'),
    ('He ______ a new phone last week. (buy)', ['bought', 'buyed', 'buied'], 'bought',
     'Buy → BOUGHT — un des irréguliers les plus surprenants.'),
    ('I ______ breakfast at 8 o\'clock. (have)', ['had', 'haved', 'has'], 'had',
     'Have → HAD.'),
    ('They ______ to my party last Saturday. (come)', ['came', 'comed', 'come'], 'came',
     'Come → CAME.'),
  ]),
  ex2=('Was ou were ? Affirmatif ou négatif ?', 'Écris la forme correcte.', [
    ('« J\'étais fatigué hier soir. » → I ______ tired last night.', 'was',
     'I → WAS : I was tired.'),
    ('« Ils étaient au parc. » → They ______ at the park.', 'were',
     'They → WERE.'),
    ('« Tu n\'étais pas à la maison. » → You ______ at home. (un mot, contraction)', 'weren\'t',
     'You → WEREN\'T (were not).'),
    ('« Elle n\'est pas allée à l\'école. » → She didn\'t ______ to school.', 'go',
     'Après didn\'t → base verbale GO (pas went).'),
    ('« As-tu vu le match ? » → Did you ______ the match?', 'see',
     'Après did → base verbale SEE (pas saw).'),
  ]),
  ex3=('Raconte au passé', 'Choisis la phrase correcte.', [
    ('« Hier, je me suis levé à 7 h. »', ['Yesterday I got up at 7.', 'Yesterday I getted up at 7.', 'Yesterday I get up at 7.'], 'Yesterday I got up at 7.',
     'Get → GOT : I got up.'),
    ('« Nous avons bu du jus d\'orange. »', ['We drank some orange juice.', 'We drinked some orange juice.', 'We drunk some orange juice.'], 'We drank some orange juice.',
     'Drink → DRANK au past simple.'),
    ('« Elle a pris le bus. »', ['She took the bus.', 'She taked the bus.', 'She did take the bus yesterday morning early.'], 'She took the bus.',
     'Take → TOOK.'),
    ('« Je n\'ai pas fait mes devoirs. »', ['I didn\'t do my homework.', 'I didn\'t did my homework.', 'I didn\'t my homework.'], 'I didn\'t do my homework.',
     'Didn\'t + base verbale DO : I didn\'t do.'),
    ('« Il a dit bonjour. »', ['He said hello.', 'He sayed hello.', 'He says hello yesterday.'], 'He said hello.',
     'Say → SAID.'),
  ]),
  game_desc='Chaque verbe irrégulier passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('went', 'went', 'allé — le passé de go', 'go → went', 'Yesterday I <b>went</b> to school.', 'Yesterday I ______ to school. (suis allé)', 'went'),
    ('saw', 'saw', 'vu — le passé de see', 'see → saw', 'She <b>saw</b> a great film.', 'She ______ a great film. (a vu)', 'saw'),
    ('ate', 'ate', 'mangé — le passé de eat', 'eat → ate', 'We <b>ate</b> pizza for dinner.', 'We ______ pizza for dinner. (avons mangé)', 'ate'),
    ('had', 'had', 'eu / pris — le passé de have', 'have → had', 'I <b>had</b> breakfast at 8.', 'I ______ breakfast at 8. (ai pris)', 'had'),
    ('was-were', 'was / were', 'était / étaient — le passé de be', 'be au passé', 'They <b>were</b> at the cinema.', 'They ______ at the cinema. (étaient)', 'were'),
    ('bought', 'bought', 'acheté — le passé de buy', 'buy → bought', 'He <b>bought</b> a new phone.', 'He ______ a new phone. (a acheté)', 'bought'),
    ('didnt-go', 'didn\'t go', 'négation — base verbale, pas la forme irrégulière', 'négation', 'I <b>didn\'t go</b> to school.', 'I didn\'t ______ to school. (aller)', 'go'),
    ('did-you-see', 'Did you see...?', 'question — did + base verbale', 'question', '<b>Did</b> you <b>see</b> the match?', 'Did you ______ the match? (voir)', 'see'),
  ],
),

'prepositions-time': dict(
  level='a1', section='grammaire', num='Ch. 23', short='Prépositions de temps',
  title='Les prépositions de temps — at, on, in',
  subtitle='At 3 o\'clock, on Monday, in March : le système qui remplace « à, le, en »',
  slides=[
    ('Trois prépositions, trois échelles', None,
     '<p class="slide-explanation">L\'anglais répartit le temps sur trois prépositions selon la <b>précision</b> : <b>at</b> pour l\'heure exacte, <b>on</b> pour le jour, <b>in</b> pour les périodes longues. Imagine un zoom : at = précis, in = large.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>at</b> 3 o\'clock — à 3 heures (moment précis)</p>'
     '<p style="margin-top:8px"><b>on</b> Monday — lundi (jour)</p>'
     '<p style="margin-top:8px"><b>in</b> March — en mars (mois, période longue)</p></div>'
     '<p style="margin-top:16px">Le français utilise « à, le, en » de façon différente — ne traduis pas mot à mot, apprends les trois catégories.</p>'),
    ('At : l\'heure et les moments fixes', None,
     '<p class="slide-explanation"><b>At</b> s\'utilise pour les heures et quelques expressions fixes à mémoriser.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>at</b> 7 o\'clock · <b>at</b> half past two · <b>at</b> midnight (à minuit)</p>'
     '<p style="margin-top:8px"><b>at</b> night (la nuit) · <b>at</b> the weekend (le week-end)</p>'
     '<p style="margin-top:8px"><b>at</b> Christmas (à Noël) · <b>at</b> lunchtime (à midi, au déjeuner)</p></div>'
     '<p style="margin-top:16px">Surprises : AT night (mais in the morning !) et AT the weekend. Ce sont les deux à retenir par cœur.</p>'),
    ('On : les jours et les dates', None,
     '<p class="slide-explanation"><b>On</b> s\'utilise pour les jours de la semaine et les dates complètes. Le français dit « lundi » sans préposition — l\'anglais exige <b>on</b> !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>on</b> Monday — lundi · <b>on</b> Mondays — le lundi (tous les lundis)</p>'
     '<p style="margin-top:8px"><b>on</b> 14th July — le 14 juillet · <b>on</b> my birthday — le jour de mon anniversaire</p>'
     '<p style="margin-top:8px"><b>on</b> Friday morning — vendredi matin</p></div>'
     '<p style="margin-top:16px">« I play tennis Monday » est une faute : il faut ON Monday. Et jour + partie de journée → on : ON Friday morning.</p>'),
    ('In : les mois, saisons, années', None,
     '<p class="slide-explanation"><b>In</b> couvre toutes les périodes longues : mois, saisons, années, siècles — et aussi les parties de la journée.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>in</b> March (en mars) · <b>in</b> summer (en été) · <b>in</b> 2026 (en 2026)</p>'
     '<p style="margin-top:8px"><b>in</b> the morning (le matin) · <b>in</b> the afternoon (l\'après-midi) · <b>in</b> the evening (le soir)</p></div>'
     '<p style="margin-top:16px">Contraste à mémoriser : <b>in</b> the morning MAIS <b>at</b> night. L\'anglais n\'est pas logique ici — apprends les deux ensemble.</p>'),
    ('Sans préposition : next, last, every, this', None,
     '<p class="slide-explanation">Piège final : devant <b>next, last, every, this</b>, on ne met AUCUNE préposition — alors que le français en met parfois une.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I saw her <b>last week</b>. — Je l\'ai vue la semaine dernière. (pas de « in » !)</p>'
     '<p style="margin-top:8px">We\'re leaving <b>next Monday</b>. — Nous partons lundi prochain. (pas de « on » !)</p>'
     '<p style="margin-top:8px">I play tennis <b>every Saturday</b>. — Je joue au tennis tous les samedis.</p></div>'
     '<p style="margin-top:16px">Règle simple : next/last/every/this « mangent » la préposition. On Monday, mais next Monday.</p>'),
  ],
  traps=[
    ('I play tennis Monday.', 'I play tennis <strong>on</strong> Monday.', 'Les jours exigent on en anglais : ON Monday — même si le français dit juste « lundi ».'),
    ('She was born on 2010.', 'She was born <strong>in</strong> 2010.', 'Les années prennent in : IN 2010. On est réservé aux jours et dates complètes.'),
    ('I get up early in the night.', 'I sleep <strong>at</strong> night.', 'La nuit fait exception : AT night (mais in the morning, in the evening).'),
    ('We\'re leaving on next Monday.', 'We\'re leaving <strong>next Monday</strong>.', 'Pas de préposition devant next/last/every/this : next Monday tout court.'),
    ('The film starts in 8 o\'clock.', 'The film starts <strong>at</strong> 8 o\'clock.', 'Les heures précises prennent at : AT 8 o\'clock.'),
  ],
  summary=[
    ('AT', 'heures et moments fixes', 'at 3 o\'clock / at night / at the weekend'),
    ('ON', 'jours et dates', 'on Monday / on 14th July / on my birthday'),
    ('IN', 'mois, saisons, années', 'in March / in summer / in 2026'),
    ('Parties du jour', 'in the morning MAIS at night', 'in the evening / at night'),
    ('Sans préposition', 'next, last, every, this', 'next Monday / last week / every day'),
    ('Jour + moment', 'on + jour + moment', 'on Friday morning'),
  ],
  ex1=('At, on ou in ?', 'Heure → at · jour → on · période → in.', [
    ('The lesson starts ______ 9 o\'clock.', ['at', 'on', 'in'], 'at',
     'Heure précise → AT 9 o\'clock.'),
    ('We have English ______ Mondays.', ['on', 'at', 'in'], 'on',
     'Jour de la semaine → ON Mondays.'),
    ('My birthday is ______ June.', ['in', 'on', 'at'], 'in',
     'Mois → IN June.'),
    ('It\'s very cold ______ winter.', ['in', 'at', 'on'], 'in',
     'Saison → IN winter.'),
    ('I don\'t work ______ the weekend.', ['at', 'on', 'in'], 'at',
     'Expression fixe → AT the weekend (anglais britannique).'),
    ('She was born ______ 14th July.', ['on', 'in', 'at'], 'on',
     'Date complète → ON 14th July.'),
  ]),
  ex2=('Traduis la préposition', 'Écris at, on, in — ou rien (écris « X ») si aucune préposition.', [
    ('« le matin » → ______ the morning', 'in',
     'Parties de la journée → IN the morning.'),
    ('« la nuit » → ______ night', 'at',
     'Exception : AT night (sans the).'),
    ('« en 2026 » → ______ 2026', 'in',
     'Année → IN 2026.'),
    ('« lundi prochain » → ______ next Monday', 'X',
     'Pas de préposition devant next : next Monday tout court.'),
    ('« vendredi matin » → ______ Friday morning', 'on',
     'Jour + partie de journée → ON Friday morning.'),
  ]),
  ex3=('Trouve la phrase correcte', 'Attention aux exceptions !', [
    ('« Je me lève à 7 h le matin. »', ['I get up at 7 in the morning.', 'I get up in 7 at the morning.', 'I get up at 7 at the morning.'], 'I get up at 7 in the morning.',
     'AT + heure, IN + the morning.'),
    ('« Nous partons la semaine prochaine. »', ['We\'re leaving next week.', 'We\'re leaving in next week.', 'We\'re leaving on next week.'], 'We\'re leaving next week.',
     'Next « mange » la préposition : next week tout court.'),
    ('« Il travaille la nuit. »', ['He works at night.', 'He works in the night.', 'He works on night.'], 'He works at night.',
     'Exception mémorisable : AT night.'),
    ('« Mon anniversaire est le 3 mars. »', ['My birthday is on 3rd March.', 'My birthday is in 3rd March.', 'My birthday is at 3rd March.'], 'My birthday is on 3rd March.',
     'Date complète → ON 3rd March.'),
    ('« On se voit samedi à midi. »', ['See you on Saturday at lunchtime.', 'See you at Saturday on lunchtime.', 'See you in Saturday at lunchtime.'], 'See you on Saturday at lunchtime.',
     'ON + jour, AT + lunchtime (moment fixe).'),
  ]),
  game_desc='Chaque préposition de temps passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('at-oclock', 'at 3 o\'clock', 'à + heure précise', 'l\'heure', 'The film starts <b>at</b> 8 o\'clock.', 'The film starts ______ 8 o\'clock. (à)', 'at'),
    ('on-monday', 'on Monday', 'le + jour de la semaine', 'les jours', 'We have English <b>on</b> Mondays.', 'We have English ______ Mondays. (le lundi)', 'on'),
    ('in-march', 'in March', 'en + mois ou saison', 'les mois', 'My birthday is <b>in</b> June.', 'My birthday is ______ June. (en)', 'in'),
    ('in-2026', 'in 2026', 'en + année', 'les années', 'She was born <b>in</b> 2010.', 'She was born ______ 2010. (en)', 'in'),
    ('at-night', 'at night', 'la nuit — l\'exception à mémoriser', 'exception', 'He works <b>at</b> night.', 'He works ______ night. (la nuit)', 'at'),
    ('in-the-morning', 'in the morning', 'le matin — in + parties de la journée', 'le matin', 'I get up early <b>in</b> the morning.', 'I get up early ______ the morning. (le matin)', 'in'),
    ('on-date', 'on 14th July', 'le + date complète', 'les dates', 'The party is <b>on</b> 14th July.', 'The party is ______ 14th July. (le)', 'on'),
    ('next-no-prep', 'next Monday (sans préposition)', 'next/last/every/this — aucune préposition', 'sans préposition', 'We\'re leaving <b>next</b> Monday.', 'We\'re leaving ______ Monday. (prochain, sans préposition)', 'next'),
  ],
),

'prepositions-place': dict(
  level='a1', section='grammaire', num='Ch. 24', short='In, at, on + lieux',
  title='In, at, on avec les lieux — in Paris, at school, on the bus',
  subtitle='Choisir la bonne préposition selon le type de lieu',
  slides=[
    ('Trois prépositions pour les lieux', None,
     '<p class="slide-explanation">Tu connais déjà in/on/under pour la position des objets (chapitre 13). Ici, on s\'attaque au choix <b>in / at / on</b> avec les <b>lieux de la vie quotidienne</b> — villes, école, travail, transports.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>in</b> Paris — à Paris (à l\'intérieur d\'un espace)</p>'
     '<p style="margin-top:8px"><b>at</b> school — à l\'école (un point, un endroit-fonction)</p>'
     '<p style="margin-top:8px"><b>on</b> the bus — dans le bus (transports publics)</p></div>'
     '<p style="margin-top:16px">Le français dit « à » dans les trois cas — c\'est pourquoi ce chapitre demande de la mémorisation.</p>'),
    ('In : villes, pays, espaces fermés', None,
     '<p class="slide-explanation"><b>In</b> s\'utilise quand on est <b>à l\'intérieur</b> d\'un espace : une ville, un pays, une pièce, un bâtiment vu comme volume.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>in</b> Paris · <b>in</b> France · <b>in</b> Europe</p>'
     '<p style="margin-top:8px"><b>in</b> the kitchen (dans la cuisine) · <b>in</b> my room (dans ma chambre)</p>'
     '<p style="margin-top:8px"><b>in</b> bed (au lit) · <b>in</b> the garden (dans le jardin)</p></div>'
     '<p style="margin-top:16px">« J\'habite à Lyon » → I live IN Lyon. Les villes et pays prennent toujours in.</p>'),
    ('At : les endroits-fonctions', None,
     '<p class="slide-explanation"><b>At</b> s\'utilise pour un lieu vu comme un <b>point</b> ou une <b>fonction</b> : on y est pour faire quelque chose, peu importe l\'intérieur du bâtiment.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>at</b> school (à l\'école) · <b>at</b> work (au travail) · <b>at</b> home (à la maison)</p>'
     '<p style="margin-top:8px"><b>at</b> the station (à la gare) · <b>at</b> the airport (à l\'aéroport)</p>'
     '<p style="margin-top:8px"><b>at</b> the doctor\'s (chez le médecin) · <b>at</b> a party (à une fête)</p></div>'
     '<p style="margin-top:16px">Les trois à automatiser : <b>at home, at school, at work</b> — sans article ! (jamais « at the home »).</p>'),
    ('On : transports et surfaces', None,
     '<p class="slide-explanation"><b>On</b> s\'utilise pour les <b>transports publics</b> (le grand piège des francophones) et pour les surfaces : étages, rues dans certains cas.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>on</b> the bus · <b>on</b> the train · <b>on</b> the plane (dans l\'avion !)</p>'
     '<p style="margin-top:8px">MAIS : <b>in</b> the car, <b>in</b> a taxi (voitures = in)</p>'
     '<p style="margin-top:8px"><b>on</b> the first floor (au premier étage)</p></div>'
     '<p style="margin-top:16px">La règle des transports : debout possible (bus, train, avion) → ON · assis serré (voiture, taxi) → IN.</p>'),
    ('Go to, arrive in/at, get home', None,
     '<p class="slide-explanation">Avec les verbes de mouvement, c\'est <b>to</b> qui exprime la destination. Et home se comporte bizarrement : pas de préposition après go !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I go <b>to</b> school. — Je vais à l\'école. (mouvement → to)</p>'
     '<p style="margin-top:8px">I am <b>at</b> school. — Je suis à l\'école. (position → at)</p>'
     '<p style="margin-top:8px">I go <b>home</b>. — Je rentre à la maison. (pas de to avec home !)</p></div>'
     '<p style="margin-top:16px">Mouvement = to, position = in/at/on. Et « go home » sans préposition — une exception ultra-fréquente.</p>'),
  ],
  traps=[
    ('I live at Paris.', 'I live <strong>in</strong> Paris.', 'Les villes prennent in : I live IN Paris. At s\'utilise pour les endroits-fonctions (at school).'),
    ('She is in home.', 'She is <strong>at</strong> home.', '« À la maison » = AT home — expression fixe, sans article.'),
    ('I am in the bus.', 'I am <strong>on</strong> the bus.', 'Transports publics → ON : on the bus, on the train. (Mais in the car !)'),
    ('We go at school at 8.', 'We go <strong>to</strong> school at 8.', 'Mouvement → TO : go TO school. At exprime la position, pas la destination.'),
    ('I want to go to home.', 'I want to go <strong>home</strong>.', 'Home s\'utilise sans préposition après go : go home.'),
  ],
  summary=[
    ('IN', 'villes, pays, espaces fermés', 'in Paris / in France / in the kitchen'),
    ('AT', 'endroits-fonctions, points', 'at school / at work / at home'),
    ('ON', 'transports publics, étages', 'on the bus / on the first floor'),
    ('Exception voiture', 'in the car / in a taxi', 'She\'s in the car.'),
    ('Mouvement', 'go to + lieu', 'I go to school.'),
    ('Home', 'at home · go home (sans to)', 'I\'m at home. / I go home.'),
  ],
  ex1=('In, at ou on ?', 'Ville → in · fonction → at · transport public → on.', [
    ('My grandparents live ______ Marseille.', ['in', 'at', 'on'], 'in',
     'Ville → IN Marseille.'),
    ('Dad is ______ work until 6.', ['at', 'in', 'on'], 'at',
     'Endroit-fonction → AT work.'),
    ('I\'m ______ the train right now.', ['on', 'in', 'at'], 'on',
     'Transport public → ON the train.'),
    ('The children are ______ school.', ['at', 'on', 'in'], 'at',
     'Endroit-fonction → AT school.'),
    ('She\'s ______ the car with her mum.', ['in', 'on', 'at'], 'in',
     'Exception : voiture → IN the car.'),
    ('My flat is ______ the third floor.', ['on', 'in', 'at'], 'on',
     'Étage → ON the third floor.'),
  ]),
  ex2=('Position ou mouvement ?', 'Écris in, at, on, to — ou « X » si aucune préposition.', [
    ('« Je vais à l\'école à 8 h. » → I go ______ school at 8.', 'to',
     'Mouvement → TO school.'),
    ('« Je suis à la maison. » → I\'m ______ home.', 'at',
     'Position + home → AT home.'),
    ('« Je rentre à la maison. » → I go ______ home.', 'X',
     'Go home SANS préposition : c\'est l\'exception de home.'),
    ('« Ils habitent en Espagne. » → They live ______ Spain.', 'in',
     'Pays → IN Spain.'),
    ('« Elle est dans l\'avion. » → She\'s ______ the plane.', 'on',
     'Transport public → ON the plane (même si on est « dans » l\'avion).'),
  ]),
  ex3=('Trouve la phrase correcte', 'Attention aux expressions fixes !', [
    ('« Mon père est au travail. »', ['My father is at work.', 'My father is in work.', 'My father is at the work.'], 'My father is at work.',
     'AT work — sans article : jamais « at the work ».'),
    ('« Nous allons à Londres demain. »', ['We\'re going to London tomorrow.', 'We\'re going at London tomorrow.', 'We\'re going in London tomorrow.'], 'We\'re going to London tomorrow.',
     'Mouvement → go TO London.'),
    ('« Elle est au lit. »', ['She\'s in bed.', 'She\'s on bed.', 'She\'s at the bed.'], 'She\'s in bed.',
     'IN bed — expression fixe sans article.'),
    ('« Je rentre chez moi après l\'école. »', ['I go home after school.', 'I go to home after school.', 'I go at home after school.'], 'I go home after school.',
     'Go HOME sans préposition.'),
    ('« Il est dans le bus. »', ['He\'s on the bus.', 'He\'s in the bus.', 'He\'s at the bus.'], 'He\'s on the bus.',
     'Transport public → ON the bus.'),
  ]),
  game_desc='Chaque préposition de lieu passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('in-paris', 'in Paris', 'dans une ville ou un pays — in + lieu géographique', 'villes, pays', 'I live <b>in</b> Paris.', 'I live ______ Paris. (à)', 'in'),
    ('at-school', 'at school', 'à l\'école — at + endroit-fonction', 'fonction', 'The children are <b>at</b> school.', 'The children are ______ school. (à)', 'at'),
    ('at-home', 'at home', 'à la maison — expression fixe sans article', 'chez soi', 'I\'m <b>at</b> home tonight.', 'I\'m ______ home tonight. (à la)', 'at'),
    ('at-work', 'at work', 'au travail — at + fonction, sans article', 'au travail', 'Dad is <b>at</b> work until 6.', 'Dad is ______ work until 6. (au)', 'at'),
    ('on-the-bus', 'on the bus', 'dans le bus — on pour les transports publics', 'transports', 'I\'m <b>on</b> the bus right now.', 'I\'m ______ the bus right now. (dans)', 'on'),
    ('in-the-car', 'in the car', 'dans la voiture — l\'exception des voitures', 'voiture', 'She\'s <b>in</b> the car with her mum.', 'She\'s ______ the car with her mum. (dans)', 'in'),
    ('go-to', 'go to school', 'aller à — to pour le mouvement', 'destination', 'I go <b>to</b> school at 8.', 'I go ______ school at 8. (à, mouvement)', 'to'),
    ('go-home', 'go home (sans to)', 'rentrer à la maison — home sans préposition', 'exception home', 'I go <b>home</b> after school.', 'I go ______ after school. (à la maison)', 'home'),
  ],
),

}
