# -*- coding: utf-8 -*-
"""Día 25 — Futuro anteriore. Solo contenido: el andamiaje vive en dia_build.py."""
from dia_build import *

dia(25, semana=4, nivel="B2",
    titulo="Futuro anteriore — avrò fatto",
    sub="Lo que habrá pasado antes… y la suposición que el español no tiene")

objetivo("formar <span class='it'>avrò fatto</span> con los dos auxiliares",
         "ordenar dos futuros: qué pasa antes y qué después",
         "usar el <strong>futuro di probabilità</strong> para suponer",
         "distinguir los tres futuros del italiano")

ripasso("Del día 24: pasa al pasado — «Dice che verrà» → «Ha detto che ___». Y forma: io ___ (fare) "
        "en condizionale composto.")

h2("Come si forma")
p("<span class='it'>Futuro semplice di ESSERE o AVERE + participio passato.</span> Otra vez lo mismo: "
  "cambia el auxiliar, el participio no se mueve.")
tabla(["", "Con AVERE", "Con ESSERE"],
      [["io", "avrò finito", "sarò arrivato / arrivata"],
       ["tu", "avrai finito", "sarai arrivato / arrivata"],
       ["lui/lei", "avrà finito", "sarà arrivato / arrivata"],
       ["noi", "avremo finito", "saremo arrivati / arrivate"],
       ["voi", "avrete finito", "sarete arrivati / arrivate"],
       ["loro", "avranno finito", "saranno arrivati / arrivate"]])
hack("los tres tiempos compuestos que ya conoces se construyen IGUAL — solo cambia en qué tiempo "
     "pones el auxiliar: <span class='it'>HO finito</span> (passato prossimo) · "
     "<span class='it'>AVREI finito</span> (condizionale composto, ayer) · "
     "<span class='it'>AVRÒ finito</span> (futuro anteriore, hoy). Aprendes uno y tienes los tres.",
     cuaderno=True)

h2("Los 2 usos")
h3("1. Anterioridad — lo que pasa ANTES de otro futuro")
p("Dos cosas van a pasar; la que ocurre primero va en futuro anteriore.")
tabla(["Italiano", "Español", "Orden"],
      [["<span class='it'>Quando <b>avrò finito</b>, ti chiamo</span>", "Cuando <b>termine</b>, te llamo",
        "1º terminar, 2º llamar"],
       ["<span class='it'>Dopo che <b>sarà arrivato</b>, mangiamo</span>", "Después de que <b>llegue</b>, comemos",
        "1º llegar, 2º comer"],
       ["<span class='it'>Appena <b>avrò capito</b>, ti spiego</span>", "En cuanto <b>entienda</b>, te explico",
        "1º entender, 2º explicar"]])
alerta("<strong>Aquí el español usa SUBJUNTIVO, el italiano usa FUTURO.</strong> «Cuando termine» "
       "(subjuntivo) = <span class='it'>quando avrò finito</span> (futuro anteriore). No traduzcas "
       "«cuando termine» por <s>«quando finisca»</s>: en italiano, tras <span class='it'>quando, "
       "dopo che, appena, non appena</span> con valor de futuro, va FUTURO. Ya lo viste en "
       "<em>Hollywood</em>: <span class='it'>«finché non sarà nero»</span>.")

h3("2. Futuro di probabilità — suponer, y esto el español NO lo tiene")
p("El uso más divertido y el que más te va a servir hablando: el futuro anteriore sirve para "
  "<strong>suponer sobre el pasado</strong>. No habla del futuro en absoluto.")
tabla(["Italiano", "Español", "Qué expresa"],
      [["<span class='it'>Sarà stato il vento</span>", "Habrá sido el viento", "supongo que fue"],
       ["<span class='it'>Avrà perso il treno</span>", "Se le habrá perdido el tren", "deduzco"],
       ["<span class='it'>Non avrà capito</span>", "No habrá entendido", "me imagino"],
       ["<span class='it'>Quanti anni avrà?</span>", "¿Cuántos años tendrá?", "cálculo aproximado"]])
