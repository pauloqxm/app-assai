@echo off
title GeoMercado - Servidor Local
cd /d "%~dp0"
echo.
echo  ====================================================
echo   GeoMercado ^| Potencial de mercado ^| Goiania
echo  ====================================================
echo   Servidor: http://localhost:8000
echo   Pressione Ctrl+C para encerrar.
echo  ====================================================
echo.
start "" http://localhost:8000
"C:\Users\paulo\AppData\Local\Programs\Python\Python313\python.exe" server.py
pause
