# -*- coding: utf-8 -*-
"""espanol/ A2 Gramática — lote 3 (G11–G15)."""

CHAPTERS = {

'preterito-perfecto': dict(
  level='a2', section='grammar', num='G11',
  short='Pretérito Perfecto',
  title='El Pretérito Perfecto — Experiencias y Acciones Recientes',
  subtitle='Expresa acciones pasadas con HABER + participio: he hablado, has comido, ha vivido',
  slides=[
    ('¿Qué es el pretérito perfecto?', None,
     '<p class="slide-explanation">El <b>pretérito perfecto</b> (he hablado, has comido) expresa acciones pasadas que tienen <b>relación con el presente</b> o se sitúan en un período de tiempo no terminado (hoy, esta semana, este año). Se forma con <b>HABER + participio</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>He comido en ese restaurante tres veces.</b> (experiencia de vida)</p>'
     '<p style="margin-top:8px"><b>Hoy he llegado tarde al trabajo.</b> (acción de hoy)</p>'
     '<p style="margin-top:8px"><b>Este año hemos viajado mucho.</b> (período no terminado)</p>'
     '</div>'
     '<p style="margin-top:16px">Nota: En España, el perfecto compite con el indefinido. En Latinoamérica, el indefinido es mucho más frecuente para todas las acciones pasadas.</p>'),
    ('Formación: HABER + participio', None,
     '<p class="slide-explanation">El participio se forma añadiendo <b>-ado</b> (-AR) o <b>-ido</b> (-ER/-IR) al radical. Es invariable (no cambia de género/número):</p>'
     '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
     '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronombre</th><th style="padding:8px;text-align:left">HABER</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">yo</td><td style="padding:8px"><b>he</b></td><td style="padding:8px">He hablado con ella.</td></tr>'
     '<tr><td style="padding:8px">tú</td><td style="padding:8px"><b>has</b></td><td style="padding:8px">¿Has comido ya?</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">él/ella</td><td style="padding:8px"><b>ha</b></td><td style="padding:8px">Ella ha vivido en París.</td></tr>'
     '<tr><td style="padding:8px">nosotros</td><td style="padding:8px"><b>hemos</b></td><td style="padding:8px">Hemos terminado el proyecto.</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">vosotros</td><td style="padding:8px"><b>habéis</b></td><td style="padding:8px">¿Habéis visto la película?</td></tr>'
     '<tr><td style="padding:8px">ellos/ustedes</td><td style="padding:8px"><b>han</b></td><td style="padding:8px">Han llegado tarde.</td></tr>'
     '</table>'
     '<p style="margin-top:8px">Participios irregulares frecuentes: hacer → <b>hecho</b>, ver → <b>visto</b>, volver → <b>vuelto</b>, escribir → <b>escrito</b>, abrir → <b>abierto</b>, decir → <b>dicho</b>, poner → <b>puesto</b>, morir → <b>muerto</b>.</p>'),
    ('Marcadores temporales del perfecto', 'Cuándo se usa',
     '<p class="slide-explanation">El pretérito perfecto se usa habitualmente con estas expresiones temporales:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>ya</b> (already): ¿Ya has desayunado? — Sí, ya he desayunado.</p>'
     '<p style="margin-top:8px"><b>todavía no</b> (not yet): Todavía no he terminado.</p>'
     '<p style="margin-top:8px"><b>alguna vez / nunca</b> (ever / never): ¿Has estado alguna vez en Japón? — Nunca he estado allí.</p>'
     '<p style="margin-top:8px"><b>hoy, esta mañana, esta semana, este mes, este año</b>: Esta semana he trabajado mucho.</p>'
     '<p style="margin-top:8px"><b>recientemente / últimamente</b>: Últimamente he dormido muy poco.</p>'
     '</div>'),
    ('Perfecto vs. Indefinido', 'Una distinción clave',
     '<p class="slide-explanation">La elección entre perfecto e indefinido depende de si el período de tiempo está <b>terminado</b> o no:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Hoy he comido pasta.</b> (hoy = período no terminado → perfecto)</p>'
     '<p style="margin-top:8px"><b>Ayer comí pasta.</b> (ayer = período terminado → indefinido)</p>'
     '<p style="margin-top:8px"><b>Esta semana he viajado a Barcelona.</b> (esta semana = no terminada → perfecto)</p>'
     '<p style="margin-top:8px"><b>La semana pasada viajé a Barcelona.</b> (semana pasada = terminada → indefinido)</p>'
     '</div>'
     '<p style="margin-top:12px">Recuerda: en Latinoamérica, incluso "hoy" y "esta semana" pueden ir con indefinido en el habla cotidiana.</p>'),
  ],
  traps=[
    ('He ido allí ayer.', 'Fui allí <strong>ayer</strong>.', '"Ayer" es un marcador de tiempo terminado → indefinido. En España, "He ido ayer" existe en algunos dialectos, pero el estándar es "fui".'),
    ('Ha volvido a casa.', 'Ha <strong>vuelto</strong> a casa.', '"Volver" tiene participio irregular: vuelto. No existe "volvido".'),
    ('He comido. He estado cansado.', 'He comido. <strong>Estaba</strong> cansado.', 'Los estados durativos pasados (cansado, enfermo) prefieren el imperfecto, no el perfecto.'),
    ('¿Haz visto esta película?', '¿<strong>Has</strong> visto esta película?', 'El auxiliar de segunda persona singular es "has", no "haz".'),
    ('El año pasado he trabajado mucho.', 'El año pasado <strong>trabajé</strong> mucho.', '"El año pasado" es tiempo terminado → pretérito indefinido.'),
  ],
  summary=[
    ('yo he + participio', 'acción pasada reciente', 'He terminado el informe.'),
    ('tú has + participio', '2.ª persona sing.', '¿Has probado el gazpacho?'),
    ('él/ella ha + participio', '3.ª persona sing.', 'Ana ha llegado tarde.'),
    ('nosotros hemos + participio', '1.ª persona pl.', 'Hemos visitado el museo.'),
    ('participios irreg. clave', 'hecho, visto, vuelto, escrito', 'He hecho los deberes.'),
    ('ya / todavía no', 'marcadores típicos', '¿Ya has comido? — Todavía no.'),
  ],
  ex1=('Elige la forma correcta del pretérito perfecto', 'Selecciona la opción correcta.',
    [('Yo ______ con mi jefe esta mañana. (hablar)',
      ['he hablado', 'hablé', 'había hablado'],
      'he hablado',
      '"Esta mañana" (período no terminado en España) → pretérito perfecto. "He hablado."'),
     ('¿Tú ______ alguna vez gazpacho? (probar)',
      ['has probado', 'probaste', 'habías probado'],
      'has probado',
      '"Alguna vez" es marcador del perfecto para expresar experiencias. "Has probado."'),
     ('Ella ______ a las ocho. (llegar)',
      ['ha llegado', 'llegó', 'llega'],
      'ha llegado',
      'Acción reciente referida al presente → "ha llegado".'),
     ('Nosotros ______ la reunión. (terminar)',
      ['hemos terminado', 'terminamos', 'habíamos terminado'],
      'hemos terminado',
      'Acción completada con resultado en el presente → "hemos terminado".'),
     ('¿Vosotros ______ la nueva película? (ver)',
      ['habéis visto', 'visteis', 'habéis vido'],
      'habéis visto',
      '"Ver" tiene participio irregular "visto". Con "vosotros" → "habéis visto".'),
     ('Ellos ______ el problema. (resolver)',
      ['han resuelto', 'resolvieron', 'han resolvido'],
      'han resuelto',
      '"Resolver" tiene participio irregular "resuelto". "Han resuelto."'),
    ]),
  ex2=('Conjuga en pretérito perfecto', 'Escribe la forma correcta.',
    [('¿Tú ______ (hacer) los deberes?', 'has hecho', '"Tú" → "has". "Hacer" → participio irregular "hecho".'),
     ('Nosotros ______ (escribir) el informe.', 'hemos escrito', '"Nosotros" → "hemos". "Escribir" → "escrito".'),
     ('Ella ______ (volver) de sus vacaciones.', 'ha vuelto', '"Ella" → "ha". "Volver" → "vuelto".'),
     ('Yo nunca ______ (estar) en Tokio.', 'he estado', '"Nunca" marcador del perfecto. "Yo" → "he". "Estar" → "estado".'),
     ('¿Vosotros ya ______ (comer)?', 'habéis comido', '"Ya" marcador del perfecto. "Vosotros" → "habéis". "Comer" → "comido".'),
    ]),
  ex3=('¿Perfecto o indefinido?', 'Elige el tiempo verbal correcto.',
    [('______ (yo, ir) al cine ayer.',
      ['Fui', 'He ido', 'Había ido'],
      'Fui',
      '"Ayer" = tiempo terminado → pretérito indefinido. "Fui."'),
     ('Este mes ______ (nosotros, viajar) mucho.',
      ['hemos viajado', 'viajamos', 'viajábamos'],
      'hemos viajado',
      '"Este mes" = período no terminado → pretérito perfecto. "Hemos viajado."'),
     ('¿______ (tú, alguna vez, probar) el mole?',
      ['Has probado', 'Probaste', 'Probabas'],
      'Has probado',
      '"Alguna vez" = marcador del perfecto para experiencias. "Has probado."'),
     ('La semana pasada ______ (ellos, trabajar) mucho.',
      ['trabajaron', 'han trabajado', 'trabajaban'],
      'trabajaron',
      '"La semana pasada" = período terminado → indefinido. "Trabajaron."'),
     ('Todavía no ______ (yo, abrir) el correo.',
      ['he abierto', 'abrí', 'abría'],
      'he abierto',
      '"Todavía no" = marcador del perfecto. "Abrir" → "abierto". "He abierto."'),
    ]),
  game_desc='4 elementos del pretérito perfecto · 3 rondas cada uno · llega a 100 puntos para ganar.',
  items=[
    ('he', 'he / has / ha / hemos / habéis / han', 'formas del auxiliar HABER para el pretérito perfecto', 'verbo auxiliar', 'He comido demasiado hoy.', 'Nosotros ______ (haber, 1.ª pl.) terminado.', 'hemos'),
    ('participio-reg', 'participio regular', '-AR → -ado; -ER/-IR → -ido. Invariable.', '-ado / -ido', 'He hablado, has comido, ha vivido.', 'Ella ha ______ (escribir — irregular)', 'escrito'),
    ('hecho', 'hecho (hacer)', 'participio irregular de HACER', 'hacer → hecho', '¿Has hecho los deberes?', 'Todavía no he ______ la tarea.', 'hecho'),
    ('visto', 'visto (ver)', 'participio irregular de VER', 'ver → visto', 'Hemos visto una película increíble.', '¿Has ______ a Carlos últimamente?', 'visto'),
    ('ya-todavia', 'ya / todavía no', 'marcadores temporales del pretérito perfecto: ya (already), todavía no (not yet)', 'already / not yet', '¿Ya has desayunado? — Todavía no.', '______ no he terminado el proyecto.', 'Todavía'),
    ('alguna-vez', 'alguna vez / nunca', 'marcadores de experiencia con el pretérito perfecto', 'ever / never', '¿Has estado alguna vez en Lisboa?', 'Nunca he ______ (comer) sushi.', 'comido'),
    ('vuelto', 'vuelto (volver)', 'participio irregular de VOLVER', 'volver → vuelto', 'Mis padres han vuelto de viaje.', '¿Ha ______ (volver) ya tu hermana?', 'vuelto'),
    ('hoy-este', 'hoy / esta semana / este año', 'períodos no terminados que piden pretérito perfecto (en España)', 'tiempo reciente no concluido', 'Hoy he trabajado mucho. Este año hemos viajado por Europa.', 'Este mes ______ (yo, estudiar) mucho.', 'he estudiado'),
  ],
),

'conjunciones': dict(
  level='a2', section='grammar', num='G12',
  short='Las Conjunciones',
  title='Las Conjunciones — Conectores del Español',
  subtitle='Conecta ideas con y, pero, sino, porque, aunque, cuando, si y que',
  slides=[
    ('Conjunciones coordinantes', 'Conectan elementos del mismo nivel',
     '<p class="slide-explanation">Las conjunciones <b>coordinantes</b> unen palabras, frases u oraciones del mismo rango gramatical:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>y / e</b> (and): Me gusta el café <b>y</b> el té. / María <b>e</b> Isabel. (ante i-/hi-)</p>'
     '<p style="margin-top:8px"><b>o / u</b> (or): ¿Quieres té <b>o</b> café? / siete <b>u</b> ocho. (ante o-/ho-)</p>'
     '<p style="margin-top:8px"><b>pero</b> (but): Me gusta el chocolate <b>pero</b> no lo como mucho.</p>'
     '<p style="margin-top:8px"><b>sino</b> (but rather, instead): No quiero café, <b>sino</b> té. (tras negación, elemento diferente)</p>'
     '<p style="margin-top:8px"><b>ni</b> (nor / not even): No como <b>ni</b> carne <b>ni</b> pescado.</p>'
     '</div>'),
    ('Pero vs. Sino', 'Una distinción esencial',
     '<p class="slide-explanation"><b>Pero</b> y <b>sino</b> se traducen ambas como "but", pero tienen usos diferentes:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Pero</b>: introduce un contraste o restricción. El primer elemento puede ser positivo o negativo:</p>'
     '<p style="margin-top:8px">— Es inteligente, <b>pero</b> no estudia.</p>'
     '<p style="margin-top:8px"><b>Sino</b>: reemplaza el elemento negado. Solo tras negación, introduce la alternativa real:</p>'
     '<p style="margin-top:8px">— No es médico, <b>sino</b> enfermero.</p>'
     '<p style="margin-top:8px">— No quiero ir al cine, <b>sino</b> (que quiero ir) al teatro.</p>'
     '</div>'),
    ('Conjunciones subordinantes causales y concesivas', None,
     '<p class="slide-explanation">Para expresar causas y concesiones:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>porque</b> (because): No fui a clase <b>porque</b> estaba enfermo.</p>'
     '<p style="margin-top:8px"><b>como</b> (since, as): <b>Como</b> no tenía dinero, no pude ir. (va al principio)</p>'
     '<p style="margin-top:8px"><b>aunque</b> (although / even though / even if): <b>Aunque</b> está cansado, trabaja mucho.</p>'
     '</div>'
     '<p style="margin-top:12px">Atención: <b>¿por qué?</b> (pregunta) / <b>porque</b> (respuesta) / <b>el porqué</b> (sustantivo: the reason).</p>'),
    ('Conjunciones temporales y condicionales', None,
     '<p class="slide-explanation">Para secuenciar o condicionar acciones:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>cuando</b> (when): Llámame <b>cuando</b> llegues. / <b>Cuando</b> era joven, jugaba al fútbol.</p>'
     '<p style="margin-top:8px"><b>si</b> (if): <b>Si</b> tienes tiempo, ven a visitarme. (condicional real)</p>'
     '<p style="margin-top:8px"><b>que</b> (that): Creo <b>que</b> tienes razón. / Me alegra <b>que</b> estés bien.</p>'
     '<p style="margin-top:8px"><b>antes de / después de</b> + infinitivo: <b>Antes de</b> salir, apaga las luces.</p>'
     '</div>'),
  ],
  traps=[
    ('Me gustan los libros e el cine.', 'Me gustan los libros <strong>y</strong> el cine.', '"E" solo se usa ante palabras que empiezan por i- o hi-. "El" empieza por e, no i → se usa "y".'),
    ('No es español, pero italiano.', 'No es español, <strong>sino</strong> italiano.', 'Tras negación, cuando se introduce la alternativa real, se usa "sino", no "pero".'),
    ('Aunque, estudia mucho pero no aprueba.', '<strong>Aunque</strong> estudia mucho, <strong>no</strong> aprueba.', '"Aunque" es suficiente para expresar el contraste. No añadas "pero" en la misma oración.'),
    ('Porque no tenía dinero, no fui.', '<strong>Como</strong> no tenía dinero, no fui.', 'Cuando la causa precede al resultado, se prefiere "como" al principio. "Porque" va normalmente después.'),
    ('¿Por que estudias español?', '¿<strong>Por qué</strong> estudias español?', '"¿Por qué?" lleva tilde. "Porque" (sin tilde) es la respuesta. Son palabras diferentes.'),
  ],
  summary=[
    ('y / e', 'adición (and)', 'café y té / María e Isabel'),
    ('o / u', 'alternativa (or)', '¿té o café? / siete u ocho'),
    ('pero', 'contraste (but)', 'es lista, pero no estudia'),
    ('sino', 'sustitución tras negación', 'no café, sino té'),
    ('porque', 'causa (because)', 'No fui porque estaba enfermo.'),
    ('aunque', 'concesión (although)', 'Aunque llueve, salgo.'),
    ('cuando / si', 'tiempo / condición', 'Cuando llegues, llámame.'),
  ],
  ex1=('Elige la conjunción correcta', 'Selecciona la conjunción adecuada.',
    [('No es médico, ______ enfermero.',
      ['sino', 'pero', 'aunque'],
      'sino',
      'Tras negación, se introduce la alternativa real con "sino".'),
     ('Estudio mucho ______ no apruebo los exámenes.',
      ['pero', 'sino', 'porque'],
      'pero',
      '"Pero" introduce un contraste sin reemplazar el primer elemento.'),
     ('No como ni carne ______ pescado.',
      ['ni', 'o', 'e'],
      'ni',
      '"Ni ... ni ..." es la estructura de negación doble (neither ... nor ...).'),
     ('Me gusta el cine ______ el teatro.',
      ['y', 'e', 'sino'],
      'y',
      '"El teatro" no empieza por i- → se usa "y" (no "e").'),
     ('No fui a la fiesta ______ estaba cansado.',
      ['porque', 'pero', 'aunque'],
      'porque',
      '"Porque" introduce la causa.'),
     ('______ hace frío, salgo a correr.',
      ['Aunque', 'Porque', 'Sino'],
      'Aunque',
      '"Aunque" introduce una concesión (= even though / despite).'),
    ]),
  ex2=('Completa con la conjunción correcta', 'Escribe la conjunción apropiada.',
    [('No quiero té, ______ café.', 'sino', 'Tras negación + alternativa real → "sino".'),
     ('¿Prefieres ir al cine ______ al teatro?', 'o', 'Alternativa → "o".'),
     ('Creo ______ tienes razón.', 'que', '"Que" introduce una oración subordinada complementaria.'),
     ('Me gusta el fútbol ______ el baloncesto.', 'y', 'Suma dos elementos → "y".'),
     ('No fui ______ no tenía tiempo.', 'porque', '"Porque" introduce la causa.'),
    ]),
  ex3=('Pero vs. Sino y otras distinciones', 'Elige la opción correcta.',
    [('¿Cuándo se usa "sino" en vez de "pero"?',
      ['Tras una negación, para introducir la alternativa real', 'Siempre que queremos decir "but"', 'Solo en preguntas'],
      'Tras una negación, para introducir la alternativa real',
      '"Sino" solo se usa cuando la primera parte es negativa y se quiere dar la alternativa verdadera.'),
     ('¿Cuándo se usa "e" en vez de "y"?',
      ['Ante palabras que empiezan por i- o hi-', 'Ante cualquier vocal', 'Siempre en lenguaje formal'],
      'Ante palabras que empiezan por i- o hi-',
      '"E" reemplaza a "y" para evitar la cacofonía: "padres e hijos" (no "padres y hijos").'),
     ('¿Cuál es la diferencia entre "aunque" y "pero"?',
      ['"Aunque" admite que la condición existe y aun así; "pero" simplemente contrasta', 'Son sinónimos perfectos', '"Pero" es más formal'],
      '"Aunque" admite que la condición existe y aun así; "pero" simplemente contrasta',
      '"Aunque llueve, salgo" = Despite the rain, I go out. "Pero" no implica esa concesión implícita.'),
     ('Completa: No es simpático, ______ es honesto.',
      ['pero', 'sino', 'aunque'],
      'pero',
      'La primera parte no está negando una característica para dar la alternativa → se usa "pero".'),
     ('______ era pequeño, mi familia vivía en el campo.',
      ['Cuando', 'Porque', 'Sino'],
      'Cuando',
      '"Cuando" introduce el tiempo. "Cuando era pequeño" = when I was little.'),
    ]),
  game_desc='4 conjunciones clave del español A2 · 3 rondas cada uno · llega a 100 puntos para ganar.',
  items=[
    ('pero', 'pero', 'conjunción de contraste (but) — no implica sustitución', 'sin embargo', 'Es lista pero no estudia.', 'Me gusta el chocolate ______ no lo tomo mucho.', 'pero'),
    ('sino', 'sino', 'sustitución tras negación (but rather) — introduce la alternativa real', 'en cambio', 'No quiero café, sino té.', 'No es abogada, ______ médica.', 'sino'),
    ('aunque', 'aunque', 'conjunción concesiva (although / even though) — el hablante admite el obstáculo', 'a pesar de que', 'Aunque llueve, salgo a correr.', '______ estaba cansado, terminó el trabajo.', 'Aunque'),
    ('porque', 'porque', 'conjunción causal (because) — introduce la razón de la acción principal', 'ya que', 'No fui porque estaba enfermo.', 'Llegué tarde ______ había mucho tráfico.', 'porque'),
    ('y-e', 'y / e', 'conjunción de adición (and) — "e" ante i-/hi-', 'además', 'Compré pan y leche. / España e Italia son países mediterráneos.', 'María ______ Isabel son amigas. (ante i-)', 'e'),
    ('o-u', 'o / u', 'conjunción disyuntiva (or) — "u" ante o-/ho-', 'o bien', '¿Café o té? / siete u ocho.', '¿Vienes ______ te quedas? (ante e/a)', 'o'),
    ('cuando', 'cuando', 'conjunción temporal (when) — introduce una oración temporal', 'en el momento en que', 'Llámame cuando llegues.', 'Estudiaré más ______ tenga tiempo.', 'cuando'),
    ('que', 'que', 'conjunción completiva (that) — introduce oraciones subordinadas completivas', 'that (completive)', 'Creo que tienes razón.', 'Espero ______ vengas mañana.', 'que'),
  ],
),

'cuantificadores': dict(
  level='a2', section='grammar', num='G13',
  short='Los Cuantificadores',
  title='Los Cuantificadores — Mucho, Poco, Bastante, Demasiado',
  subtitle='Expresa cantidad con mucho, poco, bastante, demasiado, muy, todo y alguno',
  slides=[
    ('Mucho, poco, bastante, demasiado', 'Con sustantivos y verbos',
     '<p class="slide-explanation">Estos cuantificadores concuerdan con el sustantivo en género y número cuando lo acompañan. Con verbos, van en forma invariable:</p>'
     '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
     '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Cuantificador</th><th style="padding:8px;text-align:left">+ sustantivo</th><th style="padding:8px;text-align:left">+ verbo</th></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">mucho/a/os/as</td><td style="padding:8px">mucho tiempo / mucha gente</td><td style="padding:8px">Trabajo mucho.</td></tr>'
     '<tr><td style="padding:8px">poco/a/os/as</td><td style="padding:8px">poco dinero / poca agua</td><td style="padding:8px">Duermes poco.</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">bastante/s</td><td style="padding:8px">bastante comida / bastantes coches</td><td style="padding:8px">Llueve bastante.</td></tr>'
     '<tr><td style="padding:8px">demasiado/a/os/as</td><td style="padding:8px">demasiado ruido</td><td style="padding:8px">Comes demasiado.</td></tr>'
     '</table>'),
    ('Muy vs. Mucho', 'Un error muy frecuente',
     '<p class="slide-explanation"><b>Muy</b> (very) modifica adjetivos y adverbios. <b>Mucho</b> modifica verbos, sustantivos o funciona como adverbio de intensidad:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>muy</b> + adjetivo: Es <b>muy</b> inteligente. Está <b>muy</b> bien.</p>'
     '<p style="margin-top:8px"><b>muy</b> + adverbio: Hablas <b>muy</b> rápido.</p>'
     '<p style="margin-top:8px"><b>mucho</b> + verbo: Trabaja <b>mucho</b>. Me gusta <b>mucho</b>.</p>'
     '<p style="margin-top:8px"><b>mucho/a/os/as</b> + sustantivo: Tengo <b>mucho</b> trabajo. Hay <b>mucha</b> gente.</p>'
     '</div>'
     '<p style="margin-top:12px">Truco: nunca digas "muy mucho" ni "mucho bien". Elige uno.</p>'),
    ('Todo, todos, alguno, ninguno', 'Cuantificadores totales y parciales',
     '<p class="slide-explanation">Cuantificadores que indican totalidad o ausencia:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>todo el / toda la / todos los / todas las</b> (all / the whole): <b>Todo el</b> día estudié. <b>Todas las</b> manzanas son rojas.</p>'
     '<p style="margin-top:8px"><b>algún / alguno / alguna / algunos / algunas</b> (some / any): ¿Tienes <b>algún</b> bolígrafo? Tengo <b>algunas</b> ideas.</p>'
     '<p style="margin-top:8px"><b>ningún / ninguno / ninguna</b> (no / none / not any): No tengo <b>ningún</b> problema. <b>Ninguna</b> de las respuestas es correcta.</p>'
     '</div>'),
    ('Suficiente y demás cuantificadores', None,
     '<p class="slide-explanation">Más cuantificadores útiles para el nivel A2:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>suficiente/s</b> (enough): Tengo <b>suficiente</b> dinero. No hay <b>suficientes</b> sillas.</p>'
     '<p style="margin-top:8px"><b>varios / varias</b> (several): He leído <b>varios</b> libros.</p>'
     '<p style="margin-top:8px"><b>tanto/a/os/as</b> (so much / so many): Hay <b>tanta</b> gente. No tengo <b>tanto</b> tiempo.</p>'
     '<p style="margin-top:8px"><b>cada</b> (each / every): <b>Cada</b> alumno tiene un libro. Me llama <b>cada</b> día.</p>'
     '</div>'),
  ],
  traps=[
    ('Es muy alto mucho.', 'Es <strong>muy</strong> alto.', '"Muy" y "mucho" no se combinan. "Muy" modifica adjetivos; "mucho" modifica verbos o sustantivos.'),
    ('Trabajo muy.', 'Trabajo <strong>mucho</strong>.', '"Muy" no puede ir solo ante un verbo. Usa "mucho" para modificar verbos.'),
    ('Hay muchos gente.', 'Hay <strong>mucha</strong> gente.', '"Gente" es femenino singular → "mucha" (no "muchos").'),
    ('Tengo bastante libros.', 'Tengo <strong>bastantes</strong> libros.', '"Bastante" concuerda en número: "bastantes" ante sustantivo plural.'),
    ('No tengo algún problema.', 'No tengo <strong>ningún</strong> problema.', 'En oraciones negativas, "algún" pasa a ser "ningún".'),
  ],
  summary=[
    ('mucho/a + sust.', 'cantidad grande', 'mucho tiempo / mucha gente / muchos libros'),
    ('mucho (adv.)', 'modifica verbos', 'Trabaja mucho. Me gusta mucho.'),
    ('muy + adj./adv.', 'intensificador', 'muy alto, muy bien, muy rápido'),
    ('poco/a + sust.', 'cantidad pequeña', 'poco dinero / poca agua'),
    ('demasiado/a', 'exceso', 'demasiado ruido / demasiada sal'),
    ('bastante/s', 'cantidad suficiente o considerable', 'bastante comida / bastantes personas'),
    ('todo el / toda la', 'totalidad', 'todo el día / toda la semana'),
    ('algún / ningún', 'existencia / ausencia', '¿Algún problema? / Ningún problema.'),
  ],
  ex1=('Elige el cuantificador correcto', 'Selecciona el cuantificador adecuado.',
    [('Hay ______ personas en la cola.',
      ['muchas', 'mucho', 'muy'],
      'muchas',
      '"Personas" es femenino plural → "muchas".'),
     ('Habla ______ rápido. No le entiendo.',
      ['muy', 'mucho', 'muchos'],
      'muy',
      '"Muy" modifica adverbios como "rápido".'),
     ('No tengo ______ dinero este mes.',
      ['mucho', 'muchos', 'muy'],
      'mucho',
      '"Dinero" es masculino singular → "mucho dinero".'),
     ('¿Tienes ______ bolígrafo para prestarme?',
      ['algún', 'ningún', 'mucho'],
      'algún',
      'En pregunta positiva → "algún" (some/any). Ante masculino singular: "algún".'),
     ('Este trabajo es ______ difícil.',
      ['muy', 'mucho', 'demasiados'],
      'muy',
      '"Muy" modifica adjetivos como "difícil".'),
     ('Como ______ por las noches. No es bueno.',
      ['demasiado', 'demasiados', 'muy'],
      'demasiado',
      '"Demasiado" modifica verbos (invariable) = too much.'),
    ]),
  ex2=('Muy o mucho', 'Escribe la forma correcta del cuantificador.',
    [('Esta película es ______ interesante.', 'muy', '"Muy" modifica adjetivos. "Interesante" es adjetivo.'),
     ('Ella trabaja ______ todos los días.', 'mucho', '"Mucho" modifica verbos (invariable con verbos).'),
     ('Tengo ______ (mucho, fem.) hambre.', 'mucha', '"Hambre" es femenino → "mucha hambre".'),
     ('Hay ______ tráfico hoy.', 'mucho', '"Tráfico" es masculino singular → "mucho tráfico".'),
     ('Corres ______ rápido.', 'muy', '"Muy" modifica el adverbio "rápido".'),
    ]),
  ex3=('Todo, alguno, ninguno', 'Elige la forma correcta.',
    [('______ los estudiantes han aprobado.',
      ['Todos', 'Todo', 'Toda'],
      'Todos',
      '"Los estudiantes" es masculino plural → "todos los estudiantes".'),
     ('No tengo ______ problema con eso.',
      ['ningún', 'algún', 'mucho'],
      'ningún',
      'Oración negativa + masculino singular → "ningún".'),
     ('Pasé ______ la noche estudiando.',
      ['toda', 'todas', 'todo'],
      'toda',
      '"La noche" es femenino singular → "toda la noche".'),
     ('¿Tienes ______ idea de dónde está?',
      ['alguna', 'ninguna', 'mucha'],
      'alguna',
      'Pregunta → "alguna". "Idea" es femenino singular → "alguna idea".'),
     ('¿Hay ______ sillas libres?',
      ['algunas', 'algún', 'varios'],
      'algunas',
      '"Sillas" es femenino plural → "algunas sillas".'),
    ]),
  game_desc='4 cuantificadores esenciales · 3 rondas cada uno · llega a 100 puntos para ganar.',
  items=[
    ('mucho-sust', 'mucho/a/os/as + sustantivo', 'cuantificador de cantidad grande — concuerda con el sustantivo', 'mucho/a', 'Tengo mucho trabajo y muchas reuniones.', 'Hay ______ gente en el mercado. (fem. sing.)', 'mucha'),
    ('mucho-verbo', 'mucho (adverbio)', 'modifica verbos: expresa una cantidad o grado elevado de la acción', 'a lot', 'Trabajo mucho y duermo poco.', 'Me gusta ______ la música española.', 'mucho'),
    ('muy', 'muy', 'intensificador para adjetivos y adverbios — NUNCA ante sustantivos o verbos', 'very', 'Es muy inteligente. Hablas muy rápido.', 'Este ejercicio es ______ difícil.', 'muy'),
    ('poco', 'poco/a/os/as', 'cuantificador de cantidad pequeña — concuerda con el sustantivo', 'not much / few', 'Tengo poco tiempo y pocas ideas.', 'Hay ______ agua en la botella. (fem.)', 'poca'),
    ('demasiado', 'demasiado/a/os/as', 'expresa exceso — concuerda con sustantivo o es invariable con verbos', 'too much / too many', 'Comes demasiado. Hay demasiado ruido.', 'Hablas ______ rápido. (con adverbio → muy/demasiado)', 'demasiado'),
    ('bastante', 'bastante/s', 'cantidad suficiente o considerable — concuerda en número', 'enough / quite', 'Hay bastante comida para todos.', 'Tenemos ______ tiempo para terminar. (singular)', 'bastante'),
    ('todo', 'todo/a/os/as', 'totalidad — concuerda con el sustantivo. Todo el / toda la + singular', 'all / every', 'Todos los estudiantes estudian mucho.', '______ la noche estuvo lloviendo. (fem. sing.)', 'Toda'),
    ('algun', 'algún / alguno/a', 'existencia indefinida (some/any) — algún ante masc. sing.', 'some / any (positive)', '¿Tienes algún problema?', 'No tengo ______ (masc. sing.) bolígrafo.', 'ningún'),
  ],
),

'oraciones-relativas': dict(
  level='a2', section='grammar', num='G14',
  short='Oraciones de Relativo',
  title='Oraciones de Relativo — Que, Donde, Quien',
  subtitle='Describe y especifica con cláusulas relativas: el libro que leí, la ciudad donde vivo',
  slides=[
    ('¿Qué es una oración de relativo?', None,
     '<p class="slide-explanation">Una <b>oración de relativo</b> es una oración que describe o identifica a un sustantivo (el antecedente). El pronombre relativo <b>conecta</b> las dos oraciones:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>El libro — Leí el libro — <b>El libro que leí</b> es muy bueno.</p>'
     '<p style="margin-top:8px">La chica — La chica trabaja aquí — <b>La chica que trabaja aquí</b> es mi amiga.</p>'
     '<p style="margin-top:8px">El hotel — Dormimos en el hotel — <b>El hotel donde dormimos</b> era barato.</p>'
     '</div>'
     '<p style="margin-top:16px">Los pronombres relativos más frecuentes: <b>que, donde, quien/quienes</b>.</p>'),
    ('QUE — el relativo más frecuente', None,
     '<p class="slide-explanation"><b>Que</b> es el pronombre relativo más usado. Se refiere tanto a <b>personas como a cosas</b>, y no varía en género ni número:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>La película <b>que</b> vi ayer era genial. (cosa)</p>'
     '<p style="margin-top:8px">El profesor <b>que</b> me enseña español es muy paciente. (persona)</p>'
     '<p style="margin-top:8px">Los amigos <b>que</b> vinieron a la fiesta eran diez. (personas, pl.)</p>'
     '<p style="margin-top:8px">Las ideas <b>que</b> presentó eran muy originales. (cosas, pl.)</p>'
     '</div>'
     '<p style="margin-top:12px">Nota: en español, el relativo "que" no puede omitirse, al contrario que en inglés ("the book I read" → "el libro <b>que</b> leí").</p>'),
    ('DONDE — lugar, y QUIEN — personas', None,
     '<p class="slide-explanation"><b>Donde</b> se usa para lugares; <b>quien/quienes</b> para personas (generalmente tras preposición o en frases explicativas):</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>donde</b> (where): La ciudad <b>donde</b> nací es Bogotá. / El restaurante <b>donde</b> comemos es excelente.</p>'
     '<p style="margin-top:8px"><b>quien / quienes</b> (who / whom): La mujer <b>con quien</b> hablé es directora. / Los estudiantes <b>de quienes</b> te hablé han ganado el premio.</p>'
     '</div>'
     '<p style="margin-top:12px">En el habla cotidiana, "donde" puede reemplazarse por "en que" y "quien" por "que" sin mayor cambio de sentido.</p>'),
    ('Relativas especificativas y explicativas', None,
     '<p class="slide-explanation">Hay dos tipos de oraciones de relativo, con distinto significado:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Especificativa</b> (sin comas): identifica al antecedente — no todos, sino los que cumplen la condición:</p>'
     '<p style="margin-top:4px">El estudiante <b>que</b> llegó tarde no pudo entrar. (= el estudiante específico que llegó tarde)</p>'
     '<p style="margin-top:12px"><b>Explicativa</b> (entre comas): añade información sobre un antecedente ya identificado:</p>'
     '<p style="margin-top:4px">Carlos, <b>que</b> es mi hermano, vive en Valencia. (= Carlos, que por cierto es mi hermano)</p>'
     '</div>'),
  ],
  traps=[
    ('El libro cual leí es bueno.', 'El libro <strong>que</strong> leí es bueno.', 'En oraciones especificativas, se usa "que", no "cual". "El cual" se usa en registros formales y en relativas explicativas.'),
    ('La ciudad que vivo es bonita.', 'La ciudad <strong>donde</strong> vivo es bonita.', 'Para expresar lugar, se usa "donde" (o "en la que"), no solo "que".'),
    ('El hombre que su coche es rojo.', 'El hombre <strong>cuyo</strong> coche es rojo. / El hombre que tiene el coche rojo.', '"Que su..." es incorrecto. Para posesión en relativas se usa "cuyo/a/os/as" o se reformula.'),
    ('La chica que hablé ayer es mi prima.', 'La chica <strong>con quien</strong> (/ con la que) hablé ayer es mi prima.', 'Cuando hay preposición, debe ir delante del relativo: "con quien", "de que", "en el que"...'),
    ('El libro leí es muy bueno.', 'El libro <strong>que</strong> leí es muy bueno.', 'En español, el relativo "que" no puede omitirse, a diferencia del inglés.'),
  ],
  summary=[
    ('que', 'personas y cosas', 'El libro que leí / La persona que llamó'),
    ('donde', 'lugar', 'La ciudad donde vivo / El hotel donde dormimos'),
    ('quien / quienes', 'personas (tras preposición o en explicativas)', 'La mujer con quien hablé'),
    ('especificativa', 'sin comas — identifica', 'El alumno que aprobó salió primero.'),
    ('explicativa', 'entre comas — añade info', 'Ana, que es mi amiga, vive en Málaga.'),
    ('que no se omite', 'al contrario que en inglés', '"The book I read" → "el libro que leí"'),
  ],
  ex1=('Elige el pronombre relativo correcto', 'Selecciona el pronombre relativo adecuado.',
    [('El restaurante ______ comemos siempre es excelente.',
      ['donde', 'que', 'quien'],
      'donde',
      '"Donde" se usa para lugares. El restaurante es un lugar.'),
     ('La película ______ vimos anoche era muy buena.',
      ['que', 'donde', 'quien'],
      'que',
      '"Que" es el relativo universal para cosas (y personas). "La película que vimos."'),
     ('El profesor ______ me enseña español es muy paciente.',
      ['que', 'donde', 'cual'],
      'que',
      '"Que" se usa para personas en relativas especificativas.'),
     ('La ciudad ______ nació mi abuela tiene muchos monumentos.',
      ['donde', 'que', 'quien'],
      'donde',
      '"Donde" para lugares: la ciudad donde nació.'),
     ('La mujer ______ hablé ayer es la directora.',
      ['con quien', 'que', 'donde'],
      'con quien',
      'Con preposición antes del relativo + persona → "con quien".'),
     ('Los estudiantes ______ aprobaron salieron contentos.',
      ['que', 'quienes', 'donde'],
      'que',
      '"Que" funciona con personas en relativas especificativas (plural también).'),
    ]),
  ex2=('Combina las oraciones con un relativo', 'Escribe la oración combinada correctamente.',
    [('El libro está en la mesa. Lo estoy leyendo. → El libro ______ estoy leyendo está en la mesa.', 'que', 'Combinar con relativo de cosa → "que". El libro que estoy leyendo.'),
     ('La ciudad es muy bonita. Vivo allí. → La ciudad ______ vivo es muy bonita.', 'donde', 'Lugar → "donde". La ciudad donde vivo.'),
     ('Ese es el chico. Hablé con él ayer. → Ese es el chico ______ hablé ayer.', 'con quien', 'Preposición + persona → "con quien". El chico con quien hablé.'),
     ('Mi amiga se llama Laura. Ella trabaja en el hospital. → Mi amiga, ______ trabaja en el hospital, se llama Laura.', 'que', 'Relativa explicativa (entre comas) con persona → "que".'),
     ('El hotel era muy cómodo. Dormimos allí. → El hotel ______ dormimos era muy cómodo.', 'donde', 'Lugar → "donde". El hotel donde dormimos.'),
    ]),
  ex3=('Relativas especificativas y explicativas', 'Elige la interpretación o forma correcta.',
    [('¿Cuál es la diferencia entre "que" y "donde" como relativos?',
      ['"Que" para cosas y personas; "donde" para lugares', '"Donde" para cosas; "que" para personas', 'Son intercambiables siempre'],
      '"Que" para cosas y personas; "donde" para lugares',
      '"Que" es el relativo más general. "Donde" se especializa en expresar lugar.'),
     ('¿Cuándo se omite "que" en español?',
      ['Nunca — "que" es siempre obligatorio', 'Cuando el antecedente es una persona', 'En oraciones cortas'],
      'Nunca — "que" es siempre obligatorio',
      'A diferencia del inglés ("the book I read"), en español el relativo "que" nunca se omite.'),
     ('Los alumnos que estudian mucho aprueban. ¿Qué tipo de relativa es?',
      ['Especificativa (sin comas) — identifica qué alumnos', 'Explicativa (con comas) — añade información', 'Ninguna de las dos'],
      'Especificativa (sin comas) — identifica qué alumnos',
      'Sin comas, la relativa limita o identifica el antecedente: "los alumnos (específicos) que estudian".'),
     ('¿Cuál es correcta?',
      ['El libro que leí es interesante.', 'El libro leí es interesante.', 'El libro cual leí es interesante.'],
      'El libro que leí es interesante.',
      '"Que" es el relativo correcto; no puede omitirse; "cual" en especificativas es incorrecto.'),
     ('Mi madre, que es médica, vive en Madrid. ¿Qué tipo de relativa es?',
      ['Explicativa — añade información extra sobre "mi madre"', 'Especificativa — identifica a qué madre', 'Una conjunción, no una relativa'],
      'Explicativa — añade información extra sobre "mi madre',
      'Las comas indican relativa explicativa. Solo tengo una madre, así que la relativa no identifica, sino que añade información.'),
    ]),
  game_desc='4 usos de los relativos · 3 rondas cada uno · llega a 100 puntos para ganar.',
  items=[
    ('que-cosas', 'que (cosas)', 'pronombre relativo para objetos, ideas o conceptos', 'el objeto que...', 'El coche que compré es rojo.', 'La película ______ vimos era muy buena.', 'que'),
    ('que-personas', 'que (personas)', 'pronombre relativo para personas en oraciones especificativas', 'la persona que...', 'La chica que trabaja aquí es simpática.', 'El médico ______ me atendió fue muy amable.', 'que'),
    ('donde', 'donde', 'pronombre relativo de lugar (where)', 'el lugar donde...', 'La ciudad donde nací es preciosa.', 'El restaurante ______ cenamos era excelente.', 'donde'),
    ('con-quien', 'con quien / con quienes', 'relativo de persona tras preposición', 'preposición + quien', 'La persona con quien hablé es la directora.', 'La mujer ______ trabajo es muy profesional.', 'con quien'),
    ('especificativa', 'relativa especificativa', 'sin comas — identifica o restringe el antecedente', 'relativa restrictiva', 'Los estudiantes que aprobaron salieron contentos.', 'El alumno ______ llegó tarde se perdió la explicación.', 'que'),
    ('explicativa', 'relativa explicativa', 'entre comas — añade información sobre un antecedente ya identificado', 'relativa no restrictiva', 'Carlos, que es mi hermano, vive en Valencia.', 'Ana, ______ es mi amiga, trabaja en el hospital.', 'que'),
    ('no-omision', '"que" no se omite', 'a diferencia del inglés, el relativo "que" en español es siempre obligatorio', 'the book I read = el libro que leí', 'El libro que leí era muy interesante.', 'El restaurante ______ recomendaste estaba lleno.', 'que'),
    ('cuyo', 'cuyo/a/os/as', 'relativo de posesión (whose) — concuerda con lo poseído', 'whose', 'El autor cuya novela leí ganó el premio.', 'La empresa ______ director conocí es muy grande.', 'cuyo'),
  ],
),

'presente-continuo': dict(
  level='a2', section='grammar', num='G15',
  short='El Presente Continuo',
  title='El Presente Continuo — Estar + Gerundio',
  subtitle='Expresa acciones en progreso con estar + gerundio: estoy comiendo, está trabajando',
  slides=[
    ('¿Qué es el presente continuo?', None,
     '<p class="slide-explanation">El <b>presente continuo</b> (estar + gerundio) expresa una acción que está ocurriendo <b>en este momento</b> o en un período actual. Se usa mucho menos que en inglés.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¡Silencio! Estoy estudiando.</b> (acción en este mismo momento)</p>'
     '<p style="margin-top:8px"><b>Últimamente está trabajando mucho.</b> (período actual)</p>'
     '<p style="margin-top:8px"><b>¿Qué estás haciendo?</b> (pregunta por la acción en progreso)</p>'
     '</div>'
     '<p style="margin-top:16px">Diferencia con el inglés: en español, "I go to work" y "I am going to work" se pueden traducir ambas con el presente simple, a menos que queramos enfatizar el progreso.</p>'),
    ('Formación del gerundio', None,
     '<p class="slide-explanation">El gerundio se forma añadiendo <b>-ando</b> (-AR) o <b>-iendo</b> (-ER/-IR) al radical. Es invariable:</p>'
     '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
     '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Infinitivo</th><th style="padding:8px;text-align:left">Gerundio</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">hablar (-AR)</td><td style="padding:8px"><b>hablando</b></td><td style="padding:8px">Estoy hablando.</td></tr>'
     '<tr><td style="padding:8px">comer (-ER)</td><td style="padding:8px"><b>comiendo</b></td><td style="padding:8px">Está comiendo.</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">vivir (-IR)</td><td style="padding:8px"><b>viviendo</b></td><td style="padding:8px">Estamos viviendo.</td></tr>'
     '<tr><td style="padding:8px">leer (-ER irr.)</td><td style="padding:8px"><b>leyendo</b></td><td style="padding:8px">Está leyendo.</td></tr>'
     '<tr style="background:var(--paper)"><td style="padding:8px">dormir (-IR irr.)</td><td style="padding:8px"><b>durmiendo</b></td><td style="padding:8px">Están durmiendo.</td></tr>'
     '</table>'
     '<p style="margin-top:8px">Otros gerundios irregulares frecuentes: decir → <b>diciendo</b>, pedir → <b>pidiendo</b>, seguir → <b>siguiendo</b>, venir → <b>viniendo</b>.</p>'),
    ('Estar + gerundio vs. presente simple', 'Cuándo usar cada uno',
     '<p class="slide-explanation">En español, el presente continuo se usa en situaciones más específicas que en inglés:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Usa el presente simple</b> para acciones habituales y hechos generales:</p>'
     '<p style="margin-top:4px">— Trabajo en una empresa de tecnología. (habitual)</p>'
     '<p style="margin-top:4px">— Vivo en Madrid. (estado permanente) — NO: Estoy viviendo en Madrid (salvo que sea temporal)</p>'
     '<p style="margin-top:12px"><b>Usa estar + gerundio</b> para:</p>'
     '<p style="margin-top:4px">— ¡Shh! <b>Estoy hablando</b> por teléfono. (este momento)</p>'
     '<p style="margin-top:4px">— Este mes <b>estoy trabajando</b> en un proyecto especial. (período temporal)</p>'
     '</div>'),
    ('Otros usos del gerundio', 'Más allá de estar + gerundio',
     '<p class="slide-explanation">El gerundio también se combina con otros verbos:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>seguir + gerundio</b> (to keep doing): <b>Sigue</b> lloviendo. / <b>Sigo</b> estudiando español.</p>'
     '<p style="margin-top:8px"><b>llevar + tiempo + gerundio</b> (to have been doing for): <b>Llevo</b> tres horas <b>esperando</b>.</p>'
     '<p style="margin-top:8px"><b>ir + gerundio</b> (to gradually do): El tiempo va <b>mejorando</b>.</p>'
     '</div>'
     '<p style="margin-top:12px">El gerundio nunca funciona como sujeto (eso es el infinitivo): "<b>Fumar</b> es malo" (no "Fumando es malo").</p>'),
  ],
  traps=[
    ('Estoy viviendo en Madrid. (siempre)', 'Vivo en Madrid.', '"Vivo en Madrid" (presente simple) expresa una situación estable. "Estoy viviendo" implica que es temporal.'),
    ('Estoy sabiendo la respuesta.', 'Sé la respuesta.', 'Verbos de estado (saber, conocer, querer, necesitar) no se usan en continuo.'),
    ('Está comendo.', 'Está <strong>comiendo</strong>.', 'El gerundio de verbos -ER es -iendo, no -endo.'),
    ('Ella está corrende.', 'Ella está <strong>corriendo</strong>.', '"Correr" (-ER) → gerundio "corriendo" (-iendo).'),
    ('¿Qué estás haciendo? — Escribo un email.', '¿Qué estás haciendo? — <strong>Estoy escribiendo</strong> un email.', 'Si la pregunta usa el continuo para preguntar por la acción en este momento, la respuesta natural también usa el continuo.'),
  ],
  summary=[
    ('estar + gerundio', 'acción en progreso', 'Estoy comiendo. Está trabajando.'),
    ('-AR → -ando', 'gerundio regular', 'hablar → hablando, trabajar → trabajando'),
    ('-ER/-IR → -iendo', 'gerundio regular', 'comer → comiendo, vivir → viviendo'),
    ('irreg. frecuentes', 'leer→leyendo, dormir→durmiendo', 'diciendo, pidiendo, siguiendo'),
    ('seguir + ger.', 'acción que continúa', 'Sigue lloviendo. Sigues creciendo.'),
    ('llevar + tiempo + ger.', 'duración de la acción', 'Llevo dos horas esperando.'),
  ],
  ex1=('Elige la forma del presente continuo', 'Selecciona la opción correcta.',
    [('¿Qué ______ tú en este momento? (hacer)',
      ['estás haciendo', 'haces', 'estás haber'],
      'estás haciendo',
      '"Tú" + estar en presente: "estás". Gerundio de "hacer": "haciendo".'),
     ('Silencio, el bebé ______. (dormir)',
      ['está durmiendo', 'duerme', 'está dormiendo'],
      'está durmiendo',
      '"Dormir" tiene gerundio irregular: "durmiendo". "Está durmiendo."'),
     ('Nosotros ______ un proyecto muy interesante este mes. (trabajar)',
      ['estamos trabajando', 'trabajamos', 'están trabajando'],
      'estamos trabajando',
      '"Nosotros" + "estar": "estamos". Gerundio de "trabajar": "trabajando".'),
     ('¡Corre! El tren ______. (salir)',
      ['está saliendo', 'sale', 'está saldando'],
      'está saliendo',
      '"Salir" → gerundio regular (-IR) "saliendo". "El tren está saliendo."'),
     ('¿______ (vosotros) la tele? (ver)',
      ['Estáis viendo', 'Están viendo', 'Estáis veyendo'],
      'Estáis viendo',
      '"Vosotros" + "estar": "estáis". "Ver" tiene gerundio irregular: "viendo". (La -e- cae ante -iendo)'),
     ('Últimamente ellos ______ mucho en el gimnasio. (entrenar)',
      ['están entrenando', 'entrenan', 'estaban entrenando'],
      'están entrenando',
      '"Ellos" + "estar": "están". Gerundio de "entrenar": "entrenando". Período actual → continuo.'),
    ]),
  ex2=('Forma el gerundio', 'Escribe el gerundio del verbo indicado.',
    [('El niño ______ (leer) un cuento.', 'está leyendo', '"Leer" tiene gerundio irregular: "leyendo" (no "leiendo").'),
     ('¿Por qué ______ (llorar) tú?', 'estás llorando', '"Llorar" → gerundio regular -AR: "llorando".'),
     ('Mis amigos ______ (pedir) la cuenta.', 'están pidiendo', '"Pedir" (-IR, cambia e→i) → gerundio irregular "pidiendo".'),
     ('Llevo una hora ______ (esperar).', 'esperando', 'Con "llevar + tiempo +", el gerundio es "-ando" para -AR.'),
     ('Sigue ______ (nevar) en la montaña.', 'nevando', '"Nevar" → gerundio regular -AR: "nevando".'),
    ]),
  ex3=('Presente continuo vs. presente simple', 'Elige la forma más apropiada.',
    [('Todos los días ______ a las 7. (yo, levantarse)',
      ['me levanto', 'me estoy levantando', 'estoy levantando'],
      'me levanto',
      'Acción habitual (todos los días) → presente simple, no continuo.'),
     ('¡Shh! Mi padre ______ en el sofá. (dormir)',
      ['está durmiendo', 'duerme', 'ha dormido'],
      'está durmiendo',
      'Acción que ocurre en este momento → presente continuo.'),
     ('Este semestre ______ (yo, estudiar) muchísimo.',
      ['estoy estudiando', 'estudio', 'he estudiado'],
      'estoy estudiando',
      'Período temporal actual y en progreso → presente continuo.'),
     ('¿Por qué ______ (tú, llorar)?',
      ['estás llorando', 'lloras', 'has llorado'],
      'estás llorando',
      'La pregunta por una acción visible en este momento → presente continuo.'),
     ('Sé que tienes razón. ¿Cuál es el error?',
      ['No hay error, "saber" puede ir en continuo', 'Saber no puede ir en continuo: "Estoy sabiendo" es incorrecto', '"Sé" debería ser "estoy sabiendo"'],
      'Saber no puede ir en continuo: "Estoy sabiendo" es incorrecto',
      'Los verbos de estado (saber, conocer, querer) no se usan en el presente continuo.'),
    ]),
  game_desc='4 aspectos del presente continuo · 3 rondas cada uno · llega a 100 puntos para ganar.',
  items=[
    ('estar-gerundio', 'estar + gerundio', 'forma del presente continuo — expresa acción en progreso', 'present continuous', 'Estoy comiendo. Está trabajando.', 'Ella ______ (leer, 3.ª sing.) una novela.', 'está leyendo'),
    ('ando', '-ando (gerundio -AR)', 'gerundio de verbos -AR: radical + -ando', 'hablando, trabajando, comiendo', 'Está hablando por teléfono.', 'Estamos ______ (trabajar, -AR) juntos.', 'trabajando'),
    ('iendo', '-iendo (gerundio -ER/-IR)', 'gerundio de verbos -ER/-IR: radical + -iendo', 'comiendo, viviendo, escribiendo', 'El niño está comiendo.', 'Estoy ______ (escribir, -IR) una carta.', 'escribiendo'),
    ('leyendo', 'leyendo (leer)', 'gerundio irregular de LEER (la -e- cae antes de -iendo)', 'leer → leyendo', '¿Qué estás leyendo?', 'Mi hermana está ______ (leer) un libro.', 'leyendo'),
    ('durmiendo', 'durmiendo (dormir)', 'gerundio irregular de DORMIR (o→u)', 'dormir → durmiendo', 'El bebé está durmiendo.', 'Están ______ (dormir) en el hotel.', 'durmiendo'),
    ('seguir-ger', 'seguir + gerundio', 'expresa que la acción continúa sin interrupción (to keep doing)', 'continuar + ger.', 'Sigue lloviendo. Siguen estudiando.', 'Ella ______ (seguir) trabajando después de las 8.', 'sigue'),
    ('llevar-ger', 'llevar + tiempo + gerundio', 'expresa la duración de una acción en progreso (to have been doing for)', 'hace + tiempo + que', 'Llevo tres horas esperando.', '¿Cuánto tiempo ______ (llevar, 2.ª sing.) estudiando español?', 'llevas'),
    ('verbos-estado', 'verbos de estado (no continuo)', 'verbos como saber, conocer, querer, necesitar no se usan en presente continuo', 'stative verbs', 'Sé la respuesta. (no: Estoy sabiendo) / Quiero café. (no: Estoy queriendo)', 'Yo ______ (saber) hablar español.', 'sé'),
  ],
),

}
