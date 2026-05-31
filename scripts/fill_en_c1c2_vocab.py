#!/usr/bin/env python3
"""Fill 12 stub English C1/C2 vocabulary chapters with complete content.

Generates:
  - slides.html   (word-overview format, replaces grammar-template stub)
  - flashcards.html (full flip-card + match + list interface)
  - game.html     (replaces placeholder items with real GAME_DATA)

Run from repo root:
  python3 scripts/fill_en_c1c2_vocab.py
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = dict(base='v123', slides='v115', game='v110', dark_init='v109', store='v105', deck='v113')

WP_SVG = ('<svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px">'
          '<rect width="32" height="32" rx="4" fill="currentColor"/>'
          '<text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" '
          'font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>')

# ── Vocabulary data for each chapter ────────────────────────────────────────
# Each word: {id, word, ipa, def, ex}
# Each game item uses the same word data

CHAPTERS = {

'c1/abstract-nouns': dict(
    level='c1', slug='abstract-nouns', title='Abstract Nouns',
    subtitle='concept · phenomenon · tendency · perception · assumption',
    num='V8',
    words=[
        dict(id='concept', word='Concept', ipa='ˈkɒn.sept',
             def_='an abstract idea or principle that helps us understand something',
             ex='The <b>concept</b> of justice is central to any legal system.'),
        dict(id='phenomenon', word='Phenomenon', ipa='fəˈnɒm.ɪ.nən',
             def_='an observable event or fact, especially one that is remarkable',
             ex='Climate change is a global <b>phenomenon</b> affecting every continent.'),
        dict(id='tendency', word='Tendency', ipa='ˈten.dən.si',
             def_='an inclination to think, behave, or occur in a particular way',
             ex='There is a <b>tendency</b> to oversimplify complex problems.'),
        dict(id='perception', word='Perception', ipa='pəˈsep.ʃən',
             def_='the way in which something is understood or interpreted',
             ex='Public <b>perception</b> of the government has shifted dramatically.'),
        dict(id='assumption', word='Assumption', ipa='əˈsʌmp.ʃən',
             def_='something accepted as true without proof',
             ex='The argument rests on the <b>assumption</b> that all data is accurate.'),
        dict(id='inference', word='Inference', ipa='ˈɪn.fər.əns',
             def_='a conclusion reached by reasoning from evidence',
             ex='We can draw the <b>inference</b> that demand will rise.'),
        dict(id='convention', word='Convention', ipa='kənˈven.ʃən',
             def_='an accepted way of behaving or doing things in a particular context',
             ex='It is a social <b>convention</b> to shake hands when meeting.'),
        dict(id='perspective', word='Perspective', ipa='pəˈspek.tɪv',
             def_='a particular attitude towards or way of regarding something',
             ex='The study examines poverty from a sociological <b>perspective</b>.'),
        dict(id='notion', word='Notion', ipa='ˈnəʊ.ʃən',
             def_='an idea or belief, often one that is vague or uncertain',
             ex='The <b>notion</b> that success is purely about hard work is debatable.'),
        dict(id='dilemma', word='Dilemma', ipa='dɪˈlem.ə',
             def_='a difficult situation in which a choice must be made between two options',
             ex='The ethical <b>dilemma</b> of privacy versus security remains unresolved.'),
    ]
),

'c1/academic-verbs': dict(
    level='c1', slug='academic-verbs', title='Academic Verbs',
    subtitle='argue · suggest · demonstrate · highlight · indicate · conclude',
    num='V9',
    words=[
        dict(id='argue', word='Argue', ipa='ˈɑː.ɡjuː',
             def_='to present reasons for or against a position in formal writing',
             ex='The author <b>argues</b> that economic inequality is widening.'),
        dict(id='suggest', word='Suggest', ipa='səˈdʒest',
             def_='to put forward an idea or possibility without stating it as a fact',
             ex='The data <b>suggests</b> a correlation between income and health outcomes.'),
        dict(id='demonstrate', word='Demonstrate', ipa='ˈdem.ən.streɪt',
             def_='to show clearly through evidence or example',
             ex='The experiment <b>demonstrates</b> that temperature affects reaction rate.'),
        dict(id='highlight', word='Highlight', ipa='ˈhaɪ.laɪt',
             def_='to draw attention to something important',
             ex='The report <b>highlights</b> several key policy failures.'),
        dict(id='indicate', word='Indicate', ipa='ˈɪn.dɪ.keɪt',
             def_='to show or point to something as a sign or signal',
             ex='Survey results <b>indicate</b> a decline in public trust.'),
        dict(id='conclude', word='Conclude', ipa='kənˈkluːd',
             def_='to reach a judgement or decision after reasoning or investigation',
             ex='The study <b>concludes</b> that early intervention is most effective.'),
        dict(id='assess', word='Assess', ipa='əˈses',
             def_='to evaluate or estimate the nature, value, or quality of something',
             ex='The committee will <b>assess</b> the impact of the proposed changes.'),
        dict(id='challenge', word='Challenge', ipa='ˈtʃæl.ɪndʒ',
             def_='to question the truth or validity of something',
             ex='The new findings <b>challenge</b> the widely held theory.'),
        dict(id='illustrate', word='Illustrate', ipa='ˈɪl.ə.streɪt',
             def_='to explain or make something clearer by using examples',
             ex='This case study <b>illustrates</b> how poverty affects education.'),
        dict(id='reveal', word='Reveal', ipa='rɪˈviːl',
             def_='to make previously unknown information known',
             ex='The investigation <b>revealed</b> serious flaws in the process.'),
    ]
),

'c1/attitudes-opinions': dict(
    level='c1', slug='attitudes-opinions', title='Attitudes & Opinions',
    subtitle='controversial · sceptical · compelling · contentious · persuasive',
    num='V10',
    words=[
        dict(id='controversial', word='Controversial', ipa='ˌkɒn.trəˈvɜː.ʃəl',
             def_='causing disagreement and strong debate',
             ex='The policy is <b>controversial</b> because it affects many communities.'),
        dict(id='sceptical', word='Sceptical', ipa='ˈskep.tɪ.kəl',
             def_='not easily convinced; having doubts',
             ex='Experts remain <b>sceptical</b> about the long-term benefits.'),
        dict(id='compelling', word='Compelling', ipa='kəmˈpel.ɪŋ',
             def_='very interesting or persuasive; difficult to resist or deny',
             ex='She made a <b>compelling</b> case for increased investment.'),
        dict(id='contentious', word='Contentious', ipa='kənˈten.ʃəs',
             def_='likely to cause argument or disagreement',
             ex='Immigration remains a <b>contentious</b> issue across Europe.'),
        dict(id='persuasive', word='Persuasive', ipa='pəˈsweɪ.sɪv',
             def_='good at convincing people to believe or do something',
             ex='The charity ran a <b>persuasive</b> campaign about climate action.'),
        dict(id='objective', word='Objective', ipa='əbˈdʒek.tɪv',
             def_='not influenced by personal feelings; based on facts',
             ex='A good journalist should remain <b>objective</b> when reporting news.'),
        dict(id='biased', word='Biased', ipa='ˈbaɪ.əst',
             def_='showing an unfair preference for or against something',
             ex='The report was <b>biased</b> in favour of the government position.'),
        dict(id='impartial', word='Impartial', ipa='ɪmˈpɑː.ʃəl',
             def_='treating all sides equally; not favouring one over another',
             ex='The mediator was praised for her <b>impartial</b> approach.'),
        dict(id='cynical', word='Cynical', ipa='ˈsɪn.ɪ.kəl',
             def_='believing that people are motivated only by self-interest',
             ex='He was <b>cynical</b> about politicians\' promises.'),
        dict(id='credible', word='Credible', ipa='ˈkred.ɪ.bəl',
             def_='able to be believed; convincing and trustworthy',
             ex='The government needs a <b>credible</b> plan to reduce emissions.'),
    ]
),

'c1/cause-effect': dict(
    level='c1', slug='cause-effect', title='Cause and Effect',
    subtitle='consequently · therefore · stems from · brings about · leads to',
    num='V11',
    words=[
        dict(id='consequently', word='Consequently', ipa='ˈkɒn.sɪ.kwənt.li',
             def_='as a result; therefore',
             ex='Funding was cut. <b>Consequently</b>, several programmes were abandoned.'),
        dict(id='therefore', word='Therefore', ipa='ˈðeə.fɔː',
             def_='for that reason; as a logical conclusion',
             ex='The evidence is inconclusive. <b>Therefore</b>, no firm conclusions can be drawn.'),
        dict(id='stems_from', word='Stems from', ipa='stemz frɒm',
             def_='originates from; has its source in',
             ex='The problem <b>stems from</b> a lack of effective communication.'),
        dict(id='brings_about', word='Brings about', ipa='brɪŋz əˈbaʊt',
             def_='causes something to happen; produces a change',
             ex='Economic growth does not automatically <b>bring about</b> social equality.'),
        dict(id='leads_to', word='Leads to', ipa='liːdz tuː',
             def_='results in; causes something to happen',
             ex='Prolonged stress can <b>lead to</b> serious health complications.'),
        dict(id='contributes_to', word='Contributes to', ipa='kənˈtrɪb.juːts tuː',
             def_='is one of the factors that causes or helps produce something',
             ex='Poor diet <b>contributes to</b> a higher risk of chronic disease.'),
        dict(id='results_in', word='Results in', ipa='rɪˈzʌlts ɪn',
             def_='produces or causes a particular outcome',
             ex='Deforestation <b>results in</b> the loss of biodiversity.'),
        dict(id='gives_rise_to', word='Gives rise to', ipa='ɡɪvz raɪz tuː',
             def_='causes or produces something, often something new or negative',
             ex='Urbanisation <b>gives rise to</b> overcrowding in major cities.'),
        dict(id='underpins', word='Underpins', ipa='ˌʌn.dəˈpɪnz',
             def_='supports or provides the basis for something',
             ex='Trust <b>underpins</b> all successful professional relationships.'),
        dict(id='triggers', word='Triggers', ipa='ˈtrɪɡ.əz',
             def_='causes something to start or happen, often suddenly',
             ex='A minor incident can <b>trigger</b> widespread social unrest.'),
    ]
),

'c1/contrast-concession': dict(
    level='c1', slug='contrast-concession', title='Contrast & Concession',
    subtitle='despite · nevertheless · whereas · albeit · notwithstanding',
    num='V12',
    words=[
        dict(id='despite', word='Despite', ipa='dɪˈspaɪt',
             def_='without being affected by; regardless of',
             ex='<b>Despite</b> the evidence, many people remain unconvinced.'),
        dict(id='nevertheless', word='Nevertheless', ipa='ˌnev.ə.ðəˈles',
             def_='in spite of that; used to add a contrasting point',
             ex='The experiment failed. <b>Nevertheless</b>, valuable data was collected.'),
        dict(id='whereas', word='Whereas', ipa='weərˈæz',
             def_='in contrast to the fact that; while on the other hand',
             ex='Urban areas are growing, <b>whereas</b> rural populations are declining.'),
        dict(id='albeit', word='Albeit', ipa='ɔːlˈbiː.ɪt',
             def_='although; even though — formal and concessive',
             ex='The plan was effective, <b>albeit</b> expensive to implement.'),
        dict(id='notwithstanding', word='Notwithstanding', ipa='ˌnɒt.wɪðˈstæn.dɪŋ',
             def_='in spite of; despite — very formal, used in legal/academic writing',
             ex='<b>Notwithstanding</b> these challenges, the project was completed on time.'),
        dict(id='however', word='However', ipa='haʊˈev.ər',
             def_='used to introduce a contrast or complication',
             ex='The results were positive. <b>However</b>, further testing is required.'),
        dict(id='conversely', word='Conversely', ipa='ˈkɒn.vɜːs.li',
             def_='introducing a fact that is the opposite of what was just stated',
             ex='Investment increased output. <b>Conversely</b>, cuts reduced productivity.'),
        dict(id='in_contrast', word='In contrast', ipa='ɪn ˈkɒn.trɑːst',
             def_='when compared with something different; on the other hand',
             ex='Nordic countries have high taxes. <b>In contrast</b>, the US has lower rates.'),
        dict(id='yet', word='Yet', ipa='jet',
             def_='but; nevertheless — introduces a surprising or contrary point',
             ex='The task was difficult, <b>yet</b> the team managed to meet the deadline.'),
        dict(id='even_so', word='Even so', ipa='ˈiː.vən səʊ',
             def_='despite what has just been said; nevertheless',
             ex='The evidence was weak. <b>Even so</b>, the jury returned a guilty verdict.'),
    ]
),

'c1/formal-synonyms': dict(
    level='c1', slug='formal-synonyms', title='Formal Synonyms',
    subtitle='commence · endeavour · facilitate · obtain · regarding · sufficient',
    num='V13',
    words=[
        dict(id='commence', word='Commence', ipa='kəˈmens',
             def_='to begin (formal equivalent of "start")',
             ex='The meeting will <b>commence</b> at nine o\'clock sharp.'),
        dict(id='endeavour', word='Endeavour', ipa='ɪnˈdev.ər',
             def_='to try hard to do or achieve something (formal equivalent of "try")',
             ex='We will <b>endeavour</b> to resolve the matter as soon as possible.'),
        dict(id='facilitate', word='Facilitate', ipa='fəˈsɪl.ɪ.teɪt',
             def_='to make something easier or possible (formal equivalent of "help")',
             ex='Technology can <b>facilitate</b> communication across long distances.'),
        dict(id='obtain', word='Obtain', ipa='əbˈteɪn',
             def_='to get or acquire something (formal equivalent of "get")',
             ex='You must <b>obtain</b> written permission before publishing.'),
        dict(id='regarding', word='Regarding', ipa='rɪˈɡɑː.dɪŋ',
             def_='concerning; with respect to (formal equivalent of "about")',
             ex='I am writing <b>regarding</b> your recent application.'),
        dict(id='sufficient', word='Sufficient', ipa='səˈfɪʃ.ənt',
             def_='enough for the purpose (formal equivalent of "enough")',
             ex='There is not <b>sufficient</b> evidence to support the claim.'),
        dict(id='subsequently', word='Subsequently', ipa='ˈsʌb.sɪ.kwənt.li',
             def_='after something; afterwards (formal equivalent of "later")',
             ex='The proposal was rejected and <b>subsequently</b> revised.'),
        dict(id='prior_to', word='Prior to', ipa='ˈpraɪ.ər tuː',
             def_='before (formal equivalent of "before")',
             ex='<b>Prior to</b> the merger, both companies were struggling.'),
        dict(id='pertaining_to', word='Pertaining to', ipa='pəˈteɪ.nɪŋ tuː',
             def_='relating to or connected with (formal equivalent of "relating to")',
             ex='Please refer to the section <b>pertaining to</b> data protection.'),
        dict(id='acknowledge', word='Acknowledge', ipa='əkˈnɒl.ɪdʒ',
             def_='to accept or admit that something is true (formal equivalent of "admit")',
             ex='The report <b>acknowledges</b> significant room for improvement.'),
    ]
),

'c1/topic-vocabulary-arts': dict(
    level='c1', slug='topic-vocabulary-arts', title='Arts & Culture',
    subtitle='aesthetic · portrayal · genre · narrative · interpretation · critique',
    num='V14',
    words=[
        dict(id='aesthetic', word='Aesthetic', ipa='iːsˈθet.ɪk',
             def_='relating to beauty and the appreciation of art',
             ex='The film\'s <b>aesthetic</b> was influenced by Japanese cinema.'),
        dict(id='portrayal', word='Portrayal', ipa='pɔːˈtreɪ.əl',
             def_='a representation or description of someone or something in art or media',
             ex='Critics praised her <b>portrayal</b> of the complex historical figure.'),
        dict(id='genre', word='Genre', ipa='ˈʒɒn.rə',
             def_='a category of artistic work with similar style or subject matter',
             ex='The novel defies easy classification into any single <b>genre</b>.'),
        dict(id='narrative', word='Narrative', ipa='ˈnær.ə.tɪv',
             def_='a story or account of events; also the way a story is told',
             ex='The film\'s <b>narrative</b> unfolds through multiple perspectives.'),
        dict(id='interpretation', word='Interpretation', ipa='ɪnˌtɜː.prɪˈteɪ.ʃən',
             def_='an explanation or understanding of the meaning of something',
             ex='There are many valid <b>interpretations</b> of this abstract painting.'),
        dict(id='critique', word='Critique', ipa='krɪˈtiːk',
             def_='a detailed analysis and assessment of a work of art or literature',
             ex='The essay offers a thoughtful <b>critique</b> of the director\'s style.'),
        dict(id='motif', word='Motif', ipa='məʊˈtiːf',
             def_='a recurring element — image, idea, or symbol — in a work of art',
             ex='Water is a central <b>motif</b> in the novel, representing change.'),
        dict(id='symbolism', word='Symbolism', ipa='ˈsɪm.bəl.ɪ.zəm',
             def_='the use of symbols to represent ideas or qualities in a work',
             ex='The white dove is often used in <b>symbolism</b> to represent peace.'),
        dict(id='protagonist', word='Protagonist', ipa='prəˈtæɡ.ə.nɪst',
             def_='the main character in a story or the leading figure in a cause',
             ex='The <b>protagonist</b> undergoes a profound transformation by the final act.'),
        dict(id='juxtaposition', word='Juxtaposition', ipa='ˌdʒʌk.stə.pəˈzɪʃ.ən',
             def_='the placement of two contrasting things close together for effect',
             ex='The director uses <b>juxtaposition</b> to contrast wealth and poverty.'),
    ]
),

# ── C2 chapters ────────────────────────────────────────────────────────────

'c2/connotation-register': dict(
    level='c2', slug='connotation-register', title='Connotation & Register',
    subtitle='derogatory · euphemism · loaded language · understatement · irony',
    num='V8',
    words=[
        dict(id='connotation', word='Connotation', ipa='ˌkɒn.əˈteɪ.ʃən',
             def_='the feeling or idea associated with a word, beyond its literal meaning',
             ex='"Home" has warm <b>connotations</b> that "house" does not share.'),
        dict(id='derogatory', word='Derogatory', ipa='dɪˈrɒɡ.ə.tər.i',
             def_='showing a critical or disrespectful attitude',
             ex='The review contained several <b>derogatory</b> remarks about the author.'),
        dict(id='euphemism', word='Euphemism', ipa='ˈjuː.fə.mɪ.z əm',
             def_='a mild or indirect word used in place of one that seems too harsh',
             ex='"Passed away" is a <b>euphemism</b> for "died".'),
        dict(id='loaded_language', word='Loaded language', ipa='ˈləʊ.dɪd ˈlæŋ.ɡwɪdʒ',
             def_='words that carry strong emotional associations to influence the reader',
             ex='The politician\'s speech was full of <b>loaded language</b> to provoke fear.'),
        dict(id='understatement', word='Understatement', ipa='ˈʌn.dəˌsteɪt.mənt',
             def_='deliberately describing something as less significant than it is',
             ex='"It was a bit chilly" is an <b>understatement</b> for -20°C.'),
        dict(id='irony', word='Irony', ipa='ˈaɪ.rə.ni',
             def_='expressing meaning through language that normally means the opposite',
             ex='"What lovely weather!" said with <b>irony</b> during a storm.'),
        dict(id='pejorative', word='Pejorative', ipa='pɪˈdʒɒr.ə.tɪv',
             def_='expressing disapproval or contempt in the meaning of a word',
             ex='"Bureaucrat" is often used in a <b>pejorative</b> sense.'),
        dict(id='implication', word='Implication', ipa='ˌɪm.plɪˈkeɪ.ʃən',
             def_='something suggested or hinted at rather than stated directly',
             ex='The <b>implication</b> of her silence was that she disagreed.'),
        dict(id='nuance', word='Nuance', ipa='ˈnjuː.ɑːns',
             def_='a subtle difference in meaning, tone, or feeling',
             ex='The translation failed to capture the <b>nuances</b> of the original text.'),
        dict(id='register', word='Register', ipa='ˈredʒ.ɪ.stər',
             def_='the level of formality in language suited to a particular context',
             ex='Formal academic writing requires a different <b>register</b> to casual speech.'),
    ]
),

'c2/literary-devices': dict(
    level='c2', slug='literary-devices', title='Literary Devices',
    subtitle='metaphor · simile · allusion · personification · paradox · irony',
    num='V9',
    words=[
        dict(id='metaphor', word='Metaphor', ipa='ˈmet.ə.fɔː',
             def_='describing something by saying it is something else to suggest a similarity',
             ex='"Life is a journey" is a common <b>metaphor</b>.'),
        dict(id='simile', word='Simile', ipa='ˈsɪm.ɪ.li',
             def_='a comparison using "like" or "as"',
             ex='"As cold as ice" is a <b>simile</b>.'),
        dict(id='allusion', word='Allusion', ipa='əˈluː.ʒən',
             def_='an indirect reference to a person, place, or event',
             ex='Calling someone a "Romeo" is an <b>allusion</b> to Shakespeare.'),
        dict(id='personification', word='Personification', ipa='pəˌsɒn.ɪ.fɪˈkeɪ.ʃən',
             def_='attributing human qualities to non-human things',
             ex='"The wind whispered secrets" uses <b>personification</b>.'),
        dict(id='paradox', word='Paradox', ipa='ˈpær.ə.dɒks',
             def_='a statement that seems contradictory but reveals a deeper truth',
             ex='"Less is more" is a famous <b>paradox</b>.'),
        dict(id='hyperbole', word='Hyperbole', ipa='haɪˈpɜː.bəl.i',
             def_='deliberate exaggeration for dramatic or comic effect',
             ex='"I\'ve told you a million times" is an example of <b>hyperbole</b>.'),
        dict(id='oxymoron', word='Oxymoron', ipa='ˌɒk.siˈmɔː.rɒn',
             def_='a phrase combining two contradictory terms',
             ex='"Deafening silence" is an <b>oxymoron</b>.'),
        dict(id='allegory', word='Allegory', ipa='ˈæl.ɪ.ɡər.i',
             def_='a story where characters and events symbolise deeper moral truths',
             ex='Orwell\'s <i>Animal Farm</i> is a political <b>allegory</b>.'),
        dict(id='foreshadowing', word='Foreshadowing', ipa='ˈfɔː.ˌʃæd.əʊ.ɪŋ',
             def_='giving an advance hint of what is to come later in the narrative',
             ex='The storm in chapter one was <b>foreshadowing</b> the conflict ahead.'),
        dict(id='motif', word='Motif', ipa='məʊˈtiːf',
             def_='a recurring image or idea that develops a theme throughout a work',
             ex='The recurring mirror <b>motif</b> suggests self-deception in the novel.'),
    ]
),

'c2/persuasive-language': dict(
    level='c2', slug='persuasive-language', title='Persuasive Language',
    subtitle='rhetoric · ethos · pathos · logos · assertion · refutation',
    num='V10',
    words=[
        dict(id='rhetoric', word='Rhetoric', ipa='ˈret.ər.ɪk',
             def_='language designed to persuade, often using elaborate or impressive techniques',
             ex='His speech was praised for its powerful <b>rhetoric</b>.'),
        dict(id='ethos', word='Ethos', ipa='ˈiː.θɒs',
             def_='an appeal to authority, credibility, or the speaker\'s character',
             ex='Citing research credentials is a classic use of <b>ethos</b>.'),
        dict(id='pathos', word='Pathos', ipa='ˈpeɪ.θɒs',
             def_='an appeal to the audience\'s emotions',
             ex='The charity advert used images of suffering to evoke <b>pathos</b>.'),
        dict(id='logos', word='Logos', ipa='ˈlɒɡ.ɒs',
             def_='an appeal to reason or logic using facts and evidence',
             ex='The statistics in the presentation provided strong <b>logos</b>.'),
        dict(id='assertion', word='Assertion', ipa='əˈsɜː.ʃən',
             def_='a confident and forceful statement of fact or belief',
             ex='The opening <b>assertion</b> of the essay sets out the central argument.'),
        dict(id='refutation', word='Refutation', ipa='ˌref.jʊˈteɪ.ʃən',
             def_='the action of proving an argument or theory wrong',
             ex='The second paragraph offers a thorough <b>refutation</b> of the opposing view.'),
        dict(id='anaphora', word='Anaphora', ipa='əˈnæf.ər.ə',
             def_='repetition of a word or phrase at the beginning of successive clauses',
             ex='"We shall fight... we shall never surrender" uses <b>anaphora</b>.'),
        dict(id='parallelism', word='Parallelism', ipa='ˈpær.ə.lel.ɪ.z əm',
             def_='using the same grammatical structure in successive clauses for emphasis',
             ex='"I came, I saw, I conquered" demonstrates <b>parallelism</b>.'),
        dict(id='hedging', word='Hedging', ipa='ˈhedʒ.ɪŋ',
             def_='using cautious language to soften or qualify a claim',
             ex='"This may suggest..." uses <b>hedging</b> to avoid overstatement.'),
        dict(id='polemic', word='Polemic', ipa='pəˈlem.ɪk',
             def_='a strong written or spoken attack on a particular opinion or practice',
             ex='The pamphlet was a fierce <b>polemic</b> against corporate greed.'),
    ]
),

'c2/precision-vocabulary': dict(
    level='c2', slug='precision-vocabulary', title='Precision Vocabulary',
    subtitle='marginal · negligible · substantial · profound · tentative · categorical',
    num='V11',
    words=[
        dict(id='marginal', word='Marginal', ipa='ˈmɑː.dʒɪ.nəl',
             def_='of minor importance; very small in size or effect',
             ex='The improvement was <b>marginal</b> and did not justify the cost.'),
        dict(id='negligible', word='Negligible', ipa='ˈneɡ.lɪ.dʒɪ.bəl',
             def_='so small or unimportant as to be not worth considering',
             ex='The risk to the public is <b>negligible</b> at current exposure levels.'),
        dict(id='substantial', word='Substantial', ipa='səbˈstæn.ʃəl',
             def_='of considerable importance, size, or worth',
             ex='There is <b>substantial</b> evidence to support the theory.'),
        dict(id='profound', word='Profound', ipa='prəˈfaʊnd',
             def_='very great or intense; having deep meaning or insight',
             ex='The discovery had a <b>profound</b> impact on modern medicine.'),
        dict(id='tentative', word='Tentative', ipa='ˈten.tə.tɪv',
             def_='not definite or certain; done as a first attempt',
             ex='We reached a <b>tentative</b> agreement, subject to legal review.'),
        dict(id='provisional', word='Provisional', ipa='prəˈvɪʒ.ən.əl',
             def_='arranged for the present but likely to be changed',
             ex='The <b>provisional</b> results will be confirmed next week.'),
        dict(id='definitive', word='Definitive', ipa='dɪˈfɪn.ɪ.tɪv',
             def_='done or reached decisively and with authority; final',
             ex='This is the <b>definitive</b> account of the conflict.'),
        dict(id='explicit', word='Explicit', ipa='ɪkˈsplɪs.ɪt',
             def_='stated clearly and in detail, leaving no room for confusion',
             ex='The terms of the contract are <b>explicit</b> about liability.'),
        dict(id='implicit', word='Implicit', ipa='ɪmˈplɪs.ɪt',
             def_='suggested though not directly expressed',
             ex='There was an <b>implicit</b> assumption that the deadline would be met.'),
        dict(id='categorical', word='Categorical', ipa='ˌkæt.əˈɡɒr.ɪ.kəl',
             def_='unconditional and absolute; allowing no exceptions',
             ex='The minister gave a <b>categorical</b> denial of any wrongdoing.'),
    ]
),

'c2/spoken-written-modes': dict(
    level='c2', slug='spoken-written-modes', title='Spoken vs Written Modes',
    subtitle='hedging · ellipsis · deixis · mode continuum · prosody · register shift',
    num='V12',
    words=[
        dict(id='hedging', word='Hedging', ipa='ˈhedʒ.ɪŋ',
             def_='using cautious language to qualify statements and avoid overcommitting',
             ex='"It seems that..." uses <b>hedging</b> to soften a claim.'),
        dict(id='ellipsis', word='Ellipsis', ipa='ɪˈlɪp.sɪs',
             def_='omitting words that can be inferred from context (more common in speech)',
             ex='"Coming?" instead of "Are you coming?" demonstrates <b>ellipsis</b>.'),
        dict(id='deixis', word='Deixis', ipa='ˈdaɪk.sɪs',
             def_='words that only make sense with reference to time, place, or person',
             ex='"Here", "now", and "this" are examples of <b>deixis</b>.'),
        dict(id='mode_continuum', word='Mode continuum', ipa='məʊd kənˈtɪn.ju.əm',
             def_='a scale from casual spoken language to formal written language',
             ex='A text message sits at the informal end of the <b>mode continuum</b>.'),
        dict(id='prosody', word='Prosody', ipa='ˈprɒz.ə.di',
             def_='the patterns of rhythm, stress, and intonation in spoken language',
             ex='<b>Prosody</b> changes meaning: "I didn\'t SAY it" vs "I didn\'t say IT".'),
        dict(id='register_shift', word='Register shift', ipa='ˈredʒ.ɪ.stər ʃɪft',
             def_='deliberately moving between formal and informal language for effect',
             ex='Comedy often uses <b>register shift</b>, mixing slang with formal diction.'),
        dict(id='colloquialism', word='Colloquialism', ipa='kəˈləʊ.kwi.ə.lɪ.z əm',
             def_='informal language or expressions used in everyday conversation',
             ex='"Gonna" and "wanna" are common <b>colloquialisms</b> in spoken English.'),
        dict(id='vagueness', word='Vagueness', ipa='ˈveɪɡ.nəs',
             def_='deliberate imprecision used in speech to maintain social harmony',
             ex='"Sort of", "kind of" and "thingy" are vagueness devices that signal <b>vagueness</b>.'),
        dict(id='intonation', word='Intonation', ipa='ˌɪn.təˈneɪ.ʃən',
             def_='the rise and fall of the voice in speech to convey meaning',
             ex='Rising <b>intonation</b> at the end of a sentence signals a question.'),
        dict(id='formality', word='Formality', ipa='fɔːˈmæl.ɪ.ti',
             def_='the quality of following established conventions of language and behaviour',
             ex='A job application requires a high degree of linguistic <b>formality</b>.'),
    ]
),

}


# ── HTML generators ──────────────────────────────────────────────────────────

def slides_html(ch):
    level = ch['level']
    slug = ch['slug']
    title = ch['title']
    subtitle = ch['subtitle']
    words = ch['words']
    lv_upper = level.upper()
    lv_path = {'c1': 'c/c1', 'c2': 'c/c2'}[level]
    depth = '../../../../'

    # Build word-overview slides (groups of 4)
    slides = []
    for i in range(0, len(words), 4):
        group = words[i:i+4]
        start = i + 1
        end = min(i + 4, len(words))
        label = f'Words {start}–{end}' if end > start else f'Word {start}'

        rows = '\n'.join(
            f'<div class="overview-row">'
            f'<div class="overview-label">{w["word"]}</div>'
            f'<div class="overview-desc">{w["def_"]}</div>'
            f'</div>'
            for w in group
        )
        examples = '\n'.join(
            f'<div style="font-size:.88rem;color:var(--muted);padding:4px 0;font-style:italic">'
            f'{w["ex"]}</div>'
            for w in group[:2]
        )
        slides.append(
            f'<div class="slide"><div class="slide-card">'
            f'<div class="slide-header"><h2>{label}</h2></div>'
            f'{rows}'
            f'<div style="margin-top:14px;padding-top:10px;border-top:1px solid var(--hairline)">'
            f'<div style="font-family:var(--font-sans);font-size:.65rem;font-weight:800;'
            f'letter-spacing:1px;text-transform:uppercase;color:var(--muted);margin-bottom:6px">'
            f'Examples</div>'
            f'{examples}'
            f'</div>'
            f'</div></div>'
        )

    total = len(slides)
    slide_deck = '\n'.join(slides)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{depth}favicon.svg" type="image/svg+xml">
<title>{lv_upper} Vocab · {title} — Lesson | Word Play</title>
<link rel="stylesheet" href="{depth}shared/base.css?v={V['base']}">
<link rel="stylesheet" href="{depth}shared/slides.css?v={V['slides']}">
<script src="{depth}shared/dark-init.js?v={V['dark_init']}"></script>
</head><body class="deck-body">
<div class="deck-progress"><div class="deck-progress-fill" id="deck-progress-fill"></div></div>
<header class="site-header"><div class="site-header-inner"><a href="index.html" class="back back-link" aria-label="Back"></a>
  <a href="{depth}index.html" class="brand">{WP_SVG}Word Play</a>
  <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">&#9680; Dark</button>
</div></header>
<div class="container">
  <div class="breadcrumb"><a href="{depth}index.html">Home</a><span>&#8250;</span><a href="{depth}{lv_path}/index.html">{lv_upper}</a><span>&#8250;</span><a href="../index.html">Vocabulary</a><span>&#8250;</span><a href="index.html">{title}</a></div>
  <div class="chapter-num">Vocabulary</div>
  <h1>{title}</h1>
  <p class="chapter-subtitle">{subtitle}</p>
  <nav class="chapter-nav">
    <a href="index.html" class="chapter-nav-btn">Flashcards</a>
    <a href="slides.html" class="chapter-nav-btn active">Lesson</a>
    <a href="game.html" class="chapter-nav-btn">Game</a>
  </nav>
  <div id="slide-deck">
{slide_deck}
  </div>
  <div class="deck-nav">
    <button class="deck-btn" onclick="prevSlide()" id="deck-prev" disabled>&#8592; Prev</button>
    <span class="deck-counter" id="slide-counter">1 / {total}</span>
    <button class="deck-btn primary" onclick="nextSlide()" id="deck-next">Next &#8594;</button>
  </div>
</div>
<footer class="site-footer">Word Play · Cambridge English A1&#8594;C2</footer>
<script src="{depth}shared/store.js?v={V['store']}"></script>
<script>window.LEVEL="{level}";window.CHAPTER_ID="{slug}";</script>
<script src="{depth}shared/deck.js?v={V['deck']}"></script>
<script>
(function() {{
  var dk = document.getElementById('slide-deck');
  if (dk) setTimeout(function() {{ dk.scrollIntoView({{ behavior: 'smooth', block: 'start' }}); }}, 150);
}})();
try {{
  localStorage.setItem('wordplay_last_chapter_{level}', JSON.stringify({{
    slug: '{slug}', section: 'vocabulary', title: '{title}', page: 'slides.html'
  }}));
}} catch(e) {{}}
</script>
</body>
</html>'''


def flashcards_html(ch):
    level = ch['level']
    slug = ch['slug']
    title = ch['title']
    subtitle = ch['subtitle']
    num = ch['num']
    words = ch['words']
    lv_upper = level.upper()
    lv_path = {'c1': 'c/c1', 'c2': 'c/c2'}[level]
    depth = '../../../../'

    mastery_key = f'wordplay_vocab_{level}_{slug}_mastered'
    notes_key = f'wp_notes_{level}_{slug}'

    words_json = json.dumps([
        {'id': w['id'], 'word': w['word'], 'def': w['def_'], 'ipa': w['ipa'], 'ex': w['ex']}
        for w in words
    ], ensure_ascii=False)

    count = len(words)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{depth}favicon.svg" type="image/svg+xml">
<title>{lv_upper} Vocab · {title} — Flashcards | Word Play</title>
<link rel="stylesheet" href="{depth}shared/base.css?v={V['base']}">
<link rel="stylesheet" href="{depth}shared/game.css?v={V['game']}">
<script src="{depth}shared/dark-init.js?v={V['dark_init']}"></script>
<style>
.vocab-page{{max-width:800px;margin:0 auto;padding:20px 0}}
.mode-tabs{{display:flex;gap:8px;margin-bottom:24px;flex-wrap:wrap}}
.mode-tab{{font-family:var(--font-sans);font-size:.72rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:8px 16px;border-radius:4px;cursor:pointer;border:1.5px solid var(--hairline);background:transparent;color:var(--ink);transition:all .15s}}
.mode-tab.active{{background:var(--ink);color:var(--paper);border-color:var(--ink)}}
.flashcard-wrap{{perspective:800px;margin:0 auto 20px;max-width:480px}}
.flashcard{{width:100%;height:220px;position:relative;transform-style:preserve-3d;transition:transform .5s;cursor:pointer;border-radius:10px}}
.flashcard.flipped{{transform:rotateY(180deg)}}
.fc-face{{position:absolute;inset:0;backface-visibility:hidden;border-radius:10px;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:20px;text-align:center;border:1px solid var(--hairline)}}
.fc-front{{background:var(--paper)}}
.fc-back{{background:var(--paper);transform:rotateY(180deg)}}
.fc-word{{font-size:1.6rem;font-weight:700;color:var(--ink);margin-bottom:6px}}
.fc-def{{font-size:.95rem;color:var(--ink);margin-bottom:8px}}
.fc-ex{{font-size:.85rem;color:var(--muted);font-style:italic}}
.fc-hint{{font-family:var(--font-sans);font-size:.65rem;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-top:12px}}
.fc-audio-btn{{background:none;border:1px solid var(--hairline);border-radius:4px;
  padding:5px 12px;font-family:var(--font-sans);font-size:.65rem;font-weight:700;
  letter-spacing:1px;text-transform:uppercase;color:var(--muted);cursor:pointer;margin-top:10px}}
.fc-audio-btn:hover{{border-color:var(--amber);color:var(--amber)}}
.fc-nav{{display:flex;align-items:center;gap:16px;justify-content:center;margin-bottom:20px}}
.fc-btn{{font-family:var(--font-sans);font-size:.72rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:9px 18px;border-radius:4px;cursor:pointer;border:1.5px solid var(--hairline);background:transparent;color:var(--ink)}}
.fc-btn.primary{{background:var(--ink);color:var(--paper);border-color:var(--ink)}}
.fc-counter{{font-family:var(--font-sans);font-size:.75rem;color:var(--muted);font-weight:600}}
.match-grid{{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:20px}}
.match-col{{display:flex;flex-direction:column;gap:8px}}
.match-item{{padding:12px 14px;border:1.5px solid var(--hairline);border-radius:6px;cursor:pointer;font-size:.88rem;color:var(--ink);transition:border-color .15s,background .15s;user-select:none}}
.match-item.selected{{border-color:var(--amber);background:rgba(184,134,11,.08)}}
.match-item.correct{{border-color:var(--green);background:rgba(46,125,82,.08);pointer-events:none}}
.match-item.wrong{{border-color:var(--red);background:rgba(192,57,43,.08)}}
.mastery-badge{{display:inline-block;padding:8px 18px;background:rgba(184,134,11,.12);color:var(--amber);font-family:var(--font-sans);font-size:.78rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;border-radius:4px;margin-bottom:16px}}
.word-list-item{{display:flex;align-items:baseline;gap:12px;padding:10px 0;border-bottom:1px solid var(--hairline)}}
.wl-word{{font-weight:700;font-size:1rem;min-width:180px}}
.wl-def{{font-size:.88rem;color:var(--ink)}}
</style>
</head>
<body>
<header class="site-header">
  <div class="site-header-inner">
    <a href="../index.html" class="back back-link" aria-label="Back"></a>
    <a href="{depth}index.html" class="brand">{WP_SVG}Word Play</a>
    <button class="dark-toggle" aria-label="Toggle dark mode" onclick="toggleDark()">&#9680; Dark</button>
  </div>
</header>
<div class="container">
  <div class="breadcrumb">
    <a href="{depth}index.html">Home</a><span>&#8250;</span>
    <a href="{depth}{lv_path}/index.html">{lv_upper}</a><span>&#8250;</span>
    <a href="../index.html">Vocabulary</a><span>&#8250;</span>
    <strong>{title}</strong>
  </div>
  <div class="chapter-num">{num}</div>
  <h1>{title}</h1>
  <nav class="chapter-nav">
    <a href="index.html" class="chapter-nav-btn active">Flashcards</a>
    <a href="slides.html" class="chapter-nav-btn">Lesson</a>
    <a href="game.html" class="chapter-nav-btn">Game</a>
  </nav>

  <div class="vocab-page">
    <div id="masteryBadge" style="margin:12px 0;display:none"><span class="mastery-badge">Topic mastered</span></div>
    <div style="font-family:var(--font-sans);font-size:.75rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:var(--muted);margin-bottom:16px">{count} words &middot; tap card to reveal</div>

    <div class="mode-tabs">
      <button class="mode-tab active" onclick="setMode(\'flash\',this)">Flashcards</button>
      <button class="mode-tab" onclick="setMode(\'match\',this)">Match</button>
      <button class="mode-tab" onclick="setMode(\'list\',this)">Word list</button>
    </div>

    <div id="modeFlash">
      <div class="flashcard-wrap">
        <div class="flashcard" id="flashcard" onclick="flipCard()">
          <div class="fc-face fc-front">
            <div class="fc-word" id="fcWord"></div>
            <div class="fc-hint">tap to reveal</div>
            <button class="fc-audio-btn" onclick="speakWord(event)">&#9654; Pronounce</button>
          </div>
          <div class="fc-face fc-back">
            <div class="fc-def" id="fcDef"></div>
            <div class="fc-ex" id="fcEx"></div>
          </div>
        </div>
      </div>
      <div class="fc-nav">
        <button class="fc-btn" onclick="fcPrev()">&#8592; Prev</button>
        <span class="fc-counter" id="fcCounter"></span>
        <button class="fc-btn" onclick="fcNext()">Next &#8594;</button>
      </div>
      <div style="text-align:center">
        <button class="fc-btn primary" onclick="markMastered()" id="btnMastered">Mark topic as mastered</button>
      </div>
    </div>

    <div id="modeMatch" style="display:none">
      <div class="match-score" id="matchScore">Match each word to its definition</div>
      <div class="match-grid">
        <div class="match-col" id="matchWords"></div>
        <div class="match-col" id="matchDefs"></div>
      </div>
      <div style="text-align:center">
        <button class="fc-btn" onclick="initMatch()">New round</button>
      </div>
    </div>

    <div id="modeList" style="display:none">
      <div id="wordList"></div>
    </div>
  </div>
</div>
<footer class="site-footer">Word Play · Cambridge English A1&#8594;C2</footer>
<script src="{depth}shared/store.js?v={V['store']}"></script>
<script>
var SLUG = '{slug}';
var LEVEL = '{level}';
var MASTERY_KEY = '{mastery_key}';
var WORDS = {words_json};
var fcIdx = 0, flipped = false;

function setMode(mode, btn) {{
  document.querySelectorAll('.mode-tab').forEach(function(b){{b.classList.remove('active');}});
  btn.classList.add('active');
  document.getElementById('modeFlash').style.display = mode==='flash'?'':'none';
  document.getElementById('modeMatch').style.display = mode==='match'?'':'none';
  document.getElementById('modeList').style.display = mode==='list'?'':'none';
  if(mode==='match') initMatch();
  if(mode==='list') renderList();
}}

function flipCard(){{
  flipped=!flipped;
  document.getElementById('flashcard').classList.toggle('flipped',flipped);
}}

function showCard(idx){{
  flipped=false;
  document.getElementById('flashcard').classList.remove('flipped');
  var w=WORDS[idx];
  document.getElementById('fcWord').textContent=w.word;
  document.getElementById('fcDef').textContent=w.def;
  document.getElementById('fcEx').innerHTML=w.ex||'';
  document.getElementById('fcCounter').textContent=(idx+1)+' / '+WORDS.length;
  fcSeen.add(idx);
  if (!mastered && fcSeen.size >= WORDS.length) {{ mastered = true; setTimeout(markMastered, 700); }}
}}

function fcNext(){{fcIdx=(fcIdx+1)%WORDS.length;showCard(fcIdx);}}
function fcPrev(){{fcIdx=(fcIdx-1+WORDS.length)%WORDS.length;showCard(fcIdx);}}

function speakWord(e) {{
  if (e) e.stopPropagation();
  if (!window.speechSynthesis) return;
  var utt = new SpeechSynthesisUtterance(WORDS[fcIdx].word);
  utt.lang = 'en-GB'; utt.rate = 0.9;
  window.speechSynthesis.cancel();
  window.speechSynthesis.speak(utt);
}}

function markMastered(){{
  try{{localStorage.setItem(MASTERY_KEY,'1');}}catch(e){{}}
  document.getElementById('masteryBadge').style.display='block';
  var btn=document.getElementById('btnMastered');
  btn.textContent='Mastered!'; btn.disabled=true;
  if(window.FCEStore){{FCEStore.saveResult(SLUG,1,1,{{}});}}
}}

function checkMastered(){{
  try{{
    if(localStorage.getItem(MASTERY_KEY)==='1'){{
      document.getElementById('masteryBadge').style.display='block';
      var btn=document.getElementById('btnMastered');
      btn.textContent='Mastered!'; btn.disabled=true;
    }}
  }}catch(e){{}}
}}

var matchSelected=null;
function shuffle(a){{var b=a.slice();for(var i=b.length-1;i>0;i--){{var j=Math.floor(Math.random()*(i+1));var t=b[i];b[i]=b[j];b[j]=t;}}return b;}}

function initMatch(){{
  var sample=shuffle(WORDS).slice(0,6);
  var words=shuffle(sample.map(function(w){{return{{id:w.word,text:w.word,type:'word'}};}}));
  var defs=shuffle(sample.map(function(w){{return{{id:w.word,text:w.def,type:'def'}};}}));
  matchSelected=null;
  document.getElementById('matchScore').textContent='Match each word to its definition';
  function renderCol(col,items){{
    col.innerHTML='';
    items.forEach(function(item){{
      var el=document.createElement('div');
      el.className='match-item'; el.textContent=item.text;
      el.dataset.id=item.id; el.dataset.type=item.type;
      el.addEventListener('click',handleMatch);
      col.appendChild(el);
    }});
  }}
  renderCol(document.getElementById('matchWords'),words);
  renderCol(document.getElementById('matchDefs'),defs);
}}

function handleMatch(e){{
  var el=e.currentTarget;
  if(el.classList.contains('correct')) return;
  if(!matchSelected){{
    if(matchSelected&&matchSelected!==el) matchSelected.classList.remove('selected');
    matchSelected=el; el.classList.add('selected');
  }}else{{
    var prev=matchSelected; matchSelected=null;
    var correct=prev.dataset.id===el.dataset.id&&prev.dataset.type!==el.dataset.type;
    if(correct){{
      prev.classList.remove('selected'); prev.classList.add('correct');
      el.classList.add('correct');
      var remaining=document.querySelectorAll('.match-item:not(.correct)').length;
      if(remaining===0) {{ document.getElementById('matchScore').textContent='All matched!'; completedRounds++; if (!mastered && completedRounds >= 5) {{ mastered = true; setTimeout(markMastered, 700); }} }}
    }}else{{
      prev.classList.remove('selected');
      prev.classList.add('wrong'); el.classList.add('wrong');
      setTimeout(function(){{prev.classList.remove('wrong');el.classList.remove('wrong');}},600);
    }}
  }}
}}

function renderList(){{
  var html=WORDS.map(function(w){{
    return '<div class="word-list-item"><span class="wl-word">'+w.word+'</span><span class="wl-def">'+w.def+'</span></div>';
  }}).join('');
  document.getElementById('wordList').innerHTML=html;
}}

var mastered = false;
var fcSeen = new Set();
var completedRounds = 0;
showCard(0);
checkMastered();
</script>
<div style="margin-top:24px;border-top:1px solid var(--hairline);padding-top:20px">
  <div style="font-family:var(--font-sans);font-size:.65rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--muted);margin-bottom:8px">My notes &amp; examples</div>
  <textarea id="my-notes-area" maxlength="500" placeholder="Write your own example sentence, a memory trick, or a note in your language…" style="width:100%;min-height:80px;padding:10px 12px;font-family:Georgia,serif;font-size:.88rem;color:var(--ink);background:var(--paper);border:1.5px solid var(--hairline);border-radius:6px;resize:vertical;line-height:1.6;box-sizing:border-box"></textarea>
  <div style="font-family:var(--font-sans);font-size:.65rem;color:var(--muted);margin-top:4px;text-align:right"><span id="notes-chars">0</span>/500 · auto-saved</div>
</div>
<script>
(function(){{
  var ta = document.getElementById('my-notes-area');
  var cc = document.getElementById('notes-chars');
  if (!ta) return;
  var KEY = '{notes_key}';
  try {{ ta.value = localStorage.getItem(KEY) || ''; cc.textContent = ta.value.length; }} catch(e){{}}
  var t;
  ta.addEventListener('input', function() {{
    cc.textContent = ta.value.length;
    clearTimeout(t);
    t = setTimeout(function() {{
      try {{ localStorage.setItem(KEY, ta.value); }} catch(e) {{}}
    }}, 600);
  }});
}})();
</script>
</body>
</html>'''


def patch_game_items(path, ch):
    """Replace the placeholder items array in game.html with real items."""
    with open(path, encoding='utf-8') as f:
        content = f.read()

    words = ch['words']
    items = []
    for w in words:
        # Build a gap-fill from the example sentence
        ex_text = re.sub(r'<[^>]+>', '', w['ex'])  # strip tags for completion
        completion = ex_text.replace(w['word'], '______')
        items.append({
            'id': w['id'],
            'term': w['word'],
            'meaning': w['def_'],
            'synonym': w['ipa'],
            'example': w['ex'],
            'completion': completion,
            'answer': w['word'],
        })

    items_json = json.dumps(items, ensure_ascii=False, indent=2)
    # Replace the placeholder items block
    new_items = f'items:\n{items_json}'

    # Match both placeholder and existing items patterns
    content = re.sub(
        r'items:\s*\[[\s\S]*?\](?=\s*\})',
        new_items,
        content,
        count=1
    )
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    results = []
    for key, ch in CHAPTERS.items():
        level = ch['level']
        slug = ch['slug']
        chapter_dir = os.path.join(ROOT, 'c', level, 'vocabulary', slug)

        if not os.path.isdir(chapter_dir):
            results.append(f'SKIP (no dir): {key}')
            continue

        # slides.html — full replacement
        slides_path = os.path.join(chapter_dir, 'slides.html')
        with open(slides_path, 'w', encoding='utf-8') as f:
            f.write(slides_html(ch))
        results.append(f'  slides.html  → {key}')

        # flashcards.html — full replacement
        fc_path = os.path.join(chapter_dir, 'flashcards.html')
        with open(fc_path, 'w', encoding='utf-8') as f:
            f.write(flashcards_html(ch))
        results.append(f'  flashcards   → {key}')

        # game.html — patch items only
        game_path = os.path.join(chapter_dir, 'game.html')
        if os.path.exists(game_path):
            patch_game_items(game_path, ch)
            results.append(f'  game items   → {key}')
        else:
            results.append(f'  SKIP game (not found): {key}')

    for r in results:
        print(r)
    print(f'\nDone: {len(CHAPTERS)} chapters processed.')


if __name__ == '__main__':
    main()