nota("El futuro SIMPLE hace lo mismo pero sobre el presente: <span class='it'>«Dov'è Marco?» «Sarà a "
     "casa»</span> = «estará en casa» (supongo). Y el ANTERIORE lo hace sobre el pasado: "
     "<span class='it'>«Sarà andato a casa»</span> = «se habrá ido a casa». "
     "Español e italiano coinciden aquí más de lo que parece — «habrá sido» es exactamente eso.")

h2("Los tres futuros, en una tabla")
tabla(["Tiempo", "Forma", "Para qué", "Ejemplo"],
      [["Futuro semplice", "<span class='it'>finirò</span>", "futuro normal / suposición sobre el presente",
        "<span class='it'>Domani finirò · Sarà stanco</span>"],
       ["Futuro anteriore", "<span class='it'>avrò finito</span>", "anterioridad / suposición sobre el pasado",
        "<span class='it'>Quando avrò finito · Avrà perso il treno</span>"],
       ["Futuro nel passato", "<span class='it'>avrei finito</span>", "futuro visto desde el pasado (día 24)",
        "<span class='it'>Ha detto che avrebbe finito</span>"]])

guiado(["<strong>1. ¿Qué quiero decir?</strong> «Cuando haya mandado las fotos, te aviso».",
        "<strong>2. ¿Hay dos futuros?</strong> Sí: mandar (primero) y avisar (después).",
        "<strong>3. El PRIMERO va en futuro anteriore.</strong> mandare → «ho mandato» → AVERE → "
        "<span class='it'>avrò mandato</span>.",
        "<strong>4. Monto:</strong> <span class='it'>Quando avrò mandato le foto, ti avviso.</span> ✅ "
        "(el segundo puede ir en presente, como en español)"],
       a_medias="Parte de: «En cuanto haya llegado a casa, te llamo». ① ¿cuál pasa primero? ___ "
                "② ¿auxiliar de <span class='it'>arrivare</span>? ___ ③ Frase final: ___")

frasi_pronte([("Quando avrò finito, ti faccio sapere", "Cuando termine, te aviso"),
              ("Appena sarò arrivato ti scrivo", "En cuanto llegue te escribo"),
              ("Sarà stato il vento", "Habrá sido el viento"),
              ("Avrà avuto un imprevisto", "Le habrá surgido un imprevisto"),
              ("Boh, si sarà dimenticato", "Ni idea, se habrá olvidado")])

in_contesto(
    "— Hai visto? Il bar all'angolo ha chiuso.<br>\n"
    "  — Davvero? <b>Mannaggia</b>, ci andavo sempre. <b>Avranno perso</b> troppi soldi.<br>\n"
    "  — <b>Boh</b>. Secondo me <b>sarà stato</b> l'affitto: qui è salito tantissimo.<br>\n"
    "  — Può darsi. Oppure <b>si saranno stancati</b>: lavoravano dodici ore al giorno.<br>\n"
    "  — <b>Che ne dici</b>, riapre qualcun altro?<br>\n"
    "  — Quando <b>avrò parlato</b> col proprietario ti dico. Ma il posto è buono, appena "
    "<b>avranno rifatto</b> i muri lo prende qualcuno.<br>\n"
    "  — Speriamo. Un quartiere senza bar non è un quartiere.",
    "«¿Viste? El bar de la esquina cerró.» — «¿En serio? Qué lástima, yo iba siempre. Habrán perdido "
    "demasiado dinero.» — «Ni idea. Para mí habrá sido la renta: aquí subió muchísimo.» — «Puede ser. "
    "O se habrán cansado: trabajaban doce horas al día.» — «¿Qué dices, abrirá otro?» — «Cuando haya "
    "hablado con el dueño te digo. Pero el local es bueno; en cuanto hayan rehecho las paredes lo "
    "toma alguien.» — «Ojalá. Un barrio sin bar no es un barrio.»",
    tema="negocios")

