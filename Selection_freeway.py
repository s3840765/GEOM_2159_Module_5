layers = QgsProject.instance().mapLayersByName('Traffic_Volume')
layer = layers[0]
layer.selectByExpression("\"RMA_CLSF_1\" = 'FREEWAY'")

fn = "C:/Users/George McNamara/Documents/Geospatial Programming/Module_5/QGIS project/select_freeway.shp"
writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn, 'utf-8', \
driverName='ESRI Shapefile', onlySelected= True)
selected_layer = iface.addVectorLayer(fn, '', 'ogr')
del(writer) 