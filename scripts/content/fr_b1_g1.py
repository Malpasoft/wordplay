# -*- coding: utf-8 -*-
"""fr/ B1 grammaire — lot 1 (4 chapitres). Explications en français, anglais cible."""

CHAPTERS = {

'present-perfect': dict(
  level='b1', section='grammaire', num='Ch. 1', short='Present Perfect',
  title='Present Perfect — Ce n’est pas le passé composé',
  subtitle='Have/has + participe passé : le lien entre passé et présent',
  slides=[
    ('Le piège n°1 des francophones', None,
     '<p class="slide-explanation">Le present perfect ressemble au passé composé (<b>I have seen</b> ≈ « j’ai vu »), mais il ne s’emploie <b>pas</b> de la même façon. En anglais, dès qu’un moment précis du passé est mentionné, on utilise le <b>past simple</b> — jamais le present perfect.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>« J’ai vu Paul hier. » → <b>I saw Paul yesterday.</b> (past simple !)</p>'
     '<p style="margin-top:8px">« J’ai déjà vu ce film. » → <b>I have already seen this film.</b> (expérience, sans date)</p></div>'
     '<p style="margin-top:16px">Règle d’or : passé composé + indication de temps précise = past simple anglais.</p>'),
    ('Formation', None,
     '<p class="slide-explanation">Have/has + participe passé. Le participe des verbes réguliers se termine en <b>-ed</b> ; les irréguliers sont à mémoriser (gone, seen, done, been...).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I have finished.</b> (J’ai fini.)</p>'
     '<p style="margin-top:8px"><b>She has gone to London.</b> (Elle est partie à Londres.)</p>'
     '<p style="margin-top:8px">Négation : <b>I haven’t finished.</b> · Question : <b>Have you finished?</b></p></div>'
     '<p style="margin-top:16px">Contrairement au français, l’auxiliaire est toujours <b>have</b> — jamais be : <b>She has gone</b> (et non « she is gone »).</p>'),
    ('Emploi 1 : l’expérience de vie', None,
     '<p class="slide-explanation">Pour parler d’une expérience sans dire quand, avec <b>ever</b>, <b>never</b>, <b>before</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Have you ever been to Scotland?</b> (Es-tu déjà allé en Écosse ?)</p>'
     '<p style="margin-top:8px"><b>I have never eaten haggis.</b> (Je n’ai jamais mangé de haggis.)</p></div>'
     '<p style="margin-top:16px">Note : « déjà » dans une question = <b>ever</b> (pas already) : Have you <b>ever</b>...?</p>'),
    ('Emploi 2 : depuis — for et since', None,
     '<p class="slide-explanation">Là où le français dit « j’habite ici <b>depuis</b> dix ans » (présent !), l’anglais exige le present perfect : <b>I have lived here for ten years.</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>for</b> + durée : <b>for ten years</b> (depuis dix ans)</p>'
     '<p style="margin-top:8px"><b>since</b> + point de départ : <b>since 2015</b>, <b>since Monday</b> (depuis 2015, depuis lundi)</p>'
     '<p style="margin-top:8px"><b>How long have you known her?</b> (Depuis combien de temps la connais-tu ?)</p></div>'
     '<p style="margin-top:16px">Jamais de présent simple ici : « I live here since 2015 » est l’erreur francophone classique.</p>'),
    ('Emploi 3 : résultat présent — just, already, yet', None,
     '<p class="slide-explanation">Une action passée dont le résultat compte maintenant.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I have just finished.</b> (Je viens de finir.) — « venir de » = have just !</p>'
     '<p style="margin-top:8px"><b>She has already left.</b> (Elle est déjà partie.)</p>'
     '<p style="margin-top:8px"><b>Have you finished yet? — Not yet.</b> (Déjà fini ? — Pas encore.)</p></div>'
     '<p style="margin-top:16px"><b>yet</b> s’emploie en question et à la négative, en fin de phrase.</p>'),
  ],
  traps=[
    ('I have seen Paul yesterday.', 'I <strong>saw</strong> Paul yesterday.', 'Moment précis (yesterday) → past simple. Le passé composé français ne se traduit pas automatiquement par le present perfect.'),
    ('I live here since 2015.', 'I <strong>have lived</strong> here since 2015.', '« Depuis » + présent français = present perfect anglais, jamais le présent simple.'),
    ('She is gone to London.', 'She <strong>has</strong> gone to London.', 'L’auxiliaire est toujours have — pas de « être » comme avec les verbes de mouvement français.'),
    ('Have you already been to Rome? (question d’expérience)', 'Have you <strong>ever</strong> been to Rome?', 'Dans une question d’expérience, « déjà » = ever. Already insiste sur la rapidité, pas sur l’expérience.'),
    ('I just have finished.', 'I have <strong>just</strong> finished.', 'Just se place entre have et le participe : have just finished = « je viens de finir ».'),
  ],
  summary=[
    ('Formation', 'have/has + participe passé', 'She has gone.'),
    ('Expérience', 'ever / never / before', 'Have you ever been to...?'),
    ('Depuis (durée)', 'for + durée', 'for ten years'),
    ('Depuis (départ)', 'since + point de départ', 'since 2015'),
    ('Venir de', 'have just + participe', 'I have just finished.'),
    ('Moment précis ?', '→ past simple !', 'I saw Paul yesterday.'),
  ],
  ex1=('Present perfect ou past simple ?', 'Choisis la forme correcte — attention aux indications de temps.', [
    ('I ______ this film three times.', ['have seen', 'saw', 'see'], 'have seen',
     'Bilan d’expérience sans date précise → present perfect : have seen. « Saw » exigerait un moment précis.'),
    ('She ______ to Italy last summer.', ['went', 'has gone', 'has been'], 'went',
     'Last summer = moment précis et terminé → past simple. C’est LE cas où le passé composé français trompe.'),
    ('We ______ here since 2019.', ['have lived', 'live', 'lived'], 'have lived',
     'Since + present perfect. Le présent simple (« live ») est un calque du français « nous habitons ici depuis... ».'),
    ('______ you ever ______ sushi?', ['Have / tried', 'Did / try', 'Do / try'], 'Have / tried',
     'Question d’expérience de vie → Have you ever tried...? (As-tu déjà goûté... ?)'),
    ('He ______ his keys — he can’t open the door.', ['has lost', 'lost', 'loses'], 'has lost',
     'Le résultat compte maintenant (il ne peut pas ouvrir) → present perfect : has lost.'),
    ('They ______ the project in 2020.', ['finished', 'have finished', 'finish'], 'finished',
     'In 2020 = date précise → past simple : finished.'),
  ]),
  ex2=('Complète au present perfect', 'Écris la forme correcte du verbe entre parenthèses.', [
    ('I ______ my homework — can I watch TV? (finish)', 'have finished',
     'Résultat présent → have finished. Participe régulier en -ed.'),
    ('She ______ in Lyon for five years. (live)', 'has lived',
     'For + durée → present perfect : has lived (elle y habite depuis cinq ans... et y habite encore).'),
    ('They ______ already ______ . (leave)', 'have left',
     'Have/has + participe irrégulier : leave → left. « Ils sont déjà partis » : auxiliaire have, pas be !'),
    ('______ you ______ the new café yet? (try)', 'have tried',
     'Question avec yet → Have you tried...? (« Tu as déjà essayé...? — au sens : à ce stade »)'),
    ('I ______ never ______ to Ireland. (be)', 'have been',
     'Expérience avec never → have never been. Pour « aller » au sens d’expérience, l’anglais emploie be, pas go : I have been to Ireland.'),
  ]),
  ex3=('Depuis, déjà, venir de : traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Je viens de manger. »', ['I have just eaten.', 'I just eat.', 'I come to eat.'], 'I have just eaten.',
     '« Venir de » + infinitif = have just + participe passé — jamais « come to ».'),
    ('« Elle travaille ici depuis lundi. »', ['She has worked here since Monday.', 'She works here since Monday.', 'She worked here since Monday.'], 'She has worked here since Monday.',
     'Depuis + présent français → present perfect anglais avec since.'),
    ('« Es-tu déjà allé à Londres ? »', ['Have you ever been to London?', 'Have you already gone to London?', 'Did you ever go in London?'], 'Have you ever been to London?',
     'Expérience de vie : ever + have been to. « Gone » signifierait que tu y es encore.'),
    ('« Il n’a pas encore répondu. »', ["He hasn't answered yet.", "He hasn't yet answer.", "He didn't answer already."], "He hasn't answered yet.",
     '« Pas encore » = not... yet, avec yet en fin de phrase.'),
    ('« J’ai vu ce film hier soir. »', ['I saw this film last night.', 'I have seen this film last night.', 'I have see this film yesterday night.'], 'I saw this film last night.',
     'Last night = moment précis → past simple, même si le français dit « j’ai vu ».'),
  ]),
  game_desc='Chaque structure passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('have-seen', 'have seen', 'bilan d’expérience sans date — « j’ai (déjà) vu »', 'expérience de vie', 'I <b>have seen</b> this film three times.', 'I ______ this film three times. (j’ai vu)', 'have seen'),
    ('saw-yesterday', 'saw (+ yesterday)', 'moment précis du passé — le past simple remplace notre passé composé', 'date précise = past simple', 'I <b>saw</b> Paul yesterday.', 'I ______ Paul yesterday. (j’ai vu)', 'saw'),
    ('for', 'for + durée', 'depuis + durée (for ten years = depuis dix ans)', 'depuis (durée)', 'She has lived here <b>for</b> ten years.', 'She has lived here ______ ten years. (depuis)', 'for'),
    ('since', 'since + point de départ', 'depuis + date ou moment de départ', 'depuis (point de départ)', 'I have worked here <b>since</b> 2015.', 'I have worked here ______ 2015. (depuis)', 'since'),
    ('have-just', 'have just', 'venir de faire quelque chose', 'venir de', 'I <b>have just</b> finished.', 'I ______ ______ finished. (je viens de)', 'have just'),
    ('ever', 'ever', 'déjà — dans une question d’expérience', 'déjà (question)', 'Have you <b>ever</b> been to Scotland?', 'Have you ______ been to Scotland? (déjà)', 'ever'),
    ('yet', 'yet', 'encore / déjà — en fin de question ou de négation', 'pas encore', 'Have you finished <b>yet</b>?', 'Have you finished ______ ? (déjà, à ce stade)', 'yet'),
    ('have-been-to', 'have been to', 'être allé quelque part (expérience) — be, pas go', 'être allé (expérience)', 'I <b>have been to</b> Rome twice.', 'I have ______ to Rome twice. (suis allé)', 'been'),
  ],
),

