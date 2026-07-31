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
  var ov=null, lanzado=false;
  function loginGate(onReady){
    auth.onAuthStateChanged(function(u){
      if(u){ if(ov)ov.style.display='none'; if(!lanzado){lanzado=true; onReady&&onReady(u);} }
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
})();
