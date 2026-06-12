# -*- coding: utf-8 -*-
"""fr/ A2 grammaire — lot 1 (chapitres 1-5). Explications en français, anglais cible."""

CHAPTERS = {

'past-simple': dict(
  level='a2', section='grammaire', num='Ch. 1', short='Le past simple',
  title='Le past simple — I worked, she went',
  subtitle='Réviser le passé anglais : réguliers, irréguliers, was/were et did',
  slides=[
    ('Un seul passé pour raconter', None,
     '<p class="slide-explanation">Le <b>past simple</b> raconte les actions terminées du passé. Il traduit à la fois notre passé composé (« j\'ai travaillé ») et notre passé simple — un seul temps anglais pour les deux !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>worked</b> yesterday. — J\'ai travaillé hier.</p>'
     '<p style="margin-top:8px">She <b>visited</b> her grandmother last week. — Elle a rendu visite à sa grand-mère la semaine dernière.</p>'
     '<p style="margin-top:8px">They <b>played</b> football on Saturday. — Ils ont joué au foot samedi.</p></div>'
     '<p style="margin-top:16px">Verbes réguliers : base verbale + <b>-ed</b>. Et bonne nouvelle : la forme est la même pour toutes les personnes !</p>'),
    ('Les verbes irréguliers : à mémoriser', None,
     '<p class="slide-explanation">Les verbes les plus fréquents sont <b>irréguliers</b> : leur forme passée ne prend pas -ed et doit s\'apprendre par cœur. Voici les indispensables du niveau A2.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>go → <b>went</b> &nbsp;·&nbsp; see → <b>saw</b> &nbsp;·&nbsp; have → <b>had</b> &nbsp;·&nbsp; do → <b>did</b></p>'
     '<p style="margin-top:8px">come → <b>came</b> &nbsp;·&nbsp; take → <b>took</b> &nbsp;·&nbsp; buy → <b>bought</b> &nbsp;·&nbsp; eat → <b>ate</b></p>'
     '<p style="margin-top:8px">We <b>went</b> to London last summer. — Nous sommes allés à Londres l\'été dernier.</p></div>'
     '<p style="margin-top:16px">Astuce : apprends-les par petits groupes de cinq, avec une phrase exemple pour chacun.</p>'),
    ('Was et were : le passé de be', None,
     '<p class="slide-explanation">Le verbe <b>be</b> a deux formes au passé : <b>was</b> (I, he, she, it) et <b>were</b> (you, we, they). C\'est le seul verbe qui change selon la personne au past simple.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>was</b> tired last night. — J\'étais fatigué hier soir.</p>'
     '<p style="margin-top:8px">They <b>were</b> at the cinema. — Ils étaient au cinéma.</p>'
     '<p style="margin-top:8px">Négation : <b>wasn\'t / weren\'t</b> · Question : <b>Were you</b> at home? — Étais-tu chez toi ?</p></div>'
     '<p style="margin-top:16px">Be n\'utilise jamais did : la négation et la question se font directement avec was/were.</p>'),
    ('La négation et la question : did', None,
     '<p class="slide-explanation">Pour les autres verbes, la négation et la question utilisent l\'auxiliaire <b>did</b> — et le verbe principal revient à la <b>base verbale</b>. Le passé est déjà marqué par did !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>didn\'t see</b> the film. — Je n\'ai pas vu le film. (et non « didn\'t saw »)</p>'
     '<p style="margin-top:8px"><b>Did you go</b> to the party? — Es-tu allé à la fête ?</p>'
     '<p style="margin-top:8px">Réponses courtes : <b>Yes, I did.</b> / <b>No, I didn\'t.</b></p></div>'
     '<p style="margin-top:16px">Règle d\'or : <b>une seule marque de passé par phrase</b>. Si did est là, le verbe reste nu.</p>'),
    ('Les expressions de temps du passé', None,
     '<p class="slide-explanation">Le past simple s\'accompagne d\'expressions qui situent l\'action à un <b>moment précis et terminé</b>. Repère-les : elles t\'indiquent le bon temps.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>yesterday</b> (hier) &nbsp;·&nbsp; <b>last night</b> (hier soir) &nbsp;·&nbsp; <b>last week</b> (la semaine dernière)</p>'
     '<p style="margin-top:8px"><b>two years ago</b> (il y a deux ans) &nbsp;·&nbsp; <b>in 2020</b> (en 2020)</p>'
     '<p style="margin-top:8px">I <b>met</b> her <b>three days ago</b>. — Je l\'ai rencontrée il y a trois jours.</p></div>'
     '<p style="margin-top:16px">Attention au calque : « il y a deux ans » = two years <b>ago</b> (ago se place APRÈS la durée), jamais « there is two years ».</p>'),
  ],
  traps=[
    ('I didn\'t went to school.', 'I didn\'t <strong>go</strong> to school.', 'Une seule marque de passé : did porte déjà le passé, le verbe reste à la base : didn\'t GO.'),
    ('Did you saw the film?', 'Did you <strong>see</strong> the film?', 'Après did, base verbale : Did you SEE...? Le passé est déjà sur did.'),
    ('They was at the beach.', 'They <strong>were</strong> at the beach.', 'Was pour I/he/she/it ; were pour you/we/they : they WERE.'),
    ('I have seen Paul yesterday.', 'I <strong>saw</strong> Paul yesterday.', 'Moment précis (yesterday) → past simple, jamais have + participe. Le passé composé français ne se copie pas.'),
    ('I met her there is two years.', 'I met her <strong>two years ago</strong>.', '« Il y a + durée » = durée + AGO : two years ago. Jamais « there is » pour le temps.'),
  ],
  summary=[
    ('Réguliers', 'base verbale + -ed', 'I worked. / She visited her friend.'),
    ('Irréguliers', 'forme à mémoriser', 'go → went · see → saw · buy → bought'),
    ('Be au passé', 'was (I/he/she/it) · were (you/we/they)', 'I was tired. / They were late.'),
    ('Négation', 'didn\'t + base verbale', 'I didn\'t see the film.'),
    ('Question', 'Did + sujet + base verbale?', 'Did you go to the party?'),
    ('Expressions', 'yesterday · last week · ... ago', 'I met her two years ago.'),
  ],
  ex1=('Mets le verbe au past simple', 'Régulier, irrégulier ou was/were ?', [
    ('Last summer we ______ to Spain.', ['went', 'goed', 'go'], 'went',
     'Go est irrégulier : go → WENT. « Goed » n\'existe pas.'),
    ('She ______ a new dress yesterday.', ['bought', 'buyed', 'buys'], 'bought',
     'Buy est irrégulier : buy → BOUGHT.'),
    ('I ______ very tired last night.', ['was', 'were', 'did be'], 'was',
     'Be au passé avec I → WAS. Be n\'utilise jamais did.'),
    ('They ______ TV all evening.', ['watched', 'watch', 'were watch'], 'watched',
     'Watch est régulier : watch + -ED = watched.'),
    ('We ______ at school on Sunday.', ['weren\'t', 'wasn\'t', 'didn\'t be'], 'weren\'t',
     'We → WERE, donc la négation est WEREN\'T.'),
    ('He ______ his keys this morning.', ['lost', 'losed', 'loses'], 'lost',
     'Lose est irrégulier : lose → LOST.'),
  ]),
  ex2=('Négation et question avec did', 'Écris le mot manquant.', [
    ('« Je n\'ai pas vu ce film. » → I ______ see that film. (un mot)', 'didn\'t',
     'Négation du past simple : DIDN\'T + base verbale : didn\'t SEE.'),
    ('« Es-tu allé à la fête ? » → ______ you go to the party? (un mot)', 'Did',
     'Question au passé : DID + sujet + base verbale.'),
    ('« Elle est allée à Londres. » → She ______ to London. (un mot)', 'went',
     'Go est irrégulier : she WENT to London.'),
    ('« Étais-tu chez toi ? » → ______ you at home? (un mot)', 'Were',
     'Be n\'utilise pas did : WERE you at home?'),
    ('« Oui, je l\'ai fait. » (réponse à Did you do it?) → Yes, I ______. (un mot)', 'did',
     'Réponse courte : on reprend l\'auxiliaire → Yes, I DID.'),
  ]),
  ex3=('Trouve la phrase correcte', 'Une seule marque de passé par phrase !', [
    ('« Je n\'ai pas mangé ce matin. »', ['I didn\'t eat this morning.', 'I didn\'t ate this morning.', 'I don\'t ate this morning.'], 'I didn\'t eat this morning.',
     'Didn\'t + base verbale EAT — le passé est déjà sur didn\'t.'),
    ('« As-tu acheté le pain ? »', ['Did you buy the bread?', 'Did you bought the bread?', 'Bought you the bread?'], 'Did you buy the bread?',
     'Did + sujet + BUY (base verbale).'),
    ('« Ils étaient en retard hier. »', ['They were late yesterday.', 'They was late yesterday.', 'They did be late yesterday.'], 'They were late yesterday.',
     'They → WERE. Be ne se conjugue jamais avec did.'),
    ('« J\'ai vu Marie il y a deux jours. »', ['I saw Marie two days ago.', 'I have seen Marie two days ago.', 'I saw Marie there is two days.'], 'I saw Marie two days ago.',
     'Moment précis → past simple SAW ; « il y a » = AGO après la durée.'),
    ('« Nous avons pris le bus. »', ['We took the bus.', 'We taked the bus.', 'We were take the bus.'], 'We took the bus.',
     'Take est irrégulier : take → TOOK.'),
  ]),
  game_desc='Chaque forme du past simple passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('worked', 'worked', 'verbe régulier — base + -ed', 'régulier', 'I <b>worked</b> late yesterday.', 'I ______ late yesterday. (j\'ai travaillé)', 'worked'),
    ('went', 'went', 'go au passé — irrégulier à mémoriser', 'irrégulier', 'We <b>went</b> to London last summer.', 'We ______ to London last summer. (sommes allés)', 'went'),
    ('saw', 'saw', 'see au passé — irrégulier', 'irrégulier', 'I <b>saw</b> a great film last night.', 'I ______ a great film last night. (ai vu)', 'saw'),
    ('was', 'was', 'be au passé — I/he/she/it', 'étais / était', 'I <b>was</b> very tired last night.', 'I ______ very tired last night. (étais)', 'was'),
    ('were', 'were', 'be au passé — you/we/they', 'étions / étaient', 'They <b>were</b> at the cinema.', 'They ______ at the cinema. (étaient)', 'were'),
    ('didnt', 'didn\'t + base verbale', 'négation du passé — le verbe reste nu', 'négation', 'I <b>didn\'t</b> see the film.', 'I ______ see the film. (négation)', 'didn\'t'),
    ('did-you', 'Did you...?', 'question au passé — did + sujet + base verbale', 'question', '<b>Did</b> you go to the party?', '______ you go to the party? (auxiliaire)', 'did'),
    ('ago', 'two years ago', 'il y a + durée — ago se place après', 'il y a', 'I met her two years <b>ago</b>.', 'I met her two years ______. (il y a)', 'ago'),
  ],
),

