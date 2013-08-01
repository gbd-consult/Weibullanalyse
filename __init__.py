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

# load valuetool class from file valuetool.py

def name(): 
    return 'Weibullauswertung'

def description():
    return 'Berechnung und Darstellung einer Weibullauswertung für Windenergiestandorte' 

def version(): 
    return 'Version 0.1'

def qgisMinimumVersion():
    return '2.0'

def author():
    return "dassau@gbd-consult.de"

def email():
    return "dassau@gbd-consult.de"

def category():
    return 'Raster'

def authorName():
    return 'Otto Dassau'

def icon():
    return "icon.png"

def classFactory(iface):
    # load WeibullAnalyse class from file WeibullAnalyse
    from weibullanalyse import ValueTool
    return ValueTool(iface)

## später ueberfluessig
#def classFactory(iface): 
#    from valuetool import ValueTool
#    return ValueTool(iface)


