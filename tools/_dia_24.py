# -*- coding: utf-8 -*-
"""Día 24 — Condizionale composto. Solo contenido: el andamiaje vive en dia_build.py."""
from dia_build import *

dia(24, semana=4, nivel="B2",
    titulo="Condizionale composto — avrei fatto",
    sub="El arrepentimiento, y el futuro que se ve desde el pasado")

objetivo("formar <span class='it'>avrei fatto</span> con los dos auxiliares",
         "expresar arrepentimiento y reproche",
         "usar el <strong>futuro nel passato</strong>, que el español no comparte",
         "cerrar el periodo ipotetico de 3er tipo")

ripasso("Del día 23: junta los pronombres — Do il libro a Marco → ___ · Mando le foto a voi → ___ · "
        "Y del 22, tu punto flojo: Provo ___ capire · Parto ___ Roma.")

h2("Come si forma")
p("<span class='it'>Condizionale di ESSERE o AVERE + participio passato.</span> Nada nuevo: es el "
  "condizionale que ya sabes, pero del auxiliar. Lo demás lo pone el participio.")
tabla(["", "Con AVERE (la mayoría)", "Con ESSERE (movimiento, pronominali)"],
      [["io", "avrei detto", "sarei andato / andata"],
       ["tu", "avresti detto", "saresti andato / andata"],
       ["lui/lei", "avrebbe detto", "sarebbe andato / andata"],
       ["noi", "avremmo detto", "saremmo andati / andate"],
       ["voi", "avreste detto", "sareste andati / andate"],
       ["loro", "avrebbero detto", "sarebbero andati / andate"]])
hack("el auxiliar es el MISMO que en el passato prossimo. Si dices <span class='it'>ho detto</span> "
     "→ <span class='it'>avrei detto</span>; si dices <span class='it'>sono andato</span> → "
     "<span class='it'>sarei andato</span>. Y con ESSERE el participio CONCUERDA: "
     "<span class='it'>sarei andatA</span> si habla una mujer.", cuaderno=True)

h2("Los 3 usos")
h3("1. Arrepentimiento y reproche — lo que no hiciste")
p("Es el uso más frecuente, y ya lo tienes en el oído: <span class='it'>«Non avremmo mai dovuto "
  "lasciarci»</span> es el estribillo entero de <em>Stavo pensando a te</em>.")
tabla(["Italiano", "Español", "Matiz"],
      [["<span class='it'>Avrei dovuto dirtelo</span>", "Debería habértelo dicho", "me arrepiento"],
       ["<span class='it'>Non avresti dovuto farlo</span>", "No deberías haberlo hecho", "te reprocho"],
       ["<span class='it'>Avrei voluto essere lì</span>", "Habría querido estar ahí", "deseo imposible"],
       ["<span class='it'>Sarei potuto venire</span>", "Habría podido venir", "posibilidad perdida"]])
nota("Con los modales (dovere, potere, volere) el auxiliar lo elige el verbo que va DETRÁS: "
     "<span class='it'>sarei potuto VENIRE</span> (venire va con essere) pero "
     "<span class='it'>avrei potuto FARLO</span> (fare va con avere).")

h3("2. Futuro nel passato — EL uso que el español no comparte")
p("Cuando cuentas desde el pasado algo que <em>entonces</em> era futuro. Aquí el italiano y el "
  "español se separan, y es el error más caro del tema.")
tabla(["Español", "Italiano", ""],
      [["Dijo que <b>vendría</b>", "<span class='it'>Ha detto che <b>sarebbe venuto</b></span>",
        "✅ compuesto"],
       ["Dijo que vendría", "<s>Ha detto che verrebbe</s>", "❌ el simple NO vale"],
       ["Sabía que no <b>lo lograría</b>", "<span class='it'>Sapevo che non <b>ce l'avrebbe fatta</b></span>", "✅"],
       ["Prometió que me <b>escribiría</b>", "<span class='it'>Ha promesso che mi <b>avrebbe scritto</b></span>", "✅"]])
