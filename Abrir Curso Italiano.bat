@echo off
REM Lanzador del Curso de Italiano — abre todo desde un servidor local
REM para que "Mi Vocabulario", el progreso y las actualizaciones se vean al instante.
cd /d "%~dp0"

REM 1) Matar cualquier servidor viejo "pegado" en el puerto 8099 (evita ver versiones viejas)
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":8099" ^| findstr LISTENING') do taskkill /F /PID %%a >nul 2>&1

echo Iniciando el Curso de Italiano...
echo No cierres esta ventana mientras estudias.

REM 2) Abrir el navegador y arrancar el servidor nuevo
start "" "http://localhost:8099/index.html"
python servidor.py
