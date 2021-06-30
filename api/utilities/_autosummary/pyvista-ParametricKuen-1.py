# Create a ParametricKuen mesh
#
import pyvista
mesh = pyvista.ParametricKuen()
cpos = mesh.plot(color='w', smooth_shading=True)
