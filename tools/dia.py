# -*- coding: utf-8 -*-
"""
Auditor mecánico de un DÍA del curso (§4 / §5) + chequeo de PUBLICACIÓN.

Hermano de tools/cancion.py. Existe por la misma razón: que la calidad NO dependa
de que el modelo se acuerde de las reglas. Lo que la máquina puede comprobar, lo
comprueba la máquina — así cualquier modelo (Sonnet incluido) produce días correctos.

USO
    cd tools && PYTHONIOENCODING=utf-8 python dia.py audit 21     # un día
    cd tools && PYTHONIOENCODING=utf-8 python dia.py audit        # todos los días existentes
    cd tools && PYTHONIOENCODING=utf-8 python dia.py deploy       # ¿qué falta por publicar?

QUÉ CAZA (cada uno nació de un fallo real)
  · 15 ejercicios e1..e15 + dettato, sin huecos ni repetidos
  · TODO ejercicio auto-verificable tiene solución       <- faltaba la del e12 (día 21)
  · un enunciado que promete "N cosas" y la solución lista otro número  <- e13 decía 3, eran 2
  · siembra "(ripasso tuo)" <= ~40% (aviso a partir de 35%)   <- el día 21 iba al 40%
  · bloques obligatorios de §4 presentes (objetivo, ripasso, alerta, frasi pronte,
    in contesto, slang 2-4, cultura completa, dettato, solucionario, autochequeo)
  · .spunto presente dentro de .cultura
  · palabras preguntadas en los ejercicios que NUNCA aparecen antes en el material  <- e2 y boh
  · versión ?v= coherente en toda la página
  · CSS de tabla definido pero sin ninguna <table> (síntoma de material en prosa)
"""
import io, os, re, sys, subprocess

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BLOQUES = [
    ('objetivo can-do',      r'Obiettivo di oggi'),
    ('ripasso veloce',       r'Ripasso veloce'),
    ('alerta contrastiva',   r'class="alerta"'),
    ('frasi pronte',         r'Frasi (pronte|di salvataggio)'),
    ('in contesto',          r'In contesto'),
    ('cultura ☕',            r'class="cultura"'),
    ('spunto',               r'class="spunto"'),
    ('puente 🇲🇽',            r'class="puente"'),
    ('dettato',              r'data-ej="dettato"'),
    ('solucionario',         r'class="solu"'),
    ('autochequeo',          r'Autocontrollo'),
    ('riflessione',          r'Riflessione del giorno'),
]


def _texto(html):
    """HTML -> texto plano, para buscar si una palabra se 'enseñó' antes.
    Las etiquetas EN LÍNEA (b/i/em/strong/span/sup) se quitan SIN dejar espacio: si no,
    «ca<b>pp</b>ello» se convertía en «ca pp ello» y la palabra dejaba de encontrarse."""
    t = re.sub(r'<(script|style)\b.*?</\1>', ' ', html, flags=re.S | re.I)
    t = re.sub(r'</?(b|i|em|strong|span|sup|sub|u)\b[^>]*>', '', t, flags=re.I)
    t = re.sub(r'<[^>]+>', ' ', t)
    return re.sub(r'\s+', ' ', t)


