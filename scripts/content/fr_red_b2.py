# -*- coding: utf-8 -*-
"""fr/ B2 rédaction — article, essay, formal-email, report, review (5 chapitres)."""

CHAPTERS = {

'article': dict(
  level='b2', section='redaction', num='Ch. 1', short='Article',
  title='Article — L’article B2 qui marque des points',
  subtitle='Titre, angle, opinion : viser le niveau First',
  slides=[
    ('Ce que le B2 exige en plus', None,
     '<p class="slide-explanation">Au B2 First, l’article doit montrer une <b>gamme</b> : structures variées, vocabulaire précis, opinion assumée. Le correcteur cherche du relief — pas une liste de phrases simples correctes.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>B1 : <b>I like cycling because it is healthy.</b></p>'
     '<p style="margin-top:8px">B2 : <b>What I love about cycling is the sense of freedom it gives you.</b></p></div>'),
    ('Un titre et un angle', None,
     '<p class="slide-explanation">Choisissez un angle personnel et tenez-le. Le titre peut jouer sur une question, un contraste ou une formule.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Screens: Friend or Foe?</b></p>'
     '<p style="margin-top:8px"><b>The Day I Switched Off My Phone</b></p></div>'),
    ('Impliquer le lecteur — version B2', None,
     '<p class="slide-explanation">Questions rhétoriques, mais aussi structures emphatiques : <b>What surprised me most was... · It’s not just X, it’s Y · Imagine + -ing</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Imagine spending a whole week without the internet.</b></p>'
     '<p style="margin-top:8px"><b>What struck me most was how quiet everything became.</b></p></div>'),
    ('Nuancer son opinion', None,
     '<p class="slide-explanation">Le B2 nuance : <b>Admittedly</b> (certes), <b>Having said that</b> (cela dit), <b>to some extent</b> (dans une certaine mesure), <b>There’s no denying that</b> (on ne peut pas nier que).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Admittedly, screens are useful. Having said that, we clearly overuse them.</b></p></div>'),
    ('La conclusion qui reste en tête', None,
     '<p class="slide-explanation">Bouclez sur votre angle : reprenez l’image du titre, lancez un défi au lecteur, ou finissez sur une formule.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>So next weekend, why not switch off — and see what you’ve been missing?</b></p></div>'),
  ],
  traps=[
    ('More people use the Internet. It is practical. It is fast.', 'Phrases reliées : <strong>Not only is it practical, it’s also incredibly fast.</strong>', 'Une suite de phrases simples plafonne au B1 — reliez et variez les structures.'),
    ('I will talk about the advantages and disadvantages.', 'Un angle assumé : <strong>Here’s why I think we’ve got it all wrong.</strong>', 'L’article n’est pas un essay : pas d’annonce de plan, un point de vue.'),
    ('It’s a very interesting hobby.', 'C’est un mot B1 : <strong>a fascinating / an absorbing hobby</strong>.', 'Very + adjectif faible coûte des points — montez en gamme lexicale.'),
    ('In a first time..., in a second time...', '<strong>At first... · then... · later on...</strong>', '« Dans un premier temps » ne se calque pas : in a first time n’existe pas.'),
    ('We can ask us the question of...', '<strong>This raises the question of...</strong> / <strong>You might wonder...</strong>', '« On peut se poser la question » est un gallicisme — raise the question ou wonder.'),
  ],
  summary=[
    ('Niveau visé', 'structures variées + opinion', 'What I love about X is...'),
    ('Titre', 'angle personnel, jeu de mots', 'Screens: Friend or Foe?'),
    ('Lecteur', 'Imagine + -ing · questions', 'Imagine spending a week offline.'),
    ('Nuance', 'Admittedly · Having said that', 'Admittedly, ... Having said that, ...'),
    ('Emphase', 'What struck me most was...', 'What struck me most was the silence.'),
    ('Conclusion', 'boucler sur l’angle', 'So why not switch off?'),
  ],
  ex1=('Choisis la meilleure option', 'Monter l’article au niveau B2.', [
    ('La formulation de niveau B2 :', ['What I love about running is the freedom.', 'I like running because it is free.', 'Running is good and I like it.'], 'What I love about running is the freedom.',
     'La structure emphatique What I love about... is... montre la gamme B2.'),
    ('« Certes, ... » se dit :', ['Admittedly,', 'Certainly yes,', 'Of course that,'], 'Admittedly,',
     'Admittedly concède un point avant de le contrer.'),
    ('« Cela dit, ... » :', ['Having said that,', 'This said,', 'Saying that,'], 'Having said that,',
     'Having said that = cela dit — la bascule de nuance.'),
    ('Pour impliquer le lecteur :', ['Imagine spending a week offline.', 'Let us examine the question of the internet.', 'The internet will be discussed below.'], 'Imagine spending a week offline.',
     'Imagine + -ing embarque le lecteur ; les autres sont du registre rapport.'),
    ('« Dans un premier temps » :', ['At first', 'In a first time', 'In the first time'], 'At first',
     'In a first time est un calque — at first / to begin with.'),
    ('« On ne peut pas nier que... » :', ['There’s no denying that...', 'We cannot to deny that...', 'It can’t be denied us that...'], 'There’s no denying that...',
     'There’s no denying that + proposition — la formule consacrée.'),
  ]),
  ex2=('Complète la phrase d’article', 'Écris le mot manquant.', [
    ('What struck me ______ was how friendly everyone was. (le plus)', 'most',
     'What struck me MOST — l’emphase superlative.'),
    ('______ spending a whole month without your phone. (le verbe d’invitation)', 'imagine',
     'Imagine + -ing : l’ouverture immersive.'),
    ('Having ______ that, screens do have real benefits. (say au participe)', 'said',
     'Having said that = cela dit.'),
    ('Not ______ is it cheap, it’s also good for your health. (la négation de l’inversion)', 'only',
     'Not only is it cheap... — l’inversion emphatique.'),
    ('To some ______, social media brings us closer. (dans une certaine mesure)', 'extent',
     'To some extent = dans une certaine mesure.'),
  ]),
  ex3=('Choisis la version anglaise naturelle', 'Gallicismes interdits.', [
    ('« On peut se demander si c’est une bonne idée. »', ['You might wonder whether it’s a good idea.', 'We can ask us if it is a good idea.', 'One can demand if it is a good idea.'], 'You might wonder whether it’s a good idea.',
     'Se demander = wonder ; demand = exiger.'),
    ('« Cela soulève la question du coût. »', ['This raises the question of cost.', 'This lifts the question of cost.', 'This poses itself the question of cost.'], 'This raises the question of cost.',
     'Raise a question — le verbe consacré.'),
    ('« Ce n’est pas seulement pratique, c’est indispensable. »', ['It’s not just convenient — it’s essential.', 'It is not only practic, it is indispensable.', 'Not just it is practical but indispensable.'], 'It’s not just convenient — it’s essential.',
     'Not just X — Y : le contraste percutant.'),
    ('« Certes, c’est cher. Cela dit, la qualité est exceptionnelle. »', ['Admittedly, it’s expensive. Having said that, the quality is outstanding.', 'Certainly it is expensive. This said, quality is exceptional.', 'Of course that it is expensive but said that, quality is great.'], 'Admittedly, it’s expensive. Having said that, the quality is outstanding.',
     'Admittedly + Having said that : la concession nuancée du B2.'),
    ('Quelle phrase a le niveau lexical B2 ?', ['The scenery was absolutely breathtaking.', 'The landscape was very very beautiful.', 'The view was nice and good.'], 'The scenery was absolutely breathtaking.',
     'Absolutely + adjectif extrême : la gamme attendue au First.'),
  ]),
  game_desc='Chaque outil de l’article B2 passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('what-i-love', 'What I love about X is...', 'l’emphase qui montre la gamme', 'emphase', '<b>What I love about</b> cycling <b>is</b> the freedom.', 'What I love ______ cycling is the freedom. (préposition)', 'about'),
    ('admittedly', 'Admittedly', 'certes', 'concession', '<b>Admittedly</b>, screens are useful.', '______, screens are useful. (certes)', 'admittedly'),
    ('having-said-that', 'Having said that', 'cela dit', 'nuance', '<b>Having said that</b>, we overuse them.', 'Having ______ that, we overuse them.', 'said'),
    ('imagine-ing', 'Imagine + -ing', 'l’ouverture immersive', 'accroche', '<b>Imagine spending</b> a week offline.', 'Imagine ______ a week offline. (spend en -ing)', 'spending'),
    ('no-denying', 'There’s no denying', 'on ne peut pas nier', 'affirmation', '<b>There’s no denying</b> that times have changed.', 'There’s no ______ that times have changed. (deny en -ing)', 'denying'),
    ('to-some-extent', 'to some extent', 'dans une certaine mesure', 'mesure', '<b>To some extent</b>, social media connects us.', 'To some ______, social media connects us.', 'extent'),
    ('struck-me', 'What struck me most', 'ce qui m’a le plus frappé', 'récit d’expérience', '<b>What struck me most</b> was the silence.', 'What ______ me most was the silence. (frapper — prétérit)', 'struck'),
    ('raises-question', 'raise the question', 'soulever la question', 'gallicisme évité', 'This <b>raises the question</b> of cost.', 'This ______ the question of cost. (soulever)', 'raises'),
  ],
),

