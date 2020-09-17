@echo off & setlocal

pyinstaller --name Bierliste_Tool^
   --paths "%cd%"^
   --onefile ^
   --clean ^
   --add-data "%cd%\gui\icon.ico";"." ^
   --add-data "%cd%\gui\background.png";"." ^
   --add-data "%cd%\Anleitung.pdf";"." ^
   --add-data "%cd%\Example_file.xlsx";"." ^
   --icon "%cd%\gui\icon.ico" ^
   .\Bierliste_Tool.py


