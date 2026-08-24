# -*- coding: utf-8 -*-
"""Día 27 — Concordanza dei tempi. Solo contenido: el andamiaje vive en dia_build.py."""
from dia_build import *

dia(27, semana=4, nivel="B2",
    titulo="Concordanza dei tempi — la consecutio temporum",
    sub="Cuando mueves el verbo principal al pasado, todo lo demás se mueve con él")

objetivo("encajar el congiuntivo según el tiempo del verbo principal",
         "usar <span class='it'>avessi fatto</span> y <span class='it'>sarebbe venuto</span> en su sitio",
         "pasar del discurso directo al indirecto sin que se desmonte",
         "saber qué verbos NO piden congiuntivo (que son más de los que crees)")

ripasso("Del día 26: completa — Il cliente vuole le prove → ___ (yo, hacérselas ver) stasera · "
        "Non ___ (dejarte) convincere. Y del 24: Ha detto che ___ (venire) più tardi.")

h2("El mecanismo: una escalera, no una lista")
p("Esto no es memorizar veinte combinaciones. Es <strong>una sola idea</strong>: el verbo principal "
  "fija la planta del edificio, y el subordinado se coloca arriba, al mismo nivel o abajo, según sea "
  "<em>posterior, simultáneo o anterior</em>. Si mueves la planta baja al pasado, todo el edificio "
  "baja un piso.")
big("Principal en PRESENTE → el edificio está arriba.<br>"
    "Principal en PASADO → todo baja un escalón.")

h3("① Principal en presente")
tabla(["Relación", "Qué va", "Ejemplo"],
      [["Simultáneo", "congiuntivo <b>presente</b>",
        "<span class='it'>Penso che <b>sia</b> stanco.</span> — Creo que está cansado."],
       ["Anterior", "congiuntivo <b>passato</b>",
        "<span class='it'>Penso che <b>sia stato</b> stanco.</span> — Creo que estuvo cansado."],
       ["Posterior", "futuro o presente",
        "<span class='it'>Penso che <b>verrà</b>.</span> — Creo que vendrá."]])

h3("② Principal en pasado — aquí se juega el partido")
tabla(["Relación", "Qué va", "Ejemplo"],
      [["Simultáneo", "congiuntivo <b>imperfetto</b>",
        "<span class='it'>Pensavo che <b>fosse</b> stanco.</span> — Creía que estaba cansado."],
       ["Anterior", "congiuntivo <b>trapassato</b>",
        "<span class='it'>Pensavo che <b>fosse stato</b> stanco.</span> — Creía que había estado cansado."],
       ["Posterior", "<b>condizionale composto</b>",
        "<span class='it'>Pensavo che <b>sarebbe venuto</b>.</span> — Creía que vendría."]])
hack("Esa última casilla es el día 24 entero. El <span class='it'>condizionale composto</span> no era "
     "un tema suelto: es <strong>el escalón «posterior» de la consecutio</strong>. Por eso "
     "<span class='it'>«Ha detto che sarebbe venuto»</span> y nunca <span class='it'>«verrebbe»</span> "
     "— ya lo sabías hacer, hoy sabes por qué.", cuaderno=True)

h2("Dónde se rompe el español")
p("El español tiene consecutio, así que el concepto no es nuevo. El problema es otro: hay verbos que "
  "en español van con indicativo y en italiano <strong>exigen congiuntivo</strong>, y ahí el oído no "
  "te avisa.")
tabla(["Español (indicativo)", "Italiano (congiuntivo)", ""],
      [["Creo que <b>es</b> tarde", "<span class='it'>Credo che <b>sia</b> tardi</span>", "credere"],
       ["Pienso que <b>se aprende</b>", "<span class='it'>Penso che si <b>impari</b></span>", "pensare"],
       ["Parece que <b>está</b> bien", "<span class='it'>Sembra che <b>stia</b> bene</span>", "sembrare"],
       ["Espero que <b>llega</b> a tiempo", "<span class='it'>Spero che <b>arrivi</b> in tempo</span>", "sperare"],
       ["Aunque <b>es</b> difícil", "<span class='it'>Benché <b>sia</b> difficile</span>", "benché"]])
