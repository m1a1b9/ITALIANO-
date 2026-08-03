# -*- coding: utf-8 -*-
"""vocab.py — REVISIÓN MANUAL de Mi Vocabulario, con registro de por dónde vas.

Existe por la misma razón que cancion.py: que revisar el vocabulario a mano NO sea empezar de cero
cada vez. Cada palabra guarda quién la revisó y qué se le tocó, así que siempre se sabe qué falta.

USO (el ciclo completo):
    python tools/vocab.py estado          # ¿qué hay revisado y qué falta?  (baja primero)
    python tools/vocab.py bajar           # nube -> datos/vocabulario.json
    …editar con un script tools/_vocab_<algo>.py que use fijar()…
    python tools/vocab.py subir           # datos/vocabulario.json -> nube (fusiona, no pisa)

DESDE UN SCRIPT DE CONTENIDO (igual que _song_<id>.py):
    from vocab import *
    abrir()                                     # carga datos/vocabulario.json
    fijar('premuto', lema='premere', pos='verbo', lemaEs='apretar / pulsar',
          nota='era adjetivo; en su frase es participio de premere')
    fijar('azzeccato', es='acertado', nota='el significado guardado no correspondía')
    guardar()                                   # escribe + deja el registro

EL REGISTRO vive DENTRO de cada palabra (no en un archivo aparte que se desincronice):
    rev      = fecha ISO en que Claude la revisó a mano
    revNota  = qué se corrigió
    lemaFuente='manual' / lemaEsFuente='manual'  -> la app ya no los vuelve a tocar nunca

QUIÉN MANDA: lo que se marca aquí es MANUAL y gana a Wiktionary y al contexto. Por eso `subir`
fusiona por palabra (la nube conserva lo que el usuario haya añadido desde el navegador).
"""
import firebase_admin
from firebase_admin import credentials, auth, firestore
import glob, json, os, sys, io, datetime

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(BASE, 'datos')
LOCAL = os.path.join(DATOS, 'vocabulario.json')
CLAVE = 'italiano-vocab-activo'                 # users/{uid}/progreso/{CLAVE}

_st = {'lista': None, 'tocadas': []}


# ------------------------------------------------------------------ conexión
def _db():
    if not firebase_admin._apps:
        hits = glob.glob(os.path.join(BASE, '*firebase-adminsdk*.json')) or \
               glob.glob(os.path.join(BASE, 'serviceAccount.json'))
        if not hits:
            sys.exit('No encuentro la llave de servicio (*firebase-adminsdk*.json) en ' + BASE)
        firebase_admin.initialize_app(credentials.Certificate(hits[0]))
    users = list(auth.list_users().iterate_all())
    if not users:
        sys.exit('No hay usuarios en Authentication.')
    return firestore.client().collection('users').document(users[0].uid) \
                   .collection('progreso').document(CLAVE)


def _leer_local():
    return json.load(io.open(LOCAL, encoding='utf-8')) if os.path.exists(LOCAL) else []


def _escribir_local(lista):
    os.makedirs(DATOS, exist_ok=True)
    tmp = LOCAL + '.tmp'
    with io.open(tmp, 'w', encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False, indent=2)
    os.replace(tmp, LOCAL)                       # atómico: nunca deja el archivo a medias


def _norm(s):
    return (s or '').strip().lower()


# ------------------------------------------------------------------ nube <-> local
def bajar():
    d = _db().get()
    lista = ((d.to_dict() or {}).get('data')) or []
    _escribir_local(lista)
    print('bajadas %d palabras -> datos/vocabulario.json' % len(lista))
    return lista


def subir():
    """Fusiona por palabra: lo local (revisado a mano) manda, pero NUNCA borra lo que el usuario
       haya añadido desde el navegador mientras tanto."""
    local = _leer_local()
    if not local:
        sys.exit('datos/vocabulario.json está vacío: corre antes `bajar`.')
    ref = _db()
    nube = ((ref.get().to_dict() or {}).get('data')) or []
    idx = {_norm(w.get('it')): w for w in local}
    fusion, nuevas = list(local), 0
    for w in nube:
        if _norm(w.get('it')) not in idx:
            fusion.append(w); nuevas += 1
    ref.set({'data': fusion, 't': int(datetime.datetime.now().timestamp() * 1000)})
    print('subidas %d palabras (%d añadidas desde el navegador, conservadas)' % (len(fusion), nuevas))


# ------------------------------------------------------------------ autoría
def abrir():
    _st['lista'] = _leer_local()
    if not _st['lista']:
        sys.exit('No hay datos/vocabulario.json. Corre `python tools/vocab.py bajar`.')
    print('cargadas %d palabras' % len(_st['lista']))
    return _st['lista']


