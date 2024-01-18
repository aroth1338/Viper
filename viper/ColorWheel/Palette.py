import colorsys
import matplotlib.colors as mc

class Palette():
    def __init__(self):
        pass

    def _hex_to_rgb(self, hex_code, normalize = False):
        """
        Input: Hex String
        Output: integer RGB values
        """
        hex_code = hex_code.lstrip("#")
        RGB_vals = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
        
        if normalize: 
            RGB_vals = (RGB_vals[0] / 255, RGB_vals[1] / 255, RGB_vals[2] / 255)
        
        return RGB_vals
    
    def _rgb_to_hex(self, rgb):
        """
        Input: rgb tuple, ex: (.2, .8, .2) or (40, 185, 40)
        Output: Hex Representation of color
        """
        bool_test = [type(x) == int for x in rgb]
        rgb = [max(x, 0) for x in rgb]
        
        if False in bool_test:
            int_rgb = (rgb[0] * 255, rgb[1] * 255, rgb[2] * 255)
            int_rgb = [int(x) for x in int_rgb]
            int_rgb = tuple(int_rgb)
        else:
            int_rgb = [int(x) for x in rgb]
            int_rgb = tuple(int_rgb)
            
        
        return '#%02x%02x%02x' % int_rgb
    
    def _hex_to_hsv(self, hex_code):
        r, g, b = self._hex_to_rgb(hex_code, normalize = True)

        return colorsys.rgb_to_hsv(r, g, b)
    
    def _hex_to_hls(self, hex_code):
        rgb = self._hex_to_rgb(hex_code, normalize = True)
        hls = colorsys.rgb_to_hls(*rgb)
        
        return hls
    
    def _adjust_luminance(self, color, amount = 1, return_rgb = False):
        """
        Lightens the given color by multiplying (1-luminosity) by the given amount.
        Input can be matplotlib color string, hex string, or RGB tuple.
        
        amount must be between 0 and 2
        amount = 1 returns the same color
        amount > 1 returns darker shade
        amount < 1 returns lighter shade
        
        Default return is Hex Code, set return_rgb = True for rgb tuple
        
        Examples:
        >> lighten_color('g', amount = 0.3)
        >> lighten_color('#F034A3', amount = 0.6)
        >> lighten_color((.3,.55,.1), amount = 0.5)
        """

        c = colorsys.rgb_to_hls(*mc.to_rgb(color))
        rgb = colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])
        
        if return_rgb:
            return rgb
        else:
            return self._rgb_to_hex(rgb)
        
    def _blend(self, color1, color2, ratio = .5):
        """
        Blends to given colors. Input must be hex code
        Returns blended color in hex code
        """
        colorRGBA1 = self._hex_to_rgb(color1)
        colorRGBA2 = self._hex_to_rgb(color2)
        
        amount = int(255 * ratio)
        
        red   = (colorRGBA1[0] * (255 - amount) + colorRGBA2[0] * amount) / 255
        green = (colorRGBA1[1] * (255 - amount) + colorRGBA2[1] * amount) / 255
        blue  = (colorRGBA1[2] * (255 - amount) + colorRGBA2[2] * amount) / 255
        
        result = self._rgb_to_hex((int(red), int(green), int(blue)))
        
        return result
    
    def _is_hex(self, color):
        if color[0] == "#":
            return True
        else:
            return False
    