# Create a ParametricMobius mesh
#
import pyvista
mesh = pyvista.ParametricMobius()
cpos = mesh.plot(color='w', smooth_shading=True)
