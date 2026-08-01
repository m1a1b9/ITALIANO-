/* ============================================================
   Firebase (compat) — init + login + helpers compartidos.
   Cargar DESPUÉS de los <script> compat de Firebase en el HTML.
   La config es de CLIENTE (pública): la seguridad la dan las reglas de Firestore.
   ============================================================ */
(function(){
  if(!window.firebase||!firebase.initializeApp){console.error('[FB] SDK de Firebase no cargado');return;}
  var cfg={
    apiKey:"AIzaSyAYtegyI3jkH_nQ0z1rN7eh1QfKvIYpuOY",
    authDomain:"italiano-f89ec.firebaseapp.com",
    projectId:"italiano-f89ec",
    storageBucket:"italiano-f89ec.firebasestorage.app",
    messagingSenderId:"787163994487",
    appId:"1:787163994487:web:7e5934d115ab5671486972"
  };
  if(!firebase.apps.length)firebase.initializeApp(cfg);
  var auth=firebase.auth(), db=firebase.firestore();
  try{auth.setPersistence(firebase.auth.Auth.Persistence.LOCAL);}catch(e){}   // recuerda la sesión

  function udoc(){ var u=auth.currentUser; return u?db.collection('users').doc(u.uid):null; }

  // ---- overlay de login: llama onReady(user) UNA vez cuando hay sesión ----
  //      (bandera POR LLAMADA para que varios loginGate independientes disparen su propio callback)
  var ov=null;
  function loginGate(onReady){
    var fired=false;
    auth.onAuthStateChanged(function(u){
      if(u){ if(ov)ov.style.display='none'; if(!fired){fired=true; onReady&&onReady(u);} }
      else { mostrarOverlay(); }
    });
  }
  function mostrarOverlay(){
    if(ov){ov.style.display='flex';return;}
    ov=document.createElement('div');
    ov.style.cssText='position:fixed;inset:0;z-index:100000;background:rgba(18,28,38,.97);display:flex;align-items:center;justify-content:center;font-family:-apple-system,Segoe UI,sans-serif';
    ov.innerHTML='<div style="background:#fff;border-radius:12px;padding:1.7rem 1.5rem;max-width:340px;width:90%;box-shadow:0 12px 44px rgba(0,0,0,.45)">'+
      '<h2 style="margin:.1rem 0 .3rem;color:#1a4d80;font-size:1.25rem">🔒 Entra a tu curso</h2>'+
      '<p style="margin:0 0 1rem;color:#666;font-size:.85rem">Tus datos (canciones, progreso) quedan privados y sincronizados en tus dispositivos.</p>'+
      '<input id="fb-email" type="email" autocomplete="username" placeholder="correo" style="width:100%;box-sizing:border-box;margin:.25rem 0;padding:.6rem;border:1px solid #ccc;border-radius:7px;font-size:.95rem">'+
      '<input id="fb-pass" type="password" autocomplete="current-password" placeholder="contraseña" style="width:100%;box-sizing:border-box;margin:.25rem 0;padding:.6rem;border:1px solid #ccc;border-radius:7px;font-size:.95rem">'+
      '<button id="fb-login" style="width:100%;margin-top:.6rem;background:#1a4d80;color:#fff;border:0;border-radius:7px;padding:.65rem;font-weight:700;cursor:pointer;font-size:.95rem">Entrar</button>'+
      '<div id="fb-err" style="color:#c0392b;font-size:.82rem;margin-top:.55rem;min-height:1rem"></div></div>';
    document.body.appendChild(ov);
    function entrar(){
      var em=(ov.querySelector('#fb-email').value||'').trim(), pw=ov.querySelector('#fb-pass').value||'';
      var err=ov.querySelector('#fb-err'); err.style.color='#666'; err.textContent='entrando…';
      auth.signInWithEmailAndPassword(em,pw).catch(function(e){
        err.style.color='#c0392b';
        var mal=/invalid-credential|wrong-password|user-not-found|invalid-email/.test(e.code||'');
        err.textContent='⚠ '+(mal?'Correo o contraseña incorrectos.':(e.message||'No se pudo entrar.'));
      });
    }
    ov.querySelector('#fb-login').onclick=entrar;
    ov.querySelector('#fb-pass').addEventListener('keydown',function(e){if(e.key==='Enter')entrar();});
    ov.querySelector('#fb-email').addEventListener('keydown',function(e){if(e.key==='Enter')ov.querySelector('#fb-pass').focus();});
  }

  window.FB={
    auth:auth, db:db, udoc:udoc, loginGate:loginGate,
    user:function(){return auth.currentUser;},
    logout:function(){return auth.signOut();},
    // referencias a los datos del usuario: users/{uid}/{col}/{id}
    doc:function(col,id){var u=auth.currentUser;return u?db.collection('users').doc(u.uid).collection(col).doc(String(id)):null;},
    col:function(col){var u=auth.currentUser;return u?db.collection('users').doc(u.uid).collection(col):null;}
  };

  /* ===== DATOS del curso — MISMA API en localhost y en la web =====
     En localhost manda el servidor local (/api); en la web, Firestore (tras login).
     Centralizado aquí para que ninguna página tenga que repetir ese switch.
     Las páginas solo llaman: Datos.perfil() · .errores() · .examenes() · .guardarExamen() · .marcarRasgo()
     OJO: como este archivo es `defer`, window.Datos no existe durante los <script> inline
     del <body>; esas páginas deben arrancar en DOMContentLoaded. */
  window.Datos=(function(){
    var esLocal=/localhost|127\.0\.0\.1/.test(location.hostname);
    function listo(){   // en la web hace falta sesión para poder leer/escribir Firestore
      if(esLocal)return Promise.resolve();
      return new Promise(function(res){loginGate(function(){res();});});
    }
    function get(ruta,vacio){return fetch(ruta).then(function(r){return r.json()}).catch(function(){return vacio;});}
    function post(ruta,body){return fetch(ruta,{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify(body)}).then(function(r){return r.json()}).catch(function(){return {ok:false};});}
    function colMap(col){          // users/{uid}/{col} -> {id:data}
      return listo().then(function(){
        var u=udoc(); if(!u)return {};
        return u.collection(col).get().then(function(qs){var o={};qs.forEach(function(d){o[d.id]=d.data()||{};});return o;});
      }).catch(function(){return {};});
    }
    function perfilRef(){var u=udoc();return u?u.collection('perfil').doc('actual'):null;}
    return {
      esLocal:esLocal,
      perfil:function(){
        if(esLocal)return get('/api/perfil',{});
        return listo().then(function(){
          var r=perfilRef(); if(!r)return {};
          return r.get().then(function(d){return d.exists?(d.data()||{}):{};});
        }).catch(function(){return {};});
      },
      errores:function(){  return esLocal?get('/api/errores',{}) :colMap('errores');  },
      examenes:function(){ return esLocal?get('/api/examenes',{}):colMap('examenes'); },
      guardarExamen:function(sem,resultado){
        if(esLocal)return post('/api/examenes',{semana:sem,resultado:resultado});
        return listo().then(function(){
          var u=udoc(); if(!u)return {ok:false};
          return u.collection('examenes').doc(String(sem)).set(resultado).then(function(){return {ok:true};});
        }).catch(function(){return {ok:false};});
      },
      // marca manual del diagnóstico: misma semántica que servidor.py (toca SOLO ese rasgo
      // y guarda prev_* para poder revertir con "reactivar")
      marcarRasgo:function(clave,accion){
        if(esLocal)return post('/api/perfil',{rasgo:clave,accion:accion});
        return listo().then(function(){
          var ref=perfilRef(); if(!ref)return {ok:false};
          return ref.get().then(function(d){
            var p=d.exists?(d.data()||{}):{}, rs=p.rasgos||{}, r=rs[clave];
            if(!r)return {ok:false,error:'rasgo no encontrado'};
            if(accion==='dominar'){
              r.prev_estado=r.estado||'consolidando';
              r.prev_prioridad=(r.prioridad!==undefined?r.prioridad:6);
              r.prev_tendencia=r.tendencia||'estancado';
              r.estado='dominado'; r.prioridad=0; r.tendencia='mejorando'; r.dominado_manual=true;
            }else{
              r.estado=r.prev_estado||'consolidando';
              r.prioridad=(r.prev_prioridad!==undefined?r.prev_prioridad:6);
              r.tendencia=r.prev_tendencia||'estancado';
              delete r.prev_estado; delete r.prev_prioridad; delete r.prev_tendencia; delete r.dominado_manual;
            }
            return ref.set(p).then(function(){return {ok:true};});
          });
        }).catch(function(){return {ok:false};});
      }
    };
  })();

  /* ===== Sincronización de PROGRESO (localStorage <-> Firestore) — SOLO en la WEB con sesión =====
     Espeja ciertas claves de localStorage a users/{uid}/progreso/{clave}, FUSIONANDO (unión) para
     no perder datos entre dispositivos. En localhost NO se activa (ahí manda el servidor local). */
  (function(){
    function norm(s){return (''+(s||'')).toLowerCase().trim();}
    function mergeArrBy(keyName){return function(cloud,local){
      var out=[], seen={};
      (Array.isArray(local)?local:[]).forEach(function(o){var k=norm(o&&o[keyName]);if(k&&!seen[k]){seen[k]=1;out.push(o);}});
      (Array.isArray(cloud)?cloud:[]).forEach(function(o){var k=norm(o&&o[keyName]);if(k&&!seen[k]){seen[k]=1;out.push(o);}});
      return out;
    };}
    function mergeMapUnion(cloud,local){var o={},c=cloud||{},l=local||{},k;for(k in c)o[k]=c[k];for(k in l)o[k]=l[k];return o;}
    function mergeMax(cloud,local){var o={},c=cloud||{},l=local||{},k;for(k in c)o[k]=c[k];for(k in l)o[k]=Math.max(o[k]||0,l[k]||0);return o;}
    var CLAVES={
      'italiano-vocab-activo': mergeArrBy('it'),
      'italiano-actividad':    mergeMapUnion,
      'italiano-progreso':     mergeMapUnion,
      'italiano-srs':          mergeMapUnion,
      'italiano-inmersion':    mergeMax
    };
    function lsGet(k){try{return JSON.parse(localStorage.getItem(k)||'null');}catch(e){return null;}}
    var muted=false;
    function lsSetMuted(k,v){muted=true;try{localStorage.setItem(k,JSON.stringify(v));}finally{muted=false;}}
    function progRef(k){var u=auth.currentUser;return u?db.collection('users').doc(u.uid).collection('progreso').doc(k):null;}
    function sync(k){
      var ref=progRef(k); if(!ref)return Promise.resolve(false);
      var before=localStorage.getItem(k), local=lsGet(k);
      return ref.get().then(function(d){
        var cloud=d.exists?(d.data()||{}).data:null;
        var merged=CLAVES[k](cloud, local);
        lsSetMuted(k, merged);
        ref.set({data:merged, t:Date.now()}).catch(function(){});
        return localStorage.getItem(k)!==before;   // ¿la nube trajo algo nuevo a este dispositivo?
      }).catch(function(){ if(local!=null)ref.set({data:local, t:Date.now()}).catch(function(){}); return false; });
    }
    var timers={}, _set=localStorage.setItem.bind(localStorage);
    localStorage.setItem=function(k,v){ _set(k,v); if(!muted && CLAVES[k]){ clearTimeout(timers[k]); timers[k]=setTimeout(function(){sync(k);},1200); } };
    loginGate(function(){
      Promise.all(Object.keys(CLAVES).map(sync)).then(function(res){
        if(res.some(function(c){return c;}) && !sessionStorage.getItem('fb-reload')){
          sessionStorage.setItem('fb-reload','1'); location.reload();   // recarga UNA vez para mostrar lo sincronizado
        }
      });
    });
  })();
})();
