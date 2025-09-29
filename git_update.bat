@echo off
cd /d C:\LeoEA
echo ===============================
echo Subindo código para o GitHub...
echo ===============================

set /p msg=Digite a mensagem do commit: 

git add .
git commit -m "%msg%"
git push origin main

echo ===============================
echo   ✅ Atualização enviada!
echo ===============================
pause
