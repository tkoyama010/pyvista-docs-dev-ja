# Create a ParametricSuperToroid mesh
#
import pyvista
mesh = pyvista.ParametricSuperToroid()
cpos = mesh.plot(color='w', smooth_shading=True)
