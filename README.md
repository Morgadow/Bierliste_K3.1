# Bierliste_K3.1
Python Tool mit grafischer Oberfläche um Abrechnungen und Schuldenübersichten der Bierliste unserer Wohnheimsküche zu erleichtern


Bierabrechnung basieren auf einer Excel Tabelle die am Bierkühlschrank angebracht ist. 
Dort hat jeder im Code _drinker_ gennant eine Zeile und kann für jedes entnommene Getränk Striche machen.
Irgendwann wird abgerechnet und die Striche zusammengezählt, Geld eingetrieben und eine neue Liste ausgedruckt. 
Damit nicht ungerade Beträge gezahlt werden müssen kann man auch mehr einzahlen und Guthaben aufbauen, deswegen wird die Liste nicht immer direkt gelöscht.

Ablauf Tool:
- Tool öffnen 
- Excel Liste einlesen (die gleiche Liste die am Kühlschrank hängt)
- Für jeden _drinker_ wird ein Button im Tool erstellt
- Mit Druck auf einen Button kann eingetragen werden wieviel jeder Nutzer getrunken und/oder eingezahlt hat
- Ist jeder eingetragen wird die Excel wieder in eine neue Liste exportiert
- Dafür wird die Example Datei kopiert und neu befüllt mit 2 Tabellen:
 - Eine mit den eingetragenen Werten, also alte Liste und die eingetragenen Striche
 - Eine mit dem neuen Stand, also neues berechnetes Guthaben, das ist die Liste die wieder an den Kühlschrank kommt

Hinweise:
- Format der Excel Tabellen an der Example Datei orientieren, die Spalten und Zeilen sind fix festgelegt
- Preise können über die Settingsdatei eingestellt werden
- Aufpreis für Externe ist möglich und wird über die Settings.ini eingestellt (sonst auf 0 setzen)
- In der Excel wird auch mitgeschrieben wie viel jeder getrunken hat


Noch nicht erledigte ToDos:
- Siehe .py
