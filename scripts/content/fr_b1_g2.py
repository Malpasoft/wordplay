# -*- coding: utf-8 -*-
"""fr/ B1 grammaire — lot 2 (4 chapitres)."""

CHAPTERS = {

'second-conditional': dict(
  level='b1', section='grammaire', num='Ch. 7', short='Second Conditional',
  title='Second Conditional — L’irréel du présent',
  subtitle='If + prétérit, would : « si j’avais..., je ferais... »',
  slides=[
    ('Le parallèle parfait avec le français', None,
     '<p class="slide-explanation">« Si j’avais de l’argent, j’achèterais une maison. » L’anglais suit exactement la même logique : <b>if + prétérit</b> (≈ imparfait), <b>would</b> (≈ conditionnel).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>If I had money, I would buy a house.</b></p>'
     '<p style="margin-top:8px"><b>If she lived here, we would see her every day.</b></p></div>'
     '<p style="margin-top:16px">Et comme « si j’aurais » est interdit en français, <b>if I would</b> est interdit en anglais.</p>'),
    ('Formation', None,
     '<p class="slide-explanation">If + sujet + prétérit, sujet + would + base verbale. Would se contracte en <b>’d</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>If we won the lottery, we’d travel the world.</b></p>'
     '<p style="margin-top:8px">Négation : <b>wouldn’t</b> · Question : <b>What would you do if...?</b></p></div>'),
    ('If I were you : le conseil', None,
     '<p class="slide-explanation">Avec be, on emploie <b>were</b> à toutes les personnes (subjonctif figé). <b>If I were you...</b> = « à ta place... » — la formule de conseil par excellence.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>If I were you, I would accept the offer.</b> (À ta place, j’accepterais.)</p>'
     '<p style="margin-top:8px"><b>If he were taller, he could play basketball.</b></p></div>'),
    ('First ou second ? Réel ou imaginaire', None,
     '<p class="slide-explanation">First conditional = futur possible. Second = situation imaginaire ou peu probable, <b>maintenant</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>If I have time tomorrow, I’ll help you.</b> (possible)</p>'
     '<p style="margin-top:8px"><b>If I had more time, I would learn Italian.</b> (irréel : je n’ai pas le temps)</p></div>'
     '<p style="margin-top:16px">Le prétérit ici ne parle pas du passé — il marque l’irréel, comme notre imparfait après « si ».</p>'),
    ('Could et might dans la principale', None,
     '<p class="slide-explanation">À la place de would : <b>could</b> (pourrait) ou <b>might</b> (pourrait peut-être).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>If you asked him, he might say yes.</b> (Si tu lui demandais, il dirait peut-être oui.)</p>'
     '<p style="margin-top:8px"><b>If we left now, we could catch the train.</b></p></div>'),
  ],
  traps=[
    ('If I would have money, I would buy it.', 'If I <strong>had</strong> money, I would buy it.', 'Jamais would après if — exactement comme « si j’aurais » est impossible en français.'),
    ('If I was you, I would call her.', 'If I <strong>were</strong> you, I would call her.', 'Avec be, la forme soignée est were à toutes les personnes : if I were you.'),
    ('If she lived here, we will see her every day.', 'If she lived here, we <strong>would</strong> see her every day.', 'Irréel : prétérit dans la condition, would (pas will) dans la principale.'),
    ('What you would do if you won?', 'What <strong>would you do</strong> if you won?', 'Dans la question, would passe devant le sujet : What would you do...?'),
    ('If I had money, I would to buy a house.', 'If I had money, I would <strong>buy</strong> a house.', 'Would est un modal : base verbale sans to.'),
  ],
  summary=[
    ('Structure', 'if + prétérit, would + base', 'If I had..., I would...'),
    ('Être : were', 'if I/he/she were', 'If I were you...'),
    ('Conseil', 'If I were you, I’d...', 'If I were you, I’d accept.'),
    ('Variantes', 'could / might', 'he might say yes'),
    ('Interdit', 'if + would', '« si j’aurais » = if I would ✗'),
  ],
  ex1=('Choisis la forme correcte', 'Irréel du présent : attention à la place de would.', [
    ('If I ______ rich, I would buy a boat.', ['were', 'would be', 'am'], 'were',
     'Condition irréelle → prétérit de be : were (toutes personnes).'),
    ('She ______ happier if she changed jobs.', ['would be', 'will be', 'was'], 'would be',
     'La principale de l’irréel prend would : would be (serait).'),
    ('If we ______ a car, we could drive there.', ['had', 'would have', 'have'], 'had',
     'Après if : prétérit (had). Would reste dans l’autre moitié.'),
    ('What ______ you do if you lost your phone?', ['would', 'will', 'did'], 'would',
     'Question au conditionnel : What would you do...?'),
    ('If he spoke louder, we ______ him.', ['could hear', 'can hear', 'hear'], 'could hear',
     'Variante de would : could (pourrait) + base verbale.'),
    ('If I ______ you, I’d apologise.', ['were', 'would be', 'am'], 'were',
     'Formule de conseil figée : If I were you, I’d...'),
  ]),
  ex2=('Complète la phrase', 'Écris la forme correcte du verbe entre parenthèses.', [
    ('If I ______ the answer, I would tell you. (know)', 'knew',
     'Prétérit irrégulier : know → knew. « Si je savais... »'),
    ('If they invited us, we ______ go. (would + go → contracte ou non)', 'would go',
     'Principale : would go (nous irions).'),
    ('If she ______ here, she would help us. (be)', 'were',
     'Be à l’irréel : were, même avec she (forme soignée).'),
    ('I ______ travel more if I had the money. (would)', 'would',
     'Le conditionnel français (je voyagerais) = would + base : would travel.'),
    ('If you ______ harder, you would pass. (work)', 'worked',
     'Après if : prétérit régulier en -ed : worked.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Si j’avais le temps, j’apprendrais l’italien. »', ['If I had time, I would learn Italian.', 'If I would have time, I would learn Italian.', 'If I have time, I will learn Italian.'], 'If I had time, I would learn Italian.',
     'Imparfait après si → prétérit après if ; conditionnel → would.'),
    ('« À ta place, j’accepterais. »', ['If I were you, I would accept.', 'If I was in your place, I will accept.', 'In your place, I would to accept.'], 'If I were you, I would accept.',
     '« À ta place » = if I were you — la formule de conseil.'),
    ('« Que ferais-tu si tu gagnais au loto ? »', ['What would you do if you won the lottery?', 'What will you do if you won the lottery?', 'What would you do if you would win the lottery?'], 'What would you do if you won the lottery?',
     'Would dans la question, prétérit (won) après if.'),
    ('« S’il pleuvait moins, nous sortirions plus. »', ['If it rained less, we would go out more.', 'If it would rain less, we would go out more.', 'If it rains less, we go out more.'], 'If it rained less, we would go out more.',
     'Irréel : rained (prétérit) + would go out.'),
    ('Quelle phrase exprime un futur POSSIBLE (pas irréel) ?', ['If I have time tomorrow, I’ll call you.', 'If I had time tomorrow, I would call you.', 'If I were free, I would call you.'], 'If I have time tomorrow, I’ll call you.',
     'First conditional (présent + will) = situation réaliste ; les deux autres sont à l’irréel.'),
  ]),
  game_desc='Chaque structure passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('if-had', 'if + prétérit', 'la condition irréelle — notre « si + imparfait »', 'condition irréelle', '<b>If I had</b> money, I would buy a house.', 'If I ______ money, I would buy a house. (avais)', 'had'),
    ('would', 'would + base', 'le conditionnel français « je ferais »', 'conditionnel', 'I <b>would buy</b> a house.', 'I ______ buy a house. (achèterais)', 'would'),
    ('if-i-were-you', 'If I were you', 'à ta place — formule de conseil', 'conseil', '<b>If I were you</b>, I would accept.', 'If I ______ you, I would accept. (étais)', 'were'),
    ('wouldnt', "wouldn't", 'ne ferait pas — négation de would', 'négation', 'She <b>wouldn’t</b> like it.', 'She ______ like it. (n’aimerait pas)', "wouldn't"),
    ('what-would', 'What would you do?', 'que ferais-tu — la question type', 'question', '<b>What would you do</b> if you won?', 'What ______ you do if you won?', 'would'),
    ('might-cond', 'might (principale)', 'dirait peut-être — possibilité dans l’irréel', 'peut-être', 'If you asked him, he <b>might</b> say yes.', 'If you asked him, he ______ say yes. (peut-être)', 'might'),
    ('could-cond', 'could (principale)', 'pourrait — capacité dans l’irréel', 'pourrait', 'If we left now, we <b>could</b> catch the train.', 'If we left now, we ______ catch the train. (pourrions)', 'could'),
    ('no-would-if', 'pas de would après if', 'l’équivalent de l’interdit « si j’aurais »', 'règle d’or', 'If I <b>had</b> (jamais « if I would have ») time...', 'If I ______ time, I would help. (avais)', 'had'),
  ],
),