alerta("<strong>Y ahora el contrapeso, que importa igual:</strong> hay verbos que NO piden congiuntivo "
       "y donde meterlo suena mal. Van con <b>indicativo</b>: <span class='it'>so che, sono sicuro "
       "che, è vero che, dice che, mi sa che, siccome, perché</span> (causal). "
       "<span class='it'>«So che è tardi»</span>, no «<span class='it'>sia</span>». El congiuntivo es "
       "para lo que <em>filtras</em> por tu cabeza (opinión, duda, deseo); el indicativo, para lo que "
       "<em>das por hecho</em>.")

fosil("Tu punto pegajoso: la elisión",
      "En los días 23 y 24 escribiste ocho veces <span class='it'>glielo ho</span>, "
      "<span class='it'>glielo avrei</span>, <span class='it'>me lo avresti</span>. Y sin embargo "
      "pusiste <span class='it'>Me l'ha data</span> y <span class='it'>non l'ho fatto</span> "
      "perfectos. O sea: la regla la tienes en el pronombre suelto y no la trasladas al combinado. "
      "<strong>LO y LA se eliden SIEMPRE ante vocal, también dentro del grupo:</strong> "
      "<span class='it'>gliel'ho detto, gliel'avrei dato, me l'avessi detto, te l'ho mandata</span>. "
      "Regla de bolsillo: si al leerlo en voz alta dices «glie-LO-ho», estás pronunciando dos vocales "
      "seguidas que el italiano no tolera. Hoy va en el ejercicio 7 y en el dictado.")

guiado(["<strong>1. ¿Qué quiero decir?</strong> «Pensé que ya me lo habías dicho».",
        "<strong>2. ¿En qué tiempo va el principal?</strong> «Pensé» → pasado "
        "(<span class='it'>pensavo / ho pensato</span>). Todo baja un escalón.",
        "<strong>3. ¿Qué relación?</strong> «habías dicho» ocurre ANTES de «pensé» → anterior → "
        "congiuntivo <b>trapassato</b>: <span class='it'>avessi detto</span>.",
        "<strong>4. ¿Pronombres?</strong> a mí = <span class='it'>mi</span>, eso = "
        "<span class='it'>lo</span> → <span class='it'>me lo</span> → y ante vocal se elide: "
        "<span class='it'>me l'</span>.",
        "<strong>5. Frase final:</strong> <span class='it'>Pensavo che me l'avessi già detto.</span> ✅"],
       a_medias="Parte de: «Creía que ya se lo habían mandado (a él)». ① ¿tiempo del principal? ___ "
                "② ¿anterior o simultáneo? ___ ③ ¿pronombres, con elisión? ___ ④ Frase final: ___")

frasi_pronte([("Pensavo che fosse più facile", "Creía que era más fácil"),
              ("Non sapevo che te l'avessero detto", "No sabía que te lo hubieran dicho"),
              ("Mi sa che è tardi", "Me late que es tarde"),
              ("Speravo che sarebbe andata meglio", "Esperaba que saliera mejor"),
              ("Non è che sia difficile, è che è lungo", "No es que sea difícil, es que es largo")])

in_contesto(
    "— Allora, com'era la mostra?<br>\n"
    "  — Mah. <b>Pensavo che fosse</b> più grande. Erano quattro stanze in tutto.<br>\n"
    "  — Ma come? Mi <b>avevano detto che sarebbe stata</b> enorme.<br>\n"
    "  — Eh, <b>non è che sia</b> brutta, anzi. È che ti aspetti altro dopo tutta quella pubblicità.<br>\n"
    "  — <b>Chissà</b> quanto <b>avranno speso</b> per i manifesti in metropolitana.<br>\n"
    "  — Comunque un quadro mi ha colpito davvero. <b>Non sapevo che l'avesse dipinto</b> a "
    "ottant'anni: sembra il lavoro di un ragazzo.<br>\n"
    "  — Bello. <b>Mi sa che</b> ci vado sabato, allora.<br>\n"
    "  — Vacci presto. <b>Speravo che ci fosse</b> meno gente e invece c'era la fila fuori.",
    "«¿Y qué tal la exposición?» — «Uf. Creía que era más grande. Eran cuatro salas en total.» — "
    "«¿Cómo? A mí me habían dicho que sería enorme.» — «Sí, no es que sea mala, al contrario. Es que "
    "esperas otra cosa después de toda esa publicidad.» — «Quién sabe cuánto habrán gastado en los "
    "carteles del metro.» — «De todos modos un cuadro sí me impactó. No sabía que lo hubiera pintado "
    "a los ochenta: parece el trabajo de un chavo.» — «Qué bien. Me late que voy el sábado, "
    "entonces.» — «Ve temprano. Esperaba que hubiera menos gente y había fila afuera.»",
    tema="arte")

