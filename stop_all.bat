@echo off
title Léo Barros - Stop All

echo Encerrando todos os serviços...

taskkill /FI "WINDOWTITLE eq IA 5001" /T /F
taskkill /FI "WINDOWTITLE eq NEWS 5002" /T /F
taskkill /FI "WINDOWTITLE eq VOICE 5003" /T /F
taskkill /FI "WINDOWTITLE eq EXCEL LOOP" /T /F
taskkill /FI "WINDOWTITLE eq DASHBOARD" /T /F

echo Todos os serviços foram encerrados!
pause
