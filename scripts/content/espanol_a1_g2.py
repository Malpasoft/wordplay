# -*- coding: utf-8 -*-
"""espanol/ A1 Gramática — lote 2 (G06–G10)."""

CHAPTERS = {

# ─────────────────────────────────────────────────────────────────────────────
# G06  TENER
# ─────────────────────────────────────────────────────────────────────────────
'tener': dict(
    level='a1',
    section='grammar',
    num='G06',
    short='El verbo TENER',
    title='El verbo TENER — Posesión, edad y sensaciones',
    subtitle='Cómo usar tener para hablar de lo que tienes, cuántos años tienes y cómo te sientes.',
    slides=[
        ('El verbo TENER: conjugación', None,
         '<p class="slide-explanation">El verbo <b>tener</b> es irregular en español. '
         'Se usa para expresar posesión, edad y muchas sensaciones físicas. '
         'La forma <b>yo tengo</b> es la más irregular; el resto del singular '
         'cambia la <b>e</b> de la raíz por <b>ie</b> (excepto nosotros/vosotros).</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<table style="width:100%;border-collapse:collapse">'
         '<tr><th style="text-align:left;padding:6px 10px">Pronombre</th>'
         '<th style="text-align:left;padding:6px 10px">Forma</th></tr>'
         '<tr><td style="padding:6px 10px">yo</td><td style="padding:6px 10px"><b>tengo</b></td></tr>'
         '<tr><td style="padding:6px 10px">tú</td><td style="padding:6px 10px"><b>tienes</b></td></tr>'
         '<tr><td style="padding:6px 10px">él / ella / usted</td><td style="padding:6px 10px"><b>tiene</b></td></tr>'
         '<tr><td style="padding:6px 10px">nosotros/as</td><td style="padding:6px 10px"><b>tenemos</b></td></tr>'
         '<tr><td style="padding:6px 10px">vosotros/as</td><td style="padding:6px 10px"><b>tenéis</b></td></tr>'
         '<tr><td style="padding:6px 10px">ellos / ellas / ustedes</td><td style="padding:6px 10px"><b>tienen</b></td></tr>'
         '</table></div>'),

        ('TENER para la posesión', None,
         '<p class="slide-explanation"><b>Tener</b> expresa que algo nos pertenece o que contamos con algo. '
         'Equivale al verbo <i>to have</i> en inglés. '
         'Es uno de los usos más frecuentes en la vida cotidiana.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Yo tengo un perro y dos gatos en casa.</b></p>'
         '<p style="margin-top:8px"><b>Mi hermana tiene un apartamento en el centro.</b></p>'
         '<p style="margin-top:8px"><b>Nosotros tenemos mucho trabajo esta semana.</b></p>'
         '</div>'
         '<p style="margin-top:14px">Recuerda que en las preguntas el orden es flexible: '
         '<b>¿Tienes coche?</b> o <b>¿Tú tienes coche?</b> son igualmente correctas.</p>'),

        ('TENER + años: la edad', None,
         '<p class="slide-explanation">En español la edad se expresa con <b>tener + número + años</b>. '
         'No se usa el verbo <i>ser</i> para la edad. '
         'Esta construcción es diferente al inglés («I am 20 years old»), '
         'donde se usa <i>to be</i>.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Yo tengo veinte años.</b> (I am twenty years old.)</p>'
         '<p style="margin-top:8px"><b>Mi abuela tiene ochenta y tres años.</b></p>'
         '<p style="margin-top:8px"><b>¿Cuántos años tienes tú?</b></p>'
         '</div>'
         '<p style="margin-top:14px">La pregunta para pedir la edad es siempre: '
         '<b>¿Cuántos años tienes?</b> (singular) o '
         '<b>¿Cuántos años tiene usted?</b> (formal).</p>'),

        ('TENER + sensaciones físicas', None,
         '<p class="slide-explanation">En español muchas sensaciones físicas se expresan con '
         '<b>tener + sustantivo</b>, no con el verbo <i>ser</i> o <i>estar</i>. '
         'Estas expresiones son muy comunes en la conversación diaria y hay que aprenderlas como bloques.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<table style="width:100%;border-collapse:collapse">'
         '<tr><th style="text-align:left;padding:5px 10px">Expresión</th>'
         '<th style="text-align:left;padding:5px 10px">Significado</th></tr>'
         '<tr><td style="padding:5px 10px"><b>tener hambre</b></td><td style="padding:5px 10px">to be hungry</td></tr>'
         '<tr><td style="padding:5px 10px"><b>tener sed</b></td><td style="padding:5px 10px">to be thirsty</td></tr>'
         '<tr><td style="padding:5px 10px"><b>tener frío</b></td><td style="padding:5px 10px">to be cold</td></tr>'
         '<tr><td style="padding:5px 10px"><b>tener calor</b></td><td style="padding:5px 10px">to be hot</td></tr>'
         '<tr><td style="padding:5px 10px"><b>tener sueño</b></td><td style="padding:5px 10px">to be sleepy</td></tr>'
         '<tr><td style="padding:5px 10px"><b>tener miedo</b></td><td style="padding:5px 10px">to be afraid</td></tr>'
         '<tr><td style="padding:5px 10px"><b>tener razón</b></td><td style="padding:5px 10px">to be right</td></tr>'
         '<tr><td style="padding:5px 10px"><b>tener prisa</b></td><td style="padding:5px 10px">to be in a hurry</td></tr>'
         '</table></div>'),

        ('TENER en contexto: ejemplos completos', None,
         '<p class="slide-explanation">Observa cómo <b>tener</b> aparece en situaciones reales. '
         'La misma estructura sirve para posesión, edad y sensaciones.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Tengo mucha sed. ¿Tienes agua?</b></p>'
         '<p style="margin-top:8px"><b>Mi madre tiene cuarenta y cinco años y tiene una farmacia.</b></p>'
         '<p style="margin-top:8px"><b>¿Tenéis frío? Podemos cerrar la ventana.</b></p>'
         '<p style="margin-top:8px"><b>Los niños tienen sueño; son las diez de la noche.</b></p>'
         '</div>'
         '<p style="margin-top:14px">Nota: cuando el adjetivo modifica el sustantivo de la expresión, '
         'concuerda en género y número: <b>tengo mucha hambre</b> (hambre = femenino), '
         '<b>tengo mucho frío</b> (frío = masculino).</p>'),
    ],
    traps=[
        ('Soy veinte años.', '<strong>Tengo</strong> veinte años.',
         'La edad se expresa con TENER, nunca con ser. Recuerda: tener + número + años.'),
        ('Estoy hambre.', 'Tengo <strong>hambre</strong>.',
         'Las sensaciones físicas usan TENER, no estar. Tengo hambre / sed / frío / calor / sueño.'),
        ('Yo tengo caliente.', 'Yo tengo <strong>calor</strong>.',
         'Se dice «tener calor», no «tener caliente». Calor es el sustantivo correcto en esta expresión.'),
        ('Ellos tiene un coche.', 'Ellos <strong>tienen</strong> un coche.',
         'Con ellos/ellas/ustedes la forma es «tienen» (con -n final), no «tiene».'),
        ('¿Cuántos años tienes tú?  — Tengo años veinte.', '— Tengo <strong>veinte años</strong>.',
         'El número va antes de «años»: tengo VEINTE AÑOS, no «años veinte».'),
    ],
    summary=[
        ('Posesión', 'tener + sustantivo', 'Tengo un libro nuevo.'),
        ('Edad', 'tener + número + años', 'Ella tiene doce años.'),
        ('Hambre / sed', 'tener hambre · tener sed', 'Tenemos hambre. ¿Tienes agua?'),
        ('Frío / calor', 'tener frío · tener calor', 'Los niños tienen frío hoy.'),
        ('Sueño / prisa', 'tener sueño · tener prisa', 'Tengo mucho sueño. Date prisa.'),
        ('Negación', 'no tener + sustantivo', 'No tengo tiempo ahora mismo.'),
    ],
    ex1=('Elige la forma correcta de TENER', 'Selecciona la opción adecuada para completar cada oración.',
         [
             ('Mi hermano ______ diecisiete años.',
              ['tiene', 'tengo', 'tienen'], 'tiene',
              'Con él/ella/usted la forma es «tiene». Mi hermano = él → tiene.'),
             ('Nosotros ______ mucha hambre después del partido.',
              ['tenemos', 'tienen', 'tenéis'], 'tenemos',
              'Con nosotros la forma es «tenemos». Hambre es femenino: mucha hambre.'),
             ('¿Vosotros ______ las entradas del concierto?',
              ['tenéis', 'tienen', 'tenemos'], 'tenéis',
              'Con vosotros la forma es «tenéis» (con tilde en la é).'),
             ('Ellas ______ frío porque no llevan abrigo.',
              ['tienen', 'tiene', 'tenéis'], 'tienen',
              'Con ellas/ellos/ustedes la forma es «tienen».'),
             ('Yo ______ mucho sueño. Son las dos de la madrugada.',
              ['tengo', 'tienes', 'tiene'], 'tengo',
              'Con yo la forma es «tengo». Recuerda que la -g- es la irregularidad de la primera persona.'),
             ('¿Tú ______ sed? Hay zumo en la nevera.',
              ['tienes', 'tiene', 'tengo'], 'tienes',
              'Con tú la forma es «tienes» (diptongo ie en la raíz: t-ie-nes).'),
         ]),
    ex2=('Escribe la forma correcta de TENER', 'Conjuga el verbo tener según el sujeto indicado.',
         [
             ('¿Cuántos años ______ (tú)?', 'tienes',
              'Tú + tener → tienes. Pregunta de edad con tener.'),
             ('Mi abuelo ______ setenta y dos años y ______ muy buena salud. (él / él)', 'tiene / tiene',
              'Dos formas de tiene (él): una para la edad y otra para la posesión/estado.'),
             ('Los estudiantes no ______ tiempo para descansar. (ellos)', 'tienen',
              'Ellos + tener → tienen. La negación va antes del verbo: no tienen.'),
             ('Nosotras ______ prisa; el tren sale en cinco minutos. (nosotras)', 'tenemos',
              'Nosotras + tener → tenemos. Expresión: tener prisa.'),
             ('¿Vosotros ______ miedo de los exámenes? (vosotros)', 'tenéis',
              'Vosotros + tener → tenéis (tilde obligatoria en la é).'),
         ]),
    ex3=('TENER en contexto', 'Elige la opción correcta según el significado de la oración.',
         [
             ('Son las once de la noche y los niños ______ mucho sueño.',
              ['tienen', 'tienen hambre', 'tienen calor'], 'tienen',
              'La oración menciona «sueño», así que la respuesta correcta incluye ese sustantivo: tienen sueño. Aquí «tienen» es la opción que se combina con sueño.'),
             ('Hace 35 grados. Yo ______.',
              ['tengo calor', 'tengo frío', 'tengo sueño'], 'tengo calor',
              'Con temperaturas altas se usa «tener calor». Tengo calor (yo + tener → tengo).'),
             ('¿Cuántos años ______ tu profesora?',
              ['tiene', 'es', 'está'], 'tiene',
              'La edad siempre se pregunta con TENER: ¿Cuántos años tiene...?'),
             ('Mi padre ______ una tienda de ropa en el centro.',
              ['tiene', 'hay', 'está'], 'tiene',
              'Para expresar posesión con un sujeto determinado se usa TENER: mi padre tiene.'),
             ('Hemos corrido diez kilómetros. ______ mucha sed.',
              ['Tenemos', 'Somos', 'Estamos'], 'Tenemos',
              'La sed es una sensación que se expresa con TENER: tenemos sed (nosotros → tenemos).'),
         ]),
    game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
    items=[
        ('tener-tengo', 'tengo', 'primera persona singular de TENER', 'yo tengo',
         '<b>Tengo</b> dos hermanos y un perro.', 'Yo ______ veinte años.', 'tengo'),
        ('tener-tienes', 'tienes', 'segunda persona singular de TENER', 'tú tienes',
         '¿<b>Tienes</b> hermanos?', '¿______ hambre? Voy a preparar la cena.', 'tienes'),
        ('tener-tiene', 'tiene', 'tercera persona singular de TENER', 'él/ella tiene',
         'Mi madre <b>tiene</b> cuarenta años.', 'El gato ______ mucho frío.', 'tiene'),
        ('tener-tienen', 'tienen', 'tercera persona plural de TENER', 'ellos/ellas tienen',
         'Ellos <b>tienen</b> razón.', 'Los estudiantes ______ mucha tarea hoy.', 'tienen'),
        ('tener-hambre', 'tener hambre', 'expresión para sentir necesidad de comer', 'estar hambriento',
         'Los niños <b>tienen hambre</b> después del colegio.', 'Después de correr, yo ______ ______.', 'tengo hambre'),
        ('tener-sed', 'tener sed', 'expresión para sentir necesidad de beber', 'querer beber',
         '¿<b>Tienes sed</b>? Hay agua en la mesa.', '¿Tú ______ ______? Hay zumo en la nevera.', 'tienes sed'),
        ('tener-anos', 'tener + años', 'forma de expresar la edad en español', 'cumplir años',
         'Mi abuelo <b>tiene ochenta años</b>.', 'Ella ______ quince ______.', 'tiene / años'),
        ('tener-sueno', 'tener sueño', 'expresión para sentir ganas de dormir', 'estar cansado',
         'Tenemos mucho <b>sueño</b>; son las dos de la madrugada.', 'Son las tres de la noche y yo ______ mucho ______.', 'tengo sueño'),
    ],
),

# ─────────────────────────────────────────────────────────────────────────────
# G07  HAY
# ─────────────────────────────────────────────────────────────────────────────
'hay': dict(
    level='a1',
    section='grammar',
    num='G07',
    short='HAY / No hay',
    title='HAY / No hay — Existencia y cantidad',
    subtitle='Cómo usar hay para indicar que algo existe, y no hay para negar su existencia.',
    slides=[
        ('¿Qué es HAY?', None,
         '<p class="slide-explanation"><b>Hay</b> es una forma especial del verbo <i>haber</i> '
         'que se usa para indicar que algo <b>existe</b> o <b>está presente</b> en un lugar. '
         'Equivale a <i>there is / there are</i> en inglés. '
         'Es invariable: se usa la misma forma tanto para el singular como para el plural.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Hay un banco cerca de aquí.</b> (There is a bank near here.)</p>'
         '<p style="margin-top:8px"><b>Hay tres tiendas en esta calle.</b> (There are three shops on this street.)</p>'
         '<p style="margin-top:8px"><b>¿Hay una farmacia por aquí?</b> (Is there a pharmacy around here?)</p>'
         '</div>'
         '<p style="margin-top:14px">Observa que <b>hay</b> no cambia: es igual para uno o muchos.</p>'),

        ('HAY + artículo indefinido o numeral', None,
         '<p class="slide-explanation"><b>Hay</b> siempre va seguido de un artículo '
         '<b>indefinido</b> (un, una, unos, unas) o de un <b>numeral</b>. '
         'No se usa con artículo definido (el, la, los, las). '
         'Esto lo distingue del verbo <i>estar</i>.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Hay un supermercado</b> al final de la calle.</p>'
         '<p style="margin-top:8px"><b>Hay cuatro sillas</b> en la cocina.</p>'
         '<p style="margin-top:8px"><b>Hay mucha gente</b> en el parque hoy.</p>'
         '</div>'
         '<p style="margin-top:14px">Compara: <b>Hay un libro</b> en la mesa (existencia) '
         'vs. <b>El libro está en la mesa</b> (ubicación de algo ya conocido).</p>'),

        ('No hay: la negación', None,
         '<p class="slide-explanation">La forma negativa es simplemente <b>no hay</b>. '
         'No cambia para el singular ni el plural. '
         'Se usa para decir que algo no existe o no está disponible.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>No hay pan en la tienda.</b> (There is no bread in the shop.)</p>'
         '<p style="margin-top:8px"><b>No hay entradas para el concierto.</b></p>'
         '<p style="margin-top:8px"><b>Lo siento, no hay habitaciones libres.</b></p>'
         '</div>'
         '<p style="margin-top:14px">Después de <b>no hay</b> el sustantivo suele ir sin artículo: '
         '<b>no hay agua</b>, no «no hay el agua» ni «no hay un agua».</p>'),

        ('¿Hay...? Las preguntas', None,
         '<p class="slide-explanation">Para hacer una pregunta, simplemente coloca '
         '<b>¿Hay...?</b> al inicio. No se necesita ningún auxiliar adicional. '
         'La respuesta puede ser afirmativa (<b>sí, hay</b>) o negativa (<b>no, no hay</b>).</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>¿Hay una estación de metro cerca?</b> — Sí, hay una a dos minutos.</p>'
         '<p style="margin-top:8px"><b>¿Hay leche en el frigorífico?</b> — No, no hay.</p>'
         '<p style="margin-top:8px"><b>¿Hay autobuses por la noche?</b> — Sí, hay varios.</p>'
         '</div>'
         '<p style="margin-top:14px">En preguntas de este tipo también es común usar '
         '<b>¿hay algún/alguna...?</b> para preguntar de forma más cortés: '
         '<b>¿Hay algún médico disponible?</b></p>'),

        ('HAY vs. ESTÁ/ESTÁN', None,
         '<p class="slide-explanation">Este contraste es fundamental en español. '
         '<b>Hay</b> introduce información nueva (existencia). '
         '<b>Está/Están</b> localiza algo que ya conocemos (ubicación).</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<table style="width:100%;border-collapse:collapse">'
         '<tr><th style="text-align:left;padding:6px 10px">Hay (existencia)</th>'
         '<th style="text-align:left;padding:6px 10px">Está/Están (ubicación)</th></tr>'
         '<tr><td style="padding:6px 10px"><b>Hay un cine</b> en esta ciudad.</td>'
         '<td style="padding:6px 10px"><b>El cine está</b> en la plaza.</td></tr>'
         '<tr><td style="padding:6px 10px"><b>Hay</b> dos hospitales aquí.</td>'
         '<td style="padding:6px 10px"><b>El hospital está</b> a tres kilómetros.</td></tr>'
         '</table></div>'
         '<p style="margin-top:14px">Regla práctica: si puedes poner «un/una» delante, '
         'usa <b>hay</b>. Si usas «el/la», usa <b>está</b>.</p>'),
    ],
    traps=[
        ('Hay el banco en la esquina.', '<strong>Hay un</strong> banco en la esquina.',
         'HAY va con artículo indefinido (un, una) o numeral. Con artículo definido usa ESTAR: El banco está en la esquina.'),
        ('Hays muchas tiendas aquí.', '<strong>Hay</strong> muchas tiendas aquí.',
         'HAY es invariable. No existe «hays» ni «hayen». Es la misma forma para singular y plural.'),
        ('No hay el tiempo.', 'No hay <strong>tiempo</strong>.',
         'Después de «no hay» el sustantivo va sin artículo: no hay tiempo, no hay agua, no hay pan.'),
        ('¿Está un médico disponible?', '¿<strong>Hay</strong> un médico disponible?',
         'Para preguntar si algo existe o está disponible se usa HAY, no ESTAR.'),
        ('Están tres estudiantes en clase.', '<strong>Hay</strong> tres estudiantes en clase.',
         'Cuando presentamos algo nuevo con un número o artículo indefinido, usamos HAY (existencia), no ESTAR.'),
    ],
    summary=[
        ('Existencia (+)', 'Hay + un/una/unos/unas + sustantivo', 'Hay una biblioteca cerca.'),
        ('Existencia plural', 'Hay + numeral + sustantivo', 'Hay cinco personas en la sala.'),
        ('Negación', 'No hay + sustantivo (sin artículo)', 'No hay pan en casa.'),
        ('Pregunta', '¿Hay + un/una + sustantivo?', '¿Hay un hotel por aquí?'),
        ('Respuesta afirmativa', 'Sí, hay (uno/una / varios/as)', 'Sí, hay uno a dos minutos.'),
        ('Hay vs. Está', 'Hay = existencia; Está = ubicación conocida', 'Hay un parque. El parque está cerca.'),
    ],
    ex1=('Elige la opción correcta: hay, no hay o está/están', 'Selecciona la forma más adecuada.',
         [
             ('______ un restaurante muy bueno en esta calle.',
              ['Hay', 'Está', 'Son'], 'Hay',
              'Introducimos el restaurante por primera vez (existencia) → HAY.'),
             ('El museo ______ en el centro histórico de la ciudad.',
              ['está', 'hay', 'es'], 'está',
              'El museo ya es conocido (artículo definido «el») y preguntamos su ubicación → ESTÁ.'),
             ('Lo siento, ______ habitaciones disponibles esta noche.',
              ['no hay', 'no están', 'no es'], 'no hay',
              'Para negar la existencia o disponibilidad de algo → NO HAY.'),
             ('¿______ aparcamiento cerca del teatro?',
              ['Hay', 'Están', 'Es'], 'Hay',
              'Preguntamos si existe → ¿HAY...?'),
             ('En mi barrio ______ muchos cafés y tiendas.',
              ['hay', 'están', 'son'], 'hay',
              'Presentamos información nueva con artículo indefinido implícito → HAY.'),
             ('Las llaves ______ encima de la mesa.',
              ['están', 'hay', 'son'], 'están',
              'Localizamos un objeto conocido (las llaves = artículo definido) → ESTÁN.'),
         ]),
    ex2=('Completa con hay, no hay o la forma de estar', 'Escribe la forma verbal correcta.',
         [
             ('En esta ciudad ______ tres universidades públicas y una privada.', 'hay',
              'Presentamos información nueva: tres universidades → HAY.'),
             ('¿______ alguna farmacia abierta a esta hora?', 'Hay',
              'Pregunta de existencia/disponibilidad → ¿HAY...?'),
             ('Lo siento, ______ billetes para ese vuelo.', 'no hay',
              'Negamos la existencia de billetes → NO HAY. Sin artículo después.'),
             ('El supermercado ______ al final de esta avenida, a la izquierda.', 'está',
              'Localizamos el supermercado (ya conocido, artículo definido «el») → ESTÁ.'),
             ('En el frigorífico ______ huevos, leche y queso.', 'hay',
              'Enumeramos lo que existe/disponemos → HAY.'),
         ]),
    ex3=('HAY en situaciones reales', 'Elige la oración correcta según el contexto.',
         [
             ('Quieres saber si existe una farmacia en tu calle. Preguntas:',
              ['¿Hay una farmacia en esta calle?', '¿Está la farmacia en esta calle?', '¿Es una farmacia aquí?'],
              '¿Hay una farmacia en esta calle?',
              'Preguntamos si existe → ¿Hay una...? Con ESTAR preguntaríamos por la ubicación de una farmacia ya conocida.'),
             ('El aeropuerto es un lugar conocido y preguntas dónde está:',
              ['¿Dónde está el aeropuerto?', '¿Dónde hay el aeropuerto?', '¿Dónde es el aeropuerto?'],
              '¿Dónde está el aeropuerto?',
              'Localizamos algo conocido (artículo definido «el aeropuerto») → ESTÁ.'),
             ('En la nevera no tienes nada. Dices:',
              ['No hay nada en la nevera.', 'La nevera no está nada.', 'Hay nada en la nevera.'],
              'No hay nada en la nevera.',
              'Negamos la existencia → NO HAY. La combinación «no hay nada» es muy natural en español.'),
             ('Describes tu barrio a un amigo. Dices que tiene un parque, dos colegios y una piscina:',
              ['Hay un parque, dos colegios y una piscina.', 'Están un parque, dos colegios y una piscina.', 'Son un parque, dos colegios y una piscina.'],
              'Hay un parque, dos colegios y una piscina.',
              'Presentamos la existencia de esas instalaciones → HAY.'),
             ('Tu amigo pregunta si hay wifi en el café. Contestas que sí:',
              ['Sí, hay wifi.', 'Sí, está wifi.', 'Sí, es wifi.'], 'Sí, hay wifi.',
              'Confirmamos la existencia → SÍ, HAY.'),
         ]),
    game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
    items=[
        ('hay-existe', 'hay', 'indica que algo existe o está presente', 'existe / se encuentra',
         '<b>Hay</b> un parque muy bonito cerca de mi casa.',
         '______ una farmacia en esta calle.', 'Hay'),
        ('hay-plural', 'hay (plural)', 'forma invariable: igual para uno o varios', 'there are',
         '<b>Hay</b> muchos estudiantes en la biblioteca.',
         '______ tres cafeterías en este edificio.', 'Hay'),
        ('no-hay', 'no hay', 'forma negativa para negar la existencia', 'no existe',
         '<b>No hay</b> leche en la nevera.',
         '______ ______ pan. Tenemos que ir a la panadería.', 'no hay'),
        ('hay-pregunta', '¿Hay...?', 'forma interrogativa para preguntar si algo existe', '¿existe...?',
         '¿<b>Hay</b> un médico de guardia?',
         '¿______ una estación de metro cerca de aquí?', 'Hay'),
        ('hay-vs-esta', 'hay vs. está', 'hay = existencia nueva; está = ubicación de algo conocido', 'there is vs. it is',
         '<b>Hay</b> un hotel. El hotel <b>está</b> en la plaza.',
         'El supermercado ______ al final de la calle. (ubicación conocida)', 'está'),
        ('hay-indefinido', 'hay + un/una', 'hay siempre lleva artículo indefinido o numeral, no definido', 'hay un / hay una',
         '<b>Hay una</b> tienda de ropa muy bonita aquí.',
         '______ ______ banco cerca de la estación.', 'Hay un'),
        ('hay-mucho', 'hay mucho/mucha', 'hay + mucho/mucha + sustantivo para cantidades', 'hay bastante',
         '<b>Hay mucha</b> gente en el mercado hoy.',
         '______ ______ tráfico a esta hora.', 'Hay mucho'),
        ('no-hay-sin', 'no hay + sustantivo sin artículo', 'tras no hay el sustantivo va sin artículo', 'no queda',
         '<b>No hay</b> tiempo para descansar.',
         '______ ______ habitaciones libres esta noche.', 'no hay'),
    ],
),

# ─────────────────────────────────────────────────────────────────────────────
# G08  VERBOS IRREGULARES
# ─────────────────────────────────────────────────────────────────────────────
'presente-irregular': dict(
    level='a1',
    section='grammar',
    num='G08',
    short='Verbos irregulares comunes',
    title='Verbos irregulares comunes — Presente de indicativo',
    subtitle='Las conjugaciones de ir, querer, poder, venir y tener en el presente.',
    slides=[
        ('Tipos de irregularidad en el presente', None,
         '<p class="slide-explanation">En español existen dos grandes grupos de verbos irregulares '
         'en el presente de indicativo: los verbos con <b>cambio vocálico en la raíz</b> '
         '(e → ie, e → i, o → ue) y los llamados verbos <b>go</b>, '
         'que tienen una <b>-g-</b> especial en la primera persona (yo).</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Cambio e → ie:</b> querer (e → ie), venir (e → ie)</p>'
         '<p style="margin-top:8px"><b>Cambio e → i:</b> pedir (e → i), decir (e → i + -g-)</p>'
         '<p style="margin-top:8px"><b>Cambio o → ue:</b> poder (o → ue)</p>'
         '<p style="margin-top:8px"><b>Verbos -go:</b> tener (tengo), venir (vengo), ir (voy)</p>'
         '</div>'
         '<p style="margin-top:14px">La irregularidad solo afecta a las personas con raíz tónica '
         '(yo, tú, él/ella, ellos/ellas). Nosotros y vosotros son regulares.</p>'),

        ('IR — el verbo más irregular', None,
         '<p class="slide-explanation">El verbo <b>ir</b> es completamente irregular: '
         'sus formas no tienen ninguna relación con el infinitivo. '
         'Hay que memorizarlo. Es fundamental para expresar movimiento y para el futuro próximo.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<table style="width:100%;border-collapse:collapse">'
         '<tr><th style="text-align:left;padding:5px 10px">Pronombre</th>'
         '<th style="text-align:left;padding:5px 10px">Forma</th></tr>'
         '<tr><td style="padding:5px 10px">yo</td><td style="padding:5px 10px"><b>voy</b></td></tr>'
         '<tr><td style="padding:5px 10px">tú</td><td style="padding:5px 10px"><b>vas</b></td></tr>'
         '<tr><td style="padding:5px 10px">él / ella / usted</td><td style="padding:5px 10px"><b>va</b></td></tr>'
         '<tr><td style="padding:5px 10px">nosotros/as</td><td style="padding:5px 10px"><b>vamos</b></td></tr>'
         '<tr><td style="padding:5px 10px">vosotros/as</td><td style="padding:5px 10px"><b>vais</b></td></tr>'
         '<tr><td style="padding:5px 10px">ellos / ellas / ustedes</td><td style="padding:5px 10px"><b>van</b></td></tr>'
         '</table></div>'
         '<p style="margin-top:10px"><b>Voy al trabajo en metro. ¿Vas tú en bici? Ella va a Madrid mañana.</b></p>'),

        ('QUERER y PODER — cambio e → ie y o → ue', None,
         '<p class="slide-explanation"><b>Querer</b> (to want/love) cambia la <b>e</b> de la raíz '
         'en <b>ie</b> en las formas tónicas. '
         '<b>Poder</b> (to be able to / can) cambia la <b>o</b> en <b>ue</b>. '
         'Nosotros y vosotros conservan la vocal original.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<table style="width:100%;border-collapse:collapse">'
         '<tr><th style="padding:5px 10px">Pronombre</th>'
         '<th style="padding:5px 10px">querer</th>'
         '<th style="padding:5px 10px">poder</th></tr>'
         '<tr><td style="padding:5px 10px">yo</td>'
         '<td style="padding:5px 10px"><b>quiero</b></td>'
         '<td style="padding:5px 10px"><b>puedo</b></td></tr>'
         '<tr><td style="padding:5px 10px">tú</td>'
         '<td style="padding:5px 10px"><b>quieres</b></td>'
         '<td style="padding:5px 10px"><b>puedes</b></td></tr>'
         '<tr><td style="padding:5px 10px">él/ella</td>'
         '<td style="padding:5px 10px"><b>quiere</b></td>'
         '<td style="padding:5px 10px"><b>puede</b></td></tr>'
         '<tr><td style="padding:5px 10px">nosotros</td>'
         '<td style="padding:5px 10px"><b>queremos</b></td>'
         '<td style="padding:5px 10px"><b>podemos</b></td></tr>'
         '<tr><td style="padding:5px 10px">vosotros</td>'
         '<td style="padding:5px 10px"><b>queréis</b></td>'
         '<td style="padding:5px 10px"><b>podéis</b></td></tr>'
         '<tr><td style="padding:5px 10px">ellos/ellas</td>'
         '<td style="padding:5px 10px"><b>quieren</b></td>'
         '<td style="padding:5px 10px"><b>pueden</b></td></tr>'
         '</table></div>'),

        ('VENIR — cambio e → ie + verbo -go', None,
         '<p class="slide-explanation"><b>Venir</b> (to come) combina dos irregularidades: '
         'la primera persona tiene <b>-g-</b> (vengo), '
         'y las demás personas tónicas tienen el diptongo <b>ie</b>.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<table style="width:100%;border-collapse:collapse">'
         '<tr><th style="text-align:left;padding:5px 10px">Pronombre</th>'
         '<th style="text-align:left;padding:5px 10px">Forma</th></tr>'
         '<tr><td style="padding:5px 10px">yo</td><td style="padding:5px 10px"><b>vengo</b></td></tr>'
         '<tr><td style="padding:5px 10px">tú</td><td style="padding:5px 10px"><b>vienes</b></td></tr>'
         '<tr><td style="padding:5px 10px">él / ella</td><td style="padding:5px 10px"><b>viene</b></td></tr>'
         '<tr><td style="padding:5px 10px">nosotros</td><td style="padding:5px 10px"><b>venimos</b></td></tr>'
         '<tr><td style="padding:5px 10px">vosotros</td><td style="padding:5px 10px"><b>venís</b></td></tr>'
         '<tr><td style="padding:5px 10px">ellos / ellas</td><td style="padding:5px 10px"><b>vienen</b></td></tr>'
         '</table></div>'
         '<p style="margin-top:10px"><b>¿De dónde vienes? — Vengo del trabajo. Ella viene mañana.</b></p>'),

        ('Irregulares en contexto: ejemplos clave', None,
         '<p class="slide-explanation">Practiquemos los cinco verbos juntos en situaciones reales. '
         'Fíjate en la irregularidad de cada forma.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Voy</b> al supermercado. ¿<b>Quieres</b> algo?</p>'
         '<p style="margin-top:8px">No <b>puedo</b> salir esta noche; <b>tengo</b> mucho trabajo.</p>'
         '<p style="margin-top:8px">¿<b>Vienes</b> a la fiesta? — Sí, <b>vengo</b> a las nueve.</p>'
         '<p style="margin-top:8px">Ellos <b>quieren</b> aprender español y <b>van</b> a una academia.</p>'
         '</div>'
         '<p style="margin-top:14px">Consejo: practica las formas de yo (voy, quiero, puedo, vengo, tengo) '
         'porque son las más irregulares y las más frecuentes en conversación.</p>'),
    ],
    traps=[
        ('Yo vo al cine.', 'Yo <strong>voy</strong> al cine.',
         'IR es completamente irregular. La forma de yo es «voy», sin ninguna relación con el infinitivo «ir».'),
        ('Ella quere un café.', 'Ella <strong>quiere</strong> un café.',
         'QUERER tiene cambio e → ie en las formas tónicas: qu-ie-re. La e de la raíz se convierte en ie.'),
        ('Nosotros queremos / podemos son regulares, pero yo querero.', 'Yo <strong>quiero</strong>.',
         'La primera persona de querer es «quiero» (e → ie), no «querero» ni «quero». Ojo con la irregularidad.'),
        ('Yo veno del trabajo.', 'Yo <strong>vengo</strong> del trabajo.',
         'VENIR tiene -g- en la primera persona: vengo. Es un verbo -go, como tener (tengo).'),
        ('Ellos pueden ir, pero él pueda ir.', 'Él <strong>puede</strong> ir.',
         'La forma de él/ella con PODER es «puede» (o → ue). No existe «pueda» en el presente indicativo.'),
    ],
    summary=[
        ('IR (irregular total)', 'voy · vas · va · vamos · vais · van', 'Voy al trabajo en metro.'),
        ('QUERER (e → ie)', 'quiero · quieres · quiere · queremos · queréis · quieren', 'Quiero un café, por favor.'),
        ('PODER (o → ue)', 'puedo · puedes · puede · podemos · podéis · pueden', '¿Puedes ayudarme?'),
        ('VENIR (-go + e → ie)', 'vengo · vienes · viene · venimos · venís · vienen', 'Vengo del gimnasio.'),
        ('TENER (-go + e → ie)', 'tengo · tienes · tiene · tenemos · tenéis · tienen', 'Tengo mucho trabajo.'),
        ('Nosotros / vosotros', 'siempre regulares (sin diptongo)', 'Podemos ir. Queréis descansar.'),
    ],
    ex1=('Elige la forma correcta del verbo', 'Selecciona la conjugación adecuada en presente de indicativo.',
         [
             ('Yo ______ al gimnasio todos los días.',
              ['voy', 'vo', 'vayo'], 'voy',
              'IR → yo = voy. Es totalmente irregular; no existe «vo» ni «vayo».'),
             ('¿Tú ______ venir a la fiesta del sábado?',
              ['puedes', 'puede', 'podes'], 'puedes',
              'PODER (o → ue) → tú = puedes. No existe «podes» en español estándar.'),
             ('Mi hermana ______ aprender a tocar la guitarra.',
              ['quiere', 'quere', 'querece'], 'quiere',
              'QUERER (e → ie) → ella = quiere. La raíz cambia a «quier-».'),
             ('Nosotros ______ al centro en autobús.',
              ['vamos', 'vamos', 'vayamos'], 'vamos',
              'IR → nosotros = vamos. Esta forma es regular dentro del paradigma de ir.'),
             ('¿De dónde ______ vosotros esta mañana?',
              ['venís', 'venis', 'venéis'], 'venís',
              'VENIR → vosotros = venís (con tilde en la í). Forma regular en el vosotros.'),
             ('Los estudiantes no ______ estudiar sin Internet.',
              ['pueden', 'puenden', 'poduen'], 'pueden',
              'PODER (o → ue) → ellos = pueden. La raíz cambia a «pued-».'),
         ]),
    ex2=('Escribe la forma correcta del verbo', 'Conjuga el verbo indicado entre paréntesis.',
         [
             ('Yo ______ mucho frío; ¿______ cerrar la ventana? (tener / poder — yo / tú)', 'tengo / puedes',
              'TENER yo → tengo (-go irregular). PODER tú → puedes (o → ue).'),
             ('¿Adónde ______ tú esta tarde? (ir)', 'vas',
              'IR tú → vas. Completamente irregular.'),
             ('Ellos ______ visitar Madrid en verano. (querer)', 'quieren',
              'QUERER ellos → quieren (e → ie en la raíz).'),
             ('¿A qué hora ______ tú al trabajo normalmente? (venir)', 'vienes',
              'VENIR tú → vienes (e → ie en la raíz, sin -g- porque no es yo).'),
             ('Nosotros no ______ salir tarde; mañana trabajamos. (poder)', 'podemos',
              'PODER nosotros → podemos. Nosotros no tiene cambio vocálico (forma regular).'),
         ]),
    ex3=('Irregulares en contexto', 'Elige la forma correcta del verbo según el contexto.',
         [
             ('¡Hola, Carla! ¿De dónde ______ hoy?',
              ['vienes', 'venes', 'viene'], 'vienes',
              'VENIR tú → vienes (e → ie). Pregunta con «tú» en contexto informal.'),
             ('Mi jefe no ______ trabajar el fin de semana.',
              ['quiere', 'quere', 'querece'], 'quiere',
              'QUERER él → quiere (e → ie). Sujeto = mi jefe = él.'),
             ('¿______ vosotros al mercado esta mañana?',
              ['Vais', 'Voís', 'Ís'], 'Vais',
              'IR vosotros → vais. Forma regular dentro del paradigma irregular de ir.'),
             ('Ellas no ______ hacer deporte porque están cansadas.',
              ['pueden', 'puenden', 'poduen'], 'pueden',
              'PODER ellas → pueden (o → ue en la raíz).'),
             ('Yo ______ del aeropuerto ahora mismo. ¿______ (tú) recogerme? (venir / poder)',
              ['vengo / puedes', 'veno / podes', 'vengo / puede'], 'vengo / puedes',
              'VENIR yo → vengo (-go). PODER tú → puedes (o → ue).'),
         ]),
    game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
    items=[
        ('irr-voy', 'voy', 'primera persona singular de IR', 'yo voy',
         'Todos los días <b>voy</b> al trabajo en metro.',
         'Yo ______ al supermercado ahora.', 'voy'),
        ('irr-vas', 'vas / va / van', 'formas de IR para tú, él/ella, ellos/ellas', 'tú vas',
         '¿<b>Vas</b> al gimnasio esta tarde?',
         '¿Adónde ______ tú esta tarde?', 'vas'),
        ('irr-quiero', 'quiero', 'primera persona de QUERER (e → ie)', 'yo quiero',
         '<b>Quiero</b> un vaso de agua, por favor.',
         'Yo ______ aprender a cocinar.', 'quiero'),
        ('irr-puede', 'puede', 'tercera persona de PODER (o → ue)', 'él/ella puede',
         'Mi amigo no <b>puede</b> venir hoy.',
         'Ella no ______ salir esta noche.', 'puede'),
        ('irr-vengo', 'vengo', 'primera persona de VENIR (-go + e → ie)', 'yo vengo',
         '<b>Vengo</b> del trabajo ahora mismo.',
         'Yo ______ del aeropuerto. ¿Me recoges?', 'vengo'),
        ('irr-vienes', 'vienes', 'segunda persona de VENIR (e → ie)', 'tú vienes',
         '¿<b>Vienes</b> a la fiesta esta noche?',
         '¿______ tú a cenar con nosotros?', 'vienes'),
        ('irr-podemos', 'podemos', 'primera persona plural de PODER (sin cambio)', 'nosotros podemos',
         'No <b>podemos</b> salir; está lloviendo.',
         'Nosotros no ______ comprar ese coche ahora.', 'podemos'),
        ('irr-quieren', 'quieren', 'tercera persona plural de QUERER (e → ie)', 'ellos quieren',
         'Ellos <b>quieren</b> ir a la playa en verano.',
         'Mis padres ______ visitar Roma.', 'quieren'),
    ],
),

# ─────────────────────────────────────────────────────────────────────────────
# G09  ADJETIVOS
# ─────────────────────────────────────────────────────────────────────────────
'adjetivos': dict(
    level='a1',
    section='grammar',
    num='G09',
    short='Los adjetivos',
    title='Los adjetivos — Concordancia y posición',
    subtitle='Cómo cambiar el adjetivo según el género y número del sustantivo, y dónde colocarlo.',
    slides=[
        ('¿Qué es un adjetivo?', None,
         '<p class="slide-explanation">Un <b>adjetivo</b> describe o califica a un sustantivo. '
         'En español los adjetivos <b>concuerdan</b> con el sustantivo al que acompañan '
         'en <b>género</b> (masculino / femenino) y <b>número</b> (singular / plural). '
         'Esto es diferente del inglés, donde los adjetivos no cambian.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p>Masculino singular: <b>un chico alto</b></p>'
         '<p style="margin-top:8px">Femenino singular: <b>una chica alta</b></p>'
         '<p style="margin-top:8px">Masculino plural: <b>unos chicos altos</b></p>'
         '<p style="margin-top:8px">Femenino plural: <b>unas chicas altas</b></p>'
         '</div>'
         '<p style="margin-top:14px">La concordancia es obligatoria: decir «una chica alto» '
         'es un error gramatical grave.</p>'),

        ('Concordancia: masculino y femenino', None,
         '<p class="slide-explanation">La mayoría de los adjetivos terminan en <b>-o</b> '
         'en masculino y cambian a <b>-a</b> en femenino. '
         'Pero algunos adjetivos tienen una sola forma para los dos géneros '
         '(los terminados en -e, -ista, o consonante).</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<table style="width:100%;border-collapse:collapse">'
         '<tr><th style="padding:5px 10px">Tipo</th>'
         '<th style="padding:5px 10px">Masculino</th>'
         '<th style="padding:5px 10px">Femenino</th></tr>'
         '<tr><td style="padding:5px 10px">terminan en -o / -a</td>'
         '<td style="padding:5px 10px"><b>alto</b></td>'
         '<td style="padding:5px 10px"><b>alta</b></td></tr>'
         '<tr><td style="padding:5px 10px">terminan en -e (invariable)</td>'
         '<td style="padding:5px 10px"><b>inteligente</b></td>'
         '<td style="padding:5px 10px"><b>inteligente</b></td></tr>'
         '<tr><td style="padding:5px 10px">terminan en consonante (invariable)</td>'
         '<td style="padding:5px 10px"><b>joven</b></td>'
         '<td style="padding:5px 10px"><b>joven</b></td></tr>'
         '</table></div>'
         '<p style="margin-top:10px"><b>Mi hermano es guapo. Mi hermana es guapa.</b></p>'
         '<p style="margin-top:6px"><b>Mi padre es inteligente. Mi madre también es inteligente.</b></p>'),

        ('Concordancia: singular y plural', None,
         '<p class="slide-explanation">Para el plural, los adjetivos siguen las mismas reglas '
         'que los sustantivos: se añade <b>-s</b> si terminan en vocal '
         'y <b>-es</b> si terminan en consonante.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<table style="width:100%;border-collapse:collapse">'
         '<tr><th style="padding:5px 10px">Singular</th>'
         '<th style="padding:5px 10px">Plural</th></tr>'
         '<tr><td style="padding:5px 10px"><b>un libro nuevo</b></td>'
         '<td style="padding:5px 10px"><b>unos libros nuevos</b></td></tr>'
         '<tr><td style="padding:5px 10px"><b>una ciudad grande</b></td>'
         '<td style="padding:5px 10px"><b>unas ciudades grandes</b></td></tr>'
         '<tr><td style="padding:5px 10px"><b>un estudiante joven</b></td>'
         '<td style="padding:5px 10px"><b>unos estudiantes jóvenes</b></td></tr>'
         '</table></div>'
         '<p style="margin-top:10px">Atención: <b>joven → jóvenes</b> (se añade tilde para mantener el acento).</p>'),

        ('Posición del adjetivo: después del sustantivo', None,
         '<p class="slide-explanation">En español la posición normal del adjetivo calificativo '
         'es <b>después del sustantivo</b>. Esto es lo contrario del inglés, '
         'donde el adjetivo va delante. Algunos adjetivos pueden ir delante, '
         'pero para el nivel A1 es más seguro ponerlos detrás.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>una casa grande</b> (a big house)</p>'
         '<p style="margin-top:8px"><b>un chico simpático</b> (a nice boy)</p>'
         '<p style="margin-top:8px"><b>una película interesante</b> (an interesting film)</p>'
         '<p style="margin-top:8px"><b>unos zapatos negros</b> (some black shoes)</p>'
         '</div>'
         '<p style="margin-top:14px">Excepción: los adjetivos cuantitativos y de valor '
         '(<i>mucho, poco, bueno, malo, grande</i> con significado especial) '
         'pueden ir delante, pero eso lo estudiarás más adelante.</p>'),

        ('Adjetivos con SER: describir características', None,
         '<p class="slide-explanation">Los adjetivos calificativos descriptivos '
         '(tamaño, color, personalidad, nacionalidad, forma) '
         'se usan siempre con el verbo <b>ser</b>. '
         'Recuerda que el adjetivo debe concordar con el sujeto.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Mi profesora es muy simpática y trabajadora.</b></p>'
         '<p style="margin-top:8px"><b>El edificio es antiguo y muy bonito.</b></p>'
         '<p style="margin-top:8px"><b>¿Cómo son tus hermanos? Son altos y rubios.</b></p>'
         '<p style="margin-top:8px"><b>Las calles de este barrio son estrechas y tranquilas.</b></p>'
         '</div>'
         '<p style="margin-top:14px">Aunque los adjetivos pueden ir detrás del sustantivo '
         '(un chico simpático) o con ser (el chico es simpático), '
         'el significado es prácticamente el mismo.</p>'),
    ],
    traps=[
        ('un chica guapo', 'una chica <strong>guapa</strong>',
         'El artículo y el adjetivo deben concordar con el género del sustantivo. «Chica» es femenino → una / guapa.'),
        ('unos libros interesante', 'unos libros <strong>interesantes</strong>',
         'En plural, los adjetivos terminados en -e añaden -s: interesante → interesantes.'),
        ('una persona simpátic', 'una persona <strong>simpática</strong>',
         'Los adjetivos en -o forman el femenino en -a: simpático → simpática. No se elimina la vocal, solo se cambia.'),
        ('un grande problema', 'un <strong>problema grande</strong>',
         'En español, los adjetivos descriptivos van normalmente DESPUÉS del sustantivo: problema grande (no «grande problema» en este nivel).'),
        ('Mis padres son inteligentes y trabajadores.  — Mi madre es inteligente y trabajadora.', 'Mi madre es inteligente y <strong>trabajadora</strong>.',
         'Con sujeto femenino singular, todos los adjetivos deben ir en femenino: trabajadora, no trabajador.'),
    ],
    summary=[
        ('Masc. sing.', 'sustantivo + adjetivo en -o', 'un chico alto · un coche rojo'),
        ('Fem. sing.', 'sustantivo + adjetivo en -a', 'una chica alta · una casa bonita'),
        ('Masc. pl.', 'sustantivos + adjetivo en -os', 'unos chicos altos · unos coches rojos'),
        ('Fem. pl.', 'sustantivos + adjetivo en -as', 'unas chicas altas · unas casas bonitas'),
        ('Invariables (-e, consonante)', 'misma forma M/F', 'un chico / una chica inteligente · joven'),
        ('Posición', 'normalmente después del sustantivo', 'una película interesante · un coche azul'),
    ],
    ex1=('Elige el adjetivo correcto', 'Selecciona la forma que concuerda con el sustantivo.',
         [
             ('Mi hermana es muy ______.',
              ['simpática', 'simpático', 'simpáticos'], 'simpática',
              'Hermana es femenino singular → el adjetivo también debe ser femenino singular: simpática.'),
             ('Tengo dos perros muy ______.',
              ['grandes', 'grande', 'granda'], 'grandes',
              'Perros es masculino plural → el adjetivo va en plural: grandes. «Grande» no cambia de género pero sí añade -s en plural.'),
             ('El apartamento es pequeño pero ______.',
              ['cómodo', 'cómoda', 'cómodos'], 'cómodo',
              'Apartamento es masculino singular → cómodo (masculino singular).'),
             ('Las calles de esta ciudad son muy ______.',
              ['tranquilas', 'tranquilo', 'tranquila'], 'tranquilas',
              'Calles es femenino plural → tranquilas (femenino plural).'),
             ('Mi vecino es un hombre muy ______.',
              ['trabajador', 'trabajadora', 'trabajadores'], 'trabajador',
              'Hombre es masculino singular. Trabajador termina en consonante, pero sí tiene femenino: trabajadora. Aquí masculino → trabajador.'),
             ('Tengo una mochila ______.',
              ['azul', 'azula', 'azules'], 'azul',
              'Los adjetivos de color terminados en consonante (azul, gris) son invariables en género. En singular: azul.'),
         ]),
    ex2=('Escribe el adjetivo en la forma correcta', 'Cambia el adjetivo para que concuerde con el sustantivo.',
         [
             ('Mi ciudad es muy (bonito) ______. (femenino singular)', 'bonita',
              'Ciudad es femenino → bonito cambia a bonita.'),
             ('Los exámenes de matemáticas son muy (difícil) ______. (masculino plural)', 'difíciles',
              'Difícil termina en consonante → añade -es en plural: difíciles.'),
             ('Tengo una habitación (ordenado) ______ y (luminoso) ______. (femenino singular x2)', 'ordenada / luminosa',
              'Habitación es femenino → ordenado → ordenada; luminoso → luminosa.'),
             ('Mis amigas son muy (inteligente) ______ y (divertido) ______. (femenino plural x2)', 'inteligentes / divertidas',
              'Inteligente es invariable en género, solo añade -s: inteligentes. Divertido → femenino plural: divertidas.'),
             ('El profesor tiene un estilo (moderno) ______ y (original) ______. (masculino singular x2)', 'moderno / original',
              'Moderno ya es masculino singular: moderno. Original termina en consonante: invariable en género, singular: original.'),
         ]),
    ex3=('Adjetivos en contexto', 'Elige la oración correcta.',
         [
             ('¿Cómo es tu casa? Quieres decir que es acogedora y espaciosa:',
              ['Mi casa es acogedora y espaciosa.', 'Mi casa es acogedor y espacioso.', 'Mi casa son acogedora y espaciosa.'],
              'Mi casa es acogedora y espaciosa.',
              'Casa es femenino singular → todos los adjetivos en femenino singular: acogedora, espaciosa.'),
             ('Describes a dos chicos: son simpáticos y trabajadores:',
              ['Son simpáticos y trabajadores.', 'Son simpáticas y trabajadoras.', 'Son simpático y trabajador.'],
              'Son simpáticos y trabajadores.',
              'Dos chicos = masculino plural → simpáticos, trabajadores (ambos en masculino plural).'),
             ('Hablas de un libro que has leído. Era aburrido e interesante al mismo tiempo:',
              ['El libro era aburrido e interesante.', 'El libro era aburride e interesante.', 'El libro era aburrida e interesante.'],
              'El libro era aburrido e interesante.',
              'Libro es masculino singular → aburrido (masculino). Interesante es invariable en género.'),
             ('Señalas la posición correcta del adjetivo en español:',
              ['una película aburrida', 'una aburrida película', 'aburrida una película'],
              'una película aburrida',
              'En español los adjetivos calificativos van normalmente DESPUÉS del sustantivo: una película aburrida.'),
             ('Tu amiga es de España. ¿Cómo describes su origen?',
              ['Mi amiga es española.', 'Mi amiga es español.', 'Mi amiga es espanola.'],
              'Mi amiga es española.',
              'Amiga es femenino → español → española (añade -a). Recuerda escribir la tilde: española.'),
         ]),
    game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
    items=[
        ('adj-masc-sing', 'adjetivo masculino singular', 'termina en -o para la mayoría de adjetivos', '-o',
         'El chico es <b>alto</b> y <b>guapo</b>.',
         'El piso es modern____. (masculino singular)', 'moderno'),
        ('adj-fem-sing', 'adjetivo femenino singular', 'termina en -a para los adjetivos en -o/-a', '-a',
         'La chica es <b>alta</b> y <b>guapa</b>.',
         'La casa es modern____. (femenino singular)', 'moderna'),
        ('adj-masc-pl', 'adjetivo masculino plural', 'termina en -os para los adjetivos en -o/-a', '-os',
         'Los pisos son <b>modernos</b> y <b>luminosos</b>.',
         'Los coches son roj____. (masculino plural)', 'rojos'),
        ('adj-fem-pl', 'adjetivo femenino plural', 'termina en -as para los adjetivos en -o/-a', '-as',
         'Las sillas son <b>rojas</b> y <b>cómodas</b>.',
         'Las ciudades son bonit____. (femenino plural)', 'bonitas'),
        ('adj-invariable', 'adjetivo invariable', 'adjetivos en -e o consonante no cambian de género', 'igual para M y F',
         'El chico es <b>inteligente</b>. La chica también es <b>inteligente</b>.',
         'Mi hermano es jov____. Mi hermana también es jov____. (invariable)', 'joven'),
        ('adj-posicion', 'posición del adjetivo', 'en español el adjetivo va normalmente después del sustantivo', 'sustantivo + adjetivo',
         'Tengo una <b>mochila azul</b>.',
         'Tengo un coche ______. (nuevo — pon el adjetivo en la posición correcta)', 'nuevo'),
        ('adj-ser', 'ser + adjetivo', 'se usa ser para describir características permanentes', 'descripción con ser',
         'Mi profesora <b>es</b> simpática y trabajadora.',
         'El edificio ______ antiguo y bonito.', 'es'),
        ('adj-plural-cons', 'plural de adjetivos en consonante', 'añade -es si el adjetivo termina en consonante', '-es',
         'Los estudiantes son <b>jóvenes</b>.',
         'Los ejercicios son muy difíc____. (plural en consonante)', 'difíciles'),
    ],
),

# ─────────────────────────────────────────────────────────────────────────────
# G10  PREPOSICIONES
# ─────────────────────────────────────────────────────────────────────────────
'preposiciones': dict(
    level='a1',
    section='grammar',
    num='G10',
    short='Preposiciones básicas',
    title='Preposiciones básicas — En, de, a, con, por, para, entre',
    subtitle='Los usos esenciales de las preposiciones más frecuentes del español.',
    slides=[
        ('¿Qué son las preposiciones?', None,
         '<p class="slide-explanation">Las <b>preposiciones</b> son palabras cortas que indican '
         'relaciones entre las otras palabras: lugar, tiempo, dirección, causa, finalidad o compañía. '
         'En español no se pueden separar del sustantivo que introducen, '
         'al contrario del inglés («the person I talked to»).</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<table style="width:100%;border-collapse:collapse">'
         '<tr><th style="text-align:left;padding:5px 10px">Preposición</th>'
         '<th style="text-align:left;padding:5px 10px">Usos principales</th></tr>'
         '<tr><td style="padding:5px 10px"><b>en</b></td><td style="padding:5px 10px">lugar, medio de transporte, tiempo</td></tr>'
         '<tr><td style="padding:5px 10px"><b>de</b></td><td style="padding:5px 10px">origen, posesión, material, parte de</td></tr>'
         '<tr><td style="padding:5px 10px"><b>a</b></td><td style="padding:5px 10px">dirección, hora, objeto directo de persona</td></tr>'
         '<tr><td style="padding:5px 10px"><b>con</b></td><td style="padding:5px 10px">compañía, instrumento, modo</td></tr>'
         '<tr><td style="padding:5px 10px"><b>por</b></td><td style="padding:5px 10px">causa, duración, intercambio, lugar de paso</td></tr>'
         '<tr><td style="padding:5px 10px"><b>para</b></td><td style="padding:5px 10px">finalidad, destinatario, opinión, plazo</td></tr>'
         '<tr><td style="padding:5px 10px"><b>entre</b></td><td style="padding:5px 10px">posición entre dos elementos, colectivo</td></tr>'
         '</table></div>'),

        ('EN y DE: lugar, origen y posesión', None,
         '<p class="slide-explanation"><b>En</b> indica que algo está <b>dentro de</b> un lugar '
         'o que se realiza en él. <b>De</b> indica el <b>origen</b>, la <b>pertenencia</b> '
         'o el <b>material</b> de algo. La contracción <b>del</b> (de + el) es obligatoria.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Vivo en Madrid.</b> / <b>Hay leche en la nevera.</b></p>'
         '<p style="margin-top:8px"><b>Soy de España.</b> (origen)</p>'
         '<p style="margin-top:8px"><b>Es el libro de María.</b> (posesión)</p>'
         '<p style="margin-top:8px"><b>La mesa es de madera.</b> (material)</p>'
         '<p style="margin-top:8px"><b>Vengo del supermercado.</b> (de + el = del)</p>'
         '</div>'
         '<p style="margin-top:14px">Recuerda las contracciones obligatorias: '
         '<b>a + el = al</b> y <b>de + el = del</b>. '
         'No existen «a el» ni «de el» en español correcto.</p>'),

        ('A y CON: dirección, hora y compañía', None,
         '<p class="slide-explanation"><b>A</b> indica <b>dirección</b> («voy a la tienda»), '
         '<b>hora</b> («a las tres») y se usa antes del objeto directo de persona '
         '(la «a personal»: «veo a mi amiga»). '
         '<b>Con</b> indica <b>compañía</b> («voy con Ana») o el <b>instrumento</b> '
         'con que hacemos algo.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Voy al mercado.</b> (a + el = al; dirección)</p>'
         '<p style="margin-top:8px"><b>La clase empieza a las nueve.</b> (hora)</p>'
         '<p style="margin-top:8px"><b>Llamo a mi madre todos los días.</b> (a personal)</p>'
         '<p style="margin-top:8px"><b>Voy al cine con mis amigos.</b> (compañía)</p>'
         '<p style="margin-top:8px"><b>Escribo con un bolígrafo rojo.</b> (instrumento)</p>'
         '</div>'),

        ('POR y PARA: causa vs. finalidad', None,
         '<p class="slide-explanation"><b>Por</b> y <b>para</b> son la pareja más difícil para '
         'los estudiantes de español. La clave es: '
         '<b>por</b> mira hacia el <b>pasado o la causa</b>; '
         '<b>para</b> mira hacia el <b>futuro o el objetivo</b>.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<table style="width:100%;border-collapse:collapse">'
         '<tr><th style="padding:5px 10px">POR (causa, duración, intercambio)</th>'
         '<th style="padding:5px 10px">PARA (finalidad, destinatario, plazo)</th></tr>'
         '<tr><td style="padding:5px 10px"><b>Gracias por tu ayuda.</b> (causa)</td>'
         '<td style="padding:5px 10px"><b>Estudio para aprender.</b> (finalidad)</td></tr>'
         '<tr><td style="padding:5px 10px"><b>Estudio por las mañanas.</b> (tiempo)</td>'
         '<td style="padding:5px 10px"><b>Este regalo es para ti.</b> (destinatario)</td></tr>'
         '<tr><td style="padding:5px 10px"><b>Pagué diez euros por el libro.</b> (intercambio)</td>'
         '<td style="padding:5px 10px"><b>Lo necesito para mañana.</b> (plazo)</td></tr>'
         '</table></div>'),

        ('ENTRE y resumen general', None,
         '<p class="slide-explanation"><b>Entre</b> indica una posición o situación '
         '<b>en medio de</b> dos o más cosas o personas. '
         'También se usa para indicar que algo es la acción colectiva de un grupo.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>El banco está entre la farmacia y el supermercado.</b></p>'
         '<p style="margin-top:8px"><b>Entre todos preparamos la cena.</b> (todos juntos)</p>'
         '<p style="margin-top:8px"><b>Elige entre el café y el té.</b> (opción)</p>'
         '</div>'
         '<p style="margin-top:14px">Nota especial: después de <b>entre</b> se usan los '
         'pronombres <b>tú</b> y <b>yo</b>, no ti ni mí: '
         '<b>entre tú y yo</b> (no «entre ti y mí»).</p>'),
    ],
    traps=[
        ('Voy a el trabajo.', 'Voy <strong>al</strong> trabajo.',
         'A + el = AL (contracción obligatoria). No se puede decir «a el»; siempre «al».'),
        ('Vengo de el banco.', 'Vengo <strong>del</strong> banco.',
         'De + el = DEL (contracción obligatoria). Nunca «de el»; siempre «del».'),
        ('Estudio para hablar con los locales.', 'Estudio <strong>para</strong> hablar con los locales.',
         'Esta frase es CORRECTA. Para + infinitivo expresa finalidad. Es un error frecuente dudar de esta estructura.'),
        ('Gracias para tu ayuda.', 'Gracias <strong>por</strong> tu ayuda.',
         'Con «gracias», siempre usamos POR (causa del agradecimiento), nunca para. «Gracias por tu ayuda» es la expresión fija.'),
        ('El libro es de el profesor.', 'El libro es <strong>del</strong> profesor.',
         'De + el = DEL. La contracción es obligatoria excepto cuando el artículo forma parte de un nombre propio (Vengo de El Salvador).'),
    ],
    summary=[
        ('en', 'lugar / medio de transporte / tiempo parcial del día', 'Vivo en Madrid. Voy en metro. Estudio en verano.'),
        ('de', 'origen / posesión / material + de + el = del', 'Soy de México. El libro de Ana. La mesa es de madera.'),
        ('a', 'dirección / hora / a personal + a + el = al', 'Voy al trabajo. A las ocho. Llamo a mi madre.'),
        ('con', 'compañía / instrumento / modo', 'Voy con Ana. Escribo con el bolígrafo.'),
        ('por / para', 'por = causa / duración · para = finalidad / destinatario / plazo', 'Gracias por todo. Esto es para ti.'),
        ('entre', 'posición entre dos elementos / acción colectiva', 'Está entre la tienda y el banco. Entre tú y yo.'),
    ],
    ex1=('Elige la preposición correcta', 'Selecciona la preposición más adecuada para cada oración.',
         [
             ('Vivo ______ un barrio muy tranquilo ______ Madrid.',
              ['en / de', 'a / en', 'de / en'], 'en / de',
              'EN indica el lugar donde vivo (en un barrio); DE indica la ciudad a la que pertenece (de Madrid).'),
             ('Voy ______ trabajo en metro todos los días.',
              ['al', 'a el', 'del'], 'al',
              'A + el = AL (contracción obligatoria). Dirección: voy al trabajo.'),
             ('Este regalo es ______ mi madre.',
              ['para', 'por', 'de'], 'para',
              'PARA indica el destinatario del regalo.'),
             ('Gracias ______ todo lo que has hecho.',
              ['por', 'para', 'de'], 'por',
              'La expresión «gracias por» es fija en español. POR indica la causa del agradecimiento.'),
             ('El banco está ______ la farmacia y la zapatería.',
              ['entre', 'con', 'en'], 'entre',
              'ENTRE indica una posición en medio de dos puntos de referencia.'),
             ('Llamo ______ mi abuelo todos los domingos.',
              ['a', 'de', 'para'], 'a',
              'La «a personal» se usa antes del objeto directo de persona: llamo A mi abuelo.'),
         ]),
    ex2=('Escribe la preposición correcta', 'Completa con la preposición adecuada.',
         [
             ('Vengo ______ el supermercado. Tengo mucha comida. (de + el = ?)', 'del',
              'De + el = DEL (contracción obligatoria). Vengo DEL supermercado.'),
             ('La clase de español empieza ______ las diez de la mañana.', 'a',
              'La hora se expresa con A: a las diez. La preposición A introduce el momento exacto.'),
             ('Esta mochila es ______ cuero, no ______ plástico. (material x2)', 'de / de',
              'El material se expresa con DE: de cuero, de plástico.'),
             ('Normalmente estudio ______ las mañanas, no por las tardes.', 'por',
              'Las partes del día se expresan con POR: por las mañanas, por las tardes, por las noches.'),
             ('¿Quieres venir al parque ______ nosotros?', 'con',
              'La compañía se expresa con CON: venir CON nosotros.'),
         ]),
    ex3=('POR o PARA: el contraste clave', 'Elige la preposición correcta: por o para.',
         [
             ('Estudio español ______ hablar con la familia de mi novio.',
              ['para', 'por', 'de'], 'para',
              'Finalidad (para + infinitivo): estudio PARA hablar. El objetivo es aprender a comunicarse.'),
             ('Te llamo ______ preguntarte algo importante.',
              ['para', 'por', 'a'], 'para',
              'PARA + infinitivo expresa la finalidad de la acción: te llamo PARA preguntarte.'),
             ('Pagué veinte euros ______ esta camisa.',
              ['por', 'para', 'de'], 'por',
              'Intercambio económico → POR: pagué veinte euros POR la camisa.'),
             ('Necesito el informe ______ el lunes.',
              ['para', 'por', 'en'], 'para',
              'Plazo o fecha límite → PARA: lo necesito PARA el lunes.'),
             ('Muchas gracias ______ la información.',
              ['por', 'para', 'de'], 'por',
              'Causa del agradecimiento → «gracias POR». Esta expresión es fija: nunca «gracias para».'),
         ]),
    game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
    items=[
        ('prep-en', 'en', 'indica lugar, medio de transporte o parte del día', 'dentro de / en',
         'Vivo <b>en</b> Madrid y voy al trabajo <b>en</b> metro.',
         'Estudio ______ las mañanas.', 'por'),
        ('prep-de', 'de', 'indica origen, posesión o material', 'procedencia / pertenencia',
         'Soy <b>de</b> México. La mesa es <b>de</b> madera.',
         'Este libro es ______ la profesora.', 'de'),
        ('prep-al', 'al', 'contracción obligatoria: a + el = al', 'a + el',
         'Voy <b>al</b> mercado todos los sábados.',
         'Mi madre va ______ trabajo en autobús.', 'al'),
        ('prep-del', 'del', 'contracción obligatoria: de + el = del', 'de + el',
         'Vengo <b>del</b> gimnasio.',
         'Vengo ______ banco. Tengo el dinero.', 'del'),
        ('prep-para-fin', 'para (finalidad)', 'indica el objetivo o la finalidad de una acción', 'con el objetivo de',
         'Estudio <b>para</b> aprender español.',
         'Llamo a Ana ______ invitarla a la fiesta.', 'para'),
        ('prep-por-causa', 'por (causa)', 'indica la causa o el motivo de algo', 'a causa de',
         'Gracias <b>por</b> tu ayuda.',
         'Te doy las gracias ______ todo.', 'por'),
        ('prep-con', 'con', 'indica compañía o instrumento', 'acompañado de',
         'Voy al cine <b>con</b> mis amigos.',
         'Escribo ______ un bolígrafo azul.', 'con'),
        ('prep-entre', 'entre', 'indica posición en medio de dos elementos', 'en medio de',
         'El café está <b>entre</b> la panadería y la librería.',
         'La farmacia está ______ el banco y el supermercado.', 'entre'),
    ],
),

}
