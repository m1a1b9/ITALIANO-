# -*- coding: utf-8 -*-
"""Día 26 — Verbi causativi. Solo contenido: el andamiaje vive en dia_build.py."""
from dia_build import *

dia(26, semana=4, nivel="B2",
    titulo="Verbi causativi — fare e lasciare + infinito",
    sub="Hacer que algo pase, y dejar que pase: la construcción más italiana que hay")

objetivo("usar <span class='it'>fare + infinito</span> para «hacer que…»",
         "distinguir <span class='it'>fare</span> de <span class='it'>lasciare</span>",
         "colocar los pronombres (<span class='it'>fammelo vedere</span>)",
         "reconocerla en las canciones que ya escuchas")

ripasso("Del día 25: completa — Quando ___ (io, finire), ti chiamo · Non risponde, ___ (avere) il "
        "telefono spento. Y del 23: Mando le foto a lui → ___.")

h2("Il meccanismo")
p("<span class='it'>Non faccio io la cosa: la faccio fare a qualcun altro.</span> → No hago yo la "
  "cosa: hago que otro la haga. El español necesita «hacer QUE + subjuntivo»; el italiano resuelve "
  "todo con un <strong>infinitivo</strong>, sin «che» y sin congiuntivo.")
tabla(["Español", "Italiano", ""],
      [["Hago que él <b>venga</b>", "<span class='it'>Lo <b>faccio venire</b></span>", "sin «che»"],
       ["Hice que me <b>enviaran</b> las fotos", "<span class='it'><b>Mi sono fatto mandare</b> le foto</span>", ""],
       ["Me hizo <b>reír</b>", "<span class='it'>Mi <b>ha fatto ridere</b></span>", ""],
       ["Déjame <b>ver</b>", "<span class='it'><b>Fammi vedere</b></span> / <span class='it'>Lasciami vedere</span>", ""]])
hack("<span class='it'>fare</span> + infinito = <strong>hacer que ocurra</strong> (yo provoco). "
     "<span class='it'>lasciare</span> + infinito = <strong>dejar que ocurra</strong> (yo permito). "
     "Y los dos van SIEMPRE con infinitivo desnudo: nunca «fare che…». Si te sale un «che», es calco "
     "del español.", cuaderno=True)

h3("Ya lo tienes en el oído")
p("Esta construcción te ha salido en casi todas las canciones que has traído. No es un tema nuevo: "
  "es ponerle nombre a algo que ya reconoces.")
tabla(["Canción", "Verso", "Qué hace"],
      [["8 miliardi di persone", "<span class='it'>puoi <b>far entrare</b> tutte le persone</span>", "hacer entrar"],
       ["8 miliardi di persone", "<span class='it'>per <b>far sembrare</b> stupide le mie parole</span>", "hacer parecer"],
       ["Due ali", "<span class='it'>per <b>farmi volare</b> lontano</span>", "hacerme volar"],
       ["Due ali", "<span class='it'>le corde che ti <b>fanno stare</b> meglio</span>", "hacerte estar"]])

h2("Dónde van los pronombres")
p("Aquí es donde se rompe todo el mundo, y donde se junta con tus pronombres combinados del día 23.")
tabla(["Situación", "Regla", "Ejemplo"],
      [["Verbo conjugado", "el pronombre va DELANTE de <span class='it'>fare</span>",
        "<span class='it'>Me lo fai vedere?</span>"],
       ["Imperativo tú", "PEGADO, y <span class='it'>fare</span> se apocopa en <span class='it'>fa'</span>",
        "<span class='it'>Fammelo vedere!</span>"],
       ["Infinitivo", "PEGADO al final de <span class='it'>fare</span>",
        "<span class='it'>Voglio fartelo vedere.</span>"],
       ["Passato prossimo", "auxiliar AVERE, participio <b>invariable</b>",
        "<span class='it'>Gliel'ho fatto sapere.</span>"]])
