import pyvista
pointa = [1.0, 1.0, 0.0]
pointb = [-1.0, 1.0, 0.0]
pointc = [-1.0, -1.0, 0.0]
pointd = [1.0, -1.0, 0.0]
pointe = [0.0, 0.0, 1.67]
pyramid = pyvista.Pyramid([pointa, pointb, pointc, pointd, pointe])
cpos = pyramid.plot(show_edges=True, line_width=5)
