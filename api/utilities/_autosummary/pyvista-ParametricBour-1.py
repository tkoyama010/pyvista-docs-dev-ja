# Create a ParametricBour mesh.
#
import pyvista
mesh = pyvista.ParametricBour()
cpos = mesh.plot(color='w', smooth_shading=True)
