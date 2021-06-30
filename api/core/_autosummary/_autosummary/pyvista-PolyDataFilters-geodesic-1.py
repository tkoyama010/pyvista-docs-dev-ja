# Plot the path between two points on a sphere.
#
import pyvista as pv
sphere = pv.Sphere()
path = sphere.geodesic(0, 100)
pl = pv.Plotter()
actor = pl.add_mesh(sphere)
actor = pl.add_mesh(path, line_width=5, color='k')
cpos = pl.show()
