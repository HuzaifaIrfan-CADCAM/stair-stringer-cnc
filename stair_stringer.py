import freecad_env






# Parameters
stringer_thickness = 1.5  # mm
first_rise_height = 6.62
rise_height = 7.625
num_rise = 16
run_depth = 11.5
num_run = 15
kicker_depth = 5.5
kicker_height = 1.5

def inch(inches: float) -> float:
    """Convert inches to millimeters."""
    return inches * 25.4

# Define parameters in inches, convert to mm
stringer_thickness = inch(stringer_thickness)
first_rise_height  = inch(first_rise_height)
rise_height        = inch(rise_height)
num_rise           = 16
run_depth          = inch(run_depth)
num_run            = 15
kicker_depth       = inch(kicker_depth)
kicker_height      = inch(kicker_height)

import FreeCAD, Part

import FreeCAD as App
import Part, PartDesign, Sketcher
from FreeCAD import Vector

doc_name="StairStringerFixed"

doc = App.newDocument(doc_name)
# App.setActiveDocument(doc_name)
# App.ActiveDocument=App.getDocument(doc_name)

body=doc.addObject('PartDesign::Body','Body')
body.Label = 'Body'

sketch=body.newObject('Sketcher::SketchObject','Sketch')
sketch.AttachmentSupport = (doc.getObject('XY_Plane'),[''])
sketch.MapMode = 'FlatFace'


# run_depth - kicker_depth
first_point=(run_depth,0.000000,0)
current_x, current_y, current_z = first_point
previous_vector=App.Vector(current_x, current_y, current_z)
current_x += -(run_depth - kicker_depth)
current_y += 0
current_vector=App.Vector(current_x, current_y, current_z)
sketch.addGeometry(Part.LineSegment(previous_vector,current_vector),False)
# sketch.addGeometry(Part.LineSegment(App.Vector(28.786367,0.000000,0),App.Vector(18.101997,0.000000,0)),False)
# sketch.addConstraint(Sketcher.Constraint('PointOnObject',0,1,-1)) 
# sketch.addConstraint(Sketcher.Constraint('PointOnObject',0,2,-1))
# sketch.addConstraint(Sketcher.Constraint('Horizontal',0)) 
sketch.addConstraint(Sketcher.Constraint('Distance',0,2,0,1,run_depth - kicker_depth))

# kicker_height
previous_vector=current_vector
current_x += 0
current_y += kicker_height
current_vector=App.Vector(current_x, current_y, current_z)
sketch.addGeometry(Part.LineSegment(previous_vector,current_vector),False)
# sketch.addGeometry(Part.LineSegment(App.Vector(18.101997,0.000000,0),App.Vector(18.248360,7.090004,0)),False)
sketch.addConstraint(Sketcher.Constraint('Coincident',0,2,1,1)) 
# sketch.addConstraint(Sketcher.Constraint('Vertical',1)) 
sketch.addConstraint(Sketcher.Constraint('Perpendicular',0,1))
sketch.addConstraint(Sketcher.Constraint('Distance',1,1,1,2,kicker_height))

# kicker_depth
previous_vector=current_vector
current_x += -(kicker_depth)
current_y += 0
current_vector=App.Vector(current_x, current_y, current_z)
sketch.addGeometry(Part.LineSegment(previous_vector,current_vector),False)
# sketch.addGeometry(Part.LineSegment(App.Vector(18.248360,7.090004,0),App.Vector(0.000000,6.650920,0)),False)
sketch.addConstraint(Sketcher.Constraint('Coincident',1,2,2,1)) 
# sketch.addConstraint(Sketcher.Constraint('PointOnObject',2,2,-2)) 
# sketch.addConstraint(Sketcher.Constraint('Horizontal',2)) 
sketch.addConstraint(Sketcher.Constraint('Perpendicular',1,2))
sketch.addConstraint(Sketcher.Constraint('Distance',2,2,2,1,kicker_depth)) 

# first_rise_height - kicker_height
previous_vector=current_vector
current_x += 0
current_y += first_rise_height - kicker_height
current_vector=App.Vector(current_x, current_y, current_z)
sketch.addGeometry(Part.LineSegment(previous_vector,current_vector),False)
# sketch.addGeometry(Part.LineSegment(App.Vector(0.000000,6.650920,0),App.Vector(0.000000,13.922371,0)),False)
sketch.addConstraint(Sketcher.Constraint('Coincident',2,2,3,1)) 
# sketch.addConstraint(Sketcher.Constraint('PointOnObject',3,2,-2)) 
# sketch.addConstraint(Sketcher.Constraint('Vertical',3)) 
sketch.addConstraint(Sketcher.Constraint('Perpendicular',2,3))
sketch.addConstraint(Sketcher.Constraint('Distance',3,1,3,2,first_rise_height - kicker_height)) 

