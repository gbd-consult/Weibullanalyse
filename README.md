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

Das Plugin wird über das Plugin Repository des Geoinformatikbüro Dassau GmbH https://plugins.gbd-consult.de bereitgestellt. Die können das Repository über den QGIS Pluginmanager einbinden. 

<img src="/images/repodetails.png" width="300">

Das Plugin selbst ist ein Dock Widget. Man kann es über das Menü Settings -> Panels laden.

Die interaktive Abfrage von Koordinaten und Werten kann mit dem Kontrollkästchen Start/Stop unterbrochen werden oder indem man z.B. auf die TAB Taste klickt. Dadurch wird der aktuelle Stand eingefroren.

<img src="/images/weibull_blank.png" width="300">

## Lizenz

Dieses Programm ist freie Software (GPL v2). Sie können es unter den Bedingungen der [GNU General Public License](./LICENSE), 
weitergeben und/oder ändern, entweder unter der Version 2 oder einer späteren Version.
