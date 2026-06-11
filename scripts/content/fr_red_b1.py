# -*- coding: utf-8 -*-
"""fr/ B1 rédaction — article, informal-letter, story (3 chapitres)."""

CHAPTERS = {

'article': dict(
  level='b1', section='redaction', num='Ch. 1', short='Article',
  title='Article — Écrire pour un magazine',
  subtitle='Titre accrocheur, ton direct, lecteur impliqué',
  slides=[
    ('Un article n’est pas une dissertation', None,
     '<p class="slide-explanation">Premier réflexe à désapprendre : l’article anglais n’a rien de la dissertation française. Pas de problématique, pas de plan annoncé — on capte le lecteur dès la première ligne et on lui parle <b>directement</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Have you ever dreamed of quitting your job and travelling the world?</b></p>'
     '<p style="margin-top:8px">Une question rhétorique en ouverture : la signature de l’article anglais.</p></div>'),
    ('La structure en 4 blocs', None,
     '<p class="slide-explanation">1. <b>Titre</b> court et accrocheur · 2. <b>Introduction</b> qui interpelle (question, anecdote) · 3. <b>2–3 paragraphes</b> — une idée par paragraphe · 4. <b>Conclusion</b> avec une touche personnelle ou une question finale.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Titre :</b> Why I’ll Never Stop Cycling</p>'
     '<p style="margin-top:8px"><b>Fin :</b> So why not give it a try? You won’t regret it!</p></div>'),
    ('Parler au lecteur : you et we', None,
     '<p class="slide-explanation">L’article anglais tutoie son lecteur avec <b>you</b> et l’embarque avec <b>we</b>. En français on évite le « tu » journalistique — en anglais, c’est attendu.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>You might think it’s expensive — but you’d be wrong.</b></p>'
     '<p style="margin-top:8px"><b>We all know how stressful exams can be.</b></p></div>'),
    ('Le ton : vivant mais pas relâché', None,
     '<p class="slide-explanation">Registre semi-informel : contractions autorisées (<b>it’s, don’t</b>), adjectifs expressifs (<b>amazing, unforgettable</b>), mais pas d’argot. Variez les débuts de phrases — bannissez trois « I » de suite.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>What’s more, it’s completely free.</b></p>'
     '<p style="margin-top:8px"><b>Best of all, anyone can join.</b></p></div>'),
    ('Les connecteurs de l’article', None,
     '<p class="slide-explanation">Pour enchaîner sans lourdeur : <b>What’s more</b> (de plus), <b>However</b> (cependant), <b>For example/instance</b>, <b>In fact</b>, <b>All in all</b> (tout compte fait), <b>Best of all</b> (cerise sur le gâteau).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>All in all, it was an unforgettable experience.</b></p></div>'
     '<p style="margin-top:16px">Gardez <b>Furthermore / Moreover</b> pour l’essay — trop formels ici.</p>'),
  ],
  traps=[
    ('Commencer par « In this article, I will talk about... »', 'Une question ou une anecdote : <strong>Have you ever...?</strong>', 'Annoncer le plan est un réflexe de dissertation française — l’article anglais accroche, il n’annonce pas.'),
    ('Actually, I love this city. (= actuellement)', '<strong>Currently / These days</strong>, I love this city.', 'Actually = « en fait », pas « actuellement » — le faux ami classique des rédactions.'),
    ('It exists many reasons to visit.', '<strong>There are</strong> many reasons to visit.', '« Il existe » → there is/are, jamais it exists.'),
    ('I am agree with this idea.', 'I <strong>agree</strong> with this idea.', 'Agree est un verbe, pas un adjectif : I agree (« je suis d’accord » se traduit sans be).'),
    ('Un titre-phrase : « The city where I live is very beautiful »', 'Un titre court : <strong>My City, My Home</strong>', 'Le titre d’article est une accroche de quelques mots, pas une phrase complète.'),
  ],
  summary=[
    ('Titre', 'court, accrocheur', 'Why I’ll Never Stop Cycling'),
    ('Ouverture', 'question rhétorique / anecdote', 'Have you ever dreamed of...?'),
    ('Corps', 'une idée par paragraphe', '2–3 paragraphes'),
    ('Lecteur', 'you / we', 'You might think...'),
    ('Connecteurs', 'What’s more · However · All in all', 'What’s more, it’s free.'),
    ('Fin', 'touche personnelle / question', 'So why not give it a try?'),
  ],
  ex1=('Choisis la bonne option', 'Réflexes d’article.', [
    ('La meilleure ouverture d’un article sur le sport :', ['Have you ever run a marathon?', 'In this article I will present sport.', 'Sport is an activity practised by humans.'], 'Have you ever run a marathon?',
     'L’article accroche avec une question — pas d’annonce de plan ni de définition.'),
    ('Le bon connecteur semi-informel pour ajouter une idée :', ['What’s more', 'Furthermore', 'In addition to the aforementioned'], 'What’s more',
     'What’s more est le ton article ; furthermore est trop formel ici.'),
    ('« De plus en plus de gens » se dit :', ['More and more people', 'More in more people', 'Always more people'], 'More and more people',
     'Calque correct ici : more and more + nom.'),
    ('La bonne conclusion d’article :', ['So why not give it a try?', 'In conclusion, this essay has shown...', 'That is all I have to say.'], 'So why not give it a try?',
     'L’article finit sur le lecteur — pas sur une formule d’essay.'),
    ('« Actuellement » se traduit :', ['currently', 'actually', 'in actuality'], 'currently',
     'Actually = en fait. Actuellement = currently / these days.'),
    ('Le registre de l’article de magazine :', ['semi-informel, contractions OK', 'très formel, sans contractions', 'argot et abréviations SMS'], 'semi-informel, contractions OK',
     'Vivant mais soigné : it’s et don’t oui, l’argot non.'),
  ]),
  ex2=('Complète la phrase d’article', 'Écris le mot manquant.', [
    ('______ you ever visited a place that changed your life? (l’auxiliaire de l’ouverture)', 'have',
     'Have you ever + participe : l’ouverture classique.'),
    ('What’s ______, the entrance is completely free. (de plus)', 'more',
     'What’s more = de plus, en bonus.'),
    ('______ are three good reasons to start today. (il y a)', 'there',
     '« Il y a » → there are.'),
    ('All in ______, it was a fantastic weekend. (tout compte fait)', 'all',
     'All in all = tout bien considéré.'),
    ('So why ______ give it a try? (pourquoi ne pas)', 'not',
     'Why not + base verbale : l’invitation finale au lecteur.'),
  ]),
  ex3=('Choisis la version anglaise naturelle', 'Évite les calques du français.', [
    ('« Il existe beaucoup de solutions. »', ['There are many solutions.', 'It exists many solutions.', 'Many solutions exist themselves.'], 'There are many solutions.',
     'Il existe → there are.'),
    ('« Je suis d’accord avec cette idée. »', ['I agree with this idea.', 'I am agree with this idea.', 'I am of agreement with this idea.'], 'I agree with this idea.',
     'Agree est un verbe : I agree.'),
    ('« On pourrait penser que c’est cher. »', ['You might think it’s expensive.', 'One could to think it is expensive.', 'It can think that it is expensive.'], 'You might think it’s expensive.',
     'Le « on » de l’article anglais, c’est you.'),
    ('« Cerise sur le gâteau, c’est gratuit. »', ['Best of all, it’s free.', 'Cherry on the cake, it’s free.', 'On top of the cake, it’s free.'], 'Best of all, it’s free.',
     'L’idiome anglais est best of all (ou the icing on the cake).'),
    ('« De nos jours, tout le monde a un smartphone. »', ['These days, everyone has a smartphone.', 'In our days, everyone has a smartphone.', 'Actually, everyone has a smartphone.'], 'These days, everyone has a smartphone.',
     'De nos jours = these days / nowadays — pas in our days ni actually.'),
  ]),
  game_desc='Chaque outil de l’article passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('hook-question', 'Have you ever...?', 'l’ouverture qui accroche', 'accroche', '<b>Have you ever</b> dreamed of travelling the world?', '______ you ever dreamed of travelling the world? (auxiliaire)', 'have'),
    ('whats-more', 'What’s more', 'de plus (ton article)', 'ajout', '<b>What’s more</b>, it’s completely free.', 'What’s ______, it’s completely free.', 'more'),
    ('all-in-all', 'All in all', 'tout compte fait', 'bilan', '<b>All in all</b>, it was unforgettable.', 'All in ______, it was unforgettable.', 'all'),
    ('why-not', 'So why not...?', 'l’invitation finale', 'conclusion', '<b>So why not</b> give it a try?', 'So why ______ give it a try?', 'not'),
    ('best-of-all', 'Best of all', 'cerise sur le gâteau', 'point fort', '<b>Best of all</b>, anyone can join.', '______ of all, anyone can join. (le superlatif)', 'best'),
    ('there-are', 'There are', 'il y a / il existe', 'existence', '<b>There are</b> many reasons to visit.', '______ are many reasons to visit.', 'there'),
    ('you-reader', 'you (le lecteur)', 'parler directement au lecteur', 'adresse', '<b>You</b> might think it’s expensive.', '______ might think it’s expensive. (le lecteur)', 'you'),
    ('currently', 'currently', 'actuellement (pas actually !)', 'faux ami', 'I’m <b>currently</b> living in Lyon.', 'I’m ______ living in Lyon. (actuellement)', 'currently'),
  ],
),

