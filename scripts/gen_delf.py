#!/usr/bin/env python3
"""Generate DELF/DALF exam prep pages under francais/exams/."""

import os, textwrap

ROOT = os.path.join(os.path.dirname(__file__), '..', 'francais', 'exams')

EXAMS = {
    'a1': {
        'code': 'DELF A1', 'label': 'DELF A1', 'type': 'DELF',
        'title_fr': 'DELF A1', 'subtitle': 'Diplôme d\'Études en Langue Française — Niveau A1',
        'institution': 'Ministère de l\'Éducation nationale',
        'reading_time': 30, 'n_questions': 15,
        'level_desc': 'Niveau débutant — Accès',
        'components': [
            ('Compréhension de l\'oral', '3', '15', '20 min'),
            ('Compréhension des écrits', '3', '15', '30 min'),
            ('Production écrite', '2', '—', '30 min'),
            ('Production orale', '2', '—', '~7 min'),
        ],
        'reading_desc': 'La compréhension des écrits évalue votre capacité à comprendre des textes simples : panneaux, affiches, messages courts et petites annonces. Vous avez 30 minutes pour répondre à 15 questions réparties en 3 tâches.',
        'score_note': 'Chaque épreuve est notée sur 25 points (total : 100). Pour obtenir le DELF A1, vous devez obtenir au moins 50/100, avec un minimum de 5/25 dans chacune des 4 épreuves.',
        'tips': [
            'Lisez d\'abord les questions avant de lire le texte.',
            'Les textes sont courts et simples : affiches, panneaux, messages, e-mails.',
            'Pour "on ne sait pas", assurez-vous que l\'information est absente du texte.',
            'Gérez votre temps : 30 minutes pour 3 tâches ≈ 10 minutes par tâche.',
            'Ne laissez aucune réponse vide : les réponses incorrectes ne pénalisent pas.',
        ],
        'tasks': [
            {
                'num': 1, 'q_range': '1–5', 'type': 'vrai/faux/on ne sait pas',
                'instructions': 'Vous allez lire une annonce. Lisez les affirmations (1–5) et indiquez si elles sont <strong>Vraies (V)</strong>, <strong>Fausses (F)</strong> ou si <strong>on ne sait pas (NSP)</strong>.',
                'title': 'École de langues Étoile — Rentrée septembre',
                'text': '''<p>L'école de langues Étoile ouvre ses portes du lundi au vendredi de 9h à 19h. Les samedis, les cours ont lieu de 10h à 13h. Le dimanche, l'école est fermée.</p>
<p>Nous proposons des cours de français, d'anglais et d'espagnol pour adultes et enfants à partir de 8 ans. Les cours sont disponibles le matin, l'après-midi et le soir.</p>
<p>Pour vous inscrire, appelez le 01 23 45 67 89 ou envoyez un e-mail à inscription@etoile-langues.fr. Les inscriptions pour septembre sont ouvertes jusqu'au 31 août.</p>''',
                'questions': [
                    (1, "L'école est ouverte le dimanche.", ['V','F','NSP'], 'F'),
                    (2, "On peut apprendre l'espagnol à l'école Étoile.", ['V','F','NSP'], 'V'),
                    (3, "Les enfants de 6 ans peuvent suivre des cours.", ['V','F','NSP'], 'F'),
                    (4, "Les cours du soir sont disponibles.", ['V','F','NSP'], 'V'),
                    (5, "Le prix des cours est indiqué dans l'annonce.", ['V','F','NSP'], 'NSP'),
                ],
                'q_type': 'vfn',
            },
            {
                'num': 2, 'q_range': '6–10', 'type': 'choix multiple',
                'instructions': 'Lisez ce message et répondez aux questions (6–10) en choisissant la bonne réponse (A, B ou C).',
                'title': 'Message de Marie à son amie Lucie',
                'text': '''<p>Bonjour Lucie,</p>
<p>Je t'écris pour te donner des nouvelles. Je suis arrivée à Paris vendredi dernier. J'habite maintenant dans un petit appartement près de la station de métro Bastille. C'est pratique pour aller travailler !</p>
<p>Mon nouveau bureau est au centre-ville. Je commence à 8h30 le matin et je finis à 17h30. Le trajet dure environ 20 minutes en métro.</p>
<p>Le week-end, j'aime visiter les musées et les marchés. Samedi dernier, je suis allée au marché d'Aligre — il y a des fruits et légumes très frais et des prix raisonnables.</p>
<p>Est-ce que tu peux venir me rendre visite en octobre ? Je serai très contente de te montrer la ville.</p>
<p>À bientôt, Marie</p>''',
                'questions': [
                    (6, 'Marie habite à Paris depuis…', ['A. lundi', 'B. vendredi', 'C. samedi'], 'B'),
                    (7, 'Marie va au travail…', ['A. à pied', 'B. en voiture', 'C. en métro'], 'C'),
                    (8, 'Le trajet pour aller au bureau dure…', ['A. 8 minutes', 'B. 20 minutes', 'C. 30 minutes'], 'B'),
                    (9, 'Le samedi, Marie est allée…', ['A. au musée', 'B. au marché', 'C. au cinéma'], 'B'),
                    (10, 'Marie invite Lucie à Paris…', ['A. en septembre', 'B. en octobre', 'C. en novembre'], 'B'),
                ],
                'q_type': 'mc',
            },
            {
                'num': 3, 'q_range': '11–15', 'type': 'association',
                'instructions': 'Vous allez lire cinq messages courts (A–E). Associez chaque message à la bonne situation (11–15).',
                'messages': [
                    ('A', 'Ouvert tous les jours de 10h à 18h. Entrée gratuite le premier dimanche du mois. Café et boutique au rez-de-chaussée.'),
                    ('B', "Fermé pour travaux jusqu'au 15 septembre. Merci de votre compréhension. Réouverture le 16 septembre à 9h."),
                    ('C', "Réservez votre billet en ligne et bénéficiez de 20% de réduction. Valable jusqu'au 30 juin. Code : ETE2024"),
                    ('D', 'Dernière commande avant 21h. Livraison gratuite à partir de 25 euros. Délai : 30 à 45 minutes.'),
                    ('E', "Accès réservé aux résidents. Merci de présenter votre badge à l'entrée. Interdit aux visiteurs sans autorisation."),
                ],
                'questions': [
                    (11, 'Un musée annonce ses horaires.', 'A'),
                    (12, 'Un magasin est temporairement fermé.', 'B'),
                    (13, 'Un site internet propose une promotion.', 'C'),
                    (14, 'Un restaurant propose la livraison à domicile.', 'D'),
                    (15, 'Un bâtiment est réservé à certaines personnes.', 'E'),
                ],
                'q_type': 'match',
            },
        ],
    },
    'a2': {
        'code': 'DELF A2', 'label': 'DELF A2', 'type': 'DELF',
        'title_fr': 'DELF A2', 'subtitle': 'Diplôme d\'Études en Langue Française — Niveau A2',
        'institution': 'Ministère de l\'Éducation nationale',
        'reading_time': 30, 'n_questions': 25,
        'level_desc': 'Niveau élémentaire — Survie',
        'components': [
            ('Compréhension de l\'oral', '4', '25', '25 min'),
            ('Compréhension des écrits', '4', '25', '30 min'),
            ('Production écrite', '2', '—', '45 min'),
            ('Production orale', '3', '—', '~12 min'),
        ],
        'reading_desc': 'La compréhension des écrits évalue votre capacité à comprendre des textes de la vie quotidienne : articles courts, programmes, lettres simples, petites annonces. Vous avez 30 minutes pour 25 questions en 4 tâches.',
        'score_note': 'Chaque épreuve est notée sur 25 points (total : 100). Pour obtenir le DELF A2 : au moins 50/100 et un minimum de 5/25 par épreuve.',
        'tips': [
            'Repérez d\'abord les mots-clés des questions avant de lire.',
            'Les textes A2 incluent des articles courts, horaires, programmes de cinéma.',
            'Attention aux pièges : une information peut être reformulée dans les options.',
            'Pour les associations : éliminez les réponses impossibles en premier.',
            'Vérifiez vos réponses si vous avez le temps à la fin.',
        ],
        'tasks': [
            {
                'num': 1, 'q_range': '1–6', 'type': 'vrai/faux/on ne sait pas',
                'instructions': 'Vous allez lire un article sur une manifestation culturelle. Indiquez si les affirmations (1–6) sont <strong>Vraies (V)</strong>, <strong>Fausses (F)</strong> ou si <strong>on ne sait pas (NSP)</strong>.',
                'title': 'La Fête de la Musique à Lyon',
                'text': '''<p>Chaque année, le 21 juin, Lyon célèbre la Fête de la Musique. Cette année, plus de 300 concerts sont prévus dans toute la ville, dans les parcs, les places publiques et les bars.</p>
<p>La participation est entièrement gratuite pour les musiciens et le public. Les concerts commencent à 18h et se terminent à minuit. Les styles musicaux proposés sont très variés : jazz, rock, musique classique, électro et musiques du monde.</p>
<p>Des scènes sont installées dans les 9 arrondissements de Lyon. La plus grande scène se trouvera place Bellecour, avec des groupes régionaux et des artistes nationaux. Environ 200 000 spectateurs sont attendus dans l'ensemble de la ville.</p>''',
                'questions': [
                    (1, 'La Fête de la Musique a lieu chaque été.', ['V','F','NSP'], 'V'),
                    (2, 'Les musiciens doivent payer pour participer.', ['V','F','NSP'], 'F'),
                    (3, 'Les concerts durent jusqu\'à minuit.', ['V','F','NSP'], 'V'),
                    (4, 'Tous les concerts ont lieu à Bellecour.', ['V','F','NSP'], 'F'),
                    (5, 'Le prix des billets est de 10 euros.', ['V','F','NSP'], 'NSP'),
                    (6, 'Des artistes nationaux se produiront à la grande scène.', ['V','F','NSP'], 'V'),
                ],
                'q_type': 'vfn',
            },
            {
                'num': 2, 'q_range': '7–13', 'type': 'choix multiple',
                'instructions': 'Lisez cet article sur les habitudes alimentaires des Français et répondez aux questions (7–13).',
                'title': 'Les Français et le petit-déjeuner',
                'text': '''<p>En France, le petit-déjeuner est souvent considéré comme le repas le plus important de la journée. Pourtant, les habitudes varient beaucoup selon les générations et les régions.</p>
<p>Chez les adultes, le café est la boisson préférée du matin : 65% des Français commencent leur journée avec une tasse de café. Les croissants et les tartines de pain avec du beurre et de la confiture restent très populaires.</p>
<p>Chez les enfants, le bol de céréales avec du lait domine, suivi du chocolat chaud. De nombreux parents optent également pour des fruits frais ou des yaourts pour un petit-déjeuner plus équilibré.</p>
<p>Selon une étude récente, 15% des Français sautent le petit-déjeuner, principalement par manque de temps. Les nutritionnistes recommandent pourtant de ne pas négliger ce repas pour maintenir l\'énergie tout au long de la matinée.</p>''',
                'questions': [
                    (7, 'Quelle est la boisson préférée des adultes français le matin ?', ['A. Le thé', 'B. Le café', 'C. Le jus d\'orange'], 'B'),
                    (8, 'Quel pourcentage de Français commencent avec du café ?', ['A. 15%', 'B. 50%', 'C. 65%'], 'C'),
                    (9, 'Que mangent souvent les enfants au petit-déjeuner ?', ['A. Des croissants', 'B. Des céréales avec du lait', 'C. Des tartines'], 'B'),
                    (10, 'Pourquoi certains Français sautent-ils le petit-déjeuner ?', ['A. Ils n\'ont pas faim', 'B. Ils n\'ont pas d\'argent', 'C. Ils manquent de temps'], 'C'),
                    (11, 'Quel pourcentage de Français ne prennent pas le petit-déjeuner ?', ['A. 5%', 'B. 15%', 'C. 25%'], 'B'),
                    (12, 'Qui conseille de ne pas négliger le petit-déjeuner ?', ['A. Les pharmaciens', 'B. Les nutritionnistes', 'C. Les médecins'], 'B'),
                    (13, 'Le petit-déjeuner sert à maintenir l\'énergie…', ['A. pendant la nuit', 'B. pendant la matinée', 'C. pendant l\'après-midi'], 'B'),
                ],
                'q_type': 'mc',
            },
            {
                'num': 3, 'q_range': '14–19', 'type': 'association',
                'instructions': 'Vous allez lire six annonces (A–F). Associez chaque personne (14–19) à l\'annonce qui lui correspond.',
                'messages': [
                    ('A', 'Cours de natation pour adultes, tous niveaux. Mardi et jeudi 19h-20h. Piscine municipale. 40€/mois.'),
                    ('B', 'Colocation cherche 3e colocataire. Appartement 3 pièces, centre-ville. Loyer 450€ charges comprises. Non-fumeur.'),
                    ('C', 'Donne cours de guitare à domicile. 20 ans d\'expérience. Enfants et adultes. Premier cours gratuit.'),
                    ('D', 'Cherche baby-sitter pour deux enfants (4 et 7 ans). Mercredi après-midi et vendredi soir. Expérience exigée.'),
                    ('E', 'Vends vélo de ville quasi neuf. 3 vitesses, panier avant. 150€ à débattre. À retirer sur place.'),
                    ('F', 'Restaurant cherche serveur/serveuse. Expérience souhaitée. Mi-temps ou temps plein. CDI. Se présenter au restaurant.'),
                ],
                'questions': [
                    (14, 'Lola veut apprendre à jouer de la musique.', 'C'),
                    (15, 'Thomas cherche un logement pas trop cher.', 'B'),
                    (16, 'Mme Dupont a besoin de quelqu\'un pour ses enfants.', 'D'),
                    (17, 'Paul cherche un moyen de transport économique.', 'E'),
                    (18, 'Sara veut faire du sport le soir.', 'A'),
                    (19, 'Hugo cherche un emploi dans la restauration.', 'F'),
                ],
                'q_type': 'match',
            },
            {
                'num': 4, 'q_range': '20–25', 'type': 'choix multiple',
                'instructions': 'Lisez ce programme de cinéma et répondez aux questions (20–25).',
                'title': 'Programme du Cinéma Le Lumière — semaine du 10 au 16 juillet',
                'text': '''<p><strong>Film 1 : "L'Été indien"</strong> — Comédie romantique (1h45) — Séances : lun, mer, ven à 14h30 et 20h. Sam–dim à 11h, 14h30 et 20h. Tarif plein : 11€. Tarif réduit (–26 ans, +60 ans) : 8€.</p>
<p><strong>Film 2 : "Les Enfants du vent"</strong> — Animation (1h20) — Séances : mer et sam à 10h30 et 14h. Tout public. 9€. Gratuit pour les –6 ans.</p>
<p><strong>Film 3 : "Nuit blanche"</strong> — Thriller (2h10) — Séances : mar, jeu à 21h. Ven à 21h30. Déconseillé aux –12 ans. 11€.</p>
<p>Abonnement mensuel 5 films : 40€. Réservation en ligne : www.lelumiere.fr — 10% de réduction supplémentaire.</p>''',
                'questions': [
                    (20, 'Combien coûte "L\'Été indien" pour un étudiant de 20 ans ?', ['A. 8€', 'B. 9€', 'C. 11€'], 'A'),
                    (21, 'Quand peut-on voir le film d\'animation le matin ?', ['A. Lundi', 'B. Mercredi', 'C. Vendredi'], 'B'),
                    (22, 'Un enfant de 5 ans peut voir "Les Enfants du vent"…', ['A. gratuitement', 'B. à tarif réduit', 'C. au tarif plein'], 'A'),
                    (23, '"Nuit blanche" est déconseillé à…', ['A. toute personne de moins de 6 ans', 'B. toute personne de moins de 12 ans', 'C. toute personne de moins de 18 ans'], 'B'),
                    (24, 'Quelle réduction offre la réservation en ligne ?', ['A. 5%', 'B. 10%', 'C. 15%'], 'B'),
                    (25, 'L\'abonnement mensuel donne accès à…', ['A. 3 films', 'B. 5 films', 'C. 10 films'], 'B'),
                ],
                'q_type': 'mc',
            },
        ],
    },
    'b1': {
        'code': 'DELF B1', 'label': 'DELF B1', 'type': 'DELF',
        'title_fr': 'DELF B1', 'subtitle': 'Diplôme d\'Études en Langue Française — Niveau B1',
        'institution': 'Ministère de l\'Éducation nationale',
        'reading_time': 35, 'n_questions': 25,
        'level_desc': 'Niveau intermédiaire — Seuil',
        'components': [
            ('Compréhension de l\'oral', '3', '25', '25 min'),
            ('Compréhension des écrits', '3', '25', '35 min'),
            ('Production écrite', '2', '—', '45 min'),
            ('Production orale', '3', '—', '~15 min'),
        ],
        'reading_desc': 'La compréhension des écrits B1 évalue la lecture de textes authentiques de la vie quotidienne et sociale : articles de presse, courriers, brochures. 35 minutes pour 25 questions en 3 tâches.',
        'score_note': 'Chaque épreuve est notée sur 25 points (total : 100). Pour obtenir le DELF B1 : au moins 50/100 et un minimum de 5/25 par épreuve.',
        'tips': [
            'Lisez le titre et les questions avant le texte pour anticiper le contenu.',
            'À B1, les textes sont plus longs et peuvent contenir du vocabulaire inconnu — utilisez le contexte.',
            'Reformulation : la bonne réponse paraphrase souvent le texte, elle ne le copie pas.',
            'Pour les V/F/NSP : "on ne sait pas" signifie que l\'information n\'est ni confirmée ni infirmée.',
            'Gérez votre temps : environ 10–12 minutes par tâche.',
        ],
        'tasks': [
            {
                'num': 1, 'q_range': '1–8', 'type': 'vrai/faux/on ne sait pas',
                'instructions': 'Lisez cet article de magazine. Indiquez si les affirmations (1–8) sont <strong>Vraies (V)</strong>, <strong>Fausses (F)</strong> ou si <strong>on ne sait pas (NSP)</strong>.',
                'title': 'Le covoiturage en France : une pratique en plein essor',
                'text': '''<p>Le covoiturage connaît une croissance spectaculaire en France depuis quelques années. En 2023, plus de 4 millions de trajets ont été effectués chaque mois via les différentes plateformes numériques, contre 1,5 million en 2019.</p>
<p>Ce mode de transport séduit particulièrement les jeunes actifs et les étudiants, qui y voient une façon de réduire leurs dépenses de transport tout en rencontrant de nouvelles personnes. « Je fais le trajet Paris–Lyon deux fois par mois et j'économise environ 60 euros à chaque fois », témoigne Camille, 24 ans.</p>
<p>Les avantages environnementaux sont également mis en avant par les défenseurs du covoiturage. Selon une étude de l'ADEME publiée en 2022, le covoiturage régulier permettrait de réduire les émissions de CO2 d'un trajet de 30 à 40%.</p>
<p>Cependant, le développement du covoiturage n'est pas sans difficultés. La question de la sécurité des passagers reste un sujet sensible, même si les incidents sont rares. Par ailleurs, en milieu rural, l'offre reste encore insuffisante pour répondre à la demande croissante.</p>
<p>Le gouvernement français a annoncé un plan de soutien au covoiturage, avec notamment une aide financière pour les nouveaux utilisateurs et des subventions pour les plateformes qui développent des services en zone rurale.</p>''',
                'questions': [
                    (1, 'Le nombre de trajets en covoiturage a plus que doublé entre 2019 et 2023.', ['V','F','NSP'], 'V'),
                    (2, 'Le covoiturage est surtout utilisé par les personnes âgées.', ['V','F','NSP'], 'F'),
                    (3, 'Camille utilise le covoiturage pour aller travailler tous les jours.', ['V','F','NSP'], 'F'),
                    (4, 'Le covoiturage peut réduire les émissions de CO2 d\'un trajet.', ['V','F','NSP'], 'V'),
                    (5, 'L\'étude de l\'ADEME a été publiée en 2022.', ['V','F','NSP'], 'V'),
                    (6, 'Les accidents liés au covoiturage sont très fréquents.', ['V','F','NSP'], 'F'),
                    (7, 'L\'offre de covoiturage est suffisante dans les campagnes.', ['V','F','NSP'], 'F'),
                    (8, 'Le gouvernement prévoit de taxer les plateformes de covoiturage.', ['V','F','NSP'], 'NSP'),
                ],
                'q_type': 'vfn',
            },
            {
                'num': 2, 'q_range': '9–17', 'type': 'choix multiple',
                'instructions': 'Lisez cet article et répondez aux questions (9–17) en choisissant la bonne réponse (A, B ou C).',
                'title': 'Le jardinage urbain : quand la ville se met au vert',
                'text': '''<p>Paris, Lyon, Bordeaux : de plus en plus de grandes villes françaises encouragent leurs habitants à cultiver des espaces verts dans le tissu urbain. Potagers sur les toits, jardins partagés dans les cours d'immeuble, bacs à fleurs sur les trottoirs — le jardinage urbain s'impose comme une tendance forte des années 2020.</p>
<p>La Ville de Paris a lancé en 2016 le programme « Parisculteurs », qui a permis de végétaliser plus de 100 hectares de surfaces jusqu'alors inexploitées. Les participants — particuliers, associations, entreprises — peuvent soumettre un projet et recevoir un accompagnement technique et, dans certains cas, un soutien financier.</p>
<p>Au-delà du plaisir de produire ses propres légumes, le jardinage urbain répond à des enjeux multiples. Sur le plan écologique, il contribue à la lutte contre les îlots de chaleur en ville, améliore la biodiversité et réduit le ruissellement des eaux de pluie. Sur le plan social, il favorise la création de liens entre voisins et peut contribuer à réduire les inégalités alimentaires dans certains quartiers défavorisés.</p>
<p>Mais le jardinage urbain a aussi ses limites. La qualité des sols en milieu urbain peut être problématique en raison de la pollution. Il est donc conseillé de faire analyser la terre avant de planter des légumes destinés à la consommation. De plus, la gestion des espaces partagés nécessite une organisation rigoureuse pour éviter les conflits entre utilisateurs.</p>''',
                'questions': [
                    (9, 'Quand le programme « Parisculteurs » a-t-il été lancé ?', ['A. En 2016', 'B. En 2020', 'C. En 2023'], 'A'),
                    (10, 'Combien d\'hectares le programme a-t-il végétalisés ?', ['A. Plus de 10 hectares', 'B. Plus de 100 hectares', 'C. Plus de 1 000 hectares'], 'B'),
                    (11, 'Qui peut participer au programme Parisculteurs ?', ['A. Seulement les entreprises', 'B. Seulement les associations', 'C. Les particuliers, associations et entreprises'], 'C'),
                    (12, 'Comment le jardinage urbain aide-t-il l\'environnement ?', ['A. En augmentant la pollution', 'B. En luttant contre les îlots de chaleur', 'C. En réduisant la consommation d\'eau'], 'B'),
                    (13, 'Quel avantage social le texte mentionne-t-il ?', ['A. Créer des emplois', 'B. Favoriser les liens entre voisins', 'C. Réduire les loyers'], 'B'),
                    (14, 'Quel risque est mentionné concernant les sols urbains ?', ['A. La sécheresse', 'B. La pollution', 'C. La pauvreté en nutriments'], 'B'),
                    (15, 'Que conseille-t-on de faire avant de planter des légumes ?', ['A. Acheter de la terre neuve', 'B. Analyser la qualité du sol', 'C. Demander une autorisation'], 'B'),
                    (16, 'Quelle difficulté concerne les espaces partagés ?', ['A. Le manque d\'eau', 'B. Le manque de lumière', 'C. Les conflits entre utilisateurs'], 'C'),
                    (17, 'Quel est le sujet principal de l\'article ?', ['A. Les problèmes environnementaux en ville', 'B. Le développement du jardinage en milieu urbain', 'C. Les politiques agricoles françaises'], 'B'),
                ],
                'q_type': 'mc',
            },
            {
                'num': 3, 'q_range': '18–25', 'type': 'association',
                'instructions': 'Vous allez lire huit avis de lecteurs (A–H) sur le même sujet. Associez chaque affirmation (18–25) à l\'auteur correspondant.',
                'messages': [
                    ('A', 'Je lis surtout des romans policiers. J\'apprécie les histoires à suspense où l\'on cherche à identifier le coupable jusqu\'à la dernière page.'),
                    ('B', 'La lecture m\'a sauvé pendant mes longues hospitalisations. Les livres m\'ont permis de voyager sans quitter ma chambre.'),
                    ('C', 'Je suis contre les liseuses électroniques. Le papier, l\'odeur du livre, le plaisir de tourner les pages — rien ne peut remplacer ça.'),
                    ('D', 'Je lis principalement des essais politiques et économiques. Je pense que la fiction est une perte de temps pour les adultes.'),
                    ('E', 'Je n\'ai jamais aimé lire, jusqu\'au jour où j\'ai découvert les mangas. Aujourd\'hui, je lis plus de 20 albums par mois.'),
                    ('F', 'La bibliothèque municipale a changé ma vie. Enfant pauvre, c\'était le seul endroit où j\'avais accès aux livres gratuitement.'),
                    ('G', 'Je préfère écouter les livres audio en conduisant. C\'est une façon de profiter des histoires sans avoir à s\'arrêter.'),
                    ('H', 'J\'organise un club de lecture avec des amies depuis dix ans. C\'est une occasion de se retrouver et de partager nos impressions.'),
                ],
                'questions': [
                    (18, 'Cette personne a découvert la lecture grâce à un format spécifique.', 'E'),
                    (19, 'Cette personne utilise la lecture pour se distraire en voyageant.', 'G'),
                    (20, 'Cette personne apprécie le livre comme objet physique.', 'C'),
                    (21, 'Cette personne a bénéficié d\'un service public pour accéder aux livres.', 'F'),
                    (22, 'Cette personne aime les intrigues et les enquêtes.', 'A'),
                    (23, 'La lecture a aidé cette personne pendant une période difficile.', 'B'),
                    (24, 'Cette personne préfère les textes non fictionnels.', 'D'),
                    (25, 'La lecture est pour cette personne une activité sociale.', 'H'),
                ],
                'q_type': 'match',
            },
        ],
    },
    'b2': {
        'code': 'DELF B2', 'label': 'DELF B2', 'type': 'DELF',
        'title_fr': 'DELF B2', 'subtitle': 'Diplôme d\'Études en Langue Française — Niveau B2',
        'institution': 'Ministère de l\'Éducation nationale',
        'reading_time': 60, 'n_questions': 28,
        'level_desc': 'Niveau avancé — Avancé',
        'components': [
            ('Compréhension de l\'oral', '2', '25', '30 min'),
            ('Compréhension des écrits', '3', '25', '60 min'),
            ('Production écrite', '1', '—', '60 min'),
            ('Production orale', '3', '—', '~20 min'),
        ],
        'reading_desc': 'La compréhension des écrits B2 exige de lire des textes authentiques complexes : articles de presse, textes littéraires, documents officiels. 60 minutes pour 28 questions en 3 tâches.',
        'score_note': 'Chaque épreuve est notée sur 25 points (total : 100). Pour obtenir le DELF B2 : au moins 50/100 et un minimum de 5/25 par épreuve.',
        'tips': [
            'Lisez les textes attentivement — les pièges sont souvent dans les nuances.',
            'À B2, les reformulations peuvent être très éloignées du texte original.',
            'Identifiez le type de texte (argumentatif, informatif, littéraire) pour adapter votre lecture.',
            'Ne restez pas bloqué — passez à la question suivante et revenez si vous avez le temps.',
            'Pour la tâche d\'association, lisez d\'abord toutes les opinions, puis les affirmations.',
        ],
        'tasks': [
            {
                'num': 1, 'q_range': '1–10', 'type': 'choix multiple',
                'instructions': 'Lisez cet article et répondez aux questions (1–10) en choisissant la bonne réponse (A, B ou C).',
                'title': 'L\'intelligence artificielle dans l\'enseignement : promesses et inquiétudes',
                'text': '''<p>L'intégration de l'intelligence artificielle dans les systèmes éducatifs soulève des questions qui dépassent largement le cadre technologique. Si les partisans de ces nouveaux outils mettent en avant leurs capacités à personnaliser les apprentissages et à alléger la charge administrative des enseignants, leurs détracteurs soulignent des risques bien réels pour l'autonomie intellectuelle des élèves et pour l'emploi dans le secteur éducatif.</p>
<p>Des expériences pilotes menées dans plusieurs lycées français depuis 2022 ont montré des résultats contrastés. D'un côté, des élèves en difficulté ont bénéficié d'un soutien individualisé grâce à des systèmes d'IA capables d'adapter les exercices à leur niveau et à leur rythme d'apprentissage. De l'autre, certains enseignants ont constaté une dépendance croissante des élèves à ces outils, au détriment du développement de leur capacité de réflexion autonome.</p>
<p>La question de l'évaluation est particulièrement sensible. Les outils d'IA générative permettent désormais de produire en quelques secondes des dissertations ou des résumés de qualité honorable. Face à ce défi, certains établissements ont choisi d'interdire purement et simplement l'usage de ces outils, tandis que d'autres ont préféré intégrer leur utilisation dans les pratiques pédagogiques tout en révisant les modalités d'évaluation.</p>
<p>Pour Michel Lambert, chercheur en sciences de l'éducation, la dichotomie « pour ou contre l'IA » est un faux débat : « La vraie question est de savoir comment former les enseignants à utiliser ces outils de façon critique et créative, et comment remettre les compétences de pensée complexe au cœur des apprentissages. »</p>''',
                'questions': [
                    (1, 'Selon le texte, les partisans de l\'IA dans l\'éducation soulignent…', ['A. les risques pour l\'emploi des enseignants', 'B. la personnalisation des apprentissages', 'C. la dépendance des élèves aux outils'], 'B'),
                    (2, 'Les expériences pilotes ont commencé…', ['A. en 2019', 'B. en 2022', 'C. en 2024'], 'B'),
                    (3, 'Quel problème certains enseignants ont-ils observé ?', ['A. Les élèves refusent d\'utiliser l\'IA', 'B. L\'IA n\'adapte pas les exercices', 'C. Les élèves deviennent trop dépendants des outils'], 'C'),
                    (4, 'Pourquoi l\'évaluation est-elle particulièrement sensible ?', ['A. Les élèves ne veulent plus être évalués', 'B. L\'IA peut produire des rédactions de qualité', 'C. Les enseignants manquent de temps pour corriger'], 'B'),
                    (5, 'Comment certains établissements ont-ils réagi face à l\'IA générative ?', ['A. En l\'imposant à tous les élèves', 'B. En ignorant le problème', 'C. En l\'interdisant ou en l\'intégrant différemment'], 'C'),
                    (6, 'Selon Michel Lambert, quel est le vrai défi ?', ['A. Interdire l\'IA dans les écoles', 'B. Former les enseignants à utiliser l\'IA de façon critique', 'C. Développer une meilleure IA pour l\'éducation'], 'B'),
                    (7, 'Lambert qualifie le débat « pour ou contre l\'IA » de…', ['A. stimulant intellectuellement', 'B. inévitable', 'C. faux débat'], 'C'),
                    (8, 'Quelle compétence Lambert veut-il remettre au cœur des apprentissages ?', ['A. La mémorisation', 'B. La pensée complexe', 'C. La vitesse de lecture'], 'B'),
                    (9, 'Quel ton adopte cet article ?', ['A. Entièrement favorable à l\'IA', 'B. Entièrement opposé à l\'IA', 'C. Nuancé, présentant des arguments des deux côtés'], 'C'),
                    (10, 'Qu\'est-ce que l\'IA peut faire pour les élèves en difficulté, selon le texte ?', ['A. Remplacer les enseignants', 'B. Adapter les exercices à leur niveau', 'C. Rédiger leurs devoirs à leur place'], 'B'),
                ],
                'q_type': 'mc',
            },
            {
                'num': 2, 'q_range': '11–18', 'type': 'vrai/faux/on ne sait pas',
                'instructions': 'Lisez ce texte et indiquez si les affirmations (11–18) sont <strong>Vraies (V)</strong>, <strong>Fausses (F)</strong> ou si <strong>on ne sait pas (NSP)</strong>.',
                'title': 'Le retour en grâce du train de nuit en Europe',
                'text': '''<p>Après des décennies de déclin marquées par la concurrence des vols low-cost et la montée des lignes à grande vitesse, le train de nuit connaît un remarquable regain d'intérêt en Europe. En 2022, les compagnies ferroviaires autrichiennes (ÖBB) ont lancé de nouvelles liaisons entre Vienne et plusieurs capitales européennes, avec un succès commercial qui a surpris les observateurs les plus optimistes.</p>
<p>Ce retour s'explique en grande partie par la prise de conscience écologique. Face à l'empreinte carbone de l'avion — un trajet en avion émet environ 50 fois plus de CO2 par passager qu'un trajet en train équivalent — de nombreux voyageurs européens optent désormais pour des alternatives ferroviaires, même lorsqu'elles impliquent des temps de trajet plus longs.</p>
<p>En France, la SNCF a relancé plusieurs lignes de nuit entre 2021 et 2023, notamment Paris–Nice et Paris–Tarbes, après une interruption de plus de dix ans. Les résultats sont encourageants : les trains affichent régulièrement des taux de remplissage supérieurs à 80%, et de nouvelles lignes sont à l'étude, notamment vers l'Espagne et l'Italie.</p>
<p>Mais le train de nuit doit encore relever plusieurs défis pour s'imposer durablement. Le confort des couchettes reste un point sensible : si les compartiments modernes des ÖBB offrent des prestations comparables à un hôtel économique, certaines lignes françaises fonctionnent encore avec un matériel vieillissant. Le prix, enfin, peut constituer un frein : si le train de nuit est souvent moins cher que l'avion pour des réservations anticipées, il reste plus onéreux que le bus longue distance.</p>''',
                'questions': [
                    (11, 'Les trains de nuit ont été en déclin pendant plusieurs décennies.', ['V','F','NSP'], 'V'),
                    (12, 'Les ÖBB sont une compagnie ferroviaire autrichienne.', ['V','F','NSP'], 'V'),
                    (13, 'Le succès des nouvelles liaisons des ÖBB était attendu par tous.', ['V','F','NSP'], 'F'),
                    (14, 'Un avion émet environ 50 fois plus de CO2 qu\'un train par passager.', ['V','F','NSP'], 'V'),
                    (15, 'La SNCF a relancé des trains de nuit vers l\'Espagne.', ['V','F','NSP'], 'NSP'),
                    (16, 'Les trains de nuit français affichent des taux de remplissage supérieurs à 80%.', ['V','F','NSP'], 'V'),
                    (17, 'Le confort des trains de nuit est partout excellent.', ['V','F','NSP'], 'F'),
                    (18, 'Le train de nuit est toujours moins cher que l\'avion.', ['V','F','NSP'], 'F'),
                ],
                'q_type': 'vfn',
            },
            {
                'num': 3, 'q_range': '19–28', 'type': 'association',
                'instructions': 'Vous allez lire dix avis de personnes sur le télétravail (A–J). Associez chaque affirmation (19–28) à l\'auteur correspondant.',
                'messages': [
                    ('A', 'Le télétravail m\'a permis de déménager à la campagne. Je n\'aurais jamais pu me le permettre si j\'avais dû aller au bureau tous les jours.'),
                    ('B', 'Je travaille mieux au bureau. Chez moi, les distractions sont trop nombreuses — les enfants, la cuisine, la télévision. Ma productivité a chuté.'),
                    ('C', 'En tant que manager, je trouve difficile d\'évaluer le travail de mon équipe à distance. Le manque de visibilité sur ce que font les employés me préoccupe.'),
                    ('D', 'Le télétravail a aggravé mes problèmes de dos. Je n\'ai pas de bureau ergonomique chez moi et je travaille sur ma table de cuisine depuis un an.'),
                    ('E', 'Je fais des économies considérables sur les transports et les repas. En calculant, c\'est presque 300 euros de moins par mois.'),
                    ('F', 'Mon entreprise a pu réduire la taille de ses bureaux et économiser sur le loyer. Ces économies ont été partiellement redistribuées aux employés.'),
                    ('G', 'Je souffre de l\'isolement. Le café du matin avec les collègues, les déjeuners en équipe — tout ça me manque terriblement.'),
                    ('H', 'Le télétravail a rendu possible le recrutement de talents dans d\'autres régions, voire d\'autres pays. Notre équipe est maintenant internationale.'),
                    ('I', 'La frontière entre vie professionnelle et vie personnelle a disparu. Je réponds aux e-mails le soir, le week-end. Je n\'arrive plus à décrocher.'),
                    ('J', 'Pour les personnes handicapées, le télétravail est une révolution. Je n\'ai plus les difficultés liées aux transports et aux locaux non adaptés.'),
                ],
                'questions': [
                    (19, 'Cette personne évoque un avantage financier pour l\'employeur.', 'F'),
                    (20, 'Cette personne souffre d\'un problème de santé lié au télétravail.', 'D'),
                    (21, 'Cette personne apprécie le télétravail pour une raison liée au handicap.', 'J'),
                    (22, 'Cette personne a des difficultés à gérer son équipe à distance.', 'C'),
                    (23, 'Cette personne a changé de lieu de résidence grâce au télétravail.', 'A'),
                    (24, 'Cette personne évoque des économies personnelles.', 'E'),
                    (25, 'Cette personne ne peut pas séparer travail et vie privée.', 'I'),
                    (26, 'Cette personne est moins efficace à la maison qu\'au bureau.', 'B'),
                    (27, 'Cette personne souffre du manque de contact humain.', 'G'),
                    (28, 'Le télétravail a permis à cette entreprise de recruter plus largement.', 'H'),
                ],
                'q_type': 'match',
            },
        ],
    },
    'c1': {
        'code': 'DALF C1', 'label': 'DALF C1', 'type': 'DALF',
        'title_fr': 'DALF C1', 'subtitle': 'Diplôme Approfondi de Langue Française — Niveau C1',
        'institution': 'Ministère de l\'Éducation nationale',
        'reading_time': 50, 'n_questions': 20,
        'level_desc': 'Niveau avancé supérieur',
        'components': [
            ('Compréhension de l\'oral', '2', '25', '40 min'),
            ('Compréhension des écrits', '2', '25', '50 min'),
            ('Production écrite (synthèse + essai)', '2', '—', '3h30'),
            ('Production orale', '3', '—', '~30 min'),
        ],
        'reading_desc': 'La compréhension des écrits C1 demande de lire des textes complexes (articles spécialisés, essais) avec finesse : inférences, nuances, intentions implicites. 50 minutes pour 20 questions en 2 tâches.',
        'score_note': 'Chaque épreuve est notée sur 25 points (total : 100). Pour obtenir le DALF C1 : au moins 50/100 et un minimum de 5/25 par épreuve.',
        'tips': [
            'À C1, les textes sont spécialisés et les questions testent la compréhension implicite.',
            'Identifiez le point de vue de l\'auteur : favorable, critique, nuancé, ironique ?',
            'Repérez les connecteurs logiques pour comprendre la structure argumentative.',
            'Ne répondez pas selon vos connaissances du sujet mais selon ce que dit le texte.',
            'Pour les reformulations : cherchez l\'équivalence sémantique, pas lexicale.',
        ],
        'tasks': [
            {
                'num': 1, 'q_range': '1–10', 'type': 'choix multiple',
                'instructions': 'Lisez cet essai et répondez aux questions (1–10) en choisissant la bonne réponse (A, B ou C).',
                'title': 'La mémoire à l\'ère numérique : amnésie choisie ou libération cognitive ?',
                'text': '''<p>L'essor des technologies numériques a profondément transformé notre rapport à la mémoire. Là où nos ancêtres mémorisaient poèmes, calculs et itinéraires, nous délégons désormais ces tâches à nos appareils. Ce phénomène, que le psychologue Betsy Sparrow a nommé « effet Google » en 2011, pose une question fondamentale : sommes-nous en train de nous abêtir, ou au contraire de libérer notre cognition pour des tâches plus complexes ?</p>
<p>Les partisans de la thèse de l'appauvrissement cognitif pointent une évidence : si nous ne mémorisons plus les informations, nous perdons la capacité de les relier entre elles pour former des raisonnements originaux. La mémoire n'est pas un simple disque dur externe ; elle structure la pensée elle-même. Comme l'écrivait Montaigne, « mieux vaut une tête bien faite qu'une tête bien pleine » — mais encore faut-il que cette tête soit faite de quelque chose.</p>
<p>Pourtant, les défenseurs du numérique rétorquent que l'humanité a toujours externalisé sa mémoire : de l'écriture aux bibliothèques, en passant par l'imprimerie. Chaque innovation a été accompagnée de lamentations similaires. Socrate lui-même déplorait que l'écriture affaiblirait la mémoire des hommes — et il n\'avait pas tort. Mais l'écriture a également rendu possible des formes de pensée inédites.</p>
<p>La question est peut-être moins celle de la quantité de mémoire que de sa qualité. Ce qui compte n'est pas de se souvenir de tout, mais de savoir quoi chercher, comment évaluer la fiabilité des sources, et comment articuler des informations issues de contextes différents. Ces compétences méta-cognitives, qui conditionnent l'usage intelligent du numérique, ne sont pas innées — elles s'acquièrent et doivent être enseignées.</p>''',
                'questions': [
                    (1, 'Qu\'est-ce que l\' « effet Google » selon le texte ?', ['A. La tendance à chercher des informations sur Google', 'B. La délégation de la mémoire aux appareils numériques', 'C. La dépendance aux réseaux sociaux'], 'B'),
                    (2, 'Quelle est la question centrale posée par l\'auteur ?', ['A. Le numérique appauvrit-il notre intelligence ?', 'B. Devons-nous interdire les téléphones dans les écoles ?', 'C. Comment mémoriser plus efficacement ?'], 'A'),
                    (3, 'Selon les partisans de la thèse de l\'appauvrissement, la mémoire…', ['A. est inutile à l\'ère numérique', 'B. structure la pensée elle-même', 'C. doit être remplacée par l\'IA'], 'B'),
                    (4, 'La citation de Montaigne est utilisée pour…', ['A. critiquer l\'éducation moderne', 'B. nuancer l\'idée d\'une tête bien faite', 'C. défendre l\'enseignement de la mémoire'], 'B'),
                    (5, 'Quel argument les défenseurs du numérique avancent-ils ?', ['A. Le numérique améliore la mémoire', 'B. L\'humanité a toujours externalisé la mémoire', 'C. Socrate avait tort de critiquer l\'écriture'], 'B'),
                    (6, 'Selon le texte, que craignait Socrate ?', ['A. Que l\'imprimerie détruise la culture', 'B. Que l\'écriture affaiblisse la mémoire', 'C. Que le calcul remplace la réflexion'], 'B'),
                    (7, 'L\'auteur conclut que ce qui importe, c\'est…', ['A. de mémoriser un maximum d\'informations', 'B. d\'utiliser les bons outils numériques', 'C. de savoir chercher, évaluer et articuler des informations'], 'C'),
                    (8, 'Que sont les « compétences méta-cognitives » selon le texte ?', ['A. Des compétences innées', 'B. Des compétences qui s\'acquièrent et doivent être enseignées', 'C. Des compétences liées à l\'usage des moteurs de recherche'], 'B'),
                    (9, 'Quel est le ton général de cet essai ?', ['A. Catastrophiste et alarmiste', 'B. Favorabler à la technologie sans réserves', 'C. Nuancé et dialectique'], 'C'),
                    (10, 'Selon l\'auteur, l\'écriture a…', ['A. affaibli la mémoire sans apporter de bénéfices', 'B. rendu possible des formes de pensée inédites', 'C. été rejetée par Socrate à juste titre'], 'B'),
                ],
                'q_type': 'mc',
            },
            {
                'num': 2, 'q_range': '11–20', 'type': 'association',
                'instructions': 'Vous allez lire dix extraits d\'articles sur la ville de demain (A–J). Associez chaque affirmation (11–20) au texte correspondant.',
                'messages': [
                    ('A', 'La végétalisation des façades n\'est pas qu\'esthétique : elle réduit la température intérieure des bâtiments de 2 à 4 degrés en été, diminuant ainsi la consommation de climatisation.'),
                    ('B', 'Certaines municipalités expérimentent des « zones sans voiture » permanentes dans leurs centres historiques. Les commerçants, d\'abord réticents, constatent généralement une augmentation du chiffre d\'affaires.'),
                    ('C', 'L\'éclairage public représente 37% de la consommation électrique des communes françaises. Le remplacement systématique par des LED connectées permettrait de réduire ce poste de 60%.'),
                    ('D', 'Les capteurs installés dans les poubelles intelligentes signalent en temps réel leur niveau de remplissage, optimisant ainsi les tournées de collecte et réduisant les coûts de 25%.'),
                    ('E', 'La mixité fonctionnelle — habiter, travailler et se détendre dans le même quartier — réduit les déplacements et crée des communautés plus résilientes face aux crises.'),
                    ('F', 'Des chercheurs ont démontré que les espaces verts en milieu urbain réduisent le stress, améliorent la santé mentale et favorisent les interactions sociales entre résidents.'),
                    ('G', 'Les toitures solaires des bâtiments publics pourraient couvrir jusqu\'à 30% des besoins énergétiques d\'une ville de taille moyenne, selon une étude récente.'),
                    ('H', 'L\'agriculture urbaine ne peut pas remplacer l\'agriculture conventionnelle en termes de volume, mais elle joue un rôle crucial dans l\'éducation alimentaire et le renforcement du lien social.'),
                    ('I', 'Les systèmes de gestion du trafic basés sur l\'IA réduisent les embouteillages de 15 à 30% dans les villes qui les ont adoptés, diminuant également les émissions de CO2.'),
                    ('J', 'Le bruit est le deuxième facteur environnemental de maladie en Europe après la pollution de l\'air. L\'isolation phonique des logements reste un défi majeur pour les villes denses.'),
                ],
                'questions': [
                    (11, 'Ce texte parle de l\'impact de la végétation sur l\'énergie utilisée dans les bâtiments.', 'A'),
                    (12, 'Ce texte évoque les bénéfices économiques inattendusd\'une restriction de la circulation.', 'B'),
                    (13, 'Ce texte concerne la gestion des déchets par la technologie.', 'D'),
                    (14, 'Ce texte aborde l\'impact psychologique des espaces naturels en ville.', 'F'),
                    (15, 'Ce texte traite de la production d\'énergie renouvelable en milieu urbain.', 'G'),
                    (16, 'Ce texte présente les limites de l\'agriculture en ville.', 'H'),
                    (17, 'Ce texte porte sur l\'optimisation de la circulation par les nouvelles technologies.', 'I'),
                    (18, 'Ce texte concerne la consommation électrique liée à l\'éclairage public.', 'C'),
                    (19, 'Ce texte aborde un risque sanitaire lié à l\'environnement sonore.', 'J'),
                    (20, 'Ce texte décrit un modèle d\'urbanisme favorisant la proximité des fonctions.', 'E'),
                ],
                'q_type': 'match',
            },
        ],
    },
    'c2': {
        'code': 'DALF C2', 'label': 'DALF C2', 'type': 'DALF',
        'title_fr': 'DALF C2', 'subtitle': 'Diplôme Approfondi de Langue Française — Niveau C2',
        'institution': 'Ministère de l\'Éducation nationale',
        'reading_time': 60, 'n_questions': 20,
        'level_desc': 'Niveau maîtrise',
        'components': [
            ('Compréhension et production de l\'oral', '2', '50', '1h'),
            ('Production écrite (synthèse + dissertation)', '2', '50', '3h30'),
        ],
        'reading_desc': 'Au DALF C2, la compréhension des écrits est intégrée à la production écrite. Ce simulacre couvre la lecture analytique de textes complexes et littéraires : l\'identification des positions, des nuances, des procédés rhétoriques et des sous-entendus. 60 minutes pour 20 questions.',
        'score_note': 'Le DALF C2 est noté sur 100 points en deux groupes : oral (50 pts) et écrit (50 pts). Il faut obtenir au moins 50/100 au total avec un minimum de 25/50 dans chaque groupe.',
        'tips': [
            'À C2, l\'implicite et l\'ironie doivent être identifiés avec précision.',
            'Maîtrisez le vocabulaire de l\'analyse : connotation, euphémisme, antiphrase, métaphore filée.',
            'Distinguez le fait (ce qui est dit) de l\'opinion (comment c\'est dit, avec quel registre).',
            'Repérez les procédés rhétoriques : chiasme, gradation, anaphore, prétérition.',
            'La synthèse au C2 exige une reformulation fidèle et une organisation thématique rigoureuse.',
        ],
        'tasks': [
            {
                'num': 1, 'q_range': '1–10', 'type': 'choix multiple',
                'instructions': 'Lisez cet extrait d\'essai philosophique et répondez aux questions (1–10) en choisissant la bonne réponse (A, B ou C).',
                'title': 'L\'ennui, vertu méconnue',
                'text': '''<p>On a beaucoup écrit sur le bonheur, l'amour et la mort. On a fort peu écrit sur l'ennui, comme si ce sentiment mineur ne méritait pas l'attention des philosophes sérieux. Et pourtant, l'ennui est peut-être la plus philosophique de toutes les émotions, celle qui nous arrache le plus violemment à l'illusion que nos agitations quotidiennes ont un sens.</p>
<p>Pascal, dans ses Pensées, voyait dans la « diversité » — le divertissement, l'agitation perpétuelle — la grande stratégie par laquelle l'homme fuit la conscience de sa misère fondamentale. L'ennui, pour lui, est ce qui reste lorsqu'on a retiré tous les divertissements : une vérité nue et insupportable sur notre condition. Ce n'est pas l'ennui qui est à fuir, mais ce qu'il révèle.</p>
<p>Les romantiques ont réhabilité l'ennui sous le nom de « spleen » ou de « mélancolie ». Pour Baudelaire, l'ennui n'est pas l'absence de désir, mais son excès : trop de désirs impossibles, trop de beauté non réalisée. Cette relecture transfigure l'ennui en disposition poétique, en ouverture au monde qui échappe à la banalité du quotidien.</p>
<p>Aujourd'hui, à l'ère des smartphones et des flux d'informations continues, l'ennui est devenu une denrée rare et précieuse. Des neuroscientifiques ont montré que l'esprit en état d'ennui — le « mode par défaut » du cerveau — est particulièrement actif sur le plan créatif : c'est dans ces moments de flottement que surgissent les idées inattendues, les connexions entre concepts éloignés. Supprimer l'ennui de nos vies, c'est peut-être supprimer une condition nécessaire à la pensée originale.</p>''',
                'questions': [
                    (1, 'Selon l\'auteur, pourquoi l\'ennui a-t-il été peu étudié ?', ['A. Il est considéré comme un sentiment mineur', 'B. Il est trop douloureux à analyser', 'C. Les philosophes préfèrent les émotions positives'], 'A'),
                    (2, 'Que signifie la « diversité » chez Pascal selon le texte ?', ['A. La richesse culturelle', 'B. Le divertissement et l\'agitation perpétuelle', 'C. La diversité des philosophies'], 'B'),
                    (3, 'Pour Pascal, quel est le rôle de l\'ennui ?', ['A. Révéler la condition humaine', 'B. Favoriser la créativité', 'C. Stimuler le désir'], 'A'),
                    (4, 'Comment les romantiques ont-ils transformé la conception de l\'ennui ?', ['A. En l\'associant à la philosophie', 'B. En le reliant à une disposition poétique', 'C. En le présentant comme une maladie à soigner'], 'B'),
                    (5, 'Pour Baudelaire, l\'ennui est…', ['A. l\'absence de désir', 'B. un trop-plein de désirs impossibles', 'C. la peur de la mort'], 'B'),
                    (6, 'Pourquoi l\'auteur dit-il que l\'ennui est une « denrée rare » aujourd\'hui ?', ['A. Peu de gens le ressentent encore', 'B. Les smartphones et l\'information continue l\'ont fait disparaître', 'C. Les philosophes l\'ont réhabilité'], 'B'),
                    (7, 'Qu\'ont montré les neuroscientifiques sur le « mode par défaut » du cerveau ?', ['A. Il est inactif pendant l\'ennui', 'B. Il est particulièrement actif et créatif', 'C. Il génère de l\'anxiété'], 'B'),
                    (8, 'Quelle thèse l\'auteur défend-il implicitement ?', ['A. Il faut éviter l\'ennui à tout prix', 'B. L\'ennui est une condition nécessaire à la pensée originale', 'C. Les smartphones sont nuisibles à la santé'], 'B'),
                    (9, 'Quel procédé rhétorique ouvre l\'essai ?', ['A. Une anaphore', 'B. Un chiasme', 'C. Un contraste (on a beaucoup écrit… on a fort peu écrit)'], 'C'),
                    (10, 'La progression du texte suit…', ['A. un plan chronologique de l\'Antiquité à nos jours', 'B. un plan dialectique thèse–antithèse–synthèse', 'C. une analyse de différentes conceptions de l\'ennui à travers le temps'], 'C'),
                ],
                'q_type': 'mc',
            },
            {
                'num': 2, 'q_range': '11–20', 'type': 'association',
                'instructions': 'Vous allez lire dix extraits de textes sur la langue française (A–J). Associez chaque affirmation (11–20) au texte correspondant.',
                'messages': [
                    ('A', 'La francophonie représente aujourd\'hui plus de 320 millions de locuteurs sur cinq continents, et ce nombre devrait atteindre 700 millions d\'ici 2050, principalement en raison de la croissance démographique africaine.'),
                    ('B', 'L\'Académie française, fondée en 1635 par Richelieu, a pour mission de « donner des règles certaines à la langue ». Ses 40 membres, les Immortels, ont notamment publié huit éditions du Dictionnaire depuis sa fondation.'),
                    ('C', 'Le français est une langue à genre grammatical obligatoire, ce qui pose des questions d\'équité de représentation. L\'écriture inclusive tente d\'y répondre, non sans susciter de vives polémiques.'),
                    ('D', 'Le joual québécois, l\'accent belge, le nouchi ivoirien, le verlan parisien : la langue française se décline en une multitude de variétés régionales et sociales qui témoignent de sa vitalité.'),
                    ('E', 'La langue française est l\'une des deux seules langues officielles de l\'ensemble des institutions de l\'Union européenne depuis le Brexit, avec l\'allemand.'),
                    ('F', 'Des études psycholinguistiques montrent que le genre grammatical des noms influence inconsciemment la perception des locuteurs : une « table » est perçue différemment selon qu\'elle est grammaticalement féminine ou masculine.'),
                    ('G', 'Le mouvement de défense de la langue française contre l\'anglicisation, incarné par la loi Toubon de 1994, impose l\'usage du français dans les documents officiels, la publicité et les lieux de travail.'),
                    ('H', 'L\'orthographe française est réputée parmi les plus complexes au monde. Des études estiment qu\'un enfant francophone met en moyenne deux fois plus de temps qu\'un enfant hispanophone pour maîtriser l\'écrit.'),
                    ('I', 'Certains linguistes défendent l\'idée que toutes les langues sont également complexes et que le prestige accordé au français écrit relève d\'une construction sociale et historique, non d\'une supériorité intrinsèque.'),
                    ('J', 'La Révolution française a joué un rôle décisif dans la diffusion du français sur le territoire national, au détriment des langues régionales (breton, occitan, alsacien) qui furent longtemps marginalisées.'),
                ],
                'questions': [
                    (11, 'Ce texte évoque les projections démographiques de la francophonie.', 'A'),
                    (12, 'Ce texte concerne une loi qui protège le français contre les emprunts à l\'anglais.', 'G'),
                    (13, 'Ce texte traite de la diversité des formes du français dans le monde.', 'D'),
                    (14, 'Ce texte aborde l\'influence du genre grammatical sur la cognition.', 'F'),
                    (15, 'Ce texte évoque la difficulté de l\'orthographe française comparée à d\'autres langues.', 'H'),
                    (16, 'Ce texte décrit le rôle historique d\'un événement politique dans la diffusion du français.', 'J'),
                    (17, 'Ce texte traite du débat sur la représentation des genres dans la langue écrite.', 'C'),
                    (18, 'Ce texte remet en question le prestige du français d\'un point de vue sociologique.', 'I'),
                    (19, 'Ce texte présente l\'institution chargée de normer la langue française.', 'B'),
                    (20, 'Ce texte concerne le statut du français dans les institutions européennes.', 'E'),
                ],
                'q_type': 'match',
            },
        ],
    },
}

