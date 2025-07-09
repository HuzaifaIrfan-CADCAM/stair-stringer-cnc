
from freecad_doc import FreecadDoc
from freecad_doc.stair_stringer import create_stair_stringer, create_job

def main():

    freecad_doc=FreecadDoc(doc_name="stair_stringer_cnc")

    doc=freecad_doc.doc
    
    stair_stringer_body=create_stair_stringer(doc, body_name="stair_stringer", stringer_thickness = 1.5, first_rise_height = 6.62, rise_height = 7.625,num_rise = 16, run_depth = 11.5, num_run = 15,  kicker=False, kicker_depth = 5.5, kicker_height = 1.5, stair_angle=33.5, back_cut_increase=5, rotate_for_cnc=True)
    
    gcode=create_job(doc, stair_stringer_body)

    freecad_doc.save()
    freecad_doc.export_gcode(gcode)
    freecad_doc.export_body(stair_stringer_body)



if __name__=="__main__":
    main()