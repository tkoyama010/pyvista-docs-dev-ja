import pyvista as pv
source = pv.UniformGrid(dims=(10, 10, 5))
source = source.compute_cell_sizes()
target = pv.UniformGrid(dims=(10, 10, 5))
target.copy_attributes(source)
target.plot(scalars='Volume', show_edges=True)