alerta("<strong>La regla en una línea:</strong> si el verbo principal está en PASADO "
       "(ha detto, sapevo, ha promesso), el futuro que viene detrás va en condizionale "
       "<strong>COMPUESTO</strong>, no simple. El español usa el simple («dijo que vendría») y por "
       "eso lo calcamos mal. Truco para acordarte: el italiano mira ese futuro <em>desde hoy</em>, y "
       "desde hoy ya pasó — por eso lo pone en pasado.")

h3("3. Cierre del periodo ipotetico de 3er tipo")
p("Es la mitad derecha de la estructura que ya viste en <em>Alta Marea</em>: "
  "<span class='it'>«non ti avessi avuto attorno / SAREI CADUTO sul fondo»</span>.")
tabla(["Si (condición)", "→ Resultado"],
      [["<span class='it'>Se avessi studiato</span> (cong. trapassato)",
        "<span class='it'>avrei superato l'esame</span> (cond. composto)"],
       ["<span class='it'>Se fossi partito prima</span>",
        "<span class='it'>non avrei perso il treno</span>"]])

guiado(["<strong>1. ¿Qué quiero decir?</strong> «Dijo que me llamaría».",
        "<strong>2. ¿El verbo principal está en pasado?</strong> «ha detto» → sí. Entonces toca "
        "condizionale COMPUESTO.",
        "<strong>3. ¿Qué auxiliar pide <span class='it'>chiamare</span>?</strong> «ho chiamato» → "
        "AVERE → <span class='it'>avrebbe chiamato</span>.",
        "<strong>4. Monto la frase:</strong> <span class='it'>Ha detto che mi avrebbe chiamato.</span> ✅"],
       a_medias="Parte de: «Prometió que vendría a la fiesta». ① ¿principal en pasado? ___ "
                "② ¿auxiliar de <span class='it'>venire</span>? ___ ③ Frase final: ___")

frasi_pronte([("Avrei dovuto dirtelo prima", "Debería habértelo dicho antes"),
              ("Non avresti dovuto farlo", "No deberías haberlo hecho"),
              ("Ha detto che sarebbe arrivato tardi", "Dijo que llegaría tarde"),
              ("Al posto tuo non l'avrei fatto", "Yo en tu lugar no lo habría hecho"),
              ("Chi l'avrebbe mai detto!", "¡Quién lo hubiera dicho!")])

in_contesto(
    "— Allora, il cliente ha confermato?<br>\n"
    "  — Mi ha scritto ieri: ha detto che <b>avrebbe mandato</b> l'acconto entro venerdì, ma non è "
    "arrivato niente.<br>\n"
    "  — Mah. <b>Avresti dovuto</b> chiedergli una caparra prima di cominciare.<br>\n"
    "  — Lo so, <b>avrei dovuto</b>. Al posto tuo cosa <b>avresti fatto</b>?<br>\n"
    "  — Io gliel'<b>avrei chiesta</b> subito. Comunque non ti preoccupare: se non paga entro lunedì, "
    "gli scrivi tu.<br>\n"
    "  — Meno male che me l'hai detto. <b>Sarei stato</b> zitto un altro mese.",
    "«¿El cliente confirmó?» — «Me escribió ayer: dijo que mandaría el anticipo antes del viernes, "
    "pero no llegó nada.» — «Mmm. Deberías haberle pedido un depósito antes de empezar.» — «Lo sé, "
    "debería. En tu lugar, ¿qué habrías hecho?» — «Yo se lo habría pedido enseguida. De todos modos "
    "no te preocupes: si no paga el lunes, le escribes tú.» — «Menos mal que me lo dijiste. Me habría "
    "quedado callado otro mes.»")

slang("Meno male", reg="verde", fon="[ME-no MA-le]",
      it="per fortuna; è andata bene",
      es="menos mal / qué bueno que",
      uso="Literalmente «menos mal», igualito que en español. Se usa sola como reacción de alivio, o "
          "con «che»: «meno male che sei arrivato». De las expresiones más frecuentes del día a día.",
      ej=("Meno male che me l'hai detto, non ci avevo pensato.",
          "Menos mal que me lo dijiste, no lo había pensado."))

