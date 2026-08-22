# -*- coding: utf-8 -*-
"""Día 28 — Passato remoto (reconocimiento). Solo contenido: el andamiaje vive en dia_build.py."""
from dia_build import *

dia(28, semana=4, nivel="B2",
    titulo="Passato remoto — el tiempo de los libros",
    sub="No lo vas a usar hablando. Sin él no puedes leer nada")

objetivo("reconocer un <span class='it'>passato remoto</span> y saber de qué infinitivo viene",
         "aplicar el patrón <strong>1-3-3</strong> de los irregulares",
         "combinarlo con el <span class='it'>imperfetto</span> como ya haces en español",
         "saber cuándo se usa de verdad y en qué parte de Italia")

ripasso("Del día 27: completa — Pensavo che me l'___ (tú, dire) già · Mi ha detto che ___ (venire) "
        "il giorno dopo · Mi sa che ___ (essere) tardi.")

h2("Para qué sirve, exactamente")
p("Aquí hay que ser honesto contigo: <strong>este tema no es para hablar.</strong> En Milán o en "
  "Roma puedes pasarte un año sin decir un solo <span class='it'>passato remoto</span> y nadie lo "
  "notará. Pero es el tiempo de <em>todo lo que se lee</em>: novelas, cuentos, biografías y, sobre "
  "todo, <strong>libros de historia</strong> — que es justo lo que tú estás leyendo.")
bloque("Abre cualquier página de historia italiana y vas a encontrar <span class='it'>fu, ebbe, "
       "prese, fece, morì, nacque, decise, cadde</span>. Si no reconoces esas formas, el texto se "
       "vuelve ilegible aunque conozcas todas las palabras. Hoy es un día de <strong>lectura</strong>, "
       "no de producción.")

h2("Las formas regulares")
tabla(["", "-are (parlare)", "-ere (credere)", "-ire (finire)"],
      [["io", "parl<b>ai</b>", "cred<b>ei</b> / cred<b>etti</b>", "fin<b>ii</b>"],
       ["tu", "parl<b>asti</b>", "cred<b>esti</b>", "fin<b>isti</b>"],
       ["lui/lei", "parl<b>ò</b>", "cred<b>é</b> / cred<b>ette</b>", "fin<b>ì</b>"],
       ["noi", "parl<b>ammo</b>", "cred<b>emmo</b>", "fin<b>immo</b>"],
       ["voi", "parl<b>aste</b>", "cred<b>este</b>", "fin<b>iste</b>"],
       ["loro", "parl<b>arono</b>", "cred<b>erono</b> / cred<b>ettero</b>", "fin<b>irono</b>"]])
nota("Fíjate en las que más te van a aparecer: la <b>tercera persona</b>. "
     "<span class='it'>parlò, credé, finì</span> y sus plurales <span class='it'>parlarono, "
     "finirono</span>. Un libro de historia habla de terceros casi todo el tiempo — «Mussolini "
     "<span class='it'>prese</span> il potere», «i romani <span class='it'>costruirono</span>». "
     "Si solo te llevas las terceras personas, ya lees.", cuaderno=True)

h2("El truco de los irregulares: 1-3-3")
p("Aquí está el atajo que convierte una lista imposible en algo manejable. Los verbos irregulares "
  "en <span class='it'>passato remoto</span> lo son <strong>solo en tres casillas</strong>: "
  "primera del singular, tercera del singular y tercera del plural. Las otras tres son regulares, "
  "salen del infinitivo de siempre.")
tabla(["Persona", "prendere", "¿Irregular?"],
      [["io", "<b>presi</b>", "✅ sí"],
       ["tu", "prend<b>esti</b>", "❌ regular"],
       ["lui/lei", "<b>prese</b>", "✅ sí"],
       ["noi", "prend<b>emmo</b>", "❌ regular"],
       ["voi", "prend<b>este</b>", "❌ regular"],
       ["loro", "<b>presero</b>", "✅ sí"]])
