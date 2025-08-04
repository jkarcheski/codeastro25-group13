import matplotlib.pyplot as plt
import numpy as np
import mplcursors

# Generate mock data
num_points = 100
x = np.random.rand(num_points)
y = np.random.rand(num_points)

# Create the plotting environment 
fig, ax = plt.subplots()
scatter = ax.scatter(x,y)

mplcursors.cursor(scatter, hover=True)  # or just mplcursors.cursor()

plt.show()