'essay': dict(
  level='b2', section='redaction', num='Ch. 2', short='Essay',
  title='Essay — L’essai du B2 First',
  subtitle='Deux points imposés + votre idée : la mécanique de l’essay',
  slides=[
    ('L’essay n’est pas une dissertation', None,
     '<p class="slide-explanation">Oubliez thèse-antithèse-synthèse. L’essay du First : <b>introduction</b> (reformuler la question), <b>un paragraphe par point imposé</b>, <b>un paragraphe pour votre idée</b>, <b>conclusion</b> avec opinion claire. 140–190 mots, registre formel.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Consigne type : « Every town should have a park. Notes: 1. health 2. cost 3. (your own idea) »</p></div>'),
    ('L’introduction : reformuler, pas recopier', None,
     '<p class="slide-explanation">Reformulez la question avec vos mots et annoncez la couleur — l’anglais dit son opinion dès l’intro, contrairement à la prudence française.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>It is often said that parks are essential to city life. In my view, every town does indeed need one, for several reasons.</b></p></div>'),
    ('Les connecteurs formels', None,
     '<p class="slide-explanation">Le quatuor du paragraphe : <b>Firstly / To begin with · Furthermore / Moreover · However / On the other hand · In conclusion / To sum up</b>. Pas de contractions : <b>do not, it is</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Furthermore, green spaces encourage people to exercise.</b></p>'
     '<p style="margin-top:8px"><b>On the other hand, maintaining a park is expensive.</b></p></div>'),
    ('Argumenter sans « I think » partout', None,
     '<p class="slide-explanation">Variez l’opinion : <b>In my view · It seems to me that · I would argue that · There is a strong case for</b>. Et l’impersonnel : <b>It could be argued that...</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I would argue that the benefits far outweigh the costs.</b></p>'
     '<p style="margin-top:8px"><b>It could be argued that taxes are better spent elsewhere.</b></p></div>'),
    ('La conclusion : trancher', None,
     '<p class="slide-explanation">Pas de « chacun son avis » : le First exige une position. <b>In conclusion / To sum up / On balance</b> + reprise de l’opinion + la raison maîtresse.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>In conclusion, despite the cost, I firmly believe every town needs a park: the health benefits alone justify the investment.</b></p></div>'),
  ],
  traps=[
    ('I think that... I think also that... I think finally...', 'Variez : <strong>In my view... · I would argue that... · It seems to me that...</strong>', 'Trois I think d’affilée plafonnent la note — la gamme des formules d’opinion compte.'),
    ('Don’t forget that parks aren’t free.', '<strong>It should not be forgotten that parks are not free.</strong>', 'Registre formel : pas de contractions ni d’impératif au lecteur dans un essay.'),
    ('To conclude, everyone has his own opinion.', '<strong>In conclusion, I firmly believe that...</strong>', 'La non-conclusion « chacun voit midi à sa porte » est sanctionnée : il faut trancher.'),
    ('At the contrary, parks are useful.', '<strong>On the contrary</strong>, parks are useful.', 'Au contraire = ON the contrary — et ne le confondez pas avec on the other hand (en revanche).'),
    ('We can say that the cost is a problem.', '<strong>It could be argued that</strong> the cost is a problem.', '« On peut dire que » → tournure impersonnelle académique, pas we can say.'),
  ],
  summary=[
    ('Plan', 'intro · point 1 · point 2 · votre idée · conclusion', '140–190 mots'),
    ('Intro', 'reformuler + annoncer l’opinion', 'It is often said that...'),
    ('Enchaîner', 'Firstly · Furthermore · However', 'Furthermore, ...'),
    ('Opinion variée', 'In my view · I would argue', 'I would argue that...'),
    ('Impersonnel', 'It could be argued that', 'It could be argued that...'),
    ('Conclusion', 'On balance + position nette', 'I firmly believe...'),
  ],
  ex1=('Choisis la bonne option', 'La mécanique de l’essay.', [
    ('La bonne ouverture d’essay :', ['It is often said that homework is essential.', 'Hi! Let’s talk about homework!', 'Homework: I will give my opinion below.'], 'It is often said that homework is essential.',
     'Reformulation impersonnelle et formelle — pas de ton article ni d’annonce sèche.'),
    ('Le connecteur d’ajout formel :', ['Furthermore', 'What’s more', 'Plus'], 'Furthermore',
     'Furthermore/Moreover pour l’essay ; what’s more est pour l’article.'),
    ('« En revanche » :', ['On the other hand', 'On another hand', 'In the other hand'], 'On the other hand',
     'On the other hand — jamais in/another.'),
    ('La formule d’opinion variée :', ['I would argue that...', 'I think that... again', 'For me it is like that'], 'I would argue that...',
     'I would argue that : l’opinion argumentée du B2.'),
    ('Le registre de l’essay :', ['formel, sans contractions', 'semi-informel avec contractions', 'familier et direct'], 'formel, sans contractions',
     'Essay = registre formel : do not, it is, cannot.'),
    ('La bonne conclusion :', ['On balance, I firmly believe parks are essential.', 'To finish, everyone has a different opinion.', 'So yeah, parks are cool.'], 'On balance, I firmly believe parks are essential.',
     'On balance + position tranchée — le First exige une opinion nette.'),
  ]),
  ex2=('Complète l’essay', 'Écris le mot manquant.', [
    ('To begin ______, exercise improves concentration. (la particule)', 'with',
     'To begin WITH = pour commencer.'),
    ('It could be ______ that the cost is too high. (argue au participe)', 'argued',
     'It could be argued that — l’impersonnel académique.'),
    ('On the other ______, public transport is cheaper. (en revanche)', 'hand',
     'On the other HAND.'),
    ('In ______, I believe the advantages outweigh the drawbacks. (pour conclure)', 'conclusion',
     'In conclusion — le signal de la fin.'),
    ('The benefits far ______ the costs. (l’emporter sur)', 'outweigh',
     'Outweigh = peser plus lourd que — le verbe de la balance argumentative.'),
  ]),
  ex3=('Choisis la version anglaise naturelle', 'Registre et gallicismes.', [
    ('« On peut dire que les villes sont saturées. »', ['It could be argued that cities are overcrowded.', 'We can say that cities are saturated.', 'One can say cities are full up.'], 'It could be argued that cities are overcrowded.',
     'La tournure impersonnelle académique remplace « on peut dire ».'),
    ('« Au contraire, cela crée des emplois. »', ['On the contrary, it creates jobs.', 'At the contrary, it creates jobs.', 'To the contrary, it creates the jobs.'], 'On the contrary, it creates jobs.',
     'ON the contrary.'),
    ('« Il ne faut pas oublier le coût. »', ['The cost should not be overlooked.', 'It must not forget the cost.', 'We don’t have to forget the cost.'], 'The cost should not be overlooked.',
     'Passif impersonnel formel ; don’t have to = ne pas être obligé.'),
    ('« À mon avis, c’est une erreur. »', ['In my view, this is a mistake.', 'According to me, it is an error.', 'For my opinion, it is a mistake.'], 'In my view, this is a mistake.',
     'In my view / in my opinion — jamais according to me.'),
    ('« Tout bien pesé, je suis pour. »', ['On balance, I am in favour.', 'All well weighed, I am for.', 'Everything well thought, I am pro.'], 'On balance, I am in favour.',
     'On balance + in favour (of) : la conclusion mesurée.'),
  ]),
  game_desc='Chaque outil de l’essay passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('it-is-often-said', 'It is often said that', 'l’ouverture impersonnelle', 'introduction', '<b>It is often said that</b> parks are essential.', 'It is often ______ that parks are essential. (say au participe)', 'said'),
    ('furthermore', 'Furthermore', 'de plus (formel)', 'ajout', '<b>Furthermore</b>, green spaces encourage exercise.', '______, green spaces encourage exercise. (de plus, formel)', 'furthermore'),
    ('on-the-other-hand', 'On the other hand', 'en revanche', 'contraste', '<b>On the other hand</b>, parks are expensive.', 'On the other ______, parks are expensive.', 'hand'),
    ('i-would-argue', 'I would argue that', 'je soutiens que', 'opinion', '<b>I would argue that</b> the benefits outweigh the costs.', 'I would ______ that the benefits outweigh the costs.', 'argue'),
    ('it-could-be-argued', 'It could be argued that', 'on peut soutenir que', 'impersonnel', '<b>It could be argued that</b> taxes are better spent elsewhere.', 'It could be ______ that taxes are better spent elsewhere.', 'argued'),
    ('on-balance', 'On balance', 'tout bien pesé', 'conclusion', '<b>On balance</b>, I am in favour of the idea.', 'On ______, I am in favour of the idea.', 'balance'),
    ('outweigh', 'outweigh', 'l’emporter sur', 'argument', 'The benefits far <b>outweigh</b> the costs.', 'The benefits far ______ the costs. (peser plus lourd)', 'outweigh'),
    ('to-sum-up', 'To sum up', 'en résumé', 'synthèse', '<b>To sum up</b>, every town needs a park.', 'To ______ up, every town needs a park.', 'sum'),
  ],
),

