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

def pull():
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
