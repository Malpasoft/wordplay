# -*- coding: utf-8 -*-
"""fr/ B2 grammaire — lot 3 (5 chapitres)."""

CHAPTERS = {

'inversion': dict(
  level='b2', section='grammaire', num='Ch. 9', short='Inversion',
  title='Inversion — L’emphase du style soutenu',
  subtitle='Never have I seen... : inverser pour insister',
  slides=[
    ('Le principe', None,
     '<p class="slide-explanation">Quand une phrase commence par un adverbe négatif ou restrictif (<b>never, rarely, not only, little...</b>), le sujet et l’auxiliaire s’inversent — comme dans une question. Effet : registre soutenu, emphase dramatique.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Never have I seen such a mess.</b> (Jamais je n’ai vu un tel désordre.)</p>'
     '<p style="margin-top:8px">Version neutre : I have never seen such a mess.</p></div>'
     '<p style="margin-top:16px">Le français littéraire fait pareil : « Jamais je n’ai vu... », « À peine était-il arrivé... »</p>'),
    ('Les déclencheurs courants', None,
     '<p class="slide-explanation"><b>Never, rarely, seldom, at no time, under no circumstances, not only... but also, no sooner... than, hardly... when, little</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Rarely do we get such an opportunity.</b></p>'
     '<p style="margin-top:8px"><b>Under no circumstances should you open this door.</b></p></div>'),
    ('Not only... but also', None,
     '<p class="slide-explanation">La star des rédactions B2 : <b>Not only + inversion, but (also)...</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Not only did she win, but she also broke the record.</b></p>'
     '<p style="margin-top:8px">(Non seulement elle a gagné, mais en plus elle a battu le record.)</p></div>'),
    ('No sooner / Hardly', None,
     '<p class="slide-explanation">« À peine... que » : <b>No sooner had X done... than...</b> · <b>Hardly had X done... when...</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>No sooner had we arrived than it started to rain.</b></p>'
     '<p style="margin-top:8px"><b>Hardly had I sat down when the phone rang.</b></p></div>'),
    ('Sans auxiliaire ? Ajoutez do', None,
     '<p class="slide-explanation">Au présent ou prétérit simple, l’inversion réclame do/does/did — comme les questions.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Little did he know what was coming.</b> (Il était loin de se douter...)</p>'
     '<p style="margin-top:8px"><b>Seldom does she complain.</b></p></div>'),
  ],
  traps=[
    ('Never I have seen such a mess.', 'Never <strong>have I</strong> seen such a mess.', 'L’adverbe négatif en tête déclenche l’inversion : auxiliaire avant le sujet.'),
    ('Not only she won, but...', 'Not only <strong>did she win</strong>, but...', 'Not only en tête → inversion avec did.'),
    ('No sooner had we arrived when it rained.', 'No sooner had we arrived <strong>than</strong> it rained.', 'No sooner s’apparie avec than ; hardly avec when.'),
    ('Little he knew...', 'Little <strong>did he know</strong>...', 'Prétérit simple → did + sujet + base : little did he know.'),
    ('Under no circumstances you should open it.', 'Under no circumstances <strong>should you</strong> open it.', 'Expression restrictive en tête → inversion du modal.'),
  ],
  summary=[
    ('Principe', 'adverbe négatif + aux + sujet', 'Never have I seen...'),
    ('Not only', 'Not only did X..., but (also)', 'Not only did she win...'),
    ('À peine... que', 'No sooner... than / Hardly... when', 'No sooner had we arrived than...'),
    ('Sans auxiliaire', 'do/does/did', 'Little did he know.'),
    ('Registre', 'soutenu, rédactions', 'essays, discours'),
  ],
  ex1=('Choisis la forme correcte', 'Inversion après les ouvertures négatives.', [
    ('Never ______ such a beautiful sunset.', ['have I seen', 'I have seen', 'I saw have'], 'have I seen',
     'Never en tête → have I seen (inversion).'),
    ('Not only ______ late, but he also forgot the documents.', ['was he', 'he was', 'he is'], 'was he',
     'Not only en tête → was he (inversion de be).'),
    ('No sooner had the match started ______ it began to rain.', ['than', 'when', 'that'], 'than',
     'No sooner... than — la paire fixe.'),
    ('Little ______ what was waiting for her.', ['did she know', 'she knew', 'knew she'], 'did she know',
     'Prétérit simple → did she know.'),
    ('Under no circumstances ______ leave the building.', ['should you', 'you should', 'should'], 'should you',
     'Expression restrictive → should you (inversion du modal).'),
    ('Rarely ______ a film twice.', ['do I watch', 'I watch', 'watch I'], 'do I watch',
     'Rarely en tête + présent simple → do I watch.'),
  ]),
  ex2=('Complète l’inversion', 'Écris le mot manquant.', [
    ('Never ______ I heard such nonsense! (l’auxiliaire)', 'have',
     'Never + HAVE I heard : l’auxiliaire passe devant.'),
    ('Not only ______ she speak Arabic, she also speaks Farsi. (l’auxiliaire du présent)', 'does',
     'Présent simple → does she speak.'),
    ('Hardly had I sat down ______ the phone rang. (le mot d’appariement)', 'when',
     'Hardly... WHEN (no sooner... than).'),
    ('______ did he know that we were planning a party. (il était loin de se douter)', 'little',
     'Little did he know — l’expression figée.'),
    ('At no time ______ the passengers in danger. (be au prétérit)', 'were',
     'At no time WERE the passengers in danger.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Jamais je n’ai vu une telle foule. »', ['Never have I seen such a crowd.', 'Never I saw such a crowd.', 'I never have seen a such crowd.'], 'Never have I seen such a crowd.',
     'Ouverture emphatique → Never have I seen.'),
    ('« Non seulement il chante, mais il compose aussi. »', ['Not only does he sing, but he also composes.', 'Not only he sings, but also composes.', 'Does not only he sing, he composes.'], 'Not only does he sing, but he also composes.',
     'Not only + does he sing.'),
    ('« À peine étions-nous partis qu’il a commencé à neiger. »', ['No sooner had we left than it started snowing.', 'No sooner we had left when it started snowing.', 'Sooner had we left than it snowed.'], 'No sooner had we left than it started snowing.',
     'No sooner had we left than...'),
    ('« En aucun cas vous ne devez répondre. »', ['Under no circumstances should you reply.', 'Under no circumstances you should reply.', 'In no case you reply should.'], 'Under no circumstances should you reply.',
     'Restriction en tête → inversion : should you.'),
    ('Quelle phrase est en registre NEUTRE (sans emphase) ?', ['I have rarely seen him so happy.', 'Rarely have I seen him so happy.', 'Rarely I have seen him so happy.'], 'I have rarely seen him so happy.',
     'Sans inversion = neutre ; l’inversion ajoute l’emphase ; la 3e est incorrecte.'),
  ]),
  game_desc='Chaque structure d’inversion passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('never-have-i', 'Never have I...', 'jamais je n’ai... — l’inversion emphatique', 'inversion de base', '<b>Never have I</b> seen such a mess.', 'Never ______ I seen such a mess.', 'have'),
    ('not-only-did', 'Not only did...', 'non seulement... — inversion avec did', 'not only', '<b>Not only did</b> she win, but she broke the record.', 'Not only ______ she win, but she broke the record.', 'did'),
    ('no-sooner-than', 'No sooner... than', 'à peine... que', 'no sooner', '<b>No sooner</b> had we arrived <b>than</b> it rained.', 'No sooner had we arrived ______ it rained.', 'than'),
    ('hardly-when', 'Hardly... when', 'à peine... que — la variante', 'hardly', '<b>Hardly</b> had I sat down <b>when</b> the phone rang.', 'Hardly had I sat down ______ the phone rang.', 'when'),
    ('little-did', 'Little did he know', 'il était loin de se douter', 'little did', '<b>Little did he know</b> what was coming.', 'Little ______ he know what was coming.', 'did'),
    ('under-no', 'Under no circumstances', 'en aucun cas + inversion', 'restriction', '<b>Under no circumstances</b> should you open it.', 'Under no circumstances ______ you open it.', 'should'),
    ('rarely-do', 'Rarely do...', 'rarement — inversion au présent', 'rarely', '<b>Rarely do</b> we get such a chance.', 'Rarely ______ we get such a chance.', 'do'),
    ('seldom', 'Seldom', 'rarement (soutenu)', 'seldom', '<b>Seldom</b> does she complain.', '______ does she complain. (rarement)', 'seldom'),
  ],
),