'informal-letter': dict(
  level='b1', section='redaction', num='Ch. 2', short='Informal Letter',
  title='Informal Letter — Écrire à un ami',
  subtitle='Dear Sam, ... Write soon! Les codes de la lettre amicale',
  slides=[
    ('Oubliez la lettre française', None,
     '<p class="slide-explanation">Pas de « Je vous prie d’agréer... » ici. La lettre informelle anglaise est courte, chaleureuse et pleine de contractions. <b>Dear + prénom</b> n’a rien de formel — c’est l’équivalent de « Salut ».</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Dear Sam,</b></p>'
     '<p style="margin-top:8px"><b>Thanks for your letter — it was great to hear from you!</b></p></div>'),
    ('Les ouvertures qui sonnent juste', None,
     '<p class="slide-explanation">On réagit d’abord à la lettre reçue : <b>Thanks for your letter · It was great to hear from you · Sorry I haven’t written for ages · How are things?</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Sorry I haven’t written for ages — I’ve been really busy with exams.</b></p></div>'
     '<p style="margin-top:16px">Notez le present perfect : <b>I haven’t written</b>, <b>I’ve been busy</b> — le temps des nouvelles.</p>'),
    ('Le corps : des nouvelles et des questions', None,
     '<p class="slide-explanation">Donnez vos nouvelles, réagissez aux siennes, posez des questions. Les chevilles informelles : <b>Anyway</b> (bref), <b>By the way</b> (au fait), <b>Guess what!</b> (devine quoi !), <b>Well</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Guess what! I’ve passed my driving test!</b></p>'
     '<p style="margin-top:8px"><b>By the way, how was your holiday in Italy?</b></p></div>'),
    ('Le ton informel : contractions et phrasal verbs', None,
     '<p class="slide-explanation">Contractions partout (<b>I’m, can’t, it’s</b>), phrasal verbs plutôt que verbes latins : <b>find out</b> (découvrir), <b>look forward to</b> (avoir hâte), <b>get together</b> (se retrouver).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I can’t wait to see you!</b> (J’ai trop hâte !)</p>'
     '<p style="margin-top:8px"><b>We must get together soon.</b></p></div>'),
    ('Conclure et signer', None,
     '<p class="slide-explanation">Une phrase de clôture + une formule + le prénom seul : <b>Write soon! · Give my love to your family · Looking forward to hearing from you</b> puis <b>Love, / Best wishes, / Take care,</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Anyway, I’d better go — write soon!</b></p>'
     '<p style="margin-top:8px"><b>Love,<br>Emma</b></p></div>'
     '<p style="margin-top:16px">Attention : <b>looking forward to hearING</b> — to est une préposition ici.</p>'),
  ],
  traps=[
    ('Dear my friend Sam,', '<strong>Dear Sam,</strong>', 'Dear + prénom directement — jamais my friend ni le nom de famille entre amis.'),
    ('I look forward to hear from you.', 'I look forward to <strong>hearing</strong> from you.', 'Look forward TO + -ing : to est une préposition, pas l’infinitif.'),
    ('I write you this letter to tell you...', '<strong>I’m writing to tell you...</strong>', 'L’action en cours s’exprime au present continuous — et on allège la formule.'),
    ('Best regards, (à un ami proche)', '<strong>Love, / Take care,</strong>', 'Best regards est professionnel ; entre amis : Love, Take care, Best wishes.'),
    ('I have seen Tom yesterday.', 'I <strong>saw</strong> Tom yesterday.', 'Yesterday (moment fini) → past simple, pas present perfect — l’inverse du passé composé.'),
  ],
  summary=[
    ('Salutation', 'Dear + prénom,', 'Dear Sam,'),
    ('Ouverture', 'réagir à la lettre reçue', 'Thanks for your letter!'),
    ('Nouvelles', 'present perfect', 'Guess what! I’ve passed!'),
    ('Chevilles', 'Anyway · By the way', 'By the way, how was Italy?'),
    ('Clôture', 'Write soon! · Can’t wait to see you', 'I’d better go — write soon!'),
    ('Signature', 'Love, / Take care, + prénom', 'Love, Emma'),
  ],
  ex1=('Choisis la bonne option', 'Les codes de la lettre amicale.', [
    ('La salutation correcte à un ami :', ['Dear Sam,', 'Dear Mr Sam,', 'Hello dear friend,'], 'Dear Sam,',
     'Dear + prénom, rien d’autre.'),
    ('La meilleure première phrase :', ['It was great to hear from you!', 'I am writing in response to your correspondence.', 'This letter has for purpose to answer you.'], 'It was great to hear from you!',
     'Chaleureux et direct — les deux autres sont des calques formels.'),
    ('« Au fait » se dit :', ['By the way', 'By the fact', 'In the way'], 'By the way',
     'By the way introduit un changement de sujet léger.'),
    ('« J’ai hâte de te voir » :', ['I can’t wait to see you!', 'I have haste to see you!', 'I am in a hurry of seeing you!'], 'I can’t wait to see you!',
     'L’idiome : can’t wait to + infinitif.'),
    ('La signature adaptée à un ami proche :', ['Love,', 'Yours faithfully,', 'Respectfully yours,'], 'Love,',
     'Love, / Take care, — les formules pro sont déplacées ici.'),
    ('« Désolé de ne pas avoir écrit depuis longtemps » :', ['Sorry I haven’t written for ages.', 'Sorry I don’t write since a long time.', 'Sorry to not have written since long.'], 'Sorry I haven’t written for ages.',
     'Present perfect + for ages — « depuis longtemps » ne se traduit pas par since a long time.'),
  ]),
  ex2=('Complète la lettre', 'Écris le mot manquant.', [
    ('Thanks ______ your letter — it really made my day! (la préposition)', 'for',
     'Thanks FOR + nom.'),
    ('Guess ______! I’ve got a new job! (devine... !)', 'what',
     'Guess what! — l’annonce de grande nouvelle.'),
    ('I look forward to ______ from you. (hear en -ing)', 'hearing',
     'Look forward to + -ing.'),
    ('______, I’d better go — my bus is coming. (bref / enfin bon)', 'anyway',
     'Anyway signale qu’on va conclure.'),
    ('Give my ______ to your parents. (transmets mes amitiés)', 'love',
     'Give my love to... — la formule affectueuse.'),
  ]),
  ex3=('Choisis la version anglaise naturelle', 'Évite les calques du français.', [
    ('« Quoi de neuf ? »', ['What’s new?', 'What of new?', 'Which news?'], 'What’s new?',
     'What’s new? / How are things? — les vraies formules.'),
    ('« On devrait se retrouver bientôt. »', ['We should get together soon.', 'We should find us again soon.', 'We should retrieve ourselves soon.'], 'We should get together soon.',
     'Se retrouver (entre amis) = get together.'),
    ('« J’ai vu Léa la semaine dernière. »', ['I saw Léa last week.', 'I have seen Léa last week.', 'I’ve been seeing Léa last week.'], 'I saw Léa last week.',
     'Last week (fini) → past simple, malgré le passé composé français.'),
    ('« Écris-moi vite ! »', ['Write soon!', 'Write me quickly!', 'Answer fast!'], 'Write soon!',
     'La clôture consacrée : Write soon!'),
    ('« Devine quoi ! J’ai eu mon permis ! »', ['Guess what! I’ve passed my driving test!', 'Guess what! I had my driving licence!', 'Divine what! I obtained my permit!'], 'Guess what! I’ve passed my driving test!',
     'Pass a test = réussir ; la nouvelle fraîche prend le present perfect.'),
  ]),
  game_desc='Chaque formule de la lettre passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('dear-name', 'Dear + prénom', 'la salutation amicale', 'salutation', '<b>Dear Sam,</b>', '______ Sam, (la salutation)', 'dear'),
    ('hear-from', 'great to hear from you', 'content d’avoir de tes nouvelles', 'ouverture', 'It was great to <b>hear from</b> you!', 'It was great to hear ______ you! (préposition)', 'from'),
    ('guess-what', 'Guess what!', 'devine quoi !', 'annonce', '<b>Guess what!</b> I’ve passed my test!', 'Guess ______! I’ve passed my test!', 'what'),
    ('by-the-way', 'By the way', 'au fait', 'transition', '<b>By the way</b>, how was your holiday?', 'By the ______, how was your holiday?', 'way'),
    ('anyway', 'Anyway', 'bref / enfin bon', 'clôture', '<b>Anyway</b>, I’d better go.', '______, I’d better go. (bref)', 'anyway'),
    ('cant-wait', 'can’t wait to', 'avoir trop hâte de', 'impatience', 'I <b>can’t wait to</b> see you!', 'I can’t ______ to see you!', 'wait'),
    ('write-soon', 'Write soon!', 'écris-moi vite', 'fin', '<b>Write soon!</b>', '______ soon! (la consigne finale)', 'write'),
    ('look-forward', 'look forward to + -ing', 'attendre avec impatience', 'formule', 'I look forward to <b>hearing</b> from you.', 'I look forward to ______ from you. (hear en -ing)', 'hearing'),
  ],
),

