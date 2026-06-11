# -*- coding: utf-8 -*-
"""fr/ B2 grammaire — lot 1 (4 chapitres)."""

CHAPTERS = {

'articles': dict(
  level='b2', section='grammaire', num='Ch. 1', short='Articles',
  title='Articles — The, a, ou rien du tout ?',
  subtitle='Le piège invisible : l’article zéro',
  slides=[
    ('Le grand écart avec le français', None,
     '<p class="slide-explanation">Le français met « le/la/les » partout ; l’anglais supprime l’article pour les généralités. C’est l’erreur la plus tenace des francophones avancés.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>« La vie est belle. » → <b>Life is beautiful.</b> (pas « the life »)</p>'
     '<p style="margin-top:8px">« J’adore le café. » → <b>I love coffee.</b></p>'
     '<p style="margin-top:8px">« Les chats sont indépendants. » → <b>Cats are independent.</b></p></div>'),
    ('The : du spécifique seulement', None,
     '<p class="slide-explanation"><b>The</b> s’emploie quand on sait DE QUEL exemplaire on parle — déjà mentionné, unique, ou précisé.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The coffee you made was delicious.</b> (celui que tu as fait — spécifique)</p>'
     '<p style="margin-top:8px"><b>The sun, the government, the internet</b> (uniques)</p></div>'),
    ('A/an : métiers et premières mentions', None,
     '<p class="slide-explanation">Contrairement au français, les métiers exigent l’article : <b>She’s a doctor.</b> (« Elle est médecin »).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>He’s an engineer.</b> (Il est ingénieur.)</p>'
     '<p style="margin-top:8px"><b>I saw a film last night. The film was awful.</b> (a = première mention, the = reprise)</p></div>'),
    ('Zéro article : la liste à connaître', None,
     '<p class="slide-explanation">Pas d’article devant : généralités au pluriel/indénombrable, repas, langues, sports, et les institutions « en usage ».</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>have breakfast · play football · speak English</b></p>'
     '<p style="margin-top:8px"><b>go to school / to work / to bed</b> (l’usage, pas le bâtiment)</p>'
     '<p style="margin-top:8px">mais : <b>go to the school</b> (le bâtiment précis, ex. pour une réunion)</p></div>'),
    ('Géographie', None,
     '<p class="slide-explanation">Pays au singulier sans article (<b>France, Spain</b>), mais : <b>the UK, the USA, the Netherlands</b> (pluriels/sigles). Fleuves, mers, montagnes (chaînes) → the ; lacs et sommets isolés → rien.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>the Thames, the Alps, the Mediterranean</b> · <b>Lake Geneva, Mont Blanc</b></p></div>'),
  ],
  traps=[
    ('The life is hard.', '<strong>Life</strong> is hard.', 'Généralité → article zéro. « The life » désignerait une vie précise.'),
    ('She is doctor.', 'She is <strong>a</strong> doctor.', 'Métier → a/an obligatoire, contrairement au français « elle est médecin ».'),
    ('I love the chocolate. (en général)', 'I love <strong>chocolate</strong>.', 'Goût général → zéro article. The chocolate = ce chocolat-là.'),
    ('He’s in the prison. (il est incarcéré)', "He's in <strong>prison</strong>.", 'Institution « en usage » → sans the. In the prison = dans le bâtiment (en visite).'),
    ('I visited the France last year.', 'I visited <strong>France</strong> last year.', 'Pays au singulier → sans article (sauf the UK, the USA...).'),
  ],
  summary=[
    ('Généralité', 'article zéro', 'Life is beautiful. Cats are...'),
    ('Spécifique', 'the', 'the coffee you made'),
    ('Métier', 'a/an', "She's a doctor."),
    ('Institutions', 'school, work, bed sans the', 'go to school, be in prison'),
    ('Pays', 'sans article (sauf UK, USA...)', 'France · the UK'),
    ('Fleuves, chaînes', 'the', 'the Thames, the Alps'),
  ],
  ex1=('The, a/an ou rien ?', 'Choisis l’article (∅ = aucun).', [
    ('______ money doesn’t buy happiness.', ['∅', 'The', 'A'], '∅',
     'Généralité sur l’argent → zéro article : Money doesn’t buy happiness.'),
    ('My sister is ______ architect.', ['an', 'the', '∅'], 'an',
     'Métier → a/an : an architect (an devant voyelle).'),
    ('______ book you lent me is brilliant.', ['The', 'A', '∅'], 'The',
     'Spécifique (celui que tu m’as prêté) → the.'),
    ('She goes to ______ work by bike.', ['∅', 'the', 'a'], '∅',
     'Work « en usage » → sans article : go to work.'),
    ('We sailed down ______ Thames.', ['the', '∅', 'a'], 'the',
     'Les fleuves prennent the : the Thames.'),
    ('They moved to ______ Netherlands.', ['the', '∅', 'a'], 'the',
     'Pays au pluriel → the Netherlands.'),
  ]),
  ex2=('Complète (ou laisse vide avec « x »)', 'Écris the, a, an — ou x si aucun article.', [
    ('I love ______ Italian food. (en général)', 'x',
     'Généralité → zéro article : I love Italian food.'),
    ('He’s ______ honest man. (attention au son !)', 'an',
     'Honest commence par un son voyelle (h muet) → an honest man.'),
    ('______ children learn languages quickly. (les enfants en général)', 'x',
     'Généralité au pluriel → zéro article : Children learn...'),
    ('Could you pass ______ salt, please? (celui sur la table)', 'the',
     'Objet identifiable dans la situation → the salt.'),
    ('My son is still at ______ school. (il est scolarisé)', 'x',
     'Institution en usage → at school, sans article.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise correcte.', [
    ('« La vie est trop courte. »', ['Life is too short.', 'The life is too short.', 'A life is too short.'], 'Life is too short.',
     'Généralité → zéro article.'),
    ('« Elle est avocate. »', ["She's a lawyer.", "She's lawyer.", "She's the lawyer."], "She's a lawyer.",
     'Métier → a : she’s a lawyer.'),
    ('« Les Français aiment le fromage. » (généralité)', ['French people love cheese.', 'The French people love the cheese.', 'French people love the cheese.'], 'French people love cheese.',
     'Double généralité → double zéro article.'),
    ('« Il est à l’hôpital. » (comme patient)', ["He's in hospital.", "He's in the hospital building for visit.", "He's at an hospital."], "He's in hospital.",
     'Institution en usage (anglais britannique) → in hospital.'),
    ('« Le Mont Blanc est le plus haut sommet des Alpes. »', ['Mont Blanc is the highest peak in the Alps.', 'The Mont Blanc is the highest peak in Alps.', 'Mont Blanc is highest peak in the Alps.'], 'Mont Blanc is the highest peak in the Alps.',
     'Sommet isolé sans article ; chaîne de montagnes avec the.'),
  ]),
  game_desc='Chaque règle d’article passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('zero-general', 'article zéro (généralité)', 'la vie, le café en général : pas d’article', 'généralité', '<b>Life</b> is beautiful. I love <b>coffee</b>.', '______ is beautiful. (la vie)', 'life'),
    ('a-job', 'a + métier', 'elle est médecin = she is A doctor', 'métier', "She's <b>a doctor</b>.", "She's ______ doctor. (elle est médecin)", 'a'),
    ('the-specific', 'the (spécifique)', 'celui dont on parle déjà', 'spécifique', '<b>The coffee</b> you made was delicious.', '______ coffee you made was delicious.', 'the'),
    ('go-to-school', 'go to school (sans the)', 'l’institution en usage', 'institution', 'The kids go to <b>school</b> at eight.', 'The kids go to ______ at eight. (à l’école)', 'school'),
    ('in-prison', 'in prison', 'incarcéré — sans article', 'en prison', "He spent two years in <b>prison</b>.", 'He spent two years in ______ . (en prison)', 'prison'),
    ('the-uk', 'the UK / the USA', 'pays pluriels ou sigles → the', 'pays avec the', 'She lives in <b>the</b> UK.', 'She lives in ______ UK.', 'the'),
    ('the-thames', 'the + fleuve', 'fleuves, mers, chaînes → the', 'géographie avec the', 'We sailed down <b>the</b> Thames.', 'We sailed down ______ Thames.', 'the'),
    ('an-hour', 'an + son voyelle', 'an hour, an honest man — le son décide', 'an', 'It took <b>an</b> hour.', 'It took ______ hour.', 'an'),
  ],
),

'causative': dict(
  level='b2', section='grammaire', num='Ch. 2', short='Causative',
  title='Causative — Faire faire quelque chose',
  subtitle='Have/get something done : la traduction de « faire réparer »',
  slides=[
    ('« Je fais réparer ma voiture »', None,
     '<p class="slide-explanation">Pour dire qu’on confie une tâche à quelqu’un, l’anglais emploie <b>have + objet + participe passé</b>. C’est l’équivalent exact de notre « faire faire ».</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I’m having my car repaired.</b> (Je fais réparer ma voiture.)</p>'
     '<p style="margin-top:8px"><b>She had her hair cut yesterday.</b> (Elle s’est fait couper les cheveux.)</p></div>'
     '<p style="margin-top:16px">⚠ Sans cette structure, « I repaired my car » = je l’ai réparée moi-même !</p>'),
    ('Get : la version courante', None,
     '<p class="slide-explanation"><b>Get + objet + participe</b> : même sens, plus oral.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I need to get my phone fixed.</b> (Il faut que je fasse réparer mon téléphone.)</p>'
     '<p style="margin-top:8px"><b>Where did you get your suit made?</b></p></div>'),
    ('À tous les temps', None,
     '<p class="slide-explanation">Have se conjugue normalement ; la structure reste objet + participe.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>We’re having the kitchen redone.</b> (en ce moment)</p>'
     '<p style="margin-top:8px"><b>I’ll have the documents sent to you.</b> (je vous les ferai envoyer)</p>'
     '<p style="margin-top:8px"><b>She has just had her eyes tested.</b></p></div>'),
    ('Le sens « subir »', None,
     '<p class="slide-explanation">La même structure exprime une mésaventure subie.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>He had his wallet stolen.</b> (Il s’est fait voler son portefeuille.)</p>'
     '<p style="margin-top:8px"><b>They had their flight cancelled.</b></p></div>'
     '<p style="margin-top:16px">« Se faire voler/couper/livrer... » → have/get + objet + participe, dans les deux sens (volontaire ou subi).</p>'),
    ('Faire faire à quelqu’un : make et get', None,
     '<p class="slide-explanation">Pour la personne qu’on pousse à agir : <b>make someone do</b> (obliger, sans to) et <b>get someone to do</b> (persuader, avec to).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The teacher made us rewrite the essay.</b> (nous a fait réécrire — obligation)</p>'
     '<p style="margin-top:8px"><b>I got him to help me.</b> (je l’ai convaincu de m’aider)</p></div>'),
  ],
  traps=[
    ('I repaired my car at the garage. (le garagiste l’a fait)', 'I <strong>had my car repaired</strong> at the garage.', 'Sans la structure causative, vous dites que vous l’avez réparée vous-même.'),
    ('She cut her hair yesterday. (chez le coiffeur)', 'She <strong>had her hair cut</strong> yesterday.', '« Se faire couper les cheveux » → have + hair + cut.'),
    ('I had repaired my car. (ordre des mots)', 'I had my car <strong>repaired</strong>.', 'L’objet se place entre have et le participe — sinon c’est un past perfect !'),
    ('The teacher made us to rewrite the essay.', 'The teacher made us <strong>rewrite</strong> the essay.', 'Make + personne + base verbale, sans to.'),
    ('I got him help me.', 'I got him <strong>to help</strong> me.', 'Get + personne + TO + base : c’est make qui refuse le to.'),
  ],
  summary=[
    ('Faire faire (chose)', 'have + objet + participe', 'I had my car repaired.'),
    ('Version orale', 'get + objet + participe', 'Get your phone fixed.'),
    ('Subir', 'have + objet + participe', 'He had his wallet stolen.'),
    ('Obliger qqn', 'make + personne + base', 'She made us wait.'),
    ('Persuader qqn', 'get + personne + to + base', 'I got him to help.'),
  ],
  ex1=('Choisis la structure correcte', 'Qui fait l’action ?', [
    ('I ______ at the hairdresser’s yesterday.', ['had my hair cut', 'cut my hair', 'had cut my hair'], 'had my hair cut',
     'Le coiffeur coupe → have + objet + participe : had my hair cut.'),
    ('We need to ______ before winter.', ['get the roof repaired', 'repair the roof get', 'get repaired the roof'], 'get the roof repaired',
     'Get + objet + participe : get the roof repaired.'),
    ('He ______ in the metro last week.', ['had his phone stolen', 'stole his phone', 'had stolen his phone'], 'had his phone stolen',
     'Mésaventure subie → had his phone stolen.'),
    ('The boss ______ the report twice.', ['made us redo', 'made us to redo', 'got us redo'], 'made us redo',
     'Make + personne + base verbale sans to.'),
    ('I finally ______ to sign the form.', ['got my landlord', 'made my landlord', 'had my landlord'], 'got my landlord',
     'Persuader → get + personne + to : got my landlord to sign.'),
    ('They’re ______ next month.', ['having their house painted', 'painting their house painted', 'having painted their house'], 'having their house painted',
     'En cours d’organisation → are having + objet + participe.'),
  ]),
  ex2=('Complète la structure causative', 'Écris le mot manquant.', [
    ('I must have my eyes ______ . (test → participe)', 'tested',
     'Have + objet + participe : have my eyes tested (me faire contrôler la vue).'),
    ('She got her dress ______ for the wedding. (make → participe)', 'made',
     'Get + objet + participe : got her dress made.'),
    ('We had the documents ______ to the office. (send → participe)', 'sent',
     'Had the documents sent : nous les avons fait envoyer.'),
    ('My parents made me ______ the piano for years. (practise, sans to !)', 'practise',
     'Make + personne + base verbale : made me practise.'),
    ('Can you get him ______ call me back? (le petit mot)', 'to',
     'Get + personne + to + base : get him to call me back.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Je fais réparer ma voiture. »', ["I'm having my car repaired.", "I'm repairing my car.", 'I had repaired my car.'], "I'm having my car repaired.",
     'Faire faire → have + objet + participe, ici au présent continu.'),
    ('« Il s’est fait voler son vélo. »', ['He had his bike stolen.', 'He stole his bike.', 'His bike stole him.'], 'He had his bike stolen.',
     'Subir → had his bike stolen.'),
    ('« Elle nous a fait attendre une heure. »', ['She made us wait for an hour.', 'She made us to wait for an hour.', 'She got us wait for an hour.'], 'She made us wait for an hour.',
     'Obliger → make + base verbale sans to.'),
    ('« Je l’ai convaincu de venir. »', ['I got him to come.', 'I made him to come.', 'I had him came.'], 'I got him to come.',
     'Persuader → get + personne + to come.'),
    ('« Nous faisons refaire la cuisine. »', ["We're having the kitchen redone.", "We're redoing the kitchen ourselves.", 'We had redone the kitchen.'], "We're having the kitchen redone.",
     'Faire refaire → are having + the kitchen + redone.'),
  ]),
  game_desc='Chaque structure causative passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('have-done', 'have something done', 'faire faire quelque chose par quelqu’un', 'faire faire', 'I <b>had my car repaired</b>.', 'I had my car ______ . (réparée — par le garagiste)', 'repaired'),
    ('hair-cut', 'have one’s hair cut', 'se faire couper les cheveux', 'chez le coiffeur', 'She <b>had her hair cut</b>.', 'She had her hair ______ .', 'cut'),
    ('get-fixed', 'get something fixed', 'faire réparer — version orale avec get', 'avec get', 'I need to <b>get my phone fixed</b>.', 'I need to get my phone ______ .', 'fixed'),
    ('wallet-stolen', 'have something stolen', 'se faire voler — la mésaventure subie', 'subir', 'He <b>had his wallet stolen</b>.', 'He had his wallet ______ . (volé)', 'stolen'),
    ('make-do', 'make someone do', 'obliger quelqu’un à faire — sans to', 'obliger', 'The teacher <b>made us rewrite</b> it.', 'The teacher made us ______ it. (réécrire)', 'rewrite'),
    ('get-to-do', 'get someone to do', 'persuader quelqu’un de faire — avec to', 'persuader', 'I <b>got him to help</b> me.', 'I got him ______ help me.', 'to'),
    ('having-redone', 'be having something done', 'faire faire (en cours)', 'en cours', "We're <b>having the kitchen redone</b>.", "We're having the kitchen ______ . (refaite)", 'redone'),
    ('will-have-sent', 'will have something done', 'je ferai envoyer — au futur', 'au futur', "I'll <b>have the documents sent</b> to you.", "I'll have the documents ______ to you. (envoyés)", 'sent'),
  ],
),

'comparisons': dict(
  level='b2', section='grammaire', num='Ch. 3', short='Comparisons',
  title='Comparisons — Nuancer la comparaison',
  subtitle='The more..., the more · twice as... as · by far',
  slides=[
    ('Plus..., plus... : the + comparatif', None,
     '<p class="slide-explanation">« Plus..., plus... » se construit avec <b>the + comparatif</b> des deux côtés — une structure que les francophones n’osent jamais.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The more you practise, the better you get.</b> (Plus tu t’entraînes, meilleur tu deviens.)</p>'
     '<p style="margin-top:8px"><b>The older I get, the less I worry.</b></p></div>'),
    ('De plus en plus : comparatif doublé', None,
     '<p class="slide-explanation">« De plus en plus » = <b>comparatif and comparatif</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>It’s getting colder and colder.</b> (Il fait de plus en plus froid.)</p>'
     '<p style="margin-top:8px"><b>more and more expensive</b> (de plus en plus cher)</p></div>'),
    ('Deux fois plus... : twice as... as', None,
     '<p class="slide-explanation">Les multiples passent par as... as : <b>twice as big as</b>, <b>three times as fast as</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>This flat is twice as expensive as ours.</b> (deux fois plus cher que le nôtre)</p>'
     '<p style="margin-top:8px"><b>half as big as</b> (deux fois plus petit)</p></div>'),
    ('Doser l’écart', None,
     '<p class="slide-explanation">far / much / a lot + comparatif (bien plus) · slightly / a bit (un peu) · by far + superlatif (de loin).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The train is far quicker than the bus.</b></p>'
     '<p style="margin-top:8px"><b>She’s by far the best player in the team.</b> (de loin la meilleure)</p></div>'),
    ('Like ou as ?', None,
     '<p class="slide-explanation"><b>Like + nom</b> = comme (ressemblance). <b>As + fonction</b> = en tant que. Le français dit « comme » pour les deux !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>She sings like an angel.</b> (comme un ange — ressemblance)</p>'
     '<p style="margin-top:8px"><b>She works as a nurse.</b> (en tant qu’infirmière — c’est son métier)</p></div>'),
  ],
  traps=[
    ('Plus tu attends, plus c’est dur → More you wait, more it’s hard.', '<strong>The longer</strong> you wait, <strong>the harder</strong> it gets.', 'La structure exige the + comparatif des deux côtés.'),
    ('It’s more and more cold.', "It's <strong>colder and colder</strong>.", 'Adjectif court → on double le comparatif en -er, pas more.'),
    ('two times more expensive', '<strong>twice as expensive as</strong>', '« Deux fois plus » = twice as... as.'),
    ('She works like a nurse. (c’est son métier)', 'She works <strong>as</strong> a nurse.', 'Métier/fonction → as. Like dirait qu’elle ressemble à une infirmière !'),
    ('She’s the better player of the team.', "She's the <strong>best</strong> player <strong>in</strong> the team.", 'Superlatif (best) + in pour le groupe.'),
  ],
  summary=[
    ('Plus..., plus...', 'the + comp., the + comp.', 'The more you practise, the better...'),
    ('De plus en plus', 'comp. and comp.', 'colder and colder'),
    ('Deux fois plus', 'twice as ... as', 'twice as expensive as'),
    ('Bien plus', 'far / much + comparatif', 'far quicker than'),
    ('De loin le...', 'by far the + superlatif', 'by far the best'),
    ('Comme', 'like (ressemblance) / as (fonction)', 'like an angel · as a nurse'),
  ],
  ex1=('Choisis la structure correcte', 'Nuances de comparaison.', [
    ('______ you start, the sooner you’ll finish.', ['The earlier', 'Earlier', 'More early'], 'The earlier',
     'Plus..., plus... → the + comparatif : The earlier you start...'),
    ('Housing is getting ______ expensive.', ['more and more', 'most and most', 'much and much'], 'more and more',
     'Adjectif long → more and more expensive.'),
    ('Their house is ______ as ours.', ['twice as big', 'two times bigger', 'twice bigger'], 'twice as big',
     'Multiple → twice as big as.'),
    ('This route is ______ faster than the motorway.', ['much', 'very', 'more'], 'much',
     'Doser un grand écart → much/far faster. « Very faster » n’existe pas.'),
    ('He’s ______ the most talented student in the class.', ['by far', 'far by', 'so far'], 'by far',
     '« De loin » + superlatif → by far the most talented.'),
    ('She works ______ a translator for the EU.', ['as', 'like', 'so'], 'as',
     'Fonction réelle → as a translator.'),
  ]),
  ex2=('Complète la comparaison', 'Écris le mot manquant.', [
    ('The more I read, ______ more I understand. (plus... plus)', 'the',
     'The more..., THE more... — le deuxième the est obligatoire.'),
    ('It’s getting harder ______ harder to find a flat. (de plus en plus)', 'and',
     'Comparatif doublé : harder and harder.'),
    ('My commute is twice ______ long as yours. (deux fois plus)', 'as',
     'Twice AS long AS : le multiple s’appuie sur as... as.'),
    ('He sings ______ his father — same voice! (comme, ressemblance)', 'like',
     'Ressemblance → like his father.'),
    ('This is ______ far the best pizza in town. (de loin)', 'by',
     'By far + superlatif.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Plus on attend, pire c’est. »', ['The longer we wait, the worse it gets.', 'More we wait, worse it is.', 'The more we wait, the worst it gets.'], 'The longer we wait, the worse it gets.',
     'The + comparatif des deux côtés ; pire = worse (pas worst).'),
    ('« Il fait de plus en plus chaud. »', ["It's getting hotter and hotter.", "It's getting more and more hot.", "It's hotting more."], "It's getting hotter and hotter.",
     'Adjectif court doublé : hotter and hotter.'),
    ('« Ce vol est deux fois plus cher que le train. »', ['This flight is twice as expensive as the train.', 'This flight is two times more expensive that the train.', 'This flight is twice expensiver than the train.'], 'This flight is twice as expensive as the train.',
     'Twice as... as.'),
    ('« Elle travaille comme journaliste. » (métier)', ['She works as a journalist.', 'She works like a journalist.', 'She works such a journalist.'], 'She works as a journalist.',
     'Fonction → as. Like = ressemblance seulement.'),
    ('« C’est de loin le meilleur restaurant de la ville. »', ["It's by far the best restaurant in town.", "It's far away the best restaurant of town.", "It's the by far better restaurant in town."], "It's by far the best restaurant in town.",
     'By far the best + in town.'),
  ]),
  game_desc='Chaque structure de comparaison passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('the-more', 'the more..., the more...', 'plus..., plus... — double the obligatoire', 'plus plus', '<b>The more</b> you practise, <b>the better</b> you get.', 'The more you practise, ______ better you get.', 'the'),
    ('er-and-er', 'colder and colder', 'de plus en plus — comparatif doublé', 'de plus en plus', "It's getting <b>colder and colder</b>.", "It's getting colder ______ colder.", 'and'),
    ('twice-as', 'twice as ... as', 'deux fois plus... que', 'multiple', 'This flat is <b>twice as</b> expensive <b>as</b> ours.', 'This flat is twice ______ expensive as ours.', 'as'),
    ('far-quicker', 'far/much + comparatif', 'bien plus rapide', 'grand écart', 'The train is <b>far</b> quicker than the bus.', 'The train is ______ quicker than the bus. (bien)', 'far'),
    ('a-bit', 'a bit + comparatif', 'un peu plus', 'petit écart', "It's <b>a bit</b> cheaper online.", "It's a ______ cheaper online. (un peu)", 'bit'),
    ('by-far', 'by far the + superlatif', 'de loin le meilleur', 'de loin', "She's <b>by far</b> the best player.", "She's ______ far the best player.", 'by'),
    ('like-sim', 'like + nom', 'comme — ressemblance', 'like', 'She sings <b>like</b> an angel.', 'She sings ______ an angel. (comme)', 'like'),
    ('as-role', 'as + fonction', 'en tant que — métier ou rôle', 'as', 'She works <b>as</b> a nurse.', 'She works ______ a nurse. (en tant qu’)', 'as'),
  ],
),

