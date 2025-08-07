from package_skeleton import astro_ob, AGN
import interactive_plot as ip


def UNIT_TEST1():
    """_summary_"""
    ex_num = 3
    astroob_inst = astro_ob("AGN")  # instance of astronomical object, its an AGN!
    output = astroob_inst.get_spectra(ex_num)
    instance_list = []
    for entry in output:
        instance = AGN("AGN", entry)
    instance_list.append(instance)

    #
    assert len(instance_list) == ex_num
    return
    # ip.interactive_plots(instance_list, 'ra', 'dec')
