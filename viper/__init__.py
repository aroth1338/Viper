__version__ = "0.1.1"

from viper.ColorWheel import ColorWheel
from viper.icons import *
from viper.plot_annotations import *
from viper.main_plotting import *
import viper.stylesheets
import os

import matplotlib as mpl

# mpl.rcParams["axes.facecolor"]   = "none"
# mpl.rcParams["figure.facecolor"] = "none"

#set up stylesheets
# head, tail = os.path.split(os.path.dirname(os.path.abspath(__file__)))
# viper_dark = os.path.join(head, "viper", "stylesheets", "viper_dark.mplstyle")
# viper_light = os.path.join(head, "viper", "stylesheets", "viper_light.mplstyle")
