# Make the paraview-like theme the global default.
#
import pyvista
from pyvista import themes
pyvista.set_plot_theme(themes.ParaViewTheme())  # doctest:+SKIP
#
# Alternatively, set via a string.
#
pyvista.set_plot_theme('paraview')  # doctest:+SKIP