'linking-discourse': dict(
  level='b2', section='grammaire', num='Ch. 10', short='Linking & Discourse',
  title='Linking & Discourse — Articuler son discours',
  subtitle='However, despite, although : les connecteurs du B2',
  slides=[
    ('Malgré : despite et in spite of', None,
     '<p class="slide-explanation"><b>Despite / in spite of + nom ou -ing</b> — jamais de proposition complète directement.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Despite the rain, we went out.</b> (Malgré la pluie...)</p>'
     '<p style="margin-top:8px"><b>In spite of being tired, she finished.</b></p>'
     '<p style="margin-top:8px">Avec une proposition : <b>despite the fact that</b> it was raining...</p></div>'
     '<p style="margin-top:16px">⚠ « Despite of » n’existe pas — c’est in spite OF ou despite tout court.</p>'),
    ('Bien que : although, even though', None,
     '<p class="slide-explanation"><b>Although/even though + proposition complète</b>. Even though est plus fort.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Although it was raining, we went out.</b></p>'
     '<p style="margin-top:8px"><b>Even though he apologised, she’s still angry.</b></p></div>'),
    ('However : le pivot des rédactions', None,
     '<p class="slide-explanation"><b>However</b> relie deux phrases (point ou point-virgule avant, virgule après). Ne le confondez pas avec but, qui reste à l’intérieur d’une phrase.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The plan is expensive. However, it could work.</b></p>'
     '<p style="margin-top:8px">Variantes : <b>nevertheless, on the other hand, in contrast</b>.</p></div>'),
    ('Cause et conséquence', None,
     '<p class="slide-explanation"><b>Due to / owing to + nom</b> (en raison de) · <b>therefore, as a result, consequently</b> (par conséquent) · <b>since/as</b> (puisque).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The flight was cancelled due to fog.</b></p>'
     '<p style="margin-top:8px"><b>Since you’re here, let’s start.</b> (Puisque tu es là...)</p></div>'),
    ('Organiser : firstly, in addition, to sum up', None,
     '<p class="slide-explanation">La charpente d’un essai : <b>Firstly... Furthermore/Moreover/In addition... Finally... To sum up / In conclusion</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Moreover, the costs would be lower.</b> (De plus...)</p>'
     '<p style="margin-top:8px"><b>To sum up, the benefits outweigh the risks.</b></p></div>'),
  ],
  traps=[
    ('Despite of the rain...', '<strong>Despite</strong> the rain... / <strong>In spite of</strong> the rain...', 'Despite ne prend jamais of.'),
    ('Despite it was raining, we went out.', 'Despite <strong>the rain</strong> / Although <strong>it was raining</strong>...', 'Despite + nom/-ing ; although + proposition.'),
    ('Although the rain, we went out.', '<strong>Despite</strong> the rain... / Although <strong>it was raining</strong>...', 'Although exige une proposition complète, pas un simple nom.'),
    ('The plan is expensive, however it could work. (une seule phrase)', 'The plan is expensive<strong>. However,</strong> it could work.', 'However ouvre une nouvelle phrase (ou suit un point-virgule).'),
    ('Since une heure, j’attends → Since one hour...', '<strong>For</strong> an hour... (durée)', 'Ce since-là est temporel : depuis + durée = for. Le since causal signifie « puisque ».'),
  ],
  summary=[
    ('Malgré + nom', 'despite / in spite of', 'Despite the rain...'),
    ('Bien que + prop.', 'although / even though', 'Although it was raining...'),
    ('Cependant', 'However, + phrase', 'However, it could work.'),
    ('En raison de', 'due to / owing to + nom', 'due to fog'),
    ('Puisque', 'since / as', "Since you're here..."),
    ('Structure d’essai', 'Firstly... Moreover... To sum up', 'In conclusion...'),
  ],
  ex1=('Choisis le bon connecteur', 'Nom ou proposition ? Une phrase ou deux ?', [
    ('______ the heavy traffic, we arrived on time.', ['Despite', 'Although', 'However'], 'Despite',
     'Suivi d’un nom (the traffic) → despite.'),
    ('______ he trained hard, he lost the final.', ['Although', 'Despite', 'Due to'], 'Although',
     'Suivi d’une proposition complète → although.'),
    ('The hotel was expensive. ______ , the service was poor.', ['Moreover', 'Although', 'Despite'], 'Moreover',
     'Deux phrases, ajout d’un second reproche → Moreover (de plus).'),
    ('The match was cancelled ______ the storm.', ['due to', 'because', 'although'], 'due to',
     'Due to + nom : en raison de la tempête.'),
    ('I see your point. ______ , I still disagree.', ['However', 'Despite', 'Since'], 'However',
     'Contraste entre deux phrases → However, + virgule.'),
    ('______ being injured, she finished the race.', ['In spite of', 'Even though', 'Therefore'], 'In spite of',
     'Suivi de -ing → in spite of being injured.'),
  ]),
  ex2=('Complète le connecteur', 'Écris le mot manquant.', [
    ('In spite ______ the noise, the baby slept. (le petit mot)', 'of',
     'In spite OF — c’est despite qui s’emploie seul.'),
    ('Despite the fact ______ it was late, they kept playing. (avec une proposition)', 'that',
     'Despite the fact THAT + proposition.'),
    ('He failed the exam. ______ , he can retake it in June. (heureusement : cependant)', 'however',
     'However, + nouvelle phrase.'),
    ('______ you’re asking, I’ll tell you the truth. (puisque)', 'since',
     'Since causal = puisque.'),
    ('To sum ______ , the project deserves our support. (pour conclure)', 'up',
     'To sum up = en résumé.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise correcte.', [
    ('« Malgré la pluie, le concert a eu lieu. »', ['Despite the rain, the concert took place.', 'Despite of the rain, the concert took place.', 'Although the rain, the concert took place.'], 'Despite the rain, the concert took place.',
     'Despite + nom, sans of.'),
    ('« Bien qu’il soit jeune, il est très mûr. »', ['Although he is young, he is very mature.', 'Despite he is young, he is very mature.', 'However he is young, he is mature.'], 'Although he is young, he is very mature.',
     'Although + proposition complète.'),
    ('« Le vol a été annulé en raison du brouillard. »', ['The flight was cancelled due to fog.', 'The flight was cancelled because to fog.', 'The flight was cancelled despite fog.'], 'The flight was cancelled due to fog.',
     'Due to + nom.'),
    ('« Puisque tu es là, aide-moi. »', ["Since you're here, give me a hand.", "For you're here, give me a hand.", "During you're here, help."], "Since you're here, give me a hand.",
     'Since causal = puisque.'),
    ('« C’est cher. Cependant, ça vaut le coup. »', ["It's expensive. However, it's worth it.", "It's expensive however it's worth it.", "It's expensive, despite it's worth it."], "It's expensive. However, it's worth it.",
     'However ouvre une nouvelle phrase, suivi d’une virgule.'),
  ]),
  game_desc='Chaque connecteur passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('despite', 'despite + nom', 'malgré — jamais suivi de of', 'malgré', '<b>Despite</b> the rain, we went out.', '______ the rain, we went out. (malgré)', 'despite'),
    ('in-spite-of', 'in spite of', 'malgré — la variante avec of', 'malgré (variante)', '<b>In spite of</b> being tired, she finished.', 'In ______ of being tired, she finished.', 'spite'),
    ('although', 'although + proposition', 'bien que + phrase complète', 'bien que', '<b>Although</b> it was raining, we went out.', '______ it was raining, we went out. (bien que)', 'although'),
    ('even-though', 'even though', 'bien que — version renforcée', 'bien que (fort)', '<b>Even though</b> he apologised, she’s still angry.', 'Even ______ he apologised, she’s still angry.', 'though'),
    ('however', 'However,', 'cependant — entre deux phrases', 'cependant', "It's expensive. <b>However</b>, it works.", "It's expensive. ______ , it works.", 'however'),
    ('due-to', 'due to + nom', 'en raison de', 'cause nominale', 'Cancelled <b>due to</b> fog.', 'Cancelled ______ to fog.', 'due'),
    ('since-cause', 'since (puisque)', 'puisque — cause connue', 'puisque', '<b>Since</b> you’re here, let’s start.', '______ you’re here, let’s start. (puisque)', 'since'),
    ('moreover', 'moreover', 'de plus — ajouter un argument', 'de plus', '<b>Moreover</b>, the costs would be lower.', '______ , the costs would be lower. (de plus)', 'moreover'),
  ],
),

'mixed-conditionals': dict(
  level='b2', section='grammaire', num='Ch. 11', short='Mixed Conditionals',
  title='Mixed Conditionals — Mélanger les temps',
  subtitle='Si j’avais..., je serais... : passé et présent croisés',
  slides=[
    ('Pourquoi mélanger ?', None,
     '<p class="slide-explanation">La vie mélange les temps : une erreur passée a des conséquences présentes, ou un trait présent a causé un événement passé. Les conditionnels mixtes croisent donc 2e et 3e conditionnels.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>If I had taken that job, I would be in New York now.</b></p>'
     '<p style="margin-top:8px">(Si j’avais pris ce poste [passé], je serais à New York maintenant [présent].)</p></div>'),
    ('Type 1 : passé → présent', None,
     '<p class="slide-explanation"><b>If + past perfect, would + base (now)</b>. La condition est passée, la conséquence se vit maintenant.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>If we hadn’t missed the flight, we would be on the beach now.</b></p>'
     '<p style="margin-top:8px"><b>If she had studied medicine, she would be a doctor today.</b></p></div>'),
    ('Type 2 : présent → passé', None,
     '<p class="slide-explanation"><b>If + prétérit (trait permanent), would have + participe</b>. Un trait actuel explique un événement passé.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>If he were more careful, he wouldn’t have crashed the car.</b></p>'
     '<p style="margin-top:8px">(S’il était plus prudent [en général], il n’aurait pas eu cet accident [passé].)</p></div>'),
    ('Les indices temporels', None,
     '<p class="slide-explanation">Repérez <b>now, today, still</b> (conséquence présente) ou les références passées pour choisir la moitié de chaque côté.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>If I’d saved money, I wouldn’t be broke now.</b></p>'
     '<p style="margin-top:8px"><b>If I weren’t so shy, I would have spoken to her at the party.</b></p></div>'),
    ('Méthode en deux questions', None,
     '<p class="slide-explanation">1. La condition est-elle passée ou générale ? → past perfect ou prétérit. 2. La conséquence est-elle présente ou passée ? → would + base ou would have + participe.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Chaque moitié se choisit indépendamment — c’est tout le secret.</p></div>'),
  ],
  traps=[
    ('If I had taken that job, I would have been in NY now.', 'If I had taken that job, I would <strong>be</strong> in NY <strong>now</strong>.', 'Now signale une conséquence présente → would be, pas would have been.'),
    ('If he would be more careful, he wouldn’t have crashed.', 'If he <strong>were</strong> more careful...', 'Toujours pas de would après if — même dans les mixtes.'),
    ('If I didn’t miss the flight, I would be there now. (le vol est raté, hier)', 'If I <strong>hadn’t missed</strong> the flight...', 'Condition passée → past perfect : hadn’t missed.'),
    ('Si j’étais moins timide, je lui aurais parlé. → If I had been less shy... ?', 'If I <strong>weren’t</strong> so shy, I would have spoken...', 'Trait permanent actuel → prétérit (weren’t), conséquence passée → would have spoken.'),
    ('I would been rich now.', 'I would <strong>be</strong> rich now.', 'Would + base verbale : would be. Would have + participe : would have been.'),
  ],
  summary=[
    ('Passé → présent', 'if + past perfect, would + base', '...I would be in NY now.'),
    ('Présent → passé', 'if + prétérit, would have + pp', 'If he were careful, he wouldn’t have crashed.'),
    ('Indice présent', 'now, today, still', 'I wouldn’t be broke now.'),
    ('Règle d’or', 'jamais would après if', 'If I had..., if I were...'),
    ('Méthode', 'choisir chaque moitié séparément', 'condition ? conséquence ?'),
  ],
  ex1=('Choisis la bonne moitié', 'Passé ou présent, de chaque côté ?', [
    ('If I had gone to bed earlier, I ______ so tired now.', ["wouldn't be", "wouldn't have been", "won't be"], "wouldn't be",
     'Conséquence présente (now) → wouldn’t be.'),
    ('If she ______ shy, she would have introduced herself at the meeting.', ["weren't", "hadn't been just then", "wouldn't be"], "weren't",
     'Trait permanent → prétérit : if she weren’t shy.'),
    ('If we ______ the map, we wouldn’t be lost now.', ['had brought', 'brought', 'would bring'], 'had brought',
     'Condition passée (on ne l’a pas prise) → had brought.'),
    ('If he spoke better English, he ______ that job last month.', ['would have got', 'would get', 'got'], 'would have got',
     'Conséquence passée (last month) → would have got.'),
    ('If you hadn’t helped me, I ______ still ______ on it today.', ['would / be working', 'would / have worked', 'will / work'], 'would / be working',
     'Conséquence qui dure aujourd’hui → would still be working.'),
    ('If I ______ rich, I would have bought that villa years ago.', ['were', 'had been once', 'would be'], 'were',
     'Trait général (je ne suis pas riche) → if I were rich.'),
  ]),
  ex2=('Complète le conditionnel mixte', 'Écris la forme correcte.', [
    ('If I had accepted the offer, I ______ be in London now. (would)', 'would',
     'Conséquence présente → would be in London now.'),
    ('If you ______ listened to me, you wouldn’t be in trouble now. (had, à la forme négative complète : hadn’t... non — ici affirmative : had)', 'had',
     'If you HAD listened : condition passée.'),
    ('If she weren’t so stubborn, she would ______ apologised by now. (l’auxiliaire)', 'have',
     'Conséquence passée → would HAVE apologised.'),
    ('If we hadn’t sold the house, we ______ still live there. (would)', 'would',
     'Would still live (there) : conséquence présente.'),
    ('If I ______ afraid of flying, I would have visited you in Sydney. (be au prétérit négatif : weren’t)', "weren't",
     'Trait actuel → if I weren’t afraid of flying.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Si j’avais économisé, je ne serais pas fauché aujourd’hui. »', ["If I had saved money, I wouldn't be broke today.", "If I saved money, I wouldn't have been broke today.", "If I had saved money, I wouldn't have been broke today."], "If I had saved money, I wouldn't be broke today.",
     'Condition passée + conséquence présente (today).'),
    ('« S’il était plus organisé, il n’aurait pas oublié le rendez-vous. »', ["If he were more organised, he wouldn't have forgotten the appointment.", "If he had been more organised, he wouldn't be forgetting.", "If he would be organised, he didn't forget."], "If he were more organised, he wouldn't have forgotten the appointment.",
     'Trait présent (were) + conséquence passée (wouldn’t have forgotten).'),
    ('« Si nous n’avions pas raté le train, nous serions déjà arrivés. »', ["If we hadn't missed the train, we would be there by now.", "If we didn't miss the train, we would have been there.", "If we wouldn't have missed the train, we are there."], "If we hadn't missed the train, we would be there by now.",
     'Past perfect + conséquence présente (by now).'),
    ('« Si je n’étais pas si timide, j’aurais chanté au karaoké. »', ["If I weren't so shy, I would have sung at the karaoke.", "If I hadn't been shy, I would sing at the karaoke.", "If I wouldn't be shy, I had sung."], "If I weren't so shy, I would have sung at the karaoke.",
     'Trait actuel + occasion passée manquée.'),
    ('Dans un mixte, chaque moitié se choisit :', ['indépendamment, selon son propre moment', 'toujours au même temps', 'selon la longueur de la phrase'], 'indépendamment, selon son propre moment',
     'La condition et la conséquence ont chacune leur référence temporelle.'),
  ]),
  game_desc='Chaque combinaison mixte passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('past-present', 'had done → would be now', 'erreur passée, conséquence présente', 'passé vers présent', 'If I <b>had taken</b> that job, I <b>would be</b> in NY now.', 'If I had taken that job, I would ______ in NY now.', 'be'),
    ('present-past', 'were → would have done', 'trait présent, événement passé', 'présent vers passé', 'If he <b>were</b> careful, he <b>wouldn’t have crashed</b>.', 'If he ______ careful, he wouldn’t have crashed.', 'were'),
    ('now-marker', 'now / today / still', 'les indices d’une conséquence présente', 'indices temporels', "I wouldn't be broke <b>now</b>.", "I wouldn't be broke ______ . (maintenant)", 'now'),
    ('hadnt-missed', "hadn't missed", 'condition passée négative', 'condition négative', "If we <b>hadn't missed</b> the flight...", "If we ______ missed the flight... (n'avions pas)", "hadn't"),
    ('would-still', 'would still + base', 'serait encore...', 'conséquence durable', 'We <b>would still live</b> there.', 'We would ______ live there. (encore)', 'still'),
    ('werent-shy', "weren't so shy", 'si je n’étais pas si timide — trait permanent', 'trait permanent', "If I <b>weren't</b> so shy...", "If I ______ so shy... (n'étais pas)", "weren't"),
    ('would-have-2', 'would have + participe', 'la conséquence passée du mixte', 'conséquence passée', 'She would <b>have apologised</b> by now.', 'She would ______ apologised by now.', 'have'),
    ('no-would-if-2', 'jamais would après if', 'la règle survit aux mixtes', 'règle d’or', 'If I <b>had</b> known... (jamais if I would)', 'If I ______ known... (avais)', 'had'),
  ],
),

