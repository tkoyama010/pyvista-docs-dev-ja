# Create a ParametricRandomHills mesh
#
import pyvista
mesh = pyvista.ParametricRandomHills()
cpos = mesh.plot(color='w', smooth_shading=True)
