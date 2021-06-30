# Create a ParametricBoy mesh
#
import pyvista
mesh = pyvista.ParametricBoy()
cpos = mesh.plot(color='w', smooth_shading=True)