hack("Aprende <strong>una sola forma por verbo</strong>: la tercera del singular "
     "(<span class='it'>prese</span>). De ahí sacas la primera quitando la -e "
     "(<span class='it'>presi</span>) y la tercera del plural añadiendo -ro "
     "(<span class='it'>presero</span>). Las otras tres las construyes del infinitivo. "
     "Un verbo = un dato, no seis.", cuaderno=True)

h3("Los que de verdad vas a encontrar")
tabla(["Infinitivo", "3ª sing.", "Infinitivo", "3ª sing."],
      [["essere", "<b>fu</b> (loro: furono)", "avere", "<b>ebbe</b>"],
       ["fare", "<b>fece</b>", "dire", "<b>disse</b>"],
       ["vedere", "<b>vide</b>", "venire", "<b>venne</b>"],
       ["sapere", "<b>seppe</b>", "volere", "<b>volle</b>"],
       ["dare", "<b>diede</b> / dette", "stare", "<b>stette</b>"],
       ["nascere", "<b>nacque</b>", "morire", "<b>morì</b> (regular)"],
       ["scrivere", "<b>scrisse</b>", "leggere", "<b>lesse</b>"],
       ["mettere", "<b>mise</b>", "rimanere", "<b>rimase</b>"],
       ["chiedere", "<b>chiese</b>", "rispondere", "<b>rispose</b>"],
       ["decidere", "<b>decise</b>", "conoscere", "<b>conobbe</b>"],
       ["vivere", "<b>visse</b>", "cadere", "<b>cadde</b>"]])
alerta("<strong>Ojo con dos parecidos peligrosos:</strong> <span class='it'>fu</span> (fue, passato "
       "remoto) contra <span class='it'>fa</span> (hace). Y <span class='it'>venne</span> (vino) "
       "contra <span class='it'>viene</span> (viene). En un texto de historia una letra te cambia el "
       "siglo. También: muchas terceras del plural duplican consonante — "
       "<span class='it'>ebbero, vennero, caddero, seppero, vollero</span>.")

h2("Y ahora la buena noticia: esto ya lo sabes")
p("Ayer el español te traicionaba. Hoy te regala el tema entero. La pareja "
  "<span class='it'>passato remoto</span> + <span class='it'>imperfetto</span> funciona "
  "<strong>exactamente igual</strong> que tu pretérito + imperfecto:")
tabla(["Función", "Italiano", "Español"],
      [["Lo que <b>avanza</b> el relato", "<span class='it'>passato remoto</span>",
        "pretérito — <em>llegó, dijo, salió</em>"],
       ["El <b>fondo</b>, la escena", "<span class='it'>imperfetto</span>",
        "imperfecto — <em>llovía, era tarde, había gente</em>"]])
big("<span class='it'>Pioveva</span> quando <span class='it'>arrivò</span>. — "
    "<em>Llovía</em> cuando <em>llegó</em>.")
p("Traducción casi mecánica. No tienes que aprender el concepto, solo las formas. Por eso este día "
  "es más ligero de lo que parece a primera vista.")

h2("¿Dónde se usa de verdad?")
tabla(["Zona", "Qué hacen", "Ejemplo de ayer"],
      [["Norte (Milán, Turín)", "casi nunca; todo en passato prossimo",
        "<span class='it'>Ieri sono andato al mare</span>"],
       ["Centro / estándar escrito", "remoto para lo cerrado y lejano",
        "<span class='it'>Nel 1922 Mussolini prese il potere</span>"],
       ["Sur (Sicilia, Napoli)", "remoto <b>también</b> para ayer",
        "<span class='it'>Ieri andai al mare</span>"]])
nota("O sea: si un siciliano te dice <span class='it'>«ieri mangiai una cosa strana»</span>, no está "
     "hablando raro ni antiguo. Está hablando su italiano. En el sur el passato remoto está vivo "
     "para lo que terminó, aunque terminara hace dos horas.")

