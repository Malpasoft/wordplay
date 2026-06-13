# -*- coding: utf-8 -*-
"""espanol/ B1 Gramática — lote 3 (G11–G15)."""

CHAPTERS = {
    'subjuntivo-temporal': dict(
        level='b1',
        section='grammar',
        num='G11',
        short='Subjuntivo Temporal',
        title='El Subjuntivo en Oraciones Temporales',
        subtitle='Cuando, hasta que, antes de que y otras conjunciones temporales con subjuntivo',
        slides=[
            ('Futuro + cuando + subjuntivo', None,
             '<p class="slide-explanation">En español, las oraciones temporales que se refieren al <b>futuro</b> usan '
             '<b>subjuntivo</b>, no indicativo:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Cuando llegues</b>, llámame. (futuro → subjuntivo)</p>'
             '<p><b>Cuando llegaste</b>, te llamé. (pasado → indicativo)</p>'
             '<p><b>Cuando llegues</b>, estaré aquí. (futuro → subj.)</p>'
             '</div>'
             '<p class="slide-explanation">Regla: si la acción todavía no ha ocurrido → <b>subjuntivo</b>. '
             'Si ya ocurrió o es habitual → <b>indicativo</b>.</p>'),

            ('Conjunciones temporales con subjuntivo', None,
             '<p class="slide-explanation">Estas conjunciones temporales usan <b>subjuntivo</b> cuando se refieren al futuro o a hipótesis:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Conjunción</th><th style="padding:8px;text-align:left">Significado</th><th style="padding:8px;text-align:left">Ejemplo (futuro)</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>cuando</b></td><td style="padding:8px">when</td><td style="padding:8px">Cuando <b>llegues</b>, avísame.</td></tr>'
             '<tr><td style="padding:8px"><b>hasta que</b></td><td style="padding:8px">until</td><td style="padding:8px">Espera hasta que <b>termine</b>.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>antes de que</b></td><td style="padding:8px">before</td><td style="padding:8px">Llama antes de que <b>sea</b> tarde.</td></tr>'
             '<tr><td style="padding:8px"><b>en cuanto / tan pronto como</b></td><td style="padding:8px">as soon as</td><td style="padding:8px">En cuanto <b>puedas</b>, ven.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>después de que</b></td><td style="padding:8px">after</td><td style="padding:8px">Hablaremos después de que <b>coman</b>.</td></tr>'
             '<tr><td style="padding:8px"><b>mientras</b></td><td style="padding:8px">while (fut.)</td><td style="padding:8px">Llama mientras <b>estés</b> allí.</td></tr>'
             '</table>'),

            ('Siempre vs. futuro — indicativo vs. subjuntivo', None,
             '<p class="slide-explanation">La misma conjunción puede usarse con indicativo (habitual/pasado) '
             'o subjuntivo (futuro/hipotético). El tiempo verbal determina el modo:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Indicativo (habitual/pasado)</th><th style="padding:8px;text-align:left">Subjuntivo (futuro)</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Cuando <b>llego</b>, como. (hábito)</td><td style="padding:8px">Cuando <b>llegue</b>, comeré. (futuro)</td></tr>'
             '<tr><td style="padding:8px">Cuando <b>llegué</b>, comí. (pasado)</td><td style="padding:8px">En cuanto <b>llegues</b>, avísame.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Espero hasta que <b>llega</b>. (siempre)</td><td style="padding:8px">Espera hasta que <b>llegue</b>.</td></tr>'
             '</table>'),

            ('Antes de que — siempre subjuntivo', None,
             '<p class="slide-explanation"><b>Antes de que</b> usa <b>siempre subjuntivo</b>, independientemente del tiempo de la oración principal, '
             'porque la acción subordinada es anterior (y por tanto no ocurrida desde la perspectiva del hablante):</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>Llama <b>antes de que</b> <u>llegue</u>. (futuro)</p>'
             '<p>Llamó <b>antes de que</b> <u>llegara</u>. (pasado — subj. imperfecto)</p>'
             '<p>Siempre llama <b>antes de que</b> <u>sea</u> tarde. (hábito)</p>'
             '</div>'
             '<p class="slide-explanation">Contrasta: <b>antes de</b> + infinitivo (mismo sujeto): '
             '<i>Llama <b>antes de</b> llegar.</i></p>'),

            ('Después de que — matiz temporal', None,
             '<p class="slide-explanation"><b>Después de que</b> usa subjuntivo para acciones futuras e indicativo para pasadas. '
             'Sin embargo, es más común usar <b>después de</b> + infinitivo (mismo sujeto):</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Estructura</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">después de que + subj. (futuro)</td><td style="padding:8px">Hablaremos después de que <b>termines</b>.</td></tr>'
             '<tr><td style="padding:8px">después de que + indic. (pasado)</td><td style="padding:8px">Hablamos después de que <b>terminaste</b>.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">después de + inf. (mismo sujeto)</td><td style="padding:8px">Hablaré <b>después de</b> terminar.</td></tr>'
             '</table>'),
        ],
        traps=[
            ('Cuando llegarás', '<strong>cuando llegues</strong>', 'Con referencia futura, la oración temporal usa <b>subjuntivo</b>, no futuro. «Cuando llegues» (no: *cuando llegarás).'),
            ('Hasta que llego (futuro)', '<strong>hasta que llegue</strong>', 'Expresando un límite futuro, se usa subjuntivo: <b>hasta que llegue</b>. Indicativo se reserva para hábito o pasado.'),
            ('antes de que llega', '<strong>antes de que llegue</strong>', '<b>Antes de que</b> usa siempre subjuntivo, nunca indicativo.'),
            ('En cuanto puedes, ven (orden para el futuro)', '<strong>en cuanto puedas</strong>', 'La orden/petición hacia el futuro requiere subjuntivo en la temporal: <b>en cuanto puedas</b>.'),
            ('después de que + futuro', '<strong>después de que + subjuntivo</strong>', 'En la temporal futura se usa subjuntivo, no indicativo ni futuro: <i>después de que <b>termines</b></i>.'),
        ],
        summary=[
            ('cuando + futuro', 'subjuntivo', 'Cuando llegues, avísame.'),
            ('hasta que + futuro', 'subjuntivo', 'Espera hasta que termine.'),
            ('antes de que', 'siempre subjuntivo', 'Llama antes de que sea tarde.'),
            ('en cuanto / tan pronto como', 'subjuntivo (futuro)', 'En cuanto puedas, ven.'),
            ('después de que', 'subj. (futuro) / indic. (pasado)', 'Hablaremos después de que termines.'),
            ('mientras + futuro', 'subjuntivo', 'Llámame mientras estés allí.'),
            ('habitual/pasado', 'indicativo', 'Cuando llego, como. / Cuando llegué, comí.'),
        ],
        ex1=dict(
            title='Subjuntivo o indicativo en temporales',
            questions=[
                ('«Cuando _____ (llegar, tú), avísame.»',
                 ['llegues', 'llegas', 'llegarás', 'llegaste'],
                 0, 'Referencia futura → subjuntivo: <b>llegues</b>.'),
                ('«Espera hasta que _____ (terminar, yo).»',
                 ['termine', 'termino', 'terminaré', 'terminé'],
                 0, 'Límite futuro → subjuntivo: <b>termine</b>.'),
                ('«Cuando era niño, siempre _____ (jugar) en el parque.»',
                 ['jugaba', 'juegue', 'jugará', 'jugara'],
                 0, 'Acción habitual en el pasado → indicativo imperfecto: <b>jugaba</b>.'),
                ('«Llama antes de que _____ (ser) tarde.»',
                 ['sea', 'es', 'será', 'fue'],
                 0, '<b>Antes de que</b> siempre usa subjuntivo: <b>sea</b>.'),
                ('«En cuanto _____ (poder, tú), mándame el documento.»',
                 ['puedas', 'puedes', 'podrás', 'pudiste'],
                 0, 'Petición con referencia futura → subjuntivo: <b>puedas</b>.'),
                ('«Después de que _____ (comer, ellos), saldremos.»',
                 ['coman', 'comen', 'comerán', 'comieron'],
                 0, 'Acción futura en oración temporal → subjuntivo: <b>coman</b>.'),
            ]
        ),
        ex2=dict(
            title='Completa con la forma correcta',
            questions=[
                ('Completa: «Mientras _____ (estar, tú) aquí, hablaremos.»',
                 'estés',
                 ['estés', 'estás', 'estarás'],
                 'Oración temporal con referencia a una situación futura → subjuntivo: <b>estés</b>.'),
                ('¿Cuándo se usa indicativo con «cuando»? Da un ejemplo.',
                 'cuando expresa hábito o pasado: Cuando llegué, comí.',
                 ['cuando expresa hábito o pasado', 'cuando llegué comí', 'siempre indicativo'],
                 'Indicativo con <i>cuando</i> = hábito o pasado ya ocurrido.'),
                ('Transforma usando «antes de que»: «Llama. Luego llego yo.»',
                 'Llama antes de que llegue.',
                 ['Llama antes de que llegue.', 'Llama antes de que llegas.', 'Llama antes de llegar.'],
                 '<b>Antes de que</b> + subjuntivo: <b>llegue</b>.'),
                ('Completa: «En cuanto _____ (terminar, él) el trabajo, vendrá.»',
                 'termine',
                 ['termine', 'termina', 'terminará'],
                 'Acción futura → subjuntivo: <b>termine</b>.'),
                ('¿Cuál es la diferencia entre «antes de» y «antes de que»?',
                 'Antes de + infinitivo (mismo sujeto); antes de que + subjuntivo (distinto sujeto)',
                 ['antes de + inf (mismo sujeto); antes de que + subj (distinto sujeto)', 'son iguales', 'antes de siempre subj'],
                 '<b>Antes de</b> + infinitivo cuando el sujeto no cambia. <b>Antes de que</b> + subjuntivo cuando el sujeto es diferente.'),
            ]
        ),
        ex3=dict(
            title='Identificación del modo temporal',
            questions=[
                ('¿Cuál es correcta?',
                 ['Llámame cuando llegues.', 'Llámame cuando llegarás.', 'Llámame cuando llegas.', 'Llámame cuando llegaste.'],
                 0, 'Petición futura → subjuntivo: <b>llegues</b>.'),
                ('«Cuando tengo hambre, como.» ¿Por qué está en indicativo?',
                 ['Porque expresa un hábito general.', 'Porque es futuro.', 'Porque es un error.', 'Porque sigue a «cuando» siempre.'],
                 0, 'Con <i>cuando</i> en presente habitual → <b>indicativo</b>.'),
                ('¿Qué conjunción usa SIEMPRE subjuntivo?',
                 ['antes de que', 'cuando', 'mientras', 'hasta que'],
                 0, '<b>Antes de que</b> siempre exige subjuntivo, incluso con referencia al pasado.'),
                ('«Esperaré hasta que _____.» ¿Cuál es correcta?',
                 ['termines', 'terminarás', 'terminas', 'terminaste'],
                 0, 'Límite futuro con <i>hasta que</i> → subjuntivo: <b>termines</b>.'),
                ('¿Cuál es el modo en «Después de que llegaron, comimos»?',
                 ['indicativo (pasado ya ocurrido)', 'subjuntivo imperfecto', 'indicativo futuro', 'condicional'],
                 0, 'Acción ya ocurrida en el pasado → <b>indicativo</b>.'),
            ]
        ),
        game_desc='Usa el subjuntivo o indicativo con conjunciones temporales según el contexto',
        items=[
            dict(term='cuando + subjuntivo', definition='oración temporal con referencia futura',
                 example='Cuando llegues, avísame.',
                 accept=['cuando subjuntivo', 'cuando llegues']),
            dict(term='hasta que + subjuntivo', definition='límite futuro',
                 example='Espera hasta que termine.',
                 accept=['hasta que subjuntivo', 'hasta que termine']),
            dict(term='antes de que + subjuntivo', definition='siempre subjuntivo (acción anterior)',
                 example='Llama antes de que sea tarde.',
                 accept=['antes de que', 'antes de que subjuntivo']),
            dict(term='en cuanto + subjuntivo', definition='tan pronto como — acción futura',
                 example='En cuanto puedas, ven.',
                 accept=['en cuanto subjuntivo', 'en cuanto puedas']),
            dict(term='mientras + subjuntivo (fut.)', definition='durante el tiempo en que (referencia futura)',
                 example='Llámame mientras estés allí.',
                 accept=['mientras subjuntivo', 'mientras estés']),
            dict(term='cuando + indicativo', definition='hábito o acción pasada ya ocurrida',
                 example='Cuando llegué, comí.',
                 accept=['cuando indicativo', 'cuando llegué']),
            dict(term='después de que + subjuntivo', definition='después de una acción futura',
                 example='Hablaremos después de que termines.',
                 accept=['después de que subjuntivo', 'después de que termines']),
            dict(term='antes de + infinitivo', definition='mismo sujeto — sin cambio de sujeto',
                 example='Llama antes de llegar.',
                 accept=['antes de infinitivo', 'antes de llegar']),
        ]
    ),

    'conectores-discurso': dict(
        level='b1',
        section='grammar',
        num='G12',
        short='Conectores del Discurso',
        title='Los Conectores del Discurso',
        subtitle='Une, contrasta y estructura ideas con sin embargo, además, por lo tanto y más',
        slides=[
            ('¿Qué son los conectores del discurso?', None,
             '<p class="slide-explanation">Los <b>conectores</b> (o marcadores discursivos) son palabras o expresiones '
             'que unen oraciones, párrafos o ideas, señalando la relación lógica entre ellos. '
             'Se dividen en varios tipos según la función.</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Además</b>, necesitamos más tiempo.</p>'
             '<p>Es difícil; <b>sin embargo</b>, lo intentaré.</p>'
             '<p>Estudió mucho; <b>por lo tanto</b>, aprobó.</p>'
             '</div>'),

            ('Conectores de adición y contraste', None,
             '<p class="slide-explanation"><b>Adición</b> (añaden información): <b>además, también, asimismo, igualmente, encima (coloquial)</b><br>'
             '<b>Contraste</b> (contradicen o matizan): <b>pero, sin embargo, no obstante, aunque, a pesar de (que), si bien</b></p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Conector</th><th style="padding:8px;text-align:left">Tipo</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>además</b></td><td style="padding:8px">adición</td><td style="padding:8px">Es barato y, además, cómodo.</td></tr>'
             '<tr><td style="padding:8px"><b>sin embargo</b></td><td style="padding:8px">contraste</td><td style="padding:8px">Es caro; sin embargo, lo compro.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>no obstante</b></td><td style="padding:8px">contraste (formal)</td><td style="padding:8px">No obstante, seguimos adelante.</td></tr>'
             '<tr><td style="padding:8px"><b>aunque</b></td><td style="padding:8px">concesión</td><td style="padding:8px">Aunque llueve, salgo.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>a pesar de (que)</b></td><td style="padding:8px">concesión</td><td style="padding:8px">A pesar del frío, salió.</td></tr>'
             '</table>'),

            ('Conectores causales y consecutivos', None,
             '<p class="slide-explanation"><b>Causales</b> (explican la causa): <b>porque, ya que, puesto que, dado que, como</b><br>'
             '<b>Consecutivos</b> (expresan la consecuencia): <b>por lo tanto, así que, por eso, de modo que, en consecuencia, por consiguiente</b></p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Conector</th><th style="padding:8px;text-align:left">Tipo</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>porque</b></td><td style="padding:8px">causa</td><td style="padding:8px">No fui porque estaba cansado.</td></tr>'
             '<tr><td style="padding:8px"><b>ya que / puesto que</b></td><td style="padding:8px">causa (formal)</td><td style="padding:8px">Ya que estás aquí, ayúdame.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>por lo tanto</b></td><td style="padding:8px">consecuencia</td><td style="padding:8px">Trabajó mucho; por lo tanto, aprobó.</td></tr>'
             '<tr><td style="padding:8px"><b>así que</b></td><td style="padding:8px">consecuencia (coloquial)</td><td style="padding:8px">Es tarde, así que me voy.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>por eso</b></td><td style="padding:8px">consecuencia</td><td style="padding:8px">Estudió; por eso aprobó.</td></tr>'
             '</table>'),

            ('Conectores de orden y reformulación', None,
             '<p class="slide-explanation"><b>Orden/estructuración:</b> primero, en primer lugar, a continuación, luego, después, por último, finalmente<br>'
             '<b>Reformulación/aclaración:</b> es decir, o sea, en otras palabras, esto es<br>'
             '<b>Conclusión:</b> en conclusión, en resumen, en definitiva, para concluir</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>En primer lugar</b>, analizaremos el problema. <b>A continuación</b>, buscaremos soluciones. '
             '<b>Por último</b>, presentaremos las conclusiones.</p>'
             '<p>El proyecto fue difícil; <b>es decir</b>, requirió mucho esfuerzo.</p>'
             '<p><b>En definitiva</b>, fue una experiencia positiva.</p>'
             '</div>'),

            ('Aunque — indicativo vs. subjuntivo', None,
             '<p class="slide-explanation"><b>Aunque</b> puede usarse con indicativo o subjuntivo, con diferente matiz:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Modo</th><th style="padding:8px;text-align:left">Significado</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>aunque + indicativo</b></td><td style="padding:8px">hecho real / admitido</td><td style="padding:8px">Aunque <b>llueve</b>, salgo. (sé que llueve)</td></tr>'
             '<tr><td style="padding:8px"><b>aunque + subjuntivo</b></td><td style="padding:8px">hipotético / irrelevante</td><td style="padding:8px">Aunque <b>llueva</b>, salgo. (no importa si llueve o no)</td></tr>'
             '</table>'
             '<p class="slide-explanation">Con indicativo, el hablante <b>reconoce el hecho</b>. '
             'Con subjuntivo, lo presenta como <b>indiferente o hipotético</b>.</p>'),
        ],
        traps=[
            ('sin embargo va al principio siempre', 'puede ir entre comas en el medio', '<b>Sin embargo</b> puede aparecer al inicio (<i>Sin embargo, no lo hizo</i>) o en posición media con comas (<i>No lo hizo, sin embargo, a tiempo</i>).'),
            ('porque / por eso', 'porque = causa; por eso = consecuencia', '<b>Porque</b> introduce la causa: <i>No fui porque llovía</i>. <b>Por eso</b> introduce la consecuencia: <i>Llovía; por eso no fui</i>.'),
            ('aunque llueve / aunque llueva', 'depende del matiz', '<b>Aunque llueve</b> = hecho real admitido. <b>Aunque llueva</b> = hipotético o indiferente. Ambos son correctos según el contexto.'),
            ('*pero sin embargo', 'sin embargo (solo)', '<b>Sin embargo</b> ya incluye el valor adversativo de <i>pero</i>. No se usan juntos: *<i>pero sin embargo</i> es redundante.'),
            ('ya que al principio de oración independiente', 'ya que introduce subordinada causal', '<b>Ya que</b> introduce la causa y va en la oración subordinada: <i>Ya que estás aquí, ayúdame</i>. No inicia una oración autónoma.'),
        ],
        summary=[
            ('Adición', 'además, también, asimismo', 'Es útil y, además, gratuito.'),
            ('Contraste', 'sin embargo, no obstante, pero', 'Es difícil; sin embargo, posible.'),
            ('Concesión', 'aunque, a pesar de (que), si bien', 'Aunque llueve, salgo.'),
            ('Causa', 'porque, ya que, puesto que, dado que', 'No fui porque estaba cansado.'),
            ('Consecuencia', 'por lo tanto, así que, por eso', 'Estudió; por eso aprobó.'),
            ('Orden', 'primero, a continuación, finalmente', 'Primero, analiza el texto.'),
            ('Reformulación', 'es decir, o sea, en otras palabras', 'Es tarde; es decir, debemos irnos.'),
        ],
        ex1=dict(
            title='Elige el conector correcto',
            questions=[
                ('Estudió mucho; _____, aprobó el examen.',
                 ['por lo tanto', 'sin embargo', 'aunque', 'a pesar de'],
                 0, 'Relación de consecuencia → <b>por lo tanto</b>.'),
                ('Es caro; _____, lo compré porque me encantó.',
                 ['sin embargo', 'además', 'ya que', 'por eso'],
                 0, 'Contraste entre precio alto y decisión de comprar → <b>sin embargo</b>.'),
                ('No fui a la fiesta _____ estaba cansado.',
                 ['porque', 'por lo tanto', 'sin embargo', 'además'],
                 0, 'La causa de no ir → <b>porque</b>.'),
                ('_____ estás aquí, podrías ayudarme un momento.',
                 ['Ya que', 'Sin embargo', 'Además', 'Por lo tanto'],
                 0, 'Causa que justifica la petición → <b>ya que</b>.'),
                ('El viaje fue agotador; _____, nos lo pasamos muy bien.',
                 ['sin embargo', 'por lo tanto', 'ya que', 'además'],
                 0, 'Contraste entre agotamiento y disfrute → <b>sin embargo</b>.'),
                ('_____ el frío, decidieron salir a pasear.',
                 ['A pesar de', 'Porque', 'Por lo tanto', 'Sin embargo'],
                 0, 'Concesión ante un obstáculo → <b>a pesar de</b>.'),
            ]
        ),
        ex2=dict(
            title='Conecta las oraciones con el conector adecuado',
            questions=[
                ('Une con un conector consecutivo: «Llovió mucho. No pudimos salir.»',
                 'Llovió mucho; por eso / así que / por lo tanto no pudimos salir.',
                 ['por eso', 'por lo tanto', 'así que'],
                 'Consecuencia: <b>por eso</b> / <b>así que</b> / <b>por lo tanto</b>.'),
                ('Une con un conector de adición: «Es inteligente. Trabaja duro.»',
                 'Es inteligente y, además, trabaja duro.',
                 ['además', 'también', 'asimismo'],
                 'Adición de cualidades → <b>además</b> / <b>también</b>.'),
                ('¿Cuándo usas «aunque» + indicativo vs. subjuntivo? Da un ejemplo de cada uno.',
                 'Indicativo = hecho real: «Aunque llueve, salgo.» Subjuntivo = hipotético: «Aunque llueva, saldré.»',
                 ['indicativo hecho real; subjuntivo hipotético', 'aunque llueve aunque llueva'],
                 'Indicativo = admitido como real. Subjuntivo = hipotético o indiferente.'),
                ('Reforma con «es decir»: «El texto es ambiguo. Tiene más de un significado.»',
                 'El texto es ambiguo; es decir, tiene más de un significado.',
                 ['es decir', 'o sea', 'esto es'],
                 'Reformulación/aclaración → <b>es decir</b>.'),
                ('¿Cuál es la diferencia entre «pero» y «sin embargo»?',
                 'Ambos expresan contraste; sin embargo es más formal y puede ir entre comas en posición media.',
                 ['sin embargo es más formal y puede ir en posición media', 'son idénticos', 'pero es formal'],
                 '<b>Sin embargo</b> es más formal y más flexible en posición (inicio o medio).'),
            ]
        ),
        ex3=dict(
            title='Identificación de conectores',
            questions=[
                ('¿Qué tipo de conector es «por consiguiente»?',
                 ['Consecutivo', 'Causal', 'Concesivo', 'De adición'],
                 0, '<b>Por consiguiente</b> introduce una consecuencia → <b>consecutivo</b>.'),
                ('«A pesar de que llovía, salieron.» ¿Qué relación expresa?',
                 ['Concesión', 'Causa', 'Consecuencia', 'Adición'],
                 0, '<b>A pesar de que</b> = concesión (obstáculo que no impide la acción).'),
                ('¿Cuál NO es un conector de orden?',
                 ['por eso', 'en primer lugar', 'a continuación', 'finalmente'],
                 0, '<b>Por eso</b> es consecutivo, no de orden. Los demás estructuran el discurso en secuencia.'),
                ('«Ya que no tienes tiempo, lo haré yo.» ¿Qué tipo es «ya que»?',
                 ['Causal', 'Consecutivo', 'Concesivo', 'Adversativo'],
                 0, '<b>Ya que</b> introduce la causa → <b>causal</b>.'),
                ('¿Qué conector reformula o aclara una idea?',
                 ['es decir', 'sin embargo', 'por lo tanto', 'además'],
                 0, '<b>Es decir</b> introduce una reformulación o aclaración de lo dicho.'),
            ]
        ),
        game_desc='Conecta ideas con los marcadores discursivos correctos según la relación lógica',
        items=[
            dict(term='además', definition='conector de adición',
                 example='Es útil y, además, gratuito.',
                 accept=['ademas', 'además', 'adición']),
            dict(term='sin embargo', definition='conector de contraste (semiformal)',
                 example='Es caro; sin embargo, lo compré.',
                 accept=['sin embargo', 'contraste']),
            dict(term='aunque + indicativo', definition='concesión con hecho real',
                 example='Aunque llueve, salgo.',
                 accept=['aunque indicativo', 'aunque llueve']),
            dict(term='aunque + subjuntivo', definition='concesión hipotética o indiferente',
                 example='Aunque llueva, saldré.',
                 accept=['aunque subjuntivo', 'aunque llueva']),
            dict(term='porque', definition='conector causal',
                 example='No fui porque estaba cansado.',
                 accept=['porque', 'causal']),
            dict(term='por lo tanto', definition='conector consecutivo',
                 example='Estudió; por lo tanto, aprobó.',
                 accept=['por lo tanto', 'consecutivo', 'por tanto']),
            dict(term='ya que / puesto que', definition='causales formales',
                 example='Ya que estás aquí, ayúdame.',
                 accept=['ya que', 'puesto que', 'causal formal']),
            dict(term='es decir', definition='reformulación o aclaración',
                 example='Es complejo; es decir, requiere estudio.',
                 accept=['es decir', 'reformulacion', 'reformulación']),
        ]
    ),

    'lo-neutro': dict(
        level='b1',
        section='grammar',
        num='G13',
        short='Lo Neutro',
        title='El Artículo Neutro LO',
        subtitle='Lo + adjetivo, lo que y otras estructuras con lo neutro',
        slides=[
            ('¿Qué es el artículo neutro LO?', None,
             '<p class="slide-explanation"><b>Lo</b> es el artículo neutro en español. No tiene género ni número. '
             'Se usa para nominalizar conceptos abstractos o para referirse a algo sin especificar un sustantivo concreto:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Lo importante</b> es intentarlo. (the important thing)</p>'
             '<p><b>Lo bueno</b> de vivir aquí es el clima. (the good thing)</p>'
             '<p>No entiendo <b>lo que</b> dices. (what you say)</p>'
             '</div>'),

            ('LO + adjetivo', None,
             '<p class="slide-explanation"><b>Lo + adjetivo</b> convierte el adjetivo en un sustantivo neutro abstracto '
             '(sin modificar en género ni número). Equivale a «the ___ thing/part»:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Estructura</th><th style="padding:8px;text-align:left">Significado</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>lo + adj</b></td><td style="padding:8px">the ___ thing/aspect</td><td style="padding:8px">Lo difícil es comenzar.</td></tr>'
             '<tr><td style="padding:8px"><b>lo mejor</b></td><td style="padding:8px">the best (thing)</td><td style="padding:8px">Lo mejor es descansar.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>lo peor</b></td><td style="padding:8px">the worst (thing)</td><td style="padding:8px">Lo peor fue el tráfico.</td></tr>'
             '<tr><td style="padding:8px"><b>lo mismo</b></td><td style="padding:8px">the same (thing)</td><td style="padding:8px">Dijo lo mismo de siempre.</td></tr>'
             '</table>'),

            ('LO + adverbio', None,
             '<p class="slide-explanation"><b>Lo + adverbio</b> se usa en exclamaciones e intensificaciones:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>¡<b>Lo bien</b> que cocina! (how well she cooks!)</p>'
             '<p>¡<b>Lo rápido</b> que corre! (how fast he runs!)</p>'
             '<p>Me sorprende <b>lo tarde</b> que es. (how late it is)</p>'
             '</div>'
             '<p class="slide-explanation">Esta estructura es muy común en exclamaciones o subordinadas que expresan asombro. '
             'El adjetivo/adverbio permanece invariable:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>¡<b>Lo guapa</b> que está! / ¡<b>Lo guapos</b> que están! (el adjetivo concuerda aquí en función atributiva)</p>'
             '</div>'),

            ('LO QUE — pronombre relativo neutro', None,
             '<p class="slide-explanation"><b>Lo que</b> funciona como pronombre relativo neutro: se refiere a algo sin antecedente específico o a una idea completa. '
             'Equivale a «what», «that which», «the thing that»:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>No entiendo <b>lo que</b> dices. (I don\'t understand what you say.)</p>'
             '<p><b>Lo que</b> más me gusta es el café. (What I like most is coffee.)</p>'
             '<p>Haz <b>lo que</b> quieras. (Do what(ever) you want.)</p>'
             '<p>Eso es <b>lo que</b> pensaba. (That\'s what I thought.)</p>'
             '</div>'),

            ('LO DE y otras estructuras con LO', None,
             '<p class="slide-explanation"><b>Lo de</b> introduce una referencia a algo conocido entre hablante y oyente:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Lo de</b> ayer fue un malentendido. (That thing yesterday was a misunderstanding.)</p>'
             '<p>¿Resolviste <b>lo de</b> tu contrato? (Did you sort out that thing with your contract?)</p>'
             '</div>'
             '<p class="slide-explanation">Otras estructuras frecuentes:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Estructura</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>a lo + adj/sust</b> (a la manera de)</td><td style="padding:8px">Vive a lo grande. / Cocina a lo italiano.</td></tr>'
             '<tr><td style="padding:8px"><b>por lo + adj</b></td><td style="padding:8px">Vamos a salir, por lo menos, a las ocho.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>en lo que</b> (while)</td><td style="padding:8px">Prepara el café en lo que termino.</td></tr>'
             '</table>'),
        ],
        traps=[
            ('*lo importante está bien', '<strong>lo importante es/está bien</strong>', 'El verbo que sigue a <b>lo + adj</b> como sujeto va en singular: <i>lo importante <b>es</b> intentarlo</i>.'),
            ('*el lo que dices', '<strong>lo que dices</strong>', '<b>Lo que</b> no lleva artículo adicional. Es el pronombre relativo neutro completo.'),
            ('confundir lo (OD) con lo (neutro)', 'contexto diferente', '<b>Lo</b> como OD: <i>¿Lo ves? (el coche)</i>. <b>Lo</b> neutro: <i>Lo difícil es comenzar</i>. Son usos distintos.'),
            ('*lo que mejor me gusta', '<strong>lo que más me gusta</strong>', 'Con superlativo en construcciones de lo que, se usa <b>lo que más/menos</b>: <i>lo que más me gusta</i>.'),
            ('lo guapa vs. lo guapos', 'lo + adj de exclamación concuerda', 'En exclamaciones «¡lo + adj + que!», el adjetivo concuerda con el sustantivo al que se refiere: <i>¡lo guapa que está ella!</i> / <i>¡lo guapos que están ellos!</i>'),
        ],
        summary=[
            ('lo + adjetivo', 'the ___ thing/aspect (abstracto)', 'Lo importante es participar.'),
            ('lo mejor / lo peor', 'superlativo neutro', 'Lo mejor fue el viaje.'),
            ('lo + adv / adj (exclamación)', '¡lo + adj/adv + que!', '¡Lo bien que canta!'),
            ('lo que', 'pronombre relativo neutro (what/that which)', 'Haz lo que quieras.'),
            ('lo de', 'referencia a algo conocido entre hablantes', 'Lo de ayer fue raro.'),
            ('a lo + adj', 'a la manera de', 'Vive a lo grande.'),
            ('por lo + adj', 'locutor modal/adverbial', 'Por lo menos, descansa.'),
        ],
        ex1=dict(
            title='LO neutro: elige la opción correcta',
            questions=[
                ('_____ difícil es empezar.',
                 ['Lo', 'El', 'La', 'Los'],
                 0, 'Artículo neutro <b>lo</b> + adjetivo para expresar un concepto abstracto.'),
                ('No entiendo _____ me estás diciendo.',
                 ['lo que', 'el que', 'la que', 'que'],
                 0, 'Pronombre relativo neutro → <b>lo que</b>.'),
                ('¡ _____ bien que cocina tu madre!',
                 ['Lo', 'Qué', 'El', 'Tan'],
                 0, 'Exclamación con <b>lo + adv + que</b>: <b>Lo bien que…</b>'),
                ('¿Resolviste _____ del trabajo?',
                 ['lo de', 'lo que', 'el de', 'la de'],
                 0, 'Referencia a algo conocido → <b>lo de</b>.'),
                ('Haz _____ quieras.',
                 ['lo que', 'que', 'el que', 'lo cual'],
                 0, '<b>Lo que</b> = pronombre relativo neutro sin antecedente específico.'),
                ('_____ mejor sería descansar un poco.',
                 ['Lo', 'El', 'La', 'Eso'],
                 0, 'Superlativo neutro → <b>lo mejor</b>.'),
            ]
        ),
        ex2=dict(
            title='Completa con lo/lo que/lo de',
            questions=[
                ('Completa: «_____ importante es intentarlo.»',
                 'Lo',
                 ['Lo', 'El', 'La'],
                 '<b>Lo</b> + adj neutro: <b>lo importante</b>.'),
                ('Traduce: «That\'s what I thought.»',
                 'Eso es lo que pensaba.',
                 ['Eso es lo que pensaba.', 'Eso es el que pensaba.', 'Lo que es eso.'],
                 'Pronombre relativo neutro: <b>lo que</b>.'),
                ('¿Qué expresa «a lo grande»?',
                 'De manera espléndida / a gran escala (a la manera de lo grande)',
                 ['de manera espléndida', 'lo grande', 'grandioso'],
                 '<b>A lo + adj/sust</b> = a la manera de: <i>vivir a lo grande</i>.'),
                ('Completa: «¡_____ rápido que corre!»',
                 'Lo',
                 ['Lo', 'Qué', 'El'],
                 'Exclamación → <b>lo + adj/adv + que</b>: <b>lo rápido que corre</b>.'),
                ('¿Cuál es la diferencia entre «lo que dices» y «lo cual dices»?',
                 'Lo que = pronombre relativo neutro libre; lo cual = relativo con antecedente explícito previo',
                 ['lo que libre; lo cual con antecedente', 'son iguales', 'lo cual es coloquial'],
                 '<b>Lo que</b> puede aparecer sin antecedente claro. <b>Lo cual</b> retoma un antecedente ya mencionado.'),
            ]
        ),
        ex3=dict(
            title='Lo neutro — aplicación',
            questions=[
                ('¿Qué función tiene «lo» en «Lo difícil es comenzar»?',
                 ['Artículo neutro que nominaliza el adjetivo', 'Pronombre OD', 'Adverbio', 'Conector'],
                 0, '<b>Lo + adj</b> = artículo neutro que convierte el adjetivo en un sustantivo abstracto.'),
                ('¿Cuál es correcta?',
                 ['Lo que me gusta es el café.', 'El que me gusta es el café.', 'La que me gusta es el café.', 'Que me gusta es el café.'],
                 0, 'Pronombre relativo neutro sin antecedente específico → <b>lo que</b>.'),
                ('«¡Lo guapas que están!» ¿Concuerda el adjetivo?',
                 ['Sí, el adjetivo concuerda con el referente.', 'No, siempre va en masculino.', 'No, siempre va en singular.', 'Sí, pero es incorrecto.'],
                 0, 'En exclamaciones <b>lo + adj + que</b>, el adjetivo concuerda con el referente: <i>lo guapas que están ellas</i>.'),
                ('¿Qué significa «lo de ayer»?',
                 ['Aquella cosa/situación de ayer (conocida por ambos hablantes)', 'Lo que ocurrirá ayer', 'El día de ayer', 'Ayer mismo'],
                 0, '<b>Lo de</b> + tiempo/persona/tema = referencia a algo conocido por los interlocutores.'),
                ('¿Cuál equivale a «what»?',
                 ['lo que', 'lo de', 'lo cual', 'lo mismo'],
                 0, '<b>Lo que</b> = «what» como pronombre relativo neutro.'),
            ]
        ),
        game_desc='Usa lo + adjetivo, lo que y lo de para expresar conceptos neutros y abstractos',
        items=[
            dict(term='lo + adjetivo', definition='nominalización neutra abstracta',
                 example='Lo importante es participar.',
                 accept=['lo adjetivo', 'lo importante', 'artículo neutro']),
            dict(term='lo mejor / lo peor', definition='superlativo neutro',
                 example='Lo mejor fue el viaje.',
                 accept=['lo mejor', 'lo peor', 'superlativo neutro']),
            dict(term='lo que', definition='pronombre relativo neutro (what / that which)',
                 example='Haz lo que quieras.',
                 accept=['lo que', 'pronombre relativo neutro']),
            dict(term='¡lo + adj + que!', definition='exclamación de intensidad',
                 example='¡Lo bien que canta!',
                 accept=['lo que exclamación', 'exclamación neutro', 'lo bien que']),
            dict(term='lo de', definition='referencia a algo conocido entre hablantes',
                 example='Lo de ayer fue raro.',
                 accept=['lo de', 'referencia conocida']),
            dict(term='lo mismo', definition='la misma cosa (referencia neutra)',
                 example='Dijo lo mismo de siempre.',
                 accept=['lo mismo']),
            dict(term='a lo grande', definition='de manera espléndida (a lo + adj/sust)',
                 example='Viven a lo grande.',
                 accept=['a lo grande', 'a lo adj']),
            dict(term='lo cual', definition='relativo formal que retoma antecedente previo',
                 example='Llegó tarde, lo cual me sorprendió.',
                 accept=['lo cual', 'relativo formal']),
        ]
    ),

    'verbos-cambio': dict(
        level='b1',
        section='grammar',
        num='G14',
        short='Verbos de Cambio',
        title='Los Verbos de Cambio',
        subtitle='Volverse, ponerse, quedarse, hacerse y llegar a ser: expresa transformaciones',
        slides=[
            ('¿Qué son los verbos de cambio?', None,
             '<p class="slide-explanation">Los <b>verbos de cambio</b> expresan una transformación o transición. '
             'En español, la elección del verbo depende del <b>tipo de cambio</b> (rápido/lento, permanente/temporal, '
             'voluntario/involuntario):</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>ponerse</b> — cambio de estado temporal / emocional</p>'
             '<p><b>volverse</b> — cambio profundo de carácter</p>'
             '<p><b>quedarse</b> — resultado de un proceso (a menudo involuntario)</p>'
             '<p><b>hacerse</b> — cambio gradual, voluntario / profesión / ideología</p>'
             '<p><b>llegar a ser</b> — logro tras esfuerzo</p>'
             '</div>'),

            ('PONERSE + adjetivo', None,
             '<p class="slide-explanation"><b>Ponerse + adjetivo</b>: cambio de estado <b>temporal</b>, generalmente emocional o físico. '
             'El cambio es rápido y a menudo una reacción:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Expresión</th><th style="padding:8px;text-align:left">Significado</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>ponerse nervioso/a</b></td><td style="padding:8px">to get nervous</td></tr>'
             '<tr><td style="padding:8px"><b>ponerse triste</b></td><td style="padding:8px">to become sad</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>ponerse enfermo/a</b></td><td style="padding:8px">to fall ill</td></tr>'
             '<tr><td style="padding:8px"><b>ponerse rojo/a</b></td><td style="padding:8px">to blush / turn red</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>ponerse de mal humor</b></td><td style="padding:8px">to get in a bad mood</td></tr>'
             '</table>'
             '<p class="slide-explanation">Uso: emociones y cambios físicos visibles y temporales.</p>'),

            ('VOLVERSE + adjetivo/sustantivo', None,
             '<p class="slide-explanation"><b>Volverse</b>: cambio <b>profundo e involuntario</b> en el carácter o personalidad. '
             'Generalmente negativo o sorprendente:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>Se <b>volvió</b> muy agresivo después del accidente.</p>'
             '<p>Con los años se <b>volvió</b> más paciente.</p>'
             '<p>La situación se <b>volvió</b> insoportable.</p>'
             '</div>'
             '<p class="slide-explanation">Con colores o estados físicos temporales se usa <b>ponerse</b>, no <b>volverse</b>.</p>'),

            ('QUEDARSE + adjetivo/participio', None,
             '<p class="slide-explanation"><b>Quedarse</b>: resultado de un proceso, a menudo <b>permanente o involuntario</b>. '
             'Indica un estado resultante:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Expresión</th><th style="padding:8px;text-align:left">Significado</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>quedarse sorprendido/a</b></td><td style="padding:8px">to be left surprised</td></tr>'
             '<tr><td style="padding:8px"><b>quedarse dormido/a</b></td><td style="padding:8px">to fall asleep</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>quedarse ciego/a</b></td><td style="padding:8px">to go blind</td></tr>'
             '<tr><td style="padding:8px"><b>quedarse solo/a</b></td><td style="padding:8px">to end up alone</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>quedarse sin trabajo</b></td><td style="padding:8px">to end up jobless</td></tr>'
             '</table>'),

            ('HACERSE y LLEGAR A SER', None,
             '<p class="slide-explanation"><b>Hacerse + sustantivo/adjetivo</b>: cambio <b>gradual y voluntario</b> — '
             'religión, ideología, profesión:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>Se <b>hizo</b> médico/vegetariano/rico.</p>'
             '<p>Se <b>hizo</b> famoso con el tiempo.</p>'
             '</div>'
             '<p class="slide-explanation"><b>Llegar a ser</b>: logro alcanzado tras <b>esfuerzo y tiempo</b>:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Llegó a ser</b> directora de la empresa.</p>'
             '<p><b>Llegó a ser</b> una gran artista.</p>'
             '</div>'
             '<p class="slide-explanation">Diferencia clave: <i>hacerse</i> pone énfasis en el proceso voluntario; '
             '<i>llegar a ser</i> destaca el logro final.</p>'),
        ],
        traps=[
            ('*Se volvió rojo de vergüenza', '<strong>Se puso rojo de vergüenza</strong>', '<b>Ponerse</b> se usa para cambios físicos visibles y temporales como los colores o estados emocionales repentinos. <b>Volverse</b> es para cambios de personalidad/carácter.'),
            ('*Se puso médico', '<strong>Se hizo médico</strong>', 'Para cambios de profesión, ideología o religión (graduales y voluntarios) se usa <b>hacerse</b>.'),
            ('*Se quedó muy nervioso en la reunión', '<strong>Se puso muy nervioso</strong>', 'Reacción emocional repentina → <b>ponerse</b>. <b>Quedarse</b> implica un estado resultante más permanente o involuntario.'),
            ('*Llegó a ser nervioso', '<strong>Se puso / se volvió nervioso</strong>', '<b>Llegar a ser</b> se usa para logros o cambios positivos tras esfuerzo, no para estados emocionales.'),
            ('*Se hizo dormido', '<strong>Se quedó dormido</strong>', '<b>Quedarse dormido</b> es la expresión fija. <b>Hacerse</b> no se usa con participios de este tipo.'),
        ],
        summary=[
            ('ponerse + adj', 'cambio emocional/físico temporal y repentino', 'Se puso nervioso antes del examen.'),
            ('volverse + adj/sust', 'cambio profundo de carácter (involuntario)', 'Se volvió muy introvertido.'),
            ('quedarse + adj/participio', 'estado resultante, a menudo permanente', 'Se quedó dormido en el sofá.'),
            ('hacerse + sust/adj', 'cambio gradual y voluntario (profesión/ideología)', 'Se hizo vegetariana el año pasado.'),
            ('llegar a ser', 'logro alcanzado con esfuerzo', 'Llegó a ser presidente de la empresa.'),
            ('convertirse en', 'transformación total (también voluntaria)', 'Se convirtió en la mejor del equipo.'),
            ('resultar + adj', 'resultado de una evaluación', 'La experiencia resultó muy útil.'),
        ],
        ex1=dict(
            title='Verbos de cambio: elige la opción correcta',
            questions=[
                ('Cuando recibió la mala noticia, _____ muy triste.',
                 ['se puso', 'se volvió', 'se quedó', 'se hizo'],
                 0, 'Reacción emocional repentina → <b>ponerse</b>: <b>se puso</b> triste.'),
                ('Después de años de práctica, _____ un experto en su campo.',
                 ['llegó a ser', 'se puso', 'se quedó', 'se volvió'],
                 0, 'Logro tras esfuerzo prolongado → <b>llegar a ser</b>: <b>llegó a ser</b>.'),
                ('Con los años, _____ muy desconfiado — antes era abierto y simpático.',
                 ['se volvió', 'se puso', 'se quedó', 'se hizo'],
                 0, 'Cambio profundo de carácter → <b>volverse</b>: <b>se volvió</b>.'),
                ('_____ médica después de estudiar durante diez años.',
                 ['Se hizo', 'Se puso', 'Se quedó', 'Se volvió'],
                 0, 'Cambio gradual y voluntario de profesión → <b>hacerse</b>: <b>se hizo</b>.'),
                ('Durante la reunión, _____ dormido sin darse cuenta.',
                 ['se quedó', 'se puso', 'se hizo', 'llegó a ser'],
                 0, 'Estado resultante involuntario → <b>quedarse</b>: <b>se quedó</b>.'),
                ('La película _____ muy aburrida a partir de la mitad.',
                 ['se volvió', 'se puso', 'se quedó', 'llegó a ser'],
                 0, 'Cambio de cualidad de algo (no emocional en persona) → <b>volverse</b>: <b>se volvió</b>.'),
            ]
        ),
        ex2=dict(
            title='Distingue los verbos de cambio',
            questions=[
                ('¿Cuál es la diferencia entre «ponerse nervioso» y «volverse nervioso»?',
                 'Ponerse = cambio repentino/temporal; volverse = cambio profundo y más permanente de carácter',
                 ['ponerse repentino/temporal; volverse profundo y permanente', 'son iguales', 'volverse es más frecuente'],
                 '<b>Ponerse</b> = reacción inmediata. <b>Volverse</b> = cambio de carácter que dura.'),
                ('Usa «quedarse» en una oración que exprese un resultado involuntario.',
                 'Se quedó sin trabajo. / Se quedó ciego. / Se quedó dormido.',
                 ['se quedó sin trabajo', 'se quedó ciego', 'se quedó dormido'],
                 '<b>Quedarse</b> + adj/participio = resultado no buscado, a menudo permanente o indeseado.'),
                ('¿Cuándo usarías «llegar a ser» en vez de «hacerse»?',
                 'Cuando quieres enfatizar el esfuerzo o el logro: «Llegó a ser directora» (énfasis en el logro).',
                 ['cuando enfatizas el logro tras esfuerzo', 'cuando el cambio es rápido', 'cuando es negativo'],
                 '<b>Llegar a ser</b> destaca la meta alcanzada. <b>Hacerse</b> se centra en el proceso voluntario.'),
                ('¿«Se convirtió en»? ¿Cuándo se usa?',
                 'Para una transformación total o profunda, a menudo dramática: se convirtió en una estrella.',
                 ['transformación total o dramática', 'cambio físico', 'estado emocional'],
                 '<b>Convertirse en</b> = transformación completa, frecuentemente con sustantivo.'),
                ('¿Es correcto «se puso médico»?',
                 'No; lo correcto es «se hizo médico» (hacerse = cambio de profesión voluntario y gradual).',
                 ['no; se hizo médico', 'sí, es correcto', 'sí en coloquial'],
                 'Con profesiones usamos <b>hacerse</b>: <i>se hizo médico</i>.'),
            ]
        ),
        ex3=dict(
            title='Verbos de cambio en contexto',
            questions=[
                ('¿Cuál es correcto para un cambio físico repentino?',
                 ['Se puso rojo.', 'Se volvió rojo.', 'Se quedó rojo.', 'Se hizo rojo.'],
                 0, '<b>Ponerse</b> = cambio físico repentino y temporal: <b>se puso rojo</b>.'),
                ('«Se quedó sorprendida.» ¿Qué implica?',
                 ['Quedó en estado de sorpresa como resultado de algo.', 'Decidió sorprenderse.', 'Se sorprendió voluntariamente.', 'Fue un cambio de carácter.'],
                 0, '<b>Quedarse</b> = resultado de un proceso, a menudo involuntario.'),
                ('¿Cuál NO usa «hacerse»?',
                 ['Se hizo dormido.', 'Se hizo vegetariana.', 'Se hizo rico.', 'Se hizo famoso.'],
                 0, 'La expresión correcta es <b>quedarse dormido</b>. <b>Hacerse</b> no funciona con participios de este tipo.'),
                ('Para un cambio de ideología (de conservador a progresista), ¿qué verbo es más adecuado?',
                 ['hacerse', 'ponerse', 'quedarse', 'volverse'],
                 0, 'Cambio ideológico voluntario y gradual → <b>hacerse</b>.'),
                ('«Con el tiempo llegó a ser una referencia en su campo.» ¿Qué implica esto?',
                 ['Logró ese estatus tras años de esfuerzo.', 'El cambio fue repentino.', 'Fue un cambio involuntario.', 'Cambió de profesión.'],
                 0, '<b>Llegar a ser</b> implica un logro alcanzado con tiempo y esfuerzo.'),
            ]
        ),
        game_desc='Elige el verbo de cambio correcto según el tipo de transformación',
        items=[
            dict(term='ponerse + adj', definition='cambio emocional/físico repentino y temporal',
                 example='Se puso nervioso antes del examen.',
                 accept=['ponerse', 'se puso', 'cambio temporal']),
            dict(term='volverse + adj', definition='cambio profundo de carácter (involuntario)',
                 example='Con los años se volvió más serio.',
                 accept=['volverse', 'se volvió', 'cambio carácter']),
            dict(term='quedarse + adj/participio', definition='estado resultante, frecuentemente involuntario',
                 example='Se quedó dormido en el sofá.',
                 accept=['quedarse', 'se quedó', 'estado resultante']),
            dict(term='hacerse + sust/adj', definition='cambio gradual y voluntario',
                 example='Se hizo médica después de muchos años.',
                 accept=['hacerse', 'se hizo', 'cambio voluntario gradual']),
            dict(term='llegar a ser', definition='logro alcanzado con esfuerzo',
                 example='Llegó a ser directora de la empresa.',
                 accept=['llegar a ser', 'llegó a ser', 'logro']),
            dict(term='convertirse en', definition='transformación total (con sustantivo)',
                 example='Se convirtió en una referencia del sector.',
                 accept=['convertirse en', 'se convirtió en']),
            dict(term='resultar + adj', definition='resultado de una evaluación o experiencia',
                 example='La propuesta resultó muy interesante.',
                 accept=['resultar', 'resultó']),
            dict(term='quedarse sin + sust', definition='perder algo como resultado',
                 example='Se quedó sin trabajo de repente.',
                 accept=['quedarse sin', 'se quedó sin']),
        ]
    ),

    'oraciones-causales-concesivas': dict(
        level='b1',
        section='grammar',
        num='G15',
        short='Causales y Concesivas',
        title='Oraciones Causales y Concesivas',
        subtitle='Explica causas con porque/ya que y expresa concesión con aunque/a pesar de',
        slides=[
            ('Oraciones causales — introducción', None,
             '<p class="slide-explanation">Las <b>oraciones causales</b> expresan la <b>causa o motivo</b> de la acción principal. '
             'Los conectores causales más comunes son:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Conector</th><th style="padding:8px;text-align:left">Registro</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>porque</b></td><td style="padding:8px">neutro</td><td style="padding:8px">No fui porque estaba cansado.</td></tr>'
             '<tr><td style="padding:8px"><b>ya que</b></td><td style="padding:8px">formal/escrito</td><td style="padding:8px">Ya que estás aquí, ayúdame.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>puesto que</b></td><td style="padding:8px">formal</td><td style="padding:8px">Puesto que no hay tiempo, decidimos cancelar.</td></tr>'
             '<tr><td style="padding:8px"><b>dado que</b></td><td style="padding:8px">muy formal</td><td style="padding:8px">Dado que los precios han subido, revisaremos el presupuesto.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>como</b></td><td style="padding:8px">coloquial (inicio)</td><td style="padding:8px">Como no había nadie, me fui.</td></tr>'
             '</table>'),

            ('Como causal — posición inicial', None,
             '<p class="slide-explanation"><b>Como</b> con valor causal va siempre al <b>principio de la oración</b>, '
             'antes de la oración principal. Si va en posición media puede confundirse con otros usos:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Como</b> llovía, decidimos quedarnos. ✓ (causal — inicio)</p>'
             '<p>Decidimos quedarnos como llovía. ✗ (ambiguo)</p>'
             '<p>Habla <b>como</b> su padre. (comparativo — NO es causal)</p>'
             '</div>'
             '<p class="slide-explanation">El <b>como</b> causal siempre precede a la oración principal.</p>'),

            ('Porque vs. es que', None,
             '<p class="slide-explanation"><b>Porque</b> introduce la causa; <b>es que</b> introduce una explicación o justificación '
             '(a menudo una excusa). Ambas usan indicativo:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>No vine <b>porque</b> estaba enfermo. (causa objetiva)</p>'
             '<p>— ¿Por qué no viniste? — <b>Es que</b> estaba enfermo. (justificación/excusa)</p>'
             '</div>'
             '<p class="slide-explanation"><b>Es que</b> es más coloquial y aparece frecuentemente como respuesta a una pregunta. '
             'Nunca se escribe como «esq».'),

            ('Oraciones concesivas — aunque', None,
             '<p class="slide-explanation">Las <b>oraciones concesivas</b> expresan un obstáculo que no impide la acción principal. '
             'El conector principal es <b>aunque</b>:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Aunque + modo</th><th style="padding:8px;text-align:left">Matiz</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">aunque + <b>indicativo</b></td><td style="padding:8px">hecho real/admitido</td><td style="padding:8px">Aunque llueve, salgo.</td></tr>'
             '<tr><td style="padding:8px">aunque + <b>subjuntivo</b></td><td style="padding:8px">hipotético / indiferente</td><td style="padding:8px">Aunque llueva, saldré.</td></tr>'
             '</table>'),

            ('Más conectores concesivos', None,
             '<p class="slide-explanation">Otros conectores concesivos importantes:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Conector</th><th style="padding:8px;text-align:left">Estructura</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>a pesar de</b></td><td style="padding:8px">+ sustantivo/infinitivo</td><td style="padding:8px">A pesar del frío, salió.</td></tr>'
             '<tr><td style="padding:8px"><b>a pesar de que</b></td><td style="padding:8px">+ indicativo/subjuntivo</td><td style="padding:8px">A pesar de que llovía, salió.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>si bien</b></td><td style="padding:8px">+ indicativo (formal)</td><td style="padding:8px">Si bien es caro, merece la pena.</td></tr>'
             '<tr><td style="padding:8px"><b>por más que</b></td><td style="padding:8px">+ subjuntivo</td><td style="padding:8px">Por más que lo intente, no puede.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>aun cuando</b></td><td style="padding:8px">+ indicativo/subj. (formal)</td><td style="padding:8px">Aun cuando llueva, iremos.</td></tr>'
             '</table>'),
        ],
        traps=[
            ('*porque que', '<strong>porque</strong>', '<b>Porque</b> es una sola palabra que introduce la cláusula causal directamente. <b>No</b> se escribe *«porque que».'),
            ('Como causal en posición media', '<strong>Como causal va siempre al inicio</strong>', 'El <b>como</b> causal debe ir al principio de la oración: <i>Como llovía, me quedé</i>. En posición media es comparativo o condicional.'),
            ('*a pesar de que + infinitivo', '<strong>a pesar de + infinitivo</strong>', 'Con el mismo sujeto: <i>a pesar de <b>estar</b> cansado</i>. Si el sujeto cambia, se usa <i>a pesar de <b>que</b></i> + conjugación.'),
            ('*aunque llueve saldré (sin coma)', 'correcto, pero mejor con coma', 'Con <b>aunque</b> al inicio, se recomienda coma antes de la oración principal: <i>Aunque llueve, saldré</i>.'),
            ('por más que + indicativo', '<strong>por más que + subjuntivo</strong>', '<b>Por más que</b> requiere subjuntivo: <i>por más que lo <b>intente</b></i>, no puede.'),
        ],
        summary=[
            ('porque', 'causa directa + indicativo', 'No fui porque llovía.'),
            ('ya que / puesto que', 'causa formal + indicativo', 'Ya que estás, ayúdame.'),
            ('como + oración principal', 'causa — siempre al inicio', 'Como no había nadie, me fui.'),
            ('dado que', 'causa muy formal', 'Dado que los datos son claros, decidimos actuar.'),
            ('aunque + indicativo', 'concesión — hecho real', 'Aunque llueve, salgo.'),
            ('aunque + subjuntivo', 'concesión — hipotético/indiferente', 'Aunque llueva, saldré.'),
            ('a pesar de (que)', 'concesión — formal', 'A pesar del frío, continuamos.'),
        ],
        ex1=dict(
            title='Causales y concesivas: elige el conector',
            questions=[
                ('No salimos _____ hacía mucho frío.',
                 ['porque', 'aunque', 'a pesar de', 'si bien'],
                 0, 'La causa de no salir → <b>porque</b>.'),
                ('_____ llovía a cántaros, decidieron salir igualmente.',
                 ['Aunque', 'Porque', 'Ya que', 'Como'],
                 0, 'Obstáculo que no impide la acción → <b>aunque</b>.'),
                ('_____ no había transporte, tuve que ir andando.',
                 ['Como', 'Aunque', 'A pesar de', 'Si bien'],
                 0, '<b>Como</b> causal en posición inicial: el hecho motiva la consecuencia.'),
                ('_____ que el proyecto es ambicioso, el equipo lo apoya.',
                 ['A pesar de', 'Porque', 'Como', 'Si bien'],
                 0, 'Concesión formal: <b>a pesar de que</b>.'),
                ('_____ estés cansado, debes terminar el informe.',
                 ['Aunque', 'Porque', 'Ya que', 'Como'],
                 0, 'Obstáculo hipotético → concesión con subjuntivo → <b>aunque</b>.'),
                ('_____ los precios han subido, la empresa no modificará su estrategia.',
                 ['Si bien', 'Porque', 'Como', 'Por más que'],
                 0, 'Concesión formal → <b>si bien</b>.'),
            ]
        ),
        ex2=dict(
            title='Transforma y combina oraciones',
            questions=[
                ('Une con «ya que»: «Estás aquí. Puedes ayudarme.»',
                 'Ya que estás aquí, puedes ayudarme.',
                 ['Ya que estás aquí, puedes ayudarme.', 'Estás aquí ya que puedes ayudarme.', 'Puedes ayudarme porque aquí estás.'],
                 '<b>Ya que</b> introduce la causa (oración inicial o subordinada).'),
                ('Transforma la causal en concesiva con «aunque»: «No fui porque llovía.»',
                 'Aunque llovía, fui. / Fui aunque llovía.',
                 ['Aunque llovía, fui.', 'Aunque llueva, voy.', 'A pesar de lluvia, fui.'],
                 'Concesión = el obstáculo no impide la acción: <b>Aunque llovía, fui</b>.'),
                ('¿Cuál es la posición correcta de «como» causal?',
                 'Siempre al inicio, antes de la oración principal.',
                 ['siempre al inicio antes de la principal', 'al final', 'en posición media'],
                 '<b>Como</b> causal va obligatoriamente al principio: <i>Como no había nadie, me fui</i>.'),
                ('Completa con el modo correcto: «Aunque _____ (llover), saldré.»',
                 'llueva (subjuntivo — hipotético)',
                 ['llueva', 'lloverá', 'llueve'],
                 'Hipotético o indiferente → <b>aunque + subjuntivo</b>: <b>llueva</b>.'),
                ('¿«Es que» y «porque» son intercambiables?',
                 'No exactamente; «es que» es más coloquial y funciona como justificación/excusa.',
                 ['no; es que es coloquial y expresa justificación', 'sí, son idénticos', 'sí en registros formales'],
                 '<b>Porque</b> = causa objetiva. <b>Es que</b> = justificación/excusa, más coloquial.'),
            ]
        ),
        ex3=dict(
            title='Causales y concesivas avanzadas',
            questions=[
                ('¿Cuál es causal con «como»?',
                 ['Como no sabía la respuesta, se quedó callado.', 'Lo hice como me enseñaste.', 'Habla como tú.', 'Como si nada.'],
                 0, '<b>Como</b> causal al inicio: <i>Como no sabía…, se quedó callado</i>.'),
                ('«Por más que _____ (intentar, él), no puede.» ¿Qué forma lleva?',
                 ['intente', 'intenta', 'intentará', 'intentó'],
                 0, '<b>Por más que</b> + subjuntivo: <b>intente</b>.'),
                ('¿Cuál es la diferencia entre «a pesar de» y «a pesar de que»?',
                 ['a pesar de + sustantivo/infinitivo; a pesar de que + oración conjugada', 'son iguales', 'a pesar de que es más coloquial'],
                 0, '<b>A pesar de</b> + infinitivo o sustantivo. <b>A pesar de que</b> + oración conjugada.'),
                ('«Si bien es caro, merece la pena.» ¿Qué modo usa?',
                 ['indicativo', 'subjuntivo', 'condicional', 'imperativo'],
                 0, '<b>Si bien</b> usa <b>indicativo</b> (expresa un hecho real que se concede).'),
                ('¿Cuál NO es una oración concesiva?',
                 ['No fui porque llovía.', 'Aunque llovía, fui.', 'A pesar del frío, salió.', 'Por más que lo intente, no puede.'],
                 0, '<b>No fui porque llovía</b> es causal. Las demás son concesivas.'),
            ]
        ),
        game_desc='Expresa causa y concesión con los conectores y modos correctos',
        items=[
            dict(term='porque', definition='conector causal neutro',
                 example='No fui porque estaba cansado.',
                 accept=['porque', 'causal']),
            dict(term='ya que / puesto que', definition='conectores causales formales',
                 example='Ya que estás aquí, ayúdame.',
                 accept=['ya que', 'puesto que', 'causal formal']),
            dict(term='como + inicio', definition='causal coloquial — siempre al principio',
                 example='Como no había nadie, me fui.',
                 accept=['como causal', 'como inicio']),
            dict(term='aunque + indicativo', definition='concesión con hecho real admitido',
                 example='Aunque llueve, salgo.',
                 accept=['aunque indicativo', 'concesión real']),
            dict(term='aunque + subjuntivo', definition='concesión hipotética o indiferente',
                 example='Aunque llueva, saldré.',
                 accept=['aunque subjuntivo', 'concesión hipotetica']),
            dict(term='a pesar de', definition='concesión con sustantivo o infinitivo',
                 example='A pesar del frío, salieron.',
                 accept=['a pesar de', 'concesión formal']),
            dict(term='a pesar de que', definition='concesión con oración conjugada',
                 example='A pesar de que llovía, salieron.',
                 accept=['a pesar de que', 'concesión oración']),
            dict(term='por más que + subjuntivo', definition='concesión que expresa esfuerzo inútil',
                 example='Por más que lo intente, no puede.',
                 accept=['por mas que', 'por más que', 'concesión esfuerzo']),
        ]
    ),
}