slang("Mi sa che", reg="verde", fon="[mi sa ke]",
      it="ho l'impressione che, credo proprio che",
      es="me late que / me da que / se me hace que",
      uso="Literalmente «me sabe que». Es la forma más italiana de decir «creo» — y aquí está lo bueno: "
          "<strong>va con INDICATIVO</strong>, no con congiuntivo. <span class='it'>«Mi sa che è "
          "tardi»</span>, nunca «sia». Sirve de contrapeso perfecto a <span class='it'>penso che</span>.",
      ej=("Mi sa che non viene più.",
          "Me late que ya no viene."))

slang("Non è che…", reg="verde", fon="[non e ke]",
      it="non è esattamente che…, usato per attenuare o per chiedere con delicatezza",
      es="no es que… / ¿no será que…?",
      uso="Dos usos. Para matizar: <span class='it'>«Non è che <b>sia</b> brutto, è che non mi "
          "convince»</span> — y ahí SÍ pide congiuntivo. Y para pedir sin sonar brusco: "
          "<span class='it'>«Non è che mi presti dieci euro?»</span>, que es «¿no me prestarías…?». "
          "Muy usado para suavizar.",
      ej=("Non è che tu abbia visto le mie chiavi?",
          "¿No habrás visto mis llaves?"))

slang("Chissà", reg="verde", fon="[kis-SA]",
      it="chi lo sa, non ho idea — ma detto con curiosità",
      es="quién sabe / a saber / vaya usted a saber",
      uso="Contracción de <span class='it'>chi sa</span>. A diferencia de <span class='it'>boh</span> "
          "(que cierra), <span class='it'>chissà</span> abre: invita a especular. Y encaja con el "
          "futuro de probabilidad del día 25: <span class='it'>«Chissà chi sarà stato»</span> = quién "
          "sabe quién habrá sido.",
      ej=("Chissà cosa avrà pensato quando l'ha visto.",
          "Quién sabe qué habrá pensado cuando lo vio."))

cultura(27, "Mussolini",
        gancho="Cómo un país llega ahí, y por qué la lengua todavía lo arrastra",
        ctx=("Benito Mussolini prese il potere nel 1922 e lo tenne per vent'anni. Il fascismo non "
             "arrivò con un colpo di stato improvviso: arrivò dopo anni di crisi economica, "
             "disoccupazione e violenza politica, e molti pensarono che sarebbe stato una parentesi "
             "breve. Non lo fu. Il regime controllò la stampa, sciolse i partiti, entrò in guerra a "
             "fianco della Germania nazista e nel 1938 promulgò le leggi razziali. Finì nel 1945. "
             "Il fascismo lavorò molto anche sulla lingua: vietò le parole straniere — il "
             "<i>bar</i> doveva diventare <i>qui si beve</i> — e impose il <i>voi</i> al posto del "
             "<i>Lei</i>, considerato servile e straniero. Quasi nulla di tutto questo sopravvisse.",
             "Mussolini tomó el poder en 1922 y lo mantuvo veinte años. El fascismo no llegó con un "
             "golpe repentino: llegó tras años de crisis, desempleo y violencia política, y muchos "
             "pensaron que sería un paréntesis breve. No lo fue. El régimen controló la prensa, "
             "disolvió los partidos, entró en guerra junto a la Alemania nazi y en 1938 promulgó las "
             "leyes raciales. Terminó en 1945. El fascismo también intervino la lengua: prohibió los "
             "extranjerismos —el <i>bar</i> debía llamarse <i>qui si beve</i>— e impuso el <i>voi</i> "
             "en lugar del <i>Lei</i>, considerado servil y extranjero. Casi nada de eso sobrevivió."),
        frasi=[("Molti pensarono che sarebbe stata una parentesi breve.",
                "Muchos pensaron que sería un paréntesis breve."),
               ("Il regime impose il «voi» al posto del «Lei».",
                "El régimen impuso el «voi» en lugar del «Lei»."),
               ("Non tutti sapevano cosa stesse succedendo, ma molti preferirono non guardare.",
                "No todos sabían qué estaba pasando, pero muchos prefirieron no mirar.")],
        spunto="Fíjate en las tres frases de arriba: <b>pensarono che sarebbe stata</b>, <b>cosa "
               "stesse succedendo</b>. Es la consecutio de hoy, funcionando en un texto real de "
               "historia — que es exactamente donde vas a encontrártela. Prueba a contar en voz alta, "
               "con <span class='it'>pensavo che…</span> y <span class='it'>non sapevo che…</span>, "
               "algo que creíste de un periodo histórico y luego resultó ser distinto.",
        puente="El paralelo mexicano más honesto no es un dictador militar sino el Porfiriato: "
               "treinta y cinco años de un gobierno que también empezó prometiendo orden y progreso "
               "tras décadas de caos, que también modernizó infraestructura, y que también acabó "
               "sosteniéndose con represión. Y el mismo eco incómodo: hay quien todavía dice «pero "
               "hizo cosas buenas», que es la frase con la que empiezan casi todas las conversaciones "
               "difíciles sobre este capítulo, en México y en Italia.")

