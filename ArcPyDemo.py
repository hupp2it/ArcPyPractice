print("ArcPyDemo practice file")
import arcpy

arcpy.AddField_management("c:/data/Portland.gdb/streets", "LENGTH_MILES", "TEXT")
arcpy.CalculateField_management("c:/data/Portland.gdb/streets", "LENGTH_MILES", "!shape.length@miles!", "PYTHON_9.3")
arcpy.FeatureClassToFeatureClass_conversion("c:/data/Portland.gdb/streets",
                                            "Database Connections/MySDE.sde/PortlandDataset", "streets")

# learned that I need to get python 2.7 i order to run ArcPy
# going to try to DL the old python when I'm in the desert


arcpy.AddField_management("c:/data/Portland.gdb/streets", "LENGTH_MILES", "TEXT")
arcpy.CalculateField_management("c:/data/Portland.gdb/streets", "LENGTH_MILES", "!shape.length@miles!", "PYTHON_9.3")
arcpy.FeatureClassToFeatureClass_conversion("c:/data/Portland.gdb/streets",
                                            "Database Connections/MySDE.sde/PortlandDataset", "streets")
