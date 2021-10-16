from qgis.PyQt import QtGui

fn = "C:/Users/George McNamara/Documents/Geospatial Programming/Module_5/QGIS project/select_freeway.shp"

layer = QgsVectorLayer(fn, 'freeway_priority', 'ogr')

tf = 'ALLVEHS_AA'
rangeList = []
opacity = 1

#create colour for first range
minVal = 0
maxVal = 19999

lab = 'Priority 1'

color1 = QtGui.QColor('#3DA1D1')

symbol = QgsSymbol.defaultSymbol(layer.geometryType())
symbol.setColor(color1)
symbol.setOpacity(opacity)

range1 = QgsRendererRange(minVal, maxVal, symbol, lab)
rangeList.append(range1)

#create colour for second range
minVal = 20000
maxVal = 39999

lab = 'Priority 2'

color2 = QtGui.QColor('#9AC5B4')

symbol = QgsSymbol.defaultSymbol(layer.geometryType())
symbol.setColor(color2)
symbol.setOpacity(opacity)

range2 = QgsRendererRange(minVal, maxVal, symbol, lab)
rangeList.append(range2)

#create colour for third range
minVal = 40000
maxVal = 59999

lab = 'Priority 3'

color3 = QtGui.QColor('#98E600')

symbol = QgsSymbol.defaultSymbol(layer.geometryType())
symbol.setColor(color3)
symbol.setOpacity(opacity)

range3 = QgsRendererRange(minVal, maxVal, symbol, lab)
rangeList.append(range3)

#create colour for fourth range
minVal = 60000
maxVal = 79999

lab = 'Priority 4'

color4 = QtGui.QColor('#F6D865')

symbol = QgsSymbol.defaultSymbol(layer.geometryType())
symbol.setColor(color4)
symbol.setOpacity(opacity)

range4 = QgsRendererRange(minVal, maxVal, symbol, lab)
rangeList.append(range4)

#create colour for fifth range
minVal = 80000
maxVal = 99999

lab = 'Priority 5'

color5 = QtGui.QColor('#F88F3E')

symbol = QgsSymbol.defaultSymbol(layer.geometryType())
symbol.setColor(color5)
symbol.setOpacity(opacity)

range5 = QgsRendererRange(minVal, maxVal, symbol, lab)
rangeList.append(range5)

#create colour for sixth range
minVal = 100000
maxVal = 119999

lab = 'Priority 6'

color6 = QtGui.QColor('#F0261C')

symbol = QgsSymbol.defaultSymbol(layer.geometryType())
symbol.setColor(color6)
symbol.setOpacity(opacity)

range6 = QgsRendererRange(minVal, maxVal, symbol, lab)
rangeList.append(range6)

#apply ranges
groupRenderer = QgsGraduatedSymbolRenderer('', rangeList)
groupRenderer.setMode(QgsGraduatedSymbolRenderer.EqualInterval)
groupRenderer.setClassAttribute(tf)

layer.setRenderer(groupRenderer)

QgsProject.instance().addMapLayer(layer)