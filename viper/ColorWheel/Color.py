import colorsys
import matplotlib.colors as mc
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import importlib

Palette = importlib.import_module(".Palette", "viper.ColorWheel").Palette 

class Color(Palette):

    def __init__(self, color_hex):
        """Assumes input is a hex code"""
        self.color = color_hex
        self.hex = color_hex
        self.rgb = super()._hex_to_rgb(color_hex)
        self.hsv = super()._hex_to_hsv(color_hex)
        self.hls = super()._hex_to_hls(color_hex)
        #TODO Add other representations?

        
    @property
    def dark(self):
        return super()._adjust_luminance(self.hex, 1.3)
    
    @property
    def light(self):
        return super()._adjust_luminance(self.hex, .7)
    
    def darker(self, amount = .2):
        return super()._adjust_luminance(self.hex, 1+amount)
    
    def lighter(self, amount = .2):
        return super()._adjust_luminance(self.hex, 1-amount)
    
    def __mul__(self, other):    
        return super()._adjust_luminance(self.hex, other)
    
    def __truediv__(self, other):
        
        if isinstance(other, int) or isinstance(other, float):
            n = int(other)
            return [super()._adjust_luminance(self.hex, amount = (x+1)/int(n/2+1)) for x in range(n)]
        elif isinstance(other, Color):
            cmap_colors = [super()._hex_to_rgb(x, normalize = True) for x in [self.hex, other.hex]]

            cm = LinearSegmentedColormap.from_list("Custom", cmap_colors, N=100)
            
            return cm(np.linspace(0, 1, 10))

    def __add__(self, other):
        if isinstance(other, str):
            return super()._blend(self.hex, other, ratio = .5)
        elif isinstance(other, Color):
            return super()._blend(self.hex, other.hex, ratio = .5)
        
    def __repr__(self):
        return self.hex
    
    def __str__(self):
        return self.hex