MOCK_CSS = """\
.mock-container{max-width:760px;margin:0 auto;padding:0 16px}
.timer-bar{position:sticky;top:0;background:var(--ink);color:var(--paper);padding:12px 16px;border-radius:0 0 8px 8px;display:flex;justify-content:space-between;align-items:center;z-index:100;box-shadow:0 2px 8px rgba(0,0,0,.15);margin-bottom:24px}
.timer-display{font-family:var(--font-sans);font-size:1.1rem;font-weight:700;letter-spacing:.5px}
.timer-display.warning{color:#FFD700}
.timer-display.critical{color:#FF6B6B;animation:pulse 1s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.6}}
.start-screen,.results-screen{background:var(--paper);border:1px solid var(--hairline);border-radius:8px;padding:28px;margin-bottom:24px}
.start-screen h2,.results-screen h2{font-size:1.4rem;margin:0 0 12px}
.start-btn{display:inline-block;padding:12px 28px;background:var(--ink);color:var(--paper);border:0;font-family:var(--font-sans);font-size:.82rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;border-radius:4px;cursor:pointer;margin-top:12px}
.start-btn:hover{opacity:.85}
.exam-area{display:none}
.exam-area.active{display:block}
.part-section{background:var(--paper);border:1px solid var(--hairline);border-radius:8px;padding:24px;margin-bottom:28px}
.part-header{font-family:var(--font-sans);font-size:.68rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px}
.part-section h2{font-size:1.2rem;margin:0 0 8px;color:var(--ink)}
.part-section .instructions{font-size:.85rem;color:var(--muted);margin-bottom:16px;padding-bottom:14px;border-bottom:1px solid var(--hairline)}
.text-title{font-weight:700;text-align:center;font-size:1.05rem;margin:12px 0;color:var(--ink)}
.text-content{font-size:.92rem;line-height:1.7;color:var(--ink);margin-bottom:18px;padding:14px;background:var(--cream-deep);border-radius:6px;border-left:3px solid var(--amber)}
.text-content p{margin:0 0 10px}
.text-content p:last-child{margin:0}
.mc-q{display:flex;gap:12px;padding:10px 0;border-top:1px solid var(--hairline)}
.mc-q .q-num{font-family:var(--font-sans);font-size:.85rem;font-weight:800;color:var(--amber);min-width:28px}
.mc-q .opts{flex:1;display:flex;flex-direction:column;gap:4px}
.mc-q .q-text{flex:1;font-size:.9rem;margin-bottom:6px}
.opt{display:flex;gap:6px;align-items:flex-start;padding:4px 6px;cursor:pointer;font-size:.9rem;border-radius:3px}
.opt:hover{background:rgba(184,134,11,.05)}
.opt-letter{font-family:var(--font-sans);font-weight:700;color:var(--amber);min-width:18px}
.opt input{margin-top:4px}
.vfn-row{display:flex;gap:8px;align-items:center;padding:8px 0;border-top:1px solid var(--hairline);font-size:.9rem}
.vfn-row .q-num{font-family:var(--font-sans);font-weight:800;color:var(--amber);min-width:28px}
.vfn-row .q-text{flex:1}
.vfn-opts{display:flex;gap:6px}
.vfn-opt{padding:4px 10px;border:1.5px solid var(--hairline);border-radius:3px;font-family:var(--font-sans);font-size:.75rem;font-weight:700;cursor:pointer;background:var(--paper);color:var(--ink)}
.vfn-opt:hover{border-color:var(--amber)}
.vfn-opt.selected{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.match-q{display:flex;gap:10px;align-items:center;padding:8px 0;border-top:1px solid var(--hairline);font-size:.9rem}
.match-q .q-num{font-family:var(--font-sans);font-weight:800;color:var(--amber);min-width:28px}
.match-q .q-text{flex:1}
.match-select{padding:5px 10px;border:1.5px solid var(--hairline);border-radius:3px;font-family:var(--font-sans);font-weight:700;background:var(--cream-deep);color:var(--ink);cursor:pointer}
.mm-block{display:grid;grid-template-columns:auto 1fr;gap:8px 14px;margin:14px 0;padding:14px;background:var(--cream-deep);border-radius:6px}
.mm-letter{font-family:var(--font-sans);font-weight:800;color:var(--amber);font-size:.95rem;padding-top:2px}
.mm-body{font-size:.85rem;line-height:1.55;color:var(--ink)}
.submit-area{background:var(--ink);color:var(--paper);border-radius:8px;padding:20px;text-align:center;margin:32px 0}
.submit-area p{margin:0 0 12px;opacity:.9}
.submit-btn{display:inline-block;padding:14px 36px;background:var(--amber);color:var(--ink);border:0;font-family:var(--font-sans);font-size:.9rem;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;border-radius:4px;cursor:pointer}
.submit-btn:hover{opacity:.9}
.results-screen{display:none}
.results-screen.active{display:block}
.score-big{font-size:3rem;font-weight:800;color:var(--amber);text-align:center;font-family:Georgia,serif}
.score-label{font-family:var(--font-sans);font-size:.72rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--muted);text-align:center;margin-bottom:18px}
.part-breakdown{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin:20px 0}
.part-score{background:var(--cream-deep);border:1px solid var(--hairline);border-radius:6px;padding:12px;text-align:center}
.part-score .name{font-family:var(--font-sans);font-size:.6rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:var(--muted)}
.part-score .val{font-size:1.3rem;font-weight:700;color:var(--ink);margin-top:4px}
.answer-key{margin-top:24px}
.answer-key h3{font-size:.88rem;font-family:var(--font-sans);font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--muted);margin:0 0 10px}
.ak-row{display:flex;gap:8px;flex-wrap:wrap}
.ak-item{font-family:var(--font-sans);font-size:.8rem;padding:3px 8px;border-radius:3px;font-weight:700}
.ak-item.correct{background:#d4edda;color:#155724}
.ak-item.wrong{background:#f8d7da;color:#721c24}
"""