alerta("<strong>Tres trampas:</strong> ① el participio de <span class='it'>fare</span> causativo "
       "<strong>NO concuerda</strong>: «le foto? <span class='it'>Gliele ho fatte mandare</span>» ← "
       "concuerda por el pronombre <em>gliele</em>, pero <span class='it'>fatto</span> como causativo "
       "se queda quieto en «<span class='it'>gliel'ho fatto sapere</span>». ② Con "
       "<span class='it'>fare</span> el imperativo se corta: <span class='it'>fa' + mi + lo = "
       "FAMMELO</span> (doble M). Igual pasa con <span class='it'>da'/di'/va'/sta'</span>: "
       "<span class='it'>dammelo, dimmelo, vattene, stammi bene</span>. ③ Si hay dos personas, la que "
       "ejecuta la acción lleva <span class='it'>A</span>: <span class='it'>«Faccio lavare la macchina "
       "A Marco»</span>.")

h3("farsi + infinito — hacerse hacer algo")
p("Cuando el favorecido eres tú mismo. Utilísimo en la vida real y suena avanzadísimo.")
tabla(["Italiano", "Español"],
      [["<span class='it'>Mi sono fatto tagliare i capelli</span>", "Me corté el pelo (me lo cortaron)"],
       ["<span class='it'>Mi faccio mandare il preventivo</span>", "Hago que me manden el presupuesto"],
       ["<span class='it'>Si è fatta aiutare da un amico</span>", "Hizo que un amigo la ayudara"]])
nota("Ojo al auxiliar: <span class='it'>farsi</span> es pronominale, así que en tiempos compuestos "
     "va con ESSERE y el participio de <em>farsi</em> concuerda: «mi sono fattO tagliare» (él) / "
     "«mi sono fattA tagliare» (ella).")

guiado(["<strong>1. ¿Qué quiero decir?</strong> «Hazme ver las fotos».",
        "<strong>2. ¿Quién hace la acción?</strong> Tú me las enseñas → causativo con "
        "<span class='it'>fare</span> + <span class='it'>vedere</span>.",
        "<strong>3. ¿Qué pronombres?</strong> a mí = <span class='it'>mi</span>, las fotos = "
        "<span class='it'>le</span> → combinados: <span class='it'>me le</span>.",
        "<strong>4. Imperativo tú → pegado y apocopado:</strong> fa' + me + le = "
        "<span class='it'>Fammele vedere!</span> ✅"],
       a_medias="Parte de: «Hazme saber el precio» (el precio = <span class='it'>il prezzo</span>). "
                "① ¿pronombres? ___ ② ¿combinados? ___ ③ Frase final: ___")

frasi_pronte([("Me lo fai vedere?", "¿Me lo enseñas?"),
              ("Fammi sapere!", "¡Avísame! / ¡Hazme saber!"),
              ("Mi sono fatto mandare il preventivo", "Hice que me mandaran el presupuesto"),
              ("Lascia perdere", "Déjalo / Olvídalo"),
              ("Non farmi ridere", "No me hagas reír")])

in_contesto(
    "— Ieri ho letto una storia strana. C'è della gente legata dentro una grotta, girata verso "
    "il muro.<br>\n"
    "  — Legata? E chi ce li ha messi?<br>\n"
    "  — Non si sa. Dietro c'è un fuoco, e passa gente con degli oggetti. Il fuoco "
    "<b>fa vedere</b> solo le ombre sul muro, e loro credono che le ombre siano il mondo.<br>\n"
    "  — <b>Roba da matti</b>. E nessuno li <b>lascia uscire</b>?<br>\n"
    "  — Uno esce. Il sole gli <b>fa male</b> agli occhi, ma alla fine vede le cose vere. Allora "
    "torna dentro e <b>glielo vuole far capire</b> agli altri.<br>\n"
    "  — E quelli non ci credono.<br>\n"
    "  — Peggio: si arrabbiano. Lui <b>glielo fa vedere</b> in tutti i modi, ma non "
    "<b>si lasciano convincere</b>. Alla fine gli dicono: «<b>Lascia perdere</b>».<br>\n"
    "  — Mmm. <b>Fammi sapere</b> come si chiama il libro, che me lo segno.",
    "«Ayer leí una historia rara. Hay gente atada dentro de una cueva, volteada hacia la pared.» — "
    "«¿Atada? ¿Y quién los metió ahí?» — «No se sabe. Detrás hay un fuego, y pasa gente con objetos. "
    "El fuego solo deja ver las sombras en la pared, y ellos creen que las sombras son el mundo.» — "
    "«Cosa de locos. ¿Y nadie los deja salir?» — «Uno sale. El sol le lastima los ojos, pero al final "
    "ve las cosas de verdad. Entonces vuelve adentro y quiere hacérselo entender a los demás.» — «Y "
    "esos no le creen.» — «Peor: se enojan. Él se lo enseña de todas las maneras, pero no se dejan "
    "convencer. Al final le dicen: “Déjalo”.» — «Mmm. Avísame cómo se llama el libro, que me lo apunto.»",
    tema="filosofia")