slang("Boh", reg="verde", fon="[bo, corto y seco]",
      it="non lo so, non ne ho idea",
      es="ni idea / sepa / quién sabe",
      uso="La respuesta italiana por excelencia cuando no sabes algo, y encaja perfecto con las "
          "suposiciones de hoy: «boh, sarà stato il vento». Se dice sola, encogiendo los hombros. "
          "No confundir con «mah» (duda o escepticismo).",
      ej=("— Perché non risponde? — Boh, avrà il telefono spento.",
          "«¿Por qué no contesta?» — «Ni idea, tendrá el teléfono apagado.»"))

slang("Che ne dici?", reg="verde", fon="[ke ne DI-chi]",
      it="cosa ne pensi? sei d'accordo?",
      es="¿qué te parece? / ¿cómo ves?",
      uso="Para proponer algo o pedir opinión. Fíjate en el <span class='it'>ne</span>, el mismo "
          "pronombre de «non me ne frega». Formal: «che ne pensa?». Variante: «che ne dici di + "
          "infinito» = ¿qué tal si…?",
      ej=("Che ne dici di rimandare a domani?",
          "¿Qué te parece si lo dejamos para mañana?"))

slang("Mannaggia!", reg="medio", fon="[man-NAD-ja]",
      it="esclamazione di fastidio o delusione, senza volgarità",
      es="¡rayos! / ¡qué lata!",
      uso="Del napolitano «male ne aggia» (que le venga mal). Es la palabrota que NO es palabrota: "
          "puedes decirla delante de cualquiera. Muy usada con «a…»: «mannaggia a me!» = ¡qué tonto soy!",
      ej=("Mannaggia, avrò lasciato le chiavi in ufficio!",
          "¡Rayos, habré dejado las llaves en la oficina!"))

cultura(25, "Donatello",
        gancho="Michelangelo dijo que era el más grande — y hoy suena a tortuga ninja",
        ctx=("Michelangelo — il più grande scultore che il mondo abbia conosciuto, secondo quasi "
             "tutti — diceva che Donatello era superiore a lui. Non per modestia: perché era vero. "
             "Donatello ha aperto ogni porta che Michelangelo ha poi attraversato. Figlio di un "
             "lavorante tessile, è andato a Roma con l'amico Brunelleschi verso il 1404 e insieme "
             "hanno passato mesi a misurare e disegnare le rovine antiche. Eppure oggi, nella "
             "coscienza popolare, il suo nome è associato soprattutto a una tartaruga ninja.",
             "Miguel Ángel decía que Donatello era superior a él, y no por modestia. Hijo de un "
             "obrero textil, fue a Roma con Brunelleschi hacia 1404 y pasaron meses midiendo y "
             "dibujando ruinas antiguas. Hoy su nombre suena, sobre todo, a tortuga ninja."),
        frasi=[("Michelangelo diceva che Donatello era più grande di lui.",
                "Miguel Ángel decía que Donatello era más grande que él."),
               ("È andato a Roma con Brunelleschi a misurare le rovine.",
                "Fue a Roma con Brunelleschi a medir las ruinas."),
               ("Oggi lo conoscono più per la tartaruga ninja che per le sue sculture.",
                "Hoy lo conocen más por la tortuga ninja que por sus esculturas.")],
        spunto="Usa le supposizioni di oggi: «Quanti anni <b>avrà avuto</b> quando è andato a Roma?», "
               "«<b>Avrà passato</b> mesi a disegnare», «Chi <b>avrà scelto</b> i nomi delle "
               "tartarughe?». Prova a fare tre ipotesi su di lui, ad alta voce, senza cercare i dati.",
        puente="Pasa igual con Tamayo frente a Rivera: uno llenó los muros y las portadas, el otro "
               "abrió caminos que hoy se dan por hechos. La fama y la importancia rara vez van del "
               "brazo — y a veces una caricatura pesa más que un museo.")

dettato(["Quando avrò finito, ti faccio sapere.",
         "Boh, sarà rimasto senza batteria.",
         "Mannaggia, avrà perso il treno un'altra volta."])

# ── ejercicios ──────────────────────────────────────────────────────────────
ej(1, "<strong>Forma il futuro anteriore</strong>: io ___ (finire) · tu ___ (arrivare) · noi ___ "
      "(capire) · lei ___ (partire) · loro ___ (mangiare)", rows=2, ph="avrò finito, sarai arrivato…")