'past-continuous': dict(
  level='a2', section='grammaire', num='Ch. 2', short='Le past continuous',
  title='Le past continuous — I was working',
  subtitle='L\'action en cours dans le passé, le cousin de notre imparfait',
  slides=[
    ('Une action en cours dans le passé', None,
     '<p class="slide-explanation">Le <b>past continuous</b> décrit une action qui était <b>en train de se dérouler</b> à un moment du passé. Il correspond souvent à notre <b>imparfait</b> : « je travaillais », « il pleuvait ».</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>was working</b> at eight o\'clock. — Je travaillais à huit heures.</p>'
     '<p style="margin-top:8px">It <b>was raining</b> all morning. — Il pleuvait toute la matinée.</p>'
     '<p style="margin-top:8px">They <b>were sleeping</b> when I arrived. — Ils dormaient quand je suis arrivé.</p></div>'
     '<p style="margin-top:16px">Formation : <b>was/were + verbe-ing</b>. Les deux morceaux sont obligatoires.</p>'),
    ('Was ou were + -ing', None,
     '<p class="slide-explanation">Comme au présent continuous, l\'auxiliaire be se conjugue : <b>was</b> avec I/he/she/it, <b>were</b> avec you/we/they. Le verbe principal prend <b>-ing</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I/he/she <b>was eating</b> &nbsp;·&nbsp; you/we/they <b>were eating</b></p>'
     '<p style="margin-top:8px">Négation : she <b>wasn\'t listening</b> — elle n\'écoutait pas.</p>'
     '<p style="margin-top:8px">Question : <b>Were you sleeping?</b> — Tu dormais ?</p></div>'
     '<p style="margin-top:16px">Pas de did ici : l\'auxiliaire be fait la négation et la question tout seul.</p>'),
    ('Décor en cours + action soudaine', None,
     '<p class="slide-explanation">Le duo classique du récit : le past continuous plante le <b>décor</b> (action longue), le past simple raconte l\'<b>événement</b> qui survient. Exactement comme imparfait + passé composé en français.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>was watching</b> TV when the phone <b>rang</b>. — Je regardais la télé quand le téléphone a sonné.</p>'
     '<p style="margin-top:8px">She <b>was walking</b> home when she <b>saw</b> the accident. — Elle rentrait à pied quand elle a vu l\'accident.</p></div>'
     '<p style="margin-top:16px">Action longue → was/were + -ing · action courte → past simple. Le parallèle avec le français marche très bien ici !</p>'),
    ('When et while', None,
     '<p class="slide-explanation"><b>While</b> (pendant que) introduit l\'action longue au continuous ; <b>when</b> (quand) introduit le plus souvent l\'action courte au past simple.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>While</b> I was cooking, the phone rang. — Pendant que je cuisinais, le téléphone a sonné.</p>'
     '<p style="margin-top:8px">They were playing <b>when</b> it started to rain. — Ils jouaient quand il a commencé à pleuvoir.</p>'
     '<p style="margin-top:8px"><b>While</b> I was reading, she <b>was watching</b> TV. — Deux actions parallèles : double continuous.</p></div>'
     '<p style="margin-top:16px">Astuce : while + action longue (-ing) · when + action courte (past simple).</p>'),
    ('Les verbes d\'état restent au simple', None,
     '<p class="slide-explanation">Comme au présent, les verbes d\'état (<b>know, want, like, need, understand</b>) refusent le -ing — même quand le français utilise l\'imparfait.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>« Je savais la réponse. » → I <b>knew</b> the answer. (jamais « was knowing »)</p>'
     '<p style="margin-top:8px">« Elle voulait partir. » → She <b>wanted</b> to leave.</p>'
     '<p style="margin-top:8px">« Nous aimions ce restaurant. » → We <b>liked</b> that restaurant.</p></div>'
     '<p style="margin-top:16px">Imparfait français ne veut PAS toujours dire past continuous : vérifie d\'abord que le verbe accepte le -ing.</p>'),
  ],
  traps=[
    ('I watching TV when you called.', 'I <strong>was watching</strong> TV when you called.', 'Le past continuous a deux parties : was/were + -ing. Sans was, la phrase est incorrecte.'),
    ('They was playing football.', 'They <strong>were</strong> playing football.', 'Was pour I/he/she/it ; were pour you/we/they : they WERE playing.'),
    ('I was knowing the answer.', 'I <strong>knew</strong> the answer.', 'Know est un verbe d\'état : jamais en -ing, même pour traduire un imparfait.'),
    ('While I cooked, the phone rang.', 'While I <strong>was cooking</strong>, the phone rang.', 'Après while, l\'action longue prend le continuous : while I WAS COOKING.'),
    ('Did you sleeping at ten?', '<strong>Were you sleeping</strong> at ten?', 'La question du continuous utilise be, pas did : WERE you sleeping?'),
  ],
  summary=[
    ('Formation', 'was/were + verbe-ing', 'I was working. / They were sleeping.'),
    ('Emploi', 'action en cours dans le passé (≈ imparfait)', 'It was raining all morning.'),
    ('Décor + événement', 'continuous + when + past simple', 'I was watching TV when the phone rang.'),
    ('Pendant que', 'while + past continuous', 'While I was cooking...'),
    ('Négation / question', 'wasn\'t/weren\'t · Were you...?', 'She wasn\'t listening. / Were you sleeping?'),
    ('Verbes d\'état', 'know, want, like → jamais -ing', 'I knew the answer.'),
  ],
  ex1=('Choisis la forme correcte', 'Action longue en cours ou action courte ?', [
    ('I ______ dinner when you called.', ['was making', 'made', 'am making'], 'was making',
     'Action en cours interrompue → past continuous : I WAS MAKING dinner.'),
    ('She ______ her leg while she was skiing.', ['broke', 'was breaking', 'breaks'], 'broke',
     'L\'accident est l\'action courte → past simple : BROKE.'),
    ('They ______ football at five o\'clock.', ['were playing', 'was playing', 'played at'], 'were playing',
     'They → WERE + playING : action en cours à un moment donné.'),
    ('It ______ when we left the house.', ['was raining', 'rained when', 'is raining'], 'was raining',
     'Il pleuvait (décor en cours) → WAS RAINING.'),
    ('I ______ the answer immediately.', ['knew', 'was knowing', 'know'], 'knew',
     'Know est un verbe d\'état → past simple : KNEW.'),
    ('What ______ you ______ at 9 p.m. last night?', ['were / doing', 'did / doing', 'was / doing'], 'were / doing',
     '« Que faisais-tu ? » → question au continuous : What WERE you DOING?'),
  ]),
  ex2=('Complète le récit', 'Past simple ou past continuous ? Écris la forme du verbe.', [
    ('I ______ TV when the phone rang. (watch)', 'was watching',
     'Action en cours (je regardais) → WAS WATCHING.'),
    ('While she was reading, her brother ______ . (arrive)', 'arrived',
     'L\'action courte qui survient → past simple : ARRIVED.'),
    ('They ______ in the garden at six o\'clock. (play)', 'were playing',
     'They + action en cours → WERE PLAYING.'),
    ('She ______ to leave early. (want)', 'wanted',
     'Want est un verbe d\'état → past simple : WANTED.'),
    ('« Tu dormais ? » → ______ you sleeping? (un mot)', 'Were',
     'Question du continuous : WERE you sleeping?'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Je lisais quand il est arrivé. »', ['I was reading when he arrived.', 'I read when he was arriving.', 'I was reading when he was arriving.'], 'I was reading when he arrived.',
     'Imparfait (décor) → was reading ; événement → past simple : arrived.'),
    ('« Pendant que je cuisinais, elle regardait la télé. »', ['While I was cooking, she was watching TV.', 'While I cooked, she watched TV.', 'When I was cooking, she watch TV.'], 'While I was cooking, she was watching TV.',
     'Deux actions parallèles → double past continuous avec while.'),
    ('« Il ne m\'écoutait pas. »', ['He wasn\'t listening to me.', 'He didn\'t listening to me.', 'He wasn\'t listen to me.'], 'He wasn\'t listening to me.',
     'Négation du continuous : WASN\'T + listenING.'),
    ('« Nous voulions rester. »', ['We wanted to stay.', 'We were wanting to stay.', 'We want to stayed.'], 'We wanted to stay.',
     'Want est un verbe d\'état : WANTED, jamais « were wanting ».'),
    ('« Que faisais-tu à minuit ? »', ['What were you doing at midnight?', 'What did you doing at midnight?', 'What was you doing at midnight?'], 'What were you doing at midnight?',
     'You → WERE : What were you doing?'),
  ]),
  game_desc='Chaque forme du past continuous passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('was-working', 'I was working', 'action en cours dans le passé — notre imparfait', 'imparfait', 'I <b>was working</b> at eight o\'clock.', 'I was ______ at eight o\'clock. (travaillais)', 'working'),
    ('were-sleeping', 'they were sleeping', 'pluriel — were + verbe-ing', 'were + -ing', 'They <b>were sleeping</b> when I arrived.', 'They were ______ when I arrived. (dormaient)', 'sleeping'),
    ('was-raining', 'it was raining', 'le décor du récit — il pleuvait', 'décor', 'It <b>was raining</b> all morning.', 'It was ______ all morning. (pleuvait)', 'raining'),
    ('rang', 'the phone rang', 'l\'événement qui interrompt — past simple', 'événement', 'I was watching TV when the phone <b>rang</b>.', 'I was watching TV when the phone ______. (a sonné)', 'rang'),
    ('while', 'while', 'pendant que — introduit l\'action longue', 'pendant que', '<b>While</b> I was cooking, the phone rang.', '______ I was cooking, the phone rang. (pendant que)', 'while'),
    ('when', 'when', 'quand — introduit l\'action courte', 'quand', 'They were playing <b>when</b> it started to rain.', 'They were playing ______ it started to rain. (quand)', 'when'),
    ('wasnt', 'she wasn\'t listening', 'négation — was/were + not + -ing', 'négation', 'He <b>wasn\'t</b> listening to me.', 'He ______ listening to me. (négation)', 'wasn\'t'),
    ('knew', 'I knew', 'verbe d\'état au past simple — jamais en -ing', 'verbe d\'état', 'I <b>knew</b> the answer.', 'I ______ the answer. (savais)', 'knew'),
  ],
),

