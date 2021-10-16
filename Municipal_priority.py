from qgis.PyQt import QtGui

fn = "C:/Users/George McNamara/Documents/Geospatial Programming/Module_5/QGIS project/select_municipal.shp"

layer = QgsVectorLayer(fn, 'municipal_priority', 'ogr')

tf = 'ALLVEHS_AA'
rangeList = []
opacity = 1

#create colour for first range
minVal = 0
maxVal = 999

lab = 'Priority 1'

color1 = QtGui.QColor('#007206')

symbol = QgsSymbol.defaultSymbol(layer.geometryType())
symbol.setColor(color1)
symbol.setOpacity(opacity)

range1 = QgsRendererRange(minVal, maxVal, symbol, lab)
rangeList.append(range1)

#create colour for second range
minVal = 1000
maxVal = 1999

lab = 'Priority 2'

color2 = QtGui.QColor('#33910D')

symbol = QgsSymbol.defaultSymbol(layer.geometryType())
symbol.setColor(color2)
symbol.setOpacity(opacity)

range2 = QgsRendererRange(minVal, maxVal, symbol, lab)
rangeList.append(range2)

#create colour for third range
minVal = 2000
maxVal = 2999

lab = 'Priority 3'

color3 = QtGui.QColor('#6FB113')

symbol = QgsSymbol.defaultSymbol(layer.geometryType())
symbol.setColor(color3)
symbol.setOpacity(opacity)

range3 = QgsRendererRange(minVal, maxVal, symbol, lab)
rangeList.append(range3)

#create colour for fourth range
minVal = 3000
maxVal = 3999

lab = 'Priority 4'

color4 = QtGui.QColor('#A4D016')

symbol = QgsSymbol.defaultSymbol(layer.geometryType())
symbol.setColor(color4)
symbol.setOpacity(opacity)

range4 = QgsRendererRange(minVal, maxVal, symbol, lab)
rangeList.append(range4)

#create colour for fifth range
minVal = 4000
maxVal = 4999

lab = 'Priority 5'

color5 = QtGui.QColor('#D8F01D')

symbol = QgsSymbol.defaultSymbol(layer.geometryType())
symbol.setColor(color5)
symbol.setOpacity(opacity)

range5 = QgsRendererRange(minVal, maxVal, symbol, lab)
rangeList.append(range5)

#create colour for sixth range
minVal = 5000
maxVal = 5999

lab = 'Priority 6'

color6 = QtGui.QColor('#F7EE1E')

symbol = QgsSymbol.defaultSymbol(layer.geometryType())
symbol.setColor(color6)
symbol.setOpacity(opacity)

range6 = QgsRendererRange(minVal, maxVal, symbol, lab)
rangeList.append(range6)

#create colour for seventh range
minVal = 6000
maxVal = 6999

lab = 'Priority 7'

color7 = QtGui.QColor('#FCC813')

symbol = QgsSymbol.defaultSymbol(layer.geometryType())
symbol.setColor(color7)
symbol.setOpacity(opacity)

range7 = QgsRendererRange(minVal, maxVal, symbol, lab)
rangeList.append(range7)

#create colour for eight range
minVal = 7000
maxVal = 7999

lab = 'Priority 8'

color8 = QtGui.QColor('#FCA210')

symbol = QgsSymbol.defaultSymbol(layer.geometryType())
symbol.setColor(color8)
symbol.setOpacity(opacity)

range8 = QgsRendererRange(minVal, maxVal, symbol, lab)
rangeList.append(range8)

#create colour for ninth range
minVal = 8000
maxVal = 8999

lab = 'Priority 9'

color9 = QtGui.QColor('#FF760C')

symbol = QgsSymbol.defaultSymbol(layer.geometryType())
symbol.setColor(color9)
symbol.setOpacity(opacity)

range9 = QgsRendererRange(minVal, maxVal, symbol, lab)
rangeList.append(range9)

#create colour for tenth range
minVal = 9000
maxVal = 9999

lab = 'Priority 10'

color10 = QtGui.QColor('#FC3B09')

symbol = QgsSymbol.defaultSymbol(layer.geometryType())
symbol.setColor(color10)
symbol.setOpacity(opacity)

#create colour for eleventh range
minVal = 10000
maxVal = 19999

lab = 'Priority 11'

color11 = QtGui.QColor('#A80000')

symbol = QgsSymbol.defaultSymbol(layer.geometryType())
symbol.setColor(color11)
symbol.setOpacity(opacity)

range11 = QgsRendererRange(minVal, maxVal, symbol, lab)
rangeList.append(range11)

#create colour for twelfth range
minVal = 20000
maxVal = 35000

lab = 'Priority 12'

color12 = QtGui.QColor('#730000')

symbol = QgsSymbol.defaultSymbol(layer.geometryType())
symbol.setColor(color12)
symbol.setOpacity(opacity)

range12 = QgsRendererRange(minVal, maxVal, symbol, lab)
rangeList.append(range12)

#apply ranges
groupRenderer = QgsGraduatedSymbolRenderer('', rangeList)
groupRenderer.setMode(QgsGraduatedSymbolRenderer.EqualInterval)
groupRenderer.setClassAttribute(tf)

layer.setRenderer(groupRenderer)

QgsProject.instance().addMapLayer(layer)