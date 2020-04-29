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

Das Plugin selbst ist ein Dock Widget und kann über das Menü Ansicht -> Bedienfelder geladen werden.


Bedienung
---------
## Wenn Sie das Weibullanalyse-Tool geöffnet haben, finden Sie folgendes Fenster vor:

## <img src="/images/weibull_blank.png" width="300">

Weisen Sie den Weibullparametern c, w und k und dem Rauhigkeitslayer z0 jeweils den Layer zu, welcher den passenden Parameter beinhaltet.
Die interaktive Abfrage von Koordinaten und Werten kann mit dem Kontrollkästchen Start/Stop gestartet und unterbrochen werden oder indem die TAB Taste geklickt wird. Dadurch wird der aktuelle Stand eingefroren. Über das Kontrollkästchen "Weibull" können Sie entscheiden, ob die Werte der Eingangsparameter für das ausgewählte Koordinatenpaar tabellarisch angezeigt werden, oder ob eine Weibullkurve gezeichnet wird.
Im Feld "Standort" können Sie den Standortnamen eintragen, mit dem die Weilbullkurve beschriftet wird. Durch Eintragen des Radius bestimmen Sie die Ausdehnung, von welcher das Flächenmittel der Rasterdaten berechnet wird. Über den Button "Grafik speichern" kann die gezeichnete Weibullkurve als PNG-Datei abgespeichert werden.

Ein Beispieldatensatz mit einem QGIS Projekt ist im Ordner [testdaten](./testdaten) abgelegt.
## Wenn Sie das QGIS Projekt geöffnet haben, können Sie die Parameter aus dem Beispieldatensatz verwenden.
## Das Weibullanalyse-Tool sollte dann mit den eingetragen Parametern wie folgt aussehen:

## <img src="/images/weibull_filled.png" width="300">


Das Plugin wurde zuletzt im Januar 2019 aktualisiert.

## Lizenz

Dieses Programm ist freie Software. Es kann unter der den Bedingungen der [GNU General Public License](./LICENSE) weitergegeben und/oder verändert werden. Entweder unter der Version 2 oder einer späteren Version der GPL.
