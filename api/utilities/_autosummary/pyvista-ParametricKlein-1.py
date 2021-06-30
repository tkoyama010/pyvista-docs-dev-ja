# Create a ParametricKlein mesh
#
import pyvista
mesh = pyvista.ParametricKlein()
cpos = mesh.plot(color='w', smooth_shading=True)
