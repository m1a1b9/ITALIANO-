/* ====== Respuestas que se guardan solas (sin botones) ======
   Cada <textarea class="resp" data-ej="..."> se auto-guarda en el servidor
   (datos/respuestas.json). Si no hay servidor (file://), cae a localStorage. */
(function(){
  var m=(location.pathname.match(/dia(\d+)/)||[])[1];
  if(!m)return;
  var dia=m;
  // Inyecta tus palabras del Vocabulario ★ en los ejercicios marcados con .mis-palabras.
  // FIJAS por día: se eligen una vez y se guardan (italiano-mispalabras-NN); cada F5 reutiliza
  // las mismas para que no se muevan mientras trabajas. El enlace "🔄 otras" las rota a propósito.
  (function fillVocab(){
    var els=document.querySelectorAll('.mis-palabras'); if(!els.length)return;
    var KEY='italiano-mispalabras-'+dia;
    function vocab(){var l;try{l=JSON.parse(localStorage.getItem('italiano-vocab-activo')||'[]')}catch(e){l=[]}
      var pool=l.filter(function(w){return w&&w.it&&w.estado!=='dominada'});
      if(!pool.length)pool=l.filter(function(w){return w&&w.it});
      return pool.map(function(w){return w.it});}
    function pickNew(){var p=vocab();p.sort(function(){return Math.random()-0.5});return p.slice(0,3);}
    function saved(){try{return JSON.parse(localStorage.getItem(KEY)||'null')}catch(e){return null}}
    function resolve(){
      var pool=vocab(), s=saved();
      if(s&&s.length)s=s.filter(function(w){return pool.indexOf(w)>-1}); // descarta las que ya borraste
      if(!s||!s.length)s=pickNew();
      localStorage.setItem(KEY,JSON.stringify(s));
      return s;
    }
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

  // Ejercicio EXTRA de vocabulario activo (creativo, rota por día). Se inyecta al final de la
  // lista de ejercicios de CADA día (así sale también en días futuros sin editarlos). Palabras
  // fijas por día (italiano-vocabex-NN); "🔄 otras" las rota. Guarda la consigna (evocab_q) para
  // que la corrección sepa qué se pidió. Complementa (no reemplaza) el «escribe una frase» (.mis-palabras).
  (function addVocabExtra(){
    var ols=document.querySelectorAll('ol.ejercicio'); if(!ols.length)return;
    var ol=ols[ols.length-1];
    if(document.getElementById('ej-vocabex'))return;
    var KEY='italiano-vocabex-'+dia;
    var TPL=[
      {n:2,t:'🎬 Inventa il titolo di un film e la sua trama in 2 righe, usando {W}.'},
      {n:2,t:'💬 Scrivi un mini-dialogo (3-4 battute) tra due amici che contenga {W}.'},
      {n:3,t:'📅 Racconta cosa hai fatto ieri (3-4 righe) infilando {W}.'},
      {n:3,t:'❓ Scrivi 3 domande (una con ciascuna parola) usando {W}.'},
      {n:3,t:'🔗 Collega TUTTE queste parole in UNA sola frase con senso: {W}.'},
      {n:2,t:'😱 Inventa una scusa assurda per un ritardo, usando {W}.'},
      {n:2,t:'📱 Scrivi la caption che metteresti su Instagram con {W}.'},
      {n:2,t:'⭐ Consiglia a un amico un posto, un film o un piatto usando {W}.'}
    ];
    var tpl=TPL[(parseInt(dia,10)||0)%TPL.length];
    function activePool(){var l;try{l=JSON.parse(localStorage.getItem('italiano-vocab-activo')||'[]')}catch(e){l=[]}
      return l.filter(function(w){return w&&w.it&&w.estado!=='dominada'}).map(function(w){return w.it});}
    function usedByMis(){try{return JSON.parse(localStorage.getItem('italiano-mispalabras-'+dia)||'[]')}catch(e){return[]}}
    function pickWords(){
      var pool=activePool(), used=usedByMis();
      var pref=pool.filter(function(w){return used.indexOf(w)<0});
      var base=(pref.length>=tpl.n?pref:pool).slice();
      base.sort(function(){return Math.random()-0.5});
      return base.slice(0,tpl.n);
    }
    function savedW(){try{return JSON.parse(localStorage.getItem(KEY)||'null')}catch(e){return null}}
    function resolveW(){
      var pool=activePool(), s=savedW();
      if(s&&s.length)s=s.filter(function(w){return pool.indexOf(w)>-1});
      if(!s||!s.length)s=pickWords();
      localStorage.setItem(KEY,JSON.stringify(s));
      return s;
    }
    var li=document.createElement('li');li.id='ej-vocabex';
    var prompt=document.createElement('div');
    var ta=document.createElement('textarea');ta.className='resp';ta.setAttribute('data-ej','evocab');ta.rows=3;ta.placeholder='La tua risposta creativa…';
    var hidden=document.createElement('textarea');hidden.className='resp';hidden.setAttribute('data-ej','evocab_q');hidden.style.display='none';hidden.readOnly=true;
    li.appendChild(prompt);li.appendChild(ta);li.appendChild(hidden);
    ol.appendChild(li);
    function render(words){
      if(!words.length){prompt.innerHTML='<strong>✨ Vocabolario extra:</strong> aún no tienes palabras ★ para jugar. Guarda algunas en las lecciones o canciones y aquí te reto a usarlas.';hidden.value='';return;}
      var q=tpl.t.replace('{W}','<b>«'+words.join(', ')+'»</b>');
      prompt.innerHTML='<strong>✨ Vocabolario attivo:</strong> '+q+' <a href="#" class="vx-otras" style="font-size:.72rem;color:#2d6a4f;text-decoration:none;margin-left:.3rem;white-space:nowrap">🔄 otras</a>';
      hidden.value=q.replace(/<[^>]+>/g,'');
      var lnk=prompt.querySelector('.vx-otras');
      if(lnk)lnk.onclick=function(ev){ev.preventDefault();var nw=pickWords();localStorage.setItem(KEY,JSON.stringify(nw));render(nw);};
    }
    render(resolveW());
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
  fetch('/api/respuestas').then(function(r){
    if(!r.ok)throw new Error('http '+r.status);
    return r.json();
  }).then(function(all){
    setServer(true);
    var m=mergeSaved(all[dia]||{}, loadLocal());
    fill(m.answers);
    // si recuperamos respuestas del navegador que el servidor no tenía, las persistimos en respuestas.json
    if(m.recovered){
      fetch('/api/respuestas',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({dia:dia,answers:m.answers})}).catch(function(){});
    }
  }).catch(function(){
    setServer(false);
    fill(loadLocal());
  });

  var t, dirty=false;   // dirty=true solo cuando el usuario ESCRIBE algo (evita guardar recuadros vacíos al abrir/cerrar)
  function doSave(){
    var o=gather();
    try{localStorage.setItem('resp-'+dia,JSON.stringify(o))}catch(e){}
    if(window.marcaActividad)window.marcaActividad(); // contar el día para la racha
    status('guardando…');
    fetch('/api/respuestas',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({dia:dia,answers:o})})
      .then(function(r){
        if(!r.ok)throw new Error('http '+r.status);
        setServer(true);badge.classList.remove('cb-fail');status('✓ guardado en el curso');
      })
      .catch(function(){
        setServer(false);badge.classList.add('cb-fail');status('⚠ NO guardado en el curso (solo local)');
      });
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
  // Pide SOLO la corrección de este día (datos/errores/NN.json) en vez del agregado completo.
  fetch('/api/errores?dia='+dia).then(function(r){return r.json()}).then(function(c){
    if(c&&((c.errores&&c.errores.length)||(c.aciertos&&c.aciertos.length)))renderCorreccion(c);
  }).catch(function(){});

  /* ===== CORREGIR CON IA (Gemini) — SOLO MUESTRA: no guarda, no toca errores.json/SRS/siembra ===== */
  (function(){
    function iaKey(){try{return localStorage.getItem('italiano-gemini-key')||''}catch(e){return ''}}
    function iaSetKey(k){try{localStorage.setItem('italiano-gemini-key',k||'')}catch(e){}}
    function consignaDe(ta){
      var cont=ta.closest('li')||ta.closest('.bloque')||ta.parentElement; if(!cont)return '';
      var cl=cont.cloneNode(true);
      cl.querySelectorAll('textarea,.corr-inline,.ia-inline,a').forEach(function(x){x.remove()});
      return cl.textContent.replace(/\s+/g,' ').trim().slice(0,300);
    }
    function gatherEjercicios(){
      var out=[];
      fields().forEach(function(ta){
        var ej=ta.getAttribute('data-ej'), val=(ta.value||'').trim();
        if(!val||ej==='evocab_q')return;
        out.push({ej:ej,consigna:consignaDe(ta),respuesta:val});
      });
      return out;
    }
    function clearIA(){document.querySelectorAll('.ia-inline').forEach(function(x){x.remove()});}
    function renderIA(items){
      clearIA();var pintados=0;
      items.forEach(function(it){
        var ta=document.querySelector('.resp[data-ej="'+it.ej+'"]');if(!ta)return;pintados++;
        var bien=it.estado==='bien';
        var box=document.createElement('div');box.className='ia-inline '+(bien?'ok':'corr');
        box.innerHTML='<span class="tag">🤖 IA'+(bien?' · bien':'')+'</span> '+esc(it.correccion||(bien?'Correcto 👍':''));
        ta.parentNode.insertBefore(box,ta.nextSibling);
      });
      return pintados;
    }
    function correct(){
      var key=iaKey();if(!key){keyRow.style.display='inline-flex';keyRow.querySelector('input').focus();return;}
      var ex=gatherEjercicios();
      if(!ex.length){alert('Escribe algo en los ejercicios antes de pedir corrección.');return;}
      clearIA();status('🤖 corrigiendo…');btn.disabled=true;
      var prompt='Eres un profesor de italiano corrigiendo a un alumno hispanohablante (nivel A2->B1). '+
        'Para cada ejercicio te doy la consigna y la respuesta del alumno. Corrige SOLO lo que este mal '+
        '(gramatica, auxiliar essere/avere, preposiciones, concordancia, ortografia, lexico); explica breve, '+
        'claro y motivador en espanol, y da la forma correcta. Si esta bien, dilo. '+
        'Responde SOLO con JSON valido: un array de objetos '+
        '{"ej":"<id tal cual>","estado":"bien"|"corregir","correccion":"<texto breve en espanol; vacio si bien>"}.\n'+
        'Ejercicios:\n'+JSON.stringify(ex);
      window.IA.generate(prompt,true).then(function(t){
        var arr;try{arr=JSON.parse(t)}catch(e){arr=null}
        if(!Array.isArray(arr))throw'respuesta no válida de la IA';
        var n=renderIA(arr);status('✓ IA: '+n+' ejercicios');
        setTimeout(function(){if(badge.textContent.indexOf('✓')===0)status('')},3000);
      }).catch(function(e){status('');alert('Error IA: '+(e==='nokey'?'falta la clave':e)+'\n(Cambia la clave o el modelo en Mi Vocabulario → botón «🔑 Clave IA»)');})
        .then(function(){btn.disabled=false;});
    }
    var bar=document.createElement('div');bar.className='ia-corr-bar';
    var btn=document.createElement('button');btn.className='ia-corr-btn';btn.textContent='🤖 Corregir con IA';
    var hint=document.createElement('span');hint.className='ia-corr-hint';hint.textContent='feedback al instante · no se guarda';
    var limpiar=document.createElement('button');limpiar.className='ia-corr-clear';limpiar.textContent='✕ quitar IA';limpiar.onclick=clearIA;
    var keyRow=document.createElement('span');keyRow.className='ia-corr-key';keyRow.style.display='none';
    keyRow.innerHTML='<input type="password" placeholder="pega tu clave de Google AI Studio…"><button class="ia-key-save">Guardar clave</button> <a href="https://aistudio.google.com/apikey" target="_blank" rel="noopener">obtener ↗</a>';
    bar.appendChild(btn);bar.appendChild(hint);bar.appendChild(limpiar);bar.appendChild(keyRow);
    btn.onclick=correct;
    keyRow.querySelector('.ia-key-save').onclick=function(){var k=keyRow.querySelector('input').value.trim();if(k){iaSetKey(k);keyRow.querySelector('input').value='';keyRow.style.display='none';correct();}};
    keyRow.querySelector('input').addEventListener('keydown',function(e){if(e.key==='Enter'){e.preventDefault();keyRow.querySelector('.ia-key-save').click();}});
    var hdr=document.querySelector('.header');
    if(hdr&&hdr.parentNode)hdr.parentNode.insertBefore(bar,hdr.nextSibling);
    else document.body.insertBefore(bar,document.body.firstChild);
  })();
})();