fosil("Sigue pendiente: la elisión",
      "Ayer trabajaste <span class='it'>gliel'ho / me l'avessi</span> y hoy vuelve, porque es tu "
      "punto más pegajoso y aún no está fijado. En el ejercicio 8 y en el dictado. LO y LA se comen "
      "su vocal delante de otra vocal, <strong>también dentro del grupo combinado</strong>: "
      "<span class='it'>gliel'ho, me l'ha, te l'avevo, gliel'avessi</span>.")

guiado(["<strong>1. Me topo con esto leyendo:</strong> «<span class='it'>Quando lo seppe, non "
        "rispose e uscì.</span>»",
        "<strong>2. ¿Qué formas raras hay?</strong> <span class='it'>seppe</span>, "
        "<span class='it'>rispose</span>, <span class='it'>uscì</span>. Las tres son terceras del "
        "singular: alguien hizo algo.",
        "<strong>3. ¿De qué infinitivos vienen?</strong> <span class='it'>seppe</span> → "
        "<span class='it'>sapere</span> · <span class='it'>rispose</span> → "
        "<span class='it'>rispondere</span> · <span class='it'>uscì</span> → "
        "<span class='it'>uscire</span> (regular).",
        "<strong>4. Traduzco con pretérito:</strong> «Cuando lo supo, no contestó y salió.» ✅ "
        "Ni un solo «hubo de» ni nada raro: pretérito español y ya."],
       a_medias="Parte de: «<span class='it'>Nacque a Palermo, visse a Roma e non tornò mai.</span>» "
                "① ¿qué tres formas son passato remoto? ___ ② ¿de qué infinitivos? ___ "
                "③ Traducción: ___")

frasi_pronte([("Nel 1922 prese il potere", "En 1922 tomó el poder"),
              ("Nacque a Palermo e morì a Roma", "Nació en Palermo y murió en Roma"),
              ("Pioveva quando arrivò", "Llovía cuando llegó"),
              ("Non disse niente e se ne andò", "No dijo nada y se marchó"),
              ("Fu allora che capii tutto", "Fue entonces cuando entendí todo")])

in_contesto(
    "— Sto leggendo un libro di storia italiana, ma <b>mica</b> è facile.<br>\n"
    "  — Perché? Il vocabolario?<br>\n"
    "  — No, quello lo capisco. Sono i verbi: <b>fu, ebbe, prese, nacque</b>… all'inizio non "
    "capivo <b>manco</b> di che verbo si trattasse.<br>\n"
    "  — Ah, il passato remoto. Guarda, in Sicilia lo usiamo <b>tale e quale</b> anche per ieri. "
    "Mia nonna dice sempre <b>«ieri andai dal medico»</b>.<br>\n"
    "  — Davvero? Io pensavo che <b>fosse</b> solo dei libri.<br>\n"
    "  — <b>Mica</b> tanto. Al nord sì, non lo dicono mai. Ma qui è normalissimo.<br>\n"
    "  — Allora <b>me l'hai</b> risolto: leggo il libro e lo sento parlare a tua nonna.",
    "«Estoy leyendo un libro de historia italiana, pero no es nada fácil.» — «¿Por qué? ¿El "
    "vocabulario?» — «No, ese lo entiendo. Son los verbos: fu, ebbe, prese, nacque… al principio ni "
    "siquiera entendía de qué verbo se trataba.» — «Ah, el passato remoto. Mira, en Sicilia lo usamos "
    "igualito también para ayer. Mi abuela siempre dice “ayer fui al médico”.» — «¿En serio? Yo creía "
    "que era solo de los libros.» — «Qué va. En el norte sí, no lo dicen nunca. Pero aquí es "
    "normalísimo.» — «Entonces me lo has resuelto: leo el libro y se lo oigo hablar a tu abuela.»")