'wish-if-only': dict(
  level='b1', section='grammaire', num='Ch. 8', short='Wish & If Only',
  title='Wish & If Only — Les regrets',
  subtitle='« Si seulement... » : souhaits et regrets en anglais',
  slides=[
    ('Wish + prétérit : le souhait présent', None,
     '<p class="slide-explanation">Pour souhaiter qu’une situation présente soit différente : <b>wish + prétérit</b> — la même bascule irréelle que « si seulement » + imparfait.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I wish I had more time.</b> (Si seulement j’avais plus de temps. / J’aimerais avoir plus de temps.)</p>'
     '<p style="margin-top:8px"><b>She wishes she lived by the sea.</b></p></div>'
     '<p style="margin-top:16px">Avec be : <b>I wish I were taller.</b> (forme soignée were).</p>'),
    ('If only : plus intense', None,
     '<p class="slide-explanation"><b>If only</b> = « si seulement », plus émotif que wish, même construction.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>If only I knew the answer!</b> (Si seulement je connaissais la réponse !)</p>'
     '<p style="margin-top:8px"><b>If only it weren’t so cold!</b></p></div>'),
    ('Wish + past perfect : le regret du passé', None,
     '<p class="slide-explanation">Pour regretter le passé : <b>wish + past perfect</b> (had + participe) — comme « si seulement » + plus-que-parfait.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I wish I had studied harder.</b> (Si seulement j’avais étudié davantage.)</p>'
     '<p style="margin-top:8px"><b>She wishes she hadn’t said that.</b> (Elle regrette de l’avoir dit.)</p></div>'),
    ('Wish + would : l’agacement', None,
     '<p class="slide-explanation">Pour se plaindre du comportement de quelqu’un (ou de la météo) : <b>wish + would</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I wish you would stop talking.</b> (J’aimerais bien que tu arrêtes de parler.)</p>'
     '<p style="margin-top:8px"><b>I wish it would stop raining.</b></p></div>'
     '<p style="margin-top:16px">⚠ Pas avec soi-même : on ne dit pas « I wish I would... ».</p>'),
    ('Attention : wish + infinitif = vouloir', None,
     '<p class="slide-explanation">Wish + to + infinitif est très formel et signifie simplement « vouloir » : <b>I wish to see the manager.</b> Rien à voir avec le regret.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Regret : <b>I wish I spoke German.</b> (Si seulement je parlais allemand.)</p>'
     '<p style="margin-top:8px">Volonté formelle : <b>I wish to make a complaint.</b> (Je souhaite déposer une réclamation.)</p></div>'),
  ],
  traps=[
    ('I wish I have more time.', 'I wish I <strong>had</strong> more time.', 'Après wish, on bascule au prétérit — comme l’imparfait après « si seulement ».'),
    ('I wish I would be taller.', 'I wish I <strong>were</strong> taller.', 'Pas de would avec soi-même : wish + prétérit (were).'),
    ('I wish I studied harder last year.', 'I wish I <strong>had studied</strong> harder last year.', 'Regret du passé → past perfect : had studied.'),
    ('I wish that he stops smoking. (agacement)', 'I wish he <strong>would stop</strong> smoking.', 'Se plaindre du comportement d’autrui → wish + would.'),
    ('Si seulement = if lonely...', '<strong>If only</strong> I knew!', '« Si seulement » = if only — lonely signifie « seul/esseulé ».'),
  ],
  summary=[
    ('Souhait présent', 'wish + prétérit', 'I wish I had more time.'),
    ('Avec be', 'wish + were', 'I wish I were taller.'),
    ('Regret passé', 'wish + had + participe', 'I wish I had studied.'),
    ('Agacement', 'wish + would', 'I wish you would stop.'),
    ('Plus émotif', 'if only + même structure', 'If only I knew!'),
  ],
  ex1=('Choisis la forme correcte', 'Souhait présent, regret passé ou agacement ?', [
    ('I wish I ______ a bigger flat.', ['had', 'have', 'would have'], 'had',
     'Souhait sur le présent → prétérit : I wish I had.'),
    ('She wishes she ______ to the party last night.', ['had gone', 'went', 'would go'], 'had gone',
     'Regret du passé (last night) → past perfect : had gone.'),
    ('I wish you ______ interrupting me!', ['would stop', 'stopped', 'stop'], 'would stop',
     'Plainte sur le comportement de quelqu’un → wish + would.'),
    ('If only it ______ so expensive!', ["weren't", "isn't", "wouldn't be"], "weren't",
     'Souhait présent avec be → were/weren’t : if only it weren’t...'),
    ('I wish I ______ speak Japanese.', ['could', 'can', 'would'], 'could',
     'Capacité souhaitée → could : I wish I could (j’aimerais pouvoir).'),
    ('He wishes he ______ that email.', ["hadn't sent", "didn't send", "wouldn't send"], "hadn't sent",
     'Regret d’une action passée → past perfect négatif : hadn’t sent.'),
  ]),
  ex2=('Complète la phrase', 'Écris la forme correcte du verbe entre parenthèses.', [
    ('I wish I ______ where she lives. (know)', 'knew',
     'Souhait présent → prétérit : knew (si seulement je savais).'),
    ('I wish I ______ taller. (be)', 'were',
     'Be après wish → were à toutes les personnes.'),
    ('They wish they ______ earlier yesterday. (leave, regret passé)', 'had left',
     'Regret du passé → had left (s’ils étaient partis plus tôt).'),
    ('I wish it ______ stop raining. (would)', 'would',
     'Agacement contre la pluie → wish + would : I wish it would stop.'),
    ('If only I ______ drive. (could)', 'could',
     'Si seulement je savais conduire → if only I could drive.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Si seulement j’avais plus d’argent ! »', ['If only I had more money!', 'If only I have more money!', 'If lonely I had more money!'], 'If only I had more money!',
     'Si seulement + imparfait → if only + prétérit.'),
    ('« Je regrette d’avoir dit ça. »', ["I wish I hadn't said that.", "I wish I didn't say that.", "I wish I wouldn't say that."], "I wish I hadn't said that.",
     'Regret du passé → wish + past perfect négatif.'),
    ('« J’aimerais bien qu’il arrête de fumer. » (agacement)', ['I wish he would stop smoking.', 'I wish he stops smoking.', 'I wish he would to stop smoking.'], 'I wish he would stop smoking.',
     'Comportement d’autrui → wish + would + base verbale.'),
    ('« Elle aimerait habiter au bord de la mer. »', ['She wishes she lived by the sea.', 'She wishes she lives by the sea.', 'She wishes to lived by the sea.'], 'She wishes she lived by the sea.',
     'Souhait présent → wish + prétérit : lived.'),
    ('« Je souhaite parler au directeur. » (très formel)', ['I wish to speak to the manager.', 'I wish I speak to the manager.', 'I wish speaking to the manager.'], 'I wish to speak to the manager.',
     'Wish + to + infinitif = vouloir (registre formel), pas un regret.'),
  ]),
  game_desc='Chaque structure de regret passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('wish-past', 'wish + prétérit', 'souhait sur le présent — « si seulement j’avais »', 'souhait présent', 'I <b>wish I had</b> more time.', 'I wish I ______ more time. (avais)', 'had'),
    ('wish-were', 'wish + were', 'avec be : were à toutes les personnes', 'wish avec be', 'I wish I <b>were</b> taller.', 'I wish I ______ taller. (étais)', 'were'),
    ('wish-had-done', 'wish + had + participe', 'regret du passé — « si seulement j’avais fait »', 'regret passé', 'I wish I <b>had studied</b> harder.', 'I wish I ______ studied harder. (avais)', 'had'),
    ('wish-would', 'wish + would', 'agacement contre le comportement de quelqu’un', 'agacement', 'I wish you <b>would stop</b> talking.', 'I wish you ______ stop talking.', 'would'),
    ('if-only', 'if only', 'si seulement — plus émotif que wish', 'si seulement', '<b>If only</b> I knew the answer!', '______ ______ I knew the answer! (si seulement)', 'if only'),
    ('wish-could', 'wish + could', 'aimerait pouvoir', 'capacité souhaitée', 'I wish I <b>could</b> speak Japanese.', 'I wish I ______ speak Japanese. (pouvais)', 'could'),
    ('hadnt', "wish + hadn't", 'regrette d’avoir fait — négation du regret passé', 'regret négatif', 'She wishes she <b>hadn’t</b> said that.', 'She wishes she ______ said that. (n’avait pas)', "hadn't"),
    ('wish-to', 'wish to + infinitif', 'vouloir (très formel) — pas un regret', 'volonté formelle', 'I <b>wish to</b> make a complaint.', 'I ______ to make a complaint. (souhaite)', 'wish'),
  ],
),

