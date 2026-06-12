# -*- coding: utf-8 -*-
"""fr/ A2 grammaire — lot 2 (chapitres 6-10). Explications en français, anglais cible."""

CHAPTERS = {

'modal-could-might': dict(
  level='a2', section='grammaire', num='Ch. 6', short='Could et might',
  title='Could et might — capacité passée et possibilité',
  subtitle='Deux modaux pour le passé de can et pour dire « peut-être »',
  slides=[
    ('Could : le passé de can', None,
     '<p class="slide-explanation"><b>Could</b> est d\'abord le passé de can : il exprime une <b>capacité dans le passé</b> — ce qu\'on savait faire. Comme tous les modaux, il est suivi de la base verbale, sans to.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>could swim</b> when I was five. — Je savais nager à cinq ans.</p>'
     '<p style="margin-top:8px">She <b>could read</b> at four. — Elle savait lire à quatre ans.</p>'
     '<p style="margin-top:8px">Négation : I <b>couldn\'t sleep</b> last night. — Je n\'ai pas pu dormir cette nuit.</p></div>'
     '<p style="margin-top:16px">Une seule forme pour toutes les personnes : I could, she could, they could.</p>'),
    ('Could : la possibilité', None,
     '<p class="slide-explanation">Could exprime aussi une <b>possibilité</b> dans le présent ou le futur : « ça pourrait arriver ». C\'est notre conditionnel « pourrait ».</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>It <b>could rain</b> this afternoon. — Il pourrait pleuvoir cet après-midi.</p>'
     '<p style="margin-top:8px">We <b>could go</b> to the beach tomorrow. — On pourrait aller à la plage demain. (suggestion)</p>'
     '<p style="margin-top:8px"><b>Could you help</b> me, please? — Pourriez-vous m\'aider ? (demande polie)</p></div>'
     '<p style="margin-top:16px">Could you...? est plus poli que Can you...? — comme « pourriez-vous » face à « pouvez-vous ».</p>'),
    ('Might : peut-être, mais sans certitude', None,
     '<p class="slide-explanation"><b>Might</b> exprime une possibilité <b>incertaine</b> : « il se peut que », « peut-être ». La probabilité est plus faible ou plus vague qu\'avec could.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>might come</b> tonight, but I\'m not sure. — Je viendrai peut-être ce soir, mais je ne suis pas sûr.</p>'
     '<p style="margin-top:8px">She <b>might be</b> at home. — Elle est peut-être chez elle.</p>'
     '<p style="margin-top:8px">Négation : He <b>might not come</b>. — Il se peut qu\'il ne vienne pas.</p></div>'
     '<p style="margin-top:16px">Astuce : « peut-être que je viendrai » → I might come. Pas besoin de maybe quand might est là !</p>'),
    ('Modal + base verbale : la règle d\'or', None,
     '<p class="slide-explanation">Could et might suivent les règles de tous les modaux : <b>jamais de to</b> après eux, <b>jamais de -s</b>, et négation avec <b>not</b> directement (pas de don\'t).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>She might <b>be</b> late. (et non « might to be » ni « might is »)</p>'
     '<p style="margin-top:8px">It could <b>rain</b>. (et non « could rains »)</p>'
     '<p style="margin-top:8px">He <b>might not</b> know. (et non « he don\'t might know »)</p></div>'
     '<p style="margin-top:16px">Le verbe après un modal est toujours nu : ni to, ni -s, ni -ing, ni -ed.</p>'),
    ('Can, could ou might ? Le choix', None,
     '<p class="slide-explanation">Trois nuances de possibilité, du plus sûr au moins sûr. Compare :</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>can</b> — capacité ou possibilité réelle : I can swim. — Je sais nager.</p>'
     '<p style="margin-top:8px"><b>could</b> — capacité passée ou possibilité : I could swim at five. / It could rain.</p>'
     '<p style="margin-top:8px"><b>might</b> — possibilité incertaine : It might rain, who knows? — Il pleuvra peut-être, qui sait ?</p></div>'
     '<p style="margin-top:16px">Pour une demande polie, la politesse monte aussi : Can you...? → Could you...? (pourriez-vous).</p>'),
  ],
  traps=[
    ('I could to swim when I was five.', 'I could <strong>swim</strong> when I was five.', 'Les modaux ne sont jamais suivis de to : could SWIM.'),
    ('She might comes tonight.', 'She might <strong>come</strong> tonight.', 'Après un modal, base verbale sans -s : might COME.'),
    ('He don\'t could sleep.', 'He <strong>couldn\'t</strong> sleep.', 'La négation d\'un modal se fait avec not : couldn\'t — jamais avec don\'t.'),
    ('Maybe I might will come.', 'I <strong>might come</strong>.', 'Un seul modal par verbe : might suffit pour dire « peut-être » — pas de will ni de maybe en plus.'),
    ('Do you could help me?', '<strong>Could you</strong> help me?', 'La question d\'un modal se fait par inversion : COULD you help me? Jamais do.'),
  ],
  summary=[
    ('Capacité passée', 'could + base verbale', 'I could swim when I was five.'),
    ('Possibilité', 'could + base verbale', 'It could rain this afternoon.'),
    ('Demande polie', 'Could you...?', 'Could you help me, please?'),
    ('Peut-être', 'might + base verbale', 'I might come tonight.'),
    ('Négations', 'couldn\'t · might not', 'I couldn\'t sleep. / He might not come.'),
    ('Règle des modaux', 'jamais to, -s, ni don\'t', 'She might be late.'),
  ],
  ex1=('Could ou might ?', 'Capacité passée, suggestion ou possibilité incertaine ?', [
    ('I ______ read when I was four.', ['could', 'might', 'can to'], 'could',
     'Capacité dans le passé → COULD : I could read at four.'),
    ('Take an umbrella — it ______ rain later.', ['might', 'could to', 'mights'], 'might',
     'Possibilité incertaine → MIGHT rain.'),
    ('______ you open the window, please?', ['Could', 'Might', 'Do'], 'Could',
     'Demande polie → COULD you...? (pourriez-vous).'),
    ('She ______ be at home — call her.', ['might', 'might to', 'don\'t might'], 'might',
     '« Elle est peut-être chez elle » → she MIGHT BE at home.'),
    ('I ______ sleep last night because of the noise.', ['couldn\'t', 'might not', 'don\'t could'], 'couldn\'t',
     'Incapacité passée → COULDN\'T sleep.'),
    ('After might, le verbe est nu : He might ______ late.', ['be', 'is', 'to be'], 'be',
     'Modal + base verbale : might BE late.'),
  ]),
  ex2=('Complète avec le bon modal', 'Écris could, couldn\'t ou might.', [
    ('« Je savais nager à cinq ans. » → I ______ swim when I was five. (un mot)', 'could',
     'Capacité passée → COULD swim.'),
    ('« Il viendra peut-être. » → He ______ come. (un mot)', 'might',
     'Peut-être → MIGHT come, sans maybe en plus.'),
    ('« Je n\'ai pas pu dormir. » → I ______ sleep. (un mot)', 'couldn\'t',
     'Incapacité passée → COULDN\'T sleep.'),
    ('« Pourriez-vous m\'aider ? » → ______ you help me? (un mot)', 'Could',
     'Demande polie → COULD you help me?'),
    ('« On pourrait aller au cinéma. » (suggestion) → We ______ go to the cinema. (un mot)', 'could',
     'Suggestion → we COULD go.'),
  ]),
  ex3=('Trouve la phrase correcte', 'Rappelle-toi : modal + base verbale nue.', [
    ('« Elle savait lire à quatre ans. »', ['She could read at four.', 'She could to read at four.', 'She can read at four years ago.'], 'She could read at four.',
     'Could + base verbale READ, sans to.'),
    ('« Il se peut qu\'il pleuve. »', ['It might rain.', 'It might rains.', 'It might to rain.'], 'It might rain.',
     'Might + base verbale RAIN — ni -s ni to.'),
    ('« Je ne pourrai peut-être pas venir. »', ['I might not come.', 'I don\'t might come.', 'I might not to come.'], 'I might not come.',
     'Négation d\'un modal : might NOT + base verbale.'),
    ('« Pourrais-tu fermer la porte ? »', ['Could you close the door?', 'Do you could close the door?', 'Could you to close the door?'], 'Could you close the door?',
     'Inversion : COULD you close...? Jamais do avec un modal.'),
    ('« Elle est peut-être au bureau. »', ['She might be at the office.', 'She might is at the office.', 'Maybe she might will be at the office.'], 'She might be at the office.',
     'Might + BE (base verbale) : un seul modal suffit.'),
  ]),
  game_desc='Chaque emploi de could et might passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('could-past', 'could (capacité passée)', 'savait faire — le passé de can', 'capacité passée', 'I <b>could</b> swim when I was five.', 'I ______ swim when I was five. (savais)', 'could'),
    ('couldnt', 'couldn\'t', 'n\'a pas pu — négation de could', 'incapacité', 'I <b>couldn\'t</b> sleep last night.', 'I ______ sleep last night. (n\'ai pas pu)', 'couldn\'t'),
    ('could-possib', 'could (possibilité)', 'pourrait — possibilité présente ou future', 'pourrait', 'It <b>could</b> rain this afternoon.', 'It ______ rain this afternoon. (pourrait)', 'could'),
    ('could-you', 'Could you...?', 'pourriez-vous — demande polie', 'demande polie', '<b>Could</b> you help me, please?', '______ you help me, please? (pourriez-vous)', 'could'),
    ('might', 'might', 'peut-être — possibilité incertaine', 'peut-être', 'I <b>might</b> come tonight.', 'I ______ come tonight. (peut-être)', 'might'),
    ('might-be', 'might be', 'est peut-être — might + be', 'might + be', 'She might <b>be</b> at home.', 'She might ______ at home. (être)', 'be'),
    ('might-not', 'might not', 'peut-être pas — négation de might', 'négation', 'He might <b>not</b> come.', 'He might ______ come. (négation)', 'not'),
    ('bare-verb', 'modal + base verbale', 'après un modal — verbe nu, sans to ni -s', 'verbe nu', 'She might <b>come</b> tomorrow.', 'She might ______ tomorrow. (venir)', 'come'),
  ],
),