dettato(["Pensavo che me l'avessi già detto.",
         "Mi sa che non gliel'hanno mandato.",
         "Non sapevo che sarebbe venuto anche lui."])

# ── ejercicios ──────────────────────────────────────────────────────────────
ej(1, "<strong>Principal en presente</strong> — pon el congiuntivo que toca: a) Penso che lui ___ "
      "(essere) stanco adesso. b) Penso che ieri ___ (essere) stanco. c) Credo che domani ___ "
      "(venire).", rows=3, ph="a) …")
solu(1, "a) <span class='it'>sia</span> (simultáneo) b) <span class='it'>sia stato</span> (anterior) "
        "c) <span class='it'>verrà</span> (posterior — con futuro, no congiuntivo).")

ej(2, "<strong>Principal en pasado</strong> — baja todo un escalón: a) Pensavo che ___ (essere) "
      "stanco. b) Pensavo che ___ (essere) stanco il giorno prima. c) Pensavo che ___ (venire) "
      "il giorno dopo.", rows=3, ph="a) …")
solu(2, "a) <span class='it'>fosse</span> (imperfetto) b) <span class='it'>fosse stato</span> "
        "(trapassato) c) <span class='it'>sarebbe venuto</span> (condizionale composto — el día 24).")

ej(3, "<strong>El escalón «posterior»</strong> — traduce, y fíjate en que el español usa condicional "
      "simple donde el italiano usa compuesto: a) Dijo que llamaría. b) Sabía que no vendrían. "
      "c) Prometió que lo haría.", rows=3, ph="a) …")
solu(3, "a) <span class='it'>Ha detto che avrebbe chiamato.</span> b) <span class='it'>Sapevo che non "
        "sarebbero venuti.</span> c) <span class='it'>Ha promesso che l'avrebbe fatto.</span> Nunca "
        "«chiamerebbe», «verrebbero», «farebbe».")

ej(4, "<strong>El español te traiciona</strong> — estos van con indicativo en español y con "
      "congiuntivo en italiano: a) Creo que es tarde. b) Pienso que de los errores se aprende. "
      "c) Parece que está bien.", rows=3, ph="a) …")
solu(4, "a) <span class='it'>Credo che <b>sia</b> tardi.</span> b) <span class='it'>Penso che dagli "
        "errori si <b>impari</b>.</span> c) <span class='it'>Sembra che <b>stia</b> bene.</span> "
        "(La b) es literalmente tu frase del día 24 — ahí escribiste «si impara».)")

ej(5, "<strong>Discorso indiretto</strong> — pásalo a indirecto en pasado, moviendo TODO: "
      "a) Mi ha detto: «Vengo domani». b) Mi ha chiesto: «Chi ti ha aiutato?» c) Ha detto: «Non l'ho "
      "mai visto».", rows=3, ph="a) …")