def mk_breadcrumb(level, exam_type):
    crumb = f'<a href="../../../../index.html">Accueil</a><span>›</span><a href="../../../index.html">Français</a><span>›</span><a href="../../index.html">{exam_type}</a><span>›</span><a href="../index.html">{level.upper()}</a><span>›</span><strong>Simulacre 1</strong>'
    return crumb

def render_task_html(task):
    lines = []
    lines.append(f'<div class="part-section">')
    lines.append(f'  <div class="part-header">Tâche {task["num"]}</div>')
    lines.append(f'  <h2>Questions {task["q_range"]}</h2>')
    lines.append(f'  <p class="instructions">{task["instructions"]}</p>')

    if 'title' in task:
        lines.append(f'  <div class="text-title">{task["title"]}</div>')
    if 'text' in task:
        lines.append(f'  <div class="text-content">{task["text"]}</div>')

    if task['q_type'] == 'mc':
        for q_num, q_text, opts, ans in task['questions']:
            lines.append(f'  <div class="mc-q">')
            lines.append(f'    <div class="q-num">{q_num}</div>')
            lines.append(f'    <div class="opts">')
            lines.append(f'      <div class="q-text">{q_text}</div>')
            for opt in opts:
                letter = opt[0]
                lines.append(f'      <label class="opt"><span class="opt-letter">{letter}</span><input type="radio" name="q{q_num}" value="{letter}"> {opt[3:]}</label>')
            lines.append(f'    </div></div>')

    elif task['q_type'] == 'vfn':
        for q_num, q_text, opts, ans in task['questions']:
            lines.append(f'  <div class="vfn-row">')
            lines.append(f'    <div class="q-num">{q_num}</div>')
            lines.append(f'    <div class="q-text">{q_text}</div>')
            lines.append(f'    <div class="vfn-opts">')
            for o in opts:
                lines.append(f'      <button class="vfn-opt" onclick="selectVFN(this,{q_num},\'{o}\')">{o}</button>')
            lines.append(f'    </div></div>')

    elif task['q_type'] == 'match':
        # Show messages first
        lines.append('  <div class="mm-block">')
        for letter, body in task['messages']:
            lines.append(f'    <div class="mm-letter">{letter}</div><div class="mm-body">{body}</div>')
        lines.append('  </div>')
        # Available options for select
        letters = [m[0] for m in task['messages']]
        opts_html = '<option value="">—</option>' + ''.join(f'<option value="{l}">{l}</option>' for l in letters)
        for q_num, q_text, ans in task['questions']:
            lines.append(f'  <div class="match-q">')
            lines.append(f'    <div class="q-num">{q_num}</div>')
            lines.append(f'    <div class="q-text">{q_text}</div>')
            lines.append(f'    <select class="match-select" id="q{q_num}" onchange="setAns({q_num},this.value)">{opts_html}</select>')
            lines.append(f'  </div>')

    lines.append('</div>')
    return '\n'.join(lines)

