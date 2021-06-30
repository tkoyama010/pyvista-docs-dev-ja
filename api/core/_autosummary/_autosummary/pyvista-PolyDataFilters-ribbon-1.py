# Convert a line to a ribbon and plot it.
#
import pyvista as pv
sphere = pv.Sphere()
path = sphere.geodesic(0, 100)
ribbon = path.ribbon()
cpos = pv.plot([sphere, ribbon])
