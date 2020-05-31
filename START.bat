@echo off & setlocal

set "scriptpath=%~dp0" 
set "scriptpath=%scriptpath:~0,-1%"
echo Skriptpath: %scriptpath%

python "%scriptpath%/Bierliste_Tool.py"