def build_answers_js(exam):
    answers = {}
    for task in exam['tasks']:
        qt = task['q_type']
        if qt in ('mc', 'vfn'):
            for row in task['questions']:
                q_num, q_text, opts, ans = row
                answers[q_num] = ans
        else:  # match
            for q_num, q_text, ans in task['questions']:
                answers[q_num] = ans
    return 'const ANSWERS = ' + str(answers).replace("'", '"') + ';'

def render_mock(level, exam):
    depth = '../../../../'
    exam_type = exam['type']
    t = exam['reading_time']
    n = exam['n_questions']
    tasks_html = '\n'.join(render_task_html(t2) for t2 in exam['tasks'])
    answers_js = build_answers_js(exam)
    bc = mk_breadcrumb(level, exam_type)

    # build answer key template for JS
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{depth}favicon.svg" type="image/svg+xml">
<title>{exam['code']} — Simulacre 1 | Word Play</title>
<link rel="stylesheet" href="{depth}shared/base.css?v=v124">
<script src="/shared/auth.js?v=1"></script>
<script src="{depth}shared/dark-init.js?v=v112"></script>
<style>
{MOCK_CSS}
</style>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="../index.html" class="back back-link" aria-label="Retour"></a>
  <a href="/" class="brand"><svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px"><rect width="32" height="32" rx="4" fill="currentColor"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>Word Play</a>
  <button class="dark-toggle" aria-label="Basculer mode sombre" onclick="toggleDark()">&#9680; Sombre</button>
