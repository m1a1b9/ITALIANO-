# -*- coding: utf-8 -*-
"""
Motor para CONSTRUIR un día del curso (§4). Hermano de tools/cancion.py.

Existe por dos razones medidas sobre dia23.html:
  · el 52% de cada día era ANDAMIAJE (head 16% + markup 36%) que se reescribía a mano
  · el <style> era 87% idéntico entre días… y aun así derivó (el día 22 acabó con otros colores)
Aquí el andamiaje se emite solo. Al construir un día se escribe tools/_dia_NN.py con SOLO CONTENIDO.

USO
    from dia_build import *
    dia(24, semana=4, nivel="B2", titulo="…", sub="…")
    objetivo("…", "…", "…")            # 2-4 metas can-do
    ripasso("…")
    h2("Il meccanismo"); p("…")
    tabla(["col A","col B"], [["a1","b1"], ["a2","b2"]])
    hack("…", cuaderno=True)
    alerta("…")
    guiado(["paso 1","paso 2"], a_medias="…")
    frasi_pronte([("it","es"), …])
    in_contesto("dialogo it", "traducción es")
    slang("Meno male", reg="verde", fon="[…]", it="…", es="…", uso="…", ej=("it","es"))
    cultura(24, "Título", gancho="…", ctx=("IT","ES"), frasi=[("it","es")], spunto="…", puente="…")
    dettato(["f1","f2","f3"])
    ej(1, "enunciado", rows=2, ph="…", ripasso_tuo=False)
    solu(1, "solución")
    libre(10, 15)                       # los de producción libre
    autocontrollo("…","…")
    riflessione(["…"], tiempo="50-60 min", domani="…")
    guardar()

QUE IMPONE guardar() — se NIEGA a escribir si algo falla (cada regla nació de un fallo real):
  · faltan ejercicios e1..e15 (o e1..e10 + x1..x10 en día de repaso)
  · un ejercicio no tiene solu() NI está en libre()      <- el bug del día 21 (faltaba el e12)
  · falta objetivo, ripasso, dettato, cultura con .spunto, autocontrollo o riflessione
  · el slang no está entre 2 y 4 entradas
  · la siembra "(ripasso tuo)" pasa del 35%
  · en día de repaso, falta la rúbrica CEFR
Y emite SIEMPRE el mismo <style> y el ?v= vigente: se acabó el drift y el bumpeo archivo por archivo.
"""
import io, os, re, sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── La versión de caché vive AQUÍ. Cambiarla aquí basta para los días que se generen. ──────
VERSION = '20260808d'

FIREBASE = ('<script defer src="https://www.gstatic.com/firebasejs/10.12.2/firebase-app-compat.js"></script>'
            '<script defer src="https://www.gstatic.com/firebasejs/10.12.2/firebase-auth-compat.js"></script>'
            '<script defer src="https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore-compat.js"></script>')

ASSETS = ['firebase.js', 'vocab.js', 'frases.js', 'curso.js', 'respuestas.js']