'modals-past': dict(
  level='b2', section='grammaire', num='Ch. 12', short='Modals in the Past',
  title='Modals in the Past — Should have, must have',
  subtitle='Reproches, déductions et possibilités au passé',
  slides=[
    ('Modal + have + participe', None,
     '<p class="slide-explanation">Pour projeter un modal dans le passé : <b>modal + have + participe passé</b>. Chaque combinaison a sa nuance.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>You should have called me.</b> (Tu aurais dû m’appeler.)</p>'
     '<p style="margin-top:8px"><b>She must have forgotten.</b> (Elle a dû oublier.)</p></div>'),
    ('Should have : le reproche et le regret', None,
     '<p class="slide-explanation"><b>Should have + participe</b> = aurait dû. <b>Shouldn’t have</b> = n’aurait pas dû.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I should have listened to you.</b> (J’aurais dû t’écouter.)</p>'
     '<p style="margin-top:8px"><b>You shouldn’t have said that.</b> (Tu n’aurais pas dû dire ça.)</p></div>'),
    ('Must have / can’t have : la déduction passée', None,
     '<p class="slide-explanation">Comme au présent, must (sûrement) et can’t (impossible) — mais sur un événement passé.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The ground is wet — it must have rained.</b> (Il a dû pleuvoir.)</p>'
     '<p style="margin-top:8px"><b>He can’t have finished already!</b> (Impossible qu’il ait déjà fini !)</p></div>'),
    ('Might/could have : la possibilité passée', None,
     '<p class="slide-explanation"><b>Might/could have + participe</b> = a peut-être / aurait pu.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>She might have missed the bus.</b> (Elle a peut-être raté le bus.)</p>'
     '<p style="margin-top:8px"><b>You could have been hurt!</b> (Tu aurais pu te blesser !)</p></div>'),
    ('Needn’t have : c’était inutile', None,
     '<p class="slide-explanation"><b>Needn’t have + participe</b> = a fait quelque chose qui s’est révélé inutile.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>You needn’t have brought anything — there’s plenty of food.</b></p>'
     '<p style="margin-top:8px">(Tu n’avais pas besoin d’apporter quoi que ce soit — mais tu l’as fait.)</p></div>'),
  ],
  traps=[
    ('You should called me.', 'You should <strong>have</strong> called me.', 'Le have est obligatoire : should have + participe.'),
    ('She must had forgotten.', 'She must <strong>have</strong> forgotten.', 'Modal + HAVE (jamais had) + participe.'),
    ('Il n’a pas pu finir → He mustn’t have finished.', 'He <strong>can’t have</strong> finished.', 'La déduction négative passée → can’t have, pas mustn’t have (rare en GB).'),
    ('You could have been hurt → tu as été blessé ?', 'Non : <strong>tu aurais PU te blesser</strong> (mais ça n’est pas arrivé).', 'Could have décrit un possible non réalisé.'),
    ('should of called', 'should <strong>have</strong> called', '« Should of » est une faute d’orthographe anglaise courante — c’est have (prononcé ’ve).'),
  ],
  summary=[
    ('Aurait dû', 'should have + pp', 'You should have called.'),
    ('A dû (déduction)', 'must have + pp', 'It must have rained.'),
    ('Impossible que', "can't have + pp", "He can't have finished."),
    ('A peut-être', 'might have + pp', 'She might have missed the bus.'),
    ('Aurait pu', 'could have + pp', 'You could have been hurt.'),
    ('C’était inutile', "needn't have + pp", "You needn't have brought anything."),
  ],
  ex1=('Choisis le bon modal passé', 'Reproche, déduction ou possibilité ?', [
    ('The lights were on all night — I ______ to switch them off.', ['must have forgotten', 'should forget', "can't have forgotten"], 'must have forgotten',
     'Déduction logique sur le passé → must have forgotten.'),
    ('You ______ me you were coming! I would have cooked.', ['should have told', 'must have told', 'might tell'], 'should have told',
     'Reproche → should have told (tu aurais dû me dire).'),
    ('He ______ the email — he never checks his inbox.', ["can't have read", 'must have read', 'should read'], "can't have read",
     'Impossible qu’il l’ait lu → can’t have read.'),
    ('She’s late. She ______ the train.', ['might have missed', "can't have missed", 'should have missed'], 'might have missed',
     'Hypothèse possible → might have missed.'),
    ('Don’t climb on the roof! You ______ hurt.', ['could have been', 'must have been', 'should have'], 'could have been',
     'Danger évité de justesse → could have been hurt.'),
    ('You ______ a taxi — I would have picked you up.', ["needn't have taken", "mustn't have taken", "can't have taken"], "needn't have taken",
     'Action faite mais inutile → needn’t have taken.'),
  ]),
  ex2=('Complète le modal passé', 'Écris le mot manquant.', [
    ('I should ______ listened to your advice. (l’auxiliaire)', 'have',
     'Should HAVE listened : j’aurais dû écouter.'),
    ('They must ______ left early — the car’s gone. (l’auxiliaire)', 'have',
     'Must HAVE left : ils ont dû partir tôt.'),
    ('You shouldn’t ______ spent so much. (l’auxiliaire)', 'have',
     'Shouldn’t have spent : tu n’aurais pas dû dépenser autant.'),
    ('She can’t have ______ my message — she always replies. (see → participe)', 'seen',
     'Can’t have seen : impossible qu’elle l’ait vu.'),
    ('We ______ have worried — everything went fine. (inutile de s’inquiéter : needn’t)', "needn't",
     'Needn’t have worried : on s’est inquiétés pour rien.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Tu aurais dû me prévenir. »', ['You should have warned me.', 'You must have warned me.', 'You should warned me.'], 'You should have warned me.',
     'Aurait dû → should have + participe.'),
    ('« Elle a dû rater son bus. » (j’en déduis)', ['She must have missed her bus.', 'She had to miss her bus.', 'She should have missed her bus.'], 'She must have missed her bus.',
     'Déduction passée → must have missed.'),
    ('« Impossible qu’ils soient déjà arrivés ! »', ["They can't have arrived already!", "They mustn't have arrived already!", "They shouldn't have arrived!"], "They can't have arrived already!",
     'Déduction négative → can’t have arrived.'),
    ('« On aurait pu gagner. » (mais on a perdu)', ['We could have won.', 'We could win.', 'We must have won.'], 'We could have won.',
     'Possible non réalisé → could have won.'),
    ('« Tu n’avais pas besoin de venir si tôt. » (mais tu es venu)', ["You needn't have come so early.", "You mustn't come so early.", "You didn't need coming early."], "You needn't have come so early.",
     'Action faite mais inutile → needn’t have come.'),
  ]),
  game_desc='Chaque modal passé passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('should-have', 'should have + pp', 'aurait dû — reproche ou regret', 'aurait dû', 'You <b>should have called</b> me.', 'You should ______ called me.', 'have'),
    ('shouldnt-have', "shouldn't have + pp", 'n’aurait pas dû', 'n’aurait pas dû', 'You <b>shouldn’t have said</b> that.', 'You ______ have said that. (n’aurais pas dû)', "shouldn't"),
    ('must-have', 'must have + pp', 'a dû — déduction sur le passé', 'déduction passée', 'It <b>must have rained</b>.', 'It must ______ rained. (a dû)', 'have'),
    ('cant-have', "can't have + pp", 'impossible que... ait', 'déduction négative', "He <b>can't have finished</b> already!", "He ______ have finished already! (impossible)", "can't"),
    ('might-have-p', 'might have + pp', 'a peut-être fait', 'possibilité passée', 'She <b>might have missed</b> the bus.', 'She might have ______ the bus. (raté)', 'missed'),
    ('could-have-p', 'could have + pp', 'aurait pu — non réalisé', 'aurait pu', 'You <b>could have been</b> hurt!', 'You could have ______ hurt!', 'been'),
    ('neednt-have', "needn't have + pp", 'l’a fait pour rien', 'inutile a posteriori', "You <b>needn't have brought</b> anything.", "You ______ have brought anything. (pas besoin)", "needn't"),
    ('have-not-of', 'have (jamais « of »)', 'should’ve = should have — pas should of', 'orthographe', 'You should <b>have</b> (= should’ve) called.', 'You should ______ called. (l’auxiliaire correct)', 'have'),
  ],
),

