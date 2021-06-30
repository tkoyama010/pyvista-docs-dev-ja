# Map a puppy texture to a sphere
#
import pyvista
from pyvista import examples
sphere = pyvista.Sphere()
sphere = sphere.texture_map_to_sphere()
tex = examples.download_puppy_texture()
sphere.plot(texture=tex)