STYLE = """  body { font-family: -apple-system, sans-serif; background: #f5f7fa; color: #1c1c1e; max-width: 680px; margin: 0 auto; padding: 2rem 1.5rem 4rem; line-height: 1.7; }
  .header { border-left: 4px solid %(ac)s; padding-left: 1rem; margin-bottom: 2.5rem; }
  .header .dia { font-size: .75rem; font-weight: 600; letter-spacing: .12em; text-transform: uppercase; color: %(ac)s; margin-bottom: .3rem; }
  .header h1 { font-size: 1.7rem; font-weight: 700; margin: 0; }
  .header p { color: #666; font-size: .9rem; margin: .3rem 0 0; }
  h2 { font-size: .7rem; font-weight: 700; letter-spacing: .15em; text-transform: uppercase; color: %(ac)s; margin: 2rem 0 .8rem; }
  h3 { font-size: .95rem; font-weight: 700; margin: 1.2rem 0 .5rem; }
  table { width: 100%%; border-collapse: collapse; margin: .5rem 0 1rem; font-size: .92rem; }
  th { background: #1c1c1e; color: #fff; text-align: left; padding: .5rem .8rem; font-size: .7rem; letter-spacing: .08em; text-transform: uppercase; }
  td { padding: .55rem .8rem; border-bottom: 1px solid #dde5dd; }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: #eef2ee; }
  .slang { background: #fff; border: 1px solid #dde5dd; border-radius: 8px; padding: 1rem 1.2rem; margin: .5rem 0 1rem; }
  .slang strong { color: %(ac)s; font-size: 1.05rem; }
  .slang .uso { font-size: .82rem; color: #888; margin-top: .2rem; }
  .slang .ejemplo { font-size: .88rem; font-style: italic; color: #444; margin-top: .4rem; background: #f5f7fa; padding: .3rem .6rem; border-radius: 4px; }
  .ejercicio { counter-reset: ej; padding-left: 0; }
  .ejercicio li { list-style: none; counter-increment: ej; padding: .6rem 0 .6rem 2.4rem; position: relative; border-bottom: 1px solid #dde5dd; font-size: .92rem; }
  .ejercicio li:last-child { border-bottom: none; }
  .ejercicio li::before { content: counter(ej); position: absolute; left: 0; top: .65rem; background: %(ac)s; color: #fff; font-size: .65rem; font-weight: 700; width: 1.5rem; height: 1.5rem; border-radius: 50%%; display: flex; align-items: center; justify-content: center; }
  .esame { counter-reset: ex; padding-left: 0; }
  .esame li { list-style: none; counter-increment: ex; padding: .7rem 0 .7rem 2.4rem; position: relative; border-bottom: 1px solid #e0d0d0; font-size: .92rem; }
  .esame li:last-child { border-bottom: none; }
  .esame li::before { content: "X" counter(ex); position: absolute; left: 0; top: .65rem; background: #922b21; color: #fff; font-size: .58rem; font-weight: 700; width: 1.7rem; height: 1.5rem; border-radius: 4px; display: flex; align-items: center; justify-content: center; }
  .nota { background: #f0f7f4; border-left: 3px solid %(ac)s; padding: .7rem 1rem; border-radius: 0 6px 6px 0; font-size: .88rem; color: #1a4731; margin: .8rem 0; }
  .alerta { background: #fdf0ef; border-left: 3px solid #c0392b; padding: .7rem 1rem; border-radius: 0 6px 6px 0; font-size: .88rem; color: #922b21; margin: .8rem 0; }
  .bloque { background: #fff; border: 1px solid #dde5dd; border-radius: 8px; padding: 1rem 1.2rem; margin: .8rem 0; font-size: .92rem; }
  .tiempo { text-align: right; font-size: .8rem; color: #999; margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #dde5dd; }
  .it { font-weight: 600; font-style: italic; }
  p { font-size: .92rem; }
  ul { font-size: .92rem; padding-left: 1.2rem; }
  .guiado { background: #fffdf3; border: 1px solid #e6d9a8; border-radius: 8px; padding: 1rem 1.2rem; margin: .8rem 0; font-size: .92rem; }
  .guiado h3 { margin-top: 0; color: #8a6d1f; }
  .paso { background: #fff; border-left: 3px solid #b8860b; padding: .4rem .8rem; margin: .4rem 0; border-radius: 0 4px 4px 0; }
  .big { font-size: 1.15rem; font-weight: 700; color: %(ac)s; letter-spacing: .02em; text-align: center; }
  .ascolto { background: #eef5ff; border: 1px solid #bcd4ea; border-radius: 8px; padding: 1rem 1.2rem; margin: .8rem 0; }
  .ascolto button.say-frase { background: #1a4d80; color: #fff; border: 0; border-radius: 6px; padding: .5rem .9rem; font-size: .85rem; cursor: pointer; margin: .3rem 0; }
  .fosil { background: #fff4f2; border: 2px solid #c0392b; border-radius: 8px; padding: 1rem 1.2rem; margin: 1rem 0; }
  .fosil h3 { color: #922b21; margin-top: 0; }
  .rubrica { background: #f4f0fa; border: 1px solid #cfc0e8; border-radius: 8px; padding: 1rem 1.2rem; margin: .8rem 0; font-size: .88rem; }"""

