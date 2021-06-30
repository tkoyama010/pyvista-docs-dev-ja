# Create a ParametricPluckerConoid mesh
#
import pyvista
mesh = pyvista.ParametricPluckerConoid()
cpos = mesh.plot(color='w', smooth_shading=True)