'formal-email': dict(
  level='b2', section='redaction', num='Ch. 3', short='Formal Email',
  title='Formal Email — L’email formel sans gallicismes',
  subtitle='I am writing to... · I would be grateful if... · Yours faithfully',
  slides=[
    ('Plus simple que la lettre française', None,
     '<p class="slide-explanation">Bonne nouvelle : l’anglais formel est <b>sobre</b>. Pas d’équivalent de « Je vous prie d’agréer l’expression de mes salutations distinguées » — deux mots suffisent : <b>Yours sincerely</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Dear Mr Johnson,</b> (nom connu) → <b>Yours sincerely,</b></p>'
     '<p style="margin-top:8px"><b>Dear Sir or Madam,</b> (nom inconnu) → <b>Yours faithfully,</b></p></div>'
     '<p style="margin-top:16px">La règle d’or : nom connu = sincerely ; inconnu = faithfully.</p>'),
    ('La première phrase : I am writing to...', None,
     '<p class="slide-explanation">On annonce l’objet immédiatement : <b>I am writing to enquire about / to complain about / to apply for / in response to...</b> Sans contractions : <b>I am</b>, pas I’m.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I am writing to enquire about the summer course advertised on your website.</b></p></div>'),
    ('Demander poliment', None,
     '<p class="slide-explanation">La politesse anglaise passe par le conditionnel : <b>I would be grateful if you could... · Could you possibly...? · I would appreciate it if...</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I would be grateful if you could send me further details.</b></p>'
     '<p style="margin-top:8px"><b>Could you possibly confirm the dates?</b></p></div>'
     '<p style="margin-top:16px">« Merci de m’envoyer... » ne se traduit pas par Thank you to send me — c’est <b>Please send me</b> ou la formule au conditionnel.</p>'),
    ('Se plaindre avec fermeté polie', None,
     '<p class="slide-explanation">La réclamation B2 : ferme sur les faits, polie sur la forme. <b>I was disappointed to find that... · Unfortunately, ... · I would like a full refund · Unless this matter is resolved, ...</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I was disappointed to find that the room did not match the description.</b></p></div>'),
    ('Conclure l’email formel', None,
     '<p class="slide-explanation">Avant la signature : <b>I look forward to hearing from you. · Thank you in advance for your help. · Please do not hesitate to contact me if you require further information.</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I look forward to hearing from you.<br>Yours faithfully,<br>Camille Bernard</b></p></div>'),
  ],
  traps=[
    ('Dear Sir or Madam, ... Yours sincerely,', 'Dear Sir or Madam, ... <strong>Yours faithfully,</strong>', 'Nom inconnu → faithfully ; nom connu → sincerely. Le mélange coûte des points.'),
    ('Thank you to send me the brochure.', '<strong>Please send me</strong> the brochure. / <strong>I would be grateful if you could send</strong>...', '« Merci de + infinitif » ne se calque pas : thank you to send n’existe pas.'),
    ('I’m writing to complain about my stay.', '<strong>I am writing</strong> to complain about my stay.', 'Pas de contractions dans un email formel : I am, do not, cannot.'),
    ('I wait for your answer.', '<strong>I look forward to hearing from you.</strong>', '« J’attends votre réponse » se dit avec la formule consacrée — i wait for your answer sonne abrupt.'),
    ('Please agree my distinguished salutations.', '<strong>Yours sincerely,</strong>', 'Les salutations distinguées ne se traduisent pas — la clôture anglaise tient en deux mots.'),
  ],
  summary=[
    ('Salutation', 'Dear Mr X / Dear Sir or Madam', 'Dear Ms Carter,'),
    ('Objet', 'I am writing to + infinitif', 'I am writing to enquire about...'),
    ('Demande polie', 'I would be grateful if you could', '...send me further details.'),
    ('Réclamation', 'I was disappointed to find that', '...the room was not clean.'),
    ('Avant signature', 'I look forward to hearing from you', '+ Thank you in advance'),
    ('Signature', 'sincerely (nom connu) / faithfully (inconnu)', 'Yours faithfully,'),
  ],
  ex1=('Choisis la bonne option', 'Les codes de l’email formel.', [
    ('Vous écrivez à « Dear Sir or Madam ». La signature :', ['Yours faithfully,', 'Yours sincerely,', 'Love,'], 'Yours faithfully,',
     'Nom inconnu → Yours faithfully.'),
    ('La bonne première phrase :', ['I am writing to enquire about your courses.', 'I write you because I want informations.', 'Hi! I’d like to know more!'], 'I am writing to enquire about your courses.',
     'I am writing to + infinitif — sans contraction, objet immédiat.'),
    ('« Je vous serais reconnaissant de m’envoyer... » :', ['I would be grateful if you could send me...', 'I would be recognising if you send me...', 'Thank you to send me...'], 'I would be grateful if you could send me...',
     'La formule au conditionnel — grateful if you could.'),
    ('« Veuillez ne pas hésiter à me contacter » :', ['Please do not hesitate to contact me.', 'Want well not hesitate to contact me.', 'You must contact me without hesitation.'], 'Please do not hesitate to contact me.',
     'Please do not hesitate to + infinitif.'),
    ('Le ton d’une réclamation B2 :', ['ferme sur les faits, poli sur la forme', 'agressif pour être pris au sérieux', 'd’excuse, pour ne pas déranger'], 'ferme sur les faits, poli sur la forme',
     'I was disappointed to find that... — fermeté polie.'),
    ('« informations » en anglais :', ['information (indénombrable)', 'informations', 'an information'], 'information (indénombrable)',
     'Information est indénombrable : some information, jamais informations.'),
  ]),
  ex2=('Complète l’email formel', 'Écris le mot manquant.', [
    ('I am writing ______ complain about the service I received. (la particule)', 'to',
     'I am writing TO + infinitif.'),
    ('I would be ______ if you could confirm my booking. (reconnaissant)', 'grateful',
     'I would be GRATEFUL if you could...'),
    ('I look forward to ______ from you. (hear en -ing)', 'hearing',
     'Look forward to + -ing — même en formel.'),
    ('Yours ______, (après Dear Sir or Madam)', 'faithfully',
     'Nom inconnu → Yours faithfully.'),
    ('I was ______ to find that the product was damaged. (déçu)', 'disappointed',
     'I was disappointed to find that... — l’ouverture de réclamation.'),
  ]),
  ex3=('Choisis la version anglaise naturelle', 'Formules sans calques.', [
    ('« Suite à votre annonce, je me permets de vous écrire. »', ['I am writing in response to your advertisement.', 'Following to your announce, I allow myself to write you.', 'After your annonce, I permit me to write.'], 'I am writing in response to your advertisement.',
     'In response to your advertisement — sobre et direct.'),
    ('« Merci d’avance pour votre aide. »', ['Thank you in advance for your help.', 'Thank you of advance for your help.', 'Thanks before for your helping.'], 'Thank you in advance for your help.',
     'Thank you IN advance.'),
    ('« J’exige un remboursement intégral. »', ['I would like a full refund.', 'I exige a full refunding.', 'I demand you reimburse me totally.'], 'I would like a full refund.',
     'La fermeté polie : I would like a full refund (refund = remboursement).'),
    ('« Dans l’attente de votre réponse. »', ['I look forward to hearing from you.', 'In the wait of your answer.', 'Waiting for your response, I stay.'], 'I look forward to hearing from you.',
     'La formule consacrée — pas de traduction littérale.'),
    ('« Je souhaite poser ma candidature pour le poste. »', ['I would like to apply for the position.', 'I wish to pose my candidature for the post.', 'I want to candidate for the job.'], 'I would like to apply for the position.',
     'Apply for a position — candidature = application.'),
  ]),
  game_desc='Chaque formule de l’email formel passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('writing-to', 'I am writing to...', 'l’annonce de l’objet', 'ouverture', '<b>I am writing to</b> enquire about the course.', 'I am ______ to enquire about the course.', 'writing'),
    ('grateful-if', 'I would be grateful if', 'je vous serais reconnaissant', 'demande', '<b>I would be grateful if</b> you could send details.', 'I would be ______ if you could send details.', 'grateful'),
    ('faithfully', 'Yours faithfully', 'clôture (nom inconnu)', 'signature', 'Dear Sir or Madam ... <b>Yours faithfully,</b>', 'Dear Sir or Madam ... Yours ______,', 'faithfully'),
    ('sincerely', 'Yours sincerely', 'clôture (nom connu)', 'signature', 'Dear Ms Carter ... <b>Yours sincerely,</b>', 'Dear Ms Carter ... Yours ______,', 'sincerely'),
    ('disappointed-to', 'I was disappointed to find', 'l’ouverture de réclamation', 'réclamation', '<b>I was disappointed to find</b> that the room was dirty.', 'I was ______ to find that the room was dirty.', 'disappointed'),
    ('refund', 'a full refund', 'un remboursement intégral', 'exigence', 'I would like <b>a full refund</b>.', 'I would like a full ______. (remboursement)', 'refund'),
    ('do-not-hesitate', 'do not hesitate to', 'n’hésitez pas à', 'clôture polie', 'Please <b>do not hesitate to</b> contact me.', 'Please do not ______ to contact me.', 'hesitate'),
    ('enquire', 'enquire about', 'se renseigner sur', 'objet', 'I am writing to <b>enquire about</b> the course.', 'I am writing to ______ about the course. (se renseigner)', 'enquire'),
  ],
),

