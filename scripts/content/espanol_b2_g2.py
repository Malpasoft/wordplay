# -*- coding: utf-8 -*-
"""espanol/ B2 Gramática — lote 2 (G06–G10)."""

CHAPTERS = {
    'oraciones-subordinadas': dict(
        level='b2',
        section='grammar',
        num='G06',
        short='Oraciones Subordinadas',
        title='Las Oraciones Subordinadas Complejas',
        subtitle='Sustantivas, adjetivas, adverbiales, discurso indirecto y formas no personales',
        slides=[
            ('Tipos de oraciones subordinadas', None,
             '<p class="slide-explanation">Una <b>oración subordinada</b> depende de la oración principal '
             'y desempeña la función de un sustantivo, un adjetivo o un adverbio.</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Tipo</th>'
             '<th style="padding:8px;text-align:left">Función</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Sustantiva</b></td>'
             '<td style="padding:8px">Sujeto u objeto del verbo principal</td>'
             '<td style="padding:8px">Quiero <b>que vengas</b>. / Sé <b>que es tarde</b>.</td></tr>'
             '<tr><td style="padding:8px"><b>Adjetiva especificativa</b></td>'
             '<td style="padding:8px">Restringe el significado del antecedente (sin coma)</td>'
             '<td style="padding:8px">El estudiante <b>que aprobó</b> recibirá el premio.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Adjetiva explicativa</b></td>'
             '<td style="padding:8px">Añade información no restrictiva (entre comas)</td>'
             '<td style="padding:8px">Mi hermana, <b>que vive en Madrid</b>, viene el lunes.</td></tr>'
             '<tr><td style="padding:8px"><b>Adverbial</b></td>'
             '<td style="padding:8px">Expresa tiempo, causa, condición, etc.</td>'
             '<td style="padding:8px"><b>Cuando llegues</b>, llámame.</td></tr>'
             '</table>'),

            ('Discurso indirecto: indicativo y subjuntivo', None,
             '<p class="slide-explanation">En el <b>discurso indirecto</b>, la elección del modo depende '
             'del verbo introductorio: los verbos de comunicación neutral usan <b>indicativo</b>; '
             'los de influencia o ruego, <b>subjuntivo</b>.</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Verbo introductorio</th>'
             '<th style="padding:8px;text-align:left">Modo</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">decir, afirmar, comentar</td>'
             '<td style="padding:8px">indicativo</td>'
             '<td style="padding:8px">Dice <b>que tiene</b> mucho trabajo.</td></tr>'
             '<tr><td style="padding:8px">pedir, rogar, ordenar</td>'
             '<td style="padding:8px">subjuntivo</td>'
             '<td style="padding:8px">Pide <b>que llegues</b> puntual.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">preguntar si / qué</td>'
             '<td style="padding:8px">indicativo (pregunta indirecta)</td>'
             '<td style="padding:8px">Pregunta <b>si puedes</b> ayudarle.</td></tr>'
             '<tr><td style="padding:8px">aconsejar, sugerir, recomendar</td>'
             '<td style="padding:8px">subjuntivo</td>'
             '<td style="padding:8px">Sugiere <b>que vayas</b> al médico.</td></tr>'
             '</table>'
             '<p class="slide-explanation">Regla clave: <b>decir que + indicativo</b> transmite información; '
             '<b>decir que + subjuntivo</b> (= mandar) transmite una orden o ruego.</p>'),

            ('Relativas con preposición', None,
             '<p class="slide-explanation">Las oraciones de relativo frecuentemente llevan una <b>preposición</b> '
             'antes del relativo. En español, la preposición siempre va <b>delante</b> del relativo, nunca al final:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>de que:</b> El libro <b>del que</b> te hablé está agotado.</p>'
             '<p><b>a que / a la que:</b> La ciudad <b>a la que</b> viajaremos es Cartagena.</p>'
             '<p><b>con que / con quien:</b> El colega <b>con quien</b> trabajo es muy amable.</p>'
             '<p><b>en que / en el que:</b> La época <b>en que</b> vivió fue difícil.</p>'
             '<p><b>para que / para el que:</b> El proyecto <b>para el que</b> me contrataron es enorme.</p>'
             '</div>'
             '<p class="slide-explanation">Cuando el antecedente es una <b>persona</b>, se prefiere '
             '<b>quien/quienes</b>; cuando es una cosa, se prefiere <b>el/la/los/las que</b> '
             'o <b>el/la/los/las cual(es)</b> (más formal).</p>'),

            ('Gerundio y participio en subordinadas', None,
             '<p class="slide-explanation">El <b>gerundio</b> y el <b>participio</b> pueden encabezar '
             'oraciones subordinadas con valor adverbial, reduciendo la estructura sin nexo:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Forma</th>'
             '<th style="padding:8px;text-align:left">Valor</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Gerundio</b> (simultaneidad)</td>'
             '<td style="padding:8px">Acción simultánea o en progreso</td>'
             '<td style="padding:8px"><b>Llegando tarde</b>, no pudo entrar. (= Como llegó tarde…)</td></tr>'
             '<tr><td style="padding:8px"><b>Gerundio</b> (causa)</td>'
             '<td style="padding:8px">Expresa causa de la acción principal</td>'
             '<td style="padding:8px"><b>Sabiendo la verdad</b>, calló. (= Dado que sabía la verdad…)</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Participio</b> (anterioridad)</td>'
             '<td style="padding:8px">Acción terminada antes de la principal</td>'
             '<td style="padding:8px"><b>Terminada la reunión</b>, salimos. (= Una vez terminada la reunión…)</td></tr>'
             '<tr><td style="padding:8px"><b>Participio</b> (condición)</td>'
             '<td style="padding:8px">Condición previa cumplida</td>'
             '<td style="padding:8px"><b>Revisados los documentos</b>, firmaremos el contrato.</td></tr>'
             '</table>'
             '<p class="slide-explanation">El participio en estas construcciones concuerda en género y número '
             'con el sustantivo al que se refiere.</p>'),

            ('Infinitivo en oraciones subordinadas', None,
             '<p class="slide-explanation">El <b>infinitivo</b> encabeza subordinadas cuando no hay cambio de sujeto, '
             'o en estructuras fijas como <b>al + infinitivo</b> y <b>de haber + participio</b>:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Estructura</th>'
             '<th style="padding:8px;text-align:left">Valor</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>al + infinitivo</b></td>'
             '<td style="padding:8px">Tiempo: en el momento en que</td>'
             '<td style="padding:8px"><b>Al llegar</b>, vio la nota en la puerta.</td></tr>'
             '<tr><td style="padding:8px"><b>de + infinitivo</b></td>'
             '<td style="padding:8px">Condición (= si)</td>'
             '<td style="padding:8px"><b>De saber</b> la verdad, habría actuado antes.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>de haber + participio</b></td>'
             '<td style="padding:8px">Condición pasada irreal</td>'
             '<td style="padding:8px"><b>De haber sabido</b> la noticia, habría venido.</td></tr>'
             '<tr><td style="padding:8px"><b>por + infinitivo</b></td>'
             '<td style="padding:8px">Causa</td>'
             '<td style="padding:8px">Lo castigaron <b>por llegar</b> tarde.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>para + infinitivo</b></td>'
             '<td style="padding:8px">Finalidad</td>'
             '<td style="padding:8px">Estudia mucho <b>para aprobar</b> el examen.</td></tr>'
             '</table>'),
        ],
        traps=[
            ('El libro que te hablé está aquí', 'El libro <strong>del que</strong> te hablé está aquí',
             'Cuando el verbo de la subordinada exige «de» (hablar <b>de</b> algo), la preposición debe colocarse '
             'delante del relativo: <b>del que</b> (= de + el que). No se puede omitir la preposición.'),
            ('Llegando tarde, no puede entrar (presente para relato pasado)', '<strong>Llegando tarde, no pudo entrar</strong>',
             'El gerundio en subordinadas expresa simultaneidad o causa respecto al verbo principal, que lleva el tiempo del relato. '
             'Si el relato es en pasado, el verbo principal va en pasado: <b>no pudo entrar</b>.'),
            ('Terminado la reunión, salimos', '<strong>Terminada</strong> la reunión, salimos',
             'El participio en estas construcciones concuerda con el sustantivo al que modifica: '
             '«la reunión» es femenina → <b>terminada</b>, no «terminado».'),
            ('Dice que vengas (para informar de algo)', 'Dice <strong>que viene</strong> (informar) / Dice <strong>que vengas</strong> (= ordena)',
             '«Decir que + indicativo» transmite información: «Dice que <b>viene</b> mañana». '
             '«Decir que + subjuntivo» transmite una orden: «Dice que <b>vengas</b>» = ordena que vengas.'),
            ('Al llegar, vi que la puerta estaba abierta → De llegar, vi…', '<strong>Al llegar</strong>, vi que la puerta estaba abierta',
             '<b>Al + infinitivo</b> expresa tiempo (= en el momento en que llegué). '
             '<b>De + infinitivo</b> expresa condición (= si llegara). No son intercambiables.'),
        ],
        summary=[
            ('Relativa especificativa', 'sin coma, restringe el antecedente', 'El alumno que llegó tarde se quedó sin examen.'),
            ('Relativa explicativa', 'entre comas, añade información', 'Mi profesor, que es muy exigente, nos apoya mucho.'),
            ('Relativa con preposición', 'prep. + que/quien/el cual', 'La empresa para la que trabajo es internacional.'),
            ('Discurso indirecto: decir que', 'decir que + ind. (info) / decir que + subj. (orden)', 'Dice que viene. / Dice que vengas.'),
            ('Al + infinitivo', 'tiempo: en el momento en que', 'Al salir, me encontré con ella.'),
            ('De haber + participio', 'condición pasada irreal', 'De haber estudiado, habría aprobado.'),
            ('Participio absoluto', 'participio concuerda con sust., acción anterior', 'Cerradas las puertas, empezó el concierto.'),
        ],
        ex1=dict(
            title='Elige la forma correcta de la subordinada',
            questions=[
                ('El problema ______ te hablé ya está resuelto.',
                 ['que', 'del que', 'de que', 'el cual'], 1,
                 'Hablar <b>de</b> algo exige la preposición delante del relativo: <b>del que</b> (= de + el que).'),
                ('Pide ______ (llegar, tú) puntual a la reunión.',
                 ['que llegas', 'que llegues', 'si llegas', 'que llegarás'], 1,
                 'Pedir exige influencia → subjuntivo en la subordinada: <b>que llegues</b>.'),
                ('______ (terminar) el partido, los jugadores celebraron la victoria.',
                 ['Terminando', 'Terminado', 'Terminar', 'Al terminar'], 1,
                 'Participio absoluto: acción anterior concluida. «El partido» es masc. sg. → <b>Terminado</b>.'),
                ('______ (llegar) a casa, encontré un mensaje en la puerta.',
                 ['Llegando', 'Llegado', 'Al llegar', 'De llegar'], 2,
                 '<b>Al + infinitivo</b> expresa tiempo: en el momento en que llegué.'),
                ('La ciudad ______ viajaremos el próximo verano es Granada.',
                 ['que', 'a que', 'a la que', 'la cual'], 2,
                 'Viajar <b>a</b> un lugar: la preposición va delante del relativo: <b>a la que</b>.'),
                ('Afirma ______ (estudiar) todos los días sin excepción.',
                 ['que estudia', 'que estudie', 'si estudia', 'de estudiar'], 0,
                 'Afirmar transmite información → indicativo: <b>que estudia</b>.'),
            ]
        ),
        ex2=dict(
            title='Completa con la estructura adecuada',
            questions=[
                ('La película ______ (de la que / que) más te hablé acaba de estrenarse.',
                 'de la que', ['de la que'],
                 'Hablar <b>de</b> algo: la preposición precede al relativo femenino → <b>de la que</b>.'),
                ('______ (al + salir) del trabajo, siempre llamo a mi madre.',
                 'Al salir', ['Al salir'],
                 '<b>Al + infinitivo</b> indica el momento simultáneo a la acción principal.'),
                ('______ (revisar) los datos, el director firmó el informe. (participio)',
                 'Revisados', ['Revisados'],
                 '«Los datos» es masculino plural → participio en masc. pl.: <b>Revisados</b>.'),
                ('Le rogamos ______ (enviar) la documentación antes del viernes.',
                 'que envíe', ['que envíe'],
                 'Rogar expresa influencia → subjuntivo: <b>que envíe</b>.'),
                ('______ (de haber + saber) la verdad antes, habría actuado de otra manera.',
                 'De haber sabido', ['De haber sabido'],
                 '<b>De haber + participio</b> expresa condición pasada irreal: <b>De haber sabido</b>.'),
            ]
        ),
        ex3=dict(
            title='Identifica el uso correcto',
            questions=[
                ('¿Cuál usa correctamente el relativo con preposición?',
                 ['El tema que hablamos es importante.',
                  'El tema del que hablamos es importante.',
                  'El tema de que hablamos es importante.',
                  'El tema el cual hablamos es importante.'], 1,
                 'Hablar <b>de</b> algo: preposición + artículo + relativo → <b>del que</b>.'),
                ('¿Cuál muestra un participio absoluto correcto?',
                 ['Terminando la clase, salimos rápido.',
                  'Terminada la clase, salimos rápido.',
                  'Terminado la clase, salimos rápido.',
                  'Terminar la clase, salimos rápido.'], 1,
                 '«La clase» es femenina → participio en femenino: <b>Terminada</b>. No es un gerundio.'),
                ('¿Cuál transmite una orden en discurso indirecto?',
                 ['Dice que viene mañana.',
                  'Dice que vendrá mañana.',
                  'Dice que vengas mañana.',
                  'Dice que vendría mañana.'], 2,
                 '<b>Decir que + subjuntivo</b> equivale a ordenar: «dice que <b>vengas</b>» = te ordena que vengas.'),
                ('¿Qué valor tiene «Al salir del trabajo, la llamé»?',
                 ['Causa: porque salí del trabajo.',
                  'Condición: si salgo del trabajo.',
                  'Tiempo: en el momento en que salí del trabajo.',
                  'Finalidad: para salir del trabajo.'], 2,
                 '<b>Al + infinitivo</b> expresa tiempo simultáneo: en el momento en que salí.'),
                ('¿Cuál usa «de haber + participio» correctamente?',
                 ['De haber sabido, vendría.',
                  'De haber sabido, habría venido.',
                  'De saber, habría venido.',
                  'Al haber sabido, habría venido.'], 1,
                 '<b>De haber + participio</b> expresa condición pasada irreal; la consecuencia va en condicional compuesto: <b>habría venido</b>.'),
            ]
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            dict(term='del que', definition='relativo con preposición de: hablar del que, el libro del que',
                 example='El libro <b>del que</b> te hablé ya no está disponible.',
                 accept=['del que']),
            dict(term='a la que', definition='relativo femenino con preposición a: la ciudad a la que',
                 example='La ciudad <b>a la que</b> viajaremos es Sevilla.',
                 accept=['a la que']),
            dict(term='al llegar', definition='al + infinitivo: en el momento en que llegué',
                 example='<b>Al llegar</b> a casa, encontró un mensaje urgente.',
                 accept=['al llegar', 'Al llegar']),
            dict(term='terminada la reunión', definition='participio absoluto (fem. sg.): acción anterior completada',
                 example='<b>Terminada la reunión</b>, todos salieron al pasillo.',
                 accept=['terminada la reunión', 'Terminada la reunión']),
            dict(term='dice que viene', definition='discurso indirecto: decir que + indicativo = transmitir información',
                 example='<b>Dice que viene</b> mañana por la mañana.',
                 accept=['dice que viene']),
            dict(term='pide que vengas', definition='discurso indirecto: pedir que + subjuntivo = ruego u orden',
                 example='<b>Pide que vengas</b> pronto; es urgente.',
                 accept=['pide que vengas']),
            dict(term='de haber sabido', definition='de haber + participio: condición pasada irreal',
                 example='<b>De haber sabido</b> la noticia, habría llamado antes.',
                 accept=['de haber sabido', 'De haber sabido']),
            dict(term='llegando tarde', definition='gerundio con valor causal: como llegó tarde',
                 example='<b>Llegando tarde</b>, no pudo entrar al auditorio.',
                 accept=['llegando tarde', 'Llegando tarde']),
        ],
    ),

    'cuantificadores-b2': dict(
        level='b2',
        section='grammar',
        num='G07',
        short='Cuantificadores Avanzados',
        title='Los Cuantificadores y Determinantes Avanzados',
        subtitle='Sendos, ambos, cierto, cualquier(a), demás, varios y sus usos precisos',
        slides=[
            ('Más allá de mucho y poco', None,
             '<p class="slide-explanation">El español dispone de una variedad de <b>cuantificadores y determinantes</b> '
             'más precisos que <i>mucho</i> o <i>poco</i>. Dominarlos es una marca de nivel avanzado:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Término</th>'
             '<th style="padding:8px;text-align:left">Significado</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>sendos/sendas</b></td>'
             '<td style="padding:8px">uno/una para cada uno de los mencionados</td>'
             '<td style="padding:8px">Los dos firmaron <b>sendos</b> documentos.</td></tr>'
             '<tr><td style="padding:8px"><b>ambos/ambas</b></td>'
             '<td style="padding:8px">los dos, los uno y el otro</td>'
             '<td style="padding:8px"><b>Ambas</b> propuestas son válidas.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>varios/varias</b></td>'
             '<td style="padding:8px">más de dos, algunos (plural)</td>'
             '<td style="padding:8px">He leído <b>varios</b> artículos sobre el tema.</td></tr>'
             '<tr><td style="padding:8px"><b>demás</b></td>'
             '<td style="padding:8px">el resto, los otros (invariable)</td>'
             '<td style="padding:8px">Los <b>demás</b> estudiantes llegaron puntual.</td></tr>'
             '</table>'),

            ('Cualquier y cualquiera', None,
             '<p class="slide-explanation"><b>Cualquier</b> y <b>cualquiera</b> provienen de la misma forma pero '
             'tienen distribuciones distintas:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Forma</th>'
             '<th style="padding:8px;text-align:left">Posición</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>cualquier</b></td>'
             '<td style="padding:8px">Antes del sustantivo (masc. y fem., invariable)</td>'
             '<td style="padding:8px"><b>Cualquier</b> estudiante puede participar. / <b>Cualquier</b> idea es bienvenida.</td></tr>'
             '<tr><td style="padding:8px"><b>cualquiera</b></td>'
             '<td style="padding:8px">Después del sustantivo o solo (pronombre)</td>'
             '<td style="padding:8px">Un día <b>cualquiera</b>. / <b>Cualquiera</b> de vosotros puede hacerlo.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>cualesquiera</b></td>'
             '<td style="padding:8px">Plural de cualquiera (poco frecuente)</td>'
             '<td style="padding:8px">En <b>cualesquiera</b> circunstancias que se den…</td></tr>'
             '</table>'
             '<p class="slide-explanation">Nota: «cualquier» es la forma apocopada de «cualquiera» y solo se usa '
             'antes del sustantivo. Nunca se dice «*cualquiera libro».</p>'),

            ('Sendos: uno para cada uno', None,
             '<p class="slide-explanation"><b>Sendos/sendas</b> es un cuantificador distributivo que significa '
             '«uno/una para cada uno de los sujetos mencionados». '
             'Es exclusivamente <b>plural</b> y concuerda en género:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Los dos presidentes firmaron sendos acuerdos.</b><br>'
             '(cada presidente firmó su propio acuerdo = dos acuerdos en total)</p>'
             '<p><b>Las tres ciudades recibieron sendas medallas.</b><br>'
             '(cada ciudad recibió una medalla = tres medallas en total)</p>'
             '</div>'
             '<p class="slide-explanation">Errores frecuentes: no significa «grandes», «notables» ni «ambos». '
             'Su uso es formal y literario; en el habla coloquial se prefiere «uno cada uno» o «un ______ cada uno».</p>'),

            ('Cierto: posición y cambio de significado', None,
             '<p class="slide-explanation"><b>Cierto/a</b> cambia de significado según su posición '
             'respecto al sustantivo:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Posición</th>'
             '<th style="padding:8px;text-align:left">Significado</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Antes</b> del sustantivo</td>'
             '<td style="padding:8px">Un cierto / algún (= un determinado)</td>'
             '<td style="padding:8px"><b>Cierto</b> día, recibió una carta extraña.</td></tr>'
             '<tr><td style="padding:8px"><b>Después</b> del sustantivo o con <i>ser</i></td>'
             '<td style="padding:8px">Verdadero / seguro</td>'
             '<td style="padding:8px">El rumor es <b>cierto</b>. / Hay un peligro <b>cierto</b>.</td></tr>'
             '</table>'
             '<p class="slide-explanation">Del mismo modo, <b>varios</b> siempre precede al sustantivo '
             'y no varía según posición, pero sí concuerda en género: varios libros / varias ideas.</p>'),

            ('Demás: el resto y los otros', None,
             '<p class="slide-explanation"><b>Demás</b> es <b>invariable</b> (no cambia de forma) y siempre '
             'va precedido por artículo o determinante. Hace referencia al resto de un grupo ya mencionado:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Uso</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>los/las demás</b> (personas o cosas)</td>'
             '<td style="padding:8px">Los demás llegaron tarde; solo Ana fue puntual.</td></tr>'
             '<tr><td style="padding:8px"><b>lo demás</b> (lo que queda, neutro)</td>'
             '<td style="padding:8px">Lo demás no importa; lo esencial ya está hecho.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>las demás + sust. fem. pl.</b></td>'
             '<td style="padding:8px">Las demás ideas quedaron pendientes para la próxima reunión.</td></tr>'
             '</table>'
             '<p class="slide-explanation">No confundir con <b>además</b> (= también, encima): '
             '«<b>Además</b>, hay que revisar el presupuesto.»</p>'),
        ],
        traps=[
            ('Los dos recibieron sendos premios → sendos = grandes o importantes', 'sendos = <strong>uno para cada uno</strong>',
             '<b>Sendos</b> significa «uno para cada uno de los mencionados», no «grandes» ni «notables». '
             '«Los dos recibieron sendos premios» = cada uno recibió un premio.'),
            ('Cualquiera libro puede servir', '<strong>Cualquier</strong> libro puede servir',
             'Ante sustantivo, se usa la forma apocopada <b>cualquier</b> (sin -a final), igual para masculino y femenino. '
             '«Cualquiera» se usa solo (pronombre) o detrás del sustantivo.'),
            ('Es una persona cierta / Es una cierta solución (= segura)', 'Es una solución <strong>cierta</strong> (= segura) / <strong>Cierta</strong> solución (= una determinada solución)',
             'Antes del sustantivo, «cierto» significa «un determinado». Después del sustantivo o con SER, significa «verdadero/seguro». La posición determina el significado.'),
            ('Los demás idea / Los demás ideas', 'Las <strong>demás</strong> ideas',
             '<b>Demás</b> es invariable, pero el artículo que lo precede sí concuerda: <b>las</b> demás ideas (femenino plural).'),
            ('Varios de sus libros están en la lista → varios = ambos', 'varios ≠ ambos: <strong>varios</strong> = más de dos; <strong>ambos</strong> = los dos exactamente',
             '<b>Varios</b> implica más de dos elementos. <b>Ambos</b> se refiere exactamente a dos. No son intercambiables.'),
        ],
        summary=[
            ('sendos/sendas', 'uno/una para cada uno de los mencionados (distributivo, formal)', 'Los dos embajadores firmaron sendos tratados.'),
            ('ambos/ambas', 'los dos exactamente, sin excepción', 'Ambas opciones tienen ventajas e inconvenientes.'),
            ('varios/varias', 'más de dos, algunos (precede al sustantivo)', 'He consultado varios manuales sobre el tema.'),
            ('cualquier (+ sust.)', 'forma apocopada, antes del sustantivo, invariable', 'Cualquier persona puede apuntarse al curso.'),
            ('cualquiera (solo / detrás sust.)', 'pronombre o adjetivo pospuesto', 'Un día cualquiera / Cualquiera puede equivocarse.'),
            ('cierto (antes sust.)', 'un determinado, algún', 'Cierto día, encontró una llave extraña.'),
            ('demás (invariable)', 'el resto del grupo, siempre con artículo', 'Los demás alumnos ya habían terminado.'),
        ],
        ex1=dict(
            title='Elige el cuantificador correcto',
            questions=[
                ('Los tres ganadores recibieron ______ trofeos (uno para cada uno).',
                 ['ambos', 'sendos', 'varios', 'ciertos'], 1,
                 '<b>Sendos</b> = uno para cada uno de los mencionados. Tres ganadores → tres trofeos en total.'),
                ('______ estudiante puede acceder a los recursos de la biblioteca.',
                 ['Cualquiera', 'Cualquier', 'Cierto', 'Sendos'], 1,
                 'Ante el sustantivo «estudiante», se usa la forma apocopada <b>cualquier</b>.'),
                ('______ día que estaba paseando, encontró una cartera en el suelo.',
                 ['Cierto', 'Ciertos', 'Algún cierto', 'Cualquier'], 0,
                 '<b>Cierto</b> antes del sustantivo = un determinado día; equivale a «un día concreto».'),
                ('Los ______ estudiantes que no entregaron el trabajo tendrán que repetirlo.',
                 ['demás', 'sendos', 'ambos', 'ciertos'], 0,
                 '<b>Los demás</b> = el resto del grupo ya mencionado o conocido.'),
                ('He tenido ______ problemas con el ordenador esta semana, pero ya está arreglado.',
                 ['ambos', 'sendos', 'varios', 'demás'], 2,
                 '<b>Varios</b> = más de dos problemas. Ambos sería solo dos exactamente.'),
                ('______ de las dos propuestas me parece interesante; las acepto.',
                 ['Sendas', 'Varios', 'Ambas', 'Cualquiera'], 2,
                 '<b>Ambas</b> = las dos propuestas, sin excepción. Hace referencia exacta a los dos elementos mencionados.'),
            ]
        ),
        ex2=dict(
            title='Completa con el determinante adecuado',
            questions=[
                ('Las dos delegaciones firmaron ______ acuerdos comerciales (uno cada una).',
                 'sendos', ['sendos'],
                 '<b>Sendos</b> (masc. pl.): uno para cada delegación; acuerdos es masculino plural.'),
                ('______ persona que quiera participar debe inscribirse antes del viernes.',
                 'Cualquier', ['Cualquier'],
                 'Antes de «persona» (sustantivo), se usa la forma apocopada <b>cualquier</b>.'),
                ('Lo que dijiste en la reunión es completamente ______; lo he verificado.',
                 'cierto', ['cierto'],
                 'Después del sustantivo o con SER/ESTAR, <b>cierto</b> = verdadero, correcto.'),
                ('Ana ya terminó su parte; lo ______ lo haremos mañana.',
                 'demás', ['lo demás', 'demás'],
                 '<b>Lo demás</b> (neutro) = lo que resta, el resto de las tareas.'),
                ('Me han llegado ______ correos sobre el mismo asunto; parece un problema generalizado.',
                 'varios', ['varios'],
                 '<b>Varios</b> = más de dos, cantidad indeterminada pero superior a dos.'),
            ]
        ),
        ex3=dict(
            title='Uso correcto de los cuantificadores avanzados',
            questions=[
                ('¿Qué significa «Los dos ministros firmaron sendos decretos»?',
                 ['Los dos ministros firmaron dos decretos juntos.',
                  'Cada ministro firmó un decreto diferente.',
                  'Los ministros firmaron decretos importantes.',
                  'Los ministros firmaron varios decretos.'], 1,
                 '<b>Sendos</b> = distributivo: cada uno firmó el suyo. Dos ministros → dos decretos en total.'),
                ('¿Cuál usa «cualquier» correctamente?',
                 ['Cualquiera libro sirve para el ejercicio.',
                  'Cualquier de ellos puede ayudarte.',
                  'Cualquier pregunta es bienvenida.',
                  'Un libro cualquier es suficiente.'], 2,
                 '<b>Cualquier</b> (apocopado) precede directamente al sustantivo: <b>cualquier</b> pregunta.'),
                ('¿En qué caso «cierto» significa "verdadero"?',
                 ['Cierto día llegó una carta.',
                  'Cierta persona me lo dijo.',
                  'El rumor resultó ser cierto.',
                  'Bajo ciertas condiciones.'], 2,
                 'Pospuesto o con SER, <b>cierto</b> = verdadero: «El rumor resultó ser <b>cierto</b>».'),
                ('¿Cuál usa «demás» correctamente?',
                 ['Los demás ideas quedaron pendientes.',
                  'Las demás ideas quedaron pendientes.',
                  'Los demás idea quedó pendiente.',
                  'Los demas ideas quedaron pendientes.'], 1,
                 '<b>Demás</b> es invariable, pero el artículo concuerda: <b>las</b> demás ideas (fem. pl.).'),
                ('¿Cuál es la diferencia entre «ambos» y «varios»?',
                 ['"Ambos" = más de dos; "varios" = exactamente dos.',
                  '"Ambos" = exactamente dos; "varios" = más de dos.',
                  '"Ambos" y "varios" son sinónimos intercambiables.',
                  '"Ambos" = ninguno; "varios" = todos.'], 1,
                 '<b>Ambos</b> se refiere exactamente a dos elementos; <b>varios</b> indica una cantidad superior a dos.'),
            ]
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            dict(term='sendos', definition='distributivo: uno para cada uno de los mencionados (formal)',
                 example='Los dos socios firmaron <b>sendos</b> contratos ante el notario.',
                 accept=['sendos']),
            dict(term='ambos', definition='los dos exactamente, sin excepción',
                 example='<b>Ambos</b> candidatos presentaron sus proyectos ante el jurado.',
                 accept=['ambos', 'ambas']),
            dict(term='varios', definition='más de dos, cantidad indeterminada; precede al sustantivo',
                 example='He encontrado <b>varios</b> errores en el documento.',
                 accept=['varios', 'varias']),
            dict(term='cualquier', definition='forma apocopada de cualquiera; ante sustantivo, invariable',
                 example='<b>Cualquier</b> ciudadano puede presentar una reclamación.',
                 accept=['cualquier']),
            dict(term='cualquiera', definition='pronombre o adjetivo pospuesto al sustantivo',
                 example='Un día <b>cualquiera</b> puede cambiar tu vida.',
                 accept=['cualquiera']),
            dict(term='cierto (antes)', definition='antes del sustantivo: un determinado, algún',
                 example='<b>Cierta</b> persona me contó lo que había ocurrido.',
                 accept=['cierto', 'cierta']),
            dict(term='los demás', definition='el resto del grupo; demás es invariable, el artículo concuerda',
                 example='<b>Los demás</b> participantes esperaban en el pasillo.',
                 accept=['los demás', 'las demás']),
            dict(term='lo demás', definition='el resto de las cosas (neutro); lo que queda',
                 example='Ya hemos resuelto lo esencial; <b>lo demás</b> puede esperar.',
                 accept=['lo demás']),
        ],
    ),

    'preposiciones-b2': dict(
        level='b2',
        section='grammar',
        num='G08',
        short='Preposiciones Avanzadas',
        title='Las Preposiciones Avanzadas',
        subtitle='Usos complejos de a, de, en, sin, sobre y verbos que cambian de significado con la preposición',
        slides=[
            ('A: movimiento, objeto indirecto y tiempo', None,
             '<p class="slide-explanation">La preposición <b>a</b> tiene usos muy variados. '
             'Los más importantes en nivel B2:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Uso</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Movimiento / dirección</b></td>'
             '<td style="padding:8px">Voy <b>a</b> Madrid. / Me acerqué <b>al</b> mostrador.</td></tr>'
             '<tr><td style="padding:8px"><b>Objeto indirecto</b></td>'
             '<td style="padding:8px">Le di el libro <b>a</b> Juan.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Objeto directo personal</b></td>'
             '<td style="padding:8px">Vi <b>a</b> tu hermano en el parque.</td></tr>'
             '<tr><td style="padding:8px"><b>Tiempo exacto</b></td>'
             '<td style="padding:8px">Llega <b>a</b> las tres. / <b>A</b> partir de mañana.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Al + infinitivo</b></td>'
             '<td style="padding:8px"><b>Al llegar</b>, llamó a la puerta. (tiempo)</td></tr>'
             '</table>'),

            ('DE: posesión, origen, causa y verbos', None,
             '<p class="slide-explanation"><b>De</b> es la preposición de mayor frecuencia en español y tiene '
             'un amplio espectro de usos:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Uso</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Posesión / pertenencia</b></td>'
             '<td style="padding:8px">El coche <b>de</b> mi padre. / La capital <b>de</b> España.</td></tr>'
             '<tr><td style="padding:8px"><b>Origen / procedencia</b></td>'
             '<td style="padding:8px">Soy <b>de</b> Colombia. / Vengo <b>de</b> la oficina.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Material / contenido</b></td>'
             '<td style="padding:8px">Una mesa <b>de</b> madera. / Una taza <b>de</b> café.</td></tr>'
             '<tr><td style="padding:8px"><b>Causa</b></td>'
             '<td style="padding:8px">Murió <b>de</b> frío. / Llora <b>de</b> alegría.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Partitivo</b></td>'
             '<td style="padding:8px">Quiero un poco <b>de</b> agua. / Hay mucho <b>de</b> todo.</td></tr>'
             '<tr><td style="padding:8px"><b>Tras adjetivo</b></td>'
             '<td style="padding:8px">Es fácil <b>de</b> entender. / Difícil <b>de</b> olvidar.</td></tr>'
             '</table>'),

            ('EN: lugar, tiempo y medio', None,
             '<p class="slide-explanation"><b>En</b> localiza en el espacio y en el tiempo, '
             'e indica el medio o la manera de algo:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Uso</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Lugar / ubicación</b></td>'
             '<td style="padding:8px">Está <b>en</b> casa. / Vivo <b>en</b> Madrid.</td></tr>'
             '<tr><td style="padding:8px"><b>Tiempo (estaciones, meses, años)</b></td>'
             '<td style="padding:8px"><b>En</b> verano. / <b>En</b> 2024. / <b>En</b> enero.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Duración de una tarea</b></td>'
             '<td style="padding:8px">Lo hice <b>en</b> dos horas. (tiempo que tardé)</td></tr>'
             '<tr><td style="padding:8px"><b>Medio de transporte</b></td>'
             '<td style="padding:8px">Viajé <b>en</b> tren. / Voy <b>en</b> bicicleta.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Modo / manera</b></td>'
             '<td style="padding:8px">Lo dijo <b>en</b> broma. / Habla <b>en</b> voz baja.</td></tr>'
             '</table>'),

            ('Preposiciones menos frecuentes: sin, sobre, bajo, ante, tras', None,
             '<p class="slide-explanation">Estas preposiciones tienen usos específicos y cultos '
             'que conviene conocer en B2:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Preposición</th>'
             '<th style="padding:8px;text-align:left">Significado principal</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>sin</b></td>'
             '<td style="padding:8px">ausencia, carencia</td>'
             '<td style="padding:8px">Salió <b>sin</b> abrigo. / Lo hizo <b>sin</b> esfuerzo.</td></tr>'
             '<tr><td style="padding:8px"><b>sobre</b></td>'
             '<td style="padding:8px">encima de; acerca de; aproximadamente</td>'
             '<td style="padding:8px">Un libro <b>sobre</b> historia. / Llegará <b>sobre</b> las cinco.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>bajo</b></td>'
             '<td style="padding:8px">debajo de; condición, dependencia</td>'
             '<td style="padding:8px"><b>Bajo</b> ningún concepto. / <b>Bajo</b> la lluvia.</td></tr>'
             '<tr><td style="padding:8px"><b>ante</b></td>'
             '<td style="padding:8px">delante de; en presencia de; frente a (formal)</td>'
             '<td style="padding:8px">Compareció <b>ante</b> el juez.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>tras</b></td>'
             '<td style="padding:8px">detrás de; después de (formal/literario)</td>'
             '<td style="padding:8px"><b>Tras</b> la reunión, firmaron el acuerdo.</td></tr>'
             '</table>'),

            ('Verbos que cambian de significado según la preposición', None,
             '<p class="slide-explanation">Algunos verbos en español tienen significados muy distintos '
             'dependiendo de la preposición que los acompaña. Estos son algunos de los más importantes:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Verbo</th>'
             '<th style="padding:8px;text-align:left">Con prep. 1</th><th style="padding:8px;text-align:left">Con prep. 2</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>pensar</b></td>'
             '<td style="padding:8px">pensar <b>en</b>: tener en mente (en este momento)<br><i>Pienso <b>en</b> ti.</i></td>'
             '<td style="padding:8px">pensar <b>de</b>: opinar sobre<br><i>¿Qué piensas <b>de</b> esa idea?</i></td></tr>'
             '<tr><td style="padding:8px"><b>quedar</b></td>'
             '<td style="padding:8px">quedar <b>en</b>: acordar, quedar citado<br><i>Quedamos <b>en</b> vernos el lunes.</i></td>'
             '<td style="padding:8px">quedar <b>de</b>: quedar de algo, ponerse de acuerdo<br><i>Quedamos <b>de</b> llamarnos.</i></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>dejar</b></td>'
             '<td style="padding:8px">dejar <b>de</b>: cesar, interrumpir<br><i>Dejó <b>de</b> fumar.</i></td>'
             '<td style="padding:8px">dejar <b>en</b>: depositar en un lugar<br><i>Lo dejé <b>en</b> tu escritorio.</i></td></tr>'
             '<tr><td style="padding:8px"><b>contar</b></td>'
             '<td style="padding:8px">contar <b>con</b>: tener, disponer de; confiar en<br><i>Cuento <b>con</b> tu apoyo.</i></td>'
             '<td style="padding:8px">contar <b>de</b>: narrar algo de (más raro)<br><i>Cuéntame <b>de</b> tu viaje.</i></td></tr>'
             '</table>'),
        ],
        traps=[
            ('Viajé por tren a Madrid', 'Viajé <strong>en</strong> tren a Madrid',
             'El medio de transporte usa <b>en</b>: en tren, en avión, en coche. '
             '<b>Por</b> indica movimiento a través de un lugar: pasé por Madrid.'),
            ('Pienso de ti todo el tiempo', 'Pienso <strong>en</strong> ti todo el tiempo',
             '<b>Pensar en</b> = tener en mente, recordar. <b>Pensar de</b> = opinar sobre algo: '
             '«¿Qué piensas <b>de</b> la nueva ley?»'),
            ('Dejé de las llaves en la mesa → dejar de = dejar sobre', 'Dejé <strong>las llaves en</strong> la mesa',
             '<b>Dejar de + infinitivo</b> = cesar: «Dejó de fumar». '
             '<b>Dejar en + lugar</b> = depositar allí: «Dejé las llaves <b>en</b> la mesa».'),
            ('Es fácil de entender → Es fácil entender', 'Es fácil <strong>de</strong> entender',
             'Cuando el adjetivo va con el verbo SER y el infinitivo funciona como sujeto de la valoración, '
             'se usa <b>de</b>: «Es fácil <b>de</b> entender», «Es difícil <b>de</b> olvidar».'),
            ('Murió por frío / Lloró por alegría', 'Murió <strong>de</strong> frío / Lloró <strong>de</strong> alegría',
             'La causa de muerte, enfermedad o emoción física intensa usa <b>de</b>: '
             'morir <b>de</b> hambre, temblar <b>de</b> miedo, llorar <b>de</b> risa.'),
        ],
        summary=[
            ('a: dirección y tiempo exacto', 'ir a, a las tres, al llegar, OD personal', 'Fui a verle a las diez.'),
            ('de: posesión, origen, causa', 'coche de, soy de, morir de, fácil de', 'Murió de frío en la montaña.'),
            ('en: lugar, duración, medio', 'en casa, en dos horas, en tren, en broma', 'Lo hizo en tren en una hora.'),
            ('pensar en vs. pensar de', 'en = tener en mente; de = opinar', 'Pienso en ella. / ¿Qué piensas de eso?'),
            ('dejar de vs. dejar en', 'de + inf. = cesar; en + lugar = depositar', 'Dejó de fumar. / Dejó el abrigo en la silla.'),
            ('quedar en', 'acordar, citarse para', 'Quedamos en vernos el martes a las seis.'),
            ('contar con', 'disponer de, tener el apoyo de', 'Contamos con el apoyo de toda la empresa.'),
        ],
        ex1=dict(
            title='Elige la preposición correcta',
            questions=[
                ('Viajamos ______ avión hasta Lima y luego ______ coche hasta el hotel.',
                 ['por / por', 'en / en', 'en / por', 'por / en'], 1,
                 'Medio de transporte → <b>en</b>: en avión, en coche.'),
                ('¿Qué piensas ______ la propuesta que presentaron ayer?',
                 ['en', 'de', 'sobre', 'para'], 1,
                 '<b>Pensar de</b> = opinar: «¿Qué piensas <b>de</b> la propuesta?»'),
                ('Quedamos ______ vernos en la cafetería a las tres.',
                 ['de', 'en', 'a', 'para'], 1,
                 '<b>Quedar en</b> + infinitivo = acordar citarse: quedamos <b>en</b> vernos.'),
                ('Esta novela es muy fácil ______ leer; la acabarás en un fin de semana.',
                 ['a', 'para', 'de', 'por'], 2,
                 'Adjetivo valorativo + SER + infinitivo: <b>de</b>: fácil <b>de</b> leer.'),
                ('Después de años de intentarlo, por fin dejó ______ fumar.',
                 ['en', 'a', 'de', 'por'], 2,
                 '<b>Dejar de</b> + infinitivo = cesar, interrumpir un hábito.'),
                ('Compareció ______ el tribunal para dar su testimonio.',
                 ['en', 'con', 'ante', 'para'], 2,
                 '<b>Ante</b> = en presencia de, frente a (uso formal y jurídico).'),
            ]
        ),
        ex2=dict(
            title='Completa con la preposición adecuada',
            questions=[
                ('No pienso ______ nada más; mi mente está completamente en blanco.',
                 'en', ['en'],
                 '<b>Pensar en</b> = tener en mente, concentrarse en algo.'),
                ('Puedes contar ______ mi ayuda cuando la necesites.',
                 'con', ['con'],
                 '<b>Contar con</b> = disponer de, tener el apoyo o la disponibilidad de alguien.'),
                ('Murió ______ una enfermedad rara que los médicos no pudieron diagnosticar a tiempo.',
                 'de', ['de'],
                 'La causa de muerte usa <b>de</b>: morir <b>de</b> + enfermedad o causa.'),
                ('______ la reunión, el director anunció los cambios en la plantilla.',
                 'Tras', ['Tras'],
                 '<b>Tras</b> = después de (registro formal o literario).'),
                ('Llegará ______ las ocho; no suele ser muy puntual.',
                 'sobre', ['sobre'],
                 '<b>Sobre</b> con tiempo = aproximadamente: llegará <b>sobre</b> las ocho.'),
            ]
        ),
        ex3=dict(
            title='Identifica el uso correcto de la preposición',
            questions=[
                ('¿Cuál usa el medio de transporte correctamente?',
                 ['Fui por avión a París.',
                  'Fui en avión a París.',
                  'Fui a avión a París.',
                  'Fui de avión a París.'], 1,
                 'Medio de transporte → <b>en</b>: <b>en</b> avión.'),
                ('¿Cuál expresa la causa de un estado emocional correctamente?',
                 ['Lloraba por la tristeza.',
                  'Lloraba en tristeza.',
                  'Lloraba de tristeza.',
                  'Lloraba a tristeza.'], 2,
                 'La causa de una reacción física o emocional intensa usa <b>de</b>: llorar <b>de</b> tristeza.'),
                ('¿Cuál usa «pensar» correctamente para expresar opinión?',
                 ['¿Qué piensas en esa decisión?',
                  '¿Qué piensas de esa decisión?',
                  '¿Qué piensas sobre esa decisión?',
                  'Las opciones b y c son correctas.'], 3,
                 '<b>Pensar de</b> y <b>pensar sobre</b> expresan opinión. <b>Pensar en</b> = tener en mente.'),
                ('¿Qué significa "dejar de + infinitivo"?',
                 ['Depositar algo en un lugar.',
                  'Cesar o interrumpir una acción o hábito.',
                  'Olvidar hacer algo.',
                  'Permitir que alguien haga algo.'], 1,
                 '<b>Dejar de</b> + infinitivo = cesar, dejar de hacer algo: «Dejó <b>de</b> fumar» = ya no fuma.'),
                ('¿Cuál usa «bajo» correctamente?',
                 ['Trabaja bajo la tarde.',
                  'Lo hizo bajo ninguna presión.',
                  'Actuó bajo la presión del tiempo.',
                  'Salió bajo avión.'], 2,
                 '<b>Bajo</b> puede indicar condición o circunstancia: <b>bajo</b> la presión del tiempo.'),
            ]
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            dict(term='en tren', definition='medio de transporte: en + vehículo (no "por")',
                 example='Prefiero viajar <b>en tren</b>; es más cómodo que el autobus.',
                 accept=['en tren', 'en avión', 'en coche']),
            dict(term='pensar en', definition='pensar en = tener en mente; pensar de = opinar',
                 example='Siempre <b>pienso en</b> ti cuando escucho esa canción.',
                 accept=['pensar en', 'pienso en']),
            dict(term='dejar de', definition='dejar de + infinitivo: cesar, interrumpir un hábito',
                 example='Por fin <b>dejó de</b> fumar después de veinte años.',
                 accept=['dejar de', 'dejó de']),
            dict(term='contar con', definition='contar con: disponer de, tener el apoyo o la presencia de',
                 example='Siempre puedes <b>contar con</b> mi ayuda cuando la necesites.',
                 accept=['contar con', 'cuenta con', 'cuento con']),
            dict(term='morir de', definition='de + causa: morir de, llorar de, temblar de',
                 example='El explorador casi <b>murió de</b> frío en la expedición.',
                 accept=['morir de', 'murió de']),
            dict(term='quedar en', definition='quedar en + infinitivo: acordar citarse',
                 example='<b>Quedamos en</b> reunirnos el próximo martes a mediodía.',
                 accept=['quedar en', 'quedamos en']),
            dict(term='fácil de entender', definition='adjetivo valorativo + de + infinitivo',
                 example='Su explicación es muy <b>fácil de entender</b>.',
                 accept=['fácil de entender', 'difícil de olvidar', 'de entender']),
            dict(term='ante', definition='preposición formal: en presencia de, frente a',
                 example='El acusado compareció <b>ante</b> el tribunal esta mañana.',
                 accept=['ante']),
        ],
    ),

    'expresiones-tiempo': dict(
        level='b2',
        section='grammar',
        num='G09',
        short='Expresiones Temporales',
        title='Las Expresiones Temporales Avanzadas',
        subtitle='Hace que, llevaba, desde hace, dentro de, al + infinitivo y más',
        slides=[
            ('Hace + tiempo + que: duración y anterioridad', None,
             '<p class="slide-explanation">La construcción <b>hace + tiempo + que</b> tiene dos usos '
             'según el tiempo verbal de la subordinada:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Estructura</th>'
             '<th style="padding:8px;text-align:left">Valor</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Hace + tiempo + que + presente</b></td>'
             '<td style="padding:8px">Duración hasta ahora (sigo haciéndolo)</td>'
             '<td style="padding:8px">Hace tres años que <b>vivo</b> aquí. (= y sigo viviendo aquí)</td></tr>'
             '<tr><td style="padding:8px"><b>Hace + tiempo + que + pretérito indefinido</b></td>'
             '<td style="padding:8px">Hace + tiempo (= hace X tiempo que ocurrió)</td>'
             '<td style="padding:8px">Hace dos días que <b>llegó</b>. (= llegó hace dos días)</td></tr>'
             '</table>'
             '<p class="slide-explanation">También se puede invertir el orden: '
             '«<b>Vivo</b> aquí <b>desde hace</b> tres años» o «<b>Llegó</b> hace dos días».</p>'),

            ('Llevaba + gerundio: duración en el pasado', None,
             '<p class="slide-explanation"><b>Llevaba + tiempo + gerundio</b> expresa una acción que '
             'había durado cierto tiempo hasta el momento de otra acción pasada:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Llevaba dos horas esperando</b> cuando por fin llegó el autobús.</p>'
             '<p>(= había estado esperando durante dos horas)</p>'
             '<p>&nbsp;</p>'
             '<p><b>Llevábamos un mes sin vernos</b> cuando nos encontramos por casualidad.</p>'
             '</div>'
             '<p class="slide-explanation">En el presente: <b>llevo + tiempo + gerundio</b>: '
             '«Llevo tres horas trabajando» = he estado trabajando durante tres horas hasta ahora.</p>'),

            ('Desde hace vs. desde', None,
             '<p class="slide-explanation"><b>Desde hace</b> y <b>desde</b> expresan el punto de inicio '
             'de una acción que continúa. La diferencia es si se expresa un periodo de tiempo o una fecha:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Estructura</th>'
             '<th style="padding:8px;text-align:left">Complemento</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>desde hace</b></td>'
             '<td style="padding:8px">Cantidad de tiempo (un año, tres meses…)</td>'
             '<td style="padding:8px">Vivo aquí <b>desde hace</b> un año.</td></tr>'
             '<tr><td style="padding:8px"><b>desde</b></td>'
             '<td style="padding:8px">Punto concreto en el tiempo (fecha, evento)</td>'
             '<td style="padding:8px">Vivo aquí <b>desde</b> enero. / <b>Desde</b> que llegué.</td></tr>'
             '</table>'
             '<p class="slide-explanation">Nunca se dice «*desde un año». Con cantidad de tiempo, '
             'se necesita <b>desde hace</b>.</p>'),

            ('Dentro de vs. en: tiempo futuro y duración completada', None,
             '<p class="slide-explanation"><b>Dentro de</b> señala un punto en el futuro a partir de ahora. '
             '<b>En</b> indica cuánto tiempo tarda en completarse una tarea:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Estructura</th>'
             '<th style="padding:8px;text-align:left">Valor</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>dentro de + tiempo</b></td>'
             '<td style="padding:8px">En X tiempo a partir de ahora (futuro)</td>'
             '<td style="padding:8px">Vendrá <b>dentro de</b> una hora. (= una hora desde ahora)</td></tr>'
             '<tr><td style="padding:8px"><b>en + tiempo</b></td>'
             '<td style="padding:8px">Cuánto duró / tarda en completarse una acción</td>'
             '<td style="padding:8px">Resolvió el problema <b>en</b> diez minutos.</td></tr>'
             '</table>'
             '<p class="slide-explanation">Truco: «dentro de» apunta al futuro; «en» mide la duración de una acción.</p>'),

            ('A partir de, hasta, a tiempo y otras expresiones', None,
             '<p class="slide-explanation">El español tiene expresiones temporales de gran precisión '
             'que conviene conocer en B2:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Expresión</th>'
             '<th style="padding:8px;text-align:left">Significado</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>a partir de</b></td>'
             '<td style="padding:8px">desde ese momento en adelante</td>'
             '<td style="padding:8px"><b>A partir de</b> mañana, todo cambiará.</td></tr>'
             '<tr><td style="padding:8px"><b>hasta</b></td>'
             '<td style="padding:8px">límite temporal (el punto de llegada)</td>'
             '<td style="padding:8px">Trabajaré <b>hasta</b> las ocho.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>a tiempo</b></td>'
             '<td style="padding:8px">sin llegar tarde, puntualmente</td>'
             '<td style="padding:8px">Llegamos justo <b>a tiempo</b> para el tren.</td></tr>'
             '<tr><td style="padding:8px"><b>a destiempo</b></td>'
             '<td style="padding:8px">en mal momento, demasiado tarde o pronto</td>'
             '<td style="padding:8px">Su comentario llegó <b>a destiempo</b>.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>de momento / por el momento</b></td>'
             '<td style="padding:8px">por ahora, hasta nueva orden</td>'
             '<td style="padding:8px"><b>De momento</b>, no hay novedades.</td></tr>'
             '</table>'),
        ],
        traps=[
            ('Vivo aquí desde un año', 'Vivo aquí <strong>desde hace</strong> un año',
             'Con una cantidad de tiempo, siempre se usa <b>desde hace</b>: «desde hace un año». '
             '«Desde» sola va con fechas o eventos: «desde enero», «desde que llegué».'),
            ('Hace tres años que llegué (para decir que sigo aquí)', 'Hace tres años que <strong>vivo</strong> aquí',
             'Si la acción continúa en el presente, el verbo debe estar en <b>presente</b>: '
             '«Hace tres años que <b>vivo</b> aquí». El indefinido indicaría que la acción ya terminó.'),
            ('Vendrá en una hora (= a partir de ahora)', 'Vendrá <strong>dentro de</strong> una hora',
             'Para señalar un momento futuro a partir de ahora, se usa <b>dentro de</b>. '
             '<b>En</b> mide la duración de una tarea completada: «Lo hice <b>en</b> una hora».'),
            ('Llevaba esperando dos horas / llevaba dos horas esperado', 'Llevaba <strong>dos horas esperando</strong>',
             'El orden correcto es: <b>llevaba + periodo de tiempo + gerundio</b>. '
             'El gerundio nunca se sustituye por el participio en esta construcción.'),
            ('A partir de ahora todo cambiará → desde ahora en adelante', '<strong>A partir de ahora</strong> todo cambiará (correcto)',
             '<b>A partir de</b> + punto temporal indica que algo comienza desde ese momento y continúa. '
             'Es correcto; no confundir con «a partir de» en sentido matemático (dividir entre).'),
        ],
        summary=[
            ('Hace + tiempo + que + presente', 'duración hasta ahora (acción sigue)', 'Hace cinco años que trabajo aquí.'),
            ('Hace + tiempo + que + indefinido', 'indica cuándo ocurrió algo (hace X tiempo)', 'Hace tres días que llegó de viaje.'),
            ('Llevaba + tiempo + gerundio', 'duración de acción en el pasado hasta otro punto', 'Llevaba una hora esperando cuando llamó.'),
            ('desde hace + cantidad', 'origen de la acción: periodo de tiempo', 'Estudio español desde hace dos años.'),
            ('desde + fecha/evento', 'origen de la acción: punto concreto', 'Vivo aquí desde enero / desde que me casé.'),
            ('dentro de + tiempo', 'en X tiempo a partir de ahora (futuro)', 'Estará listo dentro de media hora.'),
            ('en + tiempo', 'duración para completar una tarea', 'Terminó el informe en menos de una hora.'),
        ],
        ex1=dict(
            title='Elige la expresión temporal correcta',
            questions=[
                ('Lleva aquí ______ tres años. (cantidad de tiempo, acción continua)',
                 ['desde', 'desde hace', 'hace', 'por'], 1,
                 'Con cantidad de tiempo y acción continua, se usa <b>desde hace</b>: lleva aquí <b>desde hace</b> tres años.'),
                ('______ dos horas que esperamos y el técnico no aparece.',
                 ['Desde', 'Llevamos', 'Hace', 'En'], 2,
                 '<b>Hace</b> + tiempo + que + presente = duración hasta ahora: <b>Hace</b> dos horas que esperamos.'),
                ('El médico ______ media hora hablando con el paciente antes de darle el diagnóstico.',
                 ['hacía', 'había', 'llevaba', 'tenía'], 2,
                 '<b>Llevaba</b> + tiempo + gerundio = duración de acción en el pasado hasta otro punto.'),
                ('La conferencia empezará ______ veinte minutos; aún hay tiempo de tomar un café.',
                 ['en', 'desde hace', 'dentro de', 'hace'], 2,
                 '<b>Dentro de</b> = en X tiempo a partir de ahora: la conferencia empieza <b>dentro de</b> veinte minutos.'),
                ('¿Cuánto tardaste en terminar el examen? — Lo hice ______ dos horas exactas.',
                 ['dentro de', 'desde hace', 'en', 'hace'], 2,
                 '<b>En</b> + tiempo = duración para completar una tarea: lo hice <b>en</b> dos horas.'),
                ('Trabaja en esa empresa ______ que la fundaron, hace más de diez años.',
                 ['desde hace', 'en', 'desde', 'hace'], 2,
                 '<b>Desde</b> + evento / punto concreto: <b>desde</b> que la fundaron.'),
            ]
        ),
        ex2=dict(
            title='Completa con la expresión temporal adecuada',
            questions=[
                ('______ cinco años que no nos vemos; ¡cuánto tiempo!',
                 'Hace', ['Hace'],
                 '<b>Hace</b> + tiempo + que + indefinido = cuándo ocurrió algo (hace X tiempo que no nos vemos).'),
                ('Vivo en este barrio ______ quince años; lo conozco mejor que nadie.',
                 'desde hace', ['desde hace'],
                 'Cantidad de tiempo con acción continua → <b>desde hace</b>: desde hace quince años.'),
                ('______ tres meses estudiando este tema cuando por fin lo entendí.',
                 'Llevaba', ['Llevaba'],
                 '<b>Llevaba</b> + tiempo + gerundio: duración en el pasado hasta el momento de entenderlo.'),
                ('El paquete llegará ______ dos días; ya lo han enviado.',
                 'dentro de', ['dentro de'],
                 '<b>Dentro de</b>: en X tiempo a partir de ahora (futuro): llegará <b>dentro de</b> dos días.'),
                ('Resolvió el acertijo ______ apenas diez minutos; es muy inteligente.',
                 'en', ['en'],
                 '<b>En</b> + tiempo = duración necesaria para completar algo: lo resolvió <b>en</b> diez minutos.'),
            ]
        ),
        ex3=dict(
            title='Identifica el uso temporal correcto',
            questions=[
                ('¿Cuál expresa una acción que comenzó en el pasado y continúa ahora?',
                 ['Hace dos años llegué aquí.',
                  'Hace dos años que vivo aquí.',
                  'Llegué aquí en dos años.',
                  'Vivo aquí dentro de dos años.'], 1,
                 '<b>Hace + tiempo + que + presente</b> = duración hasta ahora (la acción continúa): «Hace dos años que <b>vivo</b> aquí».'),
                ('¿Cuál usa "desde hace" correctamente?',
                 ['Vivo aquí desde un año.',
                  'Vivo aquí desde hace un año.',
                  'Vivo aquí hace un año.',
                  'Vivo aquí en un año.'], 1,
                 'Con cantidad de tiempo y acción continua: <b>desde hace</b> + periodo. «Desde» sola va con fechas.'),
                ('¿Qué significa "Llevaba una hora estudiando cuando sonó el teléfono"?',
                 ['Estudió durante una hora después de que sonó el teléfono.',
                  'Había estado estudiando durante una hora cuando el teléfono interrumpió.',
                  'Estudia una hora todos los días.',
                  'Estudiará una hora más después de la llamada.'], 1,
                 '<b>Llevaba + tiempo + gerundio</b> expresa la duración de una acción pasada hasta el momento de otra.'),
                ('¿Cuál usa "dentro de" correctamente?',
                 ['Lo hice dentro de una hora.',
                  'Llegó dentro de dos días antes.',
                  'El vuelo sale dentro de dos horas.',
                  'Vivimos aquí dentro de tres años.'], 2,
                 '<b>Dentro de</b> señala un momento futuro a partir de ahora: el vuelo sale <b>dentro de</b> dos horas.'),
                ('¿Cuál es la diferencia entre "en" y "dentro de" con expresiones de tiempo?',
                 ['"En" apunta al futuro; "dentro de" mide la duración de una tarea.',
                  '"En" mide cuánto tarda algo en completarse; "dentro de" señala cuándo ocurrirá algo (futuro).',
                  'Son sinónimos intercambiables.',
                  '"En" solo se usa con acciones pasadas; "dentro de", con futuras.'], 1,
                 '<b>En</b> = duración de la tarea: «Lo hice <b>en</b> una hora». <b>Dentro de</b> = punto futuro: «Llegará <b>dentro de</b> una hora».'),
            ]
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            dict(term='hace tres años que vivo aquí', definition='hace + tiempo + que + presente: acción que continúa hasta ahora',
                 example='<b>Hace tres años que vivo</b> en esta ciudad y me encanta.',
                 accept=['hace tres años que vivo', 'hace que vivo']),
            dict(term='desde hace', definition='desde hace + cantidad de tiempo: inicio de acción continua',
                 example='Trabajo en esta empresa <b>desde hace</b> cinco años.',
                 accept=['desde hace']),
            dict(term='llevaba esperando', definition='llevaba + tiempo + gerundio: duración de acción en el pasado',
                 example='<b>Llevaba</b> dos horas <b>esperando</b> cuando por fin llegó el taxi.',
                 accept=['llevaba esperando', 'llevaba horas esperando']),
            dict(term='dentro de', definition='dentro de + tiempo: en X tiempo a partir de ahora (futuro)',
                 example='El resultado se publicará <b>dentro de</b> tres días.',
                 accept=['dentro de']),
            dict(term='en dos horas', definition='en + tiempo: cuánto tardó en completarse una tarea',
                 example='Los bomberos sofocaron el incendio <b>en dos horas</b>.',
                 accept=['en dos horas', 'en una hora', 'en']),
            dict(term='a partir de', definition='a partir de + momento: desde ese punto en adelante',
                 example='<b>A partir de</b> enero, las nuevas normas entran en vigor.',
                 accept=['a partir de']),
            dict(term='a tiempo', definition='a tiempo: sin llegar tarde, puntualmente',
                 example='Conseguimos llegar <b>a tiempo</b> para la última función.',
                 accept=['a tiempo']),
            dict(term='desde que llegué', definition='desde + evento/fecha concreta: punto de inicio',
                 example='No ha llamado <b>desde que llegué</b>; estoy preocupada.',
                 accept=['desde que llegué', 'desde que', 'desde']),
        ],
    ),

    'concordancia-avanzada': dict(
        level='b2',
        section='grammar',
        num='G10',
        short='Concordancia Avanzada',
        title='La Concordancia Nominal y Verbal Avanzada',
        subtitle='Sujetos colectivos, coordinados, participios, cuyo y casos especiales',
        slides=[
            ('Sujetos colectivos: la mayoría de, un grupo de', None,
             '<p class="slide-explanation">Cuando el sujeto es una expresión colectiva seguida de un complemento plural, '
             'el verbo puede ir en singular (concordancia gramatical) o en plural (concordancia por sentido). '
             'El plural es más frecuente en el habla culta:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Sujeto</th>'
             '<th style="padding:8px;text-align:left">Singular (gramatical)</th>'
             '<th style="padding:8px;text-align:left">Plural (por sentido, preferido)</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>La mayoría de los estudiantes</b></td>'
             '<td style="padding:8px">llega puntual</td>'
             '<td style="padding:8px"><b>llegan</b> puntual</td></tr>'
             '<tr><td style="padding:8px"><b>Un grupo de turistas</b></td>'
             '<td style="padding:8px">visita el museo</td>'
             '<td style="padding:8px"><b>visitan</b> el museo</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Parte de los trabajadores</b></td>'
             '<td style="padding:8px">se ha quejado</td>'
             '<td style="padding:8px"><b>se han quejado</b></td></tr>'
             '</table>'
             '<p class="slide-explanation">La norma académica acepta ambas formas. El plural es preferido '
             'cuando el núcleo del sujeto está lejos del verbo.</p>'),

            ('Sujetos coordinados y concordancia por proximidad', None,
             '<p class="slide-explanation">Cuando el sujeto está formado por varios elementos coordinados, '
             'el verbo generalmente va en <b>plural</b>. Sin embargo, existe la <b>concordancia por proximidad</b>:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Concordancia normal:</b> Ana y Luis <b>vinieron</b> a la fiesta. (plural)</p>'
             '<p><b>Concordancia por proximidad:</b> Vino Ana y Luis. (singular, el verbo concuerda con el elemento más cercano)</p>'
             '<p><b>Sujetos en tercera persona:</b> La directora y el secretario <b>firmaron</b> el documento.</p>'
             '</div>'
             '<p class="slide-explanation">La concordancia por proximidad se tolera en la lengua coloquial '
             'cuando el verbo precede a los sujetos, pero la norma formal prefiere el plural.</p>'),

            ('El participio en tiempos compuestos: sin concordancia', None,
             '<p class="slide-explanation">En español moderno, el participio en los tiempos compuestos con <b>haber</b> '
             'es <b>invariable</b>: nunca concuerda con el objeto directo.</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>He comprado las entradas.</b> (no: *he compradas las entradas)</p>'
             '<p><b>Hemos visto las películas.</b> (no: *hemos vistas las películas)</p>'
             '<p><b>Han abierto las ventanas.</b> (no: *han abiertas las ventanas)</p>'
             '</div>'
             '<p class="slide-explanation">Esta regla es absoluta con <b>haber</b>. El participio solo concuerda '
             'cuando funciona como adjetivo (con SER en pasiva o con ESTAR): '
             '«Las ventanas <b>están abiertas</b>».  «Las cartas <b>fueron escritas</b> a mano.»</p>'),

            ('Concordancia del relativo cuyo', None,
             '<p class="slide-explanation"><b>Cuyo/cuya/cuyos/cuyas</b> es un relativo posesivo que concuerda '
             'en género y número con la cosa poseída, no con el poseedor:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Poseedor</th>'
             '<th style="padding:8px;text-align:left">Poseído</th><th style="padding:8px;text-align:left">Cuyo correcto</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">La mujer (fem.)</td>'
             '<td style="padding:8px">el hijo (masc. sg.)</td>'
             '<td style="padding:8px">la mujer <b>cuyo</b> hijo</td></tr>'
             '<tr><td style="padding:8px">El autor (masc.)</td>'
             '<td style="padding:8px">las novelas (fem. pl.)</td>'
             '<td style="padding:8px">el autor <b>cuyas</b> novelas</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Los estudiantes (masc. pl.)</td>'
             '<td style="padding:8px">los trabajos (masc. pl.)</td>'
             '<td style="padding:8px">los estudiantes <b>cuyos</b> trabajos</td></tr>'
             '</table>'
             '<p class="slide-explanation"><b>Cuyo</b> nunca va acompañado de artículo: '
             'no se dice «*el cuyo hijo», sino solo «<b>cuyo</b> hijo».</p>'),

            ('El agua fría: artículo masculino, adjetivo femenino', None,
             '<p class="slide-explanation">En español, los sustantivos femeninos que empiezan por '
             '<b>a-</b> o <b>ha-</b> tónica toman el artículo masculino singular <b>el/un</b> '
             'para evitar el hiato, pero el adjetivo y otros determinantes siguen en <b>femenino</b>:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Sustantivo</th>'
             '<th style="padding:8px;text-align:left">Artículo</th><th style="padding:8px;text-align:left">Adjetivo</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>el agua</b> (fem.)</td>'
             '<td style="padding:8px">el / un</td><td style="padding:8px">fría (fem.)</td>'
             '<td style="padding:8px"><b>el agua fría</b></td></tr>'
             '<tr><td style="padding:8px"><b>el aula</b> (fem.)</td>'
             '<td style="padding:8px">el / un</td><td style="padding:8px">amplia (fem.)</td>'
             '<td style="padding:8px"><b>el aula amplia</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>el hacha</b> (fem.)</td>'
             '<td style="padding:8px">el / un</td><td style="padding:8px">afilada (fem.)</td>'
             '<td style="padding:8px"><b>el hacha afilada</b></td></tr>'
             '</table>'
             '<p class="slide-explanation">En plural, el artículo vuelve a ser femenino: <b>las aguas</b>, <b>las aulas</b>. '
             'Estos sustantivos son siempre <b>femeninos</b>; solo el artículo singular cambia por eufonía.</p>'),
        ],
        traps=[
            ('He compradas las entradas / Hemos vistas las películas', '<strong>He comprado</strong> las entradas / <strong>Hemos visto</strong> las películas',
             'El participio en tiempos compuestos con <b>haber</b> es invariable en español moderno. '
             'Nunca concuerda con el objeto directo.'),
            ('La mujer cuya hijo... / el autor cuyo novelas...', 'la mujer <strong>cuyo</strong> hijo / el autor <strong>cuyas</strong> novelas',
             '<b>Cuyo</b> concuerda con la cosa poseída, no con el poseedor: «hijo» es masc. → <b>cuyo</b>; «novelas» es fem. pl. → <b>cuyas</b>.'),
            ('El agua está fría → el agua está fría (correcto) / el agua está frío', 'El agua está <strong>fría</strong>',
             '«El agua» usa artículo masculino por eufonía, pero es un sustantivo femenino. El adjetivo va en <b>femenino</b>: el agua <b>fría</b>.'),
            ('La mayoría de los alumnos llegó tarde → correcto / incorrecto', 'Las <strong>dos formas son aceptables</strong>; el plural (llegaron) es preferido',
             'Con «la mayoría de + plural», el verbo puede ir en singular o plural. La RAE acepta ambas; '
             'el plural es preferido cuando el complemento es plural y el verbo está lejos del núcleo.'),
            ('El cuyo director / la cuya empresa', '<strong>cuyo</strong> director / <strong>cuya</strong> empresa (sin artículo)',
             '<b>Cuyo</b> nunca se combina con artículo. No se dice «el cuyo» ni «la cuya».'),
        ],
        summary=[
            ('Sujeto colectivo + plural', 'la mayoría de / un grupo de + pl. → verbo en sg. o pl. (pl. preferido)', 'La mayoría de los alumnos llegaron antes de las nueve.'),
            ('Sujeto coordinado', 'A y B → verbo en plural; verbo antes de A y B → sing. posible (proximidad)', 'Ana y Luis firmaron el contrato.'),
            ('Participio con haber', 'invariable: nunca concuerda con el OD', 'He comprado las entradas. (no: *compradas)'),
            ('Cuyo/cuya/cuyos/cuyas', 'concuerda con lo poseído, no con el poseedor', 'La directora cuyas decisiones admiro acaba de renunciar.'),
            ('El agua (fem.)', 'art. masc. sg. por eufonía; adj. y pl. en femenino', 'El agua fría / las aguas frías del río.'),
            ('Adjetivo con dos sustantivos', 'adjetivo pospuesto concuerda con el más cercano o va en masc. pl. si hay m. y f.', 'Un hombre y una mujer italianos llegaron juntos.'),
        ],
        ex1=dict(
            title='Elige la forma de concordancia correcta',
            questions=[
                ('La mayoría de los participantes ______ de acuerdo con la propuesta.',
                 ['estaba', 'estaban', 'Las dos formas son correctas.', 'estamos'], 2,
                 'Con «la mayoría de + plural», son válidas la concordancia singular (estaba) y la plural (estaban). La RAE acepta ambas; el plural es hoy más frecuente.'),
                ('¿Cuál es correcto en tiempos compuestos?',
                 ['He vistas las películas.',
                  'He vista la película.',
                  'He visto las películas.',
                  'He vistos los documentales.'], 2,
                 'El participio con <b>haber</b> es invariable: <b>he visto</b>, independientemente del género y número del OD.'),
                ('La escritora ______ novelas han ganado varios premios acaba de publicar un nuevo libro.',
                 ['cuya', 'cuyo', 'cuyas', 'cuyos'], 2,
                 '<b>Cuyo</b> concuerda con «novelas» (fem. pl.) → <b>cuyas</b>. No importa que la escritora sea femenina.'),
                ('______ agua de este manantial es muy pura.',
                 ['La', 'El', 'Un', 'Las'], 1,
                 'Sustantivo femenino con a- tónica → artículo masculino singular: <b>El</b> agua. Plural: las aguas.'),
                ('Vino ______ la reunión todos los directivos de la empresa.',
                 ['en', 'a', 'para', 'de'], 1,
                 'La expresión «vino a la reunión» usa la preposición <b>a</b> con valor de destino o finalidad.'),
                ('Un hombre y una mujer ______ entraron juntos al edificio.',
                 ['italiano', 'italiana', 'italianas', 'italianos'], 3,
                 'Cuando un adjetivo modifica a dos sustantivos de distinto género, va en <b>masculino plural</b>: <b>italianos</b>.'),
            ]
        ),
        ex2=dict(
            title='Completa con la forma de concordancia adecuada',
            questions=[
                ('La mayoría de los estudiantes ya ______ (entregar) el trabajo a tiempo.',
                 'han entregado', ['han entregado', 'ha entregado'],
                 'Con «la mayoría de + plural», se prefiere el plural: <b>han entregado</b>. El singular también es aceptable.'),
                ('La empresa ______ (cuyo/a/os/as) productos exportamos a veinte países acaba de cumplir cincuenta años.',
                 'cuyos', ['cuyos'],
                 '«Productos» es masculino plural → <b>cuyos</b>. Cuyo concuerda con lo poseído.'),
                ('______ (El/La) hacha estaba ______ (afilado/afilada) y lista para usarse.',
                 'El / afilada', ['El / afilada', 'El hacha estaba afilada'],
                 '«Hacha» comienza por a- tónica → <b>el</b> hacha (art. masc.). Pero es femenino → adj. femenino: <b>afilada</b>.'),
                ('He ______ (escribir) varias cartas esta mañana, pero ninguna me convence del todo.',
                 'escrito', ['escrito'],
                 'Participio con <b>haber</b>: invariable. Siempre <b>escrito</b>, nunca «escritas» ni «escritos».'),
                ('La directora y el secretario ______ (firmar) el acuerdo ayer por la tarde.',
                 'firmaron', ['firmaron'],
                 'Sujeto coordinado (A y B) → verbo en <b>plural</b>: <b>firmaron</b>.'),
            ]
        ),
        ex3=dict(
            title='Identifica la concordancia correcta',
            questions=[
                ('¿Cuál usa correctamente el participio con haber?',
                 ['Hemos abiertos todos los paquetes.',
                  'Han recibidas las cartas.',
                  'He terminado el informe.',
                  'Ha vistos los resultados.'], 2,
                 'El participio con <b>haber</b> es invariable: <b>he terminado</b> (nunca *terminada, *terminados).'),
                ('¿Cuál usa «cuyo» correctamente?',
                 ['El autor el cuyo libro ganó el premio.',
                  'El autor cuyo libro ganó el premio.',
                  'El autor cuya libro ganó el premio.',
                  'El autor cuyos libro ganó el premio.'], 1,
                 '<b>Cuyo</b> + sustantivo masculino singular: <b>cuyo libro</b>. Sin artículo delante de cuyo.'),
                ('¿Qué afirmación sobre «el agua» es correcta?',
                 ['«El agua» es un sustantivo masculino.',
                  '«El agua» es femenino; el artículo masculino se usa por eufonía en singular.',
                  '«El agua» siempre lleva adjetivo masculino.',
                  'El plural es «los aguas».'], 1,
                 '«Agua» es femenino; usa <b>el</b> en singular por eufonía. El adjetivo va en femenino: el agua <b>fría</b>. Plural: <b>las</b> aguas.'),
                ('¿Cuál es la concordancia correcta con sujeto coordinado?',
                 ['Mi hermano y mi hermana llegó tarde.',
                  'Mi hermano y mi hermana llegaron tarde.',
                  'Mi hermano y mi hermana llega tarde.',
                  'Mi hermano y mi hermana llegaste tarde.'], 1,
                 'Sujeto coordinado (A y B) → verbo en <b>plural</b>: <b>llegaron</b>.'),
                ('¿Qué dice la norma sobre «la mayoría de los alumnos llegó/llegaron»?',
                 ['Solo «llegó» es correcto.',
                  'Solo «llegaron» es correcto.',
                  'Ambas formas son aceptables; el plural es preferido.',
                  'Ninguna es correcta; debe decirse «los alumnos llegaron».'], 2,
                 'Con sujetos colectivos + plural, la RAE acepta <b>ambas formas</b>. El plural es hoy más frecuente y preferido.'),
            ]
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            dict(term='he visto', definition='participio con haber: invariable, nunca concuerda con el OD',
                 example='<b>He visto</b> todas las películas de ese director.',
                 accept=['he visto', 'he terminado', 'hemos comprado']),
            dict(term='cuyas novelas', definition='cuyo concuerda con lo poseído (fem. pl.): cuyas + sust. fem. pl.',
                 example='La autora <b>cuyas novelas</b> más admiro acaba de publicar su obra más ambiciosa.',
                 accept=['cuyas novelas', 'cuyas']),
            dict(term='cuyo trabajo', definition='cuyo concuerda con lo poseído (masc. sg.): cuyo + sust. masc. sg.',
                 example='El estudiante <b>cuyo trabajo</b> ganó el concurso es de Bogotá.',
                 accept=['cuyo trabajo', 'cuyo']),
            dict(term='el agua fría', definition='sustantivo femenino con a- tónica: art. masc. sg., adj. femenino',
                 example='Bebieron <b>el agua fría</b> del manantial después de la larga caminata.',
                 accept=['el agua fría', 'el agua']),
            dict(term='llegaron', definition='sujeto coordinado A y B → verbo en plural',
                 example='El director y la secretaria <b>llegaron</b> juntos a la reunión.',
                 accept=['llegaron', 'firmaron', 'vinieron']),
            dict(term='han entregado', definition='la mayoría de + plural → verbo en plural preferido',
                 example='La mayoría de los alumnos <b>han entregado</b> el trabajo antes del plazo.',
                 accept=['han entregado', 'han llegado']),
            dict(term='italianos', definition='adjetivo con sustantivos de distinto género → masculino plural',
                 example='Un hombre y una mujer <b>italianos</b> pidieron información en la oficina de turismo.',
                 accept=['italianos']),
            dict(term='sin artículo: cuyo', definition='cuyo nunca va precedido de artículo',
                 example='El proyecto <b>cuyo</b> presupuesto superó el límite fue cancelado.',
                 accept=['cuyo', 'cuya', 'cuyos', 'cuyas']),
        ],
    ),
}
