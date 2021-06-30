# Create a ParametricPseudosphere mesh
#
import pyvista
mesh = pyvista.ParametricPseudosphere()
cpos = mesh.plot(color='w', smooth_shading=True)
