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

from PyQt5.QtWidgets import QDockWidget, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from qgis.core import *

from .weibullanalysedialog import ValueWidget

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
        self.valuedockwidget.visibilityChanged.connect(self.valuewidget.changeActive)
        self.valuedockwidget.setVisible(True)
    
        # add the dockwidget to iface
        self.iface.addDockWidget(Qt.LeftDockWidgetArea,self.valuedockwidget)

        # add action to menu
        self.action = QAction("Weibullanalyse Tool",parent=self.iface.mainWindow())
        self.iface.addPluginToRasterMenu("argusim", self.action)
        self.action.setCheckable(True)
        self.action.setEnabled(True)
        self.action.setChecked(True)
        self.action.toggled.connect(self.toggleWidget)


    def toggleWidget(self, state):
        if state:
            self.valuedockwidget.setVisible(True)
        else:
            self.valuedockwidget.setVisible(False)


    #Qt.AllDockWidgetAreas
    def unload(self):
        self.valuedockwidget.close()
        self.valuewidget.disconnect()
        # remove the dockwidget from iface
        self.iface.removeDockWidget(self.valuedockwidget)
        # remove the plugin menu item and icon
        self.iface.removePluginMenu("argusim", self.action)
