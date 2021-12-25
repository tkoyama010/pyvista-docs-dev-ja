# Make the dark theme the global default.
#
import pyvista
from pyvista import themes
pyvista.set_plot_theme(themes.DarkTheme())  # doctest:+SKIP
#
# Alternatively, set via a string.
#
pyvista.set_plot_theme('dark')  # doctest:+SKIP
