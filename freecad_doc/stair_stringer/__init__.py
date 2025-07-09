
import freecad_env

import FreeCAD, Part

import FreeCAD as App
import Part, PartDesign, Sketcher
from FreeCAD import Vector


import math

def inch_to_mm(inches: float) -> float:
    """Convert inches to millimeters."""
    return inches * 25.4

def create_stair_stringer(doc, body_name, stringer_thickness, first_rise_height, rise_height, num_rise, run_depth, num_run, kicker, kicker_depth, kicker_height, stair_angle, back_cut_increase, rotate_for_cnc):
    

    # Parameters
    # stringer_thickness = 1.5  # mm
    # first_rise_height = 6.62
    # rise_height = 7.625
    # num_rise = 16
    # run_depth = 11.5
    # num_run = 15
    # kicker=True
    # kicker_depth = 5.5
    # kicker_height = 1.5

    # stair_angle=33.5
    # back_cut_increase=5

    # rotate_for_cnc=True





    # Convert degrees to radians
    stair_angle_rad = math.radians(stair_angle)


    # Define parameters in inches, convert to mm
    stringer_thickness = inch_to_mm(stringer_thickness)
    first_rise_height  = inch_to_mm(first_rise_height)
    rise_height        = inch_to_mm(rise_height)
    # num_rise           = 16
    run_depth          = inch_to_mm(run_depth)
    # num_run            = 15
    kicker_depth       = inch_to_mm(kicker_depth)
    kicker_height      = inch_to_mm(kicker_height)

    # stair back cut more according to real lumber work piece
    first_bottom_run_depth=run_depth+inch_to_mm(back_cut_increase)
    last_reverse_rise_height=rise_height+inch_to_mm(back_cut_increase)



    body=doc.addObject('PartDesign::Body',body_name)
    body.Label = body_name

    sketch=body.newObject('Sketcher::SketchObject','Stringer_Sketch')
    sketch.AttachmentSupport = (doc.getObject('XY_Plane'),[''])
    sketch.MapMode = 'FlatFace'

    i=0
    # run_depth - kicker_depth
    first_point=(first_bottom_run_depth,0.000000,0)
    current_x, current_y, current_z = first_point
    previous_vector=App.Vector(current_x, current_y, current_z)
    if kicker:
        current_x += -(first_bottom_run_depth - kicker_depth)
    else:
        current_x += -(first_bottom_run_depth)
    current_y += 0
    current_vector=App.Vector(current_x, current_y, current_z)
    sketch.addGeometry(Part.LineSegment(previous_vector,current_vector),False)
    # sketch.addGeometry(Part.LineSegment(App.Vector(28.786367,0.000000,0),App.Vector(18.101997,0.000000,0)),False)
    # sketch.addConstraint(Sketcher.Constraint('PointOnObject',0,1,-1)) 
    # sketch.addConstraint(Sketcher.Constraint('PointOnObject',0,2,-1))
    # sketch.addConstraint(Sketcher.Constraint('Horizontal',0))
    if kicker:
        sketch.addConstraint(Sketcher.Constraint('Distance',i,2,i,1,first_bottom_run_depth - kicker_depth))
    else:
        sketch.addConstraint(Sketcher.Constraint('Distance',i,2,i,1,first_bottom_run_depth))
    i+=1

    if kicker:
        # kicker_height
        previous_vector=current_vector
        current_x += 0
        current_y += kicker_height
        current_vector=App.Vector(current_x, current_y, current_z)
        sketch.addGeometry(Part.LineSegment(previous_vector,current_vector),False)
        # sketch.addGeometry(Part.LineSegment(App.Vector(18.101997,0.000000,0),App.Vector(18.248360,7.090004,0)),False)
        sketch.addConstraint(Sketcher.Constraint('Coincident',i-1,2,i,1)) 
        # sketch.addConstraint(Sketcher.Constraint('Vertical',1)) 
        sketch.addConstraint(Sketcher.Constraint('Perpendicular',i-1,i))
        sketch.addConstraint(Sketcher.Constraint('Distance',i,1,i,2,kicker_height))
        i+=1

        # kicker_depth
        previous_vector=current_vector
        current_x += -(kicker_depth)
        current_y += 0
        current_vector=App.Vector(current_x, current_y, current_z)
        sketch.addGeometry(Part.LineSegment(previous_vector,current_vector),False)
        # sketch.addGeometry(Part.LineSegment(App.Vector(18.248360,7.090004,0),App.Vector(0.000000,6.650920,0)),False)
        sketch.addConstraint(Sketcher.Constraint('Coincident',i-1,2,i,1)) 
        # sketch.addConstraint(Sketcher.Constraint('PointOnObject',2,2,-2)) 
        # sketch.addConstraint(Sketcher.Constraint('Horizontal',2)) 
        sketch.addConstraint(Sketcher.Constraint('Perpendicular',i-1,i))
        sketch.addConstraint(Sketcher.Constraint('Distance',i,2,i,1,kicker_depth))
        i+=1

    # first_rise_height - kicker_height
    previous_vector=current_vector
    current_x += 0
    if kicker:
        current_y += first_rise_height - kicker_height
    else:
        current_y += first_rise_height 
    current_vector=App.Vector(current_x, current_y, current_z)
    sketch.addGeometry(Part.LineSegment(previous_vector,current_vector),False)
    # sketch.addGeometry(Part.LineSegment(App.Vector(0.000000,6.650920,0),App.Vector(0.000000,13.922371,0)),False)
    sketch.addConstraint(Sketcher.Constraint('Coincident',i-1,2,i,1)) 
    # sketch.addConstraint(Sketcher.Constraint('PointOnObject',3,2,-2)) 
    # sketch.addConstraint(Sketcher.Constraint('Vertical',3)) 
    sketch.addConstraint(Sketcher.Constraint('Perpendicular',i-1,i))
    if kicker:
        sketch.addConstraint(Sketcher.Constraint('Distance',i,1,i,2,first_rise_height - kicker_height)) 
    else:
        sketch.addConstraint(Sketcher.Constraint('Distance',i,1,i,2,first_rise_height)) 
    i+=1

    # run_depth
    previous_vector=current_vector
    current_x += run_depth
    current_y += 0
    current_vector=App.Vector(current_x, current_y, current_z)
    sketch.addGeometry(Part.LineSegment(previous_vector,current_vector),False)
    # sketch.addGeometry(Part.LineSegment(App.Vector(0.000000,13.922371,0),App.Vector(29.782467,14.664711,0)),False)
    sketch.addConstraint(Sketcher.Constraint('Coincident',i-1,2,i,1)) 
    # sketch.addConstraint(Sketcher.Constraint('Horizontal',4)) 
    sketch.addConstraint(Sketcher.Constraint('Perpendicular',i-1,i))
    sketch.addConstraint(Sketcher.Constraint('Distance',i,1,i,2,run_depth)) 
    i+=1
    # Rise and Run in Loop

    # i=5

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

    # end rise reverse, last_reverse_rise_height 
    previous_vector=current_vector
    current_x += 0
    current_y += -(last_reverse_rise_height)
    current_vector=App.Vector(current_x, current_y, current_z)
    sketch.addGeometry(Part.LineSegment(previous_vector,current_vector),False)
    # sketch.addGeometry(Part.LineSegment(App.Vector(48.996853,27.765432,0),App.Vector(49.215199,14.228024,0)),False)
    sketch.addConstraint(Sketcher.Constraint('Coincident',i-1,2,i,1)) 
    # sketch.addConstraint(Sketcher.Constraint('Vertical',i))
    sketch.addConstraint(Sketcher.Constraint('Perpendicular',i-1,i))
    sketch.addConstraint(Sketcher.Constraint('Distance',i,2,i,1,last_reverse_rise_height)) 
    i+=1


    # close loop path
    previous_vector=current_vector
    current_x, current_y, current_z = first_point
    current_vector=App.Vector(current_x, current_y, current_z)
    sketch.addGeometry(Part.LineSegment(previous_vector,current_vector),False)
    # sketch.addGeometry(Part.LineSegment(App.Vector(49.215199,14.228024,0),App.Vector(28.786367,0.000000,0)),False)
    sketch.addConstraint(Sketcher.Constraint('Coincident',i-1,2,i,1)) 
    sketch.addConstraint(Sketcher.Constraint('Coincident',i,2,0,1))

    if not rotate_for_cnc:

        sketch.addConstraint(Sketcher.Constraint('DistanceX',-1,1,0,1,first_bottom_run_depth)) 
        sketch.addConstraint(Sketcher.Constraint('DistanceY',-1,1,0,1,0))
        sketch.addConstraint(Sketcher.Constraint('Horizontal',0))

    else:

        # Rotate Stair on x axis for cnc
        # Calculate base
        base = math.cos(stair_angle_rad) * first_bottom_run_depth

        sketch.addConstraint(Sketcher.Constraint('DistanceX',-1,1,0,1,base)) 
        sketch.addConstraint(Sketcher.Constraint('DistanceY',-1,1,0,1,0))

        sketch.addConstraint(Sketcher.Constraint('Angle',i,2,-1,2,3.141593))






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

    return body


import PathScripts
import Path
import Path.Base.Gui as PathGui
import Path.Main.Job as PathJob
import Path.Post.Processor as PostProcessor
import Path.Tool as PathTool
import Path.Op.Profile as PathProfile

def create_job(doc, body, job_name="Job"):
    
    job = PathJob.Create(job_name, [body]) 
    print(job)
    PathGui.ActiveJob = job

    doc.recompute()


    profile=PathProfile.Create(f"{job_name}_profile")


    doc.recompute()


    print("allAvailablePostProcessors")
    print(Path.Preferences.allAvailablePostProcessors())


    # Generate GCode
    postprocessor = PostProcessor.PostProcessorFactory.get_post_processor(job,"linuxcnc")
    gcode = postprocessor.export()[0][1]

    print(gcode)

    return gcode