slang("Lascia perdere", reg="verde", fon="[LA-sha PER-de-re]",
      it="non insistere, non vale la pena occuparsene",
      es="déjalo / olvídalo / ni le muevas",
      uso="Literalmente «deja perder», y es causativo puro con <span class='it'>lasciare</span>. Una "
          "de las frases más dichas de Italia. Variante seca: «lascia stare».",
      ej=("Non risponde da tre giorni? Lascia perdere.",
          "¿Lleva tres días sin contestar? Déjalo."))

slang("Fammi sapere", reg="verde", fon="[FAM-mi sa-PE-re]",
      it="tienimi aggiornato, dimmi come va a finire",
      es="avísame / me cuentas",
      uso="El cierre de conversación italiano por excelencia, y es causativo con el pronombre pegado "
          "y la doble M. Formal: «mi faccia sapere». Se dice al despedirse casi por reflejo.",
      ej=("Fammi sapere se riesci a venire.",
          "Avísame si logras venir."))

slang("Roba da matti", reg="medio", fon="[RO-ba da MAT-ti]",
      it="una cosa assurda, incredibile",
      es="cosa de locos / una locura",
      uso="Para reaccionar ante algo indignante o absurdo. Fíjate en el <span class='it'>DA</span> de "
          "característica, el mismo de «occhi da bambina» en <em>Due ali</em>. También «roba da non "
          "crederci».",
      ej=("Mi ha fatto aspettare due ore. Roba da matti!",
          "Me hizo esperar dos horas. ¡Cosa de locos!"))

cultura(26, "Napoli",
        gancho="Veintiséis siglos de dominaciones, y una ciudad debajo de la ciudad",
        ctx=("Napoli divide: chi la ama lo fa in modo viscerale, chi non la capisce la trova caotica "
             "e incomprensibile. Non esiste una posizione neutrale. È stata fondata dai greci come "
             "Neapolis — città nuova — nel VI secolo a.C., ed è uno dei nomi più antichi ancora in "
             "uso in Italia. Poi è stata romana, bizantina, normanna, sveva, aragonese, spagnola per "
             "due secoli, austriaca, borbonica. Sotto la città moderna c'è una città sotterranea "
             "greca e romana: tunnel scavati nel tufo, cisterne, catacombe. In certi quartieri gli "
             "edifici affondano lentamente nel proprio passato. Non è una metafora.",
             "Nápoles divide: no hay posición neutral. Fundada por los griegos como Neapolis (ciudad "
             "nueva) en el siglo VI a.C., es uno de los nombres más antiguos aún en uso en Italia. "
             "Fue romana, bizantina, normanda, aragonesa, española dos siglos, austriaca, borbónica. "
             "Debajo hay una ciudad subterránea de túneles y cisternas, y en algunos barrios los "
             "edificios se hunden despacio en su propio pasado. No es metáfora."),
        frasi=[("Su Napoli non esiste una posizione neutrale.",
                "Sobre Nápoles no existe una posición neutral."),
               ("Sotto la città moderna c'è una città greca e romana.",
                "Debajo de la ciudad moderna hay una ciudad griega y romana."),
               ("Neapolis vuol dire «città nuova», ed è uno dei nomi più antichi d'Italia.",
                "Neapolis significa «ciudad nueva», y es uno de los nombres más antiguos de Italia.")],
        spunto="Usa i causativi di oggi per parlarne: «Napoli <b>ti fa</b> reagire, non <b>ti lascia</b> "
               "indifferente», «Cosa <b>ti farebbe</b> venire voglia di andarci?», «<b>Fammi sapere</b> "
               "se ci sei mai stato». Prova a spiegare a voce perché una città può dividere così.",
        puente="El paralelo mexicano es la Ciudad de México: fundada sobre un lago, con Tenochtitlan "
               "literalmente debajo del Zócalo, hundiéndose unos centímetros al año. Y también "
               "divide igual — quien la ama no sabe explicarlo, y quien no, solo ve el caos.")

