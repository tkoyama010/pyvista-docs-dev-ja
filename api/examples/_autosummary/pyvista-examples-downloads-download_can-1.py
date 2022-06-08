# Plot the can dataset.
#
from pyvista import examples
import pyvista
dataset = examples.download_can()
dataset.plot(scalars='VEL', smooth_shading=True)
