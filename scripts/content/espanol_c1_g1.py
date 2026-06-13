# -*- coding: utf-8 -*-
"""espanol/ C1 Gramática — lote 1 (G01–G05)."""

CHAPTERS = {
    'subjuntivo-c1': dict(
        level='c1',
        section='grammar',
        num='G01',
        short='Subjuntivo Avanzado',
        title='El Subjuntivo en Profundidad — Todos los Contextos',
        subtitle='Domina el subjuntivo en cláusulas sustantivas, adjetivas, adverbiales y de cortesía',
        slides=[
            ('El subjuntivo: mapa completo', None,
             '<p class="slide-explanation">El subjuntivo aparece en cinco grandes contextos. A nivel C1 no basta saber <em>que existe</em>; hay que dominar cuándo el indicativo y el subjuntivo son intercambiables y cuándo cambian el significado.</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Contexto</th><th style="padding:8px;text-align:left">Disparador</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Sustantiva</b></td><td style="padding:8px">Deseo / emoción / duda / mandato</td><td style="padding:8px">Espero que <b>llegues</b> pronto.</td></tr>'
             '<tr><td style="padding:8px"><b>Adjetiva</b></td><td style="padding:8px">Antecedente indefinido o negativo</td><td style="padding:8px">Busco un piso que <b>tenga</b> terraza.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Adverbial de finalidad</b></td><td style="padding:8px">para que, a fin de que</td><td style="padding:8px">Lo expliqué para que lo <b>entendieran</b>.</td></tr>'
             '<tr><td style="padding:8px"><b>Adverbial de tiempo</b></td><td style="padding:8px">cuando, hasta que, en cuanto (futuro)</td><td style="padding:8px">Llámame cuando <b>llegues</b>.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Adverbial concesiva</b></td><td style="padding:8px">aunque (matiz de duda)</td><td style="padding:8px">Aunque <b>llueva</b>, saldré.</td></tr>'
             '</table>'
             '<p class="slide-explanation">La clave: el subjuntivo expresa algo no verificado, no definido o dependiente de otro evento. El indicativo ancla la oración en la realidad del hablante.</p>'),

            ('Oraciones adjetivas: indicativo vs. subjuntivo', None,
             '<p class="slide-explanation">En las oraciones de relativo (adjetivas), la elección de modo depende de si el antecedente existe y es conocido para el hablante.</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Antecedente</th><th style="padding:8px;text-align:left">Modo</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Conocido y definido</td><td style="padding:8px">Indicativo</td><td style="padding:8px">Tengo un vecino que <b>toca</b> el violín. (existe, lo conozco)</td></tr>'
             '<tr><td style="padding:8px">Indefinido / buscado</td><td style="padding:8px">Subjuntivo</td><td style="padding:8px">Busco un vecino que <b>toque</b> el violín. (no sé si existe)</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Negativo (no existe)</td><td style="padding:8px">Subjuntivo</td><td style="padding:8px">No hay nadie que <b>sepa</b> la respuesta.</td></tr>'
             '<tr><td style="padding:8px">Superlativo / único</td><td style="padding:8px">Indicativo</td><td style="padding:8px">Es el mejor libro que <b>he leído</b>. (ya existe)</td></tr>'
             '</table>'
             '<p class="slide-explanation">Truco: si antes de «que» puedes insertar «algún/a» sin cambiar el sentido, necesitas subjuntivo: «Busco <b>algún</b> piso que tenga terraza.»</p>'),

            ('Conjunciones adverbiales: siempre subjuntivo', None,
             '<p class="slide-explanation">Ciertas conjunciones adverbiales exigen subjuntivo de forma invariable porque su significado implica que el evento no ha ocurrido aún o es hipotético:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Conjunción</th><th style="padding:8px;text-align:left">Significado</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>para que</b></td><td style="padding:8px">finalidad</td><td style="padding:8px">Habla despacio para que te <b>entiendan</b>.</td></tr>'
             '<tr><td style="padding:8px"><b>a menos que</b></td><td style="padding:8px">condición negativa</td><td style="padding:8px">Iré, a menos que <b>llueva</b>.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>con tal de que</b></td><td style="padding:8px">condición suficiente</td><td style="padding:8px">Lo acepto, con tal de que me <b>paguen</b>.</td></tr>'
             '<tr><td style="padding:8px"><b>siempre que</b></td><td style="padding:8px">condición / cada vez que (fut.)</td><td style="padding:8px">Puedes venir, siempre que <b>avises</b>.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>a condición de que</b></td><td style="padding:8px">condición formal</td><td style="padding:8px">Firmaré, a condición de que <b>revisen</b> el contrato.</td></tr>'
             '<tr><td style="padding:8px"><b>sin que</b></td><td style="padding:8px">ausencia de condición</td><td style="padding:8px">Se fue sin que nadie lo <b>notara</b>.</td></tr>'
             '</table>'),

            ('Concordancia temporal del subjuntivo', None,
             '<p class="slide-explanation">La concordancia temporal establece qué tiempo de subjuntivo usar según el tiempo del verbo principal y la relación temporal (simultaneidad, anterioridad, posterioridad):</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Verbo principal</th><th style="padding:8px;text-align:left">Simultaneidad / posterioridad</th><th style="padding:8px;text-align:left">Anterioridad</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Presente / Futuro</td><td style="padding:8px">Pres. subjuntivo: <b>hable</b></td><td style="padding:8px">Perf. subjuntivo: <b>haya hablado</b></td></tr>'
             '<tr><td style="padding:8px">Pasado / Condicional</td><td style="padding:8px">Imperf. subjuntivo: <b>hablara</b></td><td style="padding:8px">Pluscpf. subjuntivo: <b>hubiera hablado</b></td></tr>'
             '</table>'
             '<div style="background:var(--paper);padding:16px;margin:16px 0;border-radius:6px">'
             '<p><b>Quiero</b> que <b>vengas</b>. (pres. → pres. subj.)</p>'
             '<p><b>Quería</b> que <b>vinieras</b>. (pasado → imperf. subj.)</p>'
             '<p><b>Espero</b> que ya <b>haya llegado</b>. (pres. → perf. subj., acción anterior)</p>'
             '<p><b>Esperaba</b> que ya <b>hubiera llegado</b>. (pasado → pluscpf. subj., acción anterior)</p>'
             '</div>'
             '<p class="slide-explanation">Esta tabla es la base del estilo indirecto avanzado y de los hipotéticos del pasado.</p>'),

            ('Subjuntivo de cortesía y exclamativas', None,
             '<p class="slide-explanation">El subjuntivo imperfecto de algunos verbos modales sirve para suavizar peticiones y expresar mayor cortesía que el condicional:</p>'
             '<div style="background:var(--paper);padding:16px;margin:16px 0;border-radius:6px">'
             '<p><b>Quisiera</b> reservar una mesa para dos. (= querría, más formal)</p>'
             '<p><b>Pudiera</b> usted indicarme el camino? (= ¿Podría?, registro muy elevado)</p>'
             '<p><b>Debiera</b> consultarlo con su abogado. (= debería, más suave)</p>'
             '</div>'
             '<p class="slide-explanation">El subjuntivo en oraciones exclamativas e independientes expresa deseo o resignación:</p>'
             '<div style="background:var(--paper);padding:16px;margin:16px 0;border-radius:6px">'
             '<p><b>¡Que te mejores!</b> (deseo)</p>'
             '<p><b>¡Ojalá hubiera sabido</b> la verdad antes! (lamento por algo pasado)</p>'
             '<p><b>¡Que aproveche!</b> (expresión fija)</p>'
             '<p><b>¡Ojalá pueda</b> venir mañana! (esperanza sobre el futuro)</p>'
             '</div>'
             '<p class="slide-explanation">«Ojalá» con pres. subj. expresa esperanza real; con imperf. o pluscpf. subj., expresa poca probabilidad o imposibilidad.</p>'),
        ],
        traps=[
            ('Busco un médico que sabe hablar ruso.',
             'Busco un médico que <strong>sepa</strong> hablar ruso.',
             'Cuando el antecedente del relativo es indefinido (no sabemos si existe ese médico), el verbo subordinado va en subjuntivo: <b>sepa</b>, no «sabe».'),
            ('Cuando llegará, llámame.',
             'Cuando <strong>llegue</strong>, llámame.',
             'Las conjunciones de tiempo (cuando, hasta que, en cuanto…) exigen subjuntivo cuando se refieren a eventos futuros. Solo usan indicativo para referirse al pasado habitual: «Cuando llegaba, siempre llamaba.»'),
            ('Para que + indicativo: Lo dije para que lo sabes.',
             'Lo dije para que lo <strong>supieras</strong>.',
             '«Para que» expresa finalidad y siempre exige subjuntivo. Nunca va seguida de indicativo.'),
            ('Ojalá vendría pronto.',
             '<strong>Ojalá venga</strong> pronto (esperanza) / <strong>Ojalá viniera</strong> pronto (poca probabilidad).',
             '«Ojalá» nunca admite el condicional. Usa pres. subjuntivo para deseos posibles e imperf. subjuntivo para deseos poco probables.'),
            ('Quería que vengas vs. Quería que vinieras.',
             'Quería que <strong>vinieras</strong>.',
             'La concordancia temporal exige que tras un verbo principal en pasado, el subjuntivo vaya también en pasado: quería → <b>vinieras</b> (no «vengas»).'),
        ],
        summary=[
            ('Relativa + antecedente definido', 'indicativo: que habla / que tiene', 'Tengo una amiga que habla chino.'),
            ('Relativa + antecedente indefinido/negativo', 'subjuntivo: que hable / que tenga', 'Busco una amiga que hable chino.'),
            ('Conjunciones de finalidad', 'para que + subj. (siempre)', 'Estudia para que aprendas.'),
            ('Conjunciones condicionales', 'a menos que / con tal de que / siempre que + subj.', 'Iré, a menos que llueva.'),
            ('Concordancia temporal (presente)', 'verbo pres. → pres./perf. subj.', 'Espero que haya llegado.'),
            ('Concordancia temporal (pasado)', 'verbo pasado → imperf./pluscpf. subj.', 'Esperaba que hubiera llegado.'),
            ('Cortesía y exclamativas', 'quisiera / pudiera / ¡Que + subj.!', 'Quisiera hablar con usted. / ¡Que te mejores!'),
        ],
        ex1=dict(
            title='Elige el modo verbal correcto',
            questions=[
                ('Buscan a alguien que ______ gestionar redes sociales.', ['sabe', 'sabría', 'sepa', 'supo'], 2,
                 'Antecedente indefinido («alguien») → subjuntivo: <b>sepa</b>. No sabemos si esa persona existe.'),
                ('Cuando ______ los resultados, te los mandaré.', ['llegan', 'lleguen', 'llegarán', 'llegaban'], 1,
                 'Conjunción temporal con referencia futura → subjuntivo: <b>lleguen</b>.'),
                ('Firmé el contrato a condición de que ______ el sueldo inicial.', ['aumentan', 'aumentarán', 'aumenten', 'aumentarían'], 2,
                 '«A condición de que» exige subjuntivo: <b>aumenten</b>.'),
                ('No hay ningún alumno en esta clase que ______ el tema.', ['domina', 'domine', 'dominará', 'dominaba'], 1,
                 'Antecedente negativo («ningún alumno») → subjuntivo: <b>domine</b>.'),
                ('Le expliqué la situación para que ______ una decisión informada.', ['toma', 'tome', 'tomara', 'tomara'], 2,
                 'El verbo principal está en pasado y «para que» exige subjuntivo → imperfecto de subjuntivo: <b>tomara</b>.'),
                ('______ una solución que satisfaga a todas las partes.', ['¡Ojalá encuentren', '¡Ojalá encontrarán', '¡Ojalá encontrarían', '¡Ojalá encontraban'], 0,
                 '«Ojalá» + subjuntivo presente para expresar esperanza posible: <b>Ojalá encuentren</b>.'),
            ]
        ),
        ex2=dict(
            title='Completa con la forma correcta del subjuntivo',
            questions=[
                ('Aunque ______ (llover) todo el día, no cancelo el viaje.',
                 'llueva', ['llueva'],
                 '«Aunque» + subjuntivo expresa que la condición adversa no es un hecho conocido o es irrelevante para la decisión: <b>llueva</b>.'),
                ('Me pidió que le ______ (devolver, yo) el libro la semana siguiente.',
                 'devolviera', ['devolviera'],
                 'Verbo principal en pasado (pidió) + mandato indirecto → imperfecto de subjuntivo: <b>devolviera</b>.'),
                ('Espero que ya ______ (resolver, ellos) el problema cuando llegue.',
                 'hayan resuelto', ['hayan resuelto'],
                 'Pres. + anterioridad → perfecto de subjuntivo: <b>hayan resuelto</b>.'),
                ('No conocía a nadie que ______ (haber vivido) en ese país.',
                 'hubiera vivido', ['hubiera vivido'],
                 'Antecedente negativo + verbo principal en pasado → pluscuamperfecto de subjuntivo: <b>hubiera vivido</b>.'),
                ('______ (quisiera) hacer una consulta sobre su propuesta.',
                 'Quisiera', ['Quisiera'],
                 'Subjuntivo de cortesía en función de condicional suavizado: <b>Quisiera</b> (= querría, más formal).'),
            ]
        ),
        ex3=dict(
            title='Indicativo o subjuntivo: ¿cuál es correcto?',
            questions=[
                ('¿Cuál usa el modo correcto en una relativa con antecedente conocido?',
                 ['Necesito un asistente que hable inglés. (no sé si existe)',
                  'Tengo un asistente que habla inglés. (sé que existe)',
                  'Tengo un asistente que hable inglés.',
                  'Necesito un asistente que habla inglés.'],
                 1,
                 'Antecedente conocido y definido → indicativo: «Tengo un asistente que <b>habla</b> inglés.»'),
                ('¿Cuál usa «aunque» con el matiz de posibilidad (no certeza)?',
                 ['Aunque está cansado, trabaja.', 'Aunque esté cansado, trabajará.', 'Aunque estaría cansado, trabaja.', 'Aunque estará cansado, trabaja.'],
                 1,
                 '«Aunque» + subjuntivo = incluso si (posibilidad no confirmada): «Aunque <b>esté</b> cansado, trabajará.» Con indicativo afirma el hecho como cierto.'),
                ('¿Cuál respeta la concordancia temporal?',
                 ['Quería que vengas enseguida.', 'Quería que vinieras enseguida.', 'Quería que hayas venido.', 'Quería que vendrás enseguida.'],
                 1,
                 'Verbo principal en pasado (quería) → subjuntivo en pasado: <b>vinieras</b>.'),
                ('¿Cuál expresa cortesía mediante el subjuntivo imperfecto?',
                 ['Quiero pedirle algo.', 'Quisiera pedirle algo.', 'Querría pedirle algo.', 'Quería pedirle algo.'],
                 1,
                 '<b>Quisiera</b> es el subjuntivo imperfecto de querer usado como forma de cortesía equivalente al condicional, pero más formal.'),
                ('¿Cuál usa «ojalá» correctamente para un deseo del pasado ya imposible?',
                 ['Ojalá venga ayer.', 'Ojalá vendría ayer.', 'Ojalá hubiera venido.', 'Ojalá haya venido ayer.'],
                 2,
                 'Deseo imposible referido al pasado → «ojalá» + pluscuamperfecto de subjuntivo: <b>Ojalá hubiera venido</b>.'),
            ]
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('subj-c1-01', 'sepa', 'subjuntivo en relativa con antecedente indefinido', 'relativa indefinida → subjuntivo',
             'Busco a alguien que <b>sepa</b> ruso.', 'Busco a alguien que ______ ruso. (antecedente indefinido)', 'sepa'),
            ('subj-c1-02', 'llegue', 'subjuntivo tras «cuando» con referencia futura', 'cuando + futuro → subjuntivo',
             'Cuando <b>llegue</b> a casa, te llamo.', 'Cuando ______ a casa, te llamo. (futuro)', 'llegue'),
            ('subj-c1-03', 'llueva', 'subjuntivo tras «a menos que»', 'a menos que + subjuntivo',
             'Iré al parque a menos que <b>llueva</b>.', 'Iré al parque a menos que ______. (condición negativa)', 'llueva'),
            ('subj-c1-04', 'vinieras', 'imperfecto de subjuntivo en concordancia temporal (pasado)', 'pasado → imperf. subj.',
             'Me alegré de que <b>vinieras</b> a la reunión.', 'Me alegré de que ______ a la reunión. (concordancia temporal)', 'vinieras'),
            ('subj-c1-05', 'haya llegado', 'perfecto de subjuntivo: anterioridad con verbo pres.', 'pres. + anterioridad → perf. subj.',
             'Espero que ya <b>haya llegado</b> el paquete.', 'Espero que ya ______ el paquete. (anterior al presente)', 'haya llegado'),
            ('subj-c1-06', 'hubiera sabido', 'pluscuamperfecto de subjuntivo en exclamativa', 'ojalá + pluscpf. subj.',
             '¡Ojalá <b>hubiera sabido</b> la verdad antes!', '¡Ojalá ______ la verdad antes! (lamento pasado)', 'hubiera sabido'),
            ('subj-c1-07', 'quisiera', 'subjuntivo de cortesía (quisiera)', 'quisiera = forma cortés de querer',
             '<b>Quisiera</b> hablar con el responsable, por favor.', '______ hablar con el responsable. (cortesía formal)', 'quisiera'),
            ('subj-c1-08', 'entendieran', 'imperfecto de subjuntivo tras «para que» (verbo ppal. en pasado)', 'para que + imperf. subj.',
             'Lo repetí para que todos lo <b>entendieran</b>.', 'Lo repetí para que todos lo ______. (finalidad, pasado)', 'entendieran'),
        ],
    ),

    'hipoteticos-avanzados': dict(
        level='c1',
        section='grammar',
        num='G02',
        short='Condicionales Avanzadas',
        title='Las Oraciones Condicionales Avanzadas',
        subtitle='Domina los tipos mixtos, la inversión y las conjunciones condicionales avanzadas',
        slides=[
            ('Los tres tipos básicos: revisión rápida', None,
             '<p class="slide-explanation">A nivel C1 se parte de los tres tipos fundamentales para construir estructuras más complejas:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Tipo</th><th style="padding:8px;text-align:left">Estructura</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Tipo 1</b> (real)</td><td style="padding:8px">si + pres. ind. → futuro / imperativo</td><td style="padding:8px">Si <b>tienes</b> tiempo, <b>llámame</b>.</td></tr>'
             '<tr><td style="padding:8px"><b>Tipo 2</b> (hipotético)</td><td style="padding:8px">si + imperf. subj. → condicional simple</td><td style="padding:8px">Si <b>tuviera</b> dinero, <b>viajaría</b>.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Tipo 3</b> (irreal pasado)</td><td style="padding:8px">si + pluscpf. subj. → condicional compuesto</td><td style="padding:8px">Si <b>hubiera estudiado</b>, <b>habría aprobado</b>.</td></tr>'
             '</table>'
             '<p class="slide-explanation"><b>Recuerda:</b> nunca se usa el condicional en la cláusula con «si». Esta regla es absoluta en los tres tipos.</p>'),

            ('Tipo mixto: pasado irreal con consecuencia presente', None,
             '<p class="slide-explanation">Los <b>condicionales mixtos</b> combinan tiempos de dos tipos distintos. El más frecuente mezcla el tipo 3 (condición en el pasado) con el tipo 2 (consecuencia en el presente):</p>'
             '<div style="background:var(--paper);padding:16px;margin:16px 0;border-radius:6px">'
             '<p><b>Estructura:</b> si + pluscuamperfecto subj. → condicional simple</p>'
             '<p><b>Si hubiera</b> estudiado medicina, <b>sería</b> médico ahora.</p>'
             '<p><b>Si no hubiéramos</b> llegado tarde, <b>estaríamos</b> dentro del teatro.</p>'
             '</div>'
             '<p class="slide-explanation">La condición describe lo que no ocurrió en el pasado; la consecuencia describe el estado actual que esa acción habría producido. Son situaciones donde pasado y presente están vinculados causalmente.</p>'),

            ('Inversión: De + infinitivo compuesto', None,
             '<p class="slide-explanation">En un registro formal o literario, la cláusula con «si» puede sustituirse por una construcción con <b>de + infinitivo</b> (simple o compuesto). Esta inversión es especialmente frecuente con el pluscuamperfecto:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Con «si»</th><th style="padding:8px;text-align:left">Con inversión («de»)</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Si <b>hubiera sabido</b> la verdad, habría actuado diferente.</td><td style="padding:8px"><b>De haber sabido</b> la verdad, habría actuado diferente.</td></tr>'
             '<tr><td style="padding:8px">Si <b>tuviera</b> más experiencia, conseguiría el puesto.</td><td style="padding:8px"><b>De tener</b> más experiencia, conseguiría el puesto.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Si <b>hubiera llegado</b> antes, lo habría visto.</td><td style="padding:8px"><b>De haber llegado</b> antes, lo habría visto.</td></tr>'
             '</table>'
             '<p class="slide-explanation">La inversión elide la conjunción «si» y usa el infinitivo (o el infinitivo compuesto «haber + participio»). El tono es más culto y aparece con frecuencia en textos periodísticos y literarios.</p>'),

            ('Como si: comparativo irreal', None,
             '<p class="slide-explanation"><b>Como si</b> introduce una comparación que el hablante presenta como irreal o hipotética. El verbo que le sigue siempre va en subjuntivo:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Referencia temporal</th><th style="padding:8px;text-align:left">Tiempo de subj.</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Simultaneidad (irreal presente)</td><td style="padding:8px">Imperf. subj.</td><td style="padding:8px">Se comporta <b>como si fuera</b> el jefe.</td></tr>'
             '<tr><td style="padding:8px">Anterioridad (irreal pasado)</td><td style="padding:8px">Pluscpf. subj.</td><td style="padding:8px">Habla <b>como si lo hubiera visto</b> con sus propios ojos.</td></tr>'
             '</table>'
             '<p class="slide-explanation">No existe «como si + indicativo» ni «como si + condicional». Si alguien dice «como si sabe», es un error de interferencia con otras lenguas.</p>'),

            ('Conjunciones condicionales avanzadas', None,
             '<p class="slide-explanation">A nivel C1, es imprescindible manejar conjunciones condicionales más precisas que el simple «si»:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Conjunción</th><th style="padding:8px;text-align:left">Matiz</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>a menos que</b></td><td style="padding:8px">condición negativa</td><td style="padding:8px">Saldré, a menos que <b>llueva</b>.</td></tr>'
             '<tr><td style="padding:8px"><b>siempre y cuando</b></td><td style="padding:8px">condición estricta</td><td style="padding:8px">Te ayudaré, siempre y cuando <b>pongas</b> de tu parte.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>en caso de que</b></td><td style="padding:8px">eventualidad</td><td style="padding:8px">Llévate el paraguas en caso de que <b>llueva</b>.</td></tr>'
             '<tr><td style="padding:8px"><b>a no ser que</b></td><td style="padding:8px">condición negativa (+ formal)</td><td style="padding:8px">Lo haré, a no ser que <b>surja</b> algo urgente.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>con tal de que</b></td><td style="padding:8px">condición suficiente</td><td style="padding:8px">Firmo el acuerdo, con tal de que <b>incluyan</b> esa cláusula.</td></tr>'
             '</table>'
             '<p class="slide-explanation">Todas estas conjunciones exigen subjuntivo porque introducen condiciones que no son hechos reales en el momento de hablar.</p>'),
        ],
        traps=[
            ('Si habría venido, te lo hubiera dicho.',
             'Si <strong>hubiera venido</strong>, te lo habría dicho.',
             'Nunca se usa el condicional en la cláusula con «si». La condición irreal del pasado usa el pluscuamperfecto de subjuntivo: <b>si hubiera venido</b>.'),
            ('De haber sabido = Sí hubiera sabido',
             '<strong>De haber sabido</strong> = <strong>Si hubiera sabido</strong>',
             'La inversión «de + infinitivo compuesto» es equivalente a «si + pluscuamperfecto de subjuntivo». No es un error; es un registro más formal o literario.'),
            ('Como si sabe todo / como si sabría todo',
             'Como si <strong>supiera</strong> todo',
             '«Como si» exige siempre subjuntivo (imperfecto para el presente irreal, pluscuamperfecto para el pasado irreal). Nunca se usa con indicativo ni condicional.'),
            ('A menos que + indicativo: Vendré, a menos que llueve.',
             'Vendré, a menos que <strong>llueva</strong>.',
             '«A menos que» siempre exige subjuntivo porque introduce una condición hipotética. El indicativo sería un error grave.'),
            ('Tipo mixto: Si hubiera estudiado, sería médico → confundir con tipo 3 puro.',
             'Si <strong>hubiera estudiado</strong> (pasado), <strong>sería</strong> (ahora) médico.',
             'En el tipo mixto, la condición está en el pasado (pluscpf. subj.) pero la consecuencia es presente (condicional simple, no compuesto). La consecuencia en condicional compuesto («habría sido») indicaría consecuencia también en el pasado.'),
        ],
        summary=[
            ('Tipo 3 (irreal pasado)', 'si + pluscpf. subj. → cond. compuesto', 'Si hubiera estudiado, habría aprobado.'),
            ('Tipo mixto', 'si + pluscpf. subj. → cond. simple', 'Si hubiera nacido allí, hablaría ese idioma.'),
            ('Inversión formal', 'de + inf. compuesto → cond. compuesto', 'De haberlo sabido, habría actuado diferente.'),
            ('Como si (presente irreal)', 'como si + imperf. subj.', 'Habla como si fuera experto.'),
            ('Como si (pasado irreal)', 'como si + pluscpf. subj.', 'Habla como si lo hubiera visto.'),
            ('Conjunciones + subj.', 'a menos que / siempre y cuando / en caso de que…', 'Iré, a menos que surja un imprevisto.'),
        ],
        ex1=dict(
            title='Elige la forma correcta en las condicionales avanzadas',
            questions=[
                ('Si ______ (estudiar, yo) más de joven, habría llegado más lejos.',
                 ['hubiera estudiado', 'habría estudiado', 'estudié', 'estudiaba'], 0,
                 'Condición irreal pasada (tipo 3): si + <b>pluscuamperfecto de subjuntivo</b>: <b>hubiera estudiado</b>.'),
                ('De ______ (saber) la respuesta, la habría dicho sin dudar.',
                 ['haber sabido', 'saber', 'sabido', 'haber saber'], 0,
                 'Inversión formal equivalente a «si hubiera sabido»: <b>de haber sabido</b> (de + infinitivo compuesto).'),
                ('Se comporta ______ el mejor del equipo, aunque rara vez da el cien por cien.',
                 ['como si fuera', 'como si es', 'como si sería', 'como si ha sido'], 0,
                 '«Como si» + imperfecto de subjuntivo para la comparación irreal simultánea: <b>como si fuera</b>.'),
                ('Te prestaré el coche, siempre y cuando ______ (devolvérmelo) antes del domingo.',
                 ['me lo devuelvas', 'me lo devolverás', 'me lo hayas devuelto', 'me lo devolverías'], 0,
                 '«Siempre y cuando» exige subjuntivo: <b>me lo devuelvas</b>.'),
                ('Si ______ (nacer, ella) en otro país, no estaría aquí ahora.',
                 ['hubiera nacido', 'habría nacido', 'naciera', 'nació'], 0,
                 'Tipo mixto: condición en el pasado → pluscpf. subj.: <b>hubiera nacido</b>; consecuencia en el presente → condicional simple: «estaría».'),
                ('Llévate el abrigo en caso de que ______ (hacer) frío esta noche.',
                 ['haga', 'hace', 'hará', 'haría'], 0,
                 '«En caso de que» siempre exige subjuntivo: <b>haga</b>.'),
            ]
        ),
        ex2=dict(
            title='Completa las oraciones condicionales',
            questions=[
                ('Si ______ (tener, yo) más experiencia entonces, no habría cometido ese error.',
                 'hubiera tenido', ['hubiera tenido'],
                 'Condición irreal pasada (tipo 3): si + pluscuamperfecto de subjuntivo → <b>hubiera tenido</b>.'),
                ('______ (llegar) a tiempo, no habrías perdido el vuelo. (inversión formal)',
                 'De haber llegado', ['De haber llegado'],
                 'Inversión formal: de + infinitivo compuesto: <b>De haber llegado</b> (= Si hubieras llegado).'),
                ('Lo haré, a no ser que ______ (surgir) un imprevisto de última hora.',
                 'surja', ['surja'],
                 '«A no ser que» exige subjuntivo: <b>surja</b>.'),
                ('Hablas ______ (como si / conocer) este barrio de toda la vida.',
                 'como si conocieras', ['como si conocieras'],
                 '«Como si» + imperfecto de subjuntivo (presente irreal): <b>como si conocieras</b>.'),
                ('Si ______ (estudiar, tú) arquitectura, ahora tendrías otro perfil profesional.',
                 'hubieras estudiado', ['hubieras estudiado'],
                 'Tipo mixto: condición pasada irreal → pluscpf. subj.: <b>hubieras estudiado</b>; consecuencia presente → condicional simple.'),
            ]
        ),
        ex3=dict(
            title='Identifica la estructura condicional correcta',
            questions=[
                ('¿Cuál es un condicional tipo 3 correctamente formado?',
                 ['Si hubiera llegado antes, encontraría sitio.', 'Si habría llegado antes, habría encontrado sitio.', 'Si hubiera llegado antes, habría encontrado sitio.', 'Si llegara antes, habría encontrado sitio.'],
                 2,
                 'Tipo 3: si + <b>pluscuamperfecto de subjuntivo</b> → <b>condicional compuesto</b>: «Si hubiera llegado…, habría encontrado».'),
                ('¿Cuál es un condicional mixto correctamente formado?',
                 ['Si hubiera estudiado medicina, habría sido médico.', 'Si hubiera estudiado medicina, sería médico ahora.', 'Si estudiara medicina, sería médico.', 'Si hubiera estudiado medicina, era médico.'],
                 1,
                 'Tipo mixto: pasado irreal (pluscpf. subj.) + consecuencia en el presente (condicional <b>simple</b>): «Si hubiera estudiado…, <b>sería</b> médico ahora.»'),
                ('¿Cuál usa la inversión formal correctamente?',
                 ['Si de haber sabido la noticia, habría llamado.', 'De haber sabido la noticia, habría llamado.', 'De habiendo sabido la noticia, habría llamado.', 'De saber la noticia ayer, habría llamado.'],
                 1,
                 'Inversión: <b>de + infinitivo compuesto</b> (haber + participio) al inicio: «<b>De haber sabido</b> la noticia, habría llamado.»'),
                ('¿Qué diferencia hay entre «Si viniera» y «Si hubiera venido»?',
                 ['Ninguna; son intercambiables.', '«Si viniera» es hipótesis presente/futura; «Si hubiera venido» es hipótesis en el pasado.', '«Si viniera» es más formal.', '«Si hubiera venido» expresa una condición futura.'],
                 1,
                 '<b>Si viniera</b> → hipótesis presente o futura (tipo 2). <b>Si hubiera venido</b> → hipótesis irreal en el pasado (tipo 3). No son intercambiables.'),
                ('¿Cuál usa «como si» correctamente para un pasado irreal?',
                 ['Habla como si supiera todo.', 'Habla como si sabe todo.', 'Habla como si hubiera sabido todo.', 'Habla como si habrá sabido todo.'],
                 2,
                 'Pasado irreal con «como si» → pluscuamperfecto de subjuntivo: «Habla <b>como si hubiera sabido</b> todo.» (La opción A usa imperf. subj., que sería el presente irreal.)'),
            ]
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('hipot-c1-01', 'hubiera llegado', 'pluscuamperfecto de subjuntivo en condicional tipo 3', 'tipo 3: si + pluscpf. subj.',
             'Si <b>hubiera llegado</b> antes, habría visto el espectáculo.', 'Si ______ antes, habría visto el espectáculo. (tipo 3)', 'hubiera llegado'),
            ('hipot-c1-02', 'habría aprobado', 'condicional compuesto: consecuencia tipo 3', 'tipo 3 → cond. compuesto',
             'Si hubiera estudiado, <b>habría aprobado</b> el examen.', 'Si hubiera estudiado, ______ el examen. (consecuencia tipo 3)', 'habría aprobado'),
            ('hipot-c1-03', 'sería', 'condicional simple en tipo mixto (consecuencia presente)', 'tipo mixto → cond. simple',
             'Si hubiera nacido en Madrid, <b>sería</b> madrileño ahora.', 'Si hubiera nacido en Madrid, ______ madrileño ahora. (consecuencia presente)', 'sería'),
            ('hipot-c1-04', 'de haber sabido', 'inversión formal equivalente a «si hubiera sabido»', 'de + inf. compuesto (inversión)',
             '<b>De haber sabido</b> la noticia, te habría llamado.', '______ la noticia, te habría llamado. (inversión formal)', 'de haber sabido'),
            ('hipot-c1-05', 'como si fuera', 'como si + imperfecto subj. (presente irreal)', 'como si + imperf. subj.',
             'Se viste <b>como si fuera</b> a una gala de premios.', 'Se viste ______ a una gala de premios. (comparación irreal)', 'como si fuera'),
            ('hipot-c1-06', 'llueva', 'subjuntivo tras «a menos que»', 'a menos que + subj.',
             'Saldremos, a menos que <b>llueva</b> mucho.', 'Saldremos, a menos que ______ mucho. (condición negativa)', 'llueva'),
            ('hipot-c1-07', 'surja', 'subjuntivo tras «en caso de que»', 'en caso de que + subj.',
             'Llama al médico en caso de que <b>surja</b> alguna complicación.', 'Llama al médico en caso de que ______ alguna complicación.', 'surja'),
            ('hipot-c1-08', 'pongas', 'subjuntivo tras «siempre y cuando»', 'siempre y cuando + subj.',
             'Te ayudaré, siempre y cuando <b>pongas</b> de tu parte.', 'Te ayudaré, siempre y cuando ______ de tu parte. (condición estricta)', 'pongas'),
        ],
    ),

    'estilo-indirecto-c1': dict(
        level='c1',
        section='grammar',
        num='G03',
        short='Estilo Indirecto C1',
        title='El Estilo Indirecto Avanzado',
        subtitle='Reporta enunciados, mandatos y preguntas con los cambios de tiempo, pronombre y adverbio',
        slides=[
            ('Verbos de reporte y cambios de tiempo', None,
             '<p class="slide-explanation">En el estilo indirecto, el verbo de reporte introduce la cita. Los tiempos verbales cambian cuando el verbo de reporte está en <b>pasado</b>:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Estilo directo</th><th style="padding:8px;text-align:left">Estilo indirecto (reporte en pasado)</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">«<b>Vengo</b> mañana.» (presente)</td><td style="padding:8px">Dijo que <b>venía</b> al día siguiente. (imperfecto)</td></tr>'
             '<tr><td style="padding:8px">«<b>He llegado</b>.» (pret. perfecto)</td><td style="padding:8px">Dijo que <b>había llegado</b>. (pluscpf.)</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">«<b>Vendré</b>.» (futuro)</td><td style="padding:8px">Dijo que <b>vendría</b>. (condicional)</td></tr>'
             '<tr><td style="padding:8px">«<b>Vine</b> ayer.» (indefinido)</td><td style="padding:8px">Dijo que <b>había venido</b> el día anterior. (pluscpf.)</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">«<b>Estudié</b> mucho.» (indefinido)</td><td style="padding:8px">Dijo que <b>había estudiado</b> mucho. (pluscpf.)</td></tr>'
             '</table>'
             '<p class="slide-explanation">Si el verbo de reporte está en <b>presente</b> («dice que», «afirma que»), los tiempos no cambian: «Dice que <b>viene</b> mañana.»</p>'),

            ('Mandatos en estilo indirecto', None,
             '<p class="slide-explanation">Los mandatos del estilo directo se transforman con verbos de reporte + <b>que + subjuntivo</b>:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Verbo de reporte</th><th style="padding:8px;text-align:left">Estilo directo</th><th style="padding:8px;text-align:left">Estilo indirecto</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>pedir</b></td><td style="padding:8px">«<b>Ven</b> aquí.»</td><td style="padding:8px">Me pidió que <b>fuera</b> allí.</td></tr>'
             '<tr><td style="padding:8px"><b>decir</b> (mandato)</td><td style="padding:8px">«<b>Calla.</b>»</td><td style="padding:8px">Me dijo que me <b>callara</b>.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>ordenar</b></td><td style="padding:8px">«<b>Siéntense.</b>»</td><td style="padding:8px">Ordenó que se <b>sentaran</b>.</td></tr>'
             '<tr><td style="padding:8px"><b>prohibir</b></td><td style="padding:8px">«<b>No entres.</b>»</td><td style="padding:8px">Prohibió que <b>entrara</b>.</td></tr>'
             '</table>'
             '<p class="slide-explanation"><b>Clave:</b> «dijo que vendría» (predicción, indicativo) vs. «dijo que fuera» (mandato/petición, subjuntivo). El modo diferencia la función del enunciado.</p>'),

            ('Preguntas en estilo indirecto', None,
             '<p class="slide-explanation">Las preguntas se convierten en oraciones subordinadas introducidas por <b>si</b> (preguntas totales) o por <b>un pronombre/adverbio interrogativo</b> (preguntas parciales):</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Tipo</th><th style="padding:8px;text-align:left">Estilo directo</th><th style="padding:8px;text-align:left">Estilo indirecto</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Total (sí/no)</td><td style="padding:8px">«¿<b>Vienes</b> mañana?»</td><td style="padding:8px">Preguntó <b>si</b> vendría al día siguiente.</td></tr>'
             '<tr><td style="padding:8px">Parcial (qué)</td><td style="padding:8px">«¿<b>Qué</b> quieres?»</td><td style="padding:8px">Preguntó <b>qué</b> quería.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Parcial (cuándo)</td><td style="padding:8px">«¿<b>Cuándo</b> llegaste?»</td><td style="padding:8px">Preguntó <b>cuándo</b> había llegado.</td></tr>'
             '<tr><td style="padding:8px">Parcial (dónde)</td><td style="padding:8px">«¿<b>Dónde</b> vives?»</td><td style="padding:8px">Quiso saber <b>dónde</b> vivía.</td></tr>'
             '</table>'
             '<p class="slide-explanation">En las preguntas indirectas, el orden es sujeto-verbo (sin inversión): «preguntó <b>qué quería</b>», no «preguntó qué quería él» con inversión.</p>'),

            ('Cambios de pronombre, posesivo y adverbio', None,
             '<p class="slide-explanation">Al pasar al estilo indirecto cambian también los pronombres, los posesivos y los adverbios de tiempo y lugar:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Estilo directo</th><th style="padding:8px;text-align:left">Estilo indirecto</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">yo → <b>él/ella</b></td><td style="padding:8px">«Yo vengo» → Dijo que <b>él</b> venía.</td></tr>'
             '<tr><td style="padding:8px">mi / mío → <b>su / suyo</b></td><td style="padding:8px">«mi libro» → dijo que <b>su</b> libro…</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">aquí → <b>allí / allá</b></td><td style="padding:8px">«Estoy aquí» → Dijo que estaba <b>allí</b>.</td></tr>'
             '<tr><td style="padding:8px">hoy → <b>ese día</b></td><td style="padding:8px">«Lo haré hoy» → Dijo que lo haría <b>ese día</b>.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">mañana → <b>al día siguiente</b></td><td style="padding:8px">«Vendré mañana» → Dijo que vendría <b>al día siguiente</b>.</td></tr>'
             '<tr><td style="padding:8px">ayer → <b>el día anterior</b></td><td style="padding:8px">«Lo hice ayer» → Dijo que lo había hecho <b>el día anterior</b>.</td></tr>'
             '</table>'),

            ('Verbos de duda y temor en estilo indirecto', None,
             '<p class="slide-explanation">Los verbos que expresan duda, temor o negación de certeza rigen subjuntivo en la subordinada, incluso en el estilo indirecto:</p>'
             '<div style="background:var(--paper);padding:16px;margin:16px 0;border-radius:6px">'
             '<p><b>temer que + subj.:</b> Temía que no <b>llegara</b> a tiempo.</p>'
             '<p><b>dudar de que + subj.:</b> Dudaba de que <b>fuera</b> verdad.</p>'
             '<p><b>negar que + subj.:</b> Negó que <b>hubiera</b> dicho eso.</p>'
             '<p><b>no creer que + subj.:</b> No creía que <b>pudiera</b> hacerlo.</p>'
             '</div>'
             '<p class="slide-explanation">Contrasta con los verbos de certeza afirmativa, que rigen indicativo incluso en el estilo indirecto: «Afirmó que <b>era</b> verdad.» / «Señaló que el precio <b>había subido</b>.»</p>'
             '<p class="slide-explanation">Verbos de reporte de alta frecuencia: <b>decir, afirmar, sostener, añadir, señalar, indicar, recalcar, aclarar, matizar, insistir en que</b>.</p>'),
        ],
        traps=[
            ('Dijo que vendría (orden) / Dijo que vendrás',
             'Mandato: dijo que <strong>viniera</strong>; predicción: dijo que <strong>vendría</strong>.',
             '«Dijo que vendría» = predijo algo (indicativo condicional). «Dijo que viniera» = mandato o petición (subjuntivo). El modo cambia el significado por completo.'),
            ('Preguntó dónde vives. (sin cambio de tiempo)',
             'Preguntó dónde <strong>vivías</strong>.',
             'Con verbo de reporte en pasado, el verbo subordinado también pasa a pasado: «vives» → <b>vivías</b>.'),
            ('Preguntó si ¿vendrías? (con signos de interrogación)',
             'Preguntó <strong>si</strong> vendría. (sin signos)',
             'Las preguntas en estilo indirecto son oraciones subordinadas, no preguntas directas. No llevan signos de interrogación ni inversión verbo-sujeto.'),
            ('Dijo que hoy vendría → sin cambio de adverbio',
             'Dijo que <strong>ese día</strong> vendría.',
             'Al pasar al estilo indirecto, «hoy» se convierte en «ese día», «mañana» en «al día siguiente», «aquí» en «allí».'),
            ('Negó que era culpable.',
             'Negó que <strong>fuera</strong> culpable.',
             '«Negar que» expresa negación de certeza y exige subjuntivo: <b>fuera</b>, no «era».'),
        ],
        summary=[
            ('Cambio presente → imperfecto', 'dice → dijo que + imperfecto', '«Vengo» → Dijo que venía.'),
            ('Cambio perfecto → pluscuamperfecto', 'ha venido → dijo que había venido', '«He llegado» → Dijo que había llegado.'),
            ('Cambio futuro → condicional', 'vendré → dijo que vendría', '«Vendré» → Dijo que vendría.'),
            ('Mandatos (pedir / decir / ordenar)', 'pedir/decir que + imperf. subj.', 'Me pidió que lo llamara.'),
            ('Preguntas totales', 'preguntar si + subord.', '«¿Vienes?» → Preguntó si vendría.'),
            ('Preguntas parciales', 'preguntar qué/cuándo/dónde + subord.', '«¿Cuándo llegaste?» → Preguntó cuándo había llegado.'),
            ('Adverbios y pronombres', 'aquí→allí / hoy→ese día / mañana→al día siguiente', 'Dijo que volvería al día siguiente.'),
        ],
        ex1=dict(
            title='Transforma al estilo indirecto: elige la opción correcta',
            questions=[
                ('Estilo directo: «Trabajo todos los días.» → Ella dijo que ______.',
                 ['trabaja todos los días', 'trabajaba todos los días', 'trabajará todos los días', 'trabajaría todos los días'], 1,
                 'Presente → imperfecto en el estilo indirecto con reporte en pasado: <b>trabajaba</b>.'),
                ('Estilo directo: «¿Cuándo llegarás?» → Me preguntó cuándo ______.',
                 ['llegarías', 'llegaré', 'llegas', 'llegué'], 0,
                 'Futuro en pregunta parcial con reporte en pasado → condicional: <b>llegarías</b>.'),
                ('Estilo directo: «Cállate.» (mandato) → Me dijo que ______.',
                 ['me callara', 'me callaré', 'me callaría', 'me callo'], 0,
                 'Mandato → dijo que + imperfecto de subjuntivo: <b>me callara</b>.'),
                ('Estilo directo: «He terminado el informe.» → Afirmó que ______.',
                 ['ha terminado el informe', 'termina el informe', 'había terminado el informe', 'terminaría el informe'], 2,
                 'Pret. perfecto → pluscuamperfecto: <b>había terminado</b>.'),
                ('Estilo directo: «¿Tienes hermanos?» → Me preguntó si ______.',
                 ['tengo hermanos', 'tenía hermanos', 'tendré hermanos', 'tendría hermanos'], 1,
                 'Pregunta total con reporte en pasado → si + imperfecto: <b>tenía hermanos</b>.'),
                ('Temía que ______ (ser) demasiado tarde cuando llegáramos.',
                 ['sería', 'era', 'sea', 'fuera'], 3,
                 '«Temer que» exige subjuntivo; verbo principal en pasado → imperfecto de subjuntivo: <b>fuera</b>.'),
            ]
        ),
        ex2=dict(
            title='Transforma las frases al estilo indirecto',
            questions=[
                ('Estilo directo: «Llegaré mañana.» → Dijo que ______.',
                 'llegaría al día siguiente', ['llegaría al día siguiente', 'llegaría el día siguiente'],
                 'Futuro → condicional; «mañana» → <b>al día siguiente</b>: <b>llegaría al día siguiente</b>.'),
                ('Estilo directo: «No entres.» (prohibición) → Le prohibió que ______.',
                 'entrara', ['entrara'],
                 '«Prohibir que» + imperfecto de subjuntivo: <b>entrara</b>.'),
                ('Estilo directo: «¿Dónde vives?» → Le preguntó dónde ______.',
                 'vivía', ['vivía'],
                 'Pregunta parcial con reporte en pasado: «vives» → <b>vivía</b>.'),
                ('Estilo directo: «He visto a tu hermano hoy.» → Dijo que ______ a mi hermano ______.',
                 'había visto / ese día', ['había visto ese día', 'había visto / ese día'],
                 'Pret. perfecto → pluscpf.: <b>había visto</b>; «hoy» → <b>ese día</b>.'),
                ('Negó que ______ (decir) esas palabras.',
                 'hubiera dicho', ['hubiera dicho'],
                 '«Negar que» + subjuntivo; contexto pasado → pluscuamperfecto de subjuntivo: <b>hubiera dicho</b>.'),
            ]
        ),
        ex3=dict(
            title='Identifica el estilo indirecto correcto',
            questions=[
                ('Estilo directo: «Vendré el martes.» ¿Cuál es la transformación correcta?',
                 ['Dijo que vendrá el martes.', 'Dijo que vendría el martes.', 'Dijo que viene el martes.', 'Dijo que viniera el martes.'],
                 1,
                 'Futuro → condicional con reporte en pasado: «Dijo que <b>vendría</b> el martes.»'),
                ('¿Cuál convierte correctamente una pregunta total al estilo indirecto?',
                 ['Me preguntó: ¿tienes coche?', 'Me preguntó si tenía coche.', 'Me preguntó que si tenía coche.', 'Me preguntó sí tenía coche.'], 1,
                 'Pregunta total → si + indicativo (en pasado): «Me preguntó <b>si tenía</b> coche.» Sin comillas ni «que» antes del «si».'),
                ('¿Cuál transforma correctamente un mandato?',
                 ['Me dijo que abres la puerta.', 'Me dijo que abrirías la puerta.', 'Me dijo que abriera la puerta.', 'Me dijo que abriré la puerta.'],
                 2,
                 'Mandato → decir que + imperfecto de subjuntivo: «Me dijo que <b>abriera</b> la puerta.»'),
                ('¿Cuál cambia correctamente el adverbio de tiempo?',
                 ['Dijo que vendría hoy.', 'Dijo que vendría ese día.', 'Dijo que vendría aquí.', 'Dijo que vendría entonces mañana.'],
                 1,
                 '«Hoy» → <b>ese día</b> en el estilo indirecto cuando el reporte es en pasado y en otro momento.'),
                ('¿Qué diferencia hay entre «dijo que vendría» y «dijo que viniera»?',
                 ['Ninguna; son equivalentes.', '«Dijo que vendría» es una predicción (indicativo); «dijo que viniera» es una orden o petición (subjuntivo).', '«Dijo que viniera» es más formal.', '«Dijo que vendría» solo se usa en preguntas.'],
                 1,
                 '<b>Vendría</b> (condicional) = predicción o declaración. <b>Viniera</b> (subjuntivo imperfecto) = mandato, petición o deseo expresado por el sujeto del verbo de reporte.'),
            ]
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('ei-c1-01', 'venía', 'cambio de tiempo: presente → imperfecto en estilo indirecto', 'pres. → imperfecto (reporte pasado)',
             'Dijo que <b>venía</b> al día siguiente.', '«Vengo mañana» → Dijo que ______ al día siguiente. (est. indirecto)', 'venía'),
            ('ei-c1-02', 'había llegado', 'cambio: pret. perfecto → pluscuamperfecto', 'perfecto → pluscpf.',
             'Afirmó que <b>había llegado</b> el día anterior.', '«He llegado ayer» → Afirmó que ______ el día anterior.', 'había llegado'),
            ('ei-c1-03', 'vendría', 'cambio: futuro → condicional', 'futuro → condicional',
             'Señaló que <b>vendría</b> al día siguiente.', '«Vendré mañana» → Señaló que ______ al día siguiente.', 'vendría'),
            ('ei-c1-04', 'fuera', 'mandato en estilo indirecto: pedir que + imperf. subj.', 'pedir que + imperf. subj.',
             'Me pidió que <b>fuera</b> a verle esa tarde.', '«Ven a verme.» → Me pidió que ______ a verle esa tarde.', 'fuera'),
            ('ei-c1-05', 'si vendría', 'pregunta total en estilo indirecto: preguntar si + cond.', 'preguntar si + condicional',
             'Me preguntó <b>si vendría</b> a la reunión.', '«¿Vendrás a la reunión?» → Me preguntó ______ a la reunión.', 'si vendría'),
            ('ei-c1-06', 'cuándo había llegado', 'pregunta parcial en estilo indirecto', 'preguntar cuándo + pluscpf.',
             'Quiso saber <b>cuándo había llegado</b> el paquete.', '«¿Cuándo llegó el paquete?» → Quiso saber ______ el paquete.', 'cuándo había llegado'),
            ('ei-c1-07', 'ese día', 'cambio de adverbio: hoy → ese día', 'hoy → ese día',
             'Dijo que lo terminaría <b>ese día</b>.', '«Lo terminaré hoy» → Dijo que lo terminaría ______. (adverbio de tiempo)', 'ese día'),
            ('ei-c1-08', 'hubiera dicho', 'negar que + pluscpf. de subjuntivo', 'negar que + pluscpf. subj.',
             'Negó que lo <b>hubiera dicho</b> delante de todos.', 'Negó que lo ______ delante de todos. (negación + subj. pasado)', 'hubiera dicho'),
        ],
    ),

    'modalidad-verbal': dict(
        level='c1',
        section='grammar',
        num='G04',
        short='Modalidad Verbal',
        title='La Modalidad Verbal — Deber, Poder, Haber de/que y semi-modales',
        subtitle='Expresa obligación, probabilidad y posibilidad con precisión usando los verbos modales',
        slides=[
            ('Deber: obligación vs. probabilidad', None,
             '<p class="slide-explanation">«<b>Deber</b>» tiene dos usos fundamentales que se distinguen principalmente por el contexto y, en muchos dialectos, por la presencia o ausencia de la preposición <b>de</b>:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Estructura</th><th style="padding:8px;text-align:left">Significado</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>deber + inf.</b></td><td style="padding:8px">Obligación moral o normativa</td><td style="padding:8px">Debes entregar el proyecto a tiempo.</td></tr>'
             '<tr><td style="padding:8px"><b>deber de + inf.</b></td><td style="padding:8px">Probabilidad / deducción</td><td style="padding:8px">Debe de ser tarde; no hay nadie.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>debería + inf.</b></td><td style="padding:8px">Obligación suavizada / consejo</td><td style="padding:8px">Deberías llamar antes de venir.</td></tr>'
             '<tr><td style="padding:8px"><b>debiste + haber + part.</b></td><td style="padding:8px">Obligación pasada no cumplida</td><td style="padding:8px">Debiste haber llamado ayer.</td></tr>'
             '</table>'
             '<p class="slide-explanation">En el español coloquial actual, la distinción entre «deber + inf.» y «deber de + inf.» se está difuminando, pero en el registro formal y escrito se mantiene.</p>'),

            ('Poder: posibilidad, permiso y probabilidad', None,
             '<p class="slide-explanation">«<b>Poder</b>» expresa tres significados principales según el contexto:</p>'
             '<div style="background:var(--paper);padding:16px;margin:16px 0;border-radius:6px">'
             '<p><b>Posibilidad:</b> Mañana <b>puede</b> llover. / <b>Puede que llueva</b>. (+ subjuntivo)</p>'
             '<p><b>Permiso:</b> ¿<b>Puedo</b> salir un momento? / No <b>puedes</b> entrar sin acreditación.</p>'
             '<p><b>Capacidad:</b> <b>Puede</b> hablar cuatro idiomas.</p>'
             '</div>'
             '<p class="slide-explanation">Construcción especial: <b>Puede que + subjuntivo</b> expresa posibilidad o probabilidad sin especificar sujeto:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Probabilidad alta</th><th style="padding:8px;text-align:left">Probabilidad media</th><th style="padding:8px;text-align:left">Posibilidad en el pasado</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Puede que <b>llegue</b> hoy.</td><td style="padding:8px">Podría <b>ser</b> que viniera.</td><td style="padding:8px">Pudo <b>haber llegado</b> ya.</td></tr>'
             '</table>'),

            ('Haber de y tener que: obligación', None,
             '<p class="slide-explanation">Tres construcciones expresan obligación con matices distintos de intensidad y registro:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Construcción</th><th style="padding:8px;text-align:left">Matiz</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>tener que + inf.</b></td><td style="padding:8px">Obligación personal fuerte</td><td style="padding:8px">Tengo que terminar el informe hoy.</td></tr>'
             '<tr><td style="padding:8px"><b>haber que + inf.</b></td><td style="padding:8px">Obligación impersonal</td><td style="padding:8px">Hay que respetar las normas.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>haber de + inf.</b></td><td style="padding:8px">Obligación moderada, formal o literaria</td><td style="padding:8px">He de entregar el informe mañana.</td></tr>'
             '</table>'
             '<p class="slide-explanation"><b>Haber que</b> es siempre impersonal: solo existe en 3.ª persona singular («hay que», «había que», «habrá que»). <b>Tener que</b> y <b>haber de</b> se conjugan con todos los sujetos.</p>'),

            ('Semi-modales: querer, soler y acostumbrar', None,
             '<p class="slide-explanation">Además de los modales puros, el español dispone de semi-modales que funcionan de forma similar:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Semi-modal</th><th style="padding:8px;text-align:left">Significado</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>querer + inf.</b></td><td style="padding:8px">Deseo / voluntad</td><td style="padding:8px">Quiero aprender a pintar.</td></tr>'
             '<tr><td style="padding:8px"><b>soler + inf.</b></td><td style="padding:8px">Habitualidad (sin «de»)</td><td style="padding:8px">Suelo levantarme a las siete.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>acostumbrar (a) + inf.</b></td><td style="padding:8px">Habitualidad / costumbre</td><td style="padding:8px">Acostumbra a salir a correr por las mañanas.</td></tr>'
             '</table>'
             '<p class="slide-explanation"><b>Soler</b> es defectivo: carece de futuro, condicional y formas no personales; solo se usa en presente e imperfecto. <b>Acostumbrar a</b> es más frecuente en el español americano y catalanohablante.</p>'),

            ('Escala de modalidad: de la posibilidad a la obligación', None,
             '<p class="slide-explanation">Los modales se ordenan en una escala de fuerza deóntica (obligación) y epistémica (probabilidad):</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Fuerza</th><th style="padding:8px;text-align:left">Obligación/necesidad</th><th style="padding:8px;text-align:left">Probabilidad/deducción</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Alta</td><td style="padding:8px">deber + inf. / tener que + inf.</td><td style="padding:8px">debe de + inf. (certeza casi total)</td></tr>'
             '<tr><td style="padding:8px">Media</td><td style="padding:8px">haber de + inf. / debería + inf.</td><td style="padding:8px">debería de + inf. / puede que + subj.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Baja</td><td style="padding:8px">poder + inf. (posibilidad, no oblig.)</td><td style="padding:8px">podría + inf. / quizás + subj.</td></tr>'
             '</table>'
             '<p class="slide-explanation">Dominar esta escala permite matizar el discurso con precisión: no es lo mismo «debes llamar» (obligación fuerte) que «deberías llamar» (consejo) o «podrías llamar» (sugerencia suave).</p>'),
        ],
        traps=[
            ('Debe ser tarde (probabilidad) vs. Debe de ser tarde',
             '<strong>Debe de ser</strong> tarde (probabilidad) / <strong>Debe ser</strong> tarde (también aceptado en muchas variedades).',
             'La norma prescriptiva distingue «deber + inf.» (obligación) de «deber de + inf.» (probabilidad). Sin embargo, en la práctica ambas formas se usan para la probabilidad. En un examen de nivel C1, emplea «deber de» para la deducción.'),
            ('Hay que estudiar → yo hay que estudiar',
             '<strong>Hay que</strong> estudiar (impersonal, sin sujeto)',
             '«Haber que» es siempre impersonal: no lleva sujeto expreso. Para la obligación personal, usa «tener que» o «haber de»: <b>Tengo que</b> estudiar.'),
            ('Suelo de ir al gimnasio.',
             '<strong>Suelo ir</strong> al gimnasio.',
             '«Soler» no lleva preposición: <b>suelo ir</b>, no «suelo de ir». Confusión frecuente con «dejar de», «acabar de».'),
            ('Pudo llegar ya (posibilidad pasada)',
             '<strong>Pudo haber llegado</strong> ya.',
             'Para expresar una posibilidad referida al pasado, se usa «poder» conjugado + <b>haber + participio</b>: <b>Pudo haber llegado</b>. «Pudo llegar» expresa capacidad o permiso en el pasado, no posibilidad deductiva.'),
            ('Debiste llamar ayer (obligación pasada incumplida)',
             '<strong>Debiste haber llamado</strong> ayer.',
             'La obligación pasada no cumplida se expresa con «deber» en indefinido + <b>haber + participio</b>: <b>debiste haber llamado</b>. En el español de algunos países, «debiste llamar» también se acepta, pero la forma compuesta es más precisa.'),
        ],
        summary=[
            ('deber + inf.', 'obligación moral/normativa', 'Debes respetar el plazo acordado.'),
            ('deber de + inf.', 'probabilidad o deducción', 'Debe de ser muy tarde; no hay nadie.'),
            ('tener que + inf.', 'obligación personal fuerte', 'Tengo que presentar el informe hoy.'),
            ('haber que + inf.', 'obligación impersonal', 'Hay que leer las instrucciones.'),
            ('haber de + inf.', 'obligación moderada o formal', 'He de consultar con mi abogado.'),
            ('puede que + subj.', 'posibilidad sin sujeto especificado', 'Puede que lleguen tarde.'),
            ('soler + inf.', 'habitualidad (sin «de»)', 'Suele llegar al trabajo antes que nadie.'),
        ],
        ex1=dict(
            title='Elige el modal o la estructura correcta',
            questions=[
                ('______ entregar el proyecto antes del viernes o perderás puntos.', ['Hay que', 'Debes', 'Sueles', 'Puedes que'], 1,
                 'Obligación personal dirigida a un sujeto concreto (tú) → <b>Debes</b> + infinitivo.'),
                ('______ ser muy tarde; las calles están completamente vacías.',
                 ['Debe', 'Debe de', 'Debería de', 'Tiene que'], 1,
                 'Probabilidad o deducción lógica → <b>Debe de</b> ser tarde.'),
                ('______ respetar las normas del recinto, sin excepción.',
                 ['Hay que', 'Suelo', 'Debes de', 'He de'], 0,
                 'Obligación impersonal (sin sujeto específico) → <b>Hay que</b> + infinitivo.'),
                ('______ levantarme temprano los lunes; es mi costumbre.',
                 ['Debo de', 'Suelo', 'He de', 'Puede que'], 1,
                 'Habitualidad → <b>Suelo</b> + infinitivo (sin «de»).'),
                ('______ haberme llamado antes; ahora es demasiado tarde.',
                 ['Deberías', 'Deberías de haber llamado', 'Debiste haber llamado', 'Debiste'], 2,
                 'Obligación pasada no cumplida → <b>Debiste haber llamado</b> (indefinido + haber + participio).'),
                ('______ que el director cambie su decisión, pero no es seguro.',
                 ['Puede', 'Hay', 'Suele', 'Tiene'], 0,
                 '«<b>Puede que</b>» + subjuntivo expresa posibilidad sin sujeto determinado.'),
            ]
        ),
        ex2=dict(
            title='Completa con la forma modal adecuada',
            questions=[
                ('No ______ (poder, pasado, posibilidad) haberlo dicho en serio; es imposible.',
                 'pudo haber dicho', ['pudo haber dicho'],
                 'Posibilidad en el pasado: «poder» en indefinido + <b>haber + participio</b>: <b>pudo haber dicho</b>.'),
                ('______ (haber de, yo, presente) presentarme mañana ante el comité.',
                 'He de presentarme', ['He de presentarme', 'he de presentarme'],
                 'Obligación moderada y formal: <b>he de</b> + infinitivo.'),
                ('Cuando era niño, ______ (soler, yo) jugar en la calle hasta que oscurecía.',
                 'solía', ['solía'],
                 'Habitualidad en el pasado → imperfecto de «soler»: <b>solía</b>.'),
                ('______ (puede que) lleguen tarde; mejor que empieces sin ellos.',
                 'Puede que', ['Puede que'],
                 'Posibilidad sin sujeto explícito → <b>Puede que</b> + subjuntivo.'),
                ('______ (deber, tú, obligación pasada incumplida) haber avisado con más tiempo.',
                 'Debiste haber avisado', ['Debiste haber avisado'],
                 'Obligación pasada no cumplida: <b>Debiste haber avisado</b> (deber en indefinido + haber + participio).'),
            ]
        ),
        ex3=dict(
            title='Identifica el uso modal correcto',
            questions=[
                ('¿Cuál expresa probabilidad o deducción?',
                 ['Debes llamarle ahora mismo.', 'Debe de estar en casa a estas horas.', 'Hay que llamarle.', 'Tienes que llamarle.'],
                 1,
                 '«Debe de + infinitivo» expresa deducción o probabilidad: <b>Debe de estar</b> en casa (= probablemente está).'),
                ('¿Cuál usa «haber que» correctamente?',
                 ['Yo hay que estudiar más.', 'Hay que estudiar más.', 'Ellos hay que estudiar más.', 'Hay que que estudiar más.'],
                 1,
                 '«Haber que» es impersonal: sin sujeto explícito, siempre en 3.ª persona singular: <b>Hay que estudiar</b>.'),
                ('¿Qué matiz diferencia «debes llamar» de «deberías llamar»?',
                 ['Ninguno; son equivalentes.', '«Debes» es obligación fuerte; «deberías» es consejo o recomendación suavizada.', '«Deberías» es más fuerte.', '«Debes» expresa probabilidad.'],
                 1,
                 '<b>Debes</b> = obligación fuerte (normativa o moral). <b>Deberías</b> = consejo, recomendación suavizada (condicional).'),
                ('¿Cuál expresa posibilidad en el pasado?',
                 ['Puede llegar pronto.', 'Pudo llegar temprano. (capacidad)', 'Pudo haber llegado ya.', 'Puede que llegue.'],
                 2,
                 'Posibilidad deductiva referida al pasado: <b>Pudo haber llegado</b> (poder en indef. + haber + participio).'),
                ('¿Cuál usa «soler» correctamente?',
                 ['Suelo de estudiar por las noches.', 'Suelo estudiar por las noches.', 'Solería estudiar por las noches.', 'Suelo a estudiar por las noches.'],
                 1,
                 '«Soler» no lleva preposición: <b>suelo estudiar</b>. No existe «solería» (no tiene condicional).'),
            ]
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('modal-c1-01', 'debes', 'deber + inf.: obligación moral o normativa', 'deber + inf. = obligación',
             '<b>Debes</b> entregar la solicitud antes del viernes.', '______ entregar la solicitud antes del viernes. (obligación personal)', 'debes'),
            ('modal-c1-02', 'debe de ser', 'deber de + inf.: probabilidad o deducción', 'deber de + inf. = deducción',
             '<b>Debe de ser</b> tarde; las calles están desiertas.', '______ tarde; las calles están desiertas. (deducción)', 'debe de ser'),
            ('modal-c1-03', 'hay que', 'haber que + inf.: obligación impersonal', 'haber que = impersonal',
             '<b>Hay que</b> respetar las normas de convivencia.', '______ respetar las normas de convivencia. (impersonal)', 'hay que'),
            ('modal-c1-04', 'he de', 'haber de + inf.: obligación moderada o formal', 'haber de + inf. = formal',
             '<b>He de</b> presentar el proyecto ante la junta mañana.', '______ presentar el proyecto ante la junta mañana. (formal)', 'he de'),
            ('modal-c1-05', 'puede que lleguen', 'puede que + subjuntivo: posibilidad', 'puede que + subj.',
             '<b>Puede que lleguen</b> tarde por el tráfico.', '______ tarde por el tráfico. (posibilidad, sin sujeto)', 'puede que lleguen'),
            ('modal-c1-06', 'pudo haber llegado', 'poder + haber + participio: posibilidad en el pasado', 'pudo haber + part.',
             'El paquete <b>pudo haber llegado</b> ayer sin que nadie lo recogiera.', 'El paquete ______ ayer sin que nadie lo recogiera. (posibilidad pasada)', 'pudo haber llegado'),
            ('modal-c1-07', 'debiste haber llamado', 'deber indef. + haber + part.: obligación pasada incumplida', 'debiste haber + part.',
             '<b>Debiste haber llamado</b> antes de venir; la puerta estaba cerrada.', '______ antes de venir; la puerta estaba cerrada. (obligación pasada no cumplida)', 'debiste haber llamado'),
            ('modal-c1-08', 'suelo', 'soler + inf.: habitualidad (sin preposición)', 'soler + inf. (sin «de»)',
             '<b>Suelo</b> revisar el correo electrónico nada más levantarme.', '______ revisar el correo electrónico nada más levantarme. (costumbre habitual)', 'suelo'),
        ],
    ),

    'gramatica-textual': dict(
        level='c1',
        section='grammar',
        num='G05',
        short='Cohesión Textual',
        title='La Cohesión Textual — Referencia, Sustitución y Elipsis',
        subtitle='Construye textos cohesionados usando la referencia anafórica, la sustitución y la elipsis eficazmente',
        slides=[
            ('Referencia: anafórica y catafórica', None,
             '<p class="slide-explanation">La <b>referencia</b> es el mecanismo por el que un elemento del texto remite a otro sin repetirlo. Puede mirar hacia atrás (<b>anáfora</b>) o hacia adelante (<b>catáfora</b>):</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Tipo</th><th style="padding:8px;text-align:left">Dirección</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Anáfora</b></td><td style="padding:8px">Retoma lo ya dicho</td><td style="padding:8px">«Llegó Pedro. <b>Este</b> parecía cansado.» (<i>este</i> = Pedro)</td></tr>'
             '<tr><td style="padding:8px"><b>Catáfora</b></td><td style="padding:8px">Anticipa lo que vendrá</td><td style="padding:8px">«<b>Esto</b> es lo que quiero: que me escuches.»</td></tr>'
             '</table>'
             '<p class="slide-explanation">Los demostrativos (<b>este, ese, aquel</b> y sus formas) son los mecanismos de referencia textual más potentes porque codifican tanto el género y número del referente como la distancia textual: <b>este/a</b> = mencionado recientemente; <b>ese/a</b> = algo más alejado; <b>aquel/aquella</b> = mencionado mucho antes o muy lejano.</p>'),

            ('Sustitución nominal y verbal', None,
             '<p class="slide-explanation">La <b>sustitución</b> reemplaza un elemento o una estructura por otro elemento más general o gramaticalmente más simple:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Tipo</th><th style="padding:8px;text-align:left">Mecanismo</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Sustitución nominal</td><td style="padding:8px">el/la/los/las + de / el/la que + relativa</td><td style="padding:8px">«Mi coche es rojo y <b>el de</b> Pedro es azul.»</td></tr>'
             '<tr><td style="padding:8px">Sustitución con «uno/a»</td><td style="padding:8px">uno/a como sustituto inespecífico</td><td style="padding:8px">«¿Tienes bolígrafo? — Sí, <b>uno</b> rojo.»</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Sustitución verbal con «hacerlo»</td><td style="padding:8px">hacer + lo / así como pro-verbo</td><td style="padding:8px">«¿Puedes abrir la ventana? — Ya <b>lo he hecho</b>.»</td></tr>'
             '</table>'
             '<p class="slide-explanation">La sustitución nominal con <b>el/la de</b> es muy frecuente en español: «Las ideas del director son más arriesgadas que <b>las de</b> su equipo.»</p>'),

            ('Elipsis: verbal y nominal', None,
             '<p class="slide-explanation">La <b>elipsis</b> omite un elemento recuperable del contexto. Es uno de los rasgos más característicos del español conversacional y también del escrito formal:</p>'
             '<div style="background:var(--paper);padding:16px;margin:16px 0;border-radius:6px">'
             '<p><b>Elipsis verbal:</b> «¿Has terminado el informe? — Sí, [he terminado].»</p>'
             '<p><b>Elipsis nominal:</b> «¿Qué libro prefieres? — El [libro] rojo.»</p>'
             '<p><b>Elipsis de sujeto (pro-drop):</b> «[Yo] He llamado tres veces.» (el sujeto va en la desinencia verbal)</p>'
             '</div>'
             '<p class="slide-explanation">El español es una lengua <b>pro-drop</b>: el sujeto se omite cuando es recuperable por la desinencia verbal o el contexto. Esto es una regla gramatical, no un descuido.</p>'
             '<p class="slide-explanation">Elipsis verbal con «lo»: «¿Sabes que ha dimitido? — Sí, <b>lo sé</b>.» (lo sustituye a toda la proposición).</p>'),

            ('Lo como sustituto oracional y atributivo', None,
             '<p class="slide-explanation">El pronombre neutro <b>lo</b> tiene funciones especiales de sustitución en español:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Función</th><th style="padding:8px;text-align:left">Mecanismo</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Sustitución oracional</td><td style="padding:8px">lo = toda una proposición</td><td style="padding:8px">«¿Sabes que viene? — <b>Lo</b> sé.»</td></tr>'
             '<tr><td style="padding:8px">Sustitución atributiva</td><td style="padding:8px">lo + ser/estar/parecer</td><td style="padding:8px">«¿Es rico? — Sí, <b>lo</b> es.» (<i>lo</i> = rico)</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Lo + adjetivo (nominalización)</td><td style="padding:8px">lo + adj. = aspecto abstracto</td><td style="padding:8px">«<b>Lo</b> difícil del asunto es la financiación.»</td></tr>'
             '</table>'
             '<p class="slide-explanation">«<b>Lo</b> es» nunca puede sustituirse por «la es» o «le es», porque «lo» neutro sustituye a atributos o proposiciones completas, no a sustantivos de género definido.</p>'),

            ('Conectores referenciales e isotopía léxica', None,
             '<p class="slide-explanation">Los <b>conectores de referencia</b> remiten a elementos del texto con una carga semántica adicional (orden, repetición, identidad):</p>'
             '<div style="background:var(--paper);padding:16px;margin:16px 0;border-radius:6px">'
             '<p><b>dicho / mencionado / citado</b>: El <b>mencionado</b> problema requiere atención inmediata.</p>'
             '<p><b>anterior / siguiente / último</b>: El <b>anterior</b> jefe era más flexible.</p>'
             '<p><b>susodicho/a</b> (registro muy formal): El <b>susodicho</b> contrato fue firmado en 2019.</p>'
             '</div>'
             '<p class="slide-explanation">La <b>isotopía léxica</b> mantiene la cohesión mediante redes de palabras semánticamente relacionadas:</p>'
             '<div style="background:var(--paper);padding:16px;margin:16px 0;border-radius:6px">'
             '<p><b>Sinónimos:</b> «El <i>problema</i>… Esta <i>dificultad</i>… El <i>obstáculo</i>…»</p>'
             '<p><b>Hiperónimos:</b> «Los <i>gatos</i> y los <i>perros</i>… Estos <i>animales</i>…»</p>'
             '<p><b>Palabras comodín:</b> <i>cosa, asunto, hecho, tema, cuestión, elemento</i></p>'
             '</div>'
             '<p class="slide-explanation">Un texto rico en isotopía léxica es más cohesionado que uno que repite siempre las mismas palabras o que salta de un campo semántico a otro sin conexión.</p>'),
        ],
        traps=[
            ('Este libro es interesante, pero ese es mejor. (lejanía textual)',
             'Usa <strong>este</strong> para lo más reciente y <strong>aquel</strong> para lo más lejano en el texto.',
             'Los demostrativos codifican distancia textual: <b>este</b> = mencionado hace poco, <b>ese</b> = algo antes, <b>aquel</b> = mucho antes o muy lejano en el discurso. Su uso incorrecto rompe la cohesión.'),
            ('¿Sabes que ha dimitido? — Sí, la sé.',
             '¿Sabes que ha dimitido? — Sí, <strong>lo</strong> sé.',
             '«Lo» neutro sustituye a proposiciones enteras o atributos sin género. Nunca se usa «la» para sustituir una oración.'),
            ('El coche de Ana es rojo y el Pedro es azul.',
             'El coche de Ana es rojo y <strong>el de</strong> Pedro es azul.',
             'La sustitución nominal requiere el artículo seguido de «de»: <b>el de</b> Pedro. Sin «de», la estructura es agramatical.'),
            ('Pro-drop: siempre hay que expresar el sujeto en español.',
             'En español el sujeto se omite cuando es recuperable del contexto.',
             'El español es pro-drop: «[Yo] Vengo mañana» es perfectamente correcto. La omisión del sujeto es la norma, no la excepción, cuando la desinencia verbal lo identifica.'),
            ('Usar «cosa» o «tema» en exceso.',
             'Usa sinónimos, hiperónimos y vocabulario preciso para mantener la isotopía.',
             'Las palabras comodín (<i>cosa, tema, asunto</i>) son útiles ocasionalmente, pero abusar de ellas empobrece el texto. A nivel C1, se espera variación léxica mediante sinónimos e hiperónimos precisos.'),
        ],
        summary=[
            ('Referencia anafórica', 'retoma lo ya dicho: pronombres, demostrativos', 'Pedro llegó. Este parecía cansado.'),
            ('Referencia catafórica', 'anticipa lo que sigue: esto es… / tal es…', 'Esto es lo que pido: puntualidad.'),
            ('Sustitución nominal', 'el/la de + sintagma / el/la que + relativa', 'Mi tesis es más breve que la de Carlos.'),
            ('Elipsis verbal', 'omisión del verbo recuperable por contexto', '¿Has terminado? — Sí [he terminado].'),
            ('Lo neutro', 'lo + ser/parecer / lo = proposición entera', '¿Es difícil? — Sí, lo es. / Lo sé.'),
            ('Conectores referenciales', 'dicho/mencionado/anterior/siguiente', 'El mencionado acuerdo entró en vigor.'),
            ('Isotopía léxica', 'sinónimos, hiperónimos, palabras comodín', 'El problema / esta dificultad / el obstáculo…'),
        ],
        ex1=dict(
            title='Elige el mecanismo de cohesión correcto',
            questions=[
                ('«El informe del director era muy detallado, pero ______ del subdirector era más conciso.»',
                 ['ese', 'el de', 'lo del', 'el'], 1,
                 'Sustitución nominal: artículo + «de» → <b>el de</b> el subdirector.'),
                ('«¿Es necesario revisar el contrato? — Sí, ______ es.»',
                 ['la', 'él', 'lo', 'le'], 2,
                 '«Lo» neutro sustituye al atributo «necesario» con el verbo «ser»: <b>lo</b> es.'),
                ('«Llegaron varios candidatos. ______ parecían muy preparados.»',
                 ['Estos', 'Aquellos', 'Lo', 'El que'], 0,
                 'Referencia anafórica a algo mencionado inmediatamente antes → <b>Estos</b>.'),
                ('«¿Has entregado la tarea? — Sí, ya ______.»',
                 ['la he entregado', 'lo he hecho', 'he hecho', 'lo entregué'], 1,
                 'Elipsis verbal con pro-verbo: «lo he hecho» sustituye a «la he entregado»: <b>lo he hecho</b>.'),
                ('«Los <i>robles</i>, los <i>pinos</i> y los <i>abedules</i>… Estos ______ son resistentes al frío.»',
                 ['árboles', 'seres', 'individuos', 'asuntos'], 0,
                 'Hiperónimo de robles, pinos y abedules → <b>árboles</b>. Mantiene la isotopía léxica del campo semántico vegetal.'),
                ('«______ contrato —firmado en 2021— sigue vigente.» (conector referencial formal)',
                 ['El dicho', 'El susodicho', 'Este dicho', 'Dicho el'], 1,
                 'Conector referencial de registro muy formal: <b>El susodicho</b> contrato (= el contrato mencionado antes).'),
            ]
        ),
        ex2=dict(
            title='Completa con el elemento de cohesión adecuado',
            questions=[
                ('«La propuesta de Marta es arriesgada, pero ______ (la propuesta) de Luis es directamente inviable.»',
                 'la de', ['la de'],
                 'Sustitución nominal femenina: <b>la de</b> Luis. El artículo concuerda con «propuesta» (femenino).'),
                ('«¿Sabes que han cancelado el vuelo? — Sí, ______ (= sé eso).»',
                 'lo sé', ['lo sé'],
                 '«Lo» sustituye a la proposición entera «que han cancelado el vuelo»: <b>lo sé</b>.'),
                ('«Entraron dos desconocidos. ______ (= los desconocidos, ref. anafórica reciente) miraron a todos lados.»',
                 'Estos', ['Estos'],
                 'Referencia anafórica a un referente mencionado inmediatamente antes → demostrativo de proximidad: <b>Estos</b>.'),
                ('«______ (= el aspecto) interesante del proyecto es su viabilidad económica.»',
                 'Lo', ['Lo'],
                 '«Lo + adjetivo» nominaliza el adjetivo y alude al aspecto abstracto: <b>Lo</b> interesante del proyecto…'),
                ('«Se han identificado varios riesgos. ______ (= los riesgos ya mencionados, conector formal) riesgos deben evaluarse.»',
                 'Dichos', ['Dichos'],
                 'Conector referencial formal plural masculino: <b>Dichos</b> riesgos (= los riesgos mencionados antes).'),
            ]
        ),
        ex3=dict(
            title='Identifica el mecanismo de cohesión',
            questions=[
                ('En «Pedro llegó tarde. Este no se disculpó», el demostrativo «este» es un ejemplo de…',
                 ['catáfora', 'elipsis', 'anáfora', 'sustitución léxica'], 2,
                 '<b>Anáfora</b>: «este» retoma un referente mencionado antes (Pedro). La catáfora mira hacia adelante.'),
                ('En «¿Es difícil? — Sí, lo es», «lo» funciona como…',
                 ['pronombre de objeto directo', 'sustituto atributivo neutro', 'artículo neutro', 'conector de referencia'], 1,
                 '«Lo» sustituye al atributo «difícil» con el verbo «ser»: función de <b>sustituto atributivo neutro</b>.'),
                ('¿Qué tipo de cohesión se produce en «Los tiburones y las ballenas… Estos animales…»?',
                 ['Elipsis', 'Referencia catafórica', 'Isotopía léxica mediante hiperónimo', 'Sustitución verbal'], 2,
                 '«Animales» es el hiperónimo de «tiburones» y «ballenas»: <b>isotopía léxica mediante hiperónimo</b>.'),
                ('¿Cuál es el mecanismo en «¿Has comido? — Sí [he comido]»?',
                 ['Sustitución nominal', 'Referencia anafórica', 'Elipsis verbal', 'Catáfora'], 2,
                 'Se omite el verbo «he comido» porque es recuperable del contexto: <b>elipsis verbal</b>.'),
                ('¿Qué hace el conector «mencionado» en «El mencionado acuerdo…»?',
                 ['Introduce información nueva.', 'Retoma un referente ya nombrado en el texto.', 'Anticipa algo que vendrá después.', 'Sustituye a un verbo.'], 1,
                 '«Mencionado» es un conector referencial anafórico que señala que el «acuerdo» ya fue nombrado previamente en el texto.'),
            ]
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('tex-c1-01', 'el de', 'sustitución nominal con artículo + de', 'sustitución: el/la de',
             'Mi coche es rojo, pero <b>el de</b> Ana es plateado.', 'Mi coche es rojo, pero ______ Ana es plateado. (sustitución nominal)', 'el de'),
            ('tex-c1-02', 'lo sé', '«lo» neutro como sustituto oracional', 'lo = proposición entera',
             '¿Sabes que cambiaron la fecha? — Sí, <b>lo sé</b>.', '¿Sabes que cambiaron la fecha? — Sí, ______. (sustitución oracional)', 'lo sé'),
            ('tex-c1-03', 'lo es', '«lo» neutro como sustituto atributivo con «ser»', 'lo + ser = atributo',
             '¿Es complicado el proceso? — Sí, <b>lo es</b>, pero manejable.', '¿Es complicado el proceso? — Sí, ______. (sustituto atributivo)', 'lo es'),
            ('tex-c1-04', 'estos', 'demostrativo anafórico de proximidad (masc. pl.)', 'anáfora: estos = referente reciente',
             'Entraron los inspectores. <b>Estos</b> solicitaron todos los documentos.', 'Entraron los inspectores. ______ solicitaron todos los documentos. (anáfora)', 'estos'),
            ('tex-c1-05', 'lo hecho', 'elipsis verbal con «lo hecho» como pro-verbo', 'elipsis: lo hecho = acción ya dicha',
             '¿Has reservado la sala? — Sí, ya está <b>lo hecho</b>. No, espera: ya <b>lo he hecho</b>.', '¿Has reservado la sala? — Sí, ya ______. (elipsis verbal)', 'lo he hecho'),
            ('tex-c1-06', 'dichos', 'conector referencial formal: dichos (masc. pl.)', 'dicho/a/os/as = ya mencionado',
             '<b>Dichos</b> documentos deben ser entregados antes del lunes.', '______ documentos deben ser entregados antes del lunes. (conector referencial formal, pl.)', 'dichos'),
            ('tex-c1-07', 'animales', 'hiperónimo como mecanismo de isotopía léxica', 'isotopía: hiperónimo',
             'Los delfines, las orcas y los tiburones… Estos <b>animales</b> habitan en todos los océanos.', 'Los delfines, las orcas y los tiburones… Estos ______ habitan en todos los océanos. (hiperónimo)', 'animales'),
            ('tex-c1-08', 'lo difícil', '«lo» + adjetivo: nominalización del aspecto abstracto', 'lo + adj. = aspecto abstracto',
             '<b>Lo difícil</b> del proyecto no es la técnica, sino la coordinación del equipo.', '______ del proyecto no es la técnica, sino la coordinación. (lo + adj., aspecto abstracto)', 'lo difícil'),
        ],
    ),
}
