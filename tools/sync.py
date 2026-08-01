# -*- coding: utf-8 -*-
"""sync.py — puente entre los datos LOCALES (donde Claude corrige/analiza) y Firestore (la nube del usuario).

Uso:
  python tools/sync.py status                    # qué difiere local vs nube (NO mueve nada)
  python tools/sync.py pull                      # baja lo que cambió en la nube
  python tools/sync.py push                      # sube SOLO lo que cambió en local
  python tools/sync.py pull push                 # el ciclo completo (corregir/analizar)
  python tools/sync.py pull canciones            # un ámbito suelto
  python tools/sync.py pull cancion alta-marea   # un documento suelto
  python tools/sync.py push errores 23
  python tools/sync.py push --force              # sube aunque haya conflicto (mira antes qué cambió)

Ámbitos: perfil · respuestas · errores · canciones · examenes   (sin ámbito = todos)
Singular + id apunta a un solo documento: cancion <id> · error <NN> · respuesta <NN> · examen <sem>

QUIÉN MANDA SOBRE CADA DATO
  respuestas, examenes : los escribe el USUARIO en el navegador -> solo se BAJAN (nunca se suben)
  errores              : los escribe CLAUDE en local             -> se SUBEN (se bajan solo para restaurar)
  canciones            : la letra la pone el usuario, el análisis Claude -> ambas direcciones
  perfil               : por capas (analítica = local, marcas manuales "ya lo domino" = nube)

SEGURIDAD: datos/.sync-estado.json recuerda, por documento, el hash de lo último sincronizado y la marca
de tiempo que tenía en la nube. Gracias a eso NO se re-sube lo que no cambió y, si algo cambió en la nube
desde el último sync (p. ej. lo tocaste desde el móvil), se avisa y NO se pisa.
Se compara por CONTENIDO, no por fecha: la nube siempre queda más nueva tras un push, así que las fechas
darían conflictos falsos.

Usa la llave de servicio (*firebase-adminsdk*.json o serviceAccount.json en la carpeta del curso; está en
.gitignore, nunca se sube). El usuario se detecta solo (auth.list_users) — no se guarda su correo aquí.
"""
import firebase_admin
from firebase_admin import credentials, auth, firestore
import glob, json, os, sys, io, hashlib, datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # carpeta del curso
DATOS = os.path.join(BASE, 'datos')
CANC_DIR = os.path.join(DATOS, 'canciones')
ERR_DIR = os.path.join(DATOS, 'errores')
ESTADO_P = os.path.join(DATOS, '.sync-estado.json')


def _find_key():
    for pat in ('*firebase-adminsdk*.json', 'serviceAccount.json'):
        hits = glob.glob(os.path.join(BASE, pat))
        if hits:
            return hits[0]
    sys.exit('No encuentro la llave de servicio (*firebase-adminsdk*.json) en ' + BASE)


firebase_admin.initialize_app(credentials.Certificate(_find_key()))
_users = list(auth.list_users().iterate_all())
if not _users:
    sys.exit('No hay usuarios en Authentication.')
UID = _users[0].uid                     # app de un solo usuario
db = firestore.client()
U = db.collection('users').document(UID)


# ------------------------------------------------------------------ utilidades
def _leer(p):
    with io.open(p, encoding='utf-8') as f:
        return json.load(f)