'modal-must-should': dict(
  level='a2', section='grammaire', num='Ch. 7', short='Must et should',
  title='Must et should — obligation et conseil',
  subtitle='Devoir fort, conseil ami — et le piège mustn\'t vs don\'t have to',
  slides=[
    ('Must : l\'obligation forte', None,
     '<p class="slide-explanation"><b>Must</b> exprime une <b>obligation forte</b> : règle, loi, ou nécessité que le locuteur impose. Comme tous les modaux : base verbale, pas de to, pas de -s.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>You <b>must wear</b> a seatbelt. — Tu dois mettre ta ceinture. (la loi)</p>'
     '<p style="margin-top:8px">I <b>must finish</b> this today. — Je dois finir ça aujourd\'hui.</p>'
     '<p style="margin-top:8px">Students <b>must arrive</b> on time. — Les élèves doivent arriver à l\'heure.</p></div>'
     '<p style="margin-top:16px">Have to exprime aussi l\'obligation : You <b>have to</b> wear a uniform. Au quotidien, have to est même plus fréquent que must.</p>'),
    ('Should : le conseil', None,
     '<p class="slide-explanation"><b>Should</b> donne un <b>conseil</b> : « tu devrais ». C\'est plus doux que must — on recommande, on n\'impose pas.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>You <b>should see</b> a doctor. — Tu devrais voir un médecin.</p>'
     '<p style="margin-top:8px">He <b>should study</b> more. — Il devrait étudier davantage.</p>'
     '<p style="margin-top:8px">Négation : You <b>shouldn\'t eat</b> so much sugar. — Tu ne devrais pas manger autant de sucre.</p></div>'
     '<p style="margin-top:16px">Compare : You MUST stop (obligation, c\'est la règle) / You SHOULD stop (conseil, c\'est mieux pour toi).</p>'),
    ('LE PIÈGE : mustn\'t ≠ don\'t have to', None,
     '<p class="slide-explanation">Attention, les deux négations n\'ont <b>rien à voir</b> ! <b>Mustn\'t</b> = interdiction (« il ne faut pas »). <b>Don\'t have to</b> = absence d\'obligation (« tu n\'es pas obligé »).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>You <b>mustn\'t smoke</b> here. — Il est interdit de fumer ici. (interdiction !)</p>'
     '<p style="margin-top:8px">You <b>don\'t have to come</b>. — Tu n\'es pas obligé de venir. (c\'est ton choix)</p></div>'
     '<p style="margin-top:16px">Le calque français trompe : « tu ne dois pas » peut vouloir dire les deux — l\'anglais, lui, distingue toujours interdiction et liberté.</p>'),
    ('Must : la déduction logique', None,
     '<p class="slide-explanation">Must a un deuxième emploi : la <b>déduction</b>. Quand tous les indices mènent à une conclusion, on dit must be — « ça doit être... ».</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>She works twelve hours a day — she <b>must be</b> tired. — Elle doit être fatiguée.</p>'
     '<p style="margin-top:8px">The lights are off. They <b>must be</b> asleep. — Ils doivent dormir.</p>'
     '<p style="margin-top:8px">You\'ve walked 20 km — you <b>must be</b> hungry! — Tu dois avoir faim !</p></div>'
     '<p style="margin-top:16px">Même logique qu\'en français : « elle doit être fatiguée » = conclusion évidente, pas obligation.</p>'),
    ('Questions et réponses avec should', None,
     '<p class="slide-explanation">Pour demander un conseil : <b>Should I...?</b> — « est-ce que je devrais... ? ». L\'inversion suffit, jamais de do.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Should I call</b> her? — Devrais-je l\'appeler ?</p>'
     '<p style="margin-top:8px"><b>What should I do?</b> — Que devrais-je faire ?</p>'
     '<p style="margin-top:8px">Réponses : Yes, you <b>should</b>. / No, you <b>shouldn\'t</b>.</p></div>'
     '<p style="margin-top:16px">« What should I do? » est LA phrase pour demander conseil — apprends-la en bloc.</p>'),
  ],
  traps=[
    ('You must to wear a seatbelt.', 'You must <strong>wear</strong> a seatbelt.', 'Must est un modal : jamais de to après lui — must WEAR.'),
    ('He should studies more.', 'He should <strong>study</strong> more.', 'Après should, base verbale sans -s : should STUDY.'),
    ('You mustn\'t come if you don\'t want. (= pas obligé)', 'You <strong>don\'t have to</strong> come if you don\'t want.', 'Pas obligé = don\'t have to. Mustn\'t signifierait que c\'est INTERDIT de venir !'),
    ('You don\'t have to smoke here. (panneau d\'interdiction)', 'You <strong>mustn\'t</strong> smoke here.', 'Interdiction = mustn\'t. Don\'t have to dirait juste « tu n\'es pas obligé de fumer » !'),
    ('Do I should call her?', '<strong>Should I</strong> call her?', 'Question d\'un modal par inversion : SHOULD I call her? Jamais do.'),
  ],
  summary=[
    ('Obligation forte', 'must + base verbale', 'You must wear a seatbelt.'),
    ('Conseil', 'should + base verbale', 'You should see a doctor.'),
    ('Interdiction', 'mustn\'t', 'You mustn\'t smoke here.'),
    ('Pas obligé', 'don\'t have to', 'You don\'t have to come.'),
    ('Déduction', 'must be', 'She must be tired.'),
    ('Demander conseil', 'Should I...?', 'What should I do?'),
  ],
  ex1=('Must, mustn\'t, should ou don\'t have to ?', 'Obligation, interdiction, conseil ou liberté ?', [
    ('You ______ wear a helmet on a motorbike.', ['must', 'should maybe', 'don\'t have to'], 'must',
     'C\'est la loi → obligation forte : MUST wear.'),
    ('You look tired. You ______ go to bed early.', ['should', 'must to', 'mustn\'t'], 'should',
     'Conseil ami → SHOULD go to bed.'),
    ('You ______ smoke in the hospital.', ['mustn\'t', 'don\'t have to', 'shouldn\'t maybe'], 'mustn\'t',
     'Interdiction → MUSTN\'T smoke.'),
    ('The ticket is free — you ______ pay.', ['don\'t have to', 'mustn\'t', 'must'], 'don\'t have to',
     'Pas d\'obligation (c\'est gratuit) → DON\'T HAVE TO pay.'),
    ('She has worked all day. She ______ be exhausted.', ['must', 'should to', 'don\'t have to'], 'must',
     'Déduction logique → she MUST BE exhausted.'),
    ('After should, le verbe est nu : He should ______ more water.', ['drink', 'drinks', 'to drink'], 'drink',
     'Modal + base verbale : should DRINK.'),
  ]),
  ex2=('Complète avec le bon modal', 'Écris must, mustn\'t, should ou shouldn\'t.', [
    ('« Tu devrais voir un médecin. » → You ______ see a doctor. (un mot)', 'should',
     'Conseil → SHOULD see.'),
    ('« Il est interdit de courir ici. » → You ______ run here. (un mot)', 'mustn\'t',
     'Interdiction → MUSTN\'T run.'),
    ('« Je dois finir ce soir. » → I ______ finish tonight. (un mot)', 'must',
     'Obligation forte → MUST finish.'),
    ('« Tu ne devrais pas manger autant. » → You ______ eat so much. (un mot)', 'shouldn\'t',
     'Conseil négatif → SHOULDN\'T eat.'),
    ('« Elle doit être fatiguée. » (déduction) → She ______ be tired. (un mot)', 'must',
     'Déduction logique → MUST be tired.'),
  ]),
  ex3=('Interdiction ou liberté ?', 'Le grand test mustn\'t vs don\'t have to.', [
    ('« Tu n\'es pas obligé de venir. »', ['You don\'t have to come.', 'You mustn\'t come.', 'You shouldn\'t to come.'], 'You don\'t have to come.',
     'Absence d\'obligation → DON\'T HAVE TO. Mustn\'t = interdit !'),
    ('« Défense d\'entrer. »', ['You mustn\'t enter.', 'You don\'t have to enter.', 'You should enter.'], 'You mustn\'t enter.',
     'Interdiction → MUSTN\'T enter.'),
    ('« Devrais-je l\'appeler ? »', ['Should I call her?', 'Do I should call her?', 'Must I to call her?'], 'Should I call her?',
     'Question par inversion : SHOULD I call her?'),
    ('« Les lumières sont éteintes : ils doivent dormir. »', ['They must be asleep.', 'They must to be asleep.', 'They don\'t have to sleep.'], 'They must be asleep.',
     'Déduction → MUST BE asleep, sans to.'),
    ('« C\'est samedi : je ne suis pas obligé de me lever tôt. »', ['I don\'t have to get up early.', 'I mustn\'t get up early.', 'I shouldn\'t have get up early.'], 'I don\'t have to get up early.',
     'Liberté, pas interdiction → DON\'T HAVE TO get up.'),
  ]),
  game_desc='Chaque emploi de must et should passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('must', 'must', 'obligation forte — règle ou loi', 'obligation', 'You <b>must</b> wear a seatbelt.', 'You ______ wear a seatbelt. (obligation)', 'must'),
    ('should', 'should', 'conseil — tu devrais', 'conseil', 'You <b>should</b> see a doctor.', 'You ______ see a doctor. (devrais)', 'should'),
    ('mustnt', 'mustn\'t', 'interdiction — il ne faut pas', 'interdit', 'You <b>mustn\'t</b> smoke here.', 'You ______ smoke here. (interdiction)', 'mustn\'t'),
    ('dont-have-to', 'don\'t have to', 'pas obligé — absence d\'obligation', 'pas obligé', 'You <b>don\'t have to</b> come.', 'You don\'t ______ to come. (obligation absente)', 'have'),
    ('shouldnt', 'shouldn\'t', 'tu ne devrais pas — conseil négatif', 'conseil négatif', 'You <b>shouldn\'t</b> eat so much sugar.', 'You ______ eat so much sugar. (ne devrais pas)', 'shouldn\'t'),
    ('must-be', 'must be (déduction)', 'doit être — conclusion logique', 'déduction', 'She works so much — she must <b>be</b> tired.', 'She works so much — she must ______ tired. (être)', 'be'),
    ('should-i', 'Should I...?', 'devrais-je — demander un conseil', 'demande de conseil', '<b>Should</b> I call her?', '______ I call her? (devrais-je)', 'should'),
    ('have-to', 'have to', 'devoir — l\'obligation du quotidien', 'obligation courante', 'I <b>have</b> to work on Saturdays.', 'I ______ to work on Saturdays. (dois)', 'have'),
  ],
),