slang("Mica", reg="verde", fon="[MI-ka]",
      it="per niente, affatto — rafforza la negazione",
      es="para nada / qué va / ni de broma",
      uso="Refuerza una negación, y muchas veces se come el <span class='it'>non</span>: "
          "<span class='it'>«Mica male!»</span> = ¡nada mal! Y <span class='it'>«Non è mica "
          "facile»</span> = no es nada fácil. Frecuentísimo hablando, y lo vas a encontrar también "
          "escrito en diálogos de novela.",
      ej=("Mica male questa pizza!",
          "¡Nada mal esta pizza!"))

slang("Manco", reg="medio", fon="[MAN-ko]",
      it="nemmeno, neanche — versione colloquiale",
      es="ni / ni siquiera",
      uso="Es <span class='it'>nemmeno</span> en versión de calle, muy del centro y del sur. "
          "<span class='it'>«Manco per sogno»</span> = ni en sueños, ni loco. Cuidado con el "
          "registro: en un correo de trabajo va <span class='it'>nemmeno</span>.",
      ej=("Non l'ho manco visto.",
          "Ni siquiera lo vi."))

slang("Tale e quale", reg="verde", fon="[TA-le e KWA-le]",
      it="identico, uguale preciso",
      es="igualito / clavado / tal cual",
      uso="Para decir que algo o alguien es idéntico a otra cosa. Muy usado con parecidos de "
          "familia: <span class='it'>«è tale e quale suo padre»</span> = es clavado a su padre. "
          "También <span class='it'>«tale quale»</span>, sin la e.",
      ej=("Da piccolo era tale e quale suo nonno.",
          "De pequeño era igualito a su abuelo."))

cultura(28, "La Sicilia",
        gancho="Una isla que fue reino, y que se cuenta a sí misma en passato remoto",
        ctx=("La Sicilia non è una regione qualsiasi: fu un regno indipendente per secoli. Ci "
             "passarono i greci, che vi costruirono templi meglio conservati di quelli in Grecia; "
             "poi i romani, i bizantini, gli arabi, i normanni. Nel XII secolo Palermo fu una delle "
             "città più ricche d'Europa, e alla corte di Federico II nacque la prima poesia in "
             "lingua italiana — prima ancora di Dante. Gli arabi lasciarono le arance, il cous cous, "
             "i sistemi di irrigazione e centinaia di parole. I normanni costruirono chiese con "
             "mosaici bizantini e iscrizioni in arabo sulla stessa parete. Il siciliano non è un "
             "dialetto dell'italiano: è una lingua sorella, con un suo vocabolario e una sua "
             "letteratura. E il passato remoto, che al nord è morto, lì è ancora la lingua di tutti "
             "i giorni.",
             "Sicilia no es una región cualquiera: fue un reino independiente durante siglos. "
             "Pasaron los griegos, que levantaron templos mejor conservados que los de Grecia; "
             "después romanos, bizantinos, árabes, normandos. En el siglo XII Palermo fue una de las "
             "ciudades más ricas de Europa, y en la corte de Federico II nació la primera poesía en "
             "lengua italiana — antes incluso que Dante. Los árabes dejaron las naranjas, el cuscús, "
             "los sistemas de riego y cientos de palabras. Los normandos construyeron iglesias con "
             "mosaicos bizantinos e inscripciones en árabe en la misma pared. El siciliano no es un "
             "dialecto del italiano: es una lengua hermana, con vocabulario y literatura propios. Y "
             "el passato remoto, que en el norte está muerto, allí sigue siendo lengua de diario."),
        frasi=[("La Sicilia fu un regno indipendente per secoli.",
                "Sicilia fue un reino independiente durante siglos."),
               ("I greci vi costruirono templi meglio conservati di quelli in Grecia.",
                "Los griegos levantaron allí templos mejor conservados que los de Grecia."),
               ("Alla corte di Federico II nacque la prima poesia in italiano.",
                "En la corte de Federico II nació la primera poesía en italiano.")],
        spunto="Lee las tres frases en voz alta y localiza los cuatro passato remoto: "
               "<b>fu, passarono, costruirono, nacque</b>. Ese es exactamente el aspecto que tiene "
               "una página de historia. Luego prueba a contar en italiano, con "
               "<span class='it'>fu / nacque / arrivarono</span>, tres datos de un lugar que "
               "conozcas bien.",
        puente="El paralelo mexicano es Yucatán. También una península que funcionó aparte, con su "
               "propia historia larga antes de la nación, con una lengua que no es un dialecto del "
               "español sino otra lengua entera, y con gente que sigue diciendo «yo soy yucateco» "
               "antes que cualquier otra cosa. Igual que un siciliano dice <span class='it'>«sono "
               "siciliano»</span> y solo después «italiano». Y en los dos casos, la cocina es lo "
               "primero que te lo demuestra.")