_ = {}


def dia(nn, semana, titulo, sub, nivel="B2", repaso=False, acento=None):
    _.clear()
    _.update(nn=int(nn), semana=semana, titulo=titulo, sub=sub, nivel=nivel, repaso=repaso,
             acento=acento or ('#b8860b' if repaso else '#2d6a4f'),
             cuerpo=[], ejs=[], exs=[], solus={}, libres=set(),
             objetivo=None, ripasso=None, dettato=None, cultura=None,
             auto=None, rifl=None, n_slang=0)


# ─────────────────────────────────────────────── bloques de contenido
def _add(html):
    _['cuerpo'].append(html)


def objetivo(*metas):
    _['objetivo'] = ('<div class="bloque" style="background:#eef5ff;border-color:#bcd4ea">'
                     '<strong>🎯 Obiettivo di oggi</strong> — al terminar podrás: '
                     + ' · '.join('%s %s' % (c, m) for c, m in zip('①②③④⑤', metas)) + '.</div>')


def ripasso(txt):
    _['ripasso'] = '<h2>Ripasso veloce (5 min)</h2>\n<p>%s</p>' % txt


def h2(t):   _add('<h2>%s</h2>' % t)
def h3(t):   _add('<h3>%s</h3>' % t)
def p(t):    _add('<p>%s</p>' % t)
def big(t):  _add('<p class="big">%s</p>' % t)
def bloque(t): _add('<div class="bloque">%s</div>' % t)


def tabla(cabeceras, filas):
    h = ''.join('<th>%s</th>' % c for c in cabeceras)
    b = ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in f) for f in filas)
    _add('<table>\n  <tr>%s</tr>\n  %s\n</table>' % (h, b))


def hack(txt, cuaderno=False):
    cu = ' <span class="cuad">a tu cuaderno</span>' if cuaderno else ''
    _add('<div class="nota">🔑 <strong>HACK</strong> — %s%s</div>' % (txt, cu))


def nota(txt, cuaderno=False):
    cu = ' <span class="cuad">a tu cuaderno</span>' if cuaderno else ''
    _add('<div class="nota">%s%s</div>' % (txt, cu))


def alerta(txt):
    _add('<div class="alerta">⚠️ %s</div>' % txt)


def fosil(titulo, txt):
    _add('<div class="fosil"><h3>🔴 %s</h3>%s</div>' % (titulo, txt))


def guiado(pasos, a_medias=None, titulo="Esempio guidato — paso a paso"):
    h = '<div class="guiado">\n  <h3>📐 %s</h3>\n' % titulo
    h += ''.join('  <div class="paso">%s</div>\n' % x for x in pasos)
    if a_medias:
        h += ('  <p style="margin-top:.8rem"><strong>Ahora tú, a medias.</strong> %s</p>\n'
              '  <p style="font-size:.86rem;color:#666">(la solución está en el solucionario, '
              '«esempio guidato»)</p>\n' % a_medias)
    _add(h + '</div>')


def frasi_pronte(pares):
    _add('<h2>🧱 Frasi pronte</h2>\n<ul>\n' +
         ''.join('  <li><span class="it">%s</span> → %s</li>\n' % (i, e) for i, e in pares) +
         '</ul>')


def in_contesto(dialogo_it, traduccion, titulo="In contesto"):
    _add('<h2>📖 %s</h2>\n<div class="bloque">\n  <span class="it">%s</span><br>\n'
         '  <span style="color:#666;font-size:.86rem">→ %s</span>\n</div>'
         % (titulo, dialogo_it, traduccion))


