# Simply show the plot of a mesh.
#
import pyvista as pv
pl = pv.Plotter()
_ = pl.add_mesh(pv.Cube())
pl.show()
#
# Take a screenshot interactively.  Screenshot will be of the
# first image shown, so use the first call with
# ``auto_close=False`` to set the scene before taking the
# screenshot.
#
pl = pv.Plotter()
_ = pl.add_mesh(pv.Cube())
pl.show(auto_close=False)  # doctest:+SKIP
pl.show(screenshot='my_image.png')  # doctest:+SKIP
#
# Display an ``ipygany`` scene within a jupyter notebook
#
pl.show(jupyter_backend='ipygany')  # doctest:+SKIP
#
# Return an ``ipygany`` scene.
#
pl.show(jupyter_backend='ipygany', return_viewer=True)  # doctest:+SKIP
