# -*- coding: utf-8 -*-
"""espanol/ C1 Gramática — lote 2 (G06–G10)."""

CHAPTERS = {
    'construcciones-pasivas-c1': dict(
        level='c1',
        section='grammar',
        num='G06',
        short='Construcciones Pasivas',
        title='Las Construcciones Pasivas en Profundidad',
        subtitle='Domina la pasiva perifrástica, de estado, refleja e impersonal en el texto formal',
        slides=[
            ('Pasiva perifrástica: SER + participio + por', None,
             '<p class="slide-explanation">La <b>pasiva perifrástica</b> se forma con <b>SER + participio</b> '
             'y destaca la <b>acción como proceso</b>. El agente, cuando se menciona, va introducido por <b>por</b>.</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Tiempo</th>'
             '<th style="padding:8px;text-align:left">Forma</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Presente</td><td style="padding:8px">es + part.</td><td style="padding:8px">El informe <b>es revisado</b> cada mes.</td></tr>'
             '<tr><td style="padding:8px">Pretérito indef.</td><td style="padding:8px">fue + part.</td><td style="padding:8px">La ley <b>fue aprobada</b> por el parlamento.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Imperfecto</td><td style="padding:8px">era + part.</td><td style="padding:8px">El correo <b>era entregado</b> por las mañanas.</td></tr>'
             '<tr><td style="padding:8px">Futuro</td><td style="padding:8px">será + part.</td><td style="padding:8px">El proyecto <b>será evaluado</b> el próximo mes.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Condicional</td><td style="padding:8px">sería + part.</td><td style="padding:8px">La propuesta <b>sería analizada</b> por el comité.</td></tr>'
             '</table>'
             '<p class="slide-explanation">El participio <b>concuerda en género y número</b> con el sujeto paciente. '
             'Se reserva principalmente para textos académicos, periodísticos y jurídicos.</p>'),

            ('Pasiva de estado: ESTAR + participio', None,
             '<p class="slide-explanation">La <b>pasiva de estado</b> con <b>ESTAR + participio</b> describe el '
             '<b>resultado o estado actual</b> de una acción ya completada. No expresa la acción misma, '
             'sino las consecuencias de haberla realizado:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>SER (proceso):</b> La ventana <b>fue abierta</b> por el ladrón. → acción</p>'
             '<p><b>ESTAR (estado):</b> La ventana <b>está abierta</b>. → resultado visible ahora</p>'
             '</div>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Participio</th>'
             '<th style="padding:8px;text-align:left">Estado resultante</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">terminado/a</td><td style="padding:8px">El informe <b>está terminado</b>; puedes enviarlo.</td></tr>'
             '<tr><td style="padding:8px">redactado/a</td><td style="padding:8px">El contrato ya <b>está redactado</b>.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">resuelto/a</td><td style="padding:8px">El problema <b>está resuelto</b> desde ayer.</td></tr>'
             '</table>'
             '<p class="slide-explanation">Algunos participios con ESTAR describen estados físicos sin que importe la acción previa: '
             '<i>estar sentado, estar acostado, estar preocupado</i>.</p>'),

            ('Pasiva refleja e impersonal con SE', None,
             '<p class="slide-explanation">La <b>pasiva refleja</b> con <b>se</b> omite al agente y el verbo '
             'concuerda con el sujeto gramatical. La <b>construcción impersonal</b> usa <b>se + verbo en 3.ª persona '
             'del singular</b> sin sujeto explícito:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Tipo</th>'
             '<th style="padding:8px;text-align:left">Estructura</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Pasiva refleja (pl.)</td><td style="padding:8px">se + verbo pl.</td><td style="padding:8px"><b>Se venden</b> entradas.</td></tr>'
             '<tr><td style="padding:8px">Pasiva refleja (sg.)</td><td style="padding:8px">se + verbo sg.</td><td style="padding:8px"><b>Se busca</b> un técnico.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Impersonal</td><td style="padding:8px">se + verbo sg. (sin sujeto)</td><td style="padding:8px"><b>Se trabaja</b> mucho en esta empresa.</td></tr>'
             '<tr><td style="padding:8px">Impersonal</td><td style="padding:8px">se + verbo sg.</td><td style="padding:8px"><b>Se come</b> bien aquí.</td></tr>'
             '</table>'
             '<p class="slide-explanation">La diferencia entre ambas construcciones es sutil: en la pasiva refleja existe un sujeto '
             'gramatical (la cosa vendida/buscada); en la impersonal, no hay sujeto — la acción se atribuye a nadie en particular.</p>'),

            ('Pasiva de resultado: TENER + participio', None,
             '<p class="slide-explanation">La <b>pasiva de resultado con TENER</b> pone el énfasis en quien posee '
             'el resultado de la acción, no en quien la realizó. La estructura es: '
             '<b>sujeto + tener + objeto directo + participio</b> (concuerda con el objeto):</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>Tengo <b>escrito</b> el informe. (= He escrito el informe y lo tengo listo)</p>'
             '<p>Lleva <b>leídas</b> tres novelas este mes.</p>'
             '<p>Ya tienen <b>reservadas</b> las entradas.</p>'
             '<p>El director tiene <b>firmado</b> el contrato.</p>'
             '</div>'
             '<p class="slide-explanation">Esta construcción aporta un matiz acumulativo y es muy productiva '
             'en el registro formal. Compara: <i>He terminado el trabajo</i> (proceso) vs. '
             '<i>Tengo terminado el trabajo</i> (resultado en manos del sujeto).</p>'),

            ('Verbos sin voz pasiva y registro formal', None,
             '<p class="slide-explanation">Ciertos verbos <b>no admiten voz pasiva</b> en español por su naturaleza semántica. '
             'Además, conviene saber qué construcción pasiva prefiere el texto formal:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Sin pasiva</th>'
             '<th style="padding:8px;text-align:left">Motivo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>gustar, doler, encantar</b></td><td style="padding:8px">Son verbos inversos; el sujeto ya es el paciente.</td></tr>'
             '<tr><td style="padding:8px"><b>pertenecer, costar, carecer</b></td><td style="padding:8px">Expresan estados, no acciones transitivas.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>haber (impersonal)</b></td><td style="padding:8px">Nunca tiene sujeto — no puede pasivizarse.</td></tr>'
             '</table>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Registro formal:</b> prefiere SER + participio con agente explícito.</p>'
             '<p><b>Registro periodístico:</b> muy frecuente la pasiva refleja con se.</p>'
             '<p><b>Coloquial:</b> prefiere la voz activa; la pasiva con SER suena afectado.</p>'
             '</div>'),
        ],
        traps=[
            ('La carta está escrita por Ana. (para expresar la acción)',
             'La carta <strong>fue escrita</strong> por Ana.',
             'Para expresar la acción pasada con agente explícito, se usa <b>SER + participio</b>: '
             '<i>fue escrita por Ana</i>. ESTAR describe el estado resultante, no la acción.'),
            ('Se vende pisos en esta zona.',
             '<strong>Se venden</strong> pisos en esta zona.',
             'En la pasiva refleja, el verbo concuerda con el sujeto gramatical «pisos» (plural): <b>se venden</b>.'),
            ('Me gusta fue dicho por muchas personas.',
             'Lo que dijeron muchas personas <strong>fue</strong> que les gustaba.',
             '<b>Gustar</b> no admite voz pasiva. Los verbos inversos (gustar, doler, encantar) '
             'ya tienen el objeto como sujeto gramatical y no se pasivizán.'),
            ('Tengo escrito los informes. (con objeto plural)',
             'Tengo <strong>escritos</strong> los informes.',
             'En la construcción TENER + participio, el participio concuerda en género y número con el objeto directo: '
             '«los informes» es masculino plural → <b>escritos</b>.'),
            ('El problema está resuelto por el ingeniero. (para acción)',
             'El problema <strong>fue resuelto</strong> por el ingeniero.',
             'Para mencionar al agente, se usa la pasiva con <b>SER</b>, no con ESTAR. '
             'ESTAR + participio no admite complemento agente con <i>por</i>.'),
        ],
        summary=[
            ('Pasiva perifrástica', 'SER + participio (+ por + agente) → acción', 'El puente fue construido por ingenieros suizos.'),
            ('Pasiva de estado', 'ESTAR + participio → estado resultante', 'La oficina está cerrada hasta las diez.'),
            ('Pasiva refleja', 'SE + verbo (concuerda con sujeto)', 'Se venden pisos en el centro histórico.'),
            ('Impersonal con se', 'SE + verbo en 3.ª sg. (sin sujeto)', 'En esta región se trabaja mucho.'),
            ('Pasiva de resultado', 'TENER + OD + participio (concuerda con OD)', 'Tengo escritas las conclusiones del informe.'),
            ('Verbos sin pasiva', 'gustar, doler, pertenecer, costar: no se pasivizán', 'INCORRECTO: *Es gustado por todos.'),
            ('Registro', 'Formal → SER; periodístico → SE; coloquial → voz activa', 'El decreto fue promulgado vs. Se promulgó el decreto.'),
        ],
        ex1=dict(
            title='Elige la construcción pasiva adecuada',
            questions=[
                ('La novela ______ por un autor desconocido en el siglo XIX.',
                 ['está escrita', 'fue escrita', 'se escribió', 'tiene escrita'],
                 1,
                 'Acción histórica con agente explícito → pasiva con <b>SER</b>: <b>fue escrita</b> por.'),
                ('La tienda ______ los domingos; no abren en festivos.',
                 ['fue cerrada', 'se cierra', 'está cerrada', 'es cerrada'],
                 2,
                 'Estado habitual resultante sin agente → <b>ESTAR + participio</b>: <b>está cerrada</b>.'),
                ('______ se entiende el español en toda América Latina.',
                 ['Es hablado y', 'Se habla y', 'Está hablado y', 'Ha sido hablado y'],
                 1,
                 'Agente irrelevante, hecho general → pasiva refleja con <b>se</b>: <b>se habla y se entiende</b>.'),
                ('El director ya ______ los contratos; están listos para firmar.',
                 ['fue firmado', 'está firmado', 'tiene firmados', 'se firmaron'],
                 2,
                 'Énfasis en el resultado acumulado en manos del sujeto → <b>TENER + participio</b>: <b>tiene firmados</b> los contratos.'),
                ('¿Cuál es incorrecto con el verbo PERTENECER?',
                 ['El inmueble pertenece al ayuntamiento.', 'El inmueble es pertenecido por el ayuntamiento.', 'El inmueble no es de propiedad privada.', 'El inmueble le pertenece al ayuntamiento.'],
                 1,
                 '<b>Pertenecer</b> no admite voz pasiva. «Es pertenecido por» es incorrecto; se sustituye por la voz activa.'),
                ('Los documentos ______ antes de la reunión de mañana.',
                 ['estarán revisados', 'serán revisados', 'se revisarán', 'tendrán revisados'],
                 1,
                 'Acción futura con énfasis en el proceso → pasiva perifrástica en futuro: <b>serán revisados</b>.'),
            ]
        ),
        ex2=dict(
            title='Transforma la oración usando la construcción indicada',
            questions=[
                ('Los investigadores redactaron el informe. → El informe ______ por los investigadores. (pasiva perifrástica, pasado)',
                 'fue redactado',
                 ['fue redactado'],
                 'Pasiva con SER en pretérito indefinido: «el informe» es masculino singular → <b>fue redactado</b>.'),
                ('Alguien ha cerrado la tienda. → La tienda ______. (estado actual)',
                 'está cerrada',
                 ['está cerrada'],
                 'Estado resultante actual → <b>está cerrada</b> (ESTAR + participio, femenino singular).'),
                ('Aquí venden productos artesanales. → Aquí ______ productos artesanales. (pasiva refleja)',
                 'se venden',
                 ['se venden'],
                 'Agente irrelevante, sujeto plural → pasiva refleja: <b>se venden</b>.'),
                ('He leído tres capítulos. → Tengo ______ tres capítulos. (pasiva de resultado)',
                 'leídos',
                 ['leídos'],
                 'TENER + participio concuerda con el OD «tres capítulos» (masculino plural): <b>leídos</b>.'),
                ('(Nadie en particular trabaja mucho.) → En esta empresa ______ mucho. (impersonal con se)',
                 'se trabaja',
                 ['se trabaja'],
                 'Construcción impersonal: sujeto indeterminado + verbo en 3.ª sg. → <b>se trabaja</b>.'),
            ]
        ),
        ex3=dict(
            title='Identifica el uso correcto',
            questions=[
                ('¿Cuál describe un estado resultante con ESTAR?',
                 ['El contrato fue firmado esta mañana.',
                  'El contrato está firmado y listo para entregarse.',
                  'El contrato se firmó esta mañana.',
                  'Tienen firmado el contrato.'],
                 1,
                 'Estado actual como resultado de la acción → <b>ESTAR + participio</b>: «está firmado».'),
                ('¿Cuál usa la pasiva de resultado TENER correctamente?',
                 ['Tengo escribiendo el informe.',
                  'Tengo el informe escrito.',
                  'Tengo escritos los informes.',
                  'Tanto B como C son correctas.'],
                 3,
                 'TENER + participio: «Tengo el informe escrito» (sg.) y «Tengo escritos los informes» (pl.) son ambas correctas — el participio concuerda con el OD.'),
                ('¿Cuál de estos verbos NO admite voz pasiva?',
                 ['construir', 'redactar', 'doler', 'aprobar'],
                 2,
                 '<b>Doler</b> es un verbo inverso: el sujeto ya es el paciente. No puede pasivizarse.'),
                ('¿Cuál es la diferencia entre «fue aprobada la ley» y «se aprobó la ley»?',
                 ['No hay diferencia de significado.',
                  '«Fue aprobada» permite mencionar al agente con «por»; «se aprobó» omite al agente.',
                  '«Se aprobó» solo se usa en presente.',
                  '«Fue aprobada» es informal; «se aprobó» es formal.'],
                 1,
                 'La pasiva con SER permite añadir «por + agente»; la pasiva refleja con se omite al agente. Ambas son formales.'),
                ('¿Cuál combina correctamente la pasiva refleja con el número del verbo?',
                 ['Se vende pisos nuevos.',
                  'Se venden piso nuevo.',
                  'Se venden pisos nuevos.',
                  'Se vende los pisos nuevos.'],
                 2,
                 'El verbo en la pasiva refleja concuerda con el sujeto: «pisos» es plural → <b>se venden</b>.'),
            ]
        ),
        game_desc='4 construcciones pasivas clave · 3 rondas cada una · llega a 100 puntos para ganar.',
        items=[
            dict(term='fue aprobada',
                 definition='pasiva perifrástica (SER) en pretérito: acción pasada con agente posible',
                 example='La reforma <b>fue aprobada</b> por unanimidad.',
                 accept=['fue aprobada']),
            dict(term='está resuelto',
                 definition='pasiva de estado (ESTAR): resultado actual de una acción ya completada',
                 example='El problema técnico <b>está resuelto</b> desde esta mañana.',
                 accept=['está resuelto']),
            dict(term='se construyó',
                 definition='pasiva refleja (SE): agente desconocido o irrelevante, sujeto singular',
                 example='El estadio <b>se construyó</b> en menos de dos años.',
                 accept=['se construyó']),
            dict(term='se debaten',
                 definition='pasiva refleja (SE): agente irrelevante, sujeto plural',
                 example='En el congreso <b>se debaten</b> varias propuestas de ley.',
                 accept=['se debaten']),
            dict(term='se trabaja',
                 definition='construcción impersonal (SE): sin sujeto, verbo en 3.ª persona singular',
                 example='En esa empresa <b>se trabaja</b> mucho y con exigencia.',
                 accept=['se trabaja']),
            dict(term='tiene redactado',
                 definition='pasiva de resultado (TENER): énfasis en el resultado acumulado en manos del sujeto',
                 example='La directora ya <b>tiene redactado</b> el informe anual.',
                 accept=['tiene redactado']),
            dict(term='serán evaluados',
                 definition='pasiva perifrástica en futuro: acción futura expresada con SER + participio',
                 example='Los candidatos <b>serán evaluados</b> la semana próxima.',
                 accept=['serán evaluados']),
            dict(term='están firmadas',
                 definition='pasiva de estado (ESTAR): resultado visible, participio en femenino plural',
                 example='Las actas ya <b>están firmadas</b> por todos los asistentes.',
                 accept=['están firmadas']),
        ],
    ),

    'subjuntivo-concesivas': dict(
        level='c1',
        section='grammar',
        num='G07',
        short='Oraciones Concesivas',
        title='Oraciones Concesivas con Subjuntivo',
        subtitle='Expresa obstáculos reales e hipotéticos con aunque, por más que, aun cuando y otras conjunciones',
        slides=[
            ('Aunque + indicativo vs. aunque + subjuntivo', None,
             '<p class="slide-explanation">La conjunción <b>aunque</b> puede ir seguida de indicativo o subjuntivo, '
             'con significados distintos:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Modo</th>'
             '<th style="padding:8px;text-align:left">Valor</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Indicativo</b></td>'
             '<td style="padding:8px">Hecho conocido o real</td>'
             '<td style="padding:8px">Aunque <b>llueve</b>, saldré. (sé que llueve)</td></tr>'
             '<tr><td style="padding:8px"><b>Subjuntivo</b></td>'
             '<td style="padding:8px">Hipótesis o concesión irreal</td>'
             '<td style="padding:8px">Aunque <b>llueva</b>, saldré. (puede que llueva)</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Subj. imperfecto</b></td>'
             '<td style="padding:8px">Concesión contraria a la realidad</td>'
             '<td style="padding:8px">Aunque <b>lloviera</b> a cántaros, saldría. (irrealidad)</td></tr>'
             '</table>'
             '<p class="slide-explanation">La clave: indicativo = «aunque ya sé que es así»; '
             'subjuntivo = «aunque sea así, no importa / aunque llegue a serlo».</p>'),

            ('Por más/mucho que y aun cuando', None,
             '<p class="slide-explanation"><b>Por más/mucho que</b> introduce una concesión de grado máximo '
             'y siempre exige <b>subjuntivo</b>. <b>Aun cuando</b> es una variante más formal de <i>aunque</i> '
             'y acepta ambos modos con los mismos matices:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Por más que lo intente</b>, no consigue aprender a conducir.</p>'
             '<p><b>Por mucho que estudie</b>, el examen le parece imposible.</p>'
             '<p><b>Por más esfuerzo que haga</b>, el resultado no mejora.</p>'
             '<p><b>Aun cuando llegara tarde</b>, te esperaría. (subjuntivo: irrealidad)</p>'
             '<p><b>Aun cuando llega tarde</b>, siempre termina el trabajo. (indicativo: hecho)</p>'
             '</div>'
             '<p class="slide-explanation"><b>Por más que</b> y <b>por mucho que</b> son intercambiables. '
             'Con sustantivos: <i>por más tiempo que tenga, por mucha paciencia que demuestre</i>.</p>'),

            ('A pesar de que y si bien', None,
             '<p class="slide-explanation"><b>A pesar de que</b> admite indicativo (hecho real) y subjuntivo (concesión hipotética). '
             '<b>Si bien</b> introduce una concesión con matiz adversativo y va siempre con indicativo:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Conjunción</th>'
             '<th style="padding:8px;text-align:left">Modo</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>a pesar de que</b></td>'
             '<td style="padding:8px">Indicativo (hecho)</td>'
             '<td style="padding:8px">A pesar de que <b>tiene</b> fiebre, fue a trabajar.</td></tr>'
             '<tr><td style="padding:8px"><b>a pesar de que</b></td>'
             '<td style="padding:8px">Subjuntivo (hipótesis)</td>'
             '<td style="padding:8px">A pesar de que <b>tenga</b> razón, no lo admitirá.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>si bien</b></td>'
             '<td style="padding:8px">Siempre indicativo</td>'
             '<td style="padding:8px">Si bien <b>es cierto</b> que hay problemas, no es menos verdad que hay soluciones.</td></tr>'
             '</table>'
             '<p class="slide-explanation"><b>Si bien</b> es exclusivo del registro formal y escrito. '
             'No se usa en la lengua oral coloquial.</p>'),

            ('Así + subjuntivo y correlativas bien... bien / ya... ya', None,
             '<p class="slide-explanation"><b>Así + subjuntivo</b> es una concesión enfática de uso coloquial o literario '
             'que equivale a «aunque + subjuntivo». Las correlativas <b>bien... bien</b> y <b>ya... ya</b> '
             'expresan indiferencia ante dos alternativas:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Así me lo juren</b>, no lo creo. (= aunque me lo juren)</p>'
             '<p><b>Así llueva</b> o truene, el acto se celebrará.</p>'
             '<p><b>Bien sea</b> por motivos personales, <b>bien sea</b> por razones laborales, la decisión es suya.</p>'
             '<p><b>Ya sea</b> una cosa, <b>ya sea</b> otra, el resultado será el mismo.</p>'
             '</div>'
             '<p class="slide-explanation"><b>Bien... bien</b> y <b>ya... ya</b> expresan que la concesión vale '
             'para cualquiera de las dos opciones. Son más frecuentes en el lenguaje formal y periodístico.</p>'),

            ('Cuadro de conjunciones concesivas', None,
             '<p class="slide-explanation">Resumen de las principales conjunciones concesivas y sus modos verbales:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Conjunción</th>'
             '<th style="padding:8px;text-align:left">Indicativo</th>'
             '<th style="padding:8px;text-align:left">Subjuntivo</th>'
             '<th style="padding:8px;text-align:left">Registro</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>aunque</b></td><td style="padding:8px">hecho real</td><td style="padding:8px">hipótesis/irrealidad</td><td style="padding:8px">todos</td></tr>'
             '<tr><td style="padding:8px"><b>a pesar de que</b></td><td style="padding:8px">hecho real</td><td style="padding:8px">hipótesis</td><td style="padding:8px">formal/neutro</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>por más/mucho que</b></td><td style="padding:8px">—</td><td style="padding:8px">siempre subj.</td><td style="padding:8px">neutro/formal</td></tr>'
             '<tr><td style="padding:8px"><b>aun cuando</b></td><td style="padding:8px">hecho real</td><td style="padding:8px">hipótesis/irrealidad</td><td style="padding:8px">formal</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>si bien</b></td><td style="padding:8px">siempre ind.</td><td style="padding:8px">—</td><td style="padding:8px">muy formal</td></tr>'
             '<tr><td style="padding:8px"><b>así + subj.</b></td><td style="padding:8px">—</td><td style="padding:8px">siempre subj.</td><td style="padding:8px">coloquial/lit.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>ya sea... ya sea</b></td><td style="padding:8px">—</td><td style="padding:8px">siempre subj.</td><td style="padding:8px">formal</td></tr>'
             '</table>'),
        ],
        traps=[
            ('Aunque lloverá, saldré. (para expresar hipótesis)',
             'Aunque <strong>llueva</strong>, saldré.',
             'Para expresar que la lluvia es una posibilidad futura sin certeza, se usa <b>aunque + subjuntivo</b>. '
             'El futuro de indicativo no es la forma concesiva estándar en este contexto.'),
            ('Por más que lo intentará, no lo conseguirá.',
             'Por más que lo <strong>intente</strong>, no lo conseguirá.',
             '<b>Por más/mucho que</b> exige siempre subjuntivo. Nunca se combina con futuro o condicional.'),
            ('Si bien sea cierto que hay problemas...',
             '<strong>Si bien es cierto</strong> que hay problemas...',
             '<b>Si bien</b> va siempre con indicativo. «Si bien sea» es incorrecto.'),
            ('A pesar de que tenga razón, tiene razón. (contradictorio)',
             'A pesar de que <strong>tiene</strong> razón (hecho) / a pesar de que <strong>tenga</strong> razón (hipótesis)',
             'El modo cambia el significado: indicativo = el hablante acepta que tiene razón (hecho); '
             'subjuntivo = el hablante considera la posibilidad sin afirmarla.'),
            ('Aunque llovería mucho, fue igualmente.',
             'Aunque <strong>llovía</strong> mucho, fue igualmente.',
             'Para un hecho pasado real, se usa <b>aunque + indicativo</b> (imperfecto aquí). '
             'El condicional no es forma concesiva en este contexto.'),
        ],
        summary=[
            ('aunque + indicativo', 'hecho real o conocido', 'Aunque llueve, saldré (sé que llueve).'),
            ('aunque + subjuntivo', 'hipótesis o concesión posible', 'Aunque llueva, saldré (puede que llueva).'),
            ('por más/mucho que', 'siempre + subjuntivo: concesión de grado máximo', 'Por más que estudie, no aprueba.'),
            ('aun cuando', 'formal: indicativo (hecho) / subjuntivo (hipótesis)', 'Aun cuando llegara tarde, esperaría.'),
            ('si bien', 'siempre + indicativo: matiz adversativo formal', 'Si bien es cierto que hay dificultades, hay soluciones.'),
            ('así + subjuntivo', 'coloquial/literario: aunque + subj. enfático', 'Así me lo juren, no lo creo.'),
            ('ya sea... ya sea', 'siempre + subjuntivo: indiferencia ante dos opciones', 'Ya sea por razones personales, ya sea por otras.'),
        ],
        ex1=dict(
            title='Indicativo o subjuntivo en oraciones concesivas',
            questions=[
                ('______ hace frío, siempre va en manga corta. (hecho habitual conocido)',
                 ['Aunque hace', 'Aunque haga', 'Por más que hace', 'Si bien haga'],
                 0,
                 'Hecho real y habitual → <b>aunque + indicativo</b>: «Aunque <b>hace</b> frío».'),
                ('______ me lo expliques mil veces, no lo entiendo.',
                 ['Aunque me lo explicarás', 'Por más que me lo expliques', 'Si bien me lo expliques', 'Así me lo explicabas'],
                 1,
                 'Concesión de grado máximo → <b>por más que + subjuntivo</b>: «Por más que me lo <b>expliques</b>».'),
                ('______ sea verdad lo que dices, no es el momento de decirlo. (hipótesis)',
                 ['Aunque es', 'Si bien sea', 'Aunque sea', 'Aun cuando es'],
                 2,
                 'Hipótesis sin afirmar → <b>aunque + subjuntivo</b>: «Aunque <b>sea</b> verdad».'),
                ('______ tiene sus defectos, es un proyecto innovador. (matiz adversativo formal)',
                 ['Aunque tenga', 'Si bien tiene', 'Por más que tiene', 'Así tenga'],
                 1,
                 'Matiz adversativo en registro formal → <b>si bien + indicativo</b>: «Si bien <b>tiene</b> sus defectos».'),
                ('______ me lo pidiera de rodillas, no cambiaría de opinión. (irrealidad hipotética)',
                 ['Aunque me lo pide', 'Aunque me lo pedirá', 'Aunque me lo pidiera', 'Por más que me lo pide'],
                 2,
                 'Concesión contraria a la realidad → <b>aunque + subjuntivo imperfecto</b>: «Aunque me lo <b>pidiera</b>».'),
                ('______ sea por motivos económicos, ______ sea por razones personales, la decisión es firme.',
                 ['Si bien... si bien', 'Aunque... aunque', 'Ya sea... ya sea', 'Aun cuando... aun cuando'],
                 2,
                 'Indiferencia ante dos alternativas → <b>ya sea... ya sea</b> (siempre con subjuntivo).'),
            ]
        ),
        ex2=dict(
            title='Completa con la conjunción o el modo verbal correcto',
            questions=[
                ('______ lo intente con todas sus fuerzas, no conseguirá terminar a tiempo.',
                 'Por más que',
                 ['Por más que', 'Por mucho que'],
                 'Concesión de grado máximo + subjuntivo → <b>Por más que / Por mucho que</b>.'),
                ('A pesar de que ______ (estar) cansado, continuó trabajando hasta medianoche. (hecho real)',
                 'estaba',
                 ['estaba'],
                 'Hecho real pasado → a pesar de que + <b>indicativo</b> (imperfecto): <b>estaba</b>.'),
                ('______ es cierto que el proyecto se ha retrasado, los resultados son prometedores.',
                 'Si bien',
                 ['Si bien'],
                 'Matiz adversativo formal con indicativo → <b>Si bien</b>.'),
                ('Aunque ______ (llover) el día de la boda, la ceremonia fue perfecta. (hecho pasado)',
                 'llovía',
                 ['llovía'],
                 'Hecho pasado real → aunque + <b>indicativo</b> (imperfecto): <b>llovía</b>.'),
                ('______ me lo juren todos, no me lo creo. (concesión enfática coloquial)',
                 'Así',
                 ['Así'],
                 'Concesión enfática coloquial + subjuntivo → <b>Así</b> me lo juren.'),
            ]
        ),
        ex3=dict(
            title='Identifica el uso correcto de las concesivas',
            questions=[
                ('¿Cuál expresa que el hablante conoce el hecho como real?',
                 ['Aunque llegue tarde, avísame.',
                  'Aunque llegara tarde, te esperaría.',
                  'Aunque llega tarde, siempre avisa.',
                  'Por más que llegue tarde, no importa.'],
                 2,
                 'Hecho habitual conocido → <b>aunque + indicativo</b>: «Aunque <b>llega</b> tarde, siempre avisa».'),
                ('¿Cuál usa correctamente «por más que»?',
                 ['Por más que lo intentará, fracasó.',
                  'Por más que lo intente, no lo consigue.',
                  'Por más que lo intentaba, no lo consigue.',
                  'Por más lo intente, no lo consigue.'],
                 1,
                 '<b>Por más que</b> + subjuntivo presente: «Por más que lo <b>intente</b>».'),
                ('¿Qué diferencia hay entre «aunque tiene razón» y «aunque tenga razón»?',
                 ['Ninguna; son intercambiables.',
                  '«Tiene» es más formal; «tenga» es coloquial.',
                  '«Tiene» = hecho que el hablante confirma; «tenga» = hipótesis o concesión sin afirmar.',
                  '«Tenga» se usa solo en oraciones negativas.'],
                 2,
                 'Modo indicativo = hecho confirmado; modo subjuntivo = hipótesis o valor concesivo sin afirmar el hecho.'),
                ('¿Cuál usa «si bien» correctamente?',
                 ['Si bien sea cierto, no es relevante.',
                  'Si bien fuera cierto, no sería relevante.',
                  'Si bien es cierto que hay obstáculos, el objetivo es alcanzable.',
                  'Si bien lo haya hecho bien, podría mejorar.'],
                 2,
                 '<b>Si bien</b> siempre lleva indicativo: «Si bien <b>es</b> cierto».'),
                ('¿Cuál expresa indiferencia ante dos alternativas?',
                 ['Aunque sea por A o por B.',
                  'Ya sea por razones económicas, ya sea por motivos personales.',
                  'Por más que sea A o B.',
                  'Aun cuando sea A o sea B.'],
                 1,
                 'Indiferencia ante dos opciones → <b>ya sea... ya sea</b> con subjuntivo.'),
            ]
        ),
        game_desc='4 nexos concesivos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            dict(term='aunque llueva',
                 definition='aunque + subjuntivo: concesión hipotética (posibilidad no afirmada)',
                 example='<b>Aunque llueva</b>, la ceremonia se celebrará en el exterior.',
                 accept=['aunque llueva']),
            dict(term='aunque llueve',
                 definition='aunque + indicativo: concesión sobre un hecho real y conocido',
                 example='<b>Aunque llueve</b>, los niños quieren salir a jugar.',
                 accept=['aunque llueve']),
            dict(term='por más que lo intente',
                 definition='por más que + subjuntivo: concesión de grado máximo',
                 example='<b>Por más que lo intente</b>, no consigue memorizar todos los verbos irregulares.',
                 accept=['por más que lo intente', 'por mucho que lo intente']),
            dict(term='aun cuando llegara',
                 definition='aun cuando + subjuntivo imperfecto: concesión contraria a la realidad (formal)',
                 example='<b>Aun cuando llegara</b> con horas de retraso, la reunión ya habría terminado.',
                 accept=['aun cuando llegara']),
            dict(term='si bien es cierto',
                 definition='si bien + indicativo: concesión con matiz adversativo (registro muy formal)',
                 example='<b>Si bien es cierto</b> que el plan tiene riesgos, los beneficios superan los inconvenientes.',
                 accept=['si bien es cierto', 'si bien']),
            dict(term='así me lo juren',
                 definition='así + subjuntivo: concesión enfática coloquial o literaria',
                 example='<b>Así me lo juren</b> con toda solemnidad, no pienso cambiar de opinión.',
                 accept=['así me lo juren', 'así']),
            dict(term='ya sea por una razón',
                 definition='ya sea... ya sea: indiferencia ante dos alternativas (siempre con subjuntivo)',
                 example='<b>Ya sea por una razón</b> económica, ya sea por otra personal, la decisión es irrevocable.',
                 accept=['ya sea por una razón', 'ya sea']),
            dict(term='a pesar de que tenga',
                 definition='a pesar de que + subjuntivo: concesión hipotética sin afirmar el hecho',
                 example='<b>A pesar de que tenga</b> experiencia, tendrá que superar la misma prueba que los demás.',
                 accept=['a pesar de que tenga', 'a pesar de que']),
        ],
    ),

    'oraciones-escindidas': dict(
        level='c1',
        section='grammar',
        num='G08',
        short='Oraciones Escindidas',
        title='Las Oraciones Escindidas y el Foco Informativo',
        subtitle='Domina las construcciones escindidas y pseudoescindidas para focalizar información',
        slides=[
            ('Oración escindida básica: Es [X] quien/que...', None,
             '<p class="slide-explanation">Las <b>oraciones escindidas</b> (también llamadas «hendidas») '
             'descomponen una oración simple en dos cláusulas para <b>focalizar</b> un constituyente — '
             'es decir, para presentarlo como la información más relevante o contrastiva:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>Oración neutra: <b>María lo hizo</b>.</p>'
             '<p>Escindida de sujeto: <b>Es María quien lo hizo</b>. (no Ana, no Pedro — María)</p>'
             '<p>Oración neutra: <b>Busco el libro</b>.</p>'
             '<p>Escindida de objeto: <b>Es el libro lo que busco</b>. (no la revista — el libro)</p>'
             '</div>'
             '<p class="slide-explanation">La estructura es: <b>Es + [elemento focalizado] + quien/que/lo que/donde/cuando...</b> '
             'El verbo <i>ser</i> concuerda generalmente con el elemento focalizado.</p>'),

            ('Tipos de escindidas según el elemento focalizado', None,
             '<p class="slide-explanation">El elemento que se focaliza determina el pronombre relativo que introduce la segunda cláusula:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Elemento</th>'
             '<th style="padding:8px;text-align:left">Relativo</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Sujeto (persona)</td><td style="padding:8px"><b>quien / quienes</b></td><td style="padding:8px">Es María <b>quien</b> lo organizó.</td></tr>'
             '<tr><td style="padding:8px">Objeto (cosa)</td><td style="padding:8px"><b>lo que / lo cual</b></td><td style="padding:8px">Es el libro <b>lo que</b> busco.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Lugar</td><td style="padding:8px"><b>donde</b></td><td style="padding:8px">Es en Madrid <b>donde</b> vive.</td></tr>'
             '<tr><td style="padding:8px">Tiempo</td><td style="padding:8px"><b>cuando</b></td><td style="padding:8px">Es ayer <b>cuando</b> llamó.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Modo</td><td style="padding:8px"><b>como</b></td><td style="padding:8px">Es así <b>como</b> se hace.</td></tr>'
             '<tr><td style="padding:8px">Causa</td><td style="padding:8px"><b>por lo que</b></td><td style="padding:8px">Es por eso <b>por lo que</b> dimití.</td></tr>'
             '</table>'),

            ('Pseudoescindidas: Lo que... es...', None,
             '<p class="slide-explanation">Las <b>pseudoescindidas</b> (o escindidas inversas) tienen la cláusula relativa al inicio '
             'y el elemento focalizado al final, tras el verbo <i>ser</i>:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Lo que necesitas es descansar</b>. (no estudiar, no trabajar)</p>'
             '<p><b>Donde vive es en Madrid</b>. (no en Barcelona)</p>'
             '<p><b>Lo que me sorprendió fue su reacción</b>.</p>'
             '<p><b>Quien lo hizo fue ella</b>.</p>'
             '</div>'
             '<p class="slide-explanation">En las pseudoescindidas, el foco informativo recae sobre el elemento '
             'que aparece <b>después de ser</b>. Son muy frecuentes en el español oral para contrastar información.</p>'),

            ('Dislocación: tópico y foco', None,
             '<p class="slide-explanation">La <b>dislocación</b> mueve un constituyente fuera de su posición '
             'canónica para marcarlo como <b>tópico</b> (información dada) o como <b>foco contrastivo</b>. '
             'Va acompañada de un pronombre clítico que retoma el elemento dislocado:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Tipo</th>'
             '<th style="padding:8px;text-align:left">Posición</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Dislocación izquierda</td><td style="padding:8px">Tópico al inicio</td><td style="padding:8px">El libro, <b>lo</b> tengo yo.</td></tr>'
             '<tr><td style="padding:8px">Dislocación derecha</td><td style="padding:8px">Tópico al final</td><td style="padding:8px"><b>Lo</b> tengo yo, el libro.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Foco pronominal</td><td style="padding:8px">Pronombre tónico</td><td style="padding:8px">Lo hizo <b>ella</b>, no él.</td></tr>'
             '</table>'
             '<p class="slide-explanation">La dislocación izquierda introduce un tópico ya mencionado en el discurso. '
             'La dislocación derecha tiene valor de añadido o aclaración.</p>'),

            ('Información nueva (foco) e información dada (tópico)', None,
             '<p class="slide-explanation">En el discurso, el español organiza la información siguiendo el principio '
             '<b>dado → nuevo</b>: lo que ya se conoce va primero; lo que se presenta como nuevo o relevante '
             'va al final de la oración o se focaliza mediante escindidas:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Contexto:</b> — ¿Quién llamó?</p>'
             '<p><b>Respuesta neutra (foco al final):</b> Llamó <b>Juan</b>. (Juan = información nueva)</p>'
             '<p><b>Respuesta escindida (énfasis contrastivo):</b> Fue <b>Juan</b> quien llamó. (no Pedro)</p>'
             '<p>&nbsp;</p>'
             '<p><b>Tópico:</b> El informe... ya está <b>terminado</b>. (el informe = dado; terminado = nuevo)</p>'
             '</div>'
             '<p class="slide-explanation">Las escindidas se usan cuando el hablante quiere '
             '<b>contrastar</b> el elemento focalizado con otras alternativas posibles, reales o implícitas.</p>'),
        ],
        traps=[
            ('Es María que lo hizo. (con «que» para sujeto persona)',
             'Es María <strong>quien</strong> lo hizo.',
             'Cuando el elemento focalizado es una persona en función de sujeto, se usa el relativo <b>quien</b>, no «que».'),
            ('Es el libro que busco.',
             'Es el libro <strong>lo que</strong> busco.',
             'Para focalizar un objeto de cosa, se usa el relativo <b>lo que</b>: «Es el libro <b>lo que</b> busco».'),
            ('Lo que necesitas es descansando.',
             'Lo que necesitas es <strong>descansar</strong>.',
             'En las pseudoescindidas, si la cláusula inicial contiene un verbo de necesidad o deseo, '
             'el foco final suele ser un <b>infinitivo</b>, no un gerundio.'),
            ('El libro, tengo yo. (sin clítico)',
             'El libro, <strong>lo</strong> tengo yo.',
             'En la dislocación izquierda, el elemento dislocado debe ser retomado por un <b>pronombre clítico</b>: '
             '«El libro, <b>lo</b> tengo yo».'),
            ('Es en el parque donde vivo. (cuando en realidad vive allí)',
             'Vivo en el parque. / Es en el parque <strong>donde</strong> vivo. (solo si se contrasta con otro lugar)',
             'La escindida aporta énfasis contrastivo. Sin contexto contrastivo, la oración simple es más natural.'),
        ],
        summary=[
            ('Escindida básica', 'Es + [X] + quien/lo que/donde/cuando...', 'Es ella quien tomó la decisión.'),
            ('Escindida de sujeto', 'Es + persona + quien + cláusula', 'Es el director quien debe firmar.'),
            ('Escindida de objeto', 'Es + cosa + lo que + cláusula', 'Es la verdad lo que importa.'),
            ('Escindida de lugar/tiempo', 'Es + circ. + donde/cuando + cláusula', 'Es aquí donde ocurrió.'),
            ('Pseudoescindida', 'Lo que... + ser + [foco]', 'Lo que me gusta es el silencio.'),
            ('Dislocación izquierda', 'Tópico al inicio + clítico + resto', 'El libro, lo dejé en la mesa.'),
            ('Foco y tópico', 'Dado primero, nuevo al final o en escindida', 'Llamó Juan. / Fue Juan quien llamó.'),
        ],
        ex1=dict(
            title='Elige el relativo correcto en la oración escindida',
            questions=[
                ('Es el director ______ debe autorizar el presupuesto.',
                 ['que', 'quien', 'lo que', 'donde'],
                 1,
                 'Sujeto de persona → <b>quien</b>: «Es el director <b>quien</b> debe autorizar».'),
                ('Es la confianza ______ mantiene unido al equipo.',
                 ['quien', 'cuando', 'lo que', 'donde'],
                 2,
                 'Sujeto de cosa → <b>lo que</b>: «Es la confianza <b>lo que</b> mantiene unido al equipo».'),
                ('Es en esta sala ______ se celebran todas las reuniones.',
                 ['que', 'quien', 'lo que', 'donde'],
                 3,
                 'Circunstancial de lugar → <b>donde</b>: «Es en esta sala <b>donde</b> se celebran».'),
                ('Es por esa razón ______ decidimos cambiar de estrategia.',
                 ['cuando', 'que', 'por lo que', 'lo que'],
                 2,
                 'Causa → <b>por lo que</b>: «Es por esa razón <b>por lo que</b> decidimos».'),
                ('______ más me sorprendió fue su silencio. (pseudoescindida)',
                 ['Es lo que', 'Lo que', 'Quien', 'Donde'],
                 1,
                 'Pseudoescindida con objeto focalizado al final → <b>Lo que</b> más me sorprendió fue su silencio.'),
                ('El presupuesto, ______ aprobamos sin objeciones.',
                 ['quien', 'lo', 'le', 'se'],
                 1,
                 'Dislocación izquierda de objeto directo → clítico <b>lo</b>: «El presupuesto, <b>lo</b> aprobamos».'),
            ]
        ),
        ex2=dict(
            title='Transforma la oración en una escindida con énfasis en el elemento indicado',
            questions=[
                ('Ana organizó la conferencia. → [Focaliza el sujeto] → ______ la conferencia.',
                 'Es Ana quien organizó',
                 ['Es Ana quien organizó'],
                 'Escindida de sujeto (persona): <b>Es Ana quien organizó</b> la conferencia.'),
                ('Busco la llave. → [Focaliza el objeto] → ______ busco.',
                 'Es la llave lo que',
                 ['Es la llave lo que'],
                 'Escindida de objeto (cosa): <b>Es la llave lo que</b> busco.'),
                ('El accidente ocurrió en esa esquina. → [Focaliza el lugar] → ______ ocurrió el accidente.',
                 'Es en esa esquina donde',
                 ['Es en esa esquina donde'],
                 'Escindida de lugar: <b>Es en esa esquina donde</b> ocurrió el accidente.'),
                ('Necesito descansar. → [Pseudoescindida] → ______ es descansar.',
                 'Lo que necesito',
                 ['Lo que necesito'],
                 'Pseudoescindida: <b>Lo que necesito</b> es descansar.'),
                ('Compré ese libro ayer. → [Dislocación izquierda del objeto] → Ese libro, ______ ayer.',
                 'lo compré',
                 ['lo compré'],
                 'Dislocación izquierda + clítico: «Ese libro, <b>lo compré</b> ayer».'),
            ]
        ),
        ex3=dict(
            title='Identifica el uso correcto de las escindidas',
            questions=[
                ('¿Cuál es una escindida de sujeto correctamente formada?',
                 ['Es María que llamó.',
                  'Es María quien llamó.',
                  'Es María lo que llamó.',
                  'Es quien María llamó.'],
                 1,
                 'Sujeto persona → <b>quien</b>: «Es María <b>quien</b> llamó».'),
                ('¿Cuál es una pseudoescindida?',
                 ['Es el trabajo lo que me preocupa.',
                  'Lo que me preocupa es el trabajo.',
                  'Es el trabajo quien me preocupa.',
                  'El trabajo me preocupa, lo.'],
                 1,
                 'Pseudoescindida: la cláusula relativa va al inicio y el foco al final → «<b>Lo que me preocupa</b> es el trabajo».'),
                ('En la dislocación izquierda, ¿qué elemento es obligatorio?',
                 ['Un pronombre relativo.',
                  'El verbo ser.',
                  'Un pronombre clítico que retome el elemento dislocado.',
                  'Una conjunción concesiva.'],
                 2,
                 'La dislocación izquierda requiere un <b>clítico</b> que retome el tópico: «El libro, <b>lo</b> tengo yo».'),
                ('¿Cuándo es más apropiada una escindida que una oración simple?',
                 ['Cuando la información es completamente nueva para el oyente.',
                  'Cuando se quiere contrastar el elemento focalizado con otras alternativas implícitas o explícitas.',
                  'Cuando la oración es negativa.',
                  'Cuando el sujeto es una cosa, no una persona.'],
                 1,
                 'Las escindidas expresan <b>énfasis contrastivo</b>: el elemento focalizado se opone a otras posibilidades.'),
                ('¿Qué función tiene «lo que» en «Es la honestidad lo que admiro»?',
                 ['Es el sujeto de la oración escindida.',
                  'Es el relativo que introduce la cláusula de relativo y retoma al elemento focalizado.',
                  'Es un demostrativo neutro.',
                  'Es el verbo en forma nominal.'],
                 1,
                 '<b>Lo que</b> es el pronombre relativo neutro que introduce la cláusula relativa en la escindida de objeto.'),
            ]
        ),
        game_desc='4 estructuras de focalización · 3 rondas cada una · llega a 100 puntos para ganar.',
        items=[
            dict(term='Es ella quien lo hizo',
                 definition='escindida de sujeto (persona): focalización con quien',
                 example='<b>Es ella quien lo hizo</b>, no su compañero de trabajo.',
                 accept=['Es ella quien lo hizo', 'es ella quien lo hizo']),
            dict(term='Es la verdad lo que importa',
                 definition='escindida de objeto (cosa): focalización con lo que',
                 example='<b>Es la verdad lo que importa</b> en este proceso, no las apariencias.',
                 accept=['Es la verdad lo que importa', 'es la verdad lo que importa']),
            dict(term='Es aquí donde ocurrió',
                 definition='escindida de lugar: focalización con donde',
                 example='<b>Es aquí donde ocurrió</b> el incidente que cambió la historia del barrio.',
                 accept=['Es aquí donde ocurrió', 'es aquí donde ocurrió']),
            dict(term='Lo que necesito es descansar',
                 definition='pseudoescindida: cláusula relativa al inicio, foco al final',
                 example='<b>Lo que necesito es descansar</b> unos días para recuperar las fuerzas.',
                 accept=['Lo que necesito es descansar', 'lo que necesito es descansar']),
            dict(term='El libro, lo tengo yo',
                 definition='dislocación izquierda: tópico al inicio + clítico de retoma',
                 example='<b>El libro, lo tengo yo</b>; te lo devuelvo mañana sin falta.',
                 accept=['El libro, lo tengo yo', 'el libro, lo tengo yo']),
            dict(term='Es por eso por lo que dimití',
                 definition='escindida de causa: focalización con por lo que',
                 example='<b>Es por eso por lo que dimití</b>: no podía seguir trabajando en esas condiciones.',
                 accept=['Es por eso por lo que dimití', 'es por eso por lo que dimití']),
            dict(term='Fue Juan quien llamó',
                 definition='escindida de sujeto en pasado: énfasis contrastivo sobre el agente',
                 example='<b>Fue Juan quien llamó</b>, no el cliente que esperábamos.',
                 accept=['Fue Juan quien llamó', 'fue Juan quien llamó']),
            dict(term='Lo que me sorprendió fue su calma',
                 definition='pseudoescindida en pasado: foco sobre la consecuencia o reacción',
                 example='<b>Lo que me sorprendió fue su calma</b> ante una situación tan tensa.',
                 accept=['Lo que me sorprendió fue su calma', 'lo que me sorprendió fue su calma']),
        ],
    ),

    'aspecto-verbal': dict(
        level='c1',
        section='grammar',
        num='G09',
        short='Aspecto Verbal',
        title='El Aspecto Verbal: Perfectivo e Imperfectivo',
        subtitle='Analiza el aspecto perfectivo e imperfectivo y las perífrasis aspectuales del español',
        slides=[
            ('Aspecto perfectivo vs. imperfectivo', None,
             '<p class="slide-explanation">El <b>aspecto</b> es una categoría gramatical que indica cómo '
             'el hablante percibe el desarrollo temporal interno de un evento: '
             'como un <b>todo acabado</b> (perfectivo) o como un <b>proceso en curso</b> (imperfectivo).</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Aspecto</th>'
             '<th style="padding:8px;text-align:left">Perspectiva</th>'
             '<th style="padding:8px;text-align:left">Tiempo verbal</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Perfectivo</b></td><td style="padding:8px">Evento visto como un todo cerrado</td><td style="padding:8px">Pretérito indefinido</td><td style="padding:8px">Ayer <b>escribí</b> el informe.</td></tr>'
             '<tr><td style="padding:8px"><b>Imperfectivo</b></td><td style="padding:8px">Proceso en curso, sin límite visible</td><td style="padding:8px">Pretérito imperfecto</td><td style="padding:8px">Cuando era niño, <b>leía</b> mucho.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Perfectivo</b></td><td style="padding:8px">Resultado alcanzado (pasado desde el pasado)</td><td style="padding:8px">Pluscuamperfecto</td><td style="padding:8px">Ya <b>había terminado</b> cuando llegaste.</td></tr>'
             '</table>'
             '<p class="slide-explanation">La distinción indefinido/imperfecto no es solo temporal — '
             'es ante todo <b>aspectual</b>: el indefinido «fotografía» el evento en su totalidad; '
             'el imperfecto lo «filma» desde dentro.</p>'),

            ('Indefinido vs. imperfecto: aspecto en la narración', None,
             '<p class="slide-explanation">En la narración, el <b>pretérito indefinido</b> hace avanzar la historia '
             '(eventos discretos que suceden uno tras otro); el <b>imperfecto</b> describe el escenario '
             'o los estados de fondo:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>Era una noche fría. (<b>Imperfecto:</b> escenario) <b>Llovía</b> sin parar. (<b>Imperfecto:</b> estado de fondo)</p>'
             '<p>De repente, <b>llamaron</b> a la puerta. (<b>Indefinido:</b> evento puntual que avanza la historia)</p>'
             '<p>Me <b>levanté</b>, <b>fui</b> a abrir y <b>me encontré</b> con una sorpresa. (<b>Indefinido:</b> secuencia)</p>'
             '</div>'
             '<p class="slide-explanation">Los verbos estativos (<i>ser, estar, tener, saber, querer</i>) suelen '
             'aparecer en imperfecto en la narración porque expresan <b>estados de fondo</b>, no eventos discretos.</p>'),

            ('Perífrasis aspectuales de fase', None,
             '<p class="slide-explanation">Las <b>perífrasis verbales aspectuales</b> permiten expresar con precisión '
             'la fase o el carácter del evento:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Perífrasis</th>'
             '<th style="padding:8px;text-align:left">Aspecto</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>estar + gerundio</b></td><td style="padding:8px">Progresivo (en curso)</td><td style="padding:8px"><b>Estoy escribiendo</b> el informe.</td></tr>'
             '<tr><td style="padding:8px"><b>llevar + gerundio</b></td><td style="padding:8px">Durativo (desde hace X)</td><td style="padding:8px"><b>Llevo tres horas estudiando</b>.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>acabar de + inf.</b></td><td style="padding:8px">Reciente (inmediatamente antes)</td><td style="padding:8px"><b>Acabo de llegar</b>.</td></tr>'
             '<tr><td style="padding:8px"><b>ponerse a + inf.</b></td><td style="padding:8px">Incoativo (comienzo)</td><td style="padding:8px">Se <b>puso a llover</b> de repente.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>dejar de + inf.</b></td><td style="padding:8px">Cesativo (fin)</td><td style="padding:8px"><b>Dejó de fumar</b> hace un año.</td></tr>'
             '<tr><td style="padding:8px"><b>seguir + gerundio</b></td><td style="padding:8px">Continuativo</td><td style="padding:8px"><b>Sigue trabajando</b> en el mismo proyecto.</td></tr>'
             '</table>'),

            ('Aktionsart: tipos de situaciones verbales', None,
             '<p class="slide-explanation">El <b>Aktionsart</b> (o «modo de acción») es la naturaleza aspectual '
             'inherente del significado léxico del verbo, independientemente de los tiempos gramaticales:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Tipo</th>'
             '<th style="padding:8px;text-align:left">Duración</th>'
             '<th style="padding:8px;text-align:left">Télico</th>'
             '<th style="padding:8px;text-align:left">Ejemplos</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Estado</b></td><td style="padding:8px">Duradero</td><td style="padding:8px">No</td><td style="padding:8px">saber, tener, creer, amar</td></tr>'
             '<tr><td style="padding:8px"><b>Actividad</b></td><td style="padding:8px">Duradero</td><td style="padding:8px">No</td><td style="padding:8px">correr, hablar, nadar</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Realización</b></td><td style="padding:8px">Duradero</td><td style="padding:8px">Sí</td><td style="padding:8px">escribir una carta, construir una casa</td></tr>'
             '<tr><td style="padding:8px"><b>Logro</b></td><td style="padding:8px">Instantáneo</td><td style="padding:8px">Sí</td><td style="padding:8px">llegar, encontrar, ganar (un partido)</td></tr>'
             '</table>'
             '<p class="slide-explanation">Los verbos de <b>logro</b> en imperfecto suelen interpretarse como intentos '
             'o procesos en marcha: «Ganaba el partido» = estaba a punto de ganar / iba ganando.</p>'),

            ('Interacción aspecto-tiempo y el pluscuamperfecto', None,
             '<p class="slide-explanation">El <b>pluscuamperfecto</b> combina aspecto perfectivo con anterioridad '
             'al pasado: expresa un evento acabado que ocurrió <b>antes</b> de otro punto de referencia pasado. '
             'El <b>pretérito perfecto</b> (haber + participio) expresa perfectividad con relevancia presente:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Pluscuamperfecto:</b> Cuando llegué, ya <b>habían empezado</b>. (empezaron antes de que llegara)</p>'
             '<p><b>Indefinido:</b> Ayer <b>llegué</b> y <b>empezaron</b>. (dos eventos consecutivos)</p>'
             '<p><b>Perfecto:</b> <b>He terminado</b> el informe. (resultado relevante ahora)</p>'
             '</div>'
             '<p class="slide-explanation">El uso del perfecto vs. indefinido varía según la variedad del español: '
             'en España, el perfecto expresa pasado reciente con relevancia presente; '
             'en la mayor parte de América Latina, el indefinido asume ambas funciones.</p>'),
        ],
        traps=[
            ('Cuando era niño, fui al parque cada día. (hábito pasado)',
             'Cuando era niño, <strong>iba</strong> al parque cada día.',
             'Los hábitos o acciones repetidas en el pasado sin límite temporal definido se expresan '
             'con el <b>imperfecto</b> (aspecto imperfectivo): <b>iba</b>, no «fui».'),
            ('Llevo estudiando tres horas. (error de orden)',
             '<strong>Llevo tres horas estudiando</strong>.',
             'La perífrasis durativa es <b>llevar + expresión de tiempo + gerundio</b>. '
             'El gerundio va al final, después de la expresión de tiempo.'),
            ('Acabé de llegar. (con indefinido)',
             '<strong>Acabo de llegar</strong>. (presente)',
             'La perífrasis de aspecto reciente <b>acabar de + infinitivo</b> se usa habitualmente '
             'en <b>presente</b> para indicar que la acción ocurrió hace muy poco.'),
            ('El tren llegaba a las ocho. (para un evento puntual pasado concreto)',
             'El tren <strong>llegó</strong> a las ocho.',
             'Un evento puntual y concreto en el pasado usa el <b>indefinido</b> (perfectivo). '
             'El imperfecto «llegaba» indicaría un horario habitual, no un evento específico.'),
            ('Supe la verdad desde siempre. (saber + desde siempre)',
             '<strong>Sabía</strong> la verdad desde siempre.',
             'Los verbos de estado (<i>saber, conocer, tener, querer</i>) expresan estados de fondo '
             'y suelen ir en <b>imperfecto</b>. El indefinido «supe» indica el momento en que se adquirió el conocimiento.'),
        ],
        summary=[
            ('Aspecto perfectivo', 'Evento visto como todo cerrado → indefinido, pluscuamperfecto', 'Ayer terminé el proyecto.'),
            ('Aspecto imperfectivo', 'Proceso en curso, sin límite → imperfecto, progresivo', 'Cuando llegué, dormía.'),
            ('Indefinido vs. imperfecto', 'Indef. = evento; imperf. = escenario/estado/hábito', 'Entraron cuando hablaba por teléfono.'),
            ('Estar + gerundio', 'Progresivo: acción en curso en un momento', 'Estaban discutiendo cuando llegué.'),
            ('Llevar + gerundio', 'Durativo: acción que lleva X tiempo en curso', 'Llevo dos años viviendo en Bogotá.'),
            ('Ponerse a / dejar de / seguir + inf./ger.', 'Incoativo / cesativo / continuativo', 'Se puso a hablar y no dejó de hacerlo.'),
            ('Aktionsart', 'Estado / Actividad / Realización / Logro', 'Encontré las llaves. (logro, perfectivo natural)'),
        ],
        ex1=dict(
            title='Elige el tiempo o la perífrasis aspectual adecuada',
            questions=[
                ('Cuando era pequeña, ______ (leer) un libro cada semana. (hábito pasado)',
                 ['leyó', 'leía', 'ha leído', 'había leído'],
                 1,
                 'Hábito pasado sin límite temporal definido → aspecto imperfectivo → <b>imperfecto</b>: <b>leía</b>.'),
                ('Cuando llegué a la fiesta, mis amigos ya ______ (irse).',
                 ['se fueron', 'se iban', 'se habían ido', 'se van'],
                 2,
                 'Evento acabado antes de otro evento pasado → <b>pluscuamperfecto</b>: <b>se habían ido</b>.'),
                ('______ (llevar) dos años aprendiendo chino y todavía me cuesta la escritura.',
                 ['Estoy llevando', 'He llevado', 'Llevo', 'Llevé'],
                 2,
                 'Duración de una actividad en curso hasta ahora → <b>llevar + gerundio</b>: <b>Llevo</b> dos años aprendiendo.'),
                ('De repente, ______ (ponerse) a nevar con mucha intensidad.',
                 ['empezaba', 'se había puesto', 'se puso', 'estaba poniendo'],
                 2,
                 'Comienzo abrupto de una acción → <b>ponerse a + infinitivo</b> en indefinido: <b>se puso</b> a nevar.'),
                ('Perdona, no puedo hablar ahora: ______ (estar / comer).',
                 ['como', 'comía', 'estoy comiendo', 'he comido'],
                 2,
                 'Acción en curso en el momento presente → <b>estar + gerundio</b>: <b>estoy comiendo</b>.'),
                ('______ (dejar / fumar) hace tres años y desde entonces se siente mucho mejor.',
                 ['Dejó de fumar', 'Dejaba de fumar', 'Estaba dejando de fumar', 'Había dejado fumar'],
                 0,
                 'Fin de una acción en el pasado → <b>dejar de + infinitivo</b> en indefinido: <b>Dejó de fumar</b>.'),
            ]
        ),
        ex2=dict(
            title='Explica la diferencia aspectual entre los dos enunciados',
            questions=[
                ('¿Qué diferencia hay entre «Escribí la carta» y «Escribía la carta»?',
                 'Escribí la carta (indefinido, perfectivo): la acción se presenta como un todo terminado. Escribía la carta (imperfecto, imperfectivo): la acción estaba en curso, sin indicar su fin.',
                 ['perfectivo', 'imperfectivo'],
                 'Indefinido = aspecto <b>perfectivo</b> (evento cerrado). Imperfecto = aspecto <b>imperfectivo</b> (proceso en curso).'),
                ('Transforma: «Hace dos horas que estudio.» → Perífrasis con LLEVAR.',
                 'Llevo dos horas estudiando.',
                 ['Llevo dos horas estudiando'],
                 'Durativo con LLEVAR: <b>Llevo dos horas estudiando</b>. La expresión de tiempo va entre el verbo y el gerundio.'),
                ('Transforma: «Empezó a correr de repente.» → Perífrasis incoativa equivalente.',
                 'Se puso a correr de repente.',
                 ['Se puso a correr de repente'],
                 'Inicio abrupto → <b>ponerse a + infinitivo</b>: «Se puso a correr de repente».'),
                ('¿Cómo se dice en español «She has just arrived»?',
                 'Acaba de llegar.',
                 ['Acaba de llegar'],
                 'Aspecto reciente → <b>acabar de + infinitivo</b> en presente: <b>Acaba de llegar</b>.'),
                ('¿Cuál es el Aktionsart de «encontrar las llaves»: estado, actividad, realización o logro?',
                 'logro',
                 ['logro'],
                 '«Encontrar» es un verbo de <b>logro</b>: evento instantáneo y télico. Por eso es difícil combinarlo con «estar + gerundio» sin cambiar el significado.'),
            ]
        ),
        ex3=dict(
            title='Identifica el aspecto verbal correcto',
            questions=[
                ('¿Cuál usa el imperfecto correctamente para un hábito pasado?',
                 ['Cuando vivía en París, visité el Louvre cada semana.',
                  'Cuando vivía en París, visitaba el Louvre cada semana.',
                  'Cuando viví en París, visitaba el Louvre cada semana.',
                  'Cuando viví en París, visité el Louvre cada semana.'],
                 1,
                 'Escenario habitual en el pasado: ambos verbos en <b>imperfecto</b>: «<b>vivía</b>» + «<b>visitaba</b>».'),
                ('¿Cuál expresa que una acción había terminado antes de otra acción pasada?',
                 ['Cuando llegué, empezaron.',
                  'Cuando llegué, empezaban.',
                  'Cuando llegué, habían empezado ya.',
                  'Cuando llegaba, empezaron.'],
                 2,
                 'Anterioridad en el pasado → <b>pluscuamperfecto</b>: «<b>habían empezado</b> ya».'),
                ('¿Cuál usa correctamente la perífrasis incoativa?',
                 ['Se comenzó a llover.',
                  'Se puso a llover.',
                  'Se ponía a llover.',
                  'Estaba poniéndose a llover.'],
                 1,
                 'Inicio abrupto → <b>ponerse a + infinitivo</b>: «Se <b>puso</b> a llover».'),
                ('¿Cuál corresponde a un verbo de «logro» (Aktionsart)?',
                 ['hablar durante horas', 'saber la respuesta', 'construir una casa', 'llegar a la cima'],
                 3,
                 '<b>Llegar</b> es un verbo de logro: evento instantáneo y télico (tiene un punto final natural inmediato).'),
                ('¿Qué diferencia de aspecto hay entre «Supe la verdad» y «Sabía la verdad»?',
                 ['Ninguna; son intercambiables.',
                  '«Supe» indica el momento en que se adquirió el conocimiento (perfectivo); «sabía» describe un estado de fondo (imperfectivo).',
                  '«Sabía» es más formal que «supe».',
                  '«Supe» se usa solo en oraciones negativas.'],
                 1,
                 'SABER en indefinido (perfectivo) = momento puntual en que se adquirió el conocimiento. SABER en imperfecto = estado de fondo ya existente.'),
            ]
        ),
        game_desc='4 conceptos aspectuales clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            dict(term='aspecto perfectivo',
                 definition='perspectiva que presenta el evento como un todo cerrado y acabado',
                 example='Ayer <b>terminé</b> el proyecto: el indefinido expresa <b>aspecto perfectivo</b>.',
                 accept=['aspecto perfectivo', 'perfectivo']),
            dict(term='aspecto imperfectivo',
                 definition='perspectiva que presenta el evento como un proceso en curso, sin límite visible',
                 example='<b>Estudiaba</b> cuando sonó el teléfono: imperfecto expresa <b>aspecto imperfectivo</b>.',
                 accept=['aspecto imperfectivo', 'imperfectivo']),
            dict(term='llevo tres horas estudiando',
                 definition='perífrasis durativa: llevar + expresión de tiempo + gerundio',
                 example='<b>Llevo tres horas estudiando</b> y todavía me quedan dos capítulos.',
                 accept=['llevo tres horas estudiando', 'llevar + gerundio']),
            dict(term='acaba de llegar',
                 definition='perífrasis de aspecto reciente: acabar de + infinitivo en presente',
                 example='No la llames ahora: <b>acaba de llegar</b> y necesita descansar.',
                 accept=['acaba de llegar', 'acabar de + infinitivo']),
            dict(term='se puso a trabajar',
                 definition='perífrasis incoativa: ponerse a + infinitivo (inicio abrupto)',
                 example='Nada más llegar a casa, <b>se puso a trabajar</b> sin descansar.',
                 accept=['se puso a trabajar', 'ponerse a + infinitivo']),
            dict(term='dejó de fumar',
                 definition='perífrasis cesativa: dejar de + infinitivo (fin de una acción)',
                 example='<b>Dejó de fumar</b> hace cinco años y ahora tiene mucha más energía.',
                 accept=['dejó de fumar', 'dejar de + infinitivo']),
            dict(term='verbo de logro',
                 definition='Aktionsart: evento instantáneo y télico con punto final natural',
                 example='<b>Llegar, encontrar, ganar</b> son verbos de <b>logro</b>: ocurren en un instante.',
                 accept=['verbo de logro', 'logro']),
            dict(term='había terminado',
                 definition='pluscuamperfecto: aspecto perfectivo anterior a otro punto pasado',
                 example='Cuando llegaste, yo ya <b>había terminado</b> de preparar la cena.',
                 accept=['había terminado', 'pluscuamperfecto']),
        ],
    ),

    'orden-palabras': dict(
        level='c1',
        section='grammar',
        num='G10',
        short='Orden de Palabras',
        title='El Orden de Palabras y la Focalización',
        subtitle='Comprende el orden flexible del español y sus efectos sobre el foco y el tópico informativo',
        slides=[
            ('Orden básico SVO y el principio dado-nuevo', None,
             '<p class="slide-explanation">El español tiene un orden básico <b>SVO</b> (Sujeto-Verbo-Objeto), '
             'pero es <b>flexible</b>: el orden real lo determina la estructura informativa de la oración. '
             'La tendencia general es <b>información dada primero, información nueva al final</b>:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>Contexto: — ¿Quién escribió esa novela?</p>'
             '<p>Respuesta natural: La escribió <b>García Márquez</b>. (el nombre = información nueva → al final)</p>'
             '<p>Contexto: — ¿Qué hizo García Márquez?</p>'
             '<p>Respuesta natural: García Márquez <b>escribió esa novela</b>. (García Márquez = dado → al inicio)</p>'
             '</div>'
             '<p class="slide-explanation">En inglés, el orden SVO es casi fijo. En español, '
             'mover los constituyentes cambia el <b>énfasis informativo</b>, no la gramaticalidad.</p>'),

            ('Topicalización e inversión sujeto-verbo', None,
             '<p class="slide-explanation">La <b>topicalización</b> mueve un elemento al inicio de la oración '
             'para marcarlo como <b>tópico</b> (lo de lo que se habla). '
             'La <b>inversión sujeto-verbo</b> ocurre cuando el sujeto aparece después del verbo, '
             'presentando información nueva:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Fenómeno</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th>'
             '<th style="padding:8px;text-align:left">Efecto</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Topicalización</td><td style="padding:8px">El libro, lo compré ayer.</td><td style="padding:8px">El libro = tópico ya conocido</td></tr>'
             '<tr><td style="padding:8px">VS (informativo)</td><td style="padding:8px">Llegó tarde <b>el tren</b>.</td><td style="padding:8px">El tren = información nueva</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">VS (existencial)</td><td style="padding:8px">Llamó <b>un hombre</b>.</td><td style="padding:8px">Un hombre = introducción en el discurso</td></tr>'
             '<tr><td style="padding:8px">VS (interrogativa)</td><td style="padding:8px">¿Viene <b>María</b>?</td><td style="padding:8px">Inversión obligatoria en interrogativas</td></tr>'
             '</table>'),

            ('Posición del adjetivo: antes o después del sustantivo', None,
             '<p class="slide-explanation">La posición del adjetivo en español cambia su interpretación:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Posición</th>'
             '<th style="padding:8px;text-align:left">Valor</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>Antes</b> (prenominal)</td><td style="padding:8px">Subjetivo, enfático, connotativo</td><td style="padding:8px">un <b>gran</b> escritor / la <b>pobre</b> mujer</td></tr>'
             '<tr><td style="padding:8px"><b>Después</b> (posnominal)</td><td style="padding:8px">Restrictivo, objetivo, clasificatorio</td><td style="padding:8px">un escritor <b>famoso</b> / la mujer <b>pobre</b></td></tr>'
             '</table>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>Un <b>viejo</b> amigo = un amigo de toda la vida (connotación afectiva)</p>'
             '<p>Un amigo <b>viejo</b> = un amigo de edad avanzada (descripción objetiva)</p>'
             '<p>La <b>pura</b> verdad = la verdad absoluta / La verdad <b>pura</b> = verdad sin mezcla</p>'
             '</div>'),

            ('Posición de adverbios y negación', None,
             '<p class="slide-explanation">Los <b>adverbios de frecuencia</b> y la <b>negación</b> tienen '
             'posiciones preferidas en la oración española:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A">'
             '<th style="padding:8px;text-align:left">Elemento</th>'
             '<th style="padding:8px;text-align:left">Posición</th>'
             '<th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>nunca, siempre, jamás</b></td><td style="padding:8px">Antes del verbo simple / entre auxiliar y participio</td><td style="padding:8px">Nunca <b>llego</b> tarde. / No he <b>nunca</b> dicho eso. (raro → Nunca he dicho)</td></tr>'
             '<tr><td style="padding:8px"><b>ya, todavía, aún</b></td><td style="padding:8px">Ante o tras el verbo según el matiz</td><td style="padding:8px"><b>Ya</b> ha llegado. / <b>Todavía</b> no ha llegado.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>no (negación)</b></td><td style="padding:8px">Siempre inmediatamente antes del verbo</td><td style="padding:8px"><b>No</b> lo sé. / <b>No</b> ha venido.</td></tr>'
             '</table>'
             '<p class="slide-explanation">La posición del adverbio puede cambiar el alcance o el matiz: '
             '«<b>Solo</b> Juan lo sabe» (solo él) vs. «Juan solo <b>lo sabe</b>» (solo lo sabe, no lo hace).</p>'),

            ('Dislocación izquierda y derecha', None,
             '<p class="slide-explanation">La <b>dislocación</b> extrae un constituyente de su posición canónica '
             'y lo coloca a la periferia izquierda o derecha, dejando un clítico que lo retoma en la oración:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Dislocación izquierda</b> (tópico ya conocido):</p>'
             '<p>A María, <b>le</b> encanta la música clásica.</p>'
             '<p>El informe, ya <b>lo</b> hemos enviado.</p>'
             '<p>&nbsp;</p>'
             '<p><b>Dislocación derecha</b> (añadido o aclaración):</p>'
             '<p>Ya <b>lo</b> tengo, el libro.</p>'
             '<p>Me <b>lo</b> dijeron, los vecinos.</p>'
             '</div>'
             '<p class="slide-explanation">En el <b>orden de las preguntas indirectas</b>, el español no invierte el sujeto: '
             '«Sé <b>dónde está</b>» (no *«sé dónde está él» con inversión obligatoria). '
             'Compara con la pregunta directa: «¿<b>Dónde está</b> él?»</p>'),
        ],
        traps=[
            ('Llegó tarde. El tren llegó tarde. (¿cuál es más natural para información nueva?)',
             '<strong>Llegó tarde el tren.</strong> (VS: sujeto nuevo al final)',
             'Cuando el sujeto es <b>información nueva</b> en el discurso, el español prefiere el orden '
             'Verbo-Sujeto: «Llegó tarde <b>el tren</b>». El sujeto al final es la información presentada como nueva.'),
            ('Un famoso gran escritor',
             'un <strong>gran</strong> escritor (valoración) / un escritor <strong>famoso</strong> (descripción)',
             'Los adjetivos de valoración subjetiva van preferentemente <b>antes</b> del sustantivo; '
             'los descriptivos u objetivos, <b>después</b>. Acumular dos adjetivos prenominales es forzado.'),
            ('No sé dónde está él. (con inversión obligatoria en pregunta indirecta)',
             'No sé <strong>dónde está</strong>.',
             'En las preguntas indirectas, el español no invierte el sujeto: el orden es normal (SV), '
             'a diferencia de las preguntas directas (VS).'),
            ('Nunca he dicho esto → He nunca dicho esto.',
             '<strong>Nunca he dicho esto</strong> / No he dicho esto <strong>nunca</strong>.',
             'El adverbio «nunca» va preferentemente <b>antes del auxiliar</b> o al final. '
             'Colocarlo entre el auxiliar y el participio es posible pero infrecuente y muy formal.'),
            ('La vieja amiga (para decir «amiga de toda la vida»)',
             'una <strong>vieja</strong> amiga (prenominal = amistad larga) vs. una amiga <strong>vieja</strong> (edad)',
             'La posición del adjetivo cambia el significado: <b>vieja amiga</b> = amiga de mucho tiempo; '
             '<b>amiga vieja</b> = amiga de edad avanzada.'),
        ],
        summary=[
            ('SVO flexible', 'El orden real lo determina la estructura informativa: dado → nuevo', 'Lo dijo María. / María lo dijo.'),
            ('Topicalización', 'Tópico al inicio + clítico de retoma', 'El libro, lo compré en esa librería.'),
            ('Inversión V-S', 'Sujeto nuevo al final: Verbo + Sujeto', 'Llegó tarde el tren. / Llamó un hombre.'),
            ('Adjetivo prenominal', 'Antes del sustantivo: valor subjetivo o connotativo', 'una gran ciudad / el pobre chico'),
            ('Adjetivo posnominal', 'Después del sustantivo: valor restrictivo u objetivo', 'una ciudad grande / el chico pobre'),
            ('Negación', '«no» siempre inmediatamente antes del verbo', 'No lo sé. / No ha llegado aún.'),
            ('Preguntas indirectas', 'Sin inversión: sé dónde está (no *sé dónde está él con inversión)', 'No sé quién lo dijo.'),
        ],
        ex1=dict(
            title='Elige el orden de palabras más adecuado según el contexto informativo',
            questions=[
                ('Contexto: — ¿Qué pasó? — ______ (una mujer / entró).',
                 ['Una mujer entró.', 'Entró una mujer.', 'La mujer entró.', 'Entró la mujer.'],
                 1,
                 'Sujeto indefinido, información completamente nueva → inversión V-S: <b>Entró una mujer</b>.'),
                ('El libro del que hablamos ayer, ¿______ (ya / leer / tú / lo)?',
                 ['¿ya lo leíste?', '¿lo ya leíste?', '¿lo leíste ya?', 'Tanto A como C son correctas.'],
                 3,
                 '«Ya» puede ir al inicio o al final de la oración. Tanto «¿ya lo leíste?» como «¿lo leíste ya?» son correctas en español.'),
                ('¿Cuál es más natural para presentar al sujeto como información nueva?',
                 ['María llegó tarde.', 'Llegó tarde María.', 'Tarde llegó María.', 'María tarde llegó.'],
                 1,
                 'Información nueva al final → sujeto posvérbico: <b>Llegó tarde María</b>.'),
                ('¿Cuál usa el adjetivo con valor subjetivo o connotativo?',
                 ['Conocí a un hombre pobre en el mercado.',
                  'El pobre hombre perdió todo en el incendio.',
                  'Busco un apartamento pequeño.',
                  'Tiene una voz grave.'],
                 1,
                 'Adjetivo <b>prenominal</b> «pobre» con valor de lástima o compasión: «el <b>pobre</b> hombre».'),
                ('¿Cuál refleja el orden correcto en una pregunta indirecta?',
                 ['No sé dónde está él. (con inversión)',
                  'No sé dónde él está.',
                  'No sé dónde está.',
                  'No sé él dónde está.'],
                 2,
                 'En preguntas indirectas, el español usa orden SV normal (sin inversión): «No sé <b>dónde está</b>».'),
                ('¿Cuál usa correctamente la dislocación izquierda?',
                 ['A Pedro le encanta el fútbol.',
                  'Pedro, le encanta el fútbol.',
                  'A Pedro, le encanta el fútbol.',
                  'El fútbol, a Pedro le encanta.'],
                 2,
                 'Dislocación izquierda de OI: «A Pedro, <b>le</b> encanta el fútbol» — el clítico <b>le</b> retoma «a Pedro».'),
            ]
        ),
        ex2=dict(
            title='Transforma o explica el efecto del orden de palabras',
            questions=[
                ('Reordena con el sujeto como información nueva: «El director firmó el contrato.»',
                 'Firmó el contrato el director.',
                 ['Firmó el contrato el director.'],
                 'Sujeto nuevo al final (V-O-S): <b>Firmó el contrato el director</b>.'),
                ('¿Qué diferencia hay entre «un viejo amigo» y «un amigo viejo»?',
                 'Un viejo amigo = amigo de toda la vida (valor connotativo). Un amigo viejo = amigo de edad avanzada (descripción objetiva).',
                 ['viejo amigo', 'amigo viejo'],
                 'Prenominal: valor subjetivo o connotativo. Posnominal: valor descriptivo u objetivo.'),
                ('Transforma con dislocación izquierda: «He enviado el informe ya.»',
                 'El informe, ya lo he enviado.',
                 ['El informe, ya lo he enviado.'],
                 'Dislocación izquierda del OD: «El informe, ya <b>lo</b> he enviado» — el clítico <b>lo</b> retoma «el informe».'),
                ('¿Dónde va «nunca» en una oración con tiempo verbal compuesto?',
                 'Nunca antes del auxiliar o al final: «Nunca he llegado tarde» / «No he llegado tarde nunca».',
                 ['Nunca he llegado tarde', 'No he llegado tarde nunca'],
                 'El adverbio «nunca» va antes del auxiliar o al final de la oración. No va entre el auxiliar y el participio.'),
                ('Convierte en pregunta indirecta: «¿Dónde vive?» → No sé ______.',
                 'dónde vive.',
                 ['dónde vive', 'dónde vive.'],
                 'Pregunta indirecta sin inversión: «No sé <b>dónde vive</b>» (no *«dónde vive él» con inversión).'),
            ]
        ),
        ex3=dict(
            title='Identifica el fenómeno de orden de palabras',
            questions=[
                ('¿Qué fenómeno ilustra «El libro, lo dejé en la mesa»?',
                 ['Inversión sujeto-verbo.',
                  'Topicalización con dislocación izquierda.',
                  'Foco informativo posvérbico.',
                  'Pregunta indirecta.'],
                 1,
                 '«El libro» es el tópico desplazado al inicio, retomado por el clítico «lo» → <b>dislocación izquierda</b>.'),
                ('¿Por qué es más natural «Llamó un hombre» que «Un hombre llamó» para introducir un referente nuevo?',
                 ['Porque «un hombre» es el sujeto gramatical.',
                  'Porque el español siempre pone el sujeto después del verbo.',
                  'Porque en español, la información nueva preferentemente va al final de la oración.',
                  'Porque «un hombre» es un objeto directo.'],
                 2,
                 'Principio dado-nuevo: la <b>información nueva</b> tiende a ir al final → sujeto nuevo posvérbico.'),
                ('¿Cuál de estos adjetivos cambia significativamente de sentido según su posición?',
                 ['rojo', 'grande', 'circular', 'metálico'],
                 1,
                 '«<b>Grande</b>» cambia de significado según la posición: prenominal → «gran» (admirable, importante); posnominal → «grande» (de gran tamaño).'),
                ('¿Cuál ilustra la inversión V-S para presentar información nueva?',
                 ['María llegó tarde.',
                  'Llegó tarde María.',
                  'María, llegó tarde.',
                  'La llegada tarde de María.'],
                 1,
                 'Inversión V-S con sujeto nuevo al final: «Llegó tarde <b>María</b>» — María es la información nueva o contrastiva.'),
                ('En «No sé quién lo hizo», ¿hay inversión sujeto-verbo?',
                 ['Sí, es obligatoria en todas las interrogativas.',
                  'No, las preguntas indirectas mantienen el orden SV normal.',
                  'Sí, pero solo después de «quién».',
                  'No, porque el verbo es «sé», no «hizo».'],
                 1,
                 'Las preguntas <b>indirectas</b> no invierten el sujeto: «No sé quién <b>lo hizo</b>» (SV normal).'),
            ]
        ),
        game_desc='4 fenómenos de orden de palabras · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            dict(term='información nueva al final',
                 definition='principio dado-nuevo: el elemento de información nueva ocupa posición final en la oración',
                 example='— ¿Quién escribió eso? — <b>Lo escribió García Márquez.</b> (García Márquez = información nueva → al final)',
                 accept=['información nueva al final', 'principio dado-nuevo']),
            dict(term='dislocación izquierda',
                 definition='tópico desplazado al inicio de la oración, retomado por un clítico',
                 example='<b>El contrato, lo firmamos ayer</b>: «el contrato» es el tópico; «lo» es el clítico de retoma.',
                 accept=['dislocación izquierda']),
            dict(term='inversión verbo-sujeto',
                 definition='el sujeto aparece después del verbo para presentarse como información nueva',
                 example='<b>Llegó tarde el director</b>: el director es la información nueva presentada al final.',
                 accept=['inversión verbo-sujeto', 'inversión V-S', 'orden VS']),
            dict(term='adjetivo prenominal',
                 definition='adjetivo colocado antes del sustantivo: valor subjetivo, connotativo o enfático',
                 example='Es una <b>gran</b> oportunidad: «gran» (prenominal) expresa valor subjetivo de importancia.',
                 accept=['adjetivo prenominal', 'prenominal']),
            dict(term='adjetivo posnominal',
                 definition='adjetivo colocado después del sustantivo: valor restrictivo, objetivo o clasificatorio',
                 example='Es una ciudad <b>grande</b>: «grande» (posnominal) describe el tamaño de forma objetiva.',
                 accept=['adjetivo posnominal', 'posnominal']),
            dict(term='pregunta indirecta sin inversión',
                 definition='en preguntas indirectas, el orden es SV normal, sin inversión del sujeto',
                 example='No sé <b>dónde vive</b> (no *«dónde vive él» con inversión como en la pregunta directa).',
                 accept=['pregunta indirecta sin inversión', 'pregunta indirecta']),
            dict(term='topicalización',
                 definition='desplazamiento de un constituyente al inicio de la oración para marcarlo como tópico',
                 example='<b>El libro</b>, lo compré ayer en la Feria del Libro: «el libro» es el tópico topicalizado.',
                 accept=['topicalización']),
            dict(term='foco contrastivo',
                 definition='elemento destacado como la información más relevante o contrastiva de la oración',
                 example='Lo hizo <b>ella</b>, no él: «ella» es el <b>foco contrastivo</b>, opuesto a «él».',
                 accept=['foco contrastivo', 'foco']),
        ],
    ),
}