slang("Chi l'avrebbe mai detto!", reg="verde", fon="[ki la-VREB-be MAI DET-to]",
      it="espressione di sorpresa per qualcosa di inaspettato",
      es="¡quién lo hubiera dicho! / ¡quién iba a decirlo!",
      uso="Justo el tiempo de hoy, cristalizado en exclamación. Fíjate: es un condizionale composto "
          "puro, y se dice tal cual. Apréndetela entera y ya tienes el tiempo metido en la boca.",
      ej=("Si sono sposati? Chi l'avrebbe mai detto!",
          "¿Se casaron? ¡Quién lo hubiera dicho!"))

slang("Al posto tuo", reg="verde", fon="[al PO-sto TU-o]",
      it="se fossi in te; nella tua situazione",
      es="yo en tu lugar / si yo fuera tú",
      uso="Abre consejos y reproches, y casi siempre arrastra un condizionale detrás: «al posto tuo "
          "non l'avrei fatto». Variantes: al posto suo, al posto loro.",
      ej=("Al posto tuo gliel'avrei chiesto subito.",
          "Yo en tu lugar se lo habría pedido enseguida."))

cultura(24, "Caterina de' Medici",
        gancho="La florentina de catorce años que acabó gobernando Francia treinta",
        ctx=("Caterina de' Medici è arrivata in Francia nel 1533, a quattordici anni, per sposare il "
             "figlio del re. Non parlava francese, non aveva amici a corte e non era amata: la "
             "vedevano come un'italiana di banchieri, senza sangue blu. Per vent'anni è stata quasi "
             "invisibile, mentre suo marito amava apertamente Diane de Poitiers. Ha aspettato, ha "
             "imparato il francese alla perfezione, ha coltivato i nobili — e alla fine ha governato "
             "la Francia per trent'anni. Portò con sé cuochi e pasticcieri fiorentini che cambiarono "
             "per sempre la cucina francese.",
             "Llegó a Francia a los 14 años sin hablar francés y sin aliados; la despreciaban por ser "
             "hija de banqueros. Esperó veinte años en silencio mientras su marido amaba a otra, y "
             "acabó gobernando Francia tres décadas. Se llevó cocineros florentinos que cambiaron la "
             "cocina francesa."),
        frasi=[("Aveva solo quattordici anni e non parlava una parola di francese.",
                "Tenía solo catorce años y no hablaba una palabra de francés."),
               ("Nessuno avrebbe scommesso su di lei, eppure ha governato trent'anni.",
                "Nadie habría apostado por ella, y sin embargo gobernó treinta años."),
               ("La cucina francese le deve più di quanto i francesi ammettano.",
                "La cocina francesa le debe más de lo que los franceses admiten.")],
        spunto="Usa il condizionale composto di oggi per parlare di lei: «Al posto suo, io "
               "<b>me ne sarei andato</b> subito», «<b>Avrei reagito</b> diversamente», «Chi "
               "<b>l'avrebbe mai detto</b> che sarebbe finita così?». E tu, <b>avresti resistito</b> "
               "vent'anni in silenzio?",
        puente="El paralelo mexicano es Sor Juana: también la juzgaron por su origen y su condición "
               "antes que por su cabeza, y también ganó por dentro — con la pluma en vez de con la "
               "corte. Dos mujeres que esperaron, aprendieron y acabaron marcando el siglo.")

dettato(["Avrei dovuto dirtelo prima, scusa.",
         "Ha detto che sarebbe arrivato alle otto.",
         "Meno male che me l'hai chiesto, al posto tuo non l'avrei fatto."])

# ── ejercicios ──────────────────────────────────────────────────────────────
ej(1, "<strong>Forma il condizionale composto</strong> — pon el auxiliar correcto: io ___ (dire) · "
      "lei ___ (andare) · noi ___ (fare) · loro ___ (partire) · tu ___ (scrivere)", rows=2,
   ph="avrei detto, sarebbe andata…")
solu(1, "<span class='it'>avrei detto · sarebbe andata · avremmo fatto · sarebbero partiti · "
        "avresti scritto</span>. El auxiliar es el mismo del passato prossimo.")

