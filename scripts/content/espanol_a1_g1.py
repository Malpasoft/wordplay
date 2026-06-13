# -*- coding: utf-8 -*-
"""espanol/ A1 Gramática — lote 1 (G01–G05)."""

CHAPTERS = {

'ser': dict(
  level='a1', section='grammar', num='G01',
  short='El Verbo SER',
  title='El Verbo SER — Identidad y Descripción',
  subtitle='Usa SER para hablar de identidad, origen, profesión y características permanentes',
  slides=[
    ('¿Qué es el verbo SER?', None,
     '<p class="slide-explanation">El verbo <b>SER</b> se usa para expresar características <b>permanentes o esenciales</b>: quién es alguien, de dónde es, qué profesión tiene y cómo es.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Yo soy estudiante.</b> (identidad / profesión)</p>'
     '<p style="margin-top:8px"><b>María es española.</b> (origen / nacionalidad)</p>'
     '<p style="margin-top:8px"><b>El coche es rojo.</b> (característica permanente)</p>'
     '</div>'
     '<p style="margin-top:16px">Recuerda: SER no se usa para hablar de ubicación ni de estados temporales — para eso existe ESTAR.</p>'),
    ('Conjugación de SER en presente', None,
     '<p class="slide-explanation">Aprende las formas del presente de indicativo de SER. ¡Es un verbo muy irregular!</p>'
     '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
     '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronombre</th><th style="padding:8px;text-align:left">Forma</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">yo</td><td style="padding:8px"><b>soy</b></td><td style="padding:8px">Yo soy médico.</td></tr>'
     '<tr><td style="padding:8px">tú</td><td style="padding:8px"><b>eres</b></td><td style="padding:8px">Tú eres muy simpático.</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">él/ella/usted</td><td style="padding:8px"><b>es</b></td><td style="padding:8px">Ella es de México.</td></tr>'
     '<tr><td style="padding:8px">nosotros/as</td><td style="padding:8px"><b>somos</b></td><td style="padding:8px">Nosotros somos profesores.</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">vosotros/as</td><td style="padding:8px"><b>sois</b></td><td style="padding:8px">Vosotros sois amigos.</td></tr>'
     '<tr><td style="padding:8px">ellos/ustedes</td><td style="padding:8px"><b>son</b></td><td style="padding:8px">Ellos son estudiantes.</td></tr>'
     '</table>'),
    ('Usos principales de SER', 'Cuándo usar SER',
     '<p class="slide-explanation">SER se usa en estos contextos clave:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Profesión:</b> Mi padre es ingeniero. Ana es actriz.</p>'
     '<p style="margin-top:8px"><b>Origen / nacionalidad:</b> Soy de Argentina. Son franceses.</p>'
     '<p style="margin-top:8px"><b>Descripción física / personalidad:</b> Carlos es alto y moreno. Eres muy inteligente.</p>'
     '<p style="margin-top:8px"><b>Relaciones:</b> Elena es mi hermana. Somos amigos.</p>'
     '<p style="margin-top:8px"><b>Material / identidad:</b> La mesa es de madera. Este es mi libro.</p>'
     '</div>'),
    ('SER con adjetivos de descripción', None,
     '<p class="slide-explanation">Cuando SER va seguido de un adjetivo, el adjetivo <b>concuerda en género y número</b> con el sujeto.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>masculino singular:</b> El chico es alto.</p>'
     '<p style="margin-top:8px"><b>femenino singular:</b> La chica es alta.</p>'
     '<p style="margin-top:8px"><b>masculino plural:</b> Los chicos son altos.</p>'
     '<p style="margin-top:8px"><b>femenino plural:</b> Las chicas son altas.</p>'
     '</div>'
     '<p style="margin-top:16px">Los adjetivos como <b>inteligente, joven, optimista</b> tienen la misma forma para masculino y femenino.</p>'),
  ],
  traps=[
    ('Yo so estudiante.', 'Yo <strong>soy</strong> estudiante.', 'La primera persona singular de SER es "soy", no "so".'),
    ('Ella es en Madrid.', 'Ella <strong>está</strong> en Madrid.', 'SER no se usa para ubicación. Usa ESTAR + en para indicar dónde está alguien.'),
    ('Somos cansados.', '<strong>Estamos</strong> cansados.', 'Los estados temporales (cansado, enfermo, triste) usan ESTAR, no SER.'),
    ('Carlos es médico muy bueno.', 'Carlos es un médico muy bueno.', 'Cuando el sustantivo va calificado por un adjetivo, necesita el artículo indefinido.'),
    ('Ellos es simpáticos.', 'Ellos <strong>son</strong> simpáticos.', 'Con sujeto plural (ellos/ellas/ustedes) la forma es "son", no "es".'),
  ],
  summary=[
    ('yo', 'soy', 'Yo soy español.'),
    ('tú', 'eres', 'Tú eres muy amable.'),
    ('él / ella / usted', 'es', 'Ella es profesora.'),
    ('nosotros/as', 'somos', 'Somos estudiantes.'),
    ('vosotros/as', 'sois', 'Vosotros sois de Madrid.'),
    ('ellos / ellas / ustedes', 'son', 'Son muy inteligentes.'),
  ],
  ex1=('Elige la forma correcta de SER', 'Selecciona la forma adecuada de SER para cada oración.',
    [('Mi madre ______ doctora.', ['es', 'eres', 'soy'], 'es', 'Con "mi madre" (tercera persona singular), la forma correcta es "es".'),
     ('¿De dónde ______ tú?', ['eres', 'soy', 'es'], 'eres', 'Con el pronombre "tú", la forma correcta de SER es "eres".'),
     ('Nosotros ______ de Colombia.', ['somos', 'sois', 'son'], 'somos', 'Con "nosotros", la forma de SER en presente es "somos".'),
     ('Los estudiantes ______ muy trabajadores.', ['son', 'somos', 'es'], 'son', 'Con un sujeto plural (los estudiantes), usamos "son".'),
     ('Vosotros ______ mis mejores amigos.', ['sois', 'son', 'somos'], 'sois', 'Con "vosotros", la forma de SER es "sois".'),
     ('Yo ______ ingeniero.', ['soy', 'es', 'eres'], 'soy', 'La primera persona singular del presente de SER es "soy".'),
    ]),
  ex2=('Conjuga el verbo SER', 'Escribe la forma correcta de SER para cada oración.',
    [('Ella ______ muy simpática. (SER)', 'es', '"Ella" es tercera persona singular, por eso la forma es "es".'),
     ('¿Tú ______ de Perú? (SER)', 'eres', '"Tú" requiere la forma "eres" de SER.'),
     ('Nosotros ______ profesores. (SER)', 'somos', '"Nosotros" requiere "somos".'),
     ('Los chicos ______ altos. (SER)', 'son', 'Sujeto plural tercera persona: "son".'),
     ('Yo ______ estudiante de español. (SER)', 'soy', 'Primera persona singular: "soy".'),
    ]),
  ex3=('SER para describir: ¿correcto o incorrecto?', 'Elige la oración correcta.',
    [('¿Cuál oración es correcta?',
      ['Ana es de Madrid.', 'Ana está de Madrid.', 'Ana soy de Madrid.'],
      'Ana es de Madrid.',
      'Para el origen usamos SER. La forma correcta para "ella" es "es".'),
     ('¿Qué describe el verbo SER?',
      ['Una ubicación temporal', 'Una característica permanente', 'Un estado de ánimo'],
      'Una característica permanente',
      'SER expresa características permanentes como identidad, origen o profesión.'),
     ('Carlos ______ médico. ¿Qué forma va?',
      ['es', 'está', 'hay'],
      'es',
      'Para expresar la profesión usamos SER. Con "Carlos" (él), la forma es "es".'),
     ('¿Cuál oración usa SER correctamente?',
      ['Somos cansados.', 'Somos estudiantes.', 'Somos en casa.'],
      'Somos estudiantes.',
      '"Somos estudiantes" es correcto — profesión/identidad usa SER. "Cansados" usa ESTAR y ubicación también usa ESTAR.'),
     ('Mi hermana ______ alta y rubia. ¿Qué verbo?',
      ['es', 'está', 'tiene'],
      'es',
      'Las características físicas permanentes usan SER.'),
    ]),
  game_desc='4 conceptos clave sobre SER · 3 rondas cada uno · llega a 100 puntos para ganar.',
  items=[
    ('soy', 'soy', 'primera persona singular de SER', 'yo soy', 'Yo soy estudiante de español.', 'Yo ______ de Argentina.', 'soy'),
    ('eres', 'eres', 'segunda persona singular de SER (tú)', 'tú eres', '¿Tú eres de España?', 'Tú ______ muy amable.', 'eres'),
    ('es', 'es', 'tercera persona singular de SER (él/ella)', 'él/ella es', 'María es profesora.', 'Mi amigo ______ ingeniero.', 'es'),
    ('somos', 'somos', 'primera persona plural de SER', 'nosotros somos', 'Nosotros somos estudiantes.', 'Nosotros ______ de México.', 'somos'),
    ('son', 'son', 'tercera persona plural de SER', 'ellos/ellas son', 'Los niños son muy inteligentes.', 'Mis padres ______ médicos.', 'son'),
    ('sois', 'sois', 'segunda persona plural de SER (vosotros)', 'vosotros sois', 'Vosotros sois mis amigos.', 'Vosotros ______ de Barcelona.', 'sois'),
    ('origen', 'origen con SER', 'uso de SER para indicar el país o ciudad de procedencia', 'ser de + lugar', 'Elena es de Cuba.', 'Él ______ de Japón.', 'es'),
    ('profesion', 'profesión con SER', 'uso de SER para indicar el trabajo o rol de una persona', 'ser + profesión', 'Mi padre es abogado.', 'Ella ______ médica.', 'es'),
  ],
),

'estar': dict(
  level='a1', section='grammar', num='G02',
  short='El Verbo ESTAR',
  title='El Verbo ESTAR — Estado y Ubicación',
  subtitle='Usa ESTAR para hablar de estados temporales y de dónde están las cosas y personas',
  slides=[
    ('¿Qué es el verbo ESTAR?', None,
     '<p class="slide-explanation">El verbo <b>ESTAR</b> se usa para expresar <b>estados temporales</b> (cómo está alguien en un momento) y <b>ubicación</b> (dónde está algo o alguien).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Estoy cansado.</b> (estado temporal)</p>'
     '<p style="margin-top:8px"><b>El libro está en la mesa.</b> (ubicación)</p>'
     '<p style="margin-top:8px"><b>¿Cómo estás?</b> (pregunta sobre el estado)</p>'
     '</div>'
     '<p style="margin-top:16px">ESTAR es el verbo de los estados que pueden cambiar. SER es para lo que no cambia.</p>'),
    ('Conjugación de ESTAR en presente', None,
     '<p class="slide-explanation">Aprende las formas del presente de indicativo de ESTAR:</p>'
     '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
     '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronombre</th><th style="padding:8px;text-align:left">Forma</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">yo</td><td style="padding:8px"><b>estoy</b></td><td style="padding:8px">Estoy en casa.</td></tr>'
     '<tr><td style="padding:8px">tú</td><td style="padding:8px"><b>estás</b></td><td style="padding:8px">¿Estás bien?</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">él/ella/usted</td><td style="padding:8px"><b>está</b></td><td style="padding:8px">Él está en el trabajo.</td></tr>'
     '<tr><td style="padding:8px">nosotros/as</td><td style="padding:8px"><b>estamos</b></td><td style="padding:8px">Estamos muy contentos.</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">vosotros/as</td><td style="padding:8px"><b>estáis</b></td><td style="padding:8px">¿Estáis listos?</td></tr>'
     '<tr><td style="padding:8px">ellos/ustedes</td><td style="padding:8px"><b>están</b></td><td style="padding:8px">Están en el parque.</td></tr>'
     '</table>'),
    ('ESTAR + ubicación', 'Dónde están las cosas',
     '<p class="slide-explanation">Usa ESTAR para indicar <b>dónde se encuentra</b> una persona, animal o cosa. Nunca uses SER para ubicación.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>El banco está en la calle Mayor.</b></p>'
     '<p style="margin-top:8px"><b>¿Dónde está la farmacia?</b></p>'
     '<p style="margin-top:8px"><b>Los niños están en el colegio.</b></p>'
     '<p style="margin-top:8px"><b>Mi bolso está encima de la silla.</b></p>'
     '</div>'
     '<p style="margin-top:16px">Excepciones: SER se usa para eventos ("La fiesta es aquí" = la fiesta se celebra aquí).</p>'),
    ('ESTAR + adjetivos de estado', 'Estados temporales y sentimientos',
     '<p class="slide-explanation">Usa ESTAR + adjetivo para describir <b>estados que pueden cambiar</b>: ánimo, salud, temperatura.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Estoy enfermo.</b> (salud — puede cambiar)</p>'
     '<p style="margin-top:8px"><b>Están muy contentos.</b> (ánimo)</p>'
     '<p style="margin-top:8px"><b>El café está frío.</b> (temperatura)</p>'
     '<p style="margin-top:8px"><b>Estás muy elegante hoy.</b> (aspecto en un momento)</p>'
     '</div>'
     '<p style="margin-top:16px">Compara: <b>Es aburrido</b> (es una persona aburrida, siempre) vs. <b>Está aburrido</b> (en este momento se aburre).</p>'),
  ],
  traps=[
    ('La oficina es en el centro.', 'La oficina <strong>está</strong> en el centro.', 'La ubicación siempre usa ESTAR, nunca SER.'),
    ('Yo estoy médico.', 'Yo <strong>soy</strong> médico.', 'La profesión usa SER, no ESTAR.'),
    ('Ella esta cansada.', 'Ella <strong>está</strong> cansada.', '"Está" lleva tilde: é-s-t-á. Sin tilde es la demostración "esta" (this).'),
    ('Estamos feliz.', 'Estamos <strong>felices</strong>.', 'El adjetivo debe concordar con el sujeto. "Nosotros" → "felices" (plural).'),
    ('¿Donde estas?', '¿Dónde <strong>estás</strong>?', '"Dónde" interrogativo lleva tilde. "Estás" también lleva tilde en la segunda persona singular.'),
  ],
  summary=[
    ('yo', 'estoy', 'Estoy en casa.'),
    ('tú', 'estás', '¿Estás bien?'),
    ('él / ella / usted', 'está', 'El museo está cerrado.'),
    ('nosotros/as', 'estamos', 'Estamos contentos.'),
    ('vosotros/as', 'estáis', '¿Estáis listos?'),
    ('ellos / ellas / ustedes', 'están', 'Están en el parque.'),
  ],
  ex1=('Elige la forma correcta de ESTAR', 'Selecciona la forma correcta de ESTAR.',
    [('Yo ______ muy cansado hoy.', ['estoy', 'soy', 'estás'], 'estoy', 'Primera persona singular de ESTAR es "estoy".'),
     ('¿Dónde ______ el supermercado?', ['está', 'es', 'estoy'], 'está', 'Para indicar ubicación, usamos ESTAR. Con sujeto singular: "está".'),
     ('Mis amigos ______ en la biblioteca.', ['están', 'estamos', 'estáis'], 'están', '"Mis amigos" es tercera persona plural: "están".'),
     ('Nosotros ______ muy contentos con el resultado.', ['estamos', 'somos', 'están'], 'estamos', 'Primera persona plural de ESTAR: "estamos".'),
     ('¿Cómo ______ tú?', ['estás', 'eres', 'está'], 'estás', '"¿Cómo estás?" es la forma estándar de preguntar cómo está alguien.'),
     ('El agua ______ muy fría.', ['está', 'es', 'estoy'], 'está', 'La temperatura es un estado temporal: ESTAR + adjetivo.'),
    ]),
  ex2=('Conjuga el verbo ESTAR', 'Escribe la forma correcta de ESTAR.',
    [('Ella ______ en el hospital. (ESTAR)', 'está', '"Ella" es tercera persona singular: "está".'),
     ('Nosotros ______ muy cansados. (ESTAR)', 'estamos', '"Nosotros" toma la forma "estamos".'),
     ('¿Vosotros ______ bien? (ESTAR)', 'estáis', '"Vosotros" toma la forma "estáis".'),
     ('Los niños ______ en el colegio. (ESTAR)', 'están', 'Tercera persona plural: "están".'),
     ('Yo ______ listo para empezar. (ESTAR)', 'estoy', 'Primera persona singular: "estoy".'),
    ]),
  ex3=('SER o ESTAR: ¿cuál es correcto?', 'Elige el verbo correcto para cada oración.',
    [('El libro ______ encima de la mesa.',
      ['está', 'es', 'soy'],
      'está',
      'Ubicación → ESTAR. "El libro" (tercera persona singular) → "está".'),
     ('Mi padre ______ abogado.',
      ['es', 'está', 'estoy'],
      'es',
      'Profesión → SER. "Mi padre" (tercera persona singular) → "es".'),
     ('¿Cómo ______ la sopa? — Está deliciosa.',
      ['está', 'es', 'sois'],
      'está',
      'El sabor en un momento específico es un estado temporal → ESTAR.'),
     ('Yo ______ de España.',
      ['soy', 'estoy', 'eres'],
      'soy',
      'Origen/procedencia → SER. Primera persona singular → "soy".'),
     ('Los estudiantes ______ nerviosos antes del examen.',
      ['están', 'son', 'sois'],
      'están',
      'Estado temporal (nervioso antes del examen, no siempre) → ESTAR. Plural → "están".'),
    ]),
  game_desc='4 conceptos clave sobre ESTAR · 3 rondas cada uno · llega a 100 puntos para ganar.',
  items=[
    ('estoy', 'estoy', 'primera persona singular de ESTAR', 'yo estoy', 'Estoy muy cansado hoy.', 'Yo ______ en casa.', 'estoy'),
    ('estas', 'estás', 'segunda persona singular de ESTAR (tú)', 'tú estás', '¿Estás bien?', 'Tú ______ muy contento hoy.', 'estás'),
    ('esta', 'está', 'tercera persona singular de ESTAR', 'él/ella está', 'El banco está cerrado.', 'La tienda ______ en la calle Mayor.', 'está'),
    ('estamos', 'estamos', 'primera persona plural de ESTAR', 'nosotros estamos', 'Estamos muy cansados.', 'Nosotros ______ en el parque.', 'estamos'),
    ('estan', 'están', 'tercera persona plural de ESTAR', 'ellos/ellas están', 'Los niños están en casa.', 'Mis amigos ______ en la biblioteca.', 'están'),
    ('ubicacion', 'ubicación con ESTAR', 'uso de ESTAR para indicar dónde se encuentra alguien o algo', 'estar en + lugar', 'El museo está en el centro de la ciudad.', 'La farmacia ______ cerca del hospital.', 'está'),
    ('estado-temp', 'estado temporal', 'uso de ESTAR para describir cómo está algo o alguien en un momento', 'estar + adjetivo', 'Estoy muy cansado después del trabajo.', 'El café ______ frío.', 'está'),
    ('ser-vs-estar', 'SER vs ESTAR', 'diferencia clave: SER = permanente/esencial; ESTAR = temporal/ubicación', 'identidad vs. estado', 'Él es médico (profesión) pero hoy está enfermo (estado).', 'La biblioteca ______ en la avenida principal.', 'está'),
  ],
),

'articulos': dict(
  level='a1', section='grammar', num='G03',
  short='Los Artículos',
  title='Los Artículos — El, La, Un, Una',
  subtitle='Aprende a usar los artículos determinados e indeterminados en español',
  slides=[
    ('¿Qué son los artículos?', None,
     '<p class="slide-explanation">Los artículos van delante de los sustantivos e indican si hablamos de algo <b>conocido</b> (artículo determinado) o <b>desconocido / indefinido</b> (artículo indeterminado).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>El libro</b> está en la mesa. (hablamos de un libro específico conocido)</p>'
     '<p style="margin-top:8px"><b>Un libro</b> está en la mesa. (hablamos de cualquier libro, no identificado)</p>'
     '</div>'
     '<p style="margin-top:16px">En español, todos los sustantivos tienen género (masculino o femenino), y el artículo debe concordar con ese género.</p>'),
    ('Artículos determinados', 'El, La, Los, Las',
     '<p class="slide-explanation">Usamos los artículos determinados para hablar de algo <b>específico o ya conocido</b>:</p>'
     '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
     '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Género</th><th style="padding:8px;text-align:left">Singular</th><th style="padding:8px;text-align:left">Plural</th></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">Masculino</td><td style="padding:8px"><b>el</b> (el libro)</td><td style="padding:8px"><b>los</b> (los libros)</td></tr>'
     '<tr><td style="padding:8px">Femenino</td><td style="padding:8px"><b>la</b> (la mesa)</td><td style="padding:8px"><b>las</b> (las mesas)</td></tr>'
     '</table>'
     '<p style="margin-top:12px">Ejemplos: <b>el perro, la gata, los coches, las casas</b>.</p>'),
    ('Artículos indeterminados', 'Un, Una, Unos, Unas',
     '<p class="slide-explanation">Usamos los artículos indeterminados para presentar algo <b>nuevo o no específico</b>:</p>'
     '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
     '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Género</th><th style="padding:8px;text-align:left">Singular</th><th style="padding:8px;text-align:left">Plural</th></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">Masculino</td><td style="padding:8px"><b>un</b> (un libro)</td><td style="padding:8px"><b>unos</b> (unos libros)</td></tr>'
     '<tr><td style="padding:8px">Femenino</td><td style="padding:8px"><b>una</b> (una mesa)</td><td style="padding:8px"><b>unas</b> (unas mesas)</td></tr>'
     '</table>'
     '<p style="margin-top:12px">Ejemplos: <b>un perro, una gata, unos coches, unas casas</b>.</p>'),
    ('Cuándo usar el artículo y cuándo omitirlo', None,
     '<p class="slide-explanation">Hay casos donde el artículo se omite en español:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Con profesiones tras SER:</b> Soy médico. (no: Soy un médico) — a menos que vayas calificado: Soy <b>un</b> buen médico.</p>'
     '<p style="margin-top:8px"><b>Con días de la semana:</b> Hoy es lunes.</p>'
     '<p style="margin-top:8px"><b>Tras la preposición "de" (posesión):</b> El libro de María. La mochila del (de + el) estudiante.</p>'
     '</div>'
     '<p style="margin-top:16px">Nota: <b>de + el = del</b> | <b>a + el = al</b> (contracciones obligatorias).</p>'),
  ],
  traps=[
    ('El agua está fría. (correcto?)', '¡Sí, <strong>el agua</strong> es correcto!', '"Agua" es femenino pero usa "el" en singular para evitar el hiato (a-a). En plural: las aguas.'),
    ('Soy una profesora.', 'Soy profesora.', 'Después de SER, la profesión va sin artículo indefinido, a menos que lleve adjetivo.'),
    ('Voy a el mercado.', 'Voy <strong>al</strong> mercado.', '"A + el" se contrae obligatoriamente en "al".'),
    ('Es libro de el estudiante.', 'Es el libro <strong>del</strong> estudiante.', '"De + el" se contrae obligatoriamente en "del".'),
    ('La problema es difícil.', 'El problema es difícil.', '"Problema" es masculino aunque termina en -a. Muchos sustantivos de origen griego terminados en -ma son masculinos.'),
  ],
  summary=[
    ('el / los', 'masc. determinado', 'el libro / los libros'),
    ('la / las', 'fem. determinado', 'la casa / las casas'),
    ('un / unos', 'masc. indeterminado', 'un perro / unos perros'),
    ('una / unas', 'fem. indeterminado', 'una silla / unas sillas'),
    ('de + el = del', 'contracción obligatoria', 'el coche del profesor'),
    ('a + el = al', 'contracción obligatoria', 'voy al parque'),
  ],
  ex1=('Elige el artículo correcto', 'Selecciona el artículo adecuado para cada oración.',
    [('¿Dónde está ______ llave? (yo sé de qué llave hablamos)',
      ['la', 'una', 'un'],
      'la',
      'Cuando la llave es conocida y específica, usamos el artículo determinado femenino "la".'),
     ('Tengo ______ gato muy simpático.',
      ['un', 'el', 'la'],
      'un',
      'Presentamos el gato por primera vez → artículo indeterminado masculino "un".'),
     ('______ niños juegan en el parque.',
      ['Los', 'Unos', 'El'],
      'Los',
      'Hablamos de niños en general (determinado plural masculino) → "Los".'),
     ('Voy a comprar ______ manzanas.',
      ['unas', 'los', 'el'],
      'unas',
      'No son manzanas específicas → indeterminado plural femenino "unas".'),
     ('Mi hermano es ______ médico.',
      ['médico (sin artículo)', 'un', 'el'],
      'médico (sin artículo)',
      'Con profesiones después de SER, omitimos el artículo indefinido.'),
     ('Necesito hablar con ______ director.',
      ['el', 'un', 'la'],
      'el',
      'Hablamos de un director específico (el de la empresa) → artículo determinado "el".'),
    ]),
  ex2=('Completa con el artículo correcto', 'Escribe el artículo determinado o indeterminado correcto.',
    [('______ problema es muy difícil. (un problema específico)', 'El', '"Problema" es masculino aunque termina en -a. Singular determinado = "El".'),
     ('Voy ______ cine esta tarde. (a + el)', 'al', '"A + el" se contrae en "al". Es obligatorio.'),
     ('Este es el libro ______ profesor. (de + el)', 'del', '"De + el" se contrae en "del". Es obligatorio.'),
     ('Tengo ______ pregunta. (una pregunta, no específica)', 'una', '"Pregunta" es femenino. Indeterminado singular femenino = "una".'),
     ('______ agua está muy fría. (el agua conocida)', 'El', '"Agua" es femenino pero toma "el" en singular para evitar el hiato (a-a).'),
    ]),
  ex3=('Contracciones y concordancia', 'Elige la opción correcta.',
    [('Voy a comprar el pan. Voy ______ panadería.',
      ['a la', 'al', 'a el'],
      'a la',
      '"Panadería" es femenino. "A + la" no se contrae. "Al" solo existe con "el" (masculino singular).'),
     ('Hablo ______ director del colegio.',
      ['con el', 'con al', 'con del'],
      'con el',
      'Solo "a + el" forma "al". "Con + el" no se contrae.'),
     ('Este es el coche ______ jefe.',
      ['del', 'de el', 'de la'],
      'del',
      '"Del" = "de + el". "Jefe" es masculino singular.'),
     ('Necesito ______ información importante.',
      ['una', 'un', 'el'],
      'una',
      '"Información" es femenino. Artículo indeterminado femenino singular = "una".'),
     ('______ exámenes son mañana.',
      ['Los', 'Las', 'Unos'],
      'Los',
      '"Examen" es masculino. Plural determinado = "Los".'),
    ]),
  game_desc='4 conceptos clave sobre artículos · 3 rondas cada uno · llega a 100 puntos para ganar.',
  items=[
    ('el-la', 'el / la', 'artículo determinado singular — indica algo conocido o específico', 'artículo definido', 'El libro está en la mesa.', 'Busco ______ llave de la puerta.', 'la'),
    ('los-las', 'los / las', 'artículo determinado plural — para hablar de grupos conocidos', 'artículo definido plural', 'Los estudiantes están en clase.', '______ casas de este barrio son antiguas.', 'Las'),
    ('un-una', 'un / una', 'artículo indeterminado singular — presenta algo nuevo o no específico', 'artículo indefinido', 'Tengo un gato en casa.', 'Necesito ______ bolígrafo.', 'un'),
    ('unos-unas', 'unos / unas', 'artículo indeterminado plural — cantidad aproximada o no específica', 'artículo indefinido plural', 'Hay unas sillas en el pasillo.', 'Compré ______ manzanas en el mercado.', 'unas'),
    ('del', 'del (de + el)', 'contracción obligatoria de "de" + "el"', 'posesión masculina', 'Es el coche del director.', 'El nombre ______ alumno es Carlos.', 'del'),
    ('al', 'al (a + el)', 'contracción obligatoria de "a" + "el"', 'dirección/destino masculino', 'Voy al supermercado.', 'Voy ______ banco esta tarde.', 'al'),
    ('masc-fem', 'género del artículo', 'el artículo concuerda en género (masculino/femenino) con el sustantivo', 'concordancia de género', 'El perro y la gata son animales de compañía.', '______ problema es muy complicado.', 'El'),
    ('profesion-sin', 'profesión sin artículo', 'después de SER, la profesión no lleva artículo indefinido (a menos que lleve adjetivo)', 'ser + profesión', 'Mi madre es enfermera.', 'Mi padre es ______ (abogado — sin adjetivo)', 'abogado'),
  ],
),

'pronombres': dict(
  level='a1', section='grammar', num='G04',
  short='Pronombres Personales',
  title='Pronombres Personales — Sujeto',
  subtitle='Aprende los pronombres sujeto y cuándo usarlos en español',
  slides=[
    ('Los pronombres personales de sujeto', None,
     '<p class="slide-explanation">Los pronombres personales de sujeto indican <b>quién realiza la acción</b>. En español son opcionales (el verbo ya indica la persona), pero se usan para dar énfasis o evitar ambigüedad.</p>'
     '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
     '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronombre</th><th style="padding:8px;text-align:left">Equivalente en inglés</th></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px"><b>yo</b></td><td style="padding:8px">I</td></tr>'
     '<tr><td style="padding:8px"><b>tú</b></td><td style="padding:8px">you (informal, singular)</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px"><b>él / ella / usted</b></td><td style="padding:8px">he / she / you (formal)</td></tr>'
     '<tr><td style="padding:8px"><b>nosotros / nosotras</b></td><td style="padding:8px">we</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px"><b>vosotros / vosotras</b></td><td style="padding:8px">you all (informal, Spain)</td></tr>'
     '<tr><td style="padding:8px"><b>ellos / ellas / ustedes</b></td><td style="padding:8px">they / you all (formal)</td></tr>'
     '</table>'),
    ('Tú vs. Usted — informalidad y formalidad', None,
     '<p class="slide-explanation">El español tiene dos formas para "tú" (you singular): <b>tú</b> (informal) y <b>usted</b> (formal). La elección depende del contexto.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Tú</b> (informal): con amigos, familia, personas de tu edad → <b>¿Cómo estás tú?</b></p>'
     '<p style="margin-top:8px"><b>Usted</b> (formal): con desconocidos, jefes, personas mayores → <b>¿Cómo está usted?</b></p>'
     '</div>'
     '<p style="margin-top:16px">Usted se conjuga como "él/ella": <b>¿Dónde vive usted?</b> (no "vive" — correcto; no "vives" — incorrecto con usted)</p>'),
    ('¿Cuándo se omite el pronombre?', None,
     '<p class="slide-explanation">En español, los pronombres de sujeto <b>se omiten frecuentemente</b> porque la desinencia verbal ya indica la persona:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Hablo español.</b> (= Yo hablo español. — "hablo" = primera persona singular)</p>'
     '<p style="margin-top:8px"><b>¿Comes en casa?</b> (= ¿Tú comes en casa?)</p>'
     '<p style="margin-top:8px"><b>Vivimos en Madrid.</b> (= Nosotros vivimos en Madrid.)</p>'
     '</div>'
     '<p style="margin-top:16px">Se usa el pronombre para <b>énfasis</b> o <b>contraste</b>: "Yo hablo español, pero él no."</p>'),
    ('Nosotros/as — género y número', None,
     '<p class="slide-explanation">Algunos pronombres tienen forma masculina y femenina:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>nosotros</b> = grupo mixto o solo hombres | <b>nosotras</b> = solo mujeres</p>'
     '<p style="margin-top:8px"><b>vosotros</b> = grupo mixto o solo hombres (España) | <b>vosotras</b> = solo mujeres</p>'
     '<p style="margin-top:8px"><b>ellos</b> = grupo mixto o solo hombres | <b>ellas</b> = solo mujeres</p>'
     '</div>'
     '<p style="margin-top:16px">En Latinoamérica, <b>ustedes</b> reemplaza tanto a "vosotros" (informal) como a "ustedes" (formal) para el plural.</p>'),
  ],
  traps=[
    ('Yo tengo un hermano. Yo vivo en Madrid.', 'Tengo un hermano. Vivo en Madrid.', 'Repetir "yo" en cada oración suena forzado. Omite el pronombre cuando el contexto es claro.'),
    ('Usted, ¿cómo te llamas?', 'Usted, ¿cómo <strong>se</strong> llama?', '"Usted" usa los mismos verbos que "él/ella": se llama, no "te llamas".'),
    ('Ellas son muy guapas. (grupo mixto)', '<strong>Ellos</strong> son muy guapos.', 'Para grupos mixtos (hombres y mujeres), usa el masculino plural "ellos".'),
    ('Vosotros viven en Barcelona.', 'Vosotros <strong>vivís</strong> en Barcelona.', 'Con "vosotros", los verbos regulares en -ir terminan en -ís, no -en.'),
    ('Yo y tú somos amigos.', '<strong>Tú y yo</strong> somos amigos.', 'En español, "yo" va al final por cortesía: "tú y yo", "él y yo".'),
  ],
  summary=[
    ('yo', '1.ª persona sing.', 'Yo estudio mucho.'),
    ('tú', '2.ª persona sing. (informal)', '¿Tú hablas inglés?'),
    ('él / ella / usted', '3.ª persona sing.', 'Ella vive en Sevilla.'),
    ('nosotros/as', '1.ª persona plural', 'Nosotros somos estudiantes.'),
    ('vosotros/as', '2.ª persona plural (España)', '¿Vosotros coméis aquí?'),
    ('ellos / ellas / ustedes', '3.ª persona plural', 'Ellas trabajan juntas.'),
  ],
  ex1=('Elige el pronombre correcto', 'Selecciona el pronombre personal adecuado.',
    [('______ soy de España.',
      ['Yo', 'Tú', 'Él'],
      'Yo',
      '"Soy" es primera persona singular → pronombre "Yo".'),
     ('______ eres muy inteligente.',
      ['Tú', 'Yo', 'Ella'],
      'Tú',
      '"Eres" es segunda persona singular informal → pronombre "Tú".'),
     ('Mi madre se llama Ana. ______ es profesora.',
      ['Ella', 'Yo', 'Ellos'],
      'Ella',
      'Nos referimos a una mujer (madre) → pronombre "Ella".'),
     ('______ somos de México.',
      ['Nosotros', 'Vosotros', 'Ellos'],
      'Nosotros',
      '"Somos" es primera persona plural → pronombre "Nosotros".'),
     ('Carlos y Pedro son amigos. ______ viven juntos.',
      ['Ellos', 'Ellas', 'Nosotros'],
      'Ellos',
      'Carlos y Pedro son hombres → pronombre masculino plural "Ellos".'),
     ('¿______ estáis listos? (grupo de amigos, España)',
      ['Vosotros', 'Ustedes', 'Nosotros'],
      'Vosotros',
      'Para un grupo de amigos en España, la segunda persona plural informal es "Vosotros".'),
    ]),
  ex2=('Completa con el pronombre correcto', 'Escribe el pronombre personal adecuado.',
    [('______ (I) trabajo en un hospital.', 'Yo', '"Trabajo" es primera persona singular → "Yo". (El pronombre es opcional pero aquí se pide explícitamente.)'),
     ('¿______ (you, informal) hablas francés?', 'Tú', '"Hablas" corresponde a la segunda persona singular informal → "Tú".'),
     ('Mi hermano es alto. ______ (He) juega al fútbol.', 'Él', 'Para hablar de "mi hermano" (hombre) en tercera persona → "Él".'),
     ('______ (We) estudiamos juntos todos los días.', 'Nosotros', '"Estudiamos" es primera persona plural → "Nosotros".'),
     ('Ana y María son amigas. ______ (They) viven en Bilbao.', 'Ellas', 'Ana y María son mujeres → pronombre femenino plural "Ellas".'),
    ]),
  ex3=('¿Correcto o incorrecto?', 'Elige la oración correcta.',
    [('¿Cuál es la frase correcta?',
      ['Usted, ¿cómo se llama?', 'Usted, ¿cómo te llamas?', 'Usted, ¿cómo os llamáis?'],
      'Usted, ¿cómo se llama?',
      '"Usted" se conjuga como tercera persona (él/ella): "se llama". "Te llamas" es para "tú" (informal).'),
     ('¿Cuál es la frase correcta para un grupo mixto?',
      ['Ellos son estudiantes.', 'Ellas son estudiantes.', 'Nosotras son estudiantes.'],
      'Ellos son estudiantes.',
      'Para un grupo mixto (hombres y mujeres), se usa el masculino plural "ellos".'),
     ('¿Cuándo se omite el pronombre de sujeto en español?',
      ['Siempre, porque se omite en todos los casos', 'Cuando el contexto es claro y el verbo indica la persona', 'Nunca, siempre se escribe'],
      'Cuando el contexto es claro y el verbo indica la persona',
      'El pronombre es opcional en español. Se omite cuando la desinencia verbal ya indica la persona.'),
     ('¿Qué pronombre es más formal?',
      ['Usted', 'Tú', 'Vosotros'],
      'Usted',
      '"Usted" es la forma formal de "you" singular. Se usa con personas desconocidas, de mayor edad o en contextos profesionales.'),
     ('¿Cuál es el equivalente a "vosotros" en Latinoamérica?',
      ['Ustedes', 'Ellos', 'Nosotros'],
      'Ustedes',
      'En Latinoamérica, "ustedes" se usa tanto en contextos formales como informales para el plural de "you". "Vosotros" es exclusivo de España.'),
    ]),
  game_desc='4 pronombres personales · 3 rondas cada uno · llega a 100 puntos para ganar.',
  items=[
    ('yo', 'yo', 'primera persona singular — el hablante', 'I', 'Yo hablo español todos los días.', 'Yo ______ (trabajar, 1.ª pers. sing.) en una oficina.', 'trabajo'),
    ('tu', 'tú', 'segunda persona singular informal — la persona con quien hablas', 'you (informal)', '¿Tú estudias en la universidad?', 'Tú ______ (vivir, 2.ª pers. sing.) en Madrid, ¿verdad?', 'vives'),
    ('el-ella', 'él / ella', 'tercera persona singular — una persona (él = hombre, ella = mujer)', 'he / she', 'Ella trabaja en un hospital.', 'Mi hermano ______ (ser, 3.ª pers. sing.) muy alto.', 'es'),
    ('nosotros', 'nosotros/as', 'primera persona plural — el hablante y otros', 'we', 'Nosotros vivimos en el mismo barrio.', 'Nosotros ______ (estudiar, 1.ª pers. pl.) juntos.', 'estudiamos'),
    ('vosotros', 'vosotros/as', 'segunda persona plural informal (España) — grupo de personas', 'you all (Spain)', 'Vosotros coméis mucho.', 'Vosotros ______ (hablar, 2.ª pers. pl.) muy rápido.', 'habláis'),
    ('ellos', 'ellos / ellas', 'tercera persona plural — varias personas', 'they', 'Ellos son mis mejores amigos.', 'Mis padres ______ (vivir, 3.ª pers. pl.) en Sevilla.', 'viven'),
    ('usted', 'usted', 'segunda persona singular formal — se conjuga como él/ella', 'you (formal)', '¿Cómo está usted?', 'Usted ______ (hablar) muy bien español.', 'habla'),
    ('ustedes', 'ustedes', 'segunda persona plural (toda América Latina) — formal e informal', 'you all (Latin America)', 'Ustedes son muy amables.', 'Ustedes ______ (ser) estudiantes de español.', 'son'),
  ],
),

'presente-regular': dict(
  level='a1', section='grammar', num='G05',
  short='Presente Regular',
  title='Presente de Indicativo — Verbos Regulares',
  subtitle='Conjuga los verbos regulares -AR, -ER e -IR en el presente de indicativo',
  slides=[
    ('¿Qué es el presente de indicativo?', None,
     '<p class="slide-explanation">El <b>presente de indicativo</b> es el tiempo verbal que usamos para hablar de acciones que ocurren <b>habitualmente, en este momento o en el futuro próximo</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Hablo español todos los días.</b> (acción habitual)</p>'
     '<p style="margin-top:8px"><b>Ahora mismo como.</b> (acción en progreso)</p>'
     '<p style="margin-top:8px"><b>Mañana viajo a París.</b> (futuro próximo)</p>'
     '</div>'
     '<p style="margin-top:16px">Los verbos en español se dividen en tres grupos según su terminación: <b>-AR</b>, <b>-ER</b>, <b>-IR</b>.</p>'),
    ('Verbos en -AR: hablar', 'El modelo más común',
     '<p class="slide-explanation">La mayoría de los verbos españoles son del grupo <b>-AR</b>. Elimina la terminación -ar y añade las siguientes desinencias:</p>'
     '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
     '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronombre</th><th style="padding:8px;text-align:left">habl-</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">yo</td><td style="padding:8px"><b>-o</b> → hablo</td><td style="padding:8px">Hablo español.</td></tr>'
     '<tr><td style="padding:8px">tú</td><td style="padding:8px"><b>-as</b> → hablas</td><td style="padding:8px">Hablas muy bien.</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">él/ella</td><td style="padding:8px"><b>-a</b> → habla</td><td style="padding:8px">Ella habla francés.</td></tr>'
     '<tr><td style="padding:8px">nosotros</td><td style="padding:8px"><b>-amos</b> → hablamos</td><td style="padding:8px">Hablamos cada día.</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">vosotros</td><td style="padding:8px"><b>-áis</b> → habláis</td><td style="padding:8px">Habláis mucho.</td></tr>'
     '<tr><td style="padding:8px">ellos/ustedes</td><td style="padding:8px"><b>-an</b> → hablan</td><td style="padding:8px">Hablan en clase.</td></tr>'
     '</table>'
     '<p style="margin-top:8px">Otros verbos -AR: trabajar, escuchar, estudiar, comprar, caminar.</p>'),
    ('Verbos en -ER: comer', 'Segundo grupo regular',
     '<p class="slide-explanation">Los verbos <b>-ER</b> siguen un patrón similar a -AR, pero con vocales diferentes:</p>'
     '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
     '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronombre</th><th style="padding:8px;text-align:left">com-</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">yo</td><td style="padding:8px"><b>-o</b> → como</td><td style="padding:8px">Como en casa.</td></tr>'
     '<tr><td style="padding:8px">tú</td><td style="padding:8px"><b>-es</b> → comes</td><td style="padding:8px">¿Comes aquí?</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">él/ella</td><td style="padding:8px"><b>-e</b> → come</td><td style="padding:8px">Él come mucho.</td></tr>'
     '<tr><td style="padding:8px">nosotros</td><td style="padding:8px"><b>-emos</b> → comemos</td><td style="padding:8px">Comemos juntos.</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">vosotros</td><td style="padding:8px"><b>-éis</b> → coméis</td><td style="padding:8px">Coméis a las dos.</td></tr>'
     '<tr><td style="padding:8px">ellos/ustedes</td><td style="padding:8px"><b>-en</b> → comen</td><td style="padding:8px">Comen paella.</td></tr>'
     '</table>'
     '<p style="margin-top:8px">Otros verbos -ER: beber, leer, comprender, correr, responder.</p>'),
    ('Verbos en -IR: vivir', 'Tercer grupo regular',
     '<p class="slide-explanation">Los verbos <b>-IR</b> son casi idénticos a -ER, excepto en "nosotros" y "vosotros":</p>'
     '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
     '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronombre</th><th style="padding:8px;text-align:left">viv-</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">yo</td><td style="padding:8px"><b>-o</b> → vivo</td><td style="padding:8px">Vivo en Madrid.</td></tr>'
     '<tr><td style="padding:8px">tú</td><td style="padding:8px"><b>-es</b> → vives</td><td style="padding:8px">¿Dónde vives?</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">él/ella</td><td style="padding:8px"><b>-e</b> → vive</td><td style="padding:8px">Ella vive aquí.</td></tr>'
     '<tr><td style="padding:8px">nosotros</td><td style="padding:8px"><b>-imos</b> → vivimos</td><td style="padding:8px">Vivimos juntos.</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">vosotros</td><td style="padding:8px"><b>-ís</b> → vivís</td><td style="padding:8px">¿Vivís cerca?</td></tr>'
     '<tr><td style="padding:8px">ellos/ustedes</td><td style="padding:8px"><b>-en</b> → viven</td><td style="padding:8px">Viven en el centro.</td></tr>'
     '</table>'
     '<p style="margin-top:8px">Otros verbos -IR: escribir, abrir, recibir, subir, decidir.</p>'),
  ],
  traps=[
    ('Yo hablo-o español.', 'Yo <strong>hablo</strong> español.', 'La desinencia de yo en -AR ya incluye la vocal: habl + o = hablo. No se añade nada más.'),
    ('Ella comen mucho.', 'Ella <strong>come</strong> mucho.', '"Ella" es tercera persona singular. En -ER: com + e = come. "Comen" es tercera persona plural.'),
    ('Nosotros vivemos aquí.', 'Nosotros <strong>vivimos</strong> aquí.', 'En verbos -IR, la desinencia de nosotros es -imos, no -emos.'),
    ('Vosotros comeis juntos.', 'Vosotros <strong>coméis</strong> juntos.', 'La desinencia de vosotros en -ER es -éis (con tilde): coméis.'),
    ('Ellos trabajan en el hospital. ¿Correcto?', 'Sí, <strong>trabajan</strong> es correcto.', '"Ellos" + verbo -AR: radical + -an = trabajan. ¡Bien!'),
  ],
  summary=[
    ('yo (todos)', '-o', 'habl-o, com-o, viv-o'),
    ('tú (-AR)', '-as', 'habl-as'),
    ('tú (-ER/-IR)', '-es', 'com-es, viv-es'),
    ('él/ella (-AR)', '-a', 'habl-a'),
    ('él/ella (-ER/-IR)', '-e', 'com-e, viv-e'),
    ('nosotros (-AR)', '-amos', 'habl-amos'),
    ('nosotros (-ER)', '-emos', 'com-emos'),
    ('nosotros (-IR)', '-imos', 'viv-imos'),
    ('ellos (-AR)', '-an', 'habl-an'),
    ('ellos (-ER/-IR)', '-en', 'com-en, viv-en'),
  ],
  ex1=('Elige la forma correcta del presente', 'Selecciona la forma correcta del verbo en presente de indicativo.',
    [('Yo ______ en una empresa de tecnología. (trabajar)',
      ['trabajo', 'trabajas', 'trabaja'],
      'trabajo',
      '"Yo" + verbo -AR: radical "trabaj-" + "-o" = trabajo.'),
     ('¿Tú ______ mucho agua? (beber)',
      ['bebes', 'bebo', 'beben'],
      'bebes',
      '"Tú" + verbo -ER: radical "beb-" + "-es" = bebes.'),
     ('Mis padres ______ en Sevilla. (vivir)',
      ['viven', 'vivimos', 'vive'],
      'viven',
      '"Mis padres" = ellos. Verbo -IR: radical "viv-" + "-en" = viven.'),
     ('Nosotros ______ español en clase. (estudiar)',
      ['estudiamos', 'estudian', 'estudiáis'],
      'estudiamos',
      '"Nosotros" + verbo -AR: radical "estudi-" + "-amos" = estudiamos.'),
     ('Vosotros ______ a las tres. (comer)',
      ['coméis', 'comen', 'comemos'],
      'coméis',
      '"Vosotros" + verbo -ER: radical "com-" + "-éis" = coméis.'),
     ('Ella ______ una carta a su abuela. (escribir)',
      ['escribe', 'escribes', 'escribimos'],
      'escribe',
      '"Ella" + verbo -IR: radical "escrib-" + "-e" = escribe.'),
    ]),
  ex2=('Conjuga el verbo en la persona correcta', 'Escribe la forma correcta del presente de indicativo.',
    [('Yo ______ en el centro de la ciudad. (vivir)', 'vivo', '"Yo" + -IR: radical "viv-" + "-o" = vivo.'),
     ('¿Tú ______ mucho? (leer)', 'lees', '"Tú" + -ER: radical "le-" + "-es" = lees. (Ojo: la raíz es "le-" porque dos vocales se separan.)'),
     ('Carlos ______ en una empresa internacional. (trabajar)', 'trabaja', '"Él" + -AR: radical "trabaj-" + "-a" = trabaja.'),
     ('Nosotros ______ la puerta a las ocho. (abrir)', 'abrimos', '"Nosotros" + -IR: radical "abr-" + "-imos" = abrimos.'),
     ('Los estudiantes ______ mucho en esta clase. (aprender)', 'aprenden', '"Ellos" + -ER: radical "aprend-" + "-en" = aprenden.'),
    ]),
  ex3=('Identifica el grupo verbal y la forma', 'Elige la opción correcta.',
    [('¿A qué grupo pertenece el verbo "cantar"?',
      ['-AR', '-ER', '-IR'],
      '-AR',
      '"Cantar" termina en -AR. Modelo: cantar → canto, cantas, canta, cantamos, cantáis, cantan.'),
     ('¿Cuál es la forma correcta de "comprender" para "nosotros"?',
      ['comprendemos', 'comprendimos', 'comprendemos'],
      'comprendemos',
      '"Comprender" es -ER. Nosotros + -emos: radical "comprend-" + "-emos" = comprendemos.'),
     ('¿Cuál es la diferencia entre -ER y -IR en la persona "nosotros"?',
      ['En -ER es -emos, en -IR es -imos', 'Son idénticos', 'En -ER es -imos, en -IR es -emos'],
      'En -ER es -emos, en -IR es -imos',
      'La diferencia clave entre -ER e -IR está en "nosotros" (-emos vs -imos) y "vosotros" (-éis vs -ís).'),
     ('Ellas ______ en el mismo edificio. (vivir)',
      ['viven', 'vivemos', 'vivís'],
      'viven',
      '"Ellas" es tercera persona plural. -IR: radical "viv-" + "-en" = viven.'),
     ('¿Cuál es la desinencia de "yo" en todos los verbos regulares (-AR, -ER, -IR)?',
      ['-o', '-a', '-as'],
      '-o',
      'La primera persona singular (yo) siempre termina en "-o" para los verbos regulares de los tres grupos.'),
    ]),
  game_desc='4 patrones de conjugación del presente regular · 3 rondas cada uno · llega a 100 puntos para ganar.',
  items=[
    ('ar-yo', 'yo -AR (-o)', 'primera persona singular de verbos -AR: radical + -o', 'hablo, trabajo, escucho', 'Yo hablo español todos los días.', 'Yo ______ (escuchar) música por las mañanas.', 'escucho'),
    ('ar-ellos', 'ellos -AR (-an)', 'tercera persona plural de verbos -AR: radical + -an', 'hablan, trabajan, estudian', 'Ellos trabajan en el mismo hospital.', 'Mis amigos ______ (estudiar) juntos.', 'estudian'),
    ('er-tu', 'tú -ER (-es)', 'segunda persona singular de verbos -ER: radical + -es', 'comes, bebes, lees', '¿Comes en la cafetería o en casa?', 'Tú ______ (beber) mucha agua.', 'bebes'),
    ('er-nosotros', 'nosotros -ER (-emos)', 'primera persona plural de verbos -ER: radical + -emos', 'comemos, bebemos, comprendemos', 'Comemos juntos todos los viernes.', 'Nosotros ______ (comprender) la gramática.', 'comprendemos'),
    ('ir-nosotros', 'nosotros -IR (-imos)', 'primera persona plural de verbos -IR: radical + -imos', 'vivimos, escribimos, abrimos', 'Vivimos en el mismo barrio.', 'Nosotros ______ (escribir) muchos correos.', 'escribimos'),
    ('ir-vosotros', 'vosotros -IR (-ís)', 'segunda persona plural de verbos -IR: radical + -ís', 'vivís, escribís, abrís', '¿Vivís cerca del centro?', 'Vosotros ______ (abrir) la tienda a las nueve.', 'abrís'),
    ('ar-tu', 'tú -AR (-as)', 'segunda persona singular de verbos -AR: radical + -as', 'hablas, trabajas, escuchas', '¿Hablas inglés?', 'Tú ______ (caminar) muy rápido.', 'caminas'),
    ('yo-todo', 'yo = siempre -o', 'la primera persona singular (yo) siempre termina en -o en los tres grupos', '-o (AR/ER/IR)', 'Yo hablo, como y vivo aquí.', 'Yo ______ (correr) por las mañanas.', 'corro'),
  ],
),

}
