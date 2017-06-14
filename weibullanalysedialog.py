# -*- coding: utf-8 -*-

"""
/***************************************************************************
 QGIS Plugin zur Erstellung einer Weibull-Analyse für Windenergiestandorte
 -------------------
        begin                : 2013-01-08
        copyright            : (C) 2013 by Geoinformatikbüro Dassau GmbH
        email                : info@gbd-consult.de
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

# Hilfe: Benutzung zur Ausgabe von Variablen in einem Info-Fenster
# QMessageBox.information(None, "Info:", <variable>)

import logging
# Ändere den Level zurück auf logging.WARNING(default) vor dem Release
logging.basicConfig(level=logging.WARNING)

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from ui_weibullanalyse import Ui_ValueWidgetBase

# für die Berechung des Mittelwertes
from qgis.analysis import QgsZonalStatistics

# Testen, ob matplotlib >= 1.0
hasmpl=True
try:
    import matplotlib
    import matplotlib.pyplot as plt 
    import matplotlib.ticker as ticker
    import string
    import numpy
    import scipy
    import scipy.misc
    import pylab
    from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg
    from scipy import integrate

except:
    hasmpl = False
if hasmpl:
    if int(matplotlib.__version__[0]) < 1:
        hasmpl = False

class ValueWidget(QWidget, Ui_ValueWidgetBase):

    def __init__(self, iface):

        self.hasmpl = hasmpl
        self.layerMap = dict()
        self.statsChecked = False
        
        # Variablen initialisieren
        self.ymin = 0
        self.ymax = 250
        self.xCoord = 0
        self.yCoord = 0
        self.mean = 0
        self.standortname = None
        self.fileName = None
        
        # Statistics (>=1.9)
        self.statsSampleSize = 2500000
        self.stats = {} # stats per layer        
        
        self.iface=iface
        self.canvas=self.iface.mapCanvas()
        self.legend=self.iface.legendInterface()
        self.logger = logging.getLogger('.'.join((__name__, 
                                        self.__class__.__name__)))
                                        
        QWidget.__init__(self)
        self.setupUi(self)
        self.setupUi_extra()

        QObject.connect(self.cbxActive,SIGNAL("stateChanged(int)"),self.changeActive)
        QObject.connect(self.cbxGraph,SIGNAL("stateChanged(int)"),self.changePage) 
        QObject.connect(self.canvas, SIGNAL( "keyPressed( QKeyEvent * )" ), self.pauseAnzeige )
        QObject.connect(self.canvas, SIGNAL( "keyPressed( QKeyEvent * )" ), self.pauseGraph )
        QObject.connect(self.canvas, SIGNAL( "keyPressed( QKeyEvent * )" ), self.printWeibull )
        QObject.connect(self.buttonSaveAs, SIGNAL("clicked()"), self.savePNG)

        # connect layer list in plugin combobox 
        QObject.connect(QgsMapLayerRegistry.instance(), SIGNAL("layerWasAdded(QgsMapLayer *)"), self.add_layer)
        QObject.connect(QgsMapLayerRegistry.instance(), SIGNAL("layerWillBeRemoved(QString)"), self.remove_layer)
        
        # Lade Rasterlayer in die Combobox
        self.initRasterLayerCombobox( self.InRastC, 'key_of_default_layer' )
        self.initRasterLayerCombobox( self.InRastK, 'key_of_default_layer' )
        self.initRasterLayerCombobox( self.InRastW, 'key_of_default_layer' )       
        self.initRasterLayerCombobox( self.InRastZ, 'key_of_default_layer' )

        # Setze Radius (z0) für die Pufferung
        self.buffer = self.bufferz0.value()
        #QMessageBox.information(None, "Info:", str(self.buffer))
        # Standortname für Datei und Titel der Weibullkurve
        self.standortname = self.dataName.text()
        #QMessageBox.information(None, "Info:", str(self.dateiname))
    
    def add_layer(self, layerid):
        self.initRasterLayerCombobox( self.InRastC, self.InRastC.currentText() )
        self.initRasterLayerCombobox( self.InRastK, self.InRastK.currentText() )
        self.initRasterLayerCombobox( self.InRastW, self.InRastW.currentText() )
        self.initRasterLayerCombobox( self.InRastZ, self.InRastZ.currentText() )    
    
    def remove_layer(self, layerid):
        layer = QgsMapLayerRegistry.instance().mapLayer(layerid)
        self.InRastC.removeItem( self.InRastC.findData( layer.name() ) )
        self.InRastK.removeItem( self.InRastK.findData( layer.name() ) )
        self.InRastW.removeItem( self.InRastW.findData( layer.name() ) )
        self.InRastZ.removeItem( self.InRastZ.findData( layer.name() ) )
        
    def setupUi_extra(self):
        # Checkbox  Anzeige Start/Stop
        # self.changeActive(Qt.Checked)
        # set inactive by default - should save last state in user config
        self.cbxActive.setCheckState(Qt.Unchecked)

        # plot (taken from value tool - only for matplotlib)
        # Page 2 - matplotlib
        self.mplLine = None #make sure to invalidate when layers change
        if self.hasmpl:
            # mpl definitions
            # should make figure light gray
            self.mplBackground = None  #http://www.scipy.org/Cookbook/Matplotlib/Animations
            self.mplFig = plt.Figure(facecolor='w', edgecolor='w')
            self.mplFig.subplots_adjust(left=0.1, right=0.975, bottom=0.13, top=0.95)
            self.mplPlt = self.mplFig.add_subplot(111)
            self.mplPlt.tick_params(axis='both', which='major', labelsize=12)
            self.mplPlt.tick_params(axis='both', which='minor', labelsize=10)                           
            # qt definitions
            self.pltCanvas = FigureCanvasQTAgg(self.mplFig)
            self.pltCanvas.setParent(self.stackedWidget)
            self.pltCanvas.setAutoFillBackground(False)
            self.pltCanvas.setObjectName("mplPlot")
            self.mplPlot = self.pltCanvas
            self.mplPlot.setVisible(False)
        else:
            self.mplPlot = QtGui.QLabel("Need matplotlib >= 1.0 !")

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplPlot.sizePolicy().hasHeightForWidth())
        self.mplPlot.setSizePolicy(sizePolicy)
        self.mplPlot.updateGeometry()
        self.stackedWidget.addWidget(self.mplPlot)
        self.stackedWidget.setCurrentIndex(0)

    def accept(self):
        # check input parameters
        if self.InRastC.currentIndex()  == -1:
            QMessageBox.warning( self, self.tr( "Weibullauswertung: Warning" ),
                self.tr( "Please select raster layer for scale factor A" ) )
            return
        if self.InRastK.currentIndex()  == -1:
            QMessageBox.warning( self, self.tr( "Weibullauswertung: Warning" ),
                self.tr( "Please select raster layer for form factor K" ) )
            return
        if self.InRastW.currentIndex()  == -1:
            QMessageBox.warning( self, self.tr( "Weibullauswertung: Warning" ),
                self.tr( "Please select raster layer for form factor K" ) )
            return            
        if self.InRastZ.currentIndex()  == -1:
            QMessageBox.warning( self, self.tr( "Weibullauswertung: Warning" ),
                self.tr( "Please select raster layer for roughness Z" ) )
            return
 
    # Deaktiviere wieder die Anzeige Start/Stop Auswahl, wenn Shift-A gedrückt wird
    def disconnect(self):
        self.changeActive(False)
        QObject.disconnect(self.canvas, SIGNAL( "keyPressed( QKeyEvent * )" ), self.pauseAnzeige )
        QObject.disconnect(self.canvas, SIGNAL( "keyPressed( QKeyEvent * )" ), self.pauseGraph )
        
    # Switche die Anzeige Start/Stop Auswahl, wenn Shift-A gedrückt wird
    def pauseAnzeige(self, e):
        if ( e.modifiers() == Qt.ShiftModifier or e.modifiers() == Qt.MetaModifier ) and e.key() == Qt.Key_A:
            self.cbxActive.toggle()
            return True
        return False

    # Switche zwischen Anzeige und Weibullgrafik, wenn Shift-W gedrückt wird
    def pauseGraph(self, e):
        if ( e.modifiers() == Qt.ShiftModifier or e.modifiers() == Qt.MetaModifier ) and e.key() == Qt.Key_W:
            self.cbxGraph.toggle()
            return True
        return False

    # Starte den Dialog Grafik speichern, wenn Shift-S gedrückt wird
    def printWeibull(self, e):
        if ( e.modifiers() == Qt.ShiftModifier or e.modifiers() == Qt.MetaModifier ) and e.key() == Qt.Key_S:
            self.savePNG()
            return True
        return False

    # Return QgsMapLayer.RasterLayer (only gdal) from a layer name ( as string )
    def initRasterLayerCombobox(self, combobox, layerid):
        combobox.clear()
        reg = QgsMapLayerRegistry.instance()
        for ( key, layer ) in reg.mapLayers().iteritems():
            if layer.type() == QgsMapLayer.RasterLayer: combobox.addItem( layer.name(), key )
         
        idx = combobox.findData( layerid )
        if idx != -1:
            combobox.setCurrentIndex( idx )

    # Hole Liste geladener Rasterlayer
    def getRasterLayerByName( self,  myName ):
        layerMap = QgsMapLayerRegistry.instance().mapLayers()
        for name, layer in layerMap.iteritems():
            if layer.type() == QgsMapLayer.RasterLayer and layer.name() == myName:
                if layer.isValid():
                    return layer
                else:
                    return None

    # Grafische Anzeige an- und abschalten (vom valuetool plugin)
    def changePage(self,state):
        if (state==Qt.Checked):
            self.graphControls.setVisible( True )
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.graphControls.setVisible( False )
            self.stackedWidget.setCurrentIndex(0)

    # Wechseln zwischen Anzeige der Werte und der Weibullkurve
    def changePlot(self):
        self.changePage(self.cbxActive.checkState())

    # Steuerung von Start/Stop (adapted from value tool)
    def changeActive(self,state):
        if self.cbxActive.isChecked():
            QObject.connect(self.canvas, SIGNAL( "layersChanged ()" ), self.invalidatePlot )
            QObject.connect(self.canvas, SIGNAL("xyCoordinates(const QgsPoint &)"), self.printValue)
            QObject.connect(self.canvas, SIGNAL("xyCoordinates(const QgsPoint &)"), self.listen_xCoordinates)
            QObject.connect(self.canvas, SIGNAL("xyCoordinates(const QgsPoint &)"), self.listen_yCoordinates)             
        else:
            QObject.disconnect(self.canvas, SIGNAL( "layersChanged ()" ), self.invalidatePlot )
            QObject.disconnect(self.canvas, SIGNAL("xyCoordinates(const QgsPoint &)"), self.printValue)
            QObject.disconnect(self.canvas, SIGNAL("xyCoordinates(const QgsPoint &)"), self.listen_xCoordinates)
            QObject.disconnect(self.canvas, SIGNAL("xyCoordinates(const QgsPoint &)"), self.listen_yCoordinates)          
                
    # Gebe X-Koordinate aus und überschreibe vorherige (append ergänzt)
    def listen_xCoordinates(self, point):
        if point.x():
            x = point.x()
            self.outputXEdit.setText("%d" % (x))
            self.xCoord = x
            
    # Gebe Y-Koordinate aus und überschreibe Vorherige (append ergänzt)
    def listen_yCoordinates(self, point):
        if point.y():
            y = point.y()
            self.outputYEdit.setText("%d" % (y))
            self.yCoord = y

    # Wert an Mausposition
    def sampleRaster20(self, layer, x, y):
        ident = layer.dataProvider().identify(QgsPoint(x,y), QgsRaster.IdentifyFormatValue ).results()
        return ident[1]
            
    # Frage Wert für die Rasterlayer an Mouseposition ab
    def sampleRaster(self, raster_name, x, y):
        layer = self.getRasterLayerByName(raster_name)
        return self.sampleRaster20(layer, x, y)

    # Zeige Rasterwerte als Tabelle (angepasst vom valuetool plugin)
    def printValue(self, position):
        if self.canvas.layerCount() == 0:
            self.values=[]         
            self.showValues()
            return
        
        needextremum = self.cbxGraph.isChecked() # if plot is checked
        
        # count the number of requires rows and remember the raster layers
        nrow=0
        rasterlayers=[] 
        layersWOStatistics=[]

        for i in range(self.canvas.layerCount()):
            layer = self.canvas.layer(i)
            if (layer!=None and layer.isValid() and layer.type()==QgsMapLayer.RasterLayer):
                if not layer.dataProvider():
                    continue

                if not layer.dataProvider().capabilities() & QgsRasterDataProvider.IdentifyValue:
                    continue

                nrow+=layer.bandCount()
                rasterlayers.append(layer)
                 
        # create the row if necessary
        self.tableWidget.setRowCount(nrow)

        irow=0
        self.values=[]
        self.ymin=1e38
        self.ymax=-1e38

        mapCanvasSrs = self.iface.mapCanvas().mapRenderer().destinationCrs()

        # TODO - calculate the min/max values only once, instead of every time!!!
        # keep them in a dict() with key=layer.id()
                
        for layer in rasterlayers:
            layername=unicode(layer.name())
            layerCrs = layer.crs()
            pos = position         

            # if given no position, get dummy values
            if position is None:
                pos = QgsPoint(0,0)
            # transform points if needed
            elif not mapCanvasSrs == layerCrs and self.iface.mapCanvas().hasCrsTransformEnabled():
                srsTransform = QgsCoordinateTransform(mapCanvasSrs, layerCrs)
                try:
                    pos = srsTransform.transform(position)
                except QgsCsException, err:
                    # ignore transformation errors
                    continue

            if not layer.dataProvider():
                continue

            ident = None
            if position is not None:
                canvas = self.iface.mapCanvas()

            # first test if point is within map layer extent 
            # maintain same behaviour as in 1.8 and print out of extent
                if not layer.dataProvider().extent().contains( pos ):
                    ident = dict()
                    for iband in range(1,layer.bandCount()+1):
                        ident[iband] = str(self.tr('out of extent'))
                # we can only use context if layer is not projected
                elif canvas.hasCrsTransformEnabled() and layer.dataProvider().crs() != canvas.mapRenderer().destinationCrs():
                    ident = layer.dataProvider().identify(pos, QgsRaster.IdentifyFormatValue ).results()
                else:
                    extent = canvas.extent()
                    width = round(extent.width() / canvas.mapUnitsPerPixel());
                    height = round(extent.height() / canvas.mapUnitsPerPixel());
                    
                    extent = canvas.mapRenderer().mapToLayerCoordinates( layer, extent );

                    ident = layer.dataProvider().identify(pos, QgsRaster.IdentifyFormatValue, canvas.extent(), width, height ).results()
                if not len( ident ) > 0:
                    continue

                # if given no position, set values to 0
                if position is None and ident is not None and ident.iterkeys() is not None:
                    for key in ident.iterkeys():
                        ident[key] = layer.dataProvider().noDataValue(key)

                for iband in range(1,layer.bandCount()+1): # loop over the bands
                    layernamewithband=layername
                    if ident is not None and len(ident)>1:
                        layernamewithband+=' '+layer.bandName(iband)

                    if not ident or not ident.has_key( iband ): # should not happen
                        bandvalue = "?"
                    else:                  
                        bandvalue = ident[iband]
                        if bandvalue is None:
                            bandvalue = "no data"

                    self.values.append((layernamewithband,str(bandvalue)))

                    if needextremum:
                        # estimated statistics
                        stats = self.getStats ( layer, iband )
                        if stats:
                            self.ymin=min(self.ymin,stats.minimumValue)
                            self.ymax=max(self.ymax,stats.maximumValue)
                            
        self.showValues()
    
    # Ausgabe der Rasterwerte als Tabelle oder Weibullkurve (from value tool)
    def showValues(self):
        if self.cbxGraph.isChecked():
            #TODO don't plot if there is no data to plot...
            self.plot()
        else:
            self.printInTable()

    # get cached statistics for layer and band or None if not calculated
    def getStats ( self, layer, bandNo, force = False ):
        if self.stats.has_key( layer ):
            if self.stats[layer].has_key( bandNo ) : 
                return self.stats[layer][bandNo]
        else:
            self.stats[layer] = {}
      
        if force or layer.dataProvider().hasStatistics( bandNo, QgsRasterBandStats.Min | QgsRasterBandStats.Min, QgsRectangle(), self.statsSampleSize ):
            self.stats[layer][bandNo] = layer.dataProvider().bandStatistics( bandNo, QgsRasterBandStats.Min | QgsRasterBandStats.Min, QgsRectangle(), self.statsSampleSize )
            return self.stats[layer][bandNo]

        return None

    # Gebe Rasterwerte als Tabelle aus (from value tool)
    def printInTable(self):

        irow=0
        for row in self.values:
            layername,value=row
          
            if (self.tableWidget.item(irow,0)==None):
                # create the item
                self.tableWidget.setItem(irow,0,QTableWidgetItem())
                self.tableWidget.setItem(irow,1,QTableWidgetItem())

            self.tableWidget.item(irow,0).setText(layername)
            self.tableWidget.item(irow,1).setText(value)
            irow+=1

    def meanBuffer(self):
        # leeren Memorylayer erzeugen als UTM32N KBS für den Puffer z0 um die Mousepoition
        vpoly = QgsVectorLayer("Polygon?crs=epsg:32632",  "pointbuffer", "memory")
        feature = QgsFeature()
        feature.setGeometry(QgsGeometry.fromPoint(QgsPoint(self.xCoord, self.yCoord)).buffer(self.bufferz0.value(),5))
        provider = vpoly.dataProvider()
        provider.addFeatures( [feature] )
        vpoly.commitChanges()
        stats = QgsZonalStatistics(vpoly, self.getRasterLayerByName( self.InRastZ.currentText() ).source())
        stats.calculateStatistics(None)
        allAttrs = provider.attributeIndexes()       
        for feature in vpoly.getFeatures():
            mean_value = feature.attributes()[2]
            return mean_value

    # Gebe Rasterwerte als Weibullkurve aus 
    def plot(self):
    
        # Variable initialisieren
        c = 0
        
        try:
            # Mittlere Windgeschwindigkeit
            w = float(self.sampleRaster(self.InRastW.currentText(), self.xCoord, self.yCoord))/10
            # Weibullparameter C
            c = float(self.sampleRaster(self.InRastC.currentText(), self.xCoord, self.yCoord))/10
            # Weibullparameter K
            k = float(self.sampleRaster(self.InRastK.currentText(), self.xCoord, self.yCoord))/1000
            # mittlere Rauhigkeit (Mittelwerte auf Basis des angegebenen Radius)
            z0 = self.meanBuffer()
        except ValueError:
            self.iface.messageBar().pushMessage("Weibullauswertung: Fehler", 
            "Mindestens ein Layer ausserhalb des Abfragebereichs! Passen Layer KBS zueinander?",  
            level=QgsMessageBar.CRITICAL, duration=2)
        except TypeError:
            self.iface.messageBar().pushMessage("Weibullauswertung: Fehler", 
            "Mindestens ein Layer ausserhalb des Abfragebereichs! Passen Layer KBS zueinander?",  
            level=QgsMessageBar.CRITICAL)
            
        #Haeufigkeit aus der Weibull-Dichtefunktion durch Integration
        if c > 0:
            try:
                y = lambda x: k/c*(x/c)**(k-1)*numpy.exp(-(x/c)**k)
                rh=integrate.romberg(y,0.,1.0)      
                rh=round(rh*100,1)          
                # Weibull Dichte Funktion fur Grafik
                def f(x):        
                    return k/c*(x/c)**(k-1)*numpy.exp(-(x/c)**k)
                X = numpy.linspace(0, 12, 1200)
                Y = f(X)
        
                # Plot Rahmen Beschriftungen etc
                self.mplPlt.clear()
                self.mplPlt.grid()
                self.mplPlt.plot(X, Y, linewidth=3, label=None)
                self.mplPlt.set_ylim(0,0.36)
            
                #Beschriftungen in der Grafik, Startposition uber Wertepaar
                self.mplPlt.text(2, 0.34, unicode("rel. H\344ufigkeit < 1 m/s = %.2f" %(rh,), 'latin-1'), fontsize=10)
                self.mplPlt.text(8.9, 0.34, unicode('\045', 'latin-1'), fontsize=10)
                self.mplPlt.text(2, 0.315, "mittlere Windgeschwindigkeit = %.2f [m/s]" %(w,), fontdict=None, fontsize=10)
                self.mplPlt.text(2, 0.29, unicode("mittlere Rauhigkeitsl\344nge = %.2f [m]"%(z0,), 'latin-1'),  fontsize=10)
                self.mplFig.canvas.draw()
                
            except ZeroDivisionError:
                self.iface.messageBar().pushMessage("Weibullauswertung: Fehler", 
                "Division mit 0 nicht erlaubt. Falsche Layerzuordnung?",  level=QgsMessageBar.CRITICAL)
      
    # taken from valuetool plugin
    def invalidatePlot(self,replot=True):
        self.statsChecked = False
        if self.mplLine is not None:
            del self.mplLine
            self.mplLine = None
        #update empty plot
        if replot and self.cbxGraph.isChecked():
            #self.values=[]
            self.printValue( None )

    # taken from valuetool plugin
    def resizeEvent(self, event):
        self.invalidatePlot()

    # Erstellen der Weibullfunktion als PNG für die aktuelle Mausposition
    def savePNG(self):
    
        # Mittlere Windgeschwindigkeit
        w = float(self.sampleRaster(self.InRastW.currentText(), self.xCoord, self.yCoord))/10
        # Weibullparameter C
        c = float(self.sampleRaster(self.InRastC.currentText(), self.xCoord, self.yCoord))/10
        # Weibullparameter K
        k = float(self.sampleRaster(self.InRastK.currentText(), self.xCoord, self.yCoord))/1000
        # mittlere Rauhigkeit (Mittelwerte auf Basis des angegebenen Radius)
        z0 = self.meanBuffer()
        
        #Haeufigkeit aus der Weibull-Dichtefunktion durch Integration
        y = lambda x: k/c*(x/c)**(k-1)*numpy.exp(-(x/c)**k)
        rh=integrate.romberg(y,0.,1.0)
        rh=round(rh*100,1)
        
        # Weibull Dichte Funktion fur Grafik
        def f(x):        
            return k/c*(x/c)**(k-1)*numpy.exp(-(x/c)**k)
        X = numpy.linspace(0, 12, 1200)
        Y = f(X)

        # Speicherdialog öffen und Ausgabename definieren
        
        self.standortname = self.dataName.text()  
      
        if self.dataName.text() == '':
            QMessageBox.warning( self, self.tr( "Weibullanalyse: Fehler" ),
                           self.tr( "Bitte Standortnamen eintragen" ) )
        else:
            self.standortname = self.dataName.text()  
            self.fileName = QFileDialog.getSaveFileName(self.iface.mainWindow(), "Save As", self.standortname + ".png","Portable Network Graphics (*.png)")
    
        # Plot Rahmen Beschriftungen etc   
        plt.figure().set_size_inches(7,7)  
        plt.axes().set_aspect('44')
        plt.plot(X, Y, linewidth=3, label=None)
        plt.title("%s"%(self.standortname,), fontsize=18)
        plt.xlabel("Geschwindigkeit [m/s]", fontsize=18)
        plt.ylabel((unicode('relative H\344ufigkeit', 'latin-1')), fontsize=18)
        plt.ylim(0,0.36)       
        plt.xlim(0,16)

        #Beschriftungen in der Grafik, Startposition uber Wertepaar
        plt.text(5, 0.305, "Statistische Parameter:",  fontsize=14)
        plt.text(5, 0.285, unicode('rel. H\344ufigkeit < 1 m/s = %.2f'%(rh,), 'latin-1'))
        plt.text(12.7, 0.285, unicode('\045', 'latin-1'))
        plt.text(5, 0.27, "mittl. Windgeschwindigkeit = %.2f [m/s]"%(w,), fontdict=None)
        plt.text(5, 0.255, unicode("mittl. Rauhigkeitsl\344nge = %.2f [m]"%(z0,), 'latin-1'))

        # Plot vertikale Beschriftung mit Koordinaten
        plt.text(16.2, 0.325, '$\copyright$ ArguSoft', rotation=90)
        plt.text(16.2, 0.18, "Weibull %d / %d"%(self.yCoord,self.xCoord), rotation=90)
   
        # Gitter anzeigen und Plot erstellen zum Abspeichern
        plt.grid(True)
        
        # Weibullkurve speichern
        plt.savefig(self.fileName, dpi=300, facecolor='0.9', edgecolor='w',
        orientation='portrait', papertype=None, format='png',
        transparent=False, bbox_inches=None, pad_inches=0.1)


