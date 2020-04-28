Weibullanalyse
==============

Plugin für die Bewertung von Windenergiestandorten
--------------------------------------------------


Dieses Plugin generiert eine standortbezogene Weilbullkurve, welche zum Beispiel zur Bewertung von Windenergiestandorten dienen kann. Anhand einer Analyse der Weilbullparameter c,w und k und einem Rauhigkeitslayer wird die Weilbullkurve erstellt. Die Wahl des Standorts kann über die Eingabe von Koordinatenwerten oder über die Wahl in der Karte erfolgen. Der Radius ist frei wählbar.

Das Ergebnis der Analyse kann in Form einer Weilbullkurve dargestellt und abgespeichert werden.
![image](https://github.com/gbd-consult/Weibullanalyse/images/weibull_result.png?raw=true)



Benutzerhandbuch
----------------

Vor der Benutzung muss ein Python3 Paket mit folgendem Befehl installiert werden:

# git clone git@github.com:dassau/Weibullanalyse.git ???
# cd Weibullanalyse
# make clean
# make
# make dclean
# make deploy

    sudo apt-get install python3-scipy

    Ausführliche Informationen zu diesem Paket befinden sich auf: *https://www.scipy.org/*

Starten Sie nun QGIS und öffnen das gewünschte Projekt (das Testprojekt aus dem Ordner testdaten).

Das Plugin selbst ist ein Dock Widget. Man kann es über das Menü Settings -> Panels laden.

Wie beim ValueTool kann man die interaktive Abfrage von Koordinaten und Werten stoppen, indem man z.B. auf die TAB Taste klickt. Dadurch wird der aktuelle Stand eingefroren.

![image](https://github.com/gbd-consult/Weibullanalyse/images/weibull_blank.png?raw=true)




## License

This program is free software; you can redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation; either version 2 of the
License, or (at your option) any later version.