def buscar(it):
    for w in _st['lista'] or []:
        if _norm(w.get('it')) == _norm(it):
            return w
    return None


def fijar(it, nota=None, **campos):
    """Corrige una palabra a mano y la marca como revisada. Los campos que toques quedan
       BLINDADOS: la app no los vuelve a sobrescribir."""
    if _st['lista'] is None:
        abrir()
    w = buscar(it)
    if w is None:
        raise KeyError('no está en el vocabulario: %r' % it)
    for k, v in campos.items():
        w[k] = v
    if 'lema' in campos or 'pos' in campos:
        w['lemaFuente'] = 'manual'
    if 'lemaEs' in campos:
        w['lemaEsFuente'] = 'manual'
    w['rev'] = datetime.date.today().isoformat()
    if nota:
        w['revNota'] = nota
    _st['tocadas'].append(it)
    return w


def agregar(it, es, lema=None, pos=None, lemaEs=None, ctx='', nota=None):
    """Añade una palabra nueva ya curada (equivalente a guardarla desde la app, pero revisada)."""
    if _st['lista'] is None:
        abrir()
    if buscar(it):
        raise KeyError('ya existe: %r' % it)
    w = {'it': it, 'es': es, 'ctx': ctx, 'estado': 'practica',
         't': int(datetime.datetime.now().timestamp() * 1000),
         'rev': datetime.date.today().isoformat()}
    if lema:   w['lema'] = lema;   w['lemaFuente'] = 'manual'
    if pos:    w['pos'] = pos
    if lemaEs: w['lemaEs'] = lemaEs; w['lemaEsFuente'] = 'manual'
    if nota:   w['revNota'] = nota
    _st['lista'].append(w)
    _st['tocadas'].append(it + ' (nueva)')
    return w


def guardar():
    if _st['lista'] is None:
        sys.exit('llama antes a abrir()')
    _escribir_local(_st['lista'])
    print('\n✅ escritas %d palabras · tocadas en esta pasada: %d' % (len(_st['lista']), len(_st['tocadas'])))
    for t in _st['tocadas']:
        print('   ·', t)
    print('\nAhora: python tools/vocab.py subir')


# ------------------------------------------------------------------ registro
SOSPECHOSA = 'lemaFuente'


def estado(bajar_antes=True):
    """El registro: qué revisé ya, qué falta y qué pinta mal. NO cambia nada."""
    lista = bajar() if bajar_antes else _leer_local()
    rev = [w for w in lista if w.get('rev')]
    pend = [w for w in lista if not w.get('rev')]
    dudosas = [w for w in pend if w.get('lemaFuente') == 'regla']
    sin_lema = [w for w in pend if not w.get('lema') and (w.get('pos') or '') != 'locución']
    sin_trad = [w for w in pend if w.get('lema') and not w.get('lemaEs')]

    print('\n=== REGISTRO DE REVISIÓN MANUAL ===')
    print('total %d · revisadas por Claude %d · pendientes %d' % (len(lista), len(rev), len(pend)))
    if rev:
        print('\nÚLTIMAS REVISADAS:')
        for w in sorted(rev, key=lambda x: x.get('rev', ''), reverse=True)[:10]:
            print('  %-22s %s  %s' % (w.get('it', '')[:22], w.get('rev', ''), (w.get('revNota') or '')[:52]))
    if dudosas:
        print('\n⚠ MARCADAS PARA REVISAR (%d) — la app no supo decidir:' % len(dudosas))
        for w in dudosas:
            print('  %-22s %-13s -> %-18s %s' % (w.get('it', '')[:22], w.get('pos') or '?',
                                                 w.get('lema') or '—', (w.get('ctx') or '')[:38]))
    if sin_lema:
        print('\nSIN PALABRA BASE (%d): %s' % (len(sin_lema), ', '.join(w.get('it', '') for w in sin_lema[:14])))
    if sin_trad:
        print('\nSIN TRADUCCIÓN SIMPLE (%d): %s' % (len(sin_trad), ', '.join(w.get('it', '') for w in sin_trad[:14])))
    print('\nsiguiente: revisa las ⚠ con  fijar("palabra", lema=…, pos=…, lemaEs=…, nota=…)')
    return {'total': len(lista), 'revisadas': len(rev), 'pendientes': len(pend), 'dudosas': len(dudosas)}


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'estado'
    if cmd == 'bajar':
        bajar()
    elif cmd == 'subir':
        subir()
    elif cmd == 'estado':
        estado()
    else:
        print(__doc__)
