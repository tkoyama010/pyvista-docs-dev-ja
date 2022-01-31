# Add two arrays using ``update``.
#
import numpy as np
from pyvista import examples
mesh = examples.load_uniform()
n = len(mesh.point_data)
arrays = {
    'foo': np.arange(mesh.n_points),
    'rand': np.random.random(mesh.n_points),
}
mesh.point_data.update(arrays)
mesh.point_data
# Expected:
## pyvista DataSetAttributes
## Association     : POINT
## Active Scalars  : rand
## Active Vectors  : None
## Active Texture  : None
## Active Normals  : None
## Contains arrays :
##     Spatial Point Data      float64  (1000,)
##     foo                     int64    (1000,)
##     rand                    float64  (1000,)              SCALARS
