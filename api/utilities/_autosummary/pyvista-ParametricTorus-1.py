# Create a ParametricTorus mesh
#
import pyvista
mesh = pyvista.ParametricTorus()
cpos = mesh.plot(color='w', smooth_shading=True)
