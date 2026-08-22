/* ====== Respuestas que se guardan solas (sin botones) ======
   Cada <textarea class="resp" data-ej="..."> se auto-guarda en el servidor
   (datos/respuestas.json). Si no hay servidor (file://), cae a localStorage. */
(function(){
  var m=(location.pathname.match(/dia(\d+)/)||[])[1];
  if(!m)return;
  var dia=m;
  /* ================= VOCABULARIO ★ EN LOS EJERCICIOS DEL DÍA =================
     Antes: 2 ejercicios y elección aleatoria SIN memoria → con 69 palabras unas salían cinco veces
     y otras nunca. Ahora: 3 ejercicios integrados en la lista y rotación por MENOS USADAS, con una
     plaza reservada a algo que estés fallando en Práctica. */

  // Qué gramática exige cada día (temario de index.html). `t` = lo que deben cumplir los verbos.
  var GRAM={
    1:{t:'passato prossimo o imperfetto'}, 3:{t:'futuro semplice o condizionale'},
    4:{t:'un verbo modale (dovere/potere/volere) o l\'imperativo'}, 5:{t:'un pronome diretto o indiretto'},
    6:{t:'un verbo pronominale o un comparativo'}, 7:{t:'congiuntivo presente'},
    9:{t:'congiuntivo passato o trapassato'}, 10:{t:'un periodo ipotetico'},
    11:{t:'la forma passiva'}, 12:{t:'il discorso indiretto'},
    13:{t:'il gerundio o il participio'}, 14:{t:'una preposizione o un connettivo'},
    16:{t:'congiuntivo in frase indipendente'}, 17:{t:'un pronome relativo'},
    18:{t:'una collocazione (fare/prendere/avere + sostantivo)'}, 19:{t:'un registro formale'},
    20:{t:'un\'espressione idiomatica'}, 23:{t:'un pronome combinato (glielo, me lo…)'},
    24:{t:'condizionale composto'}, 25:{t:'futuro anteriore'},
    26:{t:'un causativo (fare/lasciare + infinito)'}, 27:{t:'la concordanza dei tempi'},
    28:{t:'il passato remoto'}, 29:{t:'un alterato (-ino / -one / -accio)'}
  };
  // Días sin foco verbal propio (fonética, oído, repasos): reciclan un tiempo ya visto.
  var RECICLA={2:1, 8:7, 15:10, 21:13, 22:16, 30:9};
  function gramDia(){
    var n=parseInt(dia,10)||0;
    var g=GRAM[n]||GRAM[RECICLA[n]];
    return g?g.t:'el tiempo que quieras (repaso libre)';
  }

  // ---- lectura del vocabulario con sus metadatos ----
  function vocabFull(){
    var l;try{l=JSON.parse(localStorage.getItem('italiano-vocab-activo')||'[]')}catch(e){l=[]}
    var pool=l.filter(function(w){return w&&w.it&&w.estado!=='dominada'});
    if(!pool.length)pool=l.filter(function(w){return w&&w.it});
    return pool;
  }
  function normP(s){return (s||'').toLowerCase().replace(/[«»"“”.,;:!¿?()…]/g,'').replace(/[’]/g,"'").trim();}
  // Palabras que estás fallando en Práctica: el SRS guarda v:<palabra> con lapses/vencimiento.
  function falladas(){
    var st;try{st=JSON.parse(localStorage.getItem('italiano-srs')||'{}')}catch(e){st={}}
    var hoy=new Date();hoy.setHours(0,0,0,0);
    var out={};
    Object.keys(st).forEach(function(k){
      if(k.indexOf('v:')!==0)return;
      var s=st[k]||{};
      if((s.lapses||0)>0||(s.due||0)<=hoy.getTime())out[k.slice(2)]=1;
    });
    return out;
  }
  /* Elige N palabras: las MENOS usadas primero (desempate aleatorio) y, si hay, una plaza para una
     que estés fallando. Devuelve los objetos completos (llevan lema/pos/es para los ejercicios). */
  function elegir(n,excluir){
    var pool=vocabFull().filter(function(w){return (excluir||[]).indexOf(w.it)<0});
    if(!pool.length)return [];
    var fall=falladas(), pick=[];
    var pend=pool.filter(function(w){return fall[normP(w.it)]});
    if(pend.length){                                   // 1 plaza para lo que fallas
      pend.sort(function(a,b){return (a.usos||0)-(b.usos||0)||Math.random()-0.5;});
      pick.push(pend[0]);
    }
    var resto=pool.filter(function(w){return pick.indexOf(w)<0});
    resto.sort(function(a,b){return (a.usos||0)-(b.usos||0)||Math.random()-0.5;});
    return pick.concat(resto).slice(0,n);
  }
  // Suma 1 al contador de cada palabra usada. Vive DENTRO de italiano-vocab-activo, que sí
  // sincroniza entre dispositivos (la clave por día, no).
  function marcarUso(nombres){
    var l;try{l=JSON.parse(localStorage.getItem('italiano-vocab-activo')||'[]')}catch(e){return}
    var tocado=false;
    nombres.forEach(function(it){
      var w=l.filter(function(x){return normP(x.it)===normP(it)})[0];
      if(w){w.usos=(w.usos||0)+1;tocado=true;}
    });
    if(tocado)localStorage.setItem('italiano-vocab-activo',JSON.stringify(l));
  }
  /* Selección FIJA por día (no baila al recargar). Guarda solo los nombres; al fijarla por primera
     vez incrementa el contador de usos. */
  function seleccionDia(clave,n,excluir){
    var KEY='italiano-'+clave+'-'+dia;
    var pool=vocabFull().map(function(w){return w.it});
    var s=null;try{s=JSON.parse(localStorage.getItem(KEY)||'null')}catch(e){}
    if(s&&s.length)s=s.filter(function(w){return pool.indexOf(w)>-1});   // quita las que borraste
    if(!s||!s.length){
      s=elegir(n,excluir).map(function(w){return w.it});
      if(s.length){localStorage.setItem(KEY,JSON.stringify(s));marcarUso(s);}
    }
    return s||[];
  }
  function objetoDe(it){return vocabFull().filter(function(w){return normP(w.it)===normP(it)})[0]||null;}
  function rotar(clave,n,excluir){
    var KEY='italiano-'+clave+'-'+dia;
    var s=elegir(n,excluir).map(function(w){return w.it});
    if(s.length){localStorage.setItem(KEY,JSON.stringify(s));marcarUso(s);}
    return s;
  }

  // ---- A) el ejercicio que ya existe en el HTML: marcador .mis-palabras ----
  (function fillVocab(){
    var els=document.querySelectorAll('.mis-palabras'); if(!els.length)return;
    var KEY='italiano-mispalabras-'+dia;
    function vocab(){return vocabFull().map(function(w){return w.it});}
    function pickNew(){return rotar('mispalabras',3,[]);}
    function resolve(){return seleccionDia('mispalabras',3,[]);}
    function paint(pick){
      els.forEach(function(e){
        if(!pick.length){e.textContent='(agrega palabras en tu Vocabulario ★)';return;}
        e.textContent=pick.join(', ');
        var nx=e.nextSibling;
        if(!nx||!nx.classList||!nx.classList.contains('mp-otras')){
          var a=document.createElement('a');a.className='mp-otras';a.href='#';a.textContent=' 🔄 otras';
          a.style.cssText='font-size:.72rem;color:#2d6a4f;text-decoration:none;margin-left:.3rem;white-space:nowrap';
          a.onclick=function(ev){ev.preventDefault();var np=pickNew();localStorage.setItem(KEY,JSON.stringify(np));paint(np);};
          e.parentNode.insertBefore(a,e.nextSibling);
        }
      });
    }
    paint(resolve());
  })();

  /* B y C) dos ejercicios NUEVOS con tu vocabulario, INTERCALADOS dentro de la lista de los 15
     (no al final): así se sienten parte del día y no un bloque pegado. Aplican la gramática del día.
     El bloque creativo anterior (evocab) se retira: sus respuestas ya escritas siguen guardadas en
     respuestas.json, solo deja de mostrarse. */
  (function addVocabEjercicios(){
    var ols=document.querySelectorAll('ol.ejercicio'); if(!ols.length)return;
    var ol=ols[ols.length-1];
    if(document.getElementById('ej-voc-conj'))return;
    var yaUsadas=[];try{yaUsadas=JSON.parse(localStorage.getItem('italiano-mispalabras-'+dia)||'[]')}catch(e){}

    function caja(id,ej,rows){
      var li=document.createElement('li');li.id=id;
      var prompt=document.createElement('div');
      var ta=document.createElement('textarea');ta.className='resp';ta.setAttribute('data-ej',ej);ta.rows=rows;ta.placeholder='…';
      var hidden=document.createElement('textarea');hidden.className='resp';hidden.setAttribute('data-ej',ej+'_q');
      hidden.style.display='none';hidden.readOnly=true;    // guarda la consigna, para corregir sabiendo qué se pidió
      li.appendChild(prompt);li.appendChild(ta);li.appendChild(hidden);
      return {li:li,prompt:prompt,hidden:hidden};
    }
    // insertar a ~1/3 y ~2/3 de la lista para que queden repartidos entre los ejercicios del día
    function insertar(li,fraccion){
      var items=ol.children, pos=Math.max(1,Math.round(items.length*fraccion));
      if(pos>=items.length)ol.appendChild(li); else ol.insertBefore(li,items[pos]);
    }
    function link(el,fn){
      var a=document.createElement('a');a.href='#';a.textContent=' 🔄 otra';
      a.style.cssText='font-size:.72rem;color:#2d6a4f;text-decoration:none;margin-left:.3rem;white-space:nowrap';
      a.onclick=function(ev){ev.preventDefault();fn();};
      el.appendChild(a);
    }

    // --- B) Conjuga TU verbo con el tiempo del día ---
    var B=caja('ej-voc-conj','evoc_conj',3);
    insertar(B.li,0.34);
    function pintaConj(){
      var verbos=vocabFull().filter(function(w){return w.pos==='verbo'&&w.lema;});
      if(!verbos.length){B.prompt.innerHTML='<strong>🔧 Tu verbo:</strong> aún no tienes verbos en tu Vocabulario ★.';B.hidden.value='';return;}
      var nombre=seleccionDia('vocconj',1,yaUsadas)[0];
      var w=nombre?objetoDe(nombre):null;
      if(!w||w.pos!=='verbo'||!w.lema){                       // la elección del día no era verbo: se busca uno
        w=elegir(9,yaUsadas).filter(function(x){return x.pos==='verbo'&&x.lema;})[0]||verbos[0];
        localStorage.setItem('italiano-vocconj-'+dia,JSON.stringify([w.it]));marcarUso([w.it]);
      }
      // OJO: se da el infinitivo (es la consigna) pero NUNCA el auxiliar ni el participio: eso es la respuesta.
      var q='Coniuga <b>«'+w.lema+'»</b> ('+(w.lemaEs||w.es||'')+') usando <b>'+gramDia()+'</b> y escribe una frase tuya con esa forma.';
      B.prompt.innerHTML='<strong>🔧 Tu verbo del día:</strong> '+q;
      B.hidden.value=q.replace(/<[^>]+>/g,'');
      link(B.prompt,function(){rotar('vocconj',1,yaUsadas);pintaConj();});
    }
    pintaConj();

    // --- C) Dilo en italiano (producción ES→IT) ---
    var C=caja('ej-voc-prod','evoc_prod',3);
    insertar(C.li,0.7);
    var SIT=['algo que te pasó esta semana','un plan con un amigo','algo del trabajo',
             'una escena de una canción que escuchaste','algo que te dio risa',
             'un recuerdo de tu infancia','algo que quieres cambiar','una comida que probaste'];
    function pintaProd(){
      var excl=yaUsadas.concat(JSON.parse(localStorage.getItem('italiano-vocconj-'+dia)||'[]'));
      var nombre=seleccionDia('vocprod',1,excl)[0];
      var w=nombre?objetoDe(nombre):null;
      if(!w){C.prompt.innerHTML='<strong>🇪🇸→🇮🇹 Dilo en italiano:</strong> aún no tienes palabras en tu Vocabulario ★.';C.hidden.value='';return;}
      var sit=SIT[((parseInt(dia,10)||0)+(w.it.length))%SIT.length];
      var q='Cuéntalo en italiano usando <b>«'+w.it+'»</b> ('+(w.es||w.lemaEs||'')+') con <b>'+gramDia()+'</b> — sobre '+sit+'.';
      C.prompt.innerHTML='<strong>🇪🇸→🇮🇹 Dilo en italiano:</strong> '+q;
      C.hidden.value=q.replace(/<[^>]+>/g,'');
      link(C.prompt,function(){rotar('vocprod',1,excl);pintaProd();});
    }
    pintaProd();
  })();

  function fields(){return [].slice.call(document.querySelectorAll('.resp'));}
  if(!fields().length)return;

  var badge=document.createElement('div');
  badge.className='cb-save'; badge.textContent='';
  function status(t){badge.textContent=t;}

  function gather(){var o={};fields().forEach(function(f){o[f.getAttribute('data-ej')]=f.value;});return o;}
  function fill(d){fields().forEach(function(f){var k=f.getAttribute('data-ej');if(d&&d[k]!=null)f.value=d[k];});}

  // ---- ¿hay servidor? Si NO, las respuestas solo quedan en este navegador (NO en respuestas.json).
  //      Avisamos bien visible para que el usuario tenga certeza de que se está guardando en el curso. ----
  var aviso=document.createElement('div');
  aviso.className='cb-noserver';
  aviso.style.cssText='display:none;position:sticky;top:0;z-index:9999;background:#c0392b;color:#fff;'+
    'padding:.55rem 1rem;font:600 .84rem/1.35 sans-serif;text-align:center';
  aviso.innerHTML='⚠️ <b>Sin servidor:</b> tus respuestas NO se están guardando en el curso, solo en este navegador. '+
    'Cierra y abre el curso con <b>«Abrir Curso Italiano.bat»</b> para que se guarden en respuestas.json.';
  // Solo esperamos un servidor local en localhost (ahí lo levanta el .bat). En un host remoto
  // (GitHub Pages) NO hay servidor por diseño → nunca mostramos el aviso rojo de "sin servidor".
  var esLocal=/^(localhost|127\.0\.0\.1|0\.0\.0\.0|\[::1\])$/.test(location.hostname)||location.protocol==='file:';
  function setServer(ok){ aviso.style.display=(ok||!esLocal)?'none':'block'; }

  // cargar lo guardado (y de paso detectar si el servidor responde)
  function loadLocal(){try{return JSON.parse(localStorage.getItem('resp-'+dia)||'{}')}catch(e){return {}}}
  // Combina servidor + navegador: para cada recuadro usa el valor del SERVIDOR si no está vacío;
  // si el servidor no tiene ese día (o ese recuadro), usa lo que quedó en ESTE navegador (localStorage).
  // Así, respuestas viejas que solo se guardaron en el navegador (días previos al guardado al servidor)
  // vuelven a verse. 'recovered' = usamos algo del navegador que el servidor no tenía.
  function mergeSaved(srv,loc){
    var o={}, recovered=false;
    fields().forEach(function(f){
      var k=f.getAttribute('data-ej');
      var s=(srv&&srv[k]!=null)?srv[k]:'', l=(loc&&loc[k]!=null)?loc[k]:'';
      if(s&&s.trim()){o[k]=s;}
      else if(l&&l.trim()){o[k]=l;recovered=true;}
      else{o[k]=s||l||'';}
    });
    return {answers:o,recovered:recovered};
  }
  // usarNube = en la WEB (no localhost) con Firebase → respuestas y correcciones en Firestore.
  //            en localhost sigue el servidor local (.bat) como siempre.
  var usarNube = !esLocal && window.FB;
  function cargarLocal(){
    fetch('/api/respuestas').then(function(r){
      if(!r.ok)throw new Error('http '+r.status);
      return r.json();
    }).then(function(all){
      setServer(true);
      var m=mergeSaved(all[dia]||{}, loadLocal());
      fill(m.answers);
      if(m.recovered){
        fetch('/api/respuestas',{method:'POST',headers:{'Content-Type':'application/json'},
          body:JSON.stringify({dia:dia,answers:m.answers})}).catch(function(){});
      }
    }).catch(function(){ setServer(false); fill(loadLocal()); });
  }
  function cargarNube(){
    FB.doc('respuestas',dia).get().then(function(d){ fill(d.exists?d.data():loadLocal()); })
      .catch(function(){ fill(loadLocal()); });
  }
  if(usarNube){ FB.loginGate(function(){ cargarNube(); cargarCorreccion(); }); }
  else { cargarLocal(); cargarCorreccion(); }

  var t, dirty=false;   // dirty=true solo cuando el usuario ESCRIBE algo (evita guardar recuadros vacíos al abrir/cerrar)
  function doSave(){
    var o=gather();
    try{localStorage.setItem('resp-'+dia,JSON.stringify(o))}catch(e){}
    if(window.marcaActividad)window.marcaActividad(); // contar el día para la racha
    status('guardando…');
    if(usarNube && FB.user()){
      FB.doc('respuestas',dia).set(o)
        .then(function(){badge.classList.remove('cb-fail');status('✓ guardado en la nube');})
        .catch(function(){badge.classList.add('cb-fail');status('⚠ error al guardar');});
    } else {
      fetch('/api/respuestas',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({dia:dia,answers:o})})
        .then(function(r){
          if(!r.ok)throw new Error('http '+r.status);
          setServer(true);badge.classList.remove('cb-fail');status('✓ guardado en el curso');
        })
        .catch(function(){
          setServer(false);badge.classList.add('cb-fail');status('⚠ NO guardado en el curso (solo local)');
        });
    }
    setTimeout(function(){if(badge.textContent.indexOf('✓')===0)status('')},2500);
  }
  document.addEventListener('input',function(e){
    if(e.target&&e.target.classList&&e.target.classList.contains('resp')){
      dirty=true;   // el usuario escribió → ya hay algo que guardar
      status('…');clearTimeout(t);t=setTimeout(doSave,800);
    }
  });

  // Garantía extra: si cierras o cambias de pestaña justo después de escribir (antes del auto-guardado
  // de 0,8 s), manda las respuestas al servidor con sendBeacon para que no se pierda el último cambio.
  // IMPORTANTE: solo si dirty=true (escribiste algo). Si solo abriste y cerraste el día, NO guarda nada
  // (así no se crean recuadros vacíos ni se sobrescriben respuestas reales por una carrera al cargar).
  function flush(){
    if(!dirty)return;
    try{
      var o=gather();
      localStorage.setItem('resp-'+dia,JSON.stringify(o));
      if(navigator.sendBeacon){
        navigator.sendBeacon('/api/respuestas',
          new Blob([JSON.stringify({dia:dia,answers:o})],{type:'application/json'}));
      }
    }catch(e){}
  }
  document.addEventListener('visibilitychange',function(){if(document.visibilityState==='hidden')flush();});
  window.addEventListener('pagehide',flush);

  function mount(){
    if(!aviso.parentNode)document.body.insertBefore(aviso,document.body.firstChild);
    if(!badge.parentNode)document.body.appendChild(badge);
  }
  if(document.body)mount();
  else document.addEventListener('DOMContentLoaded',mount);

  // ===== MODO REPASO: si YA corregí este día, pintar la corrección dentro del HTML =====
  // Lee datos/errores.json["NN"] y muestra: (1) un panel plegable con tus errores en color
  // (rojo=real, ámbar=descuido, azul=matiz), tus aciertos y qué reforzar; (2) si un error trae
  // su "ej", una caja pegada JUSTO debajo de ese ejercicio.
  function esc(s){return (s==null?'':''+s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
  function ejLabel(ej){if(!ej)return '';
    if(/^e\d+$/.test(ej))return 'Ejercicio '+ej.slice(1);
    if(/^x\d+$/.test(ej))return 'Examen '+ej.slice(1);
    if(ej==='dettato')return 'Dictado';
    if(ej==='evocab')return 'Vocabulario extra';
    return ej;}
  function renderCorreccion(c){
    if(!c||document.getElementById('corr-final'))return;
    var errs=(c.errores||[]);

    function itemHTML(e){
      var chip=e.ej?' <span class="ej-chip">'+esc(ejLabel(e.ej))+'</span>':'';
      var esMatiz=e.severidad==='matiz';
      return '<div class="corr-item '+(e.severidad||'')+'">'+
        '<span class="tema">'+esc(e.tema||'')+chip+'</span>'+
        (e.tuvo?'<div>Escribiste: <span class="corr-tuvo">'+esc(e.tuvo)+'</span></div>':'')+
        (e.correcto?'<div>'+(esMatiz?'Mejor':'Correcto')+': <span class="corr-ok">'+esc(e.correcto)+'</span></div>':'')+
        (e.nota?'<div class="cnota">'+esc(e.nota)+'</div>':'')+'</div>';
    }

    // ---- (1) cada error va en una caja de color JUSTO debajo de SU ejercicio (data-ej).
    //          Es el modo de estudio principal: ves el fallo pegado al recuadro donde ocurrió.
    //          Los errores que no anclan a ningún ejercicio se acumulan para el resumen final.
    var sinEj=[];
    errs.forEach(function(e){
      var ta=e.ej?document.querySelector('.resp[data-ej="'+e.ej+'"]'):null;
      if(!ta){sinEj.push(e);return;}
      var box=document.createElement('div');box.className='corr-inline '+(e.severidad||'');
      var esMatiz=e.severidad==='matiz';
      var etq=esMatiz?'💡 Matiz':(e.severidad==='descuido'?'🟡 Descuido':'❌ Corrección');
      box.innerHTML='<span class="tag">'+etq+'</span> '+
        (e.tuvo?'Escribiste <span class="corr-tuvo">'+esc(e.tuvo)+'</span> ':'')+
        (e.correcto?'→ '+(esMatiz?'mejor ':'')+'<span class="corr-ok">'+esc(e.correcto)+'</span>':'')+
        (e.nota?'<div class="cnota" style="margin-top:.2rem">'+esc(e.nota)+'</div>':'');
      ta.parentNode.insertBefore(box,ta.nextSibling);
    });

    // ---- (2) resumen al FINAL del día: SOLO lo que no tiene un ejercicio donde vivir
    //          (errores generales sin "ej", lo que hiciste bien y lo que hay que reforzar).
    //          Ya no hay lista de errores arriba: cada error está junto a su ejercicio.
    var reales=errs.filter(function(e){return e.severidad!=='matiz'});
    var sinReales=sinEj.filter(function(e){return e.severidad!=='matiz'});
    var sinMatices=sinEj.filter(function(e){return e.severidad==='matiz'});
    var body='';
    if(sinReales.length){body+='<h4>❌ A corregir (general)</h4>';sinReales.forEach(function(e){body+=itemHTML(e);});}
    if(sinMatices.length){body+='<h4>💡 Matices (general)</h4>';sinMatices.forEach(function(e){body+=itemHTML(e);});}
    if((c.aciertos||[]).length){body+='<h4>✅ Lo que hiciste bien</h4><ul>'+c.aciertos.map(function(a){return '<li>'+esc(a)+'</li>'}).join('')+'</ul>';}
    if((c.a_reforzar||[]).length){body+='<h4>🔁 A reforzar</h4><ul>'+c.a_reforzar.map(function(a){return '<li>'+esc(a)+'</li>'}).join('')+'</ul>';}
    if(!body)return;   // todo se resolvió inline: no hace falta bloque resumen
    var inline=errs.length-sinEj.length;
    var p=document.createElement('div');p.className='corr-panel corr-final';p.id='corr-final';
    p.innerHTML='<div class="corr-head">📋 Resumen de tu corrección <span class="sub">— revisada el '+esc(c.fecha||'')+' · '+
      reales.length+' a corregir'+(inline?' · '+inline+' marcados en su ejercicio ↑':'')+' · '+(c.aciertos||[]).length+' aciertos</span></div>'+
      '<div class="corr-body">'+body+'</div>';
    document.body.appendChild(p);
  }
  // Carga la corrección del día: de Firestore (web) o del servidor local (datos/errores/NN.json).
  function cargarCorreccion(){
    function pintar(c){ if(c&&((c.errores&&c.errores.length)||(c.aciertos&&c.aciertos.length)))renderCorreccion(c); }
    if(usarNube){
      FB.doc('errores',dia).get().then(function(d){ pintar(d.exists?d.data():null); }).catch(function(){});
    } else {
      fetch('/api/errores?dia='+dia).then(function(r){return r.json()}).then(pintar).catch(function(){});
    }
  }
})();
