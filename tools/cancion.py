# -*- coding: utf-8 -*-
"""
Motor reutilizable para ANALIZAR y AUDITAR canciones (§7-ter).

Existe para una sola razón: AHORRAR TOKENS.
Todo el andamiaje (helpers, escritura atómica, validaciones, auditoría) vive AQUÍ
de forma permanente, para no volver a escribirlo en cada canción. Al analizar una
canción nueva solo se escribe el CONTENIDO, nunca la maquinaria.

USO (crear tools/_song_<id>.py y ejecutarlo):

    # -*- coding: utf-8 -*-
    from cancion import *
    abrir('non-metterci-becco')          # carga el JSON e imprime la letra numerada

    linea(0, "traducción curada", "literal opcional", [
        nota('chunk', 'fragmento exacto', 'explicación'),
    ])
    linea(1, "…")
    igual(24, 0)                          # estribillo repetido: COPIA la línea 0
    rango(58, 65, desde=24)               # bloque repetido entero: 58..65 <- 24..31

    resumen("…")
    guardar()                             # valida, audita y escribe (falla si algo no cuadra)

REGLAS QUE ESTE MOTOR IMPONE SOLO (no hace falta recordarlas):
  · cobertura 100%: guardar() se niega a escribir si falta una sola línea
  · 'es' no vacía ni placeholder
  · 'tipo' de nota dentro de los 7 válidos
  · 'frag' debe existir LITERALMENTE en su línea italiana (anclaje, como §7.1)
  · escritura atómica (temp + os.replace) y UTF-8 con acentos verbatim

vocab() SIGUE DISPONIBLE pero ya NO es parte del flujo estándar (2026-08-03): generar la lista
"⭐ Vocabulario y formas clave" costaba tokens sin rendir — el usuario entiende la mayoría de esas
palabras y agrega manualmente a Mi Vocabulario lo poco que no entienda. NO llamar vocab() por
rutina; el vocabulario de cobertura general ahora lo resuelve solo el glosado automático del
curso (traducción en línea gratuita, sin tokens). Sigue disponible por si algún caso puntual lo
justifica de verdad.
"""
import json, os, io, sys, unicodedata

# La consola de Windows usa cp1252 y revienta al imprimir ✅/·/acentos (UnicodeEncodeError),
# abortando el guardado aunque la auditoría haya salido bien. Forzamos UTF-8 en la salida.
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CANC = os.path.join(BASE, 'datos', 'canciones')

TIPOS_OK = {'forma', 'slang', 'abrev', 'chunk', 'sentido', 'cultural', 'gramm'}

_st = {'id': None, 'doc': None, 'letra': [], 'lineas': {}, 'vocab': [], 'resumen': None}


# --------------------------------------------------------------- carga
def abrir(cid, mostrar=True):
    """Carga la canción y devuelve la lista de líneas no vacías (índice 0-based)."""
    p = os.path.join(CANC, cid + '.json')
    with io.open(p, encoding='utf-8') as f:
        d = json.load(f)
    _st['id'], _st['doc'] = cid, d
    _st['letra'] = [x.strip() for x in d['letra'].split('\n') if x.strip()]
    if mostrar:
        for i, l in enumerate(_st['letra']):
            print(i, '|', l)
        print('TOTAL', len(_st['letra']))
    return _st['letra']


