import os

head, tail = os.path.split(os.path.dirname(os.path.abspath(__file__)))

viper_dark = os.path.join(head, "StyleSheets", "viper_dark.mplstyle")
viper_light = os.path.join(head, "StyleSheets", "viper_light.mplstyle")