import matplotlib.pyplot as plt
import numpy as np
import mplcursors

print("Plotting function document")


def interactive_plots(agn_obj_list, paramx, paramy):
    x = [getattr(agn_obj_list[i], paramx) for i in range(len(agn_obj_list))]
    y = [getattr(agn_obj_list[i], paramy) for i in range(len(agn_obj_list))]
    ids = [getattr(agn_obj_list[i], "id") for i in range(len(agn_obj_list))]

    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    scatter = ax[0].scatter(x, y, color="k")
    ax[0].set_title("Main Interactive Plot")
    ax[0].set(xlabel=str(paramx), ylabel=str(paramy))
    ax[1].set_title("Spectrum")

    cursor_click = mplcursors.cursor(
        scatter, hover=False
    )  # or just mplcursors.cursor()
    cursor_hover = mplcursors.cursor(scatter, hover=2)

    def on_hover(sel):
        # TODO: replace 'sel.index' with AGN name
        sel.annotation.set_text(ids[sel.index])

    def on_click(sel):
        # generates a new plot in the other panel
        ax[1].clear()
        ax[1].set_title("Spectrum")

        sel.annotation.set_text("")
        ax[0].scatter(x=sel.target[0], y=sel.target[1], color="r")
        # plot the spectrum:
        ax[1].plot(agn_obj_list[sel.index].lam, agn_obj_list[sel.index].flux)

    def on_remove(sel):
        ax[0].scatter(x=sel.target[0], y=sel.target[1], color="k")

    cursor_hover.connect("add", on_hover)
    cursor_click.connect("add", on_click)
    cursor_click.connect("remove", on_remove)

    plt.show()


if __name__ == "__main__":
    print("you shouldn't be calling this is as main")


"""

TESTING MAIN

myagn1 = agn(
    ra_in=1,
    dec_in=2.0,
    id_in=4,
    lam_in=np.linspace(0, 1, 100),
    flux_in=np.random.rand(100),
)
myagn2 = agn(
    ra_in=3.0,
    dec_in=4.0,
    id_in=7,
    lam_in=np.linspace(0, 1, 100),
    flux_in=np.random.rand(100),
)

interactive_plots([myagn1, myagn2], "ra", "dec")
"""