'conditionals': dict(
  level='b2', section='grammaire', num='Ch. 4', short='Conditionals',
  title='Conditionals — Le troisième conditionnel et la révision',
  subtitle='If I had known... : les regrets conditionnels',
  slides=[
    ('La carte complète des conditionnels', None,
     '<p class="slide-explanation">Zero (vérités), first (futur réel), second (irréel présent) — et le nouveau : <b>third conditional</b>, l’irréel du passé.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>If I had known, I would have called you.</b> (Si j’avais su, je t’aurais appelé.)</p></div>'
     '<p style="margin-top:16px">Le calque est parfait : plus-que-parfait → past perfect ; conditionnel passé → would have + participe.</p>'),
    ('Third conditional : formation', None,
     '<p class="slide-explanation"><b>If + past perfect, would have + participe passé.</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>If you had studied, you would have passed.</b></p>'
     '<p style="margin-top:8px"><b>She wouldn’t have missed the train if she had left earlier.</b></p>'
     '<p style="margin-top:8px">Contractions : <b>If I’d known, I’d have called.</b> (’d = had / ’d = would !)</p></div>'),
    ('Could have, might have', None,
     '<p class="slide-explanation">Dans la principale : <b>could have</b> (aurait pu), <b>might have</b> (aurait peut-être).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>If we had left earlier, we could have caught the train.</b></p>'
     '<p style="margin-top:8px"><b>If you had asked, he might have said yes.</b></p></div>'),
    ('Les conditionnels mixtes (aperçu)', None,
     '<p class="slide-explanation">Passé irréel → conséquence présente : <b>if + past perfect, would + base</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>If I had taken that job, I would be in New York now.</b> (Si j’avais pris ce poste, je serais à New York maintenant.)</p></div>'
     '<p style="margin-top:16px">Le chapitre Mixed Conditionals y revient en détail.</p>'),
    ('Récapitulatif des quatre', None,
     '<p class="slide-explanation">Choisir le bon conditionnel = situer la condition dans le temps et le réel.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>0 : <b>If you heat water, it boils.</b> · 1 : <b>If it rains, we’ll stay in.</b></p>'
     '<p style="margin-top:8px">2 : <b>If I had time, I would help.</b> · 3 : <b>If I had known, I would have called.</b></p></div>'),
  ],
  traps=[
    ('If I would have known, I would have called.', 'If I <strong>had known</strong>, I would have called.', 'Jamais would après if — y compris au troisième conditionnel.'),
    ('If you had studied, you would pass. (regret du passé)', 'If you had studied, you would <strong>have passed</strong>.', 'Conséquence passée → would HAVE + participe.'),
    ('If I’d known... : ’d = would ?', "If I'd known : ’d = <strong>had</strong>", 'Après if, ’d = had ; dans la principale, ’d = would. Le participe qui suit aide à trancher.'),
    ('She would have miss the train.', 'She would have <strong>missed</strong> the train.', 'Would have + participe passé : missed.'),
    ('Si j’avais su ! → If I have known!', '<strong>If I had known!</strong> / If only I’d known!', 'Plus-que-parfait → past perfect : had known.'),
  ],
  summary=[
    ('Third conditional', 'if + past perfect, would have + pp', 'If I had known, I would have called.'),
    ('Aurait pu', 'could have + pp', 'we could have caught it'),
    ('Aurait peut-être', 'might have + pp', 'he might have said yes'),
    ('Mixte', 'if + past perfect, would + base', '...I would be in NY now.'),
    ('Rappel', '0/1/2 : voir B1', 'If it rains, we’ll stay in.'),
  ],
  ex1=('Choisis la forme correcte', 'Troisième conditionnel et révision.', [
    ('If you ______ me, I would have helped you.', ['had asked', 'would have asked', 'asked'], 'had asked',
     'Condition passée irréelle → past perfect : had asked.'),
    ('If she had seen the email, she ______ .', ['would have replied', 'would reply', 'replied'], 'would have replied',
     'Conséquence passée → would have + participe.'),
    ('We ______ the match if Leo hadn’t been injured.', ['might have won', 'might win', 'won'], 'might have won',
     'Aurait peut-être gagné → might have won.'),
    ('If I ______ that job, I would be rich now. (mixte)', ['had taken', 'took', 'would take'], 'had taken',
     'Condition passée (had taken) → conséquence présente (would be now).'),
    ('If it rains tomorrow, we ______ the picnic. (premier conditionnel !)', ['will cancel', 'would have cancelled', 'would cancel'], 'will cancel',
     'Situation future réelle → first conditional : will cancel.'),
    ('I wouldn’t have said that if I ______ the truth.', ['had known', 'knew', 'would know'], 'had known',
     'Irréel du passé → had known.'),
  ]),
  ex2=('Complète le troisième conditionnel', 'Écris la forme correcte.', [
    ('If we ______ earlier, we would have caught the train. (leave)', 'had left',
     'If + past perfect : had left.'),
    ('You would ______ passed if you had revised. (l’auxiliaire manquant)', 'have',
     'Would HAVE passed — le have est indispensable.'),
    ('If I’d known, I’d ______ told you. (l’auxiliaire)', 'have',
     'I’d have told = I would have told.'),
    ('If she hadn’t missed the bus, she ______ have been late. (négation : ne serait pas arrivée en retard)', "wouldn't",
     'Wouldn’t have been late : double irréel du passé.'),
    ('If you had asked him, he might ______ said yes. (l’auxiliaire)', 'have',
     'Might have said : il aurait peut-être dit oui.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Si j’avais su, je t’aurais appelé. »', ['If I had known, I would have called you.', 'If I would have known, I called you.', 'If I knew, I would call you.'], 'If I had known, I would have called you.',
     'Plus-que-parfait → had known ; conditionnel passé → would have called.'),
    ('« Si tu étais parti plus tôt, tu aurais eu ton train. »', ['If you had left earlier, you would have caught your train.', 'If you left earlier, you would catch your train.', 'If you had left earlier, you would catch your train.'], 'If you had left earlier, you would have caught your train.',
     'Troisième conditionnel complet : had left + would have caught.'),
    ('« On aurait pu gagner ! »', ['We could have won!', 'We could win!', 'We can have won!'], 'We could have won!',
     'Aurait pu → could have + participe.'),
    ('« Si j’avais pris ce poste, je vivrais à Londres aujourd’hui. »', ['If I had taken that job, I would live in London today.', 'If I took that job, I would have lived in London today.', 'If I had taken that job, I would have lived in London today.'], 'If I had taken that job, I would live in London today.',
     'Mixte : condition passée, conséquence présente → would live now.'),
    ('Dans « If I’d seen her, I’d have said hello », les deux ’d sont :', ['had puis would', 'would puis had', 'les deux had'], 'had puis would',
     'Après if : ’d = had ; dans la principale devant have : ’d = would.'),
  ]),
  game_desc='Chaque conditionnel passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('if-had-known', 'if + had + participe', 'si j’avais su — la condition passée irréelle', 'condition passée', '<b>If I had known</b>, I would have called.', 'If I ______ known, I would have called.', 'had'),
    ('would-have', 'would have + participe', 'j’aurais fait — le conditionnel passé', 'conséquence passée', 'I <b>would have called</b> you.', 'I would ______ called you.', 'have'),
    ('could-have', 'could have + participe', 'aurait pu faire', 'aurait pu', 'We <b>could have caught</b> the train.', 'We could ______ caught the train.', 'have'),
    ('might-have', 'might have + participe', 'aurait peut-être fait', 'aurait peut-être', 'He <b>might have said</b> yes.', 'He might have ______ yes. (dit)', 'said'),
    ('wouldnt-have', "wouldn't have + participe", 'n’aurait pas fait', 'négation', 'She <b>wouldn’t have missed</b> it.', 'She ______ have missed it. (n’aurait pas)', "wouldn't"),
    ('mixed', 'mixte : past perfect + would now', 'condition passée, conséquence présente', 'conditionnel mixte', 'If I had taken that job, I <b>would be</b> in NY now.', 'If I had taken that job, I would ______ in NY now.', 'be'),
    ('d-ambiguous', "'d = had ou would", 'après if : had ; devant have : would', 'décoder ’d', "If I<b>'d</b> known, I<b>'d</b> have called.", "If I'd known : 'd = ______", 'had'),
    ('first-reminder', 'rappel : if + présent, will', 'le futur réel reste au premier conditionnel', 'rappel B1', 'If it rains, we <b>will</b> stay in.', 'If it rains, we ______ stay in.', 'will'),
  ],
),
}