dettato(["Nacque a Palermo e non tornò mai.",
         "Pioveva quando arrivò, ma non gliel'ho detto.",
         "Mica male: lo lesse tutto in due giorni."])

# ── ejercicios ──────────────────────────────────────────────────────────────
ej(1, "<strong>¿De qué verbo viene?</strong> — di el infinitivo: a) fece b) seppe c) venne d) nacque "
      "e) disse f) rimase", rows=3, ph="a) fare…")
solu(1, "a) <span class='it'>fare</span> b) <span class='it'>sapere</span> c) <span class='it'>venire"
        "</span> d) <span class='it'>nascere</span> e) <span class='it'>dire</span> f) "
        "<span class='it'>rimanere</span>.")

ej(2, "<strong>Regulares</strong> — pon la 3ª persona singular y plural: a) parlare b) credere "
      "c) finire d) costruire", rows=3, ph="a) parlò / parlarono…")
solu(2, "a) <span class='it'>parlò / parlarono</span> b) <span class='it'>credé (credette) / "
        "crederono (credettero)</span> c) <span class='it'>finì / finirono</span> d) <span class='it'>"
        "costruì / costruirono</span>.")

ej(3, "<strong>El patrón 1-3-3</strong> — te doy la 3ª singular, completa las seis: "
      "<span class='it'>mise</span> (mettere) → io ___ · tu ___ · lui ___ · noi ___ · voi ___ · "
      "loro ___", rows=3, ph="misi, mettesti…")
solu(3, "<span class='it'>misi · mettesti · mise · mettemmo · metteste · misero</span>. Irregulares "
        "solo la 1ª sing., la 3ª sing. y la 3ª plur.; las otras tres salen del infinitivo.")

ej(4, "<strong>Traduce leyendo</strong> — son frases de libro de historia: a) <span class='it'>Nel "
      "1861 l'Italia divenne un regno unito.</span> b) <span class='it'>I romani costruirono strade "
      "in tutta Europa.</span> c) <span class='it'>Dante scrisse la Commedia in esilio.</span>",
   rows=3, ph="a) En 1861…")
solu(4, "a) «En 1861 Italia se convirtió en un reino unido.» b) «Los romanos construyeron carreteras "
        "en toda Europa.» c) «Dante escribió la Commedia en el exilio.» En los tres, pretérito "
        "español y punto.")

ej(5, "<strong>Remoto o imperfetto</strong> — igual que en español: a) <span class='it'>___ "
      "(piovere) quando ___ (arrivare, lui).</span> b) <span class='it'>___ (essere) tardi e non "
      "___ (esserci) nessuno.</span> c) <span class='it'>___ (aprire, lui) la porta e ___ (entrare)."
      "</span>", rows=3, ph="a) Pioveva / arrivò…")
solu(5, "a) <span class='it'>Pioveva quando arrivò</span> (fondo + acción) b) <span class='it'>Era "
        "tardi e non c'era nessuno</span> (los dos fondo) c) <span class='it'>Aprì la porta ed "
        "entrò</span> (las dos avanzan). Idéntico a tu pretérito/imperfecto.")

