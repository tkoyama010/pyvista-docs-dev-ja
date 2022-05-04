# The following example generates a static image of the widget.
#
import pyvista as pv
from pyvista import examples
mesh = examples.download_nefertiti()
p = pv.Plotter()
_ = p.add_mesh_clip_box(mesh, color='white')
p.show(cpos=[-1, -1, 0.2])