def slang(palabra, reg, fon, it, es, uso, ej):
    if _['n_slang'] == 0:
        _add('<h2>🗣️ Cultura &amp; Strada</h2>')
    _['n_slang'] += 1
    _add('<div class="slang">\n  <strong>%s</strong> <span class="reg %s">%s</span> '
         '<span style="font-size:.78rem;color:#888;font-weight:400">%s</span><br>\n'
         '  <span class="it">%s</span> <span style="color:#666">→ %s</span>\n'
         '  <div class="uso">%s</div>\n'
         '  <div class="ejemplo"><span class="it">%s</span> → %s</div>\n</div>'
         % (palabra, 'verde' if reg == 'verde' else 'amari',
            {'verde': 'suave', 'medio': 'medio'}.get(reg, reg), fon, it, es, uso, ej[0], ej[1]))


def cultura(cap, titulo_cap, gancho, ctx, frasi, spunto, puente):
    f = ''.join('    <div class="f"><span class="it">%s</span> <span class="es">→ %s</span></div>\n'
                % (i, e) for i, e in frasi)
    _['cultura'] = (
        '<h2>☕ Cultura — di che parlare con un italiano</h2>\n<div class="cultura">\n'
        '  <span class="tipo">Dal capitolo %d — %s</span>\n  <h3>%s</h3>\n'
        '  <div class="ctx"><span class="it">%s</span> '
        '<span style="color:#666;font-size:.85rem">→ %s</span></div>\n'
        '  <div class="frasi">\n    <div class="lbl">💬 Per parlarne</div>\n%s  </div>\n'
        '  <div class="spunto">🗣️ <b>Lo spunto:</b> <span class="it">%s</span></div>\n'
        '  <div class="puente">🇲🇽 %s</div>\n</div>'
        % (cap, titulo_cap, gancho, ctx[0], ctx[1], f, spunto, puente))


def dettato(frases):
    b = ''.join('  <button class="say-frase" data-frase="%s">Frase %d</button>\n' % (f, i + 1)
                for i, f in enumerate(frases))
    _['dettato'] = ('<h2>✍️ Dettato — scrivi quello che senti</h2>\n<div class="bloque">\n%s'
                    '  <textarea class="resp" data-ej="dettato" rows="3" '
                    'placeholder="1. … 2. … 3. …"></textarea>\n</div>' % b)
    _['dettato_frases'] = frases


def audio(botones):
    """Bloque de botones de escucha dentro de un ejercicio. botones = [(etiqueta, frase), …]"""
    return ('<div class="ascolto">' +
            ''.join('<button class="say-frase" data-frase="%s">🔊 %s</button>' % (f, e)
                    for e, f in botones) + '</div>')


def ej(n, enunciado, rows=2, ph="…", ripasso_tuo=False):
    marca = ' <em>(ripasso tuo)</em>' if ripasso_tuo else ''
    _['ejs'].append((n, '<li><strong>%s</strong>%s\n    <textarea class="resp" data-ej="e%d" '
                        'rows="%d" placeholder="%s"></textarea></li>'
                     % (enunciado, marca, n, rows, ph), ripasso_tuo))


def esame(n, enunciado, rows=2, ph="…"):
    _['exs'].append((n, '<li><strong>%s</strong>\n    <textarea class="resp" data-ej="x%d" '
                        'rows="%d" placeholder="%s"></textarea></li>' % (enunciado, n, rows, ph)))


def solu(n, txt):
    _['solus'][n] = txt


def solu_guiado(txt):
    _['solus']['guiado'] = txt


def libre(*ns):
    _['libres'].update(ns)


def rubrica(txt):
    _add('<div class="rubrica">%s</div>')
    _['cuerpo'][-1] = '<div class="rubrica"><strong>📐 Rúbrica CEFR</strong> — %s</div>' % txt


def autocontrollo(*items):
    _['auto'] = ('<div class="bloque" style="background:#f3faf6;border-color:#9bd3b4">'
                 '<strong>✅ Autocontrollo</strong> — ¿ya puedes…? '
                 + ' · '.join('%s %s' % (c, m) for c, m in zip('①②③④⑤', items))
                 + '. Si algo tambalea, márcalo 🔁.</div>')


