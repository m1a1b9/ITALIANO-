# Curso de Italiano (A2 → C1)

Curso personal de italiano en HTML: lecciones diarias, práctica (SRS), inmersión,
"Il mio libro" y un vocabulario activo. Pensado para estudiar desde cualquier dispositivo.

## Cómo se usa

- **En local (autoría/desarrollo):** ejecutar `Abrir Curso Italiano.bat`, que levanta
  `servidor.py` en `http://localhost:8099` y abre el índice. El servidor local guarda
  las respuestas y correcciones en `datos/` (esa carpeta NO se publica).
- **En la web (multi-dispositivo):** el sitio se publica como estático (GitHub Pages).
  Los datos personales (respuestas, correcciones, perfil, progreso) se sincronizan con
  **Firebase / Firestore** tras iniciar sesión — no viven en el repositorio.

## Privacidad

Este repositorio contiene **solo el contenido del curso** (lecciones, estilos, scripts,
glosario). Los datos personales están excluidos vía `.gitignore` y se guardan en Firestore
(privado, tras login). Las claves de servicio nunca se suben.

## Estructura

- `index.html`, `diaNN.html`, `libro.html`, `practica.html`, `inmersion.html`, … — páginas.
- `assets/` — CSS y JS compartidos (glosario, audio, guardado, IA).
- `servidor.py` — mini-servidor local para desarrollo.
- `datos/` — datos de runtime (ignorado, salvo `drills.json`).
