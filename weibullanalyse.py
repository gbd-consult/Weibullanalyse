# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WeibullAnalyse
                                 A QGIS plugin
 Weibullauswertung für Windenergiestandorte
                             -------------------
        begin                : 2013-01-08
        copyright            : (C) 2013 by Otto Dassau
        email                : dassau@gbd-consult.de
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

from weibullanalysedialog import ValueWidget

# initialize Qt resources from file resouces.py
# import resources

# angepasst vom Plugin 'valuetool'
class ValueTool:
    def __init__(self, iface):
        # save reference to the QGIS interface
        self.iface = iface

    def initGui(self):
        # create the widget to display information
        self.valuewidget = ValueWidget(self.iface)
        # create dockwidget with correct parent and add the valuewidget
        self.valuedockwidget=QDockWidget("Weibullanalyse Tool" , self.iface.mainWindow() )
        self.valuedockwidget.setObjectName("Weibullanalyse Tool")
        self.valuedockwidget.setWidget(self.valuewidget)
        QObject.connect(self.valuedockwidget, SIGNAL('visibilityChanged ( bool )'), self.showHideDockWidget)
    
        # add the dockwidget to iface
        self.iface.addDockWidget(Qt.LeftDockWidgetArea,self.valuedockwidget)

    #Qt.AllDockWidgetAreas
    def unload(self):
        self.valuedockwidget.close()
        self.valuewidget.disconnect()
        # remove the dockwidget from iface
        self.iface.removeDockWidget(self.valuedockwidget)
        # remove the plugin menu item and icon

    def showHideDockWidget( self ):
        if self.valuedockwidget.isVisible() and self.valuewidget.cbxActive.isChecked():
            state = Qt.Checked
        else:
            state = Qt.Unchecked
        self.valuewidget.changeActive( state )
