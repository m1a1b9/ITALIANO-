/* ====== Curso Italiano — audio + glosario por palabra/selección + barra + progreso ====== */
(function(){
  var VOCAB = window.VOCAB || {};

  /* ---------- 1. VOZ ITALIANA (sin archivos) ---------- */
  var itVoice=null, itVoices=[];
  function isItalian(v){return /^it([-_]|$)/i.test(v.lang) && !/pt|por|bra/i.test(v.lang+v.name);}
  function score(v){var n=v.name.toLowerCase();var s=0;
    if(/google/.test(n))s+=5; if(/(elsa|isabella|cosimo|bianca|natural|online)/.test(n))s+=4;
    if(/microsoft/.test(n))s+=2; if(/it-it/i.test(v.lang))s+=1; return s;}
  function pickVoice(){
    var vs=speechSynthesis.getVoices();
    itVoices=vs.filter(isItalian).sort(function(a,b){return score(b)-score(a)});
    var saved=localStorage.getItem('italiano-voz');
    itVoice=(saved&&itVoices.find(function(v){return v.name===saved}))||itVoices[0]||null;
  }
  if('speechSynthesis' in window){pickVoice();speechSynthesis.onvoiceschanged=function(){pickVoice();buildVoiceSelect();};}
  function say(txt,el){
    if(!('speechSynthesis' in window)||!txt)return;
    speechSynthesis.cancel();
    var u=new SpeechSynthesisUtterance(txt);u.lang='it-IT';if(itVoice)u.voice=itVoice;u.rate=.9;
    if(el){el.classList.add('cb-speaking');u.onend=function(){el.classList.remove('cb-speaking')};}
    speechSynthesis.speak(u);
  }
  // Voz italiana para otros módulos (inmersión: velocidad y loop por línea)
  window.italianoSay=function(txt,opts){
    opts=opts||{};
    if(!('speechSynthesis' in window)||!txt)return;
    speechSynthesis.cancel();
    var u=new SpeechSynthesisUtterance(txt);u.lang='it-IT';if(itVoice)u.voice=itVoice;
    u.rate=opts.rate||.9;
    if(opts.onend)u.onend=opts.onend;
    speechSynthesis.speak(u);
  };
  window.italianoStop=function(){if('speechSynthesis' in window)speechSynthesis.cancel();};

  function buildVoiceSelect(){
    var sel=document.getElementById('cb-voice'); if(!sel)return;
    if(!itVoices.length){sel.innerHTML='<option>⚠ sin voz italiana</option>';sel.disabled=true;return;}
    sel.disabled=false;
    sel.innerHTML=itVoices.map(function(v){return '<option value="'+v.name+'"'+(itVoice&&v.name===itVoice.name?' selected':'')+'>🔊 '+v.name.replace(/microsoft|google/i,'').trim()+'</option>'}).join('');
    sel.onchange=function(){itVoice=itVoices.find(function(v){return v.name===sel.value});localStorage.setItem('italiano-voz',sel.value);say('Ciao, sono la tua voce italiana.');};
  }

  /* ---------- 2. AUTO-GLOSADO POR PALABRA ---------- */
  function norm(s){return s.toLowerCase().replace(/[«»"“”.,;:!¿?()…]/g,'').replace(/[’]/g,"'").trim();}
  // Frases compuestas (claves con espacio): tienen prioridad sobre las palabras sueltas
  var phrases=Object.keys(VOCAB).filter(function(k){return k.indexOf(' ')>-1});
  var MAXW=phrases.reduce(function(m,k){return Math.max(m,k.split(' ').length)},1);

  // Caché del "diccionario que se completa solo" (formas + traducciones online ya resueltas)
  var DKEY='italiano-dic-cache', DCACHE={};
  try{DCACHE=JSON.parse(localStorage.getItem(DKEY)||'{}')}catch(e){DCACHE={}}
  function cacheSet(n,es){if(!n||!es)return;DCACHE[n]=es;try{localStorage.setItem(DKEY,JSON.stringify(DCACHE))}catch(e){}}
  // Palabras ya consultadas online que NO tienen traducción (nombres propios, interjecciones…):
  // se recuerdan aparte para no volver a golpear el traductor con la misma palabra en cada carga.
  var NKEY='italiano-notr-cache', NOTR={};
  try{NOTR=JSON.parse(localStorage.getItem(NKEY)||'{}')}catch(e){NOTR={}}
  function notrSet(n){if(!n)return;NOTR[n]=1;try{localStorage.setItem(NKEY,JSON.stringify(NOTR))}catch(e){}}

  // Fallback morfológico: reconocer flexiones (plurales / género) de palabras conocidas
  function morph(n){
    var c=[];
    if(/che$/.test(n))c.push(n.slice(0,-3)+'ca');           // amiche→amica
    if(/chi$/.test(n))c.push(n.slice(0,-3)+'co');           // parchi→parco
    if(/ghi$/.test(n))c.push(n.slice(0,-3)+'go');
    if(/ghe$/.test(n))c.push(n.slice(0,-3)+'ga');
    if(/i$/.test(n))c.push(n.slice(0,-1)+'o',n.slice(0,-1)+'e',n.slice(0,-1)+'a'); // ragazzi→ragazzo, cani→cane
    if(/e$/.test(n))c.push(n.slice(0,-1)+'a',n.slice(0,-1)+'o');                    // case→casa, plural de -a
    for(var i=0;i<c.length;i++){if(VOCAB[c[i]])return VOCAB[c[i]];if(DCACHE[c[i]])return DCACHE[c[i]];}
    return null;
  }

  // Búsqueda local: glosario curado → caché → fallback morfológico
  function localLookup(raw){var n=norm(raw);return VOCAB[n]||DCACHE[n]||morph(n)||null;}
  function lookup(raw){return localLookup(raw);}

  // Traducción en línea (solo para palabras que el usuario selecciona y aún no conocemos)
  function translateOnline(text){
    return fetch('https://translate.googleapis.com/translate_a/single?client=gtx&sl=it&tl=es&dt=t&q='+encodeURIComponent(text))
      .then(function(r){return r.json()})
      .then(function(j){var t=(j&&j[0])?j[0].map(function(x){return x[0]}).join(''):null;
        return (t&&t.toLowerCase()!==text.toLowerCase())?t.trim():null;})
      .catch(function(){return null});
  }

  function makeSpan(cls,es,txt){var s=document.createElement('span');s.className=cls;s.setAttribute('data-es',es);s.textContent=txt;return s;}

  function wrapTextNode(node,pend){
    var text=node.nodeValue;
    if(!/\S/.test(text))return;
    var segs=text.split(/(\s+)/);                 // alterna palabra/espacio
    var frag=document.createDocumentFragment(), changed=false, i=0;
    while(i<segs.length){
      var seg=segs[i];
      if(seg===''){i++;continue;}
      if(/^\s+$/.test(seg)){frag.appendChild(document.createTextNode(seg));i++;continue;}
      // 1) intentar la FRASE más larga que empiece aquí
      var best=null, idx=[], k=i;
      while(k<segs.length){
        if(/\S/.test(segs[k])){
          idx.push(k);
          var joined=idx.map(function(j){return norm(segs[j])}).join(' ');
          var pe=VOCAB[joined]||DCACHE[joined];
          if(idx.length>1 && pe)best={last:k, es:pe, key:joined};
          if(idx.length>=MAXW)break;
        }
        k++;
      }
      if(best){
        var raw=segs.slice(i,best.last+1).join('');
        var sp=makeSpan('gp',best.es,raw);              // frase = un bloque
        var lit=(window.LIT&&window.LIT[best.key])||''; // trampa literal (si la hay)
        if(lit)sp.setAttribute('data-lit',lit);
        frag.appendChild(sp);
        changed=true; i=best.last+1; continue;
      }
      // 2) palabra suelta
      var es=localLookup(seg);
      if(es){frag.appendChild(makeSpan('g',es,seg));changed=true;}
      else{
        var tn=document.createTextNode(seg);
        frag.appendChild(tn);
        // no se conoce todavía: se apunta para traducirla sola en segundo plano (gratis, sin
        // tokens — es una llamada del navegador). Se necesita el nodo YA insertado en el DOM
        // (por eso se fuerza el reemplazo abajo) para poder sustituirlo por su glosa más tarde.
        var n2=norm(seg);
        if(pend&&n2&&/[a-zàèéìòù]/i.test(n2)&&!DCACHE[n2]&&!NOTR[n2]){
          changed=true;
          (pend[n2]=pend[n2]||{raw:seg,nodes:[]}).nodes.push(tn);
        }
      }
      i++;
    }
    if(changed)node.parentNode.replaceChild(frag,node);
  }

  var SKIP={SCRIPT:1,STYLE:1,TH:1,SUMMARY:1,BUTTON:1,A:1};
  function autogloss(root){
    var walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,{acceptNode:function(n){
      var p=n.parentNode;
      while(p&&p!==root){
        if(SKIP[p.nodeName])return NodeFilter.FILTER_REJECT;
        if(p.classList&&(p.classList.contains('cb-bar')||p.classList.contains('g')||p.classList.contains('gp')||p.classList.contains('cb-pop')))return NodeFilter.FILTER_REJECT;
        p=p.parentNode;
      }
      return /\S/.test(n.nodeValue)?NodeFilter.FILTER_ACCEPT:NodeFilter.FILTER_REJECT;
    }});
    var nodes=[],n;while(n=walker.nextNode())nodes.push(n);
    var pend={};                                   // {palabra_normalizada: {raw, nodes:[textNode,…]}}
    nodes.forEach(function(nd){wrapTextNode(nd,pend)});
    resolverPendientes(pend);
  }
  window.italianoGloss = autogloss; // para glosar contenido añadido después (ej. letra de canción en inmersión)

  /* Traduce en segundo plano las palabras que el glosado local no reconoció (no cuesta tokens: es
     una llamada del navegador a Google Translate). Una a la vez, con pausa, para no saturar el
     traductor — mismo patrón que ya usa Mi Vocabulario para su propio relleno en segundo plano.
     Una palabra puede repetirse muchas veces en el mismo texto (una canción, sobre todo): se pide
     la traducción UNA sola vez por palabra y se aplica a TODAS sus apariciones a la vez. */
  function resolverPendientes(pend){
    var claves=Object.keys(pend);
    (function step(i){
      if(i>=claves.length)return;
      var k=claves[i], p=pend[k];
      translateOnline(p.raw).then(function(t){
        if(t){
          cacheSet(k,t);
          p.nodes.forEach(function(tn){
            if(tn.parentNode)tn.parentNode.replaceChild(makeSpan('g',t,tn.nodeValue),tn);
          });
        }else notrSet(k);
      }).then(function(){setTimeout(function(){step(i+1)},180)});
    })(0);
  }

  /* ---------- 3. TRADUCTOR DE SELECCIÓN ---------- */
  var pop=document.createElement('div');pop.className='cb-pop';pop.style.display='none';
  document.addEventListener('DOMContentLoaded',function(){document.body.appendChild(pop)});
  function hidePop(){pop.style.display='none';}
  document.addEventListener('mousedown',function(e){if(!pop.contains(e.target))hidePop();});

  var SENT=window.SENTENCES||{};
  function fullTranslation(raw){
    var n=norm(raw);
    return VOCAB[n]||SENT[n]||DCACHE[n]||null;   // glosario, frase del día o caché
  }
  function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
  // --- Mi Vocabulario Activo (★) ---
  var VKEY='italiano-vocab-activo';
  function loadVocabList(){try{return JSON.parse(localStorage.getItem(VKEY)||'[]')}catch(e){return[]}}
  function saveWord(it,es,ctx){
    it=(it||'').trim(); if(!it)return false;
    var list=loadVocabList();
    if(list.some(function(w){return norm(w.it)===norm(it)}))return 'dup';
    list.push({it:it, es:es||'', ctx:ctx||'', estado:'practica', t:Date.now()});
    localStorage.setItem(VKEY,JSON.stringify(list));
    completarLema(it);          // la palabra base se busca DESPUÉS: guardar debe ser instantáneo
    return true;
  }
  /* Busca la palabra base en segundo plano y la añade a la entrada ya guardada.
     Aquí no se pregunta nada (el globo del ★ es efímero): si hay varias lecturas se marca
     'regla' para que aparezca con el aviso «revisar» en Mi Vocabulario y la elijas allí. */
  function completarLema(it){
    if(!window.LEMA)return;
    LEMA.analizar(it).then(function(ls){
      if(!ls||!ls.length)return;
      var cur=loadVocabList(), f=cur.filter(function(x){return norm(x.it)===norm(it)})[0];
      if(!f||f.lema||f.pos)return;
      var l=ls[0];
      f.lema=l.lema||''; f.pos=l.pos||''; f.flex=l.flex||'';
      f.lemaFuente=(ls.length>1?'regla':(l.fuente||''));
      localStorage.setItem(VKEY,JSON.stringify(cur));
    }).catch(function(){});
  }
  function translateSelection(sel){
    var raw=sel.toString().trim();
    if(!raw||raw.length>200||!/[a-zàèéìòù]/i.test(raw))return null;
    var full=fullTranslation(raw);
    var words=raw.split(/\s+/), parts=[];
    words.forEach(function(w){parts.push({w:w,es:localLookup(w)||'—'});});
    var ctx='';
    try{var n=sel.anchorNode, el=n&&(n.nodeType===3?n.parentElement:n);
      while(el&&el.textContent&&el.textContent.replace(/\s+/g,' ').trim().length<25&&el.parentElement)el=el.parentElement;
      ctx=(el?el.textContent:'').replace(/\s+/g,' ').trim().slice(0,150);
    }catch(e){}
    return {raw:raw, full:full, parts:words.length>1?parts:null, ctx:ctx};
  }
  function renderPop(res){
    var html='<div class="cb-pop-it">'+esc(res.raw)+'</div>';
    if(res.full)html+='<div class="cb-pop-es">🇲🇽 '+esc(res.full)+'</div>';
    else if(res._loading)html+='<div class="cb-pop-es" style="opacity:.6;font-size:.8rem">buscando traducción…</div>';
    else html+='<div class="cb-pop-es" style="opacity:.6;font-size:.8rem">(sin traducción)</div>';
    if(res.parts){html+='<div class="cb-pop-break">';
      res.parts.forEach(function(p){html+='<div class="cb-pop-row"><b>'+esc(p.w)+'</b><span>'+esc(p.es)+'</span></div>';});
      html+='</div>';}
    var esSave=res.full||(res.parts?res.parts.filter(function(p){return p.es!=='—'}).map(function(p){return p.w+' = '+p.es}).join(' · '):'');
    html+='<div class="cb-pop-actions"><button class="cb-pop-say">🔊 oír</button><button class="cb-pop-fav">★ Guardar</button></div>';
    pop.innerHTML=html;
    pop.querySelector('.cb-pop-say').onclick=function(){say(res.raw);};
    pop.querySelector('.cb-pop-fav').onclick=function(){
      var r=saveWord(res.raw, res.full||esSave, res.ctx);
      this.textContent = r==='dup' ? '✓ ya guardada' : (r ? '✓ guardada' : '✕');
      this.disabled=true;
    };
  }
  function enrichPop(res){
    var jobs=[];
    if(!res.full)jobs.push(translateOnline(res.raw).then(function(t){if(t){res.full=t;cacheSet(norm(res.raw),t);}}));
    if(res.parts)res.parts.forEach(function(p){if(p.es==='—')jobs.push(translateOnline(p.w).then(function(t){if(t){p.es=t;cacheSet(norm(p.w),t);}}));});
    if(!jobs.length){res._loading=false;return;}
    Promise.all(jobs).then(function(){res._loading=false;if(pop.style.display!=='none')renderPop(res);});
  }
  function showPop(res,rect){
    res._loading=true; renderPop(res); pop.style.display='block';
    var top=window.scrollY+rect.bottom+8, left=window.scrollX+rect.left;
    pop.style.top=top+'px';pop.style.left=Math.max(8,Math.min(left,window.scrollX+window.innerWidth-pop.offsetWidth-8))+'px';
    enrichPop(res);
  }
  document.addEventListener('mouseup',function(){
    setTimeout(function(){
      var sel=window.getSelection();
      if(!sel||sel.isCollapsed){return;}
      var res=translateSelection(sel);
      if(!res){hidePop();return;}
      var rect=sel.getRangeAt(0).getBoundingClientRect();
      showPop(res,rect);
    },10);
  });

  /* ---------- 4. CLIC PARA OÍR (palabra glosada o italiano) ---------- */
  document.addEventListener('click',function(e){
    var sf=e.target.closest('.say-frase');
    if(sf){say(sf.getAttribute('data-frase')||'',sf);return;}
    var t=e.target.closest('.g,.gp,.it,.cb-say');
    if(t&&!e.target.closest('.cb-pop'))say(t.textContent.trim(),t);
  });

  /* ---------- 4-bis. REGISTRO DE ACTIVIDAD (racha diaria) ---------- */
  window.marcaActividad=function(){try{
    var d=new Date(),k=d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2);
    var m=JSON.parse(localStorage.getItem('italiano-actividad')||'{}');
    if(!m[k]){m[k]=1;localStorage.setItem('italiano-actividad',JSON.stringify(m));}
  }catch(e){}};

  /* ---------- 4-ter. SIEMBRA VIVA ----------
     Los días pueden estar PRE-CONSTRUIDOS (buffer): esta caja lee tu perfil ACTUAL
     al abrir el día, así los focos siempre reflejan tu última corrección. */
  function siembraViva(){
    if(!window.Datos)return;   // sin el helper (página suelta) no hay perfil que leer
    Datos.perfil().then(function(p){
      var rs=(p&&p.rasgos)?Object.keys(p.rasgos).map(function(k){return p.rasgos[k]}):[];
      rs=rs.filter(function(t){return t&&t.estado!=='dominado'&&(t.prioridad||0)>=6});
      if(!rs.length)return;
      rs.sort(function(a,b){return (b.prioridad||0)-(a.prioridad||0)});
      var box=document.createElement('div');box.className='siembra-viva';
      box.innerHTML='<b>🔄 Tus focos de hoy</b> <span class="sv-sub">(de tu perfil vivo — busca cazarlos en los ejercicios)</span><ul>'+
        rs.slice(0,3).map(function(t){return '<li>'+t.etiqueta+'</li>'}).join('')+'</ul>';
      var hdr=document.querySelector('.header')||document.querySelector('.head');
      if(hdr&&hdr.parentNode)hdr.parentNode.insertBefore(box,hdr.nextSibling);
    }).catch(function(){});
  }

  /* ---------- 5. BARRA + PROGRESO ---------- */
  function init(){
    autogloss(document.body);
    if(!pop.parentNode)document.body.appendChild(pop);
    var m=(location.pathname.match(/dia(\d+)/)||[])[1];
    var dia=m?parseInt(m,10):0;
    var esInmer=/inmersion/.test(location.pathname);
    if(!dia&&!esInmer)return;
    var bar=document.createElement('div');bar.className='cb-bar';
    if(dia){
      var prev=dia>1?'dia'+String(dia-1).padStart(2,'0')+'.html':'index.html';
      // ULTIMO_DIA = el día más alto cuyo diaNN.html YA EXISTE. Súbelo al crear un día nuevo
      // (index.html tiene su equivalente en PREP_DESDE = ULTIMO_DIA + 1).
      var ULTIMO_DIA=23;
      var next=dia<ULTIMO_DIA?'dia'+String(dia+1).padStart(2,'0')+'.html':'index.html';
      bar.innerHTML='<a href="index.html">⌂ Índice</a><a href="'+prev+'">‹ Anterior</a><a href="'+next+'">Siguiente ›</a><a href="mi-vocabulario.html">★ Vocabulario</a><a href="practica.html">🎯 Práctica</a><a href="inmersion.html">🎧 Inmersión</a>'+
        '<span class="sp"></span><select id="cb-voice" title="Voz italiana"></select>'+
        '<button id="cb-done">Marcar completado</button>';
    }else{
      bar.innerHTML='<a href="index.html">⌂ Índice</a><a href="mi-vocabulario.html">★ Vocabulario</a><a href="practica.html">🎯 Práctica</a>'+
        '<span class="sp"></span><select id="cb-voice" title="Voz italiana"></select>';
    }
    document.body.insertBefore(bar,document.body.firstChild);
    buildVoiceSelect();
    if(dia){
      var key='italiano-progreso',done=JSON.parse(localStorage.getItem(key)||'{}'),btn=document.getElementById('cb-done');
      function render(){if(done[dia]){btn.textContent='✓ Completado';btn.classList.add('on')}else{btn.textContent='Marcar completado';btn.classList.remove('on')}}
      render();btn.onclick=function(){done[dia]=!done[dia];localStorage.setItem(key,JSON.stringify(done));render();if(done[dia])window.marcaActividad();};
      siembraViva();
    }
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