'present-perfect-intro': dict(
  level='a2', section='grammaire', num='Ch. 3', short='Le present perfect',
  title='Le present perfect — I have seen',
  subtitle='Have + participe passé : attention, ce n\'est PAS le passé composé',
  slides=[
    ('Have + participe passé', None,
     '<p class="slide-explanation">Le <b>present perfect</b> se forme avec <b>have/has + participe passé</b>. Il ressemble à notre passé composé... mais son emploi est différent — c\'est LE piège des francophones.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>have finished</b> my homework. — J\'ai fini mes devoirs.</p>'
     '<p style="margin-top:8px">She <b>has visited</b> many countries. — Elle a visité beaucoup de pays.</p>'
     '<p style="margin-top:8px">Participes irréguliers : see → <b>seen</b>, go → <b>gone/been</b>, do → <b>done</b>, eat → <b>eaten</b></p></div>'
     '<p style="margin-top:16px">L\'auxiliaire est toujours <b>have</b> — jamais be : She <b>has gone</b> (et non « she is gone »).</p>'),
    ('Le PIÈGE : pas de moment précis !', None,
     '<p class="slide-explanation">Règle d\'or : dès qu\'un <b>moment précis du passé</b> est mentionné (yesterday, last week, in 2020), l\'anglais exige le <b>past simple</b>. Le present perfect ne supporte aucune date !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>« J\'ai vu Paul hier. » → I <b>saw</b> Paul yesterday. (past simple !)</p>'
     '<p style="margin-top:8px;color:var(--muted)">« I have seen him yesterday » est FAUX — c\'est l\'erreur francophone n°1.</p>'
     '<p style="margin-top:8px">« J\'ai déjà vu ce film. » → I <b>have seen</b> this film. (expérience, sans date → perfect)</p></div>'
     '<p style="margin-top:16px">Le passé composé français se traduit donc tantôt par le past simple (avec date), tantôt par le present perfect (sans date).</p>'),
    ('Ever et never : l\'expérience de vie', None,
     '<p class="slide-explanation">Le present perfect sert à faire le <b>bilan d\'une vie</b> : ce qu\'on a déjà fait, sans dire quand. Avec <b>ever</b> (déjà, dans les questions) et <b>never</b> (jamais).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Have you ever been</b> to England? — Es-tu déjà allé en Angleterre ?</p>'
     '<p style="margin-top:8px">I <b>have never eaten</b> sushi. — Je n\'ai jamais mangé de sushi.</p>'
     '<p style="margin-top:8px">She <b>has been</b> to Rome twice. — Elle est allée à Rome deux fois.</p></div>'
     '<p style="margin-top:16px">Pour « être allé » (expérience), l\'anglais dit <b>have been to</b> — pas have gone, qui voudrait dire qu\'on y est encore.</p>'),
    ('Just : venir de faire', None,
     '<p class="slide-explanation">« Je <b>viens de</b> finir » se dit <b>I have just finished</b>. Just se place entre have et le participe — n\'essaie jamais de traduire « venir de » avec come !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>have just finished</b> my homework. — Je viens de finir mes devoirs.</p>'
     '<p style="margin-top:8px">She <b>has just left</b>. — Elle vient de partir.</p>'
     '<p style="margin-top:8px">We <b>have just eaten</b>. — Nous venons de manger.</p></div>'
     '<p style="margin-top:16px">Ordre fixe : have/has + <b>just</b> + participe passé.</p>'),
    ('Négation et question', None,
     '<p class="slide-explanation">L\'auxiliaire have fait la négation et la question lui-même — pas besoin de do/did.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>haven\'t finished</b> yet. — Je n\'ai pas encore fini.</p>'
     '<p style="margin-top:8px"><b>Have you finished?</b> — As-tu fini ? · <b>Has she arrived?</b> — Est-elle arrivée ?</p>'
     '<p style="margin-top:8px">Réponses courtes : <b>Yes, I have.</b> / <b>No, she hasn\'t.</b></p></div>'
     '<p style="margin-top:16px">Avec he/she/it : <b>has</b> + participe — She HAS visited, HAS she visited?, she HASN\'T visited.</p>'),
  ],
  traps=[
    ('I have seen him yesterday.', 'I <strong>saw</strong> him yesterday.', 'Moment précis (yesterday) → past simple obligatoire. Le present perfect refuse toute date.'),
    ('She is gone to London.', 'She <strong>has</strong> gone to London.', 'L\'auxiliaire du present perfect est toujours have — jamais be comme en français (« elle est partie »).'),
    ('Have you ever go to Spain?', 'Have you ever <strong>been</strong> to Spain?', 'Après have, le participe passé : have you ever BEEN. Et pour l\'expérience, on emploie been, pas gone.'),
    ('I just have finished.', 'I have <strong>just</strong> finished.', 'Just se place entre have et le participe : have JUST finished = « je viens de finir ».'),
    ('Did you ever eaten sushi?', '<strong>Have</strong> you ever <strong>eaten</strong> sushi?', 'L\'expérience de vie se demande au present perfect : HAVE you ever EATEN...?'),
  ],
  summary=[
    ('Formation', 'have/has + participe passé', 'I have finished. / She has left.'),
    ('Participes irréguliers', 'seen · been · done · eaten · gone', 'I have seen this film.'),
    ('Expérience', 'ever (question) · never (négation)', 'Have you ever been to England?'),
    ('Venir de', 'have just + participe', 'I have just finished.'),
    ('Être allé', 'have been to (expérience)', 'She has been to Rome twice.'),
    ('Date précise ?', '→ past simple, jamais perfect !', 'I saw Paul yesterday.'),
  ],
  ex1=('Present perfect ou past simple ?', 'Cherche l\'indication de temps avant de choisir.', [
    ('I ______ this film three times.', ['have seen', 'saw', 'see'], 'have seen',
     'Bilan sans date → present perfect : HAVE SEEN.'),
    ('She ______ to Italy last summer.', ['went', 'has gone', 'has been'], 'went',
     'Last summer = moment précis → past simple : WENT.'),
    ('______ you ever ______ sushi?', ['Have / eaten', 'Did / eat', 'Do / eat'], 'Have / eaten',
     'Question d\'expérience → HAVE you ever EATEN?'),
    ('I ______ my homework — I can play now.', ['have finished', 'finished yesterday', 'finish'], 'have finished',
     'Résultat présent (je peux jouer) sans date → HAVE FINISHED.'),
    ('They ______ the house in 2019.', ['bought', 'have bought', 'buy'], 'bought',
     'In 2019 = date précise → past simple : BOUGHT.'),
    ('He ______ never ______ to England.', ['has / been', 'has / gone', 'did / go'], 'has / been',
     'Expérience avec never → has never BEEN to (et non gone).'),
  ]),
  ex2=('Complète au present perfect', 'Écris la forme correcte (deux mots : auxiliaire + participe).', [
    ('I ______ my keys! I can\'t open the door. (lose) (deux mots)', 'have lost',
     'Résultat présent → HAVE LOST. Lose → lost (participe irrégulier).'),
    ('She ______ just ______ . (leave) → She ______ . (deux mots : has + participe)', 'has left',
     'Elle vient de partir : she HAS just LEFT. Leave → left.'),
    ('« Je n\'ai jamais mangé de sushi. » → I have never ______ sushi. (un mot)', 'eaten',
     'Participe passé de eat : EATEN.'),
    ('« Es-tu déjà allé à Rome ? » → Have you ever ______ to Rome? (un mot)', 'been',
     'Expérience : have been to — BEEN, pas gone.'),
    ('« As-tu fini ? » → ______ you finished? (un mot)', 'Have',
     'Question : HAVE + sujet + participe : Have you finished?'),
  ]),
  ex3=('Le bon temps pour chaque situation', 'Date précise → past simple. Sans date → present perfect.', [
    ('« J\'ai visité Londres en 2022. »', ['I visited London in 2022.', 'I have visited London in 2022.', 'I have visit London in 2022.'], 'I visited London in 2022.',
     'In 2022 = date précise → past simple VISITED.'),
    ('« Elle vient d\'arriver. »', ['She has just arrived.', 'She just arrives.', 'She comes to arrive.'], 'She has just arrived.',
     '« Venir de » = have/has JUST + participe : has just arrived.'),
    ('« Je ne suis jamais allé en Espagne. »', ['I have never been to Spain.', 'I have never gone in Spain.', 'I never went to Spain yesterday.'], 'I have never been to Spain.',
     'Expérience de vie → have never BEEN TO Spain.'),
    ('« Il a perdu ses clés » (il les cherche encore).', ['He has lost his keys.', 'He lost his keys in 2020.', 'He is lost his keys.'], 'He has lost his keys.',
     'Résultat présent → HAS LOST. L\'auxiliaire est have, jamais be.'),
    ('« As-tu déjà vu ce film ? »', ['Have you ever seen this film?', 'Did you ever saw this film?', 'Have you ever see this film?'], 'Have you ever seen this film?',
     'Expérience → HAVE you ever SEEN (participe passé de see).'),
  ]),
  game_desc='Chaque emploi du present perfect passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('have-finished', 'I have finished', 'have + participe passé — résultat présent', 'bilan présent', 'I <b>have finished</b> my homework.', 'I have ______ my homework. (fini)', 'finished'),
    ('has-gone', 'she has gone', 'auxiliaire have, jamais be — 3e personne has', 'has + participe', 'She <b>has gone</b> to London.', 'She ______ gone to London. (auxiliaire)', 'has'),
    ('seen', 'seen', 'participe passé de see — irrégulier', 'participe irrégulier', 'I have <b>seen</b> this film three times.', 'I have ______ this film three times. (vu)', 'seen'),
    ('ever', 'ever', 'déjà — dans les questions d\'expérience', 'déjà (question)', 'Have you <b>ever</b> been to England?', 'Have you ______ been to England? (déjà)', 'ever'),
    ('never', 'never', 'jamais — la négation de l\'expérience', 'jamais', 'I have <b>never</b> eaten sushi.', 'I have ______ eaten sushi. (jamais)', 'never'),
    ('just', 'have just', 'venir de — have + just + participe', 'venir de', 'I have <b>just</b> finished.', 'I have ______ finished. (viens de)', 'just'),
    ('been-to', 'have been to', 'être allé (expérience) — been, pas gone', 'être allé', 'She has <b>been</b> to Rome twice.', 'She has ______ to Rome twice. (est allée)', 'been'),
    ('saw-date', 'saw + yesterday', 'date précise → past simple, jamais perfect', 'date = past simple', 'I <b>saw</b> Paul yesterday.', 'I ______ Paul yesterday. (ai vu)', 'saw'),
  ],
),

