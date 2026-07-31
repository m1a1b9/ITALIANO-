/* ====== Exámenes semanales (estilo certificación) ======
   Cada examen cubre los temas de su semana. Pesado hacia RECORDAR y PRODUCIR
   (completar/transformar/escritura) por encima de solo reconocer (opción múltiple). */
window.EXAMENES = {
  "1": {
    "titulo": "Examen — Semana 1",
    "nivel": "A2 → B1",
    "temas": ["Passato prossimo vs imperfetto", "Fonética", "Futuro + condizionale", "Modali + imperativo", "Pronomi diretti/indiretti", "Comparativi", "Congiuntivo presente", "Slang"],
    "secciones": [
      {
        "tipo": "completar", "titulo": "1. Completa (conjuga el verbo)",
        "peso": "alto",
        "preguntas": [
          {"q": "Ieri ___ (mangiare, io) una pizza.", "resp": ["ho mangiato"], "tema": "Passato prossimo"},
          {"q": "Da bambino ___ (abitare, io) a Milano.", "resp": ["abitavo"], "tema": "Imperfetto"},
          {"q": "Domani ___ (andare, io) al mare.", "resp": ["andro", "andrò"], "tema": "Futuro semplice"},
          {"q": "Se potessi, ___ (comprare, io) una macchina nuova.", "resp": ["comprerei"], "tema": "Condizionale"},
          {"q": "Penso che lui ___ (essere) stanco.", "resp": ["sia"], "tema": "Congiuntivo presente"}
        ]
      },
      {
        "tipo": "transformar", "titulo": "2. Transforma al passato prossimo",
        "peso": "alto",
        "preguntas": [
          {"q": "Vado a Roma.", "resp": ["sono andato a roma", "sono andata a roma"], "tema": "Passato prossimo (essere)"},
          {"q": "Faccio la doccia.", "resp": ["ho fatto la doccia"], "tema": "Passato prossimo (avere)"},
          {"q": "Devo studiare.", "resp": ["ho dovuto studiare"], "tema": "Modali al passato"},
          {"q": "Esco con gli amici.", "resp": ["sono uscito con gli amici", "sono uscita con gli amici"], "tema": "Passato prossimo (essere)"}
        ]
      },
      {
        "tipo": "opcion", "titulo": "3. Elige la opción correcta",
        "preguntas": [
          {"q": "¿Cómo se pronuncia «ciao»?", "op": ["«chao»", "«kiao»", "«siao»"], "correcta": 0, "tema": "Fonética C/G"},
          {"q": "«gli» suena como…", "op": ["la «ll» española (llave)", "g + l + i separadas", "la «g» de «gato»"], "correcta": 0, "tema": "Fonética GLI"},
          {"q": "El imperfetto se usa sobre todo para…", "op": ["descripción y costumbre en el pasado", "una acción puntual y terminada", "dar una orden"], "correcta": 0, "tema": "PP vs imperfetto"},
          {"q": "«Compro il pane» con pronombre directo:", "op": ["Lo compro", "La compro", "Gli compro"], "correcta": 0, "tema": "Pronomi diretti"},
          {"q": "«pesce» se pronuncia…", "op": ["«pé-she»", "«pés-ke»", "«pé-se»"], "correcta": 0, "tema": "Fonética SC"}
        ]
      },
      {
        "tipo": "opcion", "titulo": "4. Vocabulario y slang",
        "preguntas": [
          {"q": "«sgamare» =", "op": ["cachar / descubrir a alguien", "tenedor", "escoria"], "correcta": 0, "tema": "Slang"},
          {"q": "«gasato» =", "op": ["emocionado / clavado", "cansado", "enojado"], "correcta": 0, "tema": "Slang"},
          {"q": "«meglio» =", "op": ["mejor", "peor", "menos"], "correcta": 0, "tema": "Comparativi"},
          {"q": "«bagno» =", "op": ["baño", "balcón", "barco"], "correcta": 0, "tema": "Vocabulario"}
        ]
      },
      {
        "tipo": "escritura", "titulo": "5. Escritura (te la corrijo yo)",
        "peso": "alto",
        "preguntas": [
          {"q": "Escribe 3–4 frases sobre tu fin de semana pasado. Usa al menos 2 passato prossimo y 1 imperfetto como contexto.", "tema": "Producción"}
        ]
      }
    ]
  }
};
