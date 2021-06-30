# Create a ParametricHenneberg mesh
#
import pyvista
mesh = pyvista.ParametricHenneberg()
cpos = mesh.plot(color='w', smooth_shading=True)