'future-going-to': dict(
  level='a2', section='grammaire', num='Ch. 4', short='Le futur avec going to',
  title='Going to — projets et prédictions',
  subtitle='Approfondir le futur des intentions, comme notre futur proche',
  slides=[
    ('Rappel : be going to + base verbale', None,
     '<p class="slide-explanation"><b>Be going to</b> fonctionne comme notre futur proche « aller + infinitif ». Trois morceaux, toujours dans le même ordre : <b>am/is/are + going to + base verbale</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>am going to visit</b> my cousins. — Je vais rendre visite à mes cousins.</p>'
     '<p style="margin-top:8px">She <b>is going to study</b> English. — Elle va étudier l\'anglais.</p>'
     '<p style="margin-top:8px">We <b>are going to move</b> next month. — Nous allons déménager le mois prochain.</p></div>'
     '<p style="margin-top:16px">Après going to, le verbe reste <b>nu</b> : ni -s, ni -ing, ni to supplémentaire.</p>'),
    ('Emploi 1 : les projets décidés', None,
     '<p class="slide-explanation">Going to exprime une <b>intention déjà décidée</b> avant de parler : un projet, un plan. Si tu as déjà pris ta décision, c\'est going to.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I\'<b>m going to learn</b> Italian next year. — Je vais apprendre l\'italien l\'année prochaine. (c\'est décidé)</p>'
     '<p style="margin-top:8px">They\'<b>re going to sell</b> their car. — Ils vont vendre leur voiture. (plan établi)</p>'
     '<p style="margin-top:8px">What <b>are</b> you <b>going to do</b> this summer? — Que vas-tu faire cet été ?</p></div>'
     '<p style="margin-top:16px">Le test : la décision date d\'avant la conversation ? → going to.</p>'),
    ('Emploi 2 : les prédictions évidentes', None,
     '<p class="slide-explanation">Going to sert aussi pour les <b>prédictions fondées sur ce qu\'on voit</b> : les signes sont déjà là, le résultat est inévitable.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Look at those clouds! It\'<b>s going to rain</b>. — Regarde ces nuages ! Il va pleuvoir.</p>'
     '<p style="margin-top:8px">Careful! You\'<b>re going to fall</b>! — Attention ! Tu vas tomber !</p>'
     '<p style="margin-top:8px">She\'s driving too fast — she\'<b>s going to have</b> an accident.</p></div>'
     '<p style="margin-top:16px">Comme en français : « il va pleuvoir » quand les nuages sont visibles. Le parallèle avec le futur proche est presque parfait.</p>'),
    ('Négation et question', None,
     '<p class="slide-explanation">L\'auxiliaire be fait tout le travail : négation avec <b>not</b>, question par <b>inversion</b>. Jamais de do/does avec going to.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I\'m <b>not going to watch</b> this film. — Je ne vais pas regarder ce film.</p>'
     '<p style="margin-top:8px"><b>Are you going to come</b> with us? — Tu vas venir avec nous ?</p>'
     '<p style="margin-top:8px">Réponses courtes : <b>Yes, I am.</b> / <b>No, I\'m not.</b></p></div>'
     '<p style="margin-top:16px">« Do you going to...? » est une faute classique : la question se fait avec be → ARE you going to...?</p>'),
    ('Les expressions de temps du futur', None,
     '<p class="slide-explanation">Going to s\'accompagne d\'expressions qui situent le projet : apprends-les en bloc, et attention aux articles !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>tonight</b> (ce soir) &nbsp;·&nbsp; <b>tomorrow</b> (demain) &nbsp;·&nbsp; <b>next week/month/year</b></p>'
     '<p style="margin-top:8px"><b>this summer</b> (cet été) &nbsp;·&nbsp; <b>soon</b> (bientôt) &nbsp;·&nbsp; <b>in two weeks</b> (dans deux semaines)</p>'
     '<p style="margin-top:8px">We\'re going to travel <b>next month</b>. — Nous allons voyager le mois prochain.</p></div>'
     '<p style="margin-top:16px">Piège : « la semaine prochaine » = <b>next week</b>, sans the. « Dans deux semaines » = <b>in</b> two weeks.</p>'),
  ],
  traps=[
    ('I going to visit my cousins.', 'I <strong>am going to</strong> visit my cousins.', 'Be est obligatoire : I AM going to. Sans am/is/are, la structure s\'effondre.'),
    ('She is going to studies English.', 'She is going to <strong>study</strong> English.', 'Après going to, base verbale nue : going to STUDY, sans -s.'),
    ('Do you going to come?', '<strong>Are you going to</strong> come?', 'La question se fait avec be : ARE you going to come? Jamais do.'),
    ('We are going to move the next month.', 'We are going to move <strong>next month</strong>.', 'Next month sans article : pas de « the next month ».'),
    ('It will rain — look at those clouds!', 'It <strong>is going to</strong> rain — look at those clouds!', 'Prédiction fondée sur un signe visible → going to, pas will.'),
  ],
  summary=[
    ('Formation', 'am/is/are + going to + base verbale', 'I am going to travel.'),
    ('Projet décidé', 'intention prise avant de parler', 'I\'m going to learn Italian.'),
    ('Prédiction évidente', 'signes visibles', 'Look! It\'s going to rain.'),
    ('Négation', 'be + not + going to', 'I\'m not going to watch it.'),
    ('Question', 'Am/Is/Are + sujet + going to...?', 'Are you going to come?'),
    ('Expressions', 'tomorrow · next week · soon', 'We\'re moving next month.'),
  ],
  ex1=('Forme le futur avec going to', 'be + going to + base verbale : trois morceaux.', [
    ('She ______ visit her grandmother on Sunday.', ['is going to', 'are going to', 'going to'], 'is going to',
     'She → IS going to visit.'),
    ('Look at the sky! It ______ rain.', ['is going to', 'will going to', 'is going'], 'is going to',
     'Prédiction évidente → it IS GOING TO rain.'),
    ('They ______ sell their house.', ['are going to', 'is going to', 'are going'], 'are going to',
     'They → ARE going to sell.'),
    ('I\'m going to ______ Italian next year.', ['learn', 'learning', 'learns'], 'learn',
     'Après going to → base verbale : LEARN.'),
    ('______ you going to come to the party?', ['Are', 'Do', 'Will'], 'Are',
     'Question avec be : ARE you going to come?'),
    ('We ______ going to stay at home tonight.', ['aren\'t', 'don\'t', 'won\'t'], 'aren\'t',
     'Négation avec be : we AREN\'T going to stay.'),
  ]),
  ex2=('Traduis le futur proche', 'Écris la forme manquante.', [
    ('« Je vais acheter une voiture. » → I ______ going to buy a car. (un mot)', 'am',
     'I → AM going to buy.'),
    ('« Il va pleuvoir. » → It is ______ to rain. (un mot)', 'going',
     'It is GOING TO rain : les trois morceaux sont obligatoires.'),
    ('« Elle va étudier ce soir. » → She is going to ______ tonight. (un mot)', 'study',
     'Après going to → base verbale : STUDY.'),
    ('« Vas-tu venir ? » → ______ you going to come? (un mot)', 'Are',
     'Question par inversion de be : ARE you going to come?'),
    ('« Nous n\'allons pas sortir. » → We are ______ going to go out. (un mot)', 'not',
     'Négation : are NOT going to.'),
  ]),
  ex3=('Projets et prédictions', 'Choisis la phrase correcte.', [
    ('« Que vas-tu faire ce week-end ? »', ['What are you going to do this weekend?', 'What do you going to do this weekend?', 'What you are going to do this weekend?'], 'What are you going to do this weekend?',
     'Question : What + ARE + sujet + going to + verbe.'),
    ('« Attention ! Tu vas tomber ! »', ['Careful! You\'re going to fall!', 'Careful! You will to fall!', 'Careful! You go to fall!'], 'Careful! You\'re going to fall!',
     'Prédiction évidente → you\'re GOING TO fall.'),
    ('« Ils vont déménager le mois prochain. »', ['They\'re going to move next month.', 'They\'re going to move the next month.', 'They going to move next month.'], 'They\'re going to move next month.',
     'Next month SANS article, et be obligatoire : they\'RE going to.'),
    ('« Je ne vais pas regarder ce match. »', ['I\'m not going to watch this match.', 'I don\'t going to watch this match.', 'I\'m going not to watch this match.'], 'I\'m not going to watch this match.',
     'Négation : be + NOT + going to.'),
    ('Réponse courte à « Are you going to come? »', ['Yes, I am.', 'Yes, I do.', 'Yes, I going.'], 'Yes, I am.',
     'L\'auxiliaire est be → Yes, I AM.'),
  ]),
  game_desc='Chaque emploi de going to passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('going-to-plan', 'be going to (projet)', 'intention déjà décidée — notre futur proche', 'projet', 'I am <b>going</b> to learn Italian next year.', 'I am ______ to learn Italian next year. (vais)', 'going'),
    ('is-going-to', 'she is going to', '3e personne — is + going to + base verbale', 'is going to', 'She <b>is</b> going to visit her grandmother.', 'She ______ going to visit her grandmother. (auxiliaire)', 'is'),
    ('base-nue', 'going to + base verbale', 'après going to — verbe nu, sans -s ni -ing', 'verbe nu', 'She is going to <b>study</b> English.', 'She is going to ______ English. (étudier)', 'study'),
    ('prediction', 'It\'s going to rain', 'prédiction évidente — les signes sont visibles', 'évidence', 'Look at those clouds! It\'s going to <b>rain</b>.', 'Look at those clouds! It\'s going to ______. (pleuvoir)', 'rain'),
    ('not-going', 'I\'m not going to', 'négation — be + not + going to', 'négation', 'I\'m <b>not</b> going to watch this film.', 'I\'m ______ going to watch this film. (négation)', 'not'),
    ('are-you-going', 'Are you going to...?', 'question — inversion de be, jamais do', 'question', '<b>Are</b> you going to come with us?', '______ you going to come with us? (auxiliaire)', 'are'),
    ('next-month', 'next month', 'le mois prochain — sans article the', 'sans article', 'We are going to move <b>next</b> month.', 'We are going to move ______ month. (prochain)', 'next'),
    ('in-two-weeks', 'in two weeks', 'dans deux semaines — in + durée', 'dans + durée', 'They are going to arrive <b>in</b> two weeks.', 'They are going to arrive ______ two weeks. (dans)', 'in'),
  ],
),

