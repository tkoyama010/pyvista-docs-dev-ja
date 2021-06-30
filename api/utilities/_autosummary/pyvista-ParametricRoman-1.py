# Create a ParametricRoman mesh
#
import pyvista
mesh = pyvista.ParametricRoman()
cpos = mesh.plot(color='w', smooth_shading=True)
