# -*- coding: utf-8 -*-
"""espanol/ A2 Gramática — lote 1 (G01–G05)."""

CHAPTERS = {
    'preterito-indefinido': dict(
        level='a2',
        section='grammar',
        num='G01',
        short='Pretérito Indefinido',
        title='El Pretérito Indefinido — El pasado simple',
        subtitle='Habla de acciones completadas en el pasado',
        slides=[
            ('¿Qué es el pretérito indefinido?', None,
             '<p class="slide-explanation">El <b>pretérito indefinido</b> expresa acciones <b>completadas</b> en el pasado. '
             'La acción tiene un inicio y un fin claros, o se produjo en un momento concreto.</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Ayer comí una paella.</b> (acción terminada)</p>'
             '<p><b>El año pasado viajé a México.</b> (momento concreto)</p>'
             '<p><b>Llamé tres veces.</b> (número de veces)</p>'
             '</div>'
             '<p class="slide-explanation">Palabras clave: <b>ayer</b>, <b>anoche</b>, <b>el lunes pasado</b>, '
             '<b>en 2020</b>, <b>hace dos días</b>, <b>una vez</b>.</p>'),

            ('Verbos regulares en -AR', None,
             '<p class="slide-explanation">Los verbos terminados en <b>-AR</b> toman estas terminaciones:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronombre</th><th style="padding:8px;text-align:left">HABLAR</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">yo</td><td style="padding:8px"><b>hablé</b></td><td style="padding:8px">Yo hablé con Juan.</td></tr>'
             '<tr><td style="padding:8px">tú</td><td style="padding:8px"><b>hablaste</b></td><td style="padding:8px">¿Hablaste con ella?</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">él/ella</td><td style="padding:8px"><b>habló</b></td><td style="padding:8px">Ella habló mucho.</td></tr>'
             '<tr><td style="padding:8px">nosotros</td><td style="padding:8px"><b>hablamos</b></td><td style="padding:8px">Hablamos dos horas.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">vosotros</td><td style="padding:8px"><b>hablasteis</b></td><td style="padding:8px">Hablasteis muy alto.</td></tr>'
             '<tr><td style="padding:8px">ellos/ellas</td><td style="padding:8px"><b>hablaron</b></td><td style="padding:8px">Ellos hablaron claro.</td></tr>'
             '</table>'
             '<p class="slide-explanation">Nota: la <b>yo</b> termina en <b>-é</b> (con tilde) y la forma <b>nosotros</b> es igual al presente.</p>'),

            ('Verbos regulares en -ER e -IR', None,
             '<p class="slide-explanation">Los verbos en <b>-ER</b> e <b>-IR</b> comparten las mismas terminaciones en indefinido:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronombre</th><th style="padding:8px;text-align:left">COMER</th><th style="padding:8px;text-align:left">VIVIR</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">yo</td><td style="padding:8px"><b>comí</b></td><td style="padding:8px"><b>viví</b></td></tr>'
             '<tr><td style="padding:8px">tú</td><td style="padding:8px"><b>comiste</b></td><td style="padding:8px"><b>viviste</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">él/ella</td><td style="padding:8px"><b>comió</b></td><td style="padding:8px"><b>vivió</b></td></tr>'
             '<tr><td style="padding:8px">nosotros</td><td style="padding:8px"><b>comimos</b></td><td style="padding:8px"><b>vivimos</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">vosotros</td><td style="padding:8px"><b>comisteis</b></td><td style="padding:8px"><b>vivisteis</b></td></tr>'
             '<tr><td style="padding:8px">ellos/ellas</td><td style="padding:8px"><b>comieron</b></td><td style="padding:8px"><b>vivieron</b></td></tr>'
             '</table>'),

            ('Verbos irregulares esenciales (I)', None,
             '<p class="slide-explanation"><b>SER</b> e <b>IR</b> tienen formas idénticas en indefinido — el contexto aclara el significado:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronombre</th><th style="padding:8px;text-align:left">SER / IR</th><th style="padding:8px;text-align:left">TENER</th><th style="padding:8px;text-align:left">ESTAR</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">yo</td><td style="padding:8px"><b>fui</b></td><td style="padding:8px"><b>tuve</b></td><td style="padding:8px"><b>estuve</b></td></tr>'
             '<tr><td style="padding:8px">tú</td><td style="padding:8px"><b>fuiste</b></td><td style="padding:8px"><b>tuviste</b></td><td style="padding:8px"><b>estuviste</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">él/ella</td><td style="padding:8px"><b>fue</b></td><td style="padding:8px"><b>tuvo</b></td><td style="padding:8px"><b>estuvo</b></td></tr>'
             '<tr><td style="padding:8px">nosotros</td><td style="padding:8px"><b>fuimos</b></td><td style="padding:8px"><b>tuvimos</b></td><td style="padding:8px"><b>estuvimos</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">ellos/ellas</td><td style="padding:8px"><b>fueron</b></td><td style="padding:8px"><b>tuvieron</b></td><td style="padding:8px"><b>estuvieron</b></td></tr>'
             '</table>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Fui</b> al mercado. (IR) &nbsp;|&nbsp; <b>Fue</b> un día especial. (SER)</p>'
             '</div>'),

            ('Verbos irregulares esenciales (II)', None,
             '<p class="slide-explanation">Otros irregulares frecuentes: <b>HACER</b> y <b>PODER</b>. '
             'Observa que la raíz cambia pero las terminaciones son las mismas para todos los verbos irregulares en -e-:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronombre</th><th style="padding:8px;text-align:left">HACER</th><th style="padding:8px;text-align:left">PODER</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">yo</td><td style="padding:8px"><b>hice</b></td><td style="padding:8px"><b>pude</b></td></tr>'
             '<tr><td style="padding:8px">tú</td><td style="padding:8px"><b>hiciste</b></td><td style="padding:8px"><b>pudiste</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">él/ella</td><td style="padding:8px"><b>hizo</b></td><td style="padding:8px"><b>pudo</b></td></tr>'
             '<tr><td style="padding:8px">nosotros</td><td style="padding:8px"><b>hicimos</b></td><td style="padding:8px"><b>pudimos</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">ellos/ellas</td><td style="padding:8px"><b>hicieron</b></td><td style="padding:8px"><b>pudieron</b></td></tr>'
             '</table>'
             '<p class="slide-explanation">Nota especial: <b>él hizo</b> (con z) para preservar el sonido /θ/ ante -o.</p>'),
        ],
        traps=[
            ('yo hablé', '<strong>yo hablé</strong> (con tilde)', 'La primera persona singular de -AR lleva tilde: <b>hablé</b>, <b>llegué</b>, <b>empecé</b>. Sin tilde cambia el significado o es incorrecto.'),
            ('yo hable', '<strong>yo hablé</strong>', 'Sin tilde, «hable» es subjuntivo presente, no indefinido. La tilde es obligatoria en la forma yo.'),
            ('él hicó / él hacé', '<strong>él hizo</strong>', 'HACER es completamente irregular. La raíz cambia a <b>hic-</b> y en tercera persona singular se escribe <b>hizo</b> (con z).'),
            ('nosotros hablaron', '<strong>nosotros hablamos</strong>', 'La forma <b>nosotros</b> de los verbos -AR es <b>-amos</b>, igual en presente e indefinido. <b>-aron</b> es solo para ellos/ellas.'),
            ('yo fue', '<strong>yo fui</strong>', 'La primera persona de SER/IR es <b>fui</b>, no <b>fue</b>. <b>Fue</b> corresponde a él/ella/usted.'),
        ],
        summary=[
            ('Verbos -AR (yo)', '-é', 'Yo hablé con mi madre.'),
            ('Verbos -ER/-IR (yo)', '-í', 'Yo comí tarde. / Yo viví allí.'),
            ('SER / IR', 'fui, fuiste, fue, fuimos, fueron', 'Fui al cine. / Fue un buen día.'),
            ('TENER', 'tuve, tuviste, tuvo, tuvimos, tuvieron', 'Tuve un accidente ayer.'),
            ('ESTAR', 'estuve, estuviste, estuvo, estuvimos, estuvieron', 'Estuve en Lima tres días.'),
            ('HACER', 'hice, hiciste, hizo, hicimos, hicieron', 'Ella hizo la tarea sola.'),
        ],
        ex1=('Elige la forma correcta', 'Selecciona la forma de pretérito indefinido que corresponde.',
             [('Ayer yo ______ (hablar) con mi jefa.', ['hablo', 'hablé', 'hablaba'], 'hablé', 'La forma yo del indefinido en -AR es <b>hablé</b> (con tilde).'),
              ('El sábado, ellos ______ (comer) en un restaurante nuevo.', ['comieron', 'comían', 'comen'], 'comieron', 'Ellos/ellas del indefinido en -ER es <b>comieron</b>.'),
              ('¿Dónde ______ (estar, tú) anoche?', ['estabas', 'estuviste', 'estás'], 'estuviste', 'ESTAR es irregular: tú → <b>estuviste</b>.'),
              ('Nosotros ______ (ir) al museo el domingo.', ['íbamos', 'fuimos', 'vamos'], 'fuimos', 'IR/SER → nosotros: <b>fuimos</b>.'),
              ('María ______ (hacer) un pastel para la fiesta.', ['hació', 'hacía', 'hizo'], 'hizo', 'HACER → él/ella: <b>hizo</b> (con z, no c).'),
              ('Yo no ______ (poder) dormir bien esa noche.', ['podía', 'pude', 'puedo'], 'pude', 'PODER → yo: <b>pude</b>.'),
             ]),
        ex2=('Escribe la forma correcta', 'Escribe el verbo entre paréntesis en pretérito indefinido.',
             [('Ayer (tener, yo) ______ mucho trabajo.', 'tuve', 'TENER → yo: <b>tuve</b>.'),
              ('El año pasado (vivir, ellos) ______ en Barcelona.', 'vivieron', 'VIVIR → ellos: <b>vivieron</b>.'),
              ('¿(Ser, vosotros) ______ estudiantes en esa universidad?', 'fuisteis', 'SER → vosotros: <b>fuisteis</b>.'),
              ('Anoche (hacer, nosotros) ______ los deberes juntos.', 'hicimos', 'HACER → nosotros: <b>hicimos</b>.'),
              ('Ella (llamar) ______ tres veces pero no contesté.', 'llamó', 'LLAMAR → ella: <b>llamó</b> (con tilde).'),
             ]),
        ex3=('¿Indefinido o no?', 'Elige la oración que usa correctamente el pretérito indefinido.',
             [('¿Cuál usa el indefinido correctamente?', ['Ayer comía pizza.', 'Ayer comí pizza.', 'Ayer como pizza.'], 'Ayer comí pizza.', '<b>Comí</b> es indefinido. <b>Comía</b> es imperfecto y <b>como</b> es presente.'),
              ('¿Cuál está en indefinido?', ['Siempre tuve hambre de niño.', 'Tuve hambre ayer a las tres.', 'Tengo hambre ahora.'], 'Tuve hambre ayer a las tres.', 'El indefinido marca un momento concreto pasado. «Siempre… de niño» pide imperfecto.'),
              ('¿Qué forma es incorrecta?', ['él habló', 'yo hable', 'tú hablaste'], 'yo hable', '<b>yo hable</b> no lleva tilde y es subjuntivo, no indefinido. Lo correcto es <b>yo hablé</b>.'),
              ('¿Cuál expresa una acción completa en el pasado?', ['Estudiaba cada día.', 'Estudié toda la noche.', 'Estudio mucho.'], 'Estudié toda la noche.', '<b>Estudié</b> indica una acción terminada. <b>Estudiaba</b> es hábito pasado (imperfecto).'),
              ('¿Cuál está bien formado?', ['yo fuí', 'yo fui', 'yo fue'], 'yo fui', '<b>fui</b> no lleva tilde (monosílabo). <b>fue</b> es tercera persona.'),
             ]),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('indef-01', 'hablé', 'primera persona yo de HABLAR en indefinido', 'pasado de hablar', 'Ayer yo hablé con mi profesora.', 'Ayer yo ______ con mi profesora.', 'hablé'),
            ('indef-02', 'comieron', 'tercera persona plural de COMER en indefinido', 'pasado de comer (ellos)', 'Ellos comieron paella el sábado.', 'Ellos ______ paella el sábado.', 'comieron'),
            ('indef-03', 'fui', 'primera persona yo de IR/SER en indefinido', 'yo → ir/ser pasado', 'Yo fui al mercado por la mañana.', 'Yo ______ al mercado por la mañana.', 'fui'),
            ('indef-04', 'tuve', 'primera persona yo de TENER en indefinido', 'yo → tener pasado', 'Tuve un examen muy difícil.', 'Yo ______ un examen muy difícil.', 'tuve'),
            ('indef-05', 'hizo', 'tercera persona él/ella de HACER en indefinido', 'él/ella → hacer pasado', 'María hizo un pastel delicioso.', 'María ______ un pastel delicioso.', 'hizo'),
            ('indef-06', 'pude', 'primera persona yo de PODER en indefinido', 'yo → poder pasado', 'No pude abrir la puerta.', 'No ______ abrir la puerta.', 'pude'),
            ('indef-07', 'estuvo', 'tercera persona él/ella de ESTAR en indefinido', 'él/ella → estar pasado', 'Él estuvo en el hospital dos días.', 'Él ______ en el hospital dos días.', 'estuvo'),
            ('indef-08', 'vivisteis', 'segunda persona plural vosotros de VIVIR en indefinido', 'vosotros → vivir pasado', '¿Vivisteis en Madrid muchos años?', '¿______ en Madrid muchos años?', 'vivisteis'),
        ],
    ),

    'preterito-imperfecto': dict(
        level='a2',
        section='grammar',
        num='G02',
        short='Pretérito Imperfecto',
        title='El Pretérito Imperfecto — Hábitos y descripciones del pasado',
        subtitle='Describe cómo eran las cosas o qué hacías habitualmente',
        slides=[
            ('¿Para qué sirve el imperfecto?', None,
             '<p class="slide-explanation">El <b>pretérito imperfecto</b> se usa para tres funciones principales en el pasado:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>1. Hábitos y acciones repetidas:</b> De pequeño, <b>comía</b> mucho chocolate.</p>'
             '<p><b>2. Descripciones en el pasado:</b> La casa <b>era</b> muy grande y <b>tenía</b> un jardín.</p>'
             '<p><b>3. Acciones en curso que se interrumpen:</b> <b>Dormía</b> cuando sonó el teléfono.</p>'
             '</div>'
             '<p class="slide-explanation">Palabras clave: <b>siempre</b>, <b>normalmente</b>, <b>antes</b>, '
             '<b>de pequeño/a</b>, <b>todos los días</b>, <b>generalmente</b>.</p>'),

            ('Conjugación: verbos en -AR', None,
             '<p class="slide-explanation">Los verbos en <b>-AR</b> toman la raíz + <b>-aba, -abas, -aba, -ábamos, -abais, -aban</b>:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronombre</th><th style="padding:8px;text-align:left">HABLAR</th><th style="padding:8px;text-align:left">TRABAJAR</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">yo</td><td style="padding:8px"><b>hablaba</b></td><td style="padding:8px"><b>trabajaba</b></td></tr>'
             '<tr><td style="padding:8px">tú</td><td style="padding:8px"><b>hablabas</b></td><td style="padding:8px"><b>trabajabas</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">él/ella</td><td style="padding:8px"><b>hablaba</b></td><td style="padding:8px"><b>trabajaba</b></td></tr>'
             '<tr><td style="padding:8px">nosotros</td><td style="padding:8px"><b>hablábamos</b></td><td style="padding:8px"><b>trabajábamos</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">vosotros</td><td style="padding:8px"><b>hablabais</b></td><td style="padding:8px"><b>trabajabais</b></td></tr>'
             '<tr><td style="padding:8px">ellos/ellas</td><td style="padding:8px"><b>hablaban</b></td><td style="padding:8px"><b>trabajaban</b></td></tr>'
             '</table>'
             '<p class="slide-explanation">Solo <b>nosotros</b> lleva tilde: <b>-ábamos</b>.</p>'),

            ('Conjugación: verbos en -ER e -IR', None,
             '<p class="slide-explanation">Los verbos en <b>-ER</b> e <b>-IR</b> toman <b>-ía, -ías, -ía, -íamos, -íais, -ían</b>:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronombre</th><th style="padding:8px;text-align:left">COMER</th><th style="padding:8px;text-align:left">VIVIR</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">yo</td><td style="padding:8px"><b>comía</b></td><td style="padding:8px"><b>vivía</b></td></tr>'
             '<tr><td style="padding:8px">tú</td><td style="padding:8px"><b>comías</b></td><td style="padding:8px"><b>vivías</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">él/ella</td><td style="padding:8px"><b>comía</b></td><td style="padding:8px"><b>vivía</b></td></tr>'
             '<tr><td style="padding:8px">nosotros</td><td style="padding:8px"><b>comíamos</b></td><td style="padding:8px"><b>vivíamos</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">vosotros</td><td style="padding:8px"><b>comíais</b></td><td style="padding:8px"><b>vivíais</b></td></tr>'
             '<tr><td style="padding:8px">ellos/ellas</td><td style="padding:8px"><b>comían</b></td><td style="padding:8px"><b>vivían</b></td></tr>'
             '</table>'
             '<p class="slide-explanation">Todas las formas llevan tilde en la <b>í</b>: comía, comías…</p>'),

            ('Los tres irregulares del imperfecto', None,
             '<p class="slide-explanation">El imperfecto tiene solo <b>tres verbos irregulares</b>: <b>SER</b>, <b>IR</b> y <b>VER</b>. '
             'Todos los demás verbos son completamente regulares.</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronombre</th><th style="padding:8px;text-align:left">SER</th><th style="padding:8px;text-align:left">IR</th><th style="padding:8px;text-align:left">VER</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">yo</td><td style="padding:8px"><b>era</b></td><td style="padding:8px"><b>iba</b></td><td style="padding:8px"><b>veía</b></td></tr>'
             '<tr><td style="padding:8px">tú</td><td style="padding:8px"><b>eras</b></td><td style="padding:8px"><b>ibas</b></td><td style="padding:8px"><b>veías</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">él/ella</td><td style="padding:8px"><b>era</b></td><td style="padding:8px"><b>iba</b></td><td style="padding:8px"><b>veía</b></td></tr>'
             '<tr><td style="padding:8px">nosotros</td><td style="padding:8px"><b>éramos</b></td><td style="padding:8px"><b>íbamos</b></td><td style="padding:8px"><b>veíamos</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">ellos/ellas</td><td style="padding:8px"><b>eran</b></td><td style="padding:8px"><b>iban</b></td><td style="padding:8px"><b>veían</b></td></tr>'
             '</table>'),

            ('Imperfecto vs. Indefinido', None,
             '<p class="slide-explanation">La diferencia clave: el <b>indefinido</b> cuenta un evento terminado; '
             'el <b>imperfecto</b> describe el contexto o el hábito.</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Cuando era</b> pequeño, <b>comía</b> muchos dulces. (imperfecto: hábito/descripción)</p>'
             '<p>Ayer <b>comí</b> un helado enorme. (indefinido: acción concreta terminada)</p>'
             '<p><b>Leía</b> el periódico cuando <b>llegó</b> Ana. (imperfecto = contexto; indefinido = evento)</p>'
             '</div>'
             '<p class="slide-explanation">Truco: si puedes añadir «todas las semanas / siempre» → imperfecto. '
             'Si puedes añadir «una vez / ayer» → indefinido.</p>'),
        ],
        traps=[
            ('yo comia (sin tilde)', '<strong>yo comía</strong>', 'La <b>í</b> de los verbos -ER/-IR en imperfecto siempre lleva tilde. Sin ella, la pronunciación y la escritura son incorrectas.'),
            ('nosotros hablabiamos', '<strong>nosotros hablábamos</strong>', 'La forma correcta es <b>hablábamos</b>. No existe «-abiamos». La tilde va sobre la <b>á</b>.'),
            ('yo era / yo iba → con tilde', '<strong>era, iba</strong> (sin tilde)', 'SER → <b>era</b> e IR → <b>iba</b> no llevan tilde. Son formas regulares del imperfecto, no se confunden con presente.'),
            ('Usé imperfecto para acción concreta', 'Usa <strong>indefinido</strong>', 'Para una acción terminada en un momento concreto usa el indefinido. Ejemplo: «Ayer <b>comí</b> pizza» (no «comía»).'),
            ('Confundir SER e IR en imperfecto', 'Son <strong>diferentes</strong>: era / iba', 'En imperfecto SER e IR NO son iguales: SER → <b>era</b>, IR → <b>iba</b>. Solo en indefinido comparten formas (fui/fue…).'),
        ],
        summary=[
            ('Verbos -AR (hábito)', '-aba, -abas, -aba, -ábamos, -abais, -aban', 'Siempre hablaba con su abuela.'),
            ('Verbos -ER/-IR (descripción)', '-ía, -ías, -ía, -íamos, -íais, -ían', 'El edificio tenía cinco pisos.'),
            ('SER (irregular)', 'era, eras, era, éramos, erais, eran', 'De niño era muy tímido.'),
            ('IR (irregular)', 'iba, ibas, iba, íbamos, ibais, iban', 'Iba al parque todos los domingos.'),
            ('VER (irregular)', 'veía, veías, veía, veíamos, veíais, veían', 'Veíamos la tele después de cenar.'),
            ('Contexto interrumpido', 'Imperfecto + cuando + indefinido', 'Dormía cuando sonó el despertador.'),
        ],
        ex1=('Elige la forma correcta de imperfecto', 'Selecciona la opción correcta para completar la oración.',
             [('Cuando era niño, (vivir, yo) ______ en el campo.', ['vivía', 'viví', 'vivo'], 'vivía', 'Imperfecto de VIVIR, yo: <b>vivía</b>. Describe una situación habitual del pasado.'),
              ('Mis abuelos siempre (cocinar) ______ juntos los domingos.', ['cocinaron', 'cocinaban', 'cocinan'], 'cocinaban', 'Hábito repetido → imperfecto: <b>cocinaban</b>.'),
              ('De pequeña, ella (ser) ______ muy alegre.', ['fue', 'es', 'era'], 'era', 'SER en imperfecto → él/ella: <b>era</b>.'),
              ('Nosotros (ir) ______ a la playa cada verano.', ['fuimos', 'íbamos', 'vamos'], 'íbamos', 'Hábito pasado con IR → nosotros: <b>íbamos</b>.'),
              ('¿Qué (ver, tú) ______ cuando apagué la luz?', ['viste', 'veías', 'ves'], 'veías', 'Acción en curso interrumpida → imperfecto: <b>veías</b>.'),
              ('Antes, los trenes (ser) ______ muy lentos.', ['fueron', 'son', 'eran'], 'eran', 'Descripción general del pasado → imperfecto: <b>eran</b>.'),
             ]),
        ex2=('Escribe el verbo en imperfecto', 'Conjuga el verbo entre paréntesis en pretérito imperfecto.',
             [('Todos los veranos (viajar, nosotros) ______ a la sierra.', 'viajábamos', 'VIAJAR → nosotros imperfecto: <b>viajábamos</b>.'),
              ('De niño él (tener) ______ miedo a la oscuridad.', 'tenía', 'TENER → él imperfecto: <b>tenía</b>.'),
              ('¿Adónde (ir, vosotros) ______ de vacaciones antes?', 'ibais', 'IR → vosotros imperfecto: <b>ibais</b>.'),
              ('Ellas (estudiar) ______ en la biblioteca cada tarde.', 'estudiaban', 'ESTUDIAR → ellas imperfecto: <b>estudiaban</b>.'),
              ('Yo (ver) ______ mucha televisión cuando era joven.', 'veía', 'VER → yo imperfecto: <b>veía</b>.'),
             ]),
        ex3=('Imperfecto o indefinido', 'Elige el tiempo verbal correcto según el contexto.',
             [('Antes, (ir, yo) siempre ______ al cine los viernes.', ['fui', 'iba', 'voy'], 'iba', '«Siempre» indica hábito → imperfecto: <b>iba</b>.'),
              ('El martes pasado (ir, yo) ______ al cine con Ana.', ['iba', 'fui', 'voy'], 'fui', 'Momento concreto («el martes pasado») → indefinido: <b>fui</b>.'),
              ('¿Qué (hacer, tú) ______ cuando te llamé?', ['hiciste', 'hacías', 'haces'], 'hacías', 'Acción en progreso interrumpida → imperfecto: <b>hacías</b>.'),
              ('Ayer (hacer, yo) ______ la compra a las diez.', ['hacía', 'hice', 'hago'], 'hice', 'Acción completa en momento concreto → indefinido: <b>hice</b>.'),
              ('El apartamento (tener) ______ dos habitaciones y una terraza.', ['tuvo', 'tiene', 'tenía'], 'tenía', 'Descripción de una situación pasada → imperfecto: <b>tenía</b>.'),
             ]),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('imp-01', 'hablaba', 'imperfecto yo/él de HABLAR', 'pasado habitual de hablar', 'De pequeño hablaba mucho en clase.', 'De pequeño ______ mucho en clase.', 'hablaba'),
            ('imp-02', 'era', 'imperfecto yo/él de SER', 'pasado descriptivo de ser', 'La ciudad era muy tranquila antes.', 'La ciudad ______ muy tranquila antes.', 'era'),
            ('imp-03', 'tenía', 'imperfecto yo/él de TENER', 'pasado habitual de tener', 'Ella tenía muchos amigos en el colegio.', 'Ella ______ muchos amigos en el colegio.', 'tenía'),
            ('imp-04', 'vivía', 'imperfecto yo/él de VIVIR', 'pasado descriptivo de vivir', 'Antes vivía en un pueblo pequeño.', 'Antes ______ en un pueblo pequeño.', 'vivía'),
            ('imp-05', 'íbamos', 'imperfecto nosotros de IR', 'hábito pasado de ir (nosotros)', 'Íbamos al mercado cada sábado.', '______ al mercado cada sábado.', 'íbamos'),
            ('imp-06', 'veía', 'imperfecto yo/él de VER', 'pasado habitual de ver', 'Veía las noticias todas las noches.', '______ las noticias todas las noches.', 'veía'),
            ('imp-07', 'comían', 'imperfecto ellos de COMER', 'hábito pasado de comer (ellos)', 'Ellos comían juntos cada domingo.', 'Ellos ______ juntos cada domingo.', 'comían'),
            ('imp-08', 'éramos', 'imperfecto nosotros de SER', 'pasado descriptivo de ser (nosotros)', 'Éramos muy buenos amigos.', '______ muy buenos amigos.', 'éramos'),
        ],
    ),

    'futuro-simple': dict(
        level='a2',
        section='grammar',
        num='G03',
        short='Futuro Simple',
        title='El Futuro Simple — Hablar del futuro',
        subtitle='Expresa predicciones, promesas y planes futuros',
        slides=[
            ('¿Para qué usamos el futuro simple?', None,
             '<p class="slide-explanation">El <b>futuro simple</b> se forma con el infinitivo + terminaciones. '
             'Se usa para:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Predicciones:</b> Mañana <b>lloverá</b> en el norte.</p>'
             '<p><b>Promesas:</b> Te <b>llamaré</b> cuando llegue.</p>'
             '<p><b>Suposiciones sobre el presente:</b> ¿Dónde estará Juan? (<i>me pregunto dónde está</i>)</p>'
             '<p><b>Planes futuros:</b> El año que viene <b>estudiaré</b> en el extranjero.</p>'
             '</div>'
             '<p class="slide-explanation">Palabras clave: <b>mañana</b>, <b>el año que viene</b>, <b>dentro de</b>, '
             '<b>pronto</b>, <b>algún día</b>.</p>'),

            ('Verbos regulares: las terminaciones', None,
             '<p class="slide-explanation">En el futuro simple, los tres grupos de verbos comparten las <b>mismas terminaciones</b>, '
             'que se añaden directamente al <b>infinitivo completo</b>:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronombre</th><th style="padding:8px;text-align:left">HABLAR</th><th style="padding:8px;text-align:left">COMER</th><th style="padding:8px;text-align:left">VIVIR</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">yo</td><td style="padding:8px"><b>hablaré</b></td><td style="padding:8px"><b>comeré</b></td><td style="padding:8px"><b>viviré</b></td></tr>'
             '<tr><td style="padding:8px">tú</td><td style="padding:8px"><b>hablarás</b></td><td style="padding:8px"><b>comerás</b></td><td style="padding:8px"><b>vivirás</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">él/ella</td><td style="padding:8px"><b>hablará</b></td><td style="padding:8px"><b>comerá</b></td><td style="padding:8px"><b>vivirá</b></td></tr>'
             '<tr><td style="padding:8px">nosotros</td><td style="padding:8px"><b>hablaremos</b></td><td style="padding:8px"><b>comeremos</b></td><td style="padding:8px"><b>viviremos</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">vosotros</td><td style="padding:8px"><b>hablaréis</b></td><td style="padding:8px"><b>comeréis</b></td><td style="padding:8px"><b>viviréis</b></td></tr>'
             '<tr><td style="padding:8px">ellos/ellas</td><td style="padding:8px"><b>hablarán</b></td><td style="padding:8px"><b>comerán</b></td><td style="padding:8px"><b>vivirán</b></td></tr>'
             '</table>'
             '<p class="slide-explanation">Todas las formas llevan tilde, excepto <b>nosotros</b> (<b>-remos</b>).</p>'),

            ('Verbos irregulares: la raíz cambia', None,
             '<p class="slide-explanation">En los verbos irregulares, la <b>raíz</b> cambia pero las <b>terminaciones son iguales</b>. '
             'Los más importantes a nivel A2:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Infinitivo</th><th style="padding:8px;text-align:left">Raíz irregular</th><th style="padding:8px;text-align:left">Yo</th><th style="padding:8px;text-align:left">Él/ella</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">tener</td><td style="padding:8px"><b>tendr-</b></td><td style="padding:8px">tendré</td><td style="padding:8px">tendrá</td></tr>'
             '<tr><td style="padding:8px">poder</td><td style="padding:8px"><b>podr-</b></td><td style="padding:8px">podré</td><td style="padding:8px">podrá</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">hacer</td><td style="padding:8px"><b>har-</b></td><td style="padding:8px">haré</td><td style="padding:8px">hará</td></tr>'
             '<tr><td style="padding:8px">ir</td><td style="padding:8px"><b>ir-</b></td><td style="padding:8px">iré</td><td style="padding:8px">irá</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">salir</td><td style="padding:8px"><b>saldr-</b></td><td style="padding:8px">saldré</td><td style="padding:8px">saldrá</td></tr>'
             '<tr><td style="padding:8px">venir</td><td style="padding:8px"><b>vendr-</b></td><td style="padding:8px">vendré</td><td style="padding:8px">vendrá</td></tr>'
             '</table>'),

            ('Futuro vs. "ir a + infinitivo"', None,
             '<p class="slide-explanation">En español hay dos formas principales de hablar del futuro:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Ir a + infinitivo</b> → plan concreto, ya decidido: <b>Voy a estudiar</b> esta tarde.</p>'
             '<p><b>Futuro simple</b> → predicción, promesa, o plan más abierto: <b>Estudiaré</b> medicina algún día.</p>'
             '</div>'
             '<p class="slide-explanation">Ambas formas son correctas. El futuro simple suena más formal '
             'o indica menos certeza sobre los detalles concretos.</p>'),
        ],
        traps=[
            ('yo hablare (sin tilde)', '<strong>yo hablaré</strong>', 'La forma yo del futuro lleva tilde en la última sílaba: <b>hablaré</b>. Sin tilde es subjuntivo imperfecto en algunos contextos o simplemente incorrecto.'),
            ('él tendrá → tendará', '<strong>él tendrá</strong>', 'TENER → raíz irregular <b>tendr-</b>, no «tendrá» derivado de «tener» completo. El infinitivo entero no se mantiene.'),
            ('yo iré → yo ire', '<strong>yo iré</strong>', 'IR en futuro: <b>iré</b>. La raíz es <b>ir-</b> + terminaciones normales. Lleva tilde.'),
            ('nosotros hablaremos (con tilde)', '<strong>nosotros hablaremos</strong> (sin tilde)', 'La forma <b>nosotros</b> es la única sin tilde en futuro simple: <b>hablaremos</b>, <b>comeremos</b>.'),
            ('yo hacere / yo haceré', '<strong>yo haré</strong>', 'HACER tiene raíz irregular en futuro: <b>har-</b>. Por eso es <b>haré</b>, no «haceré».'),
        ],
        summary=[
            ('Verbos regulares', 'infinitivo + -é/-ás/-á/-emos/-éis/-án', 'Mañana hablaré con el director.'),
            ('TENER', 'tendr- + terminaciones', 'Tendré una reunión importante.'),
            ('PODER', 'podr- + terminaciones', '¿Podrás venir mañana?'),
            ('HACER', 'har- + terminaciones', 'Ella hará un viaje el verano que viene.'),
            ('IR', 'ir- + terminaciones', 'Iremos a la playa en agosto.'),
            ('Predicción / suposición', 'Futuro para adivinar', '¿Dónde estará mi móvil?'),
        ],
        ex1=('Elige la forma de futuro correcta', 'Selecciona el futuro simple correcto.',
             [('Mañana (hablar, yo) ______ con mi jefe.', ['hablo', 'hablé', 'hablaré'], 'hablaré', 'Futuro simple, yo: <b>hablaré</b>.'),
              ('El año que viene ellos (vivir) ______ en París.', ['vivieron', 'vivirán', 'viven'], 'vivirán', 'Futuro de VIVIR, ellos: <b>vivirán</b>.'),
              ('¿(Poder, tú) ______ ayudarme esta tarde?', ['pudiste', 'puedes', 'podrás'], 'podrás', 'PODER es irregular en futuro: tú → <b>podrás</b>.'),
              ('Nosotros (hacer) ______ una fiesta el sábado.', ['hacemos', 'haremos', 'hicimos'], 'haremos', 'HACER → nosotros futuro: <b>haremos</b>.'),
              ('Ella (tener) ______ que estudiar mucho para el examen.', ['tiene', 'tuvo', 'tendrá'], 'tendrá', 'TENER → ella futuro: <b>tendrá</b>.'),
              ('¿Adónde (ir, vosotros) ______ de vacaciones?', ['vais', 'fuisteis', 'iréis'], 'iréis', 'IR → vosotros futuro: <b>iréis</b>.'),
             ]),
        ex2=('Escribe el verbo en futuro simple', 'Conjuga el verbo entre paréntesis en futuro simple.',
             [('Pronto (abrir) ______ el nuevo museo de arte.', 'abrirá', 'ABRIR → él/ella futuro: <b>abrirá</b>.'),
              ('Este verano (viajar, nosotros) ______ por toda España.', 'viajaremos', 'VIAJAR → nosotros futuro: <b>viajaremos</b>.'),
              ('¿Cuándo (venir, tú) ______ a visitarme?', 'vendrás', 'VENIR es irregular: tú → <b>vendrás</b>.'),
              ('Mañana (salir, yo) ______ temprano de casa.', 'saldré', 'SALIR es irregular: yo → <b>saldré</b>.'),
              ('Los científicos (descubrir) ______ muchas cosas nuevas.', 'descubrirán', 'DESCUBRIR → ellos futuro: <b>descubrirán</b>.'),
             ]),
        ex3=('Futuro o presente', 'Elige qué tiempo verbal es el correcto según el contexto.',
             [('Prometo que ______ a tiempo. (llegar, yo)', ['llego', 'llegué', 'llegaré'], 'llegaré', 'Una promesa sobre el futuro → futuro simple: <b>llegaré</b>.'),
              ('¿Dónde ______ mis gafas? (estar) [suposición]', ['estaban', 'estarán', 'están'], 'estarán', 'Suposición sobre el presente/futuro → <b>estarán</b>.'),
              ('¿Cuál es el futuro de HACER para yo?', ['haceré', 'haré', 'hicé'], 'haré', 'HACER tiene raíz irregular <b>har-</b>: yo → <b>haré</b>.'),
              ('¿Cuál es la forma correcta de TENER para ella en futuro?', ['tendrá', 'tenerá', 'tuvo'], 'tendrá', 'TENER → raíz <b>tendr-</b>: ella → <b>tendrá</b>.'),
              ('El próximo mes nosotros ______ un nuevo compañero. (tener)', ['teníamos', 'tenemos', 'tendremos'], 'tendremos', 'TENER → nosotros futuro: <b>tendremos</b>.'),
             ]),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('fut-01', 'hablaré', 'futuro yo de HABLAR', 'primera persona futuro -AR', 'Mañana hablaré con la directora.', 'Mañana ______ con la directora.', 'hablaré'),
            ('fut-02', 'comerán', 'futuro ellos de COMER', 'tercera persona plural futuro -ER', 'Este domingo comerán en casa de los abuelos.', 'Este domingo ______ en casa de los abuelos.', 'comerán'),
            ('fut-03', 'tendrá', 'futuro él/ella de TENER', 'tener: raíz irregular tendr-', 'El niño tendrá una sorpresa mañana.', 'El niño ______ una sorpresa mañana.', 'tendrá'),
            ('fut-04', 'podremos', 'futuro nosotros de PODER', 'poder: raíz irregular podr-', 'El año que viene podremos visitar Italia.', 'El año que viene ______ visitar Italia.', 'podremos'),
            ('fut-05', 'haré', 'futuro yo de HACER', 'hacer: raíz irregular har-', 'Mañana haré la compra por la mañana.', 'Mañana ______ la compra por la mañana.', 'haré'),
            ('fut-06', 'iréis', 'futuro vosotros de IR', 'ir: raíz ir- + terminación -éis', '¿Adónde iréis el verano que viene?', '¿Adónde ______ el verano que viene?', 'iréis'),
            ('fut-07', 'saldrá', 'futuro él/ella de SALIR', 'salir: raíz irregular saldr-', 'El tren saldrá a las ocho en punto.', 'El tren ______ a las ocho en punto.', 'saldrá'),
            ('fut-08', 'viviremos', 'futuro nosotros de VIVIR', 'vivir futuro regular nosotros', 'Pronto viviremos en un apartamento más grande.', 'Pronto ______ en un apartamento más grande.', 'viviremos'),
        ],
    ),

    'condicional': dict(
        level='a2',
        section='grammar',
        num='G04',
        short='Condicional Simple',
        title='El Condicional Simple — Sería, comería, viviría',
        subtitle='Peticiones educadas, deseos e hipótesis',
        slides=[
            ('¿Para qué sirve el condicional?', None,
             '<p class="slide-explanation">El <b>condicional simple</b> expresa lo que <b>haríamos</b> en una situación '
             'hipotética, o se usa para hacer peticiones de forma más educada.</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Petición educada:</b> ¿<b>Podrías</b> abrir la ventana, por favor?</p>'
             '<p><b>Deseo o consejo:</b> Yo en tu lugar, <b>estudiaría</b> más.</p>'
             '<p><b>Hipótesis:</b> Si tuviera dinero, <b>viajaría</b> por todo el mundo.</p>'
             '<p><b>Futuro en el pasado:</b> Dijo que <b>llamaría</b> después.</p>'
             '</div>'),

            ('Formación: verbos regulares', None,
             '<p class="slide-explanation">El condicional se forma igual que el futuro: <b>infinitivo completo + terminaciones</b>. '
             'Las terminaciones son las mismas para los tres grupos de verbos:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronombre</th><th style="padding:8px;text-align:left">HABLAR</th><th style="padding:8px;text-align:left">COMER</th><th style="padding:8px;text-align:left">VIVIR</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">yo</td><td style="padding:8px"><b>hablaría</b></td><td style="padding:8px"><b>comería</b></td><td style="padding:8px"><b>viviría</b></td></tr>'
             '<tr><td style="padding:8px">tú</td><td style="padding:8px"><b>hablarías</b></td><td style="padding:8px"><b>comerías</b></td><td style="padding:8px"><b>vivirías</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">él/ella</td><td style="padding:8px"><b>hablaría</b></td><td style="padding:8px"><b>comería</b></td><td style="padding:8px"><b>viviría</b></td></tr>'
             '<tr><td style="padding:8px">nosotros</td><td style="padding:8px"><b>hablaríamos</b></td><td style="padding:8px"><b>comeríamos</b></td><td style="padding:8px"><b>viviríamos</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">vosotros</td><td style="padding:8px"><b>hablaríais</b></td><td style="padding:8px"><b>comeríais</b></td><td style="padding:8px"><b>viviríais</b></td></tr>'
             '<tr><td style="padding:8px">ellos/ellas</td><td style="padding:8px"><b>hablarían</b></td><td style="padding:8px"><b>comerían</b></td><td style="padding:8px"><b>vivirían</b></td></tr>'
             '</table>'
             '<p class="slide-explanation">Todas las formas del condicional llevan tilde en la <b>í</b>.</p>'),

            ('Verbos irregulares en condicional', None,
             '<p class="slide-explanation">Los verbos con raíz irregular en <b>futuro</b> tienen la <b>misma raíz irregular en condicional</b>. '
             'Solo cambian las terminaciones (-ía, -ías…):</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Infinitivo</th><th style="padding:8px;text-align:left">Raíz</th><th style="padding:8px;text-align:left">Yo</th><th style="padding:8px;text-align:left">Él/ella</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">tener</td><td style="padding:8px"><b>tendr-</b></td><td style="padding:8px">tendría</td><td style="padding:8px">tendría</td></tr>'
             '<tr><td style="padding:8px">poder</td><td style="padding:8px"><b>podr-</b></td><td style="padding:8px">podría</td><td style="padding:8px">podría</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">hacer</td><td style="padding:8px"><b>har-</b></td><td style="padding:8px">haría</td><td style="padding:8px">haría</td></tr>'
             '<tr><td style="padding:8px">salir</td><td style="padding:8px"><b>saldr-</b></td><td style="padding:8px">saldría</td><td style="padding:8px">saldría</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">venir</td><td style="padding:8px"><b>vendr-</b></td><td style="padding:8px">vendría</td><td style="padding:8px">vendría</td></tr>'
             '</table>'),

            ('Condicional para peticiones educadas', None,
             '<p class="slide-explanation">El condicional es más <b>educado y cortés</b> que el imperativo o el presente. '
             'Se usa mucho en situaciones formales o para pedir un favor:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Brusco:</b> Abre la ventana.</p>'
             '<p><b>Normal:</b> ¿Puedes abrir la ventana?</p>'
             '<p><b>Educado:</b> ¿<b>Podrías</b> abrir la ventana, por favor?</p>'
             '<p>&nbsp;</p>'
             '<p>¿<b>Le importaría</b> bajar el volumen?</p>'
             '<p>¿<b>Tendría</b> usted un momento?</p>'
             '<p><b>Querría</b> una mesa para dos, por favor.</p>'
             '</div>'),
        ],
        traps=[
            ('yo hablaría → yo hablaria (sin tilde)', '<strong>hablaría</strong> (con tilde en í)', 'Todas las formas del condicional llevan tilde en la <b>í</b>: hablaría, comerías, viviríamos…'),
            ('Confundir imperfecto y condicional', 'Son tiempos <strong>distintos</strong>', 'Imperfecto: <b>comía</b> (pasado habitual). Condicional: <b>comería</b> (hipotético). Las terminaciones parecen similares pero los usos son muy diferentes.'),
            ('yo hacería / yo haceríe', '<strong>yo haría</strong>', 'HACER tiene raíz irregular <b>har-</b> en condicional (igual que en futuro). Por eso es <b>haría</b>, nunca «hacería».'),
            ('nosotros hablaríamos → hablarían', '<strong>nosotros hablaríamos</strong>', 'La forma nosotros termina en <b>-íamos</b>, no <b>-ían</b>. <b>-ían</b> es para ellos/ellas.'),
            ('Usar condicional con "si" + presente', 'Si + <strong>presente → futuro</strong>; Si + <strong>imperfecto → condicional</strong>', 'En las frases hipotéticas: «Si <b>tengo</b> dinero, <b>viajaré</b>» (real). «Si <b>tuviera</b> dinero, <b>viajaría</b>» (irreal/hipotético).'),
        ],
        summary=[
            ('Verbos regulares', 'infinitivo + -ía/-ías/-ía/-íamos/-íais/-ían', 'Yo hablaría con él directamente.'),
            ('TENER', 'tendría, tendrías, tendría…', '¿Tendrías tiempo esta tarde?'),
            ('PODER', 'podría, podrías, podría…', '¿Podrías repetirlo, por favor?'),
            ('HACER', 'haría, harías, haría…', 'Yo no haría eso en tu lugar.'),
            ('Petición educada', '¿Podría/Querría/Tendría…?', '¿Querría un café, señora?'),
            ('Hipótesis', 'Si + imperfecto + condicional', 'Si pudiera, viviría en el campo.'),
        ],
        ex1=('Elige la forma correcta de condicional', 'Selecciona la opción correcta.',
             [('En tu lugar, yo (estudiar) ______ más.', ['estudié', 'estudiaría', 'estudiaba'], 'estudiaría', 'Consejo hipotético → condicional: <b>estudiaría</b>.'),
              ('¿(Poder, usted) ______ ayudarme con esto?', ['puede', 'pudo', 'podría'], 'podría', 'Petición educada → condicional: <b>podría</b>.'),
              ('Ella dijo que (llegar) ______ tarde.', ['llegará', 'llegaría', 'llegó'], 'llegaría', 'Futuro en el pasado (reported speech) → condicional: <b>llegaría</b>.'),
              ('Si tuviéramos más tiempo, (hacer, nosotros) ______ un viaje largo.', ['haríamos', 'hicimos', 'haremos'], 'haríamos', 'Hipótesis → condicional: <b>haríamos</b>.'),
              ('¿(Importar, te) ______ hablar más despacio?', ['importa', 'importaría', 'importó'], 'importaría', 'Petición educada: ¿Te <b>importaría</b>…?'),
              ('¿Cuál es el condicional de HACER para yo?', ['haré', 'hiciera', 'haría'], 'haría', 'HACER → raíz <b>har-</b>: yo condicional: <b>haría</b>.'),
             ]),
        ex2=('Escribe el verbo en condicional', 'Escribe la forma de condicional simple.',
             [('¿(Poder, tú) ______ abrir la puerta, por favor?', 'podrías', 'PODER → tú condicional: <b>podrías</b>.'),
              ('En tu lugar, yo no (decir) ______ eso.', 'diría', 'DECIR → raíz irregular <b>dir-</b>: yo condicional: <b>diría</b>.'),
              ('Ellos (venir) ______ si los invitáramos.', 'vendrían', 'VENIR → raíz <b>vendr-</b>: ellos condicional: <b>vendrían</b>.'),
              ('Nosotros (vivir) ______ en el campo si pudiéramos.', 'viviríamos', 'VIVIR → nosotros condicional: <b>viviríamos</b>.'),
              ('¿(Tener, usted) ______ un momento para hablar?', 'tendría', 'TENER → raíz <b>tendr-</b>: usted condicional: <b>tendría</b>.'),
             ]),
        ex3=('Usos del condicional', 'Elige la oración donde el condicional está bien usado.',
             [('¿Cuál expresa una petición educada?', ['Abre la ventana.', '¿Podrías abrir la ventana?', 'Abriste la ventana.'], '¿Podrías abrir la ventana?', '<b>¿Podrías…?</b> es una petición educada con condicional.'),
              ('¿Cuál expresa una hipótesis?', ['Si tengo dinero, viajo.', 'Si tuviera dinero, viajaría.', 'Cuando tenga dinero, viajaré.'], 'Si tuviera dinero, viajaría.', 'Hipótesis irreal: si + imperfecto + <b>condicional</b>.'),
              ('¿Cuál usa el condicional correctamente?', ['Yo comería más si tuviera hambre.', 'Yo comería ayer mucho.', 'Comeré mañana en tu casa.'], 'Yo comería más si tuviera hambre.', '<b>Comería</b> es condicional correcto en un contexto hipotético.'),
              ('¿Cuál es el condicional correcto de SALIR para ella?', ['saldrá', 'saldría', 'salió'], 'saldría', 'SALIR → raíz <b>saldr-</b>: ella condicional: <b>saldría</b>.'),
              ('¿Qué expresa «Dijo que vendría»?', ['Una orden', 'Un futuro en el pasado', 'Una descripción'], 'Un futuro en el pasado', 'El condicional en discurso indirecto expresa un futuro visto desde el pasado: <b>vendría</b>.'),
             ]),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('cond-01', 'hablaría', 'condicional yo/él de HABLAR', 'hablar en situación hipotética', 'Yo hablaría con ella directamente.', 'Yo ______ con ella directamente.', 'hablaría'),
            ('cond-02', 'comería', 'condicional yo/él de COMER', 'comer en situación hipotética', 'En ese restaurante comería todos los días.', 'En ese restaurante ______ todos los días.', 'comería'),
            ('cond-03', 'podría', 'condicional yo/él de PODER', 'poder: raíz podr- + -ía', '¿Podría hablar con el director, por favor?', '¿______ hablar con el director, por favor?', 'podría'),
            ('cond-04', 'tendría', 'condicional yo/él de TENER', 'tener: raíz tendr- + -ía', '¿Tendría usted un momento libre?', '¿______ usted un momento libre?', 'tendría'),
            ('cond-05', 'haría', 'condicional yo/él de HACER', 'hacer: raíz har- + -ía', 'Yo no haría eso en tu lugar.', 'Yo no ______ eso en tu lugar.', 'haría'),
            ('cond-06', 'viviríamos', 'condicional nosotros de VIVIR', 'vivir hipotético (nosotros)', 'Viviríamos en la playa si pudiéramos.', '______ en la playa si pudiéramos.', 'viviríamos'),
            ('cond-07', 'vendrían', 'condicional ellos de VENIR', 'venir: raíz vendr- + -ían', 'Ellos vendrían si los invitaras.', 'Ellos ______ si los invitaras.', 'vendrían'),
            ('cond-08', 'saldría', 'condicional yo/él de SALIR', 'salir: raíz saldr- + -ía', 'Ella saldría antes si terminara pronto.', 'Ella ______ antes si terminara pronto.', 'saldría'),
        ],
    ),

    'ser-estar-a2': dict(
        level='a2',
        section='grammar',
        num='G05',
        short='SER y ESTAR avanzado',
        title='SER y ESTAR: usos avanzados — Matices y participios',
        subtitle='Distingue ser aburrido de estar aburrido y otros matices esenciales',
        slides=[
            ('Repaso rápido: SER vs. ESTAR', None,
             '<p class="slide-explanation">Ya conoces la regla básica: <b>SER</b> para características permanentes o esenciales, '
             '<b>ESTAR</b> para estados temporales o condiciones cambiantes. En A2 profundizamos en los casos más complejos.</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>SER:</b> origen, profesión, material, relación, hora/fecha, identidad</p>'
             '<p>&nbsp;&nbsp;→ Madrid <b>es</b> la capital. / Ella <b>es</b> médica. / <b>Es</b> de madera.</p>'
             '<p><b>ESTAR:</b> lugar (de personas/cosas), estado físico/emocional, resultado de acción</p>'
             '<p>&nbsp;&nbsp;→ <b>Estoy</b> cansado. / El libro <b>está</b> en la mesa. / <b>Estamos</b> listos.</p>'
             '</div>'),

            ('El truco del significado doble', None,
             '<p class="slide-explanation">Muchos adjetivos cambian de significado según se usen con <b>SER</b> o <b>ESTAR</b>. '
             'Este es el tema más importante del nivel A2:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Adjetivo</th><th style="padding:8px;text-align:left">Con SER</th><th style="padding:8px;text-align:left">Con ESTAR</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>aburrido</b></td><td style="padding:8px">Es aburrido. (Es una persona aburrida por naturaleza)</td><td style="padding:8px">Está aburrido. (Siente aburrimiento ahora)</td></tr>'
             '<tr><td style="padding:8px"><b>listo</b></td><td style="padding:8px">Es listo. (Es inteligente)</td><td style="padding:8px">Está listo. (Está preparado)</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>malo</b></td><td style="padding:8px">Es malo. (Es una mala persona)</td><td style="padding:8px">Está malo. (Está enfermo)</td></tr>'
             '<tr><td style="padding:8px"><b>bueno</b></td><td style="padding:8px">Es bueno. (Tiene buen carácter)</td><td style="padding:8px">Está bueno. (Sabe bien / está rico)</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>rico</b></td><td style="padding:8px">Es rico. (Tiene mucho dinero)</td><td style="padding:8px">Está rico. (Sabe muy bien)</td></tr>'
             '<tr><td style="padding:8px"><b>muerto</b></td><td style="padding:8px">Es un hombre muerto. (en ficción: personaje)</td><td style="padding:8px">Está muerto. (ha fallecido)</td></tr>'
             '</table>'),

            ('SER + participio pasado: voz pasiva', None,
             '<p class="slide-explanation">En español, <b>SER + participio</b> forma la <b>voz pasiva</b>: '
             'el sujeto recibe la acción. El participio concuerda en género y número con el sujeto.</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>La carta <b>fue escrita</b> por Ana. (<i>Ana escribió la carta</i>)</p>'
             '<p>El puente <b>fue construido</b> en 1900.</p>'
             '<p>Las ventanas <b>fueron abiertas</b> por el viento.</p>'
             '</div>'
             '<p class="slide-explanation">En español coloquial se prefiere la <b>voz activa</b> o la construcción con <b>se</b>: '
             '«<b>Se escribió</b> la carta». La pasiva con SER es más formal y escrita.</p>'),

            ('ESTAR + participio: resultado de una acción', None,
             '<p class="slide-explanation"><b>ESTAR + participio</b> describe el <b>estado resultante</b> de una acción. '
             'No indica quién lo hizo, sino cómo está la cosa <b>ahora</b>:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>La puerta <b>está abierta</b>. (resultado: alguien la abrió)</p>'
             '<p>La tienda <b>está cerrada</b>. (está en ese estado ahora)</p>'
             '<p>El trabajo <b>está terminado</b>. (ya se acabó)</p>'
             '<p>Las ventanas <b>están rotas</b>. (ese es su estado actual)</p>'
             '</div>'
             '<p class="slide-explanation">El participio concuerda en <b>género y número</b> con el sustantivo: '
             'abierto/abierta/abiertos/abiertas.</p>'),

            ('Casos especiales con ESTAR', None,
             '<p class="slide-explanation">ESTAR se usa también en contextos que a veces sorprenden a los estudiantes:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Localización</b> (incluso de sitios fijos): El Prado <b>está</b> en Madrid.</p>'
             '<p><b>Estados de ánimo:</b> Hoy <b>estoy</b> muy contento.</p>'
             '<p><b>Aspecto visual percibido:</b> ¡Qué guapo <b>estás</b> hoy!</p>'
             '<p><b>Precio (informal):</b> ¿A cuánto <b>están</b> los tomates?</p>'
             '<p><b>Gerundio (estar + -ando/-iendo):</b> <b>Estoy comiendo</b>. (acción en progreso)</p>'
             '</div>'
             '<p class="slide-explanation">Recuerda: la localización de personas y objetos siempre con ESTAR, '
             'aunque el lugar sea permanente. Solo la identidad y características esenciales usan SER.</p>'),
        ],
        traps=[
            ('Es cansado (persona) vs. Está cansado', '<strong>Está cansado</strong> para el estado', 'Cuando describes cómo se siente alguien <b>en este momento</b>, usa ESTAR: <b>está cansado</b>. «Es cansado» significaría que esa persona es pesada/aburrida por naturaleza.'),
            ('El museo es en el centro', '<strong>El museo está en el centro</strong>', 'La localización, incluso de edificios permanentes, usa siempre <b>ESTAR</b>: «El museo <b>está</b> en el centro».'),
            ('Soy listo → significado equivocado', '<strong>Estoy listo</strong> para «estoy preparado»', 'Cuidado con <b>listo</b>: «<b>Soy</b> listo» = soy inteligente. «<b>Estoy</b> listo» = estoy preparado/listo para hacer algo.'),
            ('La puerta fue abierta vs. está abierta', 'Son construcciones <strong>distintas</strong>', '«<b>Fue abierta</b>» (SER + participio) es voz pasiva: alguien la abrió. «<b>Está abierta</b>» (ESTAR + participio) es el estado actual.'),
            ('Este pastel es muy rico / bueno → ser bueno', '<strong>Está muy rico</strong> para el sabor', 'Para comentar el sabor de la comida, usa siempre ESTAR: «Este pastel <b>está</b> muy rico/bueno».'),
        ],
        summary=[
            ('SER + adjetivo esencial', 'Característica permanente de identidad', 'Juan es inteligente y trabajador.'),
            ('ESTAR + adjetivo de estado', 'Estado temporal o percibido', 'Juan está cansado hoy.'),
            ('Adjetivos con doble significado', 'SER ≠ ESTAR con el mismo adjetivo', 'Es malo (mala persona) / Está malo (enfermo).'),
            ('SER + participio', 'Voz pasiva: sujeto recibe la acción', 'El puente fue construido en 1850.'),
            ('ESTAR + participio', 'Estado resultante de una acción', 'La puerta está abierta.'),
            ('Localización', 'Siempre ESTAR, también edificios', 'La catedral está en el centro.'),
        ],
        ex1=('SER o ESTAR: elige correctamente', 'Selecciona el verbo correcto según el contexto.',
             [('El Amazonas ______ el río más largo del mundo.', ['está', 'es', 'estaba'], 'es', 'Característica esencial / identidad → <b>es</b>.'),
              ('¿Dónde ______ el banco más cercano?', ['es', 'fue', 'está'], 'está', 'Localización → siempre <b>ESTAR</b>: <b>está</b>.'),
              ('La película ______ muy aburrida. (característica de la película)', ['está', 'estuvo', 'es'], 'es', 'Característica esencial de la película → <b>es</b>.'),
              ('¡Qué cansada ______ hoy! (estado temporal)', ['soy', 'eres', 'estás'], 'estás', 'Estado temporal → <b>ESTAR</b>: <b>estás</b>.'),
              ('Este café ______ muy rico. (sabor)', ['es', 'está', 'era'], 'está', 'Sabor/estado → <b>ESTAR</b>: <b>está</b>.'),
              ('La puerta ______ cerrada con llave. (estado resultante)', ['es', 'fue', 'está'], 'está', 'Estado resultante → <b>ESTAR</b>: <b>está</b>.'),
             ]),
        ex2=('Completa con SER o ESTAR', 'Escribe la forma correcta de SER o ESTAR.',
             [('Esta sopa ______ deliciosa. (sabor)', 'está', 'Sabor → ESTAR: <b>está</b>.'),
              ('El informe ya ______ terminado.', 'está', 'Estado resultante de una acción → <b>está terminado</b>.'),
              ('Mis padres ______ de vacaciones esta semana.', 'están', 'Estado temporal y localización → <b>están</b>.'),
              ('La reunión ______ a las nueve de la mañana. (hora fija)', 'es', 'Hora/evento → SER: <b>es</b>.'),
              ('¿ ______ listo para el examen?', 'Estás', 'Preparado = estado → <b>¿Estás listo?</b>'),
             ]),
        ex3=('SER + participio vs. ESTAR + participio', 'Elige la opción que corresponde al significado indicado.',
             [('La ventana ______ rota. (estado actual)', ['es rota', 'está rota', 'fue rota'], 'está rota', 'Estado actual del resultado de una acción → ESTAR + participio: <b>está rota</b>.'),
              ('El edificio ______ construido en 1920. (voz pasiva histórica)', ['está construido', 'es construido', 'fue construido'], 'fue construido', 'Voz pasiva en pasado → SER + participio (indefinido): <b>fue construido</b>.'),
              ('¿Cuál significa «es una persona aburrida»?', ['Está aburrido.', 'Es aburrido.', 'Fue aburrido.'], 'Es aburrido.', 'Característica esencial de la persona → <b>Es aburrido</b>.'),
              ('¿Cuál significa «siente aburrimiento ahora»?', ['Es aburrido.', 'Está aburrido.', 'Era aburrido.'], 'Está aburrido.', 'Estado temporal → <b>Está aburrido</b>.'),
              ('¿Cuál usa correctamente ESTAR + participio?', ['Los deberes son hechos.', 'Los deberes están hechos.', 'Los deberes fueron hechos ahora.'], 'Los deberes están hechos.', 'Estado resultante actual → <b>están hechos</b>.'),
             ]),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('serestar-01', 'es aburrido', 'SER + aburrido: característica de personalidad', 'adjetivo esencial con SER', 'No me gusta ese profesor, es aburrido.', 'No me gusta ese profesor, ______ aburrido.', 'es'),
            ('serestar-02', 'está aburrido', 'ESTAR + aburrido: estado emocional temporal', 'adjetivo de estado con ESTAR', 'Hoy está aburrido porque no hay nada que hacer.', 'Hoy ______ aburrido porque no hay nada que hacer.', 'está'),
            ('serestar-03', 'está abierta', 'ESTAR + participio: estado resultante', 'resultado de una acción pasada', 'La tienda está abierta hasta las nueve.', 'La tienda ______ abierta hasta las nueve.', 'está abierta'),
            ('serestar-04', 'fue construido', 'SER + participio: voz pasiva', 'voz pasiva con ser + participio', 'Este palacio fue construido en el siglo XVII.', 'Este palacio ______ en el siglo XVII.', 'fue construido'),
            ('serestar-05', 'es listo', 'SER + listo: inteligente', 'listo con SER = inteligente', 'Tu hermano es muy listo, siempre saca buenas notas.', 'Tu hermano es muy ______, siempre saca buenas notas.', 'listo'),
            ('serestar-06', 'está listo', 'ESTAR + listo: preparado', 'listo con ESTAR = preparado', '¿Estás listo? El taxi llega en cinco minutos.', '¿______ listo? El taxi llega en cinco minutos.', 'Estás'),
            ('serestar-07', 'está rico', 'ESTAR + rico: tiene buen sabor', 'rico con ESTAR = sabor', 'Este arroz está muy rico, ¿cuál es la receta?', 'Este arroz ______ muy rico.', 'está'),
            ('serestar-08', 'está cerrado', 'ESTAR + participio: estado actual', 'resultado de acción → ESTAR', 'El supermercado está cerrado los domingos por la tarde.', 'El supermercado ______ cerrado los domingos por la tarde.', 'está cerrado'),
        ],
    ),
}
