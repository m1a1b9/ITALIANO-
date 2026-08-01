# -*- coding: utf-8 -*-
"""sync.py — puente entre los datos LOCALES (para que Claude corrija/analice) y Firestore (la nube del usuario).

Uso:
  python tools/sync.py pull        # baja respuestas + canciones de la nube a datos/  (antes de corregir/analizar)
  python tools/sync.py push        # sube correcciones (datos/errores/*) + canciones (datos/canciones/*) a la nube
  python tools/sync.py pull push   # ambos

Usa la llave de servicio (archivo *firebase-adminsdk*.json o serviceAccount.json en la carpeta del curso;
está en .gitignore, nunca se sube). El usuario se detecta solo (auth.list_users) — no se guarda su correo aquí.
"""
import firebase_admin
from firebase_admin import credentials, auth, firestore
import glob, json, os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # carpeta del curso
DATOS = os.path.join(BASE, 'datos')
CANC_DIR = os.path.join(DATOS, 'canciones')
ERR_DIR = os.path.join(DATOS, 'errores')

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


def pull():
    # perfil: la nube solo aporta las marcas manuales; el resto sigue siendo el local
    pp = os.path.join(DATOS, 'perfil.json')
    if os.path.exists(pp):
        local = json.load(open(pp, encoding='utf-8'))
        snap = U.collection('perfil').document('actual').get()
        cloud = snap.to_dict() if snap.exists else {}
        local, n_manual = _merge_perfil(local, cloud)
        json.dump(local, open(pp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        print('pull perfil: %d rasgo(s) marcados a mano desde la web' % n_manual)
    # examenes: los produce el usuario en el navegador -> la nube MANDA (nunca se suben desde aquí)
    ex = {}
    for d in U.collection('examenes').stream():
        ex[d.id] = d.to_dict()
    if ex:
        json.dump(ex, open(os.path.join(DATOS, 'examenes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('pull examenes: %d' % len(ex))
    # respuestas: Firestore -> datos/respuestas.json  (Firestore gana por día; conserva días solo-locales)
    p = os.path.join(DATOS, 'respuestas.json')
    local = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}
    n = 0
    for d in U.collection('respuestas').stream():
        local[d.id] = d.to_dict(); n += 1
    os.makedirs(DATOS, exist_ok=True)
    json.dump(local, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('pull respuestas: %d dias de la nube -> %s' % (n, os.path.basename(p)))
    # canciones: Firestore -> datos/canciones/<id>.json  (decodifica el campo json)
    os.makedirs(CANC_DIR, exist_ok=True); m = 0
    for d in U.collection('canciones').stream():
        v = d.to_dict() or {}
        data = json.loads(v['json']) if v.get('json') else v
        json.dump(data, open(os.path.join(CANC_DIR, d.id + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        m += 1
    print('pull canciones: %d -> datos/canciones/' % m)

def push():
    # perfil: local -> Firestore (para que la web filtre drills, pinte el diagnóstico y los focos del día).
    # Ojo: corre SIEMPRE después de pull(), que es quien conserva las marcas manuales hechas en la web.
    pp = os.path.join(DATOS, 'perfil.json')
    if os.path.exists(pp):
        U.collection('perfil').document('actual').set(json.load(open(pp, encoding='utf-8')))
        print('push perfil: 1')
    # examenes: NO se suben (los escribe el usuario en el navegador; subir el local los borraría)
    # correcciones: datos/errores/NN.json -> Firestore (directo)
    n = 0
    for f in sorted(glob.glob(os.path.join(ERR_DIR, '*.json'))):
        nn = os.path.splitext(os.path.basename(f))[0]
        U.collection('errores').document(nn).set(json.load(open(f, encoding='utf-8'))); n += 1
    print('push correcciones: %d' % n)
    # canciones: datos/canciones/*.json -> Firestore (json string + metadatos; Firestore no admite arrays anidados)
    m = 0
    for f in sorted(glob.glob(os.path.join(CANC_DIR, '*.json'))):
        cid = os.path.splitext(os.path.basename(f))[0]
        data = json.load(open(f, encoding='utf-8'))
        U.collection('canciones').document(cid).set({
            'json': json.dumps(data, ensure_ascii=False),
            'titulo': data.get('titulo', cid), 'artista': data.get('artista', ''),
            'fecha': data.get('fecha', ''), 'analizada': bool(data.get('analisis')),
        }); m += 1
    print('push canciones: %d' % m)

cmds = [a for a in sys.argv[1:] if a in ('pull', 'push')]
if not cmds:
    print(__doc__); sys.exit()
print('uid:', UID)
for c in cmds:
    (pull if c == 'pull' else push)()
print('LISTO')