ej(6, "<strong>¿Quién lo diría?</strong> — di si es más de un milanés, de un texto escrito o de un "
      "siciliano: a) <span class='it'>Ieri sono andato al mare.</span> b) <span class='it'>Nel 1922 "
      "prese il potere.</span> c) <span class='it'>Ieri andai al mare.</span>", rows=3, ph="a) …")
solu(6, "a) milanés (y también estándar hablado en todo el norte y centro) b) texto escrito / "
        "historia c) siciliano — o napolitano. Ninguna de las tres está mal: cambia la zona.")

ej(7, "<strong>Pronomi combinati</strong> — sustituye: a) Ho mandato le foto a lui → ___. b) Ha "
      "raccontato la storia a noi → ___. c) Diede il libro a me → ___.", rows=3,
   ph="a) Gliele ho mandate…", ripasso_tuo=True)
solu(7, "a) <span class='it'>Gliele ho mandate.</span> b) <span class='it'>Ce l'ha raccontata.</span> "
        "c) <span class='it'>Me lo diede.</span> Ojo a la concordancia del participio en a) y b).")

ej(8, "<strong>Elisión (sigue pendiente)</strong> — escribe con apóstrofo: a) glielo ho letto → ___ "
      "b) me lo aveva detto → ___ c) te lo avevo mandato → ___ d) glielo avessi chiesto → ___",
   rows=3, ph="a) gliel'ho letto…", ripasso_tuo=True)
solu(8, "a) <span class='it'>gliel'ho letto</span> b) <span class='it'>me l'aveva detto</span> "
        "c) <span class='it'>te l'avevo mandato</span> d) <span class='it'>gliel'avessi chiesto</span>.")

ej(9, "<strong>Diretto o indiretto?</strong> — marca D o I y pon el pronombre: a) Rispose ___ "
      "(a Marco). b) Chiamò ___ (Maria). c) Telefonò ___ (ai clienti). d) Vide ___ (i documenti).",
   rows=3, ph="a) I → gli…", ripasso_tuo=True)
solu(9, "a) I → <span class='it'>gli rispose</span> b) D → <span class='it'>la chiamò</span> c) I → "
        "<span class='it'>gli telefonò</span> d) D → <span class='it'>li vide</span>. Rispondere y "
        "telefonare piden indirecto; chiamare y vedere, directo.")

ej(10, "<strong>Il tuo vocabolario</strong> — 2 frases con → <strong class='mis-palabras'>(abre tu "
       "Vocabulario ★)</strong>, contando algo en passato remoto como si fuera una novela.",
   rows=3, ph="…")
libre(10)

ej(11, "<strong>Caccia all'errore</strong> — hay CUATRO: a) «Nel 1922 <span class='it'>ha preso</span> "
       "il potere e lo <span class='it'>tenne</span> vent'anni». b) «<span class='it'>Gliele ho "
       "raccontato</span> la storia a loro». c) «<span class='it'>Pioveva</span> quando "
       "<span class='it'>arrivava</span>». d) «<span class='it'>Glielo avevo</span> già detto».",
   rows=4, ph="a) …")
solu(11, "a) mezcla dos sistemas: o <span class='it'>prese… tenne</span> (narrativo) o <span class='it'>"
         "ha preso… ha tenuto</span>. b) doble falta: <span class='it'>gliele</span> repite «a loro» "
         "y no concuerda con «la storia» → <span class='it'>Gliel'ho raccontata</span> (o «Ho "
         "raccontato la storia a loro», pero no las dos). c) el segundo avanza el relato → "
         "<span class='it'>arrivò</span>. d) <span class='it'>Gliel'avevo</span>, con apóstrofo.")

ej(12, "<strong>Ascolto</strong> — escucha y escribe; luego di qué verbos están en passato remoto: " +
       audio([("1", "Nacque nel 1901 e morì a Roma."),
              ("2", "Pioveva quando arrivò, e non disse niente."),
              ("3", "Mica male: lo lesse tutto in due giorni.")]), rows=3,
   ph="1. … (remoto: …)", ripasso_tuo=True)
