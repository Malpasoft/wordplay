# -*- coding: utf-8 -*-
"""espanol/ B2 Gramatica -- lote 1 (G01-G05)."""

CHAPTERS = {
    'subjuntivo-b2': dict(
        level='b2',
        section='grammar',
        num='G01',
        short='Subjuntivo: tres clausulas',
        title='El Subjuntivo en Oraciones Sustantivas, Adjetivas y Adverbiales',
        subtitle='Domina los tres contextos en que el subjuntivo es obligatorio',
        slides=[
            ('Oraciones sustantivas con subjuntivo', None,
             '<p class="slide-explanation">Las <b>oraciones sustantivas</b> funcionan como sujeto u objeto del verbo '
             'principal. Cuando la clausula principal expresa deseo, emocion, necesidad o temor, '
             'la subordinada va en subjuntivo:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Verbo principal</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>querer que</b></td>'
             '<td style="padding:8px">Quiero que <b>vengas</b> a la reunion.</td></tr>'
             '<tr><td style="padding:8px"><b>esperar que</b></td>'
             '<td style="padding:8px">Espero que <b>lleguen</b> a tiempo.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>necesitar que</b></td>'
             '<td style="padding:8px">Necesito que me <b>ayudes</b> con esto.</td></tr>'
             '<tr><td style="padding:8px"><b>temer que</b></td>'
             '<td style="padding:8px">Temo que no <b>haya</b> solucion.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>alegrarse de que</b></td>'
             '<td style="padding:8px">Me alegra que <b>estes</b> bien.</td></tr>'
             '</table>'
             '<p class="slide-explanation">Regla fundamental: si los sujetos son distintos, se usa subjuntivo. '
             'Si son el mismo, se usa infinitivo: <i>Quiero <b>venir</b></i> (mismo sujeto).</p>'),

            ('Oraciones adjetivas (de relativo) con subjuntivo', None,
             '<p class="slide-explanation">Las <b>oraciones de relativo</b> usan el subjuntivo cuando el antecedente '
             '(la persona o cosa a la que se refieren) es <b>indefinido</b> o <b>negativo</b>:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Tipo de antecedente</th>'
             '<th style="padding:8px;text-align:left">Indicativo o subjuntivo</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Conocido y existente</td>'
             '<td style="padding:8px"><b>Indicativo</b></td>'
             '<td style="padding:8px">Busco al piso que <b>tiene</b> terraza. (existe, lo conozco)</td></tr>'
             '<tr><td style="padding:8px">Indefinido (no se sabe si existe)</td>'
             '<td style="padding:8px"><b>Subjuntivo</b></td>'
             '<td style="padding:8px">Busco un piso que <b>tenga</b> terraza. (cualquiera que cumpla esto)</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Negativo (no existe)</td>'
             '<td style="padding:8px"><b>Subjuntivo</b></td>'
             '<td style="padding:8px">No hay nadie que <b>sepa</b> la respuesta.</td></tr>'
             '</table>'
             '<p class="slide-explanation">La clave: <b>articulo indefinido</b> (un/una/unos) o '
             '<b>negacion</b> (no hay, no conozco) ante el antecedente → subjuntivo.</p>'),

            ('Oraciones adverbiales temporales y finales', None,
             '<p class="slide-explanation">Las <b>oraciones adverbiales temporales</b> con <i>cuando</i>, '
             '<i>en cuanto</i>, <i>hasta que</i>, <i>antes de que</i> usan subjuntivo cuando se refieren al '
             'futuro. Las <b>finales</b> con <i>para que</i> siempre exigen subjuntivo:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Temporal (futuro) → subj.:</b> Llama <b>cuando llegues</b> a casa.</p>'
             '<p><b>Temporal (habito/pasado) → indic.:</b> Siempre me llamas <b>cuando llegas</b>.</p>'
             '<p><b>En cuanto (futuro):</b> En cuanto <b>termines</b>, avísame.</p>'
             '<p><b>Antes de que:</b> Sal antes de que <b>empiece</b> a llover.</p>'
             '<p><b>Final con para que:</b> Te lo explico para que <b>entiendas</b>.</p>'
             '</div>'
             '<p class="slide-explanation">La diferencia clave con <i>cuando</i>: '
             'si la accion es habitual o pasada → indicativo; si es futura o hipotetica → subjuntivo.</p>'),

            ('Oraciones concesivas y condicionales', None,
             '<p class="slide-explanation"><b>Aunque</b> puede ir con indicativo (hecho real) o subjuntivo '
             '(posibilidad o informacion no relevante). Las condicionales con <b>si + presente de subj.</b> '
             'son una variante formal de las condicionales reales:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Nexo</th>'
             '<th style="padding:8px;text-align:left">Modo</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">aunque (hecho cierto)</td>'
             '<td style="padding:8px">Indicativo</td>'
             '<td style="padding:8px">Aunque <b>llueve</b>, saldré. (se que llueve)</td></tr>'
             '<tr><td style="padding:8px">aunque (posibilidad)</td>'
             '<td style="padding:8px">Subjuntivo</td>'
             '<td style="padding:8px">Aunque <b>llueva</b>, saldre. (puede que llueva)</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">a menos que</td>'
             '<td style="padding:8px">Subjuntivo siempre</td>'
             '<td style="padding:8px">Ire a menos que <b>llueva</b> mucho.</td></tr>'
             '<tr><td style="padding:8px">con tal de que</td>'
             '<td style="padding:8px">Subjuntivo siempre</td>'
             '<td style="padding:8px">Lo hare con tal de que me <b>ayudes</b>.</td></tr>'
             '</table>'),

            ('Concordancia temporal del subjuntivo', None,
             '<p class="slide-explanation">La <b>concordancia temporal</b> determina que tiempo de subjuntivo usar '
             'segun el tiempo del verbo principal:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Verbo principal</th>'
             '<th style="padding:8px;text-align:left">Subjuntivo subordinado</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Presente / Futuro</td>'
             '<td style="padding:8px">Presente de subjuntivo</td>'
             '<td style="padding:8px">Quiero que <b>vengas</b>. / Querr&eacute; que <b>vengas</b>.</td></tr>'
             '<tr><td style="padding:8px">Indefinido / Imperfecto / Condicional</td>'
             '<td style="padding:8px">Imperfecto de subjuntivo</td>'
             '<td style="padding:8px">Quería que <b>vinieras</b>. / Querria que <b>vinieras</b>.</td></tr>'
             '</table>'
             '<p class="slide-explanation">Regla practica: presente/futuro → subj. presente; '
             'pasado/condicional → subj. imperfecto.</p>'),
        ],
        traps=[
            ('Busco un piso que tiene terraza', 'Busco un piso que <strong>tenga</strong> terraza',
             'El antecedente «un piso» es indefinido (no se sabe si existe ese piso especifico): la oracion de relativo '
             'exige subjuntivo. El indicativo «tiene» implicaria que el piso ya existe y se conoce.'),
            ('Llama cuando llegas → referencia al futuro', 'Llama cuando <strong>llegues</strong>',
             'Las oraciones temporales con <i>cuando</i> y referencia al futuro requieren subjuntivo: '
             '<b>cuando llegues</b>. El indicativo «llegas» solo se usa para acciones habituales o pasadas.'),
            ('Te lo explico para que entiendes', 'Te lo explico para que <strong>entiendas</strong>',
             'La conjuncion <b>para que</b> siempre exige subjuntivo. Nunca va seguida de indicativo.'),
            ('Aunque llueve, saldre (queriendo indicar posibilidad)', 'Aunque <strong>llueva</strong>, saldre',
             'Si la lluvia es una posibilidad (no un hecho confirmado), se usa subjuntivo: <b>aunque llueva</b>. '
             'El indicativo <i>aunque llueve</i> afirma que en efecto esta lloviendo.'),
            ('Queria que vienes', 'Queria que <strong>vinieras</strong>',
             'La concordancia temporal exige que un verbo principal en pasado (queria) '
             'vaya seguido de subjuntivo <b>imperfecto</b>, no de subjuntivo presente.'),
        ],
        summary=[
            ('Sustantivas (deseo/emocion/necesidad)', 'querer/esperar/alegrarse de que + subj.', 'Espero que llegues pronto.'),
            ('Adjetivas (antecedente indefinido)', 'un/una + sust. + que + subj.', 'Busco un piso que tenga terraza.'),
            ('Adjetivas (antecedente negativo)', 'no hay/nadie/nada + que + subj.', 'No hay nadie que sepa la respuesta.'),
            ('Temporales con cuando (futuro)', 'cuando + pres. subj. (accion futura)', 'Llama cuando llegues.'),
            ('Finales con para que', 'para que + subj. (siempre)', 'Te lo explico para que entiendas.'),
            ('Concesivas con aunque', 'aunque + subj. (posibilidad) / indic. (hecho)', 'Aunque llueva, saldre.'),
            ('Concordancia temporal', 'pres./fut. → subj. pres.; pasado/cond. → subj. imperf.', 'Queria que vinieras.'),
        ],
        ex1=dict(
            title='Elige el modo correcto',
            questions=[
                ('Busco una secretaria que ______ tres idiomas.', ['habla', 'hable', 'hablara', 'hablaria'], 1,
                 'Antecedente indefinido (se busca a cualquiera que cumpla el requisito): subjuntivo presente → <b>hable</b>.'),
                ('Llama en cuanto ______ (llegar, tu) al hotel.', ['llegas', 'llegaras', 'llegues', 'llegaras'], 2,
                 'Temporal con <i>en cuanto</i> y referencia al futuro: subjuntivo presente → <b>llegues</b>.'),
                ('Queria que todos ______ (venir) a la cena.', ['vienen', 'vengan', 'vinieran', 'vendrian'], 2,
                 'Verbo principal en pasado (queria) + cambio de sujeto: subjuntivo imperfecto → <b>vinieran</b>.'),
                ('No hay nadie en la oficina que ______ (saber) donde esta el jefe.', ['sabe', 'sepa', 'supiera', 'sabria'], 1,
                 'Antecedente negativo (<i>no hay nadie</i>): subjuntivo presente → <b>sepa</b>.'),
                ('Te presto el coche con tal de que lo ______ (cuidar) bien.', ['cuidas', 'cuidaras', 'cuides', 'cuidabas'], 2,
                 '<i>Con tal de que</i> siempre exige subjuntivo → <b>cuides</b>.'),
                ('Aunque ______ (estar) cansado, termino el trabajo.', ['este', 'estoy', 'estuviera', 'estaria'], 1,
                 'El hablante confirma que esta cansado (hecho cierto): indicativo → <b>estoy</b>.'),
            ]
        ),
        ex2=dict(
            title='Escribe la forma correcta del subjuntivo',
            questions=[
                ('Espero que vosotros ______ (leer) el informe antes de la reunion.',
                 'leais', ['leáis', 'leais'],
                 'Esperar que + cambio de sujeto → subjuntivo presente. LEER, vosotros: <b>leais</b>.'),
                ('Cuando ______ (terminar, tu) los deberes, puedes salir.',
                 'termines', ['termines'],
                 'Temporal con <i>cuando</i>, referencia al futuro → subjuntivo presente: <b>termines</b>.'),
                ('Necesitaba a alguien que ______ (poder) trabajar los fines de semana.',
                 'pudiera', ['pudiera'],
                 'Antecedente indefinido con verbo principal en pasado → subjuntivo imperfecto: <b>pudiera</b>.'),
                ('Te lo cuento para que ______ (entender) la situacion.',
                 'entiendas', ['entiendas'],
                 '<i>Para que</i> siempre exige subjuntivo → ENTENDER toma vocal opuesta: <b>entiendas</b>.'),
                ('No conozco a nadie que ______ (hablar) cinco idiomas.',
                 'hable', ['hable'],
                 'Antecedente negativo (<i>nadie</i>): subjuntivo presente → <b>hable</b>.'),
            ]
        ),
        ex3=dict(
            title='Identifica el uso correcto del subjuntivo',
            questions=[
                ('¿Que oracion usa el subjuntivo correctamente en una relativa?',
                 ['Conozco a un medico que habla ruso.',
                  'Busco un medico que hable ruso.',
                  'Conozco a un medico que hable ruso.',
                  'Busco al medico que habla ruso.'],
                 1,
                 'Antecedente indefinido «un medico» (no sabemos si existe) → subjuntivo <b>hable</b>. '
                 'Si el antecedente es conocido y existente, se usa indicativo.'),
                ('¿Cual es la oracion temporal correcta con referencia al futuro?',
                 ['Llame cuando llego.',
                  'Llamame cuando llegas.',
                  'Llamame cuando llegues.',
                  'Llamame cuando llegabas.'],
                 2,
                 'Temporal con <i>cuando</i> y accion futura → subjuntivo: <b>cuando llegues</b>.'),
                ('¿Cual usa <i>aunque</i> correctamente para indicar posibilidad?',
                 ['Aunque llueve, ire.',
                  'Aunque llueva, ire.',
                  'Aunque lloviera, ire.',
                  'Aunque ha llovido, ire.'],
                 1,
                 'Posibilidad (puede que llueva) → subjuntivo presente: <b>aunque llueva</b>. '
                 'El imperfecto sería para contextos hipoteticos pasados.'),
                ('¿Que estructura sigue obligatoriamente la final <i>para que</i>?',
                 ['para que + futuro', 'para que + indicativo', 'para que + subjuntivo', 'para que + condicional'],
                 2,
                 '<i>Para que</i> siempre va seguido de <b>subjuntivo</b>, sin excepcion.'),
                ('Si el verbo principal esta en indefinido, ¿que tiempo de subjuntivo se usa en la subordinada?',
                 ['Presente de subjuntivo', 'Futuro de subjuntivo', 'Imperfecto de subjuntivo', 'Pluscuamperfecto'],
                 2,
                 'Concordancia temporal: verbo principal en pasado (indefinido) → subjuntivo <b>imperfecto</b>: '
                 'quise que <b>vinieras</b>.'),
            ]
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            dict(term='hable', definition='subjuntivo presente de HABLAR (yo/el): oracion sustantiva o relativa con antecedente indefinido',
                 example='Quiero que el <b>hable</b> con nosotros.', accept=['hable']),
            dict(term='llegues', definition='subjuntivo presente de LLEGAR (tu): temporal con cuando referido al futuro',
                 example='Llamame cuando <b>llegues</b> a casa.', accept=['llegues']),
            dict(term='tenga', definition='subjuntivo presente de TENER (yo/el): relativa con antecedente indefinido',
                 example='Busco un piso que <b>tenga</b> terraza.', accept=['tenga']),
            dict(term='vinieran', definition='subjuntivo imperfecto de VENIR (ellos): concordancia temporal con pasado',
                 example='Queria que todos <b>vinieran</b> a la fiesta.', accept=['vinieran']),
            dict(term='sepa', definition='subjuntivo presente de SABER (yo/el): relativa con antecedente negativo',
                 example='No hay nadie que <b>sepa</b> la respuesta.', accept=['sepa']),
            dict(term='entiendas', definition='subjuntivo presente de ENTENDER (tu): oracion final con para que',
                 example='Te lo explico para que <b>entiendas</b> el tema.', accept=['entiendas']),
            dict(term='llueva', definition='subjuntivo presente de LLOVER: concesiva con aunque (posibilidad)',
                 example='Aunque <b>llueva</b>, iremos al parque.', accept=['llueva']),
            dict(term='cuides', definition='subjuntivo presente de CUIDAR (tu): condicional con con tal de que',
                 example='Te presto el libro con tal de que lo <b>cuides</b>.', accept=['cuides']),
        ],
    ),

    'subjuntivo-perfecto': dict(
        level='b2',
        section='grammar',
        num='G02',
        short='Subjuntivo Perfecto',
        title='El Subjuntivo Perfecto y Pluscuamperfecto',
        subtitle='Acciones completadas en la esfera del presente y pasado hipotetico',
        slides=[
            ('El subjuntivo perfecto: haya + participio', None,
             '<p class="slide-explanation">El <b>subjuntivo perfecto</b> (haya + participio) expresa una accion '
             'completada vista desde una perspectiva de presente o futuro, en contextos que exigen subjuntivo:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Pronombre</th>'
             '<th style="padding:8px;text-align:left">HABER (subj. pres.)</th>'
             '<th style="padding:8px;text-align:left">+ participio</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">yo</td><td style="padding:8px"><b>haya</b></td><td style="padding:8px">haya comido / hablado / ido</td></tr>'
             '<tr><td style="padding:8px">tu</td><td style="padding:8px"><b>hayas</b></td><td style="padding:8px">hayas comido</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">el/ella</td><td style="padding:8px"><b>haya</b></td><td style="padding:8px">haya llegado</td></tr>'
             '<tr><td style="padding:8px">nosotros</td><td style="padding:8px"><b>hayamos</b></td><td style="padding:8px">hayamos terminado</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">vosotros</td><td style="padding:8px"><b>hayais</b></td><td style="padding:8px">hayais vuelto</td></tr>'
             '<tr><td style="padding:8px">ellos/ellas</td><td style="padding:8px"><b>hayan</b></td><td style="padding:8px">hayan podido</td></tr>'
             '</table>'
             '<p class="slide-explanation">Se usa cuando el verbo principal esta en presente y la accion subordinada '
             'es anterior: <i>Espero que <b>hayas comido</b> algo.</i></p>'),

            ('Usos del subjuntivo perfecto', None,
             '<p class="slide-explanation">El subjuntivo perfecto aparece en los mismos contextos que el presente de subjuntivo, '
             'pero cuando la accion de la subordinada es <b>anterior</b> a la del verbo principal:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Deseo/esperanza:</b> Espero que <b>hayas llegado</b> bien. (espero ahora; llegas/llegaste antes)</p>'
             '<p><b>Valoracion:</b> Es una lastima que no <b>hayas venido</b> ayer.</p>'
             '<p><b>Duda/negacion:</b> No creo que <b>hayan terminado</b> ya el proyecto.</p>'
             '<p><b>Temporal (hasta que / en cuanto):</b> Avísame en cuanto <b>hayas leido</b> el correo.</p>'
             '</div>'
             '<p class="slide-explanation">Comparacion: <i>Espero que <b>venga</b></i> (accion futura) vs. '
             '<i>Espero que <b>haya venido</b></i> (accion anterior al momento presente).</p>'),

            ('El subjuntivo pluscuamperfecto: hubiera + participio', None,
             '<p class="slide-explanation">El <b>subjuntivo pluscuamperfecto</b> (hubiera + participio) expresa '
             'una accion completa en el pasado, anterior a otro momento pasado, en contextos de subjuntivo:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Pronombre</th>'
             '<th style="padding:8px;text-align:left">HABER (subj. imperf.)</th>'
             '<th style="padding:8px;text-align:left">+ participio</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">yo</td><td style="padding:8px"><b>hubiera</b></td><td style="padding:8px">hubiera venido / dicho / hecho</td></tr>'
             '<tr><td style="padding:8px">tu</td><td style="padding:8px"><b>hubieras</b></td><td style="padding:8px">hubieras llegado</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">el/ella</td><td style="padding:8px"><b>hubiera</b></td><td style="padding:8px">hubiera sabido</td></tr>'
             '<tr><td style="padding:8px">nosotros</td><td style="padding:8px"><b>hubieramos</b></td><td style="padding:8px">hubieramos podido</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">vosotros</td><td style="padding:8px"><b>hubierais</b></td><td style="padding:8px">hubierais visto</td></tr>'
             '<tr><td style="padding:8px">ellos/ellas</td><td style="padding:8px"><b>hubieran</b></td><td style="padding:8px">hubieran dicho</td></tr>'
             '</table>'),

            ('Condicional tipo 3: Si hubiera + habria', None,
             '<p class="slide-explanation">El <b>condicional tipo 3</b> expresa una hipotesis irreal en el pasado: '
             'algo que no ocurrio. La estructura es:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p style="font-size:1.1em;font-weight:bold">Si + hubiera + participio → habria + participio</p>'
             '</div>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Condicion (irreal en pasado)</th>'
             '<th style="padding:8px;text-align:left">Consecuencia</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Si hubiera <b>sabido</b>,</td>'
             '<td style="padding:8px">habria <b>venido</b>. (pero no supe, no vine)</td></tr>'
             '<tr><td style="padding:8px">Si hubiera <b>estudiado</b>,</td>'
             '<td style="padding:8px">habria <b>aprobado</b>. (pero no estudie, no aprobe)</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Si me lo hubiera <b>dicho</b>,</td>'
             '<td style="padding:8px">te habria <b>ayudado</b>. (no me lo dijiste)</td></tr>'
             '</table>'
             '<p class="slide-explanation">Variante: <b>hubiese</b> + participio es equivalente a hubiera en todos los contextos.</p>'),

            ('Subjuntivo perfecto en discurso indirecto', None,
             '<p class="slide-explanation">En el <b>discurso indirecto en pasado</b>, el subjuntivo perfecto o '
             'pluscuamperfecto aparece cuando el verbo introductor esta en pasado:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Directo:</b> «Espero que hayas comido.»</p>'
             '<p><b>Indirecto presente:</b> Dice que espera que <b>hayas comido</b>.</p>'
             '<p><b>Indirecto pasado:</b> Dijo que esperaba que <b>hubieras comido</b>.</p>'
             '<p>&nbsp;</p>'
             '<p><b>Directo:</b> «No creo que haya llegado.»</p>'
             '<p><b>Indirecto pasado:</b> Dijo que no creia que <b>hubiera llegado</b>.</p>'
             '</div>'
             '<p class="slide-explanation">La concordancia temporal sigue la misma regla general: '
             'verbo principal en pasado → subjuntivo pluscuamperfecto en la subordinada.</p>'),
        ],
        traps=[
            ('Si hubiera sabido, habria venido → Si habria sabido, habria venido', 'Si <strong>hubiera</strong> sabido, habria venido',
             'En el condicional tipo 3, la clausula con <i>si</i> nunca lleva condicional. '
             'Lo correcto es siempre <b>si + hubiera + participio</b>.'),
            ('Espero que has terminado → con indicativo', 'Espero que <strong>hayas terminado</strong>',
             'Tras verbos de esperanza y deseo, la subordinada va en subjuntivo: <b>hayas terminado</b>, '
             'no el perfecto de indicativo «has terminado».'),
            ('No creo que ha llegado', 'No creo que <strong>haya llegado</strong>',
             'La negacion de certeza exige subjuntivo: <b>haya llegado</b> (subj. perfecto). '
             '«Ha llegado» es perfecto de indicativo y no puede usarse tras «no creo que».'),
            ('Si hubiera sabido, habria sabido (tipo 3 con mismo verbo)', 'Si hubiera sabido, habria <strong>venido</strong> (otro verbo en la consecuencia)',
             'En el tipo 3, la consecuencia expresa que habria ocurrido otra cosa diferente: '
             'si hubiera sabido → habria venido (no: si hubiera sabido → habria sabido, que es una tautologia).'),
            ('Hubiera o hubiese: son diferentes', '<strong>Hubiera</strong> y <strong>hubiese</strong> son equivalentes',
             'Las formas en <b>-ra</b> (hubiera) y en <b>-se</b> (hubiese) del subjuntivo imperfecto '
             'son intercambiables en todos los contextos.'),
        ],
        summary=[
            ('Subj. perfecto: haya + part.', 'haya/hayas/haya/hayamos/hayais/hayan + participio', 'Espero que hayas llegado bien.'),
            ('Cuando usar subj. perfecto', 'Subord. anterior al presente, en contexto de subj.', 'Es una lastima que no hayas venido.'),
            ('Subj. pluscuamperfecto: hubiera + part.', 'hubiera/hubieras… + participio', 'No creia que hubiera llegado tan pronto.'),
            ('Condicional tipo 3', 'Si + hubiera + part. → habria + part.', 'Si hubiera estudiado, habria aprobado.'),
            ('NUNCA: si + condicional compuesto', 'si + NUNCA habria/habrias…', 'Incorrecto: *Si habria sabido…'),
            ('Discurso indirecto en pasado', 'dijo que esperaba que + subj. pluscuamperf.', 'Dijo que esperaba que hubiera comido.'),
            ('Hubiera = hubiese', 'Formas equivalentes del subj. imperf.', 'Si lo hubiera/hubiese sabido, habria venido.'),
        ],
        ex1=dict(
            title='Elige la forma correcta del subjuntivo compuesto',
            questions=[
                ('Espero que tu ______ (recibir) mi mensaje de ayer.',
                 ['has recibido', 'hayas recibido', 'hubiera recibido', 'recibieras'], 1,
                 'Esperar que + subj.: accion anterior al presente → subjuntivo perfecto: <b>hayas recibido</b>.'),
                ('Es una lastima que ellos no ______ (poder) venir a la boda.',
                 ['han podido', 'hayan podido', 'hubieran podido', 'podrian'], 1,
                 'Valoracion (<i>es una lastima que</i>) + accion anterior al presente → subj. perfecto: <b>hayan podido</b>.'),
                ('Si ______ (saber, yo) la verdad antes, habria actuado de otra forma.',
                 ['hubiera sabido', 'habria sabido', 'haya sabido', 'supiera'], 0,
                 'Condicional tipo 3: si + <b>hubiera + participio</b>: <b>si hubiera sabido</b>.'),
                ('Dijo que no creia que el jefe ______ (firmar) el contrato.',
                 ['haya firmado', 'hubiera firmado', 'habia firmado', 'firmara'], 1,
                 'Discurso indirecto en pasado: «dijo que no creia que» → subjuntivo <b>pluscuamperfecto</b>: hubiera firmado.'),
                ('No creo que todavia ______ (terminar, ellos) el informe.',
                 ['han terminado', 'hayan terminado', 'hubieran terminado', 'terminaran'], 1,
                 'No creer que + accion anterior al presente (verbo principal en presente) → subj. perfecto: <b>hayan terminado</b>.'),
                ('Avísame en cuanto ______ (leer, tu) el documento.',
                 ['leas', 'hayas leido', 'leyeras', 'hayas leido'], 1,
                 '<i>En cuanto</i> con accion anterior al momento futuro → subj. perfecto: <b>hayas leido</b>.'),
            ]
        ),
        ex2=dict(
            title='Completa con el subjuntivo compuesto correcto',
            questions=[
                ('Si lo ______ (decir, tu) antes, habria podido ayudarte.',
                 'hubieras dicho', ['hubieras dicho', 'hubieses dicho'],
                 'Condicional tipo 3: si + subjuntivo pluscuamperfecto → <b>hubieras dicho</b>.'),
                ('Me alegra que ______ (resolver, vosotros) el problema.',
                 'hayais resuelto', ['hayáis resuelto', 'hayais resuelto'],
                 'Emocion positiva + subj.: accion anterior al presente → subj. perfecto vosotros: <b>hayais resuelto</b>.'),
                ('No habia nadie que ______ (ver) lo que paso.',
                 'hubiera visto', ['hubiera visto', 'hubiese visto'],
                 'Antecedente negativo con verbo principal en pasado → subj. pluscuamperfecto: <b>hubiera visto</b>.'),
                ('Si ellos ______ (llegar) a tiempo, habrian encontrado un sitio.',
                 'hubieran llegado', ['hubieran llegado', 'hubiesen llegado'],
                 'Condicional tipo 3: si + hubiera/hubieran + participio → <b>hubieran llegado</b>.'),
                ('Es increible que tu ______ (olvidar) nuestro aniversario.',
                 'hayas olvidado', ['hayas olvidado'],
                 'Valoracion con verbo principal en presente → subj. perfecto: <b>hayas olvidado</b>.'),
            ]
        ),
        ex3=dict(
            title='Condicional tipo 3 y subjuntivo compuesto',
            questions=[
                ('¿Cual forma el condicional tipo 3 correctamente?',
                 ['Si habria llegado antes, lo habria visto.',
                  'Si hubiera llegado antes, lo habria visto.',
                  'Si llegara antes, lo habria visto.',
                  'Si hubiera llegado antes, lo hubiera habido visto.'],
                 1,
                 'Tipo 3: <b>si + hubiera + participio → habria + participio</b>: si hubiera llegado, lo habria visto.'),
                ('¿En que se diferencia el subj. perfecto del pluscuamperfecto?',
                 ['No hay diferencia, son identicos.',
                  'El perfecto usa haya y se orienta al presente; el pluscuamperfecto usa hubiera y se orienta al pasado.',
                  'El perfecto usa hubiera; el pluscuamperfecto usa haya.',
                  'El perfecto es solo para verbos regulares.'],
                 1,
                 '<b>Haya + part.</b> = subj. perfecto (presente). <b>Hubiera + part.</b> = subj. pluscuamperfecto (pasado anterior a otro pasado).'),
                ('¿Cual usa el subjuntivo perfecto correctamente?',
                 ['Espero que has descansado.',
                  'Espero que hayas descansado.',
                  'Espero que hubieras descansado.',
                  'Espero que habias descansado.'],
                 1,
                 'Esperar que + accion anterior al presente → subj. perfecto: <b>hayas descansado</b>.'),
                ('En discurso indirecto pasado, «Espero que hayas llegado» se transforma en:',
                 ['Dijo que esperaba que hayas llegado.',
                  'Dijo que esperaba que hubieras llegado.',
                  'Dijo que espera que hayas llegado.',
                  'Dijo que esperaba que has llegado.'],
                 1,
                 'Concordancia temporal: verbo introductor en pasado → subj. pluscuamperfecto: <b>hubieras llegado</b>.'),
                ('¿Cual de estas frases es equivalente a «Si lo hubiese sabido, habria venido»?',
                 ['Si lo hubiera sabido, habria venido.',
                  'Si lo habria sabido, habria venido.',
                  'Si lo supiera, vendria.',
                  'Si lo hubiera sabido, vendria.'],
                 0,
                 '<b>Hubiese</b> y <b>hubiera</b> son formas equivalentes del subj. pluscuamperfecto. '
                 'La consecuencia correcta es <i>habria venido</i> (condicional compuesto).'),
            ]
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            dict(term='haya llegado', definition='subjuntivo perfecto de LLEGAR: accion anterior al presente en contexto de subjuntivo',
                 example='Espero que <b>haya llegado</b> bien a casa.', accept=['haya llegado']),
            dict(term='hayas comido', definition='subjuntivo perfecto de COMER (tu): valoracion de accion anterior al presente',
                 example='Me alegra que <b>hayas comido</b> algo antes de salir.', accept=['hayas comido']),
            dict(term='hubiera sabido', definition='subjuntivo pluscuamperfecto de SABER: condicional tipo 3 o subord. pasada anterior',
                 example='Si <b>hubiera sabido</b> la verdad, habria actuado diferente.', accept=['hubiera sabido', 'hubiese sabido']),
            dict(term='hubieran terminado', definition='subjuntivo pluscuamperfecto de TERMINAR (ellos): subordinada en pasado',
                 example='Dijo que no creia que <b>hubieran terminado</b> el proyecto.', accept=['hubieran terminado', 'hubiesen terminado']),
            dict(term='habria venido', definition='condicional compuesto de VENIR: consecuencia del condicional tipo 3',
                 example='Si hubiera sabido, <b>habria venido</b> a la fiesta.', accept=['habria venido']),
            dict(term='hayan resuelto', definition='subjuntivo perfecto de RESOLVER (ellos): duda o negacion de accion anterior',
                 example='No creo que <b>hayan resuelto</b> el problema todavia.', accept=['hayan resuelto']),
            dict(term='hubieras dicho', definition='subjuntivo pluscuamperfecto de DECIR (tu): condicional tipo 3',
                 example='Si <b>hubieras dicho</b> algo, habria podido ayudarte.', accept=['hubieras dicho', 'hubieses dicho']),
            dict(term='hayas descansado', definition='subjuntivo perfecto de DESCANSAR (tu): esperanza sobre accion anterior al presente',
                 example='Espero que <b>hayas descansado</b> bien esta noche.', accept=['hayas descansado']),
        ],
    ),

    'ser-estar-b2': dict(
        level='b2',
        section='grammar',
        num='G03',
        short='SER y ESTAR avanzado',
        title='SER y ESTAR: Usos Avanzados y Diferencias de Significado',
        subtitle='Adjetivos que cambian de significado segun ser o estar',
        slides=[
            ('Repaso: ser (identidad) vs. estar (estado)', None,
             '<p class="slide-explanation">A nivel B2, la distincion fundamental ya se conoce: '
             '<b>ser</b> expresa identidad, origen y cualidades permanentes; <b>estar</b> expresa '
             'estados, condiciones y ubicacion. Pero hay usos mas sutiles que requieren dominio avanzado.</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">SER</th>'
             '<th style="padding:8px;text-align:left">ESTAR</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">identidad: Es medico. Es espanol.</td>'
             '<td style="padding:8px">estado: Esta cansado. Esta enfermo.</td></tr>'
             '<tr><td style="padding:8px">origen/material: Es de Madrid. Es de madera.</td>'
             '<td style="padding:8px">ubicacion: El libro esta en la mesa.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">tiempo/fecha: Son las tres. Es lunes.</td>'
             '<td style="padding:8px">resultado de accion: La puerta esta cerrada.</td></tr>'
             '<tr><td style="padding:8px">evento (donde ocurre): El concierto es en Madrid.</td>'
             '<td style="padding:8px">participio (pasiva estado): El trabajo esta hecho.</td></tr>'
             '</table>'),

            ('Adjetivos con significado diferente segun ser o estar', None,
             '<p class="slide-explanation">Algunos adjetivos cambian radicalmente de significado segun vayan con '
             '<b>ser</b> o <b>estar</b>. Este es el uso mas avanzado y mas importante a nivel B2:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Adjetivo</th>'
             '<th style="padding:8px;text-align:left">Con SER</th>'
             '<th style="padding:8px;text-align:left">Con ESTAR</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>listo/a</b></td>'
             '<td style="padding:8px"><b>es listo</b> = es inteligente</td>'
             '<td style="padding:8px"><b>esta listo</b> = esta preparado</td></tr>'
             '<tr><td style="padding:8px"><b>malo/a</b></td>'
             '<td style="padding:8px"><b>es malo</b> = es malvado / de mala calidad</td>'
             '<td style="padding:8px"><b>esta malo</b> = esta enfermo</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>aburrido/a</b></td>'
             '<td style="padding:8px"><b>es aburrido</b> = es una persona/cosa aburrida</td>'
             '<td style="padding:8px"><b>esta aburrido</b> = siente aburrimiento</td></tr>'
             '<tr><td style="padding:8px"><b>rico/a</b></td>'
             '<td style="padding:8px"><b>es rico</b> = tiene mucho dinero</td>'
             '<td style="padding:8px"><b>esta rico</b> = sabe delicioso</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>seguro/a</b></td>'
             '<td style="padding:8px"><b>es seguro</b> = no hay peligro (lugar/objeto)</td>'
             '<td style="padding:8px"><b>esta seguro</b> = tiene certeza / se siente seguro</td></tr>'
             '<tr><td style="padding:8px"><b>vivo/a</b></td>'
             '<td style="padding:8px"><b>es vivo</b> = es astuto/listo</td>'
             '<td style="padding:8px"><b>esta vivo</b> = tiene vida (no ha muerto)</td></tr>'
             '</table>'),

            ('ESTAR con adjetivos de ser: sorpresa o cambio', None,
             '<p class="slide-explanation">En espanol coloquial, se puede usar <b>estar</b> con adjetivos que '
             'normalmente acompanan a <b>ser</b> para expresar <b>sorpresa</b> o un <b>cambio notable</b> '
             'respecto a lo habitual:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Esta muy guapa hoy.</b> (normalmente no tanto, pero hoy si — sorpresa)</p>'
             '<p><b>Esta muy alto el nino.</b> (ha crecido mucho — cambio)</p>'
             '<p><b>Esta muy simpatico tu jefe hoy.</b> (normalmente no tanto — contraste)</p>'
             '<p><b>Estas muy delgada.</b> (has adelgazado — cambio perceptible)</p>'
             '</div>'
             '<p class="slide-explanation">Con <b>ser</b> se expresaria una cualidad neutra y permanente: '
             '<i>Es guapa</i> (una cualidad objetiva). Con <b>estar</b> se anade el matiz de '
             'percepcion subjetiva, cambio o contraste.</p>'),

            ('Ubicacion de eventos: SER vs. ESTAR', None,
             '<p class="slide-explanation">La ubicacion de <b>eventos</b> usa <b>ser</b> (no estar), '
             'porque la localizacion del evento forma parte de su identidad. '
             'La ubicacion de <b>personas y objetos</b> usa siempre <b>estar</b>:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">SER (eventos)</th>'
             '<th style="padding:8px;text-align:left">ESTAR (personas/objetos)</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">El concierto <b>es</b> en el Palacio de Deportes.</td>'
             '<td style="padding:8px">Los musicos <b>estan</b> en el Palacio de Deportes.</td></tr>'
             '<tr><td style="padding:8px">La boda <b>sera</b> en la iglesia.</td>'
             '<td style="padding:8px">Los novios <b>estan</b> en la iglesia.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">La reunion <b>es</b> en la sala B.</td>'
             '<td style="padding:8px">El director <b>esta</b> en la sala B.</td></tr>'
             '</table>'
             '<p class="slide-explanation">Regla: si se puede sustituir por «tiene lugar» o «se celebra», se usa <b>ser</b>.</p>'),

            ('SER con adjetivos: cualidad permanente y edad', None,
             '<p class="slide-explanation">A veces <b>ser</b> se usa con adjetivos que parecen expresar estados '
             'para indicar que la cualidad es inherente al sujeto o se considera permanente '
             'en un contexto dado:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Es joven</b> (todavia) = la juventud es su condicion actual. Contraste: <i>Esta muy joven para su edad</i> (sorpresa).</p>'
             '<p><b>Es alto / es bajo</b> = descripcion objetiva de estatura. Contraste: <i>Que alto esta</i> (ha crecido).</p>'
             '<p><b>El cielo es azul</b> = cualidad inherente. <i>El cielo esta muy azul hoy</i> = estado especialmente llamativo hoy.</p>'
             '</div>'
             '<p class="slide-explanation">La diferencia entre ser y estar con muchos adjetivos '
             'no es blanco o negro: depende de si el hablante presenta la cualidad como inherente (ser) '
             'o como estado percibido en un momento concreto (estar).</p>'),
        ],
        traps=[
            ('Esta listo = es inteligente', '<strong>Es listo</strong> = es inteligente; <strong>esta listo</strong> = esta preparado',
             'El adjetivo <b>listo</b> cambia de significado: <i>es listo</i> (inteligente, cualidad permanente) '
             'vs. <i>esta listo</i> (preparado para hacer algo).'),
            ('El concierto esta en el teatro', 'El concierto <strong>es</strong> en el teatro',
             'Los eventos se localizan con <b>ser</b>: el concierto <b>es</b> en el teatro. '
             '<b>Estar</b> se reserva para la ubicacion de personas y objetos.'),
            ('Esta malo = es malvado', '<strong>Es malo</strong> = es malvado; <strong>esta malo</strong> = esta enfermo',
             '<b>Es malo</b> describe el caracter o la calidad (malvado, de mala calidad). '
             '<b>Esta malo</b> describe un estado temporal de enfermedad.'),
            ('Es rico el pastel = sabe bien', 'El pastel <strong>esta</strong> rico',
             'El sabor agradable de una comida o bebida se expresa con <b>estar</b>: el pastel <b>esta</b> rico. '
             '<b>Ser</b> rico se refiere a la riqueza economica o a la abundancia.'),
            ('Que guapa es hoy (expresando sorpresa)', 'Que guapa <strong>esta</strong> hoy',
             'Para expresar sorpresa o un cambio notable respecto a lo habitual, se usa <b>estar</b>: '
             '<i>que guapa <b>esta</b> hoy</i>. <b>Ser</b> expresa la cualidad de forma neutra y permanente.'),
        ],
        summary=[
            ('ser (identidad/permanente)', 'ser + adj. = cualidad inherente o permanente', 'Es inteligente. Es espanol. Es medico.'),
            ('estar (estado/condicion)', 'estar + adj. = estado o condicion temporal', 'Esta cansado. Esta enfermo. Esta listo (= preparado).'),
            ('Adjetivos que cambian', 'listo/malo/rico/seguro/vivo/aburrido', 'Es rico (dinero) vs. esta rico (sabor).'),
            ('Sorpresa/cambio con estar', 'estar + adj. normalmente de ser = cambio notable', 'Que alta esta la nina — cuanto ha crecido.'),
            ('Ubicacion de eventos', 'evento + ser (no estar) + lugar', 'La boda es en la catedral.'),
            ('Ubicacion de cosas/personas', 'objeto/persona + estar + lugar', 'El libro esta en la mesa.'),
        ],
        ex1=dict(
            title='SER o ESTAR: elige la forma correcta',
            questions=[
                ('La pelicula ______ muy aburrida. (es una pelicula sin interes)', ['esta', 'es', 'era', 'fue'], 1,
                 'Cualidad inherente de la pelicula → <b>es</b> aburrida (califica la pelicula en si, no el estado del espectador).'),
                ('El nino ______ muy listo; siempre saca las mejores notas.', ['esta', 'es', 'estuvo', 'fue'], 1,
                 'Cualidad intelectual permanente → <b>es</b> listo (= es inteligente).'),
                ('¿Ya ______ lista la cena? Tengo mucha hambre.', ['es', 'esta', 'fue', 'sera'], 1,
                 'Estado de preparacion → <b>esta</b> lista (= preparada, puede comerse ya).'),
                ('Este pastel ______ buenísimo; ¿puedo repetir?', ['es', 'fue', 'esta', 'sera'], 2,
                 'Sabor delicioso → <b>esta</b> buenísimo (el gusto es un estado percibido, no una cualidad permanente).'),
                ('El festival de jazz ______ en la Plaza Mayor este sabado.', ['esta', 'estara', 'es', 'sera'], 3,
                 'Ubicacion de un evento → <b>sera</b> (ser para eventos): el festival <b>sera</b> en la Plaza Mayor.'),
                ('Que elegante ______ tu hoy, ¿vas a alguna fiesta?', ['eres', 'seras', 'estas', 'fuiste'], 2,
                 'Sorpresa o cambio notable respecto a lo habitual → <b>estas</b>: que elegante <b>estas</b> hoy.'),
            ]
        ),
        ex2=dict(
            title='Explica la diferencia de significado',
            questions=[
                ('¿Que significa «El guarda de seguridad es muy vivo»?',
                 'es vivo = es astuto o listo', ['es vivo = es astuto', 'es astuto', 'es listo', 'es vivo significa que es astuto o rapido de mente'],
                 '<b>Ser vivo</b> = ser astuto, listo, avispado. <b>Estar vivo</b> = tener vida, no haber muerto.'),
                ('Transforma: «Ese hombre es malo» (malvado) al sentido de «esta enfermo».',
                 'esta malo', ['esta malo'],
                 '<b>Esta malo</b> = esta enfermo. <b>Es malo</b> = es malvado o de mala calidad.'),
                ('¿Que frase ubica correctamente el evento? El partido ______ en el estadio.',
                 'es', ['es', 'sera'],
                 'Evento + lugar → <b>ser</b>: el partido <b>es</b> (o <b>sera</b>) en el estadio, no «esta».'),
                ('¿Como se dice que algo sabe delicioso con ser/estar?',
                 'esta rico', ['esta rico', 'esta bueno', 'esta delicioso'],
                 'El sabor agradable se expresa siempre con <b>estar</b>: <b>esta rico</b>, <b>esta bueno</b>.'),
                ('¿Que significa «Estas muy segura de eso»?',
                 'tiene certeza o confianza', ['tiene certeza', 'esta convencida', 'tiene seguridad', 'esta convencida o tiene certeza'],
                 '<b>Estar seguro/a</b> = tener certeza o sentirse convencido. <b>Ser seguro</b> = no entrañar peligro (lugar u objeto).'),
            ]
        ),
        ex3=dict(
            title='Elige el significado correcto de ser/estar + adjetivo',
            questions=[
                ('¿Que significa «Mi jefe esta muy aburrido hoy»?',
                 ['Mi jefe causa aburrimiento.', 'Mi jefe siente aburrimiento.', 'Mi jefe es una persona aburrida.', 'Mi jefe ha muerto de aburrimiento.'],
                 1,
                 '<b>Estar aburrido</b> = sentir aburrimiento. <b>Ser aburrido</b> = ser una persona o cosa que causa aburrimiento.'),
                ('¿Cual usa ser/estar correctamente para ubicar personas y eventos?',
                 ['El museo esta cerrado y la exposicion esta en el museo.',
                  'El museo esta cerrado y la exposicion es en el museo.',
                  'El museo es cerrado y la exposicion es en el museo.',
                  'El museo es cerrado y la exposicion esta en el museo.'],
                 1,
                 'Estado del lugar → <b>esta</b> cerrado. Ubicacion del evento → <b>es</b> en el museo.'),
                ('¿Que comunica «Que alto estas» en vez de «Que alto eres»?',
                 ['Que la persona es siempre muy alta.',
                  'Que la persona ha crecido o el hablante nota un cambio.',
                  'Que la persona es de origen alto.',
                  'No hay diferencia entre las dos frases.'],
                 1,
                 '<b>Estar</b> + adj. de cualidad comunica sorpresa o cambio perceptible. <b>Ser</b> + adj. expresa la cualidad de forma neutra y permanente.'),
                ('¿Cual es la diferencia entre «es seguro» y «esta seguro»?',
                 ['"Es seguro" describe un estado; "esta seguro" es una cualidad permanente.',
                  '"Es seguro" describe un lugar sin peligro; "esta seguro" expresa certeza o confianza.',
                  'No hay diferencia.',
                  '"Es seguro" se usa solo con personas; "esta seguro" solo con cosas.'],
                 1,
                 '<b>Es seguro</b> = no hay peligro (calidad del lugar u objeto). <b>Esta seguro</b> = tiene certeza o se siente convencido.'),
                ('¿Cual describe el sabor de una comida correctamente?',
                 ['La paella es muy rica.', 'La paella esta muy rica.', 'La paella fue muy rica.', 'La paella sera muy rica.'],
                 1,
                 'El sabor de la comida se expresa con <b>estar</b>: la paella <b>esta</b> muy rica. '
                 '<b>Ser</b> rico hace referencia a la riqueza economica.'),
            ]
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            dict(term='es listo', definition='SER + listo = es inteligente (cualidad permanente)',
                 example='Juan <b>es listo</b>; siempre encuentra la mejor solucion.', accept=['es listo']),
            dict(term='esta listo', definition='ESTAR + listo = esta preparado (estado temporal)',
                 example='La cena <b>esta lista</b>; podemos sentarnos a la mesa.', accept=['esta listo', 'esta lista']),
            dict(term='es malo', definition='SER + malo = es malvado o de mala calidad',
                 example='El villano de la pelicula <b>es muy malo</b>.', accept=['es malo']),
            dict(term='esta malo', definition='ESTAR + malo = esta enfermo (estado temporal)',
                 example='No puede ir al trabajo hoy porque <b>esta malo</b>.', accept=['esta malo']),
            dict(term='esta rico', definition='ESTAR + rico = tiene buen sabor (estado percibido)',
                 example='Prueba el guiso; <b>esta riquísimo</b>.', accept=['esta rico', 'esta riquísimo']),
            dict(term='es rico', definition='SER + rico = tiene mucho dinero (cualidad permanente)',
                 example='Su familia <b>es muy rica</b> y tiene varios negocios.', accept=['es rico']),
            dict(term='es en', definition='SER + lugar = ubicacion de un evento (el evento tiene lugar en)',
                 example='La conferencia <b>es en</b> el auditorio principal.', accept=['es en', 'sera en']),
            dict(term='esta aburrido', definition='ESTAR + aburrido = siente aburrimiento (estado de la persona)',
                 example='Los ninos <b>estan aburridos</b> porque no hay nada que hacer.', accept=['esta aburrido', 'estan aburridos']),
        ],
    ),

    'modo-subjuntivo-expresiones': dict(
        level='b2',
        section='grammar',
        num='G04',
        short='Subjuntivo: valoracion y emocion',
        title='El Subjuntivo con Expresiones de Valoracion y Emocion',
        subtitle='Aprende que expresiones impersonales exigen subjuntivo y cuales no',
        slides=[
            ('Expresiones de valoracion que exigen subjuntivo', None,
             '<p class="slide-explanation">Las expresiones impersonales de <b>valoracion</b> '
             '(importancia, necesidad, conveniencia, juicio de valor) siempre van seguidas de <b>que + subjuntivo</b>:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Expresion</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>es importante que</b></td>'
             '<td style="padding:8px">Es importante que <b>practiques</b> cada dia.</td></tr>'
             '<tr><td style="padding:8px"><b>es necesario que</b></td>'
             '<td style="padding:8px">Es necesario que todos <b>firmen</b> el documento.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>es util que</b></td>'
             '<td style="padding:8px">Es util que <b>sepas</b> otro idioma.</td></tr>'
             '<tr><td style="padding:8px"><b>es bueno/malo que</b></td>'
             '<td style="padding:8px">Es malo que <b>duermas</b> tan poco.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>es una lastima que</b></td>'
             '<td style="padding:8px">Es una lastima que no <b>puedas</b> venir.</td></tr>'
             '<tr><td style="padding:8px"><b>es logico/normal que</b></td>'
             '<td style="padding:8px">Es normal que <b>estés</b> cansado.</td></tr>'
             '</table>'),

            ('Expresiones de incertidumbre o probabilidad → subjuntivo', None,
             '<p class="slide-explanation">Las expresiones que expresan <b>posibilidad, probabilidad, duda '
             'o rareza</b> exigen subjuntivo porque no afirman la realidad de la proposicion:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Expresion</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>es posible que</b></td>'
             '<td style="padding:8px">Es posible que <b>lleguen</b> tarde.</td></tr>'
             '<tr><td style="padding:8px"><b>es probable que</b></td>'
             '<td style="padding:8px">Es probable que <b>haya</b> retrasos.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>es imposible que</b></td>'
             '<td style="padding:8px">Es imposible que eso <b>sea</b> cierto.</td></tr>'
             '<tr><td style="padding:8px"><b>es dudoso que</b></td>'
             '<td style="padding:8px">Es dudoso que <b>aprueben</b> el proyecto.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>es raro que</b></td>'
             '<td style="padding:8px">Es raro que no <b>haya</b> contestado.</td></tr>'
             '</table>'),

            ('Expresiones de certeza → indicativo', None,
             '<p class="slide-explanation">Las expresiones que presentan algo como un <b>hecho cierto</b> '
             'o evidencia van seguidas de <b>indicativo</b>, no de subjuntivo:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Expresion (certeza → indicativo)</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>es cierto que</b></td>'
             '<td style="padding:8px">Es cierto que <b>existe</b> el problema.</td></tr>'
             '<tr><td style="padding:8px"><b>es verdad que</b></td>'
             '<td style="padding:8px">Es verdad que <b>ha llovido</b> mucho.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>es evidente que</b></td>'
             '<td style="padding:8px">Es evidente que <b>tienen</b> razon.</td></tr>'
             '<tr><td style="padding:8px"><b>es obvio que</b></td>'
             '<td style="padding:8px">Es obvio que <b>sabe</b> mucho.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>es claro que</b></td>'
             '<td style="padding:8px">Es claro que <b>necesitan</b> apoyo.</td></tr>'
             '</table>'
             '<p class="slide-explanation">Pero: cuando estas expresiones se niegan, '
             'pasan a expresar duda → subjuntivo: <i>No es cierto que <b>exista</b> ese problema.</i></p>'),

            ('Expresiones emocionales → subjuntivo', None,
             '<p class="slide-explanation">Los verbos y expresiones de <b>emocion</b> exigen subjuntivo '
             'cuando hay cambio de sujeto. El hablante valora emocionalmente la accion de otra persona:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Expresion</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>me alegra que</b></td>'
             '<td style="padding:8px">Me alegra que <b>estes</b> mejor.</td></tr>'
             '<tr><td style="padding:8px"><b>me sorprende que</b></td>'
             '<td style="padding:8px">Me sorprende que no <b>lo sepas</b>.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>me preocupa que</b></td>'
             '<td style="padding:8px">Me preocupa que no <b>coman</b> bien.</td></tr>'
             '<tr><td style="padding:8px"><b>me molesta que</b></td>'
             '<td style="padding:8px">Me molesta que <b>lleguen</b> tarde siempre.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>me gusta que</b></td>'
             '<td style="padding:8px">Me gusta que <b>seas</b> tan amable.</td></tr>'
             '</table>'),

            ('La negacion transforma indicativo en subjuntivo', None,
             '<p class="slide-explanation">Esta regla es fundamental a nivel B2: negar una expresion de '
             '<b>certeza</b> la convierte en expresion de <b>duda</b>, cambiando el modo:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Afirmacion (certeza → indicativo)</th>'
             '<th style="padding:8px;text-align:left">Negacion (duda → subjuntivo)</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Es cierto que <b>viene</b>.</td>'
             '<td style="padding:8px">No es cierto que <b>venga</b>.</td></tr>'
             '<tr><td style="padding:8px">Es verdad que <b>ha pasado</b>.</td>'
             '<td style="padding:8px">No es verdad que <b>haya pasado</b>.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Es evidente que <b>saben</b> la respuesta.</td>'
             '<td style="padding:8px">No es evidente que <b>sepan</b> la respuesta.</td></tr>'
             '</table>'
             '<p class="slide-explanation">Comparar tambien: <i>Creo que <b>viene</b></i> (afirmacion → indicativo) vs. '
             '<i>No creo que <b>venga</b></i> (negacion → subjuntivo).</p>'),
        ],
        traps=[
            ('Es posible que viene', 'Es posible que <strong>venga</strong>',
             '<i>Es posible que</i> expresa probabilidad, no certeza → exige subjuntivo: <b>venga</b>, no indicativo.'),
            ('Es cierto que haya un problema', 'Es cierto que <strong>hay</strong> un problema',
             '<i>Es cierto que</i> presenta un hecho como verdad → indicativo: <b>hay</b>. '
             'El subjuntivo solo aparece cuando se niega: «No es cierto que haya…»'),
            ('Me alegra que estas bien', 'Me alegra que <strong>estes</strong> bien',
             'Los verbos de emocion con cambio de sujeto exigen siempre subjuntivo: <b>estes</b>, no indicativo.'),
            ('Es dudoso que viene', 'Es dudoso que <strong>venga</strong>',
             '<i>Es dudoso que</i> expresa duda, no certeza → subjuntivo: <b>venga</b>.'),
            ('No es verdad que tienen → tienen con indicativo', 'No es verdad que <strong>tengan</strong>',
             'Al negar una expresion de certeza, el modo cambia a subjuntivo: '
             'no es verdad que <b>tengan</b> (no «tienen»).'),
        ],
        summary=[
            ('Valoracion → subjuntivo', 'es importante/necesario/bueno/malo + que + subj.', 'Es importante que llegues a tiempo.'),
            ('Probabilidad/duda → subjuntivo', 'es posible/probable/dudoso/raro + que + subj.', 'Es posible que llueva manana.'),
            ('Certeza → indicativo', 'es cierto/verdad/evidente/obvio/claro + que + indic.', 'Es evidente que tiene razon.'),
            ('Negacion de certeza → subjuntivo', 'no es cierto/verdad/evidente + que + subj.', 'No es cierto que venga hoy.'),
            ('Emocion → subjuntivo', 'me alegra/sorprende/preocupa/molesta/gusta + que + subj.', 'Me alegra que estes mejor.'),
            ('Creer: afirm. → indic., neg. → subj.', 'creo que + indic. / no creo que + subj.', 'No creo que sea tan facil.'),
        ],
        ex1=dict(
            title='¿Indicativo o subjuntivo? Elige la forma correcta',
            questions=[
                ('Es importante que vosotros ______ (leer) las instrucciones.', ['leis', 'leais', 'leereis', 'leais'], 1,
                 '<i>Es importante que</i> = valoracion → subjuntivo: vosotros de LEER → <b>leais</b>.'),
                ('Es cierto que el cambio climatico ______ (afectar) a todo el planeta.', ['afecte', 'afecta', 'afectara', 'afectaria'], 1,
                 '<i>Es cierto que</i> = certeza → indicativo presente: <b>afecta</b>.'),
                ('Me preocupa que los ninos no ______ (dormir) lo suficiente.', ['duermen', 'durmieran', 'duerman', 'dormiran'], 2,
                 'Expresion de emocion con cambio de sujeto → subjuntivo: DORMIR → <b>duerman</b>.'),
                ('Es probable que el tren ______ (llegar) con retraso.', ['llega', 'llegara', 'llegue', 'llegaria'], 2,
                 '<i>Es probable que</i> = probabilidad → subjuntivo: <b>llegue</b>.'),
                ('No es verdad que ella ______ (mentir) en esa declaracion.', ['miente', 'mintio', 'mienta', 'mentira'], 2,
                 'Negacion de certeza → subjuntivo: MENTIR → <b>mienta</b>.'),
                ('Es evidente que el equipo ______ (necesitar) apoyo.', ['necesite', 'necesita', 'necesitara', 'necesitaria'], 1,
                 '<i>Es evidente que</i> = certeza → indicativo: <b>necesita</b>.'),
            ]
        ),
        ex2=dict(
            title='Completa con indicativo o subjuntivo',
            questions=[
                ('Es una lastima que no ______ (poder, tu) asistir a la ceremonia.',
                 'puedas', ['puedas'],
                 'Valoracion (lastima) → subjuntivo: PODER, tu → <b>puedas</b>.'),
                ('Es obvio que ellos ______ (tener) mucha experiencia en este campo.',
                 'tienen', ['tienen'],
                 '<i>Es obvio que</i> = certeza → indicativo: <b>tienen</b>.'),
                ('Me sorprende que tu jefe ______ (tomar) esa decision sin consultar.',
                 'haya tomado', ['haya tomado', 'tome'],
                 'Emocion + accion anterior al presente → subj. perfecto: <b>haya tomado</b>. Subj. pres. <b>tome</b> tambien es posible.'),
                ('Es raro que nadie ______ (saber) donde esta el director.',
                 'sepa', ['sepa'],
                 '<i>Es raro que</i> = rareza/duda → subjuntivo: SABER → <b>sepa</b>.'),
                ('Es verdad que muchas personas ______ (sufrir) las consecuencias de la crisis.',
                 'sufren', ['sufren'],
                 '<i>Es verdad que</i> = certeza → indicativo: <b>sufren</b>.'),
            ]
        ),
        ex3=dict(
            title='Identifica la expresion correcta',
            questions=[
                ('¿Cual usa subjuntivo correctamente tras una expresion de valoracion?',
                 ['Es importante que llega a tiempo.',
                  'Es importante que llegue a tiempo.',
                  'Es importante que llegara a tiempo.',
                  'Es importante que llegaria a tiempo.'],
                 1,
                 '<i>Es importante que</i> → subjuntivo presente: <b>llegue</b>.'),
                ('¿Cual usa indicativo correctamente tras una expresion de certeza?',
                 ['Es evidente que tenga razon.',
                  'Es evidente que hubiera tenido razon.',
                  'Es evidente que tiene razon.',
                  'Es evidente que tuviera razon.'],
                 2,
                 '<i>Es evidente que</i> = certeza → indicativo: <b>tiene</b> razon.'),
                ('¿Que ocurre cuando se niega «es cierto que»?',
                 ['Sigue usando indicativo.',
                  'Usa condicional.',
                  'Usa subjuntivo.',
                  'Usa infinitivo.'],
                 2,
                 'Al negar una expresion de certeza, el modo cambia a <b>subjuntivo</b>: '
                 'no es cierto que <b>venga</b>.'),
                ('¿Cual expresa emocion correctamente con subjuntivo?',
                 ['Me alegra que estas aqui.',
                  'Me alegra que estes aqui.',
                  'Me alegra que estuvieras aqui.',
                  'Me alegra que habias venido.'],
                 1,
                 'Emocion + cambio de sujeto → subjuntivo presente: <b>estes</b>.'),
                ('¿Con que expresion es correcto el indicativo?',
                 ['Es probable que hay trafico.', 'Es posible que hay trafico.', 'Es claro que hay trafico.', 'Es dudoso que hay trafico.'],
                 2,
                 'Solo <i>es claro que</i> es una expresion de certeza → indicativo: <b>hay</b>. '
                 'Las demas expresan probabilidad o duda → subjuntivo habrá.'),
            ]
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            dict(term='es importante que + subj.', definition='expresion de valoracion: siempre seguida de subjuntivo',
                 example='Es importante que todos <b>participen</b> en la reunion.', accept=['es importante que']),
            dict(term='es posible que + subj.', definition='expresion de probabilidad: siempre seguida de subjuntivo',
                 example='Es posible que <b>llueva</b> esta tarde.', accept=['es posible que']),
            dict(term='es cierto que + indic.', definition='expresion de certeza: seguida de indicativo (no subjuntivo)',
                 example='Es cierto que el proyecto <b>tiene</b> problemas.', accept=['es cierto que']),
            dict(term='no es verdad que + subj.', definition='negacion de certeza: cambia a subjuntivo',
                 example='No es verdad que ella <b>haya</b> dicho eso.', accept=['no es verdad que']),
            dict(term='me preocupa que + subj.', definition='expresion de emocion: seguida de subjuntivo con cambio de sujeto',
                 example='Me preocupa que los alumnos no <b>comprendan</b> la explicacion.', accept=['me preocupa que']),
            dict(term='es evidente que + indic.', definition='expresion de evidencia/certeza: seguida de indicativo',
                 example='Es evidente que el equipo <b>necesita</b> refuerzos.', accept=['es evidente que']),
            dict(term='es una lastima que + subj.', definition='expresion de valoracion negativa: siempre seguida de subjuntivo',
                 example='Es una lastima que no <b>puedas</b> quedarte mas tiempo.', accept=['es una lastima que']),
            dict(term='me sorprende que + subj.', definition='emocion de sorpresa: seguida de subjuntivo con cambio de sujeto',
                 example='Me sorprende que no <b>lo sepas</b> todavia.', accept=['me sorprende que']),
        ],
    ),

    'indefinido-imperfecto-perfecto': dict(
        level='b2',
        section='grammar',
        num='G05',
        short='Contraste de los tres pasados',
        title='Contraste de los Tres Pasados: Indefinido, Imperfecto y Perfecto',
        subtitle='Usa con precision los tres tiempos del pasado en espanol',
        slides=[
            ('El preterito indefinido: accion puntual y completada', None,
             '<p class="slide-explanation">El <b>preterito indefinido</b> (tambien llamado preterito perfecto simple) '
             'expresa acciones <b>puntuales, completas</b> en el pasado, con una referencia temporal '
             'especifica o percibida como cerrada:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Ayer</b> fui al medico. / Nos conocimos <b>en 2015</b>.</p>'
             '<p>El lunes <b>pasado</b> entregue el informe.</p>'
             '<p>Colon <b>llego</b> a America en 1492. (hecho historico completado)</p>'
             '</div>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Marcadores tipicos del indefinido</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">ayer, anteayer, el lunes pasado, la semana pasada, '
             'el ano pasado, hace dos anos, en 1998, entonces, aquel dia, de repente, en ese momento</td></tr>'
             '</table>'),

            ('El preterito imperfecto: fondo, habito y descripcion', None,
             '<p class="slide-explanation">El <b>imperfecto</b> describe <b>estados pasados</b>, '
             '<b>acciones habituales</b> en el pasado y el <b>fondo o escenario</b> de una narracion. '
             'No indica cuando empezo ni cuando termino la situacion:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Estado/descripcion:</b> Cuando era nino, <b>vivia</b> en el campo. El cielo <b>estaba</b> despejado.</p>'
             '<p><b>Habito:</b> Todos los dias <b>tomaba</b> el autobus. <b>Ibamos</b> al parque cada semana.</p>'
             '<p><b>Accion en curso interrumpida:</b> <b>Dormia</b> cuando sono el telefono.</p>'
             '</div>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Marcadores tipicos del imperfecto</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">siempre, normalmente, generalmente, '
             'todos los dias, cada semana, de nino, cuando era pequeno, en aquella epoca, a menudo, antes, '
             'en ese momento (estado en curso)</td></tr>'
             '</table>'),

            ('El preterito perfecto: pasado vinculado al presente', None,
             '<p class="slide-explanation">El <b>preterito perfecto</b> (he/has/ha... + participio) relaciona '
             'el pasado con el <b>presente del hablante</b>. Se usa para acciones pasadas que tienen '
             'relevancia en el momento actual o que ocurren dentro de un periodo de tiempo que el hablante '
             'considera no terminado:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Hoy</b> he comido ensalada. / <b>Esta semana</b> han aprobado la ley.</p>'
             '<p><b>Ya</b> he terminado el proyecto. (resultado relevante ahora)</p>'
             '<p><b>Nunca</b> he visitado Tokyo. / <b>Alguna vez</b> has comido sushi?</p>'
             '</div>'
             '<p class="slide-explanation"><b>Variacion regional importante:</b> En gran parte de Latinoamerica '
             'y en algunas zonas de Espana, el indefinido reemplaza al perfecto incluso con marcadores '
             'de presente: <i>hoy fui al medico</i> (L.Am.) vs. <i>hoy he ido al medico</i> (Espana peninsular).</p>'),

            ('Indefinido e imperfecto en la narracion', None,
             '<p class="slide-explanation">La distincion mas importante a nivel B2 es el uso narrativo: '
             '<b>indefinido</b> para los eventos que hacen avanzar la trama, '
             '<b>imperfecto</b> para el escenario y las circunstancias de fondo:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Era</b> una noche de invierno. <b>Nevaba</b> y <b>hacia</b> mucho frio. '
             '(imperfecto: escenario)</p>'
             '<p>De repente, <b>sono</b> el telefono. <b>Me levante</b> y lo <b>cogi</b>. '
             '(indefinido: eventos de la trama)</p>'
             '<p>Era la voz de mi hermana. Me <b>dijo</b> que <b>necesitaba</b> ayuda. '
             '(indefinido: evento; imperfecto: estado/explicacion)</p>'
             '</div>'
             '<p class="slide-explanation">Analogia: el imperfecto es el <b>fondo de un cuadro</b>; '
             'el indefinido es la <b>figura principal</b> que se mueve sobre ese fondo.</p>'),

            ('Contraste sistematico de los tres pasados', None,
             '<p class="slide-explanation">Resumen comparativo de los tres pasados en los contextos mas frecuentes:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Aspecto</th>'
             '<th style="padding:8px;text-align:left">Indefinido</th>'
             '<th style="padding:8px;text-align:left">Imperfecto</th>'
             '<th style="padding:8px;text-align:left">Perfecto</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Tipo de accion</b></td>'
             '<td style="padding:8px">Puntual, completa</td>'
             '<td style="padding:8px">Durativa, habitual, en curso</td>'
             '<td style="padding:8px">Vinculada al presente</td></tr>'
             '<tr><td style="padding:8px"><b>Marcadores</b></td>'
             '<td style="padding:8px">ayer, hace X, el lunes pasado</td>'
             '<td style="padding:8px">siempre, cuando era, de nino</td>'
             '<td style="padding:8px">hoy, ya, esta semana, nunca</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>En narracion</b></td>'
             '<td style="padding:8px">Evento principal (figura)</td>'
             '<td style="padding:8px">Escenario (fondo)</td>'
             '<td style="padding:8px">Resultado relevante ahora</td></tr>'
             '<tr><td style="padding:8px"><b>Ejemplo</b></td>'
             '<td style="padding:8px">Ayer <b>fui</b> al cine.</td>'
             '<td style="padding:8px">De nino <b>iba</b> al cine cada semana.</td>'
             '<td style="padding:8px">Hoy <b>he ido</b> al cine.</td></tr>'
             '</table>'),
        ],
        traps=[
            ('Ayer he ido al medico (en Espana peninsular)', 'Ayer <strong>fui</strong> al medico',
             '<b>Ayer</b> indica tiempo cerrado y desvinculado del presente → indefinido: <b>fui</b>. '
             'El perfecto «he ido» se usa con marcadores de tiempo abierto (hoy, esta semana, ya).'),
            ('Cuando era nino, fui al colegio todos los dias', 'Cuando era nino, <strong>iba</strong> al colegio todos los dias',
             'La referencia a un habito pasado (todos los dias, de nino) pide imperfecto: <b>iba</b>. '
             'El indefinido «fui» expresaria una accion puntual, no un habito.'),
            ('Ya termino el trabajo = todavia en el pasado', '<strong>Ya he terminado</strong> el trabajo (resultado relevante ahora)',
             'Para expresar que una accion pasada tiene resultado relevante en el presente, se usa el perfecto: '
             '<b>ya he terminado</b>. El indefinido «ya termine» enfatizaria el momento de finalizacion, no el resultado presente.'),
            ('Dormia cuando sonaba el telefono', 'Dormia cuando <strong>sono</strong> el telefono',
             'La accion que interrumpe va en indefinido (evento puntual): <b>sono</b>. '
             'La accion en curso en ese momento va en imperfecto: dormia.'),
            ('Esta semana fue muy productiva (en Espana peninsular)', 'Esta semana <strong>ha sido</strong> muy productiva',
             '<b>Esta semana</b> es un periodo que el hablante considera aun activo o conectado al presente → perfecto: '
             '<b>ha sido</b>. El indefinido «fue» se usaria cuando el periodo se percibe cerrado.'),
        ],
        summary=[
            ('Indefinido: accion puntual y completa', 'ayer/el lunes pasado/hace X → indefinido', 'Ayer llegue tarde a la oficina.'),
            ('Imperfecto: estado, habito, fondo', 'siempre/de nino/cuando era → imperfecto', 'De nino vivia en el campo.'),
            ('Perfecto: pasado vinculado al presente', 'hoy/ya/esta semana/nunca → perfecto', 'Esta semana he trabajado mucho.'),
            ('Narracion: indefinido = figura', 'eventos que avanzan la trama → indefinido', 'De repente sono el telefono y me levante.'),
            ('Narracion: imperfecto = fondo', 'escenario y circunstancias → imperfecto', 'Llovía y hacia mucho frio.'),
            ('Indefinido interrumpe al imperfecto', 'imperf. (en curso) + indef. (interrupcion)', 'Dormia cuando llego mi hermano.'),
            ('Variacion regional', 'L.Am.: indef. por perfecto con hoy/ya; Espana: perfecto', 'Hoy fui (L.Am.) / hoy he ido (Esp.).'),
        ],
        ex1=dict(
            title='Elige el tiempo de pasado correcto',
            questions=[
                ('______ (nacer, yo) en 1990 y ______ (crecer) en Sevilla.', ['He nacido / he crecido', 'Naci / creci', 'Nacia / crecia', 'Naci / crecia'], 1,
                 'Eventos puntuales con referencia temporal cerrada (1990, ciudad) → <b>indefinido</b>: naci / creci.'),
                ('De nino ______ (ir) al parque todos los sabados con mi padre.', ['fui', 'iba', 'he ido', 'habia ido'], 1,
                 'Habito en el pasado (todos los sabados, de nino) → <b>imperfecto</b>: <b>iba</b>.'),
                ('Esta semana ______ (tener) tres reuniones importantisimas.', ['tuve', 'tenia', 'he tenido', 'habia tenido'], 2,
                 'Periodo de tiempo vinculado al presente (esta semana) → <b>perfecto</b>: <b>he tenido</b>.'),
                ('______ (dormir) profundamente cuando de repente ______ (sonar) la alarma.', ['Dormi / sono', 'Dormia / sono', 'Dormia / sonaba', 'Dormi / sonaba'], 1,
                 'Accion en curso (fondo) → imperfecto: <b>dormia</b>. Interrupcion puntual → indefinido: <b>sono</b>.'),
                ('Nunca ______ (probar) el durian; dicen que tiene un olor muy fuerte.', ['probe', 'probaba', 'he probado', 'habia probado'], 2,
                 '<i>Nunca</i> en relacion con el presente del hablante → <b>perfecto</b>: <b>he probado</b>.'),
                ('El ano pasado ______ (publicar, ellos) su primera novela.', ['han publicado', 'publicaban', 'publicaron', 'habian publicado'], 2,
                 '<i>El ano pasado</i> = periodo cerrado → <b>indefinido</b>: <b>publicaron</b>.'),
            ]
        ),
        ex2=dict(
            title='Completa con el tiempo de pasado adecuado',
            questions=[
                ('Cuando ______ (ser) pequena, mi abuela me ______ (contar) cuentos cada noche.',
                 'era / contaba', ['era / contaba', 'era/contaba'],
                 'Estado pasado (era pequena) + habito pasado (cada noche) → ambos en <b>imperfecto</b>: era / contaba.'),
                ('El lunes pasado ______ (ir, yo) a la conferencia y ______ (conocer) a mucha gente interesante.',
                 'fui / conoci', ['fui / conoci', 'fui/conoci'],
                 'Acciones puntuales con referencia temporal cerrada → <b>indefinido</b>: fui / conoci.'),
                ('¿Ya ______ (hablar, tu) con el director sobre el presupuesto?',
                 'has hablado', ['has hablado'],
                 '<i>Ya</i> con pregunta sobre resultado actual → <b>perfecto</b>: <b>has hablado</b>.'),
                ('______ (hacer) mucho calor aquella tarde y todo el mundo ______ (buscar) sombra.',
                 'hacia / buscaba', ['hacia / buscaba', 'hacia/buscaba'],
                 'Descripcion de las circunstancias (fondo) → <b>imperfecto</b>: hacia / buscaba.'),
                ('De repente ______ (aparecer) un ciervo en medio de la carretera y el conductor ______ (frenar) bruscamente.',
                 'aparecio / freno', ['aparecio / freno', 'apareció / frenó'],
                 'Eventos puntuales que avanzan la narracion → <b>indefinido</b>: aparecio / freno.'),
            ]
        ),
        ex3=dict(
            title='Identifica el tiempo correcto en contexto',
            questions=[
                ('¿Cual describe correctamente un habito pasado?',
                 ['El ano pasado corri todos los dias.',
                  'Cuando estaba en la universidad, corria todos los dias.',
                  'Hoy he corrido por el parque.',
                  'Ayer corri diez kilometros.'],
                 1,
                 'Habito en el pasado con marcador de contexto (<i>cuando estaba en la universidad</i>) → <b>imperfecto</b>: corria.'),
                ('¿Cual usa el perfecto correctamente?',
                 ['Ayer he comido en ese restaurante.',
                  'En 2019 he viajado a Japon.',
                  'Esta manana he recibido una noticia increible.',
                  'El mes pasado he empezado un nuevo trabajo.'],
                 2,
                 '<i>Esta manana</i> es un periodo aun vinculado al presente (en espanol peninsular) → <b>perfecto</b>: he recibido.'),
                ('¿Cual describe correctamente el fondo de una narracion?',
                 ['De repente entro un hombre en la cafeteria.',
                  'Pedi un cafe y me sente en la terraza.',
                  'En la cafeteria habia mucha gente y sonaba musica suave.',
                  'El camarero me cobro diez euros.'],
                 2,
                 'Descripcion del escenario (fondo) → <b>imperfecto</b>: habia / sonaba. Los demas son eventos puntuales (indefinido).'),
                ('¿Que comunica «Dormia cuando llego Juan»?',
                 ['Dormi y luego llego Juan.',
                  'Juan llego y yo me quede dormido.',
                  'Estaba durmiendo en el momento en que llego Juan.',
                  'Juan y yo dormimos juntos.'],
                 2,
                 '<b>Imperfecto</b> (dormia) = accion en curso en ese momento. <b>Indefinido</b> (llego) = evento puntual que interrumpe.'),
                ('¿Cual diferencia correctamente el indefinido del perfecto?',
                 ['Ayer fui al banco (periodo cerrado) / Hoy he ido al banco (vinculado al presente).',
                  'Ayer he ido al banco / Hoy fui al banco.',
                  'Ambos son intercambiables en todos los contextos.',
                  'El indefinido siempre expresa habito; el perfecto, una accion puntual.'],
                 0,
                 '<b>Ayer</b> = tiempo cerrado → indefinido: <i>fui</i>. '
                 '<b>Hoy</b> = vinculado al presente → perfecto: <i>he ido</i>.'),
            ]
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            dict(term='indefinido (ayer / hace X)', definition='preterito indefinido: accion puntual y completa con referencia temporal cerrada',
                 example='<b>Ayer</b> sali a correr y <b>recorri</b> diez kilometros.', accept=['indefinido', 'preterito indefinido']),
            dict(term='imperfecto (de nino / siempre)', definition='preterito imperfecto: habito pasado o estado en un periodo pasado',
                 example='De nino <b>jugaba</b> al futbol todos los dias con mis amigos.', accept=['imperfecto', 'preterito imperfecto']),
            dict(term='perfecto (hoy / ya / nunca)', definition='preterito perfecto: accion pasada vinculada al presente o resultado actual',
                 example='Esta semana <b>he trabajado</b> mas de cincuenta horas.', accept=['perfecto', 'preterito perfecto']),
            dict(term='imperfecto (fondo) + indefinido (figura)', definition='en narracion: imperfecto para el escenario, indefinido para los eventos',
                 example='<b>Llovía</b> mucho cuando de repente <b>sono</b> el timbre.', accept=['imperfecto fondo', 'imperfecto para el fondo']),
            dict(term='dormia cuando sono', definition='imperfecto (accion en curso) + indefinido (interrupcion): estructura tipica de narracion',
                 example='<b>Dormia</b> profundamente cuando <b>sono</b> la alarma.', accept=['dormia cuando sono', 'imperfecto + indefinido']),
            dict(term='he terminado', definition='perfecto: resultado presente de una accion pasada (ya, esta semana, hoy)',
                 example='Ya <b>he terminado</b> el informe; puedes leerlo cuando quieras.', accept=['he terminado']),
            dict(term='fui (ayer / el lunes pasado)', definition='indefinido de IR: accion puntual en periodo de tiempo cerrado',
                 example='<b>Ayer</b> fui al medico y me receto antibioticos.', accept=['fui']),
            dict(term='iba (de nino / siempre)', definition='imperfecto de IR: habito o estado pasado recurrente',
                 example='Cuando era joven, <b>iba</b> a la biblioteca todos los viernes.', accept=['iba']),
        ],
    ),
}
