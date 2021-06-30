# Compute the distance between all the points on a sphere and a
# plane.
#
import pyvista as pv
sphere = pv.Sphere()
plane = pv.Plane()
_ = sphere.compute_implicit_distance(plane, inplace=True)
dist = sphere['implicit_distance']
print(type(dist))
# Expected:
## <class 'numpy.ndarray'>
#
# Plot these distances as a heatmap
#
pl = pv.Plotter()
_ = pl.add_mesh(sphere, scalars='implicit_distance', cmap='bwr')
_ = pl.add_mesh(plane, color='w', style='wireframe')
cpos = pl.show()
