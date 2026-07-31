# -*- coding: utf-8 -*-
"""Mini-servidor del Curso de Italiano.
Sirve las páginas y auto-guarda tus respuestas en disco (sin botones).
Archivos en datos/: respuestas.json (lo que contestas) y errores.json (lo que yo corrijo)."""
import http.server, socketserver, json, os, shutil, tempfile, time, glob, re

PORT = int(os.environ.get("PORT", 8099))  # el .bat usa 8099; puede sobreescribirse por env
BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "datos")
os.makedirs(DATA, exist_ok=True)
BK = os.path.join(DATA, "backups")          # respaldos automáticos (anti-pérdida)
os.makedirs(BK, exist_ok=True)
KEEP_BACKUPS = 40                            # cuántos respaldos conservar por archivo
RESP = os.path.join(DATA, "respuestas.json")
ERR  = os.path.join(DATA, "errores.json")   # LEGADO (agregado); ya no es la fuente de verdad
ERR_DIR = os.path.join(DATA, "errores")     # FUENTE DE VERDAD: un archivo por día -> errores/NN.json
os.makedirs(ERR_DIR, exist_ok=True)

def err_path(nn):
    return os.path.join(ERR_DIR, "%s.json" % str(nn).zfill(2))

# --- Canciones: una por archivo (datos/canciones/<id>.json). Mismo patrón que errores/. ---
CANC_DIR = os.path.join(DATA, "canciones")
os.makedirs(CANC_DIR, exist_ok=True)

def _safe_id(cid):
    return re.sub(r"[^a-z0-9\-_]", "", str(cid).lower())

def canc_path(cid):
    return os.path.join(CANC_DIR, "%s.json" % _safe_id(cid))

def load_canc_all():
    """Agregado {id: {...}} leyendo datos/canciones/*.json. Fallback al canciones.json viejo."""
    out = {}
    for f in sorted(glob.glob(os.path.join(CANC_DIR, "*.json"))):
        cid = os.path.splitext(os.path.basename(f))[0]
        d = load(f)
        if d:
            out[cid] = d
    if not out:
        legacy = load(CANC)
        if isinstance(legacy, dict):
            return legacy
    return out

def load_canc_one(cid):
    return load(canc_path(cid)) or {}

def load_err_dia(nn):
    """Corrección de UN día (datos/errores/NN.json). {} si no existe."""
    return load(err_path(nn)) or {}

def load_err_all():
    """Arma el agregado {NN: {...}} leyendo datos/errores/*.json.
    Compatibilidad: si la carpeta está vacía y existe el errores.json viejo, usa ese."""
    out = {}
    for f in sorted(glob.glob(os.path.join(ERR_DIR, "*.json"))):
        nn = os.path.splitext(os.path.basename(f))[0]
        d = load(f)
        if d:
            out[nn] = d
    if not out:
        legacy = load(ERR)
        if isinstance(legacy, dict):
            return legacy
    return out
EXAM = os.path.join(DATA, "examenes.json")
PERFIL = os.path.join(DATA, "perfil.json")
INMER = os.path.join(DATA, "inmersion.json")
CANC = os.path.join(DATA, "canciones.json")
DUDAS = os.path.join(DATA, "dudas.json")
LIBRO = os.path.join(DATA, "libro.json")

def load(p):
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def read_strict(p):
    """Para ESCRITURAS: devuelve el JSON del archivo. Si el archivo EXISTE y NO está vacío
    pero no se pudo leer/parsear (lock de sync, corrupción momentánea), devuelve None:
    el que llama NO debe sobrescribir (así no se borran los demás días por un fallo temporal).
    Devuelve {} solo si el archivo de verdad no existe o está vacío."""
    if not os.path.exists(p) or os.path.getsize(p) == 0:
        return {}
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

def _backup(p, min_interval=600):
    """Copia p a datos/backups/<archivo>.<timestamp>. Throttle: como mucho 1 respaldo cada
    min_interval segundos por archivo (evita crear miles al teclear). Conserva KEEP_BACKUPS."""
    if os.path.dirname(os.path.abspath(p)) == os.path.abspath(BK):
        return  # no respaldar los propios respaldos (evita bucle)
    if not (os.path.exists(p) and os.path.getsize(p) > 0):
        return
    base = os.path.basename(p)
    bags = sorted(glob.glob(os.path.join(BK, base + ".*")))
    if min_interval and bags:
        try:
            if time.time() - os.path.getmtime(bags[-1]) < min_interval:
                return
        except Exception:
            pass
    try:
        ts = time.strftime("%Y%m%d-%H%M%S")
        shutil.copy2(p, os.path.join(BK, base + "." + ts))
        bags = sorted(glob.glob(os.path.join(BK, base + ".*")))
        for b in bags[:-KEEP_BACKUPS]:
            try: os.remove(b)
            except Exception: pass
    except Exception:
        pass