'past-simple-continuous': dict(
  level='b1', section='grammaire', num='Ch. 2', short='Past Simple & Continuous',
  title='Past Simple & Continuous — Imparfait ou passé simple ?',
  subtitle='Was/were + -ing pour le décor, past simple pour les actions',
  slides=[
    ('La logique : décor et actions', None,
     '<p class="slide-explanation">Le <b>past continuous</b> (was/were + -ing) joue le rôle de notre <b>imparfait</b> : il plante le décor, décrit ce qui était en cours. Le <b>past simple</b> raconte les actions qui font avancer l’histoire.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I was walking home when it started to rain.</b></p>'
     '<p style="margin-top:8px">(Je rentrais à pied quand il a commencé à pleuvoir.)</p></div>'
     '<p style="margin-top:16px">« Je rentrais » (imparfait) → was walking · « il a commencé » (action) → started.</p>'),
    ('Formation du past continuous', None,
     '<p class="slide-explanation">Was/were + verbe en -ing.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I/he/she was working</b> · <b>you/we/they were working</b></p>'
     '<p style="margin-top:8px">Négation : <b>wasn’t / weren’t working</b> · Question : <b>Were you working?</b></p></div>'),
    ('When et while', None,
     '<p class="slide-explanation"><b>While</b> (pendant que) introduit l’action longue ; <b>when</b> (quand) introduit le plus souvent l’action courte qui interrompt.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>While I was cooking, the phone rang.</b> (Pendant que je cuisinais, le téléphone a sonné.)</p>'
     '<p style="margin-top:8px"><b>They were sleeping when the alarm went off.</b> (Ils dormaient quand l’alarme s’est déclenchée.)</p></div>'),
    ('Deux actions en parallèle', None,
     '<p class="slide-explanation">Deux actions longues simultanées : double past continuous, souvent avec while.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>While I was reading, she was watching TV.</b> (Pendant que je lisais, elle regardait la télé.)</p></div>'
     '<p style="margin-top:16px">Suite d’actions courtes = past simples enchaînés : <b>He came in, took off his coat and sat down.</b></p>'),
    ('Attention : verbes d’état', None,
     '<p class="slide-explanation">Les verbes d’état (know, want, like, believe, understand) ne se mettent pas en continu, même si le français utilise l’imparfait.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>« Je savais la réponse. » → <b>I knew the answer.</b> (jamais « was knowing »)</p>'
     '<p style="margin-top:8px">« Elle voulait partir. » → <b>She wanted to leave.</b></p></div>'),
  ],
  traps=[
    ('I was knowing the answer.', 'I <strong>knew</strong> the answer.', 'Know est un verbe d’état : jamais en -ing, même pour traduire un imparfait.'),
    ('When I cooked, the phone rang.', 'When I <strong>was cooking</strong>, the phone rang.', 'L’action en cours (je cuisinais) prend le past continuous — sinon on comprend deux actions successives.'),
    ('While she was reading, I was answer the phone.', 'While she was reading, I <strong>answered</strong> the phone.', 'L’action courte qui survient reste au past simple.'),
    ('They was watching TV.', 'They <strong>were</strong> watching TV.', 'Was pour I/he/she/it ; were pour you/we/they.'),
    ('Yesterday I was going to the gym, then I was doing my shopping. (récit d’actions)', 'Yesterday I <strong>went</strong> to the gym, then I <strong>did</strong> my shopping.', 'Une suite d’actions accomplies se raconte au past simple, pas au continu.'),
  ],
  summary=[
    ('Décor / en cours', 'was/were + -ing (≈ imparfait)', 'I was walking home.'),
    ('Action / événement', 'past simple (≈ passé composé)', 'It started to rain.'),
    ('Pendant que', 'while + continu', 'While I was cooking...'),
    ('Quand (interruption)', 'when + past simple', '...when the phone rang.'),
    ('Verbes d’état', 'jamais en -ing', 'I knew / wanted / understood.'),
  ],
  ex1=('Choisis la forme correcte', 'Décor en cours ou action ? Choisis la bonne option.', [
    ('I ______ TV when you called.', ['was watching', 'watched', 'am watching'], 'was watching',
     'Action en cours interrompue par « you called » → past continuous : was watching (je regardais).'),
    ('She ______ her leg while she was skiing.', ['broke', 'was breaking', 'breaks'], 'broke',
     'L’accident est l’action courte → past simple : broke.'),
    ('While they ______ , the children were playing outside.', ['were talking', 'talked', 'talk'], 'were talking',
     'Deux actions parallèles (pendant que...) → double past continuous.'),
    ('He ______ in, said hello and sat down.', ['came', 'was coming', 'comes'], 'came',
     'Suite d’actions accomplies → past simples enchaînés : came, said, sat.'),
    ('Sorry, I ______ what you meant.', ["didn't understand", "wasn't understanding", "don't understood"], "didn't understand",
     'Understand est un verbe d’état : pas de forme en -ing. Négation du past simple : didn’t + base verbale.'),
    ('What ______ you ______ at 8 p.m. last night?', ['were / doing', 'did / doing', 'were / did'], 'were / doing',
     '« Que faisais-tu à 20 h ? » : action en cours à un moment donné → were you doing.'),
  ]),
  ex2=('Écris la forme correcte', 'Mets le verbe entre parenthèses au past simple ou au past continuous.', [
    ('It ______ when we left the house. (rain)', 'was raining',
     'Il pleuvait (décor en cours) → was raining.'),
    ('I ______ my keys while I was running for the bus. (drop)', 'dropped',
     'L’action ponctuelle (j’ai fait tomber) → past simple : dropped.'),
    ('They ______ dinner when the lights went out. (have)', 'were having',
     'Ils étaient en train de dîner → were having. Ici have = prendre un repas, donc le continu est possible.'),
    ('She ______ the answer immediately. (know)', 'knew',
     'Verbe d’état → past simple : knew (irrégulier).'),
    ('While he ______ , his brother was playing video games. (study)', 'was studying',
     'Deux actions parallèles avec while → was studying.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond à la phrase française.', [
    ('« Je lisais quand il est arrivé. »', ['I was reading when he arrived.', 'I read when he was arriving.', 'I was reading when he was arriving.'], 'I was reading when he arrived.',
     'Imparfait (décor) → was reading ; passé composé (événement) → arrived.'),
    ('« Pendant que tu dormais, j’ai fait le ménage. »', ['While you were sleeping, I did the housework.', 'While you slept, I was doing the housework.', 'When you were sleeping, I was doing the housework.'], 'While you were sleeping, I did the housework.',
     'While + action longue (were sleeping), action accomplie au past simple (did).'),
    ('« Ils regardaient la télé toute la soirée. »', ['They were watching TV all evening.', 'They watched TV all the evening while.', 'They were watch TV all evening.'], 'They were watching TV all evening.',
     'Activité en cours sur la durée → past continuous : were watching.'),
    ('« Elle a ouvert la porte, a souri et est entrée. »', ['She opened the door, smiled and came in.', 'She was opening the door, smiling and coming in.', 'She opened the door, was smiling and came in.'], 'She opened the door, smiled and came in.',
     'Suite d’actions du récit → past simples enchaînés.'),
    ('« Je voulais te demander quelque chose. »', ['I wanted to ask you something.', 'I was wanting to ask you something.', 'I want asked you something.'], 'I wanted to ask you something.',
     'Want est un verbe d’état : wanted, jamais « was wanting ».'),
  ]),
  game_desc='Chaque structure passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('was-walking', 'was walking', 'action en cours dans le passé — notre imparfait « je marchais »', 'décor en cours', 'I <b>was walking</b> home when it started to rain.', 'I ______ home when it started to rain. (je rentrais)', 'was walking'),
    ('started', 'started', 'action ponctuelle qui survient — past simple', 'événement du récit', 'It <b>started</b> to rain suddenly.', 'It ______ to rain suddenly. (a commencé)', 'started'),
    ('while', 'while', 'pendant que — introduit l’action longue', 'pendant que', '<b>While</b> I was cooking, the phone rang.', '______ I was cooking, the phone rang. (pendant que)', 'while'),
    ('when', 'when', 'quand — introduit souvent l’action courte', 'quand', 'They were sleeping <b>when</b> the alarm went off.', 'They were sleeping ______ the alarm went off. (quand)', 'when'),
    ('were-having', 'were having', 'étaient en train de — continu pluriel', 'en train de (pluriel)', 'They <b>were having</b> dinner at nine.', 'They ______ dinner at nine. (étaient en train de dîner)', 'were having'),
    ('knew', 'knew', 'verbe d’état au past simple — jamais en -ing', 'verbe d’état', 'I <b>knew</b> the answer.', 'I ______ the answer. (je savais)', 'knew'),
    ('was-doing', 'What were you doing?', 'que faisais-tu — question au continu', 'question au continu', 'What <b>were you doing</b> at 8 p.m.?', 'What ______ you ______ at 8 p.m.? (faisais)', 'were doing'),
    ('went-off', 'went off', 'sonner / se déclencher (alarme) — phrasal verb du récit', 'alarme', 'The alarm <b>went off</b> at six.', 'The alarm ______ ______ at six. (s’est déclenchée)', 'went off'),
  ],
),

'future-forms': dict(
  level='b1', section='grammaire', num='Ch. 5', short='Future Forms',
  title='Future Forms — Will, going to ou présent continu ?',
  subtitle='Trois futurs anglais pour un futur français',
  slides=[
    ('Trois outils pour le futur', None,
     '<p class="slide-explanation">Le français se contente souvent du futur simple ou du futur proche. L’anglais choisit selon le <b>type</b> de futur : décision spontanée, intention, ou rendez-vous fixé.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>will</b> + base verbale → décision prise à l’instant, prédiction</p>'
     '<p style="margin-top:8px"><b>be going to</b> + base verbale → intention, projet déjà décidé</p>'
     '<p style="margin-top:8px"><b>présent continu</b> → arrangement fixé (agenda, billets achetés)</p></div>'),
    ('Will : décision spontanée et prédiction', None,
     '<p class="slide-explanation"><b>Will</b> exprime une décision prise au moment où l’on parle, une promesse ou une prédiction d’opinion.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I’ll get the door!</b> (J’y vais !) — décision instantanée</p>'
     '<p style="margin-top:8px"><b>I think it will rain tomorrow.</b> (Je pense qu’il pleuvra demain.)</p></div>'
     '<p style="margin-top:16px">Jamais de « to » après will : <b>I will call you</b> (et non « will to call »).</p>'),
    ('Going to : intention et signes visibles', None,
     '<p class="slide-explanation"><b>Be going to</b> ≈ notre futur proche « aller faire ». Intention déjà décidée, ou prédiction fondée sur ce qu’on voit.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>We’re going to visit Rome in May.</b> (Nous allons visiter Rome en mai.) — projet</p>'
     '<p style="margin-top:8px"><b>Look at those clouds! It’s going to rain.</b> (Regarde ces nuages ! Il va pleuvoir.) — signe visible</p></div>'),
    ('Présent continu : l’agenda', None,
     '<p class="slide-explanation">Pour un arrangement déjà organisé (heure, lieu, personnes), l’anglais emploie le <b>présent continu</b> — très déroutant pour un francophone.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I’m seeing the dentist tomorrow at 10.</b> (Je vois le dentiste demain à 10 h.)</p>'
     '<p style="margin-top:8px"><b>We’re flying to Dublin on Friday.</b> (Nous partons pour Dublin vendredi — billets achetés.)</p></div>'),
    ('Après when, if, as soon as : présent !', None,
     '<p class="slide-explanation">Comme en français avec « si », mais aussi avec <b>when</b> : pas de will dans la subordonnée de temps.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I’ll call you when I arrive.</b> (Je t’appellerai quand j’arriverai.)</p>'
     '<p style="margin-top:8px">⚠ Le français dit « quand j’arriver<b>ai</b> » (futur), l’anglais dit <b>when I arrive</b> (présent) !</p></div>'),
  ],
  traps=[
    ('I will to call you later.', 'I will <strong>call</strong> you later.', 'Will est un modal : jamais de to après lui.'),
    ('I’ll call you when I will arrive.', 'I’ll call you when I <strong>arrive</strong>.', 'Après when/as soon as, l’anglais emploie le présent — contrairement au futur français « quand j’arriverai ».'),
    ('Look at those clouds! It will rain.', 'It <strong>is going to</strong> rain.', 'Prédiction fondée sur un signe visible → going to, pas will.'),
    ('We will visit Rome in May. (projet déjà décidé)', 'We <strong>are going to</strong> visit Rome in May.', 'Une intention déjà décidée s’exprime avec going to (ou le présent continu si tout est réservé).'),
    ('I see the dentist tomorrow at 10. (rendez-vous noté)', 'I <strong>am seeing</strong> the dentist tomorrow at 10.', 'Un arrangement fixé prend le présent continu, pas le présent simple.'),
  ],
  summary=[
    ('Décision spontanée', 'will + base verbale', 'I’ll get the door!'),
    ('Prédiction (opinion)', 'I think... will', 'I think it will rain.'),
    ('Intention / projet', 'be going to + base', 'We’re going to visit Rome.'),
    ('Signe visible', 'be going to', 'It’s going to rain.'),
    ('Arrangement fixé', 'présent continu', 'I’m seeing the dentist at 10.'),
    ('Après when / if', 'présent (pas will !)', 'when I arrive'),
  ],
  ex1=('Will, going to ou présent continu ?', 'Choisis la forme la plus naturelle.', [
    ('The phone’s ringing! — I ______ it.', ["'ll get", "'m going to get", 'get'], "'ll get",
     'Décision prise à l’instant → will : I’ll get it.'),
    ('We ______ married in June — everything is booked.', ['are getting', 'will get', 'get'], 'are getting',
     'Tout est réservé = arrangement fixé → présent continu : we’re getting married.'),
    ('Watch out! You ______ that glass.', ['are going to drop', 'will drop', 'drop'], 'are going to drop',
     'Signe visible (le verre penche déjà) → going to.'),
    ('I promise I ______ you every day.', ["'ll text", "'m texting", 'text'], "'ll text",
     'Promesse → will : I’ll text you.'),
    ('She ______ start a new job next month — she signed yesterday.', ['is going to', 'will', 'would'], 'is going to',
     'Décision déjà prise (elle a signé) → going to.'),
    ('I’ll email you as soon as I ______ the results.', ['get', 'will get', 'got'], 'get',
     'Après as soon as → présent, même si le sens est futur.'),
  ]),
  ex2=('Complète la phrase', 'Écris la forme demandée entre parenthèses.', [
    ('Don’t worry, I ______ you with the boxes. (will + help)', 'will help',
     'Offre spontanée d’aide → will help (sans to).'),
    ('Look at the sky — it ______ rain. (going to)', 'is going to',
     'Signe visible → it is going to rain.'),
    ('We ______ to Dublin on Friday — the tickets are booked. (fly, présent continu)', 'are flying',
     'Arrangement réservé → présent continu : are flying.'),
    ('I’ll call you when I ______ home. (get)', 'get',
     'Subordonnée de temps → présent simple : when I get home.'),
    ('They ______ probably ______ the match. (will + win)', 'will win',
     'Prédiction d’opinion (avec probably) → will win.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Je vais visiter Rome en mai. » (projet)', ["I'm going to visit Rome in May.", 'I will to visit Rome in May.', 'I visit Rome in May.'], "I'm going to visit Rome in May.",
     'Futur proche français (intention) → be going to.'),
    ('« Je t’appellerai quand j’arriverai. »', ["I'll call you when I arrive.", "I'll call you when I'll arrive.", 'I call you when I arrive.'], "I'll call you when I arrive.",
     'Will dans la principale, présent dans la subordonnée de temps — le double futur français ne se traduit pas.'),
    ('« Il va pleuvoir, regarde ces nuages. »', ["It's going to rain — look at those clouds.", 'It will rain — look at those clouds.', 'It rains — look at those clouds.'], "It's going to rain — look at those clouds.",
     'Prédiction sur indice visible → going to.'),
    ('« Je vois le médecin demain matin. » (rendez-vous pris)', ["I'm seeing the doctor tomorrow morning.", 'I will see the doctor tomorrow morning.', 'I see the doctor tomorrow morning.'], "I'm seeing the doctor tomorrow morning.",
     'Rendez-vous dans l’agenda → présent continu.'),
    ('« D’accord, je prends celui-là. » (décision à la caisse)', ["OK, I'll take this one.", "OK, I'm going to take this one.", 'OK, I take this one.'], "OK, I'll take this one.",
     'Décision prise sur le moment → will : I’ll take this one.'),
  ]),
  game_desc='Chaque forme du futur passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('will-spontaneous', "I'll + base verbale", 'décision prise à l’instant même', 'décision spontanée', "The phone's ringing — <b>I'll get</b> it!", "The phone's ringing — I'll ______ it! (décrocher)", 'get'),
    ('will-promise', 'will (promesse)', 'promesse ou engagement', 'promesse', 'I promise I <b>will help</b> you.', 'I promise I ______ help you.', 'will'),
    ('going-to-plan', 'be going to (projet)', 'intention déjà décidée — notre futur proche', 'intention', "We <b>are going to</b> visit Rome in May.", 'We are ______ to visit Rome in May.', 'going'),
    ('going-to-sign', 'be going to (signe)', 'prédiction fondée sur ce qu’on voit', 'signe visible', "Look at those clouds — it <b>is going to</b> rain.", 'Look at those clouds — it is ______ to rain.', 'going'),
    ('present-cont', 'présent continu (agenda)', 'arrangement fixé : heure, lieu, réservation', 'rendez-vous fixé', "I<b>'m seeing</b> the dentist tomorrow at 10.", "I'm ______ the dentist tomorrow at 10. (je vois)", 'seeing'),
    ('when-present', 'when + présent', 'pas de will après when — contrairement au français', 'subordonnée de temps', "I'll call you when I <b>arrive</b>.", "I'll call you when I ______ . (arriverai)", 'arrive'),
    ('no-to', 'will + base (sans to)', 'will n’est jamais suivi de to', 'modal sans to', 'I will <b>call</b> you later.', 'I will ______ you later. (appeler)', 'call'),
    ('wont', "won't", 'forme négative de will — refus ou prédiction négative', 'négation de will', 'He <b>won’t</b> be happy about this.', 'He ______ be happy about this. (ne sera pas)', "won't"),
  ],
),