solu(1, "<span class='it'>avrò finito · sarai arrivato/a · avremo capito · sarà partita · avranno "
        "mangiato</span>")

ej(2, "<strong>Anterioridad</strong> — une con el tiempo correcto: a) Quando ___ (io, finire) il "
      "lavoro, esco. b) Appena ___ (tu, arrivare), chiamami. c) Dopo che ___ (loro, mangiare), "
      "andiamo.", rows=3, ph="avrò finito…")
solu(2, "a) <span class='it'>avrò finito</span> b) <span class='it'>sarai arrivato</span> "
        "c) <span class='it'>avranno mangiato</span>")

ej(3, "<strong>El español dice subjuntivo, el italiano futuro</strong> — traduce: a) Cuando termine, "
      "te aviso. b) En cuanto llegues, escríbeme. c) Después de que lo haya visto, te digo.", rows=3,
   ph="a) Quando avrò finito, ti avviso…")
solu(3, "a) <span class='it'>Quando avrò finito, ti avviso.</span> b) <span class='it'>Appena sarai "
        "arrivato, scrivimi.</span> c) <span class='it'>Dopo che l'avrò visto, ti dico.</span> "
        "Nunca «quando finisca».")

ej(4, "<strong>Futuro di probabilità</strong> — convierte la certeza en suposición: a) «Ha perso il "
      "treno» → ___. b) «È andato a casa» → ___. c) «Non ha capito» → ___.", rows=3,
   ph="a) Avrà perso il treno…")
solu(4, "a) <span class='it'>Avrà perso il treno.</span> b) <span class='it'>Sarà andato a casa.</span> "
        "c) <span class='it'>Non avrà capito.</span>")

ej(5, "<strong>Semplice o anteriore?</strong> — suposición sobre el PRESENTE o sobre el PASADO: "
      "a) ¿Dónde estará ahora? b) ¿Dónde habrá estado ayer? c) Tendrá unos cuarenta años. "
      "d) Habrá tenido un problema.", rows=3, ph="a) Dove sarà adesso?…")
solu(5, "a) <span class='it'>Dove sarà adesso?</span> (semplice) b) <span class='it'>Dove sarà stato "
        "ieri?</span> (anteriore) c) <span class='it'>Avrà una quarantina d'anni.</span> (semplice) "
        "d) <span class='it'>Avrà avuto un problema.</span> (anteriore)")

ej(6, "<strong>Los tres futuros</strong> — completa con el correcto: a) Domani ___ (io, partire) "
      "presto. b) Quando ___ (io, partire), ti scrivo. c) Ha detto che ___ (lui, partire) presto.",
   rows=3, ph="a) partirò b) sarò partito c) sarebbe partito")
solu(6, "a) <span class='it'>partirò</span> (semplice) b) <span class='it'>sarò partito</span> "
        "(anteriore) c) <span class='it'>sarebbe partito</span> (futuro nel passato, día 24)")

ej(7, "<strong>Clitici</strong> — pon el pronombre y conjuga en futuro anteriore: a) Quando ___ "
      "(mandare, le foto a lui) → «Quando ___ ___». b) Appena ___ (dire, la verità a me) → «Appena "
      "___ ___».", rows=3, ph="Quando gliele avrò mandate…", ripasso_tuo=True)
solu(7, "a) <span class='it'>Quando gliele avrò mandate…</span> (concordancia: mandatE) "
        "b) <span class='it'>Appena me l'avrai detta…</span>")

ej(8, "<strong>Reggenze</strong> — completa: Appena ___ (io, riuscire) ___ finire, ti chiamo · "
      "Quando ___ (io, smettere) ___ lavorare, usciamo · Dopo che ___ (io, provare) ___ farlo, ti dico.",
   rows=3, ph="sarò riuscito a … avrò smesso di … avrò provato a", ripasso_tuo=True)
solu(8, "<span class='it'>sarò riuscito A · avrò smesso DI · avrò provato A</span>. Riuscire A, "
        "smettere DI, provare A.")

