Weibullanalyse
==============

Plugin für die Bewertung von Windenergiestandorten
--------------------------------------------------

Das Plugin führt eine Bewertung von Windenergiestandorten auf Basis der Dichtefunktion der Weibull-Verteilung für Windgeschwindigkeiten durch. Als Eingabewerte dienen die Weibullparameter c, w und k sowie die Rauhigkeit z0. Die Wahl des Standorts kann über die Eingabe von Koordinatenwerten oder per Mausklick in der Karte erfolgen. Über den Parameter Radius wird um den Standortradius das Flächenmittel der Rasterzellen der Eingabedaten berechnet, die vollständig innerhalb des Radius liegen.

Das Ergebnis der Abfrage kann tabellarisch oder als Weilbullkurve dargestellt und als Bild abgespeichert werden.

<img src="/images/weibull_result.png" width="300">

Die Werte müssen als Rasterdaten in gleicher Auflösung aufbereitet sein. 

Installation
------------

Das Plugin wird über das [Plugin Repository der Geoinformatikbüro Dassau GmbH](https://plugins.gbd-consult.de) bereitgestellt. Sie können das Repository über den QGIS Pluginmanager einbinden. 

<img src="/images/repodetails.png" width="300">

Das Plugin selbst ist ein Dock Widget. Man kann es über das Menü Ansicht -> Bedienfelder laden.

Die interaktive Abfrage von Koordinaten und Werten kann mit dem Kontrollkästchen Start/Stop unterbrochen werden oder indem die TAB Taste geklickt wird. Dadurch wird der aktuelle Stand eingefroren. Über das Kontrollkästchen Weibull können Sie entscheiden, ob die Werte der Eingangsparameter für das ausgewählte Koordinatenpaar tabellarisch angezeigt werden, oder ob eine Weibullkurve gezeichnet wird.

<img src="/images/weibull_blank.png" width="300">

Ein Beispieldatensatz mit einem QGIS Projekt ist im Ordner [testdaten](./testdaten) abgelegt.

## Lizenz

Dieses Programm ist freie Software. Es kann unter der den Bedingungen der [GNU General Public License](./LICENSE) weitergegeben und/oder verändert werden. Entweder unter der Version 2 oder einer späteren Version der GPL.