'story': dict(
  level='b1', section='redaction', num='Ch. 3', short='Story',
  title='Story — Raconter une histoire',
  subtitle='Temps du récit, suspense et chute',
  slides=[
    ('Les trois temps du récit', None,
     '<p class="slide-explanation">Le trio narratif anglais : <b>past simple</b> (les actions, l’une après l’autre), <b>past continuous</b> (le décor en cours), <b>past perfect</b> (l’avant). Pas de passé simple littéraire ici — le past simple anglais est le temps normal du récit.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The sun was setting</b> (décor) <b>when we reached the cabin</b> (action). <b>Someone had broken</b> the window (avant).</p></div>'),
    ('Une première phrase qui plante le décor', None,
     '<p class="slide-explanation">Souvent imposée par la consigne Cambridge. Sinon : lancez l’action ou l’ambiance immédiatement — pas de présentation des personnages à la française.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>It was midnight when the phone rang.</b></p>'
     '<p style="margin-top:8px"><b>Anna was walking home when she noticed the open door.</b></p></div>'),
    ('Les connecteurs du temps', None,
     '<p class="slide-explanation">Pour dérouler : <b>As soon as</b> (dès que), <b>While</b> (pendant que), <b>Suddenly</b> (soudain), <b>A few minutes later</b>, <b>In the end</b> (finalement), <b>at first</b> (au début).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>As soon as she opened the box, the lights went out.</b></p>'
     '<p style="margin-top:8px"><b>In the end, everything turned out fine.</b></p></div>'
     '<p style="margin-top:16px">⚠ <b>At the end</b> = à la fin de quelque chose (at the end of the film) ; <b>in the end</b> = finalement.</p>'),
    ('Montrer, pas raconter', None,
     '<p class="slide-explanation">Adjectifs forts et verbes précis font vivre le récit : <b>terrified</b> (pas very scared), <b>whisper, rush, grab, slam</b>. Une ligne de dialogue direct réveille l’histoire.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>“Don’t move,” she whispered.</b></p>'
     '<p style="margin-top:8px"><b>He grabbed the keys and rushed outside.</b></p></div>'),
    ('La chute', None,
     '<p class="slide-explanation">Une bonne histoire B1 se termine — résolution, surprise ou clin d’œil. Ne la laissez jamais en suspens faute de temps : gardez deux minutes pour écrire la fin.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>It was only then that I realised: the letter had been from my own brother.</b></p></div>'),
  ],
  traps=[
    ('While I walked home, I was seeing a strange light.', 'While I <strong>was walking</strong> home, I <strong>saw</strong> a strange light.', 'Le décor en cours → past continuous ; l’événement → past simple. See ne se met presque jamais en continu.'),
    ('When I arrived, the train already left.', 'When I arrived, the train <strong>had already left</strong>.', 'L’action antérieure prend le past perfect : had left.'),
    ('At the end, the police found the thief.', '<strong>In the end</strong>, the police found the thief.', 'Finalement = in the end ; at the end = à la fin de qqch.'),
    ('« Come here », she said. (ponctuation française)', '<strong>“Come here,” she said.</strong>', 'Dialogue anglais : guillemets doubles hauts, virgule avant la fermeture — pas de « » ni de tirets.'),
    ('She was very very scared.', 'She was <strong>terrified</strong>.', 'Un adjectif fort vaut mieux que very very — c’est noté au Cambridge.'),
  ],
  summary=[
    ('Actions', 'past simple', 'she opened, he ran'),
    ('Décor en cours', 'past continuous', 'the sun was setting'),
    ('L’avant', 'past perfect', 'someone had broken in'),
    ('Dès que / soudain', 'as soon as · suddenly', 'As soon as she opened...'),
    ('Finalement', 'in the end (≠ at the end)', 'In the end, all was fine.'),
    ('Vie du récit', 'adjectifs forts · dialogue', '“Don’t move,” she whispered.'),
  ],
  ex1=('Choisis la forme correcte', 'Les temps et outils du récit.', [
    ('I ______ TV when someone knocked at the door.', ['was watching', 'watched', 'had watched'], 'was watching',
     'Action en cours interrompue → past continuous.'),
    ('When we got to the station, the train ______.', ['had already left', 'already left', 'was already leaving'], 'had already left',
     'Antériorité → past perfect.'),
    ('______ she heard the noise, she called the police.', ['As soon as', 'During', 'Meanwhile'], 'As soon as',
     'Dès que = as soon as + proposition.'),
    ('______, we found the keys under the sofa.', ['In the end', 'At the end', 'By the end'], 'In the end',
     'Finalement = in the end.'),
    ('“Run!” he ______.', ['shouted', 'said loudly very', 'told'], 'shouted',
     'Un verbe de parole précis : shouted. (Told exige un objet.)'),
    ('Everyone was ______ when the lights went out.', ['terrified', 'very very afraid', 'much frightened of'], 'terrified',
     'L’adjectif fort remplace very + adjectif faible.'),
  ]),
  ex2=('Complète le récit', 'Écris le mot manquant.', [
    ('It was midnight ______ the phone rang. (quand)', 'when',
     'It was... when... — l’ouverture de récit.'),
    ('She opened the door and realised someone ______ been inside. (l’auxiliaire de l’antériorité)', 'had',
     'Past perfect : someone HAD been inside.'),
    ('______ , a dog started barking. (soudain)', 'suddenly',
     'Suddenly lance l’événement inattendu.'),
    ('At ______ , I thought it was a joke — but I was wrong. (au début)', 'first',
     'At first = au début (contraste avec la suite).'),
    ('He grabbed his coat and ______ outside. (se précipiter — prétérit)', 'rushed',
     'Rush = se précipiter ; rushed outside.'),
  ]),
  ex3=('Choisis la version anglaise naturelle', 'Réflexes de narration.', [
    ('« Pendant que je courais, il a commencé à pleuvoir. »', ['While I was running, it started to rain.', 'While I ran, it was starting to rain.', 'During I was running, it started to rain.'], 'While I was running, it started to rain.',
     'While + past continuous pour l’arrière-plan ; during + nom seulement.'),
    ('« Dès que le film a commencé, elle s’est endormie. »', ['As soon as the film started, she fell asleep.', 'Since the film started, she fell asleep.', 'From that the film started, she slept.'], 'As soon as the film started, she fell asleep.',
     'Dès que = as soon as.'),
    ('« Je ne l’avais jamais vu auparavant. »', ['I had never seen him before.', 'I never saw him before that never.', 'I have never seen him before yesterday.'], 'I had never seen him before.',
     'Antériorité dans un récit au passé → past perfect.'),
    ('« — Suis-moi, murmura-t-elle. »', ['“Follow me,” she whispered.', '— Follow me, she whispered.', '« Follow me » she whispered.'], '“Follow me,” she whispered.',
     'Guillemets doubles hauts + virgule intérieure : la ponctuation anglaise du dialogue.'),
    ('« Finalement, tout s’est bien terminé. »', ['In the end, everything turned out fine.', 'At the end, everything finished good.', 'Finally at the end, all ended well.'], 'In the end, everything turned out fine.',
     'In the end + turn out fine — la chute apaisée.'),
  ]),
  game_desc='Chaque outil du récit passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('past-continuous', 'past continuous (décor)', 'l’action en cours du récit', 'décor', 'The sun <b>was setting</b> when we arrived.', 'The sun ______ setting when we arrived. (be au passé)', 'was'),
    ('past-perfect', 'past perfect (l’avant)', 'l’action antérieure', 'antériorité', 'The train <b>had left</b> when we arrived.', 'The train ______ left when we arrived. (auxiliaire)', 'had'),
    ('as-soon-as', 'as soon as', 'dès que', 'enchaînement', '<b>As soon as</b> she opened the box, the lights went out.', 'As ______ as she opened the box... (dès que)', 'soon'),
    ('suddenly', 'suddenly', 'soudain', 'rebondissement', '<b>Suddenly</b>, a dog started barking.', '______, a dog started barking. (soudain)', 'suddenly'),
    ('in-the-end', 'in the end', 'finalement (≠ at the end)', 'chute', '<b>In the end</b>, everything turned out fine.', '______ the end, everything turned out fine. (préposition)', 'in'),
    ('at-first', 'at first', 'au début', 'contraste', '<b>At first</b>, I thought it was a joke.', 'At ______, I thought it was a joke.', 'first'),
    ('whisper', 'whisper', 'murmurer (verbe de parole)', 'dialogue', '“Don’t move,” she <b>whispered</b>.', '“Don’t move,” she ______. (murmurer — prétérit)', 'whispered'),
    ('terrified', 'terrified', 'terrifié (mieux que very scared)', 'adjectif fort', 'She was <b>terrified</b>.', 'She was ______. (bien plus que scared)', 'terrified'),
  ],
),

}
