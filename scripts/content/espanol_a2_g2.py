# -*- coding: utf-8 -*-
"""espanol/ A2 Gramática — lote 2 (G06–G10)."""

CHAPTERS = {
    'comparativos': dict(
        level='a2',
        section='grammar',
        num='G06',
        short='Comparativos',
        title='Comparativos y Superlativos — Comparar personas y cosas',
        subtitle='Aprende a comparar con más/menos/tan...como y a expresar el grado máximo con el superlativo.',
        slides=[
            (
                'Comparativos de superioridad e inferioridad',
                'más / menos + adjetivo/adverbio + que',
                '<p>Usamos <strong>más + adj/adv + que</strong> para indicar superioridad y <strong>menos + adj/adv + que</strong> para inferioridad.</p>'
                '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
                '<tr><th style="background:var(--amber);color:#fff;padding:6px 10px">Tipo</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Estructura</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Ejemplo</th></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">Superioridad</td><td style="padding:6px 10px">más + adj + que</td><td style="padding:6px 10px">Madrid es <em>más grande que</em> Bilbao.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">Inferioridad</td><td style="padding:6px 10px">menos + adj + que</td><td style="padding:6px 10px">Este libro es <em>menos interesante que</em> el otro.</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">Igualdad</td><td style="padding:6px 10px">tan + adj + como</td><td style="padding:6px 10px">Ana es <em>tan alta como</em> su hermano.</td></tr>'
                '</table>'
                '<p>Con sustantivos usamos <strong>tanto/a/os/as + sust + como</strong>: <em>Tengo tantos libros como tú.</em></p>',
            ),
            (
                'Comparativos irregulares',
                'mejor / peor / mayor / menor',
                '<p>Estos cuatro comparativos son irregulares y no usan <em>más</em> ni <em>menos</em>:</p>'
                '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
                '<tr><th style="background:var(--amber);color:#fff;padding:6px 10px">Adjetivo base</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Comparativo</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Ejemplo</th></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">bueno/a</td><td style="padding:6px 10px">mejor(es)</td><td style="padding:6px 10px">Este restaurante es <em>mejor que</em> el otro.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">malo/a</td><td style="padding:6px 10px">peor(es)</td><td style="padding:6px 10px">El tiempo hoy es <em>peor que</em> ayer.</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">grande</td><td style="padding:6px 10px">mayor(es)</td><td style="padding:6px 10px">Mi hermana es <em>mayor que</em> yo.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">pequeño/a</td><td style="padding:6px 10px">menor(es)</td><td style="padding:6px 10px">El riesgo es <em>menor que</em> pensábamos.</td></tr>'
                '</table>'
                '<p><strong>Nota:</strong> <em>Mayor/menor</em> también expresan edad o importancia, no solo tamaño.</p>',
            ),
            (
                'Superlativo relativo',
                'el/la/los/las + más/menos + adjetivo + de',
                '<p>El superlativo relativo indica el grado máximo dentro de un grupo. Se forma con <strong>artículo + más/menos + adj + de</strong>:</p>'
                '<ul style="line-height:2">'
                '<li>Es <strong>el edificio más alto de</strong> la ciudad.</li>'
                '<li>Sofía es <strong>la estudiante más trabajadora de</strong> la clase.</li>'
                '<li>Estos son <strong>los precios más bajos del</strong> mercado.</li>'
                '<li>Es <strong>el menos interesante de</strong> todos los cursos.</li>'
                '</ul>'
                '<p>Con comparativos irregulares: <em>Es el mejor restaurante de la zona.</em></p>',
            ),
            (
                'Superlativo absoluto',
                '-ísimo/a/os/as — el grado máximo sin comparar',
                '<p>El superlativo absoluto expresa un grado muy alto sin comparar con nadie. Se añade <strong>-ísimo/a</strong> al adjetivo (quitando la vocal final si termina en vocal):</p>'
                '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
                '<tr><th style="background:var(--amber);color:#fff;padding:6px 10px">Adjetivo</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Superlativo absoluto</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Ejemplo</th></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">grande</td><td style="padding:6px 10px">grandísimo</td><td style="padding:6px 10px">La casa es <em>grandísima</em>.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">fácil</td><td style="padding:6px 10px">facilísimo</td><td style="padding:6px 10px">El examen fue <em>facilísimo</em>.</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">rico</td><td style="padding:6px 10px">riquísimo</td><td style="padding:6px 10px">Esta sopa está <em>riquísima</em>.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">largo</td><td style="padding:6px 10px">larguísimo</td><td style="padding:6px 10px">El camino es <em>larguísimo</em>.</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">feliz</td><td style="padding:6px 10px">felicísimo</td><td style="padding:6px 10px">Estoy <em>felicísima</em> hoy.</td></tr>'
                '</table>'
                '<p>También se puede usar <em>muy + adj</em> con el mismo significado: <em>muy grande = grandísimo</em>.</p>',
            ),
            (
                'Repaso y contrastes clave',
                'Cuándo usar cada estructura',
                '<p>Resumen de todas las estructuras comparativas:</p>'
                '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
                '<tr><th style="background:var(--amber);color:#fff;padding:6px 10px">Función</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Estructura</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Ejemplo</th></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">Superioridad</td><td style="padding:6px 10px">más + adj + que</td><td style="padding:6px 10px">Pedro es más alto que Luis.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">Inferioridad</td><td style="padding:6px 10px">menos + adj + que</td><td style="padding:6px 10px">Este coche es menos caro que el otro.</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">Igualdad (adj)</td><td style="padding:6px 10px">tan + adj + como</td><td style="padding:6px 10px">María es tan lista como Juan.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">Igualdad (sust)</td><td style="padding:6px 10px">tanto/a + sust + como</td><td style="padding:6px 10px">Tengo tanto dinero como tú.</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">Sup. relativo</td><td style="padding:6px 10px">el/la más + adj + de</td><td style="padding:6px 10px">Es la película más bonita del año.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">Sup. absoluto</td><td style="padding:6px 10px">adj + -ísimo/a</td><td style="padding:6px 10px">La comida estaba buenísima.</td></tr>'
                '</table>',
            ),
        ],
        traps=[
            (
                'más mejor',
                '<strong>mejor</strong>',
                '<em>Mejor</em> ya es un comparativo; añadir <em>más</em> es redundante e incorrecto. Di simplemente: <em>Este método es mejor que el anterior.</em>',
            ),
            (
                'tan grande como yo esperaba',
                '<strong>tan grande como yo esperaba</strong> (correcto, pero cuidado con <em>tanto</em>)',
                'Con adjetivos usa <em>tan + adj + como</em>. Con sustantivos usa <em>tanto/a/os/as + sust + como</em>. El error común es usar <em>tan</em> con sustantivos: <em>*tan libros como</em> — incorrecto.',
            ),
            (
                'el más bueno de la clase',
                '<strong>el mejor de la clase</strong>',
                'Con los comparativos irregulares (mejor, peor, mayor, menor) no se usa <em>más</em>. La forma correcta en superlativo relativo es <em>el mejor</em>, no <em>el más bueno</em>.',
            ),
            (
                'muy altísimo',
                '<strong>altísimo</strong> o <strong>muy alto</strong>',
                '<em>-ísimo</em> ya expresa el grado máximo; combinar con <em>muy</em> es una redundancia incorrecta. Usa uno u otro, no los dos juntos.',
            ),
            (
                'Es el mejor estudiante en la clase',
                '<strong>Es el mejor estudiante de la clase</strong>',
                'Después del superlativo relativo se usa la preposición <em>de</em>, no <em>en</em>, para introducir el grupo de referencia: <em>el mejor de la clase, el más alto del equipo</em>.',
            ),
        ],
        summary=[
            ('Superioridad', 'más + adj/adv + que', 'Este hotel es más cómodo que el anterior.'),
            ('Inferioridad', 'menos + adj/adv + que', 'El tren es menos rápido que el avión.'),
            ('Igualdad (adj)', 'tan + adj + como', 'Hoy hace tan frío como ayer.'),
            ('Igualdad (sust)', 'tanto/a/os/as + sust + como', 'Ella tiene tanta experiencia como él.'),
            ('Comparativo irregular', 'mejor / peor / mayor / menor + que', 'Esta solución es peor que la primera.'),
            ('Superlativo relativo', 'el/la/los/las + más/menos + adj + de', 'Es el museo más visitado de España.'),
            ('Superlativo absoluto', 'adj + -ísimo/a/os/as', 'La obra de teatro estuvo buenísima.'),
        ],
        ex1=(
            'Ejercicio 1 — Selección múltiple: Comparativos',
            'Elige la opción correcta para completar cada oración.',
            [
                (
                    'El metro es _____ rápido _____ el autobús.',
                    ['más... que', 'tan... como', 'tanto... como'],
                    'más... que',
                    'Expresamos superioridad con <em>más + adjetivo + que</em>. El metro supera en rapidez al autobús.',
                ),
                (
                    'Mi hermana es _____ alta _____ yo.',
                    ['tan... como', 'más... de', 'tan... que'],
                    'tan... como',
                    'La igualdad de adjetivos se expresa con <em>tan + adj + como</em>.',
                ),
                (
                    'Esta película es la _____ interesante _____ todas.',
                    ['más... de', 'más... que', 'mejor... de'],
                    'más... de',
                    'El superlativo relativo usa <em>el/la más + adj + de</em> para indicar el grado máximo dentro de un grupo.',
                ),
                (
                    'El nuevo profesor es _____ que el anterior — explica mucho mejor.',
                    ['más bueno', 'mejor', 'buenísimo'],
                    'mejor',
                    '<em>Mejor</em> es el comparativo irregular de <em>bueno</em>. No se dice <em>más bueno</em>.',
                ),
                (
                    'Hoy tengo _____ trabajo _____ ayer — estoy agotado.',
                    ['más... que', 'tanto... como', 'tan... como'],
                    'más... que',
                    'Con sustantivos en comparaciones de superioridad usamos <em>más + sust + que</em>.',
                ),
                (
                    'La sopa que hizo mi abuela estaba _____.',
                    ['muy buenísima', 'buenísima', 'más buena'],
                    'buenísima',
                    'El superlativo absoluto <em>-ísimo/a</em> ya expresa el grado máximo. No se combina con <em>muy</em>.',
                ),
            ],
        ),
        ex2=(
            'Ejercicio 2 — Escribe la forma correcta',
            'Completa las oraciones con la forma comparativa o superlativa correcta del adjetivo entre paréntesis.',
            [
                (
                    'El Aconcagua es la montaña _____ (alto) de América del Sur.',
                    'más alta',
                    'Superlativo relativo: <em>la más alta de</em>. El adjetivo concuerda en género y número con el sustantivo femenino <em>montaña</em>.',
                ),
                (
                    'Este examen fue _____ (fácil) — terminé en diez minutos.',
                    'facilísimo',
                    'Superlativo absoluto: <em>fácil → facilísimo</em>. La -l final permanece y se añade -ísimo.',
                ),
                (
                    'Mi abuela es _____ (mayor) que mi abuelo — tiene tres años más.',
                    'mayor',
                    '<em>Mayor</em> es el comparativo irregular de <em>grande</em> para referirse a la edad. No se dice <em>más grande</em> en este contexto.',
                ),
                (
                    'Este camino es _____ (largo) que el otro — tardamos dos horas más.',
                    'más largo',
                    'Comparativo de superioridad regular: <em>más + adj + que</em>.',
                ),
                (
                    'La nueva versión del programa es _____ (malo) que la anterior — tiene muchos errores.',
                    'peor',
                    '<em>Peor</em> es el comparativo irregular de <em>malo</em>. No se dice <em>más malo</em> en este contexto.',
                ),
            ],
        ),
        ex3=(
            'Ejercicio 3 — Corrección de errores',
            'Cada oración contiene un error. Elige la versión corregida.',
            [
                (
                    '"Esta novela es más mejor que la anterior."',
                    [
                        'Esta novela es mejor que la anterior.',
                        'Esta novela es más buena que la anterior.',
                        'Esta novela es la mejor que la anterior.',
                    ],
                    'Esta novela es mejor que la anterior.',
                    '<em>Mejor</em> ya es comparativo; añadir <em>más</em> es redundante. La forma correcta es simplemente <em>mejor que</em>.',
                ),
                (
                    '"Tengo tan problemas como tú."',
                    [
                        'Tengo tantos problemas como tú.',
                        'Tengo tan muchos problemas como tú.',
                        'Tengo más problemas que tú.',
                    ],
                    'Tengo tantos problemas como tú.',
                    'Con sustantivos usamos <em>tanto/a/os/as</em>, no <em>tan</em>. <em>Problemas</em> es masculino plural, entonces <em>tantos</em>.',
                ),
                (
                    '"Es el restaurante más bueno en la ciudad."',
                    [
                        'Es el mejor restaurante de la ciudad.',
                        'Es el más bueno restaurante de la ciudad.',
                        'Es el restaurante mejor en la ciudad.',
                    ],
                    'Es el mejor restaurante de la ciudad.',
                    'Dos errores: se usa el comparativo irregular <em>mejor</em>, no <em>más bueno</em>, y la preposición es <em>de</em>, no <em>en</em>.',
                ),
                (
                    '"Esta tarea es muy facilísima."',
                    [
                        'Esta tarea es facilísima.',
                        'Esta tarea es muy fácil y facilísima.',
                        'Esta tarea es la más fácil.',
                    ],
                    'Esta tarea es facilísima.',
                    '<em>-ísimo/a</em> ya expresa el grado máximo. Combinar <em>muy</em> con <em>-ísimo</em> es incorrecto en español estándar.',
                ),
                (
                    '"Mi hermano es menor que yo — solo tiene seis años."',
                    [
                        'Mi hermano es menor que yo — solo tiene seis años.',
                        'Mi hermano es más pequeño que yo — solo tiene seis años.',
                        'Mi hermano es más menor que yo — solo tiene seis años.',
                    ],
                    'Mi hermano es menor que yo — solo tiene seis años.',
                    'Esta oración es correcta. <em>Menor</em> se usa para comparar edades y es el comparativo irregular de <em>pequeño</em> en este contexto.',
                ),
            ],
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('comp-sup-01', 'más ... que', 'Expresa que algo tiene una cualidad en mayor grado que otra cosa', 'comparativo de superioridad', 'Este edificio es más alto que el mío.', 'El monte Everest es _____ alto _____ cualquier otra montaña del mundo.', 'más ... que'),
            ('comp-inf-02', 'menos ... que', 'Expresa que algo tiene una cualidad en menor grado que otra cosa', 'comparativo de inferioridad', 'El autobús es menos cómodo que el tren.', 'Este apartamento es _____ espacioso _____ el anterior.', 'menos ... que'),
            ('comp-igu-03', 'tan ... como', 'Expresa que dos cosas tienen la misma cualidad en igual grado', 'comparativo de igualdad', 'Hoy hace tan calor como ayer.', 'Mi perro es _____ inteligente _____ el tuyo.', 'tan ... como'),
            ('comp-irr-04', 'mejor', 'Comparativo irregular de bueno; indica superioridad en calidad', 'superior en calidad', 'Este médico es mejor que el anterior.', 'La segunda propuesta es _____ que la primera — tiene menos errores.', 'mejor'),
            ('comp-irr-05', 'peor', 'Comparativo irregular de malo; indica inferioridad en calidad', 'inferior en calidad', 'El tiempo hoy es peor que ayer.', 'Este resultado es _____ de lo esperado — fallaron tres pruebas.', 'peor'),
            ('sup-rel-06', 'el/la más ... de', 'Indica el grado máximo de una cualidad dentro de un grupo', 'superlativo relativo', 'Es la ciudad más bonita de todo el país.', 'El Nilo es _____ río largo _____ África.', 'el ... más ... de'),
            ('sup-abs-07', '-ísimo/a', 'Expresa un grado muy alto de una cualidad sin comparar con nadie', 'superlativo absoluto', 'La paella estaba riquísima.', 'El partido estuvo aburr_____ — no marcaron ningún gol.', 'idísimo'),
            ('comp-may-08', 'mayor / menor', 'Comparativos irregulares usados especialmente para expresar diferencia de edad', 'comparativo de edad', 'Mi hermana mayor tiene veinte años.', 'Carlos tiene treinta años y Roberto tiene veinticinco: Carlos es _____ que Roberto.', 'mayor'),
        ],
    ),

    'pronombres-objeto': dict(
        level='a2',
        section='grammar',
        num='G07',
        short='Pronombres Objeto',
        title='Pronombres de Complemento Directo e Indirecto — Lo, la, le y sus combinaciones',
        subtitle='Domina los pronombres objeto para evitar repeticiones y hablar con fluidez.',
        slides=[
            (
                'Pronombres de Complemento Directo (CD)',
                'lo / la / los / las — sustituyen al objeto directo',
                '<p>El <strong>complemento directo</strong> responde a la pregunta <em>¿qué?</em> o <em>¿a quién?</em> del verbo. Los pronombres CD son:</p>'
                '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
                '<tr><th style="background:var(--amber);color:#fff;padding:6px 10px">Persona</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Singular</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Plural</th></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">1.ª</td><td style="padding:6px 10px">me</td><td style="padding:6px 10px">nos</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">2.ª</td><td style="padding:6px 10px">te</td><td style="padding:6px 10px">os</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">3.ª masc.</td><td style="padding:6px 10px">lo</td><td style="padding:6px 10px">los</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">3.ª fem.</td><td style="padding:6px 10px">la</td><td style="padding:6px 10px">las</td></tr>'
                '</table>'
                '<p>Ejemplos: <em>¿Has visto la película? — Sí, <strong>la</strong> he visto.</em><br>'
                '<em>¿Tienes los libros? — No, no <strong>los</strong> tengo.</em></p>',
            ),
            (
                'Pronombres de Complemento Indirecto (CI)',
                'le / les — sustituyen al objeto indirecto',
                '<p>El <strong>complemento indirecto</strong> responde a <em>¿a quién?</em> o <em>¿para quién?</em>. Los pronombres CI de tercera persona son <strong>le</strong> (singular) y <strong>les</strong> (plural). Son invariables en género.</p>'
                '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
                '<tr><th style="background:var(--amber);color:#fff;padding:6px 10px">Persona</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Singular</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Plural</th></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">1.ª</td><td style="padding:6px 10px">me</td><td style="padding:6px 10px">nos</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">2.ª</td><td style="padding:6px 10px">te</td><td style="padding:6px 10px">os</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">3.ª</td><td style="padding:6px 10px">le</td><td style="padding:6px 10px">les</td></tr>'
                '</table>'
                '<p>Ejemplos:<br>'
                '<em>Le dije la verdad a María.</em> (a María = CI)<br>'
                '<em>Les mandé un mensaje a mis amigos.</em> (a mis amigos = CI)<br>'
                'Con frecuencia se usa el pronombre CI junto al nombre para claridad: <em>Le dije <strong>a ella</strong>...</em></p>',
            ),
            (
                'Orden cuando se combinan CD y CI',
                'CI + CD — el indirecto siempre va primero',
                '<p>Cuando usamos los dos pronombres juntos, el <strong>CI va antes que el CD</strong>. Y cuando el CI es <em>le/les</em>, se convierte en <strong>se</strong>:</p>'
                '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
                '<tr><th style="background:var(--amber);color:#fff;padding:6px 10px">Combinación</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Resultado</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Ejemplo</th></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">le + lo/la</td><td style="padding:6px 10px">se lo / se la</td><td style="padding:6px 10px">Se lo dije. (= Le dije eso a él/ella)</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">les + lo/la</td><td style="padding:6px 10px">se lo / se la</td><td style="padding:6px 10px">Se la mandé. (= Les mandé la carta a ellos)</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">me + lo/la</td><td style="padding:6px 10px">me lo / me la</td><td style="padding:6px 10px">Me lo explicó muy bien.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">te + los/las</td><td style="padding:6px 10px">te los / te las</td><td style="padding:6px 10px">Te los devuelvo mañana.</td></tr>'
                '</table>',
            ),
            (
                'Posición del pronombre',
                'Antes del verbo conjugado o unido al infinitivo/gerundio',
                '<p>Los pronombres objeto van <strong>antes del verbo conjugado</strong>. Con infinitivo o gerundio, pueden ir <strong>antes del verbo auxiliar</strong> o <strong>unidos al infinitivo/gerundio</strong>. Ambas formas son correctas:</p>'
                '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
                '<tr><th style="background:var(--amber);color:#fff;padding:6px 10px">Estructura</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Pronombre antes</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Pronombre unido</th></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">querer + inf</td><td style="padding:6px 10px">Lo quiero comprar.</td><td style="padding:6px 10px">Quiero comprarlo.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">estar + ger</td><td style="padding:6px 10px">Lo estoy leyendo.</td><td style="padding:6px 10px">Estoy leyéndolo.</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">poder + inf</td><td style="padding:6px 10px">No te puedo ayudar.</td><td style="padding:6px 10px">No puedo ayudarte.</td></tr>'
                '</table>'
                '<p><strong>Importante:</strong> al unir el pronombre al gerundio, hay que añadir tilde si es necesario: <em>leyéndolo, haciéndolo</em>.</p>',
            ),
        ],
        traps=[
            (
                'Le vi en el parque. (refiriéndose a un hombre)',
                '<strong>Lo vi en el parque.</strong>',
                'Para el complemento directo de persona masculina se usa <em>lo</em> (norma estándar panhispánica), no <em>le</em>. El uso de <em>le</em> como CD masculino (<em>leísmo</em>) existe en algunas zonas de España pero no es la norma general.',
            ),
            (
                'Se les enviamos el correo.',
                '<strong>Se lo enviamos.</strong>',
                'Cuando <em>le/les</em> precede a un pronombre CD, se transforma en <em>se</em>. La frase correcta es <em>se lo enviamos</em> (se = a ellos, lo = el correo).',
            ),
            (
                'Lo le dije.',
                '<strong>Se lo dije.</strong>',
                'El orden siempre es CI + CD, y <em>le/les</em> ante un pronombre CD se convierte en <em>se</em>. Nunca se antepone el CD al CI.',
            ),
            (
                'Quiero comprarlo a ella el libro.',
                '<strong>Quiero comprárselo.</strong> / <strong>Se lo quiero comprar.</strong>',
                'Cuando se combinan dos pronombres con infinitivo, ambos se unen al final o van juntos antes del auxiliar. No se separan: <em>se lo quiero comprar</em> o <em>quiero comprárselo</em>.',
            ),
            (
                'Ella les escribió a sus padres el mensaje.',
                '<strong>Ella les escribió el mensaje a sus padres.</strong>',
                'El pronombre CI puede coexistir con el complemento nominal para dar énfasis o claridad, pero la oración requiere el pronombre <em>les</em> de todos modos: <em>les escribió el mensaje a sus padres</em>.',
            ),
        ],
        summary=[
            ('CD 3.ª masc.', 'lo / los', 'No encuentro el libro. — ¿Lo has visto?'),
            ('CD 3.ª fem.', 'la / las', 'Compré las entradas. — Las compré ayer.'),
            ('CI 3.ª', 'le / les', 'Le mandé un regalo a mi madre.'),
            ('CI + CD (le → se)', 'se lo / se la / se los / se las', 'Le di el informe. → Se lo di.'),
            ('Posición: verbo conjugado', 'pronombre + verbo', 'No lo entiendo. / La veo cada día.'),
            ('Posición: infinitivo/gerundio', 'auxiliar + pron + inf  O  inf + pron', 'Lo quiero ver. / Quiero verlo.'),
        ],
        ex1=(
            'Ejercicio 1 — Selección múltiple: Pronombres objeto',
            'Elige el pronombre correcto para sustituir la parte subrayada.',
            [
                (
                    '¿Has comprado el pan? — Sí, _____ he comprado esta mañana.',
                    ['lo', 'le', 'la'],
                    'lo',
                    '<em>El pan</em> es el complemento directo, masculino singular. El pronombre CD correspondiente es <em>lo</em>.',
                ),
                (
                    'Voy a llamar a mis hermanas ahora mismo. — _____ voy a llamar enseguida.',
                    ['Las', 'Les', 'Los'],
                    'Las',
                    '<em>A mis hermanas</em> es el complemento directo de <em>llamar</em>, femenino plural. El pronombre CD es <em>las</em>.',
                ),
                (
                    'Le mandé un correo a mi jefe. — _____ mandé un correo.',
                    ['Lo', 'Le', 'Se'],
                    'Le',
                    '<em>A mi jefe</em> es el complemento indirecto. El pronombre CI de tercera persona singular es <em>le</em>.',
                ),
                (
                    'Voy a explicarle la gramática a los estudiantes. — Voy a _____ la gramática.',
                    ['explicarles', 'explicarlos', 'explicarle'],
                    'explicarles',
                    '<em>A los estudiantes</em> es CI plural. El pronombre es <em>les</em>, que se une al infinitivo: <em>explicarles</em>.',
                ),
                (
                    'Le di el regalo a mi madre. — _____ di.',
                    ['Le lo', 'Se lo', 'Lo le'],
                    'Se lo',
                    'Cuando el CI (<em>le</em>) va junto al CD (<em>lo</em>), el CI se convierte en <em>se</em>: <em>se lo</em>. El orden es siempre CI + CD.',
                ),
                (
                    'Estoy leyendo el informe ahora. — Estoy _____ ahora.',
                    ['leyéndolo', 'leyéndole', 'lo leyendo'],
                    'leyéndolo',
                    'El pronombre se puede unir al gerundio. <em>El informe</em> es CD masculino singular: <em>leyéndolo</em>. Se añade tilde para mantener el acento.',
                ),
            ],
        ),
        ex2=(
            'Ejercicio 2 — Escribe el pronombre correcto',
            'Reescribe la parte entre corchetes con el pronombre de objeto directo o indirecto adecuado.',
            [
                (
                    '¿Tienes [las llaves]? — Sí, _____ tengo en el bolsillo.',
                    'las',
                    '<em>Las llaves</em> es CD femenino plural. El pronombre CD correspondiente es <em>las</em>.',
                ),
                (
                    'Quiero comprar [ese ordenador]. _____ quiero comprar en la tienda de informática.',
                    'Lo',
                    '<em>Ese ordenador</em> es CD masculino singular. El pronombre es <em>lo</em>, que va antes del verbo auxiliar conjugado.',
                ),
                (
                    'Necesito hablar [a ti] urgentemente. Necesito hablar_____ urgentemente.',
                    'te',
                    '<em>A ti</em> es CI de segunda persona singular. El pronombre CI es <em>te</em>, que se une al infinitivo.',
                ),
                (
                    'Enviamos [el contrato] [a los clientes] la semana pasada. _____ _____ enviamos la semana pasada.',
                    'Se lo',
                    '<em>A los clientes</em> = CI (les → se ante CD). <em>El contrato</em> = CD masculino singular (lo). Orden: se + lo.',
                ),
                (
                    'Están buscando [a María] por todo el edificio. _____ están buscando por todo el edificio.',
                    'La',
                    '<em>A María</em> es CD femenino singular. El pronombre CD es <em>la</em>, que va antes del verbo auxiliar.',
                ),
            ],
        ),
        ex3=(
            'Ejercicio 3 — Corrección de errores',
            'Cada oración tiene un error con los pronombres objeto. Elige la versión correcta.',
            [
                (
                    '"Le veo todos los días en el trabajo." (refiriéndose a un compañero masculino)',
                    [
                        'Lo veo todos los días en el trabajo.',
                        'Les veo todos los días en el trabajo.',
                        'La veo todos los días en el trabajo.',
                    ],
                    'Lo veo todos los días en el trabajo.',
                    'Para el complemento directo masculino en español estándar se usa <em>lo</em>, no <em>le</em>. El leísmo no es la norma general.',
                ),
                (
                    '"Lo le di el dinero."',
                    [
                        'Se lo di.',
                        'Le lo di.',
                        'Lo di a él.',
                    ],
                    'Se lo di.',
                    'El orden correcto es CI + CD. Además, <em>le</em> ante un pronombre CD se convierte en <em>se</em>: <em>se lo di</em>.',
                ),
                (
                    '"Puedo explicarle a ella los ejercicios. → Se los puedo explicar a ella."',
                    [
                        'Se los puedo explicar a ella.',
                        'Les los puedo explicar a ella.',
                        'Le los puedo explicar a ella.',
                    ],
                    'Se los puedo explicar a ella.',
                    'La oración es correcta: <em>le → se</em> ante <em>los</em>, y el pronombre nominal <em>a ella</em> aclara el referente. Esta opción es la correcta.',
                ),
                (
                    '"Estoy haciéndola el desayuno a mi madre."',
                    [
                        'Estoy haciéndole el desayuno a mi madre.',
                        'Estoy haciéndolo el desayuno a mi madre.',
                        'Le estoy haciendo el desayuno a mi madre.',
                    ],
                    'Estoy haciéndole el desayuno a mi madre.',
                    '<em>A mi madre</em> es CI; el pronombre CI es <em>le</em>, no <em>la</em> (que sería CD femenino). También es correcta la opción <em>Le estoy haciendo</em>.',
                ),
                (
                    '"¿Las cartas? Sí, las enviamos a ellos ayer." (queremos usar dos pronombres)',
                    [
                        'Se las enviamos ayer.',
                        'Les las enviamos ayer.',
                        'Las les enviamos ayer.',
                    ],
                    'Se las enviamos ayer.',
                    '<em>A ellos</em> = CI (les → se ante CD). <em>Las cartas</em> = CD femenino plural (las). Resultado: <em>se las enviamos</em>.',
                ),
            ],
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('pron-cd-01', 'lo / la', 'Pronombres de complemento directo de tercera persona singular', 'CD singular 3.ª', 'He perdido el paraguas. — Lo he perdido.', 'No encuentro la llave. — No _____ encuentro.', 'la'),
            ('pron-cd-02', 'los / las', 'Pronombres de complemento directo de tercera persona plural', 'CD plural 3.ª', 'Compré las flores. — Las compré esta mañana.', 'Busco los documentos. — _____ busco desde ayer.', 'Los'),
            ('pron-ci-03', 'le / les', 'Pronombres de complemento indirecto de tercera persona', 'CI 3.ª', 'Le mandé un mensaje a Carlos.', 'Voy a escribir a mis padres. — Voy a escribir_____ esta noche.', 'les'),
            ('pron-se-04', 'se lo / se la', 'Combinación de CI (le/les) + CD cuando le/les se convierte en se', 'le → se + CD', 'Le di el libro. → Se lo di.', 'Les expliqué la lección. → _____ expliqué.', 'Se la'),
            ('pron-pos-05', 'antes del verbo conjugado', 'Posición estándar del pronombre objeto en oraciones con un solo verbo', 'pronombre preverbal', 'No lo entiendo. / La veo cada día.', 'Tengo el informe. — _____ tengo aquí mismo. (pronombre + verbo)', 'Lo'),
            ('pron-inf-06', 'unido al infinitivo o antes del auxiliar', 'Posición del pronombre con perífrasis verbales: dos opciones igualmente correctas', 'pronombre con infinitivo', 'Quiero comprarlo. / Lo quiero comprar.', 'Necesito llamar a Ana. — Necesito llamar_____ / _____ necesito llamar.', 'la / La'),
            ('pron-me-07', 'me / te / nos / os', 'Pronombres de primera y segunda persona para CD y CI', 'pronombres de 1.ª y 2.ª persona', 'Me ayudó mucho. / Te lo digo mañana.', 'El profesor _____ explicó la gramática a nosotros muy bien. (CI 1.ª pl.)', 'nos'),
            ('pron-ger-08', 'gerundio + pronombre (con tilde)', 'Al unir el pronombre al gerundio se añade tilde si el acento lo requiere', 'pronombre enclítico en gerundio', 'Estoy leyéndolo. / Están haciéndoselo.', 'Estoy escrib_____ una carta. (escrib + CI te + CD la)', 'iéndotela'),
        ],
    ),

    'reflexivos': dict(
        level='a2',
        section='grammar',
        num='G08',
        short='Verbos Reflexivos',
        title='Verbos Reflexivos — La rutina diaria y las acciones recíprocas',
        subtitle='Aprende a conjugar y usar los verbos reflexivos para hablar de tu rutina y de acciones mutuas.',
        slides=[
            (
                'Los verbos reflexivos: qué son y cómo se forman',
                'Pronombre reflexivo + verbo conjugado',
                '<p>Un verbo reflexivo expresa que el sujeto realiza la acción sobre sí mismo. Se conjugan con un <strong>pronombre reflexivo</strong> que concuerda con el sujeto.</p>'
                '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
                '<tr><th style="background:var(--amber);color:#fff;padding:6px 10px">Persona</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Pronombre</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">levantarse</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">ducharse</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">vestirse (e→i)</th></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">yo</td><td style="padding:6px 10px">me</td><td style="padding:6px 10px">me levanto</td><td style="padding:6px 10px">me ducho</td><td style="padding:6px 10px">me visto</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">tú</td><td style="padding:6px 10px">te</td><td style="padding:6px 10px">te levantas</td><td style="padding:6px 10px">te duchas</td><td style="padding:6px 10px">te vistes</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">él/ella</td><td style="padding:6px 10px">se</td><td style="padding:6px 10px">se levanta</td><td style="padding:6px 10px">se ducha</td><td style="padding:6px 10px">se viste</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">nosotros</td><td style="padding:6px 10px">nos</td><td style="padding:6px 10px">nos levantamos</td><td style="padding:6px 10px">nos duchamos</td><td style="padding:6px 10px">nos vestimos</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">vosotros</td><td style="padding:6px 10px">os</td><td style="padding:6px 10px">os levantáis</td><td style="padding:6px 10px">os ducháis</td><td style="padding:6px 10px">os vestís</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">ellos/ellas</td><td style="padding:6px 10px">se</td><td style="padding:6px 10px">se levantan</td><td style="padding:6px 10px">se duchan</td><td style="padding:6px 10px">se visten</td></tr>'
                '</table>',
            ),
            (
                'La rutina diaria con verbos reflexivos',
                'Verbos reflexivos más comunes',
                '<p>Los verbos reflexivos son muy frecuentes para describir la rutina diaria:</p>'
                '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
                '<tr><th style="background:var(--amber);color:#fff;padding:6px 10px">Verbo reflexivo</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Significado</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Ejemplo</th></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">despertarse</td><td style="padding:6px 10px">dejar de dormir</td><td style="padding:6px 10px">Me despierto a las siete.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">lavarse</td><td style="padding:6px 10px">limpiar el cuerpo</td><td style="padding:6px 10px">Me lavo los dientes después de comer.</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">peinarse</td><td style="padding:6px 10px">arreglar el pelo</td><td style="padding:6px 10px">Se peina frente al espejo.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">maquillarse</td><td style="padding:6px 10px">aplicar maquillaje</td><td style="padding:6px 10px">Se maquilla antes de salir.</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">acostarse</td><td style="padding:6px 10px">ir a la cama</td><td style="padding:6px 10px">Nos acostamos a las once.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">quedarse</td><td style="padding:6px 10px">permanecer en un lugar</td><td style="padding:6px 10px">Me quedé en casa todo el día.</td></tr>'
                '</table>',
            ),
            (
                'Posición del pronombre reflexivo',
                'Antes del verbo conjugado o unido al infinitivo/gerundio',
                '<p>El pronombre reflexivo sigue las mismas reglas de posición que los demás pronombres objeto:</p>'
                '<ul style="line-height:2">'
                '<li><strong>Verbo conjugado:</strong> el pronombre va delante. <em>Me levanto temprano.</em></li>'
                '<li><strong>Infinitivo:</strong> puede ir antes del auxiliar o unido al infinitivo.<br>'
                '<em>Me voy a duchar.</em> / <em>Voy a ducharme.</em></li>'
                '<li><strong>Gerundio:</strong> puede ir antes del auxiliar o unido al gerundio.<br>'
                '<em>Me estoy peinando.</em> / <em>Estoy peinándome.</em></li>'
                '<li><strong>Imperativo afirmativo:</strong> se une al verbo.<br>'
                '<em>¡Levántate! / ¡Siéntese!</em></li>'
                '</ul>',
            ),
            (
                'Uso recíproco: nos, os, se',
                'Cuando la acción es mutua entre dos o más personas',
                '<p>Los pronombres reflexivos <strong>nos / os / se</strong> también expresan una acción <strong>recíproca</strong> (que se realizan mutuamente):</p>'
                '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
                '<tr><th style="background:var(--amber);color:#fff;padding:6px 10px">Pronombre</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Uso recíproco</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Ejemplo</th></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">nos</td><td style="padding:6px 10px">nosotros ↔ nosotros</td><td style="padding:6px 10px">Nos vemos todos los días. (= el uno al otro)</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">os</td><td style="padding:6px 10px">vosotros ↔ vosotros</td><td style="padding:6px 10px">¿Os conocéis desde el colegio?</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">se</td><td style="padding:6px 10px">ellos ↔ ellos</td><td style="padding:6px 10px">Se escriben cartas cada semana.</td></tr>'
                '</table>'
                '<p>Para aclarar el sentido recíproco se puede añadir: <em>el uno al otro, mutuamente, entre sí</em>.</p>',
            ),
            (
                'Verbos que cambian de significado con se',
                'Reflexivo vs. no reflexivo',
                '<p>Algunos verbos tienen un significado diferente cuando son reflexivos:</p>'
                '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
                '<tr><th style="background:var(--amber);color:#fff;padding:6px 10px">Sin reflexivo</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Con reflexivo</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Contraste</th></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">ir (moverse)</td><td style="padding:6px 10px">irse (marcharse)</td><td style="padding:6px 10px">Voy al mercado. / Me voy a casa.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">dormir (descansar)</td><td style="padding:6px 10px">dormirse (quedarse dormido)</td><td style="padding:6px 10px">Duermo ocho horas. / Me dormí en el sofá.</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">poner (colocar)</td><td style="padding:6px 10px">ponerse (colocarse, enfadarse)</td><td style="padding:6px 10px">Pon la mesa. / Se puso nervioso.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">llamar (telefonear)</td><td style="padding:6px 10px">llamarse (tener como nombre)</td><td style="padding:6px 10px">Llama a tu madre. / Me llamo Ana.</td></tr>'
                '</table>',
            ),
        ],
        traps=[
            (
                'Me ducho a mí mismo.',
                '<strong>Me ducho.</strong>',
                'En español no se añade "a mí mismo" con los verbos reflexivos de higiene y rutina — ya está implícito en el pronombre reflexivo. Decirlo es redundante y suena muy forzado.',
            ),
            (
                'Yo me levanto yo a las siete.',
                '<strong>Yo me levanto a las siete.</strong>',
                'El sujeto explícito y el pronombre reflexivo no se repiten. Basta con <em>yo me levanto</em> o simplemente <em>me levanto</em>.',
            ),
            (
                'Ellos se escriben el uno el otro cartas.',
                '<strong>Ellos se escriben cartas (el uno al otro).</strong>',
                'La expresión aclaratoria es <em>el uno al otro</em> (no "el uno el otro"). El pronombre <em>se</em> ya indica reciprocidad; el aclarativo es opcional.',
            ),
            (
                'Voy a me duchar ahora.',
                '<strong>Voy a ducharme</strong> / <strong>Me voy a duchar</strong>',
                'El pronombre reflexivo nunca se coloca entre el auxiliar y el infinitivo. Debe ir unido al infinitivo o delante de todo el grupo verbal.',
            ),
            (
                'Se llaman Pedro y Ana.',
                '<strong>Se llaman Pedro y Ana.</strong> (correcto en contexto adecuado)',
                'Esta oración puede ser correcta ("sus nombres son Pedro y Ana"), pero es ambigua: también podría significar que se llaman por teléfono mutuamente. Si hay ambigüedad, se recomienda aclarar el contexto.',
            ),
        ],
        summary=[
            ('Formación', 'pronombre reflexivo + verbo conjugado', 'Me levanto a las seis y media.'),
            ('Pronombres', 'me / te / se / nos / os / se', 'Ella se ducha por las mañanas.'),
            ('Con infinitivo', 'pronombre + auxiliar + inf  O  auxiliar + inf + pronombre', 'Me voy a vestir. / Voy a vestirme.'),
            ('Con gerundio', 'pronombre + aux + ger  O  aux + ger + pronombre', 'Me estoy peinando. / Estoy peinándome.'),
            ('Uso recíproco', 'nos / os / se + verbo', 'Nos vemos cada semana. / Se escriben mensajes.'),
            ('Cambio de significado', 'algunos verbos cambian con el reflexivo', 'Dormir (descansar) → dormirse (quedarse dormido).'),
        ],
        ex1=(
            'Ejercicio 1 — Selección múltiple: Verbos reflexivos',
            'Elige la forma correcta del verbo reflexivo.',
            [
                (
                    'Todos los días _____ (ducharse) antes de desayunar.',
                    ['me ducho', 'ducho', 'me ducha'],
                    'me ducho',
                    'El sujeto es <em>yo</em> (implícito). El verbo reflexivo conjugado en primera persona singular es <em>me ducho</em>.',
                ),
                (
                    'Mis hijos _____ (acostarse) a las nueve de la noche.',
                    ['se acuestan', 'se acostan', 'nos acostamos'],
                    'se acuestan',
                    '<em>Acostarse</em> es un verbo con diptongación (o→ue). En tercera persona plural: <em>se acuestan</em>. La forma <em>se acostan</em> no existe.',
                ),
                (
                    'Vosotros _____ (conocerse) desde el instituto, ¿verdad?',
                    ['os conocéis', 'se conocen', 'nos conocemos'],
                    'os conocéis',
                    'Con <em>vosotros</em>, el pronombre reflexivo es <em>os</em>. El verbo en segunda persona plural es <em>conocéis</em>.',
                ),
                (
                    'Ana y Carlos _____ (llamarse) todas las noches.',
                    ['se llaman', 'os llamáis', 'nos llamamos'],
                    'se llaman',
                    'El sujeto es <em>Ana y Carlos</em> (tercera persona plural). El pronombre reflexivo es <em>se</em> y el verbo es <em>llaman</em>. También expresa reciprocidad.',
                ),
                (
                    'Necesito _____ (levantarse) temprano mañana.',
                    ['levantarme', 'me levantar', 'levantarme yo'],
                    'levantarme',
                    'Con infinitivo, el pronombre se une al final del infinitivo: <em>levantarme</em>. La posición "me levantar" no es correcta.',
                ),
                (
                    'Esta mañana Juan _____ (dormirse) en el metro y pasó su parada.',
                    ['se durmió', 'se dormió', 'durmió'],
                    'se durmió',
                    '<em>Dormirse</em> (quedarse dormido involuntariamente) es irregular en pretérito indefinido: <em>se durmió</em> (o→u en la raíz). Sin el reflexivo cambiaría el significado.',
                ),
            ],
        ),
        ex2=(
            'Ejercicio 2 — Escribe la forma correcta',
            'Conjuga el verbo reflexivo en la persona indicada.',
            [
                (
                    '(Yo — despertarse) _____ a las seis y media cada mañana.',
                    'Me despierto',
                    '<em>Despertarse</em> es un verbo con diptongación (e→ie). Primera persona singular: <em>me despierto</em>.',
                ),
                (
                    '(Nosotros — verse) _____ en el café todos los viernes.',
                    'Nos vemos',
                    'Uso recíproco de <em>verse</em>. Primera persona plural: <em>nos vemos</em>. Significa que se ven el uno al otro.',
                ),
                (
                    '(Tú — ponerse) _____ nervioso cuando tienes un examen.',
                    'Te pones',
                    '<em>Ponerse</em> es irregular en primera persona (yo me pongo), pero en segunda persona es regular: <em>te pones</em>.',
                ),
                (
                    '(Ella — peinarse) Está _____ delante del espejo ahora mismo.',
                    'peinándose',
                    'Con <em>estar + gerundio</em>, el pronombre puede unirse al gerundio: <em>peinándose</em>. Se añade tilde para mantener el acento.',
                ),
                (
                    '(Vosotros — irse) ¿A qué hora _____ mañana por la mañana?',
                    'os vais',
                    '<em>Irse</em> con el sujeto vosotros: <em>os vais</em>. El pronombre es <em>os</em> y el verbo es la forma irregular de <em>ir</em>: <em>vais</em>.',
                ),
            ],
        ),
        ex3=(
            'Ejercicio 3 — Selección múltiple: Reflexivo vs. no reflexivo',
            'Elige la opción que mejor completa la oración según el contexto.',
            [
                (
                    'El bebé _____ a las tres de la madrugada y lloró mucho.',
                    ['se despertó', 'despertó', 'le despertó'],
                    'se despertó',
                    'El bebé dejó de dormir por sí solo: uso reflexivo. <em>Se despertó</em> indica que el sujeto realizó la acción sobre sí mismo involuntariamente.',
                ),
                (
                    'La madre _____ al bebé para darle el biberón.',
                    ['despertó', 'se despertó', 'se despertó a'],
                    'despertó',
                    'Aquí la madre despertó al bebé (complemento directo). El verbo no es reflexivo porque la acción recae sobre otra persona, no sobre el sujeto.',
                ),
                (
                    'No encuentro mis gafas. Creo que _____ en el coche.',
                    ['las dejé', 'me dejé', 'me las dejé'],
                    'las dejé',
                    'Aquí "las gafas" es el complemento directo y el sujeto no realiza la acción sobre sí mismo. Se usa el pronombre de CD <em>las</em>, no el reflexivo.',
                ),
                (
                    'Todos los veranos, mi familia y yo _____ en la misma playa.',
                    ['nos reunimos', 'se reúnen', 'os reunís'],
                    'nos reunimos',
                    'El sujeto es <em>mi familia y yo</em> (= nosotros). El pronombre reflexivo/recíproco es <em>nos</em> y el verbo es <em>reunimos</em>.',
                ),
                (
                    'Cuando llegué a casa, _____ el abrigo y me senté en el sofá.',
                    ['me quité', 'quité', 'me quitó'],
                    'me quité',
                    '<em>Quitarse</em> (la ropa) es reflexivo: la acción recae sobre uno mismo. <em>Me quité el abrigo</em> es la forma correcta.',
                ),
            ],
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('refl-form-01', 'me / te / se / nos / os / se', 'Pronombres reflexivos que se usan con verbos reflexivos para indicar que la acción recae sobre el propio sujeto', 'pronombres reflexivos', 'Me levanto, te duchas, se viste.', 'Ella _____ peina cada mañana frente al espejo.', 'se'),
            ('refl-rut-02', 'levantarse', 'Verbo reflexivo que indica el acto de dejar de estar en la cama', 'dejar la cama', 'Me levanto a las siete de la mañana.', 'Mis hijos _____ muy tarde los fines de semana.', 'se levantan'),
            ('refl-rut-03', 'ducharse / lavarse', 'Verbos reflexivos de higiene personal cotidiana', 'higiene diaria', 'Siempre me ducho por la noche antes de acostarme.', 'Después de hacer deporte, _____ (nosotros) inmediatamente.', 'nos duchamos'),
            ('refl-pos-04', 'pronombre + infinitivo / infinitivo + pronombre', 'Dos posiciones correctas del pronombre reflexivo con perífrasis de infinitivo', 'posición con infinitivo', 'Me voy a vestir. / Voy a vestirme.', 'Tengo que _____ ya — llego tarde. (despertarse, yo)', 'levantarme'),
            ('refl-rec-05', 'uso recíproco (nos/os/se)', 'Cuando la acción se realiza mutuamente entre dos o más personas', 'acción mutua', 'Nos vemos todos los días en la oficina.', 'Ana y Pedro _____ mucho — son muy buenos amigos. (escribirse)', 'se escriben'),
            ('refl-sig-06', 'irse vs. ir', 'Contraste de significado entre el verbo con y sin pronombre reflexivo', 'cambio de significado', 'Voy al supermercado. / Me voy a casa, estoy cansado.', 'Ya _____ — hasta mañana. (marcharse, yo)', 'me voy'),
            ('refl-ger-07', 'gerundio + pronombre enclítico', 'Cuando el pronombre reflexivo se une al gerundio se añade tilde si es necesario', 'acento en gerundio reflexivo', 'Estoy duchándome. / Está vistiéndose.', 'Está _____ para la fiesta. (maquillarse, ella)', 'maquillándose'),
            ('refl-dif-08', 'dormirse vs. dormir', 'Contraste: dormir = descansar / dormirse = quedarse dormido involuntariamente', 'reflexivo con cambio de significado', 'Duermo ocho horas. / Me dormí en el autobús.', 'El estudiante _____ durante la clase de matemáticas. (quedarse dormido)', 'se durmió'),
        ],
    ),

    'imperativo': dict(
        level='a2',
        section='grammar',
        num='G09',
        short='Imperativo',
        title='El Imperativo — Dar órdenes, instrucciones y consejos',
        subtitle='Domina las formas afirmativas y negativas del imperativo para dar instrucciones con precisión.',
        slides=[
            (
                'El imperativo afirmativo regular',
                'tú / usted / vosotros / ustedes',
                '<p>El imperativo afirmativo se usa para dar órdenes, instrucciones o consejos. Estas son las formas regulares:</p>'
                '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
                '<tr><th style="background:var(--amber);color:#fff;padding:6px 10px">Persona</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">-AR (hablar)</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">-ER (comer)</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">-IR (escribir)</th></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">tú</td><td style="padding:6px 10px">habla</td><td style="padding:6px 10px">come</td><td style="padding:6px 10px">escribe</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">usted</td><td style="padding:6px 10px">hable</td><td style="padding:6px 10px">coma</td><td style="padding:6px 10px">escriba</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">vosotros</td><td style="padding:6px 10px">hablad</td><td style="padding:6px 10px">comed</td><td style="padding:6px 10px">escribid</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">ustedes</td><td style="padding:6px 10px">hablen</td><td style="padding:6px 10px">coman</td><td style="padding:6px 10px">escriban</td></tr>'
                '</table>'
                '<p><strong>Nota:</strong> <em>tú</em> = 3.ª pers. sg. del presente indicativo. <em>usted/ustedes</em> = formas del presente de subjuntivo.</p>',
            ),
            (
                'El imperativo negativo',
                'no + presente de subjuntivo para todas las personas',
                '<p>En el imperativo negativo, <strong>todas las personas</strong> usan el presente de subjuntivo:</p>'
                '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
                '<tr><th style="background:var(--amber);color:#fff;padding:6px 10px">Persona</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">-AR (hablar)</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">-ER (comer)</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">-IR (escribir)</th></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">tú</td><td style="padding:6px 10px">no hables</td><td style="padding:6px 10px">no comas</td><td style="padding:6px 10px">no escribas</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">usted</td><td style="padding:6px 10px">no hable</td><td style="padding:6px 10px">no coma</td><td style="padding:6px 10px">no escriba</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">vosotros</td><td style="padding:6px 10px">no habléis</td><td style="padding:6px 10px">no comáis</td><td style="padding:6px 10px">no escribáis</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">ustedes</td><td style="padding:6px 10px">no hablen</td><td style="padding:6px 10px">no coman</td><td style="padding:6px 10px">no escriban</td></tr>'
                '</table>'
                '<p>La forma <em>tú</em> negativa difiere completamente de la afirmativa: <em>habla</em> (af.) / <em>no hables</em> (neg.).</p>',
            ),
            (
                'Irregulares en el imperativo afirmativo de tú',
                'ven / ve / haz / di / pon / sal / ten / sé',
                '<p>Ocho verbos comunes tienen formas irregulares en el imperativo afirmativo de <em>tú</em>:</p>'
                '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
                '<tr><th style="background:var(--amber);color:#fff;padding:6px 10px">Infinitivo</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Imperativo tú</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Ejemplo</th></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">venir</td><td style="padding:6px 10px">ven</td><td style="padding:6px 10px">Ven aquí, por favor.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">ir</td><td style="padding:6px 10px">ve</td><td style="padding:6px 10px">Ve al médico si te duele.</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">hacer</td><td style="padding:6px 10px">haz</td><td style="padding:6px 10px">Haz los deberes ahora.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">decir</td><td style="padding:6px 10px">di</td><td style="padding:6px 10px">Di la verdad siempre.</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">poner</td><td style="padding:6px 10px">pon</td><td style="padding:6px 10px">Pon la mesa, por favor.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">salir</td><td style="padding:6px 10px">sal</td><td style="padding:6px 10px">Sal de aquí inmediatamente.</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">tener</td><td style="padding:6px 10px">ten</td><td style="padding:6px 10px">Ten paciencia, por favor.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">ser</td><td style="padding:6px 10px">sé</td><td style="padding:6px 10px">Sé amable con todos.</td></tr>'
                '</table>',
            ),
            (
                'Pronombres con el imperativo',
                'Afirmativo: pronombre unido al verbo / Negativo: pronombre antes del verbo',
                '<p>La posición del pronombre cambia según el imperativo sea afirmativo o negativo:</p>'
                '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
                '<tr><th style="background:var(--amber);color:#fff;padding:6px 10px">Tipo</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Posición del pronombre</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Ejemplo</th></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">Afirmativo</td><td style="padding:6px 10px">verbo + pronombre (enclítico)</td><td style="padding:6px 10px">Dímelo. / Levántate. / Cómpraselo.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">Negativo</td><td style="padding:6px 10px">pronombre + verbo</td><td style="padding:6px 10px">No me lo digas. / No te levantes. / No se lo compres.</td></tr>'
                '</table>'
                '<p>Al unir pronombres al imperativo afirmativo, a veces es necesario añadir tilde: <em>dime → dímelo</em>, <em>levanta → levántate</em>.</p>',
            ),
            (
                'Usos del imperativo',
                'Órdenes, instrucciones, consejos, peticiones y prohibiciones',
                '<p>El imperativo tiene varios usos en español:</p>'
                '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
                '<tr><th style="background:var(--amber);color:#fff;padding:6px 10px">Uso</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Ejemplo</th></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">Orden directa</td><td style="padding:6px 10px">¡Silencio! Siéntate.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">Instrucción</td><td style="padding:6px 10px">Gira a la derecha y sigue recto.</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">Consejo</td><td style="padding:6px 10px">Descansa un poco, que estás muy cansado.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">Petición cortés</td><td style="padding:6px 10px">Pase usted, por favor.</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">Prohibición</td><td style="padding:6px 10px">No entres sin llamar.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">Ofrecimiento</td><td style="padding:6px 10px">Coge lo que quieras.</td></tr>'
                '</table>',
            ),
        ],
        traps=[
            (
                'No habla tan alto. (imperativo negativo de tú)',
                '<strong>No hables tan alto.</strong>',
                'El imperativo negativo de <em>tú</em> usa el presente de subjuntivo, no la tercera persona del presente de indicativo. La forma correcta es <em>no hables</em>.',
            ),
            (
                'Ven aquí, no vengas allí. → "No ven allí."',
                '<strong>No vengas allí.</strong>',
                'El imperativo negativo de <em>tú</em> de <em>venir</em> es <em>no vengas</em>. La forma irregular <em>ven</em> solo se usa en el afirmativo; el negativo sigue el patrón del subjuntivo.',
            ),
            (
                'Dime lo. / Dime-lo.',
                '<strong>Dímelo.</strong>',
                'Cuando se añaden dos pronombres al imperativo afirmativo, ambos se unen directamente al verbo formando una sola palabra, y se añade tilde si es necesario: <em>dímelo</em>.',
            ),
            (
                'Hacéd los deberes. (imperativo de vosotros)',
                '<strong>Haced los deberes.</strong>',
                'La forma de vosotros del imperativo afirmativo se forma sustituyendo la -r del infinitivo por -d. No lleva tilde y no tiene irregularidades: <em>hablad, comed, escribid, haced</em>.',
            ),
            (
                'Se lo digas. (prohibición)',
                '<strong>No se lo digas.</strong>',
                'Para expresar prohibición siempre se usa <em>no</em> + subjuntivo. Sin <em>no</em>, la frase es incompleta. Además, en el imperativo negativo el pronombre va antes del verbo: <em>no se lo digas</em>.',
            ),
        ],
        summary=[
            ('Imperativo afirmativo tú (reg.)', '3.ª pers. sg. presente indicativo', 'Habla más despacio. / Come despacio.'),
            ('Imperativo negativo tú', 'no + 2.ª pers. sg. subjuntivo', 'No hables tan rápido. / No comas tan rápido.'),
            ('Imperativo usted', 'forma del presente de subjuntivo', 'Hable más alto, por favor.'),
            ('Imperativo vosotros', 'infinitivo con -r → -d', 'Hablad en voz alta. / Escribid vuestros nombres.'),
            ('Irregulares de tú', 'ven / ve / haz / di / pon / sal / ten / sé', 'Haz los deberes. / Di la verdad. / Ven aquí.'),
            ('Pronombres', 'afirm.: verbo+pron / neg.: pron+verbo', 'Dímelo (af.) / No me lo digas (neg.).'),
        ],
        ex1=(
            'Ejercicio 1 — Selección múltiple: Imperativo afirmativo',
            'Elige la forma correcta del imperativo afirmativo.',
            [
                (
                    '_____ (escuchar, tú) con atención la explicación.',
                    ['Escucha', 'Escuche', 'Escuchad'],
                    'Escucha',
                    'El imperativo afirmativo de <em>tú</em> para verbos -AR regulares es la 3.ª persona del presente indicativo: <em>escucha</em>.',
                ),
                (
                    '_____ (venir, tú) aquí un momento, necesito hablar contigo.',
                    ['Viene', 'Ven', 'Venga'],
                    'Ven',
                    '<em>Venir</em> es uno de los ocho verbos irregulares en el imperativo de tú. La forma correcta es <em>ven</em>, no <em>viene</em>.',
                ),
                (
                    '_____ (leer, vosotros) el texto en voz alta.',
                    ['Leed', 'Lean', 'Leen'],
                    'Leed',
                    'El imperativo afirmativo de <em>vosotros</em> se forma sustituyendo la -r del infinitivo por -d: <em>leer → leed</em>.',
                ),
                (
                    '_____ (poner, tú) el abrigo — hace mucho frío fuera.',
                    ['Pon', 'Pone', 'Ponga'],
                    'Pon',
                    '<em>Poner</em> tiene imperativo de tú irregular: <em>pon</em>. La forma <em>pone</em> es indicativo, no imperativo.',
                ),
                (
                    'Si tiene problemas, _____ (llamar, usted) a este número de teléfono.',
                    ['llame', 'llama', 'llamad'],
                    'llame',
                    'El imperativo de <em>usted</em> usa la forma del presente de subjuntivo: <em>llame</em> (del subjuntivo de <em>llamar</em>).',
                ),
                (
                    '_____ (ser, tú) más paciente con tus compañeros de trabajo.',
                    ['Sé', 'Se', 'Es'],
                    'Sé',
                    '<em>Ser</em> tiene imperativo de tú irregular: <em>sé</em> (con tilde para diferenciarlo del pronombre reflexivo <em>se</em>).',
                ),
            ],
        ),
        ex2=(
            'Ejercicio 2 — Escribe la forma del imperativo',
            'Escribe el imperativo de tú o usted (afirmativo o negativo) según se indica.',
            [
                (
                    '(hacer, tú, afirmativo) _____ ejercicio todos los días para estar en forma.',
                    'Haz',
                    '<em>Hacer</em> tiene imperativo de tú irregular: <em>haz</em>. Es uno de los ocho irregulares fundamentales.',
                ),
                (
                    '(hablar, tú, negativo) No _____ por teléfono durante la clase.',
                    'hables',
                    'Imperativo negativo de tú: <em>no</em> + presente de subjuntivo. De <em>hablar</em>: <em>no hables</em>.',
                ),
                (
                    '(salir, usted, afirmativo) _____ por la puerta principal, por favor.',
                    'Salga',
                    'Imperativo de usted: presente de subjuntivo. De <em>salir</em> (irregular): <em>salga</em>.',
                ),
                (
                    '(decir, tú, negativo) No _____ mentiras — siempre se descubren.',
                    'digas',
                    'Imperativo negativo de tú de <em>decir</em> (irregular en subjuntivo): <em>no digas</em>.',
                ),
                (
                    '(escribir, vosotros, afirmativo) _____ vuestros nombres al principio del examen.',
                    'Escribid',
                    'Imperativo de vosotros: infinitivo <em>escribir</em> → sustituir -r por -d: <em>escribid</em>.',
                ),
            ],
        ),
        ex3=(
            'Ejercicio 3 — Corrección de errores en el imperativo',
            'Cada oración tiene un error en el imperativo. Elige la versión correcta.',
            [
                (
                    '"No habla tan rápido — no te entiendo." (dirigido a tú)',
                    [
                        'No hables tan rápido.',
                        'No hablas tan rápido.',
                        'No hable tan rápido.',
                    ],
                    'No hables tan rápido.',
                    'El imperativo negativo de <em>tú</em> usa el subjuntivo: <em>no hables</em>. La forma <em>habla</em> es solo para el afirmativo.',
                ),
                (
                    '"Vene aquí cuando puedas." (imperativo irregular de tú)',
                    [
                        'Ven aquí cuando puedas.',
                        'Viene aquí cuando puedas.',
                        'Venga aquí cuando puedas.',
                    ],
                    'Ven aquí cuando puedas.',
                    'El imperativo irregular de tú de <em>venir</em> es <em>ven</em>, no <em>vene</em>. Las formas irregulares deben memorizarse.',
                ),
                (
                    '"Dime lo todo." (imperativo con dos pronombres)',
                    [
                        'Dímelo todo.',
                        'Dime-lo todo.',
                        'Me lo di todo.',
                    ],
                    'Dímelo todo.',
                    'Los pronombres se unen directamente al imperativo afirmativo sin guion: <em>dímelo</em>. Se añade tilde porque el acento cae en la antepenúltima sílaba.',
                ),
                (
                    '"Hacéd los ejercicios para mañana, chicos."',
                    [
                        'Haced los ejercicios para mañana, chicos.',
                        'Hacen los ejercicios para mañana, chicos.',
                        'Haceis los ejercicios para mañana, chicos.',
                    ],
                    'Haced los ejercicios para mañana, chicos.',
                    'La forma de vosotros no lleva tilde: <em>haced</em>, no <em>hacéd</em>. El imperativo de vosotros nunca es acentuado.',
                ),
                (
                    '"No se lo digas a nadie — es un secreto." (¿es correcta?)',
                    [
                        'Es correcta.',
                        'Di a nadie no lo.',
                        'No digas lo a nadie.',
                    ],
                    'Es correcta.',
                    'La oración es perfectamente correcta. En el imperativo negativo los pronombres van antes del verbo: <em>no se lo digas</em>. El pronombre reflexivo/CI <em>se</em> va primero, luego el CD <em>lo</em>.',
                ),
            ],
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('imp-afi-01', 'imperativo afirmativo tú (regular)', 'Se forma con la 3.ª persona del singular del presente de indicativo', '3.ª pers. sg. indicativo', 'Habla más despacio. / Corre más rápido.', '_____ (escuchar, tú) la música más bajito, por favor.', 'Escucha'),
            ('imp-neg-02', 'imperativo negativo tú', 'Se forma con "no" más la 2.ª persona del singular del presente de subjuntivo', 'no + subjuntivo tú', 'No hables tan alto. / No comas tan rápido.', 'No _____ (hablar, tú) con la boca llena.', 'hables'),
            ('imp-ust-03', 'imperativo usted/ustedes', 'Usa las formas del presente de subjuntivo para las dos personas de cortesía', 'subjuntivo para cortesía', 'Hable usted más alto. / Pasen ustedes, por favor.', '_____ (sentarse, usted) aquí, por favor.', 'Siéntese'),
            ('imp-vos-04', 'imperativo vosotros', 'Se forma sustituyendo la -r del infinitivo por -d; nunca lleva tilde', '-r → -d', 'Hablad en voz alta. / Comed toda la verdura.', '_____ (escribir, vosotros) la fecha al principio de la hoja.', 'Escribid'),
            ('imp-irr-05', 'irregulares tú: ven / ve / haz / di', 'Cuatro de los ocho imperativos irregulares de tú más frecuentes', 'imperativos irregulares 1', 'Ven aquí. / Ve al médico. / Haz la cama. / Di la verdad.', '_____ (hacer, tú) los deberes antes de salir.', 'Haz'),
            ('imp-irr-06', 'irregulares tú: pon / sal / ten / sé', 'Los otros cuatro imperativos irregulares de tú fundamentales', 'imperativos irregulares 2', 'Pon la mesa. / Sal de aquí. / Ten paciencia. / Sé honesto.', '_____ (tener, tú) cuidado con el escalón.', 'Ten'),
            ('imp-pro-07', 'afirmativo: verbo + pronombre', 'En el imperativo afirmativo el pronombre se une al verbo formando una sola palabra', 'pronombre enclítico', 'Dímelo. / Levántate. / Cómpraselo.', 'Por favor, _____ (decir, tú + me + lo) — ¡quiero saber la verdad!', 'dímelo'),
            ('imp-neg-08', 'negativo: no + pronombre + verbo', 'En el imperativo negativo el pronombre va entre no y el verbo', 'pronombre preverbal en negativo', 'No me lo digas. / No te vayas todavía.', 'No _____ (levantarse, tú) todavía — la clase no ha terminado.', 'te levantes'),
        ],
    ),

    'gerundio': dict(
        level='a2',
        section='grammar',
        num='G10',
        short='Gerundio',
        title='El Gerundio y Estar + Gerundio — Acciones en progreso',
        subtitle='Aprende a formar el gerundio y a usarlo con estar, seguir y llevar para describir acciones en curso.',
        slides=[
            (
                'Formación del gerundio',
                '-ando para -AR / -iendo para -ER e -IR',
                '<p>El gerundio es una forma no personal del verbo. Se forma así:</p>'
                '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
                '<tr><th style="background:var(--amber);color:#fff;padding:6px 10px">Tipo</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Terminación</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Ejemplos</th></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">Verbos -AR</td><td style="padding:6px 10px">-ando</td><td style="padding:6px 10px">hablar → hablando / trabajar → trabajando</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">Verbos -ER</td><td style="padding:6px 10px">-iendo</td><td style="padding:6px 10px">comer → comiendo / leer → leyendo*</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">Verbos -IR</td><td style="padding:6px 10px">-iendo</td><td style="padding:6px 10px">vivir → viviendo / escribir → escribiendo</td></tr>'
                '</table>'
                '<p>*Cuando la raíz termina en vocal, -iendo se convierte en <strong>-yendo</strong>: <em>leer → leyendo, caer → cayendo, oír → oyendo</em>.</p>',
            ),
            (
                'Gerundios irregulares y con cambio vocálico',
                'Verbos con cambio e→i y o→u en la raíz',
                '<p>Los verbos -IR con cambio vocálico en el presente también cambian en el gerundio:</p>'
                '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
                '<tr><th style="background:var(--amber);color:#fff;padding:6px 10px">Infinitivo</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Cambio</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Gerundio</th></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">decir</td><td style="padding:6px 10px">e→i</td><td style="padding:6px 10px">diciendo</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">pedir</td><td style="padding:6px 10px">e→i</td><td style="padding:6px 10px">pidiendo</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">seguir</td><td style="padding:6px 10px">e→i</td><td style="padding:6px 10px">siguiendo</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">dormir</td><td style="padding:6px 10px">o→u</td><td style="padding:6px 10px">durmiendo</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">morir</td><td style="padding:6px 10px">o→u</td><td style="padding:6px 10px">muriendo</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">ir</td><td style="padding:6px 10px">irregular</td><td style="padding:6px 10px">yendo</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">ser</td><td style="padding:6px 10px">irregular</td><td style="padding:6px 10px">siendo</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">tener</td><td style="padding:6px 10px">irregular</td><td style="padding:6px 10px">teniendo</td></tr>'
                '</table>',
            ),
            (
                'Estar + gerundio',
                'Para expresar una acción en progreso en el momento actual',
                '<p><strong>Estar + gerundio</strong> indica que una acción está ocurriendo en este momento o en un período de tiempo actual:</p>'
                '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
                '<tr><th style="background:var(--amber);color:#fff;padding:6px 10px">Persona</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Estar + gerundio</th></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">yo</td><td style="padding:6px 10px">estoy trabajando</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">tú</td><td style="padding:6px 10px">estás comiendo</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">él/ella</td><td style="padding:6px 10px">está durmiendo</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">nosotros</td><td style="padding:6px 10px">estamos estudiando</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">vosotros</td><td style="padding:6px 10px">estáis hablando</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">ellos/ellas</td><td style="padding:6px 10px">están leyendo</td></tr>'
                '</table>'
                '<p>Marcadores típicos: <em>ahora mismo, en este momento, estos días, esta semana</em>.</p>',
            ),
            (
                'Seguir + gerundio y llevar + gerundio',
                'Continuidad y duración de una acción',
                '<p>Además de <em>estar</em>, el gerundio se combina con otros verbos para expresar matices especiales:</p>'
                '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
                '<tr><th style="background:var(--amber);color:#fff;padding:6px 10px">Perífrasis</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Significado</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Ejemplo</th></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">seguir + gerundio</td><td style="padding:6px 10px">continuar haciendo algo</td><td style="padding:6px 10px">Sigue lloviendo desde ayer.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">llevar + tiempo + gerundio</td><td style="padding:6px 10px">duración de una acción hasta ahora</td><td style="padding:6px 10px">Llevo tres horas esperando.</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">seguir sin + infinitivo</td><td style="padding:6px 10px">negación continuada</td><td style="padding:6px 10px">Sigue sin llamarme.</td></tr>'
                '</table>'
                '<p>Con <em>llevar + gerundio</em> se expresa cuánto tiempo lleva una acción en progreso: <em>Llevo dos años viviendo aquí.</em></p>',
            ),
            (
                'Usos del gerundio: resumen',
                'Cuándo y cómo usar el gerundio correctamente',
                '<p>El gerundio tiene varios usos importantes en español:</p>'
                '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
                '<tr><th style="background:var(--amber);color:#fff;padding:6px 10px">Uso</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Estructura</th>'
                '<th style="background:var(--amber);color:#fff;padding:6px 10px">Ejemplo</th></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">Acción en progreso</td><td style="padding:6px 10px">estar + gerundio</td><td style="padding:6px 10px">Estoy leyendo un libro muy interesante.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">Continuidad</td><td style="padding:6px 10px">seguir + gerundio</td><td style="padding:6px 10px">Sigo buscando trabajo.</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">Duración</td><td style="padding:6px 10px">llevar + tiempo + gerundio</td><td style="padding:6px 10px">Llevamos dos horas esperando.</td></tr>'
                '<tr style="background:transparent"><td style="padding:6px 10px">Acción simultánea</td><td style="padding:6px 10px">gerundio al inicio o al final</td><td style="padding:6px 10px">Escuchando música, se relajó.</td></tr>'
                '<tr style="background:var(--paper)"><td style="padding:6px 10px">Con pronombres</td><td style="padding:6px 10px">gerundio + pronombre enclítico</td><td style="padding:6px 10px">Estoy leyéndolo. / Estoy haciéndolo.</td></tr>'
                '</table>',
            ),
        ],
        traps=[
            (
                'Estoy sabiendo la respuesta.',
                '<strong>Sé la respuesta.</strong>',
                'Los verbos de estado como <em>saber, conocer, tener, querer, poder</em> no se usan normalmente con <em>estar + gerundio</em> porque ya expresan un estado. Se usa el presente simple.',
            ),
            (
                'Llevo esperando tres horas.',
                '<strong>Llevo tres horas esperando.</strong>',
                'La estructura correcta de <em>llevar + gerundio</em> es: <em>llevar + expresión de tiempo + gerundio</em>. El tiempo va entre <em>llevar</em> y el gerundio.',
            ),
            (
                'Estoy comido.',
                '<strong>Estoy comiendo.</strong>',
                '<em>Estar</em> para acciones en progreso requiere el gerundio (-ando/-iendo), no el participio (-ado/-ido). <em>Estoy comido</em> significaría algo como "estoy consumido/gastado", no "estoy comiendo".',
            ),
            (
                'Leyendo el libro, me dormí. → "Leyiéndo el libro..."',
                '<strong>Leyendo</strong>',
                'El gerundio de <em>leer</em> es <em>leyendo</em> (no <em>leyiendo</em>). Cuando la raíz termina en vocal, la terminación es <em>-yendo</em> sin la <em>i</em> inicial adicional.',
            ),
            (
                'Sigo a estudiar español.',
                '<strong>Sigo estudiando español.</strong>',
                '<em>Seguir</em> en perífrasis verbal se construye con gerundio, no con infinitivo precedido de <em>a</em>. La estructura correcta es <em>seguir + gerundio</em>.',
            ),
        ],
        summary=[
            ('Formación -AR', 'raíz + -ando', 'trabajar → trabajando / hablar → hablando'),
            ('Formación -ER/-IR', 'raíz + -iendo', 'comer → comiendo / vivir → viviendo'),
            ('Irregulares con cambio vocálico', 'e→i / o→u en raíz', 'pedir → pidiendo / dormir → durmiendo'),
            ('Estar + gerundio', 'acción en progreso ahora', 'Estoy estudiando para el examen.'),
            ('Seguir + gerundio', 'acción que continúa', 'Sigue lloviendo — no salgas.'),
            ('Llevar + tiempo + gerundio', 'duración de la acción hasta ahora', 'Llevo dos horas esperando el autobús.'),
        ],
        ex1=(
            'Ejercicio 1 — Selección múltiple: Formación del gerundio',
            'Elige la forma correcta del gerundio.',
            [
                (
                    '¿Cómo se forma el gerundio de <em>leer</em>?',
                    ['leyendo', 'leendo', 'leyiendo'],
                    'leyendo',
                    '<em>Leer</em> tiene la raíz <em>le-</em>, que termina en vocal. La terminación es <em>-yendo</em>: <em>leyendo</em>. La forma <em>leiendo</em> no existe.',
                ),
                (
                    'Ahora mismo mi jefe _____ (hablar) por teléfono.',
                    ['está hablando', 'es hablando', 'estaba hablando'],
                    'está hablando',
                    'Para una acción en progreso en el momento actual se usa <em>estar (presente) + gerundio</em>: <em>está hablando</em>.',
                ),
                (
                    '¿Cómo se forma el gerundio de <em>pedir</em>?',
                    ['pidiendo', 'pediendo', 'pidendo'],
                    'pidiendo',
                    '<em>Pedir</em> es un verbo -IR con cambio vocálico e→i. En el gerundio el cambio se mantiene: <em>pidiendo</em>.',
                ),
                (
                    'Los estudiantes _____ (seguir) preparando el proyecto — lo entregarán la semana que viene.',
                    ['siguen preparando', 'siguen a preparar', 'están siguiendo preparar'],
                    'siguen preparando',
                    '<em>Seguir + gerundio</em> expresa continuidad. La estructura es <em>seguir + gerundio</em> directamente, sin preposición.',
                ),
                (
                    'El gerundio de <em>dormir</em> es:',
                    ['durmiendo', 'dormiendo', 'durmendo'],
                    'durmiendo',
                    '<em>Dormir</em> es un verbo -IR con cambio vocálico o→u. Este cambio aparece también en el gerundio: <em>durmiendo</em>.',
                ),
                (
                    '_____ (llevar) dos años _____ (estudiar) español y ya hablo bastante bien.',
                    ['Llevo... estudiando', 'Llevo... a estudiar', 'Sigo... estudiando dos años'],
                    'Llevo... estudiando',
                    '<em>Llevar + tiempo + gerundio</em> expresa la duración de una acción hasta el presente: <em>Llevo dos años estudiando</em>.',
                ),
            ],
        ),
        ex2=(
            'Ejercicio 2 — Escribe el gerundio o la forma verbal correcta',
            'Completa las oraciones con la forma correcta del gerundio o la perífrasis verbal.',
            [
                (
                    'El niño _____ (dormir) plácidamente cuando llegamos a casa.',
                    'estaba durmiendo',
                    '<em>Dormir</em> tiene gerundio irregular o→u: <em>durmiendo</em>. La perífrasis en pasado es <em>estaba durmiendo</em>.',
                ),
                (
                    'Mis padres _____ (llevar) diez años _____ (vivir) en esta ciudad.',
                    'llevan... viviendo',
                    '<em>Llevar + tiempo + gerundio</em>: <em>llevan diez años viviendo</em>. El gerundio de <em>vivir</em> es regular: <em>viviendo</em>.',
                ),
                (
                    'Todavía _____ (seguir, yo) _____ (buscar) trabajo — el mercado está muy difícil.',
                    'sigo... buscando',
                    '<em>Seguir + gerundio</em>: <em>sigo buscando</em>. El gerundio de <em>buscar</em> es regular: <em>buscando</em>.',
                ),
                (
                    '¿Qué _____ (hacer, vosotros) este fin de semana? — _____ (visitar) a los abuelos.',
                    'estáis haciendo... Estamos visitando',
                    'Presente de <em>estar</em> con vosotros: <em>estáis</em>. Los gerundios son regulares: <em>haciendo, visitando</em>.',
                ),
                (
                    'María entró en la habitación _____ (cantar) una canción muy bonita.',
                    'cantando',
                    'Gerundio para expresar una acción simultánea: María realizó las dos acciones a la vez. El gerundio de <em>cantar</em> es <em>cantando</em>.',
                ),
            ],
        ),
        ex3=(
            'Ejercicio 3 — Corrección de errores con el gerundio',
            'Identifica el error en cada oración y elige la versión correcta.',
            [
                (
                    '"Llevo esperando media hora aquí."',
                    [
                        'Llevo media hora esperando aquí.',
                        'Llevo esperando a media hora aquí.',
                        'Estoy esperando media hora aquí.',
                    ],
                    'Llevo media hora esperando aquí.',
                    'La estructura de <em>llevar + gerundio</em> requiere la expresión de tiempo entre <em>llevar</em> y el gerundio: <em>llevo media hora esperando</em>.',
                ),
                (
                    '"Estoy sabiendo la respuesta ahora mismo."',
                    [
                        'Sé la respuesta.',
                        'Estoy conociéndola ahora mismo.',
                        'Estoy sabiéndola.',
                    ],
                    'Sé la respuesta.',
                    '<em>Saber</em> es un verbo de estado que no admite el progresivo. Se usa el presente simple: <em>sé la respuesta</em>.',
                ),
                (
                    '"Siguen a trabajar hasta las nueve todas las noches."',
                    [
                        'Siguen trabajando hasta las nueve todas las noches.',
                        'Siguen trabajar hasta las nueve todas las noches.',
                        'Están siguiendo trabajar hasta las nueve.',
                    ],
                    'Siguen trabajando hasta las noches todas las noches.',
                    '<em>Seguir</em> se construye directamente con gerundio, sin preposición: <em>siguen trabajando</em>.',
                ),
                (
                    '"El gerundio de decir es dicendo."',
                    [
                        'El gerundio de decir es diciendo.',
                        'El gerundio de decir es deciendo.',
                        'El gerundio de decir es dicho.',
                    ],
                    'El gerundio de decir es diciendo.',
                    '<em>Decir</em> tiene cambio vocálico e→i en el gerundio: <em>diciendo</em>. La forma <em>dicendo</em> no existe en español.',
                ),
                (
                    '"Leyiéndo el periódico, me enteré de la noticia."',
                    [
                        'Leyendo el periódico, me enteré de la noticia.',
                        'Leiendo el periódico, me enteré de la noticia.',
                        'Leendo el periódico, me enteré de la noticia.',
                    ],
                    'Leyendo el periódico, me enteré de la noticia.',
                    'El gerundio de <em>leer</em> es <em>leyendo</em>: la raíz <em>le-</em> + <em>-yendo</em>. No se escribe <em>leyiendo</em> porque solo se añade una <em>y</em>.',
                ),
            ],
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('ger-form-01', '-ando / -iendo', 'Terminaciones del gerundio regular: -ando para -AR y -iendo para -ER e -IR', 'terminaciones del gerundio', 'hablar → hablando / comer → comiendo / vivir → viviendo', 'El gerundio de "trabajar" es trabaj_____.', 'ando'),
            ('ger-irr-02', 'diciendo / pidiendo / siguiendo', 'Gerundios irregulares de verbos -IR con cambio e→i en la raíz', 'gerundio con e→i', 'decir → diciendo / pedir → pidiendo / seguir → siguiendo', 'El gerundio de "pedir" es p_____.', 'idiendo'),
            ('ger-irr-03', 'durmiendo / muriendo', 'Gerundios irregulares de verbos -IR con cambio o→u en la raíz', 'gerundio con o→u', 'dormir → durmiendo / morir → muriendo', 'El gerundio de "dormir" es d_____.', 'urmiendo'),
            ('ger-est-04', 'estar + gerundio', 'Perífrasis para expresar que una acción está ocurriendo en el momento presente', 'acción en progreso', 'Estoy comiendo. / Está leyendo. / Estamos trabajando.', 'Ahora mismo _____ (ella, hablar) por teléfono con su jefe.', 'está hablando'),
            ('ger-seg-05', 'seguir + gerundio', 'Perífrasis que expresa que una acción continúa sin interrupción', 'acción continuada', 'Sigo buscando trabajo. / Siguen estudiando juntos.', '¿Todavía _____ (tú, vivir) en Madrid?', 'sigues viviendo'),
            ('ger-lle-06', 'llevar + tiempo + gerundio', 'Perífrasis que expresa la duración de una acción desde su inicio hasta el presente', 'duración hasta ahora', 'Llevo dos horas esperando. / Llevan un año estudiando juntos.', '_____ (nosotros) tres horas _____ (esperar) el tren.', 'Llevamos... esperando'),
            ('ger-ley-07', 'leyendo / cayendo / oyendo', 'Gerundios con -yendo cuando la raíz del verbo termina en vocal', 'raíz vocal + -yendo', 'leer → leyendo / caer → cayendo / oír → oyendo', 'El gerundio de "leer" es _____.', 'leyendo'),
            ('ger-pro-08', 'gerundio + pronombre enclítico', 'Al unir un pronombre al gerundio se añade tilde si es necesario mantener el acento', 'tilde en gerundio con pronombre', 'Estoy leyéndolo. / Está haciéndolo. / Sigo escribiéndote.', 'Estoy escrib_____ una carta a mis amigos. (escribir + CD la)', 'iéndola'),
        ],
    ),
}
