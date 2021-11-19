# Find nearest cell on a sphere centered on the
# origin to the point ``[0.1, 0.2, 0.3]``.
#
import pyvista
mesh = pyvista.Sphere()
point = [0.1, 0.2, 0.3]
index = mesh.find_closest_cell(point)
index
# Expected:
## 591
#
# Make sure that this cell indeed is the closest to
# ``[0.1, 0.2, 0.3]``.
#
import numpy as np
cell_centers = mesh.cell_centers()
relative_position = cell_centers.points - point
distance = np.linalg.norm(relative_position, axis=1)
np.argmin(distance)
# Expected:
## 591
#
# Find the nearest cells to several random points that
# are centered on the origin.
#
points = 2 * np.random.random((5000, 3)) - 1
indices = mesh.find_closest_cell(points)
indices.shape
# Expected:
## (5000,)
