# -*- coding: utf-8 -*-
"""Tanda de drills nueva — cubre los 8 rasgos ACTIVOS que no tenían ninguno.
Salieron al auditar Práctica: el usuario practicaba «drills frescos» pero sus puntos débiles
de mayor prioridad no aparecían nunca. Escritura directa sobre datos/drills.json.

Estándar (el que ya funcionaba): frase COMPLETA como contexto, `accettate` con variantes válidas,
`explica` breve. Contextos nuevos (anti-repetición §8). Incluye producción ES→IT.
"""
import json, io, os, sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(BASE, 'datos', 'drills.json')

NUEVOS = {
 'pronomi_combinati': {
  'etiqueta': 'Pronombres combinados (glielo, me lo, se ne, gliene)',
  'drills': [
   {'id':'prcomb_1','tipo':'scrivi',
    'q':"Sostituisci i pronomi: «Ho dato le chiavi a Marco» → «___ ho date».",
    'soluzione':'gliele','accettate':[],
    'explica':"a Marco = gli; le chiavi = le → gli+le = GLIELE (una sola parola). El participio concuerda: date."},
   {'id':'prcomb_2','tipo':'scelta',
    'q':"«Mi presti la macchina?» — «Sì, ___ presto volentieri.»",
    'op':['te la','ti la','la ti'],'c':0,
    'explica':"ti + la → TE LA: delante de otro pronombre, mi/ti/ci/vi cambian la -i en -e."},
   {'id':'prcomb_3','tipo':'scrivi',
    'q':"Traduci: «Se lo dije ayer» (a él, el secreto).",
    'soluzione':"gliel'ho detto ieri",'accettate':['glielo ho detto ieri',"gliel ho detto ieri"],
    'explica':"⚠️ TRAMPA del español: «se lo» aquí NO es «si lo». a lui + lo = GLIELO (→ gliel'ho ante vocal)."},
   {'id':'prcomb_4','tipo':'scrivi',
    'q':"Completa con se ne: «Non gli piaceva il lavoro e ___ è andato.»",
    'soluzione':"se n'","accettate":['se ne'],
    'explica':"andarsene = irse: si + ne → SE NE (se n'è andato). Muy frecuente en el habla."},
  ]},

 'soggetto_esplicito_congiuntivo': {
  'etiqueta': 'Decir el pronombre en congiuntivo (che TU riposi)',
  'drills': [
   {'id':'sogcong_1','tipo':'scrivi',
    'q':"Completa: «Il medico vuole che ___ riposi almeno tre giorni.» (tú)",
    'soluzione':'tu','accettate':[],
    'explica':"io/tu/lui comparten la forma «riposi»: sin el pronombre no se sabe quién. En congiuntivo el sujeto se DICE."},
   {'id':'sogcong_2','tipo':'scelta',
    'q':"Quale frase è chiara? (il soggetto è «tu»)",
    'op':['Penso che tu abbia ragione','Penso che abbia ragione','Penso che ragione abbia'],'c':0,
    'explica':"«abbia» vale para io/tu/lui: hay que decir «tu» para que se entienda."},
   {'id':'sogcong_3','tipo':'scrivi',
    'q':"Traduci: «Es necesario que tú vengas mañana.»",
    'soluzione':'è necessario che tu venga domani','accettate':['bisogna che tu venga domani'],
    'explica':"El español marca la persona en «vengas»; el italiano no (venga = io/tu/lui) → el pronombre es obligatorio."},
  ]},

 'par_vedere_vendere': {
  'etiqueta': 'Par engañoso vedere / vendere (una letra cambia el sentido)',
  'drills': [
   {'id':'vedven_1','tipo':'scelta',
    'q':"«L'ho riconosciuto ___ la sua faccia in TV.» (viéndola)",
    'op':['vedendo','vendendo','vededo'],'c':0,
    'explica':"vedere → VEDENDO (viendo). vendendo = vendiendo: una sola letra cambia todo."},
   {'id':'vedven_2','tipo':'scrivi',
    'q':"Traduci: «Está ganando dinero vendiendo su coche.»",
    'soluzione':'sta guadagnando soldi vendendo la sua macchina',
    'accettate':['sta guadagnando dei soldi vendendo la sua macchina','sta guadagnando soldi vendendo la macchina',
                 "sta guadagnando soldi vendendo la sua auto"],
    'explica':"vendere → vendendo. Compáralo con vedere → vedendo (ver)."},
   {'id':'vedven_3','tipo':'scrivi',
    'q':"Completa con il gerundio di VEDERE: «___ che pioveva, ho preso l'ombrello.»",
    'soluzione':'vedendo','accettate':[],
    'explica':"vedendo = viendo. Si escribes «vendendo» dices «vendiendo»."},
  ]},

 'gerundio_non_relativo': {
  'etiqueta': 'El gerundio no sirve de relativo de sujeto (che porta, no «portando»)',
  'drills': [
   {'id':'gernr_1','tipo':'scelta',
    'q':"«Ho visto un uomo ___ i bagagli in albergo.» (un hombre que llevaba las maletas)",
    'op':['che portava','portando','a portare'],'c':0,
    'explica':"En español «llevando» puede describir al hombre; en italiano NO. Para describir un sustantivo se usa CHE + verbo."},
   {'id':'gernr_2','tipo':'scrivi',
    'q':"Correggi: «C'è una ragazza aspettandoti fuori.»",
    'soluzione':"c'è una ragazza che ti aspetta fuori",'accettate':["c'è una ragazza che ti sta aspettando fuori"],
    'explica':"El gerundio no puede ser relativo de sujeto: che ti aspetta."},
   {'id':'gernr_3','tipo':'scelta',
    'q':"Quale è corretta?",
    'op':['Le persone che arrivano tardi non entrano','Le persone arrivando tardi non entrano','Le persone arrivate tardi non entrano'],'c':0,
    'explica':"Con CHE + presente. (La 3ª existe pero cambia el sentido: «las llegadas tarde», ya sucedido.)"},
  ]},

 'verbi_supporto_collocazioni': {
  'etiqueta': 'Collocazioni con verbi de apoyo (fare / prendere / avere / dare)',
  'drills': [
   {'id':'vsupp_1','tipo':'scelta',
    'q':"«Non voglio ___ niente a che fare con questa storia.»",
    'op':['avere','fare','prendere'],'c':0,
    'explica':"AVERE a che fare con = tener que ver con. Es fija: no «essere a che fare»."},
   {'id':'vsupp_2','tipo':'scrivi',
    'q':"Completa: «Prima di decidere voglio ___ una domanda al capo.»",
    'soluzione':'fare','accettate':[],
    'explica':"FARE una domanda = hacer una pregunta (no «chiedere una domanda»)."},
   {'id':'vsupp_3','tipo':'scrivi',
    'q':"Traduci: «Tomé una decisión difícil.»",
    'soluzione':'ho preso una decisione difficile','accettate':['ho preso una difficile decisione'],
    'explica':"PRENDERE una decisione. El verbo de apoyo cambia según el sustantivo: fare/prendere/avere/dare."},
   {'id':'vsupp_4','tipo':'scelta',
    'q':"«Mi ___ una mano con questi scatoloni?»",
    'op':['dai','fai','prendi'],'c':0,
    'explica':"DARE una mano = echar una mano."},
  ]},

 'calco_vale_la_pena': {
  'etiqueta': '(ne) vale la pena — sin el «lo» del español',
  'drills': [
   {'id':'valpena_1','tipo':'scelta',
    'q':"«È un film lungo, ma ___ vale la pena.»",
    'op':['ne','lo','si'],'c':0,
    'explica':"⚠️ Calco del español: «lo vale» → en italiano NE vale la pena (ne = de eso)."},
   {'id':'valpena_2','tipo':'scrivi',
    'q':"Traduci: «El viaje es caro, pero vale la pena.»",
    'soluzione':'il viaggio è caro, ma ne vale la pena','accettate':['il viaggio è caro però ne vale la pena',
                 'il viaggio costa caro, ma ne vale la pena'],
    'explica':"NE vale la pena. Nunca «lo vale la pena»."},
   {'id':'valpena_3','tipo':'scrivi',
    'q':"Completa: «Studiare tanto stanca, ma alla fine ___ vale la pena.»",
    'soluzione':'ne','accettate':[],
    'explica':"El pronombre ne sustituye «di questo/di ciò»."},
  ]},

 'consecutio_scala': {
  'etiqueta': 'La escalera del pasado: pensavo/credevo che → imperfetto o trapassato',
  'drills': [
   {'id':'escala_1','tipo':'scrivi',
    'q':"Completa: «Credevo che tu ___ già a casa.» (essere, en ese momento)",
    'soluzione':'fossi','accettate':[],
    'explica':"Verbo principal en pasado + congiuntivo → IMPERFETTO (fossi) si es simultáneo."},
   {'id':'escala_2','tipo':'scelta',
    'q':"«Pensavo che voi ___ il treno.» (que ya lo habíais perdido, ANTES)",
    'op':['aveste perso','perdeste','avete perso'],'c':0,
    'explica':"Si la acción es ANTERIOR a la principal en pasado → congiuntivo TRAPASSATO (aveste perso)."},
   {'id':'escala_3','tipo':'scrivi',
    'q':"Traduci: «Creía que ellos venían con nosotros.»",
    'soluzione':'credevo che loro venissero con noi','accettate':['credevo che venissero con noi'],
    'explica':"credevo (pasado) → venissero (cong. imperfetto). La escalera baja un escalón."},
  ]},

 'concordanza_numero': {
  'etiqueta': 'Concordancia de número (più grande, il migliore ristorante)',
  'drills': [
   {'id':'concnum_1','tipo':'scelta',
    'q':"«Questi sono i problemi ___ del progetto.»",
    'op':['principali','principale','principali i'],'c':0,
    'explica':"problemi (pl.) → principali. Los adjetivos en -e hacen el plural en -i."},
   {'id':'concnum_2','tipo':'scrivi',
    'q':"Completa: «Sono le ___ pizzerie della città.» (migliore)",
    'soluzione':'migliori','accettate':[],
    'explica':"migliore → migliori en plural, aunque el español diga «mejores» igual en ambos géneros."},
   {'id':'concnum_3','tipo':'scrivi',
    'q':"Traduci: «Son las ciudades más grandes del país.»",
    'soluzione':'sono le città più grandi del paese','accettate':['sono le più grandi città del paese'],
    'explica':"grandi (pl.), no «grande». «città» es invariable, pero el adjetivo NO."},
  ]},
}

d = json.load(io.open(P, encoding='utf-8'))
d.setdefault('rasgos', {})
nuevos = añadidos = 0
for k, v in NUEVOS.items():
    r = d['rasgos'].setdefault(k, {'etiqueta': v['etiqueta'], 'drills': []})
    r.setdefault('etiqueta', v['etiqueta'])
    r.setdefault('drills', [])
    tiene = set(x['id'] for x in r['drills'])
    if not r['drills']:
        nuevos += 1
    for dr in v['drills']:
        if dr['id'] in tiene:
            continue
        r['drills'].append(dr)
        añadidos += 1

tmp = P + '.tmp'
json.dump(d, io.open(tmp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
os.replace(tmp, P)
tot = sum(len(r.get('drills') or []) for r in d['rasgos'].values())
print('rasgos que pasan de 0 a tener drills: %d' % nuevos)
print('drills añadidos: %d' % añadidos)
print('TOTAL drills ahora: %d (antes 38)' % tot)
