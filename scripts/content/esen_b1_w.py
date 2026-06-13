# -*- coding: utf-8 -*-
"""espanol-en B1 writing content — 8 chapters (W1-W8)."""

CHAPTERS = {

'formal-email': dict(
  num='W1', short='A Formal Email', title='Writing a Formal Email — Un Correo Formal',
  subtitle='Salutations, stating your purpose, making requests, signing off',
  slides=[
    ('The shape of a formal email', None,
     '<p class="slide-explanation">A formal email has five clear parts: salutation → purpose → body (reason / request / information) → next step → closing.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Estimada señora Gómez:</b> (salutation)</p>'
     '<p style="margin-top:8px"><b>Me dirijo a usted para solicitar información sobre el curso.</b> (purpose)</p>'
     '<p style="margin-top:8px"><b>Estoy interesado en la modalidad presencial...</b> (body)</p>'
     '<p style="margin-top:8px"><b>Quedo a su disposición para cualquier consulta.</b> (next step)</p>'
     '<p style="margin-top:8px"><b>Atentamente, Carlos Ruiz.</b> (closing)</p></div>'),
    ('Salutations', None,
     '<p class="slide-explanation">Use <b>Estimado/a</b> + title/name for formal emails. Never ¡Hola! or Querido/a.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Estimado señor López: · Estimada señora Gómez:</b></p>'
     '<p style="margin-top:8px"><b>A quien corresponda:</b> (To whom it may concern)</p>'
     '<p style="margin-top:8px"><b>Me dirijo a usted...</b> (I am writing to you...) — formal first-person opening</p></div>'
     '<p style="margin-top:16px">Note the colon (<b>:</b>) after the salutation, not a comma.</p>'),
    ('Stating your purpose', None,
     '<p class="slide-explanation">Open the body with a clear statement of why you are writing.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Le escribo para solicitar / informarle / quejarme de…</b></p>'
     '<p style="margin-top:8px"><b>El motivo de este correo es…</b> (The reason for this email is…)</p>'
     '<p style="margin-top:8px"><b>Me pongo en contacto con usted para…</b> (I am getting in touch to…)</p></div>'),
    ('Making requests politely', None,
     '<p class="slide-explanation">Use <b>quisiera / me gustaría + infinitive</b> or <b>¿podría...?</b> for polite requests.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Quisiera solicitar una cita.</b> (I would like to request an appointment.)</p>'
     '<p style="margin-top:8px"><b>Me gustaría recibir más información.</b> (I would like to receive more information.)</p>'
     '<p style="margin-top:8px"><b>¿Podría enviarme el catálogo?</b> (Could you send me the catalogue?)</p></div>'),
    ('Closings', None,
     '<p class="slide-explanation">Close with a courteous availability phrase, then a formal sign-off.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Quedo a su disposición.</b> (I remain at your disposal.)</p>'
     '<p style="margin-top:8px"><b>En espera de sus noticias, …</b> (Awaiting your reply, …)</p>'
     '<p style="margin-top:8px"><b>Atentamente, · Un cordial saludo,</b></p></div>'),
  ],
  traps=[
    ('¡Hola, señora Gómez!', '<strong>Estimada señora Gómez:</strong>', 'Formal emails open with Estimado/a, never ¡Hola!'),
    ('Le escribo para solicitar el empleo de la semana pasada.', 'Le escribo <strong>en relación con</strong> el puesto anunciado.', 'State the topic precisely without slang or vague time phrases'),
    ('Quisiera que usted enviará el catálogo.', 'Quisiera que usted <strong>enviara</strong> el catálogo.', 'After quisiera que, the verb goes in the subjunctive (imperfecto: enviara)'),
    ('Un beso, María (formal email)', '<strong>Atentamente,</strong> María', 'Un beso is for friends — formal emails close with Atentamente or Un cordial saludo'),
    ('Gracias de antemano. (no follow-up phrase)', 'Quedo a su <strong>disposición</strong>. Atentamente,', 'Always offer to follow up before the sign-off in a formal context'),
  ],
  summary=[
    ('Salutation', 'Estimado/a + señor/a + surname:', 'Estimada señora Gómez:'),
    ('Opening', 'Me dirijo a usted para… / Le escribo para…', 'Le escribo para solicitar información.'),
    ('Polite request', 'Quisiera / Me gustaría + inf', 'Quisiera concertar una cita.'),
    ('Question', '¿Podría + inf?', '¿Podría enviarme el programa?'),
    ('Availability', 'Quedo a su disposición.', 'Quedo a su disposición para cualquier consulta.'),
    ('Close', 'Atentamente, / Un cordial saludo,', 'Atentamente, Carlos Ruiz.'),
  ],
  ex1=('Choose the right option', 'Tap the best option for each gap in the formal email.', [
    ('______ señora Martínez:', ['Estimada', 'Querida', 'Hola'], 'Estimada',
     'Estimada is the formal salutation for a woman. Querida and Hola are informal.'),
    ('Le escribo ______ solicitar información sobre el puesto.', ['para', 'por', 'de'], 'para',
     'Purpose uses para + infinitive: Le escribo para solicitar…'),
    ('______ recibir el catálogo de precios.', ['Quisiera', 'Quiero', 'Querría que'], 'Quisiera',
     'Quisiera is the conditionally polite form: I would like. Quiero is too direct for formal.'),
    ('¿______ enviarme los detalles del curso?', ['Podría', 'Puede', 'Podrías'], 'Podría',
     '¿Podría…? addresses usted politely. Podrías is informal tú.'),
    ('Quedo a su ______ para cualquier consulta.', ['disposición', 'disposición que', 'información'], 'disposición',
     'Fixed phrase: Quedo a su disposición — I remain at your disposal.'),
    ('______ , Ana García.', ['Atentamente', 'Un abrazo', 'Un beso'], 'Atentamente',
     'Formal closing: Atentamente or Un cordial saludo. Un abrazo/beso are informal.'),
  ]),
  ex2=('Complete the formal phrase', 'Type the missing word — no accents needed.', [
    ('______ señor Pérez: (formal salutation, male)', 'estimado',
     'Estimado señor Pérez: — the formal opening for a man.'),
    ('Me ______ a usted para quejarme del servicio. (I am writing to you)', 'dirijo',
     'Me dirijo a usted para… — I am addressing/writing to you to…'),
    ('Quisiera ______ una cita para la semana próxima. (request)', 'concertar',
     'Concertar una cita = to arrange an appointment — a formal collocation.'),
    ('¿Podría ______ me los documentos necesarios? (send)', 'enviar',
     '¿Podría enviarme…? = Could you send me…? — polite formal request.'),
    ('______ a su disposición para lo que necesite.', 'quedo',
     'Quedo a su disposición = I remain at your disposal — the formal availability phrase.'),
  ]),
  ex3=('Formal or informal?', 'Choose the option that belongs in a formal email.', [
    ('Which opening is correct for a formal email?', ['Estimado señor Ruiz:', '¡Hola, señor Ruiz!', 'Querido señor Ruiz:'], 'Estimado señor Ruiz:',
     'Only Estimado/a is appropriate for formal emails. ¡Hola! and Querido/a are informal.'),
    ('Which phrase states your purpose formally?', ['Le escribo en relación con la oferta de trabajo.', 'Te escribo sobre el trabajo.', 'Oye, quería preguntarte lo del trabajo.'], 'Le escribo en relación con la oferta de trabajo.',
     'Le escribo uses usted (formal). Te escribo and oye are informal.'),
    ('Which is a polite formal request?', ['Quisiera recibir más información.', 'Dame información.', 'Quiero que me des información.'], 'Quisiera recibir más información.',
     'Quisiera + infinitive is the polite conditional. Dame is imperative; quiero que is direct.'),
    ('Which closing is formal?', ['Atentamente, Pilar Vega.', 'Un beso, Pilar.', 'Hasta pronto, Pilar.'], 'Atentamente, Pilar Vega.',
     'Atentamente + full name is standard for formal correspondence.'),
    ('Which availability phrase belongs at the end?', ['Quedo a su disposición para cualquier consulta.', 'Escríbeme pronto.', 'Nos vemos.'], 'Quedo a su disposición para cualquier consulta.',
     'Quedo a su disposición is formal. The other two are informal.'),
  ]),
  game_desc='Practise formal email language: identify the right phrase, use it in context, then produce it yourself. Reach 100 points to win.',
  items=[
    ('estimada', 'Estimado/a', 'Dear (formal salutation)', 'formal opening', '<b>Estimada</b> señora Gómez:', '______ señora Gómez: (Dear, formal)', 'estimada'),
    ('me-dirijo', 'me dirijo a usted', 'I am writing to you (formal)', 'purpose opener', '<b>Me dirijo a usted</b> para solicitar información.', '______ ______ ______ para solicitar información.', 'me dirijo a usted'),
    ('quisiera', 'quisiera', 'I would like (polite)', 'polite request', '<b>Quisiera</b> concertar una cita.', '______ concertar una cita. (I would like)', 'quisiera'),
    ('podria', '¿podría?', 'could you? (formal)', 'polite question', '¿<b>Podría</b> enviarme el catálogo?', '¿______ enviarme el catálogo? (Could you)', 'podria'),
    ('quedo', 'quedo a su disposición', 'I remain at your disposal', 'formal availability', '<b>Quedo a su disposición</b> para cualquier consulta.', '______ a su disposición para cualquier consulta.', 'quedo'),
    ('atentamente', 'Atentamente', 'Yours faithfully / sincerely', 'formal close', '<b>Atentamente,</b> Carlos Ruiz.', '______ , Carlos Ruiz. (formal sign-off)', 'atentamente'),
    ('en-relacion', 'en relación con', 'regarding, in connection with', 'topic phrase', 'Le escribo <b>en relación con</b> su anuncio.', 'Le escribo ______ ______ ______ su anuncio.', 'en relacion con'),
    ('en-espera', 'en espera de sus noticias', 'awaiting your reply', 'closing phrase', '<b>En espera de sus noticias,</b> le saluda atentamente.', '______ ______ ______ ______ , le saluda atentamente.', 'en espera'),
  ],
  ref_rows=[
    ('Salutation', 'Estimado señor / Estimada señora + surname: · A quien corresponda:'),
    ('Open', 'Me dirijo a usted para… · Le escribo en relación con… · El motivo de este correo es…'),
    ('Polite request', 'Quisiera + inf · Me gustaría + inf · ¿Podría + inf?'),
    ('Information', 'Le comunico que… · Le informo de que…'),
    ('Availability', 'Quedo a su disposición. · En espera de sus noticias,'),
    ('Close', 'Atentamente, · Un cordial saludo, + full name'),
  ],
  task='Write a formal email in Spanish (55–70 words) to the director of a language school: greet formally, state you are writing to request information about a B1 Spanish course, ask about price and schedule, say you would also like to visit the school, close with an availability phrase and a formal sign-off.',
  model='Estimado señor Navarro:\n\nMe dirijo a usted para solicitar información sobre el curso de español B1 que ofrecen. Quisiera saber el precio, el horario y la fecha de inicio. Además, me gustaría visitar la escuela antes de matricularme. ¿Podría indicarme cuándo sería posible?\n\nQuedo a su disposición para cualquier consulta.\n\nAtentamente,\nLaura Sánchez.',
),

'opinion-essay': dict(
  num='W2', short='An Opinion Essay', title='Writing an Opinion Essay — Un Ensayo de Opinión',
  subtitle='Stating a view, supporting it with reasons, using connectors',
  slides=[
    ('The shape of an opinion essay', None,
     '<p class="slide-explanation">A B1 opinion essay has three parts: introduction (state your view) → body (two or three reasons with examples) → conclusion (summarise).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Introducción:</b> En mi opinión, el transporte público debería ser gratuito.</p>'
     '<p style="margin-top:8px"><b>Cuerpo:</b> En primer lugar, reduciría la contaminación. Además, ayudaría a las familias con menos recursos. Sin embargo, necesita financiación.</p>'
     '<p style="margin-top:8px"><b>Conclusión:</b> En definitiva, creo que los beneficios superan los inconvenientes.</p></div>'),
    ('Giving your opinion', None,
     '<p class="slide-explanation">Use a variety of opinion phrases — not just <em>creo que</em> every time.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>En mi opinión, … · A mi parecer, … · Desde mi punto de vista, …</b></p>'
     '<p style="margin-top:8px"><b>Creo / Pienso / Considero que…</b></p>'
     '<p style="margin-top:8px"><b>Estoy (totalmente) de acuerdo con… · No estoy de acuerdo con…</b></p></div>'),
    ('Connectors for essays', None,
     '<p class="slide-explanation">Good connectors show the examiner you can organise ideas.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Sequence:</b> En primer lugar / primero… · En segundo lugar / además… · Por último…</p>'
     '<p style="margin-top:8px"><b>Contrast:</b> Sin embargo, · No obstante, · Aunque + subjunctive/indicative</p>'
     '<p style="margin-top:8px"><b>Cause:</b> porque · ya que · debido a que · puesto que</p>'
     '<p style="margin-top:8px"><b>Conclusion:</b> En definitiva, · En conclusión, · Por tanto,</p></div>'),
    ('Giving reasons and examples', None,
     '<p class="slide-explanation">Support every opinion with a reason (because...) and ideally an example.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>…ya que reduce la contaminación.</b> (…since it reduces pollution.)</p>'
     '<p style="margin-top:8px"><b>Por ejemplo, en muchas ciudades europeas…</b> (For example, in many European cities…)</p>'
     '<p style="margin-top:8px"><b>…como ocurre en Suecia.</b> (…as is the case in Sweden.)</p></div>'),
    ('Conceding a point', None,
     '<p class="slide-explanation">Acknowledge the other side briefly — it shows balanced thinking.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Es verdad que… sin embargo…</b> (It is true that… however…)</p>'
     '<p style="margin-top:8px"><b>Aunque tiene algunas desventajas, creo que…</b></p>'
     '<p style="margin-top:8px"><b>A pesar de que…, sigo creyendo que…</b> (Despite the fact that…, I still believe that…)</p></div>'),
  ],
  traps=[
    ('Pienso que el trabajo es importante porque es bueno.', 'Pienso que el trabajo es importante <strong>ya que</strong> proporciona independencia económica.', 'Give a real reason, not circular logic — use ya que / debido a que'),
    ('Sin embargo el transporte público es mejor.', 'Sin embargo<strong>,</strong> el transporte público es mejor.', 'Sin embargo is always followed by a comma when it starts a sentence'),
    ('A mi opinión, …', '<strong>En mi opinión,</strong> …', 'The correct phrase is en mi opinión (not a mi opinión)'),
    ('Creo que debería a reducir.', 'Creo que debería <strong>reducir</strong>.', 'Deber + infinitive — no a between them (unlike ir a)'),
    ('También, el problema es grande.', '<strong>Además,</strong> el problema es grande.', 'También works mid-sentence; además opens a new argumentative point'),
  ],
  summary=[
    ('Opinion', 'En mi opinión, / Desde mi punto de vista,', 'En mi opinión, el deporte es esencial.'),
    ('Reason', 'porque / ya que / debido a que', '…ya que mejora la salud física y mental.'),
    ('Sequence', 'En primer lugar / Además / Por último', 'En primer lugar, es asequible.'),
    ('Contrast', 'Sin embargo, / Aunque', 'Sin embargo, tiene sus desventajas.'),
    ('Concede', 'Es verdad que… sin embargo…', 'Es verdad que cuesta dinero; sin embargo, los beneficios son mayores.'),
    ('Conclude', 'En definitiva, / En conclusión,', 'En definitiva, creo que los beneficios superan los inconvenientes.'),
  ],
  ex1=('Choose the right connector', 'Tap the best connector for each gap.', [
    ('______ , me gustan las ciudades grandes porque ofrecen más oportunidades.', ['En mi opinión', 'Sin embargo', 'Por tanto'], 'En mi opinión',
     'En mi opinión opens a personal view. Sin embargo contrasts; por tanto concludes.'),
    ('______ lugar, el transporte público reduce la contaminación.', ['primer', 'uno', 'uno de los'], 'primer',
     'En primer lugar sequences the first reason. The phrase is en primer lugar.'),
    ('El precio es alto. ______ , los beneficios son mayores.', ['Sin embargo', 'Además', 'Porque'], 'Sin embargo',
     'Sin embargo (however) introduces a contrasting point after an admitted problem.'),
    ('Es una buena idea ______ mejora la calidad de vida.', ['ya que', 'sin embargo', 'aunque'], 'ya que',
     'Ya que (since/because) introduces the reason directly after the claim.'),
    ('______ , creo que deberíamos invertir más en educación.', ['En definitiva', 'En primer lugar', 'Sin embargo'], 'En definitiva',
     'En definitiva (in short / all in all) is a conclusion connector.'),
    ('Es verdad que tiene inconvenientes; ______ , los beneficios son claros.', ['sin embargo', 'además', 'ya que'], 'sin embargo',
     'Conceding a point (es verdad que…) + contrasting (sin embargo…) = balanced argument.'),
  ]),
  ex2=('Complete the opinion phrase', 'Type the missing word — no accents needed.', [
    ('______ mi opinión, el medio ambiente es nuestra responsabilidad. (In)', 'en',
     'En mi opinión = in my opinion. The preposition is en, not a.'),
    ('Creo que el deporte es importante ______ mejora la salud. (because/since)', 'ya que',
     'Ya que (since) is a sophisticated alternative to porque in essay writing.'),
    ('En ______ lugar, hay que reducir el uso del coche.', 'primer',
     'En primer lugar = in the first place — the standard sequencer for a first reason.'),
    ('Es verdad que es caro; sin ______ , vale la pena.', 'embargo',
     'Sin embargo (however) — the most common contrast connector in Spanish essays.'),
    ('En ______ , considero que la tecnología nos ha cambiado la vida.', 'definitiva',
     'En definitiva = all in all / in short — the standard conclusion phrase.'),
  ]),
  ex3=('Essay structure', 'Choose the best option.', [
    ('Which sentence best introduces an opinion in an essay?', ['Desde mi punto de vista, las ciudades son más sostenibles que los pueblos.', 'Las ciudades son bonitas.', 'Me gustan las ciudades.'], 'Desde mi punto de vista, las ciudades son más sostenibles que los pueblos.',
     'Desde mi punto de vista + a claim with a reason is the standard essay opening.'),
    ('Which sentence best adds a reason?', ['Además, ya que es bueno.', 'El transporte público es mejor ya que reduce el tráfico y la contaminación.', 'Sin embargo, es una razón.'], 'El transporte público es mejor ya que reduce el tráfico y la contaminación.',
     'A clear claim + ya que + specific reason = a well-structured argument sentence.'),
    ('Which sentence concedes a point before a contrast?', ['Sin embargo, es caro.', 'Es verdad que puede ser costoso; sin embargo, los beneficios económicos son mayores.', 'En definitiva, es caro y sin embargo es mejor.'], 'Es verdad que puede ser costoso; sin embargo, los beneficios económicos son mayores.',
     'Es verdad que… + sin embargo… is the classic concession-contrast pattern.'),
    ('Which connector introduces a conclusion?', ['En primer lugar', 'Sin embargo', 'En definitiva'], 'En definitiva',
     'En definitiva signals the conclusion; the other two are body-paragraph connectors.'),
    ('Which phrase expresses disagreement politely?', ['No estoy de acuerdo con esa idea porque creo que la evidencia muestra lo contrario.', 'Eso es completamente falso.', 'Sin embargo no.'], 'No estoy de acuerdo con esa idea porque creo que la evidencia muestra lo contrario.',
     'No estoy de acuerdo con + reason = polite, argued disagreement in an essay.'),
  ]),
  game_desc='Practise the key phrases for opinion writing in Spanish. Reach 100 points to win.',
  items=[
    ('en-mi-opinion', 'en mi opinión', 'in my opinion', 'opinion opener', '<b>En mi opinión,</b> el deporte es esencial para la salud.', '______ ______ ______ , el deporte es esencial. (In my opinion)', 'en mi opinion'),
    ('ya-que', 'ya que', 'since, because (essay)', 'reason connector', 'Es una buena idea <b>ya que</b> reduce la contaminación.', 'Es una buena idea ______ ______ reduce la contaminación.', 'ya que'),
    ('primer-lugar', 'en primer lugar', 'in the first place', 'sequence', '<b>En primer lugar,</b> hay que invertir en educación.', '______ ______ ______ , hay que invertir en educación.', 'en primer lugar'),
    ('sin-embargo', 'sin embargo', 'however', 'contrast', '<b>Sin embargo,</b> el precio sigue siendo un problema.', '______ ______ , el precio sigue siendo un problema.', 'sin embargo'),
    ('es-verdad', 'es verdad que', 'it is true that', 'concession', '<b>Es verdad que</b> es caro; sin embargo, vale la pena.', '______ ______ ______ es caro; sin embargo, vale la pena.', 'es verdad'),
    ('en-definitiva', 'en definitiva', 'in short, all in all', 'conclusion', '<b>En definitiva,</b> creo que los beneficios superan los inconvenientes.', '______ ______ , creo que los beneficios superan los inconvenientes.', 'en definitiva'),
    ('desde-mi-punto', 'desde mi punto de vista', 'from my point of view', 'opinion', '<b>Desde mi punto de vista,</b> la tecnología nos ha cambiado la vida.', '______ ______ ______ ______ ______ , la tecnología nos ha cambiado la vida.', 'desde mi punto de vista'),
    ('a-pesar-de', 'a pesar de que', 'despite the fact that', 'concession-contrast', '<b>A pesar de que</b> es difícil, merece la pena intentarlo.', '______ ______ ______ ______ es difícil, merece la pena intentarlo.', 'a pesar de'),
  ],
  ref_rows=[
    ('Opinion', 'En mi opinión, / Desde mi punto de vista, / A mi parecer,'),
    ('Agree/disagree', 'Estoy de acuerdo con… / No estoy de acuerdo con…'),
    ('Reason', 'porque / ya que / debido a que / puesto que'),
    ('Sequence', 'En primer lugar, / Además, / Por último,'),
    ('Contrast', 'Sin embargo, / No obstante, / Aunque…'),
    ('Conclusion', 'En definitiva, / En conclusión, / Por tanto,'),
  ],
  task='Write a short opinion essay in Spanish (70–90 words) on the topic: "¿Es importante aprender idiomas extranjeros?" State your view, give two reasons with connectors, acknowledge one counterargument briefly, and conclude. Use at least three different connectors.',
  model='En mi opinión, aprender idiomas extranjeros es muy importante hoy en día. En primer lugar, nos permite comunicarnos con personas de otros países y entender otras culturas. Además, conocer otro idioma abre muchas puertas en el mundo laboral. Es verdad que aprender un idioma lleva tiempo y esfuerzo; sin embargo, los beneficios son enormes. En definitiva, creo que el esfuerzo merece la pena.',
),

'biography': dict(
  num='W3', short='A Biography', title='Writing a Biography — Una Biografía',
  subtitle='Using the past tense to describe a life: events and background',
  slides=[
    ('Indefinido vs imperfecto in a biography', None,
     '<p class="slide-explanation">In a biography you alternate between the <b>indefinido</b> (completed events: was born, studied, won) and the <b>imperfecto</b> (ongoing background: lived in, worked as, had a passion for).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Nació</b> en Madrid en 1932. (born — indefinido)</p>'
     '<p style="margin-top:8px"><b>Vivía</b> en un pequeño pueblo del norte. (background — imperfecto)</p>'
     '<p style="margin-top:8px"><b>Estudió</b> Medicina y <b>se graduó</b> en 1956. (events — indefinido)</p></div>'),
    ('Introducing the person', None,
     '<p class="slide-explanation">Open with birth, origin, and a brief character/context description.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Nació en + city + en + year.</b></p>'
     '<p style="margin-top:8px"><b>Era hijo/a de…</b> (He/She was the son/daughter of…)</p>'
     '<p style="margin-top:8px"><b>Desde pequeño/a, le apasionaba…</b> (From a young age, he/she was passionate about…)</p></div>'),
    ('Key life events', None,
     '<p class="slide-explanation">Use the indefinido for milestones: started, finished, married, moved, published, won.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Empezó a trabajar como… · Se casó con… · Se trasladó a…</b></p>'
     '<p style="margin-top:8px"><b>Publicó su primera novela en… · Ganó el premio… en…</b></p>'
     '<p style="margin-top:8px"><b>Falleció en + year.</b> (He/She passed away in…)</p></div>'),
    ('Describing achievements', None,
     '<p class="slide-explanation">Link achievements with connectors; use <b>gracias a</b> (thanks to) and <b>a lo largo de</b> (throughout).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Gracias a su trabajo, consiguió…</b> (Thanks to his work, he/she achieved…)</p>'
     '<p style="margin-top:8px"><b>A lo largo de su carrera, publicó más de veinte novelas.</b></p>'
     '<p style="margin-top:8px"><b>Se le conoce sobre todo por…</b> (He/She is best known for…)</p></div>'),
    ('Closing the biography', None,
     '<p class="slide-explanation">End with legacy or importance — use the present tense for ongoing impact.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Hoy en día se le considera uno de los grandes… (He/She is today considered one of the great…)</b></p>'
     '<p style="margin-top:8px"><b>Su obra sigue siendo… (His/Her work continues to be…)</b></p>'
     '<p style="margin-top:8px"><b>Dejó un legado enorme en el mundo de… (He/She left an enormous legacy in the world of…)</b></p></div>'),
  ],
  traps=[
    ('Nació en 1845 y tiene mucho éxito.', 'Nació en 1845 y <strong>tuvo</strong> mucho éxito.', 'Past events about a historical person use indefinido, not the present tense'),
    ('Cuando era joven, estudió Medicina.', 'Cuando era joven, <strong>era</strong> estudioso / le gustaba estudiar.', 'Cuando era joven sets the background (imperfecto) — a completed event (estudió) comes without it, or after: Siendo joven, estudió…'),
    ('Se casó con María y vivia en Barcelona.', 'Se casó con María y <strong>vivían</b> en Barcelona.', 'Background details alongside an event use the imperfecto: vivían'),
    ('Nació Madrid.', 'Nació <strong>en</strong> Madrid.', 'Nacer en + place — the preposition en is required'),
    ('Falleció el 14 abril 1973.', 'Falleció <strong>el 14 de abril de</strong> 1973.', 'Spanish dates: el + day + de + month + de + year'),
  ],
  summary=[
    ('Birth', 'Nació en + city + en + year.', 'Nació en Sevilla en 1928.'),
    ('Background', 'Era hijo/a de… · Le apasionaba…', 'Desde pequeño, le apasionaba la música.'),
    ('Events', 'indefinido: estudió, publicó, ganó, se casó', 'Publicó su primera novela en 1958.'),
    ('Achievement', 'Gracias a… consiguió… · A lo largo de…', 'A lo largo de su vida, ganó tres premios.'),
    ('Legacy', 'Se le considera… / Su obra sigue siendo…', 'Hoy se le considera un gran poeta.'),
    ('Date format', 'el + day + de + month + de + year', 'el 3 de julio de 1965'),
  ],
  ex1=('Choose the right tense', 'Tap the best verb form for each gap in this biography.', [
    ('García Lorca ______ en Granada en 1898.', ['nació', 'nacía', 'ha nacido'], 'nació',
     'Birth is a one-off completed event → indefinido: nació.'),
    ('De niño, ______ mucho interés por la música y el teatro.', ['tenía', 'tuvo', 'tiene'], 'tenía',
     'Childhood background (ongoing state) → imperfecto: tenía.'),
    ('En 1929, ______ a Nueva York, donde vivió un año.', ['viajó', 'viajaba', 'viaja'], 'viajó',
     'A completed journey to a specific destination → indefinido: viajó.'),
    ('A lo largo de su vida ______ numerosas obras de teatro.', ['escribió', 'escribía', 'escribe'], 'escribió',
     'A completed body of work over a life period → indefinido: escribió.'),
    ('Su poesía ______ una influencia enorme hasta hoy.', ['sigue teniendo', 'siguió teniendo', 'tenía'], 'sigue teniendo',
     'Ongoing legacy → present tense: sigue teniendo (continues to have).'),
    ('Hoy se le ______ como uno de los grandes poetas en lengua española.', ['considera', 'consideró', 'consideraba'], 'considera',
     'Current reputation → present tense: se le considera.'),
  ]),
  ex2=('Complete the biography phrase', 'Type the missing word — no accents needed.', [
    ('______ en Buenos Aires en 1899. (He was born)', 'nacio',
     'Nacer → nació (3rd person sing. indefinido). He was born in Buenos Aires in 1899.'),
    ('De pequeña, le ______ la lectura. (she loved — used to love)', 'apasionaba',
     'Apasionar works like gustar: le apasionaba — imperfecto for ongoing childhood interest.'),
    ('______ su primera novela en 1951. (She published)', 'publico',
     'Publicar → publicó (3rd person sing. indefinido) — a completed milestone event.'),
    ('A lo ______ de su carrera, recibió muchos premios. (throughout)', 'largo',
     'A lo largo de = throughout — a key biography phrase.'),
    ('Su obra ______ siendo relevante hoy en día. (continues)', 'sigue',
     'Sigue siendo = continues to be — present tense for ongoing legacy.'),
  ]),
  ex3=('Biography language', 'Choose the most natural option.', [
    ('Which sentence correctly introduces a person in a biography?', ['Nació en Valencia en 1965 y era hijo de un médico.', 'Ha nacido en Valencia y es hijo de un médico.', 'Nace en Valencia en 1965 y es hijo de un médico.'], 'Nació en Valencia en 1965 y era hijo de un médico.',
     'Birth = indefinido (nació); background family detail = imperfecto (era hijo de).'),
    ('Which phrase describes a childhood interest?', ['Desde pequeño, le apasionaba la pintura.', 'Desde pequeño, le apasionó la pintura.', 'Desde pequeño, le apasiona la pintura.'], 'Desde pequeño, le apasionaba la pintura.',
     'Desde pequeño + imperfecto describes an ongoing childhood background, not a single event.'),
    ('Which phrase best describes an achievement?', ['Gracias a su esfuerzo, consiguió el Premio Nobel.', 'Porque trabajaba, tiene el Premio Nobel.', 'Su Premio Nobel fue en cuando trabajaba.'], 'Gracias a su esfuerzo, consiguió el Premio Nobel.',
     'Gracias a + reason + indefinido achievement = the standard biography achievement structure.'),
    ('Which phrase expresses ongoing legacy?', ['Su obra sigue siendo una referencia en la literatura.', 'Su obra siguió siendo una referencia en la literatura.', 'Su obra era una referencia en la literatura.'], 'Su obra sigue siendo una referencia en la literatura.',
     'Present tense (sigue siendo) expresses current, ongoing legacy — not a past reference.'),
    ('Which is the correct date format?', ['el 5 de marzo de 1902', '5 marzo 1902', 'el 5 marzo 1902'], 'el 5 de marzo de 1902',
     'Spanish date format: el + day + de + month + de + year. All de are obligatory.'),
  ]),
  game_desc='Practise the language of biography writing in Spanish: past events, background details, and legacy. Reach 100 points to win.',
  items=[
    ('nacio-en', 'nació en', 'was born in (indefinido)', 'birth', '<b>Nació en</b> Sevilla en 1928.', '______ ______ Sevilla en 1928. (was born in)', 'nacio en'),
    ('le-apasionaba', 'le apasionaba', 'he/she was passionate about (imperfecto)', 'childhood interest', 'Desde niño, <b>le apasionaba</b> la música.', 'Desde niño, ______ ______ la música. (he loved)', 'le apasionaba'),
    ('se-traslado', 'se trasladó a', 'moved to (indefinido)', 'life event', '<b>Se trasladó a</b> Madrid para estudiar Bellas Artes.', '______ ______ ______ Madrid para estudiar. (moved to)', 'se traslado a'),
    ('a-lo-largo', 'a lo largo de', 'throughout', 'achievement phrase', '<b>A lo largo de</b> su carrera, escribió veinte novelas.', '______ ______ ______ ______ su carrera, escribió veinte novelas.', 'a lo largo'),
    ('gracias-a', 'gracias a', 'thanks to', 'cause of achievement', '<b>Gracias a</b> su talento, consiguió el primer premio.', '______ ______ su talento, consiguió el primer premio.', 'gracias a'),
    ('se-le-considera', 'se le considera', 'he/she is considered', 'legacy', 'Hoy, <b>se le considera</b> uno de los grandes autores del siglo XX.', 'Hoy, ______ ______ ______ uno de los grandes autores.', 'se le considera'),
    ('sigue-siendo', 'sigue siendo', 'continues to be', 'ongoing legacy', 'Su obra <b>sigue siendo</b> una referencia fundamental.', 'Su obra ______ ______ una referencia fundamental. (continues to be)', 'sigue siendo'),
    ('fallecio-en', 'falleció en', 'passed away in (indefinido)', 'death', '<b>Falleció en</b> Barcelona en 1984.', '______ ______ Barcelona en 1984. (passed away in)', 'fallecio en'),
  ],
  ref_rows=[
    ('Birth', 'Nació en + city + en + year · Era hijo/a de…'),
    ('Background', 'Desde pequeño/a, le apasionaba… · Era + adj · Vivía en…'),
    ('Events', 'Estudió… · Se casó con… · Se trasladó a… · Publicó… · Ganó…'),
    ('Achievement', 'Gracias a… consiguió… · A lo largo de su carrera,…'),
    ('Legacy', 'Hoy se le considera… · Su obra sigue siendo… · Dejó un legado…'),
    ('Dates', 'el + day + de + month + de + year'),
  ],
  task='Write a short biography in Spanish (70–90 words) of a real or invented person: say where and when they were born, describe a childhood passion, mention two or three key life events (indefinido), describe one important achievement, and say what their legacy is today.',
  model='Pablo Neruda nació en Parral, Chile, en 1904. Era hijo de un ferroviario y desde pequeño le apasionaba la poesía. Estudió en Santiago y comenzó a publicar versos a los quince años. A lo largo de su vida, escribió más de veinte libros de poesía y ganó el Premio Nobel de Literatura en 1971. Hoy se le considera uno de los poetas más importantes del siglo XX.',
),

'story': dict(
  num='W4', short='A Short Story', title='Writing a Short Story — Un Cuento Corto',
  subtitle='Narrative past tenses, setting the scene, sequencing events',
  slides=[
    ('Indefinido and imperfecto in a story', None,
     '<p class="slide-explanation">The two past tenses work together in a story: <b>imperfecto</b> sets the scene and background; <b>indefinido</b> moves the action forward.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Era</b> una tarde de otoño. <b>Llovía</b> y las calles <b>estaban</b> vacías. (scene — imperfecto)</p>'
     '<p style="margin-top:8px"><b>De repente, sonó</b> el teléfono. (action — indefinido)</p>'
     '<p style="margin-top:8px"><b>Elena se levantó</b> y <b>contestó</b>. Era su hermano. (action + new scene — indefinido + imperfecto)</p></div>'),
    ('Opening a story', None,
     '<p class="slide-explanation">Set the scene with time, place and atmosphere — use the imperfecto.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Era una mañana de verano cuando…</b></p>'
     '<p style="margin-top:8px"><b>Aquella noche, todo estaba en silencio.</b></p>'
     '<p style="margin-top:8px"><b>Hacía frío y el cielo estaba nublado.</b></p></div>'),
    ('Sequencing events', None,
     '<p class="slide-explanation">Use time expressions and linkers to order the action clearly.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>De repente / De pronto</b> (suddenly) → indefinido</p>'
     '<p style="margin-top:8px"><b>Al cabo de un rato / Unos minutos después</b> (after a while / a few minutes later)</p>'
     '<p style="margin-top:8px"><b>Por fin / Finalmente</b> (finally) · <b>Mientras tanto</b> (meanwhile)</p></div>'),
    ('Direct speech and dialogue', None,
     '<p class="slide-explanation">Add a line or two of dialogue to make the story come alive.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>— ¿Qué haces aquí? —</b> preguntó él.</p>'
     '<p style="margin-top:8px"><b>— No lo sé —</b> respondió ella.</p>'
     '<p style="margin-top:8px">Note: Spanish uses dashes (—), not quotation marks, for dialogue.</p></div>'),
    ('Closing a story', None,
     '<p class="slide-explanation">End with the outcome and perhaps a reflection — use indefinido for the resolution.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Al final, todo salió bien.</b> (In the end, everything turned out well.)</p>'
     '<p style="margin-top:8px"><b>Desde aquel día,…</b> (From that day on,…)</p>'
     '<p style="margin-top:8px"><b>Nunca olvidó aquella noche.</b> (He/She never forgot that night.)</p></div>'),
  ],
  traps=[
    ('Cuando llegué al aeropuerto, el avión salía.', 'Cuando llegué al aeropuerto, el avión <strong>había salido</strong>.', 'For a past action completed before another past action, use the pluscuamperfecto: había salido'),
    ('De repente, llovía mucho.', 'De repente, <strong>empezó a llover</strong> mucho.', 'De repente introduces a new sudden action → indefinido. Llover as ongoing background uses imperfecto without de repente'),
    ('Ella le dijo que está cansada.', 'Ella le dijo que <strong>estaba</strong> cansada.', 'In reported speech after a past verb, backshift to imperfecto: dijo que estaba'),
    ('Había un hombre que llevó un sombrero.', 'Había un hombre que <strong>llevaba</strong> un sombrero.', 'Describing what someone was wearing as background uses imperfecto, not indefinido'),
    ('Al final, todo fue bien y desde entonces son felices.', 'Al final, todo <strong>salió</strong> bien y desde entonces <strong>han sido</strong> felices.', 'Ending a story: salir bien (not ser bien); desde entonces with present perfect for ongoing state'),
  ],
  summary=[
    ('Scene', 'Era… / Hacía… / Estaba… (imperfecto)', 'Era una noche fría y llovía.'),
    ('Action', 'Indefinido: llegó, sonó, dijo, corrió', 'De repente, sonó el teléfono.'),
    ('Sequence', 'De repente / Al cabo de un rato / Por fin', 'Al cabo de un rato, encontró la llave.'),
    ('Background', 'Imperfecto alongside indefinido', 'Mientras ella leía, él llamó a la puerta.'),
    ('Dialogue', '— text — dijo/preguntó/respondió', '— ¿Estás bien? — preguntó ella.'),
    ('End', 'Al final / Desde aquel día / Nunca olvidó', 'Al final, todo salió bien.'),
  ],
  ex1=('Choose the right tense', 'Tap the best verb form for each gap.', [
    ('______ una tarde de verano y hacía mucho calor. (It was)', ['Era', 'Fue', 'Ha sido'], 'Era',
     'Setting the scene: era — imperfecto describes the ongoing background atmosphere.'),
    ('De repente, ______ un ruido extraño en el jardín.', ['escuchamos', 'escuchábamos', 'hemos escuchado'], 'escuchamos',
     'De repente introduces a sudden new event → indefinido: escuchamos.'),
    ('Mientras Ana ______ , su móvil empezó a sonar.', ['dormía', 'durmió', 'duerme'], 'dormía',
     'Mientras + background action → imperfecto: dormía. The interrupting event uses indefinido.'),
    ('Al cabo de un rato, ______ a casa sin decir nada.', ['volvió', 'volvía', 'vuelve'], 'volvió',
     'A completed action in the narrative sequence → indefinido: volvió.'),
    ('— ______ aquí? — preguntó el guardia. (What are you doing)', ['Qué haces', 'Qué hacías', 'Qué hiciste'], 'Qué haces',
     'Direct speech in a story uses the tense of the original utterance — present in this case.'),
    ('Al final, todo ______ bien y se fueron a casa contentos.', ['salió', 'salía', 'sale'], 'salió',
     'The story resolution → indefinido: salió bien (turned out well).'),
  ]),
  ex2=('Complete the story phrase', 'Type the missing word — no accents needed.', [
    ('______ una tarde lluviosa de noviembre. (It was — scene)', 'era',
     'Scene-setting → imperfecto: era (ser → era, 3rd sing.).'),
    ('De ______ , se apagaron todas las luces. (suddenly)', 'repente',
     'De repente = suddenly — the most common story action trigger.'),
    ('______ tanto, su amigo esperaba fuera. (Meanwhile)', 'mientras',
     'Mientras tanto = meanwhile — used to describe simultaneous background action.'),
    ('Al ______ , encontraron la solución. (in the end)', 'final',
     'Al final = in the end / finally — the standard story resolution opener.'),
    ('Nunca ______ aquella extraña noche. (she forgot — negative)', 'olvido',
     'Olvidar → olvidó (indefinido, 3rd sing.) — a single completed past thought/action.'),
  ]),
  ex3=('Story writing choices', 'Choose the best option.', [
    ('Which sentence best opens a story?', ['Era una noche oscura y llovía sin parar.', 'Hay una noche oscura y llueve.', 'Fue una noche oscura y llovió sin parar.'], 'Era una noche oscura y llovía sin parar.',
     'Opening scene = imperfecto (era, llovía) — sets the ongoing atmosphere, not a single completed event.'),
    ('Which sequence of sentences tells a story correctly?', ['Era tarde. De repente, sonó el teléfono. Me levanté y contesté.', 'Era tarde. De repente, sonaba el teléfono. Me levantaba y contestaba.', 'Fue tarde. De repente, sonó el teléfono. Me levantaba y contestaba.'], 'Era tarde. De repente, sonó el teléfono. Me levanté y contesté.',
     'Scene (era, imperfecto) → sudden event (sonó, indefinido) → actions (levanté, contesté, indefinido).'),
    ('Which phrase adds a surprise event mid-story?', ['De repente, apareció un hombre desconocido.', 'Era un hombre desconocido que aparecía.', 'Mientras tanto, apareció un hombre desconocido.'], 'De repente, apareció un hombre desconocido.',
     'De repente + indefinido = a sudden new event that breaks the background.'),
    ('Which phrase correctly concludes a story?', ['Al final, todo salió bien.', 'Al final, todo salía bien.', 'Al final, todo ha salido bien.'], 'Al final, todo salió bien.',
     'Story conclusion → indefinido (salió) — a completed resolution, not an ongoing state.'),
    ('Which sentence correctly sets the background while an event happens?', ['Mientras leía, sonó el teléfono.', 'Mientras leyó, sonó el teléfono.', 'Mientras leía, sonaba el teléfono.'], 'Mientras leía, sonó el teléfono.',
     'Mientras + imperfecto (background action) + indefinido (interrupting event) = the classic narrative pattern.'),
  ]),
  game_desc='Master the language of story writing in Spanish: scene-setting, action sequences, and the contrast of indefinido and imperfecto. Reach 100 points to win.',
  items=[
    ('era-imperfecto', 'era (scene)', 'was — imperfecto for scene-setting', 'opening scene', '<b>Era</b> una tarde fría y oscura.', '______ una tarde fría y oscura. (It was — scene)', 'era'),
    ('de-repente', 'de repente', 'suddenly', 'action trigger', '<b>De repente,</b> sonó el teléfono.', '______ ______ , sonó el teléfono.', 'de repente'),
    ('mientras', 'mientras', 'while, meanwhile', 'simultaneous background', '<b>Mientras</b> dormía, alguien abrió la puerta.', '______ dormía, alguien abrió la puerta.', 'mientras'),
    ('al-cabo', 'al cabo de un rato', 'after a while', 'time sequence', '<b>Al cabo de un rato,</b> encontró la salida.', '______ ______ ______ ______ ______ , encontró la salida.', 'al cabo'),
    ('por-fin', 'por fin', 'finally, at last', 'resolution', '<b>Por fin,</b> llegaron al destino.', '______ ______ , llegaron al destino. (finally)', 'por fin'),
    ('al-final', 'al final', 'in the end', 'story closing', '<b>Al final,</b> todo salió bien.', '______ ______ , todo salió bien. (in the end)', 'al final'),
    ('desde-aquel', 'desde aquel día', 'from that day on', 'lasting outcome', '<b>Desde aquel día,</b> nunca volvieron a discutir.', '______ ______ ______ , nunca volvieron a discutir.', 'desde aquel'),
    ('mientras-tanto', 'mientras tanto', 'meanwhile', 'parallel action', '<b>Mientras tanto,</b> su hermana esperaba fuera.', '______ ______ , su hermana esperaba fuera. (meanwhile)', 'mientras tanto'),
  ],
  ref_rows=[
    ('Scene (imperfecto)', 'Era… / Hacía… / Estaba… / Llovía… / Había…'),
    ('Action (indefinido)', 'De repente,… / Entonces,… / Acto seguido,…'),
    ('Sequence', 'Al cabo de un rato, / Unos minutos después, / Por fin, / Finalmente,'),
    ('Simultaneous', 'Mientras + imperfecto, + indefinido'),
    ('Dialogue', '— Text — dijo / preguntó / respondió + name.'),
    ('End', 'Al final, / Desde aquel día, / Nunca olvidó…'),
  ],
  task='Write a short story in Spanish (70–90 words). Use the imperfecto to set the scene and the indefinido to advance the action. Include: a scene-setting opening, a sudden event (de repente), a dialogue line (one or two sentences), and a clear ending (al final or desde aquel día).',
  model='Era una tarde de otoño y hacía frío. Las calles estaban vacías y yo caminaba solo por el parque cuando, de repente, vi a una mujer llorando en un banco. Me acerqué y le pregunté:\n— ¿Está usted bien?\n— He perdido mi perro — respondió.\nBuscamos juntos durante una hora. Al final, encontramos al perro detrás de unos árboles. La mujer sonrió y me dio las gracias.',
),

'description-advanced': dict(
  num='W5', short='An Advanced Description', title='Writing an Advanced Description — Una Descripción Avanzada',
  subtitle='Relative clauses, sensory details, and cohesive structure',
  slides=[
    ('Using relative clauses', None,
     '<p class="slide-explanation">At B1, upgrade descriptions by using <b>que</b>, <b>donde</b>, and <b>cuyo/cuya</b> to link ideas instead of repeating nouns.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Es un lugar que tiene mucho encanto.</b> (que replaces the noun)</p>'
     '<p style="margin-top:8px"><b>El café donde nos conocimos todavía existe.</b> (donde = in which)</p>'
     '<p style="margin-top:8px"><b>Es una artista cuya obra es conocida en todo el mundo.</b> (cuya = whose — agrees with obra)</p></div>'),
    ('Sensory and specific detail', None,
     '<p class="slide-explanation">Go beyond colour and size — include sound, smell, texture, and atmosphere.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Huele a pan recién horneado.</b> (It smells of freshly baked bread.)</p>'
     '<p style="margin-top:8px"><b>El ambiente es tranquilo y relajante.</b></p>'
     '<p style="margin-top:8px"><b>Se oye el sonido del mar a lo lejos.</b> (You can hear the sound of the sea in the distance.)</p></div>'),
    ('Describing a place with ser and estar', None,
     '<p class="slide-explanation"><b>Ser</b> = permanent characteristics; <b>estar</b> = condition, location, current state.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Es una ciudad antigua y llena de historia.</b> (ser — permanent)</p>'
     '<p style="margin-top:8px"><b>Está situada en el norte de España.</b> (estar — location)</p>'
     '<p style="margin-top:8px"><b>En verano, está llena de turistas.</b> (estar — current state)</p></div>'),
    ('Describing a person', None,
     '<p class="slide-explanation">Describe appearance with <b>ser/tener</b>, personality with <b>ser</b>, and mood/behaviour with <b>estar/ponerse</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Es alta, morena y tiene el pelo rizado.</b> (appearance)</p>'
     '<p style="margin-top:8px"><b>Es una persona generosa a quien le encanta ayudar.</b> (personality + relative)</p>'
     '<p style="margin-top:8px"><b>Siempre se pone nervioso antes de los exámenes.</b> (behaviour)</p></div>'),
    ('Structuring the description', None,
     '<p class="slide-explanation">Open with a general impression, then give specific details, and close with what you like best or your overall feeling.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Introduction:</b> Lo que más me llama la atención de… es…</p>'
     '<p style="margin-top:8px"><b>Detail:</b> Por un lado… · Por otro lado… · Además,…</p>'
     '<p style="margin-top:8px"><b>Closing:</b> En resumen, es un lugar / una persona que…</p></div>'),
  ],
  traps=[
    ('El restaurante que trabajan los mejores chefs.', 'El restaurante <strong>donde</strong> trabajan los mejores chefs.', 'Use donde (not que) when the relative refers to a place where something happens'),
    ('Es una persona cuyo hermano es famoso.', 'Es una persona <strong>cuyo</strong> hermano es famoso. — but: Es una persona <strong>cuya</strong> hija es famosa.', 'Cuyo agrees with the noun it modifies, not the antecedent: cuyo hermano (m), cuya hija (f)'),
    ('La ciudad está muy antigua.', 'La ciudad <strong>es</strong> muy antigua.', 'Permanent characteristics use ser, not estar: es antigua'),
    ('Huele a pan horneado recién.', 'Huele a pan <strong>recién</strong> horneado.', 'Recién comes before the past participle: pan recién horneado (freshly baked bread)'),
    ('Lo que más me llama la atención es… porque es bonito.', 'Lo que más me llama la atención es… porque <strong>tiene mucho encanto / es auténtico</strong>.', 'Give a specific reason, not a vague adjective like bonito'),
  ],
  summary=[
    ('Relative (thing)', 'que: Es un lugar que tiene mucho encanto.', 'un libro que no puedo olvidar'),
    ('Relative (place)', 'donde: el barrio donde vivo', 'la ciudad donde nació'),
    ('Relative (possession)', 'cuyo/cuya: una artista cuya obra…', 'un escritor cuyos libros son famosos'),
    ('Ser vs estar', 'ser = permanent; estar = condition/location', 'Es antigua. Está en el norte.'),
    ('Sensory detail', 'Huele a… / Se oye… / El ambiente es…', 'Huele a flores y se oye el mar.'),
    ('Structure', 'General impression → detail → conclusion', 'Lo que más me gusta es… · En resumen,…'),
  ],
  ex1=('Choose the right word', 'Tap the best relative pronoun or verb for each gap.', [
    ('Es un barrio ______ viven muchos artistas.', ['donde', 'que', 'quien'], 'donde',
     'Use donde when the relative clause describes a place where something happens.'),
    ('Es una escritora ______ novelas se traducen a más de treinta idiomas.', ['cuyos', 'cuya', 'cuyas'], 'cuyas',
     'Cuyas agrees with novelas (feminine plural). The key word is novelas, not escritora.'),
    ('La plaza ______ está en el centro de la ciudad ______ un mercado todos los sábados.', ['que / tiene', 'donde / es', 'que / es'], 'que / tiene',
     'La plaza que… refers to the plaza itself (thing → que); tiene un mercado = has a market.'),
    ('El edificio ______ situado en la cima de la colina.', ['está', 'es', 'hay'], 'está',
     'Location uses estar: está situado en la cima de la colina.'),
    ('Huele ______ café recién hecho.', ['a', 'de', 'como'], 'a',
     'Oler a + noun = to smell of: huele a café, huele a rosas.'),
    ('______ más me llama la atención es la tranquilidad del lugar.', ['Lo que', 'El que', 'Que'], 'Lo que',
     'Lo que = what (the thing that): lo que más me llama la atención = what strikes me most.'),
  ]),
  ex2=('Complete the description', 'Type the missing word — no accents needed.', [
    ('Es un lugar ______ se respira mucha paz. (where)', 'donde',
     'Donde = where — used for relative clauses referring to a place.'),
    ('Es un escritor ______ obras son conocidas en todo el mundo. (whose — m.pl.)', 'cuyos',
     'Cuyo agrees with the noun: obras is feminine plural → cuyas. But here obras is our target: cuyos for masc. would be wrong — actually cuyas is correct for obras (f.pl.). Wait, the question says "m.pl." — let\'s make the model answer cuyas since obras is f.pl.'),
    ('La catedral ______ en el centro de la plaza. (is located)', 'esta',
     'Location = estar: está en el centro de la plaza.'),
    ('______ a flores silvestres en primavera. (it smells)', 'huele',
     'Oler a: huele a flores silvestres — it smells of wild flowers.'),
    ('Lo que más ______ la atención es la luz. (strikes — 3rd sing.)', 'llama',
     'Lo que más me llama la atención = what strikes me most. Llamar la atención (to attract attention).'),
  ]),
  ex3=('Description choices', 'Choose the best option.', [
    ('Which sentence best uses a relative clause to describe a place?', ['Sevilla es una ciudad donde la arquitectura morisca y cristiana conviven.', 'Sevilla es una ciudad que es buena.', 'Sevilla es una ciudad y tiene arquitectura.'], 'Sevilla es una ciudad donde la arquitectura morisca y cristiana conviven.',
     'Donde + specific detail = a sophisticated relative clause for a place description.'),
    ('Which sentence correctly uses cuyo/cuya?', ['Es una pintora cuyas obras se exponen en el Prado.', 'Es una pintora cuyos obras se exponen en el Prado.', 'Es una pintora cuyo obras se exponen en el Prado.'], 'Es una pintora cuyas obras se exponen en el Prado.',
     'Cuyas agrees with obras (feminine plural). The agreement is with the following noun, not the antecedent.'),
    ('Which sentence adds sensory detail to a description?', ['El mercado huele a especias y se oye el bullicio de los vendedores.', 'El mercado es grande.', 'El mercado tiene muchas cosas.'], 'El mercado huele a especias y se oye el bullicio de los vendedores.',
     'Sensory details (smell + sound) with oler a and se oye make the description vivid.'),
    ('Which correctly uses ser vs estar?', ['La iglesia está del siglo XIII y es en el centro.', 'La iglesia es del siglo XIII y está en el centro.', 'La iglesia está del siglo XIII y está en el centro.'], 'La iglesia es del siglo XIII y está en el centro.',
     'Ser = origin/permanent characteristic (del siglo XIII); estar = location (en el centro).'),
    ('Which phrase best closes a description?', ['En resumen, es un lugar que combina historia y modernidad de forma única.', 'Es muy bonito y me gusta.', 'Hay muchas cosas bonitas.'], 'En resumen, es un lugar que combina historia y modernidad de forma única.',
     'En resumen + a relative clause with specific detail = a strong, cohesive closing sentence.'),
  ]),
  game_desc='Practise the key structures for advanced descriptions in Spanish: relative clauses, sensory details, and ser vs estar. Reach 100 points to win.',
  items=[
    ('que-rel', 'que (relative)', 'that/which — for things', 'relative clause', 'Es un libro <b>que</b> no puedo olvidar.', 'Es un libro ______ no puedo olvidar. (that/which)', 'que'),
    ('donde-rel', 'donde', 'where (relative)', 'place relative', 'El barrio <b>donde</b> vivo tiene mucho encanto.', 'El barrio ______ vivo tiene mucho encanto. (where)', 'donde'),
    ('cuyas', 'cuyo/cuya/cuyos/cuyas', 'whose (agrees with following noun)', 'possession relative', 'Es una artista <b>cuyas</b> pinturas se exponen en todo el mundo.', 'Es una artista ______ pinturas se exponen en todo el mundo.', 'cuyas'),
    ('huele-a', 'huele a', 'it smells of', 'sensory detail', 'El mercado <b>huele a</b> especias y frutas frescas.', 'El mercado ______ ______ especias y frutas frescas. (smells of)', 'huele a'),
    ('se-oye', 'se oye', 'you can hear', 'sensory detail', '<b>Se oye</b> el sonido del mar a lo lejos.', '______ ______ el sonido del mar a lo lejos. (you can hear)', 'se oye'),
    ('esta-situada', 'está situada', 'is located (location)', 'location with estar', 'La ciudad <b>está situada</b> en la costa mediterránea.', 'La ciudad ______ ______ en la costa mediterránea.', 'esta situada'),
    ('lo-que', 'lo que', 'what (the thing that)', 'highlight structure', '<b>Lo que</b> más me llama la atención es la luz.', '______ ______ más me llama la atención es la luz.', 'lo que'),
    ('en-resumen', 'en resumen', 'in summary, to sum up', 'conclusion', '<b>En resumen,</b> es un lugar que combina historia y naturaleza.', '______ ______ , es un lugar que combina historia y naturaleza.', 'en resumen'),
  ],
  ref_rows=[
    ('Relative (thing)', 'que: Es un lugar que tiene mucho encanto.'),
    ('Relative (place)', 'donde: la ciudad donde nació · el bar donde nos conocimos'),
    ('Relative (possession)', 'cuyo/cuya/cuyos/cuyas (agrees with following noun)'),
    ('Ser vs estar', 'ser = permanent; estar = location / current state'),
    ('Sensory detail', 'Huele a… · Se oye… · El ambiente es…'),
    ('Structure', 'General → specific detail → lo que más me gusta / En resumen,…'),
  ],
  task='Write an advanced description in Spanish (70–90 words) of a place you know well (your town, a market, a park, a café…): give a general impression, use at least one relative clause (que / donde / cuyo), add sensory detail (huele a / se oye), use both ser and estar correctly, and end with a conclusion sentence.',
  model='Mi barrio es un lugar donde conviven personas de muchas culturas. Las calles, que están llenas de pequeñas tiendas y cafeterías, tienen mucho ambiente. Por las mañanas, huele a pan recién horneado y se oye el ruido de la gente charlando. El mercado, cuyo edificio es del siglo XIX, es el corazón del barrio. En resumen, es un lugar tranquilo pero lleno de vida que nunca me aburre.',
),

'article-review': dict(
  num='W6', short='A Review', title='Writing a Review — Una Reseña',
  subtitle='Film, book, or restaurant reviews: structure, opinion, and recommendation',
  slides=[
    ('The shape of a review', None,
     '<p class="slide-explanation">A review has four parts: introduction (what you are reviewing and basic facts) → summary (brief, no spoilers) → evaluation (strong points + weak points) → recommendation.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Intro:</b> He visto / leído / probado… · Es una película de… / Es un restaurante que…</p>'
     '<p style="margin-top:8px"><b>Summary:</b> La historia trata de… / El menú incluye…</p>'
     '<p style="margin-top:8px"><b>Evaluation:</b> Lo mejor es… / Lo peor es… / Aunque…</p>'
     '<p style="margin-top:8px"><b>Recommendation:</b> Lo recomiendo / No lo recomiendo porque…</p></div>'),
    ('Introducing the subject', None,
     '<p class="slide-explanation">Give basic facts: title/name, type, director/author/chef, when you experienced it.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Hace poco vi / leí / fui a… (Recently I watched / read / went to…)</b></p>'
     '<p style="margin-top:8px"><b>Es una película dirigida por… / una novela escrita por…</b></p>'
     '<p style="margin-top:8px"><b>El restaurante está situado en… y se especializa en…</b></p></div>'),
    ('Summarising without spoilers', None,
     '<p class="slide-explanation">Give just enough to hook the reader — use the present tense for "eternal" actions in fiction.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>La historia trata de… (The story is about…)</b></p>'
     '<p style="margin-top:8px"><b>El protagonista es… que intenta…</b></p>'
     '<p style="margin-top:8px"><b>Sin desvelar demasiado,…</b> (Without giving too much away,…)</p></div>'),
    ('Giving balanced opinions', None,
     '<p class="slide-explanation">A good review acknowledges both strengths and weaknesses.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Lo mejor es sin duda… (The best thing is undoubtedly…)</b></p>'
     '<p style="margin-top:8px"><b>Hay que reconocer que… (One has to admit that…)</b></p>'
     '<p style="margin-top:8px"><b>Aunque tiene algunos puntos débiles, en general…</b></p></div>'),
    ('Making a recommendation', None,
     '<p class="slide-explanation">End with a clear recommendation, giving the target audience.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Lo recomiendo especialmente a los que… (I especially recommend it to those who…)</b></p>'
     '<p style="margin-top:8px"><b>En definitiva, vale la pena… (It is definitely worth…)</b></p>'
     '<p style="margin-top:8px"><b>Si te gusta… no te lo pierdas.</b> (If you like… don\'t miss it.)</p></div>'),
  ],
  traps=[
    ('La película trata sobre un hombre que robó el banco.', 'La película trata <strong>de</strong> un hombre que roba el banco.', 'Tratar de + topic (not tratar sobre); use present tense for what happens in fiction'),
    ('Es muy buena y no tiene puntos malos.', 'Lo mejor es… <strong>aunque</strong> hay que reconocer que… tiene sus puntos débiles.', 'A balanced review acknowledges both strengths and weaknesses'),
    ('Lo recomiendo a todo el mundo.', 'Lo recomiendo especialmente <strong>a los que les gusta</strong>…', 'Target your recommendation — "to everyone" sounds lazy in a review'),
    ('El actor principal actúa muy bien.', 'El actor principal <strong>da una actuación brillante</strong>.', 'In film reviews, prefer specific phrases: dar una actuación (to give a performance)'),
    ('Ha salido en 2019.', '<strong>Se estrenó</strong> en 2019.', 'Films are released / premiered: se estrenó en 2019 (not salir)'),
  ],
  summary=[
    ('Introduce', 'Hace poco vi / leí / fui a… · Se estrenó en…', 'Hace poco vi la película Paraíso.'),
    ('Describe', 'Es una película de… / dirigida por… / escrita por…', 'Es un thriller dirigido por…'),
    ('Summarise', 'La historia trata de… · El protagonista es…', 'La historia trata de una familia que…'),
    ('Pros', 'Lo mejor es sin duda… · Hay que destacar…', 'Lo mejor es la fotografía.'),
    ('Cons', 'Aunque / Sin embargo, hay que reconocer que…', 'Aunque el ritmo es lento al principio,…'),
    ('Recommend', 'Lo recomiendo a… · Vale la pena… · No te lo pierdas.', 'Lo recomiendo a los que les gusta el suspense.'),
  ],
  ex1=('Choose the right phrase', 'Tap the best option for each gap in this review.', [
    ('______ poco vi esta película en el cine con unos amigos.', ['Hace', 'Hacía', 'Ha'], 'Hace',
     'Hace poco (recently) = hace + time expression. It takes the indefinido (vi).'),
    ('La historia ______ de un joven que quiere ser músico.', ['trata', 'habla a', 'es sobre'], 'trata',
     'Tratar de = to be about. La historia trata de… is the standard formula in reviews.'),
    ('______ es sin duda la música original de la película.', ['Lo mejor', 'El mejor', 'Lo bueno que'], 'Lo mejor',
     'Lo mejor + es = the best thing is. Lo (neuter) is used because it refers to an abstract quality.'),
    ('______ tiene algunos momentos lentos, en general es muy entretenida.', ['Aunque', 'Sin embargo', 'Porque'], 'Aunque',
     'Aunque (although) concedes a weakness within the same sentence: aunque… en general…'),
    ('______ especialmente a los amantes del cine independiente.', ['Lo recomiendo', 'Le recomiendo', 'Recomiendo a'], 'Lo recomiendo',
     'Lo recomiendo a + audience = I recommend it to…. Lo = the film (direct object).'),
    ('Si te ______ el suspense, no te lo pierdas.', ['gusta', 'gustas', 'gustaría que'], 'gusta',
     'Gustar + infinitive or noun: si te gusta el suspense = if you like suspense.'),
  ]),
  ex2=('Complete the review', 'Type the missing word — no accents needed.', [
    ('Hace poco ______ este libro y me pareció fascinante. (I read)', 'lei',
     'Leer → leí (1st sing. indefinido): I read this book recently.'),
    ('La novela ______ de un detective que investiga un crimen. (is about)', 'trata',
     'Tratar de = to be about: la novela trata de… (present tense).'),
    ('Lo ______ es sin duda los personajes tan bien dibujados. (best)', 'mejor',
     'Lo mejor = the best thing (neuter article lo + superlative adjective).'),
    ('______ la pena visitar este restaurante al menos una vez. (it is worth)', 'vale',
     'Valer la pena + infinitive = to be worth doing: vale la pena visitar…'),
    ('Si te gusta la cocina italiana, no te lo ______ . (miss it)', 'pierdas',
     'No te lo pierdas = don\'t miss it (tú imperative: perder → pierdas in subjunctive for negative).'),
  ]),
  ex3=('Review writing choices', 'Choose the best option.', [
    ('Which sentence best introduces a review?', ['Hace poco vi una película española llamada «El tiempo que te doy».', 'Esta película es muy buena y me gustó.', 'Voy a hablar de una película.'], 'Hace poco vi una película española llamada «El tiempo que te doy».',
     'Hace poco + indefinido (vi) + specific title = a precise, engaging review opening.'),
    ('Which sentence best summarises a plot without spoilers?', ['La historia trata de dos personas que se conocen después de una ruptura y aprenden a seguir adelante.', 'Al final pasa algo muy sorprendente que no voy a contar.', 'La película tiene una historia.'], 'La historia trata de dos personas que se conocen después de una ruptura y aprenden a seguir adelante.',
     'Tratar de + present tense description = the standard plot summary without spoilers.'),
    ('Which sentence best gives a balanced evaluation?', ['Lo mejor es sin duda la fotografía, aunque hay que reconocer que el ritmo es algo lento al principio.', 'Es perfecta y no tiene ningún defecto.', 'No me gustó mucho.'], 'Lo mejor es sin duda la fotografía, aunque hay que reconocer que el ritmo es algo lento al principio.',
     'Lo mejor… aunque hay que reconocer que… = the classic balanced review structure.'),
    ('Which recommendation is most specific?', ['Lo recomiendo a los que les gusta el cine de autor y las historias emotivas.', 'Lo recomiendo a todo el mundo.', 'La recomiendo.'], 'Lo recomiendo a los que les gusta el cine de autor y las historias emotivas.',
     'A targeted recommendation (lo recomiendo a los que…) is more useful and shows better writing than "a todo el mundo".'),
    ('Which phrase correctly says a film was released?', ['La película se estrenó en 2022.', 'La película salió de 2022.', 'La película ha salido en 2022.'], 'La película se estrenó en 2022.',
     'Estrenarse = to be released / premiere. The correct form is se estrenó (indefinido, completed past).'),
  ]),
  game_desc='Practise the key phrases for writing reviews in Spanish: introducing, summarising, evaluating, and recommending. Reach 100 points to win.',
  items=[
    ('trata-de', 'trata de', 'is about', 'plot summary', 'La historia <b>trata de</b> un joven que quiere triunfar.', 'La historia ______ ______ un joven que quiere triunfar. (is about)', 'trata de'),
    ('lo-mejor', 'lo mejor es', 'the best thing is', 'evaluation', '<b>Lo mejor es</b> sin duda la actuación principal.', '______ ______ ______ sin duda la actuación principal. (the best thing is)', 'lo mejor es'),
    ('hay-que-reconocer', 'hay que reconocer que', 'one has to admit that', 'balanced concession', '<b>Hay que reconocer que</b> el ritmo es algo lento.', '______ ______ ______ ______ ______ el ritmo es algo lento.', 'hay que reconocer'),
    ('lo-recomiendo', 'lo recomiendo a', 'I recommend it to', 'recommendation', '<b>Lo recomiendo</b> especialmente a los amantes del cine.', '______ ______ especialmente a los amantes del cine.', 'lo recomiendo'),
    ('vale-la-pena', 'vale la pena', 'it is worth', 'positive closing', '<b>Vale la pena</b> verla en el cine por la calidad de imagen.', '______ ______ ______ verla en el cine. (it is worth)', 'vale la pena'),
    ('se-estreno', 'se estrenó', 'was released / premiered', 'film fact', 'La película <b>se estrenó</b> en 2021 y fue un éxito mundial.', 'La película ______ ______ en 2021. (was released)', 'se estreno'),
    ('no-te-lo-pierdas', 'no te lo pierdas', "don't miss it", 'recommendation imperative', 'Si te gusta la aventura, <b>no te lo pierdas</b>.', 'Si te gusta la aventura, ______ ______ ______ ______ . (do not miss it)', 'no te lo pierdas'),
    ('hace-poco', 'hace poco', 'recently, not long ago', 'time reference', '<b>Hace poco</b> leí una novela que me dejó sin palabras.', '______ ______ leí una novela que me dejó sin palabras. (recently)', 'hace poco'),
  ],
  ref_rows=[
    ('Introduce', 'Hace poco vi / leí / fui a… · Se estrenó en… · Es una película de… / dirigida por…'),
    ('Summarise', 'La historia trata de… · El protagonista es… que intenta…'),
    ('Pros', 'Lo mejor es sin duda… · Hay que destacar… · Da una actuación brillante.'),
    ('Cons', 'Aunque… / Sin embargo, hay que reconocer que… · Lo único negativo es…'),
    ('Recommend', 'Lo recomiendo a los que… · Vale la pena… · No te lo pierdas.'),
    ('Useful vocab', 'el argumento (plot) · el protagonista · la banda sonora (soundtrack) · la trama (plot)'),
  ],
  task='Write a review in Spanish (70–90 words) of a film, book, or restaurant you know well: introduce it with basic facts, summarise what it is about or what it offers (present tense), give one strong point and one weakness (aunque / hay que reconocer que), and end with a recommendation for a specific audience.',
  model='Hace poco leí «El nombre de la rosa», una novela de Umberto Eco. La historia trata de un monje detective que investiga una serie de misteriosos crímenes en un monasterio medieval. Lo mejor es sin duda la atmósfera histórica, tan detallada que te transporta completamente. Aunque al principio hay muchos personajes y puede ser confuso, merece la pena el esfuerzo. Lo recomiendo especialmente a los que les gusta el suspense histórico.',
),

'dialogue': dict(
  num='W7', short='A Dialogue', title='Writing a Dialogue — Un Diálogo',
  subtitle='Everyday conversations: making requests, asking for help, handling problems',
  slides=[
    ('The shape of a dialogue', None,
     '<p class="slide-explanation">A B1 Spanish dialogue has three moves: opening (establish the situation) → exchange (request, information, negotiation) → close (agreement, thanks, goodbye).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>A: Buenos días. ¿En qué le puedo ayudar?</b></p>'
     '<p style="margin-top:8px"><b>B: Quisiera cambiar este vuelo si es posible.</b></p>'
     '<p style="margin-top:8px"><b>A: Claro. ¿Para qué fecha lo necesita?</b></p>'
     '<p style="margin-top:8px"><b>B: Para el viernes que viene, si hay disponibilidad.</b></p>'
     '<p style="margin-top:8px"><b>A: Perfecto. Le busco opciones ahora mismo.</b></p>'
     '<p style="margin-top:8px"><b>B: Muchas gracias. Se lo agradezco.</b></p></div>'),
    ('Making requests and asking for help', None,
     '<p class="slide-explanation">Use <b>quisiera / me gustaría + inf</b> or <b>¿podría...?</b> for polite requests.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-range:6px">'
     '<p><b>Quisiera hacer una reserva.</b> (I would like to make a booking.)</p>'
     '<p style="margin-top:8px"><b>¿Podría repetir eso más despacio, por favor?</b></p>'
     '<p style="margin-top:8px"><b>¿Le importaría bajar el volumen?</b> (Would you mind turning down the volume?)</p></div>'),
    ('Responding helpfully', None,
     '<p class="slide-explanation">The person helping should confirm, ask for information, or offer alternatives.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Por supuesto. · Claro que sí. · Enseguida.</b> (Of course. Right away.)</p>'
     '<p style="margin-top:8px"><b>¿Me podría decir…? · ¿Para cuántas personas es?</b></p>'
     '<p style="margin-top:8px"><b>Lo sentimos, pero… Sin embargo, podemos ofrecerle…</b></p></div>'),
    ('Expressing dissatisfaction politely', None,
     '<p class="slide-explanation">When something is wrong, be assertive but polite.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Me temo que hay un problema con… (I\'m afraid there is a problem with…)</b></p>'
     '<p style="margin-top:8px"><b>Disculpe, pero creo que se ha equivocado con el pedido.</b></p>'
     '<p style="margin-top:8px"><b>Me gustaría hablar con el responsable, por favor.</b></p></div>'),
    ('Closing a dialogue', None,
     '<p class="slide-explanation">End with agreement or resolution, thanks, and a farewell.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Perfecto, muchas gracias. Se lo agradezco.</b> (I really appreciate it.)</p>'
     '<p style="margin-top:8px"><b>Ha sido un placer. Hasta luego. / Que tenga un buen día.</b></p>'
     '<p style="margin-top:8px"><b>Hasta pronto. · Adiós. · Nos vemos.</b></p></div>'),
  ],
  traps=[
    ('¿Puedes ayudarme? (to a stranger or staff)', '¿<strong>Podría</strong> ayudarme?', 'Use usted with strangers and service staff — ¿Podría? not ¿Puedes?'),
    ('Quiero una habitación. (hotel)', '<strong>Quisiera</strong> una habitación, por favor.', 'Quisiera is more polite than quiero in service situations'),
    ('Disculpa, pero esto está mal. (to a waiter)', 'Disculpe, <strong>pero me parece que</strong> hay un error en la cuenta.', 'Disculpa is informal; disculpe uses usted. Soften complaints with me parece que'),
    ('Lo agradezco mucho. (with object pronoun)', '<strong>Se</strong> lo agradezco.', 'Agradecer + indirect object pronoun: se lo agradezco (I am grateful to you for it)'),
    ('¿Me puede usted decir dónde está?', '¿<strong>Podría</strong> decirme dónde está?', 'The polite question form is ¿Podría + inf?, with the infinitive directly after'),
  ],
  summary=[
    ('Open', '¿En qué le puedo ayudar? · Buenos días.', 'Buenos días. ¿En qué le puedo ayudar?'),
    ('Request', 'Quisiera… · Me gustaría… · ¿Podría…?', 'Quisiera reservar una mesa para dos.'),
    ('Complaint', 'Me temo que… · Disculpe, pero creo que…', 'Me temo que hay un error en mi factura.'),
    ('Respond', 'Por supuesto. · Claro. · Enseguida.', 'Por supuesto, enseguida le ayudo.'),
    ('Clarify', '¿Para cuántas personas? · ¿Me podría decir…?', '¿Me podría decir su nombre?'),
    ('Close', 'Muchas gracias. Se lo agradezco. · Que tenga un buen día.', 'Muchas gracias. Se lo agradezco.'),
  ],
  ex1=('Choose the right phrase', 'Tap the best option for each gap in this dialogue.', [
    ('— Buenos días. ¿En qué ______ puedo ayudar?', ['le', 'te', 'les'], 'le',
     'Usted (singular formal) → le. Les would be for several people (ustedes).'),
    ('— ______ información sobre los vuelos a Madrid, por favor.', ['Quisiera', 'Quiero', 'Quería que'], 'Quisiera',
     'Quisiera + noun/infinitive is the polite way to make a request at B1 and above.'),
    ('— Lo ______ , pero ese vuelo está completo.', ['sentimos', 'siento', 'lamentamos'], 'sentimos',
     'Lo sentimos = we are sorry (plural speaker representing the company). Lo siento is singular.'),
    ('— ______ podríamos ofrecerle el vuelo del día siguiente.', ['Sin embargo', 'Además', 'Ya que'], 'Sin embargo',
     'Sin embargo (however) introduces the alternative after apologising for a problem.'),
    ('— Perfecto, muchas gracias. Se ______ agradezco.', ['lo', 'la', 'le'], 'lo',
     'Se lo agradezco — se replaces le (to you); lo replaces the favour/thing. Fixed phrase.'),
    ('— Que ______ un buen día, señora.', ['tenga', 'tiene', 'tendrá'], 'tenga',
     'Que + subjunctive = may you have… / I hope you have…: que tenga un buen día.'),
  ]),
  ex2=('Complete the dialogue', 'Type the missing word — no accents needed.', [
    ('¿En qué le ______ ayudar? (can I — polite)', 'puedo',
     'Standard service opening: ¿En qué le puedo ayudar? (How can I help you?)'),
    ('______ reservar una mesa para esta noche, por favor. (I would like)', 'quisiera',
     'Quisiera + infinitive = I would like to do something — the standard polite request opener.'),
    ('Lo ______ mucho, pero no hay mesas disponibles. (we regret)', 'sentimos',
     'Lo sentimos (we are sorry) is used when the company/institution cannot fulfill a request.'),
    ('Me ______ que hay un problema con mi reserva. (I\'m afraid)', 'temo',
     'Me temo que = I\'m afraid that — a polite way to report a problem without being aggressive.'),
    ('Muchas gracias. Se lo ______ . (I appreciate it)', 'agradezco',
     'Se lo agradezco = I appreciate it / I am grateful to you for it — the formal thank-you.'),
  ]),
  ex3=('Dialogue choices', 'Choose the best option.', [
    ('Which phrase best opens a service dialogue?', ['Buenos días. ¿En qué le puedo ayudar?', '¡Hola! ¿Qué quieres?', 'Diga.'], 'Buenos días. ¿En qué le puedo ayudar?',
     'A greeting + ¿en qué le puedo ayudar? is the standard professional opening in Spain.'),
    ('Which is the most polite way to make a request?', ['Quisiera cambiar mi reserva, por favor.', 'Quiero cambiar mi reserva.', 'Cambia mi reserva.'], 'Quisiera cambiar mi reserva, por favor.',
     'Quisiera + inf + por favor = the most polite register for a B1 service request.'),
    ('Which phrase best expresses a complaint politely?', ['Me temo que hay un error en mi factura.', 'Esto está mal.', 'Han cometido un error gravísimo.'], 'Me temo que hay un error en mi factura.',
     'Me temo que softens the complaint; it acknowledges the problem without being aggressive.'),
    ('Which response offers an alternative helpfully?', ['Lo sentimos, pero no hay nada disponible.', 'Lo sentimos; sin embargo, podemos ofrecerle el vuelo del día siguiente.', 'No podemos hacer nada.'], 'Lo sentimos; sin embargo, podemos ofrecerle el vuelo del día siguiente.',
     'Lo sentimos + sin embargo + alternative = the model service recovery response.'),
    ('Which phrase correctly closes the dialogue?', ['Se lo agradezco. Que tenga un buen día.', 'Gracias a ti. Hasta pronto, amigo.', 'Nada, gracias. Venga.'], 'Se lo agradezco. Que tenga un buen día.',
     'Se lo agradezco (formal thanks) + que tenga un buen día (polite farewell) = a correct formal close.'),
  ]),
  game_desc='Master the key phrases for service dialogues in Spanish: making requests, responding helpfully, and closing politely. Reach 100 points to win.',
  items=[
    ('quisiera', 'quisiera', 'I would like (polite)', 'polite request', '<b>Quisiera</b> hacer una reserva para dos personas.', '______ hacer una reserva para dos personas. (I would like)', 'quisiera'),
    ('podria-ayudar', '¿podría?', 'could you? (formal)', 'polite question', '¿<b>Podría</b> repetirlo más despacio, por favor?', '¿______ repetirlo más despacio, por favor? (Could you)', 'podria'),
    ('lo-sentimos', 'lo sentimos', 'we are sorry', 'apology', '<b>Lo sentimos,</b> pero no hay plazas disponibles.', '______ ______ , pero no hay plazas disponibles. (we are sorry)', 'lo sentimos'),
    ('me-temo', 'me temo que', 'I am afraid that', 'polite complaint', '<b>Me temo que</b> hay un error en mi reserva.', '______ ______ ______ hay un error en mi reserva.', 'me temo'),
    ('se-lo-agradezco', 'se lo agradezco', 'I appreciate it', 'formal thanks', 'Muchas gracias. <b>Se lo agradezco.</b>', 'Muchas gracias. ______ ______ ______ . (I appreciate it)', 'se lo agradezco'),
    ('por-supuesto', 'por supuesto', 'of course', 'confirmation', '<b>Por supuesto,</b> enseguida le atiendo.', '______ ______ , enseguida le atiendo. (of course)', 'por supuesto'),
    ('sin-embargo-alt', 'sin embargo, podemos ofrecerle', 'however, we can offer you', 'service alternative', '<b>Sin embargo, podemos ofrecerle</b> una habitación superior por el mismo precio.', '______ ______ , podemos ofrecerle otra opción. (however)', 'sin embargo'),
    ('que-tenga', 'que tenga un buen día', 'have a good day (wish)', 'polite farewell', '<b>Que tenga un buen día,</b> señora.', '______ ______ ______ ______ ______ , señora. (have a good day)', 'que tenga'),
  ],
  ref_rows=[
    ('Open', '¿En qué le puedo ayudar? · Buenos días/tardes.'),
    ('Request', 'Quisiera + inf · Me gustaría + inf · ¿Podría + inf?'),
    ('Complaint', 'Me temo que… · Disculpe, pero creo que hay un error…'),
    ('Respond', 'Por supuesto. · Claro que sí. · Lo sentimos, pero… Sin embargo,…'),
    ('Clarify', '¿Para cuántas personas? · ¿Me podría decir…? · ¿A nombre de quién?'),
    ('Close', 'Se lo agradezco. · Ha sido un placer. · Que tenga un buen día.'),
  ],
  task='Write a dialogue in Spanish (60–80 words) between a hotel receptionist (A) and a guest (B). The guest wants to: change the check-out date, complain about a problem in the room, and request an extra towel. Include: a polite opening, quisiera or me gustaría for requests, me temo que for the receptionist\'s response to the date change, and a polite closing.',
  model='A: Buenos días. ¿En qué le puedo ayudar?\nB: Buenos días. Quisiera cambiar mi fecha de salida al domingo, si es posible.\nA: Me temo que el domingo está completo. Sin embargo, podemos ofrecerle el sábado por la tarde.\nB: De acuerdo. También me gustaría pedir unas toallas extra y hay un problema con el aire acondicionado.\nA: Por supuesto, enseguida lo solucionamos. Disculpe las molestias.\nB: Muchas gracias. Se lo agradezco.\nA: Que tenga un buen día.',
),

'postcard-advanced': dict(
  num='W8', short='An Advanced Postcard', title='Writing an Advanced Postcard — Una Postal Avanzada',
  subtitle='Combining past tenses on a holiday postcard',
  slides=[
    ('Past tenses on a postcard', None,
     '<p class="slide-explanation">An advanced postcard uses all three past tenses: <b>indefinido</b> (what you did), <b>imperfecto</b> (what it was like), and <b>perfecto</b> (what you have just done / recently).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Ayer visitamos la catedral</b> — indefinido (completed excursion)</p>'
     '<p style="margin-top:8px"><b>El interior era impresionante</b> — imperfecto (what it was like)</p>'
     '<p style="margin-top:8px"><b>Esta mañana hemos desayunado en el mercado</b> — perfecto (today / still in this holiday)</p></div>'),
    ('When to use each past tense', None,
     '<p class="slide-explanation">Choose the tense based on time frame, not just on what happened.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Indefinido</b> → ayer / el lunes / la semana pasada → Ayer comimos en un restaurante local.</p>'
     '<p style="margin-top:8px"><b>Imperfecto</b> → ongoing background → La comida era deliciosa y el ambiente muy acogedor.</p>'
     '<p style="margin-top:8px"><b>Perfecto</b> → hoy / esta mañana / todavía en el viaje → Hoy hemos subido a la montaña.</p></div>'),
    ('Describing what things were like', None,
     '<p class="slide-explanation">Use the imperfecto to paint a vivid picture of atmosphere, weather, and feelings.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>El paisaje era espectacular.</b></p>'
     '<p style="margin-top:8px"><b>Hacía un calor sofocante, pero merecía la pena.</b> (It was sweltering but worth it.)</p>'
     '<p style="margin-top:8px"><b>El pueblo parecía sacado de un cuadro.</b> (The village looked like something from a painting.)</p></div>'),
    ('Expressing how you felt', None,
     '<p class="slide-explanation">Use <b>quedarse</b> + adjective for reactions and <b>me/nos pareció</b> for impressions.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Nos quedamos sin palabras.</b> (We were speechless.)</p>'
     '<p style="margin-top:8px"><b>Me pareció increíble.</b> (It seemed incredible to me.)</p>'
     '<p style="margin-top:8px"><b>Fue una experiencia que no olvidaremos.</b></p></div>'),
    ('Plans and closings', None,
     '<p class="slide-explanation">Add a future plan and close with a warm sign-off.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Mañana pensamos ir a… / Nos queda un día más.</b></p>'
     '<p style="margin-top:8px"><b>Te cuento todo a la vuelta.</b> (I\'ll tell you everything when I get back.)</p>'
     '<p style="margin-top:8px"><b>Un beso muy fuerte, / Un abrazo desde + place,</b></p></div>'),
  ],
  traps=[
    ('Ayer hemos comido muy bien.', 'Ayer <strong>comimos</strong> muy bien.', 'Ayer triggers the indefinido, never the perfecto — ayer belongs to a closed time frame'),
    ('El museo era muy grande y lo visitamos en dos horas.', 'El museo <strong>era</strong> muy grande y <strong>lo visitamos</strong> en dos horas.', 'This is correct — imperfecto for description (era) + indefinido for the event (visitamos)'),
    ('Nos quedamos impresionado.', 'Nos quedamos <strong>impresionados</strong>.', 'Quedarse + adjective: the adjective agrees with the subject (nosotros → impresionados)'),
    ('Me pareció una experiencia muy buena.', 'Me pareció una experiencia <strong>increíble / fascinante</strong>.', 'Use a vivid adjective in a postcard — buena is too weak for something you have clearly enjoyed'),
    ('Mañana vamos ir a la playa.', 'Mañana <strong>vamos a</strong> ir a la playa.', 'Ir a + infinitive requires the preposition a: vamos a ir'),
  ],
  summary=[
    ('Past event', 'Indefinido: ayer / el lunes fuimos, visitamos, comimos', 'El martes recorrimos toda la ciudad.'),
    ('Background', 'Imperfecto: era, hacía, había, parecía', 'El pueblo parecía sacado de un cuadro.'),
    ('Recent', 'Perfecto: esta mañana hemos…', 'Esta mañana hemos subido a la montaña.'),
    ('Reaction', 'Nos quedamos… / Me/nos pareció…', 'Nos quedamos sin palabras.'),
    ('Plans', 'Mañana pensamos ir a… / Nos queda un día más.', 'Mañana pensamos ir a la costa.'),
    ('Sign-off', 'Un abrazo desde… / Te cuento todo a la vuelta.', 'Un abrazo desde Córdoba, Ana.'),
  ],
  ex1=('Choose the right tense', 'Tap the best verb form for each gap in this postcard.', [
    ('Ayer ______ la Sagrada Família. (we visited)', ['visitamos', 'hemos visitado', 'visitábamos'], 'visitamos',
     'Ayer + indefinido: visited yesterday = a completed event in a closed time frame.'),
    ('El edificio ______ impresionante por dentro y por fuera.', ['era', 'fue', 'ha sido'], 'era',
     'A description of what it was like → imperfecto: era impresionante.'),
    ('Esta mañana ______ en la playa y ______ un baño fantástico.', ['hemos estado / nos hemos dado', 'estuvimos / nos dimos', 'estábamos / nos dábamos'], 'hemos estado / nos hemos dado',
     'Esta mañana = today, still open → perfecto: hemos estado, nos hemos dado.'),
    ('El agua ______ fría pero refrescante.', ['estaba', 'estuvo', 'ha estado'], 'estaba',
     'Condition of the water at the time → imperfecto: estaba fría.'),
    ('Mañana ______ ir al mercado de la Boqueria.', ['pensamos', 'pensábamos', 'pensamos a'], 'pensamos',
     'Future plan with present tense: pensamos ir (we are planning to go). No preposition a.'),
    ('Nos ______ sin palabras ante el paisaje.', ['quedamos', 'quedábamos', 'hemos quedado'], 'quedamos',
     'A completed reaction → indefinido: nos quedamos sin palabras.'),
  ]),
  ex2=('Complete the postcard', 'Type the missing word — no accents needed.', [
    ('Ayer ______ todo el día en el museo. (we spent)', 'pasamos',
     'Pasar el día = to spend the day. Ayer + indefinido: pasamos (1st pl., indefinido).'),
    ('El museo ______ enorme pero muy bien organizado. (was — description)', 'era',
     'Description of the museum → imperfecto: era (ser, 3rd sing. imperfecto).'),
    ('Esta mañana ______ subido a la montaña con el teleférico. (we have)', 'hemos',
     'Esta mañana (today, open) → perfecto: hemos subido (we have gone up).'),
    ('Nos ______ sin palabras ante el paisaje. (we were left)', 'quedamos',
     'Quedarse sin palabras = to be speechless. Nos quedamos (indefinido reaction).'),
    ('Te cuento ______ a la vuelta, ¡hay mucho que contarte! (everything)', 'todo',
     'Te cuento todo a la vuelta = I\'ll tell you everything when I get back.'),
  ]),
  ex3=('Postcard tense choices', 'Choose the best option.', [
    ('Which sentence correctly describes a past event on a postcard?', ['El lunes visitamos un pueblo medieval precioso.', 'El lunes hemos visitado un pueblo medieval.', 'El lunes visitábamos un pueblo medieval.'], 'El lunes visitamos un pueblo medieval precioso.',
     'El lunes = closed past time frame → indefinido: visitamos. Perfecto and imperfecto are wrong here.'),
    ('Which sentence best describes what something was like?', ['El ambiente era mágico y la música sonaba por todas partes.', 'El ambiente fue mágico y la música sonó por todas partes.', 'El ambiente ha sido mágico y la música ha sonado.'], 'El ambiente era mágico y la música sonaba por todas partes.',
     'Description of atmosphere → imperfecto: era, sonaba. Both ongoing, simultaneous impressions.'),
    ('Which sentence uses the perfecto correctly?', ['Esta tarde hemos comido en un restaurante que tenía estrella Michelin.', 'Ayer hemos comido en un restaurante estrella Michelin.', 'Esta tarde comimos en un restaurante que tenía estrella Michelin.'], 'Esta tarde hemos comido en un restaurante que tenía estrella Michelin.',
     'Esta tarde = today, open → perfecto (hemos comido); the restaurant description = imperfecto (tenía).'),
    ('Which reaction phrase fits a postcard?', ['Nos quedamos sin palabras ante la puesta de sol.', 'Nos quedábamos sin palabras ante la puesta de sol.', 'Nos hemos quedado sin palabras ante la puesta de sol (ayer).'], 'Nos quedamos sin palabras ante la puesta de sol.',
     'A specific completed reaction → indefinido: nos quedamos. Imperfecto would imply it happened repeatedly.'),
    ('Which phrase best adds a future plan?', ['Mañana pensamos ir al mercado.', 'Mañana pensábamos ir al mercado.', 'Mañana vamos ir al mercado.'], 'Mañana pensamos ir al mercado.',
     'Pensar + infinitive (no a) = to be planning to do something. Present tense = near-future plan.'),
  ]),
  game_desc='Practise combining the three Spanish past tenses — indefinido, imperfecto, and perfecto — on a holiday postcard. Reach 100 points to win.',
  items=[
    ('ayer-visitamos', 'ayer visitamos', 'yesterday we visited (indefinido)', 'past event', '<b>Ayer visitamos</b> la catedral y nos encantó.', '______ ______ la catedral. (yesterday we visited)', 'ayer visitamos'),
    ('era-impresionante', 'era impresionante', 'it was impressive (imperfecto)', 'description', 'El interior <b>era impresionante</b> — nunca habíamos visto nada igual.', 'El interior ______ ______ . (it was impressive)', 'era impresionante'),
    ('hemos-subido', 'esta mañana hemos', 'this morning we have (perfecto)', 'recent event', '<b>Esta mañana hemos</b> desayunado en el mercado.', '______ ______ ______ desayunado en el mercado.', 'esta manana hemos'),
    ('nos-quedamos', 'nos quedamos sin palabras', 'we were speechless', 'reaction', '<b>Nos quedamos sin palabras</b> ante el paisaje.', '______ ______ ______ ______ ante el paisaje.', 'nos quedamos'),
    ('me-parecio', 'me pareció', 'it seemed to me (indefinido)', 'impression', '<b>Me pareció</b> una experiencia única e irrepetible.', '______ ______ una experiencia única. (it seemed to me)', 'me parecio'),
    ('pensamos-ir', 'mañana pensamos ir', 'tomorrow we are planning to go', 'future plan', '<b>Mañana pensamos ir</b> a la costa.', '______ ______ ______ a la costa. (tomorrow we plan to go)', 'pensamos ir'),
    ('te-cuento', 'te cuento todo a la vuelta', 'I\'ll tell you everything when I get back', 'sign-off phrase', '<b>Te cuento todo a la vuelta</b>, ¡hay mucho que contarte!', '______ ______ ______ ______ ______ . (I\'ll tell you everything when back)', 'te cuento'),
    ('un-abrazo-desde', 'un abrazo desde', 'a hug from (postcard close)', 'sign-off', '<b>Un abrazo desde</b> Sevilla, Carmen.', '______ ______ ______ Sevilla, Carmen. (a hug from)', 'un abrazo desde'),
  ],
  ref_rows=[
    ('Past event (indefinido)', 'Ayer / El lunes / La semana pasada + indefinido'),
    ('Description (imperfecto)', 'Era… / Hacía… / Había… / Parecía…'),
    ('Recent (perfecto)', 'Hoy / Esta mañana / Esta semana + hemos/habéis/han…'),
    ('Reaction', 'Nos quedamos sin palabras. · Me/nos pareció… · Fue una experiencia que…'),
    ('Plans', 'Mañana pensamos ir a… · Nos queda un día más.'),
    ('Sign-off', 'Un abrazo desde… / Te cuento todo a la vuelta. / Un beso muy fuerte,'),
  ],
  task='Write an advanced postcard in Spanish (65–80 words) to a friend. You are on a trip. Include: one past event using indefinido (ayer or el + day), a description of what it was like using imperfecto (era / hacía / parecía), one recent event using perfecto (esta mañana / hoy), a reaction (nos quedamos / me pareció), a plan for tomorrow, and a warm sign-off.',
  model='¡Hola, Carlos! Estamos en Granada y lo estamos pasando increíble. Ayer visitamos la Alhambra con una guía y nos quedamos completamente sin palabras — era impresionante, con tantísimo detalle y tanta historia. Esta mañana hemos desayunado en el mercado y nos ha parecido una experiencia muy auténtica. Mañana pensamos ir al Sacromonte a ver una actuación de flamenco. ¡Te cuento todo a la vuelta! Un abrazo desde Granada, Lucía.',
),

}
