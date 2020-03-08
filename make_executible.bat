@echo off & setlocal

pyinstaller --name Bierliste_Tool^
   --paths "%cd%"^
   --onefile ^
   --clean ^
   --add-data "%cd%\resources\icon.ico";"." ^
   --add-data "%cd%\resources\child_icon.ico";"." ^
   --add-data "%cd%\resources\background.png";"." ^
   --add-data "%cd%\Anleitung.pdf";"." ^
   --icon "%cd%\resources\icon.ico" ^
   .\Bierliste_Tool.py


