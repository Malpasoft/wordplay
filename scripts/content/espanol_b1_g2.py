# -*- coding: utf-8 -*-
"""espanol/ B1 Gramática — lote 2 (G06–G10)."""

CHAPTERS = {
    'pluscuamperfecto': dict(
        level='b1',
        section='grammar',
        num='G06',
        short='Pluscuamperfecto',
        title='El Pretérito Pluscuamperfecto — Antes del pasado',
        subtitle='Expresa una acción completada antes de otro momento en el pasado',
        slides=[
            ('¿Qué es el pluscuamperfecto?', None,
             '<p class="slide-explanation">El <b>pretérito pluscuamperfecto</b> expresa una acción que ocurrió <b>antes que otra acción pasada</b>. '
             'Es el «pasado del pasado»: primero sucedió algo, y luego sucedió otra cosa.</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Ya había comido</b> cuando llegaste. (primero comí, luego llegaste)</p>'
             '<p><b>Todavía no habían llegado</b> cuando empezó la película.</p>'
             '<p>Me di cuenta de que <b>había olvidado</b> las llaves.</p>'
             '</div>'
             '<p class="slide-explanation">Marcadores temporales frecuentes: <b>ya</b>, <b>todavía no</b>, '
             '<b>antes de que</b>, <b>cuando</b>, <b>después de que</b>, <b>nunca antes</b>.</p>'),

            ('Formación: haber en imperfecto + participio', None,
             '<p class="slide-explanation">El pluscuamperfecto se forma con el <b>imperfecto de haber</b> + <b>participio pasado</b>. '
             'El participio es invariable (no concuerda con el sujeto).</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronombre</th><th style="padding:8px;text-align:left">HABER (imperfecto)</th><th style="padding:8px;text-align:left">Ejemplo con COMER</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">yo</td><td style="padding:8px"><b>había</b></td><td style="padding:8px">yo <b>había comido</b></td></tr>'
             '<tr><td style="padding:8px">tú</td><td style="padding:8px"><b>habías</b></td><td style="padding:8px">tú <b>habías comido</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">él/ella</td><td style="padding:8px"><b>había</b></td><td style="padding:8px">ella <b>había comido</b></td></tr>'
             '<tr><td style="padding:8px">nosotros</td><td style="padding:8px"><b>habíamos</b></td><td style="padding:8px">nosotros <b>habíamos comido</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">vosotros</td><td style="padding:8px"><b>habíais</b></td><td style="padding:8px">vosotros <b>habíais comido</b></td></tr>'
             '<tr><td style="padding:8px">ellos/ellas</td><td style="padding:8px"><b>habían</b></td><td style="padding:8px">ellos <b>habían comido</b></td></tr>'
             '</table>'
             '<p class="slide-explanation">Recuerda: los participios irregulares más frecuentes son <b>hecho</b> (hacer), <b>dicho</b> (decir), '
             '<b>visto</b> (ver), <b>puesto</b> (poner), <b>vuelto</b> (volver), <b>roto</b> (romper), <b>escrito</b> (escribir).</p>'),

            ('Pluscuamperfecto vs. Pretérito Perfecto', None,
             '<p class="slide-explanation">El <b>pretérito perfecto</b> relaciona el pasado con el presente; '
             'el <b>pluscuamperfecto</b> relaciona un pasado con <b>otro pasado anterior</b>:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Tiempo</th><th style="padding:8px;text-align:left">Formación</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Pretérito perfecto</td><td style="padding:8px">he/has/ha… + participio</td><td style="padding:8px">Esta semana <b>he comido</b> mucha fruta.</td></tr>'
             '<tr><td style="padding:8px">Pluscuamperfecto</td><td style="padding:8px">había/habías/había… + participio</td><td style="padding:8px">Cuando llegué, ya <b>habían comido</b>.</td></tr>'
             '</table>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Nunca <u>había</u> visto</b> el mar. (antes de un momento pasado concreto)</p>'
             '<p>Hoy <b><u>he</u> visto</b> el mar por primera vez. (relacionado con hoy)</p>'
             '</div>'),

            ('Pluscuamperfecto con marcadores temporales', None,
             '<p class="slide-explanation">Los marcadores temporales ayudan a identificar qué acción ocurrió primero '
             'y cuál después. Observa la secuencia:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Marcador</th><th style="padding:8px;text-align:left">Uso</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>ya</b></td><td style="padding:8px">acción completada antes</td><td style="padding:8px">Ya <b>había salido</b> cuando llamaste.</td></tr>'
             '<tr><td style="padding:8px"><b>todavía no</b></td><td style="padding:8px">acción no completada aún</td><td style="padding:8px">Todavía no <b>habían llegado</b>.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>cuando</b></td><td style="padding:8px">punto de referencia pasado</td><td style="padding:8px"><b>Cuando llegué</b>, ya <b>habían empezado</b>.</td></tr>'
             '<tr><td style="padding:8px"><b>antes de que</b></td><td style="padding:8px">anterioridad</td><td style="padding:8px"><b>Antes de que</b> llegaras, yo ya <b>había terminado</b>.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>después de que</b></td><td style="padding:8px">posterioridad</td><td style="padding:8px"><b>Después de que</b> <b>hubimos</b> cenado, salimos. (formal)</td></tr>'
             '</table>'),

            ('Uso narrativo del pluscuamperfecto', None,
             '<p class="slide-explanation">En textos narrativos, el pluscuamperfecto se usa para dar <b>información de fondo</b>: '
             'hechos que ya habían ocurrido antes de la historia principal. El relato principal suele ir en <b>indefinido</b>.</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>Esa mañana, Laura <b>llegó</b> tarde al trabajo. <b>Había perdido</b> el autobús porque '
             '<b>se había dormido</b> y no <b>había oído</b> el despertador.</p>'
             '</div>'
             '<p class="slide-explanation">Secuencia de hechos: (1) no oyó el despertador → (2) se durmió → (3) perdió el autobús → (4) llegó tarde.<br>'
             'Los hechos 1-3 se expresan en pluscuamperfecto porque son anteriores al hecho 4 (que va en indefinido).</p>'),
        ],
        traps=[
            ('había comido → yo habría comido', '<strong>había comido</strong> (pluscuamperfecto)', 'No confundas <b>había</b> (imperfecto de haber) con <b>habría</b> (condicional de haber). «Habría comido» es el condicional compuesto, no el pluscuamperfecto.'),
            ('el participio concuerda: habían llegadas', '<strong>habían llegado</strong>', 'El participio en los tiempos compuestos es <b>invariable</b>: siempre termina en -o. Nunca «llegadas», «llegados»: <b>habían llegado</b>.'),
            ('No insertar nada entre haber y el participio', '<strong>había ya comido</strong> — el adverbio va antes', 'Los adverbios como <b>ya</b> o <b>todavía</b> van <b>antes</b> de «haber», no entre «haber» y el participio: «<b>ya había comido</b>», no «había ya comido» (aunque se usa en registro literario).'),
            ('Usar pluscuamperfecto sin referencia a otro pasado', 'El pluscuamperfecto necesita <strong>contexto pasado de referencia</strong>', 'El pluscuamperfecto no se usa solo: necesita un punto de referencia en el pasado (expresado o implícito). No digas solo «Había comido» sin contexto.'),
            ('Confundir había con había de', '<strong>había</strong> ≠ <strong>había de</strong>', '«<b>Había de</b> + infinitivo» es una perífrasis que expresa obligación o destino (registro literario). «<b>Había</b> + participio» es el pluscuamperfecto. Son construcciones completamente distintas.'),
        ],
        summary=[
            ('Formación', 'había/habías/había/habíamos/habíais/habían + participio', 'Ya había terminado cuando llegaron.'),
            ('Pasado del pasado', 'Acción A antes de acción B (ambas pasadas)', 'Cuando llamaste, ya había salido.'),
            ('Marcador ya', 'Acción completada antes del punto de referencia', 'Ya habíamos comido cuando empezó.'),
            ('Marcador todavía no', 'Acción no completada en el punto de referencia', 'Todavía no había llegado cuando cerraron.'),
            ('Participios irregulares clave', 'hecho, dicho, visto, puesto, vuelto, roto, escrito', 'Nunca había visto algo así.'),
            ('Pluscuamp. vs. Perfecto', 'había + p.p. (antes de otro pasado) / he + p.p. (pasado → presente)', 'Hoy he comido poco; ayer ya había comido antes de medianoche.'),
        ],
        ex1=('Elige la forma correcta', 'Selecciona el pluscuamperfecto que corresponde a cada oración.',
             [('Cuando llegué a la fiesta, todos ya ______ (marcharse).', ['se habían marchado', 'se marcharon', 'se han marchado'], 0, 'Acción anterior a «llegué» (indefinido) → <b>se habían marchado</b> (pluscuamperfecto).'),
              ('Nunca ______ (ver, yo) una puesta de sol tan bonita.', ['había visto', 'he visto', 'vi'], 0, 'Anterioridad a un momento pasado implícito → <b>había visto</b>. «He visto» sería válido si hablamos del presente.'),
              ('Me di cuenta de que ______ (olvidar, yo) el pasaporte.', ['había olvidado', 'olvidé', 'he olvidado'], 0, 'Acción anterior a «me di cuenta» (indefinido) → <b>había olvidado</b>.'),
              ('El tren ya ______ (salir) cuando llegamos a la estación.', ['había salido', 'ha salido', 'salió'], 0, '<b>Había salido</b>: ocurrió antes que «llegamos». El contexto es pasado, no presente.'),
              ('Ella ______ (estudiar) toda la noche antes del examen.', ['había estudiado', 'estudió', 'ha estudiado'], 0, 'Acción anterior al examen (otro momento pasado) → <b>había estudiado</b>.'),
              ('Todavía no ______ (comer, nosotros) cuando sonó el teléfono.', ['habíamos comido', 'comimos', 'habemos comido'], 0, '«Todavía no» + pluscuamperfecto: <b>habíamos comido</b>. «Habemos» no existe en español estándar.'),
             ]),
        ex2=('Escribe el pluscuamperfecto', 'Escribe el verbo entre paréntesis en pretérito pluscuamperfecto.',
             [('Antes de conocerte, yo nunca (probar) ______ la comida japonesa.', 'había probado', 'PROBAR → yo pluscuamperfecto: <b>había probado</b>.'),
              ('Cuando llegaron los bomberos, el fuego ya (apagarse) ______.', 'se había apagado', 'APAGARSE → él/ella pluscuamperfecto: <b>se había apagado</b>.'),
              ('Me sorprendió que ellos no (leer) ______ el libro.', 'hubieran leído', 'Tras «me sorprendió que» en pasado → subjuntivo pluscuamperfecto: <b>hubieran leído</b>.'),
              ('Nosotros ya (hablar) ______ con el director antes de la reunión.', 'habíamos hablado', 'HABLAR → nosotros pluscuamperfecto: <b>habíamos hablado</b>.'),
              ('Cuando cumplió 30 años, ya (vivir, él) ______ en cuatro países distintos.', 'había vivido', 'VIVIR → él pluscuamperfecto: <b>había vivido</b>.'),
             ]),
        ex3=('Pluscuamperfecto en contexto', 'Elige la oración que usa correctamente el pretérito pluscuamperfecto.',
             [('¿Cuál usa correctamente el pluscuamperfecto?', ['Cuando llegué, ya había terminado la clase.', 'Cuando llegué, ya ha terminado la clase.', 'Cuando llegué, ya terminó la clase.'], 0, '<b>Había terminado</b>: acción anterior a «llegué» en el pasado. El perfecto «ha terminado» no encaja con el indefinido «llegué».'),
              ('¿Cuál describe un hecho anterior a otro pasado?', ['Nunca había viajado en avión hasta ese día.', 'Nunca he viajado en avión.', 'Nunca viajé en avión.'], 0, '<b>Había viajado</b>: anterioridad a «ese día» (punto pasado de referencia).'),
              ('¿Cuál es la forma correcta de pluscuamperfecto para «ellas / escribir»?', ['ellas habían escrito', 'ellas habían escribido', 'ellas hubieron escrito'], 0, 'ESCRIBIR tiene participio irregular: <b>escrito</b>. Por eso: <b>habían escrito</b>.'),
              ('¿En qué oración el pluscuamperfecto está mal usado?', ['Había comido antes de salir.', 'Ayer había comido pizza. (sin referencia pasada)', 'Cuando llegaste, ya había comido.'], 1, 'El pluscuamperfecto necesita un punto de referencia pasado. «Ayer había comido pizza» sin más contexto es incorrecto; se diría «Ayer comí pizza» (indefinido).'),
              ('¿Cuál es el participio correcto de HACER?', ['hacido', 'hecho', 'hacido'], 1, 'HACER tiene participio irregular: <b>hecho</b>. Por eso: <b>había hecho</b>.'),
             ]),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('plusc-01', 'había comido', 'pluscuamperfecto yo/él de COMER', 'pasado anterior a otro pasado — comer', 'Cuando llegaron, yo ya había comido.', 'Cuando llegaron, yo ya ______ comido.', 'había'),
            ('plusc-02', 'habíamos llegado', 'pluscuamperfecto nosotros de LLEGAR', 'nosotros llegamos antes de otro pasado', 'Ya habíamos llegado cuando empezó la tormenta.', 'Ya ______ llegado cuando empezó la tormenta.', 'habíamos'),
            ('plusc-03', 'había visto', 'pluscuamperfecto yo/él de VER — participio irregular', 'ver: participio irregular visto', 'Nunca había visto tanta gente junta.', 'Nunca ______ visto tanta gente junta.', 'había'),
            ('plusc-04', 'habían salido', 'pluscuamperfecto ellos de SALIR', 'ellos salieron antes del punto de referencia', 'Cuando llamé, ya habían salido de casa.', 'Cuando llamé, ya ______ salido de casa.', 'habían'),
            ('plusc-05', 'había hecho', 'pluscuamperfecto yo/él de HACER — participio irregular', 'hacer: participio irregular hecho', 'Él ya había hecho los deberes antes de cenar.', 'Él ya ______ hecho los deberes antes de cenar.', 'había'),
            ('plusc-06', 'habías dicho', 'pluscuamperfecto tú de DECIR — participio irregular', 'decir: participio irregular dicho', 'No recordé lo que me habías dicho.', 'No recordé lo que me ______ dicho.', 'habías'),
            ('plusc-07', 'habíais terminado', 'pluscuamperfecto vosotros de TERMINAR', 'vosotros terminaron antes del punto de referencia', '¿Habíais terminado el proyecto antes de las vacaciones?', '¿______ terminado el proyecto antes de las vacaciones?', 'habíais'),
            ('plusc-08', 'había escrito', 'pluscuamperfecto yo/él de ESCRIBIR — participio irregular', 'escribir: participio irregular escrito', 'La autora ya había escrito tres novelas antes de los 30 años.', 'La autora ya ______ escrito tres novelas antes de los 30 años.', 'había'),
        ],
    ),

    'estilo-indirecto': dict(
        level='b1',
        section='grammar',
        num='G07',
        short='Estilo Indirecto',
        title='El Estilo Indirecto — Reportar lo que dijo alguien',
        subtitle='Transmite palabras y preguntas de otros con los cambios necesarios',
        slides=[
            ('¿Qué es el estilo indirecto?', None,
             '<p class="slide-explanation">El <b>estilo indirecto</b> (o discurso reportado) sirve para transmitir lo que otra persona dijo, '
             'preguntó o pidió, sin repetir sus palabras exactas. Los verbos más usados son '
             '<b>decir que</b>, <b>preguntar si/qué</b> y <b>pedir que</b>.</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Estilo directo:</b> Ana dijo: «<i>Estoy cansada</i>.»</p>'
             '<p><b>Estilo indirecto:</b> Ana dijo que <b>estaba</b> cansada.</p>'
             '<p>&nbsp;</p>'
             '<p><b>Estilo directo:</b> Luis preguntó: «<i>¿Vienes mañana?</i>»</p>'
             '<p><b>Estilo indirecto:</b> Luis preguntó <b>si</b> venía al día siguiente.</p>'
             '</div>'),

            ('Cambios de tiempo verbal', None,
             '<p class="slide-explanation">Cuando el verbo introductor está en <b>pasado</b> (dijo, preguntó…), '
             'el tiempo verbal de la cita cambia así:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Estilo directo</th><th style="padding:8px;text-align:left">Estilo indirecto (verbo introductor en pasado)</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">presente → <b>estoy</b></td><td style="padding:8px">imperfecto → <b>estaba</b></td></tr>'
             '<tr><td style="padding:8px">pretérito perfecto → <b>he comido</b></td><td style="padding:8px">pluscuamperfecto → <b>había comido</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">pretérito indefinido → <b>comí</b></td><td style="padding:8px">pluscuamperfecto → <b>había comido</b></td></tr>'
             '<tr><td style="padding:8px">futuro → <b>vendré</b></td><td style="padding:8px">condicional → <b>vendría</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">imperfecto → <b>comía</b></td><td style="padding:8px">imperfecto → <b>comía</b> (sin cambio)</td></tr>'
             '<tr><td style="padding:8px">imperativo → <b>ven</b></td><td style="padding:8px">imperfecto de subjuntivo → <b>que viniera</b></td></tr>'
             '</table>'),

            ('Cambios de pronombres y referencias', None,
             '<p class="slide-explanation">Al pasar al estilo indirecto, los <b>pronombres personales</b> y las '
             '<b>referencias de tiempo y lugar</b> también cambian según la perspectiva del hablante:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Estilo directo</th><th style="padding:8px;text-align:left">Estilo indirecto</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">yo</td><td style="padding:8px">él/ella (o el sujeto correspondiente)</td></tr>'
             '<tr><td style="padding:8px">tú</td><td style="padding:8px">yo / él / ella (según contexto)</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">aquí</td><td style="padding:8px">allí / allá</td></tr>'
             '<tr><td style="padding:8px">este/esta/esto</td><td style="padding:8px">aquel/aquella/aquello</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">hoy</td><td style="padding:8px">ese día</td></tr>'
             '<tr><td style="padding:8px">mañana</td><td style="padding:8px">al día siguiente</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">ayer</td><td style="padding:8px">el día anterior</td></tr>'
             '<tr><td style="padding:8px">la semana que viene</td><td style="padding:8px">la semana siguiente</td></tr>'
             '</table>'),

            ('Preguntas en estilo indirecto', None,
             '<p class="slide-explanation">Para reportar <b>preguntas</b> usamos <b>preguntar si</b> (preguntas de sí/no) '
             'o <b>preguntar + pronombre interrogativo</b> (preguntas abiertas). Nunca se usa signo de interrogación.</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Pregunta sí/no:</b><br>'
             'Directo: «¿Tienes hambre?»<br>'
             'Indirecto: Me preguntó <b>si tenía</b> hambre.</p>'
             '<p>&nbsp;</p>'
             '<p><b>Pregunta abierta:</b><br>'
             'Directo: «¿Dónde vives?»<br>'
             'Indirecto: Me preguntó <b>dónde vivía</b>.</p>'
             '<p>&nbsp;</p>'
             '<p><b>Pregunta con qué:</b><br>'
             'Directo: «¿Qué quieres comer?»<br>'
             'Indirecto: Me preguntó <b>qué quería</b> comer.</p>'
             '</div>'),

            ('Órdenes y peticiones en estilo indirecto', None,
             '<p class="slide-explanation">Para reportar <b>órdenes</b> o <b>peticiones</b>, se usa '
             '<b>pedir/decir/ordenar + que + imperfecto de subjuntivo</b>:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>Directo: «<b>Abre</b> la ventana.»</p>'
             '<p>Indirecto: Me pidió que <b>abriera</b> la ventana.</p>'
             '<p>&nbsp;</p>'
             '<p>Directo: «<b>No hagas</b> ruido.»</p>'
             '<p>Indirecto: Me dijo que <b>no hiciera</b> ruido.</p>'
             '<p>&nbsp;</p>'
             '<p>Directo: «<b>Llama</b> antes de venir.»</p>'
             '<p>Indirecto: Me pidió que <b>llamara</b> antes de ir.</p>'
             '</div>'
             '<p class="slide-explanation">Cuando el verbo introductor está en <b>presente</b> (dice, pregunta…), '
             'no hay cambio de tiempo verbal: «Dice que <b>está</b> cansada.»</p>'),
        ],
        traps=[
            ('Dijo que viene (sin cambio cuando introductor es pasado)', '<strong>Dijo que vendría / venía</strong>', 'Si el verbo introductor está en pasado («dijo», «contó»…), el tiempo del verbo subordinado debe cambiar. «Dijo que <b>viene</b>» es incorrecto; lo correcto es «Dijo que <b>venía</b>» o «que <b>vendría</b>».'),
            ('Pregunta indirecta con signos de interrogación', 'Sin signos: <strong>Me preguntó si venías</strong>', 'En estilo indirecto no se usan signos de interrogación ni exclamación. «Me preguntó ¿si venías?» es incorrecto.'),
            ('Usar "si" para preguntas con pronombre interrogativo', 'Usa el <strong>pronombre interrogativo directamente</strong>', '«Me preguntó si dónde vivía» es incorrecto. Para preguntas con pronombre interrogativo se usa directamente: «Me preguntó <b>dónde vivía</b>».'),
            ('Olvidar cambiar los adverbios de tiempo', 'Cambia <strong>mañana → al día siguiente</strong>, <strong>hoy → ese día</strong>', 'No basta con cambiar los verbos. «Dijo que vendría mañana» puede ser ambiguo o incorrecto si se dijo hace tiempo; lo correcto es «Dijo que vendría <b>al día siguiente</b>».'),
            ('Pedir + infinitivo vs. pedir que + subjuntivo', '<strong>Me pidió que lo hiciera</strong> (no «me pidió hacerlo»)', '«Pedir» + que + subjuntivo es la estructura estándar para reportar órdenes: «Me pidió <b>que</b> lo <b>hiciera</b>». «Me pidió hacerlo» es posible con cambio de sujeto en algunos dialectos, pero la estructura más segura usa «que + subjuntivo».'),
        ],
        summary=[
            ('Verbo introductor en pasado', 'Los tiempos verbales retroceden un nivel', 'Dijo que estaba cansado. (estoy → estaba)'),
            ('Presente → Imperfecto', 'estoy → estaba, vivo → vivía', 'Dijo que vivía en Madrid.'),
            ('Futuro → Condicional', 'vendré → vendría', 'Prometió que vendría al día siguiente.'),
            ('Indefinido/Perfecto → Pluscuamperfecto', 'comí / he comido → había comido', 'Explicó que había llegado tarde.'),
            ('Preguntas sí/no', 'preguntar + si + verbo', 'Me preguntó si tenía tiempo.'),
            ('Preguntas abiertas', 'preguntar + pronombre interrogativo + verbo', 'Me preguntó dónde vivía.'),
            ('Órdenes', 'pedir/decir + que + imperfecto de subjuntivo', 'Me pidió que cerrara la puerta.'),
        ],
        ex1=('Elige la opción correcta en estilo indirecto', 'Selecciona la transformación correcta al estilo indirecto.',
             [('Elena dijo: «Tengo mucho trabajo.» → Elena dijo que ______.', ['tiene mucho trabajo', 'tenía mucho trabajo', 'tuvo mucho trabajo'], 1, 'Presente → imperfecto en estilo indirecto con verbo introductor en pasado: <b>tenía</b>.'),
              ('Pedro preguntó: «¿Vienes a la fiesta?» → Pedro me preguntó ______.', ['si venía a la fiesta', 'si vengo a la fiesta', 'que si venía a la fiesta'], 0, 'Pregunta de sí/no → <b>si + imperfecto</b>: «si venía». «Que si» es coloquial e incorrecto en registro formal.'),
              ('La profesora dijo: «Estudiad más.» → La profesora nos dijo que ______.', ['estudiamos más', 'estudiáramos más', 'estudiaríamos más'], 1, 'Imperativo → imperfecto de subjuntivo: <b>estudiáramos</b>.'),
              ('Carlos prometió: «Te llamaré mañana.» → Carlos prometió que ______.', ['me llamará al día siguiente', 'me llamaría al día siguiente', 'me llamó al día siguiente'], 1, 'Futuro → condicional: <b>llamaría</b>. «Mañana» → <b>al día siguiente</b>.'),
              ('Ana preguntó: «¿Dónde has estado?» → Ana me preguntó ______.', ['dónde había estado', 'si dónde había estado', 'dónde he estado'], 0, 'Pregunta abierta con «dónde» → <b>dónde + pluscuamperfecto</b>: «dónde había estado». Sin «si».'),
              ('El jefe ordenó: «No llegues tarde.» → El jefe me ordenó que ______.', ['no llego tarde', 'no llegaría tarde', 'no llegara tarde'], 2, 'Imperativo negativo → imperfecto de subjuntivo: <b>no llegara</b>.'),
             ]),
        ex2=('Transforma al estilo indirecto', 'Escribe la frase en estilo indirecto. Cambia el tiempo verbal cuando sea necesario.',
             [('Juan dijo: «Estoy muy cansado.» → Juan dijo que ______.', 'estaba muy cansado', 'Presente → imperfecto: <b>estaba</b> muy cansado.'),
              ('Marta preguntó: «¿Tienes hambre?» → Marta me preguntó ______.', 'si tenía hambre', 'Pregunta de sí/no → <b>si tenía</b> hambre.'),
              ('El médico dijo: «Descanse y beba mucha agua.» → El médico me dijo que ______.', 'descansara y bebiera mucha agua', 'Imperativo → subjuntivo imperfecto: <b>descansara y bebiera</b>.'),
              ('Ella prometió: «Volveré pronto.» → Ella prometió que ______.', 'volvería pronto', 'Futuro → condicional: <b>volvería</b>.'),
              ('Él me preguntó: «¿Cuándo llegaste?» → Él me preguntó ______.', 'cuándo había llegado', 'Pregunta abierta + indefinido → pluscuamperfecto: <b>cuándo había llegado</b>.'),
             ]),
        ex3=('Identifica el error en estilo indirecto', 'Elige la oración en estilo indirecto que es correcta.',
             [('¿Cuál es la transformación correcta de «Dijo: tengo hambre»?', ['Dijo que tiene hambre.', 'Dijo que tenía hambre.', 'Dijo que tuviera hambre.'], 1, 'Presente → imperfecto cuando el introductor está en pasado: <b>tenía</b>.'),
              ('¿Cuál reporta correctamente una pregunta de sí/no?', ['Me preguntó que si vendría.', 'Me preguntó si vendría.', 'Me preguntó si ¿vendría?'], 1, 'Pregunta de sí/no → «<b>si</b> + verbo» sin «que» delante y sin signos de interrogación.'),
              ('¿Cuál reporta correctamente una orden?', ['Me pidió que abro la ventana.', 'Me pidió que abriera la ventana.', 'Me pidió abrir la ventana.'], 1, 'Orden → pedir <b>que + imperfecto de subjuntivo</b>: <b>abriera</b>.'),
              ('¿Cuál usa correctamente el cambio temporal futuro → condicional?', ['Dijo que vendrá mañana.', 'Dijo que vendría al día siguiente.', 'Dijo que venía mañana.'], 1, 'Futuro → condicional: <b>vendría</b>. «Mañana» también cambia a <b>al día siguiente</b>.'),
              ('¿Cuál reporta correctamente una pregunta abierta con «dónde»?', ['Me preguntó si dónde vivía.', 'Me preguntó dónde vivía.', 'Me preguntó dónde vivió.'], 1, 'Pregunta abierta → pronombre interrogativo directamente (sin «si»): <b>dónde vivía</b>.'),
             ]),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('indirecto-01', 'estaba cansado', 'estilo indirecto: presente → imperfecto', 'dijo que estaba (no «está»)', 'Dijo que estaba muy cansado después del viaje.', 'Dijo que ______ muy cansado después del viaje.', 'estaba'),
            ('indirecto-02', 'si venía', 'reportar pregunta de sí/no: ¿Vienes? → si venía', 'pregunta sí/no con «si» + imperfecto', 'Me preguntó si venía a la reunión.', 'Me preguntó ______ a la reunión.', 'si venía'),
            ('indirecto-03', 'vendría', 'futuro → condicional en estilo indirecto', 'prometió que vendría (no «vendrá»)', 'Prometió que vendría al día siguiente.', 'Prometió que ______ al día siguiente.', 'vendría'),
            ('indirecto-04', 'que lo hiciera', 'reportar orden: hazlo → que lo hiciera', 'pedir que + subjuntivo imperfecto', 'Me pidió que lo hiciera enseguida.', 'Me pidió ______ enseguida.', 'que lo hiciera'),
            ('indirecto-05', 'dónde vivía', 'pregunta abierta: ¿Dónde vives? → dónde vivía', 'pregunta abierta sin «si»', 'Me preguntó dónde vivía en aquella época.', 'Me preguntó ______ en aquella época.', 'dónde vivía'),
            ('indirecto-06', 'había llegado', 'indefinido → pluscuamperfecto en estilo indirecto', 'dijo que había llegado (no «llegó»)', 'Explicó que había llegado tarde por el tráfico.', 'Explicó que ______ tarde por el tráfico.', 'había llegado'),
            ('indirecto-07', 'al día siguiente', 'cambio de referencia temporal: mañana → al día siguiente', 'mañana cambia en estilo indirecto', 'Dijo que nos vería al día siguiente.', 'Dijo que nos vería ______.', 'al día siguiente'),
            ('indirecto-08', 'que salieran', 'reportar orden a terceros: salid → que salieran', 'decir que + subjuntivo imperfecto', 'Les dijo que salieran por la puerta trasera.', 'Les dijo ______ por la puerta trasera.', 'que salieran'),
        ],
    ),

    'pronombres-relativos': dict(
        level='b1',
        section='grammar',
        num='G08',
        short='Pronombres Relativos',
        title='Los Pronombres Relativos — que, quien, donde y más',
        subtitle='Conecta cláusulas y da información sobre personas, cosas y lugares',
        slides=[
            ('¿Qué son los pronombres relativos?', None,
             '<p class="slide-explanation">Los <b>pronombres relativos</b> conectan una cláusula subordinada con su '
             '<b>antecedente</b> (la palabra a la que se refieren). Evitan la repetición y añaden información.</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>El libro <b>que</b> me prestaste es muy interesante. (<i>que</i> = el libro)</p>'
             '<p>La profesora <b>con quien</b> estudié ganó un premio. (<i>quien</i> = la profesora)</p>'
             '<p>La ciudad <b>donde</b> nací tiene muy poca lluvia. (<i>donde</i> = la ciudad)</p>'
             '</div>'
             '<p class="slide-explanation">El antecedente puede ser una persona, una cosa o un lugar. '
             'El pronombre relativo debe concordar con él en número y, en algunos casos, en género.</p>'),

            ('QUE y QUIEN / QUIENES', None,
             '<p class="slide-explanation"><b>QUE</b> es el pronombre relativo más frecuente. Se usa para personas y cosas. '
             '<b>QUIEN / QUIENES</b> se usa solo para personas, especialmente después de preposición.</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronombre</th><th style="padding:8px;text-align:left">Uso</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>que</b></td><td style="padding:8px">personas y cosas (sujeto u objeto directo)</td><td style="padding:8px">El chico <b>que</b> vino ayer es mi primo.</td></tr>'
             '<tr><td style="padding:8px"><b>que</b></td><td style="padding:8px">cosas después de «a» (objeto indirecto raro)</td><td style="padding:8px">La película <b>que</b> vi era buena.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>quien</b></td><td style="padding:8px">persona, tras preposición</td><td style="padding:8px">La persona <b>con quien</b> hablé era amable.</td></tr>'
             '<tr><td style="padding:8px"><b>quienes</b></td><td style="padding:8px">plural de quien</td><td style="padding:8px">Los amigos <b>a quienes</b> escribí respondieron.</td></tr>'
             '</table>'
             '<p class="slide-explanation">Nota: «la chica <b>que</b> hablé» es incorrecto; se necesita preposición: '
             '«la chica <b>con quien</b> hablé» o «la chica <b>con la que</b> hablé».</p>'),

            ('EL QUE / LA QUE / LOS QUE / LAS QUE y EL CUAL', None,
             '<p class="slide-explanation">Las formas <b>artículo + que</b> y <b>artículo + cual</b> se usan '
             'tras preposición o cuando hay ambigüedad sobre el antecedente. <b>El cual</b> es más formal.</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Forma</th><th style="padding:8px;text-align:left">Uso</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>el/la/los/las que</b></td><td style="padding:8px">tras preposición; referencia clara</td><td style="padding:8px">La mesa <b>sobre la que</b> escribes es antigua.</td></tr>'
             '<tr><td style="padding:8px"><b>el cual / la cual</b></td><td style="padding:8px">formal; tras preposiciones largas</td><td style="padding:8px">El edificio, <b>frente al cual</b> hay un parque, es el ayuntamiento.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>los/las cuales</b></td><td style="padding:8px">plural de el cual / la cual</td><td style="padding:8px">Los documentos, <b>los cuales</b> firma el director, están listos.</td></tr>'
             '</table>'
             '<p class="slide-explanation">Tras preposiciones largas o compuestas (<b>a pesar de</b>, <b>en frente de</b>, '
             '<b>a través de</b>…) es obligatorio usar <b>el cual / la cual</b> o <b>el/la que</b>, nunca «que» solo.</p>'),

            ('DONDE y CUYO / CUYA', None,
             '<p class="slide-explanation"><b>DONDE</b> se refiere a lugares. <b>CUYO / CUYA / CUYOS / CUYAS</b> '
             'expresa posesión y concuerda con la cosa poseída (no con el poseedor).</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronombre</th><th style="padding:8px;text-align:left">Uso</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>donde</b></td><td style="padding:8px">lugar (equivale a «en el que / en la que»)</td><td style="padding:8px">La ciudad <b>donde</b> nació tiene un castillo.</td></tr>'
             '<tr><td style="padding:8px"><b>cuyo/cuya</b></td><td style="padding:8px">posesión (singular)</td><td style="padding:8px">El autor <b>cuya</b> novela leí ganó el premio.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>cuyos/cuyas</b></td><td style="padding:8px">posesión (plural)</td><td style="padding:8px">La empresa <b>cuyos</b> empleados trabajan aquí es famosa.</td></tr>'
             '</table>'
             '<p class="slide-explanation">Truco de <b>cuyo</b>: concuerda con lo que se posee, no con el poseedor. '
             '«El hombre <b>cuya</b> hija estudia aquí» (<i>cuya</i> concuerda con <i>hija</i>, femenino).</p>'),

            ('Cláusulas restrictivas y explicativas', None,
             '<p class="slide-explanation">Hay dos tipos de cláusulas relativas según si añaden información <b>esencial</b> o <b>adicional</b>:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Restrictiva</b> (sin coma): limita o identifica el antecedente. Sin ella, la frase cambia de significado.</p>'
             '<p>Los alumnos <b>que estudian</b> aprobarán. (solo los que estudian)</p>'
             '<p>&nbsp;</p>'
             '<p><b>Explicativa</b> (con coma): añade información extra. Si la quitamos, la frase sigue siendo completa.</p>'
             '<p>Los alumnos, <b>que estudian</b> mucho, aprobarán. (todos estudian mucho → información extra)</p>'
             '</div>'
             '<p class="slide-explanation">En las cláusulas explicativas se prefiere <b>el cual / la cual</b> en registro formal. '
             'La coma es obligatoria en las explicativas y está prohibida en las restrictivas.</p>'),
        ],
        traps=[
            ('Usar «quien» para cosas', '<strong>que</strong> para cosas', '«La película <b>quien</b> vi» es incorrecto. <b>Quien</b> solo se usa para personas. Para cosas, usa siempre <b>que</b>: «La película <b>que</b> vi».'),
            ('Olvidar la preposición antes de que/quien', 'Incluye la <strong>preposición</strong>: con quien, en el que, de la que…', '«La persona <b>que</b> hablé» es incorrecto; falta la preposición. Lo correcto: «La persona <b>con quien / con la que</b> hablé».'),
            ('Cuyo concuerda con el poseedor', '<strong>Cuyo</strong> concuerda con lo poseído', '«El autor <b>cuyo</b> novela leí» es incorrecto. <b>Cuyo</b> concuerda con <i>novela</i> (femenino): «El autor <b>cuya</b> novela leí».'),
            ('Usar «que» tras preposiciones largas', 'Usa <strong>el cual / el que</strong> tras preposiciones largas', '«El motivo <b>a través de que</b> llegamos» es incorrecto. Tras preposiciones largas es obligatorio: «a través <b>del cual</b>» o «a través <b>del que</b>».'),
            ('Coma en cláusulas restrictivas', 'Sin coma en restrictivas; <strong>coma obligatoria</strong> en explicativas', '«Los alumnos, que estudian, aprobarán» implica que todos estudian. Sin coma («Los alumnos que estudian aprobarán») solo los que estudian aprobarán. La coma cambia el significado.'),
        ],
        summary=[
            ('que', 'personas y cosas; sujeto u objeto directo', 'El libro que compré es excelente.'),
            ('quien / quienes', 'solo personas; tras preposición', 'La persona con quien hablé era el director.'),
            ('el/la/los/las que', 'tras preposición; antecedente conocido', 'La silla en la que me siento es cómoda.'),
            ('el cual / la cual (formal)', 'tras preposiciones largas o compuestas', 'El edificio frente al cual vivo es histórico.'),
            ('donde', 'lugar (= en el que / en la que)', 'La ciudad donde nació mi madre tiene playas.'),
            ('cuyo / cuya / cuyos / cuyas', 'posesión; concuerda con lo poseído', 'El músico cuyas canciones me gustan actúa hoy.'),
            ('Restrictiva vs. explicativa', 'Sin coma = limita; con coma = añade info extra', 'Los que estudian pasan. / Los alumnos, que son muy trabajadores, pasan.'),
        ],
        ex1=('Elige el pronombre relativo correcto', 'Selecciona el pronombre relativo adecuado.',
             [('El edificio ______ ves al fondo es el ayuntamiento.', ['que', 'quien', 'cuyo'], 0, '<b>Que</b> para cosas: «el edificio <b>que</b> ves».'),
              ('La chica ______ hablé ayer es mi vecina.', ['que', 'con quien', 'cuya'], 1, 'Tras preposición «con» + persona → <b>con quien</b>.'),
              ('El autor ______ novela leímos ganó el premio.', ['que', 'quien', 'cuya'], 2, '<b>Cuya</b>: posesión; concuerda con <i>novela</i> (femenino singular).'),
              ('La ciudad ______ vivo tiene un río muy bonito.', ['en la que', 'que', 'cuya'], 0, 'Lugar con preposición → <b>en la que</b> (o «donde»).'),
              ('Esos son los documentos ______ firma el notario.', ['que', 'quien', 'donde'], 0, '<b>Que</b> para cosas (objeto directo de «firma»): <b>que</b>.'),
              ('El parque, ______ hay muchos árboles, está cerca de aquí.', ['donde', 'cuyo', 'quien'], 0, 'Lugar con información adicional → <b>donde</b>.'),
             ]),
        ex2=('Completa con el pronombre relativo adecuado', 'Escribe el pronombre relativo correcto en cada espacio.',
             [('La película ______ vimos ayer me pareció aburrida.', 'que', '<b>Que</b> para cosas (objeto directo).'),
              ('El científico ______ descubrimiento cambió la medicina nació aquí.', 'cuyo', '<b>Cuyo</b>: posesión; concuerda con <i>descubrimiento</i> (masculino singular).'),
              ('Hay personas con ______ es muy difícil trabajar.', 'quienes', 'Plural de «quien» tras preposición «con»: <b>quienes</b>.'),
              ('La razón por ______ me fui es complicada.', 'la que', 'Preposición «por» + cosa → <b>la que</b>.'),
              ('El restaurante ______ comemos siempre está lleno los fines de semana.', 'donde', 'Lugar → <b>donde</b> (= en el que).'),
             ]),
        ex3=('Identifica el uso correcto', 'Elige la oración con el pronombre relativo bien usado.',
             [('¿Cuál es correcta?', ['La persona quien vi era alta.', 'La persona que vi era alta.', 'La persona cuya vi era alta.'], 1, '<b>Que</b> para persona como objeto directo (sin preposición): <b>que vi</b>.'),
              ('¿Cuál usa «cuyo» correctamente?', ['El chico cuyo padre es médico está en mi clase.', 'El chico cuya padre es médico está en mi clase.', 'El chico cuyo es médico está en mi clase.'], 0, '<b>Cuyo</b> concuerda con <i>padre</i> (masculino singular).'),
              ('¿Cuál es la oración explicativa correcta?', ['Los alumnos, que trabajan mucho, sacan buenas notas.', 'Los alumnos que, trabajan mucho, sacan buenas notas.', 'Los alumnos que trabajan mucho sacan buenas notas.'], 0, 'Cláusula explicativa (adicional) → comas obligatorias a los dos lados.'),
              ('¿Cuál usa «donde» correctamente?', ['La tienda donde compro el pan está cerrada.', 'La tienda quien compro el pan está cerrada.', 'La tienda cuya compro el pan está cerrada.'], 0, '<b>Donde</b> para lugares: «la tienda <b>donde</b> compro».'),
              ('¿Cuál es correcta tras preposición larga?', ['El motivo a través de que actuó.', 'El motivo a través del cual actuó.', 'El motivo a través quien actuó.'], 1, 'Tras «a través de» es obligatorio <b>el cual</b> o <b>el que</b>.'),
             ]),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('relat-01', 'que', 'pronombre relativo para cosas o personas (sujeto/OD)', 'el relativo más frecuente', 'El libro que me regalaste es fascinante.', 'El libro ______ me regalaste es fascinante.', 'que'),
            ('relat-02', 'con quien', 'quien tras preposición para personas', 'preposición + quien (personas)', 'La directora con quien hablé es muy eficiente.', 'La directora ______ hablé es muy eficiente.', 'con quien'),
            ('relat-03', 'cuya', 'cuya — posesión; concuerda con la cosa poseída (femenino singular)', 'cuyo/cuya concuerda con lo poseído', 'La escritora cuya novela gané era joven.', 'La escritora ______ novela gané era joven.', 'cuya'),
            ('relat-04', 'donde', 'donde — lugar', 'relativo de lugar', 'El pueblo donde crecí tiene pocas casas.', 'El pueblo ______ crecí tiene pocas casas.', 'donde'),
            ('relat-05', 'en la que', 'en la que — preposición + artículo + que (femenino singular)', 'la que tras preposición', 'La oficina en la que trabajo tiene mucha luz.', 'La oficina ______ trabajo tiene mucha luz.', 'en la que'),
            ('relat-06', 'al cual', 'al cual — preposición a + el cual (formal)', 'preposición larga + el cual', 'El club al cual pertenezco organiza eventos.', 'El club ______ pertenezco organiza eventos.', 'al cual'),
            ('relat-07', 'cuyos', 'cuyos — posesión plural masculina', 'cuyo en plural masculino', 'El equipo cuyos jugadores entreno ganó el torneo.', 'El equipo ______ jugadores entreno ganó el torneo.', 'cuyos'),
            ('relat-08', 'quienes', 'quienes — plural de quien (personas)', 'quien en plural', 'Los vecinos a quienes saludé son simpáticos.', 'Los vecinos a ______ saludé son simpáticos.', 'quienes'),
        ],
    ),

    'subjuntivo-imperfecto': dict(
        level='b1',
        section='grammar',
        num='G09',
        short='Subjuntivo Imperfecto',
        title='El Subjuntivo Imperfecto — Hipótesis y deseos en el pasado',
        subtitle='Forma y usa el pretérito imperfecto de subjuntivo en contextos reales',
        slides=[
            ('¿Qué es el subjuntivo imperfecto?', None,
             '<p class="slide-explanation">El <b>pretérito imperfecto de subjuntivo</b> expresa situaciones hipotéticas, '
             'deseos referidos al pasado o condiciones irreales. Se usa principalmente en:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>1. Condicional tipo 2 (hipótesis irreal):</b> Si <b>tuviera</b> tiempo, viajaría.</p>'
             '<p><b>2. Deseos con ojalá:</b> <b>Ojalá</b> tuvieras razón.</p>'
             '<p><b>3. Como si:</b> Habla <b>como si</b> supiera todo.</p>'
             '<p><b>4. Subordinadas en pasado:</b> Quería que lo <b>hiciera</b> él.</p>'
             '</div>'
             '<p class="slide-explanation">Existe también la forma en <b>-se</b> (hablase, tuviese…) que es intercambiable '
             'con la forma en <b>-ra</b> en la mayoría de contextos, aunque la forma en <b>-ra</b> es la más usada en el habla.</p>'),

            ('Formación: de la tercera persona plural del indefinido', None,
             '<p class="slide-explanation">El imperfecto de subjuntivo se forma a partir de la <b>tercera persona plural del pretérito indefinido</b> '
             '(ellos/ellas): se elimina la terminación <b>-ron</b> y se añaden las terminaciones correspondientes.</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Infinitivo</th><th style="padding:8px;text-align:left">Ellos (indef.)</th><th style="padding:8px;text-align:left">Raíz</th><th style="padding:8px;text-align:left">Yo (subj. imp.)</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">hablar</td><td style="padding:8px">habla<b>ron</b></td><td style="padding:8px">habla-</td><td style="padding:8px"><b>hablara</b></td></tr>'
             '<tr><td style="padding:8px">comer</td><td style="padding:8px">comie<b>ron</b></td><td style="padding:8px">comie-</td><td style="padding:8px"><b>comiera</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">vivir</td><td style="padding:8px">vivie<b>ron</b></td><td style="padding:8px">vivie-</td><td style="padding:8px"><b>viviera</b></td></tr>'
             '<tr><td style="padding:8px">ser / ir</td><td style="padding:8px">fue<b>ron</b></td><td style="padding:8px">fue-</td><td style="padding:8px"><b>fuera</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">tener</td><td style="padding:8px">tuvie<b>ron</b></td><td style="padding:8px">tuvie-</td><td style="padding:8px"><b>tuviera</b></td></tr>'
             '</table>'
             '<p class="slide-explanation">Regla práctica: cualquier irregularidad del indefinido (ellos) '
             'se mantiene en todo el imperfecto de subjuntivo.</p>'),

            ('Conjugación completa', None,
             '<p class="slide-explanation">Las terminaciones del imperfecto de subjuntivo son las mismas para todos los verbos. '
             'La forma <b>nosotros</b> siempre lleva tilde en la vocal anterior a <b>-ramos</b>:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronombre</th><th style="padding:8px;text-align:left">HABLAR</th><th style="padding:8px;text-align:left">COMER</th><th style="padding:8px;text-align:left">SER/IR</th><th style="padding:8px;text-align:left">TENER</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">yo</td><td style="padding:8px"><b>hablara</b></td><td style="padding:8px"><b>comiera</b></td><td style="padding:8px"><b>fuera</b></td><td style="padding:8px"><b>tuviera</b></td></tr>'
             '<tr><td style="padding:8px">tú</td><td style="padding:8px"><b>hablaras</b></td><td style="padding:8px"><b>comieras</b></td><td style="padding:8px"><b>fueras</b></td><td style="padding:8px"><b>tuvieras</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">él/ella</td><td style="padding:8px"><b>hablara</b></td><td style="padding:8px"><b>comiera</b></td><td style="padding:8px"><b>fuera</b></td><td style="padding:8px"><b>tuviera</b></td></tr>'
             '<tr><td style="padding:8px">nosotros</td><td style="padding:8px"><b>habláramos</b></td><td style="padding:8px"><b>comiéramos</b></td><td style="padding:8px"><b>fuéramos</b></td><td style="padding:8px"><b>tuviéramos</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">vosotros</td><td style="padding:8px"><b>hablarais</b></td><td style="padding:8px"><b>comierais</b></td><td style="padding:8px"><b>fuerais</b></td><td style="padding:8px"><b>tuvierais</b></td></tr>'
             '<tr><td style="padding:8px">ellos/ellas</td><td style="padding:8px"><b>hablaran</b></td><td style="padding:8px"><b>comieran</b></td><td style="padding:8px"><b>fueran</b></td><td style="padding:8px"><b>tuvieran</b></td></tr>'
             '</table>'),

            ('Irregulares clave del imperfecto de subjuntivo', None,
             '<p class="slide-explanation">Los irregulares del indefinido producen irregulares en el imperfecto de subjuntivo. '
             'Los más importantes a nivel B1:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Infinitivo</th><th style="padding:8px;text-align:left">Ellos (indefinido)</th><th style="padding:8px;text-align:left">Yo (subj. imp.)</th><th style="padding:8px;text-align:left">Él/ella (subj. imp.)</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">ser / ir</td><td style="padding:8px">fueron</td><td style="padding:8px"><b>fuera</b></td><td style="padding:8px"><b>fuera</b></td></tr>'
             '<tr><td style="padding:8px">tener</td><td style="padding:8px">tuvieron</td><td style="padding:8px"><b>tuviera</b></td><td style="padding:8px"><b>tuviera</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">poder</td><td style="padding:8px">pudieron</td><td style="padding:8px"><b>pudiera</b></td><td style="padding:8px"><b>pudiera</b></td></tr>'
             '<tr><td style="padding:8px">querer</td><td style="padding:8px">quisieron</td><td style="padding:8px"><b>quisiera</b></td><td style="padding:8px"><b>quisiera</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">decir</td><td style="padding:8px">dijeron</td><td style="padding:8px"><b>dijera</b></td><td style="padding:8px"><b>dijera</b></td></tr>'
             '<tr><td style="padding:8px">saber</td><td style="padding:8px">supieron</td><td style="padding:8px"><b>supiera</b></td><td style="padding:8px"><b>supiera</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">venir</td><td style="padding:8px">vinieron</td><td style="padding:8px"><b>viniera</b></td><td style="padding:8px"><b>viniera</b></td></tr>'
             '</table>'),

            ('Usos principales del imperfecto de subjuntivo', None,
             '<p class="slide-explanation">Resumen de los contextos más comunes:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>1. Si + subj. imp. + condicional (hipótesis irreal):</b><br>'
             'Si <b>tuviera</b> más dinero, <b>compraría</b> un coche.</p>'
             '<p><b>2. Ojalá + subj. imp. (deseo poco probable):</b><br>'
             'Ojalá <b>pudiera</b> volar.</p>'
             '<p><b>3. Como si + subj. imp. (comparación irreal):</b><br>'
             'Se comporta como si <b>fuera</b> el jefe.</p>'
             '<p><b>4. Subordinadas con verbo principal en pasado:</b><br>'
             'Le pedí que <b>viniera</b> antes. / Me alegró que <b>estuvieras</b> bien.</p>'
             '</div>'
             '<p class="slide-explanation">Contraste: «Ojalá <b>tenga</b> suerte» (presente de subjuntivo: posible) vs. '
             '«Ojalá <b>tuviera</b> suerte» (imperfecto de subjuntivo: poco probable o imposible).</p>'),
        ],
        traps=[
            ('Si tengo → Si tuviera (confundir condicional tipo 1 y tipo 2)', 'Tipo 1: <strong>si + presente</strong>; Tipo 2: <strong>si + subjuntivo imperfecto</strong>', '«Si tengo tiempo, voy» (tipo 1: probable). «Si <b>tuviera</b> tiempo, iría» (tipo 2: hipotético/irreal). No mezcles: nunca «si tendría» o «si tenía» en la condición.'),
            ('Nosotros habláramos sin tilde', '<strong>habláramos</strong> (con tilde)', 'La forma nosotros del imperfecto de subjuntivo siempre lleva tilde: <b>habláramos</b>, <b>comiéramos</b>, <b>fuéramos</b>.'),
            ('Ojalá + indicativo para deseos poco probables', 'Ojalá + <strong>subjuntivo imperfecto</strong>', '«Ojalá tenía más tiempo» es incorrecto. Usa el subjuntivo: «Ojalá <b>tuviera</b> más tiempo» (poco probable) o «Ojalá <b>tenga</b> más tiempo» (posible).'),
            ('Dijera → deciera (regularizar el irregular)', '<strong>dijera</strong> (raíz del indefinido: dij-)', 'DECIR es irregular: ellos dijeron → imperfecto subj.: <b>dijera</b>. Nunca «deciera», ya que la raíz en subjuntivo viene del indefinido, no del infinitivo.'),
            ('Como si + indicativo', 'Como si + <strong>subjuntivo imperfecto</strong>', '«Habla como si <b>es</b> el director» es incorrecto. «Como si» siempre exige subjuntivo: «Habla como si <b>fuera</b> el director».'),
        ],
        summary=[
            ('Formación', 'Ellos (indefinido) − ron + -ra/-ras/-ra/-ramos/-rais/-ran', 'habla<b>ron</b> → <b>hablara</b>, hiciéron → <b>hiciera</b>'),
            ('Tilde en nosotros', 'Siempre tilde: -áramos / -iéramos', 'habláramos, comiéramos, tuviéramos'),
            ('Condicional tipo 2', 'Si + subj. imp. + condicional', 'Si pudiera, viviría en el campo.'),
            ('Ojalá + subj. imp.', 'Deseo poco probable o imposible', 'Ojalá tuviera más tiempo.'),
            ('Como si', 'Comparación irreal → siempre subj. imp.', 'Habla como si supiera todo.'),
            ('Subordinada en pasado', 'Verbo principal pasado → subj. imp.', 'Quería que lo hicieras tú.'),
            ('Irregulares clave', 'fuera, tuviera, pudiera, quisiera, dijera, supiera', 'Si fuera rico, donaría todo.'),
        ],
        ex1=('Elige la forma correcta de subjuntivo imperfecto', 'Selecciona la forma adecuada del imperfecto de subjuntivo.',
             [('Si ______ (tener, yo) más tiempo, leería más.', ['tengo', 'tuviera', 'tendría'], 1, 'Condicional tipo 2 → si + <b>subjuntivo imperfecto</b>: <b>tuviera</b>.'),
              ('Ojalá ______ (poder, tú) venir a la fiesta.', ['puedes', 'pudieras', 'podrías'], 1, 'Ojalá + subjuntivo imperfecto (deseo poco probable): <b>pudieras</b>.'),
              ('El profesor quería que nosotros ______ (estudiar) más.', ['estudiamos', 'estudiáramos', 'estudiábamos'], 1, 'Subordinada con verbo en pasado (quería) → subj. imp. nosotros: <b>estudiáramos</b>.'),
              ('Se comporta como si ______ (ser) el dueño del lugar.', ['es', 'fuera', 'sería'], 1, '«Como si» → siempre subjuntivo imperfecto: <b>fuera</b>.'),
              ('¿Cuál es el imperfecto de subjuntivo de DECIR para él?', ['deciera', 'dijera', 'diría'], 1, 'DECIR: ellos dijeron → raíz <b>dij-</b>: él → <b>dijera</b>.'),
              ('Le pedí que me ______ (llamar) antes de salir.', ['llama', 'llamara', 'llamaría'], 1, 'Pedir que + subjuntivo imperfecto (pasado): <b>llamara</b>.'),
             ]),
        ex2=('Escribe la forma de subjuntivo imperfecto', 'Conjuga el verbo entre paréntesis en pretérito imperfecto de subjuntivo.',
             [('Si (saber, yo) ______ la respuesta, te lo diría.', 'supiera', 'SABER: ellos supieron → yo subj. imp.: <b>supiera</b>.'),
              ('Ojalá (venir, ellos) ______ a visitarnos este verano.', 'vinieran', 'VENIR: ellos vinieron → subj. imp. ellos: <b>vinieran</b>.'),
              ('Me alegró mucho que tú (estar) ______ bien.', 'estuvieras', 'ESTAR: ellos estuvieron → tú subj. imp.: <b>estuvieras</b>.'),
              ('Habla como si (conocer) ______ a todo el mundo.', 'conociera', 'CONOCER: ellos conocieron → subj. imp. él/ella: <b>conociera</b>.'),
              ('Quería que nosotros (ir) ______ juntos a la conferencia.', 'fuéramos', 'IR: ellos fueron → nosotros subj. imp.: <b>fuéramos</b> (con tilde).'),
             ]),
        ex3=('Subjuntivo imperfecto en contexto', 'Elige la oración que usa correctamente el imperfecto de subjuntivo.',
             [('¿Cuál expresa una hipótesis irreal?', ['Si tengo dinero, viajo.', 'Si tuviera dinero, viajaría.', 'Si tendría dinero, viajaría.'], 1, 'Tipo 2: <b>si + subjuntivo imperfecto + condicional</b>: «Si <b>tuviera</b> dinero, viajaría».'),
              ('¿Cuál usa «ojalá» correctamente para un deseo poco probable?', ['Ojalá tengo tiempo.', 'Ojalá tendré tiempo.', 'Ojalá tuviera tiempo.'], 2, 'Deseo poco probable → ojalá + subjuntivo imperfecto: <b>tuviera</b>.'),
              ('¿Cuál usa «como si» correctamente?', ['Gasta como si es millonario.', 'Gasta como si fuera millonario.', 'Gasta como si será millonario.'], 1, '«Como si» → siempre subjuntivo: <b>fuera</b>.'),
              ('¿Cuál es la forma correcta de QUERER para nosotros en subj. imp.?', ['quisiéramos', 'queramos', 'quisiéremos'], 0, 'QUERER: quisieron → nosotros subj. imp.: <b>quisiéramos</b>.'),
              ('¿Cuál reporta correctamente una orden en pasado?', ['Me dijo que venir pronto.', 'Me dijo que viniera pronto.', 'Me dijo que vendría pronto.'], 1, 'Decir que + subjuntivo imperfecto para órdenes en pasado: <b>viniera</b>.'),
             ]),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('subjimp-01', 'tuviera', 'subjuntivo imperfecto de TENER (yo/él)', 'tener: cond. tipo 2 / deseos', 'Si tuviera más dinero, viajaría por el mundo.', 'Si ______ más dinero, viajaría por el mundo.', 'tuviera'),
            ('subjimp-02', 'fuera', 'subjuntivo imperfecto de SER/IR (yo/él)', 'ser/ir: hipótesis e irrealidad', 'Actúa como si fuera el jefe de todos.', 'Actúa como si ______ el jefe de todos.', 'fuera'),
            ('subjimp-03', 'pudiera', 'subjuntivo imperfecto de PODER (yo/él)', 'poder: deseos y condiciones irreales', 'Ojalá pudiera quedarme más tiempo.', 'Ojalá ______ quedarme más tiempo.', 'pudiera'),
            ('subjimp-04', 'dijera', 'subjuntivo imperfecto de DECIR (yo/él)', 'decir: raíz dij- del indefinido', 'Quería que lo dijera él mismo.', 'Quería que lo ______ él mismo.', 'dijera'),
            ('subjimp-05', 'habláramos', 'subjuntivo imperfecto de HABLAR (nosotros) — con tilde', 'nosotros: tilde obligatoria -áramos', 'Nos pidió que habláramos más despacio.', 'Nos pidió que ______ más despacio.', 'habláramos'),
            ('subjimp-06', 'quisiera', 'subjuntivo imperfecto de QUERER (yo/él)', 'querer: raíz quis- del indefinido', 'Ojalá quisiera acompañarnos.', 'Ojalá ______ acompañarnos.', 'quisiera'),
            ('subjimp-07', 'supiera', 'subjuntivo imperfecto de SABER (yo/él)', 'saber: raíz sup- del indefinido', 'Si supiera la verdad, te la contaría.', 'Si ______ la verdad, te la contaría.', 'supiera'),
            ('subjimp-08', 'vinieran', 'subjuntivo imperfecto de VENIR (ellos)', 'venir: raíz vinier- del indefinido', 'Le sorprendió que vinieran tan tarde.', 'Le sorprendió que ______ tan tarde.', 'vinieran'),
        ],
    ),

    'perifrasis-verbales': dict(
        level='b1',
        section='grammar',
        num='G10',
        short='Perífrasis Verbales',
        title='Las Perífrasis Verbales — Verbos que se combinan',
        subtitle='Expresa matices de tiempo, aspecto y modalidad con verbos auxiliares',
        slides=[
            ('¿Qué son las perífrasis verbales?', None,
             '<p class="slide-explanation">Una <b>perífrasis verbal</b> es una construcción de dos (o más) verbos que funciona como una unidad. '
             'El primer verbo (<b>auxiliar</b>) aporta el matiz de tiempo o aspecto; '
             'el segundo (<b>verbo principal</b>) lleva el contenido léxico. '
             'Se unen mediante un <b>infinitivo</b>, un <b>gerundio</b> o un <b>participio</b>, '
             'a veces con una preposición.</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>ir a + infinitivo</b>: Voy a estudiar. (intención futura)</p>'
             '<p><b>acabar de + infinitivo</b>: Acabo de llegar. (pasado reciente)</p>'
             '<p><b>llevar + gerundio</b>: Llevo dos horas esperando. (duración en curso)</p>'
             '<p><b>seguir + gerundio</b>: Sigue lloviendo. (continuación)</p>'
             '</div>'),

            ('Perífrasis de infinitivo (I)', None,
             '<p class="slide-explanation">Estas perífrasis se construyen con <b>verbo auxiliar + infinitivo</b> '
             '(con o sin preposición):</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Perífrasis</th><th style="padding:8px;text-align:left">Significado</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>ir a + inf.</b></td><td style="padding:8px">intención o futuro próximo</td><td style="padding:8px">Voy a llamar a mi madre.</td></tr>'
             '<tr><td style="padding:8px"><b>acabar de + inf.</b></td><td style="padding:8px">acción muy reciente</td><td style="padding:8px">Acaban de publicar los resultados.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>dejar de + inf.</b></td><td style="padding:8px">cesar una acción</td><td style="padding:8px">Ha dejado de fumar este año.</td></tr>'
             '<tr><td style="padding:8px"><b>ponerse a + inf.</b></td><td style="padding:8px">inicio de una acción</td><td style="padding:8px">Se puso a llorar de repente.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>volver a + inf.</b></td><td style="padding:8px">repetición de una acción</td><td style="padding:8px">Ha vuelto a cometer el mismo error.</td></tr>'
             '<tr><td style="padding:8px"><b>llegar a + inf.</b></td><td style="padding:8px">logro o punto culminante</td><td style="padding:8px">Llegó a ganar tres torneos.</td></tr>'
             '</table>'),

            ('Perífrasis de infinitivo (II): obligación y posibilidad', None,
             '<p class="slide-explanation">Estas perífrasis expresan <b>obligación</b>, <b>necesidad</b> o <b>posibilidad</b>:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Perífrasis</th><th style="padding:8px;text-align:left">Significado</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>tener que + inf.</b></td><td style="padding:8px">obligación personal</td><td style="padding:8px">Tengo que entregar el informe hoy.</td></tr>'
             '<tr><td style="padding:8px"><b>hay que + inf.</b></td><td style="padding:8px">obligación impersonal</td><td style="padding:8px">Hay que respetar las normas.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>deber + inf.</b></td><td style="padding:8px">obligación moral</td><td style="padding:8px">Debes llamar a tus padres.</td></tr>'
             '<tr><td style="padding:8px"><b>poder + inf.</b></td><td style="padding:8px">capacidad o permiso</td><td style="padding:8px">¿Puedo salir un momento?</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>deber de + inf.</b></td><td style="padding:8px">suposición o probabilidad</td><td style="padding:8px">Debe de ser tarde ya.</td></tr>'
             '</table>'
             '<p class="slide-explanation">Nota clave: <b>deber + inf.</b> (obligación) ≠ <b>deber <u>de</u> + inf.</b> (suposición). '
             'La preposición «de» cambia completamente el significado.</p>'),

            ('Perífrasis de gerundio', None,
             '<p class="slide-explanation">Estas perífrasis se forman con <b>verbo auxiliar + gerundio</b> '
             'y expresan acciones en desarrollo:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Perífrasis</th><th style="padding:8px;text-align:left">Significado</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>estar + gerundio</b></td><td style="padding:8px">acción en progreso en el momento</td><td style="padding:8px">Estoy comiendo ahora mismo.</td></tr>'
             '<tr><td style="padding:8px"><b>llevar + gerundio</b></td><td style="padding:8px">duración de una acción continua hasta ahora</td><td style="padding:8px">Llevo tres horas esperando.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>seguir + gerundio</b></td><td style="padding:8px">continuación de una acción</td><td style="padding:8px">Sigue nevando en las montañas.</td></tr>'
             '<tr><td style="padding:8px"><b>continuar + gerundio</b></td><td style="padding:8px">continuación (más formal que seguir)</td><td style="padding:8px">El proyecto continúa avanzando.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>andar + gerundio</b></td><td style="padding:8px">acción repetida e imprecisa</td><td style="padding:8px">Anda buscando trabajo desde enero.</td></tr>'
             '</table>'
             '<p class="slide-explanation">Con <b>llevar + gerundio</b>, la expresión de tiempo va inmediatamente después de «llevar»: '
             '«Llevo <b>dos años</b> estudiando español» (no «estudio español desde hace dos años», aunque también es correcto).</p>'),

            ('Contraste entre perífrasis similares', None,
             '<p class="slide-explanation">Es importante distinguir perífrasis que expresan matices parecidos:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Perífrasis A</th><th style="padding:8px;text-align:left">Perífrasis B</th><th style="padding:8px;text-align:left">Diferencia</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>ir a + inf.</b><br>Voy a hablar con él.</td><td style="padding:8px"><b>estar a punto de + inf.</b><br>Estoy a punto de hablar con él.</td><td style="padding:8px">«Ir a» = intención; «estar a punto de» = acción inminente en segundos.</td></tr>'
             '<tr><td style="padding:8px"><b>acabar de + inf.</b><br>Acabo de llamarle.</td><td style="padding:8px"><b>dejar de + inf.</b><br>Dejé de llamarle.</td><td style="padding:8px">«Acabar de» = hace un instante; «dejar de» = cesar definitivamente.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>seguir + ger.</b><br>Sigue estudiando.</td><td style="padding:8px"><b>volver a + inf.</b><br>Volvió a estudiar.</td><td style="padding:8px">«Seguir» = sin interrupción; «volver a» = lo hizo, paró, y empezó de nuevo.</td></tr>'
             '<tr><td style="padding:8px"><b>tener que + inf.</b><br>Tengo que estudiar.</td><td style="padding:8px"><b>hay que + inf.</b><br>Hay que estudiar.</td><td style="padding:8px">«Tener que» = obligación personal; «hay que» = norma general o impersonal.</td></tr>'
             '</table>'),
        ],
        traps=[
            ('Ir a + gerundio (confundir con estar + gerundio)', '<strong>ir a + infinitivo</strong> (no gerundio)', '«Voy a estudiando» es incorrecto. <b>Ir a</b> siempre va con <b>infinitivo</b>: «Voy a <b>estudiar</b>». El gerundio va con «estar», «seguir», «llevar»…'),
            ('Deber + infinitivo vs. deber de + infinitivo', '<strong>deber + inf.</strong> (obligación) ≠ <strong>deber de + inf.</strong> (suposición)', '«Debe llegar a tiempo» (obligación). «Debe <b>de</b> llegar tarde» (suposición: probablemente llegará tarde). La preposición «de» cambia completamente el significado.'),
            ('Llevar + que + infinitivo', '<strong>llevar + gerundio</strong> (no infinitivo)', '«Llevo dos horas que espero» es incorrecto en esta perífrasis. Lo correcto: «Llevo dos horas <b>esperando</b>» (gerundio).'),
            ('Acabar de + gerundio', '<strong>acabar de + infinitivo</strong>', '«Acabo de llegando» es incorrecto. <b>Acabar de</b> siempre va con <b>infinitivo</b>: «Acabo de <b>llegar</b>».'),
            ('Hay que conjugado: «hayo que», «has que»', '<strong>hay que</strong> es invariable', '«Hay que» es la única forma de esta perífrasis impersonal. No existe «hayo que», «has que», «hubo que salvo en pasado: «había que / hubo que + infinitivo».'),
        ],
        summary=[
            ('ir a + inf.', 'intención o futuro próximo', 'Voy a llamarte esta tarde.'),
            ('acabar de + inf.', 'acción muy reciente (pasado inmediato)', 'Acaba de salir del edificio.'),
            ('llevar + ger.', 'duración acumulada hasta el presente', 'Llevamos un año viviendo aquí.'),
            ('seguir/continuar + ger.', 'acción que continúa sin interrupción', 'Sigue estudiando a pesar del cansancio.'),
            ('dejar de + inf.', 'cese definitivo de una acción', 'Dejó de comer carne hace un año.'),
            ('ponerse a + inf.', 'inicio brusco o espontáneo de una acción', 'Se puso a cantar en medio de la calle.'),
            ('tener que / hay que + inf.', 'obligación personal / impersonal', 'Tienes que descansar. / Hay que respetar las normas.'),
        ],
        ex1=('Elige la perífrasis correcta', 'Selecciona la opción que completa correctamente cada oración.',
             [('No encuentro las llaves. ______ perderlas.', ['Acabo de perder', 'Debo de haber perdido', 'Llevo perdiendo'], 1, 'Suposición/probabilidad → <b>deber de + infinitivo</b>: «Debo de haberlas perdido».'),
              ('¿______ apagar la televisión? Quiero dormir.', ['Llevas', 'Puedes', 'Sigues'], 1, 'Petición de permiso o capacidad → <b>poder + infinitivo</b>: «¿<b>Puedes</b> apagar la televisión?»'),
              ('Estoy agotada. ______ trabajar doce horas seguidas.', ['Acabo de', 'Llevo', 'Me pongo a'], 1, 'Duración acumulada → <b>llevar + gerundio</b>: «<b>Llevo</b> trabajando doce horas».'),
              ('De repente, el niño ______ llorar sin ninguna razón.', ['fue a', 'se puso a', 'acabó de'], 1, 'Inicio brusco → <b>ponerse a + infinitivo</b>: «se puso a <b>llorar</b>».'),
              ('______ estudiar más si quieres aprobar el examen.', ['Hay que', 'Llevas', 'Acabas de'], 0, 'Obligación general/impersonal → <b>hay que + infinitivo</b>: «<b>Hay que</b> estudiar más».'),
              ('No te preocupes, ______ terminar el proyecto a tiempo.', ['vamos a', 'llevamos', 'seguimos de'], 0, 'Intención futura → <b>ir a + infinitivo</b>: «<b>Vamos a</b> terminar a tiempo».'),
             ]),
        ex2=('Completa con la perífrasis adecuada', 'Escribe la perífrasis verbal correcta.',
             [('El médico me ha dicho que ______ (dejar de / fumar) inmediatamente.', 'deje de fumar', '<b>Dejar de + infinitivo</b>: cese de una acción. En presente de subjuntivo por el verbo «ha dicho que»: <b>deje de fumar</b>.'),
              ('No entres, el director ______ (estar / hablar) por teléfono.', 'está hablando', '<b>Estar + gerundio</b>: acción en progreso: <b>está hablando</b>.'),
              ('¿Cuánto tiempo ______ (llevar / esperar, tú) aquí?', 'llevas esperando', '<b>Llevar + gerundio</b>: duración acumulada: <b>llevas esperando</b>.'),
              ('Después del accidente, ______ (volver a / conducir, él) al cabo de seis meses.', 'volvió a conducir', '<b>Volver a + infinitivo</b>: repetición de una acción: <b>volvió a conducir</b>.'),
              ('______ respetar el turno de palabra en las reuniones.', 'Hay que', 'Obligación impersonal y general → <b>hay que</b>. Solo esta forma es posible.'),
             ]),
        ex3=('Identifica el uso correcto de la perífrasis', 'Elige la oración que usa correctamente la perífrasis verbal.',
             [('¿Cuál usa correctamente «ir a»?', ['Voy a estudiando más.', 'Voy a estudiar más.', 'Voy estudiar más.'], 1, '<b>Ir a + infinitivo</b>: «Voy a <b>estudiar</b>» (no gerundio, no se omite «a»).'),
              ('¿Cuál expresa una acción reciente?', ['Acabo de comer.', 'Acabo comiendo.', 'Acabo de comiendo.'], 0, '<b>Acabar de + infinitivo</b>: «Acabo de <b>comer</b>».'),
              ('¿Cuál usa «llevar» correctamente?', ['Llevo dos horas que espero.', 'Llevo dos horas esperando.', 'Llevo esperando dos horas hace.'], 1, '<b>Llevar + tiempo + gerundio</b>: «Llevo dos horas <b>esperando</b>».'),
              ('¿Cuál expresa obligación personal (no impersonal)?', ['Hay que llamar al médico.', 'Tengo que llamar al médico.', 'Debe de llamar al médico.'], 1, 'Obligación personal → <b>tener que + infinitivo</b>: «<b>Tengo que</b> llamar».'),
              ('¿Cuál expresa que alguien dejó de hacer algo?', ['Sigue sin fumar.', 'Ha dejado de fumar.', 'Lleva sin fumar.'], 1, 'Cese definitivo → <b>dejar de + infinitivo</b>: «Ha <b>dejado de</b> fumar».'),
             ]),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('perifrasis-01', 'voy a estudiar', 'ir a + infinitivo — intención o futuro próximo', 'ir a + inf.: intención futura', 'Esta noche voy a estudiar para el examen.', 'Esta noche ______ estudiar para el examen.', 'voy a'),
            ('perifrasis-02', 'acabo de llegar', 'acabar de + infinitivo — acción muy reciente', 'acabar de + inf.: pasado inmediato', 'No me esperes, acabo de llegar a casa.', 'No me esperes, ______ llegar a casa.', 'acabo de'),
            ('perifrasis-03', 'lleva esperando', 'llevar + gerundio — duración acumulada', 'llevar + ger.: cuánto tiempo lleva', 'Mi madre lleva esperando media hora en la cola.', 'Mi madre ______ media hora en la cola.', 'lleva esperando'),
            ('perifrasis-04', 'sigue lloviendo', 'seguir + gerundio — continuación sin interrupción', 'seguir + ger.: la acción continúa', 'Aunque ya es tarde, sigue lloviendo con fuerza.', 'Aunque ya es tarde, ______ con fuerza.', 'sigue lloviendo'),
            ('perifrasis-05', 'ha dejado de fumar', 'dejar de + infinitivo — cese de una acción', 'dejar de + inf.: parar definitivamente', 'Mi padre ha dejado de fumar después de veinte años.', 'Mi padre ______ después de veinte años.', 'ha dejado de fumar'),
            ('perifrasis-06', 'se puso a llorar', 'ponerse a + infinitivo — inicio brusco', 'ponerse a + inf.: empezar de repente', 'Al escuchar la noticia, se puso a llorar sin poder parar.', 'Al escuchar la noticia, ______ sin poder parar.', 'se puso a llorar'),
            ('perifrasis-07', 'hay que estudiar', 'hay que + infinitivo — obligación impersonal', 'hay que + inf.: norma general', 'Para aprobar este examen, hay que estudiar mucho.', 'Para aprobar este examen, ______ mucho.', 'hay que estudiar'),
            ('perifrasis-08', 'volvió a cometer', 'volver a + infinitivo — repetición de una acción', 'volver a + inf.: hacer algo otra vez', 'No lo entiendo: volvió a cometer el mismo error.', 'No lo entiendo: ______ el mismo error.', 'volvió a cometer'),
        ],
    ),
}