solu(12, "1) <span class='it'>Nacque nel 1901 e morì a Roma</span> — nacque, morì. 2) <span class='it'>"
         "Pioveva quando arrivò, e non disse niente</span> — arrivò, disse (<span class='it'>pioveva"
         "</span> es imperfetto). 3) <span class='it'>Mica male: lo lesse tutto in due giorni</span> "
         "— lesse.")

ej(13, "<strong>Lettura</strong> — traduce este fragmento, del tipo que te vas a encontrar: "
       "«<span class='it'>Arrivò a Palermo che era ancora buio. Non conosceva nessuno e non aveva "
       "un posto dove dormire, ma non gli importava. Si sedette sui gradini della stazione e "
       "aspettò. Quando il sole si alzò, capì che non sarebbe più tornato indietro.</span>»",
   rows=5, ph="Llegó a Palermo cuando todavía…")
solu(13, "«Llegó a Palermo cuando todavía estaba oscuro. No conocía a nadie y no tenía dónde dormir, "
         "pero no le importaba. Se sentó en los escalones de la estación y esperó. Cuando el sol "
         "salió, entendió que ya no volvería atrás.» Cuenta los remotos: <span class='it'>arrivò, "
         "si sedette, aspettò, si alzò, capì</span> avanzan; <span class='it'>era, conosceva, aveva, "
         "importava</span> son el fondo. Y el último, <span class='it'>sarebbe tornato</span>, es la "
         "consecutio de ayer.")

ej(14, "<strong>Concordanza dei tempi (día 27)</strong> — completa: a) Pensavo che ___ (essere) più "
       "giovane. b) Mi disse che ___ (tornare) presto. c) Non sapevo che ___ (nascere) in Sicilia.",
   rows=3, ph="a) fosse…", ripasso_tuo=True)
solu(14, "a) <span class='it'>fosse</span> b) <span class='it'>sarebbe tornato</span> c) "
         "<span class='it'>fosse nato</span>. Principal en pasado → todo baja un escalón.")

ej(15, "<strong>Produzione libera</strong> — escribe 6-8 líneas contando <em>el día que abriste el "
       "estudio, o el primer trabajo grande que te tocó</em>, pero <strong>como lo escribiría una "
       "novela</strong>: en passato remoto. Obligatorio: 4 passato remoto (2 de ellos irregulares), "
       "2 <span class='it'>imperfetto</span> de fondo, 1 elisión con apóstrofo y un slang de hoy.",
   rows=7, ph="Quel giorno pioveva e non c'era nessuno in strada. Aprii…")
libre(15)

autocontrollo("reconocer fu, ebbe, fece, disse, nacque sin pensarlo",
              "sacar las seis formas de un verbo con el patrón 1-3-3",
              "repartir remoto e imperfetto como pretérito e imperfecto",
              "saber que en Sicilia «ieri andai» es normal, no antiguo")

riflessione(["Hoy pasó algo que conviene que notes: es el primer día del curso pensado para "
             "<strong>leer</strong>, no para hablar. Y llega justo cuando estás metido en libros de "
             "historia italiana. Sin el passato remoto esos libros se te resisten aunque conozcas "
             "todo el vocabulario; con él, se abren de golpe.",
             "Fíjate también en la simetría con ayer. El día 27 el español te traicionaba y había "
             "que desconfiar de él. Hoy te regala el tema entero: remoto e imperfetto se reparten "
             "el trabajo igual que tu pretérito y tu imperfecto. Aprender un idioma cercano es "
             "esto — saber cuándo apoyarte en el que ya tienes y cuándo soltarlo."],
            tiempo="50-60 min", domani="Alterati (-ino / -one / -accio)")

solu_guiado("① <span class='it'>nacque, visse, tornò</span> · ② <span class='it'>nascere, vivere, "
            "tornare</span> · ③ «Nació en Palermo, vivió en Roma y no volvió nunca.»")

guardar()