def riflessione(items, tiempo, domani):
    _['rifl'] = ('<h2>Riflessione del giorno</h2>\n<ul>\n'
                 + ''.join('  <li>%s</li>\n' % x for x in items)
                 + '  <li>🎧 Bonus: 10 min de <a href="inmersion.html">Inmersión</a>.</li>\n</ul>\n'
                 + '<div class="tiempo">⏱ Tempo stimato: %s &nbsp;·&nbsp; Domani: %s</div>'
                 % (tiempo, domani))


# ─────────────────────────────────────────────── validación + escritura
def _validar():
    f = []
    nn, rep = _['nn'], _['repaso']
    nums = sorted(n for n, _h, _r in _['ejs'])
    tope = 10 if rep else 15
    faltan = [i for i in range(1, tope + 1) if i not in nums]
    if faltan:
        f.append('faltan ejercicios: %s' % ', '.join('e%d' % i for i in faltan))
    if len(nums) != len(set(nums)):
        f.append('hay ejercicios repetidos')
    if rep:
        xn = sorted(n for n, _h in _['exs'])
        fx = [i for i in range(1, 11) if i not in xn]
        if fx:
            f.append('faltan ítems de examen: %s' % ', '.join('x%d' % i for i in fx))
        if not any('rubrica' in c for c in _['cuerpo']):
            f.append('día de repaso sin RÚBRICA CEFR')
    # el bug del día 21: ejercicio sin solución y sin declarar libre
    huer = [n for n in nums if n not in _['solus'] and n not in _['libres']]
    if huer:
        f.append('ejercicios sin solu() NI en libre(): %s' % ', '.join(str(x) for x in huer))
    for k, v in (('objetivo', 'objetivo can-do'), ('ripasso', 'ripasso veloce'),
                 ('dettato', 'dettato'), ('cultura', 'cápsula ☕'),
                 ('auto', 'autocontrollo'), ('rifl', 'riflessione')):
        if not _.get(k):
            f.append('falta el bloque: %s' % v)
    if _['cultura'] and 'class="spunto"' not in _['cultura']:
        f.append('la cápsula no tiene .spunto')
    if not 2 <= _['n_slang'] <= 4:
        f.append('slang: %d entradas (§4 pide 2-4)' % _['n_slang'])
    if not any('class="alerta"' in c for c in _['cuerpo']):
        f.append('falta alguna alerta contrastiva')
    # Audios demasiado largos: Chrome/Edge fallan EN SILENCIO por encima de ~300 chars y además
    # atascan la cola, dejando muda toda la página (pasó en el día 21 con un audio de 512).
    # curso.js ya trocea, pero conviene no depender solo de eso: mejor varios botones cortos.
    for fr in re.findall(r'data-frase="([^"]*)"', ' '.join(_['cuerpo']) +
                         (_['dettato'] or '') + ' '.join(h for _n, h, _r in _['ejs'])):
        if len(fr) > 300:
            f.append('audio de %d caracteres («%s…») — pártelo en varios botones: por encima de '
                     '~300 Chrome/Edge enmudecen' % (len(fr), fr[:45]))

    n_siembra = sum(1 for _n, _h, r in _['ejs'] if r)
    if nums:
        pct = 100 * n_siembra // len(nums)
        if pct > 35:
            f.append('siembra %d%% (%d/%d) — máximo ~35%%' % (pct, n_siembra, len(nums)))
    return f