dettato(["Fammelo vedere un attimo, per favore.",
         "Mi sono fatto mandare il preventivo per mail.",
         "Lascia perdere, non farti convincere."])

# ── ejercicios ──────────────────────────────────────────────────────────────
ej(1, "<strong>Fare o lasciare?</strong> — elige según el sentido: a) Mia madre mi ___ mangiare le "
      "verdure (me obliga). b) I miei mi ___ uscire fino a tardi (me lo permiten). c) Il film mi ___ "
      "piangere.", rows=3, ph="a) …")
solu(1, "a) <span class='it'>fa mangiare</span> (obliga) b) <span class='it'>lasciano uscire</span> "
        "(permite) c) <span class='it'>ha fatto piangere</span>")

ej(2, "<strong>Sin «che»</strong> — traduce sin calcar el subjuntivo español: a) Hago que venga. "
      "b) Me hizo reír. c) Hicieron que esperáramos dos horas.", rows=3, ph="a) …")
solu(2, "a) <span class='it'>Lo faccio venire.</span> b) <span class='it'>Mi ha fatto ridere.</span> "
        "c) <span class='it'>Ci hanno fatto aspettare due ore.</span> Nunca «faccio che venga».")

ej(3, "<strong>Pronombres delante</strong> — sustituye: a) Faccio vedere le foto a te → ___. "
      "b) Faccio sapere il prezzo a lui → ___. c) Fai vedere il contratto a noi → ___.", rows=3,
   ph="a) …", ripasso_tuo=True)
solu(3, "a) <span class='it'>Te le faccio vedere.</span> b) <span class='it'>Glielo faccio sapere.</span> "
        "c) <span class='it'>Ce lo fai vedere.</span>")

ej(4, "<strong>Imperativo con doble M</strong> — pega los pronombres: a) Fa' vedere a me il libro → "
      "___! b) Fa' sapere a me la data → ___! c) Fa' vedere a lui le prove → ___!", rows=3,
   ph="a) …")
solu(4, "a) <span class='it'>Fammelo vedere!</span> b) <span class='it'>Fammela sapere!</span> "
        "c) <span class='it'>Fagliele vedere!</span> (fa' + pronombre = doble consonante)")

ej(5, "<strong>farsi + infinito</strong> — traduce: a) Me corté el pelo. b) Hago que me manden el "
      "presupuesto. c) Se hizo ayudar por un amigo.", rows=3, ph="a) …")
solu(5, "a) <span class='it'>Mi sono fatto/a tagliare i capelli.</span> b) <span class='it'>Mi faccio "
        "mandare il preventivo.</span> c) <span class='it'>Si è fatto/a aiutare da un amico.</span>")

ej(6, "<strong>Reggenze</strong> — completa: Provo ___ farglielo capire · Cerco ___ farmi ascoltare · "
      "Continuo ___ far finta di niente.", rows=2, ph="…", ripasso_tuo=True)
solu(6, "Provo <span class='it'>a</span> · Cerco <span class='it'>di</span> · Continuo "
        "<span class='it'>a</span>.")

ej(7, "<strong>Diretto o indiretto?</strong> — di quién ejecuta la acción y ponle la preposición: "
      "a) Faccio lavare la macchina ___ Marco. b) Faccio leggere il testo ___ gli studenti.", rows=2,
   ph="a) …", ripasso_tuo=True)
solu(7, "a) <span class='it'>a Marco</span> b) <span class='it'>agli studenti</span>. Cuando hay dos "
        "personas, la que EJECUTA lleva A.")

ej(8, "<strong>Passato prossimo</strong> — completa el participio: a) Le foto? Gliele ho ___ (fare) "
      "vedere. b) Mi sono ___ (fare) mandare il file — habla una mujer. c) Ci ha ___ (fare) "
      "aspettare.", rows=2, ph="a) …")
solu(8, "a) <span class='it'>fatte</span> (concuerda con <em>gliele</em>) b) <span class='it'>fatta</span> "
        "(farsi va con essere y concuerda) c) <span class='it'>fatto</span> (invariable con avere).")

ej(9, "<strong>Caccia all'errore</strong> — corrige: a) «Faccio che lui venga». b) «Fai mi vedere!» "
      "c) «Mi ho fatto tagliare i capelli».", rows=3, ph="a) …")
