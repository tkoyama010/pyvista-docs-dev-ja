# Extrude a half arc circle
#
import pyvista
arc = pyvista.CircularArc([-1, 0, 0], [1, 0, 0], [0, 0, 0])
mesh = arc.extrude([0, 0, 1])
cpos = mesh.plot()
