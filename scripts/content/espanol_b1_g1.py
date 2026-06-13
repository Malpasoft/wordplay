# -*- coding: utf-8 -*-
"""espanol/ B1 Gramática — lote 1 (G01–G05)."""

CHAPTERS = {
    'subjuntivo-presente': dict(
        level='b1',
        section='grammar',
        num='G01',
        short='Subjuntivo Presente',
        title='El Subjuntivo Presente — Deseos, emociones y dudas',
        subtitle='Expresa deseos, emociones, necesidades y dudas con el subjuntivo',
        slides=[
            ('¿Qué es el subjuntivo?', None,
             '<p class="slide-explanation">El <b>modo subjuntivo</b> expresa realidades subjetivas: deseos, emociones, '
             'dudas, posibilidades. A diferencia del indicativo, que describe hechos, el subjuntivo describe '
             'lo que <b>queremos</b>, <b>tememos</b>, <b>dudamos</b> o consideramos <b>posible</b>.</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Indicativo (hechos):</b> Sé que <b>hablas</b> bien. / Es verdad que <b>llueve</b>.</p>'
             '<p><b>Subjuntivo (deseos/dudas):</b> Quiero que <b>hables</b> con ella. / No creo que <b>llueva</b>.</p>'
             '</div>'
             '<p class="slide-explanation">El subjuntivo casi siempre aparece en la cláusula subordinada, '
             'introducida por <b>que</b>, después de un verbo de influencia, emoción o duda en la cláusula principal.</p>'),

            ('Formación: verbos regulares', None,
             '<p class="slide-explanation">La clave: los verbos <b>-AR</b> toman las terminaciones vocálicas de <b>-ER</b> '
             'y viceversa. Esta «vocal opuesta» es la regla de oro del subjuntivo presente.</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pronombre</th>'
             '<th style="padding:8px;text-align:left">HABLAR (-AR → -e)</th>'
             '<th style="padding:8px;text-align:left">COMER (-ER → -a)</th>'
             '<th style="padding:8px;text-align:left">VIVIR (-IR → -a)</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">yo</td><td style="padding:8px"><b>hable</b></td><td style="padding:8px"><b>coma</b></td><td style="padding:8px"><b>viva</b></td></tr>'
             '<tr><td style="padding:8px">tú</td><td style="padding:8px"><b>hables</b></td><td style="padding:8px"><b>comas</b></td><td style="padding:8px"><b>vivas</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">él/ella</td><td style="padding:8px"><b>hable</b></td><td style="padding:8px"><b>coma</b></td><td style="padding:8px"><b>viva</b></td></tr>'
             '<tr><td style="padding:8px">nosotros</td><td style="padding:8px"><b>hablemos</b></td><td style="padding:8px"><b>comamos</b></td><td style="padding:8px"><b>vivamos</b></td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">vosotros</td><td style="padding:8px"><b>habléis</b></td><td style="padding:8px"><b>comáis</b></td><td style="padding:8px"><b>viváis</b></td></tr>'
             '<tr><td style="padding:8px">ellos/ellas</td><td style="padding:8px"><b>hablen</b></td><td style="padding:8px"><b>coman</b></td><td style="padding:8px"><b>vivan</b></td></tr>'
             '</table>'
             '<p class="slide-explanation">Truco: parte de la forma <b>yo</b> del presente de indicativo y añade la '
             'vocal opuesta: hablo → habl- → <b>hable</b>.</p>'),

            ('Irregulares frecuentes', None,
             '<p class="slide-explanation">Los verbos más irregulares tienen formas únicas que debes memorizar:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Infinitivo</th>'
             '<th style="padding:8px;text-align:left">Yo</th><th style="padding:8px;text-align:left">Tú</th>'
             '<th style="padding:8px;text-align:left">Él/Ella</th><th style="padding:8px;text-align:left">Nosotros</th>'
             '<th style="padding:8px;text-align:left">Ellos</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>SER</b></td><td style="padding:8px">sea</td><td style="padding:8px">seas</td><td style="padding:8px">sea</td><td style="padding:8px">seamos</td><td style="padding:8px">sean</td></tr>'
             '<tr><td style="padding:8px"><b>ESTAR</b></td><td style="padding:8px">esté</td><td style="padding:8px">estés</td><td style="padding:8px">esté</td><td style="padding:8px">estemos</td><td style="padding:8px">estén</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>IR</b></td><td style="padding:8px">vaya</td><td style="padding:8px">vayas</td><td style="padding:8px">vaya</td><td style="padding:8px">vayamos</td><td style="padding:8px">vayan</td></tr>'
             '<tr><td style="padding:8px"><b>HABER</b></td><td style="padding:8px">haya</td><td style="padding:8px">hayas</td><td style="padding:8px">haya</td><td style="padding:8px">hayamos</td><td style="padding:8px">hayan</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>SABER</b></td><td style="padding:8px">sepa</td><td style="padding:8px">sepas</td><td style="padding:8px">sepa</td><td style="padding:8px">sepamos</td><td style="padding:8px">sepan</td></tr>'
             '<tr><td style="padding:8px"><b>VER</b></td><td style="padding:8px">vea</td><td style="padding:8px">veas</td><td style="padding:8px">vea</td><td style="padding:8px">veamos</td><td style="padding:8px">vean</td></tr>'
             '</table>'),

            ('Usos del subjuntivo: deseo y necesidad', None,
             '<p class="slide-explanation">El subjuntivo aparece obligatoriamente tras verbos de <b>deseo</b>, <b>necesidad</b> '
             'y <b>recomendación</b> cuando hay un cambio de sujeto entre la cláusula principal y la subordinada:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Querer que:</b> Quiero que <b>vengas</b> a la fiesta.</p>'
             '<p><b>Esperar que:</b> Espero que <b>haga</b> buen tiempo.</p>'
             '<p><b>Necesitar que:</b> Necesito que me <b>ayudes</b>.</p>'
             '<p><b>Recomendar que:</b> Te recomiendo que <b>estudies</b> más.</p>'
             '<p><b>Ojalá:</b> Ojalá <b>apruebe</b> el examen. (deseo intenso)</p>'
             '</div>'
             '<p class="slide-explanation">Mismo sujeto → infinitivo: Quiero <b>venir</b> (yo quiero, yo vengo). '
             'Sujeto diferente → subjuntivo: Quiero que <b>vengas</b> (yo quiero, tú vienes).</p>'),

            ('Usos del subjuntivo: duda y emoción', None,
             '<p class="slide-explanation">El subjuntivo también se usa para expresar <b>duda</b>, <b>negación de certeza</b> '
             'y <b>emociones</b> ante la acción de otro:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Duda:</b> No creo que <b>sea</b> verdad. / Dudo que <b>lleguen</b> a tiempo.</p>'
             '<p><b>Emoción:</b> Me alegra que <b>estés</b> bien. / Temo que <b>haya</b> un problema.</p>'
             '<p><b>Necesidad impersonal:</b> Es importante que <b>practiques</b> cada día.</p>'
             '<p><b>Certeza → indicativo:</b> Creo que <b>es</b> verdad. (afirmación positiva)</p>'
             '</div>'
             '<p class="slide-explanation">Regla práctica: si la frase principal expresa certeza positiva '
             '(<i>creo, es verdad, sé</i>), usa indicativo. Si expresa duda, negación, emoción o deseo, usa subjuntivo.</p>'),
        ],
        traps=[
            ('Quiero que hablas más', '<strong>Quiero que hables</strong> más',
             'Tras «querer que» con cambio de sujeto, el verbo subordinado va siempre en subjuntivo: <b>hables</b>, no «hablas».'),
            ('yo hablo → yo habla (subjuntivo)', '<strong>yo hable</strong>',
             'Los verbos -AR forman el subjuntivo con la vocal <b>-e</b>, no <b>-a</b>. La vocal -a es para los verbos -ER/-IR.'),
            ('Ojalá vendrá / Ojalá vendrías', '<strong>Ojalá venga</strong>',
             '<b>Ojalá</b> siempre exige subjuntivo. Nunca se usa con futuro ni condicional.'),
            ('No creo que es verdad', '<strong>No creo que sea</strong> verdad',
             'La negación de certeza («no creo que») exige subjuntivo: <b>sea</b>, no «es».'),
            ('Es importante estudiar → con subjuntivo siempre', 'Es importante <strong>estudiar</strong> (infinitivo sin sujeto)',
             'Cuando no hay sujeto específico, se usa el infinitivo: «Es importante estudiar». El subjuntivo aparece cuando hay un sujeto: «Es importante que <b>estudies</b>».'),
        ],
        summary=[
            ('Verbos -AR en subjuntivo', 'raíz + -e, -es, -e, -emos, -éis, -en', 'Espero que hablen despacio.'),
            ('Verbos -ER/-IR en subjuntivo', 'raíz + -a, -as, -a, -amos, -áis, -an', 'Necesito que comas bien.'),
            ('SER', 'sea, seas, sea, seamos, seáis, sean', 'Ojalá sea un buen día.'),
            ('IR', 'vaya, vayas, vaya, vayamos, vayáis, vayan', 'Quiero que vayas al médico.'),
            ('Deseo/necesidad + que', 'Quiero/Espero/Necesito + que + subjuntivo', 'Necesito que me ayudes.'),
            ('Duda/negación + que', 'No creo/Dudo + que + subjuntivo', 'Dudo que lleguen a tiempo.'),
            ('Ojalá', 'Ojalá + subjuntivo (deseo intenso)', 'Ojalá haga sol mañana.'),
        ],
        ex1=dict(
            title='Elige la forma correcta de subjuntivo',
            questions=[
                ('Espero que tú ______ (llegar) a tiempo.', ['llegas', 'llegues', 'llegarás', 'llegabas'], 1,
                 'Tras «esperar que», el verbo va en subjuntivo: tú → <b>llegues</b>. La vocal -e es la marca de -AR en subjuntivo.'),
                ('No creo que ella ______ (ser) la culpable.', ['es', 'era', 'sea', 'sería'], 2,
                 'La negación de certeza exige subjuntivo. SER → ella subjuntivo: <b>sea</b>.'),
                ('Ojalá ______ (hacer) buen tiempo mañana.', ['hace', 'hará', 'hiciera', 'haga'], 3,
                 '<b>Ojalá</b> siempre requiere subjuntivo presente (para deseos sobre el futuro cercano). HACER → <b>haga</b>.'),
                ('Necesito que vosotros ______ (estudiar) más.', ['estudiais', 'estudiáis', 'estudiéis', 'estudieis'], 2,
                 'Subjuntivo de ESTUDIAR, vosotros: <b>estudiéis</b> (con tilde, vocal -e de los verbos -AR).'),
                ('Me alegra que ______ (estar, tú) mejor.', ['estás', 'estuvieras', 'estés', 'estarás'], 2,
                 'Emoción + que → subjuntivo. ESTAR → tú subjuntivo: <b>estés</b>.'),
                ('El médico recomienda que ______ (beber, tú) más agua.', ['bebes', 'bebas', 'beberás', 'bebías'], 1,
                 'Recomendación + que → subjuntivo. BEBER (-ER) → tú subjuntivo: <b>bebas</b>.'),
            ]
        ),
        ex2=dict(
            title='Escribe el verbo en subjuntivo',
            questions=[
                ('Quiero que él ______ (venir) a la reunión.',
                 'venga', ['venga'], 'VENIR tiene raíz irregular en presente yo: vengo → veng-. Él subjuntivo: <b>venga</b>.'),
                ('Ojalá nosotros ______ (tener) más tiempo libre.',
                 'tengamos', ['tengamos'], 'TENER → yo tengo → teng-. Nosotros subjuntivo: <b>tengamos</b>.'),
                ('Es importante que (ir, vosotros) ______ al dentista.',
                 'vayáis', ['vayáis', 'vayais'], 'IR es irregular en subjuntivo: vaya, vayas, vaya, vayamos, <b>vayáis</b>, vayan.'),
                ('No creo que eso ______ (ser) posible.',
                 'sea', ['sea'], 'SER en subjuntivo → <b>sea</b>. La negación de certeza exige subjuntivo.'),
                ('Espero que ella ______ (saber) la respuesta.',
                 'sepa', ['sepa'], 'SABER es irregular en subjuntivo: yo sepa, tú sepas, él <b>sepa</b>…'),
            ]
        ),
        ex3=dict(
            title='Indicativo o subjuntivo',
            questions=[
                ('¿Cuál usa el subjuntivo correctamente?',
                 ['Creo que viene mañana.', 'Espero que venga mañana.', 'Sé que viene mañana.', 'Es verdad que viene.'],
                 1,
                 'Solo «esperar que» desencadena subjuntivo. Las demás expresan certeza → indicativo.'),
                ('¿Cuál es incorrecto?',
                 ['Ojalá haga sol.', 'Ojalá hará sol.', 'Espero que haga sol.', 'No creo que haga sol.'],
                 1,
                 '«Ojalá» nunca admite futuro de indicativo. Lo correcto es siempre <b>ojalá + subjuntivo</b>.'),
                ('¿Cuál expresa duda con subjuntivo?',
                 ['Sé que están en casa.', 'Veo que están en casa.', 'Dudo que estén en casa.', 'Es cierto que están en casa.'],
                 2,
                 'Solo «dudo que» desencadena subjuntivo: <b>estén</b>. Las demás expresan certeza.'),
                ('Elige la forma correcta: No quiero que él ______ (irse).',
                 ['se va', 'se vaya', 'se irá', 'se fuera'],
                 1,
                 '«No querer que» exige subjuntivo. IRSE → él subjuntivo: <b>se vaya</b>.'),
                ('¿Cuándo se usa el infinitivo en lugar del subjuntivo?',
                 ['Cuando el sujeto cambia entre las dos cláusulas.', 'Cuando los dos sujetos son distintos.', 'Cuando los dos sujetos son el mismo.', 'Siempre con ojalá.'],
                 2,
                 'Mismo sujeto → infinitivo: «Quiero <b>venir</b>». Sujeto diferente → subjuntivo: «Quiero que <b>vengas</b>».'),
            ]
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('subj-01', 'hable', 'subjuntivo yo/él de HABLAR', 'hablar en subjuntivo', 'Espero que él <b>hable</b> con el director.', 'Espero que él ______ con el director.', 'hable'),
            ('subj-02', 'coma', 'subjuntivo yo/él de COMER', 'comer en subjuntivo', 'Necesito que tú <b>comas</b> antes de salir.', 'Necesito que tú ______ antes de salir.', 'comas'),
            ('subj-03', 'sea', 'subjuntivo yo/él de SER', 'ser en subjuntivo', 'No creo que <b>sea</b> tan difícil.', 'No creo que ______ tan difícil.', 'sea'),
            ('subj-04', 'vaya', 'subjuntivo yo/él de IR', 'ir en subjuntivo', 'Quiero que ella <b>vaya</b> al médico.', 'Quiero que ella ______ al médico.', 'vaya'),
            ('subj-05', 'esté', 'subjuntivo yo/él de ESTAR', 'estar en subjuntivo', 'Espero que todo <b>esté</b> bien.', 'Espero que todo ______ bien.', 'esté'),
            ('subj-06', 'haya', 'subjuntivo yo/él de HABER', 'haber en subjuntivo', 'Ojalá no <b>haya</b> problemas.', 'Ojalá no ______ problemas.', 'haya'),
            ('subj-07', 'sepa', 'subjuntivo yo/él de SABER', 'saber en subjuntivo', 'Dudo que él <b>sepa</b> la respuesta.', 'Dudo que él ______ la respuesta.', 'sepa'),
            ('subj-08', 'hablemos', 'subjuntivo nosotros de HABLAR', 'hablar nosotros en subjuntivo', 'Es importante que <b>hablemos</b> claro.', 'Es importante que ______ claro.', 'hablemos'),
        ],
    ),

    'por-para': dict(
        level='b1',
        section='grammar',
        num='G02',
        short='POR y PARA',
        title='POR y PARA — Dos preposiciones, muchos usos',
        subtitle='Distingue los usos de por y para con ejemplos claros',
        slides=[
            ('POR: causa, motivo y duración', None,
             '<p class="slide-explanation"><b>POR</b> expresa la <b>causa o el motivo</b> de una acción, '
             'y también la <b>duración</b> de un evento en el tiempo:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Causa/motivo:</b> Lo hice <b>por</b> ti. / Gracias <b>por</b> tu ayuda.</p>'
             '<p><b>Duración:</b> Estudié <b>por</b> dos horas. / Vivió allí <b>por</b> diez años.</p>'
             '<p><b>Intercambio:</b> Pagué cien euros <b>por</b> este libro.</p>'
             '<p><b>Medio de comunicación/transporte:</b> Hablé <b>por</b> teléfono. / Envialo <b>por</b> correo.</p>'
             '</div>'
             '<p class="slide-explanation">Clave de POR: mira <b>hacia atrás</b> — expresa la causa o el origen de algo.</p>'),

            ('POR: movimiento, agente y distribución', None,
             '<p class="slide-explanation">POR también indica <b>movimiento a través</b> de un espacio, '
             'el <b>agente</b> en la voz pasiva y expresiones de <b>distribución o aproximación</b>:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Uso</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Movimiento a través</td><td style="padding:8px">Paseamos <b>por</b> el parque. / Pasé <b>por</b> tu casa.</td></tr>'
             '<tr><td style="padding:8px">Agente (voz pasiva)</td><td style="padding:8px">El libro fue escrito <b>por</b> Cervantes.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Distribución</td><td style="padding:8px">Gana diez euros <b>por</b> hora.</td></tr>'
             '<tr><td style="padding:8px">Frecuencia</td><td style="padding:8px">Voy al gimnasio tres veces <b>por</b> semana.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Aproximación</td><td style="padding:8px">Vivo <b>por</b> aquí. / Estará <b>por</b> las cinco.</td></tr>'
             '</table>'),

            ('PARA: propósito, destino y destinatario', None,
             '<p class="slide-explanation"><b>PARA</b> mira <b>hacia adelante</b>: expresa el <b>propósito</b>, '
             'el <b>destino</b> o el <b>destinatario</b> de una acción:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Propósito / finalidad:</b> Estudio <b>para</b> aprender. / Esta llave es <b>para</b> la puerta.</p>'
             '<p><b>Destino:</b> Salgo <b>para</b> Madrid mañana.</p>'
             '<p><b>Destinatario:</b> Este regalo es <b>para</b> ti.</p>'
             '<p><b>Plazo/fecha límite:</b> Necesito el informe <b>para</b> el lunes.</p>'
             '<p><b>Empleo:</b> Trabajo <b>para</b> una empresa internacional.</p>'
             '</div>'
             '<p class="slide-explanation">Clave de PARA: piensa en la <b>meta o el objetivo</b> final.</p>'),

            ('PARA: opinión y comparación', None,
             '<p class="slide-explanation"><b>PARA</b> también introduce una opinión personal o una comparación '
             'que resulta sorprendente:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Opinión:</b> <b>Para mí</b>, esta solución es la mejor.</p>'
             '<p><b>Para ti / para él / para nosotros…</b> = en mi/tu/su opinión</p>'
             '<p><b>Comparación inesperada:</b> Habla muy bien español <b>para</b> ser principiante.</p>'
             '<p><b>Para ser + cargo/edad:</b> Es muy maduro <b>para</b> su edad.</p>'
             '</div>'
             '<p class="slide-explanation">Esta diferencia es especialmente útil en conversaciones y textos de opinión.</p>'),

            ('POR vs. PARA: los pares clave', None,
             '<p class="slide-explanation">Compara directamente los usos que más se confunden:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Con POR</th><th style="padding:8px;text-align:left">Con PARA</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Lo hice <b>por</b> amor. (causa)</td><td style="padding:8px">Lo hice <b>para</b> mejorar. (propósito)</td></tr>'
             '<tr><td style="padding:8px">Estudié <b>por</b> dos horas. (duración)</td><td style="padding:8px">Necesito el trabajo <b>para</b> el viernes. (plazo)</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Salgo <b>por</b> la puerta. (movimiento)</td><td style="padding:8px">Salgo <b>para</b> Madrid. (destino)</td></tr>'
             '<tr><td style="padding:8px">Fue escrito <b>por</b> él. (agente)</td><td style="padding:8px">Es un libro <b>para</b> niños. (destinatario)</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Cien euros <b>por</b> el abrigo. (intercambio)</td><td style="padding:8px">Un abrigo <b>para</b> el invierno. (propósito)</td></tr>'
             '</table>'),
        ],
        traps=[
            ('Salgo para Madrid por el tren', 'Salgo <strong>para</strong> Madrid <strong>en</strong> tren',
             'El medio de transporte usa <b>en</b> (en tren, en avión), no «por». POR indica el medio de comunicación: <b>por</b> teléfono, <b>por</b> correo.'),
            ('Lo hice para ti → causa', 'Lo hice <strong>por</strong> ti (causa), para ti = para tu beneficio',
             '«<b>Por</b> ti» expresa la causa («a causa de ti»). «<b>Para</b> ti» indica el destinatario («para tu beneficio/uso»).'),
            ('Estudié para dos horas', 'Estudié <strong>por</strong> dos horas',
             'La duración usa <b>POR</b>: estudié <b>por</b> dos horas. PARA marca el plazo límite: necesito esto <b>para</b> las dos.'),
            ('Trabajo por una empresa', 'Trabajo <strong>para</strong> una empresa',
             'El empleo (quién te contrata) usa <b>PARA</b>. POR se usa para intercambio: trabajo <b>por</b> un salario.'),
            ('Para mí, creo que… / Para mi opinión', '<strong>Para mí</strong>, … (sin «creo que» adicional)',
             '«Para mí» ya introduce la opinión. No es necesario añadir «creo que» a continuación — sería redundante.'),
        ],
        summary=[
            ('POR: causa', 'lo hice por ti / gracias por', 'Gracias por tu ayuda en el proyecto.'),
            ('POR: duración', 'por + periodo de tiempo', 'Viví en Londres por tres años.'),
            ('POR: movimiento', 'pasar/caminar por', 'Paseamos por el centro histórico.'),
            ('POR: agente (pasiva)', 'fue escrito/hecho por', 'La sinfonía fue compuesta por Mozart.'),
            ('PARA: propósito', 'estudiar para / para + infinitivo', 'Estudio para mejorar mi nivel.'),
            ('PARA: destino/plazo', 'salir para / entregar para', 'El informe es para el viernes.'),
            ('PARA: destinatario/opinión', 'un regalo para / para mí', 'Para mí, es la mejor opción.'),
        ],
        ex1=dict(
            title='POR o PARA: elige la preposición correcta',
            questions=[
                ('Gracias ______ tu ayuda con el proyecto.', ['por', 'para', 'en', 'de'], 0,
                 'Agradecimiento → causa → <b>por</b>. «Gracias por» es una expresión fija.'),
                ('El avión sale ______ Buenos Aires a las seis.', ['por', 'para', 'hacia', 'en'], 1,
                 'Destino de un viaje → <b>para</b>: sale para Buenos Aires.'),
                ('Esta novela fue escrita ______ una autora colombiana.', ['para', 'de', 'por', 'en'], 2,
                 'Agente de la voz pasiva → <b>por</b>: fue escrita por.'),
                ('Necesito terminar el informe ______ el jueves.', ['por', 'en', 'para', 'hasta'], 2,
                 'Plazo o fecha límite → <b>para</b>: para el jueves.'),
                ('Paseamos ______ la orilla del río durante una hora.', ['para', 'por', 'hasta', 'hacia'], 1,
                 'Movimiento a través de un lugar → <b>por</b>: paseamos por la orilla.'),
                ('Compré estas flores ______ mi madre, es su cumpleaños.', ['por', 'en', 'de', 'para'], 3,
                 'Destinatario → <b>para</b>: para mi madre.'),
            ]
        ),
        ex2=dict(
            title='Completa con por o para',
            questions=[
                ('Estudio español ______ trabajar en Latinoamérica.',
                 'para', ['para'], 'Finalidad u objetivo → <b>para</b>: para trabajar.'),
                ('Lo hice todo ______ amor, no ______ dinero.',
                 'por', ['por'], 'Causa/motivo → <b>por</b>: por amor.'),
                ('Hablamos ______ teléfono durante media hora.',
                 'por', ['por'], 'Medio de comunicación → <b>por</b>: por teléfono.'),
                ('Este regalo es ______ ti; espero que te guste.',
                 'para', ['para'], 'Destinatario → <b>para</b>: para ti.'),
                ('Gana veinte euros ______ hora de trabajo.',
                 'por', ['por'], 'Distribución o tasa → <b>por</b>: por hora.'),
            ]
        ),
        ex3=dict(
            title='Identifica el uso correcto',
            questions=[
                ('¿Cuál expresa duración con POR correctamente?',
                 ['Estudié para dos horas.', 'Estudié por dos horas.', 'Estudié en dos horas.', 'Estudié durante para dos horas.'],
                 1,
                 'Duración → <b>POR</b>: estudié <b>por</b> dos horas. «Para» marca plazos, no duración.'),
                ('¿Cuál usa PARA para indicar propósito?',
                 ['Trabajo por esta empresa.', 'Viajo por Madrid.', 'Compré un diccionario para aprender vocabulario.', 'Gracias para tu ayuda.'],
                 2,
                 'Propósito/finalidad → <b>para</b>: para aprender vocabulario.'),
                ('¿Qué significa «Lo hice por ti»?',
                 ['Lo hice con el objetivo de dártelo.', 'Lo hice a causa de ti.', 'Te lo di a ti.', 'Salí hacia tu casa.'],
                 1,
                 '«Por ti» expresa causa o motivo: lo hice <b>a causa de ti</b> / <b>por tu culpa o mérito</b>.'),
                ('¿Cuál usa POR para indicar el agente de la voz pasiva?',
                 ['El cuadro fue pintado para Picasso.', 'El cuadro fue pintado por Picasso.', 'El cuadro fue pintado en Picasso.', 'El cuadro fue pintado de Picasso.'],
                 1,
                 'Agente en voz pasiva → <b>por</b>: fue pintado <b>por</b> Picasso.'),
                ('¿Cuál expresa opinión personal con PARA?',
                 ['Según mí, es correcto.', 'Para mí, es la mejor solución.', 'Por mí, es la mejor solución.', 'En mí opinión, es correcto.'],
                 1,
                 'Opinión personal → <b>para mí</b>. «Según yo» no es estándar; «por mí» tiene otro matiz (= en cuanto a mí, no me importa).'),
            ]
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('porpara-01', 'por', 'POR expresa causa o motivo', 'causa: gracias por / lo hice por', 'Lo hice todo <b>por</b> amor.', 'Lo hice todo ______ amor. (causa)', 'por'),
            ('porpara-02', 'para', 'PARA indica propósito o finalidad', 'propósito: para + infinitivo', 'Estudio español <b>para</b> mejorar mi carrera.', 'Estudio español ______ mejorar mi carrera. (propósito)', 'para'),
            ('porpara-03', 'por', 'POR marca duración en el tiempo', 'duración: por dos horas', 'Esperé <b>por</b> media hora en la cola.', 'Esperé ______ media hora en la cola. (duración)', 'por'),
            ('porpara-04', 'para', 'PARA señala el destinatario de algo', 'destinatario: este regalo para ti', 'Este pastel es <b>para</b> toda la familia.', 'Este pastel es ______ toda la familia. (destinatario)', 'para'),
            ('porpara-05', 'por', 'POR introduce al agente en la voz pasiva', 'agente pasiva: fue escrito por', 'La carta fue firmada <b>por</b> el director.', 'La carta fue firmada ______ el director. (agente)', 'por'),
            ('porpara-06', 'para', 'PARA expresa plazo o fecha límite', 'plazo: para el lunes', 'Necesito la respuesta <b>para</b> mañana.', 'Necesito la respuesta ______ mañana. (plazo)', 'para'),
            ('porpara-07', 'por', 'POR indica movimiento a través de un lugar', 'movimiento: pasear por', 'Los turistas caminaron <b>por</b> las calles del casco viejo.', 'Los turistas caminaron ______ las calles del casco viejo. (movimiento)', 'por'),
            ('porpara-08', 'para', 'PARA señala el destino de un viaje', 'destino: salir para', 'El tren sale <b>para</b> Sevilla a las nueve.', 'El tren sale ______ Sevilla a las nueve. (destino)', 'para'),
        ],
    ),

    'indefinidos': dict(
        level='b1',
        section='grammar',
        num='G03',
        short='Pronombres Indefinidos',
        title='Los Pronombres y Adjetivos Indefinidos',
        subtitle='Algo, nada, alguien, nadie, alguno, ninguno y más',
        slides=[
            ('Indefinidos afirmativos: algo y alguien', None,
             '<p class="slide-explanation">Los indefinidos se refieren a personas, cosas o cantidades de forma '
             'no específica. Los afirmativos indican existencia; los negativos, ausencia.</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>algo</b> — una cosa no especificada: ¿Quieres <b>algo</b> de beber?</p>'
             '<p><b>alguien</b> — una persona no especificada: ¿Hay <b>alguien</b> en casa?</p>'
             '<p><b>algún / alguno / alguna</b> — parte de un grupo: Tengo <b>algún</b> problema. / <b>Alguno</b> de ellos vendrá.</p>'
             '<p><b>algunos / algunas</b> — varios de un grupo: <b>Algunos</b> estudiantes llegaron tarde.</p>'
             '</div>'
             '<p class="slide-explanation"><b>Algún</b> se usa ante sustantivo masculino singular: algún libro, algún día. '
             '<b>Alguno</b> se usa solo, sin sustantivo.</p>'),

            ('Indefinidos negativos: nada, nadie y ninguno', None,
             '<p class="slide-explanation">Los indefinidos negativos expresan ausencia total. En español '
             'se usa la <b>doble negación</b> cuando el indefinido va detrás del verbo:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Indefinido</th><th style="padding:8px;text-align:left">Antes del verbo</th><th style="padding:8px;text-align:left">Después del verbo (doble negación)</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>nada</b></td><td style="padding:8px"><b>Nada</b> me sorprende.</td><td style="padding:8px">No me sorprende <b>nada</b>.</td></tr>'
             '<tr><td style="padding:8px"><b>nadie</b></td><td style="padding:8px"><b>Nadie</b> sabe la verdad.</td><td style="padding:8px">No sabe la verdad <b>nadie</b>.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>ningún/ninguno/a</b></td><td style="padding:8px"><b>Ningún</b> alumno faltó.</td><td style="padding:8px">No faltó <b>ningún</b> alumno.</td></tr>'
             '</table>'
             '<p class="slide-explanation"><b>Ninguno/ninguna</b> se usa solo en singular en español estándar. '
             'Para la forma apocofada: ningún (masc. sg.) + sustantivo.</p>'),

            ('Indefinidos universales: todo, cada y ambos', None,
             '<p class="slide-explanation">Los indefinidos universales hacen referencia a la totalidad de un grupo:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Indefinido</th><th style="padding:8px;text-align:left">Uso</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>todo/toda/todos/todas</b></td><td style="padding:8px">La totalidad</td><td style="padding:8px"><b>Todos</b> los estudiantes aprobaron.</td></tr>'
             '<tr><td style="padding:8px"><b>cada</b></td><td style="padding:8px">Distribución individual (invariable)</td><td style="padding:8px">Vengo <b>cada</b> semana. / <b>Cada</b> alumno tiene su libro.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>ambos/ambas</b></td><td style="padding:8px">Los dos (siempre plural)</td><td style="padding:8px"><b>Ambos</b> equipos jugaron bien.</td></tr>'
             '</table>'
             '<p class="slide-explanation"><b>Cada</b> es invariable: cada día, cada semana, cada estudiante (no «cadas»).</p>'),

            ('Algo vs. nada / alguien vs. nadie', None,
             '<p class="slide-explanation">Estos pares se confunden con frecuencia. La elección depende de si la oración '
             'es afirmativa, negativa o una pregunta:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Afirmativa:</b> Tengo <b>algo</b> que contarte. / <b>Alguien</b> me llamó.</p>'
             '<p><b>Negativa:</b> No tengo <b>nada</b> que contarte. / No llamó <b>nadie</b>.</p>'
             '<p><b>Pregunta (esperando sí):</b> ¿Tienes <b>algo</b> que contarme?</p>'
             '<p><b>Pregunta (esperando no / neutra):</b> ¿No tienes <b>nada</b>? / ¿Hay <b>alguien</b> ahí?</p>'
             '</div>'
             '<p class="slide-explanation">En inglés se usa <i>something/someone</i> en preguntas afables; '
             'en español también: «¿Quieres <b>algo</b>?» es más amable que «¿No quieres nada?».</p>'),

            ('Alguno y ninguno: concordancia', None,
             '<p class="slide-explanation"><b>Alguno/ninguno</b> concuerdan en género y número con el sustantivo al que se refieren. '
             'Ante sustantivo masculino singular, se apocopan:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Forma</th><th style="padding:8px;text-align:left">Uso</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>algún</b></td><td style="padding:8px">+ sust. masc. sg.</td><td style="padding:8px">¿Tienes <b>algún</b> libro de García Márquez?</td></tr>'
             '<tr><td style="padding:8px"><b>alguna</b></td><td style="padding:8px">+ sust. fem. sg.</td><td style="padding:8px">¿Tienes <b>alguna</b> idea?</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>ningún</b></td><td style="padding:8px">+ sust. masc. sg. (sola neg.)</td><td style="padding:8px">No tengo <b>ningún</b> problema.</td></tr>'
             '<tr><td style="padding:8px"><b>ninguna</b></td><td style="padding:8px">+ sust. fem. sg.</td><td style="padding:8px">No hay <b>ninguna</b> solución fácil.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>algunos/algunas</b></td><td style="padding:8px">varios (plural)</td><td style="padding:8px"><b>Algunos</b> días me levanto tarde.</td></tr>'
             '</table>'
             '<p class="slide-explanation">Recuerda: <b>ningunos/ningunas</b> existe pero es rarísimo. '
             'En la práctica, ninguno/ninguna es siempre singular.</p>'),
        ],
        traps=[
            ('No hay nadie → Nadie no hay', '<strong>No hay nadie</strong> (orden correcto)',
             'Con doble negación, el «no» va antes del verbo: <b>No hay nadie</b>. «Nadie no hay» es incorrecto en español estándar.'),
            ('Ningunas personas vinieron', '<strong>Ninguna</strong> persona vino',
             'Ninguno/ninguna se usa casi siempre en singular. Para expresar «ni una sola persona», se dice «<b>ninguna</b> persona».'),
            ('Algo persona / alguien cosa', '<strong>alguien</strong> (personas) / <strong>algo</strong> (cosas)',
             '<b>Algo</b> se refiere a cosas; <b>alguien</b>, a personas. No se intercambian.'),
            ('Cada días / cadas semana', '<strong>cada</strong> día / <strong>cada</strong> semana',
             '<b>Cada</b> es invariable: nunca lleva -s. Se dice «cada día», «cada semana», «cada estudiante».'),
            ('¿Tienes ningún problema?', '¿Tienes <strong>algún</strong> problema?',
             'En preguntas sin negación explícita, se usan los afirmativos: <b>algún</b>, <b>algo</b>, <b>alguien</b>. Los negativos (ningún, nada, nadie) requieren «no» antes del verbo.'),
        ],
        summary=[
            ('algo / nada', 'cosas (afirm. / neg.)', '¿Quieres algo? — No, no quiero nada.'),
            ('alguien / nadie', 'personas (afirm. / neg.)', '¿Llamó alguien? — No, no llamó nadie.'),
            ('algún(o)/a / ningún(o)/a', 'parte o cero de un grupo', '¿Tienes algún libro? — No tengo ninguno.'),
            ('algunos/algunas', 'varios de un grupo', 'Algunos estudiantes ya terminaron.'),
            ('todo/a/os/as', 'la totalidad', 'Todos los días estudio media hora.'),
            ('cada', 'distribución individual (invariable)', 'Cada semana hay una clase nueva.'),
            ('Doble negación', 'no + verbo + negativo', 'No he visto a nadie en toda la tarde.'),
        ],
        ex1=dict(
            title='Elige el indefinido correcto',
            questions=[
                ('¿Quieres ______ de comer? Hay bocadillos.', ['nada', 'algo', 'nadie', 'ninguno'], 1,
                 'Oferta amable en pregunta afirmativa → <b>algo</b> (se espera que la respuesta sea sí o puede ser que sí).'),
                ('No hay ______ en la sala de espera; está vacía.', ['alguien', 'algo', 'nadie', 'ningún'], 2,
                 'Ausencia de personas con «no hay» → <b>nadie</b>: no hay nadie.'),
                ('______ de mis amigos habla cuatro idiomas.', ['Ningún', 'Nada', 'Alguien', 'Alguno'], 3,
                 'Referencia indefinida afirmativa a una persona de un grupo → <b>alguno</b> (de mis amigos).'),
                ('No tengo ______ duda sobre el resultado.', ['alguna', 'nada', 'ninguna', 'nadie'], 2,
                 'Negación de un sustantivo femenino singular → <b>ninguna</b>: no tengo ninguna duda.'),
                ('Viene ______ día a visitarnos; no sé exactamente cuándo.', ['ningún', 'algún', 'nada', 'nadie'], 1,
                 'Referencia afirmativa indeterminada a un día futuro → <b>algún</b> (+ sustantivo masculino singular).'),
                ('______ los participantes recibieron un certificado al final del curso.', ['Alguno', 'Cada', 'Todos', 'Ninguno'], 2,
                 'Totalidad del grupo → <b>todos</b>: todos los participantes.'),
            ]
        ),
        ex2=dict(
            title='Completa con el indefinido adecuado',
            questions=[
                ('No vi a ______ conocido en la fiesta; no había nadie de mi clase.',
                 'ningún', ['ningún', 'ninguno'], 'Negación ante sustantivo masculino singular → <b>ningún</b> conocido.'),
                ('¿Sabes si llamó ______ mientras yo estaba fuera?',
                 'alguien', ['alguien'], 'Pregunta sobre la existencia de una persona → <b>alguien</b>.'),
                ('______ semana hay reunión del equipo; es una norma fija.',
                 'cada', ['cada'], 'Distribución regular e individual → <b>cada</b> (invariable).'),
                ('No entendí ______ de lo que dijiste; habla más despacio, por favor.',
                 'nada', ['nada'], 'Negación total referida a cosas/contenido → <b>nada</b>.'),
                ('Tengo ______ preguntas sobre el tema; ¿puedo hacértelas ahora?',
                 'algunas', ['algunas'], 'Cantidad indefinida positiva de sustantivo femenino plural → <b>algunas</b>.'),
            ]
        ),
        ex3=dict(
            title='Uso correcto de los indefinidos',
            questions=[
                ('¿Cuál usa la doble negación correctamente?',
                 ['Nadie no vino a la reunión.', 'No vino nadie a la reunión.', 'Vino no nadie a la reunión.', 'No nadie vino a la reunión.'],
                 1,
                 'Doble negación correcta: <b>no</b> + verbo + <b>nadie</b>: «No vino nadie».'),
                ('¿Cuál es incorrecto?',
                 ['No tengo ningún problema.', 'No tengo ningunas ideas.', 'No tengo ninguna duda.', 'No tengo ningún dinero.'],
                 1,
                 '«<b>Ningunas</b> ideas» es prácticamente inexistente en el español actual. Lo correcto es «ninguna idea» (singular).'),
                ('"Algo" se refiere a…',
                 ['personas desconocidas', 'cosas o hechos no especificados', 'todos los miembros de un grupo', 'una cantidad exacta'],
                 1,
                 '<b>Algo</b> hace referencia a cosas, hechos o situaciones no específicas. <b>Alguien</b> es para personas.'),
                ('¿Qué significa «Ambos equipos jugaron bien»?',
                 ['Todos los equipos jugaron bien.', 'Ningún equipo jugó bien.', 'Los dos equipos jugaron bien.', 'Cada equipo jugó bien.'],
                 2,
                 '<b>Ambos</b> = los dos, los uno y el otro. Es sinónimo de «los dos» y siempre en plural.'),
                ('¿Cuál usa «algún» correctamente?',
                 ['Tengo algún libros interesantes.', 'Tengo algún idea nueva.', 'Tienes algún momento libre esta tarde?', '¿Tienes algún momento libre esta tarde?'],
                 3,
                 '<b>Algún</b> + sustantivo masculino singular: «¿Tienes <b>algún</b> momento libre?»'),
            ]
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('indef-01', 'algo', 'algo: referencia a una cosa no especificada (afirmativo)', 'algo → cosas (afirm.)', '¿Quieres <b>algo</b> de tomar?', '¿Quieres ______ de tomar? (una cosa, afirm.)', 'algo'),
            ('indef-02', 'nada', 'nada: ausencia total de cosas (negativo)', 'nada → cosas (neg.)', 'No quiero <b>nada</b>, gracias.', 'No quiero ______, gracias. (cero cosas)', 'nada'),
            ('indef-03', 'alguien', 'alguien: una persona no identificada (afirmativo)', 'alguien → persona (afirm.)', '¿Hay <b>alguien</b> que hable inglés aquí?', '¿Hay ______ que hable inglés aquí? (persona, afirm.)', 'alguien'),
            ('indef-04', 'nadie', 'nadie: ausencia total de personas (negativo)', 'nadie → persona (neg.)', 'No conocía a <b>nadie</b> en la fiesta.', 'No conocía a ______ en la fiesta. (cero personas)', 'nadie'),
            ('indef-05', 'algún', 'algún: adjetivo indefinido masc. sg. afirmativo', 'algún + sust. masc. sg.', '¿Tienes <b>algún</b> consejo para mí?', '¿Tienes ______ consejo para mí? (uno, masc.)', 'algún'),
            ('indef-06', 'ningún', 'ningún: adjetivo indefinido masc. sg. negativo', 'ningún + sust. masc. sg. neg.', 'No tengo <b>ningún</b> problema con eso.', 'No tengo ______ problema con eso. (cero, masc.)', 'ningún'),
            ('indef-07', 'cada', 'cada: distribución individual, invariable', 'cada (invariable)', 'Llamo a mi familia <b>cada</b> semana.', 'Llamo a mi familia ______ semana. (distribución individual)', 'cada'),
            ('indef-08', 'todos', 'todos: la totalidad del grupo (masc. plural)', 'todos → totalidad masc. pl.', '<b>Todos</b> los alumnos participaron con entusiasmo.', '______ los alumnos participaron con entusiasmo. (totalidad)', 'todos'),
        ],
    ),

    'oraciones-condicionales': dict(
        level='b1',
        section='grammar',
        num='G04',
        short='Oraciones Condicionales',
        title='Las Oraciones Condicionales — Si real e hipotético',
        subtitle='Construye frases condicionales de tipo 1 y tipo 2 correctamente',
        slides=[
            ('¿Qué es una oración condicional?', None,
             '<p class="slide-explanation">Una <b>oración condicional</b> expresa que una situación depende de '
             'otra condición. La cláusula con <b>si</b> establece la condición; la cláusula principal, '
             'la consecuencia.</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Si</b> tienes tiempo, <b>llámame</b>. (condición real/posible)</p>'
             '<p><b>Si</b> tuviera dinero, <b>viajaría</b> por el mundo. (condición hipotética)</p>'
             '</div>'
             '<p class="slide-explanation">La cláusula con <b>si</b> puede ir al principio o al final: '
             '«Llámame <b>si</b> tienes tiempo» es igualmente correcto.</p>'),

            ('Tipo 1: condición real o posible', None,
             '<p class="slide-explanation">El <b>tipo 1</b> expresa situaciones que son <b>posibles o probables</b> '
             'en el presente o futuro. La estructura es:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p style="font-size:1.1em;font-weight:bold">Si + presente de indicativo → futuro simple / imperativo</p>'
             '</div>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Condición (si + presente)</th><th style="padding:8px;text-align:left">Consecuencia (futuro/imperativo)</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Si <b>llueve</b> mañana,</td><td style="padding:8px">no <b>saldremos</b>.</td></tr>'
             '<tr><td style="padding:8px">Si <b>tienes</b> hambre,</td><td style="padding:8px"><b>come</b> algo.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Si <b>apruebo</b> el examen,</td><td style="padding:8px">me <b>tomaré</b> unas vacaciones.</td></tr>'
             '</table>'
             '<p class="slide-explanation">También es posible usar el presente en ambas cláusulas para expresar hechos generales: '
             '«Si <b>calientas</b> el hielo, <b>se derrite</b>.»</p>'),

            ('Tipo 2: condición hipotética o irreal', None,
             '<p class="slide-explanation">El <b>tipo 2</b> expresa situaciones <b>hipotéticas, imaginarias o contrarias</b> '
             'a la realidad actual. La estructura es:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p style="font-size:1.1em;font-weight:bold">Si + imperfecto de subjuntivo → condicional simple</p>'
             '</div>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Condición (si + imperf. subj.)</th><th style="padding:8px;text-align:left">Consecuencia (condicional)</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Si <b>tuviera</b> dinero,</td><td style="padding:8px"><b>viajaría</b> por el mundo.</td></tr>'
             '<tr><td style="padding:8px">Si <b>fuera</b> más joven,</td><td style="padding:8px"><b>estudiaría</b> música.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Si <b>pudiera</b> elegir,</td><td style="padding:8px"><b>viviría</b> en el campo.</td></tr>'
             '</table>'
             '<p class="slide-explanation">El imperfecto de subjuntivo de los verbos -AR: hablara, hablaras, hablara, habláramos… '
             'y de los verbos -ER/-IR: comiera, comieras…</p>'),

            ('Error crítico: NUNCA «si + condicional»', None,
             '<p class="slide-explanation">Este es el error más común y más grave. '
             'En español, <b>nunca</b> se usa el condicional en la cláusula con <b>si</b>:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>INCORRECTO:</b> <span style="color:#B8860B">Si tendría dinero, viajaría.</span></p>'
             '<p><b>CORRECTO:</b> Si <b>tuviera</b> dinero, viajaría.</p>'
             '<p>&nbsp;</p>'
             '<p><b>INCORRECTO:</b> <span style="color:#B8860B">Si podría venir, te avisaría.</span></p>'
             '<p><b>CORRECTO:</b> Si <b>pudiera</b> venir, te avisaría.</p>'
             '</div>'
             '<p class="slide-explanation">Regla absoluta: <b>si + subjuntivo</b> (para hipótesis) o <b>si + indicativo</b> '
             '(para hechos posibles). El condicional solo va en la cláusula de la consecuencia, nunca en la condición.</p>'),

            ('Como si + subjuntivo imperfecto', None,
             '<p class="slide-explanation">La expresión <b>como si</b> («as if» en inglés) siempre va seguida '
             'del subjuntivo imperfecto y expresa una comparación irreal o imaginaria:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p>Habla <b>como si supiera</b> todo. (habla así, pero no lo sabe todo)</p>'
             '<p>Me mira <b>como si me conociera</b>. (me mira así, pero no me conoce)</p>'
             '<p>Gasta dinero <b>como si fuera</b> millonario.</p>'
             '</div>'
             '<p class="slide-explanation">El subjuntivo de «como si» puede ser imperfecto (presente irreal) '
             'o pluscuamperfecto (pasado irreal): «Habla como si lo <b>hubiera hecho</b> él mismo.»</p>'),
        ],
        traps=[
            ('Si tendría más tiempo, estudiaría más.', 'Si <strong>tuviera</strong> más tiempo, estudiaría más.',
             'Nunca se usa el condicional después de «si». Para la hipótesis, la estructura correcta es <b>si + imperfecto de subjuntivo</b>: si tuviera.'),
            ('Si tienes tiempo, me llamas. (usando futuro)', 'Si tienes tiempo, <strong>llámame</strong> o <strong>me llamas</strong>.',
             'Tras «si + presente», la consecuencia puede ser futuro, imperativo o también presente (hechos generales). El futuro «llamarás» también es posible.'),
            ('Como si sabe / como si sabe todo', 'Como si <strong>supiera</strong> todo',
             '«Como si» exige siempre subjuntivo imperfecto: <b>como si supiera</b>, nunca indicativo.'),
            ('Si yo sería rico…', 'Si yo <strong>fuera</strong> rico…',
             'La forma correcta para hipótesis con SER es el subjuntivo imperfecto: <b>si fuera</b>. Nunca «si sería».'),
            ('Si llueva mañana…', 'Si <strong>llueve</strong> mañana…',
             'Para condiciones reales o posibles, se usa el <b>presente de indicativo</b> tras «si», no el subjuntivo.'),
        ],
        summary=[
            ('Tipo 1 (real/posible)', 'Si + presente indicativo → futuro/imperativo', 'Si estudias, aprobarás el examen.'),
            ('Tipo 2 (hipotético)', 'Si + imperfecto subjuntivo → condicional', 'Si tuviera coche, iría en coche.'),
            ('Regla absoluta', 'NUNCA: si + condicional', 'NUNCA: *Si tendría… SIEMPRE: Si tuviera…'),
            ('Subjuntivo imperfecto -AR', '-ara, -aras, -ara, -áramos, -arais, -aran', 'Si hablara más, aprendería más.'),
            ('Subjuntivo imperfecto -ER/-IR', '-iera, -ieras, -iera, -iéramos, -ierais, -ieran', 'Si comiera menos, estaría mejor.'),
            ('Como si', 'como si + subj. imperfecto (comparación irreal)', 'Habla como si supiera todo.'),
        ],
        ex1=dict(
            title='Elige la forma correcta en oraciones condicionales',
            questions=[
                ('Si ______ (tener, tú) fiebre, debes ir al médico.', ['tendrías', 'tengas', 'tienes', 'tuvieras'], 2,
                 'Condición posible o real (tipo 1): si + <b>presente de indicativo</b>: si <b>tienes</b>.'),
                ('Si tuviera más dinero, ______ (comprar, yo) un apartamento.', ['compro', 'compraré', 'compraría', 'comprara'], 2,
                 'Hipótesis (tipo 2): consecuencia en <b>condicional</b>: <b>compraría</b>.'),
                ('______ un error usaría el condicional después de «si».', ['Si vendría,', 'Si viniera,', 'Si vendrá,', 'Si vendrías,'], 1,
                 'Nunca «si + condicional». La forma correcta es <b>si viniera</b> (subjuntivo imperfecto).'),
                ('Si ______ (poder) elegir, viviría cerca del mar.', ['podré', 'puedo', 'pudiera', 'podría'], 2,
                 'Hipótesis (tipo 2): si + <b>subjuntivo imperfecto</b>: <b>pudiera</b>.'),
                ('Habla ______ (como si) lo supiera todo.', ['como que', 'como si', 'si como', 'como que si'], 1,
                 'La comparación irreal usa siempre <b>como si</b> + subjuntivo imperfecto.'),
                ('Si ______ (llover) mañana, cancelaremos el partido.', ['lloviera', 'llovería', 'llueve', 'lloverá'], 2,
                 'Condición posible (tipo 1): si + <b>presente de indicativo</b>: <b>llueve</b>.'),
            ]
        ),
        ex2=dict(
            title='Completa la oración condicional',
            questions=[
                ('Si (tener, yo) ______ tiempo esta tarde, iré a verte.',
                 'tengo', ['tengo'], 'Condición real/posible (tipo 1): si + presente de indicativo → <b>tengo</b>.'),
                ('Si (saber, tú) ______ la respuesta, escríbela en el papel.',
                 'sabes', ['sabes'], 'Condición real, consecuencia en imperativo (tipo 1): si + presente → <b>sabes</b>.'),
                ('Si yo (ser) ______ el director, cambiaría muchas cosas.',
                 'fuera', ['fuera'], 'Hipótesis (tipo 2): si + subjuntivo imperfecto de SER → <b>fuera</b>.'),
                ('Ella habla (como si / conocer) ______ a todo el mundo.',
                 'como si conociera', ['como si conociera', 'como si lo conociera'], '«Como si» + subjuntivo imperfecto de CONOCER → <b>como si conociera</b>.'),
                ('Si (estudiar, vosotros) ______ más, obtendríais mejores notas.',
                 'estudiarais', ['estudiarais'], 'Hipótesis (tipo 2): si + subjuntivo imperfecto vosotros (-AR) → <b>estudiarais</b>.'),
            ]
        ),
        ex3=dict(
            title='Identifica la oración correcta',
            questions=[
                ('¿Cuál es una condicional de tipo 1 correctamente formada?',
                 ['Si tendría dinero, viajaría.', 'Si tienes hambre, come algo.', 'Si tuvieras tiempo, vendrías.', 'Si comería más, estaría mejor.'],
                 1,
                 'Tipo 1: si + <b>presente indicativo</b> → imperativo: «Si tienes hambre, <b>come</b> algo.»'),
                ('¿Cuál es una condicional de tipo 2 correctamente formada?',
                 ['Si tuviera más experiencia, conseguiría ese trabajo.', 'Si tendría más experiencia, conseguiría ese trabajo.', 'Si tengo más experiencia, conseguiré ese trabajo.', 'Si tenga más experiencia, conseguiría ese trabajo.'],
                 0,
                 'Tipo 2: si + <b>imperfecto subjuntivo</b> → condicional: «Si <b>tuviera</b>… <b>conseguiría</b>».'),
                ('¿Cuál contiene el error más típico con las condicionales?',
                 ['Si llueve mañana, no saldremos.', 'Si tuviera más tiempo, estudiaría más.', 'Si tendría más tiempo, estudiaría más.', 'Si hace frío, me abrigaré.'],
                 2,
                 '«<b>Si tendría</b>» es incorrecto: nunca se usa el condicional después de «si».'),
                ('¿Qué estructura sigue «como si»?',
                 ['como si + futuro', 'como si + indicativo presente', 'como si + condicional', 'como si + subjuntivo imperfecto'],
                 3,
                 '«Como si» siempre exige <b>subjuntivo imperfecto</b>: como si <b>supiera</b>, como si <b>fuera</b>…'),
                ('¿Cuál expresa una condición hipotética?',
                 ['Si llueve, me mojo.', 'Si llueve, me mojaré.', 'Si lloviera, me mojaría.', 'Si llueve, mójate.'],
                 2,
                 'Hipótesis (tipo 2): «Si <b>lloviera</b>, me <b>mojaría</b>.» Las demás son condiciones reales (tipo 1).'),
            ]
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('cond-01', 'si tienes', 'condicional tipo 1: si + presente de indicativo', 'tipo 1: si + presente', 'Si <b>tienes</b> frío, cierra la ventana.', 'Si ______ frío, cierra la ventana. (tipo 1: condición posible)', 'tienes'),
            ('cond-02', 'si tuviera', 'condicional tipo 2: si + imperfecto de subjuntivo', 'tipo 2: si + imperf. subj.', 'Si <b>tuviera</b> más tiempo, leería más.', 'Si ______ más tiempo, leería más. (tipo 2: hipótesis)', 'tuviera'),
            ('cond-03', 'viajaría', 'condicional simple: consecuencia hipotética', 'consecuencia tipo 2 → condicional', 'Si pudiera, <b>viajaría</b> a Japón.', 'Si pudiera, ______ a Japón. (consecuencia hipotética)', 'viajaría'),
            ('cond-04', 'llueve', 'tipo 1: si + presente (condición posible)', 'tipo 1: presente indicativo', 'Si <b>llueve</b>, nos quedamos en casa.', 'Si ______, nos quedamos en casa. (condición posible)', 'llueve'),
            ('cond-05', 'fuera', 'si fuera: subjuntivo imperfecto de SER para hipótesis', 'si + fuera (ser, hipótesis)', 'Si <b>fuera</b> más joven, aprendería a tocar la guitarra.', 'Si ______ más joven, aprendería a tocar la guitarra.', 'fuera'),
            ('cond-06', 'como si supiera', 'como si + subjuntivo imperfecto: comparación irreal', 'como si + subjuntivo imperf.', 'Actúa <b>como si supiera</b> todo, pero no es así.', 'Actúa ______ todo, pero no es así. (comparación irreal)', 'como si supiera'),
            ('cond-07', 'estudiaras', 'tipo 2: si + subjuntivo imperfecto tú (-AR)', 'si + estudiaras', 'Si <b>estudiaras</b> un poco más, aprobarías fácilmente.', 'Si ______ un poco más, aprobarías fácilmente.', 'estudiaras'),
            ('cond-08', 'aprobarás', 'tipo 1: consecuencia en futuro simple', 'tipo 1 → futuro en consecuencia', 'Si practicas cada día, <b>aprobarás</b> el examen sin problema.', 'Si practicas cada día, ______ el examen sin problema. (futuro)', 'aprobarás'),
        ],
    ),

    'voz-pasiva': dict(
        level='b1',
        section='grammar',
        num='G05',
        short='La Voz Pasiva',
        title='La Voz Pasiva — Ser, estar y la pasiva refleja',
        subtitle='Construye oraciones pasivas y elige entre ser, estar y se',
        slides=[
            ('Voz activa vs. voz pasiva', None,
             '<p class="slide-explanation">En la <b>voz activa</b>, el sujeto realiza la acción. '
             'En la <b>voz pasiva</b>, el sujeto <b>recibe</b> la acción. '
             'El elemento que realiza la acción se llama <b>agente</b> y va introducido por <b>por</b>.</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Activa:</b> García Márquez <b>escribió</b> «Cien años de soledad».</p>'
             '<p><b>Pasiva:</b> «Cien años de soledad» <b>fue escrita</b> por García Márquez.</p>'
             '<p>&nbsp;</p>'
             '<p><b>Activa:</b> El arquitecto <b>diseñó</b> el edificio.</p>'
             '<p><b>Pasiva:</b> El edificio <b>fue diseñado</b> por el arquitecto.</p>'
             '</div>'
             '<p class="slide-explanation">La voz pasiva con <b>ser</b> es más frecuente en textos formales, '
             'periodísticos e históricos.</p>'),

            ('Construcción: SER + participio', None,
             '<p class="slide-explanation">La voz pasiva se forma con <b>SER + participio pasado</b>. '
             'El participio concuerda en <b>género y número</b> con el sujeto de la oración pasiva:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Sujeto</th><th style="padding:8px;text-align:left">SER</th><th style="padding:8px;text-align:left">Participio</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">La carta (fem. sg.)</td><td style="padding:8px">fue</td><td style="padding:8px"><b>escrita</b></td><td style="padding:8px">La carta fue <b>escrita</b> por Ana.</td></tr>'
             '<tr><td style="padding:8px">El libro (masc. sg.)</td><td style="padding:8px">fue</td><td style="padding:8px"><b>escrito</b></td><td style="padding:8px">El libro fue <b>escrito</b> en 1967.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">Las cartas (fem. pl.)</td><td style="padding:8px">fueron</td><td style="padding:8px"><b>escritas</b></td><td style="padding:8px">Las cartas fueron <b>escritas</b> a mano.</td></tr>'
             '<tr><td style="padding:8px">Los libros (masc. pl.)</td><td style="padding:8px">fueron</td><td style="padding:8px"><b>escritos</b></td><td style="padding:8px">Los libros fueron <b>escritos</b> en español.</td></tr>'
             '</table>'),

            ('La pasiva refleja: SE + verbo', None,
             '<p class="slide-explanation">La <b>pasiva refleja</b> (o impersonal con <b>se</b>) se usa cuando '
             'el agente es desconocido, irrelevante o queremos evitar mencionarlo. '
             'Es mucho más frecuente en el español hablado que la pasiva con <b>ser</b>:</p>'
             '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
             '<p><b>Se venden</b> pisos. (alguien los vende, no importa quién)</p>'
             '<p><b>Se habla</b> español en 20 países.</p>'
             '<p><b>Se necesitan</b> camareros para el verano.</p>'
             '<p><b>Se construyó</b> el puente en 1965.</p>'
             '</div>'
             '<p class="slide-explanation">El verbo concuerda con el sujeto gramatical (la cosa vendida/hablada): '
             '«Se vende <b>un piso</b>» (singular) / «Se venden <b>pisos</b>» (plural).</p>'),

            ('Pasiva de estado: ESTAR + participio', None,
             '<p class="slide-explanation"><b>ESTAR + participio</b> no es la voz pasiva propiamente dicha, '
             'sino la <b>pasiva de estado</b>: describe el <b>resultado o estado actual</b> '
             'de una acción ya completada. No indica quién realizó la acción:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Pasiva con SER (acción)</th><th style="padding:8px;text-align:left">Pasiva de estado con ESTAR (resultado)</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">La tienda <b>fue cerrada</b> a las nueve. (la acción de cerrar)</td><td style="padding:8px">La tienda <b>está cerrada</b>. (el estado actual)</td></tr>'
             '<tr><td style="padding:8px">La ventana <b>fue abierta</b> por alguien. (la acción)</td><td style="padding:8px">La ventana <b>está abierta</b>. (estado ahora)</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px">El trabajo <b>fue terminado</b> ayer. (acción)</td><td style="padding:8px">El trabajo <b>está terminado</b>. (resultado)</td></tr>'
             '</table>'),

            ('Comparación de las tres construcciones', None,
             '<p class="slide-explanation">Resume las tres formas y cuándo elegir cada una:</p>'
             '<table style="width:100%;margin:16px 0;border-collapse:collapse">'
             '<tr style="background:var(--amber);color:#1A1A1A"><th style="padding:8px;text-align:left">Construcción</th><th style="padding:8px;text-align:left">Énfasis</th><th style="padding:8px;text-align:left">Ejemplo</th></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>SER + participio</b></td><td style="padding:8px">La acción; el agente puede mencionarse</td><td style="padding:8px">La novela <b>fue escrita</b> por Vargas Llosa.</td></tr>'
             '<tr><td style="padding:8px"><b>SE + verbo</b></td><td style="padding:8px">La acción; agente desconocido/irrelevante</td><td style="padding:8px"><b>Se construyó</b> el estadio en 1992.</td></tr>'
             '<tr style="background:var(--paper)"><td style="padding:8px"><b>ESTAR + participio</b></td><td style="padding:8px">El estado resultante actual</td><td style="padding:8px">La tienda <b>está cerrada</b> los domingos.</td></tr>'
             '</table>'
             '<p class="slide-explanation">En conversación cotidiana, la pasiva refleja con <b>se</b> y la voz activa '
             'son mucho más naturales que la pasiva con <b>ser</b>.</p>'),
        ],
        traps=[
            ('El libro fue escrito por García Márquez → El libro fue escrito de García Márquez', 'fue escrito <strong>por</strong> García Márquez',
             'El agente de la voz pasiva siempre va introducido por <b>por</b>, nunca por «de». (Excepción muy formal: «conocido de todos».)'),
            ('La carta fue escrito por Ana', 'La carta fue <strong>escrita</strong> por Ana',
             'El participio concuerda con el sujeto en género y número: «la carta» es femenina → <b>escrita</b>, no «escrito».'),
            ('Se vende pisos / Se necesita camareros', 'Se <strong>venden</strong> pisos / Se <strong>necesitan</strong> camareros',
             'En la pasiva refleja, el verbo concuerda con el sujeto gramatical: «pisos» y «camareros» son plurales, así que el verbo también va en plural.'),
            ('La tienda fue cerrada (para decir que está cerrada ahora)', 'La tienda <strong>está cerrada</strong>',
             'Para describir el estado actual como resultado de una acción pasada, usa <b>ESTAR + participio</b>. «Fue cerrada» expresa la acción de cerrar, no el estado actual.'),
            ('Se hablan español en México', '<strong>Se habla</strong> español en México',
             'El español es un sustantivo singular → el verbo va en singular: <b>se habla</b>. No confundir con «Se hablan <b>varios idiomas</b>» (plural).'),
        ],
        summary=[
            ('Pasiva con SER', 'SER + participio (+ por + agente)', 'El puente fue construido por ingenieros suizos.'),
            ('Concordancia del participio', 'Género y número del sujeto pasivo', 'Las cartas fueron firmadas por la directora.'),
            ('Pasiva refleja', 'SE + verbo (concuerda con sujeto)', 'Se venden pisos en esta zona.'),
            ('Pasiva de estado', 'ESTAR + participio (resultado actual)', 'La oficina está cerrada hasta las diez.'),
            ('Cuándo usar SER', 'Acción; agente mencionado o implícito', 'La ley fue aprobada por el parlamento.'),
            ('Cuándo usar SE', 'Agente desconocido o irrelevante', 'Se abrió el nuevo museo en abril.'),
        ],
        ex1=dict(
            title='Elige la construcción pasiva correcta',
            questions=[
                ('La catedral ______ en el siglo XV. (acción histórica, agente no mencionado)', ['está construida', 'fue construida', 'se construida', 'construyó'], 1,
                 'Acción histórica con SER + participio: <b>fue construida</b>. La catedral es femenina → participio en femenino.'),
                ('______ pisos en este edificio. (agente irrelevante)', ['Se vende', 'Se venden', 'Son vendidos', 'Están vendidos'], 1,
                 'Pasiva refleja con agente no mencionado: <b>se venden</b> (plural, porque «pisos» es plural).'),
                ('La tienda ______ cerrada los domingos. (estado habitual)', ['fue', 'es', 'está', 'se'], 2,
                 'Estado resultante habitual → <b>ESTAR</b> + participio: la tienda <b>está</b> cerrada.'),
                ('Los documentos ______ firmados por el notario ayer.', ['están', 'fueron', 'son', 'se'], 1,
                 'Acción en el pasado con agente mencionado → SER (pasado): <b>fueron</b> firmados.'),
                ('______ español en toda América Latina.', ['Es hablado', 'Se habla', 'Habla', 'Están hablando'], 1,
                 'Agente irrelevante, hecho general → pasiva refleja: <b>se habla</b> (español es singular).'),
                ('Las ventanas ______ rotas durante la tormenta de anoche.', ['están', 'estaban', 'fueron', 'se'], 2,
                 'La acción de romperlas ocurrió durante la tormenta → acción pasada: <b>fueron</b> rotas.'),
            ]
        ),
        ex2=dict(
            title='Transforma a la voz pasiva',
            questions=[
                ('Los arquitectos diseñaron el puente. → El puente ______ por los arquitectos.',
                 'fue diseñado', ['fue diseñado'], 'Activa → pasiva: SER en pasado + participio (masc. sg.): <b>fue diseñado</b>.'),
                ('Alguien vendió la casa. → La casa ______.',
                 'fue vendida', ['fue vendida'], 'Pasiva con SER: «la casa» es femenina singular → <b>fue vendida</b>.'),
                ('(Agente irrelevante) Aquí hablan catalán. → Aquí ______ catalán.',
                 'se habla', ['se habla'], 'Pasiva refleja con agente desconocido/irrelevante: <b>se habla</b> catalán (singular).'),
                ('Han terminado el informe. → El informe ya ______. (estado actual)',
                 'está terminado', ['está terminado'], 'Estado resultante actual → <b>está terminado</b> (ESTAR + participio).'),
                ('Cerraron las tiendas a las ocho. → Las tiendas ______ a las ocho.',
                 'fueron cerradas', ['fueron cerradas'], 'Acción pasada → <b>fueron cerradas</b> (femenino plural).'),
            ]
        ),
        ex3=dict(
            title='SER, SE o ESTAR: elige la construcción adecuada',
            questions=[
                ('¿Cuál describe un estado actual con ESTAR?',
                 ['El parque fue cerrado por el ayuntamiento.', 'Se cierra el parque a las diez.', 'El parque está cerrado.', 'El ayuntamiento cerró el parque.'],
                 2,
                 'Estado actual → <b>ESTAR + participio</b>: «El parque <b>está cerrado</b>.»'),
                ('¿Cuál usa la pasiva refleja correctamente?',
                 ['Se vende los pisos.', 'Se venden los pisos.', 'Son vendidos los pisos.', 'Los pisos están vendidos.'],
                 1,
                 'Pasiva refleja: el verbo concuerda con el sujeto «los pisos» (plural) → <b>se venden</b>.'),
                ('¿Cuál menciona al agente correctamente?',
                 ['La sinfonía fue compuesta de Beethoven.', 'La sinfonía fue compuesta por Beethoven.', 'La sinfonía se compuso por Beethoven.', 'La sinfonía está compuesta de Beethoven.'],
                 1,
                 'El agente de la voz pasiva va con <b>por</b>: «fue compuesta <b>por</b> Beethoven».'),
                ('El participio en «Los cuadros fueron pintados» está en forma…',
                 ['masculina singular', 'femenina plural', 'masculina plural', 'femenina singular'],
                 2,
                 '«Los cuadros» es masculino plural → el participio va en <b>masculino plural</b>: pintad<b>os</b>.'),
                ('¿Cuál es la diferencia entre «fue cerrada» y «está cerrada»?',
                 ['"Fue cerrada" describe el estado actual; "está cerrada" describe la acción pasada.',
                  '"Fue cerrada" describe la acción de cerrar; "está cerrada" describe el estado resultante.',
                  'No hay diferencia, son intercambiables.',
                  '"Fue cerrada" solo se usa con agente; "está cerrada" solo sin agente.'],
                 1,
                 '<b>Fue cerrada</b> = la acción ocurrió (SER). <b>Está cerrada</b> = el estado actual como resultado (ESTAR).'),
            ]
        ),
        game_desc='4 conceptos clave · 3 rondas cada uno · llega a 100 puntos para ganar.',
        items=[
            ('pasiva-01', 'fue escrito', 'pasiva con SER: acción en pasado (masc. sg.)', 'ser + participio (pasado masc.)', 'El poema <b>fue escrito</b> por Pablo Neruda.', 'El poema ______ por Pablo Neruda. (voz pasiva, pasado)', 'fue escrito'),
            ('pasiva-02', 'fue escrita', 'pasiva con SER: acción en pasado (fem. sg.)', 'ser + participio (pasado fem.)', 'La carta <b>fue escrita</b> a mano.', 'La carta ______ a mano. (voz pasiva, femenino)', 'fue escrita'),
            ('pasiva-03', 'fueron construidos', 'pasiva con SER: acción en pasado (masc. pl.)', 'ser + participio (pasado masc. pl.)', 'Los puentes <b>fueron construidos</b> en el siglo XIX.', 'Los puentes ______ en el siglo XIX. (voz pasiva, plural)', 'fueron construidos'),
            ('pasiva-04', 'se habla', 'pasiva refleja: agente irrelevante (sg.)', 'se + verbo (sg.) → agente desconocido', '<b>Se habla</b> español en más de veinte países.', '______ español en más de veinte países. (pasiva refleja)', 'se habla'),
            ('pasiva-05', 'se venden', 'pasiva refleja: agente irrelevante (pl.)', 'se + verbo (pl.) → agente desconocido', '<b>Se venden</b> entradas para el concierto.', '______ entradas para el concierto. (pasiva refleja)', 'se venden'),
            ('pasiva-06', 'está abierta', 'pasiva de estado: resultado actual (fem. sg.)', 'estar + participio → estado actual', 'La farmacia <b>está abierta</b> hasta las diez de la noche.', 'La farmacia ______ hasta las diez de la noche. (estado actual)', 'está abierta'),
            ('pasiva-07', 'está terminado', 'pasiva de estado: resultado actual (masc. sg.)', 'estar + participio → resultado', 'El informe ya <b>está terminado</b>; puedes leerlo.', 'El informe ya ______; puedes leerlo. (resultado actual)', 'está terminado'),
            ('pasiva-08', 'fueron firmadas', 'pasiva con SER: acción en pasado (fem. pl.)', 'ser + participio (pasado fem. pl.)', 'Las actas <b>fueron firmadas</b> por todos los socios.', 'Las actas ______ por todos los socios. (pasiva, femenino plural)', 'fueron firmadas'),
        ],
    ),
}