def guardar(force=False):
    fallos = _validar()
    print('--- DÍA %02d ---' % _['nn'])
    print('ejercicios: %d%s · slang: %d · siembra: %d'
          % (len(_['ejs']), (' + %d examen' % len(_['exs'])) if _['repaso'] else '',
             _['n_slang'], sum(1 for _n, _h, r in _['ejs'] if r)))
    if fallos and not force:
        for x in fallos:
            print('   ❌', x)
        print('\n⛔ NO SE ESCRIBIÓ NADA. Corrige y vuelve a ejecutar.')
        sys.exit(1)
    for x in fallos:
        print('   ⚠️ (forzado)', x)

    assets = ('<link rel="stylesheet" href="assets/curso.css?v=%s">' % VERSION) + FIREBASE + \
             ''.join('<script defer src="assets/%s?v=%s"></script>' % (a, VERSION) for a in ASSETS)

    partes = [_['objetivo'], _['ripasso']] + _['cuerpo']
    partes.append(_['cultura'])
    partes.append(_['dettato'])

    tit_ej = 'Ripasso — consolidación (%d)' % len(_['ejs']) if _['repaso'] else 'Esercizi'
    partes.append('<h2>%s</h2>\n<ol class="ejercicio">\n%s\n</ol>'
                  % (tit_ej, '\n'.join(h for _n, h, _r in sorted(_['ejs']))))
    if _['repaso'] and _['exs']:
        partes.append('<h2>📝 Esame della settimana (%d)</h2>\n<ol class="esame">\n%s\n</ol>'
                      % (len(_['exs']), '\n'.join(h for _n, h in sorted(_['exs']))))

    sol = ''
    if 'guiado' in _['solus']:
        sol += '    <p><strong>Esempio guidato:</strong> %s</p>\n' % _['solus']['guiado']
    if _.get('dettato_frases'):
        sol += ('    <p><strong>Dettato:</strong> ' +
                ' '.join('%d) <span class="it">%s</span>' % (i + 1, x)
                         for i, x in enumerate(_['dettato_frases'])) + '</p>\n')
    for n in sorted(k for k in _['solus'] if isinstance(k, int)):
        sol += '    <p><strong>%d.</strong> %s</p>\n' % (n, _['solus'][n])
    if _['libres']:
        ls = ', '.join(str(x) for x in sorted(_['libres']))
        sol += ('    <p><strong>%s:</strong> respuesta libre — dime «ya terminé el día %d» '
                'y te las corrijo.</p>\n' % (ls, _['nn']))
    partes.append('<details class="solu">\n  <summary>Soluzioni / Soluciones (ábrelas después de '
                  'intentarlo)</summary>\n  <div class="body">\n%s  </div>\n</details>' % sol)
    partes.append(_['auto'])
    partes.append(_['rifl'])

    etiqueta = ('Ripasso + Esame' if _['repaso'] else 'Livello ' + _['nivel'])
    html = ('<!DOCTYPE html>\n<html lang="it">\n<head>\n<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            '<title>Giorno %d — Italiano</title>\n<style>\n%s\n</style>\n%s\n</head>\n<body>\n\n'
            '<div class="header">\n  <div class="dia">Settimana %s · Giorno %d · %s</div>\n'
            '  <h1>%s</h1>\n  <p>%s</p>\n</div>\n\n%s\n\n</body>\n</html>\n'
            % (_['nn'], STYLE % {'ac': _['acento']}, assets,
               _['semana'], _['nn'], etiqueta, _['titulo'], _['sub'],
               '\n\n'.join(x for x in partes if x)))

    p_out = os.path.join(BASE, 'dia%02d.html' % _['nn'])
    tmp = p_out + '.tmp'
    with io.open(tmp, 'w', encoding='utf-8') as fh:
        fh.write(html)
    os.replace(tmp, p_out)
    print('   ✅ escrito %s (%d bytes)' % (os.path.basename(p_out), len(html)))


def focos(n=6):
    """Imprime en una línea los rasgos vencidos del perfil (para no releer perfil.json entero)."""
    import json
    p = json.load(io.open(os.path.join(BASE, 'datos', 'perfil.json'), encoding='utf-8'))
    rs = [(v.get('prioridad', 0), k, v) for k, v in p['rasgos'].items()
          if v.get('estado') != 'dominado' and v.get('prioridad', 0) >= 4]
    for pr, k, v in sorted(rs, reverse=True)[:n]:
        print('%-34s p=%-2s sig=%-9s %s' % (k, pr, v.get('proxima_siembra'), v.get('estado')))