ej(9, "<strong>Concordanza</strong> — habla una mujer o un grupo: a) «___ (io, arrivare) tardi». "
       "b) «Quando ___ (noi, finire) — dos amigas». c) «___ (loro, partire) senza di noi».", rows=2,
   ph="Sarò arrivata…")
solu(9, "a) <span class='it'>Sarò arrivata</span> b) <span class='it'>saremo finite</span>… ojo: "
        "<em>finire</em> aquí es transitivo → <span class='it'>avremo finito</span> (con avere no "
        "concuerda) c) <span class='it'>Saranno partiti/e</span>")

ej(10, "<strong>Il tuo vocabolario</strong> — 2 frases con → <strong class='mis-palabras'>(abre tu "
       "Vocabulario ★)</strong>, una con anterioridad y otra con suposición.", rows=3, ph="…")
libre(10)

ej(11, "<strong>Ascolto</strong> — escucha y di si es anterioridad o suposición: " +
       audio([("1", "Quando avrò finito il progetto, mi prendo una settimana."),
              ("2", "Non risponde, avrà il telefono spento."),
              ("3", "Appena sarà arrivata, cominciamo.")]), rows=3, ph="1. … (uso: …)",
   ripasso_tuo=True)
solu(11, "1) anterioridad 2) suposición (aquí futuro semplice, sobre el presente) 3) anterioridad.")

ej(12, "<strong>Caccia all'errore</strong> — corrige: a) «Quando finisca, ti chiamo». b) «Sarò "
       "finito il lavoro» (yo termino el trabajo). c) «Avrà andato a casa».", rows=3, ph="…")
solu(12, "a) <span class='it'>Quando avrò finito</span> (futuro, no subjuntivo) b) <span class='it'>"
         "Avrò finito il lavoro</span> (finire transitivo → avere) c) <span class='it'>Sarà andato</span> "
         "(andare → essere)")

ej(13, "<strong>Suposiciones en cadena</strong> — alguien no llegó a una cita. Escribe 3 hipótesis "
       "distintas con futuro anteriore, empezando una con «boh».", rows=3, ph="Boh, avrà…")
solu(13, "Respuesta abierta. Deben ser futuro anteriore: <span class='it'>avrà perso il treno · si "
         "sarà dimenticato · sarà rimasto bloccato nel traffico</span>.")

ej(14, "<strong>Che ne dici?</strong> — propón 2 planes usando «che ne dici di + infinito» y responde "
       "a cada uno suponiendo un obstáculo con futuro anteriore.", rows=3,
   ph="— Che ne dici di…? — Mah, avrà…")
solu(14, "Respuesta abierta. Estructura: <span class='it'>Che ne dici di uscire stasera? — Boh, "
         "Marco avrà già altri piani.</span>")

ej(15, "<strong>Produzione libera</strong> — escribe 6-8 líneas sobre <em>un día de trabajo que "
       "todavía no ha pasado</em>: qué harás cuando hayas terminado cada cosa, y qué supones que "
       "habrá pasado con un cliente que no contesta. Obligatorio: 3 de anterioridad (quando/appena + "
       "futuro anteriore), 2 suposiciones y 1 slang de hoy.", rows=7,
   ph="Domani, appena sarò arrivato in studio…")
libre(15)

autocontrollo("formar avrò finito / sarò arrivato",
              "decir «quando avrò finito» y NO «quando finisca»",
              "suponer con «sarà stato il vento»",
              "distinguir los tres futuros")

riflessione(["El <em>futuro di probabilità</em> es de lo más útil que te llevas: te permite opinar "
             "sin comprometerte, que es medio arte de la conversación italiana. Y no tiene traducción "
             "directa — el español lo hace, pero mucho menos.",
             "Con el día de ayer ya tienes los tres futuros del italiano. Vuelve a la tabla "
             "comparativa cuando dudes: es el mapa entero en cuatro filas."],
            tiempo="50-60 min", domani="Verbi causativi")

solu_guiado("① llegar pasa primero · ② arrivare → ESSERE → sarò arrivato · "
            "③ <span class='it'>Appena sarò arrivato a casa, ti chiamo.</span>")

guardar()