'modals-obligation': dict(
  level='b1', section='grammaire', num='Ch. 9', short='Modals of Obligation',
  title='Modals of Obligation — Must, have to, mustn’t',
  subtitle='Obligation, interdiction et absence d’obligation',
  slides=[
    ('Must et have to : devoir', None,
     '<p class="slide-explanation">Les deux traduisent « devoir ». <b>Must</b> : obligation ressentie par celui qui parle (ou règle écrite). <b>Have to</b> : obligation extérieure, imposée.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I must finish this today.</b> (Je dois finir — je me l’impose.)</p>'
     '<p style="margin-top:8px"><b>I have to wear a uniform at work.</b> (Le règlement l’impose.)</p></div>'
     '<p style="margin-top:16px">Au passé et au futur, must n’existe pas : <b>had to</b>, <b>will have to</b>.</p>'),
    ('Le piège : mustn’t ≠ don’t have to', None,
     '<p class="slide-explanation">La négation change tout — c’est LE piège de ce chapitre.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>You mustn’t park here.</b> = interdiction (Tu ne dois pas / c’est interdit.)</p>'
     '<p style="margin-top:8px"><b>You don’t have to come.</b> = pas d’obligation (Tu n’es pas obligé de venir.)</p></div>'
     '<p style="margin-top:16px">« Tu ne dois pas » français est ambigu ; l’anglais distingue interdiction et liberté.</p>'),
    ('Should : le conseil', None,
     '<p class="slide-explanation"><b>Should</b> = devrait. Conseil ou opinion, plus doux que must.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>You should see a doctor.</b> (Tu devrais voir un médecin.)</p>'
     '<p style="margin-top:8px"><b>You shouldn’t eat so much sugar.</b></p></div>'),
    ('Need to et needn’t', None,
     '<p class="slide-explanation"><b>Need to</b> = avoir besoin de / devoir. <b>Needn’t</b> = inutile de (= don’t have to).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I need to renew my passport.</b></p>'
     '<p style="margin-top:8px"><b>You needn’t bring anything.</b> (Inutile d’apporter quoi que ce soit.)</p></div>'),
    ('Les modaux : rappel technique', None,
     '<p class="slide-explanation">Must et should sont des modaux : pas de -s à la 3e personne, pas de to, négation directe.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>She must leave.</b> (jamais « musts » ni « must to leave »)</p>'
     '<p style="margin-top:8px">Have to, lui, se conjugue : <b>she has to, she doesn’t have to, did she have to?</b></p></div>'),
  ],
  traps=[
    ('You mustn’t come if you’re busy. (= pas obligé)', 'You <strong>don’t have to</strong> come if you’re busy.', 'Mustn’t = interdit ! Pour « pas obligé », don’t have to.'),
    ('She must to wear a uniform.', 'She <strong>must wear</strong> a uniform. / She <strong>has to wear</strong>...', 'Must est un modal : jamais de to derrière.'),
    ('Yesterday I must work late.', 'Yesterday I <strong>had to</strong> work late.', 'Must n’a pas de passé : had to.'),
    ('He musts study more.', 'He <strong>must</strong> study more.', 'Les modaux ne prennent jamais de -s à la 3e personne.'),
    ('You should to rest.', 'You should <strong>rest</strong>.', 'Should + base verbale, sans to.'),
  ],
  summary=[
    ('Obligation (interne)', 'must + base', 'I must finish this.'),
    ('Obligation (externe)', 'have to', 'I have to wear a uniform.'),
    ('Interdiction', 'mustn’t', 'You mustn’t park here.'),
    ('Pas d’obligation', 'don’t have to / needn’t', 'You don’t have to come.'),
    ('Conseil', 'should / shouldn’t', 'You should see a doctor.'),
    ('Passé', 'had to', 'I had to work late.'),
  ],
  ex1=('Choisis le bon modal', 'Obligation, interdiction ou liberté ?', [
    ('You ______ smoke in the hospital — it’s forbidden.', ["mustn't", "don't have to", "shouldn't"], "mustn't",
     'Interdiction stricte → mustn’t. Don’t have to dirait « pas obligé » !'),
    ('The entrance is free — you ______ pay.', ["don't have to", "mustn't", "should"], "don't have to",
     'Absence d’obligation → don’t have to. Mustn’t interdirait de payer !'),
    ('I ______ get up at six every day for work.', ['have to', 'must to', 'should to'], 'have to',
     'Obligation extérieure régulière → have to. Jamais de to après must/should.'),
    ('You look tired — you ______ go to bed earlier.', ['should', 'must to', "mustn't"], 'should',
     'Conseil → should : tu devrais.'),
    ('Last week I ______ work overtime.', ['had to', 'must', 'have to'], 'had to',
     'Passé de l’obligation → had to (must n’a pas de passé).'),
    ('She ______ renew her passport before July.', ['needs to', 'need', "needn't to"], 'needs to',
     'Need to se conjugue : she needs to.'),
  ]),
  ex2=('Complète avec le bon mot', 'Écris le modal ou l’auxiliaire qui manque.', [
    ('You ______ be late for the exam — they close the doors. (interdiction)', 'mustn\'t'.replace("\\'","'"),
     'Interdiction → mustn’t : tu ne dois absolument pas être en retard.'),
    ('Tomorrow I will ______ to get up early. (obligation future)', 'have',
     'Futur de l’obligation : will have to.'),
    ('You ______ bring anything — we have everything. (inutile de)', "needn't",
     'Inutile de = needn’t (ou don’t have to).'),
    ('He ______ study more if he wants to pass. (conseil)', 'should',
     'Conseil → should : il devrait réviser davantage.'),
    ('Did you ______ to wait long? (question au passé)', 'have',
     'Question passée de have to : Did you have to...?'),
  ]),
  ex3=('Interdiction ou liberté ? Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Tu n’es pas obligé de venir. »', ["You don't have to come.", "You mustn't come.", "You shouldn't come."], "You don't have to come.",
     'Liberté de choix → don’t have to. Mustn’t = interdiction de venir !'),
    ('« Il est interdit d’utiliser son téléphone ici. »', ["You mustn't use your phone here.", "You don't have to use your phone here.", 'You should use your phone here.'], "You mustn't use your phone here.",
     'Interdiction → mustn’t.'),
    ('« J’ai dû attendre deux heures. »', ['I had to wait for two hours.', 'I must waited for two hours.', 'I must to wait for two hours.'], 'I had to wait for two hours.',
     'Passé de devoir → had to.'),
    ('« Tu devrais lui parler. »', ['You should talk to her.', 'You must talk to her.', 'You have to talk to her.'], 'You should talk to her.',
     'Conseil doux (devrais) → should. Must/have to seraient une obligation.'),
    ('« Elle doit porter un casque sur le chantier. » (règlement)', ['She has to wear a helmet on site.', 'She should wear a helmet on site.', "She doesn't have to wear a helmet on site."], 'She has to wear a helmet on site.',
     'Obligation imposée par le règlement → has to.'),
  ]),
  game_desc='Chaque modal d’obligation passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('must', 'must', 'obligation forte, souvent ressentie par celui qui parle', 'obligation interne', 'I <b>must</b> finish this today.', 'I ______ finish this today. (dois)', 'must'),
    ('have-to', 'have to', 'obligation extérieure ou imposée', 'obligation externe', 'I <b>have to</b> wear a uniform at work.', 'I ______ ______ wear a uniform at work.', 'have to'),
    ('mustnt', "mustn't", 'interdiction — à ne pas confondre avec don’t have to', 'interdiction', 'You <b>mustn’t</b> park here.', 'You ______ park here. (interdit)', "mustn't"),
    ('dont-have-to', "don't have to", 'pas obligé — absence d’obligation', 'liberté', 'You <b>don’t have to</b> come.', "You ______ have to come. (pas obligé)", "don't"),
    ('should', 'should', 'devrait — le conseil', 'conseil', 'You <b>should</b> see a doctor.', 'You ______ see a doctor. (devrais)', 'should'),
    ('had-to', 'had to', 'a dû — le passé de must et have to', 'obligation passée', 'I <b>had to</b> work late yesterday.', 'I ______ ______ work late yesterday. (ai dû)', 'had to'),
    ('neednt', "needn't", 'inutile de — synonyme de don’t have to', 'inutile de', 'You <b>needn’t</b> bring anything.', 'You ______ bring anything. (inutile d’)', "needn't"),
    ('will-have-to', 'will have to', 'devra — le futur de l’obligation', 'obligation future', 'You <b>will have to</b> book early.', 'You will ______ ______ book early. (devras)', 'have to'),
  ],
),