'future-will': dict(
  level='a2', section='grammaire', num='Ch. 5', short='Le futur avec will',
  title='Will — décisions, promesses, prédictions',
  subtitle='Le deuxième futur anglais, et quand le préférer à going to',
  slides=[
    ('Will + base verbale', None,
     '<p class="slide-explanation"><b>Will</b> est un modal : il se place devant la <b>base verbale</b>, ne change jamais de forme et n\'est jamais suivi de to. Contraction : <b>\'ll</b> ; négation : <b>won\'t</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>will call</b> you tomorrow. = I\'<b>ll call</b> you tomorrow. — Je t\'appellerai demain.</p>'
     '<p style="margin-top:8px">She <b>won\'t come</b>. — Elle ne viendra pas.</p>'
     '<p style="margin-top:8px"><b>Will you help</b> me? — M\'aideras-tu ?</p></div>'
     '<p style="margin-top:16px">Une seule forme pour toutes les personnes : I will, she will, they will — pas de -s !</p>'),
    ('Emploi 1 : la décision spontanée', None,
     '<p class="slide-explanation">On emploie will pour une décision prise <b>à l\'instant même</b> où l\'on parle : le téléphone sonne, on réagit. C\'est la grande différence avec going to (décision déjà prise).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>The phone\'s ringing! — I\'<b>ll get</b> it! — J\'y vais ! (décision instantanée)</p>'
     '<p style="margin-top:8px">It\'s cold here. — I\'<b>ll close</b> the window. — Je vais fermer la fenêtre.</p>'
     '<p style="margin-top:8px">OK, I\'<b>ll take</b> this one. — D\'accord, je prends celui-là. (au magasin)</p></div>'
     '<p style="margin-top:16px">Le test : tu décides en parlant ? → will. Tu avais déjà décidé ? → going to.</p>'),
    ('Emploi 2 : promesses et offres', None,
     '<p class="slide-explanation">Will exprime aussi les <b>promesses</b>, les <b>offres d\'aide</b> et les engagements.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I promise I <b>will help</b> you. — Je te promets que je t\'aiderai.</p>'
     '<p style="margin-top:8px">Don\'t worry, I <b>won\'t tell</b> anyone. — Ne t\'inquiète pas, je ne le dirai à personne.</p>'
     '<p style="margin-top:8px">I\'<b>ll carry</b> your bag. — Je vais porter ton sac. (offre)</p></div>'
     '<p style="margin-top:16px"><b>Won\'t</b> = will not : He won\'t listen — il ne veut pas écouter / il n\'écoutera pas.</p>'),
    ('Emploi 3 : prédictions d\'opinion', None,
     '<p class="slide-explanation">Pour une prédiction fondée sur une <b>opinion</b> (pas sur un signe visible), on emploie will — souvent avec <b>I think, probably, maybe</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I think it <b>will rain</b> tomorrow. — Je pense qu\'il pleuvra demain. (opinion)</p>'
     '<p style="margin-top:8px">She <b>will probably win</b>. — Elle gagnera probablement.</p>'
     '<p style="margin-top:8px">You\'<b>ll love</b> this film! — Tu vas adorer ce film !</p></div>'
     '<p style="margin-top:16px">Compare : I think it will rain (opinion) / Look at those clouds — it\'s going to rain (signe visible).</p>'),
    ('Will ou going to ? Le récapitulatif', None,
     '<p class="slide-explanation">Le choix dépend du <b>moment de la décision</b> et du <b>type de prédiction</b>. Voici la règle en deux lignes.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>will</b> → décision à l\'instant, promesse, prédiction d\'opinion : I\'ll get it! / I think she\'ll win.</p>'
     '<p style="margin-top:8px"><b>going to</b> → projet déjà décidé, signe visible : I\'m going to travel in May. / It\'s going to rain.</p></div>'
     '<p style="margin-top:16px">Le futur simple français (« j\'appellerai ») se traduit le plus souvent par will ; le futur proche (« je vais appeler ») par going to. Mais vérifie toujours le contexte !</p>'),
  ],
  traps=[
    ('I will to call you tomorrow.', 'I will <strong>call</strong> you tomorrow.', 'Will est un modal : jamais de to après lui — will CALL.'),
    ('She wills come tomorrow.', 'She <strong>will</strong> come tomorrow.', 'Will ne prend jamais de -s : she WILL come, pour toutes les personnes.'),
    ('The phone\'s ringing! I\'m going to get it!', 'The phone\'s ringing! <strong>I\'ll get</strong> it!', 'Décision prise à l\'instant → will : I\'LL get it. Going to = décision déjà prise avant.'),
    ('I think it is going to rain tomorrow. (simple opinion)', 'I think it <strong>will rain</strong> tomorrow.', 'Prédiction d\'opinion (avec I think) → will. Going to exige un signe visible.'),
    ('He will not comes.', 'He <strong>won\'t come</strong>.', 'Après will/won\'t, base verbale sans -s : won\'t COME.'),
  ],
  summary=[
    ('Formation', 'will + base verbale (sans to)', 'I will call you. / I\'ll call you.'),
    ('Négation', 'won\'t = will not', 'She won\'t come.'),
    ('Décision spontanée', 'décidé à l\'instant même', 'The phone\'s ringing — I\'ll get it!'),
    ('Promesse / offre', 'engagement du locuteur', 'I promise I\'ll help you.'),
    ('Prédiction d\'opinion', 'I think... will · probably', 'I think it will rain.'),
    ('Will vs going to', 'instant → will · déjà décidé → going to', 'I\'ll get it! / I\'m going to travel in May.'),
  ],
  ex1=('Will ou going to ?', 'Quand la décision a-t-elle été prise ?', [
    ('The doorbell is ringing! I ______ answer it.', ['\'ll', '\'m going to', 'going to'], '\'ll',
     'Décision à l\'instant → will : I\'LL answer it.'),
    ('I ______ visit Rome in May — I bought the tickets.', ['\'m going to', '\'ll', 'will to'], '\'m going to',
     'Projet déjà décidé (billets achetés) → GOING TO.'),
    ('I promise I ______ you every day.', ['\'ll call', '\'m calling to', 'calling'], '\'ll call',
     'Promesse → will : I\'LL CALL you.'),
    ('I think she ______ the match.', ['will win', 'is going to wins', 'wins tomorrow'], 'will win',
     'Prédiction d\'opinion (I think) → WILL WIN.'),
    ('She ______ come — she\'s too busy.', ['won\'t', 'don\'t will', 'willn\'t'], 'won\'t',
     'Négation de will : WON\'T (will not).'),
    ('After will, le verbe est nu : He will ______ you tomorrow.', ['help', 'helps', 'to help'], 'help',
     'Will + base verbale : will HELP, sans -s ni to.'),
  ]),
  ex2=('Complète avec will', 'Écris le ou les mots manquants.', [
    ('« Je t\'appellerai demain. » → I ______ call you tomorrow. (un mot)', 'will',
     'Futur simple français → WILL + base verbale.'),
    ('« Elle ne viendra pas. » → She ______ come. (un mot)', 'won\'t',
     'Négation : WON\'T = will not.'),
    ('« M\'aideras-tu ? » → ______ you help me? (un mot)', 'Will',
     'Question par inversion : WILL you help me?'),
    ('« Je prends celui-là ! » (décision au magasin) → I\'ll ______ this one. (un mot)', 'take',
     'Décision spontanée : I\'ll TAKE this one — base verbale après \'ll.'),
    ('« Ne t\'inquiète pas, je ne le dirai pas. » → Don\'t worry, I won\'t ______ anyone. (un mot)', 'tell',
     'Après won\'t → base verbale : won\'t TELL.'),
  ]),
  ex3=('Choisis le bon futur', 'Décision spontanée, promesse, projet ou signe visible ?', [
    ('« D\'accord, je prends le menu du jour. » (le serveur attend)', ['OK, I\'ll have the lunch menu.', 'OK, I\'m going to have the lunch menu.', 'OK, I have the lunch menu tomorrow.'], 'OK, I\'ll have the lunch menu.',
     'Décision prise à l\'instant → will : I\'LL have.'),
    ('« Regarde ces nuages ! Il va pleuvoir. »', ['Look at those clouds! It\'s going to rain.', 'Look at those clouds! It will rain.', 'Look at those clouds! It rains.'], 'Look at those clouds! It\'s going to rain.',
     'Signe visible → GOING TO rain.'),
    ('« Je te promets que je serai à l\'heure. »', ['I promise I\'ll be on time.', 'I promise I\'m going to be on time.', 'I promise I am on time tomorrow.'], 'I promise I\'ll be on time.',
     'Promesse → will : I\'LL BE on time.'),
    ('« Nous allons nous marier en juin. » (tout est réservé)', ['We\'re going to get married in June.', 'We\'ll get married in June, I decide now.', 'We will to get married in June.'], 'We\'re going to get married in June.',
     'Projet déjà décidé → GOING TO get married.'),
    ('« Je pense qu\'ils gagneront. »', ['I think they\'ll win.', 'I think they\'re going to win, look!', 'I think they wins.'], 'I think they\'ll win.',
     'Prédiction d\'opinion avec I think → WILL : they\'ll win.'),
  ]),
  game_desc='Chaque emploi de will passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('will-call', 'I will call', 'will + base verbale — le futur simple anglais', 'futur', 'I <b>will</b> call you tomorrow.', 'I ______ call you tomorrow. (futur)', 'will'),
    ('ll-get', 'I\'ll get it!', 'décision prise à l\'instant même', 'décision spontanée', 'The phone\'s ringing — I\'ll <b>get</b> it!', 'The phone\'s ringing — I\'ll ______ it! (décrocher)', 'get'),
    ('wont', 'won\'t', 'négation de will — will not', 'négation', 'She <b>won\'t</b> come tonight.', 'She ______ come tonight. (ne viendra pas)', 'won\'t'),
    ('promise', 'I promise I\'ll...', 'promesse — engagement du locuteur', 'promesse', 'I promise I\'ll <b>help</b> you.', 'I promise I\'ll ______ you. (aider)', 'help'),
    ('think-will', 'I think... will', 'prédiction d\'opinion — souvent avec I think', 'opinion', 'I think it <b>will</b> rain tomorrow.', 'I think it ______ rain tomorrow. (opinion)', 'will'),
    ('probably', 'probably', 'probablement — se place après will', 'probablement', 'She will <b>probably</b> win.', 'She will ______ win. (probablement)', 'probably'),
    ('will-you', 'Will you...?', 'question — inversion de will', 'question', '<b>Will</b> you help me?', '______ you help me? (auxiliaire)', 'will'),
    ('no-to', 'will + base (sans to)', 'will n\'est jamais suivi de to', 'modal sans to', 'He will <b>come</b> tomorrow.', 'He will ______ tomorrow. (venir)', 'come'),
  ],
),

}