solu(5, "a) <span class='it'>Mi ha detto che sarebbe venuto il giorno dopo.</span> b) <span class='it'>"
        "Mi ha chiesto chi mi <b>avesse</b> aiutato.</span> c) <span class='it'>Ha detto che non "
        "l'aveva mai visto.</span> Fíjate en la b): es tu frase del examen del día 22.")

ej(6, "<strong>Reggenze</strong> — completa: Speravo ___ riuscirci · Non sapevo ___ chi rivolgermi · "
      "Ho cercato ___ spiegarglielo · Ha promesso ___ chiamare.", rows=2, ph="…",
   ripasso_tuo=True)
solu(6, "Speravo <span class='it'>di</span> · Non sapevo <span class='it'>a</span> chi · Ho cercato "
        "<span class='it'>di</span> · Ha promesso <span class='it'>di</span>.")

ej(7, "<strong>Elisión (tu punto pegajoso)</strong> — escríbelas bien, con apóstrofo: a) glielo ho "
      "detto → ___ b) me lo avresti dato → ___ c) glielo avrei mandato → ___ d) te lo ho già "
      "spiegato → ___", rows=3, ph="a) …", ripasso_tuo=True)
solu(7, "a) <span class='it'>gliel'ho detto</span> b) <span class='it'>me l'avresti dato</span> "
        "c) <span class='it'>gliel'avrei mandato</span> d) <span class='it'>te l'ho già spiegato</span>. "
        "En los cuatro, LO se come su vocal delante de otra vocal.")

ej(8, "<strong>Sujeto explícito</strong> — el congiuntivo imperfetto es igual para io/tu/lui, así que "
      "sin pronombre no se entiende. Aclara el sujeto: a) Pensava che ___ (yo) fossi in ritardo. "
      "b) Credevo che ___ (tú) avessi capito.", rows=2, ph="a) …", ripasso_tuo=True)
solu(8, "a) <span class='it'>Pensava che <b>io</b> fossi in ritardo.</span> b) <span class='it'>Credevo "
        "che <b>tu</b> avessi capito.</span> Sin el pronombre, «fossi» vale para las dos personas.")

ej(9, "<strong>Falsi amici</strong> — corrige la palabra española infiltrada: a) «Il progetto è "
      "stato un <span class='it'>fracasso</span>». b) «<span class='it'>Mi sono sentito "
      "vergognato</span>». c) «<span class='it'>Ho una domanda in mente</span>» — ¿es correcta?",
   rows=3, ph="a) …")
solu(9, "a) <span class='it'>un <b>fiasco</b></span> — <span class='it'>fracasso</span> existe, pero "
        "es <em>estruendo</em>. b) <span class='it'>mi sono <b>vergognato</b></span> — el verbo ya lo "
        "dice todo. c) Sí, es correcta: <span class='it'>domanda</span> es <em>pregunta</em> (la "
        "demanda judicial es <span class='it'>causa</span>). Las dos primeras son tuyas, del día 24.")

ej(10, "<strong>Il tuo vocabolario</strong> — 2 frases con → <strong class='mis-palabras'>(abre tu "
       "Vocabulario ★)</strong>, una con <span class='it'>pensavo che…</span> y otra con "
       "<span class='it'>mi sa che…</span>.", rows=3, ph="…")
libre(10)

ej(11, "<strong>Caccia all'errore</strong> — hay CUATRO: a) «Penso che dagli errori si impara». "
       "b) «Mi ha detto che verrebbe più tardi». c) «Non ci avrebbe lasciato tutti noi senza cibo». "
       "d) «Mi sa che sia tardi».", rows=4, ph="a) …")
solu(11, "a) <span class='it'>si <b>impari</b></span> (penso che pide congiuntivo). b) <span class='it'>"
         "sarebbe venuto</span> (futuro nel passato, no condizionale simple). c) <span class='it'>non "
         "ci avrebbe <b>lasciati</b> senza cibo</span> — «ci» ya es «nosotros», sobra «tutti noi», y "
         "el participio concuerda. d) <span class='it'>Mi sa che <b>è</b> tardi</span> — "
         "<span class='it'>mi sa che</span> va con INDICATIVO. Las a) y c) son tuyas del día 24.")