</div></header>

<div class="mock-container">
  <div class="breadcrumb">{bc}</div>

  <div id="startScreen" class="start-screen">
    <div class="part-header">{exam['code']} &middot; Compréhension des écrits</div>
    <h2>Simulacre 1</h2>
    <p style="font-size:.95rem;color:var(--ink);margin-bottom:8px"><strong>Durée :</strong> {t} minutes</p>
    <p style="font-size:.95rem;color:var(--ink);margin-bottom:8px"><strong>Questions :</strong> {n} ({len(exam['tasks'])} tâches)</p>
    <p style="font-size:.95rem;color:var(--ink);margin-bottom:16px">En cliquant sur <strong>Commencer</strong>, le chronomètre démarre. Le simulacre est soumis automatiquement lorsque le temps est écoulé.</p>
    <p style="font-size:.85rem;color:var(--muted);margin-bottom:18px">Conseil : lisez les questions avant les textes pour mieux cibler votre lecture.</p>
    <button class="start-btn" onclick="startExam(false)">Commencer (avec chronomètre)</button>
    <button class="start-btn" onclick="startExam(true)" style="background:var(--paper);color:var(--ink);border:1.5px solid var(--hairline);margin-left:8px">Mode pratique (sans chronomètre)</button>
    <div id="resumeSection" style="display:none;margin-top:18px;padding:14px 16px;background:var(--cream-deep);border:1px solid var(--hairline);border-radius:6px"><div style="font-family:var(--font-sans);font-size:.65rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">Progression sauvegardée</div><div id="resumeInfo" style="font-size:.88rem;color:var(--ink);margin-bottom:10px"></div><button class="start-btn" onclick="resumeExam()" style="background:var(--amber);color:var(--ink)">Continuer</button><button class="start-btn" onclick="clearSave()" style="background:var(--paper);color:var(--ink);border:1.5px solid var(--hairline);margin-left:8px">Recommencer</button></div>
    <div id="prevAttempt" style="display:none;margin-top:12px;font-family:var(--font-sans);font-size:.78rem;color:var(--muted)">Meilleur résultat précédent : <strong id="prevScore"></strong></div>
  </div>

  <div id="examArea" class="exam-area">
    <div class="timer-bar">
      <div class="timer-display" id="timerDisplay">{t:02d}:00</div>
      <div class="timer-meta">Temps restant</div>
      <button onclick="saveProgress()" style="background:transparent;border:1px solid rgba(255,255,255,.3);color:rgba(255,255,255,.85);font-family:var(--font-sans);font-size:.65rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:5px 10px;border-radius:3px;cursor:pointer">Sauvegarder</button>
    </div>