'comparatives-basic': dict(
  level='a2', section='grammaire', num='Ch. 8', short='Comparatif et superlatif',
  title='Comparatif et superlatif — taller, more beautiful, the best',
  subtitle='Comparer en anglais : -er/-est ou more/most, jamais les deux !',
  slides=[
    ('Adjectifs courts : -er + than', None,
     '<p class="slide-explanation">Pour comparer avec un adjectif <b>court</b> (1 syllabe, ou 2 finissant en -y), on ajoute <b>-er</b> et on utilise <b>than</b> (que).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Tom is <b>taller than</b> me. — Tom est plus grand que moi.</p>'
     '<p style="margin-top:8px">This book is <b>cheaper than</b> that one. — Ce livre est moins cher que celui-là.</p>'
     '<p style="margin-top:8px">Orthographe : big → <b>bigger</b> (consonne doublée) · happy → <b>happier</b> (y → i)</p></div>'
     '<p style="margin-top:16px">« Que » de comparaison = <b>than</b> — ne le confonds pas avec that !</p>'),
    ('Adjectifs longs : more + adjectif', None,
     '<p class="slide-explanation">Pour les adjectifs <b>longs</b> (2 syllabes ou plus), pas de -er : on place <b>more</b> devant l\'adjectif, qui ne change pas.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>This film is <b>more interesting than</b> the book. — Ce film est plus intéressant que le livre.</p>'
     '<p style="margin-top:8px">She is <b>more famous than</b> her brother. — Elle est plus célèbre que son frère.</p>'
     '<p style="margin-top:8px">Moins... que : <b>less expensive than</b> — moins cher que.</p></div>'
     '<p style="margin-top:16px">Règle simple : court → -er · long → more. Jamais les deux à la fois !</p>'),
    ('Le superlatif : the -est / the most', None,
     '<p class="slide-explanation">Le superlatif (« le plus... ») suit la même logique : <b>the + adjectif-est</b> pour les courts, <b>the most + adjectif</b> pour les longs.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Tom is <b>the tallest</b> in the class. — Tom est le plus grand de la classe.</p>'
     '<p style="margin-top:8px">This is <b>the most expensive</b> restaurant in town. — C\'est le restaurant le plus cher de la ville.</p>'
     '<p style="margin-top:8px">Remarque : « de la classe / du monde » = <b>in</b> the class, <b>in</b> the world.</p></div>'
     '<p style="margin-top:16px">N\'oublie pas le <b>the</b> : the tallest, the most famous.</p>'),
    ('Les irréguliers : good, bad, far', None,
     '<p class="slide-explanation">Trois adjectifs très fréquents ont des formes irrégulières à mémoriser absolument.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>good → <b>better</b> → <b>the best</b> : This pizza is better than mine. — Meilleure que la mienne.</p>'
     '<p style="margin-top:8px">bad → <b>worse</b> → <b>the worst</b> : The weather is worse today. — Le temps est pire aujourd\'hui.</p>'
     '<p style="margin-top:8px">far → <b>farther/further</b> → <b>the farthest</b> : My house is farther. — Ma maison est plus loin.</p></div>'
     '<p style="margin-top:16px">PIÈGE n°1 : « more better » n\'existe PAS. Better est déjà un comparatif — more good non plus !</p>'),
    ('L\'égalité : as... as', None,
     '<p class="slide-explanation">Pour dire « aussi... que », on encadre l\'adjectif avec <b>as... as</b>. À la négative : <b>not as... as</b> (pas aussi... que).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>She is <b>as tall as</b> her mother. — Elle est aussi grande que sa mère.</p>'
     '<p style="margin-top:8px">This exercise is <b>not as difficult as</b> the last one. — Pas aussi difficile que le dernier.</p>'
     '<p style="margin-top:8px">L\'adjectif reste à sa forme de base entre les deux as.</p></div>'
     '<p style="margin-top:16px">Trois outils donc : -er/more + than · the -est/most · as... as. Choisis selon le sens !</p>'),
  ],
  traps=[
    ('This film is more better than the book.', 'This film is <strong>better</strong> than the book.', '« More better » n\'existe pas : better est déjà le comparatif de good.'),
    ('Tom is taller that me.', 'Tom is taller <strong>than</strong> me.', 'Le « que » de comparaison est THAN, pas that : taller THAN me.'),
    ('She is more tall than her brother.', 'She is <strong>taller</strong> than her brother.', 'Tall est court → -er : TALLER. More est réservé aux adjectifs longs.'),
    ('It\'s the most cheap restaurant.', 'It\'s the <strong>cheapest</strong> restaurant.', 'Cheap est court → the cheapEST, pas the most cheap.'),
    ('He is the taller in the class.', 'He is the <strong>tallest</strong> in the class.', 'Le superlatif (« le plus grand de la classe ») exige -est : the tallEST.'),
  ],
  summary=[
    ('Adjectif court', 'adjectif-er + than', 'Tom is taller than me.'),
    ('Adjectif long', 'more + adjectif + than', 'more interesting than'),
    ('Superlatif court', 'the + adjectif-est', 'the tallest in the class'),
    ('Superlatif long', 'the most + adjectif', 'the most expensive restaurant'),
    ('Irréguliers', 'good→better→best · bad→worse→worst', 'This pizza is better.'),
    ('Égalité', 'as + adjectif + as', 'She is as tall as her mother.'),
  ],
  ex1=('Comparatif ou superlatif ?', 'Adjectif court ou long ? Choisis la bonne forme.', [
    ('My brother is ______ than me.', ['taller', 'more tall', 'the tallest'], 'taller',
     'Tall est court → -ER : taller THAN me.'),
    ('This film is ______ than the book.', ['more interesting', 'interestinger', 'most interesting'], 'more interesting',
     'Interesting est long → MORE interesting.'),
    ('She is ______ student in the school.', ['the best', 'the better', 'the most good'], 'the best',
     'Superlatif irrégulier de good → THE BEST.'),
    ('Today the weather is ______ than yesterday.', ['worse', 'more bad', 'badder'], 'worse',
     'Comparatif irrégulier de bad → WORSE.'),
    ('This is ______ restaurant in town.', ['the most expensive', 'the expensivest', 'the more expensive'], 'the most expensive',
     'Expensive est long → THE MOST expensive.'),
    ('My city is ______ than London.', ['smaller', 'more small', 'smallest'], 'smaller',
     'Small est court → smallER than.'),
  ]),
  ex2=('Écris la forme comparative', 'Attention à l\'orthographe et aux irréguliers.', [
    ('big → My dog is ______ than yours. (un mot)', 'bigger',
     'Big double sa consonne : bigGER.'),
    ('happy → She looks ______ today. (un mot)', 'happier',
     'Happy : le y devient i → happIER.'),
    ('good → This cake is ______ than the other one. (un mot)', 'better',
     'Irrégulier : good → BETTER.'),
    ('« Tom est plus grand QUE moi » → Tom is taller ______ me. (un mot)', 'than',
     'Le que de comparaison = THAN.'),
    ('tall (superlatif) → He is the ______ in the team. (un mot)', 'tallest',
     'Superlatif court : the tallEST.'),
  ]),
  ex3=('Trouve la phrase correcte', 'Jamais more + -er ensemble !', [
    ('« Ce livre est meilleur que le film. »', ['This book is better than the film.', 'This book is more better than the film.', 'This book is more good than the film.'], 'This book is better than the film.',
     'BETTER, jamais more better ni more good.'),
    ('« Elle est aussi grande que sa mère. »', ['She is as tall as her mother.', 'She is as taller as her mother.', 'She is so tall that her mother.'], 'She is as tall as her mother.',
     'Égalité : AS + forme de base + AS : as tall as.'),
    ('« C\'est la pire journée de ma vie. »', ['It\'s the worst day of my life.', 'It\'s the most bad day of my life.', 'It\'s the worse day of my life.'], 'It\'s the worst day of my life.',
     'Superlatif irrégulier de bad → THE WORST.'),
    ('« Paris est plus grand que Lyon. »', ['Paris is bigger than Lyon.', 'Paris is more big than Lyon.', 'Paris is bigger that Lyon.'], 'Paris is bigger than Lyon.',
     'Big → biggER + THAN (pas that).'),
    ('« C\'est la ville la plus célèbre du monde. »', ['It\'s the most famous city in the world.', 'It\'s the famousest city of the world.', 'It\'s the more famous city in the world.'], 'It\'s the most famous city in the world.',
     'Famous est long → THE MOST famous ; « du monde » = IN the world.'),
  ]),
  game_desc='Chaque forme de comparaison passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('taller', 'taller than', 'comparatif court — adjectif + -er + than', 'plus... que', 'Tom is <b>taller</b> than me.', 'Tom is ______ than me. (plus grand)', 'taller'),
    ('than', 'than', 'que — le mot de la comparaison', 'que', 'This book is cheaper <b>than</b> that one.', 'This book is cheaper ______ that one. (que)', 'than'),
    ('more', 'more + adjectif long', 'plus — devant les adjectifs longs', 'plus (long)', 'This film is <b>more</b> interesting than the book.', 'This film is ______ interesting than the book. (plus)', 'more'),
    ('the-tallest', 'the tallest', 'superlatif court — the + -est', 'le plus', 'Tom is the <b>tallest</b> in the class.', 'Tom is the ______ in the class. (le plus grand)', 'tallest'),
    ('the-most', 'the most + adjectif', 'superlatif long — the most', 'le plus (long)', 'It\'s the <b>most</b> expensive restaurant in town.', 'It\'s the ______ expensive restaurant in town. (le plus)', 'most'),
    ('better', 'better', 'comparatif irrégulier de good — jamais more better', 'meilleur', 'This pizza is <b>better</b> than mine.', 'This pizza is ______ than mine. (meilleure)', 'better'),
    ('worst', 'the worst', 'superlatif irrégulier de bad', 'le pire', 'It was the <b>worst</b> day of my life.', 'It was the ______ day of my life. (pire)', 'worst'),
    ('as-as', 'as... as', 'aussi... que — égalité', 'aussi... que', 'She is <b>as</b> tall <b>as</b> her mother.', 'She is ______ tall as her mother. (aussi)', 'as'),
  ],
),

