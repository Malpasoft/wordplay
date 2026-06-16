"""francais-en A2 Grammar G01–G06 — French for English speakers"""

CHAPTERS = {
    "passe-compose-avoir": {
        "level": "a2",
        "section": "grammar",
        "num": "G01",
        "short": "Passé composé with avoir",
        "title": "Passé composé with avoir — Le Passé Composé avec Avoir",
        "subtitle": "The most common French past tense — formed with avoir + a past participle",
        "slides": [
            ("What Is the Passé Composé?",
             "The passé composé is the main past tense in spoken and written French. It describes completed actions in the past. It is formed with two parts: a present-tense auxiliary (avoir or être) + a past participle.",
             '<table class="sum-table"><thead><tr><th>Part 1: avoir (present)</th><th>Part 2: past participle</th><th>English</th></tr></thead><tbody>'
             '<tr><td>j\'ai</td><td>parlé</td><td>I spoke / I have spoken</td></tr>'
             '<tr><td>tu as</td><td>mangé</td><td>you ate / you have eaten</td></tr>'
             '<tr><td>il/elle a</td><td>fini</td><td>he/she finished</td></tr>'
             '<tr><td>nous avons</td><td>attendu</td><td>we waited</td></tr>'
             '<tr><td>vous avez</td><td>choisi</td><td>you chose</td></tr>'
             '<tr><td>ils/elles ont</td><td>vendu</td><td>they sold</td></tr>'
             '</tbody></table>'),
            ("Forming the Past Participle: Regular Verbs",
             "The past participle is formed from the infinitive. Each verb group has its own ending:",
             '<table class="sum-table"><thead><tr><th>Infinitive group</th><th>Rule</th><th>Examples</th></tr></thead><tbody>'
             '<tr><td>-er verbs</td><td>drop -er, add <b>-é</b></td><td>parler → parl<b>é</b>, manger → mang<b>é</b>, travailler → travaill<b>é</b></td></tr>'
             '<tr><td>-ir verbs</td><td>drop -ir, add <b>-i</b></td><td>finir → fin<b>i</b>, choisir → chois<b>i</b>, partir → part<b>i</b></td></tr>'
             '<tr><td>-re verbs</td><td>drop -re, add <b>-u</b></td><td>attendre → attend<b>u</b>, vendre → vend<b>u</b>, répondre → répond<b>u</b></td></tr>'
             '</tbody></table>'
             '<p>Examples in full: <em>J\'ai parlé avec elle.</em> (I spoke with her.) — <em>Il a fini son travail.</em> (He finished his work.) — <em>Nous avons attendu le bus.</em> (We waited for the bus.)</p>'),
            ("Irregular Past Participles — Must Be Memorised",
             "Many very common verbs have irregular past participles. These must be learned individually:",
             '<table class="sum-table"><thead><tr><th>Infinitive</th><th>Past Participle</th><th>Example</th></tr></thead><tbody>'
             '<tr><td>avoir (to have)</td><td><b>eu</b></td><td>J\'ai eu de la chance. (I was lucky.)</td></tr>'
             '<tr><td>être (to be)</td><td><b>été</b></td><td>Il a été malade. (He was ill.)</td></tr>'
             '<tr><td>faire (to do/make)</td><td><b>fait</b></td><td>Tu as fait quoi? (What did you do?)</td></tr>'
             '<tr><td>prendre (to take)</td><td><b>pris</b></td><td>Elle a pris le train. (She took the train.)</td></tr>'
             '<tr><td>dire (to say)</td><td><b>dit</b></td><td>Il a dit bonjour. (He said hello.)</td></tr>'
             '<tr><td>mettre (to put)</td><td><b>mis</b></td><td>J\'ai mis mon manteau. (I put on my coat.)</td></tr>'
             '<tr><td>voir (to see)</td><td><b>vu</b></td><td>Nous avons vu ce film. (We saw that film.)</td></tr>'
             '<tr><td>savoir (to know)</td><td><b>su</b></td><td>Elle a su la vérité. (She found out the truth.)</td></tr>'
             '</tbody></table>'),
            ("Negation in the Passé Composé",
             "To make the passé composé negative, place <em>ne...pas</em> around the auxiliary verb (avoir), not around the whole phrase:",
             '<ul class="slide-list">'
             '<li><b>Positive:</b> J\'ai mangé une pizza. (I ate a pizza.)</li>'
             '<li><b>Negative:</b> Je <b>n\'ai pas</b> mangé de pizza. (I didn\'t eat a pizza.)</li>'
             '<li><b>Positive:</b> Elle a vu le film. (She saw the film.)</li>'
             '<li><b>Negative:</b> Elle <b>n\'a pas</b> vu le film. (She didn\'t see the film.)</li>'
             '<li><b>Positive:</b> Nous avons fini. (We finished.)</li>'
             '<li><b>Negative:</b> Nous <b>n\'avons pas</b> fini. (We haven\'t finished.)</li></ul>'
             '<p>Note: after negation, indefinite articles change: <em>une pizza → pas de pizza</em>.</p>'),
            ("Agreement Note with Avoir",
             "Unlike être verbs, avoir verbs do NOT agree with the subject. The past participle stays in its base form. There IS one exception: agreement with a preceding direct object — but this is rarely tested at A2.",
             '<table class="sum-table"><thead><tr><th>Subject</th><th>No agreement needed</th></tr></thead><tbody>'
             '<tr><td>Il</td><td>Il a <b>mangé</b> (not mangés)</td></tr>'
             '<tr><td>Elle</td><td>Elle a <b>mangé</b> (not mangée)</td></tr>'
             '<tr><td>Elles</td><td>Elles ont <b>mangé</b> (not mangées)</td></tr>'
             '</tbody></table>'
             '<p><strong>Key rule:</strong> With avoir, the past participle does not change to match the subject. This is the opposite of être verbs (see G02).</p>'
             '<p><em>Contrast:</em> Elle est allée (être → agreement) vs Elle a mangé (avoir → no agreement).</p>'),
        ],
        "traps": [
            ("J'ai été fatigué = I was tired", "J'ai été fatigué / J'étais fatigué", "Both are possible, but <em>j'étais</em> (imparfait) is more natural for states. Use <em>a été</em> for a temporary completed state."),
            ("Il a mangée la pomme.", "Il a mangé la pomme.", "With avoir, the past participle does NOT agree with the subject. <em>Mangée</em> would only apply with a preceding direct object pronoun."),
            ("Nous avons vendu-s.", "Nous avons vendu.", "The past participle with avoir never takes -s just because the subject is plural. <em>Vendu</em> stays as is."),
            ("J'ai pris-é / j'ai prendu.", "J'ai pris.", "<em>Prendre</em> has an irregular past participle: <em>pris</em>. Never add regular endings to irregular participles."),
        ],
        "summary": [
            ("Formula", "avoir (present) + past participle", "J'ai mangé. (I ate.)"),
            ("-er → -é", "manger → mangé", "J'ai mangé une pomme."),
            ("-ir → -i", "finir → fini", "Elle a fini son travail."),
            ("-re → -u", "vendre → vendu", "Nous avons vendu la voiture."),
            ("avoir → eu", "irregular", "J'ai eu de la chance."),
            ("faire → fait", "irregular", "Tu as fait quoi?"),
            ("voir → vu", "irregular", "Nous avons vu ce film."),
            ("No agreement", "avoir: participle unchanged", "Elles ont mangé. (not mangées)"),
        ],
        "ex1": (
            "Forming the Passé Composé",
            "Choose the correct passé composé form.",
            [
                ("Elle ___ (manger) une salade.", ["a mangé", "a mangée", "est mangée", "a mangé(e)"], "a mangé", "With avoir: elle a + past participle. -er verb: manger → mangé. No agreement with avoir."),
                ("Nous ___ (finir) les devoirs.", ["avons finis", "avons fini", "sommes fini", "avons finit"], "avons fini", "-ir verb: finir → fini. Nous + avons. No -s on participle with avoir."),
                ("Tu ___ (prendre) le bus?", ["as pris", "as prendu", "as prit", "es pris"], "as pris", "Prendre is irregular: participle = <em>pris</em>. Tu + as."),
                ("Ils ___ (vendre) leur maison.", ["ont vendus", "ont vendu", "sont vendu", "ont vendues"], "ont vendu", "-re verb: vendre → vendu. Ils + ont. No agreement with avoir."),
                ("J'___ (voir) un bon film hier.", ["ai vus", "ai vue", "ai vu", "suis vu"], "ai vu", "Voir is irregular: participle = <em>vu</em>. Je + ai. No agreement with avoir."),
                ("Vous ___ (faire) du sport?", ["avez fait", "avez faite", "êtes fait", "avez fais"], "avez fait", "Faire is irregular: participle = <em>fait</em>. Vous + avez."),
            ]
        ),
        "ex2": (
            "Translate into French",
            "Write the sentence in French using the passé composé.",
            [
                ("I watched a film yesterday.", "J'ai regardé un film hier.", "regarder → regardé (regular -er). Je + ai. Hier = yesterday."),
                ("She didn't eat breakfast.", "Elle n'a pas mangé de petit-déjeuner.", "Negative: n'...pas around avoir. une → de after negation."),
                ("They (m.) took the train.", "Ils ont pris le train.", "prendre → irregular participle: pris. Ils + ont."),
                ("We saw Paul last night.", "Nous avons vu Paul hier soir.", "voir → vu (irregular). Nous + avons. Hier soir = last night."),
                ("Did you (informal) say something?", "Tu as dit quelque chose?", "dire → dit (irregular). Tu + as. Rising intonation for question."),
            ]
        ),
        "ex3": (
            "Irregular Participles",
            "Choose the correct past participle for each irregular verb.",
            [
                ("avoir → ___", ["avé", "eu", "avu", "aué"], "eu", "Avoir is completely irregular: past participle = <em>eu</em>. J'ai eu de la chance."),
                ("être → ___", ["éé", "été", "été", "est"], "été", "Être → <em>été</em>. Il a été malade. (Careful: 'a été' uses avoir as auxiliary here.)"),
                ("mettre → ___", ["mettit", "mis", "mettu", "mettré"], "mis", "Mettre → <em>mis</em>. J'ai mis mon manteau."),
                ("savoir → ___", ["savé", "su", "savi", "savait"], "su", "Savoir → <em>su</em>. Elle a su la vérité."),
                ("dire → ___", ["diré", "dit", "diru", "dis"], "dit", "Dire → <em>dit</em>. Il a dit bonjour."),
                ("prendre → ___", ["prendu", "prit", "pris", "prené"], "pris", "Prendre → <em>pris</em>. Elle a pris le métro."),
            ]
        ),
        "game_desc": "Master the passé composé with avoir and irregular past participles",
        "items": [
            ("avoir-aux", "avoir + participe", "auxiliary for most verbs in the passé composé", "to have (aux.)", "J'ai mangé une pomme. (I ate an apple.)", "avoir + participe passé = passé composé", "ai"),
            ("er-e", "-er → -é", "regular -er past participle ending", "-é ending", "parler → parlé — J'ai parlé avec elle.", "-er verbs: drop -er, add -é", "parlé"),
            ("ir-i", "-ir → -i", "regular -ir past participle ending", "-i ending", "finir → fini — Elle a fini. (She finished.)", "-ir verbs: drop -ir, add -i", "fini"),
            ("re-u", "-re → -u", "regular -re past participle ending", "-u ending", "vendre → vendu — Nous avons vendu la voiture.", "-re verbs: drop -re, add -u", "vendu"),
            ("fait", "fait", "irregular past participle of faire (to do/make)", "done", "Tu as fait quoi? (What did you do?)", "faire → fait (irregular)", "fait"),
            ("pris", "pris", "irregular past participle of prendre (to take)", "taken", "Elle a pris le train. (She took the train.)", "prendre → pris (irregular)", "pris"),
            ("vu", "vu", "irregular past participle of voir (to see)", "seen", "Nous avons vu ce film. (We saw that film.)", "voir → vu (irregular)", "vu"),
            ("no-agree-avoir", "pas d'accord", "past participle with avoir does not agree with the subject", "no agreement", "Elles ont mangé. (not mangées)", "avec avoir: pas d'accord avec le sujet", "mangé"),
        ],
    },

    "passe-compose-etre": {
        "level": "a2",
        "section": "grammar",
        "num": "G02",
        "short": "Passé composé with être",
        "title": "Passé composé with être — Le Passé Composé avec Être",
        "subtitle": "A group of movement and reflexive verbs use être — and the past participle agrees with the subject",
        "slides": [
            ("Which Verbs Use Être?",
             "Most verbs use avoir in the passé composé, but a specific group uses être. Two categories: (1) the DR MRS VANDERTRAMP movement verbs; (2) all reflexive verbs.",
             '<table class="sum-table"><thead><tr><th colspan="2">DR MRS VANDERTRAMP</th></tr></thead><tbody>'
             '<tr><td><b>D</b>evenir (to become)</td><td><b>D</b>escendre (to go down)</td></tr>'
             '<tr><td><b>R</b>evenir (to come back)</td><td><b>R</b>entrer (to go back home)</td></tr>'
             '<tr><td><b>M</b>ourir (to die)</td><td><b>M</b>onter (to go up)</td></tr>'
             '<tr><td><b>R</b>ester (to stay)</td><td><b>S</b>ortir (to go out)</td></tr>'
             '<tr><td><b>S</b>ortir (to go out)</td><td><b>V</b>enir (to come)</td></tr>'
             '<tr><td><b>V</b>enir (to come)</td><td><b>A</b>ller (to go)</td></tr>'
             '<tr><td><b>A</b>rriver (to arrive)</td><td><b>N</b>aître (to be born)</td></tr>'
             '<tr><td><b>N</b>aître (to be born)</td><td><b>D</b>écéder (to pass away)</td></tr>'
             '<tr><td><b>D</b>écéder (to pass away)</td><td><b>E</b>ntrer (to enter)</td></tr>'
             '<tr><td><b>E</b>ntrer (to enter)</td><td><b>R</b>etourner (to return)</td></tr>'
             '<tr><td><b>R</b>etourner (to return)</td><td><b>T</b>omber (to fall)</td></tr>'
             '<tr><td><b>T</b>omber (to fall)</td><td><b>R</b>ester (to stay)</td></tr>'
             '<tr><td><b>R</b>ester (to stay)</td><td><b>A</b>rriver (to arrive)</td></tr>'
             '<tr><td><b>A</b>rriver (to arrive)</td><td><b>M</b>ourir (to die)</td></tr>'
             '<tr><td><b>P</b>artir (to leave)</td><td><b>P</b>artir (to leave)</td></tr>'
             '</tbody></table>'
             '<p><strong>Tip:</strong> These are mostly verbs of motion or change of state — entering, leaving, arriving, going, coming, being born, dying.</p>'),
            ("Agreement with Subject",
             "With être verbs, the past participle agrees in gender and number with the subject — just like an adjective.",
             '<table class="sum-table"><thead><tr><th>Subject</th><th>Participle of aller</th><th>English</th></tr></thead><tbody>'
             '<tr><td>il</td><td>allé</td><td>he went</td></tr>'
             '<tr><td>elle</td><td>allé<b>e</b></td><td>she went</td></tr>'
             '<tr><td>ils</td><td>allé<b>s</b></td><td>they (m.) went</td></tr>'
             '<tr><td>elles</td><td>allé<b>es</b></td><td>they (f.) went</td></tr>'
             '<tr><td>je (m.)</td><td>allé</td><td>I went</td></tr>'
             '<tr><td>je (f.)</td><td>allé<b>e</b></td><td>I went</td></tr>'
             '<tr><td>nous (m./mixed)</td><td>allé<b>s</b></td><td>we went</td></tr>'
             '<tr><td>nous (f.)</td><td>allé<b>es</b></td><td>we went</td></tr>'
             '</tbody></table>'),
            ("Full Conjugation: être + allé",
             "Here is how to conjugate a typical être verb in the passé composé:",
             '<table class="sum-table"><thead><tr><th>Pronoun</th><th>Être (present)</th><th>Allé(e/s/es)</th></tr></thead><tbody>'
             '<tr><td>je (m.)</td><td>suis</td><td>allé</td></tr>'
             '<tr><td>je (f.)</td><td>suis</td><td>allée</td></tr>'
             '<tr><td>tu (m.)</td><td>es</td><td>allé</td></tr>'
             '<tr><td>tu (f.)</td><td>es</td><td>allée</td></tr>'
             '<tr><td>il</td><td>est</td><td>allé</td></tr>'
             '<tr><td>elle</td><td>est</td><td>allée</td></tr>'
             '<tr><td>nous (m.)</td><td>sommes</td><td>allés</td></tr>'
             '<tr><td>nous (f.)</td><td>sommes</td><td>allées</td></tr>'
             '<tr><td>vous (m.)</td><td>êtes</td><td>allés</td></tr>'
             '<tr><td>vous (f.)</td><td>êtes</td><td>allées</td></tr>'
             '<tr><td>ils</td><td>sont</td><td>allés</td></tr>'
             '<tr><td>elles</td><td>sont</td><td>allées</td></tr>'
             '</tbody></table>'),
            ("Reflexive Verbs Always Use Être",
             "All reflexive verbs (verbs with <em>se/s'</em>) use être in the passé composé. The past participle agrees with the subject:",
             '<ul class="slide-list">'
             '<li><b>se lever</b> (to get up): Je me suis levé(e). / Elle s\'est levée. / Ils se sont levés.</li>'
             '<li><b>se coucher</b> (to go to bed): Tu t\'es couché(e).</li>'
             '<li><b>s\'habiller</b> (to get dressed): Nous nous sommes habillé(e)s.</li>'
             '<li><b>se réveiller</b> (to wake up): Elle s\'est réveillée tôt. (She woke up early.)</li></ul>'
             '<p>The reflexive pronoun (me, te, se, nous, vous, se) comes before the être auxiliary.</p>'),
            ("Être vs Avoir: Quick Test",
             "Not sure which auxiliary to use? Ask yourself: Is this a DR MRS VANDERTRAMP verb? Is it reflexive? If yes to either → être. If no → avoir.",
             '<table class="sum-table"><thead><tr><th>Verb</th><th>Auxiliary</th><th>Example</th></tr></thead><tbody>'
             '<tr><td>manger</td><td>avoir</td><td>J\'ai mangé.</td></tr>'
             '<tr><td>aller</td><td>être</td><td>Je suis allé(e).</td></tr>'
             '<tr><td>partir</td><td>être</td><td>Elle est partie.</td></tr>'
             '<tr><td>voir</td><td>avoir</td><td>Nous avons vu.</td></tr>'
             '<tr><td>se lever</td><td>être (reflexive)</td><td>Il s\'est levé.</td></tr>'
             '<tr><td>tomber</td><td>être</td><td>Il est tombé.</td></tr>'
             '<tr><td>descendre*</td><td>avoir (transitive)</td><td>Il a descendu les valises. (He carried the bags down.)</td></tr>'
             '</tbody></table>'
             '<p>*A few DR MRS VANDERTRAMP verbs take avoir when they have a direct object.</p>'),
        ],
        "traps": [
            ("Elle est allé.", "Elle est allée.", "With être, the participle agrees with the subject. Elle is feminine → allée (add -e)."),
            ("Ils ont parti.", "Ils sont partis.", "Partir uses être, not avoir. And with a masculine plural subject: partis (+s)."),
            ("Je me suis levée (m.)", "Je me suis levé.", "If the speaker is male, no -e is added. Levée is only for a female speaker."),
            ("Nous sommes allé.", "Nous sommes allés / allées.", "Nous requires -s on the participle (mixed/male → -s, all female → -es)."),
        ],
        "summary": [
            ("DR MRS VANDERTRAMP", "être auxiliary", "aller, venir, partir, arriver…"),
            ("Reflexive verbs", "être auxiliary", "se lever → je me suis levé(e)"),
            ("Agreement (m. sg.)", "no change", "Il est allé."),
            ("Agreement (f. sg.)", "+e", "Elle est allée."),
            ("Agreement (m. pl.)", "+s", "Ils sont allés."),
            ("Agreement (f. pl.)", "+es", "Elles sont allées."),
            ("Negative", "ne...pas round être", "Elle n'est pas venue."),
            ("Être vs avoir test", "DR MRS VANDERTRAMP or reflexive?", "If yes → être; if no → avoir"),
        ],
        "ex1": (
            "Choose the Correct Form",
            "Select the correct passé composé form using être.",
            [
                ("Elle ___ au marché. (aller)", ["a allée", "est allée", "est allé", "a allé"], "est allée", "Aller uses être. Subject is elle (feminine) → allée (+e)."),
                ("Ils ___ à 8 heures. (partir)", ["ont partis", "sont partir", "sont partis", "ont parti"], "sont partis", "Partir uses être. Ils = masculine plural → partis (+s)."),
                ("Je ___ à Paris. (naître — f.)", ["suis née", "suis né", "ai née", "est née"], "suis née", "Naître uses être. Je (female) → née (+e). Auxiliary = suis."),
                ("Nous ___ chez Paul. (rester — mixed group)", ["avons resté", "sommes restés", "sommes restées", "avons restés"], "sommes restés", "Rester uses être. Nous (mixed/male) → restés (+s)."),
                ("Elle ___ hier soir. (se coucher)", ["a couchée", "est couchée", "s'est couchée", "se suis couchée"], "s'est couchée", "Reflexive: se + être. Elle = feminine → couchée. s'est (elle form of être)."),
                ("Les filles ___ tôt. (arriver)", ["ont arrivées", "sont arrivées", "sont arrivés", "ont arrivé"], "sont arrivées", "Arriver uses être. Les filles = feminine plural → arrivées (+es)."),
            ]
        ),
        "ex2": (
            "Translate into French",
            "Write the sentence in French using the passé composé with être.",
            [
                ("She arrived at noon.", "Elle est arrivée à midi.", "Arriver uses être. Elle = feminine → arrivée."),
                ("They (f.) went to the cinema.", "Elles sont allées au cinéma.", "Aller uses être. Elles = feminine plural → allées."),
                ("He fell in the street.", "Il est tombé dans la rue.", "Tomber uses être. Il = masculine → tombé (no change)."),
                ("We (m.) got up at seven.", "Nous nous sommes levés à sept heures.", "Se lever is reflexive → être. Nous (male/mixed) → levés."),
                ("Did you (formal) leave early?", "Vous êtes parti(e/s) tôt?", "Partir uses être. Vous = formal — participle depends on group. Tôt = early."),
            ]
        ),
        "ex3": (
            "Être or Avoir?",
            "Which auxiliary does this verb use in the passé composé?",
            [
                ("venir (to come)", ["avoir", "être", "Either", "Neither"], "être", "Venir is in DR MRS VANDERTRAMP → uses être. Il est venu."),
                ("regarder (to watch)", ["avoir", "être", "Either", "Neither"], "avoir", "Regarder is a regular -er verb, not in DR MRS VANDERTRAMP → avoir. J'ai regardé."),
                ("se réveiller (to wake up)", ["avoir", "être", "Either", "Neither"], "être", "All reflexive verbs use être. Je me suis réveillé(e)."),
                ("entrer (to enter)", ["avoir", "être", "Either", "Neither"], "être", "Entrer is in DR MRS VANDERTRAMP → être. Il est entré."),
                ("finir (to finish)", ["avoir", "être", "Either", "Neither"], "avoir", "Finir is a regular -ir verb, not reflexive, not in DR MRS VANDERTRAMP → avoir. J'ai fini."),
                ("mourir (to die)", ["avoir", "être", "Either", "Neither"], "être", "Mourir is in DR MRS VANDERTRAMP → être. Il est mort."),
            ]
        ),
        "game_desc": "Master the passé composé with être — movement verbs and agreement",
        "items": [
            ("etre-aux", "être + participe", "auxiliary for movement and reflexive verbs in the passé composé", "to be (aux.)", "Elle est allée au marché. (She went to the market.)", "être + participe = passé composé for movement verbs", "est"),
            ("aller", "allé(e/s)", "past participle of aller (to go) — être verb", "gone", "Je suis allé(e) à Paris. (I went to Paris.)", "aller → allé (être verb, agreement required)", "allé"),
            ("partir", "parti(e/s)", "past participle of partir (to leave) — être verb", "left", "Elle est partie tôt. (She left early.)", "partir → parti (être verb, agreement required)", "parti"),
            ("venir", "venu(e/s)", "past participle of venir (to come) — être verb", "come", "Ils sont venus hier. (They came yesterday.)", "venir → venu (être verb, agreement required)", "venu"),
            ("arriver", "arrivé(e/s)", "past participle of arriver (to arrive) — être verb", "arrived", "Nous sommes arrivés à midi. (We arrived at noon.)", "arriver → arrivé (être verb, agreement required)", "arrivé"),
            ("f-agree", "+e (feminine)", "add -e to participle when subject is feminine", "feminine agreement", "Elle est partie. (She left.)", "feminine subject: add -e to participle", "partie"),
            ("pl-agree", "+s (plural)", "add -s to participle when subject is plural (m./mixed)", "plural agreement", "Ils sont allés. (They went.)", "plural subject: add -s to participle", "allés"),
            ("reflexive-etre", "se + être", "reflexive verbs always use être in the passé composé", "reflexive aux.", "Je me suis levé(e). (I got up.)", "reflexive verbs → être auxiliary", "levé"),
        ],
    },

    "imparfait": {
        "level": "a2",
        "section": "grammar",
        "num": "G03",
        "short": "Imparfait",
        "title": "Imparfait — L'Imparfait",
        "subtitle": "The imparfait describes habits, ongoing states, and background action in the past",
        "slides": [
            ("When to Use the Imparfait",
             "The imparfait is used for: (1) habits and repeated actions in the past; (2) ongoing states, feelings, or descriptions in the past; (3) background context when telling a story (while something else happened).",
             '<table class="sum-table"><thead><tr><th>Use</th><th>Signal words</th><th>Example</th></tr></thead><tbody>'
             '<tr><td>Habit</td><td>toujours, souvent, tous les jours, le lundi…</td><td>Quand j\'étais enfant, je <b>jouais</b> au foot. (I used to play football.)</td></tr>'
             '<tr><td>State / description</td><td>être, avoir, aimer, savoir, penser…</td><td>Il <b>faisait</b> beau. (The weather was nice.)</td></tr>'
             '<tr><td>Background action</td><td>quand, pendant que, alors que…</td><td>Je <b>regardais</b> la télé quand il est arrivé.</td></tr>'
             '</tbody></table>'),
            ("Formation: The nous-Stem Rule",
             "The imparfait is formed from the <em>nous</em> form of the present tense. Drop <em>-ons</em> to get the stem, then add the imparfait endings. The endings are the same for ALL verbs (except être).",
             '<table class="sum-table"><thead><tr><th>Pronoun</th><th>Ending</th><th>Parler (nous parlons → stem: parl-)</th></tr></thead><tbody>'
             '<tr><td>je</td><td>-ais</td><td>je parl<b>ais</b></td></tr>'
             '<tr><td>tu</td><td>-ais</td><td>tu parl<b>ais</b></td></tr>'
             '<tr><td>il/elle/on</td><td>-ait</td><td>il parl<b>ait</b></td></tr>'
             '<tr><td>nous</td><td>-ions</td><td>nous parl<b>ions</b></td></tr>'
             '<tr><td>vous</td><td>-iez</td><td>vous parl<b>iez</b></td></tr>'
             '<tr><td>ils/elles</td><td>-aient</td><td>ils parl<b>aient</b></td></tr>'
             '</tbody></table>'
             '<p>More examples: <em>finir</em> (nous finissons → stem: finiss-): je finissais, tu finissais… | <em>faire</em> (nous faisons → stem: fais-): je faisais, tu faisais…</p>'),
            ("Être: The Only Irregular Imparfait",
             "Être is the only verb with an irregular imparfait stem: <b>ét-</b>. All endings are regular.",
             '<table class="sum-table"><thead><tr><th>Pronoun</th><th>Être — imparfait</th></tr></thead><tbody>'
             '<tr><td>je</td><td>j\'<b>étais</b></td></tr>'
             '<tr><td>tu</td><td>tu <b>étais</b></td></tr>'
             '<tr><td>il/elle/on</td><td>il/elle <b>était</b></td></tr>'
             '<tr><td>nous</td><td>nous <b>étions</b></td></tr>'
             '<tr><td>vous</td><td>vous <b>étiez</b></td></tr>'
             '<tr><td>ils/elles</td><td>ils/elles <b>étaient</b></td></tr>'
             '</tbody></table>'
             '<p>Example: <em>Il était fatigué quand il est rentré.</em> (He was tired when he got home.)</p>'),
            ("Imparfait vs Passé Composé",
             "Both tenses describe the past, but they are used differently. This contrast is one of the most important in French grammar.",
             '<table class="sum-table"><thead><tr><th>Imparfait</th><th>Passé composé</th></tr></thead><tbody>'
             '<tr><td>Ongoing, background: <em>je regardais</em></td><td>Single completed event: <em>il est arrivé</em></td></tr>'
             '<tr><td>Habit / repeated: <em>je jouais tous les jours</em></td><td>One-off event: <em>j\'ai joué hier</em></td></tr>'
             '<tr><td>State / description: <em>il faisait beau</em></td><td>Change of state: <em>il a commencé à pleuvoir</em></td></tr>'
             '<tr><td>Feeling: <em>j\'avais faim</em></td><td>Sudden feeling: <em>j\'ai eu peur</em></td></tr>'
             '</tbody></table>'
             '<p><em>Je regardais la télé quand le téléphone a sonné.</em> (I was watching TV when the phone rang.) — imparfait sets the scene; passé composé gives the event.</p>'),
            ("Time Markers and Practice",
             "Certain time expressions typically trigger the imparfait or the passé composé:",
             '<table class="sum-table"><thead><tr><th>Imparfait signals</th><th>Passé composé signals</th></tr></thead><tbody>'
             '<tr><td>toujours (always)</td><td>soudain (suddenly)</td></tr>'
             '<tr><td>souvent (often)</td><td>un jour (one day)</td></tr>'
             '<tr><td>tous les jours (every day)</td><td>hier (yesterday)</td></tr>'
             '<tr><td>chaque semaine (every week)</td><td>la semaine dernière (last week)</td></tr>'
             '<tr><td>d\'habitude (usually)</td><td>une fois (once)</td></tr>'
             '<tr><td>le lundi, le matin… (Mondays…)</td><td>ce matin-là (that morning)</td></tr>'
             '</tbody></table>'),
        ],
        "traps": [
            ("j'étais allé (imparfait of aller)", "j'allais", "Aller in the imparfait: nous allons → stem all- → j'allais. Don't confuse with the passé composé <em>je suis allé</em>."),
            ("Je jouais une fois.", "J'ai joué une fois.", "Une fois (once) signals a completed one-off event → passé composé, not imparfait."),
            ("Il parlait bien (every day) vs Il a parlé (yesterday)", "D'habitude il parlait bien. / Hier il a parlé.", "Context and time markers decide the tense. Imparfait = ongoing/habitual; passé composé = specific completed event."),
            ("nous finissions (wrong stem)", "nous finissions (correct)", "For -ir verbs, the nous-present is finissons → stem: finiss- → je finissais. Preserve the extended stem."),
        ],
        "summary": [
            ("Stem rule", "nous (present) – ons", "parler → parlons → parl-"),
            ("je / tu", "-ais", "je parlais, tu parlais"),
            ("il / elle / on", "-ait", "il parlait"),
            ("nous", "-ions", "nous parlions"),
            ("vous", "-iez", "vous parliez"),
            ("ils / elles", "-aient", "ils parlaient"),
            ("être (irregular)", "ét- + endings", "j'étais, il était"),
            ("Habit / background", "imparfait (not PC)", "Je jouais tous les jours."),
        ],
        "ex1": (
            "Form the Imparfait",
            "Choose the correct imparfait form.",
            [
                ("Quand j\'étais jeune, je ___ (jouer) au foot.", ["jouais", "jouait", "jouions", "ai joué"], "jouais", "Jouer: stem = jou- (from jouons). Je → -ais: je jouais."),
                ("Elle ___ (habiter) à Lyon à l\'époque.", ["habitait", "habitais", "habitaient", "a habité"], "habitait", "Habiter: stem = habit-. Elle → -ait: elle habitait."),
                ("Nous ___ (finir) toujours nos devoirs.", ["finissions", "finissions", "finisiez", "avons fini"], "finissions", "Finir: nous finissons → stem finiss-. Nous → -ions: finissions."),
                ("Ils ___ (être) très contents.", ["étaient", "étais", "étions", "ont été"], "étaient", "Être is irregular: ét-. Ils → -aient: étaient."),
                ("Vous ___ (manger) souvent ici?", ["mangiez", "mangeais", "mangions", "avez mangé"], "mangiez", "Manger: nous mangeons → stem mange-. Vous → -iez: mangiez."),
                ("Tu ___ (savoir) déjà la réponse.", ["savais", "savait", "sache", "as su"], "savais", "Savoir: nous savons → stem sav-. Tu → -ais: savais. (Knowing something = imparfait.)"),
            ]
        ),
        "ex2": (
            "Imparfait or Passé Composé?",
            "Write the verb in the correct past tense.",
            [
                ("Quand il était enfant, il ___ (jouer) souvent dehors.", "il jouait", "Souvent + enfant = habitual past → imparfait. Jouer: il jouait."),
                ("Soudain, le téléphone ___ (sonner).", "a sonné", "Soudain = sudden completed event → passé composé. Sonner: il a sonné."),
                ("Elle ___ (être) fatiguée, alors elle ___ (se coucher) tôt.", "elle était / elle s'est couchée", "Être fatigué = state → imparfait (était). Se coucher = completed action → passé composé (s'est couchée)."),
                ("Tous les étés, nous ___ (aller) à la mer.", "nous allions", "Tous les étés = repeated habit → imparfait. Aller: nous allions."),
                ("Un jour, il ___ (décider) de partir.", "il a décidé", "Un jour = one-off event → passé composé. Décider: il a décidé."),
            ]
        ),
        "ex3": (
            "Identify the Correct Use",
            "Which sentence correctly uses the imparfait?",
            [
                ("Describing the weather during a story:", ["Il a fait beau.", "Il faisait beau.", "Il fait beau.", "Il fera beau."], "Il faisait beau.", "Background description in a story → imparfait: il faisait beau."),
                ("A habit in childhood:", ["J'ai mangé des céréales le matin.", "Je mangeais des céréales le matin.", "Je mange des céréales le matin.", "J'ai mangé souvent."], "Je mangeais des céréales le matin.", "Childhood habit → imparfait: je mangeais."),
                ("A one-off completed event:", ["Je regardais un film hier soir.", "J'ai regardé un film hier soir.", "Je regardais hier une fois.", "Je regardais souvent hier."], "J'ai regardé un film hier soir.", "Hier soir + specific event → passé composé: j'ai regardé."),
                ("Background action when something else happened:", ["Elle a lu quand je suis arrivé.", "Elle lisait quand je suis arrivé.", "Elle lit quand je suis arrivé.", "Elle lira quand je suis arrivé."], "Elle lisait quand je suis arrivé.", "Ongoing background → imparfait (lisait); sudden event → passé composé (suis arrivé)."),
                ("Being born on a specific date:", ["J'étais né en 2002.", "Je suis né en 2002.", "Je naissais en 2002.", "Je nais en 2002."], "Je suis né en 2002.", "Birth = specific event → passé composé with être: je suis né."),
            ]
        ),
        "game_desc": "Master the imparfait — formation and contrast with the passé composé",
        "items": [
            ("imparfait-stem", "nous – ons", "take the nous-present form and drop -ons to get the imparfait stem", "stem rule", "parler → nous parlons → parl- → je parlais", "imparfait stem = nous present minus -ons", "parl-"),
            ("ais-ait", "-ais / -ait", "imparfait endings for je, tu (-ais) and il/elle (-ait)", "past endings", "je parlais, tu parlais, il parlait", "-ais (je/tu), -ait (il/elle) in imparfait", "parlais"),
            ("ions-iez", "-ions / -iez", "imparfait endings for nous (-ions) and vous (-iez)", "past endings", "nous parlions, vous parliez", "-ions (nous), -iez (vous) in imparfait", "parlions"),
            ("aient", "-aient", "imparfait ending for ils/elles — silent -ent as usual", "past ending", "ils parlaient (sounds like: parlais)", "-aient = ils/elles imparfait (silent -ent)", "parlaient"),
            ("etais", "j'étais", "imparfait of être (irregular stem: ét-)", "I was", "J'étais fatigué. (I was tired.)", "être → j'étais (irregular stem ét-)", "étais"),
            ("habitude", "toujours / souvent", "time markers that signal the imparfait (habit/repetition)", "habit signals", "Je jouais toujours au foot. (I always played football.)", "toujours/souvent/chaque → imparfait", "jouais"),
            ("background", "pendant que / quand", "imparfait for background action while something else happened", "while / when", "Je lisais quand il a téléphoné.", "background action → imparfait", "lisais"),
            ("etat", "état / description", "use imparfait for states, feelings, and descriptions in the past", "state", "Il faisait beau. Elle était heureuse.", "state/feeling/description → imparfait", "était"),
        ],
    },

    "direct-indirect-objects": {
        "level": "a2",
        "section": "grammar",
        "num": "G04",
        "short": "Object Pronouns",
        "title": "Object Pronouns — Les Pronoms Objets",
        "subtitle": "French direct and indirect object pronouns replace nouns and come before the verb",
        "slides": [
            ("Direct Object Pronouns (COD)",
             "A direct object answers 'what?' or 'whom?' after the verb (no preposition). Replace it with a direct object pronoun. These come directly before the conjugated verb.",
             '<table class="sum-table"><thead><tr><th>Person</th><th>Direct Object Pronoun</th><th>Example</th></tr></thead><tbody>'
             '<tr><td>me / m\'</td><td>me / m\'</td><td>Il <b>me</b> voit. (He sees me.)</td></tr>'
             '<tr><td>te / t\'</td><td>te / t\'</td><td>Je <b>te</b> connais. (I know you.)</td></tr>'
             '<tr><td>him / it (m.)</td><td>le / l\'</td><td>Je <b>le</b> mange. / Je <b>l\'</b>aime.</td></tr>'
             '<tr><td>her / it (f.)</td><td>la / l\'</td><td>Tu <b>la</b> vois? / Tu <b>l\'</b>appelles?</td></tr>'
             '<tr><td>us</td><td>nous</td><td>Il <b>nous</b> écoute. (He listens to us.)</td></tr>'
             '<tr><td>you (pl.)</td><td>vous</td><td>Elle <b>vous</b> attend. (She is waiting for you.)</td></tr>'
             '<tr><td>them</td><td>les</td><td>Je <b>les</b> adore. (I love them.)</td></tr>'
             '</tbody></table>'),
            ("Indirect Object Pronouns (COI)",
             "An indirect object answers 'to whom?' or 'for whom?' (preceded by <em>à</em> in French). Replace <em>à + person</em> with an indirect object pronoun. Note: the third-person forms differ from direct objects.",
             '<table class="sum-table"><thead><tr><th>Person</th><th>Indirect Object Pronoun</th><th>Example</th></tr></thead><tbody>'
             '<tr><td>to me</td><td>me / m\'</td><td>Il <b>me</b> parle. (He speaks to me.)</td></tr>'
             '<tr><td>to you</td><td>te / t\'</td><td>Je <b>te</b> téléphone. (I call you.)</td></tr>'
             '<tr><td>to him / to her</td><td><b>lui</b></td><td>Je <b>lui</b> dis la vérité. (I tell him/her the truth.)</td></tr>'
             '<tr><td>to us</td><td>nous</td><td>Il <b>nous</b> écrit. (He writes to us.)</td></tr>'
             '<tr><td>to you (pl.)</td><td>vous</td><td>Elle <b>vous</b> répond. (She replies to you.)</td></tr>'
             '<tr><td>to them</td><td><b>leur</b></td><td>Je <b>leur</b> envoie un message. (I send them a message.)</td></tr>'
             '</tbody></table>'
             '<p>Key difference: 3rd person — direct: <em>le/la/les</em>; indirect: <em>lui/leur</em>.</p>'),
            ("Placement: Before the Verb",
             "Object pronouns in French come BEFORE the conjugated verb — the opposite of English.",
             '<ul class="slide-list">'
             '<li>English: I see <em>him</em>. → French: Je <b>le</b> vois. (pronoun before verb)</li>'
             '<li>English: She calls <em>me</em>. → French: Elle <b>me</b> téléphone.</li>'
             '<li>With negation: ne goes before the pronoun, pas after the verb:<br>Je <b>ne le</b> vois <b>pas</b>. (I don\'t see him.)</li>'
             '<li>With infinitive: pronoun goes before the infinitive, not the conjugated verb:<br>Je veux <b>le</b> voir. (I want to see him.)</li></ul>'),
            ("Double Object Pronouns — Order",
             "When a sentence has both a direct and indirect object pronoun, the order is fixed:",
             '<table class="sum-table"><thead><tr><th>Position 1</th><th>Position 2</th><th>Position 3</th></tr></thead><tbody>'
             '<tr><td>me, te, nous, vous</td><td>le, la, les</td><td>lui, leur</td></tr>'
             '</tbody></table>'
             '<p>Examples:</p>'
             '<ul class="slide-list">'
             '<li>Il <b>me le</b> donne. (He gives it to me.) — me before le</li>'
             '<li>Je <b>le lui</b> dis. (I tell him/her it.) — le before lui</li>'
             '<li>Elle <b>nous les</b> envoie. (She sends them to us.) — nous before les</li>'
             '<li>Je <b>le leur</b> explique. (I explain it to them.) — le before leur</li></ul>'),
            ("Common Verbs Taking Indirect Objects",
             "Some French verbs take <em>à + person</em> and therefore use indirect object pronouns (COI), even where English might not use 'to':",
             '<ul class="slide-list">'
             '<li><b>parler à</b> → lui/leur: Il lui parle. (He speaks to him/her.)</li>'
             '<li><b>téléphoner à</b> → lui/leur: Je lui téléphone. (I call him/her.)</li>'
             '<li><b>dire à</b> → lui/leur: Je lui dis. (I tell him/her.)</li>'
             '<li><b>donner à</b> → lui/leur: Tu lui donnes. (You give it to him/her.)</li>'
             '<li><b>écrire à</b> → lui/leur: Elle leur écrit. (She writes to them.)</li>'
             '<li><b>répondre à</b> → lui/leur: Il me répond. (He answers me.)</li></ul>'),
        ],
        "traps": [
            ("Je le veux voir.", "Je veux le voir.", "With an infinitive, the object pronoun goes before the infinitive: veux + le voir, not le + veux voir."),
            ("Je lui vois. (for a direct object)", "Je le vois.", "Voir takes a direct object (see whom? → no à). Use le/la/les, not lui/leur."),
            ("Je parle le. (for parler à)", "Je lui parle.", "Parler à takes an indirect object → lui/leur, not le/la."),
            ("Je les leur donne. (wrong order)", "Je le leur donne.", "Double pronouns: me/te/nous/vous come first, then le/la/les, then lui/leur. Les + leur is not a standard double sequence; restructure."),
        ],
        "summary": [
            ("Direct: me/te/le/la", "before verb", "Je le vois. (I see him.)"),
            ("Direct: nous/vous/les", "before verb", "Je les adore. (I love them.)"),
            ("Indirect: me/te/lui", "before verb", "Je lui parle. (I speak to him.)"),
            ("Indirect: nous/vous/leur", "before verb", "Je leur écrit. (I write to them.)"),
            ("Negation", "ne + pronoun + verb + pas", "Je ne le vois pas."),
            ("With infinitive", "pronoun before infinitive", "Je veux le voir."),
            ("Double order", "me/te/nous/vous → le/la/les → lui/leur", "Je le lui dis."),
            ("lui vs le", "lui = indirect (à); le = direct", "Je lui parle. / Je le vois."),
        ],
        "ex1": (
            "Choose the Right Direct Object Pronoun",
            "Replace the underlined object with the correct direct object pronoun.",
            [
                ("Je mange [la pomme].", ["le", "la", "lui", "les"], "la", "Pomme is feminine singular → direct object pronoun: la. Je la mange."),
                ("Tu connais [mes amis]?", ["les", "leur", "le", "lui"], "les", "Amis is plural → direct object pronoun: les. Tu les connais?"),
                ("Elle appelle [Paul].", ["lui", "le", "les", "la"], "le", "Paul is masculine singular and is a direct object (appeler quelqu'un, no à) → le. Elle le appelle."),
                ("Nous regardons [le film].", ["lui", "le", "les", "la"], "le", "Film is masculine → le. Nous le regardons."),
                ("Il voit [Marie et Sophie].", ["leur", "lui", "les", "la"], "les", "Two people = plural → les. Il les voit."),
                ("Je n\'aime pas [cette idée].", ["lui", "les", "la", "le"], "la", "Idée is feminine → la. Je ne la aime pas → Je ne l'aime pas."),
            ]
        ),
        "ex2": (
            "Direct or Indirect?",
            "Choose the correct pronoun — direct (le/la/les) or indirect (lui/leur).",
            [
                ("Je ___ parle. (to him)", "lui", "Parler à → indirect object: lui. Je lui parle."),
                ("Je ___ vois. (him)", "le", "Voir → direct object (no à): le. Je le vois."),
                ("Elle ___ envoie un mail. (to them)", "leur", "Envoyer à → indirect: leur. Elle leur envoie un mail."),
                ("Nous ___ attendons. (her)", "l'", "Attendre → direct (no à): la → l' before vowel. Nous l'attendons."),
                ("Il ___ dit bonjour. (to them)", "leur", "Dire à → indirect: leur. Il leur dit bonjour."),
            ]
        ),
        "ex3": (
            "Pronoun Placement",
            "Choose the sentence with correct pronoun placement.",
            [
                ("I don't see him.", ["Je vois ne le pas.", "Je ne vois pas le.", "Je ne le vois pas.", "Ne je le vois pas."], "Je ne le vois pas.", "Negation: ne + pronoun + verb + pas. The pronoun comes between ne and the verb."),
                ("I want to call her.", ["Je veux appeler la.", "Je la veux appeler.", "Je veux la appeler.", "Je veux l'appeler."], "Je veux l'appeler.", "With infinitive: pronoun before the infinitive. La + appeler → l'appeler."),
                ("He gives it to her. (le + lui)", ["Il lui le donne.", "Il le lui donne.", "Il donne le lui.", "Il lui donne le."], "Il le lui donne.", "Double pronoun order: le/la/les before lui/leur. Il le lui donne."),
                ("She speaks to us.", ["Elle parle nous.", "Elle nous parle.", "Elle parle à nous.", "Elle nous parle à."], "Elle nous parle.", "Parler à → indirect. Nous before verb: elle nous parle."),
                ("Do you know them? (informal)", ["Tu connais les?", "Tu les connais?", "Les tu connais?", "Tu sais les?"], "Tu les connais?", "Direct object: les before the verb. Connaître (not savoir) for people."),
            ]
        ),
        "game_desc": "Master French direct and indirect object pronouns and their placement",
        "items": [
            ("le-la-les", "le / la / les", "direct object pronouns: him/it (m.) / her/it (f.) / them", "direct obj.", "Je le vois. Je la connais. Je les adore.", "le/la/les = direct object (replaces à + noun? → no)", "le"),
            ("lui-leur", "lui / leur", "indirect object pronouns: to him/her / to them", "indirect obj.", "Je lui parle. Je leur écris.", "lui/leur = indirect object (replaces à + person)", "lui"),
            ("me-te", "me / te", "1st and 2nd person object pronouns (direct and indirect)", "me/you", "Il me voit. Je te téléphone.", "me = me / te = you (direct and indirect)", "me"),
            ("nous-vous-obj", "nous / vous", "1st and 2nd plural object pronouns (direct and indirect)", "us/you", "Il nous écoute. Elle vous répond.", "nous/vous = us/you (object)", "nous"),
            ("before-verb", "avant le verbe", "object pronouns go before the conjugated verb in French", "placement", "Je le mange. (not Je mange le.)", "pronoun comes BEFORE the conjugated verb", "le"),
            ("neg-order", "ne + pron + verbe + pas", "in negation, ne comes before the pronoun", "neg. placement", "Je ne le vois pas. (I don't see him.)", "negation: ne + pronoun + verb + pas", "ne le"),
            ("inf-order", "pron. before infinitif", "with an infinitive, pronoun goes before the infinitive", "infinitive", "Je veux le voir. (not Je le veux voir.)", "infinitive: pronoun before the infinitive", "le voir"),
            ("double-order", "COD avant COI (3e pers.)", "with two pronouns: le/la/les come before lui/leur", "double order", "Je le lui dis. (I tell it to him.)", "double pronoun: le/la/les before lui/leur", "le lui"),
        ],
    },

    "depuis-pendant-il-y-a": {
        "level": "a2",
        "section": "grammar",
        "num": "G05",
        "short": "Time Expressions",
        "title": "Time Expressions — Depuis, Pendant, Il y a",
        "subtitle": "Express how long, for how long, and how long ago using the right French time expression",
        "slides": [
            ("Depuis — Since / For (Ongoing)",
             "<b>Depuis</b> is used with the <em>present tense</em> to describe a situation that started in the past and is STILL continuing now. English often uses 'for' or 'since' + perfect tense, but French uses the present.",
             '<table class="sum-table"><thead><tr><th>French (présent + depuis)</th><th>English</th></tr></thead><tbody>'
             '<tr><td>J\'habite ici <b>depuis</b> trois ans.</td><td>I have lived here for three years. (still living here)</td></tr>'
             '<tr><td>Elle travaille là <b>depuis</b> 2020.</td><td>She has worked there since 2020. (still working)</td></tr>'
             '<tr><td>Il apprend le français <b>depuis</b> six mois.</td><td>He has been learning French for six months.</td></tr>'
             '</tbody></table>'
             '<p><strong>Rule:</strong> If the action is still happening now → <em>depuis</em> + present tense.</p>'),
            ("Pendant — For (Completed Duration)",
             "<b>Pendant</b> expresses a duration that is completed or finished. It is used with the passé composé or any tense describing a bounded period. It translates as 'for'.",
             '<table class="sum-table"><thead><tr><th>French (PC + pendant)</th><th>English</th></tr></thead><tbody>'
             '<tr><td>J\'ai habité à Paris <b>pendant</b> deux ans.</td><td>I lived in Paris for two years. (no longer live there)</td></tr>'
             '<tr><td>Elle a travaillé là <b>pendant</b> six mois.</td><td>She worked there for six months. (finished)</td></tr>'
             '<tr><td>Il a dormi <b>pendant</b> dix heures.</td><td>He slept for ten hours.</td></tr>'
             '</tbody></table>'
             '<p><em>Pendant</em> can also be used with the present tense for planned durations: <em>Je vais rester pendant une semaine.</em> (I\'m going to stay for a week.)</p>'),
            ("Il y a — Ago",
             "<b>Il y a</b> + time expression = ago. It is always used with a past tense (passé composé). It indicates when something happened, not how long it lasted.",
             '<table class="sum-table"><thead><tr><th>French (PC + il y a)</th><th>English</th></tr></thead><tbody>'
             '<tr><td>Je suis arrivé <b>il y a</b> deux ans.</td><td>I arrived two years ago.</td></tr>'
             '<tr><td>Elle a téléphoné <b>il y a</b> une heure.</td><td>She called an hour ago.</td></tr>'
             '<tr><td>Il a commencé ce travail <b>il y a</b> longtemps.</td><td>He started this job a long time ago.</td></tr>'
             '</tbody></table>'
             '<p><strong>Position:</strong> <em>Il y a</em> + time normally comes after the verb phrase, though it can also open the sentence: <em>Il y a deux ans, je suis arrivé ici.</em></p>'),
            ("Ça fait… que — It's been… since / for",
             "<b>Ça fait</b> + duration + <b>que</b> + present tense is an alternative to <em>depuis</em> for ongoing situations. Both are correct; <em>ça fait</em> is more emphatic.",
             '<ul class="slide-list">'
             '<li><b>Ça fait</b> trois ans <b>que</b> j\'habite ici. = J\'habite ici depuis trois ans.</li>'
             '<li><b>Ça fait</b> longtemps <b>que</b> je ne t\'ai pas vu. (It\'s been a long time since I\'ve seen you.)</li>'
             '<li>The structure is: <em>ça fait + [duration] + que + [present / past tense]</em>.</li>'
             '<li>In questions: <em>Ça fait combien de temps que tu attends?</em> (How long have you been waiting?)</li></ul>'),
        ],
        "traps": [
            ("J'ai habité ici depuis trois ans. (still living here)", "J'habite ici depuis trois ans.", "If the action is ongoing now, use the PRESENT tense with depuis — not the passé composé."),
            ("J'habite ici pour deux ans. (English 'for')", "J'habite ici depuis deux ans.", "French does not use <em>pour</em> for duration already elapsed. Use <em>depuis</em> for ongoing, <em>pendant</em> for completed."),
            ("Il y a deux ans que j'habite ici.", "Ça fait deux ans que j'habite ici. / J'habite ici depuis deux ans.", "<em>Il y a</em> means 'ago' (completed past). For ongoing since: use <em>depuis</em> or <em>ça fait…que</em>."),
            ("pendant deux ans il y a (for ago)", "pendant deux ans / il y a deux ans", "<em>Pendant</em> = duration. <em>Il y a</em> = ago. Never mix them to mean the same thing."),
        ],
        "summary": [
            ("depuis + present", "ongoing since/for", "J'habite ici depuis 3 ans."),
            ("depuis + point in time", "since (date/year)", "Elle travaille ici depuis 2021."),
            ("pendant + PC/past", "completed duration for", "J'ai dormi pendant 8 heures."),
            ("pendant + future/present", "planned duration for", "Je reste pendant une semaine."),
            ("il y a + PC", "ago", "Il a appelé il y a 10 minutes."),
            ("il y a (opening)", "time ago opening", "Il y a deux ans, je suis parti."),
            ("ça fait…que + present", "it's been… (ongoing)", "Ça fait 3 ans que j'habite ici."),
            ("ça fait combien…que", "how long (question)", "Ça fait combien de temps que tu attends?"),
        ],
        "ex1": (
            "Choose the Correct Time Expression",
            "Select depuis, pendant, or il y a to complete the sentence.",
            [
                ("J\'apprends le français ___ deux ans. (I've been learning French for two years — still learning.)", ["depuis", "pendant", "il y a", "ça fait"], "depuis", "Still ongoing → depuis + present tense. J'apprends (present) depuis deux ans."),
                ("Elle a vécu à Rome ___ trois ans. (She lived in Rome for three years — she no longer does.)", ["depuis", "pendant", "il y a", "ça fait"], "pendant", "Completed duration → pendant + passé composé (a vécu)."),
                ("Il a commencé à 9h, ___ deux heures. (He started at 9, two hours ago.)", ["depuis", "pendant", "il y a", "ça fait"], "il y a", "When it happened (ago) → il y a + passé composé."),
                ("___ six mois que je cherche un appartement. (I've been looking for a flat for six months.)", ["Ça fait", "Il y a", "Pendant", "Depuis"], "Ça fait", "Ça fait + duration + que + present = ongoing alternative to depuis."),
                ("Nous avons travaillé ___ toute la nuit. (We worked all night.)", ["depuis", "il y a", "pendant", "ça fait"], "pendant", "Completed duration (toute la nuit = all night) → pendant."),
                ("Je l\'ai rencontré ___ exactement un an. (I met him exactly one year ago.)", ["depuis", "pendant", "il y a", "ça fait"], "il y a", "Specific point in the past (ago) → il y a + passé composé."),
            ]
        ),
        "ex2": (
            "Translate the Time Expression",
            "Translate into French using depuis, pendant, or il y a.",
            [
                ("She has lived in Paris for five years. (still living there)", "Elle habite à Paris depuis cinq ans.", "Ongoing → depuis + present. Habiter = present tense."),
                ("He studied for three hours.", "Il a étudié pendant trois heures.", "Completed duration → pendant + passé composé."),
                ("I called her two days ago.", "Je l'ai appelée il y a deux jours.", "Ago → il y a + passé composé. La → l' before vowel; agree with la (f.) in PC with avoir → appelée."),
                ("It's been a week since we left.", "Ça fait une semaine qu'on est partis.", "Ongoing since (we're still gone) → ça fait + duration + que + past."),
                ("They worked in Lyon for two years. (no longer)", "Ils ont travaillé à Lyon pendant deux ans.", "Completed → pendant + passé composé."),
            ]
        ),
        "ex3": (
            "Ongoing or Completed?",
            "Does the situation call for depuis (ongoing) or pendant (completed)?",
            [
                ("I've been waiting for 20 minutes. (still waiting)", ["depuis + present", "pendant + PC", "il y a + PC", "ça fait + PC"], "depuis + present", "Still waiting now → depuis + present tense: J'attends depuis 20 minutes."),
                ("She slept for 9 hours. (finished sleeping)", ["depuis + present", "pendant + PC", "il y a + present", "ça fait + present"], "pendant + PC", "Completed sleep → pendant + passé composé: Elle a dormi pendant 9 heures."),
                ("They have known each other for 10 years. (still friends)", ["depuis + present", "pendant + PC", "il y a + PC", "pendant + present"], "depuis + present", "Ongoing relationship → depuis + present: Ils se connaissent depuis 10 ans."),
                ("He lived abroad for a year. (came back)", ["depuis + present", "pendant + PC", "il y a + PC", "depuis + PC"], "pendant + PC", "Completed period → pendant + passé composé: Il a vécu à l'étranger pendant un an."),
                ("We've been married for six months. (still married)", ["depuis + present", "pendant + PC", "il y a + PC", "pendant + future"], "depuis + present", "Ongoing state → depuis + present: Nous sommes mariés depuis six mois."),
            ]
        ),
        "game_desc": "Master depuis, pendant, and il y a for expressing time in French",
        "items": [
            ("depuis-ongoing", "depuis", "for/since — ongoing action still happening now, used with present tense", "since/for (now)", "J'habite ici depuis trois ans. (I've lived here for three years.)", "depuis + present = ongoing duration", "depuis"),
            ("pendant-completed", "pendant", "for — completed duration, used with past or future tense", "for (done)", "J'ai dormi pendant huit heures. (I slept for eight hours.)", "pendant + PC = completed duration", "pendant"),
            ("il-y-a", "il y a", "ago — indicates when something happened in the past", "ago", "Il a appelé il y a une heure. (He called an hour ago.)", "il y a = ago (with PC)", "il y a"),
            ("ca-fait-que", "ça fait…que", "it's been… since — alternative to depuis for ongoing situations", "it's been", "Ça fait six mois que j'apprends le français.", "ça fait + time + que = it's been (ongoing)", "ça fait"),
            ("present-avec-depuis", "présent + depuis", "key rule: ongoing action = present tense + depuis (NOT passé composé)", "present ongoing", "J'attends depuis 20 minutes. (I've been waiting for 20 min.)", "ongoing since/for → présent + depuis", "j'attends"),
            ("il-y-a-vs-depuis", "il y a vs depuis", "il y a = ago (completed point); depuis = since/for (ongoing)", "ago vs since", "Il est parti il y a 2 ans. / Il est là depuis 2 ans.", "il y a = ago; depuis = still now", "il y a"),
            ("combien-depuis", "depuis combien de temps", "question: how long have you been doing X? (ongoing)", "how long?", "Depuis combien de temps tu travailles ici?", "depuis combien de temps = how long? (ongoing)", "depuis combien"),
            ("ca-fait-combien", "ça fait combien de temps que", "question: how long has it been? (alternative form)", "how long? (alt.)", "Ça fait combien de temps que tu attends?", "ça fait combien de temps que = how long? (alt.)", "ça fait combien"),
        ],
    },

    "adverbs": {
        "level": "a2",
        "section": "grammar",
        "num": "G06",
        "short": "Adverbs",
        "title": "Adverbs — Les Adverbes",
        "subtitle": "Form adverbs from adjectives with -ment, and learn their position in French sentences",
        "slides": [
            ("Forming Adverbs: -ment Suffix",
             "Most French adverbs are formed by adding <b>-ment</b> to the feminine form of the adjective (similar to English -ly).",
             '<table class="sum-table"><thead><tr><th>Adjective (m.)</th><th>Adjective (f.)</th><th>Adverb</th><th>Meaning</th></tr></thead><tbody>'
             '<tr><td>lent</td><td>lente</td><td>lente<b>ment</b></td><td>slowly</td></tr>'
             '<tr><td>doux</td><td>douce</td><td>douce<b>ment</b></td><td>gently / softly</td></tr>'
             '<tr><td>heureux</td><td>heureuse</td><td>heureuse<b>ment</b></td><td>happily / fortunately</td></tr>'
             '<tr><td>sérieux</td><td>sérieuse</td><td>sérieuse<b>ment</b></td><td>seriously</td></tr>'
             '<tr><td>complet</td><td>complète</td><td>complète<b>ment</b></td><td>completely</td></tr>'
             '<tr><td>facile</td><td>facile</td><td>facile<b>ment</b></td><td>easily</td></tr>'
             '</tbody></table>'
             '<p>If the masculine adjective ends in a vowel, add <em>-ment</em> directly to the masculine form: <em>vrai → vraiment</em>, <em>absolu → absolument</em>.</p>'),
            ("Special Rule: -ant and -ent Adjectives",
             "Adjectives ending in <b>-ant</b> or <b>-ent</b> form adverbs with <b>-amment</b> or <b>-emment</b> (both pronounced /amɑ̃/).",
             '<table class="sum-table"><thead><tr><th>Adjective</th><th>Ending</th><th>Adverb</th><th>Meaning</th></tr></thead><tbody>'
             '<tr><td>courant</td><td>-ant</td><td>cour<b>amment</b></td><td>fluently</td></tr>'
             '<tr><td>élégant</td><td>-ant</td><td>éleg<b>amment</b></td><td>elegantly</td></tr>'
             '<tr><td>évident</td><td>-ent</td><td>évid<b>emment</b></td><td>obviously</td></tr>'
             '<tr><td>fréquent</td><td>-ent</td><td>fréqu<b>emment</b></td><td>frequently</td></tr>'
             '<tr><td>récent</td><td>-ent</td><td>réc<b>emment</b></td><td>recently</td></tr>'
             '</tbody></table>'
             '<p>Memory trick: <em>-ant → -amment</em>, <em>-ent → -emment</em>. Both sound the same: /amɑ̃/.</p>'),
            ("Common Irregular Adverbs",
             "Some very common French adverbs are not formed by the -ment rule and must be memorised:",
             '<table class="sum-table"><thead><tr><th>Adverb</th><th>Meaning</th><th>Example</th></tr></thead><tbody>'
             '<tr><td><b>bien</b></td><td>well</td><td>Il parle bien français. (He speaks French well.)</td></tr>'
             '<tr><td><b>mal</b></td><td>badly / poorly</td><td>Elle chante mal. (She sings badly.)</td></tr>'
             '<tr><td><b>vite</b></td><td>quickly / fast</td><td>Tu marches vite! (You walk fast!)</td></tr>'
             '<tr><td><b>tôt</b></td><td>early</td><td>Je me lève tôt. (I get up early.)</td></tr>'
             '<tr><td><b>tard</b></td><td>late</td><td>Il rentre tard. (He comes home late.)</td></tr>'
             '<tr><td><b>beaucoup</b></td><td>a lot / much</td><td>J\'aime beaucoup ce film.</td></tr>'
             '<tr><td><b>peu</b></td><td>little / not much</td><td>Elle mange peu.</td></tr>'
             '</tbody></table>'),
            ("Position of Adverbs",
             "In French, most adverbs of manner come AFTER the conjugated verb (not between subject and verb as sometimes in English).",
             '<ul class="slide-list">'
             '<li><b>Simple tense:</b> subject + verb + <em>adverb</em><br>Elle parle <b>rapidement</b>. (She speaks quickly.)</li>'
             '<li><b>Compound tense (PC):</b> subject + avoir/être + <em>adverb</em> + participle (short adverbs)<br>Il a <b>bien</b> mangé. / J\'ai <b>beaucoup</b> travaillé.</li>'
             '<li><b>Compound tense:</b> longer adverbs usually follow the participle<br>Il a parlé <b>lentement</b>.</li>'
             '<li><b>Adverbs of time/place</b> often come at the start or end of the sentence<br><b>Hier</b>, elle est arrivée tard. / Elle est arrivée <b>hier</b>.</li></ul>'),
            ("Adverbs vs Adjectives — Don't Confuse Them",
             "In English, some words can be both adjective and adverb (fast, hard, late). In French, always use the adverb form to modify a verb.",
             '<table class="sum-table"><thead><tr><th>Incorrect (adjective form)</th><th>Correct (adverb form)</th><th>Why</th></tr></thead><tbody>'
             '<tr><td>Elle travaille <em>sérieuse</em>.</td><td>Elle travaille <b>sérieusement</b>.</td><td>Modifies verb → adverb needed</td></tr>'
             '<tr><td>Il parle <em>lent</em>.</td><td>Il parle <b>lentement</b>.</td><td>Modifies verb → adverb needed</td></tr>'
             '<tr><td>C\'est une idée <em>vraiment bien</em>.</td><td>C\'est une idée <b>vraiment bien</b>.</td><td>Correct — adverb modifies adjective</td></tr>'
             '</tbody></table>'
             '<p><strong>Rule:</strong> If you are modifying a verb → adverb. If modifying a noun → adjective (with agreement).</p>'),
        ],
        "traps": [
            ("Elle chante beautiful.", "Elle chante bien / magnifiquement.", "Never use an adjective to modify a verb in French. Use the adverb form."),
            ("courantement (from courant)", "couramment", "Adjectives ending in -ant form adverbs with -amment, not -antement. courant → couramment."),
            ("Il a bien parlé / Il a parlé bien", "Il a bien parlé.", "Short common adverbs (bien, mal, beaucoup, peu, vite) go between avoir/être and the participle in compound tenses."),
            ("évidemment (misspelling)", "évidemment", "Évident → évidemment (not évidemment with an 'a'). The -ent → -emment spelling is standard."),
        ],
        "summary": [
            ("Basic rule", "adj. (f.) + -ment", "lente → lentement"),
            ("Masc. adj. in vowel", "adj. (m.) + -ment", "vrai → vraiment"),
            ("-ant → -amment", "courant → couramment", "fluently"),
            ("-ent → -emment", "évident → évidemment", "obviously"),
            ("bien / mal", "well / badly (irregular)", "Il parle bien."),
            ("vite / tôt / tard", "fast / early / late (irregular)", "Tu marches vite!"),
            ("Position: simple tense", "after conjugated verb", "Elle parle lentement."),
            ("Position: compound tense", "short: before participle", "Il a bien mangé."),
        ],
        "ex1": (
            "Form the Adverb",
            "Choose the correct adverb form.",
            [
                ("lent → ___", ["lentement", "lentement", "lentément", "lentomment"], "lentement", "Lent → lente (f.) + -ment = lentement (slowly)."),
                ("heureux → ___", ["heureusement", "heureuxment", "heureusément", "heureusament"], "heureusement", "Heureux → heureuse (f.) + -ment = heureusement (happily/fortunately)."),
                ("courant → ___", ["courantement", "courantment", "couramment", "couramentement"], "couramment", "-ant adjective → -amment: courant → couramment (fluently)."),
                ("évident → ___", ["évidemment", "évidentement", "évidemtement", "évidemament"], "évidemment", "-ent adjective → -emment: évident → évidemment (obviously)."),
                ("vrai → ___", ["vraiment", "vraiment", "vraiement", "vraiément"], "vraiment", "Vrai ends in a vowel (m. form) → add -ment directly: vraiment (truly)."),
                ("fréquent → ___", ["fréquentement", "fréquemment", "fréquentment", "fréquamment"], "fréquemment", "-ent adjective → -emment: fréquent → fréquemment (frequently)."),
            ]
        ),
        "ex2": (
            "Adjective or Adverb?",
            "Fill in the blank with the correct form.",
            [
                ("Il parle ___ (lent) pour que je comprenne.", "lentement", "Modifies the verb parler → adverb: lentement."),
                ("C\'est une réponse ___. (rapide)", "rapide", "Modifies the noun réponse → adjective (agrees): rapide (f. same form)."),
                ("Elle travaille très ___. (sérieux)", "sérieusement", "Modifies the verb travailler → adverb: sérieusement."),
                ("Tu marches ___. (vite)", "vite", "Irregular adverb: vite (fast). No -ment form."),
                ("C\'est un film ___. (récent)", "récent", "Modifies the noun film → adjective: récent (masculine singular)."),
            ]
        ),
        "ex3": (
            "Position of the Adverb",
            "Choose the sentence with the adverb in the correct position.",
            [
                ("She speaks French well.", ["Elle bien parle français.", "Elle parle bien français.", "Elle parle français bien.", "Bien elle parle français."], "Elle parle bien français.", "Adverb of manner (bien) comes after the conjugated verb: parle bien."),
                ("He has worked a lot. (PC)", ["Il a beaucoup travaillé.", "Il beaucoup a travaillé.", "Il a travaillé beaucoup.", "Beaucoup il a travaillé."], "Il a beaucoup travaillé.", "In the PC, short adverbs (beaucoup) go between avoir/être and the participle."),
                ("She spoke slowly. (PC)", ["Elle a lentement parlé.", "Elle a parlé lentement.", "Elle lentement a parlé.", "Lentement elle a parlé."], "Elle a parlé lentement.", "Long adverbs (-ment) in the PC typically follow the past participle."),
                ("I always eat well.", ["Je toujours mange bien.", "Je mange bien toujours.", "Je mange toujours bien.", "Toujours je mange bien."], "Je mange toujours bien.", "Toujours (adverb of frequency) comes after the conjugated verb in simple tenses."),
                ("Yesterday, she arrived late.", ["Tard, hier elle est arrivée.", "Elle est arrivée hier tard.", "Hier, elle est arrivée tard.", "Elle est tard arrivée hier."], "Hier, elle est arrivée tard.", "Time adverbs can open or close the sentence: hier at start is natural; tard at end."),
            ]
        ),
        "game_desc": "Master French adverb formation and position in the sentence",
        "items": [
            ("ment-rule", "adj. (f.) + -ment", "standard rule for forming adverbs from adjectives", "-ment suffix", "lente → lentement, heureuse → heureusement", "adverb = feminine adj. + -ment", "lentement"),
            ("amment", "-ant → -amment", "adjectives ending in -ant form adverbs with -amment", "-amment", "courant → couramment, élégant → élégamment", "-ant adjectives → -amment", "couramment"),
            ("emment", "-ent → -emment", "adjectives ending in -ent form adverbs with -emment", "-emment", "évident → évidemment, fréquent → fréquemment", "-ent adjectives → -emment", "évidemment"),
            ("bien", "bien", "well (irregular adverb — not bienment)", "well", "Il parle bien français. (He speaks French well.)", "bien = well (irregular)", "bien"),
            ("mal", "mal", "badly / poorly (irregular adverb — not malament)", "badly", "Elle chante mal. (She sings badly.)", "mal = badly (irregular)", "mal"),
            ("vite", "vite", "quickly / fast (irregular adverb)", "fast", "Tu marches vite! (You walk fast!)", "vite = quickly/fast (irregular)", "vite"),
            ("tot-tard", "tôt / tard", "early / late (irregular adverbs)", "early/late", "Je me lève tôt. Il rentre tard.", "tôt = early, tard = late (irregular)", "tôt"),
            ("position", "après le verbe", "adverbs of manner come after the conjugated verb (simple) or before the participle (short adverbs in PC)", "after verb", "Elle parle lentement. / Il a bien mangé.", "adverb position: after conjugated verb", "lentement"),
        ],
    },
}
