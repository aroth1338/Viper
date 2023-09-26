__version__ = "0.1.0"

from viper.ColorWheel import ColorWheel
import viper.icons
import viper.plot_annotations
import viper.main_plotting
from viper.StyleSheets import viper_style

import matplotlib as mpl

mpl.rcParams["axes.facecolor"]   = "none"
mpl.rcParams["figure.facecolor"] = "none"

viper_stylesheet = "viper/StyleSheets/viper_style.mplstyle"