'countable-uncountable-basic': dict(
  level='a2', section='grammaire', num='Ch. 9', short='Dénombrables et indénombrables',
  title='Dénombrables et indénombrables — much ou many ?',
  subtitle='Pourquoi on ne dit jamais « an information » ni « advices »',
  slides=[
    ('Deux familles de noms', None,
     '<p class="slide-explanation">L\'anglais classe les noms en deux familles : les <b>dénombrables</b> (countable — on peut les compter : one apple, two apples) et les <b>indénombrables</b> (uncountable — pas de pluriel, pas de a/an : water, money).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Dénombrables : <b>an apple → two apples</b> · <b>a car → three cars</b></p>'
     '<p style="margin-top:8px">Indénombrables : <b>water, milk, bread, money, time, music</b> — jamais de -s, jamais de a/an.</p>'
     '<p style="margin-top:8px">I need <b>money</b>. (et non « a money » ni « moneys »)</p></div>'
     '<p style="margin-top:16px">Le problème : certains mots indénombrables en anglais sont dénombrables en français...</p>'),
    ('Les pièges : advice, information, furniture', None,
     '<p class="slide-explanation">Voici les indénombrables qui piègent les francophones, parce qu\'on dit « un conseil, des informations, des meubles » en français.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>advice</b> (les conseils) — jamais « an advice » ni « advices »</p>'
     '<p style="margin-top:8px"><b>information</b> — jamais « an information » ni « informations »</p>'
     '<p style="margin-top:8px"><b>furniture</b> (les meubles) · <b>luggage</b> (les bagages) · <b>news</b> (les nouvelles) · <b>work</b> (le travail)</p></div>'
     '<p style="margin-top:16px">Can you give me some <b>information</b>? — Peux-tu me donner des informations ? (sans -s !)</p>'),
    ('A piece of : compter l\'indénombrable', None,
     '<p class="slide-explanation">Pour compter un indénombrable, on passe par <b>a piece of</b> (un morceau de, une unité de) ou un autre « compteur ».</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>a piece of advice</b> — un conseil · <b>two pieces of information</b> — deux informations</p>'
     '<p style="margin-top:8px"><b>a piece of furniture</b> — un meuble · <b>a piece of news</b> — une nouvelle</p>'
     '<p style="margin-top:8px">Autres compteurs : <b>a cup of tea</b>, <b>a glass of water</b>, <b>a slice of bread</b></p></div>'
     '<p style="margin-top:16px">Let me give you <b>a piece of advice</b>. — Laisse-moi te donner un conseil.</p>'),
    ('Much ou many ?', None,
     '<p class="slide-explanation">« Beaucoup de » se traduit différemment selon la famille : <b>many</b> + dénombrable pluriel, <b>much</b> + indénombrable. Surtout dans les questions et les négations.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>How many books</b> do you have? — Combien de livres as-tu ? (dénombrable)</p>'
     '<p style="margin-top:8px"><b>How much money</b> do you need? — Combien d\'argent te faut-il ? (indénombrable)</p>'
     '<p style="margin-top:8px">I don\'t have <b>much time</b>. — Je n\'ai pas beaucoup de temps.</p></div>'
     '<p style="margin-top:16px">Astuce : si tu peux mettre un nombre devant (three books), c\'est many. Sinon, much.</p>'),
    ('There is / there are et l\'accord', None,
     '<p class="slide-explanation">L\'accord du verbe suit la famille du nom : indénombrable = <b>singulier</b>, même si le français dit « les » !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>There <b>is</b> some milk in the fridge. — Il y a du lait. (indénombrable → is)</p>'
     '<p style="margin-top:8px">There <b>are</b> some apples on the table. — Il y a des pommes. (pluriel → are)</p>'
     '<p style="margin-top:8px">The news <b>is</b> good. — Les nouvelles sont bonnes. (news = indénombrable singulier !)</p></div>'
     '<p style="margin-top:16px">Your hair <b>is</b> beautiful (les cheveux !), the information <b>is</b> correct : toujours le singulier.</p>'),
  ],
  traps=[
    ('Can you give me an advice?', 'Can you give me <strong>some advice</strong>?', 'Advice est indénombrable : some advice, ou a piece of advice pour « un conseil ».'),
    ('I need some informations.', 'I need some <strong>information</strong>.', 'Information ne prend jamais de -s en anglais : some information.'),
    ('How much books do you have?', 'How <strong>many</strong> books do you have?', 'Books est dénombrable pluriel → many : how MANY books.'),
    ('The news are good.', 'The news <strong>is</strong> good.', 'News est indénombrable singulier malgré son -s : the news IS good.'),
    ('We bought new furnitures.', 'We bought new <strong>furniture</strong>.', 'Furniture est indénombrable : pas de pluriel. Un meuble = a piece of furniture.'),
  ],
  summary=[
    ('Dénombrables', 'a/an + singulier · pluriel en -s', 'an apple → two apples'),
    ('Indénombrables', 'pas de a/an, pas de pluriel', 'water · money · advice · information'),
    ('Pièges francophones', 'advice · information · furniture · luggage', 'some advice (jamais « advices »)'),
    ('Compter', 'a piece of + indénombrable', 'a piece of advice = un conseil'),
    ('Beaucoup de', 'many + pluriel · much + indénombrable', 'many books / much money'),
    ('Accord', 'indénombrable → verbe au singulier', 'The news is good.'),
  ],
  ex1=('Much ou many ?', 'Dénombrable pluriel ou indénombrable ?', [
    ('How ______ money do you have?', ['much', 'many', 'a lot'], 'much',
     'Money est indénombrable → how MUCH money.'),
    ('How ______ brothers do you have?', ['many', 'much', 'piece of'], 'many',
     'Brothers est dénombrable pluriel → how MANY brothers.'),
    ('I don\'t have ______ time today.', ['much', 'many', 'a'], 'much',
     'Time est indénombrable → MUCH time.'),
    ('There aren\'t ______ students in the class.', ['many', 'much', 'a'], 'many',
     'Students est dénombrable → MANY students.'),
    ('She gave me some good ______.', ['advice', 'advices', 'an advice'], 'advice',
     'Advice est indénombrable : some ADVICE, sans -s.'),
    ('We need some ______ about the trains.', ['information', 'informations', 'an information'], 'information',
     'Information : jamais de -s, jamais de an.'),
  ]),
  ex2=('Écris le mot correct', 'Attention aux indénombrables !', [
    ('« Un conseil » → a ______ of advice. (un mot)', 'piece',
     'Pour compter un indénombrable : a PIECE of advice.'),
    ('« Combien d\'argent ? » → How ______ money? (un mot)', 'much',
     'Money est indénombrable → how MUCH.'),
    ('« Combien de pommes ? » → How ______ apples? (un mot)', 'many',
     'Apples est dénombrable pluriel → how MANY.'),
    ('« Les nouvelles sont bonnes. » → The news ______ good. (un mot)', 'is',
     'News = indénombrable singulier → the news IS good.'),
    ('« Il y a du lait dans le frigo. » → There ______ some milk in the fridge. (un mot)', 'is',
     'Milk est indénombrable → there IS some milk.'),
  ]),
  ex3=('Trouve la phrase correcte', 'Les indénombrables ne prennent ni a/an ni -s.', [
    ('« Elle m\'a donné un bon conseil. »', ['She gave me a good piece of advice.', 'She gave me a good advice.', 'She gave me good advices.'], 'She gave me a good piece of advice.',
     'Un conseil = A PIECE OF advice — advice seul ne se compte pas.'),
    ('« J\'ai beaucoup de travail. »', ['I have a lot of work.', 'I have many works.', 'I have much works.'], 'I have a lot of work.',
     'Work est indénombrable : a lot of WORK, sans -s.'),
    ('« Nous avons acheté des meubles. »', ['We bought some furniture.', 'We bought some furnitures.', 'We bought a furniture.'], 'We bought some furniture.',
     'Furniture est indénombrable → some furniture.'),
    ('« Combien de temps as-tu ? »', ['How much time do you have?', 'How many time do you have?', 'How many times you have?'], 'How much time do you have?',
     'Time (le temps) est indénombrable → how MUCH time.'),
    ('« Tes cheveux sont très beaux. »', ['Your hair is very beautiful.', 'Your hairs are very beautiful.', 'Your hair are very beautiful.'], 'Your hair is very beautiful.',
     'Hair est indénombrable singulier : your hair IS beautiful.'),
  ]),
  game_desc='Chaque famille de noms passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('advice', 'advice', 'les conseils — indénombrable, jamais « an advice »', 'indénombrable', 'She gave me some good <b>advice</b>.', 'She gave me some good ______. (conseils)', 'advice'),
    ('information', 'information', 'les informations — jamais de -s', 'indénombrable', 'I need some <b>information</b> about the trains.', 'I need some ______ about the trains. (informations)', 'information'),
    ('furniture', 'furniture', 'les meubles — indénombrable', 'indénombrable', 'We bought some new <b>furniture</b>.', 'We bought some new ______. (meubles)', 'furniture'),
    ('piece-of', 'a piece of', 'une unité de — pour compter un indénombrable', 'compteur', 'Let me give you a <b>piece</b> of advice.', 'Let me give you a ______ of advice. (un conseil)', 'piece'),
    ('much', 'much + indénombrable', 'beaucoup de — avec les indénombrables', 'beaucoup (indén.)', 'How <b>much</b> money do you need?', 'How ______ money do you need? (combien)', 'much'),
    ('many', 'many + pluriel', 'beaucoup de — avec les dénombrables', 'beaucoup (dén.)', 'How <b>many</b> books do you have?', 'How ______ books do you have? (combien)', 'many'),
    ('news-is', 'the news is', 'news — indénombrable singulier malgré le -s', 'accord singulier', 'The news <b>is</b> good today.', 'The news ______ good today. (accord)', 'is'),
    ('luggage', 'luggage', 'les bagages — indénombrable', 'indénombrable', 'My <b>luggage</b> is very heavy.', 'My ______ is very heavy. (bagages)', 'luggage'),
  ],
),