def auditar(nn, verbose=True):
    p = os.path.join(BASE, 'dia%s.html' % nn)
    if not os.path.exists(p):
        return ['no existe %s' % os.path.basename(p)]
    html = io.open(p, encoding='utf-8').read()
    fallos, avisos = [], []

    # ---- 1. ejercicios ----------------------------------------------------
    # Los días 8/15/22/30 son REPASO+EXAMEN: 10 eN + 10 xN (§5), no 15 eN.
    repaso = int(nn) in (8, 15, 22, 30)
    ejs = re.findall(r'data-ej="(\w+)"', html)
    nums = [e for e in ejs if re.fullmatch(r'e\d+', e)]
    xs = [e for e in ejs if re.fullmatch(r'x\d+', e)]
    if repaso:
        esperados = ['e%d' % i for i in range(1, 11)] + ['x%d' % i for i in range(1, 11)]
        presentes = nums + xs
    else:
        esperados = ['e%d' % i for i in range(1, 16)]
        presentes = nums
    faltan = [e for e in esperados if e not in presentes]
    dups = {e for e in presentes if presentes.count(e) > 1}
    if faltan:
        fallos.append('faltan ejercicios: %s' % ', '.join(faltan))
    if dups:
        fallos.append('data-ej duplicados: %s' % ', '.join(sorted(dups)))
    if 'dettato' not in ejs:
        fallos.append('falta el dettato')
    if repaso and not re.search(r'rubrica|rúbrica|CEFR', html, re.I):
        fallos.append('día de repaso sin RÚBRICA CEFR para la producción larga (§5)')

    # ---- 2. solucionario cubre lo auto-verificable ------------------------
    m = re.search(r'<details class="solu">(.*?)</details>', html, re.S)
    if not m:
        fallos.append('sin solucionario')
        sol_txt = ''
    else:
        sol_txt = m.group(1)
        con_sol = set(int(x) for x in re.findall(r'<strong>(\d+)\.', sol_txt))
        libres = set()
        for gr in re.findall(r'<strong>([\d,\sxXy]+)[:y]', sol_txt):
            if re.search(r'respuesta libre|te los corrijo|te las corrijo|corrijo yo', sol_txt):
                libres |= set(int(x) for x in re.findall(r'\d+', gr))
        # en día de repaso el EXAMEN (xN) no lleva soluciones a propósito: solo se auditan los eN
        tope = 11 if repaso else 16
        huerfanos = [i for i in range(1, tope) if i not in con_sol and i not in libres]
        if huerfanos:
            fallos.append('ejercicios sin solución NI declarados libres: %s'
                          % ', '.join(str(i) for i in huerfanos))

    # ---- 3. enunciado que promete N cosas vs solución ----------------------
    NUM = {'una': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5,
           '1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
    for li in re.findall(r'<li>(.*?)</li>', html, re.S):
        mm = re.search(r'tiene\s+(\w+)\s+(?:palabras|cosas|errori|errores)', _texto(li), re.I)
        if not mm:
            continue
        prometidas = NUM.get(mm.group(1).lower())
        ej = re.search(r'data-ej="(e\d+)"', li)
        if not (prometidas and ej):
            continue
        n_ej = int(ej.group(1)[1:])
        ms = re.search(r'<strong>%d\.</strong>(.*?)(?=<p><strong>|$)' % n_ej, sol_txt, re.S)
        if ms:
            flechas = ms.group(1).count('→')
            if flechas and flechas != prometidas:
                fallos.append('ejercicio %d: el enunciado promete %d pero la solución lista %d'
                              % (n_ej, prometidas, flechas))

    # ---- 4. porcentaje de siembra ----------------------------------------
    lis = re.findall(r'<li>(.*?)</li>', html, re.S)
    lis = [l for l in lis if 'data-ej="e' in l]
    siembra = sum(1 for l in lis if re.search(r'ripasso tuo', l, re.I))
    if lis:
        pct = 100 * siembra // len(lis)
        if pct > 40:
            fallos.append('siembra %d%% (%d/%d) — máximo ~40%% en día normal' % (pct, siembra, len(lis)))
        elif pct > 34:
            avisos.append('siembra %d%% (%d/%d) — el tema del día queda justo' % (pct, siembra, len(lis)))

    # ---- 5. bloques de §4 -------------------------------------------------
    # Un día de REPASO no enseña material nuevo, así que no le aplican los bloques de
    # presentación: "in contesto" (input i+1 con la estructura del día) ni "frasi pronte".
    # Convención establecida por el día 15, ya aprobado.
    EXENTOS_REPASO = {'in contesto', 'frasi pronte', 'ripasso veloce'}
    for nombre, pat in BLOQUES:
        if repaso and nombre in EXENTOS_REPASO:
            continue
        if not re.search(pat, html, re.I):
            fallos.append('falta el bloque: %s' % nombre)

    n_slang = len(re.findall(r'class="slang"', html))
    if not 2 <= n_slang <= 4:
        fallos.append('slang: %d entradas (§4 pide 2-4)' % n_slang)

    # ---- 6. ¿se pregunta algo que nunca se enseñó? -------------------------
    # OJO: los ejercicios de "caccia all'errore" / "corrige" citan formas MAL a propósito;
    # esas NO deben estar en el material. Se saltan, o el auditor grita en falso.
    cuerpo = html.split('<h2>Esercizi</h2>')[0] if '<h2>Esercizi</h2>' in html else html
    ense = _texto(cuerpo).lower()
    TRAMPA = re.compile(r"caccia all'errore|corrig[ei]|correggi|corrija|sbagliat", re.I)
    for li in lis:
        if TRAMPA.search(_texto(li)):
            continue
        for tok in re.findall(r'«([^»]{2,30})»|\b(fra\'|boh|mah|\'sti|dov\'è)\b', _texto(li)):
            w = (tok[0] or tok[1]).strip().lower()
            if len(w) < 2 or w in ('___',):
                continue
            if w not in ense:
                avisos.append('se pregunta «%s» pero no aparece en el material de estudio' % w)

    # ---- 7. versión ?v= coherente ----------------------------------------
    vs = set(re.findall(r'\?v=(\d{8}[a-z])', html))
    if len(vs) > 1:
        fallos.append('versiones ?v= mezcladas: %s' % ', '.join(sorted(vs)))
    elif not vs:
        avisos.append('sin ?v= en los assets (caché de GitHub Pages)')

    # ---- 8. CSS de tabla sin tablas --------------------------------------
    if re.search(r'^\s*table\s*\{', html, re.M) and '<table' not in html:
        avisos.append('define estilos de <table> pero no usa ninguna (¿material en prosa?)')

    if verbose:
        print('--- DÍA %s ---' % nn)
        print('ejercicios: %d · siembra: %d · slang: %d · tablas: %d'
              % (len(nums), siembra, n_slang, html.count('<table')))
        for f in fallos:
            print('   ❌', f)
        for a in sorted(set(avisos)):
            print('   ⚠️ ', a)
        if not fallos and not avisos:
            print('   ✅ OK')
        elif not fallos:
            print('   ✅ sin fallos (solo avisos)')
    return fallos


def deploy():
    """Lo que de verdad falló con el día 21: estaba en disco pero no publicado."""
    def git(*a):
        return subprocess.run(['git', '-C', BASE] + list(a),
                              capture_output=True, text=True, encoding='utf-8').stdout.strip()
    print('--- PUBLICACIÓN ---')
    print('rama:', git('status', '-sb').splitlines()[0] if git('status', '-sb') else '?')
    pend = [l for l in git('status', '--short').splitlines() if l.strip()]
    if not pend:
        print('   ✅ todo publicado (nada sin commitear)')
    else:
        print('   ⚠️  %d archivo(s) SIN PUBLICAR — un día no existe para el usuario hasta el push:' % len(pend))
        for l in pend[:12]:
            print('      ', l)
        if len(pend) > 12:
            print('       … y %d más' % (len(pend) - 12))
    unt = [l[3:] for l in pend if l.startswith('??')]
    riesgo = [f for f in unt if re.search(r'_corr_|_song_|_vocab_|datos/|adminsdk|serviceAccount', f)]
    if riesgo:
        print('   ❌ DATOS PERSONALES sin ignorar (NO hagas git add -A):')
        for f in riesgo:
            print('      ', f)
    return pend


if __name__ == '__main__':
    args = sys.argv[1:]
    if args and args[0] == 'deploy':
        deploy()
    else:
        objetivo = args[1:] if args and args[0] == 'audit' else args
        if not objetivo:
            objetivo = sorted(re.findall(r'dia(\d+)\.html', ' '.join(os.listdir(BASE))))
        malos = 0
        for nn in objetivo:
            if auditar(nn.zfill(2)):
                malos += 1
            print()
        sys.exit(1 if malos else 0)
