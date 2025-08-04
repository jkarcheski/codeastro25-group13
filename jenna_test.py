import matplotlib.pyplot as plt
import numpy as np
import mplcursors

# Generate mock data
num_points = 10
x = np.random.rand(num_points)
y = np.random.rand(num_points)

# Create the plotting environment 
fig, ax = plt.subplots(1,2, figsize = (10, 4))
scatter = ax[0].scatter(x,y)

cursor_hover = mplcursors.cursor(scatter, hover=True)
cursor_click = mplcursors.cursor(scatter, hover=False)  # or just mplcursors.cursor()

############ Cursor customization ######################################################################
# (from https://mplcursors.readthedocs.io/en/stable/)
# Selection has the following fields:
# artist: the selected artist,
# target: the (x, y) coordinates of the point picked within the artist.
# index: an index of the selected point, within the artist data, as detailed below.
# dist: the distance from the point clicked to the target (mostly used to decide which artist to select).
# annotation: a Matplotlib Annotation object.
# extras: an additional list of artists, that will be removed whenever the main annotation is deselected.
########################################################################################################

def on_hover(sel):
    # TODO: replace 'sel.index' with AGN name
    # ax[1].scatter(x,y)
    return sel.annotation.set_text(sel.index)

def on_click(sel):
    return ax[1].scatter(x,y)

cursor_hover.connect("add", on_hover)
cursor_click.connect("add", on_click)

#cursor.connect("click", on_click)

plt.show()