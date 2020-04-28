Weibullanalyse
==============

Plugin für die Bewertung von Windenergiestandorten
--------------------------------------------------

Das Plugin führt eine Bewertung von Windenergiestandorten auf Basis einer Weibullfunktion durch. Als Eingabewerte dienen die Weibullparameter c, w und k sowie die Rauhigkeit z0. Die Werte müssen als Rasterdaten aufbereitet sein. Einen Beispieldatensatz mit einem QGIS Projekt finden Sie im Ordner testdaten. 

Die Wahl des Standorts kann über die Eingabe von Koordinatenwerten oder per Mausklick in der Karte erfolgen. Der Radius ist frei wählbar.

Das Ergebnis der Analyse kann als Weilbullkurve dargestellt und als Bild abgespeichert werden.

<img src="/images/weibull_result.png" width="300">


Benutzerhandbuch
----------------

Das Plugin wird über das Plugin Repository des Geoinformatikbüro Dassau GmbH https://plugins.gbd-consult.de bereitgestellt. Es wird vorausgesetzt, dass Scipy https://www.scipy.org/ installiert ist. Unter Debian/Ubuntu kann das stattfinden mit:

    sudo apt-get install python3-scipy

Starten Sie nun QGIS und öffnen das gewünschte Projekt (das Testprojekt aus dem Ordner testdaten).

Das Plugin selbst ist ein Dock Widget. Man kann es über das Menü Settings -> Panels laden.

Wie beim ValueTool kann man die interaktive Abfrage von Koordinaten und Werten stoppen, indem man z.B. auf die TAB Taste klickt. Dadurch wird der aktuelle Stand eingefroren.

<img src="/images/weibull_blank.png" width="300">

## License

This program is free software; you can redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation; either version 2 of the
License, or (at your option) any later version.
