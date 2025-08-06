import matplotlib.pyplot as plt
import numpy as np
import mplcursors

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

        sel.annotation.set_text("")
        ax[0].scatter(x=sel.target[0], y=sel.target[1], color="r")
        # plot the spectrum:
        plot_spectrum(agn_obj_list, sel.index, ax[1])

    def on_remove(sel):
        ax[0].scatter(x=sel.target[0], y=sel.target[1], color="k")

    cursor_hover.connect("add", on_hover)
    cursor_click.connect("add", on_click)
    cursor_click.connect("remove", on_remove)

    plt.show()


def plot_spectrum(agn_obj_list, index, ax):
    ax.plot(
        agn_obj_list[index].wavelength, agn_obj_list[index].flux, color="black", lw=0.7
    )
    ax.set(
        xlabel="Wavelength [Å]",
        ylabel="Flux [1e-17 erg/s/cm$^2$/Å]",
        title="Spectrum of " + agn_obj_list[index].id,
    )


if __name__ == "__main__":
    print("you shouldn't be calling this is as main")