'narrative-tenses': dict(
  level='b2', section='grammaire', num='Ch. 13', short='Narrative Tenses',
  title='Narrative Tenses — Raconter comme un pro',
  subtitle='Prétérit, continu, past perfect : les trois étages du récit',
  slides=[
    ('Les trois étages d’un récit', None,
     '<p class="slide-explanation">Un bon récit anglais superpose trois temps : <b>past simple</b> (les actions), <b>past continuous</b> (le décor), <b>past perfect</b> (l’avant-histoire).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The sun was setting. We had walked all day, and we needed a place to sleep. Suddenly, we saw a light.</b></p>'
     '<p style="margin-top:8px">(décor → was setting · avant-histoire → had walked · action → saw)</p></div>'),
    ('Past perfect continuous', None,
     '<p class="slide-explanation">Le quatrième outil : <b>had been + -ing</b> — une activité qui durait déjà avant le moment du récit.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>She was exhausted because she had been driving for ten hours.</b></p>'
     '<p style="margin-top:8px">(Elle conduisait depuis dix heures — durée avant le moment raconté.)</p></div>'),
    ('Les enchaînements du récit', None,
     '<p class="slide-explanation">Les connecteurs du récit : <b>as soon as, while, by the time, meanwhile, eventually, suddenly</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>As soon as the door opened, the cat ran out.</b></p>'
     '<p style="margin-top:8px"><b>Eventually, we found the hotel.</b> (⚠ eventually = finalement, PAS « éventuellement » !)</p></div>'),
    ('Le faux ami du récit : eventually', None,
     '<p class="slide-explanation"><b>Eventually</b> = finalement, au bout du compte. « Éventuellement » (peut-être) = <b>possibly / if necessary</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>We eventually found a taxi.</b> (Nous avons fini par trouver un taxi.)</p>'
     '<p style="margin-top:8px">« Je viendrai éventuellement » → <b>I might come.</b></p></div>'),
    ('Un récit modèle', None,
     '<p class="slide-explanation">Tous les étages ensemble :</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>It was raining hard when we left. We had been planning the trip for months, so we refused to give up. While Anna was checking the map, I drove south. By the time we reached the coast, the sky had cleared.</b></p></div>'),
  ],
  traps=[
    ('Eventually = éventuellement', '<strong>Eventually = finalement</strong>', 'Le faux ami du récit. « Éventuellement » se dit possibly / might.'),
    ('When we arrived, the film started. (déjà commencé)', 'When we arrived, the film <strong>had started</strong>.', 'L’avant-histoire prend le past perfect.'),
    ('She was exhausted because she drove for ten hours.', '...because she <strong>had been driving</strong> for ten hours.', 'Durée avant le moment du récit → had been + -ing.'),
    ('While I drove, Anna was check the map.', 'While I was driving, Anna <strong>was checking</strong> the map.', 'Deux actions parallèles → deux past continuous.'),
    ('As soon as the door had opened the cat had run out. (tout en past perfect)', 'As soon as the door <strong>opened</strong>, the cat <strong>ran</strong> out.', 'Les actions en chaîne restent au past simple — le past perfect est réservé à l’avant-histoire.'),
  ],
  summary=[
    ('Actions', 'past simple', 'we saw a light'),
    ('Décor', 'past continuous', 'the sun was setting'),
    ('Avant-histoire', 'past perfect', 'we had walked all day'),
    ('Durée antérieure', 'had been + -ing', 'she had been driving for hours'),
    ('Connecteurs', 'as soon as, by the time, eventually', 'Eventually, we found it.'),
    ('Faux ami', 'eventually = finalement', '« éventuellement » = possibly'),
  ],
  ex1=('Choisis le bon temps du récit', 'Action, décor ou avant-histoire ?', [
    ('When I opened the curtains, the sun ______ .', ['was shining', 'shone once', 'had shone'], 'was shining',
     'Décor en cours → was shining.'),
    ('We arrived late because we ______ the wrong train.', ['had taken', 'took', 'were taking'], 'had taken',
     'L’erreur précède l’arrivée → had taken.'),
    ('He was out of breath — he ______ for an hour.', ['had been running', 'ran', 'was running just then'], 'had been running',
     'Durée avant le moment → had been running.'),
    ('As soon as she saw the spider, she ______ .', ['screamed', 'was screaming', 'had screamed'], 'screamed',
     'Action en chaîne → past simple : screamed.'),
    ('While we ______ , the children were playing on the beach.', ['were unpacking', 'unpacked', 'had unpacked'], 'were unpacking',
     'Deux actions parallèles → deux continus.'),
    ('______ , after three hours of waiting, the plane took off.', ['Eventually', 'Possibly', 'Actually'], 'Eventually',
     'Finalement (au bout du compte) → eventually.'),
  ]),
  ex2=('Complète le récit', 'Écris la forme correcte du verbe.', [
    ('It ______ hard when we left the house. (rain, décor)', 'was raining',
     'Décor → past continuous : was raining.'),
    ('By the time we got there, the meeting ______ . (end, avant nous)', 'had ended',
     'Fini avant notre arrivée → had ended.'),
    ('She was angry because she ______ waiting for an hour. (be — durée antérieure)', 'had been',
     'Had been waiting : elle attendait depuis une heure.'),
    ('Suddenly, the lights ______ out. (go, action)', 'went',
     'Action du récit → past simple : went out.'),
    ('______ , we found the keys under the sofa. (finalement)', 'eventually',
     'Eventually = finalement, après des recherches.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Le soleil se couchait quand nous sommes arrivés. »', ['The sun was setting when we arrived.', 'The sun set when we arrived.', 'The sun had set when we arrived later.'], 'The sun was setting when we arrived.',
     'Décor en cours → was setting.'),
    ('« Elle était épuisée car elle avait conduit toute la nuit. »', ['She was exhausted because she had been driving all night.', 'She was exhausted because she drove all night just.', 'She is exhausted because she had driven.'], 'She was exhausted because she had been driving all night.',
     'Durée antérieure → had been driving.'),
    ('« Nous avons fini par trouver un hôtel. »', ['We eventually found a hotel.', 'We eventually find a hotel.', 'We possibly found a hotel.'], 'We eventually found a hotel.',
     'Finir par → eventually + past simple.'),
    ('« Je viendrai éventuellement. » (peut-être)', ['I might come.', 'I will eventually come.', 'I come eventually.'], 'I might come.',
     '« Éventuellement » français = peut-être → might. Eventually dirait que c’est sûr, au bout du compte.'),
    ('« À peine sortis, il a commencé à pleuvoir. »', ['As soon as we went out, it started to rain.', 'As soon as we had been going out, it had rained.', 'While we went out, it was starting rain.'], 'As soon as we went out, it started to rain.',
     'Chaîne d’actions → past simples avec as soon as.'),
  ]),
  game_desc='Chaque étage du récit passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('was-setting', 'past continuous (décor)', 'le décor du récit — was/were + -ing', 'décor', 'The sun <b>was setting</b>.', 'The sun was ______ . (se couchait)', 'setting'),
    ('saw', 'past simple (action)', 'les actions qui font avancer', 'action', 'Suddenly, we <b>saw</b> a light.', 'Suddenly, we ______ a light. (avons vu)', 'saw'),
    ('had-walked', 'past perfect (avant)', 'l’avant-histoire', 'avant-histoire', 'We <b>had walked</b> all day.', 'We ______ walked all day. (avions)', 'had'),
    ('had-been-driving', 'had been + -ing', 'la durée antérieure au récit', 'durée antérieure', 'She <b>had been driving</b> for ten hours.', 'She had been ______ for ten hours. (conduisait)', 'driving'),
    ('as-soon-as', 'as soon as', 'dès que', 'dès que', '<b>As soon as</b> the door opened, the cat ran out.', 'As ______ as the door opened, the cat ran out.', 'soon'),
    ('by-the-time-n', 'by the time', 'le temps que... (tout était déjà fait)', 'by the time', '<b>By the time</b> we arrived, it had ended.', 'By the ______ we arrived, it had ended.', 'time'),
    ('eventually', 'eventually', 'finalement — le faux ami (≠ éventuellement)', 'faux ami', '<b>Eventually</b>, we found the hotel.', '______ , we found the hotel. (finalement)', 'eventually'),
    ('meanwhile', 'meanwhile', 'pendant ce temps', 'pendant ce temps', '<b>Meanwhile</b>, Anna was checking the map.', '______ , Anna was checking the map. (pendant ce temps)', 'meanwhile'),
  ],
),
}
