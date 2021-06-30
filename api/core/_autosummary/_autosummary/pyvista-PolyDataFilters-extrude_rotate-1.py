import pyvista
line = pyvista.Line(pointa=(0, 0, 0), pointb=(1, 0, 0))
mesh = line.extrude_rotate(resolution = 4)
cpos = mesh.plot()