{tasks_html}

    <div class="submit-area">
      <p>Vérifiez vos réponses avant de soumettre.</p>
      <button class="submit-btn" onclick="submitExam()">Soumettre le simulacre</button>
    </div>
  </div>

  <div id="resultsScreen" class="results-screen">
    <div class="part-header">{exam['code']} &middot; Résultats</div>
    <h2>Simulacre 1 — Résultats</h2>
    <div class="score-big" id="scoreDisplay">—</div>
    <div class="score-label">Score / {n}</div>
    <div class="part-breakdown" id="partBreakdown"></div>
    <div class="answer-key">
      <h3>Corrigé</h3>
      <div class="ak-row" id="akRow"></div>
    </div>
    <div style="text-align:center;margin-top:24px">
      <button class="start-btn" onclick="restart()">Recommencer</button>
      <a href="../index.html" class="start-btn" style="text-decoration:none;margin-left:8px;background:var(--paper);color:var(--ink);border:1.5px solid var(--hairline)">Retour</a>
    </div>
  </div>
</div>

<footer class="site-footer">Word Play &middot; {exam['code']}</footer>
<script>
{answers_js}
const TOTAL = {n};
const DURATION = {t} * 60;
const STORAGE_KEY = 'wp_delf_{level}_mock1';
let userAnswers = {{}};
let timerInterval = null;
let timeLeft = DURATION;
let timerActive = false;
let practiceMode = false;