'report': dict(
  level='b2', section='redaction', num='Ch. 4', short='Report',
  title='Report — Le rapport structuré',
  subtitle='Sous-titres, passif, recommandations : l’écrit le plus balisé',
  slides=[
    ('Le format le plus reconnaissable', None,
     '<p class="slide-explanation">Le report est l’écrit le plus codifié du First : <b>titre + sous-titres</b> (Introduction · Findings · Recommendations), ton impersonnel, zéro anecdote. C’est l’ami des candidats méthodiques.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Report on the school canteen</b></p>'
     '<p style="margin-top:8px"><b>Introduction</b> · <b>Current situation</b> · <b>Recommendations</b></p></div>'),
    ('L’introduction : but du rapport', None,
     '<p class="slide-explanation">Une formule consacrée : <b>The aim of this report is to...</b> + comment l’information a été collectée.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The aim of this report is to assess the canteen facilities and suggest improvements. Fifty students were interviewed.</b></p></div>'),
    ('Le passif : la voix du rapport', None,
     '<p class="slide-explanation">Le rapport s’écrit à l’impersonnel — le passif y règne : <b>It was found that... · Students were asked... · A survey was carried out...</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>It was found that most students avoid the canteen on Fridays.</b></p>'
     '<p style="margin-top:8px"><b>A number of complaints were received about the queues.</b></p></div>'
     '<p style="margin-top:16px">Là où le français dirait « on a constaté que », l’anglais passe au passif.</p>'),
    ('Quantifier les résultats', None,
     '<p class="slide-explanation">Findings = des faits chiffrés ou proportionnés : <b>The majority of... · Almost half of... · Only a minority... · Most of those surveyed...</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The majority of students said prices were too high.</b></p>'
     '<p style="margin-top:8px"><b>Almost half of those surveyed asked for vegetarian options.</b></p></div>'),
    ('Les recommandations', None,
     '<p class="slide-explanation">La section finale recommande sans ordonner : <b>It is recommended that... · It would be advisable to... · The school should consider + -ing...</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>It is recommended that opening hours be extended.</b></p>'
     '<p style="margin-top:8px"><b>The school should consider installing more seating.</b></p></div>'),
  ],
  traps=[
    ('Écrire le report comme une lettre (Dear..., I think...)', 'Titre + sous-titres + ton impersonnel : <strong>The aim of this report is to...</strong>', 'Le report n’a ni destinataire nommé ni je omniprésent — c’est un document, pas une correspondance.'),
    ('We made a survey.', 'A survey <strong>was carried out</strong>.', '« Faire un sondage » = carry out/conduct a survey — et le passif est le ton du rapport.'),
    ('The most of students are happy.', '<strong>Most</strong> students are happy. / <strong>The majority of</strong> students...', '« La plupart des » = most + nom (sans the) ou the majority of.'),
    ('It is recommended to extend the hours. (correct mais limité)', 'Variez : <strong>It is recommended that hours be extended.</strong>', 'La structure that + subjonctif (be extended) montre la gamme B2-C1 attendue dans un report.'),
    ('I think the canteen is bad.', '<strong>It was felt that the canteen needed improvement.</strong>', 'L’opinion personnelle brute n’a pas sa place — l’impersonnel rapporte ce que pensent les sondés.'),
  ],
  summary=[
    ('Format', 'titre + sous-titres', 'Introduction · Findings · Recommendations'),
    ('But', 'The aim of this report is to...', '...assess the facilities.'),
    ('Voix', 'passif impersonnel', 'It was found that...'),
    ('Enquête', 'a survey was carried out', 'Fifty students were interviewed.'),
    ('Quantifier', 'the majority of · almost half', 'Most of those surveyed...'),
    ('Recommander', 'It is recommended that... be...', '...hours be extended.'),
  ],
  ex1=('Choisis la bonne option', 'Les codes du report.', [
    ('La bonne première phrase d’un report :', ['The aim of this report is to assess the new library.', 'Hi everyone, let me tell you about the library!', 'I am writing to complain about the library.'], 'The aim of this report is to assess the new library.',
     'The aim of this report is to... — la formule d’ouverture consacrée.'),
    ('« On a constaté que... » :', ['It was found that...', 'We have constated that...', 'One found that...'], 'It was found that...',
     'Le passif impersonnel : it was found that.'),
    ('« Réaliser un sondage » :', ['carry out a survey', 'make a survey', 'realise a survey'], 'carry out a survey',
     'Carry out / conduct a survey — make a survey est un calque.'),
    ('« La plupart des élèves » :', ['most students', 'the most of students', 'the most students'], 'most students',
     'Most + nom directement, sans the.'),
    ('La section finale d’un report :', ['Recommendations', 'Conclusion of my opinions', 'The end'], 'Recommendations',
     'Le report se termine par des recommandations actionnables.'),
    ('« Il serait souhaitable de... » :', ['It would be advisable to...', 'It would be wishable to...', 'It should be souhaitable to...'], 'It would be advisable to...',
     'Advisable = souhaitable/judicieux — la recommandation mesurée.'),
  ]),
  ex2=('Complète le report', 'Écris le mot manquant.', [
    ('The ______ of this report is to evaluate the sports facilities. (le but)', 'aim',
     'The AIM of this report is to...'),
    ('A survey was carried ______ among 80 members. (la particule)', 'out',
     'Carry OUT a survey.'),
    ('It was ______ that queues were the main complaint. (find au participe)', 'found',
     'It was FOUND that — le constat passif.'),
    ('It is recommended that the café ______ open until 8 pm. (be au subjonctif)', 'be',
     'Recommend that + subjonctif : that the café BE open.'),
    ('The ______ of users were satisfied with the staff. (la majorité)', 'majority',
     'The MAJORITY of users.'),
  ]),
  ex3=('Choisis la version anglaise naturelle', 'Le ton impersonnel.', [
    ('« On a interrogé cinquante étudiants. »', ['Fifty students were interviewed.', 'One interrogated fifty students.', 'We made interviews to fifty students.'], 'Fifty students were interviewed.',
     'Le passif remplace le « on » : were interviewed.'),
    ('« Presque la moitié des sondés sont mécontents. »', ['Almost half of those surveyed are dissatisfied.', 'Almost the half of sounded people are unhappy.', 'Nearly the half of the survey is angry.'], 'Almost half of those surveyed are dissatisfied.',
     'Almost half of those surveyed — la quantification du report.'),
    ('« Il est recommandé d’agrandir le parking. »', ['It is recommended that the car park be extended.', 'It is recommended to agrandise the parking.', 'We recommend you must extend the parking.'], 'It is recommended that the car park be extended.',
     'It is recommended that + subjonctif passif. (Et car park, pas parking seul.)'),
    ('« L’école devrait envisager d’embaucher un deuxième cuisinier. »', ['The school should consider hiring a second cook.', 'The school should consider to hire a second cook.', 'The school should envisage to engage a second cook.'], 'The school should consider hiring a second cook.',
     'Consider + -ing : should consider hiring.'),
    ('Quelle phrase appartient à un report (et non à une lettre) ?', ['It was felt that prices were too high.', 'I really hate the prices here!', 'You should lower your prices, please.'], 'It was felt that prices were too high.',
     'L’impersonnel passif est la voix du report.'),
  ]),
  game_desc='Chaque outil du report passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('aim-of-report', 'The aim of this report', 'le but de ce rapport', 'introduction', '<b>The aim of this report</b> is to assess the canteen.', 'The ______ of this report is to assess the canteen.', 'aim'),
    ('it-was-found', 'It was found that', 'on a constaté que', 'constat', '<b>It was found that</b> most students avoid Fridays.', 'It was ______ that most students avoid Fridays.', 'found'),
    ('carry-out', 'carry out a survey', 'réaliser un sondage', 'méthode', 'A survey <b>was carried out</b>.', 'A survey was carried ______.', 'out'),
    ('majority', 'the majority of', 'la majorité de', 'quantité', '<b>The majority of</b> students were satisfied.', 'The ______ of students were satisfied.', 'majority'),
    ('recommended-that', 'It is recommended that', 'il est recommandé que', 'recommandation', '<b>It is recommended that</b> hours be extended.', 'It is ______ that hours be extended.', 'recommended'),
    ('advisable', 'It would be advisable to', 'il serait souhaitable de', 'conseil', '<b>It would be advisable to</b> install more seating.', 'It would be ______ to install more seating.', 'advisable'),
    ('consider-ing', 'consider + -ing', 'envisager de faire', 'suggestion', 'The school should <b>consider installing</b> more seats.', 'The school should consider ______ more seats. (install en -ing)', 'installing'),
    ('those-surveyed', 'those surveyed', 'les personnes sondées', 'enquête', 'Half of <b>those surveyed</b> wanted longer hours.', 'Half of those ______ wanted longer hours. (sondés)', 'surveyed'),
  ],
),

