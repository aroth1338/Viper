__version__ = "0.1.0"

from viper.ColorWheel import ColorWheel
import viper.icons
import viper.plot_annotations
import viper.main_plotting
import os

import matplotlib as mpl

mpl.rcParams["axes.facecolor"]   = "none"
mpl.rcParams["figure.facecolor"] = "none"

head, tail = os.path.split(os.path.dirname(os.path.abspath(__file__)))
viper_dark = os.path.join(head, "viper", "StyleSheets", "viper_dark.mplstyle")
viper_light = os.path.join(head, "viper", "StyleSheets", "viper_light.mplstyle")