# run_depth
previous_vector=current_vector
current_x += run_depth
current_y += 0
current_vector=App.Vector(current_x, current_y, current_z)
sketch.addGeometry(Part.LineSegment(previous_vector,current_vector),False)
# sketch.addGeometry(Part.LineSegment(App.Vector(0.000000,13.922371,0),App.Vector(29.782467,14.664711,0)),False)
sketch.addConstraint(Sketcher.Constraint('Coincident',3,2,4,1)) 
# sketch.addConstraint(Sketcher.Constraint('Horizontal',4)) 
sketch.addConstraint(Sketcher.Constraint('Perpendicular',3,4))
sketch.addConstraint(Sketcher.Constraint('Distance',4,1,4,2,run_depth)) 

# Rise and Run in Loop

i=5

for _ in range(0,num_run-1):
    # rise_height
    previous_vector=current_vector
    current_x += 0
    current_y += rise_height
    current_vector=App.Vector(current_x, current_y, current_z)
    sketch.addGeometry(Part.LineSegment(previous_vector,current_vector),False)
    # sketch.addGeometry(Part.LineSegment(App.Vector(29.782467,14.664711,0),App.Vector(30.000813,27.547087,0)),False)
    sketch.addConstraint(Sketcher.Constraint('Coincident',i-1,2,i,1)) 
    # sketch.addConstraint(Sketcher.Constraint('Vertical',i)) 
    sketch.addConstraint(Sketcher.Constraint('Perpendicular',i-1,i))
    sketch.addConstraint(Sketcher.Constraint('Distance',i,1,i,2,rise_height)) 
    i+=1

    # run_depth
    previous_vector=current_vector
    current_x += run_depth
    current_y += 0
    current_vector=App.Vector(current_x, current_y, current_z)
    sketch.addGeometry(Part.LineSegment(previous_vector,current_vector),False)
    # sketch.addGeometry(Part.LineSegment(App.Vector(30.000813,27.547087,0),App.Vector(48.996853,27.765432,0)),False)
    sketch.addConstraint(Sketcher.Constraint('Coincident',i-1,2,i,1)) 
    # sketch.addConstraint(Sketcher.Constraint('Horizontal',i))
    sketch.addConstraint(Sketcher.Constraint('Perpendicular',i-1,i))
    sketch.addConstraint(Sketcher.Constraint('Distance',i,1,i,2,run_depth)) 
    i+=1

# end rise reverse, rise_height
previous_vector=current_vector
current_x += 0
current_y += -(rise_height)
current_vector=App.Vector(current_x, current_y, current_z)
sketch.addGeometry(Part.LineSegment(previous_vector,current_vector),False)
# sketch.addGeometry(Part.LineSegment(App.Vector(48.996853,27.765432,0),App.Vector(49.215199,14.228024,0)),False)
sketch.addConstraint(Sketcher.Constraint('Coincident',i-1,2,i,1)) 
# sketch.addConstraint(Sketcher.Constraint('Vertical',i))
sketch.addConstraint(Sketcher.Constraint('Perpendicular',i-1,i))
sketch.addConstraint(Sketcher.Constraint('Distance',i,2,i,1,rise_height)) 
i+=1

# close loop path
previous_vector=current_vector
current_x, current_y, current_z = first_point
current_vector=App.Vector(current_x, current_y, current_z)
sketch.addGeometry(Part.LineSegment(previous_vector,current_vector),False)
# sketch.addGeometry(Part.LineSegment(App.Vector(49.215199,14.228024,0),App.Vector(28.786367,0.000000,0)),False)
sketch.addConstraint(Sketcher.Constraint('Coincident',i-1,2,i,1)) 
sketch.addConstraint(Sketcher.Constraint('Coincident',i,2,0,1))



# sketch.delConstraint(10)#11
# sketch.delConstraint(2)#3
# 35
# 33
# 31
# 29
# 27
# 25
# 23
# 21

# run_depth - kicker_depth
# sketch.addConstraint(Sketcher.Constraint('Distance',0,1,0,2,run_depth - kicker_depth))
# sketch.addConstraint(Sketcher.Constraint('DistanceX',0,2,0,1,run_depth - kicker_depth))