def _escribir(p, obj):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    tmp = p + '.tmp'
    with io.open(tmp, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
    os.replace(tmp, p)                  # escritura atómica: nunca deja un JSON a medias


def _hash(obj):
    """Huella del CONTENIDO (no de la fecha): re-guardar algo idéntico no cuenta como cambio."""
    return hashlib.sha1(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode('utf-8')).hexdigest()


def _ts(x):
    return str(x) if x else ''


def _corto(ts):
    return (ts or '')[:19].replace('T', ' ') or '—'


ESTADO = _leer(ESTADO_P) if os.path.exists(ESTADO_P) else {}


def _guardar_estado():
    _escribir(ESTADO_P, ESTADO)


def _marcar(clave, obj, update_time):
    ESTADO[clave] = {'hash': _hash(obj), 'nube': _ts(update_time)}


# ------------------------------------------------------------------ perfil (dos autorías)
MANUAL = ('dominado_manual', 'prev_estado', 'prev_prioridad', 'prev_tendencia')


def _merge_perfil(local, cloud):
    """Funde las DOS autorías del perfil, para que ninguna pise a la otra:
       · capa ANALÍTICA (fallos, aciertos, etiqueta, proxima_siembra…) la escribe Claude en LOCAL;
       · capa MANUAL ("ya lo domino" / "vuelve a seguirlo" del diagnóstico) la escribe el usuario
         desde la WEB → en esas claves manda la NUBE.
    """
    lr = (local or {}).get('rasgos') or {}
    cr = (cloud or {}).get('rasgos') or {}
    tocados = 0
    for k, c in cr.items():
        l = lr.get(k)
        if not isinstance(l, dict) or not isinstance(c, dict):
            continue
        for key in MANUAL:                      # se recalcula desde la nube (si allá se reactivó, aquí desaparece)
            l.pop(key, None)
        if c.get('dominado_manual'):
            for key in MANUAL + ('estado', 'prioridad', 'tendencia'):
                if key in c:
                    l[key] = c[key]
            tocados += 1
    return local, tocados


# ------------------------------------------------------------------ mapeo dato <-> archivo
# Cada ámbito sabe: dónde vive en local, cómo se codifica hacia/desde Firestore y quién manda.
def _canc_local(cid):
    return os.path.join(CANC_DIR, cid + '.json')


def _canc_a_nube(data, cid):
    # Firestore no admite arrays anidados -> el objeto entero va serializado en un campo string
    return {
        'json': json.dumps(data, ensure_ascii=False),
        'titulo': data.get('titulo', cid), 'artista': data.get('artista', ''),
        'fecha': data.get('fecha', ''), 'analizada': bool(data.get('analisis')),
    }


def _canc_de_nube(v):
    return json.loads(v['json']) if (v or {}).get('json') else (v or {})


AMBITOS = {
    # nombre        singular      dueño          local(id)                                nube->local        local->nube
    'canciones':  dict(sing='cancion',   dueno='mixto',  ruta=_canc_local,
                       de_nube=_canc_de_nube, a_nube=_canc_a_nube),
    'errores':    dict(sing='error',     dueno='local',  ruta=lambda i: os.path.join(ERR_DIR, i + '.json'),
                       de_nube=lambda v: v or {}, a_nube=lambda d, i: d),
    'respuestas': dict(sing='respuesta', dueno='nube',   ruta=None,   # viven juntas en respuestas.json
                       de_nube=lambda v: v or {}, a_nube=None),
    'examenes':   dict(sing='examen',    dueno='nube',   ruta=None,   # viven juntos en examenes.json
                       de_nube=lambda v: v or {}, a_nube=None),
}


def _docs_nube(col):
    """{id: (datos_decodificados, update_time)} de una colección."""
    cfg = AMBITOS[col]
    out = {}
    for d in U.collection(col).stream():
        out[d.id] = (cfg['de_nube'](d.to_dict()), d.update_time)
    return out


def _ids_local(col):
    """Ids que existen en local. OJO: respuestas y examenes NO tienen un archivo por documento,
       viven juntas dentro de datos/<col>.json — si no se distingue, status las daría por ausentes."""
    cfg = AMBITOS[col]
    if not cfg['ruta']:
        p = os.path.join(DATOS, col + '.json')
        return sorted((_leer(p) or {}).keys()) if os.path.exists(p) else []
    carpeta = os.path.dirname(cfg['ruta']('x'))
    if not os.path.isdir(carpeta):
        return []
    return sorted(os.path.splitext(os.path.basename(f))[0] for f in glob.glob(os.path.join(carpeta, '*.json')))


def _local_doc(col, did):
    """El contenido local de UN documento, venga de su propio archivo o del JSON combinado."""
    cfg = AMBITOS[col]
    if cfg['ruta']:
        p = cfg['ruta'](did)
        return _leer(p) if os.path.exists(p) else None
    p = os.path.join(DATOS, col + '.json')
    return (_leer(p) or {}).get(did) if os.path.exists(p) else None


# ------------------------------------------------------------------ diagnóstico por documento
def _sin_baseline(col, local, nube):
    """Sin registro previo (primer sync, o equipo recién instalado) es IMPOSIBLE saber quién cambió.
       Marcar 'conflicto' bloquearía el trabajo normal —corregir un día y subirlo—, así que se
       resuelve por el DUEÑO del dato; solo se declara conflicto cuando de verdad es ambiguo."""
    dueno = 'local' if col == 'perfil' else AMBITOS[col]['dueno']
    if dueno == 'local':                 # errores y perfil: los escribe Claude en local
        return 'cambio-local'
    if dueno == 'nube':                  # respuestas y examenes: los escribe el usuario
        return 'cambio-nube'
    if col == 'canciones':               # gana el lado que ya tiene el análisis hecho
        al, an = bool((local or {}).get('analisis')), bool((nube or {}).get('analisis'))
        if al and not an:
            return 'cambio-local'
        if an and not al:
            return 'cambio-nube'
    return 'conflicto'


def _situacion(col, clave, local_obj, nube_obj, nube_t):
    """Compara contra lo último sincronizado. Devuelve: nuevo-local | nuevo-nube | igual |
       cambio-local | cambio-nube | conflicto | solo-local"""
    st = ESTADO.get(clave)
    hay_l, hay_n = local_obj is not None, nube_obj is not None
    if not hay_l and not hay_n:
        return 'igual'
    if not st:
        if hay_l and not hay_n:
            return 'nuevo-local'
        if hay_n and not hay_l:
            return 'nuevo-nube'
        return 'igual' if _hash(local_obj) == _hash(nube_obj) else _sin_baseline(col, local_obj, nube_obj)
    cambio_l = hay_l and _hash(local_obj) != st.get('hash')
    cambio_n = hay_n and _ts(nube_t) != st.get('nube')
    if not hay_n:
        return 'nuevo-local' if cambio_l else 'solo-local'
    if not hay_l:
        return 'nuevo-nube'
    if cambio_l and cambio_n:
        return 'conflicto'
    if cambio_l:
        return 'cambio-local'
    if cambio_n:
        return 'cambio-nube'
    return 'igual'


# ------------------------------------------------------------------ PULL
def pull(ambitos, solo_id=None, force=False):
    if 'perfil' in ambitos:
        _pull_perfil()
    for col in ('respuestas', 'examenes'):
        if col in ambitos:
            _pull_bloque(col, solo_id)
    for col in ('errores', 'canciones'):
        if col in ambitos:
            _pull_docs(col, solo_id, force)


def _pull_perfil():
    """La nube solo aporta las marcas manuales; el resto del perfil sigue siendo el local."""
    pp = os.path.join(DATOS, 'perfil.json')
    if not os.path.exists(pp):
        print('perfil     · no hay perfil local, nada que fundir')
        return
    snap = U.collection('perfil').document('actual').get()
    cloud = snap.to_dict() if snap.exists else {}
    local, n = _merge_perfil(_leer(pp), cloud)
    _escribir(pp, local)
    _marcar('perfil/actual', local, snap.update_time if snap.exists else None)
    print('perfil     · %d rasgo(s) marcados a mano desde la web' % n)


def _pull_bloque(col, solo_id):
    """respuestas y examenes: son del usuario -> la nube MANDA. Se juntan en un solo archivo."""
    destino = os.path.join(DATOS, col + '.json')
    actual = _leer(destino) if os.path.exists(destino) else {}
    n = 0
    for did, (datos, t) in sorted(_docs_nube(col).items()):
        if solo_id and did != solo_id:
            continue
        actual[did] = datos
        _marcar('%s/%s' % (col, did), datos, t)
        n += 1
    if n or not os.path.exists(destino):
        _escribir(destino, actual)
    print('%-10s · %d de la nube -> datos/%s.json' % (col, n, col))


def _pull_docs(col, solo_id, force):
    """errores y canciones: un archivo por documento; se respeta el trabajo local sin subir."""
    cfg = AMBITOS[col]
    nube = _docs_nube(col)
    bajados = saltados = conflictos = 0
    for did, (datos, t) in sorted(nube.items()):
        if solo_id and did != solo_id:
            continue
        p = cfg['ruta'](did)
        local = _leer(p) if os.path.exists(p) else None
        sit = _situacion(col, '%s/%s' % (col, did), local, datos, t)
        if sit in ('igual', 'solo-local', 'cambio-local'):
            saltados += 1
            continue
        if sit == 'conflicto' and not force:
            print('   ⚠ %s/%s cambió en LOS DOS lados — no lo bajo (usa --force para que gane la nube)' % (col, did))
            conflictos += 1
            continue
        _escribir(p, datos)
        _marcar('%s/%s' % (col, did), datos, t)
        bajados += 1
    _guardar_estado()
    print('%-10s · %d bajadas, %d sin cambios%s' %
          (col, bajados, saltados, (', %d en conflicto' % conflictos) if conflictos else ''))


# ------------------------------------------------------------------ PUSH
def push(ambitos, solo_id=None, force=False):
    if 'perfil' in ambitos:
        _push_perfil(force)
    for col in ('errores', 'canciones'):
        if col in ambitos:
            _push_docs(col, solo_id, force)
    for col in ('respuestas', 'examenes'):
        if col in ambitos and solo_id is None:
            print('%-10s · no se suben nunca (los escribe el usuario en el navegador)' % col)


def _subir(ref, clave, obj_local, payload, etiqueta):
    res = ref.set(payload)                     # el WriteResult ya trae update_time: no hace falta releer
    _marcar(clave, obj_local, getattr(res, 'update_time', None))
    print('   ⬆ %s' % etiqueta)


def _push_perfil(force):
    pp = os.path.join(DATOS, 'perfil.json')
    if not os.path.exists(pp):
        return
    local = _leer(pp)
    ref = U.collection('perfil').document('actual')
    snap = ref.get()
    sit = _situacion('perfil', 'perfil/actual', local, snap.to_dict() if snap.exists else None,
                     snap.update_time if snap.exists else None)
    if sit in ('igual', 'cambio-nube'):
        print('perfil     · sin cambios locales')
        return
    if sit == 'conflicto' and not force:
        print('perfil     · ⚠ CONFLICTO: cambió en la nube desde el último sync. Haz `pull perfil` '
              'primero (funde tus marcas manuales) o usa --force.')
        return
    _subir(ref, 'perfil/actual', local, local, 'perfil')
    _guardar_estado()
    print('perfil     · subido')


def _push_docs(col, solo_id, force):
    cfg = AMBITOS[col]
    nube = _docs_nube(col)
    subidos = saltados = 0
    conflictos = []
    for did in _ids_local(col):
        if solo_id and did != solo_id:
            continue
        local = _leer(cfg['ruta'](did))
        datos_n, t_n = nube.get(did, (None, None))
        sit = _situacion(col, '%s/%s' % (col, did), local, datos_n, t_n)
        if sit in ('igual', 'cambio-nube', 'solo-local') and did in nube:
            saltados += 1
            continue
        if sit == 'conflicto' and not force:
            conflictos.append(did)
            continue
        _subir(U.collection(col).document(did), '%s/%s' % (col, did), local,
               cfg['a_nube'](local, did), '%s/%s' % (col, did))
        subidos += 1
    _guardar_estado()
    print('%-10s · %d subidas, %d sin cambios%s' %
          (col, subidos, saltados, (', %d en CONFLICTO' % len(conflictos)) if conflictos else ''))
    for did in conflictos:
        print('   ⚠ %s/%s cambió en la nube desde el último sync — NO lo subo. '
              'Mira qué cambió y, si quieres pisarlo, repite con --force' % (col, did))


# ------------------------------------------------------------------ STATUS
ICONO = {'igual': '✔ igual', 'nuevo-local': '⬆ subir (nuevo)', 'cambio-local': '⬆ subir',
         'nuevo-nube': '⬇ bajar (nuevo)', 'cambio-nube': '⬇ bajar', 'conflicto': '⚠ CONFLICTO',
         'solo-local': '· solo local', 'solo-nube': '⬇ bajar'}


def status(ambitos, solo_id=None):
    print('%-11s %-24s %10s  %-19s %s' % ('ÁMBITO', 'DOC', 'LOCAL', 'CAMBIO EN LA NUBE', 'ESTADO'))
    print('-' * 88)
    resumen = {}

    def fila(col, did, p_local, local_obj, sit, t):
        if p_local and os.path.exists(p_local):
            tam = '%.1f KB' % (os.path.getsize(p_local) / 1024.0)
        else:
            tam = 'en bloque' if local_obj is not None else '—'   # respuestas/examenes: sin archivo propio
        print('%-11s %-24s %10s  %-19s %s' % (col, did[:24], tam, _corto(_ts(t)), ICONO.get(sit, sit)))
        resumen[sit] = resumen.get(sit, 0) + 1

    if 'perfil' in ambitos:
        pp = os.path.join(DATOS, 'perfil.json')
        snap = U.collection('perfil').document('actual').get()
        local = _leer(pp) if os.path.exists(pp) else None
        t = snap.update_time if snap.exists else None
        fila('perfil', 'actual', pp, local,
             _situacion('perfil', 'perfil/actual', local, snap.to_dict() if snap.exists else None, t), t)

    for col in ('errores', 'canciones', 'respuestas', 'examenes'):
        if col not in ambitos:
            continue
        cfg = AMBITOS[col]
        nube = _docs_nube(col)
        for did in sorted(set(list(nube.keys()) + _ids_local(col))):
            if solo_id and did != solo_id:
                continue
            p = cfg['ruta'](did) if cfg['ruta'] else None
            local = _local_doc(col, did)
            datos_n, t_n = nube.get(did, (None, None))
            fila(col, did, p, local, _situacion(col, '%s/%s' % (col, did), local, datos_n, t_n), t_n)

    print('-' * 88)
    print('resumen: ' + ' · '.join('%s %d' % (ICONO.get(k, k), v) for k, v in sorted(resumen.items())))

    # canciones pendientes de analizar (mismo criterio que tools/cancion.py)
    pend = []
    for cid in _ids_local('canciones'):
        d = _leer(_canc_local(cid))
        versos = len([x for x in (d.get('letra') or '').split('\n') if x.strip()])
        hechas = len(((d.get('analisis') or {}).get('lineas')) or {})
        if versos and hechas < versos:
            pend.append((cid, 100 * hechas // versos))
    print('\ncanciones pendientes de analizar: ' +
          (', '.join('%s (%d%%)' % x for x in pend) if pend else 'ninguna ✔'))
    if os.path.exists(ESTADO_P):
        print('último sync: %s · %d documentos recordados' %
              (datetime.datetime.fromtimestamp(os.path.getmtime(ESTADO_P)).strftime('%Y-%m-%d %H:%M'),
               len(ESTADO)))
    else:
        print('último sync: (sin registro todavía — el primer push tratará todo como nuevo)')


# ------------------------------------------------------------------ CLI
TODOS = ['perfil', 'respuestas', 'errores', 'canciones', 'examenes']
SINGULARES = {c['sing']: n for n, c in AMBITOS.items()}
SINGULARES['perfil'] = 'perfil'


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    force = '--force' in sys.argv[1:]
    acciones = [a for a in args if a in ('pull', 'push', 'status')]
    if not acciones:
        print(__doc__)
        return
    resto = [a for a in args if a not in ('pull', 'push', 'status')]

    ambitos, solo_id = TODOS, None
    if resto:
        clave = resto[0]
        if clave in TODOS:
            ambitos = [clave]
        elif clave in SINGULARES:
            ambitos = [SINGULARES[clave]]
            solo_id = resto[1] if len(resto) > 1 else None
            if solo_id is None:
                sys.exit('Falta el id: p. ej. `sync.py pull cancion alta-marea`')
        else:
            sys.exit('No conozco «%s». Ámbitos: %s (o en singular + id)' % (clave, ', '.join(TODOS)))

    print('uid: %s%s' % (UID, '   [--force: se pisarán los conflictos]' if force else ''))
    for a in acciones:
        print('\n=== %s ===' % a.upper())
        if a == 'status':
            status(ambitos, solo_id)          # solo lectura: mirar nunca cambia nada
        elif a == 'pull':
            pull(ambitos, solo_id, force)
            _guardar_estado()
        else:
            push(ambitos, solo_id, force)
            _guardar_estado()
    print('\nLISTO')


main()
