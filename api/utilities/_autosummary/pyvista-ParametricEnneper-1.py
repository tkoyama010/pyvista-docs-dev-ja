# Create a ParametricEnneper mesh
#
import pyvista
mesh = pyvista.ParametricEnneper()
cpos = mesh.plot(color='w', smooth_shading=True)