'review': dict(
  level='b2', section='redaction', num='Ch. 5', short='Review',
  title='Review — La critique qui donne envie (ou pas)',
  subtitle='Décrire, évaluer, recommander : le trio de la review',
  slides=[
    ('La mission de la review', None,
     '<p class="slide-explanation">Trois temps : <b>décrire</b> (film, livre, restaurant...), <b>évaluer</b> (points forts ET faibles), <b>recommander</b> (clairement). Registre semi-informel, lecteur impliqué — entre l’article et le report.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>If you only watch one film this year, make it this one.</b></p></div>'),
    ('Décrire sans tout révéler', None,
     '<p class="slide-explanation">L’intrigue se raconte au <b>présent</b> (comme en français) et sans spoiler : <b>The story follows... · It is set in... · The plot revolves around...</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Set in 1980s Berlin, the story follows two brothers who...</b></p>'
     '<p style="margin-top:8px"><b>I won’t give away the ending — but expect a twist.</b></p></div>'),
    ('Le lexique de l’évaluation', None,
     '<p class="slide-explanation">La review vit de ses adjectifs : <b>gripping</b> (captivant), <b>breathtaking</b> (à couper le souffle), <b>outstanding</b> (exceptionnel), <b>disappointing</b>, <b>predictable</b> (convenu), <b>far-fetched</b> (tiré par les cheveux).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The plot is gripping, although the ending feels rushed.</b></p></div>'),
    ('Équilibrer : le bémol qui crédibilise', None,
     '<p class="slide-explanation">Une review 100 % élogieuse sonne faux. Un bémol nuancé crédibilise : <b>My only criticism is that... · The only letdown was... · Although..., ...</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>My only criticism is that the second half drags a little.</b></p></div>'),
    ('La recommandation finale', None,
     '<p class="slide-explanation">La review se termine par un verdict net : <b>I would thoroughly recommend it to anyone who... · It’s well worth + -ing · Don’t miss it. · Give it a miss.</b> (passez votre chemin)</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I would thoroughly recommend it to anyone who enjoys clever thrillers.</b></p>'
     '<p style="margin-top:8px"><b>It’s well worth seeing on the big screen.</b></p></div>'),
  ],
  traps=[
    ('I recommend you this film.', 'I recommend <strong>this film (to you)</strong>. / I’d <strong>recommend it to anyone who...</strong>', 'Recommend something to somebody — l’objet direct d’abord, comme explain.'),
    ('The film tells the story of... it passed in Berlin.', 'The film is <strong>set in</strong> Berlin.', '« Ça se passe à » = it is set in — pas it passes.'),
    ('The actors play very well.', 'The acting is <strong>outstanding</strong>. / The cast <strong>gives a superb performance</strong>.', '« Jouer bien » se dit avec acting/performance — play well, c’est pour le sport.'),
    ('It’s a very good film. The actors are very good. The music is very good.', 'Variez : <strong>gripping · outstanding · memorable</strong>', 'Trois very good d’affilée plafonnent la note lexicale.'),
    ('I advise you to not see this film.', '<strong>Give it a miss.</strong> / I <strong>wouldn’t recommend it</strong>.', 'La déconseillance idiomatique : give it a miss, not worth seeing.'),
  ],
  summary=[
    ('Plan', 'décrire · évaluer · recommander', '3 temps + titre'),
    ('Intrigue', 'présent + is set in', 'The story follows...'),
    ('Éloge', 'gripping · outstanding · breathtaking', 'The plot is gripping.'),
    ('Bémol', 'My only criticism is that...', '...the ending feels rushed.'),
    ('Conseiller', 'well worth + -ing · Don’t miss it', 'It’s well worth seeing.'),
    ('Déconseiller', 'Give it a miss.', 'predictable · far-fetched'),
  ],
  ex1=('Choisis la bonne option', 'Les outils de la review.', [
    ('« L’histoire se déroule à Tokyo » :', ['The story is set in Tokyo.', 'The story passes in Tokyo.', 'The story deroules in Tokyo.'], 'The story is set in Tokyo.',
     'Be set in = se dérouler à (lieu/époque).'),
    ('« Captivant » :', ['gripping', 'gripped', 'grippy'], 'gripping',
     'Gripping — l’adjectif fétiche des reviews.'),
    ('Le bémol bien formulé :', ['My only criticism is that the ending feels rushed.', 'It is bad at the end.', 'The end is null.'], 'My only criticism is that the ending feels rushed.',
     'My only criticism is that... — le bémol qui crédibilise.'),
    ('« Ça vaut vraiment le coup d’y aller » :', ['It’s well worth going.', 'It values really the blow to go.', 'It worths the pain.'], 'It’s well worth going.',
     'Well worth + -ing — « valoir le coup » ne se traduit jamais littéralement.'),
    ('« Tiré par les cheveux » :', ['far-fetched', 'pulled by the hair', 'hair-pulled'], 'far-fetched',
     'Far-fetched = invraisemblable, tiré par les cheveux.'),
    ('On raconte l’intrigue :', ['au présent', 'au prétérit', 'au past perfect'], 'au présent',
     'The story follows... he discovers... — le présent de narration critique.'),
  ]),
  ex2=('Complète la review', 'Écris le mot manquant.', [
    ('______ in 1920s Paris, the novel follows a young painter. (se déroulant à — participe)', 'set',
     'Set in + lieu/époque, en tête de phrase.'),
    ('The plot is ______ from start to finish. (captivant)', 'gripping',
     'Gripping = qui tient en haleine.'),
    ('My only ______ is that the film is slightly too long. (bémol)', 'criticism',
     'My only criticism is that...'),
    ('I won’t give ______ the ending. (révéler — particule)', 'away',
     'Give away = révéler, spoiler.'),
    ('It’s well ______ visiting if you love modern art. (vaut le coup)', 'worth',
     'Well WORTH + -ing.'),
  ]),
  ex3=('Choisis la version anglaise naturelle', 'Le lexique de la critique.', [
    ('« Je le recommande vivement à tous les amateurs de polars. »', ['I would thoroughly recommend it to anyone who enjoys crime fiction.', 'I recommend it strongly at all the amateurs of polars.', 'I advise it vividly to crime amateurs.'], 'I would thoroughly recommend it to anyone who enjoys crime fiction.',
     'Thoroughly recommend it to anyone who... — la recommandation B2.'),
    ('« Les acteurs sont excellents. »', ['The cast gives an outstanding performance.', 'The actors play very good.', 'The actors are playing well themselves.'], 'The cast gives an outstanding performance.',
     'Cast + performance : le lexique de la critique.'),
    ('« La fin est convenue et décevante. »', ['The ending is predictable and disappointing.', 'The end is convened and deceiving.', 'The final is predictable and deceptive.'], 'The ending is predictable and disappointing.',
     'Predictable + disappointing — attention : deceiving = trompeur, pas décevant.'),
    ('« Franchement, passez votre chemin. »', ['Frankly, give it a miss.', 'Frankly, pass your road.', 'Honestly, pass away.'], 'Frankly, give it a miss.',
     'Give it a miss = ne vous donnez pas la peine. (Pass away = décéder !)'),
    ('« À couper le souffle » :', ['breathtaking', 'breath-cutting', 'air-stopping'], 'breathtaking',
     'Breathtaking — l’éloge superlatif des reviews.'),
  ]),
  game_desc='Chaque outil de la review passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('set-in', 'is set in', 'se déroule à/en', 'décor', 'The story <b>is set in</b> 1980s Berlin.', 'The story is ______ in 1980s Berlin.', 'set'),
    ('gripping', 'gripping', 'captivant', 'éloge', 'The plot is <b>gripping</b>.', 'The plot is ______. (captivant)', 'gripping'),
    ('breathtaking', 'breathtaking', 'à couper le souffle', 'superlatif', 'The scenery is <b>breathtaking</b>.', 'The scenery is ______. (à couper le souffle)', 'breathtaking'),
    ('predictable', 'predictable', 'convenu, prévisible', 'critique', 'The ending is <b>predictable</b>.', 'The ending is ______. (prévisible)', 'predictable'),
    ('far-fetched', 'far-fetched', 'tiré par les cheveux', 'critique', 'The plot twist is <b>far-fetched</b>.', 'The plot twist is far-______. (tiré par les cheveux)', 'fetched'),
    ('only-criticism', 'My only criticism', 'mon seul bémol', 'nuance', '<b>My only criticism</b> is that it drags a little.', 'My only ______ is that it drags a little.', 'criticism'),
    ('well-worth', 'well worth + -ing', 'ça vaut vraiment le coup', 'recommandation', 'It’s <b>well worth seeing</b>.', 'It’s well ______ seeing.', 'worth'),
    ('give-it-a-miss', 'give it a miss', 'passez votre chemin', 'déconseiller', 'Frankly, <b>give it a miss</b>.', 'Frankly, give it a ______. (passez votre chemin)', 'miss'),
  ],
),

}