'quantifiers-basic': dict(
  level='a2', section='grammaire', num='Ch. 10', short='Les quantifieurs',
  title='Les quantifieurs — a lot of, a few, a little',
  subtitle='Exprimer la quantité, et le piège few vs a few',
  slides=[
    ('A lot of : le passe-partout', None,
     '<p class="slide-explanation"><b>A lot of</b> (beaucoup de) fonctionne avec <b>tout</b> : dénombrables et indénombrables. C\'est le quantifieur le plus simple, surtout dans les phrases affirmatives.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>She has <b>a lot of friends</b>. — Elle a beaucoup d\'amis. (dénombrable)</p>'
     '<p style="margin-top:8px">We have <b>a lot of time</b>. — Nous avons beaucoup de temps. (indénombrable)</p>'
     '<p style="margin-top:8px">Forme familière : <b>lots of</b> — There are lots of shops here.</p></div>'
     '<p style="margin-top:16px">À l\'affirmatif, préfère a lot of ; much et many brillent dans les questions et les négations.</p>'),
    ('Much et many : questions et négations', None,
     '<p class="slide-explanation">Rappel du chapitre 9 : <b>many</b> + dénombrable pluriel, <b>much</b> + indénombrable. Ils s\'utilisent surtout dans les <b>questions</b> et les <b>négations</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I don\'t have <b>much money</b>. — Je n\'ai pas beaucoup d\'argent.</p>'
     '<p style="margin-top:8px">There aren\'t <b>many shops</b> here. — Il n\'y a pas beaucoup de magasins ici.</p>'
     '<p style="margin-top:8px"><b>How much</b> sugar? · <b>How many</b> eggs? — Combien de sucre ? Combien d\'œufs ?</p></div>'
     '<p style="margin-top:16px">« I have much money » sonne bizarre à l\'affirmatif : dis plutôt I have a lot of money.</p>'),
    ('A few et a little : un peu, quelques', None,
     '<p class="slide-explanation"><b>A few</b> + dénombrable pluriel = quelques. <b>A little</b> + indénombrable = un peu de. Les deux ont un sens <b>positif</b> : il y en a, et ça suffit.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I have <b>a few friends</b> in London. — J\'ai quelques amis à Londres.</p>'
     '<p style="margin-top:8px">There is <b>a little milk</b> left. — Il reste un peu de lait.</p>'
     '<p style="margin-top:8px">Can you wait <b>a little</b>? — Tu peux attendre un peu ?</p></div>'
     '<p style="margin-top:16px">Même duo que much/many : few va avec les pluriels, little avec les indénombrables.</p>'),
    ('PIÈGE : few sans a = presque rien', None,
     '<p class="slide-explanation">Sans l\'article a, le sens bascule au <b>négatif</b> ! <b>Few</b> = peu de, pas assez. <b>A few</b> = quelques, assez. La nuance change tout le message.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I have <b>a few friends</b>. — J\'ai quelques amis. (positif : j\'en ai !)</p>'
     '<p style="margin-top:8px">I have <b>few friends</b>. — J\'ai peu d\'amis. (négatif : je me sens seul...)</p>'
     '<p style="margin-top:8px">There is <b>little hope</b>. — Il y a peu d\'espoir. (hélas)</p></div>'
     '<p style="margin-top:16px">Au niveau A2, retiens surtout : pour dire « quelques / un peu », garde toujours le <b>a</b>.</p>'),
    ('Le tableau récapitulatif', None,
     '<p class="slide-explanation">Voici la carte complète des quantifieurs selon la famille du nom. Garde-la en tête !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Dénombrables : <b>many</b> (beaucoup) · <b>a few</b> (quelques) · <b>few</b> (peu de)</p>'
     '<p style="margin-top:8px">Indénombrables : <b>much</b> (beaucoup) · <b>a little</b> (un peu) · <b>little</b> (peu de)</p>'
     '<p style="margin-top:8px">Les deux familles : <b>a lot of</b> · <b>some</b> · <b>any</b> · <b>no</b></p></div>'
     '<p style="margin-top:16px">How many apples? · How much sugar? · a few eggs · a little flour — la recette parfaite !</p>'),
  ],
  traps=[
    ('I have much friends.', 'I have <strong>a lot of</strong> friends.', 'Friends est dénombrable : many ou a lot of — much est réservé aux indénombrables, et a lot of est plus naturel à l\'affirmatif.'),
    ('She has a few money.', 'She has <strong>a little</strong> money.', 'Money est indénombrable → a little. A few exige un pluriel : a few coins.'),
    ('I have few friends, so I\'m happy. (sens voulu : quelques)', 'I have <strong>a few</strong> friends, so I\'m happy.', 'Few (sans a) = trop peu, sens négatif. Pour « quelques », garde le a : A FEW friends.'),
    ('How many sugar do you want?', 'How <strong>much</strong> sugar do you want?', 'Sugar est indénombrable → how MUCH sugar.'),
    ('There are a lot of milk in the fridge.', 'There <strong>is</strong> a lot of milk in the fridge.', 'Milk est indénombrable → verbe au singulier : there IS a lot of milk.'),
  ],
  summary=[
    ('Beaucoup (partout)', 'a lot of + tout', 'a lot of friends / a lot of time'),
    ('Beaucoup (questions/nég.)', 'many + pluriel · much + indén.', 'not many shops / not much money'),
    ('Quelques', 'a few + pluriel', 'a few friends'),
    ('Un peu de', 'a little + indénombrable', 'a little milk'),
    ('Peu de (négatif)', 'few / little (sans a)', 'few friends · little hope'),
    ('Combien ?', 'How many...? · How much...?', 'How many eggs? / How much sugar?'),
  ],
  ex1=('Choisis le bon quantifieur', 'Dénombrable ou indénombrable ? Affirmatif ou négatif ?', [
    ('She has ______ friends at school.', ['a lot of', 'much', 'a little'], 'a lot of',
     'Affirmatif + dénombrable → A LOT OF friends (much est impossible avec un pluriel).'),
    ('I don\'t have ______ money this month.', ['much', 'many', 'a few'], 'much',
     'Money est indénombrable + négation → not MUCH money.'),
    ('There are only ______ eggs left.', ['a few', 'a little', 'much'], 'a few',
     'Eggs est dénombrable pluriel → A FEW eggs.'),
    ('Can I have ______ milk in my coffee?', ['a little', 'a few', 'many'], 'a little',
     'Milk est indénombrable → A LITTLE milk.'),
    ('How ______ apples do we need for the cake?', ['many', 'much', 'little'], 'many',
     'Apples est dénombrable → how MANY apples.'),
    ('There aren\'t ______ hotels in this village.', ['many', 'much', 'a little'], 'many',
     'Hotels est dénombrable + négation → not MANY hotels.'),
  ]),
  ex2=('Écris le quantifieur', 'a lot of, much, many, a few ou a little ?', [
    ('« Beaucoup de temps » → a lot ______ time. (un mot)', 'of',
     'A LOT OF : les trois mots sont obligatoires — a lot OF time.'),
    ('« Quelques amis » → ______ few friends. (un mot)', 'a',
     'Quelques (sens positif) → A few. Sans a, le sens devient négatif.'),
    ('« Un peu d\'eau » → a ______ water. (un mot)', 'little',
     'Water est indénombrable → a LITTLE water.'),
    ('« Combien de sucre ? » → How ______ sugar? (un mot)', 'much',
     'Sugar est indénombrable → how MUCH.'),
    ('« Pas beaucoup de magasins » → not ______ shops. (un mot)', 'many',
     'Shops est dénombrable pluriel → not MANY shops.'),
  ]),
  ex3=('Le sens exact', 'Attention au piège few vs a few !', [
    ('« J\'ai quelques amis ici, c\'est sympa. »', ['I have a few friends here.', 'I have few friends here.', 'I have a little friends here.'], 'I have a few friends here.',
     'Sens positif (quelques) → A FEW. Few seul = trop peu.'),
    ('« Il reste un peu de pain. »', ['There is a little bread left.', 'There are a few bread left.', 'There is a few bread left.'], 'There is a little bread left.',
     'Bread est indénombrable → A LITTLE bread + verbe au singulier.'),
    ('« Elle a beaucoup de travail. »', ['She has a lot of work.', 'She has many work.', 'She has a few work.'], 'She has a lot of work.',
     'Work est indénombrable, affirmatif → A LOT OF work.'),
    ('« Peu de gens le savent. » (hélas)', ['Few people know it.', 'A few people know it.', 'Little people know it.'], 'Few people know it.',
     'Sens négatif (pas assez) → FEW sans a. People est pluriel, donc few, pas little.'),
    ('« Combien d\'œufs faut-il ? »', ['How many eggs do we need?', 'How much eggs do we need?', 'How a few eggs do we need?'], 'How many eggs do we need?',
     'Eggs est dénombrable → how MANY eggs.'),
  ]),
  game_desc='Chaque quantifieur passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('a-lot-of', 'a lot of', 'beaucoup de — avec tout type de nom', 'beaucoup', 'She has <b>a lot of</b> friends.', 'She has a ______ of friends. (beaucoup)', 'lot'),
    ('much', 'much', 'beaucoup — indénombrables, questions et négations', 'beaucoup (indén.)', 'I don\'t have <b>much</b> money.', 'I don\'t have ______ money. (beaucoup)', 'much'),
    ('many', 'many', 'beaucoup — dénombrables, questions et négations', 'beaucoup (dén.)', 'There aren\'t <b>many</b> shops here.', 'There aren\'t ______ shops here. (beaucoup)', 'many'),
    ('a-few', 'a few', 'quelques — sens positif, avec un pluriel', 'quelques', 'I have <b>a few</b> friends in London.', 'I have a ______ friends in London. (quelques)', 'few'),
    ('a-little', 'a little', 'un peu de — sens positif, avec un indénombrable', 'un peu de', 'There is a <b>little</b> milk left.', 'There is a ______ milk left. (un peu de)', 'little'),
    ('few-neg', 'few (sans a)', 'peu de — sens négatif : pas assez', 'trop peu', '<b>Few</b> people know this secret.', '______ people know this secret. (peu de)', 'few'),
    ('how-much', 'How much...?', 'combien de — indénombrable', 'combien (indén.)', 'How <b>much</b> sugar do you want?', 'How ______ sugar do you want? (combien)', 'much'),
    ('how-many', 'How many...?', 'combien de — dénombrable', 'combien (dén.)', 'How <b>many</b> eggs do we need?', 'How ______ eggs do we need? (combien)', 'many'),
  ],
),

}