function selectVFN(btn, qNum, val) {{
  document.querySelectorAll(`[onclick*="selectVFN(this,${{qNum}},"]`).forEach(b => b.classList.remove('selected'));
  btn.classList.add('selected');
  userAnswers[qNum] = val;
  saveProgress();
}}
function setAns(qNum, val) {{ userAnswers[qNum] = val; saveProgress(); }}

function saveProgress() {{
  const data = {{ answers: userAnswers, timeLeft, saved: Date.now() }};
  localStorage.setItem(STORAGE_KEY + '_progress', JSON.stringify(data));
}}
function clearSave() {{
  localStorage.removeItem(STORAGE_KEY + '_progress');
  document.getElementById('resumeSection').style.display = 'none';
  userAnswers = {{}};
  timeLeft = DURATION;
}}

function startExam(practice) {{
  practiceMode = practice;
  document.getElementById('startScreen').style.display = 'none';
  const ea = document.getElementById('examArea');
  ea.classList.add('active');
  document.getElementById('timerDisplay').textContent = fmtTime(timeLeft);
  if (!practice) startTimer();
}}
function resumeExam() {{
  const saved = JSON.parse(localStorage.getItem(STORAGE_KEY + '_progress') || 'null');
  if (!saved) return;
  userAnswers = saved.answers || {{}};
  timeLeft = saved.timeLeft || DURATION;
  // restore VFN
  Object.entries(userAnswers).forEach(([k,v]) => {{
    const btns = document.querySelectorAll(`[onclick*="selectVFN(this,${{k}},"]`);
    btns.forEach(b => {{ if (b.textContent.trim() === v) b.classList.add('selected'); }});
    const sel = document.getElementById('q' + k);
    if (sel && sel.tagName === 'SELECT') sel.value = v;
    document.querySelectorAll(`input[name="q${{k}}"]`).forEach(r => {{ if (r.value === v) r.checked = true; }});
  }});
  startExam(false);
}}

function startTimer() {{
  timerActive = true;
  timerInterval = setInterval(() => {{
    timeLeft--;
    const d = document.getElementById('timerDisplay');
    d.textContent = fmtTime(timeLeft);
    d.className = 'timer-display' + (timeLeft < 60 ? ' critical' : timeLeft < 300 ? ' warning' : '');
    if (timeLeft <= 0) {{ clearInterval(timerInterval); submitExam(); }}
  }}, 1000);
}}
function fmtTime(s) {{
  const m = Math.floor(s/60); return (m<10?'0'+m:m)+':'+(s%60<10?'0'+s%60:s%60);
}}

