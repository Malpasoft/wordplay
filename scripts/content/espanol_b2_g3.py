# -*- coding: utf-8 -*-
"""espanol/ B2 Gramática — lote 3 (G11–G15)."""

CHAPTERS = {
    'nominalización': dict(
        level='b2',
        section='grammar',
        num='G11',
        short='La Nominalización',
        title='La Nominalización y los Sustantivos Verbales',
        subtitle='Transforma verbos y adjetivos en sustantivos para un discurso más formal y preciso',
        slides=[
            ('¿Qué es la nominalización?', None,
             '<p class="slide-explanation">La <b>nominalización</b> consiste en convertir un verbo o adjetivo en un sustantivo. '
             'Es muy frecuente en el lenguaje académico, periodístico y formal. '
             'Permite condensar información y crear un estilo más objetivo:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>El gobierno <b>decidió</b> aumentar los impuestos.</p>'
             '<p>→ La <b>decisión</b> del gobierno de aumentar los impuestos.</p>'
             '<p>El precio <b>subió</b> rápidamente.</p>'
             '<p>→ La <b>subida</b> rápida del precio.</p>'
             '</div>'),

            ('Formación de sustantivos desde verbos', None,
             '<p class="slide-explanation">Los sufijos más comunes para nominalizar verbos:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Sufijo</th><th style="padding:8px;text-align:left">Verbo</th><th style="padding:8px;text-align:left">Sustantivo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">-ción / -sión</td><td style="padding:8px">decidir, producir</td><td style="padding:8px"><b>decisión</b>, <b>producción</b></td></tr>'
             '<tr><td style="padding:8px">-miento</td><td style="padding:8px">crecer, desarrollar</td><td style="padding:8px"><b>crecimiento</b>, <b>desarrollo</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">-anza / -encia</td><td style="padding:8px">confiar, existir</td><td style="padding:8px"><b>confianza</b>, <b>existencia</b></td></tr>'
             '<tr><td style="padding:8px">-da / -ida</td><td style="padding:8px">llegar, subir</td><td style="padding:8px"><b>llegada</b>, <b>subida</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">-dura / -tura</td><td style="padding:8px">cubrir, abrir</td><td style="padding:8px"><b>cobertura</b>, <b>apertura</b></td></tr>'
             '<tr><td style="padding:8px">infinitivo como sust.</td><td style="padding:8px">saber, poder</td><td style="padding:8px">el <b>saber</b>, el <b>poder</b></td></tr>'
             '</table>'),

            ('Nominalización de adjetivos', None,
             '<p class="slide-explanation">Los adjetivos se nominalizan con artículo neutro o con sufijos:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Estructura</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>lo + adj</b> (abstracto)</td><td style="padding:8px">Lo <b>importante</b> es participar.</td></tr>'
             '<tr><td style="padding:8px">adj + <b>-dad/-tad</b></td><td style="padding:8px">libre → <b>libertad</b>; igual → <b>igualdad</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">adj + <b>-eza</b></td><td style="padding:8px">rico → <b>riqueza</b>; bello → <b>belleza</b></td></tr>'
             '<tr><td style="padding:8px">adj + <b>-ura</b></td><td style="padding:8px">alto → <b>altura</b>; amargo → <b>amargura</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">adj + <b>-ía</b></td><td style="padding:8px">cobarde → <b>cobardía</b>; valiente → <b>valentía</b></td></tr>'
             '</table>'),

            ('Nominalizaciones con DE', None,
             '<p class="slide-explanation">En la nominalización, el sujeto del verbo original se expresa con <b>de</b> '
             'y el complemento directo también suele ir con <b>de</b>:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>El gobierno <b>aprobó</b> la ley.</p>'
             '<p>→ La <b>aprobación</b> <i>de la ley</i> <i>por el gobierno</i>. (pasiva nominal)</p>'
             '<p>Los precios <b>subirán</b>.</p>'
             '<p>→ La prevista <b>subida</b> <i>de los precios</i>.</p>'
             '</div>'
             '<p class="slide-explanation">El complemento agente en la nominalización se introduce con <b>por</b> o <b>de</b> '
             '(la aprobación <i>de</i> la ley <i>por</i> el gobierno).</p>'),

            ('Nominalizaciones en lenguaje formal', None,
             '<p class="slide-explanation">La nominalización abunda en textos académicos, noticias y documentos formales. '
             'Identifica las nominalizaciones en los siguientes contextos:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Registro informal</th><th style="padding:8px;text-align:left">Registro formal (nominalización)</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Cuando el país <i>creció</i>…</td><td style="padding:8px">Durante el <b>crecimiento</b> del país…</td></tr>'
             '<tr><td style="padding:8px">Como no <i>confían</i> en nosotros…</td><td style="padding:8px">Ante la <b>falta de confianza</b> en nosotros…</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Porque <i>decidieron</i> mal…</td><td style="padding:8px">Debido a una <b>mala decisión</b>…</td></tr>'
             '<tr><td style="padding:8px">Si <i>aumentan</i> los precios…</td><td style="padding:8px">Con el <b>aumento</b> de los precios…</td></tr>'
             '</table>'),
        ],
        traps=[
            ('*la decidir', '<strong>la decisión</strong>', 'El infinitivo como sustantivo lleva artículo masculino: <b>el decidir</b>. Pero para una acción concreta usa el sustantivo nominalizado: <b>la decisión</b>.'),
            ('*subimiento de precios', '<strong>subida de precios</strong>', 'El sustantivo de <i>subir</i> es <b>subida</b>, no *subimiento. Consulta el diccionario si tienes dudas sobre el sustantivo correcto.'),
            ('*libertedad', '<strong>libertad</strong>', 'El sufijo es <b>-tad</b> (no -tedad): libre → <b>libertad</b>. Igualmente: lealtad, voluntad, mitad.'),
            ('*el aprobamiento de la ley', '<strong>la aprobación de la ley</strong>', 'Aprobar → <b>aprobación</b> (no *aprobamiento). Los verbos en -ar terminados en -ar con vocal larga suelen dar -ción.'),
            ('nominalizar en exceso', 'usa el verbo cuando sea más natural', 'La nominalización excesiva hace el texto pesado. Úsala cuando aporte precisión o sea requerida por el registro, no de forma mecánica.'),
        ],
        summary=[
            ('-ción / -sión', 'verbo → sustantivo (acción/proceso)', 'producir → producción'),
            ('-miento', 'verbo → sustantivo (proceso)', 'crecer → crecimiento'),
            ('-dad / -tad', 'adj → sustantivo (cualidad abstracta)', 'libre → libertad'),
            ('-eza', 'adj → sustantivo (cualidad)', 'rico → riqueza'),
            ('lo + adj', 'nominalización neutra del adjetivo', 'lo importante'),
            ('infinitivo como sust.', 'el + infinitivo (concepto abstracto)', 'el saber, el poder'),
            ('de en la nominalización', 'introduce complemento o agente', 'la aprobación de la ley por el gobierno'),
        ],
        ex1=dict(
            title='Nominalización: elige el sustantivo correcto',
            questions=[
                ('¿Cuál es el sustantivo de «crecer»?',
                 ['crecimiento', 'cresción', 'crecida', 'crecedura'],
                 0, 'Crecer → <b>crecimiento</b>. El sufijo -miento es frecuente con verbos de proceso.'),
                ('¿Cuál nominaliza correctamente «El gobierno decidió»?',
                 ['La decisión del gobierno', 'El decidir del gobierno', 'La decidura del gobierno', 'El decidimiento del gobierno'],
                 0, 'El sustantivo de <i>decidir</i> es <b>decisión</b>.'),
                ('¿Cuál es el sustantivo de «libre»?',
                 ['libertad', 'librez', 'librería', 'libertación'],
                 0, 'Libre → <b>libertad</b> (sufijo -tad para adjetivos de esta familia).'),
                ('Completa: «La _____ de los precios afecta a todos.» (subir)',
                 ['subida', 'subición', 'suba', 'subimiento'],
                 0, 'El sustantivo de <i>subir</i> es <b>subida</b>.'),
                ('¿Cuál es la nominalización formal de «los precios subieron»?',
                 ['la subida de los precios', 'el subimiento de precios', 'lo de los precios', 'el subir de precios'],
                 0, '<b>La subida de los precios</b> es la nominalización estándar.'),
                ('¿Cuál nominaliza el adjetivo «amargo»?',
                 ['amargura', 'amargedad', 'amargía', 'amargución'],
                 0, 'Amargo → <b>amargura</b> (sufijo -ura para adjetivos de sensación o cualidad física).'),
            ]
        ),
        ex2=dict(
            title='Nominaliza las siguientes oraciones',
            questions=[
                ('Transforma en nominalización: «El director aprobó el proyecto.»',
                 'La aprobación del proyecto por el director.',
                 ['La aprobación del proyecto por el director.', 'El aprobamiento del proyecto.', 'La aprobadura del proyecto.'],
                 'Nominalización: verbo <i>aprobar</i> → sustantivo <b>aprobación</b>. Complementos con <b>de</b> y <b>por</b>.'),
                ('¿Qué significa «el saber» en «el saber no ocupa lugar»?',
                 'El saber = el conocimiento (infinitivo nominalizado)',
                 ['el conocimiento / knowledge', 'el hecho de saber', 'el sabio'],
                 'El infinitivo con artículo masculino = sustantivo: <b>el saber</b> = knowledge.'),
                ('Transforma: «El ejército retiró sus tropas.»',
                 'La retirada de las tropas por el ejército.',
                 ['La retirada de las tropas por el ejército.', 'La retiramiento de tropas.', 'La retirida de tropas.'],
                 'Retirar → <b>retirada</b>. Complemento directo → de, agente → por.'),
                ('¿Cuál es el sufijo para «valiente → valentía»?',
                 '-ía',
                 ['-ía', '-ez', '-ura', '-cia'],
                 'Valiente → <b>valentía</b> (sufijo -ía). Igual: cobardía, alegría, ironía.'),
                ('Identifica la nominalización en: «El aumento de la producción fue inesperado.»',
                 'aumento (de aumentar) y producción (de producir)',
                 ['aumento y producción', 'solo aumento', 'solo producción'],
                 '<b>Aumento</b> (aumentar) y <b>producción</b> (producir) son las dos nominalizaciones.'),
            ]
        ),
        ex3=dict(
            title='Nominalización en contexto formal',
            questions=[
                ('¿Cuál es el registro más formal?',
                 ['Ante el crecimiento económico, se revisará la política.', 'Como la economía creció, se cambiará la política.', 'Cuando creció la economía, cambiarán la política.', 'Ya que la economía fue creciendo, cambian la política.'],
                 0, 'La nominalización <b>crecimiento económico</b> caracteriza el registro formal y académico.'),
                ('¿Qué sufijo da sustantivos abstractos de cualidad?',
                 ['-dad / -tad', '-miento', '-da / -ida', '-ción'],
                 0, 'Los sufijos <b>-dad/-tad</b> forman sustantivos de cualidad abstracta: libertad, igualdad, lealtad.'),
                ('«La existencia de este problema…» ¿De qué verbo procede «existencia»?',
                 ['existir', 'existenciar', 'existar', 'existicionar'],
                 0, 'Existir → <b>existencia</b> (sufijo -encia, como diferencia, presencia, urgencia).'),
                ('¿Cuál es el sustantivo de «abrir»?',
                 ['apertura', 'abertura', 'ambas son correctas', 'abrimiento'],
                 2, 'Tanto <b>apertura</b> (apertura de un plazo, una tienda) como <b>abertura</b> (abertura física) son correctas, con matices.'),
                ('¿Qué estructura nominaliza adjetivos de forma neutra?',
                 ['lo + adjetivo', 'el + adjetivo', 'un + adjetivo', 'muy + adjetivo'],
                 0, '<b>Lo + adj</b>: lo importante, lo esencial, lo curioso — nominalización neutra abstracta.'),
            ]
        ),
        game_desc='Nominaliza verbos y adjetivos con los sufijos y estructuras correctas',
        items=[
            dict(term='-ción / -sión', definition='sufijo nominalizador de verbos (acción/proceso)',
                 example='producir → producción',
                 accept=['-cion', '-sion', 'ción sión', 'sufijo accion']),
            dict(term='-miento', definition='sufijo nominalizador de verbos (proceso continuo)',
                 example='crecer → crecimiento',
                 accept=['-miento', 'miento', 'sufijo proceso']),
            dict(term='-dad / -tad', definition='sufijo nominalizador de adjetivos (cualidad abstracta)',
                 example='libre → libertad',
                 accept=['-dad', '-tad', 'dad tad', 'sufijo cualidad']),
            dict(term='-eza', definition='sufijo nominalizador de adjetivos (cualidad)',
                 example='rico → riqueza',
                 accept=['-eza', 'eza', 'sufijo eza']),
            dict(term='el + infinitivo', definition='nominalización del verbo como concepto abstracto',
                 example='el saber, el poder',
                 accept=['infinitivo sustantivo', 'el saber', 'el poder']),
            dict(term='apertura / cobertura', definition='nominalizaciones de abrir / cubrir',
                 example='la apertura del plazo',
                 accept=['apertura', 'cobertura', '-tura']),
            dict(term='nominalización con DE', definition='complemento del sustantivo verbal',
                 example='la decisión del gobierno',
                 accept=['de en nominalización', 'complemento de', 'sustantivo verbal de']),
            dict(term='valentía / cobardía', definition='sufijo -ía en adjetivos de cualidad moral',
                 example='valiente → valentía',
                 accept=['-ía', 'valentia', 'cobardia', 'sufijo ia']),
        ]
    ),

    'futuro-avanzado': dict(
        level='b2',
        section='grammar',
        num='G12',
        short='El Futuro Avanzado',
        title='Los Tiempos del Futuro y el Condicional Avanzado',
        subtitle='Futuro simple, futuro perfecto, condicional y sus usos modales',
        slides=[
            ('Futuro simple — usos avanzados', None,
             '<p class="slide-explanation">Además de expresar predicciones y planes, el futuro simple tiene importantes '
             '<b>usos modales</b> en el español actual:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Uso</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Predicción/plan</td><td style="padding:8px">Mañana <b>lloverá</b>.</td></tr>'
             '<tr><td style="padding:8px">Conjetura (presente)</td><td style="padding:8px">¿Dónde estará? <b>Estará</b> en casa.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Mandato enfático</td><td style="padding:8px">¡No <b>mentirás</b>! (como los Mandamientos)</td></tr>'
             '<tr><td style="padding:8px">Valor concesivo</td><td style="padding:8px"><b>Será</b> caro, pero merece la pena.</td></tr>'
             '</table>'
             '<p class="slide-explanation">La <b>conjetura</b> es uno de los usos más frecuentes en habla cotidiana.</p>'),

            ('El futuro perfecto', None,
             '<p class="slide-explanation">El <b>futuro perfecto</b> (habré + participio) expresa:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Uso</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Acción futura anterior a otra</td><td style="padding:8px">Cuando llegues, ya <b>habrá comido</b>.</td></tr>'
             '<tr><td style="padding:8px">Conjetura sobre el pasado reciente</td><td style="padding:8px">¿Dónde estará? <b>Se habrá perdido</b>.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Reprobación o sorpresa</td><td style="padding:8px">¡Cómo <b>habrá cambiado</b>!</td></tr>'
             '</table>'
             '<p class="slide-explanation">Formación: <b>habré/habrás/habrá/habremos/habréis/habrán + participio</b>.</p>'),

            ('El condicional simple — usos modales', None,
             '<p class="slide-explanation">El condicional simple (hablaría, comería…) tiene varios usos además de la hipótesis:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Uso</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Hipótesis tipo 2</td><td style="padding:8px">Si tuviera tiempo, <b>viajaría</b>.</td></tr>'
             '<tr><td style="padding:8px">Futuro del pasado</td><td style="padding:8px">Dijo que <b>vendría</b>. (futuro relativo al pasado)</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Conjetura en el pasado</td><td style="padding:8px">¿Qué hora sería? <b>Serían</b> las tres.</td></tr>'
             '<tr><td style="padding:8px">Atenuación / cortesía</td><td style="padding:8px"><b>Podría</b> usted ayudarme? <b>Querría</b> hablar con usted.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Valor concesivo</td><td style="padding:8px"><b>Sería</b> difícil, pero lo consiguió.</td></tr>'
             '</table>'),

            ('El condicional perfecto', None,
             '<p class="slide-explanation">El <b>condicional perfecto</b> (habría + participio) se usa en:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Uso</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Hipótesis tipo 3 (irreal pasado)</td><td style="padding:8px">Si hubiera sabido, <b>habría venido</b>.</td></tr>'
             '<tr><td style="padding:8px">Reprobación / lamento</td><td style="padding:8px"><b>Habrías</b> podido llamar…</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Futuro perfecto del pasado</td><td style="padding:8px">Dijo que para el lunes ya <b>habría terminado</b>.</td></tr>'
             '</table>'
             '<p class="slide-explanation">Formación: <b>habría/habrías/habría/habríamos/habríais/habrían + participio</b>.</p>'),

            ('Ir a + infinitivo vs. futuro simple', None,
             '<p class="slide-explanation">Ambas formas expresan futuro pero con matices diferentes:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Forma</th><th style="padding:8px;text-align:left">Matiz</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>ir a + inf</b></td><td style="padding:8px">intención, plan inmediato</td><td style="padding:8px"><b>Voy a llamarle</b> ahora mismo.</td></tr>'
             '<tr><td style="padding:8px"><b>futuro simple</b></td><td style="padding:8px">predicción, promesa, más distante</td><td style="padding:8px"><b>Te llamaré</b> mañana.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>presente</b></td><td style="padding:8px">plan fijo, agenda</td><td style="padding:8px">El tren <b>sale</b> a las tres.</td></tr>'
             '</table>'
             '<p class="slide-explanation">En el español coloquial, <b>ir a + inf</b> reemplaza frecuentemente al futuro simple.</p>'),
        ],
        traps=[
            ('*si vendría', '<strong>si viniera</strong>', 'NUNCA se usa el condicional después de <b>si</b> condicional. Lo correcto es <b>si + subjuntivo imperfecto</b>: si viniera.'),
            ('*habría venido → hipótesis presente', '<strong>habría venido = hipótesis pasada</strong>', 'El condicional perfecto (<b>habría venido</b>) expresa una hipótesis irrealizable en el PASADO. Para el presente: <b>vendría</b>.'),
            ('confundir futuro de conjetura con predicción', 'ambos usan futuro simple', 'Tanto la predicción (<i>mañana lloverá</i>) como la conjetura (<i>estará en casa</i>) usan futuro simple. El contexto distingue.'),
            ('*habrá llegado cuando llegues', '<strong>cuando llegues, habrá llegado</strong>', 'En la oración temporal «cuando + subj», el futuro perfecto expresa la acción completada en ese momento futuro: <i>cuando llegues, ya <b>habrá comido</b></i>.'),
            ('*querría = quería', '<strong>querría = condicional; quería = imperfecto</strong>', '<b>Querría</b> es el condicional de <i>querer</i> (atenuación/cortesía). <b>Quería</b> es el imperfecto. No los confundas.'),
        ],
        summary=[
            ('futuro simple', 'predicción, conjetura (presente), mandato enfático', '¿Dónde estará? Estará en casa.'),
            ('futuro perfecto', 'habrá + participio — anterior a otra acción futura', 'Cuando llegues, ya habrá comido.'),
            ('condicional simple', 'hipótesis tipo 2, futuro del pasado, conjetura pasada', 'Dijo que vendría. / ¿Qué hora sería?'),
            ('condicional perfecto', 'habría + participio — hipótesis irreal en el pasado', 'Si hubiera sabido, habría venido.'),
            ('ir a + inf', 'intención/plan inmediato', 'Voy a llamarle ahora.'),
            ('futuro concesivo', 'Será + adj/sust + pero', 'Será difícil, pero posible.'),
            ('condicional de cortesía', 'querría, podría, debería (atenuación)', '¿Podría ayudarme?'),
        ],
        ex1=dict(
            title='Futuro y condicional: elige la opción correcta',
            questions=[
                ('¿Dónde estará Juan? Creo que _____ en el trabajo.',
                 ['estará', 'está', 'estaría', 'esté'],
                 0, 'Conjetura sobre el presente → futuro simple: <b>estará</b>.'),
                ('Si hubiera tenido tiempo, _____ a verte.',
                 ['habría ido', 'iría', 'fui', 'iré'],
                 0, 'Hipótesis irreal en el pasado (tipo 3): si + hubiera + participio → <b>habría ido</b>.'),
                ('Para cuando llegues, ya _____ los deberes.',
                 ['habré terminado', 'terminaré', 'habría terminado', 'termine'],
                 0, 'Acción futura completada antes de otra → <b>futuro perfecto</b>: habré terminado.'),
                ('Dijo que _____ a las ocho.',
                 ['vendría', 'vendrá', 'venía', 'venga'],
                 0, 'Futuro del pasado en estilo indirecto → <b>condicional</b>: vendría.'),
                ('¿Qué hora sería cuando llamaste? _____ las dos de la madrugada.',
                 ['Serían', 'Serán', 'Sean', 'Eran'],
                 0, 'Conjetura sobre el pasado → <b>condicional</b>: serían.'),
                ('_____ caro, pero merece la pena probarlo.',
                 ['Será', 'Es', 'Sea', 'Sería'],
                 0, 'Valor concesivo con futuro: <b>Será</b> caro (concedo que sea caro), pero…'),
            ]
        ),
        ex2=dict(
            title='Forma los tiempos futuros y condicionales',
            questions=[
                ('Forma el futuro perfecto de «ella / terminar».',
                 'ella habrá terminado',
                 ['habrá terminado', 'ella habrá terminado', 'habrá terminada'],
                 'Futuro perfecto: <b>habrá</b> + participio → <b>habrá terminado</b>.'),
                ('¿Por qué es incorrecto «si vendría»?',
                 'Porque después de «si» condicional nunca va el condicional, sino el subjuntivo imperfecto: si viniera.',
                 ['si + condicional es incorrecto; se usa subjuntivo imperfecto', 'es incorrecto porque falta acento', 'es correcto en algunos dialectos'],
                 'Regla: <b>si + subjuntivo imperfecto</b> → <b>si viniera</b>. Nunca si + condicional.'),
                ('¿Cómo se usa el condicional para la conjetura en el pasado? Da un ejemplo.',
                 '¿Cuántos años tendría? Tendría unos cuarenta.',
                 ['tendría unos cuarenta', '¿cuántos años tendría? tendría unos cuarenta', 'serían las tres'],
                 'Conjetura sobre el pasado → <b>condicional simple</b>: <i>¿Qué hora sería? Serían las tres</i>.'),
                ('Forma el condicional perfecto de «nosotros / poder hacer».',
                 'nosotros habríamos podido hacer',
                 ['habríamos podido hacer', 'nosotros habríamos podido hacer', 'habremos podido'],
                 'Condicional perfecto: <b>habríamos</b> + participio → <b>habríamos podido</b>.'),
                ('¿Cuál es la diferencia entre «voy a llamarte» y «te llamaré»?',
                 'Ir a + inf = intención/plan inmediato; futuro simple = predicción más general o distante.',
                 ['ir a + inf es inmediato; futuro es más distante o general', 'son idénticos', 'futuro es más coloquial'],
                 '<b>Voy a llamarte</b> = intención presente, inmediata. <b>Te llamaré</b> = promesa, predicción, más distante.'),
            ]
        ),
        ex3=dict(
            title='Futuro avanzado: identificación y uso',
            questions=[
                ('«Serán las cinco.» ¿Qué expresa el futuro aquí?',
                 ['Conjetura sobre el tiempo presente', 'Predicción del futuro', 'Mandato enfático', 'Valor concesivo'],
                 0, 'El futuro simple expresa conjetura sobre el presente: <b>serán las cinco</b> (creo que son las cinco).'),
                ('¿Cuál es correcto en estilo indirecto (pasado)?',
                 ['Dijo que vendría.', 'Dijo que vendrá.', 'Dijo que venía.', 'Dijo que venga.'],
                 0, 'Futuro del pasado → <b>condicional</b>: dijo que <b>vendría</b>.'),
                ('«Habrás podido hacerlo mejor.» ¿Qué expresa?',
                 ['Reproche o lamento', 'Predicción futura', 'Conjetura del presente', 'Hipótesis irreal'],
                 0, 'Condicional perfecto con matiz de <b>reproche o lamento</b>: habrías podido hacerlo mejor.'),
                ('¿Cuál hipótesis es irreal en el pasado?',
                 ['Si hubiera estudiado, habría aprobado.', 'Si estudias, aprobarás.', 'Si estudiara, aprobaría.', 'Si estudiaste, aprobaste.'],
                 0, 'Tipo 3 (irreal pasado): <b>si + hubiera + participio → habría + participio</b>.'),
                ('¿Qué forma expresa una acción futura completada antes de otra futura?',
                 ['El futuro perfecto (habré + participio)', 'El futuro simple', 'El condicional perfecto', 'El subjuntivo perfecto'],
                 0, '<b>Futuro perfecto</b>: <i>cuando llegues, ya habrá comido</i>.'),
            ]
        ),
        game_desc='Usa el futuro simple, futuro perfecto, condicional y sus valores modales',
        items=[
            dict(term='futuro de conjetura', definition='futuro simple para suposición sobre el presente',
                 example='¿Dónde estará? Estará en casa.',
                 accept=['futuro conjetura', 'estará', 'conjetura presente']),
            dict(term='futuro perfecto', definition='habrá + participio — acción futura anterior a otra',
                 example='Cuando llegues, ya habrá comido.',
                 accept=['futuro perfecto', 'habrá comido', 'habrá terminado']),
            dict(term='futuro concesivo', definition='Será + adj + pero — concesión con futuro',
                 example='Será difícil, pero lo haré.',
                 accept=['futuro concesivo', 'será pero']),
            dict(term='condicional futuro del pasado', definition='condicional simple para referencia futura desde el pasado',
                 example='Dijo que vendría.',
                 accept=['condicional futuro pasado', 'dijo que vendría']),
            dict(term='condicional de conjetura pasada', definition='condicional para suposición sobre el pasado',
                 example='¿Qué hora sería? Serían las tres.',
                 accept=['condicional conjetura pasada', 'serían las tres']),
            dict(term='condicional perfecto', definition='habría + participio — hipótesis irreal en el pasado',
                 example='Si hubiera sabido, habría venido.',
                 accept=['condicional perfecto', 'habría venido', 'habrían podido']),
            dict(term='si + imperfecto subj → condicional', definition='hipótesis tipo 2 (presente/futuro irreal)',
                 example='Si tuviera dinero, viajaría.',
                 accept=['tipo 2', 'si imperfecto condicional', 'tuviera viajaría']),
            dict(term='si + pluscuamperf subj → cond. perfecto', definition='hipótesis tipo 3 (pasado irreal)',
                 example='Si hubiera sabido, habría venido.',
                 accept=['tipo 3', 'si hubiera habría', 'pluscuamperfecto condicional']),
        ]
    ),

    'construcciones-absolutas': dict(
        level='b2',
        section='grammar',
        num='G13',
        short='Construcciones Absolutas',
        title='Las Construcciones Absolutas con Gerundio y Participio',
        subtitle='Expresa simultaneidad, causa y consecuencia con gerundio y participio absolutos',
        slides=[
            ('El gerundio en construcciones absolutas', None,
             '<p class="slide-explanation">El <b>gerundio</b> puede funcionar como núcleo de una construcción absoluta '
             '— una frase nominal que expresa circunstancias de la acción principal. '
             'Esta construcción es más propia del registro formal y escrito:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Llegando tarde</b>, no pudo entrar. (causa)</p>'
             '<p><b>Estudiando más</b>, aprobarías. (condición)</p>'
             '<p><b>Cantando</b>, se sintió mejor. (modo)</p>'
             '</div>'
             '<p class="slide-explanation">El sujeto del gerundio puede ser diferente del sujeto principal:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Siendo ya tarde</b>, decidimos cancelar. (causa absoluta — sujeto implícito)</p>'
             '</div>'),

            ('Gerundio de anterioridad y posterioridad', None,
             '<p class="slide-explanation">El gerundio simple (<b>-ndo</b>) expresa simultaneidad o anterioridad inmediata. '
             'El gerundio compuesto (<b>habiendo + participio</b>) expresa anterioridad clara:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Tipo</th><th style="padding:8px;text-align:left">Forma</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Simultaneidad</td><td style="padding:8px">gerundio simple</td><td style="padding:8px">Hablando por teléfono, entró.</td></tr>'
             '<tr><td style="padding:8px">Anterioridad</td><td style="padding:8px">habiendo + participio</td><td style="padding:8px"><b>Habiendo terminado</b> el trabajo, salió.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Manera</td><td style="padding:8px">gerundio simple</td><td style="padding:8px">Entró silbando.</td></tr>'
             '</table>'),

            ('El participio en construcciones absolutas', None,
             '<p class="slide-explanation">El <b>participio</b> puede encabezar una construcción absoluta — '
             'frase con sujeto propio que expresa acción completada antes de la principal. '
             'El participio concuerda con su sujeto en género y número:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Terminada la reunión</b>, todos se fueron. (sujeto: la reunión)</p>'
             '<p><b>Firmados los contratos</b>, comenzó el proyecto. (sujeto: los contratos)</p>'
             '<p><b>Dicho esto</b>, se marchó. (sujeto: esto — neutro)</p>'
             '</div>'
             '<p class="slide-explanation">La construcción de participio absoluto es muy frecuente en registros formales '
             'y literarios. Expresa una acción <b>anterior</b> a la principal.</p>'),

            ('Al + infinitivo — construcción temporal-causal', None,
             '<p class="slide-explanation"><b>Al + infinitivo</b> expresa simultaneidad o causa. '
             'Equivale a «cuando + verbo» o «porque + verbo»:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Al llegar</b>, me di cuenta de que había olvidado las llaves. (cuando llegué)</p>'
             '<p><b>Al ver</b> el resultado, se echó a llorar. (cuando vio)</p>'
             '<p><b>Al ser</b> tarde, decidimos cancelar. (porque era tarde)</p>'
             '</div>'
             '<p class="slide-explanation"><b>De + infinitivo</b> expresa condición (más formal que <i>si</i>):</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>De haberlo sabido</b>, habría actuado de otra manera. (si lo hubiera sabido)</p>'
             '</div>'),

            ('Restricciones del gerundio como modificador de sustantivo', None,
             '<p class="slide-explanation">El gerundio en español <b>NO</b> puede modificar a un sustantivo como adjetivo '
             '(a diferencia del inglés). Solo puede hacerlo en pocos casos fijados:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Agua hirviendo</b> ✓ (excepción lexicalizada)</p>'
             '<p><b>Un niño llorando</b> ✓ (predicativo, no atributivo)</p>'
             '<p>*Un libro conteniendo errores ✗ (correcto: que contiene errores)</p>'
             '<p>*El hombre hablando español ✗ (correcto: que habla español)</p>'
             '</div>'
             '<p class="slide-explanation">En posición postnominal, usa una cláusula relativa en vez de gerundio.</p>'),
        ],
        traps=[
            ('*Un libro conteniendo errores', '<strong>un libro que contiene errores</strong>', 'El gerundio en español no se usa como adjetivo postnominal. Usa <b>que + verbo conjugado</b>.'),
            ('*Habiendo llegado, voy al mercado (futuro)', '<strong>Al llegar, iré al mercado</strong>', 'El gerundio compuesto (<i>habiendo + participio</i>) expresa anterioridad en el pasado, no en el futuro. Para futuro: <b>al llegar</b>.'),
            ('*Terminado la reunión…', '<strong>Terminada la reunión…</strong>', 'El participio absoluto concuerda con su sujeto en género: la reunión (fem.) → <b>terminada</b>.'),
            ('Gerundio como sujeto', 'incorrecto en español formal', 'El gerundio NO es sujeto en español formal: *«Fumar es malo». En registro formal: <b>Fumar</b> es incorrecto pero muy frecuente; se prefiere «El tabaco es malo».'),
            ('*de haber sabido → de habiendo sabido', '<strong>de haber sabido</strong>', 'La construcción condicional formal es <b>de + infinitivo compuesto</b>: <i>de haber sabido</i>. No se usa gerundio aquí.'),
        ],
        summary=[
            ('gerundio simultáneo', 'acción simultánea o de modo', 'Entró corriendo.'),
            ('habiendo + participio', 'acción anterior a la principal', 'Habiendo terminado, salió.'),
            ('participio absoluto', 'sujeto propio + participio — acción anterior', 'Terminada la reunión, salimos.'),
            ('al + infinitivo', 'simultaneidad / causa — equivale a cuando/porque', 'Al llegar, llamó.'),
            ('de + infinitivo compuesto', 'condición formal — equivale a si hubiera', 'De haberlo sabido, actuaría distinto.'),
            ('gerundio como adj', 'solo en formas lexicalizadas (agua hirviendo)', 'Agua hirviendo (excepción).'),
            ('restricción de gerundio postnominal', 'usa cláusula relativa', 'el libro que contiene errores (no *conteniendo).'),
        ],
        ex1=dict(
            title='Construcciones absolutas: elige la correcta',
            questions=[
                ('«_____ la reunión, todos se fueron.» (terminar)',
                 ['Terminada', 'Terminando', 'Al terminar', 'Habiendo terminando'],
                 0, 'Participio absoluto: la reunión (fem.) → <b>terminada</b>. Expresa acción anterior.'),
                ('«_____ al mercado, recuerda comprar pan.» (ir)',
                 ['Al ir', 'Habiendo ido', 'Ido', 'Yendo'],
                 0, 'Simultaneidad/condición temporal → <b>al + infinitivo</b>: al ir.'),
                ('¿Cuál es incorrecta?',
                 ['Un libro conteniendo errores.', 'Un libro que contiene errores.', 'Habiendo terminado, salió.', 'Terminada la clase, salimos.'],
                 0, '<b>Un libro conteniendo errores</b> es incorrecto. El gerundio no modifica sustantivos. Usa: «que contiene».'),
                ('«_____ los contratos, comenzaron las obras.» (firmar)',
                 ['Firmados', 'Firmando', 'Al firmar', 'Habiendo firmando'],
                 0, 'Participio absoluto: los contratos (masc. pl.) → <b>firmados</b>.'),
                ('«_____ el trabajo, salió a cenar.» (terminar — acción anterior)',
                 ['Habiendo terminado', 'Terminando', 'Al terminar', 'Terminado él'],
                 0, 'Anterioridad clara → gerundio compuesto: <b>habiendo terminado</b>.'),
                ('«_____ haberlo sabido, habría actuado de otra manera.»',
                 ['De', 'Si', 'Al', 'Por'],
                 0, 'Condición formal: <b>de + infinitivo compuesto</b> = si hubiera…'),
            ]
        ),
        ex2=dict(
            title='Reformula con construcción absoluta',
            questions=[
                ('Reemplaza: «Cuando llegó, llamó al médico.»',
                 'Al llegar, llamó al médico.',
                 ['Al llegar, llamó al médico.', 'Llegando, llamó al médico.', 'Habiendo llegado, llamó al médico.'],
                 '<b>Al + infinitivo</b> = cuando + verbo pasado: <b>al llegar</b>.'),
                ('Reformula: «Una vez firmados los contratos, comenzaron las obras.»',
                 'Firmados los contratos, comenzaron las obras.',
                 ['Firmados los contratos, comenzaron las obras.', 'Firmando los contratos, comenzaron.', 'Al firmar contratos, comenzaron.'],
                 'Participio absoluto: <b>firmados los contratos</b>.'),
                ('¿Cómo corriges «un señor hablando ruso»?',
                 'un señor que habla ruso',
                 ['un señor que habla ruso', 'un señor hablante de ruso', 'un señor hablado ruso'],
                 'El gerundio no modifica sustantivos. Usa <b>que + verbo conjugado</b>.'),
                ('Completa: «_____ este problema, podemos pasar al siguiente.» (resolver — acción anterior, sujeto: el problema)',
                 'Resuelto este problema,',
                 ['Resuelto este problema,', 'Resolviendo este problema,', 'Al resolver este problema,'],
                 'El problema es masculino singular → participio <b>resuelto</b>. Construcción absoluta de anterioridad.'),
                ('Transforma en condición formal: «Si lo hubiera visto, te lo habría contado.»',
                 'De haberlo visto, te lo habría contado.',
                 ['De haberlo visto, te lo habría contado.', 'Habiendo visto, te lo habría contado.', 'Al verlo, te lo habría contado.'],
                 '<b>De + infinitivo compuesto</b> = si hubiera…: <b>de haberlo visto</b>.'),
            ]
        ),
        ex3=dict(
            title='Gerundio y participio: uso correcto',
            questions=[
                ('¿Cuál es la construcción de participio absoluto correcta?',
                 ['Aprobado el proyecto, comenzaron las obras.', 'Aprobando el proyecto, comenzaron las obras.', 'Al aprobar el proyecto, comenzaron las obras.', 'Habiendo aprobado el proyecto, comenzaron las obras.'],
                 0, 'Participio absoluto: el proyecto (masc.) → <b>aprobado</b>. Acción anterior a la principal.'),
                ('¿Qué expresa «al + infinitivo»?',
                 ['Simultaneidad o causa temporal', 'Acción anterior con sujeto propio', 'Condición irreal', 'Modo de hacer la acción'],
                 0, '<b>Al + infinitivo</b> = cuando + verbo o porque + verbo: expresa simultaneidad o causa temporal.'),
                ('¿Cuándo se usa el gerundio compuesto (habiendo + participio)?',
                 ['Para una acción claramente anterior a la principal', 'Para una acción simultánea', 'Para modificar un sustantivo', 'Para condiciones formales'],
                 0, 'Gerundio compuesto = anterioridad clara: <b>habiendo terminado</b>, salió.'),
                ('¿Cuál es correcta?',
                 ['Dicho esto, se fue.', 'Diciendo esto, se fue.', 'Al decir esto, se fue.', 'Habiendo dicho esto, se fue.'],
                 0, '<b>Dicho esto</b> = participio absoluto lexicalizado muy frecuente (sujeto: esto, neutro).'),
                ('«De haberlo sabido…» equivale a:',
                 ['Si lo hubiera sabido…', 'Cuando lo supo…', 'Al saberlo…', 'Sabiéndolo…'],
                 0, '<b>De + infinitivo compuesto</b> = condición irreal en el pasado: <b>si lo hubiera sabido</b>.'),
            ]
        ),
        game_desc='Usa construcciones absolutas con participio, gerundio y al + infinitivo',
        items=[
            dict(term='participio absoluto', definition='participio con sujeto propio — acción anterior a la principal',
                 example='Terminada la reunión, todos salieron.',
                 accept=['participio absoluto', 'terminada la reunión']),
            dict(term='habiendo + participio', definition='gerundio compuesto — anterioridad clara',
                 example='Habiendo terminado, salió.',
                 accept=['habiendo participio', 'gerundio compuesto', 'habiendo terminado']),
            dict(term='al + infinitivo', definition='simultaneidad o causa temporal',
                 example='Al llegar, llamó.',
                 accept=['al infinitivo', 'al llegar', 'simultaneidad']),
            dict(term='de + inf. compuesto', definition='condición formal equivalente a si hubiera',
                 example='De haberlo sabido, habría actuado distinto.',
                 accept=['de haber', 'condición formal', 'de infinitivo compuesto']),
            dict(term='gerundio simultáneo', definition='gerundio simple — simultaneidad o modo',
                 example='Entró corriendo.',
                 accept=['gerundio simultaneo', 'gerundio simple', 'corriendo']),
            dict(term='concordancia del participio absoluto', definition='el participio concuerda con su sujeto',
                 example='Firmados los contratos. / Terminada la reunión.',
                 accept=['concordancia participio', 'firmados terminada']),
            dict(term='restricción gerundio postnominal', definition='gerundio NO modifica sustantivos (usa cláusula relativa)',
                 example='El libro que contiene errores (no: *conteniendo)',
                 accept=['gerundio adjetivo', 'restricción gerundio', 'que contiene']),
            dict(term='dicho esto', definition='participio absoluto lexicalizado',
                 example='Dicho esto, se marchó.',
                 accept=['dicho esto', 'participio lexicalizado']),
        ]
    ),

    'lenguaje-formal': dict(
        level='b2',
        section='grammar',
        num='G14',
        short='Lenguaje Formal',
        title='El Lenguaje Formal y los Registros del Español',
        subtitle='Construye textos formales con la voz pasiva, las impersonales y el léxico apropiado',
        slides=[
            ('Registros del español', None,
             '<p class="slide-explanation">El español tiene distintos <b>registros</b> según el contexto. '
             'Pasar de uno a otro requiere cambios léxicos, morfológicos y sintácticos:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Registro</th><th style="padding:8px;text-align:left">Características</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Coloquial</td><td style="padding:8px">vocabulario simple, elipsis, frases cortas</td><td style="padding:8px">Se cargaron el proyecto.</td></tr>'
             '<tr><td style="padding:8px">Estándar</td><td style="padding:8px">norma culta, gramática correcta</td><td style="padding:8px">Cancelaron el proyecto.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Formal</td><td style="padding:8px">nominalización, pasiva, léxico técnico</td><td style="padding:8px">El proyecto fue cancelado por la dirección.</td></tr>'
             '<tr><td style="padding:8px">Académico/jurídico</td><td style="padding:8px">impersonal, subjuntivo, perífrasis pasiva</td><td style="padding:8px">Se procedió a la cancelación del proyecto.</td></tr>'
             '</table>'),

            ('La voz pasiva formal', None,
             '<p class="slide-explanation">En el registro formal y escrito la voz pasiva es más frecuente. '
             'Hay tres construcciones pasivas principales:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Tipo</th><th style="padding:8px;text-align:left">Estructura</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Pasiva perifrástica</td><td style="padding:8px">ser + participio (+ por)</td><td style="padding:8px">El informe fue aprobado por el director.</td></tr>'
             '<tr><td style="padding:8px">Pasiva refleja</td><td style="padding:8px">se + 3.ª persona</td><td style="padding:8px">Se aprobó el informe.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Pasiva de estado</td><td style="padding:8px">estar + participio</td><td style="padding:8px">El informe está aprobado.</td></tr>'
             '</table>'
             '<p class="slide-explanation">La <b>pasiva refleja</b> es la más frecuente en el español formal moderno; '
             'la <b>perifrástica</b> se usa cuando se menciona el agente.</p>'),

            ('Impersonales formales', None,
             '<p class="slide-explanation">El lenguaje formal usa frecuentemente estructuras <b>impersonales</b> '
             'para evitar referentes personales y dar objetividad:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Estructura</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Se + verbo 3.ª sing./pl.</td><td style="padding:8px">Se considera que los datos son fiables.</td></tr>'
             '<tr><td style="padding:8px">Es + adj + infinitivo</td><td style="padding:8px">Es necesario revisar los resultados.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Resulta + adj/sust</td><td style="padding:8px">Resulta evidente que hay un problema.</td></tr>'
             '<tr><td style="padding:8px">Cabe + infinitivo</td><td style="padding:8px">Cabe señalar que los datos son incompletos.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Conviene + infinitivo</td><td style="padding:8px">Conviene recordar que el plazo es hoy.</td></tr>'
             '</table>'),

            ('Léxico formal vs. coloquial', None,
             '<p class="slide-explanation">El léxico formal requiere palabras y expresiones específicas. '
             'Algunos pares coloquial / formal frecuentes:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Coloquial</th><th style="padding:8px;text-align:left">Formal</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">hacer</td><td style="padding:8px"><b>llevar a cabo, realizar, efectuar</b></td></tr>'
             '<tr><td style="padding:8px">decir</td><td style="padding:8px"><b>señalar, indicar, manifestar, declarar</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">poner</td><td style="padding:8px"><b>establecer, disponer, colocar</b></td></tr>'
             '<tr><td style="padding:8px">dar</td><td style="padding:8px"><b>otorgar, conceder, proporcionar</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">usar</td><td style="padding:8px"><b>emplear, utilizar, recurrir a</b></td></tr>'
             '<tr><td style="padding:8px">porque</td><td style="padding:8px"><b>dado que, puesto que, en virtud de</b></td></tr>'
             '</table>'),

            ('Conectores formales y construcciones más complejas', None,
             '<p class="slide-explanation">El texto formal usa conectores más elaborados y construcciones complejas:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Función</th><th style="padding:8px;text-align:left">Conectores formales</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Adición</td><td style="padding:8px">asimismo, igualmente, del mismo modo, además de lo anterior</td></tr>'
             '<tr><td style="padding:8px">Contraste</td><td style="padding:8px">no obstante, si bien, con todo, a pesar de lo cual</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Consecuencia</td><td style="padding:8px">por consiguiente, en consecuencia, de ahí que + subj</td></tr>'
             '<tr><td style="padding:8px">Causa</td><td style="padding:8px">dado que, habida cuenta de, en virtud de</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Conclusión</td><td style="padding:8px">en definitiva, en suma, a modo de conclusión</td></tr>'
             '</table>'),
        ],
        traps=[
            ('*se realizaron los estudios por los investigadores', '<strong>los estudios fueron realizados por los investigadores</strong>', 'La pasiva refleja (se + verb) NO admite complemento agente explícito con «por». Para mencionar el agente, usa la pasiva perifrástica con <b>ser</b>.'),
            ('usar «hacer» en registro formal', '<strong>llevar a cabo / realizar</strong>', 'En el registro formal, <b>hacer</b> suena coloquial. Usa <b>llevar a cabo, realizar, efectuar</b> según el contexto.'),
            ('*resulta que los datos ser fiables', '<strong>resulta que los datos son fiables</strong>', 'Tras <b>resulta que</b>, el verbo va en <b>indicativo</b> (expresa un hecho). No se usa infinitivo.'),
            ('*cabe señalando que…', '<strong>cabe señalar que…</strong>', 'La construcción impersonal formal es <b>cabe + infinitivo</b>: <i>cabe señalar, cabe mencionar, cabe destacar</i>.'),
            ('se considera → con agente', '<strong>se considera / es considerado por</strong>', 'La pasiva refleja no lleva agente explícito: *«se considera por los expertos» → «es considerado por los expertos» (pasiva perifrástica) o «los expertos consideran» (activa).'),
        ],
        summary=[
            ('pasiva perifrástica', 'ser + participio (+ por agente)', 'El informe fue aprobado por la dirección.'),
            ('pasiva refleja', 'se + 3.ª persona', 'Se aprobó el informe.'),
            ('pasiva de estado', 'estar + participio', 'El informe está aprobado.'),
            ('impersonal formal', 'es + adj + inf / cabe + inf / conviene + inf', 'Cabe señalar que…'),
            ('nominalizaciones', 'sustituyen verbos en texto formal', 'la aprobación del informe'),
            ('léxico formal', 'realizar, señalar, establecer, otorgar', 'Se llevó a cabo la reunión.'),
            ('conectores formales', 'no obstante, asimismo, por consiguiente', 'No obstante, los resultados son positivos.'),
        ],
        ex1=dict(
            title='Registro formal: elige la opción más adecuada',
            questions=[
                ('En un informe formal, ¿cuál es más apropiada?',
                 ['Se procedió a la revisión del documento.', 'Revisamos el documento.', 'Se revisó el documento rápido.', 'Hicimos la revisión del documento.'],
                 0, 'El registro formal usa nominalización (<b>revisión</b>) y pasiva refleja (<b>se procedió a</b>).'),
                ('¿Cuál es el equivalente formal de «porque»?',
                 ['dado que', 'es que', 'así que', 'o sea'],
                 0, '<b>Dado que</b> es un conector causal formal equivalente a «porque».'),
                ('¿Qué construcción NO puede llevar complemento agente con «por»?',
                 ['La pasiva refleja (se + verb)', 'La pasiva perifrástica (ser + part.)', 'La construcción activa', 'La nominalizacion'],
                 0, 'La <b>pasiva refleja</b> no admite agente con «por». Para mencionar el agente, usa la perifrástica.'),
                ('¿Cuál es el equivalente formal de «hacer una investigación»?',
                 ['llevar a cabo una investigación', 'realizar una investigación', 'efectuar una investigación', 'Las tres son correctas'],
                 3, '<b>Llevar a cabo, realizar y efectuar</b> son equivalentes formales de <i>hacer</i> con este significado.'),
                ('En un texto académico, ¿cómo expresarías impersonalmente «hay que revisar los datos»?',
                 ['Cabe proceder a la revisión de los datos.', 'Es que hay que revisar.', 'O sea, hay que revisar.', 'Digamos que habría que revisar.'],
                 0, 'Construcción impersonal formal: <b>cabe + infinitivo / proceder a</b>.'),
                ('¿Cuál conecta la consecuencia en estilo formal?',
                 ['por consiguiente', 'así que', 'o sea', 'pues'],
                 0, '<b>Por consiguiente</b> es el conector consecutivo formal. «Así que» es coloquial.'),
            ]
        ),
        ex2=dict(
            title='Transforma al registro formal',
            questions=[
                ('Transforma al registro formal: «Hicieron un estudio sobre el tema.»',
                 'Se llevó a cabo un estudio sobre el tema. / Se realizó un estudio sobre el tema.',
                 ['se llevó a cabo un estudio', 'se realizó un estudio', 'se efectuó un estudio'],
                 'Pasiva refleja + verbo formal: <b>se llevó a cabo</b> / <b>se realizó</b>.'),
                ('¿Cómo dices formalmente «dieron los resultados»?',
                 'Se presentaron/facilitaron/proporcionaron los resultados.',
                 ['se proporcionaron los resultados', 'se presentaron los resultados', 'se facilitaron los resultados'],
                 'Dar → <b>proporcionar, facilitar, presentar</b> en registro formal.'),
                ('Reescribe formalmente: «Los científicos dicen que el cambio climático existe.»',
                 'Los científicos señalan/manifiestan/indican que el cambio climático existe.',
                 ['los científicos señalan que', 'los científicos indican que', 'los científicos manifiestan que'],
                 'Decir → <b>señalar, indicar, manifestar, declarar</b> en registro formal.'),
                ('¿Cómo introduces una conclusión formal?',
                 'En definitiva, / En suma, / A modo de conclusión, / En consecuencia,',
                 ['en definitiva', 'en suma', 'a modo de conclusión'],
                 'Conclusión formal: <b>en definitiva, en suma, a modo de conclusión</b>.'),
                ('¿Cuándo usas «se aprobó» vs. «fue aprobado por»?',
                 '«Se aprobó» (sin agente); «fue aprobado por» (con agente explícito)',
                 ['se aprobó sin agente; fue aprobado por con agente', 'son idénticos', 'se aprobó es más formal'],
                 'Pasiva refleja = sin agente. Perifrástica con <b>fue aprobado por</b> = agente mencionado.'),
            ]
        ),
        ex3=dict(
            title='Identificación del registro formal',
            questions=[
                ('¿Cuál pertenece al registro más formal?',
                 ['Habida cuenta de los resultados, se procederá a la revisión.', 'Como los resultados son así, lo revisarán.', 'Ya que salió eso, van a revisarlo.', 'O sea, hay que revisar.'],
                 0, '<b>Habida cuenta de</b> es una construcción muy formal equivalente a «dado que».'),
                ('¿Qué impersonal formal es más apropiada en un texto académico?',
                 ['Cabe destacar que los datos son significativos.', 'Hay que destacar que los datos son significativos.', 'Se debe destacar que los datos son significativos.', 'Deberían destacar que los datos son significativos.'],
                 0, '<b>Cabe + infinitivo</b> es la construcción impersonal más formal y apropiada en texto académico.'),
                ('«El estudio fue elaborado por el equipo de investigación.» ¿Qué tipo de pasiva es?',
                 ['Perifrástica (ser + participio + por)', 'Refleja (se + verbo)', 'De estado (estar + participio)', 'Impersonal'],
                 0, '<b>Fue elaborado por</b> = pasiva perifrástica con agente.'),
                ('¿Cuál NO es una impersonal formal?',
                 ['Hacemos notar que…', 'Cabe señalar que…', 'Resulta evidente que…', 'Es necesario que…'],
                 0, '<b>Hacemos notar</b> es un sujeto de primera persona del plural, no impersonal.'),
                ('«Se considera que los datos son fiables.» ¿Se puede añadir «por los científicos»?',
                 ['No; la pasiva refleja no lleva agente con «por».', 'Sí, es correcto.', 'Sí, en registro formal es posible.', 'Solo en oraciones negativas.'],
                 0, 'La pasiva refleja <b>no admite agente con «por»</b>. Usa la perifrástica: <i>es considerado por los científicos</i>.'),
            ]
        ),
        game_desc='Construye textos formales con pasiva, impersonales y léxico apropiado',
        items=[
            dict(term='pasiva perifrástica', definition='ser + participio + por (agente explícito)',
                 example='El informe fue aprobado por la junta.',
                 accept=['pasiva perifrástica', 'ser participio por', 'fue aprobado']),
            dict(term='pasiva refleja', definition='se + verbo 3.ª persona (sin agente)',
                 example='Se aprobó el informe.',
                 accept=['pasiva refleja', 'se aprobó', 'se verbo']),
            dict(term='cabe + infinitivo', definition='construcción impersonal formal',
                 example='Cabe señalar que los datos son incompletos.',
                 accept=['cabe infinitivo', 'cabe señalar', 'impersonal formal']),
            dict(term='llevar a cabo', definition='equivalente formal de «hacer»',
                 example='Se llevó a cabo una investigación.',
                 accept=['llevar a cabo', 'realizó', 'efectuó']),
            dict(term='señalar / indicar / manifestar', definition='equivalentes formales de «decir»',
                 example='El portavoz señaló que la reunión fue un éxito.',
                 accept=['señalar', 'indicar', 'manifestar', 'formal de decir']),
            dict(term='dado que / puesto que', definition='causales formales equivalentes a «porque»',
                 example='Dado que los resultados son positivos, se continuará.',
                 accept=['dado que', 'puesto que', 'causal formal']),
            dict(term='no obstante / asimismo', definition='conectores formales de contraste y adición',
                 example='No obstante, los resultados son positivos.',
                 accept=['no obstante', 'asimismo', 'conector formal']),
            dict(term='por consiguiente / en consecuencia', definition='conectores formales consecutivos',
                 example='Por consiguiente, se tomaron medidas.',
                 accept=['por consiguiente', 'en consecuencia', 'consecutivo formal']),
        ]
    ),

    'oraciones-relativas-b2': dict(
        level='b2',
        section='grammar',
        num='G15',
        short='Relativas Avanzadas',
        title='Las Oraciones de Relativo Avanzadas',
        subtitle='Cláusulas especificativas y explicativas, antecedente en subjuntivo y relativos complejos',
        slides=[
            ('Especificativas vs. explicativas', None,
             '<p class="slide-explanation">Las oraciones de relativo pueden ser <b>especificativas</b> (sin coma — restringen el antecedente) '
             'o <b>explicativas</b> (con coma — añaden información adicional):</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>Los estudiantes <b>que estudian</b> aprueban. (especificativa — solo esos estudiantes)</p>'
             '<p>Los estudiantes<b>, que estudian,</b> aprueban. (explicativa — todos los estudiantes; todos estudian)</p>'
             '</div>'
             '<p class="slide-explanation">Las explicativas tienen <b>coma</b> y pueden separarse sin cambiar el significado de la oración principal. '
             'Con <b>que</b> o <b>el cual/la cual</b> (más formal en las explicativas).</p>'),

            ('Subjuntivo en oraciones de relativo', None,
             '<p class="slide-explanation">El verbo de la relativa va en <b>subjuntivo</b> cuando el antecedente es '
             '<b>indefinido, hipotético o negativo</b>:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Antecedente</th><th style="padding:8px;text-align:left">Modo</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Conocido/específico</td><td style="padding:8px"><b>Indicativo</b></td><td style="padding:8px">El libro que <b>leí</b> era interesante.</td></tr>'
             '<tr><td style="padding:8px">Indefinido/hipotético</td><td style="padding:8px"><b>Subjuntivo</b></td><td style="padding:8px">Busco un libro que <b>sea</b> interesante.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Negativo</td><td style="padding:8px"><b>Subjuntivo</b></td><td style="padding:8px">No hay nadie que <b>sepa</b> la respuesta.</td></tr>'
             '<tr><td style="padding:8px">Superlativo restrictivo</td><td style="padding:8px"><b>Indicativo</b></td><td style="padding:8px">El mejor libro que <b>he leído</b>.</td></tr>'
             '</table>'),

            ('Relativos con preposición', None,
             '<p class="slide-explanation">Cuando el relativo va precedido de preposición, las formas cambian:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Antecedente</th><th style="padding:8px;text-align:left">Con preposición</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Persona</td><td style="padding:8px"><b>a quien / con quien</b></td><td style="padding:8px">La persona <b>con quien</b> hablé.</td></tr>'
             '<tr><td style="padding:8px">Cosa</td><td style="padding:8px"><b>el/la/los/las que</b></td><td style="padding:8px">El tema <b>del que</b> hablamos.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Formal (cualquier)</td><td style="padding:8px"><b>el cual / la cual</b></td><td style="padding:8px">La empresa <b>para la cual</b> trabajo.</td></tr>'
             '<tr><td style="padding:8px">Lugar</td><td style="padding:8px"><b>donde / en el que</b></td><td style="padding:8px">El lugar <b>donde</b> nací.</td></tr>'
             '</table>'),

            ('Cuyo/a — posesión en relativas', None,
             '<p class="slide-explanation"><b>Cuyo/a/os/as</b> es el relativo posesivo. '
             'Concuerda en género y número con el <b>sustantivo poseído</b>, no con el antecedente:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>El autor <b>cuya</b> novela leí. (novela = fem. sg.)</p>'
             '<p>La empresa <b>cuyos</b> empleados trabajan aquí. (empleados = masc. pl.)</p>'
             '<p>El científico <b>cuyo</b> descubrimiento cambió la medicina. (descubrimiento = masc. sg.)</p>'
             '</div>'
             '<p class="slide-explanation"><b>Cuyo</b> es formal. En coloquial se usa «que tiene»: <i>el autor que tiene una novela famosa</i>.</p>'),

            ('Lo que / lo cual — relativos neutros', None,
             '<p class="slide-explanation"><b>Lo que</b> y <b>lo cual</b> son relativos neutros. '
             'Retoman una oración completa o una idea:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>Llegó tarde, <b>lo que</b> sorprendió a todos. (retoma toda la oración anterior)</p>'
             '<p>No avisó, <b>lo cual</b> fue una falta de respeto. (más formal)</p>'
             '<p>Diferencia: <b>lo que</b> puede ser libre (sin antecedente claro); <b>lo cual</b> siempre retoma un antecedente.</p>'
             '</div>'
             '<p class="slide-explanation"><b>Lo que</b> libre: <i>No entiendo lo que dices</i>. (what you say — sin antecedente)</p>'),
        ],
        traps=[
            ('*el libro que está en la mesa que leí', 'Reestructura la oración', 'Con dos que seguidos, reestructura: <b>el libro que leí, el cual estaba en la mesa</b>. Usa <i>el cual</i> para separar las cláusulas.'),
            ('*cuyo persona', '<strong>cuya persona</strong>', '<b>Cuyo</b> concuerda con el sustantivo poseído, no con el antecedente. Si el sustantivo es femenino: <b>cuya</b>.'),
            ('Busco el libro que es interesante (indefinido)', '<strong>Busco un libro que sea interesante</strong>', 'Antecedente indefinido (buscando algo que quizá no existe) → <b>subjuntivo</b>: <i>que sea</i>.'),
            ('*lo cual no entiendo', '<strong>lo que no entiendo</strong>', '<b>Lo cual</b> retoma un antecedente previo en la oración. Si no hay antecedente claro, usa <b>lo que</b>: <i>no entiendo lo que dices</i>.'),
            ('con quien vs. con el que', 'ambas son correctas para personas', 'Con personas puedes usar <b>con quien</b> o <b>con el/la que</b>: <i>la persona con quien hablé = la persona con la que hablé</i>.'),
        ],
        summary=[
            ('especificativa (sin coma)', 'restringe el antecedente', 'Los alumnos que estudian aprueban.'),
            ('explicativa (con coma)', 'añade información — no restringe', 'Los alumnos, que estudian, aprueban.'),
            ('relativa + indicativo', 'antecedente conocido y específico', 'El libro que leí era bueno.'),
            ('relativa + subjuntivo', 'antecedente indefinido, hipotético o negativo', 'Busco un libro que sea bueno.'),
            ('cuyo/-a/-os/-as', 'relativo posesivo — concuerda con lo poseído', 'El autor cuya novela leí.'),
            ('lo que / lo cual', 'relativos neutros — retoman toda una idea', 'Llegó tarde, lo que sorprendió a todos.'),
            ('prep. + quien / el que / el cual', 'relativos precedidos de preposición', 'La empresa para la cual trabajo.'),
        ],
        ex1=dict(
            title='Oraciones de relativo avanzadas',
            questions=[
                ('«Busco a alguien que _____ hablar chino.» (saber)',
                 ['sepa', 'sabe', 'sabía', 'sabrá'],
                 0, 'Antecedente indefinido → <b>subjuntivo</b>: <b>sepa</b>.'),
                ('«El médico _____ consulté es excelente.» (antecedente específico)',
                 ['al que', 'que', 'quien', 'al cual'],
                 1, 'Relativa especificativa con antecedente conocido + verbo en indicativo. Con «al que» o «a quien» también si hay preposición: aquí directamente <b>que consulté</b>.'),
                ('«La empresa _____ trabajo ha crecido mucho.» (con preposición «para»)',
                 ['para la que', 'para la cual', 'para quien', 'Las opciones A y B son correctas'],
                 3, '<b>Para la que</b> y <b>para la cual</b> son ambas correctas. «Para la cual» es más formal.'),
                ('«El científico _____ descubrimiento cambió la medicina.» (posesión)',
                 ['cuyo', 'cuyos', 'cuya', 'de quien'],
                 0, 'Posesivo relativo: <i>descubrimiento</i> es masc. sg. → <b>cuyo</b>.'),
                ('«No hay nadie que _____ la solución.» (saber)',
                 ['sepa', 'sabe', 'supiera', 'sabrá'],
                 0, 'Antecedente negativo → <b>subjuntivo presente</b>: <b>sepa</b>.'),
                ('«Llegó tarde, _____ molestó a todos.»',
                 ['lo que', 'lo cual', 'que', 'Las opciones A y B son correctas'],
                 3, 'Relativo neutro que retoma toda la oración anterior: <b>lo que</b> o <b>lo cual</b>. Ambas son correctas; <i>lo cual</i> es más formal.'),
            ]
        ),
        ex2=dict(
            title='Usa el modo y el relativo correctos',
            questions=[
                ('¿Indicativo o subjuntivo? «El libro que _____ (buscar, yo) debe ser corto.» (lo busco en la librería ahora)',
                 'busco (indicativo — antecedente específico: busco uno concreto)',
                 ['busco indicativo', 'busque subjuntivo', 'buscaba indicativo'],
                 'Si tienes un libro específico en mente → <b>indicativo: busco</b>. Si es cualquier libro → subjuntivo.'),
                ('Completa con cuyo/cuya/cuyos/cuyas: «La autora _____ libros admiro acaba de publicar uno nuevo.»',
                 'cuyos (libros = masc. pl.)',
                 ['cuyos', 'cuya', 'cuyo'],
                 '<i>Libros</i> es masc. pl. → <b>cuyos</b>.'),
                ('¿Por qué «lo cual» y no «lo que» en «No avisó, lo cual fue una falta de respeto»?',
                 'Lo cual retoma el antecedente claro (el hecho de que no avisó). Lo que también sería correcto; lo cual es más formal.',
                 ['lo cual retoma antecedente previo; lo que también correcto pero lo cual es más formal', 'solo lo cual es correcto', 'solo lo que es correcto'],
                 'Ambas son correctas. <b>Lo cual</b> = formal, siempre con antecedente. <b>Lo que</b> = más versátil.'),
                ('Añade coma para hacer explicativa: «Los estudiantes que estudian aprueban.»',
                 'Los estudiantes, que estudian, aprueban.',
                 ['Los estudiantes, que estudian, aprueban.', 'Los estudiantes que, estudian, aprueban.', 'Los estudiantes, que estudian aprueban.'],
                 'La explicativa añade comas antes y después de la cláusula relativa.'),
                ('¿Subjuntivo o indicativo? «Cuando encontremos a alguien que _____ (poder) ayudarnos, le llamaremos.»',
                 'pueda (subjuntivo — antecedente indefinido: buscamos a alguien que quizá no existe todavía)',
                 ['pueda subjuntivo', 'puede indicativo', 'pudiera subjuntivo'],
                 'Antecedente hipotético/indefinido → <b>subjuntivo: pueda</b>.'),
            ]
        ),
        ex3=dict(
            title='Relativos avanzados: identificación',
            questions=[
                ('¿Cuál es una relativa especificativa?',
                 ['Los estudiantes que trabajan duermen poco.', 'Los estudiantes, que trabajan, duermen poco.', 'Los estudiantes, los cuales trabajan, duermen poco.', 'Los estudiantes, que suelen trabajar, duermen poco.'],
                 0, 'Sin coma = especificativa (solo esos estudiantes que trabajan).'),
                ('«No encuentro a nadie que sepa la respuesta.» ¿Por qué va en subjuntivo?',
                 ['Porque el antecedente es negativo (nadie).', 'Porque es una pregunta.', 'Porque el verbo principal está en presente.', 'Porque «encontrar» siempre exige subjuntivo.'],
                 0, 'Antecedente <b>negativo</b> (nadie) → <b>subjuntivo</b>.'),
                ('¿Cuál es el relativo posesivo en «La empresa cuyas oficinas visité»?',
                 ['cuyas (fem. pl. — concuerda con «oficinas»)', 'cuya (fem. sg.)', 'cuyos (masc. pl.)', 'cuyo (masc. sg.)'],
                 0, '<b>Cuyas</b>: <i>oficinas</i> es fem. pl. → <b>cuyas</b>.'),
                ('¿Cuál usa correctamente el relativo con preposición?',
                 ['El libro del que hablamos es de García Márquez.', 'El libro que hablamos es de García Márquez.', 'El libro el que hablamos es de García Márquez.', 'El libro que del hablamos es de García Márquez.'],
                 0, 'Con preposición «de»: <b>del que</b> (contracción de + el que).'),
                ('«Llegó tarde, lo que/lo cual molestó a todos.» ¿Cuál es más formal?',
                 ['lo cual', 'lo que', 'Son igualmente formales.', 'que (sin artículo)'],
                 0, '<b>Lo cual</b> es el relativo neutro más formal. <i>Lo que</i> es más frecuente en el habla.'),
            ]
        ),
        game_desc='Usa los relativos complejos, el modo y la puntuación correctos',
        items=[
            dict(term='especificativa (sin coma)', definition='relativa que restringe el antecedente',
                 example='Los alumnos que estudian aprueban.',
                 accept=['especificativa', 'sin coma', 'relativa especificativa']),
            dict(term='explicativa (con coma)', definition='relativa que añade información sin restringir',
                 example='Los alumnos, que estudian, aprueban.',
                 accept=['explicativa', 'con coma', 'relativa explicativa']),
            dict(term='subjuntivo en relativa indefinida', definition='antecedente hipotético/negativo → subjuntivo',
                 example='Busco un libro que sea interesante.',
                 accept=['subjuntivo relativa', 'antecedente indefinido', 'que sea']),
            dict(term='cuyo / cuya / cuyos / cuyas', definition='relativo posesivo — concuerda con lo poseído',
                 example='El autor cuya novela leí.',
                 accept=['cuyo', 'cuya', 'cuyos', 'cuyas', 'posesivo relativo']),
            dict(term='del que / de la que', definition='relativo con preposición DE',
                 example='El tema del que hablamos.',
                 accept=['del que', 'de la que', 'relativo preposicion de']),
            dict(term='para la que / para la cual', definition='relativo con preposición PARA',
                 example='La empresa para la que trabajo.',
                 accept=['para la que', 'para la cual', 'relativo preposicion para']),
            dict(term='lo que / lo cual', definition='relativos neutros — retoman una oración',
                 example='Llegó tarde, lo cual sorprendió a todos.',
                 accept=['lo que', 'lo cual', 'relativo neutro']),
            dict(term='con quien / con el que', definition='relativo de persona con preposición CON',
                 example='La persona con quien hablé.',
                 accept=['con quien', 'con el que', 'con la que', 'relativo persona preposicion']),
        ]
    ),
}
