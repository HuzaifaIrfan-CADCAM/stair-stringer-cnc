from stair_stringer import create_stair_stringer

def main():
    create_stair_stringer(doc_name="stair_stringer_assembly", stringer_thickness = 1.5, first_rise_height = 6.62, rise_height = 7.625,num_rise = 16, run_depth = 11.5, num_run = 15,  kicker=True, kicker_depth = 5.5, kicker_height = 1.5, stair_angle=33.5, back_cut_increase=5, rotate_for_cnc=False)

if __name__=="__main__":
    main()