# Create a ParametricBohemianDome mesh.
#
import pyvista
mesh = pyvista.ParametricBohemianDome()
cpos = mesh.plot(color='w', smooth_shading=True)