ej(2, "<strong>Arrepentimiento</strong> — traduce: a) Debería haberte llamado. b) No deberías haber "
      "bebido tanto. c) Habría querido ayudarte.", rows=3, ph="a) Avrei dovuto chiamarti…")
solu(2, "a) <span class='it'>Avrei dovuto chiamarti.</span> b) <span class='it'>Non avresti dovuto "
        "bere così tanto.</span> c) <span class='it'>Avrei voluto aiutarti.</span>")

ej(3, "<strong>Futuro nel passato</strong> — pasa al pasado: «Dice che verrà» → «Ha detto che ___». "
      "«So che mi scriverà» → «Sapevo che mi ___». «Promette che lo farà» → «Ha promesso che lo ___».",
   rows=3, ph="sarebbe venuto…")
solu(3, "<span class='it'>sarebbe venuto · avrebbe scritto · avrebbe fatto</span>. Verbo principal "
        "en pasado → condizionale COMPUESTO, nunca el simple.")

ej(4, "<strong>Caccia all'errore</strong> — corrige: a) «Ha detto che verrebbe domani». "
      "b) «Sarei dovuto andare» (habla una mujer). c) «Avrei andato al mare».", rows=3, ph="…")
solu(4, "a) <span class='it'>Ha detto che sarebbe venuto</span> (futuro nel passato = compuesto). "
        "b) <span class='it'>Sarei dovuta andare</span> (con essere el participio concuerda). "
        "c) <span class='it'>Sarei andato/a</span> (andare va con essere, no con avere).")

ej(5, "<strong>Periodo ipotetico di 3° tipo</strong> — completa: Se ___ (studiare) di più, "
      "___ (superare) l'esame. · Se ___ (partire) prima, non ___ (perdere) il treno.", rows=2,
   ph="avessi studiato, avrei superato…")
solu(5, "<span class='it'>Se avessi studiato di più, avrei superato l'esame. Se fossi partito prima, "
        "non avrei perso il treno.</span> Cong. trapassato → condizionale composto.")

ej(6, "<strong>Reggenze</strong> — completa y luego mete un condizionale composto: Provo ___ "
      "spiegarglielo → «___ dovuto provare ___ spiegarglielo». · Cerco ___ capire · Parto ___ Roma.",
   rows=3, ph="a … Avrei dovuto provare a … di … per", ripasso_tuo=True)
solu(6, "Provo <span class='it'>a</span> → «<span class='it'>Avrei dovuto provare a spiegarglielo</span>» · "
        "Cerco <span class='it'>di</span> capire · Parto <span class='it'>per</span> Roma.")

ej(7, "<strong>Pronomi combinati + condizionale</strong> — traduce: a) Se lo habría dicho (a él). "
      "b) Te las habría mandado ayer. c) Me lo deberías haber dicho.", rows=3,
   ph="a) Gliel'avrei detto…", ripasso_tuo=True)
solu(7, "a) <span class='it'>Gliel'avrei detto.</span> b) <span class='it'>Te le avrei mandate ieri</span> "
        "(concordancia: mandatE). c) <span class='it'>Me lo avresti dovuto dire</span> / "
        "<span class='it'>Avresti dovuto dirmelo.</span>")

ej(8, "<strong>Al posto tuo…</strong> — da un consejo con condizionale composto para cada situación: "
      "a) Un amigo no cobró un trabajo. b) Alguien llegó tarde a una cita importante.", rows=3,
   ph="a) Al posto tuo gli avrei chiesto…")
solu(8, "Respuesta abierta, pero debe llevar condizionale composto. Ej.: a) <span class='it'>Al posto "
        "tuo gli avrei chiesto un acconto.</span> b) <span class='it'>Avrebbe dovuto avvisare prima.</span>")

ej(9, "<strong>Concordanza del participio</strong> — habla una mujer: a) «Sarei ___ (andare) volentieri». "
      "b) «Ci saremmo ___ (divertire)» (dos amigas). c) «Avrei ___ (fare) lo stesso».", rows=2,
   ph="andata, divertite, fatto")
solu(9, "a) <span class='it'>andata</span> b) <span class='it'>divertite</span> c) <span class='it'>fatto</span> "
        "— con AVERE el participio NO concuerda con el sujeto.")