'modals-advice': dict(
  level='b1', section='grammaire', num='Ch. 10', short='Modals of Advice',
  title='Modals of Advice — Should, ought to, had better',
  subtitle='Donner des conseils avec la bonne nuance',
  slides=[
    ('Should : le conseil standard', None,
     '<p class="slide-explanation"><b>Should</b> = devrait. C’est le conseil neutre, utilisable partout.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>You should drink more water.</b> (Tu devrais boire plus d’eau.)</p>'
     '<p style="margin-top:8px"><b>Should I call her?</b> (Devrais-je l’appeler ?)</p></div>'),
    ('Ought to : le cousin formel', None,
     '<p class="slide-explanation"><b>Ought to</b> = should, en plus formel. C’est le seul « modal » suivi de to.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>You ought to apologise.</b> (Tu devrais présenter tes excuses.)</p></div>'
     '<p style="margin-top:16px">En cas de doute, should est toujours correct.</p>'),
    ('Had better : l’avertissement', None,
     '<p class="slide-explanation"><b>Had better</b> (’d better) = « tu ferais mieux de » — un conseil urgent avec menace implicite. Toujours suivi de la base verbale (sans to).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>You’d better hurry — the train leaves in 5 minutes.</b></p>'
     '<p style="margin-top:8px">Négation : <b>You’d better not be late.</b></p></div>'
     '<p style="margin-top:16px">⚠ « Had » ne renvoie pas au passé ici — le conseil porte sur maintenant.</p>'),
    ('Demander un conseil', None,
     '<p class="slide-explanation">Pour demander conseil : <b>What should I do?</b>, <b>Do you think I should...?</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>What should I wear to the interview?</b></p>'
     '<p style="margin-top:8px"><b>Do you think I should accept?</b> (Tu penses que je devrais accepter ?)</p></div>'),
    ('Adoucir un conseil', None,
     '<p class="slide-explanation">Pour rester diplomate : <b>maybe you should</b>, <b>perhaps you could</b>, <b>why don’t you...?</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Maybe you should talk to him first.</b></p>'
     '<p style="margin-top:8px"><b>Why don’t you take a break?</b> (Et si tu faisais une pause ?)</p></div>'),
  ],
  traps=[
    ('You should to rest.', 'You should <strong>rest</strong>.', 'Should + base verbale sans to — seul ought to garde le to.'),
    ('You had better to leave now.', 'You had better <strong>leave</strong> now.', 'Had better + base verbale, sans to.'),
    ('You don’t had better be late.', 'You’d better <strong>not</strong> be late.', 'La négation se place après better : had better not.'),
    ('What I should do?', 'What <strong>should I</strong> do?', 'Dans la question, should passe devant le sujet.'),
    ('He shoulds see a doctor.', 'He <strong>should</strong> see a doctor.', 'Les modaux sont invariables : jamais de -s.'),
  ],
  summary=[
    ('Conseil neutre', 'should + base', 'You should rest.'),
    ('Formel', 'ought to + base', 'You ought to apologise.'),
    ('Urgent / menace', '’d better + base', 'You’d better hurry.'),
    ('Négation urgente', '’d better not', 'You’d better not be late.'),
    ('Demander', 'What should I...?', 'What should I do?'),
    ('Adoucir', 'maybe you should...', 'Maybe you should call him.'),
  ],
  ex1=('Choisis le bon conseil', 'Nuance neutre, formelle ou urgente ?', [
    ('You ______ eat more vegetables.', ['should', 'should to', 'had better to'], 'should',
     'Conseil standard → should + base verbale, sans to.'),
    ('It’s icy — you ______ drive slowly!', ["'d better", 'ought', 'should to'], "'d better",
     'Danger immédiat → you’d better drive slowly (tu ferais mieux de...).'),
    ('You ______ to thank them for the invitation.', ['ought', 'should', 'had better'], 'ought',
     'Le seul suivi de to est ought : you ought to thank them.'),
    ('______ I tell her the truth?', ['Should', 'Had better', 'Ought'], 'Should',
     'Question de conseil → Should I...?'),
    ('You’d better ______ forget your passport.', ['not', "don't", 'no'], 'not',
     'Négation : had better not + base verbale.'),
    ('Maybe you ______ talk to your boss about it.', ['should', 'had better not', 'ought'], 'should',
     'Conseil adouci → maybe you should.'),
  ]),
  ex2=('Complète la phrase', 'Écris le mot qui manque.', [
    ('You ______ better hurry — we’re late! (ferais mieux de)', 'had',
     'Had better (souvent contracté ’d better) : you had better hurry.'),
    ('What ______ I wear to the wedding? (devrais)', 'should',
     'Demande de conseil : What should I wear?'),
    ('You ought ______ apologise to her. (le petit mot manquant)', 'to',
     'Ought est le seul à garder to : ought to apologise.'),
    ('Why ______ you take a day off? (suggestion : et si... ?)', "don't",
     'Suggestion douce : Why don’t you take a day off?'),
    ('You should ______ go to bed so late. (négation du conseil)', 'not',
     'Should not (shouldn’t) : tu ne devrais pas te coucher si tard.'),
  ]),
  ex3=('Choisis la bonne nuance', 'Quelle phrase correspond à la situation ?', [
    ('Le train part dans 3 minutes. Le conseil le plus naturel :', ["You'd better run!", 'You ought to run.', 'Maybe you should run someday.'], "You'd better run!",
     'Urgence avec conséquence immédiate → had better.'),
    ('« Tu ferais mieux de ne pas en parler. »', ["You'd better not mention it.", "You don't had better mention it.", "You'd not better mention it."], "You'd better not mention it.",
     'Ordre des mots : ’d better not + base verbale.'),
    ('Conseil poli à un collègue :', ['Maybe you should double-check the figures.', "You'd better check or else!", 'Check the figures!'], 'Maybe you should double-check the figures.',
     'Maybe you should adoucit le conseil — idéal au travail.'),
    ('« Devrais-je accepter cette offre ? »', ['Should I accept this offer?', 'Had I better accept this offer?', 'Ought I accept this offer?'], 'Should I accept this offer?',
     'La question de conseil standard → Should I...?'),
    ('Quelle phrase est INCORRECTE ?', ['You should to see a dentist.', 'You ought to see a dentist.', 'You should see a dentist.'], 'You should to see a dentist.',
     'Should ne prend jamais de to — c’est ought qui le garde.'),
  ]),
  game_desc='Chaque structure de conseil passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('should', 'should', 'devrait — le conseil standard', 'conseil neutre', 'You <b>should</b> drink more water.', 'You ______ drink more water. (devrais)', 'should'),
    ('shouldnt', "shouldn't", 'ne devrait pas', 'conseil négatif', 'You <b>shouldn’t</b> eat so much sugar.', 'You ______ eat so much sugar. (ne devrais pas)', "shouldn't"),
    ('ought-to', 'ought to', 'devrait — formel, le seul avec to', 'conseil formel', 'You <b>ought to</b> apologise.', 'You ______ to apologise. (devrais)', 'ought'),
    ('had-better', "'d better", 'ferais mieux de — urgent, menace implicite', 'avertissement', 'You<b>’d better</b> hurry!', "You'd ______ hurry! (ferais mieux)", 'better'),
    ('better-not', "'d better not", 'ferais mieux de ne pas', 'avertissement négatif', 'You’d better <b>not</b> be late.', "You'd better ______ be late.", 'not'),
    ('should-i', 'Should I...?', 'devrais-je — demander un conseil', 'demander conseil', '<b>Should I</b> call her?', '______ I call her? (devrais-je)', 'should'),
    ('why-dont', "Why don't you...?", 'et si tu... — suggestion amicale', 'suggestion', '<b>Why don’t you</b> take a break?', 'Why ______ you take a break? (et si)', "don't"),
    ('maybe-should', 'maybe you should', 'tu devrais peut-être — conseil adouci', 'conseil diplomate', '<b>Maybe you should</b> talk to him first.', '______ you should talk to him first. (peut-être)', 'maybe'),
  ],
),
}
