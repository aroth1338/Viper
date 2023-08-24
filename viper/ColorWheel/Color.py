import colorsys
import matplotlib.colors as mc
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

class Color():

    def __init__(self, color_hex):
        """Assumes input is a hex code"""
        self.color = color_hex
        self.hex = color_hex
        self.rgb = self.__hex_to_rgb(color_hex)
        
        #TODO Add other representations?

        
    @property
    def dark(self):
        return self.__lighten_color(self.color, 1.3)
    
    @property
    def light(self):
        return self.__lighten_color(self.color, .7)
    
    def darker(self, amount = .2):
        return self.__lighten_color(self.color, 1+amount)
    
    def lighter(self, amount = .2):
        return self.__lighten_color(self.color, 1-amount)

    def __lighten_color(self, color, amount = 1):
        
        if amount <= 0:
            return "#FFFFFF"
        elif amount >= 2:
            return "#000000"
        
        c = colorsys.rgb_to_hls(*mc.to_rgb(color))
        rgb = colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])
        
        return self.__rgb_to_hex(rgb)
        
    def __hex_to_rgb(self, hex_code, normalize = False):
        """
        Input: Hex String
        Output: integer RGB values
        """
        hex_code = hex_code.lstrip("#")
        RGB_vals = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
        if normalize: 
            RGB_vals = (RGB_vals[0] / 255, RGB_vals[1] / 255, RGB_vals[2] / 255)

        return RGB_vals
    
    def __rgb_to_hex(self, rgb):
        """
        Input: rgb tuple, ex: (.2, .8, .2) or (40, 185, 40)
        Output: Hex Representation of color
        """
        if rgb[0] < 1:
            int_rgb = (rgb[0] * 255, rgb[1] * 255, rgb[2] * 255)
            int_rgb = [int(x) for x in int_rgb]
            int_rgb = tuple(int_rgb)
        else:
            int_rgb = rgb
            
        return '#%02x%02x%02x' % int_rgb
    
    def __blend(self, color1, color2, ratio = .5):
        """
        Blends to given colors. Input must be hex code
        Returns blended color in hex code
        """
        colorRGBA1 = self.__hex_to_rgb(color1)
        colorRGBA2 = self.__hex_to_rgb(color2)
        
        amount = int(255 * ratio)
        
        red   = (colorRGBA1[0] * (255 - amount) + colorRGBA2[0] * amount) / 255
        green = (colorRGBA1[1] * (255 - amount) + colorRGBA2[1] * amount) / 255
        blue  = (colorRGBA1[2] * (255 - amount) + colorRGBA2[2] * amount) / 255
        
        result = self.__rgb_to_hex((int(red), int(green), int(blue)))

        return result 
    
    def __mul__(self, other):    
        return self.__lighten_color(self.color, other)
    
    def __truediv__(self, other):
        
        if isinstance(other, int) or isinstance(other, float):
            n = int(other)
            return [self.__lighten_color(self.color, amount = (x+1)/int(n/2+1)) for x in range(n)]
        elif isinstance(other, Color):
            cmap_colors = [self.__hex_to_rgb(x, normalize = True) for x in [self.color, other.color]]

            cm = LinearSegmentedColormap.from_list(
                    "Custom", cmap_colors, N=100)
            
            return cm(np.linspace(0, 1, 10))

    def __add__(self, other):
        if isinstance(other, str):
            return self.__blend(self.color, other, ratio = .5)
        elif isinstance(other, Color):
            return self.__blend(self.color, other.color, ratio = .5)
        
    def __repr__(self):
        return self.color
    
    def __str__(self):
        return self.color