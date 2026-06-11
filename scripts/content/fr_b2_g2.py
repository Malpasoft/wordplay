# -*- coding: utf-8 -*-
"""fr/ B2 grammaire — lot 2 (4 chapitres)."""

CHAPTERS = {

'countable-uncountable': dict(
  level='b2', section='grammaire', num='Ch. 5', short='Countable & Uncountable',
  title='Countable & Uncountable — Les indénombrables pièges',
  subtitle='Advice, information, news : les mots qui trompent les francophones',
  slides=[
    ('Le problème : des pluriels français devenus singuliers', None,
     '<p class="slide-explanation">Des mots courants sont indénombrables en anglais alors qu’ils se comptent en français : <b>advice</b> (des conseils), <b>information</b>, <b>news</b>, <b>furniture</b> (des meubles), <b>luggage</b> (des bagages), <b>work</b>, <b>evidence</b>, <b>research</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Can I give you some advice?</b> (jamais « an advice » ni « advices »)</p>'
     '<p style="margin-top:8px"><b>The news is good.</b> (news + verbe singulier !)</p></div>'),
    ('Compter l’indénombrable : a piece of', None,
     '<p class="slide-explanation">Pour isoler une unité : <b>a piece of advice/information/furniture</b>, <b>an item of news</b>, <b>a bit of luck</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Let me give you a piece of advice.</b> (un conseil)</p>'
     '<p style="margin-top:8px"><b>Two pieces of luggage</b> (deux bagages)</p></div>'),
    ('Much, many, little, few', None,
     '<p class="slide-explanation">Indénombrable → <b>much, little</b> ; dénombrable → <b>many, few</b>. A little/a few (un peu/quelques) sont positifs ; little/few seuls sont négatifs.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I have little time.</b> (peu de temps — hélas)</p>'
     '<p style="margin-top:8px"><b>I have a little time.</b> (un peu de temps — ça va)</p></div>'),
    ('Les doubles vies', None,
     '<p class="slide-explanation">Certains mots changent de sens en changeant de catégorie : <b>a paper</b> (un journal) / <b>paper</b> (du papier), <b>a hair</b> (un poil) / <b>hair</b> (les cheveux), <b>a coffee</b> (un café commandé) / <b>coffee</b> (le café en général).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Her hair is beautiful.</b> (cheveux : singulier ! « are » est l’erreur classique)</p>'
     '<p style="margin-top:8px"><b>Two coffees, please.</b></p></div>'),
    ('Travel, trip, journey', None,
     '<p class="slide-explanation"><b>Travel</b> (indénombrable, les voyages en général) vs <b>a trip / a journey</b> (un voyage précis).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Travel broadens the mind.</b> · <b>We went on a trip to Rome.</b></p>'
     '<p style="margin-top:8px">⚠ « Un voyage » → a trip, jamais « a travel ».</p></div>'),
  ],
  traps=[
    ('She gave me some good advices.', 'She gave me some good <strong>advice</strong>.', 'Advice est indénombrable : jamais de pluriel ni de « an advice ».'),
    ('The news are good.', 'The news <strong>is</strong> good.', 'News finit par s mais est singulier : the news is...'),
    ('Her hair are so long.', 'Her hair <strong>is</strong> so long.', 'Hair (chevelure) est indénombrable singulier.'),
    ('We bought new furnitures.', 'We bought new <strong>furniture</strong>.', 'Furniture est indénombrable : some furniture, a piece of furniture.'),
    ('How was your travel?', 'How was your <strong>trip</strong>?', 'Un voyage précis = a trip/journey ; travel reste général.'),
  ],
  summary=[
    ('Indénombrables pièges', 'advice, information, news, furniture, luggage', 'some advice'),
    ('Une unité', 'a piece of + indénombrable', 'a piece of advice'),
    ('Quantité', 'much/little vs many/few', 'much time, many friends'),
    ('Positif/négatif', 'a little/a few vs little/few', 'a little time ≠ little time'),
    ('News, hair', '+ verbe singulier', 'The news is good.'),
    ('Voyage', 'a trip (jamais a travel)', 'a trip to Rome'),
  ],
  ex1=('Choisis la forme correcte', 'Dénombrable ou non ?', [
    ('He gave me ______ about the visa.', ['some information', 'an information', 'informations'], 'some information',
     'Information est indénombrable : some information.'),
    ('The news ______ better than expected.', ['is', 'are', 'be'], 'is',
     'News + verbe singulier : the news is.'),
    ('How ______ luggage are you taking?', ['much', 'many', 'few'], 'much',
     'Luggage indénombrable → how much luggage.'),
    ('Let me give you ______ of advice.', ['a piece', 'an advice', 'a few'], 'a piece',
     'Un conseil → a piece of advice.'),
    ('There were very ______ people at the meeting.', ['few', 'little', 'less little'], 'few',
     'People dénombrable pluriel → few.'),
    ('We still have ______ time — no need to rush.', ['a little', 'a few', 'few'], 'a little',
     'Time indénombrable, sens positif → a little time.'),
  ]),
  ex2=('Complète la phrase', 'Écris le mot manquant.', [
    ('Can you give me some ______ ? I don’t know what to choose. (des conseils)', 'advice',
     'Des conseils → some advice, invariable.'),
    ('Her ______ is dark and curly. (les cheveux)', 'hair',
     'La chevelure → hair, singulier : her hair is.'),
    ('We need to buy some new ______ for the flat. (des meubles)', 'furniture',
     'Des meubles → furniture, indénombrable.'),
    ('They went on a ______ to Morocco last spring. (un voyage)', 'trip',
     'Un voyage précis → a trip (jamais a travel).'),
    ('How ______ pieces of luggage can I check in? (combien)', 'many',
     'Pieces est dénombrable → how many pieces.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise correcte.', [
    ('« Merci pour tes conseils. »', ['Thanks for your advice.', 'Thanks for your advices.', 'Thanks for your an advice.'], 'Thanks for your advice.',
     'Advice invariable, même pour plusieurs conseils.'),
    ('« Les nouvelles sont bonnes. »', ['The news is good.', 'The news are good.', 'The new is good.'], 'The news is good.',
     'News = singulier malgré le s.'),
    ('« J’ai peu d’espoir. » (hélas)', ['I have little hope.', 'I have a little hope.', 'I have few hope.'], 'I have little hope.',
     'Sens négatif → little sans article. A little serait plutôt rassurant.'),
    ('« Deux cafés, s’il vous plaît. »', ['Two coffees, please.', 'Two coffee, please.', 'Two pieces of coffee, please.'], 'Two coffees, please.',
     'Au café, coffee se compte : two coffees.'),
    ('« Le voyage a duré dix heures. »', ['The journey took ten hours.', 'The travel took ten hours.', 'The travelling took ten hours there.'], 'The journey took ten hours.',
     'Un trajet précis → journey (ou trip).'),
  ]),
  game_desc='Chaque indénombrable piège passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('advice', 'advice', 'des conseils — toujours singulier', 'indénombrable n°1', 'Can I give you some <b>advice</b>?', 'Can I give you some ______ ? (conseils)', 'advice'),
    ('information', 'information', 'des informations — invariable', 'invariable', 'I need some <b>information</b>.', 'I need some ______ . (informations)', 'information'),
    ('news-is', 'the news is', 'les nouvelles — verbe au singulier', 'news singulier', 'The news <b>is</b> good.', 'The news ______ good. (sont)', 'is'),
    ('piece-of', 'a piece of', 'une unité d’indénombrable', 'compter l’incomptable', 'A <b>piece of</b> advice.', 'A ______ of advice. (un conseil)', 'piece'),
    ('luggage', 'luggage', 'des bagages — indénombrable', 'bagages', 'How much <b>luggage</b> do you have?', 'How much ______ do you have? (bagages)', 'luggage'),
    ('hair-is', 'hair is', 'les cheveux — singulier en anglais', 'cheveux', 'Her hair <b>is</b> beautiful.', 'Her hair ______ beautiful. (sont)', 'is'),
    ('a-little', 'a little / little', 'un peu (positif) vs peu (négatif)', 'nuance little', 'I have <b>a little</b> time. / I have little time.', 'I have ______ little time. (un peu — positif)', 'a'),
    ('a-trip', 'a trip', 'un voyage — jamais « a travel »', 'voyage', 'We went on a <b>trip</b> to Rome.', 'We went on a ______ to Rome. (voyage)', 'trip'),
  ],
),

'future-forms': dict(
  level='b2', section='grammaire', num='Ch. 6', short='Future Forms (B2)',
  title='Future Forms — Futur continu et futur antérieur',
  subtitle='Will be doing, will have done : les futurs avancés',
  slides=[
    ('Rappel express du B1', None,
     '<p class="slide-explanation">Will (décision/prédiction), going to (intention/signe), présent continu (agenda). Le B2 ajoute deux outils de précision.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>This time tomorrow, I’ll be flying to Rome.</b> (futur continu)</p>'
     '<p style="margin-top:8px"><b>By Friday, I’ll have finished the report.</b> (futur antérieur)</p></div>'),
    ('Will be + -ing : en plein dedans', None,
     '<p class="slide-explanation">Le futur continu décrit une action qui sera <b>en cours</b> à un moment donné — « je serai en train de ».</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Don’t call at nine — we’ll be having dinner.</b></p>'
     '<p style="margin-top:8px"><b>This time next week, she’ll be lying on a beach.</b></p></div>'),
    ('Will have + participe : déjà fait', None,
     '<p class="slide-explanation">Le futur antérieur (« j’aurai fini ») : une action achevée <b>avant</b> une échéance, presque toujours avec <b>by</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>By 2030, they will have built the new line.</b></p>'
     '<p style="margin-top:8px"><b>I’ll have left by the time you arrive.</b> (Je serai parti le temps que tu arrives.)</p></div>'),
    ('By : la préposition des échéances', None,
     '<p class="slide-explanation"><b>by Friday</b> = d’ici vendredi, au plus tard vendredi. À distinguer d’<b>until</b> (jusqu’à).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I’ll finish it by Monday.</b> (au plus tard lundi)</p>'
     '<p style="margin-top:8px"><b>I’ll work until Monday.</b> (sans interruption jusqu’à lundi)</p></div>'),
    ('Le futur poli', None,
     '<p class="slide-explanation">Will you be + -ing sert aussi à poser une question sans pression.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Will you be using the car tonight?</b> (simple curiosité — pas une demande)</p>'
     '<p style="margin-top:8px">Comparez : <b>Will you use the car tonight?</b> (presque une requête)</p></div>'),
  ],
  traps=[
    ('Demain à cette heure-ci, je vole vers Rome. → I fly to Rome.', "I<strong>'ll be flying</strong> to Rome.", 'Action en cours à un moment futur → will be + -ing.'),
    ('By Friday, I will finish the report. (déjà fini à cette date)', 'By Friday, I will <strong>have finished</strong> the report.', 'Achevé avant l’échéance → will have + participe.'),
    ('I’ll have finish by noon.', "I'll have <strong>finished</strong> by noon.", 'Will have + PARTICIPE PASSÉ : finished.'),
    ('I’ll stay here by Monday. (jusqu’à lundi)', "I'll stay here <strong>until</strong> Monday.", 'Jusqu’à = until ; by = au plus tard.'),
    ('Will you be use the car?', 'Will you be <strong>using</strong> the car?', 'Will be + -ing : using.'),
  ],
  summary=[
    ('Futur continu', 'will be + -ing', "We'll be having dinner."),
    ('Futur antérieur', 'will have + participe', "I'll have finished by Friday."),
    ('Échéance', 'by + date', 'by Monday (au plus tard)'),
    ('Jusqu’à', 'until + date', 'until Monday'),
    ('Question polie', 'Will you be + -ing?', 'Will you be using the car?'),
  ],
  ex1=('Choisis le bon futur', 'En cours, achevé, ou simple ?', [
    ('This time tomorrow, we ______ over the Atlantic.', ['will be flying', 'will fly', 'will have flown'], 'will be flying',
     'En plein vol à ce moment-là → will be flying.'),
    ('By the end of the year, she ______ her degree.', ['will have completed', 'will complete', 'will be completing'], 'will have completed',
     'Achevé avant l’échéance (by) → will have completed.'),
    ('Don’t phone at eight — they ______ dinner.', ['will be having', 'will have', 'will have had'], 'will be having',
     'Action en cours à 20 h → will be having dinner.'),
    ('I ______ everything ______ by the time you get back.', ['will have / done', 'will / do', 'will be / doing'], 'will have / done',
     'Fini avant ton retour → will have done.'),
    ('______ you ______ the printer in the next hour? (question polie)', ['Will / be using', 'Will / use urgently', 'Do / be using'], 'Will / be using',
     'Question neutre sur les plans → will you be using.'),
    ('The builders say the roof will be ready ______ Friday.', ['by', 'until', 'since'], 'by',
     'Échéance (au plus tard vendredi) → by Friday.'),
  ]),
  ex2=('Complète le futur', 'Écris la forme demandée.', [
    ('At ten tonight, I’ll ______ watching the match. (be)', 'be',
     'Will BE watching : le futur continu garde be.'),
    ('By next summer, they will ______ moved to Lyon. (have)', 'have',
     'Will HAVE moved : futur antérieur.'),
    ('She’ll be ______ in a meeting all morning. (sit → en réunion : sitting)', 'sitting',
     'Will be sitting : assise en réunion toute la matinée.'),
    ('I’ll have ______ the book by Sunday. (finish → participe)', 'finished',
     'Will have finished : je l’aurai terminé.'),
    ('We’ll have left ______ the time you arrive. (le temps que tu arrives)', 'by',
     'By the time + présent : le temps que tu arrives.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Demain à cette heure-ci, je serai en train de conduire. »', ["This time tomorrow, I'll be driving.", 'This time tomorrow, I will drive.', "This time tomorrow, I'll have driven."], "This time tomorrow, I'll be driving.",
     'En train de + moment futur → will be driving.'),
    ('« D’ici vendredi, j’aurai fini. »', ["I'll have finished by Friday.", "I'll finish until Friday.", "I'll be finishing since Friday."], "I'll have finished by Friday.",
     'Futur antérieur + by : will have finished by Friday.'),
    ('« Je travaille jusqu’à 18 h. »', ['I work until 6 p.m.', 'I work by 6 p.m.', 'I work for 6 p.m.'], 'I work until 6 p.m.',
     'Jusqu’à = until. By signifierait « au plus tard ».'),
    ('« Tu comptes utiliser la voiture ce soir ? » (sans pression)', ['Will you be using the car tonight?', 'Will you use the car tonight or not?', 'Are you using to use the car?'], 'Will you be using the car tonight?',
     'Question neutre sur les plans → will you be + -ing.'),
    ('« Le temps que tu arrives, je serai parti. »', ["I'll have left by the time you arrive.", "I'll leave when you will arrive.", "I'm leaving until you arrive."], "I'll have left by the time you arrive.",
     'Will have left + by the time + présent.'),
  ]),
  game_desc='Chaque futur avancé passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('will-be-ing', 'will be + -ing', 'serai en train de — futur continu', 'futur continu', "This time tomorrow, I<b>'ll be flying</b>.", "This time tomorrow, I'll be ______ . (en plein vol)", 'flying'),
    ('will-have-pp', 'will have + participe', 'aurai fini — futur antérieur', 'futur antérieur', "By Friday, I<b>'ll have finished</b>.", "By Friday, I'll have ______ . (fini)", 'finished'),
    ('by-deadline', 'by + échéance', 'd’ici / au plus tard', 'échéance', "I'll finish it <b>by</b> Monday.", "I'll finish it ______ Monday. (d’ici)", 'by'),
    ('until', 'until', 'jusqu’à — la durée, pas l’échéance', 'jusqu’à', "I'll work <b>until</b> Monday.", "I'll work ______ Monday. (jusqu’à)", 'until'),
    ('by-the-time', 'by the time + présent', 'le temps que tu arrives...', 'by the time', "I'll have left <b>by the time</b> you arrive.", "I'll have left by the ______ you arrive.", 'time'),
    ('will-you-be', 'Will you be + -ing?', 'la question polie sur les plans', 'question polie', '<b>Will you be using</b> the car tonight?', 'Will you be ______ the car tonight?', 'using'),
    ('wont-be', "won't be + -ing", 'ne serai pas en train de', 'négation du continu', "I <b>won't be working</b> on Sunday.", "I won't be ______ on Sunday. (en train de travailler)", 'working'),
    ('have-had', 'will have had', 'le futur antérieur de have', 'cas de have', "By July, we'll <b>have had</b> the car for ten years.", "By July, we'll have ______ the car for ten years.", 'had'),
  ],
),

'gerunds-infinitives': dict(
  level='b2', section='grammaire', num='Ch. 7', short='Gerunds & Infinitives',
  title='Gerunds & Infinitives — Le niveau supérieur',
  subtitle='Stop, remember, regret : quand le sens bascule',
  slides=[
    ('Rappel et approfondissement', None,
     '<p class="slide-explanation">Le B1 a posé les familles (want to / enjoy doing). Le B2 maîtrise les verbes qui acceptent les deux formes <b>en changeant de sens</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>remember, forget, stop, try, regret, go on, mean</b></p></div>'),
    ('Remember et forget', None,
     '<p class="slide-explanation">+ to = l’action à faire (tournée vers l’avenir) ; + -ing = le souvenir (tourné vers le passé).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Remember to lock the door.</b> (Pense à fermer !)</p>'
     '<p style="margin-top:8px"><b>I remember locking it.</b> (Je me souviens de l’avoir fermée.)</p>'
     '<p style="margin-top:8px"><b>I’ll never forget meeting her.</b> (Je n’oublierai jamais notre rencontre.)</p></div>'),
    ('Stop et try', None,
     '<p class="slide-explanation"><b>Stop doing</b> = arrêter de faire · <b>stop to do</b> = s’arrêter pour faire. <b>Try doing</b> = essayer (tester) · <b>try to do</b> = s’efforcer de.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I stopped drinking coffee.</b> / <b>I stopped to drink a coffee.</b></p>'
     '<p style="margin-top:8px"><b>Try restarting the router.</b> (teste ça) / <b>I tried to open the door, but it was locked.</b> (je me suis efforcé)</p></div>'),
    ('Regret et mean', None,
     '<p class="slide-explanation"><b>Regret doing</b> = regretter d’avoir fait · <b>regret to say</b> = avoir le regret de (formules). <b>Mean to</b> = avoir l’intention · <b>mean doing</b> = impliquer.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I regret saying that.</b> (Je regrette de l’avoir dit.)</p>'
     '<p style="margin-top:8px"><b>We regret to inform you that...</b> (Nous avons le regret de...)</p>'
     '<p style="margin-top:8px"><b>Taking this job means moving to Berlin.</b> (implique de déménager)</p></div>'),
    ('Après les adjectifs et les noms', None,
     '<p class="slide-explanation">Adjectif + to (easy to learn, happy to help) ; mais préposition → -ing (good at cooking, interested in applying, the advantage of living...).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>It’s hard to explain.</b> · <b>I’m looking forward to seeing you.</b></p>'
     '<p style="margin-top:8px"><b>There’s no point in arguing.</b> (Ça ne sert à rien de discuter.)</p></div>'),
  ],
  traps=[
    ('I stopped to smoke. (j’ai arrêté de fumer)', 'I stopped <strong>smoking</strong>.', 'Stop + -ing = arrêter de faire. Stop + to = s’arrêter pour faire autre chose.'),
    ('I regret to say that to her yesterday.', 'I regret <strong>saying</strong> that to her yesterday.', 'Regretter d’avoir fait → regret + -ing. Regret to ne sert qu’aux annonces formelles.'),
    ('Did you remember locking the door? (pense à fermer ce soir !)', 'Did you remember <strong>to lock</strong> the door?', 'L’action à accomplir → remember + to.'),
    ('There’s no point to argue.', "There's no point <strong>in arguing</strong>.", 'No point in + -ing : ça ne sert à rien de...'),
    ('Taking this job means to move to Berlin.', 'Taking this job means <strong>moving</strong> to Berlin.', 'Mean = impliquer → + -ing. Mean to = avoir l’intention.'),
  ],
  summary=[
    ('remember/forget + to', 'action à faire', 'Remember to lock the door.'),
    ('remember/forget + -ing', 'souvenir', 'I remember locking it.'),
    ('stop + -ing / + to', 'arrêter de / s’arrêter pour', 'stopped smoking / stopped to smoke'),
    ('try + -ing / + to', 'tester / s’efforcer', 'try restarting / tried to open'),
    ('regret + -ing / + to', 'regretter d’avoir / avoir le regret de', 'regret saying / regret to inform'),
    ('préposition + -ing', 'in/at/of/to(prép) + -ing', 'no point in arguing'),
  ],
  ex1=('Quel sens, quelle forme ?', 'Choisis la forme qui correspond au sens.', [
    ('Please remember ______ the plants while I’m away.', ['to water', 'watering', 'water'], 'to water',
     'Tâche à accomplir → remember to water.'),
    ('I’ll never forget ______ the Northern Lights.', ['seeing', 'to see', 'see'], 'seeing',
     'Souvenir marquant → forget + -ing : never forget seeing.'),
    ('He stopped ______ when his doctor warned him.', ['smoking', 'to smoke', 'smoke'], 'smoking',
     'Arrêter l’habitude → stop + -ing.'),
    ('We stopped ______ petrol on the way.', ['to get', 'getting', 'got'], 'to get',
     'S’arrêter dans le but de → stop + to get.'),
    ('If the screen freezes, try ______ the app.', ['restarting', 'to restart hard', 'restart'], 'restarting',
     'Suggestion à tester → try + -ing.'),
    ('We regret ______ you that the position has been filled.', ['to inform', 'informing', 'inform'], 'to inform',
     'Formule d’annonce → regret to inform you.'),
  ]),
  ex2=('Complète la phrase', 'Écris le verbe à la forme correcte.', [
    ('I regret ______ so much money on that car. (spend → regretter d’avoir dépensé)', 'spending',
     'Regret + -ing : regrette d’avoir dépensé.'),
    ('Did you remember ______ the lights? (turn off — à faire)', 'to turn off',
     'Tâche à accomplir → remember to turn off.'),
    ('There’s no point in ______ about it now. (worry)', 'worrying',
     'No point IN + -ing : worrying.'),
    ('I tried ______ the window, but it was stuck. (open — je me suis efforcé)', 'to open',
     'Effort → try to open.'),
    ('Accepting the offer would mean ______ abroad. (live — impliquerait de)', 'living',
     'Mean = impliquer → + -ing : would mean living abroad.'),
  ]),
  ex3=('Choisis la phrase qui correspond', 'Le sens bascule selon la forme.', [
    ('« Je me souviens d’avoir éteint le four. »', ['I remember turning off the oven.', 'I remember to turn off the oven.', 'I remind turning off the oven.'], 'I remember turning off the oven.',
     'Souvenir → remember + -ing.'),
    ('« Il s’est arrêté pour répondre au téléphone. »', ['He stopped to answer the phone.', 'He stopped answering the phone.', 'He stopped the phone to answer.'], 'He stopped to answer the phone.',
     'But de l’arrêt → stop + to answer.'),
    ('« Essaie de mettre moins de sel. » (suggestion à tester)', ['Try using less salt.', 'Try to use less salt with effort.', 'Try use less salt.'], 'Try using less salt.',
     'Tester une solution → try + -ing.'),
    ('« Nous avons le regret de vous informer... »', ['We regret to inform you...', 'We regret informing you...', 'We are regretting to inform...'], 'We regret to inform you...',
     'La formule administrative → regret to inform.'),
    ('« Ça ne sert à rien de crier. »', ["There's no point in shouting.", "There's no point to shout.", 'It serves nothing to shout.'], "There's no point in shouting.",
     'No point in + -ing.'),
  ]),
  game_desc='Chaque bascule de sens passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('remember-to', 'remember to do', 'penser à faire — l’action est devant soi', 'à faire', '<b>Remember to lock</b> the door!', 'Remember ______ lock the door! (pense à)', 'to'),
    ('remember-ing', 'remember doing', 'se souvenir d’avoir fait', 'souvenir', 'I remember <b>locking</b> it.', 'I remember ______ it. (l’avoir fermée)', 'locking'),
    ('stop-ing', 'stop doing', 'arrêter de faire', 'arrêter de', 'I stopped <b>drinking</b> coffee.', 'I stopped ______ coffee. (de boire)', 'drinking'),
    ('stop-to', 'stop to do', 's’arrêter pour faire', 's’arrêter pour', 'We stopped <b>to get</b> petrol.', 'We stopped ______ get petrol. (pour prendre)', 'to'),
    ('try-ing', 'try doing', 'essayer = tester une solution', 'tester', 'Try <b>restarting</b> the router.', 'Try ______ the router. (redémarrer, pour voir)', 'restarting'),
    ('try-to', 'try to do', 's’efforcer de faire', 's’efforcer', 'I tried <b>to open</b> the door.', 'I tried ______ open the door. (me suis efforcé d’)', 'to'),
    ('regret-ing', 'regret doing', 'regretter d’avoir fait', 'regret du passé', 'I regret <b>saying</b> that.', 'I regret ______ that. (de l’avoir dit)', 'saying'),
    ('no-point', 'no point in doing', 'ça ne sert à rien de', 'inutilité', "There's no point <b>in arguing</b>.", "There's no point in ______ . (discuter)", 'arguing'),
  ],
),

