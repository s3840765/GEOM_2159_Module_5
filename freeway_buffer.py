from qgis import *
from qgis import processing

filepath = "C:/Users/George McNamara/Documents/Geospatial Programming/Module_5/QGIS project/"
outputfilepath = "C:/Users/George McNamara/Documents/Geospatial Programming/Module_5/QGIS project/"

select_freeway = "select_freeway.shp"
buffer_output = "freeway_buffer.shp"

selectedfreeway = iface.addVectorLayer(filepath + select_freeway, select_freeway[:-4], 'ogr')


processing.run("native:buffer",
    {
        'INPUT': selectedfreeway,
        'DISTANCE': 500,
        'SEGMENTS': 5,
        'END_CAP_STYLE': 0,
        'JOIN_STYLE': 1,
        'MITER_LIMIT': 2,
        'DISSOLVE': False,
        'OUTPUT': outputfilepath + buffer_output
    }
)


buffer_Layer = iface.addVectorLayer(filepath+buffer_output,buffer_output[:-4],"ogr")