def pendientes():
    """Lista id/título/¿analizada? SIN imprimir las letras (§7-ter: no cargar letras en contexto)."""
    out = []
    for fn in sorted(os.listdir(CANC)):
        if not fn.endswith('.json'):
            continue
        with io.open(os.path.join(CANC, fn), encoding='utf-8') as f:
            d = json.load(f)
        n = len([x for x in d['letra'].split('\n') if x.strip()])
        a = d.get('analisis')
        cob = (100 * len(a.get('lineas', {})) // n) if a and n else 0
        out.append((fn[:-5], d.get('titulo', '?'), n, cob))
        print('%-32s %-28s %3d líneas  %3d%%' % (fn[:-5], d.get('titulo', '?')[:27], n, cob))
    return out


# --------------------------------------------------------------- autoría
def nota(tipo, frag, texto, conjug=None):
    d = {"tipo": tipo, "frag": frag, "nota": texto}
    if conjug:
        d["conjug"] = conjug
    return d


def linea(i, es, lit=None, notas=None):
    d = {"es": es}
    if lit:
        d["lit"] = lit
    if notas:
        d["notas"] = notas
    _st['lineas'][str(i)] = d
    return d


def igual(i, desde):
    """Estribillo repetido: copia la línea `desde`. Ahorra reescribir versos idénticos."""
    src = _st['lineas'].get(str(desde))
    if src is None:
        raise KeyError('igual(%d, %d): la línea %d aún no está definida' % (i, desde, desde))
    _st['lineas'][str(i)] = json.loads(json.dumps(src))
    return _st['lineas'][str(i)]


def rango(ini, fin, desde):
    """Bloque repetido: rango(58, 65, desde=24) copia 24..31 en 58..65."""
    for k, i in enumerate(range(ini, fin + 1)):
        igual(i, desde + k)


def vocab(it, es, nota_=None, conjug=None):
    d = {"it": it, "es": es}
    if nota_:
        d["nota"] = nota_
    if conjug:
        d["conjug"] = conjug
    _st['vocab'].append(d)
    return d


def resumen(txt):
    _st['resumen'] = txt


# --------------------------------------------------------------- auditoría
def _norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return s.replace('’', "'").replace('‘', "'")


def auditar(cid=None, verbose=True):
    """Audita una canción en disco (o la que se está escribiendo). Devuelve lista de fallos."""
    if cid:
        with io.open(os.path.join(CANC, cid + '.json'), encoding='utf-8') as f:
            d = json.load(f)
        letra = [x.strip() for x in d['letra'].split('\n') if x.strip()]
        a = d.get('analisis') or {}
        L, V = a.get('lineas', {}), a.get('vocab', [])
    else:
        letra, L, V = _st['letra'], _st['lineas'], _st['vocab']

    fallos = []
    n = len(letra)

    faltan = [i for i in range(n) if str(i) not in L]
    if faltan:
        fallos.append('COBERTURA: faltan %d/%d líneas -> %s' % (len(faltan), n, faltan[:20]))
    sobran = [k for k in L if not k.isdigit() or int(k) >= n]
    if sobran:
        fallos.append('ÍNDICES fuera de rango: %s' % sobran)

    n_lit = 0
    for k, v in L.items():
        if not k.isdigit() or int(k) >= n:
            continue
        it = letra[int(k)]
        es = (v.get('es') or '').strip()
        if not es or es in ('…', '...', '-', '?'):
            fallos.append("línea %s: 'es' vacía o placeholder" % k)
        if v.get('lit'):
            n_lit += 1
        for nt in v.get('notas', []):
            t = nt.get('tipo')
            if t not in TIPOS_OK:
                fallos.append("línea %s: tipo inválido '%s' (válidos: %s)" % (k, t, ', '.join(sorted(TIPOS_OK))))
            fr = nt.get('frag') or ''
            if fr and _norm(fr) not in _norm(it):
                fallos.append('línea %s: frag NO ANCLADO -> «%s» no está en «%s»' % (k, fr, it))

    # vocab() ya NO es obligatorio (2026-08-03): la lista "⭐ Vocabulario y formas clave" se quitó
    # de la app. Si de todos modos se usó vocab() para algún caso puntual, se sigue validando que
    # no tenga duplicados; una lista vacía ya no es un fallo.
    vistos, dup = set(), []
    for e in V:
        key = _norm(e.get('it', ''))
        if key in vistos:
            dup.append(e.get('it'))
        vistos.add(key)
    if dup:
        fallos.append('vocab duplicado: %s' % dup)

    if verbose:
        print('--- AUDITORÍA %s ---' % (cid or _st['id'] or ''))
        print('cobertura: %d/%d (%d%%) · lit curadas: %d · vocab: %d'
              % (len(L), n, (100 * len(L) // n) if n else 0, n_lit, len(V)))
        if fallos:
            print('❌ %d FALLO(S):' % len(fallos))
            for f in fallos:
                print('   -', f)
        else:
            print('✅ OK')
    return fallos


# --------------------------------------------------------------- guardado
def guardar(force=False):
    """Valida + audita y, solo si todo está OK, escribe atómicamente."""
    if not _st['doc']:
        raise RuntimeError('llama antes a abrir("<id>")')
    if not _st['resumen']:
        raise RuntimeError('falta resumen("…")')
    fallos = auditar()
    if fallos and not force:
        print('\n⛔ NO SE ESCRIBIÓ NADA. Corrige los fallos y vuelve a ejecutar.')
        sys.exit(1)

    a = {"resumen": _st['resumen'], "lineas": _st['lineas'], "vocab": _st['vocab']}
    viejo = _st['doc'].get('analisis') or {}
    if viejo.get('quiz'):                      # §7-ter: no se generan quiz nuevos,
        a['quiz'] = viejo['quiz']              # pero NUNCA se borra uno ya existente
    _st['doc']['analisis'] = a

    p = os.path.join(CANC, _st['id'] + '.json')
    tmp = p + '.tmp'
    with io.open(tmp, 'w', encoding='utf-8') as f:
        json.dump(_st['doc'], f, ensure_ascii=False, indent=2)
    os.replace(tmp, p)
    print('\n✅ escrito %s (%d líneas, %d vocab)' % (p, len(_st['lineas']), len(_st['vocab'])))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'audit':
        objetivo = sys.argv[2:] or [f[:-5] for f in sorted(os.listdir(CANC)) if f.endswith('.json')]
        malas = 0
        for c in objetivo:
            if auditar(c):
                malas += 1
            print()
        sys.exit(1 if malas else 0)
    pendientes()
