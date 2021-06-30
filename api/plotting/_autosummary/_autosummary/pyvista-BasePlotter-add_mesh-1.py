# Add a sphere to the plotter and show it with a custom scalar
# bar title.
#
import pyvista
sphere = pyvista.Sphere()
sphere['Data'] = sphere.points[:, 2]
plotter = pyvista.Plotter()
_ = plotter.add_mesh(sphere,
                     scalar_bar_args={'title': 'Z Position'})
plotter.show()
