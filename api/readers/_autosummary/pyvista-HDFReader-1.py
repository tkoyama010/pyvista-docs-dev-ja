import pyvista
from pyvista import examples
filename = examples.download_can(partial=True, load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'can_0.hdf'
reader = pyvista.get_reader(filename)
mesh = reader.read()
mesh.plot()