# kicker_height
# sketch.addConstraint(Sketcher.Constraint('DistanceY',1,1,1,2,kicker_height))
# sketch.addConstraint(Sketcher.Constraint('Distance',1,1,1,2,6.276437)) 

# kicker_depth
# sketch.addConstraint(Sketcher.Constraint('Distance',2,1,2,2,kicker_depth))
# sketch.addConstraint(Sketcher.Constraint('DistanceX',2,2,2,1,kicker_depth)) 

# first_rise_height - kicker_height
# sketch.addConstraint(Sketcher.Constraint('Distance',3,1,3,2,first_rise_height - kicker_height)) 
# sketch.addConstraint(Sketcher.Constraint('DistanceY',3,1,3,2,first_rise_height - kicker_height)) 


# run_depth
# sketch.addConstraint(Sketcher.Constraint('Distance',4,1,4,2,run_depth)) 
# sketch.addConstraint(Sketcher.Constraint('DistanceX',4,1,4,2,run_depth)) 


# Rise and Run in Loop
 
# i=5

# for _ in range(0,num_run-1):
#     # rise_height
#     # sketch.addConstraint(Sketcher.Constraint('Distance',5,1,5,2,rise_height)) 
#     sketch.addConstraint(Sketcher.Constraint('DistanceY',i,1,i,2,rise_height)) 
#     i+=1

#     # run_depth
#     # sketch.addConstraint(Sketcher.Constraint('Distance',6,1,6,2,run_depth)) 
#     sketch.addConstraint(Sketcher.Constraint('DistanceX',i,1,i,2,run_depth)) 
#     i+=1


# end rise reverse, rise_height
# sketch.addConstraint(Sketcher.Constraint('Distance',7,1,7,2,rise_height))
# sketch.addConstraint(Sketcher.Constraint('DistanceY',i,2,i,1,rise_height)) 


pad=body.newObject('PartDesign::Pad','Pad')
pad.Profile = (sketch, ['',])
pad.Length = stringer_thickness
pad.ReferenceAxis = (sketch,['N_Axis'])
sketch.Visibility = False

pad.Length = stringer_thickness
pad.TaperAngle = 0.000000
pad.UseCustomVector = 0
pad.Direction = (0, 0, 1)
pad.ReferenceAxis = (sketch, ['N_Axis'])
pad.AlongSketchNormal = 1
pad.Type = 0
pad.UpToFace = None
pad.Reversed = 0
pad.Midplane = 0
pad.Offset = 0

sketch.Visibility = False
body.Visibility = True
pad.Visibility = True


doc.recompute()


import os

current_directory = os.getcwd()
print("Current Working Directory:", current_directory)

file_name="stair_stringer"
output_folder=f"{current_directory}/output/"
doc_file_name=f"{output_folder}/{file_name}.FCStd"
doc.saveAs(doc_file_name)
print(f"doc_file_name: {doc_file_name}")

__objs__ = []
__objs__.append(body)
import importers.importOBJ

obj_file_name=f"{output_folder}/{file_name}.obj"
print(f"obj_file_name: {obj_file_name}")
if hasattr(importers.importOBJ, "exportOptions"):
    options = importers.importOBJ.exportOptions(obj_file_name)
    importers.importOBJ.export(__objs__,obj_file_name, options)
else:
    importers.importOBJ.export(__objs__, obj_file_name)

del __objs__


__objs__ = []
__objs__.append(body)
import Mesh
stl_file_name=f"{output_folder}/{file_name}.stl"
print(f"stl_file_name: {stl_file_name}")
if hasattr(Mesh, "exportOptions"):
    options = Mesh.exportOptions(stl_file_name)
    Mesh.export(__objs__, stl_file_name, options)
else:
    Mesh.export(__objs__, stl_file_name)

del __objs__


__objs__ = []
__objs__.append(body)
import importDXF
dxf_file_name=f"{output_folder}/{file_name}.dxf"
print(f"dxf_file_name: {dxf_file_name}")
if hasattr(importDXF, "exportOptions"):
    options = importDXF.exportOptions(dxf_file_name)
    importDXF.export(__objs__, dxf_file_name, options)
else:
    importDXF.export(__objs__, dxf_file_name)

del __objs__


# __objs__ = []
# __objs__.append(body)

# import ImportGui
# step_file_name=f"{output_folder}/{file_name}.step"
# print(f"step_file_name: {step_file_name}")
# if hasattr(ImportGui, "exportOptions"):
#     options = ImportGui.exportOptions(step_file_name)
#     ImportGui.export(__objs__, step_file_name, options)
# else:
#     ImportGui.export(__objs__, step_file_name)

# del __objs__