'zero-first-conditional': dict(
  level='b1', section='grammaire', num='Ch. 6', short='Zero & First Conditional',
  title='Zero & First Conditional — Si + présent',
  subtitle='Vérités générales et futurs possibles avec if',
  slides=[
    ('Bonne nouvelle : comme en français', None,
     '<p class="slide-explanation">Après <b>si</b>, le français refuse le futur (« si j’aurai » est impossible). L’anglais fait exactement pareil : après <b>if</b>, jamais de will.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>If it rains, we’ll stay at home.</b> (S’il pleut, nous resterons à la maison.)</p></div>'
     '<p style="margin-top:16px">if + présent → conséquence avec will : c’est le <b>first conditional</b>.</p>'),
    ('Zero conditional : vérités générales', None,
     '<p class="slide-explanation">Pour une vérité générale ou une habitude, présent des deux côtés.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>If you heat water, it boils.</b> (Si on chauffe l’eau, elle bout.)</p>'
     '<p style="margin-top:8px"><b>If I drink coffee at night, I can’t sleep.</b></p></div>'
     '<p style="margin-top:16px">Ici if peut se remplacer par when : <b>When you heat water, it boils.</b></p>'),
    ('First conditional : futur possible', None,
     '<p class="slide-explanation">Pour une situation future réaliste : if + présent, will dans la principale.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>If you study, you’ll pass the exam.</b> (Si tu révises, tu réussiras.)</p>'
     '<p style="margin-top:8px"><b>She won’t come if it snows.</b> (Elle ne viendra pas s’il neige.)</p></div>'
     '<p style="margin-top:16px">L’ordre des deux moitiés est libre ; la virgule n’apparaît que si if ouvre la phrase.</p>'),
    ('Variantes utiles : unless, as long as', None,
     '<p class="slide-explanation"><b>Unless</b> = if... not (à moins que). <b>As long as</b> = à condition que. Les deux suivent la même règle : présent, pas de will.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Unless you hurry, you’ll miss the train.</b> (À moins de te dépêcher, tu vas rater le train.)</p>'
     '<p style="margin-top:8px"><b>You can borrow it as long as you return it.</b> (Tu peux l’emprunter à condition de le rendre.)</p></div>'),
    ('Impératif et modaux dans la principale', None,
     '<p class="slide-explanation">La principale n’est pas limitée à will : impératif, can, must, should y sont fréquents.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>If you see Anna, tell her to call me.</b> (Si tu vois Anna, dis-lui de m’appeler.)</p>'
     '<p style="margin-top:8px"><b>If it hurts, you should see a doctor.</b></p></div>'),
  ],
  traps=[
    ('If it will rain, we will stay at home.', 'If it <strong>rains</strong>, we will stay at home.', 'Jamais de will après if — exactement comme « si » ne prend pas le futur en français.'),
    ('If you will heat water, it boils.', 'If you <strong>heat</strong> water, it boils.', 'Vérité générale : présent des deux côtés (zero conditional).'),
    ('Unless you don’t hurry, you’ll miss the train.', '<strong>Unless you hurry</strong>, you’ll miss the train.', 'Unless contient déjà la négation (= if... not) : pas de double négation.'),
    ('If you study you,’ll pass. (virgule au milieu)', 'If you study<strong>,</strong> you’ll pass.', 'La virgule sépare les deux moitiés quand if ouvre la phrase ; pas de virgule si if est en deuxième position.'),
    ('If I’ll see her, I’ll tell her.', 'If I <strong>see</strong> her, I’ll tell her.', 'Le will reste dans la principale ; la condition reste au présent.'),
  ],
  summary=[
    ('Vérité générale', 'if + présent, présent', 'If you heat water, it boils.'),
    ('Futur possible', 'if + présent, will', 'If you study, you’ll pass.'),
    ('À moins que', 'unless + présent', 'Unless you hurry...'),
    ('À condition que', 'as long as + présent', 'as long as you return it'),
    ('Avec impératif', 'if..., + impératif', 'If you see Anna, tell her.'),
  ],
  ex1=('Choisis la forme correcte', 'Zero ou first conditional ? Attention à la place de will.', [
    ('If it ______ tomorrow, we’ll cancel the picnic.', ['rains', 'will rain', 'rained'], 'rains',
     'Après if : présent. Le will reste dans la principale (we’ll cancel).'),
    ('If you ______ ice, it melts.', ['heat', 'will heat', 'heated'], 'heat',
     'Vérité générale → zero conditional : présent + présent.'),
    ('You ______ the train unless you leave now.', ['will miss', 'miss', 'would miss'], 'will miss',
     'La conséquence future prend will : you will miss the train.'),
    ('If she calls, ______ her I’m busy.', ['tell', 'you will tell', 'telling'], 'tell',
     'Impératif dans la principale : tell her (dis-lui).'),
    ('______ you water plants, they die.', ['Unless', 'If', 'As long as'], 'Unless',
     '« À moins d’arroser les plantes, elles meurent » : unless = if... not.'),
    ('If I ______ time, I’ll help you tonight.', ['have', 'will have', 'had'], 'have',
     'Condition au présent : if I have time. « Had » basculerait dans le second conditional (irréel).'),
  ]),
  ex2=('Complète la phrase', 'Écris le verbe entre parenthèses à la forme correcte.', [
    ('If you ______ , you’ll feel better. (rest)', 'rest',
     'Après if → présent simple : if you rest.'),
    ('If you mix blue and yellow, you ______ green. (get)', 'get',
     'Vérité générale → présent : you get green.'),
    ('She ______ angry if you forget her birthday. (will + be)', 'will be',
     'Conséquence future → will be angry.'),
    ('Unless we ______ now, we’ll be late. (leave)', 'leave',
     'Unless + présent : unless we leave now.'),
    ('If it ______ , the match will be cancelled. (snow)', 'snows',
     'Présent après if, 3e personne : snows.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« S’il pleut, nous resterons ici. »', ['If it rains, we’ll stay here.', 'If it will rain, we’ll stay here.', 'If it rained, we’ll stay here.'], 'If it rains, we’ll stay here.',
     'Si + présent → if + présent ; le futur français (resterons) → will stay.'),
    ('« Si on chauffe l’eau, elle bout. »', ['If you heat water, it boils.', 'If you heat water, it will boils.', 'If you will heat water, it boils.'], 'If you heat water, it boils.',
     'Vérité générale → zero conditional, présent des deux côtés.'),
    ('« À moins que tu partes maintenant, tu seras en retard. »', ['Unless you leave now, you’ll be late.', 'Unless you don’t leave now, you’ll be late.', 'If you leave now, you’ll be late.'], 'Unless you leave now, you’ll be late.',
     'Unless = à moins que, sans négation supplémentaire.'),
    ('« Si tu vois Marc, dis-lui bonjour. »', ['If you see Marc, say hello to him.', 'If you will see Marc, say hello to him.', 'If you saw Marc, say hello to him.'], 'If you see Marc, say hello to him.',
     'If + présent, impératif dans la principale.'),
    ('« Tu peux venir à condition d’être à l’heure. »', ['You can come as long as you are on time.', 'You can come unless you are on time.', 'You can come if you will be on time.'], 'You can come as long as you are on time.',
     'À condition que = as long as + présent.'),
  ]),
  game_desc='Chaque structure conditionnelle passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('if-present', 'if + présent', 'la condition reste au présent — jamais de will après if', 'condition au présent', '<b>If it rains</b>, we’ll stay at home.', 'If it ______ , we’ll stay at home. (pleut)', 'rains'),
    ('will-main', 'will (principale)', 'la conséquence future prend will', 'conséquence future', 'If you study, you <b>will pass</b>.', 'If you study, you ______ pass.', 'will'),
    ('zero-cond', 'zero conditional', 'vérité générale : présent + présent', 'vérité générale', 'If you heat water, it <b>boils</b>.', 'If you heat water, it ______ . (bout)', 'boils'),
    ('unless', 'unless', 'à moins que — contient déjà la négation', 'à moins que', '<b>Unless</b> you hurry, you’ll miss the train.', '______ you hurry, you’ll miss the train. (à moins que)', 'unless'),
    ('as-long-as', 'as long as', 'à condition que', 'à condition que', 'You can borrow it <b>as long as</b> you return it.', 'You can borrow it as ______ as you return it.', 'long'),
    ('imperative', 'if + impératif', 'si..., fais... — impératif dans la principale', 'avec impératif', 'If you see Anna, <b>tell</b> her to call me.', 'If you see Anna, ______ her to call me. (dis)', 'tell'),
    ('wont-if', 'won’t ... if', 'négation de la conséquence', 'conséquence négative', 'She <b>won’t</b> come if it snows.', 'She ______ come if it snows. (ne viendra pas)', "won't"),
    ('when-boils', 'when (vérité)', 'dans le zero conditional, if ≈ when', 'if = when', '<b>When</b> you heat water, it boils.', '______ you heat water, it boils. (quand)', 'when'),
  ],
),
}