ej(10, "<strong>Il tuo vocabolario</strong> — 2 frases con → <strong class='mis-palabras'>(abre tu "
       "Vocabulario ★)</strong>, una de arrepentimiento y otra de futuro nel passato.", rows=3, ph="…")
libre(10)

ej(11, "<strong>Ascolto</strong> — escucha y escribe la frase; luego di qué uso del condizionale es "
       "(arrepentimiento / futuro nel passato / hipotético): " +
       audio([("1", "Avrei dovuto ascoltarti."),
              ("2", "Mi ha detto che sarebbe passato più tardi."),
              ("3", "Se l'avessi saputo, non sarei venuto.")]), rows=3, ph="1. … (uso: …)",
   ripasso_tuo=True)
solu(11, "1) <span class='it'>Avrei dovuto ascoltarti</span> — arrepentimiento. "
         "2) <span class='it'>Mi ha detto che sarebbe passato più tardi</span> — futuro nel passato. "
         "3) <span class='it'>Se l'avessi saputo, non sarei venuto</span> — hipotético de 3er tipo.")

ej(12, "<strong>Del español, sin calcar</strong> — traduce cuidando el tiempo: «Me dijo que me "
       "escribiría, pero nunca lo hizo. Yo en su lugar habría avisado.»", rows=3,
   ph="Mi ha detto che mi avrebbe scritto…")
solu(12, "<span class='it'>Mi ha detto che mi avrebbe scritto, ma non l'ha mai fatto. Al posto suo "
         "avrei avvisato.</span>")

ej(13, "<strong>Modales</strong> — elige el auxiliar y explica por qué: «Sarei/Avrei potuto venire» · "
       "«Sarei/Avrei dovuto farlo» · «Sarei/Avrei voluto restare».", rows=3, ph="…")
solu(13, "<span class='it'>SAREI potuto venire</span> (venire→essere) · <span class='it'>AVREI dovuto "
         "farlo</span> (fare→avere) · <span class='it'>SAREI voluto restare</span> (restare→essere). "
         "Con los modales manda el auxiliar del verbo de DETRÁS.")

ej(14, "<strong>Chi l'avrebbe mai detto</strong> — escribe 3 cosas sorprendentes de tu año usando esa "
       "fórmula o «meno male che…».", rows=3, ph="Chi l'avrebbe mai detto che…")
solu(14, "Respuesta abierta. Debe usar <span class='it'>chi l'avrebbe mai detto che…</span> "
         "(+ indicativo o congiuntivo) o <span class='it'>meno male che…</span>")

ej(15, "<strong>Produzione libera</strong> — escribe 6-8 líneas contando <em>un trabajo del estudio "
       "que no salió como esperabas</em>: qué te dijeron que pasaría, qué pasó, y qué habrías hecho "
       "distinto. Obligatorio: 2 arrepentimientos (avrei dovuto…), 1 futuro nel passato (ha detto che "
       "sarebbe…) y 1 «al posto tuo/suo».", rows=7, ph="Il mese scorso un cliente…")
libre(15)

autocontrollo("formar avrei fatto / sarei andato sin dudar",
              "usar «ha detto che sarebbe venuto» y NO «verrebbe»",
              "elegir el auxiliar con los modales",
              "hacer concordar el participio con essere")

riflessione(["Este tiempo es el que convierte un relato plano en uno con capas: lo que pasó, lo que "
             "iba a pasar y lo que habría podido pasar. Es el salto de B1 a B2 en narración.",
             "Vuelve a oír el estribillo de <em>Stavo pensando a te</em>: "
             "<span class='it'>«non avremmo mai dovuto lasciarci»</span>. Ya no es una frase suelta, "
             "ahora sabes exactamente qué tiempo es y por qué."],
            tiempo="50-60 min", domani="Futuro anteriore")

solu_guiado("① sí, «ha promesso» está en pasado · ② venire → ESSERE → sarebbe venuto · "
            "③ <span class='it'>Ha promesso che sarebbe venuto alla festa.</span>")

guardar()