ej(12, "<strong>Ascolto</strong> — escucha y escribe; luego di si el principal está en presente o en "
       "pasado: " + audio([("1", "Pensavo che me l'avessi già mandato."),
                           ("2", "Mi sa che non gliel'hanno detto."),
                           ("3", "Speravo che sarebbe andata meglio.")]), rows=3,
   ph="…", ripasso_tuo=True)
solu(12, "1) <span class='it'>Pensavo che me l'avessi già mandato</span> — pasado (trapassato). "
         "2) <span class='it'>Mi sa che non gliel'hanno detto</span> — presente, e indicativo. "
         "3) <span class='it'>Speravo che sarebbe andata meglio</span> — pasado (posterior).")

ej(13, "<strong>Congiuntivo SÍ o NO</strong> — decide y completa: a) So che ___ (essere) tardi. "
       "b) Credo che ___ (essere) tardi. c) È vero che ___ (avere) ragione. d) Non è che ___ (essere) "
       "difficile.", rows=3, ph="a) …")
solu(13, "a) <span class='it'>è</span> (so che → indicativo) b) <span class='it'>sia</span> (credo che "
         "→ congiuntivo) c) <span class='it'>ha</span> (è vero che → indicativo) d) <span class='it'>"
         "sia</span> (non è che → congiuntivo). Lo que das por hecho va en indicativo; lo que filtras "
         "por tu cabeza, en congiuntivo.")

ej(14, "<strong>En tu estudio</strong> — traduce estas tres, que vas a decir de verdad: a) Creía que "
       "ya te lo había mandado. b) Me dijo que lo pensaría. c) No sabía que fuera tan urgente.",
   rows=3, ph="a) …")
solu(14, "a) <span class='it'>Pensavo di <b>avertelo</b> già mandato</span> (mismo sujeto → "
         "<span class='it'>di</span> + infinitivo) o <span class='it'>Pensavo che te l'avessero già "
         "mandato</span> si lo mandó otro. b) <span class='it'>Mi ha detto che ci avrebbe pensato.</span> "
         "c) <span class='it'>Non sapevo che fosse così urgente.</span> Truco de la a): si el sujeto "
         "es el mismo, el italiano prefiere <span class='it'>di</span> + infinitivo antes que «che».")

ej(15, "<strong>Produzione libera</strong> — escribe 6-8 líneas sobre <em>algo que creíste que iba a "
       "pasar en el estudio y pasó distinto</em>. Obligatorio: 2 congiuntivo imperfetto o trapassato "
       "(<span class='it'>fosse, avessi, avesse detto</span>), 1 condizionale composto "
       "(<span class='it'>sarebbe / avrebbe</span>), 1 elisión con apóstrofo "
       "(<span class='it'>gliel'ho, me l'ha</span>) y un slang de hoy.",
   rows=7, ph="…")
libre(15)

autocontrollo("bajar un escalón cuando el principal está en pasado",
              "usar sarebbe venuto y no verrebbe para lo posterior",
              "distinguir penso che (congiuntivo) de mi sa che (indicativo)",
              "escribir gliel'ho y me l'avessi con apóstrofo")

riflessione(["Hoy no aprendiste una regla nueva: ataste tres que ya tenías sueltas. El congiuntivo "
             "del día 12, el condizionale composto del día 24 y el discurso indirecto del examen "
             "eran <strong>la misma cosa vista por tres ventanas</strong>. Esto es lo que separa un "
             "B2 de un C1: no más temas, sino los temas encajando entre sí.",
             "Y una cosa práctica: la mitad de los ejemplos de hoy son frases tuyas de los días 22 y "
             "24. No te las puse para señalarte, te las puse porque una regla se fija mucho mejor "
             "sobre un error propio que sobre un ejemplo de libro."],
            tiempo="55-65 min", domani="Passato remoto")

solu_guiado("① pasado (<span class='it'>credevo</span>) · ② anterior → trapassato "
            "(<span class='it'>avessero mandato</span>) · ③ a él = <span class='it'>glie</span>, eso = "
            "<span class='it'>lo</span> → <span class='it'>glielo</span> → ante vocal "
            "<span class='it'>gliel'</span> · ④ <span class='it'>Credevo che gliel'avessero già "
            "mandato.</span>")

guardar()
