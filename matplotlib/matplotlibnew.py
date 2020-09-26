import matplotlib
import matplotlib.pyplot as plt
import numpy as np

r_array = np.linspace(0, 2, 1000)
phi_array = np.linspace(0, 2 * np.pi, 1000)

r_grid, phi_grid, = np.meshgrid(r_array, phi_array)


z_grid = r_grid + phi_grid
x_grid = r_grid * np.cos(phi_grid)
y_grid = r_grid * np.sin(phi_grid)

plt.pcolormesh(x_grid, y_grid, z_grid)
plt.show()