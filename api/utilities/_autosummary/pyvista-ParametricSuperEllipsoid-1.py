# Create a ParametricSuperEllipsoid mesh
#
import pyvista
mesh = pyvista.ParametricSuperEllipsoid()
cpos = mesh.plot(color='w', smooth_shading=True)