function submitExam() {{
  if (timerInterval) clearInterval(timerInterval);
  // collect MC radios
  document.querySelectorAll('input[type=radio]:checked').forEach(r => {{
    const m = r.name.match(/^q(\d+)$/); if (m) userAnswers[parseInt(m[1])] = r.value;
  }});
  // collect selects
  document.querySelectorAll('select.match-select').forEach(s => {{
    const m = s.id.match(/^q(\d+)$/); if (m && s.value) userAnswers[parseInt(m[1])] = s.value;
  }});
  let correct = 0;
  const akRow = document.getElementById('akRow');
  akRow.innerHTML = '';
  Object.entries(ANSWERS).forEach(([k,ans]) => {{
    const given = userAnswers[parseInt(k)] || '';
    const ok = given === ans;
    if (ok) correct++;
    const span = document.createElement('span');
    span.className = 'ak-item ' + (ok ? 'correct' : 'wrong');
    span.textContent = k + ': ' + (given || '—') + (ok ? ' ✓' : ' ✗ (' + ans + ')');
    akRow.appendChild(span);
  }});
  const pct = Math.round(correct/TOTAL*100);
  document.getElementById('scoreDisplay').textContent = correct + '/' + TOTAL;
  document.getElementById('examArea').classList.remove('active');
  const rs = document.getElementById('resultsScreen');
  rs.style.display = 'block'; rs.classList.add('active');
  // save best
  const prev = parseInt(localStorage.getItem(STORAGE_KEY + '_best') || '0');
  if (correct > prev) localStorage.setItem(STORAGE_KEY + '_best', correct);
  localStorage.removeItem(STORAGE_KEY + '_progress');
}}
function restart() {{
  location.reload();
}}

// Check for saved progress
window.addEventListener('DOMContentLoaded', () => {{
  const saved = localStorage.getItem(STORAGE_KEY + '_progress');
  const best = localStorage.getItem(STORAGE_KEY + '_best');
  if (saved) {{
    const d = JSON.parse(saved);
    const mins = Math.round((Date.now() - d.saved) / 60000);
    document.getElementById('resumeInfo').textContent = 'Sauvegardé il y a ' + mins + ' minute(s). Temps restant : ' + fmtTime(d.timeLeft || DURATION) + '.';
    document.getElementById('resumeSection').style.display = 'block';
  }}
  if (best) {{
    document.getElementById('prevAttempt').style.display = 'block';
    document.getElementById('prevScore').textContent = best + '/' + TOTAL;
  }}
}});
</script>
</body>
</html>"""

def render_about(level, exam):
    depth = '../../../'
    exam_type = exam['type']
    bc = f'<a href="{depth}../index.html">Accueil</a><span>›</span><a href="{depth}index.html">Français</a><span>›</span><a href="../../../exams/index.html">{exam_type}</a><span>›</span><a href="../index.html">{level.upper()}</a><span>›</span><strong>À propos</strong>'
    comps = '\n'.join(f'<tr style="border-bottom:1px solid var(--hairline)"><td style="padding:8px 0;font-weight:600">{c[0]}</td><td style="text-align:center;padding:8px 0">{c[1]}</td><td style="text-align:center;padding:8px 0">{c[2]}</td><td style="text-align:right;padding:8px 0">{c[3]}</td></tr>' for c in exam['components'])
    tips = '\n'.join(f'<li>{t}</li>' for t in exam['tips'])
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{depth}../favicon.svg" type="image/svg+xml">
<title>À propos du {exam['code']} | Word Play</title>
<link rel="stylesheet" href="{depth}../shared/base.css?v=v124">
<script src="/shared/auth.js?v=1"></script>
<script src="{depth}../shared/dark-init.js?v=v112"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="../index.html" class="back back-link" aria-label="Retour"></a>
  <a href="/" class="brand"><svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px"><rect width="32" height="32" rx="4" fill="currentColor"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>Word Play</a>
  <button class="dark-toggle" aria-label="Basculer mode sombre" onclick="toggleDark()">&#9680; Sombre</button>
</div></header>
<div class="container">
  <div class="breadcrumb">{bc}</div>
  <div class="chapter-num">{exam_type} &middot; {level.upper()}</div>
  <h1>À propos du {exam['code']}</h1>
  <p class="chapter-subtitle">{exam['subtitle']}</p>
  <section class="exercise">
    <div class="ex-head">Qu'est-ce que le {exam['code']} ?</div>
    <p style="font-size:.92rem;line-height:1.7">Le {exam['code']} ({exam['subtitle']}) est un diplôme officiel délivré par le {exam['institution']}, attestant un niveau {exam['level_desc']} en français selon le Cadre Européen Commun de Référence pour les Langues (CECRL). Il est reconnu internationalement et ne comporte pas de date d'expiration.</p>
  </section>
  <section class="exercise">
    <div class="ex-head">Épreuves de l'examen</div>
    <div style="overflow-x:auto">
    <table style="width:100%;border-collapse:collapse;font-size:.88rem;margin-top:8px">
      <thead><tr style="background:var(--cream-deep)">
        <th style="text-align:left;padding:10px 12px;border-bottom:2px solid var(--hairline)">Épreuve</th>
        <th style="text-align:center;padding:10px 12px;border-bottom:2px solid var(--hairline)">Tâches</th>
        <th style="text-align:center;padding:10px 12px;border-bottom:2px solid var(--hairline)">Items</th>
        <th style="text-align:right;padding:10px 12px;border-bottom:2px solid var(--hairline)">Durée</th>
      </tr></thead>
      <tbody>
{comps}
      </tbody>
    </table>
    </div>
  </section>
  <section class="exercise">
    <div class="ex-head">Compréhension des écrits — Présentation</div>
    <p style="font-size:.92rem;line-height:1.7">{exam['reading_desc']}</p>
  </section>
  <section class="exercise">
    <div class="ex-head">Notation et conditions de réussite</div>
    <p style="font-size:.92rem;line-height:1.7">{exam['score_note']}</p>
  </section>
  <section class="exercise">
    <div class="ex-head">Conseils pour la compréhension des écrits</div>
    <ul style="font-size:.9rem;line-height:1.9;padding-left:20px">
{tips}
    </ul>
  </section>
  <div style="text-align:center;margin:28px 0">
    <a href="../mock-1/index.html" style="display:inline-block;padding:14px 32px;background:var(--amber);color:var(--ink);font-family:var(--font-sans);font-size:.85rem;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;border-radius:4px;text-decoration:none">Faire le simulacre 1 &#8594;</a>
  </div>
</div>
<footer class="site-footer">Word Play &middot; {exam['code']}</footer>
</body>
</html>"""

def render_level(level, exam):
    depth = '../../'
    exam_type = exam['type']
    bc = f'<a href="{depth}../index.html">Accueil</a><span>›</span><a href="{depth}index.html">Français</a><span>›</span><a href="../index.html">{exam_type}</a><span>›</span><strong>{exam["code"]}</strong>'
    comps_rows = ''.join(f'<tr style="border-bottom:1px solid var(--hairline)"><td style="padding:8px 0;font-weight:600">{c[0]}</td><td style="text-align:right;padding:8px 0">{c[3]}</td></tr>' for c in exam['components'])
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{depth}../favicon.svg" type="image/svg+xml">
<title>{exam['code']} — Préparation | Word Play</title>
<link rel="stylesheet" href="{depth}../shared/base.css?v=v124">
<script src="/shared/auth.js?v=1"></script>
<script src="{depth}../shared/dark-init.js?v=v112"></script>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="../index.html" class="back back-link" aria-label="Retour"></a>
  <a href="/" class="brand"><svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px"><rect width="32" height="32" rx="4" fill="currentColor"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>Word Play</a>
  <button class="dark-toggle" aria-label="Basculer mode sombre" onclick="toggleDark()">&#9680; Sombre</button>
</div></header>
<div class="section-page">
  <div class="breadcrumb">{bc}</div>
  <div style="font-family:var(--font-sans);font-size:.65rem;font-weight:800;letter-spacing:2.5px;text-transform:uppercase;color:var(--amber);margin-bottom:8px">{exam_type} &middot; NIVEAU {level.upper()}</div>
  <h1 style="font-family:Georgia,serif;font-size:2.4rem;font-weight:700;color:var(--ink);margin:0 0 8px">{exam['code']}</h1>
  <p style="color:var(--muted);font-size:.9rem;margin:0 0 28px">{exam['subtitle']}</p>
  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px;margin-bottom:32px">
    <a href="about/index.html" style="display:block;background:#1A1A1A;border-radius:10px;padding:22px 20px;text-decoration:none">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">COMMENCER ICI</div>
      <h2 style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin:0 0 8px">À propos du {exam['code']}</h2>
      <p style="font-family:var(--font-sans);font-size:.78rem;color:rgba(255,255,255,.55);margin:0">Format, épreuves, notation et conseils</p>
    </a>
    <a href="mock-1/index.html" style="display:block;background:#1A1A1A;border-radius:10px;padding:22px 20px;text-decoration:none">
      <div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:6px">SIMULACRE</div>
      <h2 style="font-family:Georgia,serif;font-size:1.25rem;font-weight:700;color:white;margin:0 0 8px">Simulacre 1</h2>
      <p style="font-family:var(--font-sans);font-size:.78rem;color:rgba(255,255,255,.55);margin:0">Compréhension des écrits — chronométrée</p>
    </a>
  </div>
  <div style="background:var(--cream-deep);border:1px solid var(--hairline);border-radius:8px;padding:20px 24px;margin-bottom:24px">
    <div style="font-family:var(--font-sans);font-size:.65rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:10px">Structure de l'examen {exam['code']}</div>
    <table style="width:100%;border-collapse:collapse;font-size:.88rem">
      <tr style="border-bottom:1px solid var(--hairline)"><th style="text-align:left;padding:6px 0;color:var(--muted)">Épreuve</th><th style="text-align:right;padding:6px 0;color:var(--muted)">Durée</th></tr>
{comps_rows}
    </table>
    <p style="font-size:.8rem;color:var(--muted);margin:12px 0 0">Le simulacre interactif couvre la <strong>Compréhension des écrits</strong>.</p>
  </div>
</div>
<footer class="site-footer">Word Play &middot; {exam['code']}</footer>
</body>
</html>"""

def main():
    for level, exam in EXAMS.items():
        base = os.path.join(ROOT, level)
        # level hub
        with open(os.path.join(base, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(render_level(level, exam))
        # about
        with open(os.path.join(base, 'about', 'index.html'), 'w', encoding='utf-8') as f:
            f.write(render_about(level, exam))
        # mock-1
        with open(os.path.join(base, 'mock-1', 'index.html'), 'w', encoding='utf-8') as f:
            f.write(render_mock(level, exam))
        print(f'{exam["code"]}: OK')

if __name__ == '__main__':
    main()