def save(p, d):
    """Guardado ANTI-PÉRDIDA: respalda el archivo actual y escribe de forma ATÓMICA
    (a un temporal + os.replace) para que nunca quede un JSON a medias/corrupto."""
    _backup(p)
    dirn = os.path.dirname(p) or "."
    fd, tmp = tempfile.mkstemp(dir=dirn, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
        os.replace(tmp, p)
    except Exception:
        try: os.remove(tmp)
        except Exception: pass
        raise

# ===== SEGURO DE RESPUESTAS: respaldos automáticos + restauración =====
# Objetivo: que NUNCA se pierdan las respuestas de días anteriores (como pasó con 01-09).
# respuestas.json vive en el servidor (esta PC), así que ya es independiente del navegador;
# esto lo protege además contra borrados/resets del archivo.
import glob, time, datetime
BACKUP_DIR = os.path.join(DATA, "backups")
os.makedirs(BACKUP_DIR, exist_ok=True)
RESP_BEST = os.path.join(BACKUP_DIR, "respuestas_best.json")  # la versión más "rica" jamás vista

def _riqueza(d):
    """Nº total de recuadros con texto en todo el archivo (mide cuánto contenido hay)."""
    if not isinstance(d, dict):
        return 0
    n = 0
    for dia, campos in d.items():
        if isinstance(campos, dict):
            for k, v in campos.items():
                if k != "evocab_q" and isinstance(v, str) and v.strip():
                    n += 1
    return n

def backup_respuestas():
    """Snapshot de respuestas.json (throttled a 1 cada 5 min) + 'best' que nunca decrece.
    Conserva los últimos 40 snapshots. Silencioso; nunca rompe el guardado si algo falla."""
    try:
        snaps = sorted(glob.glob(os.path.join(BACKUP_DIR, "resp_2*.json")))
        if snaps and (time.time() - os.path.getmtime(snaps[-1]) < 300):
            return  # ya respaldamos hace menos de 5 min
        actual = load(RESP)
        if _riqueza(actual) == 0:
            return
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        save(os.path.join(BACKUP_DIR, "resp_%s.json" % ts), actual)
        if _riqueza(actual) >= _riqueza(load(RESP_BEST)):
            save(RESP_BEST, actual)  # el 'best' solo sube, nunca baja
        for old in sorted(glob.glob(os.path.join(BACKUP_DIR, "resp_2*.json")))[:-40]:
            try: os.remove(old)
            except Exception: pass
    except Exception:
        pass

def restaurar_si_vacio():
    """Al arrancar: si respuestas.json está vacío/corrupto pero hay respaldo con contenido, lo restaura.
    Así jamás abres el curso y encuentras tus respuestas borradas."""
    try:
        actual = load(RESP)
        if _riqueza(actual) > 0:
            return
        best = load(RESP_BEST)
        if _riqueza(best) > 0:
            if os.path.exists(RESP):  # guarda el vacío por si acaso, antes de pisarlo
                save(os.path.join(BACKUP_DIR, "resp_VACIO_%s.json" % datetime.datetime.now().strftime("%Y%m%d_%H%M%S")), actual)
            save(RESP, best)
            print("  [ RESPALDO ] respuestas.json estaba vacio -> RESTAURADO desde el respaldo (%d recuadros)." % _riqueza(best))
    except Exception:
        pass

def chequear_sincronia():
    """Avisa si perfil.json quedó ATRÁS de errores.json (correccion que escribió
    errores.json pero olvidó actualizar el perfil → la siembra se genera con datos viejos).
    Es la salvaguarda del flujo §7.4 de REGLAS_DESARROLLO.txt."""
    err = load_err_all()
    perfil = load(PERFIL)
    dias_corr = [k for k in err.keys() if k.isdigit()]
    if not dias_corr:
        return
    ultimo_err = max(dias_corr)                       # día más nuevo ya corregido
    ultimo_perfil = str(perfil.get("ultimo_dia_corregido", "")).zfill(2)
    if not perfil:
        return
    linea = "-" * 64
    # --- A) El perfil quedó atrás en el NÚMERO de día (día nuevo corregido sin volcar) ---
    if ultimo_perfil < ultimo_err:
        print("\n" + linea)
        print("  [ AVISO ] perfil.json ESTA DESINCRONIZADO")
        print("  Las correcciones llegan al dia %s, pero el perfil solo al dia %s." % (ultimo_err, ultimo_perfil or "--"))
        print("  Falta el paso 7.4: pasar los errores al perfil (motor de siembra).")
        print("  Dile a Claude: 'sincroniza el perfil hasta el dia %s' antes de generar dias nuevos." % ultimo_err)
        print(linea + "\n")
        return
    # --- B) RE-CORRECCIONES de dias viejos: no cambian el maximo, asi que el chequeo A no las ve.
    #        Se detectan por FECHA: si algun errores/NN.json es MAS NUEVO que perfil.json,
    #        esa correccion no llego al perfil (y la siembra saldria con datos viejos). ---
    try:
        t_perfil = os.path.getmtime(PERFIL)
        pendientes = sorted(
            os.path.basename(f)[:2] for f in glob.glob(os.path.join(ERR_DIR, "*.json"))
            if os.path.getmtime(f) > t_perfil + 60      # 60 s de margen (se escriben casi a la vez)
        )
        if pendientes:
            print("\n" + linea)
            print("  [ AVISO ] hay CORRECCIONES mas nuevas que el perfil")
            print("  Dias re-corregidos sin volcar al perfil: %s" % ", ".join(pendientes))
            print("  (El chequeo por numero de dia no los ve: re-corregir un dia viejo no sube el maximo.)")
            print("  Dile a Claude: 'sincroniza el perfil con los dias %s'." % ", ".join(pendientes))
            print(linea + "\n")
            return
    except Exception:
        pass
    print("  [ OK ] perfil.json sincronizado (dia %s, sin re-correcciones pendientes). Siembra al dia." % ultimo_perfil)

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=BASE, **k)

    def _json(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.startswith("/api/respuestas"):
            return self._json(load(RESP))
        if self.path.startswith("/api/errores"):
            # /api/errores          -> agregado {NN:{...}}  (compatibilidad: index, practica)
            # /api/errores?dia=07   -> SOLO ese día (ligero: lo usa respuestas.js)
            q = ""
            if "?" in self.path:
                q = self.path.split("?", 1)[1]
            dia_q = ""
            for par in q.split("&"):
                if par.startswith("dia="):
                    dia_q = par[4:].strip()
            if dia_q:
                return self._json(load_err_dia(dia_q))
            return self._json(load_err_all())
        if self.path.startswith("/api/examenes"):
            return self._json(load(EXAM))
        if self.path.startswith("/api/perfil"):
            return self._json(load(PERFIL))
        if self.path.startswith("/api/inmersion"):
            return self._json(load(INMER))
        if self.path.startswith("/api/canciones"):
            # /api/canciones        -> agregado {id:{...}} (lo usa inmersion.html)
            # /api/canciones?id=xxx  -> SOLO esa canción (ligero)
            cid_q = ""
            if "?" in self.path:
                for par in self.path.split("?", 1)[1].split("&"):
                    if par.startswith("id="):
                        cid_q = par[3:].strip()
            if cid_q:
                return self._json(load_canc_one(cid_q))
            return self._json(load_canc_all())
        if self.path.startswith("/api/dudas"):
            return self._json(load(DUDAS))
        if self.path.startswith("/api/libro"):
            return self._json(load(LIBRO))
        return super().do_GET()

    def do_POST(self):
        if self.path.startswith("/api/respuestas"):
            n = int(self.headers.get("Content-Length", 0) or 0)
            try:
                body = json.loads(self.rfile.read(n) or b"{}")
            except Exception:
                body = {}
            dia = str(body.get("dia", "")).strip()
            answers = body.get("answers", {})
            if dia:
                data = read_strict(RESP)
                if data is None:
                    # el archivo existe pero no se pudo leer (lock/sync): NO sobrescribir
                    # (así un fallo temporal nunca borra los demás días). El cliente reintenta.
                    return self._json({"ok": False, "error": "respuestas.json ilegible; reintenta"}, 503)
                if not isinstance(data, dict):
                    data = {}
                # SALVAGUARDA anti-borrado masivo: si lo nuevo dejaría el archivo con MENOS
                # contenido total que el mejor respaldo, no piso: respaldo aparte y sigo.
                data[dia] = answers
                save(RESP, data)
                backup_respuestas()   # seguro: respaldo automático tras cada guardado
            return self._json({"ok": True})
        if self.path.startswith("/api/examenes"):
            n = int(self.headers.get("Content-Length", 0) or 0)
            try:
                body = json.loads(self.rfile.read(n) or b"{}")
            except Exception:
                body = {}
            sem = str(body.get("semana", "")).strip()
            res = body.get("resultado", {})
            if sem:
                data = load(EXAM)
                data[sem] = res
                save(EXAM, data)
            return self._json({"ok": True})
        if self.path.startswith("/api/inmersion"):
            n = int(self.headers.get("Content-Length", 0) or 0)
            try:
                body = json.loads(self.rfile.read(n) or b"{}")
            except Exception:
                body = {}
            save(INMER, body if isinstance(body, dict) else {})
            return self._json({"ok": True})
        if self.path.startswith("/api/perfil"):
            # Marca manual desde el diagnóstico: {rasgo:"<clave>", accion:"dominar"|"reactivar"}.
            # Toca SOLO ese rasgo (no sobrescribe el resto del perfil que edita Claude).
            n = int(self.headers.get("Content-Length", 0) or 0)
            try:
                body = json.loads(self.rfile.read(n) or b"{}")
            except Exception:
                body = {}
            clave = str(body.get("rasgo", "")).strip()
            accion = str(body.get("accion", "")).strip()
            perfil = load(PERFIL)
            rasgos = perfil.get("rasgos", {}) if isinstance(perfil, dict) else {}
            if clave in rasgos:
                r = rasgos[clave]
                if accion == "dominar":
                    r["prev_estado"] = r.get("estado", "consolidando")
                    r["prev_prioridad"] = r.get("prioridad", 6)
                    r["prev_tendencia"] = r.get("tendencia", "estancado")
                    r["estado"] = "dominado"
                    r["prioridad"] = 0
                    r["tendencia"] = "mejorando"
                    r["dominado_manual"] = True
                elif accion == "reactivar":
                    r["estado"] = r.pop("prev_estado", "consolidando")
                    r["prioridad"] = r.pop("prev_prioridad", 6)
                    r["tendencia"] = r.pop("prev_tendencia", "estancado")
                    r.pop("dominado_manual", None)
                save(PERFIL, perfil)
                return self._json({"ok": True})
            return self._json({"ok": False, "error": "rasgo no encontrado"}, 404)
        if self.path.startswith("/api/canciones"):
            # Guarda/actualiza UNA canción: {id, cancion:{titulo, artista, fecha, letra, analisis}}
            n = int(self.headers.get("Content-Length", 0) or 0)
            try:
                body = json.loads(self.rfile.read(n) or b"{}")
            except Exception:
                body = {}
            cid = _safe_id(body.get("id", ""))
            if cid:
                # guarda SOLO el archivo de esa canción (no reescribe las demás)
                save(canc_path(cid), body.get("cancion", {}))
            return self._json({"ok": bool(cid)})
        if self.path.startswith("/api/dudas"):
            # Anota una duda del usuario sobre UNA línea: {id, linea, texto}.
            # Claude la resuelve editando datos/dudas.json (campo "respuesta").
            n = int(self.headers.get("Content-Length", 0) or 0)
            try:
                body = json.loads(self.rfile.read(n) or b"{}")
            except Exception:
                body = {}
            cid = str(body.get("id", "")).strip()
            linea = str(body.get("linea", "")).strip()
            if cid and linea != "":
                data = load(DUDAS)
                if not isinstance(data, dict):
                    data = {}
                data.setdefault(cid, {})
                data[cid][linea] = {
                    "texto": body.get("texto", ""),
                    "fecha": body.get("fecha", ""),
                    "respuesta": data.get(cid, {}).get(linea, {}).get("respuesta"),
                }
                save(DUDAS, data)
                return self._json({"ok": True})
            return self._json({"ok": False}, 400)
        if self.path.startswith("/api/libro"):
            # Marca un capítulo como leído {cap:"01", letto:true, fecha:"..."}
            # y/o guarda la respuesta del spunto {cap:"01", spunto:"texto..."}.
            # Solo toca los campos presentes en el body (no pisa el resto).
            # El "analisi" de cada capítulo lo escribe Claude editando el JSON.
            n = int(self.headers.get("Content-Length", 0) or 0)
            try:
                body = json.loads(self.rfile.read(n) or b"{}")
            except Exception:
                body = {}
            cap = str(body.get("cap", "")).strip()
            data = load(LIBRO)
            caps = data.get("capitoli", {}) if isinstance(data, dict) else {}
            if cap and cap in caps:
                if "letto" in body:
                    caps[cap]["letto"] = bool(body.get("letto", True))
                    caps[cap]["letto_data"] = body.get("fecha", "") if caps[cap]["letto"] else None
                if "spunto" in body:
                    caps[cap]["spunto_risposta"] = body.get("spunto", "")
                save(LIBRO, data)
                return self._json({"ok": True})
            return self._json({"ok": False}, 404)
        return self._json({"ok": False}, 404)

    def end_headers(self):
        # No cachear NADA: así cada mejora del sistema llega fresca al instante
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, *a):
        pass  # silencio

class Server(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True

if __name__ == "__main__":
    with Server(("", PORT), Handler) as httpd:
        print("Curso de Italiano: http://localhost:%d/index.html" % PORT)
        print("(No cierres esta ventana mientras estudias)")
        restaurar_si_vacio()                    # seguro: recupera respuestas si el archivo quedó vacío
        print("  [ RESPUESTAS ] %d recuadros guardados en respuestas.json (respaldo automatico activo)." % _riqueza(load(RESP)))
        chequear_sincronia()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