solu(9, "a) <span class='it'>Lo faccio venire</span> (sin «che»). b) <span class='it'>Fammi vedere!</span> "
        "(pegado, doble M). c) <span class='it'>Mi SONO fatto tagliare</span> (farsi → essere).")

ej(10, "<strong>Il tuo vocabolario</strong> — 2 frases con → <strong class='mis-palabras'>(abre tu "
       "Vocabulario ★)</strong>, una con <span class='it'>fare + infinito</span> y otra con "
       "<span class='it'>farsi</span>.", rows=3, ph="…")
libre(10)

ej(11, "<strong>De las canciones</strong> — estos versos son causativos. Tradúcelos y di qué hace "
       "cada uno: a) <span class='it'>puoi far entrare tutte le persone</span> b) <span class='it'>"
       "per farmi volare lontano</span> c) <span class='it'>le corde che ti fanno stare meglio</span>",
   rows=3, ph="a) …")
solu(11, "a) «puedes dejar entrar a todas las personas» — hacer entrar. b) «para hacerme volar lejos» "
         "— hacerme volar. c) «las cuerdas que te hacen sentir mejor» — hacer que estés.")

ej(12, "<strong>Ascolto</strong> — escucha y escribe la frase; luego di si es fare o lasciare: " +
       audio([("1", "Fammi sapere come va a finire."),
              ("2", "Lascia perdere, non ne vale la pena."),
              ("3", "Me lo sono fatto mandare per mail.")]), rows=3, ph="…",
   ripasso_tuo=True)
solu(12, "1) <span class='it'>Fammi sapere come va a finire</span> — fare. 2) <span class='it'>Lascia "
         "perdere, non ne vale la pena</span> — lasciare. 3) <span class='it'>Me lo sono fatto mandare "
         "per mail</span> — farsi.")

ej(13, "<strong>En tu estudio</strong> — reescribe con causativo: a) «El cliente quiere ver las "
       "pruebas» → hazle verlas. b) «Necesito que me manden el contrato» → hazte que te lo manden. "
       "c) «Avísame cuando esté listo».", rows=3, ph="a) …")
solu(13, "a) <span class='it'>Gliele faccio vedere.</span> b) <span class='it'>Mi faccio mandare il "
         "contratto.</span> c) <span class='it'>Fammi sapere quando è pronto.</span>")

ej(14, "<strong>Fare vs lasciare, matiz</strong> — explica en 1 línea la diferencia entre: "
       "«<span class='it'>L'ho fatto parlare</span>» y «<span class='it'>L'ho lasciato parlare</span>».",
   rows=2, ph="…")
solu(14, "<span class='it'>L'ho fatto parlare</span> = lo obligué o provoqué que hablara (yo causo). "
         "<span class='it'>L'ho lasciato parlare</span> = no lo interrumpí, le permití hablar (yo "
         "permito). Fare provoca, lasciare permite.")

ej(15, "<strong>Produzione libera</strong> — escribe 6-8 líneas sobre <em>un encargo del estudio en "
       "el que dependiste de otras personas</em>: qué hiciste que hicieran, qué dejaste pasar y qué "
       "te hiciste mandar. Obligatorio: 3 <span class='it'>fare + infinito</span>, 1 "
       "<span class='it'>lasciare</span>, 1 <span class='it'>farsi</span> y un slang de hoy.",
   rows=7, ph="…")
libre(15)

autocontrollo("decir «lo faccio venire» sin meter «che»",
              "distinguir fare (provocar) de lasciare (permitir)",
              "pegar los pronombres: fammelo, fagliele",
              "usar farsi: mi sono fatto mandare")

riflessione(["Este es de los temas que más rendimiento te va a dar hablando, porque resuelve en dos "
             "palabras lo que el español necesita una subordinada entera para decir.",
             "Y fíjate en lo que acaba de pasar: no aprendiste algo nuevo, le pusiste nombre a algo "
             "que ya reconocías de <em>Due ali</em> y <em>8 miliardi di persone</em>. Eso es exactamente "
             "cómo se supone que funciona escuchar música en el idioma."],
            tiempo="50-60 min", domani="Concordanza dei tempi")

solu_guiado("① a mí = <span class='it'>mi</span>, el precio = <span class='it'>lo</span> · "
            "② combinados: <span class='it'>me lo</span> · ③ <span class='it'>Fammelo sapere!</span>")

guardar()
