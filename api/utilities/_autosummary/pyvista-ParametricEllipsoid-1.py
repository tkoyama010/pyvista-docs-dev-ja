# Create a ParametricEllipsoid mesh
#
import pyvista
mesh = pyvista.ParametricEllipsoid()
cpos = mesh.plot(color='w', smooth_shading=True)
