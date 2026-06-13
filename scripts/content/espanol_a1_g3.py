# -*- coding: utf-8 -*-
"""espanol/ A1 Gramática — lote 3 (G11–G15)."""

CHAPTERS = {

'numeros': dict(
  level='a1', section='grammar', num='G11',
  short='Los Números',
  title='Los Números — Cardinales y Ordinales',
  subtitle='Aprende los números del 0 al 1000 y los ordinales del 1.º al 10.º',
  slides=[
    ('Números del 0 al 20', None,
     '<p class="slide-explanation">Los números del 0 al 20 son fundamentales y hay que memorizarlos:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>0</b> cero &nbsp; <b>1</b> uno &nbsp; <b>2</b> dos &nbsp; <b>3</b> tres &nbsp; <b>4</b> cuatro &nbsp; <b>5</b> cinco</p>'
     '<p style="margin-top:8px"><b>6</b> seis &nbsp; <b>7</b> siete &nbsp; <b>8</b> ocho &nbsp; <b>9</b> nueve &nbsp; <b>10</b> diez</p>'
     '<p style="margin-top:8px"><b>11</b> once &nbsp; <b>12</b> doce &nbsp; <b>13</b> trece &nbsp; <b>14</b> catorce &nbsp; <b>15</b> quince</p>'
     '<p style="margin-top:8px"><b>16</b> dieciséis &nbsp; <b>17</b> diecisiete &nbsp; <b>18</b> dieciocho &nbsp; <b>19</b> diecinueve &nbsp; <b>20</b> veinte</p>'
     '</div>'),
    ('Números del 21 al 100', None,
     '<p class="slide-explanation">Del 21 al 29 se escriben en una sola palabra. Del 30 en adelante se unen con "y":</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>21</b> veintiuno &nbsp; <b>22</b> veintidós &nbsp; <b>23</b> veintitrés &nbsp; <b>29</b> veintinueve</p>'
     '<p style="margin-top:8px"><b>30</b> treinta &nbsp; <b>31</b> treinta y uno &nbsp; <b>40</b> cuarenta &nbsp; <b>50</b> cincuenta</p>'
     '<p style="margin-top:8px"><b>60</b> sesenta &nbsp; <b>70</b> setenta &nbsp; <b>80</b> ochenta &nbsp; <b>90</b> noventa &nbsp; <b>100</b> cien</p>'
     '</div>'
     '<p style="margin-top:12px">Nota: "cien" para exactamente 100; "ciento" cuando va seguido de otro número: <b>ciento uno, ciento veinte</b>.</p>'),
    ('Números del 100 al 1000', None,
     '<p class="slide-explanation">Las centenas tienen formas especiales y concuerdan en género:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>100</b> cien / ciento &nbsp; <b>200</b> doscientos/as &nbsp; <b>300</b> trescientos/as</p>'
     '<p style="margin-top:8px"><b>400</b> cuatrocientos/as &nbsp; <b>500</b> quinientos/as &nbsp; <b>600</b> seiscientos/as</p>'
     '<p style="margin-top:8px"><b>700</b> setecientos/as &nbsp; <b>800</b> ochocientos/as &nbsp; <b>900</b> novecientos/as &nbsp; <b>1000</b> mil</p>'
     '</div>'
     '<p style="margin-top:12px">Concordancia: <b>doscientas personas</b> (femenino), <b>doscientos euros</b> (masculino).</p>'),
    ('Números ordinales', 'Del 1.º al 10.º',
     '<p class="slide-explanation">Los ordinales indican posición o orden. Concuerdan en género y número con el sustantivo:</p>'
     '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
     '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Ordinal</th><th style="padding:8px;text-align:left">Masc.</th><th style="padding:8px;text-align:left">Fem.</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">1.º / 1.ª</td><td style="padding:8px">primero</td><td style="padding:8px">primera</td><td style="padding:8px">el primer día</td></tr>'
     '<tr><td style="padding:8px">2.º / 2.ª</td><td style="padding:8px">segundo</td><td style="padding:8px">segunda</td><td style="padding:8px">la segunda planta</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">3.º / 3.ª</td><td style="padding:8px">tercero</td><td style="padding:8px">tercera</td><td style="padding:8px">el tercer piso</td></tr>'
     '<tr><td style="padding:8px">4.º–10.º</td><td style="padding:8px">cuarto…décimo</td><td style="padding:8px">cuarta…décima</td><td style="padding:8px">la quinta vez</td></tr>'
     '</table>'
     '<p style="margin-top:8px">Primero y tercero pierden la -o ante masculino singular: el <b>primer</b> día, el <b>tercer</b> premio.</p>'),
  ],
  traps=[
    ('Tengo venti años.', 'Tengo <strong>veinte</strong> años.', '"Veinte" es la forma correcta. "Venti" es italiano, no español.'),
    ('Ella tiene trentaydos años.', 'Ella tiene <strong>treinta y dos</strong> años.', 'Del 31 en adelante, se escribe separado: treinta y dos.'),
    ('Cien y dos personas.', '<strong>Ciento dos</strong> personas.', '"Cien" es solo para exactamente 100. Cuando va seguido de otra cifra: ciento + número.'),
    ('Es el primero día del curso.', 'Es el <strong>primer</strong> día del curso.', 'Primero y tercero se acortan a primer y tercer ante sustantivo masculino singular.'),
    ('Dosciento euros.', '<strong>Doscientos</strong> euros.', 'Las centenas concuerdan en género: doscientos (masc.), doscientas (fem.).'),
  ],
  summary=[
    ('1–15', 'formas únicas', 'uno, dos, tres, cuatro, cinco… quince'),
    ('16–19', 'dieci- + unidad', 'dieciséis, diecisiete, dieciocho, diecinueve'),
    ('20–29', 'veinti- + unidad', 'veinte, veintiuno, veintidós…'),
    ('30–99', 'decena + y + unidad', 'treinta y uno, cuarenta y cinco'),
    ('100 exacto', 'cien', 'Tengo cien euros.'),
    ('101+', 'ciento + número', 'ciento uno, ciento veinte'),
    ('200–900', 'centenas concuerdan', 'doscientas personas / doscientos libros'),
    ('ordinales', 'primero/a, segundo/a…', 'la primera vez, el segundo piso'),
  ],
  ex1=('Elige el número correcto', 'Selecciona la opción correcta para cada oración.',
    [('Mi abuela tiene ______ años.',
      ['setenta y cinco', 'setentaicinco', 'setenta cinco'],
      'setenta y cinco',
      'Del 31 en adelante, los números se escriben con "y": setenta y cinco.'),
     ('Hay ______ estudiantes en la clase.',
      ['veintidós', 'veinty dos', 'veinte y dos'],
      'veintidós',
      'Del 21 al 29, se escribe en una sola palabra: veintidós.'),
     ('El libro cuesta ______ euros.',
      ['ciento veinte', 'cien veinte', 'ciento y veinte'],
      'ciento veinte',
      '"Ciento" (no "cien") cuando va seguido de otra cifra. No se añade "y" entre centenas y decenas/unidades.'),
     ('Es la ______ vez que visito Madrid.',
      ['primera', 'uno', 'primero'],
      'primera',
      '"Vez" es femenino, por eso el ordinal es "primera".'),
     ('Hay ______ personas en la sala.',
      ['doscientas', 'doscientos', 'dos cientos'],
      'doscientas',
      '"Personas" es femenino. Las centenas concuerdan: doscientas.'),
     ('Mi número de teléfono termina en ______.',
      ['tres', 'ter', 'tercero'],
      'tres',
      'Los números de teléfono usan cardinales, no ordinales.'),
    ]),
  ex2=('Escribe el número en palabras', 'Escribe la forma correcta.',
    [('¿Cuántos años tienes? — Tengo ______ (35) años.', 'treinta y cinco', '35 = treinta y cinco (decena + y + unidad).'),
     ('Hay ______ (100) personas en el concierto.', 'cien', 'Para exactamente 100, usamos "cien".'),
     ('El vuelo sale en ______ (15) minutos.', 'quince', '15 = quince.'),
     ('Vivo en el ______ (3.º) piso.', 'tercer', '"Tercer" es la forma apocopada de "tercero" ante masculino singular.'),
     ('El apartamento cuesta ______ (500) euros al mes.', 'quinientos', '500 = quinientos (masculino, porque "euros" es masculino).'),
    ]),
  ex3=('Ordinales: género y posición', 'Elige la forma correcta del ordinal.',
    [('Vivo en el ______ piso.',
      ['tercer', 'tercero', 'tercera'],
      'tercer',
      '"Piso" es masculino singular. Tercero → tercer ante masculino singular.'),
     ('Es la ______ semana de clase.',
      ['segunda', 'segundo', 'dos'],
      'segunda',
      '"Semana" es femenino. El ordinal es "segunda".'),
     ('¡Llegamos en ______ lugar!',
      ['primer', 'primera', 'primero'],
      'primer',
      '"Lugar" es masculino singular. Primero → primer ante masculino singular.'),
     ('Hoy es el ______ día del año.',
      ['primero', 'primer', 'primera'],
      'primero',
      'Cuando el ordinal va solo (predicado) o sin sustantivo inmediato, se mantiene: "el primero" o "el primer día".'),
     ('Es la ______ vez que visita España.',
      ['cuarta', 'cuarto', 'cuatro'],
      'cuarta',
      '"Vez" es femenino. El ordinal es "cuarta".'),
    ]),
  game_desc='4 grupos de números clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
  items=[
    ('1-20', '1 al 20', 'los veinte primeros números cardinales', 'los números básicos', 'Tengo quince euros en la cartera.', 'Mi hermano tiene ______ (17) años.', 'diecisiete'),
    ('21-99', '21 al 99', 'números del 21 al 99: decenas + y + unidades', 'números compuestos', 'Hay treinta y dos estudiantes en la clase.', 'El autobús sale en ______ (45) minutos.', 'cuarenta y cinco'),
    ('cien-ciento', 'cien / ciento', 'cien = exactamente 100; ciento cuando va seguido de más cifras', 'la centena', 'Cien personas asistieron al evento.', 'Hay ______ (101) páginas en el libro.', 'ciento uno'),
    ('centenas', 'centenas (200–900)', 'doscientos, trescientos… novecientos — concuerdan en género', 'múltiplos de cien', 'La ciudad tiene doscientas mil habitantes.', 'El tren cuesta ______ (300) euros.', 'trescientos'),
    ('primer', 'primer / primero', 'ordinal de 1.º: primer ante masc. sing., primero en otros casos', 'primer / primera', 'El primer día de clase es importante.', 'Vivo en el ______ (1.º) piso.', 'primer'),
    ('segundo', 'segundo/a', 'ordinal de 2.º — concuerda en género', 'segundo / segunda', 'Es la segunda vez que vengo aquí.', 'Tiene una ______ (2.ª) oportunidad.', 'segunda'),
    ('decenas', 'decenas (30–90)', 'treinta, cuarenta, cincuenta, sesenta, setenta, ochenta, noventa', 'múltiplos de diez', 'Mi padre tiene sesenta años.', 'La ciudad está a ______ (80) kilómetros.', 'ochenta'),
    ('veinti', 'veinti- (21–29)', 'del 21 al 29: se escribe en una sola palabra con veinti-', 'veintiuno a veintinueve', 'Tengo veintitrés años.', 'Hay ______ (22) personas aquí.', 'veintidós'),
  ],
),

'interrogativos': dict(
  level='a1', section='grammar', num='G12',
  short='Las Preguntas',
  title='Las Preguntas — Palabras Interrogativas',
  subtitle='Aprende a hacer preguntas con qué, quién, cómo, dónde, cuándo, por qué y cuánto',
  slides=[
    ('Las palabras interrogativas', None,
     '<p class="slide-explanation">Las palabras interrogativas siempre llevan <b>tilde</b> cuando se usan en preguntas directas o indirectas. Son las siguientes:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¿Qué?</b> — What? &nbsp; <b>¿Quién? / ¿Quiénes?</b> — Who?</p>'
     '<p style="margin-top:8px"><b>¿Cómo?</b> — How? / What ... like? &nbsp; <b>¿Dónde?</b> — Where?</p>'
     '<p style="margin-top:8px"><b>¿Cuándo?</b> — When? &nbsp; <b>¿Por qué?</b> — Why?</p>'
     '<p style="margin-top:8px"><b>¿Cuánto/a?</b> — How much? &nbsp; <b>¿Cuántos/as?</b> — How many?</p>'
     '<p style="margin-top:8px"><b>¿Cuál? / ¿Cuáles?</b> — Which? / What?</p>'
     '</div>'),
    ('Qué, cuál y cómo', 'Preguntas sobre identidad y descripción',
     '<p class="slide-explanation">Estos tres interrogativos son los más usados y a veces se confunden:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¿Qué es esto?</b> (What is this? — pedimos una definición o categoría)</p>'
     '<p style="margin-top:8px"><b>¿Cuál es tu nombre?</b> (What is your name? — elegimos entre opciones)</p>'
     '<p style="margin-top:8px"><b>¿Cómo te llamas?</b> (What is your name? — cómo se llama, la manera)</p>'
     '<p style="margin-top:8px"><b>¿Cómo estás?</b> (How are you? — estado/manera)</p>'
     '</div>'
     '<p style="margin-top:12px">Regla general: <b>¿qué + SER?</b> para definiciones; <b>¿cuál + SER?</b> para identificar entre opciones.</p>'),
    ('Dónde, cuándo y por qué', 'Lugar, tiempo y causa',
     '<p class="slide-explanation">Tres interrogativos esenciales para preguntar sobre circunstancias:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¿Dónde vives?</b> — En Madrid. (lugar)</p>'
     '<p style="margin-top:8px"><b>¿De dónde eres?</b> — Soy de Colombia. (origen)</p>'
     '<p style="margin-top:8px"><b>¿Cuándo empieza la clase?</b> — A las nueve. (tiempo)</p>'
     '<p style="margin-top:8px"><b>¿Por qué estudias español?</b> — Porque me gusta. (causa/razón)</p>'
     '</div>'
     '<p style="margin-top:12px">Atención: <b>¿por qué?</b> (pregunta) vs. <b>porque</b> (respuesta, sin tilde).</p>'),
    ('Cuánto y quién', 'Cantidad y persona',
     '<p class="slide-explanation">Interrogativos para preguntar sobre cantidad y personas:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¿Cuánto cuesta?</b> — Cuesta diez euros. (cantidad, incontable o sin sustantivo)</p>'
     '<p style="margin-top:8px"><b>¿Cuántos años tienes?</b> — Tengo veinte años. (plural masculino)</p>'
     '<p style="margin-top:8px"><b>¿Cuántas personas hay?</b> — Hay treinta. (plural femenino)</p>'
     '<p style="margin-top:8px"><b>¿Quién es ella?</b> — Es mi profesora. (persona singular)</p>'
     '<p style="margin-top:8px"><b>¿Quiénes son ellos?</b> — Son mis compañeros. (persona plural)</p>'
     '</div>'),
  ],
  traps=[
    ('¿Que es tu nombre?', '¿<strong>Cuál</strong> es tu nombre?', '"¿Qué es...?" pide una definición. Para identificar (el nombre), se usa "¿Cuál es...?".'),
    ('¿Porque estudias español?', '¿<strong>Por qué</strong> estudias español?', '"¿Por qué?" (dos palabras, con tilde) es la pregunta. "Porque" (una palabra, sin tilde) es la respuesta.'),
    ('¿Cuánto personas hay?', '¿Cuántas <strong>personas</strong> hay?', '"Personas" es femenino plural → "cuántas", no "cuánto".'),
    ('¿Donde vives?', '¿<strong>Dónde</strong> vives?', 'Las palabras interrogativas llevan tilde: dónde, cuándo, cómo, qué, quién, cuál, cuánto.'),
    ('¿Quien son ellos?', '¿<strong>Quiénes</strong> son ellos?', 'Para referirse a varias personas, "quién" va en plural: "¿quiénes?".'),
  ],
  summary=[
    ('¿Qué?', 'definición / cosa', '¿Qué es eso? — Es una mochila.'),
    ('¿Cuál? / ¿Cuáles?', 'identificación / elección', '¿Cuál es tu libro?'),
    ('¿Quién? / ¿Quiénes?', 'persona/s', '¿Quién llama? / ¿Quiénes vienen?'),
    ('¿Cómo?', 'manera / descripción', '¿Cómo te llamas? / ¿Cómo estás?'),
    ('¿Dónde?', 'lugar', '¿Dónde está el banco?'),
    ('¿Cuándo?', 'tiempo', '¿Cuándo empieza?'),
    ('¿Por qué?', 'causa', '¿Por qué estudias? — Porque me gusta.'),
    ('¿Cuánto/a/os/as?', 'cantidad', '¿Cuántos años tienes?'),
  ],
  ex1=('Elige la palabra interrogativa correcta', 'Selecciona el interrogativo correcto para cada pregunta.',
    [('______ es tu profesora de español?',
      ['¿Quién', '¿Qué', '¿Cuándo'],
      '¿Quién',
      'Preguntamos por una persona → "¿quién?".'),
     ('______ vives? — En Sevilla.',
      ['¿Dónde', '¿Cuándo', '¿Cómo'],
      '¿Dónde',
      'Preguntamos por un lugar → "¿dónde?".'),
     ('______ cuesta este libro?',
      ['¿Cuánto', '¿Cuántos', '¿Qué'],
      '¿Cuánto',
      'Preguntamos por el precio (cantidad sin sustantivo) → "¿cuánto?".'),
     ('______ estudias español? — Porque me gusta.',
      ['¿Por qué', '¿Porque', '¿Cómo'],
      '¿Por qué',
      '¿Por qué? (dos palabras, con tilde) pregunta por la causa. "Porque" es la respuesta.'),
     ('______ es tu número de teléfono?',
      ['¿Cuál', '¿Qué', '¿Quién'],
      '¿Cuál',
      'Para pedir información específica (elegir entre opciones) → "¿cuál?".'),
     ('______ se llama tu amiga?',
      ['¿Cómo', '¿Qué', '¿Dónde'],
      '¿Cómo',
      '"¿Cómo se llama?" es la forma estándar de preguntar el nombre de alguien.'),
    ]),
  ex2=('Completa la pregunta', 'Escribe la palabra interrogativa correcta.',
    [('______ años tienes? — Tengo veintitrés años.', '¿Cuántos', '"Años" es masculino plural → "¿cuántos?".'),
     ('______ empieza la película? — A las ocho.', '¿Cuándo', 'Preguntamos por el momento → "¿cuándo?".'),
     ('______ son esas chicas? — Son mis compañeras.', '¿Quiénes', 'Son varias personas → "¿quiénes?" (plural).'),
     ('______ es la capital de España? — Madrid.', '¿Cuál', 'Pedimos identificar entre opciones → "¿cuál?".'),
     ('______ hablas inglés? — Porque lo necesito para trabajar.', '¿Por qué', '"¿Por qué?" (dos palabras, tilde) pregunta la causa.'),
    ]),
  ex3=('Forma preguntas correctas', 'Elige la pregunta correcta.',
    [('¿Cuál es la diferencia entre "¿qué?" y "¿cuál?"?',
      ['¿Qué? pide definición; ¿cuál? identifica entre opciones', '¿Cuál? pide definición; ¿qué? identifica', 'Son sinónimos perfectos'],
      '¿Qué? pide definición; ¿cuál? identifica entre opciones',
      'Regla clave: ¿Qué es...? = define/explica. ¿Cuál es...? = identifica algo específico.'),
     ('Para preguntar la razón de algo, ¿qué usamos?',
      ['¿Por qué?', '¿Porque?', '¿Para qué?'],
      '¿Por qué?',
      '"¿Por qué?" (dos palabras, tilde) pregunta la causa. "Porque" (una palabra, sin tilde) responde.'),
     ('¿Cuántas personas hay en la foto? ¿Por qué "cuántas"?',
      ['Porque "personas" es femenino plural', 'Porque "personas" es masculino', 'Porque se usa siempre "cuántas"'],
      'Porque "personas" es femenino plural',
      '"Cuánto" concuerda con el sustantivo: cuántos (masc. pl.), cuántas (fem. pl.).'),
     ('¿Cuál es la forma correcta de pedir el nombre?',
      ['¿Cómo te llamas? / ¿Cuál es tu nombre?', '¿Qué es tu nombre?', '¿Quién te llamas?'],
      '¿Cómo te llamas? / ¿Cuál es tu nombre?',
      'Ambas son correctas. "¿Qué es tu nombre?" es un anglicismo incorrecto en español.'),
     ('¿Cuál es la pregunta correcta?',
      ['¿Dónde vives tú?', '¿Donde vives tú?', '¿Dónde vives tu?'],
      '¿Dónde vives tú?',
      '"Dónde" y "tú" (pronombre enfático) llevan tilde. "Tu" sin tilde es el posesivo.'),
    ]),
  game_desc='4 palabras interrogativas clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
  items=[
    ('que', '¿Qué?', 'pregunta por una cosa, definición o categoría', 'what?', '¿Qué es esto? — Es un bolígrafo.', '______ idiomas hablas?', '¿Qué'),
    ('donde', '¿Dónde?', 'pregunta por el lugar o la ubicación', 'where?', '¿Dónde está la estación de metro?', '______ vives ahora?', '¿Dónde'),
    ('cuando', '¿Cuándo?', 'pregunta por el momento o el tiempo', 'when?', '¿Cuándo empieza la clase?', '______ es tu cumpleaños?', '¿Cuándo'),
    ('quien', '¿Quién? / ¿Quiénes?', 'pregunta por una o varias personas', 'who?', '¿Quién es ese señor?', '______ viene a la fiesta?', '¿Quién'),
    ('como', '¿Cómo?', 'pregunta por la manera, descripción o estado', 'how? / what ... like?', '¿Cómo estás? — Muy bien, gracias.', '______ te llamas?', '¿Cómo'),
    ('cuanto', '¿Cuánto/a/os/as?', 'pregunta por la cantidad — concuerda con el sustantivo', 'how much / many?', '¿Cuántos años tienes?', '______ cuesta este libro?', '¿Cuánto'),
    ('por-que', '¿Por qué?', 'pregunta por la causa o razón (dos palabras, con tilde)', 'why?', '¿Por qué estudias español?', '______ no comes?', '¿Por qué'),
    ('cual', '¿Cuál? / ¿Cuáles?', 'pregunta para identificar o elegir entre opciones', 'which? / what (specific)?', '¿Cuál es tu número de teléfono?', '______ es tu dirección?', '¿Cuál'),
  ],
),

'negacion': dict(
  level='a1', section='grammar', num='G13',
  short='La Negación',
  title='La Negación — No, Nada, Nunca, Nadie',
  subtitle='Aprende a negar en español con no, nunca, nada, nadie, ninguno y tampoco',
  slides=[
    ('La negación simple con NO', None,
     '<p class="slide-explanation">Para negar en español, se coloca <b>no</b> directamente <b>delante del verbo</b>. Es la negación más frecuente:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Afirmativo → Negativo:</p>'
     '<p style="margin-top:8px"><b>Hablo español.</b> → <b>No hablo español.</b></p>'
     '<p style="margin-top:8px"><b>Tengo hambre.</b> → <b>No tengo hambre.</b></p>'
     '<p style="margin-top:8px"><b>Es médico.</b> → <b>No es médico.</b></p>'
     '</div>'
     '<p style="margin-top:16px">En español, "no" va siempre justo antes del verbo, sin ninguna otra palabra entre medias.</p>'),
    ('Doble negación', 'Un rasgo esencial del español',
     '<p class="slide-explanation">En español, la <b>doble negación es obligatoria</b> cuando la oración contiene palabras negativas junto al verbo:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>No como nada.</b> (I don\'t eat anything.) — "no" + "nada" ✓</p>'
     '<p style="margin-top:8px"><b>No viene nadie.</b> (Nobody comes.) — "no" + "nadie" ✓</p>'
     '<p style="margin-top:8px"><b>No hablo nunca.</b> (I never speak.) — "no" + "nunca" ✓</p>'
     '</div>'
     '<p style="margin-top:12px">Si la palabra negativa va <b>antes</b> del verbo, no se usa "no": <b>Nunca como allí.</b> / <b>Nadie viene.</b></p>'),
    ('Palabras negativas clave', None,
     '<p class="slide-explanation">El español tiene un conjunto de palabras negativas muy útiles:</p>'
     '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
     '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Negativo</th><th style="padding:8px;text-align:left">Significado</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px"><b>nada</b></td><td style="padding:8px">nothing / anything</td><td style="padding:8px">No quiero nada.</td></tr>'
     '<tr><td style="padding:8px"><b>nadie</b></td><td style="padding:8px">nobody / anybody</td><td style="padding:8px">No conozco a nadie.</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px"><b>nunca / jamás</b></td><td style="padding:8px">never / ever</td><td style="padding:8px">No como nunca aquí.</td></tr>'
     '<tr><td style="padding:8px"><b>tampoco</b></td><td style="padding:8px">neither / not either</td><td style="padding:8px">Yo tampoco quiero ir.</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px"><b>ningún / ninguno</b></td><td style="padding:8px">no / none / not any</td><td style="padding:8px">No tengo ningún problema.</td></tr>'
     '</table>'),
    ('Tampoco y también', 'Acuerdo negativo y positivo',
     '<p class="slide-explanation">Para expresar acuerdo en frases negativas usamos <b>tampoco</b>; para positivas, <b>también</b>:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>— No me gusta el café. — A mí <b>tampoco</b>. (Me neither.)</p>'
     '<p style="margin-top:8px">— Me gusta el chocolate. — A mí <b>también</b>. (Me too.)</p>'
     '<p style="margin-top:8px">— No voy a la fiesta. — Yo <b>tampoco</b> voy.</p>'
     '</div>'
     '<p style="margin-top:12px">Compara: <b>también</b> (also / too) vs. <b>tampoco</b> (neither / not either).</p>'),
  ],
  traps=[
    ('No hablo nada. ¿Es incorrecto?', '¡<strong>No hablo nada</strong> es correcto!', 'La doble negación es obligatoria en español. "No + nada" es perfectamente correcto.'),
    ('Nadie no viene.', '<strong>Nadie viene.</strong> (o No viene nadie.)', 'Si "nadie" va antes del verbo, no se necesita el "no" adicional.'),
    ('No tengo ningún problema. ¿Y si el sustantivo es femenino?', 'No tengo <strong>ninguna</strong> duda.', '"Ningún" va ante masculino singular; "ninguna" ante femenino singular.'),
    ('Yo no como también.', 'Yo <strong>tampoco</strong> como.', 'Para acuerdo negativo se usa "tampoco", no "también".'),
    ('¿Hablas español? — No, no hablo.', '— No, no hablo <strong>nada</strong> / no hablo <strong>nada de</strong> español.', 'Aunque "No, no hablo" es comprensible, añadir "nada" suena más natural.'),
  ],
  summary=[
    ('no + verbo', 'negación simple', 'No hablo alemán.'),
    ('no + verbo + nada', 'nada = nothing', 'No como nada por la mañana.'),
    ('no + verbo + nadie', 'nadie = nobody', 'No conozco a nadie aquí.'),
    ('no + verbo + nunca', 'nunca = never', 'No voy nunca al gimnasio.'),
    ('nunca/nadie + verbo', 'negativo antes del verbo = sin no', 'Nunca como aquí. Nadie viene.'),
    ('tampoco', 'acuerdo negativo', '— No me gusta. — A mí tampoco.'),
  ],
  ex1=('Elige la opción correcta para negar', 'Selecciona la negación correcta.',
    [('______ tengo dinero.',
      ['No', 'Nunca', 'Nadie'],
      'No',
      'Para una negación simple del verbo, usamos "no" delante del verbo.'),
     ('No quiero ______ de comer.',
      ['nada', 'nadie', 'nunca'],
      'nada',
      '"Nada" niega cosas (food = cosa). "No quiero nada" = I don\'t want anything.'),
     ('No conozco a ______ en esta ciudad.',
      ['nadie', 'nada', 'ningún'],
      'nadie',
      '"Nadie" niega personas. "No conozco a nadie" = I don\'t know anybody.'),
     ('No voy ______ al médico.',
      ['nunca', 'nadie', 'nada'],
      'nunca',
      '"Nunca" niega la frecuencia: never/ever.'),
     ('— No me gusta el fútbol. — A mí ______.',
      ['tampoco', 'también', 'nada'],
      'tampoco',
      'Para expresar acuerdo con una oración negativa usamos "tampoco".'),
     ('No tengo ______ libro de matemáticas.',
      ['ningún', 'nadie', 'nada'],
      'ningún',
      '"Ningún" + sustantivo masculino singular: no tengo ningún libro.'),
    ]),
  ex2=('Transforma a negativo', 'Escribe la oración en negativo.',
    [('Como en la cafetería. → No ______', 'como en la cafetería', 'Ponemos "no" delante del verbo: No como en la cafetería.'),
     ('Tengo hambre. → No ______', 'tengo hambre', 'No + verbo + resto: No tengo hambre.'),
     ('Siempre llego tarde. → ______ llego tarde. (con "nunca")', 'Nunca', '"Siempre" (always) → "nunca" (never). Si va antes del verbo, no necesita "no".'),
     ('Alguien llama a la puerta. → ______ llama a la puerta. (con "nadie")', 'Nadie', '"Alguien" (someone) → "nadie" (nobody). Antes del verbo, sin "no".'),
     ('Me gusta la música pop. (responde con tampoco) → A mí ______', 'tampoco', 'Para acuerdo negativo: "A mí tampoco (me gusta)."'),
    ]),
  ex3=('Doble negación: correcto o incorrecto', 'Elige la oración correctamente negada.',
    [('¿Cuál es correcta?',
      ['No hablo con nadie.', 'No hablo con alguien.', 'Hablo con nadie.'],
      'No hablo con nadie.',
      'En español, si el verbo lleva "no", la palabra negativa correspondiente es "nadie" (no "alguien"). La doble negación es obligatoria.'),
     ('¿Cuál es correcta?',
      ['Nunca como allí.', 'No nunca como allí.', 'Nunca no como allí.'],
      'Nunca como allí.',
      'Cuando la palabra negativa va antes del verbo, no se añade "no".'),
     ('¿Cuál expresa "I don\'t have any problems"?',
      ['No tengo ningún problema.', 'No tengo nada problema.', 'No tengo nadie problema.'],
      'No tengo ningún problema.',
      '"Ningún" + sustantivo masculino singular = not any + noun.'),
     ('¿Qué significa "Yo tampoco voy"?',
      ['Yo tampoco voy = I\'m not going either', 'Yo tampoco voy = I\'m also going', 'Yo tampoco voy = I sometimes go'],
      'Yo tampoco voy = I\'m not going either',
      '"Tampoco" indica acuerdo con una oración negativa (= neither / not ... either).'),
     ('— No me gusta el invierno. ¿Cómo estás de acuerdo?',
      ['A mí tampoco.', 'A mí también.', 'A mí nada.'],
      'A mí tampoco.',
      'Para acuerdo con una oración negativa, se usa "tampoco": A mí tampoco (me gusta).'),
    ]),
  game_desc='4 elementos de negación · 3 rondas cada uno · llega a 100 puntos para ganar.',
  items=[
    ('no-simple', 'no + verbo', 'negación simple: se coloca "no" directamente antes del verbo', 'no hablo, no tengo, no es', 'No hablo ruso.', 'Yo ______ vivo en Madrid. (negar)', 'no'),
    ('nada', 'nada', 'negación de cosas o cantidades (nothing / anything)', 'ninguna cosa', 'No quiero nada de comer.', 'No tengo ______ que decir.', 'nada'),
    ('nadie', 'nadie', 'negación de personas (nobody / anybody)', 'ninguna persona', 'No conozco a nadie en esta clase.', 'No hay ______ en casa.', 'nadie'),
    ('nunca', 'nunca', 'negación temporal (never / ever) — siempre o antes del verbo o con no', 'jamás', 'No voy nunca al gimnasio. / Nunca voy al gimnasio.', 'No como ______ en este restaurante.', 'nunca'),
    ('tampoco', 'tampoco', 'acuerdo negativo (neither / not either)', 'yo tampoco, a mí tampoco', '— No me gusta. — A mí tampoco.', '— No quiero café. — Yo ______.', 'tampoco'),
    ('ningun', 'ningún / ninguna', 'ningún + sust. masc. sing.; ninguna + sust. fem. sing. (no / none)', 'ningún libro, ninguna idea', 'No tengo ningún problema.', 'No hay ______ duda. (femenino)', 'ninguna'),
    ('doble-neg', 'doble negación', 'en español, si el verbo lleva no, la palabra negativa que le sigue también es negativa', 'no + nada/nadie/nunca', 'No hablo con nadie. No como nada.', 'No veo ______ aquí. (nobody)', 'a nadie'),
    ('alguien-nadie', 'alguien → nadie', 'alguien (someone) en positivo se convierte en nadie (nobody) en negativo', 'somebody vs nobody', '¿Hay alguien? — No, no hay nadie.', 'No conozco a ______ en esta ciudad.', 'nadie'),
  ],
),

'posesivos': dict(
  level='a1', section='grammar', num='G14',
  short='Los Posesivos',
  title='Los Posesivos — Mi, Tu, Su, Nuestro',
  subtitle='Expresa posesión en español con adjetivos y pronombres posesivos',
  slides=[
    ('Adjetivos posesivos átonos', 'Los más usados en español',
     '<p class="slide-explanation">Los adjetivos posesivos átonos van <b>antes del sustantivo</b> y concuerdan en número (no siempre en género) con lo poseído:</p>'
     '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
     '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Poseedor</th><th style="padding:8px;text-align:left">Singular</th><th style="padding:8px;text-align:left">Plural</th></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">yo</td><td style="padding:8px"><b>mi</b> libro</td><td style="padding:8px"><b>mis</b> libros</td></tr>'
     '<tr><td style="padding:8px">tú</td><td style="padding:8px"><b>tu</b> casa</td><td style="padding:8px"><b>tus</b> casas</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">él/ella/usted</td><td style="padding:8px"><b>su</b> coche</td><td style="padding:8px"><b>sus</b> coches</td></tr>'
     '<tr><td style="padding:8px">nosotros/as</td><td style="padding:8px"><b>nuestro/a</b> perro/a</td><td style="padding:8px"><b>nuestros/as</b> perros/as</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">vosotros/as</td><td style="padding:8px"><b>vuestro/a</b> piso</td><td style="padding:8px"><b>vuestros/as</b> pisos</td></tr>'
     '<tr><td style="padding:8px">ellos/ustedes</td><td style="padding:8px"><b>su</b> hijo</td><td style="padding:8px"><b>sus</b> hijos</td></tr>'
     '</table>'),
    ('Concordancia: con lo poseído', None,
     '<p class="slide-explanation">Los posesivos concuerdan con el <b>objeto poseído</b>, no con el poseedor (excepto nuestro/vuestro que sí tienen formas de género):</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>mi</b> hermano / <b>mi</b> hermana (mi no cambia de género)</p>'
     '<p style="margin-top:8px"><b>mis</b> amigos / <b>mis</b> amigas (mi → mis en plural)</p>'
     '<p style="margin-top:8px"><b>nuestro</b> perro / <b>nuestra</b> gata (nuestro sí cambia)</p>'
     '<p style="margin-top:8px"><b>vuestros</b> amigos / <b>vuestras</b> amigas</p>'
     '</div>'
     '<p style="margin-top:12px">La pregunta clave: ¿cuántos son los objetos poseídos? → si son varios, añade -s.</p>'),
    ('Su: el posesivo ambiguo', None,
     '<p class="slide-explanation"><b>Su/sus</b> puede referirse a él, ella, usted, ellos o ustedes — para aclarar, se añade "de + pronombre":</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Su coche</b> → ambiguo: puede ser de él, de ella, de usted...</p>'
     '<p style="margin-top:8px">Para aclarar: <b>el coche de él</b> / <b>el coche de ella</b> / <b>el coche de usted</b></p>'
     '<p style="margin-top:8px">También: <b>¿Es este su libro?</b> — ¿de usted, de él, de ella...?</p>'
     '</div>'
     '<p style="margin-top:12px">En la práctica, el contexto suele aclarar a quién se refiere "su".</p>'),
    ('Tú vs. Tu — La tilde del pronombre', None,
     '<p class="slide-explanation">Un error muy frecuente: confundir el pronombre personal y el posesivo:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>tú</b> (con tilde) = pronombre personal: <b>Tú</b> eres mi amigo.</p>'
     '<p style="margin-top:8px"><b>tu</b> (sin tilde) = adjetivo posesivo: <b>Tu</b> amigo es muy simpático.</p>'
     '<p style="margin-top:8px"><b>mi</b> (sin tilde) = posesivo: <b>Mi</b> casa es grande.</p>'
     '<p style="margin-top:8px"><b>mí</b> (con tilde) = pronombre preposicional: Esto es para <b>mí</b>.</p>'
     '</div>'),
  ],
  traps=[
    ('Mi gusta el café.', '<strong>Me</strong> gusta el café.', '"Mi" es posesivo (mi libro). "Me" es pronombre de objeto indirecto (me gusta). Son palabras completamente diferentes.'),
    ('Esta es la casa de mi.', 'Esta es <strong>mi</strong> casa. / Esta es la casa <strong>mía</strong>.', 'No usamos "de + mi". Usamos el posesivo antepuesto (mi) o pospuesto (mía, tuya…).'),
    ('Nuestros padre trabaja mucho.', '<strong>Nuestro</strong> padre trabaja mucho.', '"Padre" es masculino singular → "nuestro" (no "nuestros").'),
    ('Tu eres muy simpático.', '<strong>Tú</strong> eres muy simpático.', '"Tú" pronombre lleva tilde. "Tu" sin tilde es el posesivo (tu libro).'),
    ('Sus padres de ella llegan mañana.', 'Los padres <strong>de ella</strong> llegan mañana. / <strong>Sus</strong> padres llegan mañana.', 'No se combina "sus" y "de ella" a la vez; se usa uno u otro.'),
  ],
  summary=[
    ('mi / mis', '1.ª pers. sing.', 'mi libro / mis libros'),
    ('tu / tus', '2.ª pers. sing.', 'tu casa / tus casas'),
    ('su / sus', '3.ª pers. sing. y pl.', 'su coche / sus coches'),
    ('nuestro/a/os/as', '1.ª pers. pl.', 'nuestro perro / nuestra gata'),
    ('vuestro/a/os/as', '2.ª pers. pl. (España)', 'vuestro piso / vuestras notas'),
    ('tú (pronombre) ≠ tu (posesivo)', 'tilde diferenciadora', 'Tú eres mi amigo. / Tu amigo es simpático.'),
  ],
  ex1=('Elige el posesivo correcto', 'Selecciona el adjetivo posesivo correcto.',
    [('______ libro está en la mochila. (de yo)',
      ['Mi', 'Me', 'Mis'],
      'Mi',
      '"Mi" es el posesivo de primera persona singular. "Libro" es singular → "mi".'),
     ('¿Cómo se llama ______ profesora? (de tú)',
      ['tu', 'tú', 'sus'],
      'tu',
      '"Tu" (sin tilde) es el posesivo de segunda persona singular.'),
     ('Carlos ha perdido ______ llaves. (de él)',
      ['sus', 'su', 'nuestras'],
      'sus',
      '"Sus" es el posesivo de tercera persona con sustantivo plural (llaves = varias).'),
     ('Vivimos en ______ nuevo apartamento. (de nosotros)',
      ['nuestro', 'nuestros', 'su'],
      'nuestro',
      '"Nuestro" concuerda con "apartamento" (masculino singular).'),
     ('¿Es este ______ móvil? (de vosotros)',
      ['vuestro', 'vuestra', 'vuestros'],
      'vuestro',
      '"Vuestro" + masculino singular = vuestro. "Móvil" es masculino.'),
     ('Ellos han venido con ______ hijos. (de ellos)',
      ['sus', 'su', 'nuestros'],
      'sus',
      '"Sus" = posesivo de tercera persona plural. "Hijos" es plural.'),
    ]),
  ex2=('Completa con el posesivo correcto', 'Escribe el posesivo apropiado.',
    [('______ hermana vive en Barcelona. (de yo)', 'Mi', '"Mi" es el posesivo de primera persona singular.'),
     ('¿Dónde están ______ padres? (de tú)', 'tus', '"Tus" = posesivo de segunda persona con sustantivo plural.'),
     ('Esta es ______ casa. (de nosotros, casa es femenino)', 'nuestra', '"Nuestra" concuerda con "casa" (femenino singular).'),
     ('Los estudiantes han olvidado ______ deberes. (de ellos)', 'sus', '"Sus" = posesivo de tercera persona plural con sustantivo plural.'),
     ('______ perro es muy grande. (de vosotros)', 'Vuestro', '"Vuestro" + masculino singular.'),
    ]),
  ex3=('Tú o tu, mi o mí', 'Elige la forma correcta.',
    [('______ eres muy amable.',
      ['Tú', 'Tu', 'Mi'],
      'Tú',
      '"Tú" con tilde es el pronombre personal sujeto.'),
     ('¿Es ______ mochila la roja?',
      ['tu', 'tú', 'su'],
      'tu',
      '"Tu" sin tilde es el posesivo. "Tu mochila" = your bag.'),
     ('Esto es para ______.',
      ['mí', 'mi', 'me'],
      'mí',
      '"Mí" con tilde es el pronombre preposicional: "para mí" (for me).'),
     ('______ coche está aparcado aquí.',
      ['Mi', 'Mí', 'Me'],
      'Mi',
      '"Mi" sin tilde es el posesivo (my car).'),
     ('¿______ hermana estudia medicina?',
      ['Tu', 'Tú', 'Su'],
      'Tu',
      '"Tu" sin tilde = tu hermana (your sister, posesivo ante sustantivo).'),
    ]),
  game_desc='4 posesivos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
  items=[
    ('mi-mis', 'mi / mis', 'posesivo de primera persona singular: mi (sing.) / mis (pl.)', 'de yo', 'Mi libro está en la mesa.', 'Tengo ______ mochila aquí.', 'mi'),
    ('tu-tus', 'tu / tus', 'posesivo de segunda persona singular: tu (sing.) / tus (pl.)', 'de tú', '¿Dónde está tu hermano?', 'He olvidado ______ llaves.', 'tus'),
    ('su-sus', 'su / sus', 'posesivo de tercera persona (él, ella, usted, ellos, ustedes)', 'de él/ella/usted', 'Su coche es muy caro.', 'Los niños han perdido ______ mochilas.', 'sus'),
    ('nuestro', 'nuestro/a/os/as', 'posesivo de primera persona plural — concuerda en género y número', 'de nosotros/as', 'Nuestra profesora es muy buena.', 'Vivimos en ______ piso. (masc.)', 'nuestro'),
    ('vuestro', 'vuestro/a/os/as', 'posesivo de segunda persona plural (España) — concuerda en género y número', 'de vosotros/as', '¿Es vuestra esta bicicleta?', '¿Dónde está ______ madre? (masc. sing.)', 'vuestro'),
    ('tu-tilde', 'tú ≠ tu', '"tú" con tilde = pronombre personal; "tu" sin tilde = posesivo', 'pronombre vs. posesivo', 'Tú eres muy inteligente. Tu hermano también.', '______ (you, sujeto) eres mi mejor amigo.', 'Tú'),
    ('mi-tilde', 'mi ≠ mí', '"mi" sin tilde = posesivo; "mí" con tilde = pronombre preposicional', 'posesivo vs. pronombre', 'Mi casa es grande. Esto es para mí.', 'Este regalo es para ______. (for me)', 'mí'),
    ('nuestro-conc', 'concordancia de nuestro', '"nuestro/a" cambia según género del sustantivo poseído', 'nuestro perro / nuestra casa', 'Nuestro piso es pequeño pero nuestra cocina es grande.', '______ (nuest-, fem.) hermana vive en Málaga.', 'Nuestra'),
  ],
),

'demostrativos': dict(
  level='a1', section='grammar', num='G15',
  short='Los Demostrativos',
  title='Los Demostrativos — Este, Ese, Aquel',
  subtitle='Señala objetos y personas según su distancia con este, ese y aquel',
  slides=[
    ('¿Qué son los demostrativos?', None,
     '<p class="slide-explanation">Los demostrativos señalan la <b>distancia</b> entre el hablante y el objeto o persona mencionada. En español hay tres series:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>este/esta/estos/estas</b> — aquí, cerca del hablante (this / these)</p>'
     '<p style="margin-top:8px"><b>ese/esa/esos/esas</b> — ahí, cerca del oyente (that / those)</p>'
     '<p style="margin-top:8px"><b>aquel/aquella/aquellos/aquellas</b> — allí, lejos de ambos (that ... over there)</p>'
     '</div>'
     '<p style="margin-top:16px">Los demostrativos concuerdan en <b>género y número</b> con el sustantivo al que acompañan.</p>'),
    ('Este / Esta / Estos / Estas', 'Cerca del hablante',
     '<p class="slide-explanation"><b>Este</b> y sus formas se usan para objetos o personas <b>próximos al hablante</b>:</p>'
     '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
     '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Género</th><th style="padding:8px;text-align:left">Singular</th><th style="padding:8px;text-align:left">Plural</th></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">Masculino</td><td style="padding:8px"><b>este</b> libro</td><td style="padding:8px"><b>estos</b> libros</td></tr>'
     '<tr><td style="padding:8px">Femenino</td><td style="padding:8px"><b>esta</b> mesa</td><td style="padding:8px"><b>estas</b> mesas</td></tr>'
     '</table>'
     '<p style="margin-top:12px">Ejemplos: <b>Este café está frío. Esta silla es cómoda. Estos zapatos son caros.</b></p>'),
    ('Ese / Aquel', 'Distancias medias y lejanas',
     '<p class="slide-explanation"><b>Ese</b> (distancia media) y <b>aquel</b> (distancia lejana):</p>'
     '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
     '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Género</th><th style="padding:8px;text-align:left">Ese (ahí)</th><th style="padding:8px;text-align:left">Aquel (allí)</th></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">Masc. sing.</td><td style="padding:8px">ese hombre</td><td style="padding:8px">aquel edificio</td></tr>'
     '<tr><td style="padding:8px">Fem. sing.</td><td style="padding:8px">esa mujer</td><td style="padding:8px">aquella montaña</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">Masc. pl.</td><td style="padding:8px">esos niños</td><td style="padding:8px">aquellos árboles</td></tr>'
     '<tr><td style="padding:8px">Fem. pl.</td><td style="padding:8px">esas flores</td><td style="padding:8px">aquellas casas</td></tr>'
     '</table>'),
    ('Demostrativos neutros: esto, eso, aquello', None,
     '<p class="slide-explanation">Los <b>demostrativos neutros</b> (esto, eso, aquello) no tienen género ni plural. Se usan para referirse a algo no identificado o a una idea:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¿Qué es esto?</b> — No sé qué es. (objeto no identificado)</p>'
     '<p style="margin-top:8px"><b>Eso es verdad.</b> (una idea o hecho)</p>'
     '<p style="margin-top:8px"><b>Aquello fue increíble.</b> (algo lejano en espacio o tiempo)</p>'
     '</div>'
     '<p style="margin-top:12px">Nota: los neutros nunca acompañan a un sustantivo; siempre funcionan solos como pronombres.</p>'),
  ],
  traps=[
    ('Este libro o este libro o esta libro?', '<strong>Este</strong> libro (masculino).', '"Libro" es masculino → "este" (masculino singular), no "esta".'),
    ('Estos sillas son nuevas.', '<strong>Estas</strong> sillas son nuevas.', '"Sillas" es femenino plural → "estas".'),
    ('¿Que es esto? (sin tilde)', '¿<strong>Qué</strong> es esto?', '"¿Qué?" interrogativo siempre lleva tilde.'),
    ('Aquel chica es mi prima.', '<strong>Aquella</strong> chica es mi prima.', '"Chica" es femenino → "aquella" (no "aquel").'),
    ('Este es correcto siempre con objetos cercanos?', 'Sí, <strong>este</strong> = cerca del hablante.', '"Este" señala lo que está cerca de quien habla; "ese" cerca del oyente; "aquel" lejos de ambos.'),
  ],
  summary=[
    ('este/esta', 'cerca del hablante', 'este libro / esta mesa'),
    ('estos/estas', 'cerca del hablante (plural)', 'estos libros / estas mesas'),
    ('ese/esa', 'cerca del oyente', 'ese coche / esa silla'),
    ('esos/esas', 'cerca del oyente (plural)', 'esos coches / esas sillas'),
    ('aquel/aquella', 'lejos de ambos', 'aquel edificio / aquella montaña'),
    ('aquellos/aquellas', 'lejos de ambos (plural)', 'aquellos árboles / aquellas casas'),
    ('esto / eso / aquello', 'neutros (sin sustantivo)', '¿Qué es esto? / Eso es verdad.'),
  ],
  ex1=('Elige el demostrativo correcto', 'Selecciona el demostrativo adecuado.',
    [('______ café está muy caliente. (el café está aquí, cerca de mí)',
      ['Este', 'Ese', 'Aquel'],
      'Este',
      'Cerca del hablante → "este" (masculino singular).'),
     ('______ chica de allí es mi amiga. (lejos de los dos)',
      ['Aquella', 'Esta', 'Esa'],
      'Aquella',
      'Lejos de ambos → "aquel-". "Chica" es femenino → "aquella".'),
     ('¿Puedes pasarme ______ sal? (la sal está cerca de ti)',
      ['esa', 'esta', 'aquella'],
      'esa',
      'Cerca del oyente → "ese/esa". "Sal" es femenino → "esa".'),
     ('______ libros son muy interesantes. (los libros están aquí, conmigo)',
      ['Estos', 'Esos', 'Aquellos'],
      'Estos',
      'Cerca del hablante, plural → "estos". "Libros" es masculino.'),
     ('______ montañas de allá son los Pirineos.',
      ['Aquellas', 'Esas', 'Estas'],
      'Aquellas',
      'Lejos de ambos, femenino plural → "aquellas".'),
     ('¿Qué es ______? — No sé, parece un insecto. (objeto desconocido)',
      ['esto', 'este', 'esta'],
      'esto',
      'Para objetos no identificados, se usa el neutro "esto".'),
    ]),
  ex2=('Completa con el demostrativo correcto', 'Escribe el demostrativo correcto.',
    [('______ zapatos son muy caros. (los zapatos están aquí, plural masculino)', 'Estos', 'Cerca del hablante, masculino plural → "estos".'),
     ('______ película es muy aburrida. (la película la estamos viendo juntos, femenino singular)', 'Esta', 'Cerca del hablante, femenino singular → "esta".'),
     ('Mira ______ casa de allí. (lejos, femenino singular)', 'aquella', 'Lejos de ambos, femenino singular → "aquella".'),
     ('¿Puedes coger ______ carpeta? (la carpeta está cerca de ti, femenino singular)', 'esa', 'Cerca del oyente, femenino singular → "esa".'),
     ('______ es lo que me preocupa. (referencia a una situación, neutro)', 'Eso', 'Para referirse a una idea o situación usamos el neutro "eso".'),
    ]),
  ex3=('Identifica el uso correcto', 'Elige la oración correcta.',
    [('¿Cuál es correcta?',
      ['Este ordenador es mío.', 'Esta ordenador es mío.', 'Estos ordenador es mío.'],
      'Este ordenador es mío.',
      '"Ordenador" es masculino singular → "este".'),
     ('¿Cuál es correcta?',
      ['Aquellas flores son preciosas.', 'Aquel flores son preciosas.', 'Aquella flores son preciosas.'],
      'Aquellas flores son preciosas.',
      '"Flores" es femenino plural → "aquellas".'),
     ('¿Cuándo usamos "esto", "eso" o "aquello"?',
      ['Cuando no sabemos el género del objeto o nos referimos a una idea', 'Siempre antes de un sustantivo', 'Solo en preguntas'],
      'Cuando no sabemos el género del objeto o nos referimos a una idea',
      'Los neutros (esto/eso/aquello) se usan solos, sin acompañar a un sustantivo con género.'),
     ('Quiero ______ libro que está en el estante de allí.',
      ['aquel', 'este', 'ese'],
      'aquel',
      'El libro está lejos de ambos → "aquel" (masculino singular).'),
     ('______ son mis amigos. (están aquí conmigo, masculino plural)',
      ['Estos', 'Esos', 'Aquellos'],
      'Estos',
      'Cerca del hablante, masculino plural → "estos".'),
    ]),
  game_desc='4 series de demostrativos · 3 rondas cada uno · llega a 100 puntos para ganar.',
  items=[
    ('este', 'este / esta', 'demostrativo singular para objetos cercanos al hablante', 'this (singular)', 'Este libro es muy bueno.', '______ casa es muy grande. (aquí, femenino)', 'Esta'),
    ('estos', 'estos / estas', 'demostrativo plural para objetos cercanos al hablante', 'these', 'Estos zapatos son muy cómodos.', '______ flores son muy bonitas. (aquí, femenino plural)', 'Estas'),
    ('ese', 'ese / esa', 'demostrativo singular para objetos cercanos al oyente', 'that (near listener)', '¿Puedes pasarme esa sal?', 'Ese ______ (hombre, cerca de ti) es mi vecino.', 'hombre'),
    ('aquel', 'aquel / aquella', 'demostrativo singular para objetos lejanos de ambos', 'that (far, over there)', 'Aquel edificio es muy antiguo.', '______ montaña de allí es el Teide. (femenino)', 'Aquella'),
    ('aquellos', 'aquellos / aquellas', 'demostrativo plural para objetos lejanos de ambos', 'those (far, over there)', 'Aquellos árboles son centenarios.', '______ casas de allá son muy antiguas. (fem. pl.)', 'Aquellas'),
    ('esto', 'esto / eso / aquello', 'demostrativos neutros — para objetos no identificados o ideas', 'this/that (neuter)', '¿Qué es esto? — No sé.', '______ es lo que más me gusta de España. (neutro, referencia general)', 'Eso'),
    ('concordancia', 'concordancia del demostrativo', 'el demostrativo concuerda en género y número con el sustantivo', 'género y número', 'Este hombre / esta mujer / estos niños / estas niñas.', '______ (lejano, fem. sing.) ciudad es muy bonita.', 'Aquella'),
    ('distancia', 'tres distancias', 'este = cerca del hablante; ese = cerca del oyente; aquel = lejos de ambos', 'aquí / ahí / allí', 'Este café, esa silla, aquel edificio.', '______ (cerca de ti) sombrero es tuyo?', '¿Ese'),
  ],
),

}