'hypothetical-meaning': dict(
  level='b2', section='grammaire', num='Ch. 8', short='Hypothetical Meaning',
  title='Hypothetical Meaning — Would rather, it’s time, as if',
  subtitle='Les tournures de l’irréel au-delà de if',
  slides=[
    ('Le prétérit irréel, partout', None,
     '<p class="slide-explanation">Vous connaissez déjà le prétérit irréel (second conditional, wish). D’autres tournures l’exigent aussi : <b>would rather, it’s time, as if/as though, suppose</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I’d rather you stayed.</b> (Je préférerais que tu restes.)</p>'
     '<p style="margin-top:8px"><b>It’s time we left.</b> (Il est temps qu’on parte.)</p></div>'),
    ('Would rather : préférer', None,
     '<p class="slide-explanation">Même sujet → <b>’d rather + base verbale</b>. Sujet différent → <b>’d rather + sujet + prétérit</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I’d rather stay at home.</b> (Je préférerais rester.)</p>'
     '<p style="margin-top:8px"><b>I’d rather you didn’t tell anyone.</b> (Je préférerais que tu ne le dises à personne.)</p></div>'
     '<p style="margin-top:16px">Le subjonctif français (« que tu restes ») devient un simple prétérit anglais.</p>'),
    ('It’s time : il est temps que', None,
     '<p class="slide-explanation"><b>It’s time + sujet + prétérit</b> — ou it’s time to + infinitif si le sujet est général. <b>It’s high time</b> renforce l’urgence.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>It’s time we went home.</b> · <b>It’s time to go.</b></p>'
     '<p style="margin-top:8px"><b>It’s high time you found a job!</b> (Il serait grand temps que...)</p></div>'),
    ('As if / as though : comme si', None,
     '<p class="slide-explanation">« Comme si » + irréel → <b>as if + prétérit</b> (ou past perfect pour le passé). Avec be : were.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>He acts as if he were the boss.</b> (Il se comporte comme s’il était le patron.)</p>'
     '<p style="margin-top:8px"><b>She looked as if she had seen a ghost.</b></p></div>'),
    ('Suppose / What if', None,
     '<p class="slide-explanation"><b>Suppose/Supposing + prétérit</b> = et si... ? <b>What if + prétérit</b> : même logique que if.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Suppose we moved to the coast?</b> (Et si on déménageait sur la côte ?)</p>'
     '<p style="margin-top:8px"><b>What if it rained during the ceremony?</b></p></div>'),
  ],
  traps=[
    ('I’d rather that you stay. (préférerais que tu restes)', "I'd rather you <strong>stayed</strong>.", 'Sujet différent → prétérit irréel : I’d rather you stayed.'),
    ('It’s time we go.', "It's time we <strong>went</strong>.", 'It’s time + sujet → prétérit : went.'),
    ('He acts as if he is the boss. (il ne l’est pas)', 'He acts as if he <strong>were</strong> the boss.', 'Irréel → were. « Is » laisserait croire qu’il est peut-être bien le patron.'),
    ('I’d rather to stay at home.', "I'd rather <strong>stay</strong> at home.", 'Would rather + base verbale, sans to.'),
    ('Comme si rien ne s’était passé → as if nothing happened ?', 'as if nothing <strong>had happened</strong>', 'Irréel du passé → past perfect : had happened.'),
  ],
  summary=[
    ('Préférer (soi)', '’d rather + base', "I'd rather stay."),
    ('Préférer (autrui)', '’d rather + sujet + prétérit', "I'd rather you stayed."),
    ('Il est temps que', "it's (high) time + prétérit", "It's time we left."),
    ('Comme si', 'as if/as though + prétérit/were', 'as if he were the boss'),
    ('Et si... ?', 'suppose / what if + prétérit', 'Suppose we moved?'),
  ],
  ex1=('Choisis la forme correcte', 'L’irréel se cache partout.', [
    ('I’d rather you ______ smoke in here.', ["didn't", "don't", "won't"], "didn't",
     'Sujet différent → prétérit : I’d rather you didn’t smoke.'),
    ('It’s time the children ______ to bed.', ['went', 'go', 'will go'], 'went',
     'It’s time + sujet + prétérit : went.'),
    ('He spends money as if he ______ a millionaire.', ['were', 'is', 'would be'], 'were',
     'Comme si (irréel) → were.'),
    ('I’d rather ______ at home tonight.', ['stay', 'to stay', 'staying'], 'stay',
     'Même sujet → ’d rather + base verbale.'),
    ('She looked as if she ______ a ghost.', ['had seen', 'sees', 'would see'], 'had seen',
     'Irréel du passé → past perfect : had seen.'),
    ('______ we sold the car and bought bikes?', ['Suppose', 'If only', 'Unless'], 'Suppose',
     'Et si... ? → Suppose + prétérit : Suppose we sold...'),
  ]),
  ex2=('Complète la phrase', 'Écris la forme correcte.', [
    ('It’s high time you ______ a decision. (make)', 'made',
     'It’s high time + prétérit : made.'),
    ('I’d rather you ______ me the truth. (tell)', 'told',
     'Préférer que l’autre fasse → prétérit : told.'),
    ('He talks as if he ______ everything. (know)', 'knew',
     'Comme s’il savait tout → knew.'),
    ('What if we ______ the early train? (take — et si on prenait ?)', 'took',
     'What if + prétérit : took.'),
    ('I’d rather ______ than take the bus. (walk)', 'walk',
     'Même sujet → base verbale : I’d rather walk.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Je préférerais que tu ne dises rien. »', ["I'd rather you didn't say anything.", "I'd rather you don't say anything.", "I'd rather that you say nothing."], "I'd rather you didn't say anything.",
     'Sujet différent → didn’t (prétérit irréel).'),
    ('« Il est temps qu’on parte. »', ["It's time we left.", "It's time we leave.", "It's time that we will leave."], "It's time we left.",
     'It’s time + prétérit : left.'),
    ('« Il agit comme s’il était le patron. »', ['He acts as if he were the boss.', 'He acts as if he is the boss.', 'He acts like he be the boss.'], 'He acts as if he were the boss.',
     'Irréel → were.'),
    ('« Elle a continué comme si rien ne s’était passé. »', ['She carried on as if nothing had happened.', 'She carried on as if nothing happened just then truly.', 'She carried on as if nothing happens.'], 'She carried on as if nothing had happened.',
     'Irréel du passé → had happened.'),
    ('« Et si on déménageait ? »', ['Suppose we moved?', 'Suppose we move now?', 'What if we will move?'], 'Suppose we moved?',
     'Suppose + prétérit pour l’hypothèse.'),
  ]),
  game_desc='Chaque tournure hypothétique passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('rather-base', "'d rather + base", 'je préférerais faire — même sujet', 'préférence (soi)', "I<b>'d rather stay</b> at home.", "I'd rather ______ at home. (rester)", 'stay'),
    ('rather-past', "'d rather you + prétérit", 'je préférerais que tu... — sujet différent', 'préférence (autrui)', "I'd rather you <b>stayed</b>.", "I'd rather you ______ . (restes)", 'stayed'),
    ('its-time', "it's time + prétérit", 'il est temps que...', 'il est temps', "It's time we <b>left</b>.", "It's time we ______ . (parte)", 'left'),
    ('high-time', "it's high time", 'il serait grand temps', 'grand temps', "It's <b>high</b> time you found a job!", "It's ______ time you found a job!", 'high'),
    ('as-if-were', 'as if + were', 'comme s’il était...', 'comme si', 'He acts as if he <b>were</b> the boss.', 'He acts as if he ______ the boss.', 'were'),
    ('as-if-had', 'as if + past perfect', 'comme si rien ne s’était passé', 'comme si (passé)', 'As if nothing <b>had happened</b>.', 'As if nothing ______ happened.', 'had'),
    ('suppose', 'suppose + prétérit', 'et si on... ?', 'et si', '<b>Suppose</b> we moved to the coast?', '______ we moved to the coast? (et si)', 'suppose'),
    ('what-if', 'what if + prétérit', 'et si... ? — la variante', 'what if', '<b>What if</b> it rained?', '______ ______ it rained? (et si)', 'what if'),
  ],
),
}
