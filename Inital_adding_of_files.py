from qgis import *
from qgis import processing

filepath = "C:/Users/George McNamara/Documents/Geospatial Programming/Module_5/QGIS project/"
outputfilepath = "C:/Users/George McNamara/Documents/Geospatial Programming/Module_5/QGIS project/"

Traffic_Filename = "Traffic_Volume.shp"

Traffic = iface.addVectorLayer(filepath + Traffic_Filename, Traffic_Filename[:-4], 'ogr')


