import pyvista
pyvista.parse_color('blue')
# Expected:
## (0.0, 0.0, 1.0)
#
pyvista.parse_color('k')
# Expected:
## (0.0, 0.0, 0.0)
#
pyvista.parse_color('#FFFFFF')
# Expected:
## (1.0, 1.0, 1.0)
#
pyvista.parse_color((0.4, 0.3, 0.4, 1))
# Expected:
## (0.4, 0.3, 0.4, 1.0)
