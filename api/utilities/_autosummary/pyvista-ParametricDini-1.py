# Create a ParametricDini mesh
#
import pyvista
mesh = pyvista.ParametricDini()
cpos = mesh.plot(color='w', smooth_shading=True)
