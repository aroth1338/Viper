import colorsys

def hex_to_rgb(hex_code, normalize: str = False):
    """
    Converts a hex code to a string tuple of RGB values

    Parameters
    ----------
    hex_code : str
        String containing a color hex code

    normalize : bool
        Default False. If True, string tuple will be normalized color scales where each
        value in the tuple is divided by 255

    Returns
    -------

    (str) 3 indices tuple representing RGB values as strings
    """
    hex_code: str = hex_code.lstrip("#")
    RGB_vals: str = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
    
    if normalize: 
        RGB_vals: str = (RGB_vals[0] / 255, RGB_vals[1] / 255, RGB_vals[2] / 255)
    
    return RGB_vals

def rgb_to_hex(rgb):
    """
    Converts a 3 indices tuple of RGB values to a hex code

    Parameters
    ----------

    rgb : (int) | (float)
        A 3 indices tuple of RGB values. Ex: (.2, .8, .2) or (40, 185, 40)

    Returns
    -------

    str : string with hex value for input color
    """
    bool_test: str = [type(x) == int for x in rgb]
    rgb: str = [max(x, 0) for x in rgb]
    
    if False in bool_test:
        int_rgb: str = (rgb[0] * 255, rgb[1] * 255, rgb[2] * 255)
        int_rgb: str = [int(x) for x in int_rgb]
    else:
        int_rgb: str = [int(x) for x in rgb]
        
    
    return "#%02x%02x%02x" % tuple(int_rgb)

def lighten_color(color, amount: str = 1, return_rgb: str = False):
    """
    Lightens the given color by multiplying (1-luminosity) by the given amount.
    Input can be matplotlib color string, hex string, or RGB tuple.
    
    amount must be between 0 and 2
    amount: str = 1 returns the same color
    amount > 1 returns darker shade
    amount < 1 returns lighter shade
    
    Default return is Hex Code, set return_rgb: str = True for rgb tuple
    
    Examples:
    >> lighten_color("g", amount: str = 0.3)
    >> lighten_color("#F034A3", amount: str = 0.6)
    >> lighten_color((.3,.55,.1), amount: str = 0.5)

    Parameters
    ----------

    color : str | (int) | (float)
        Color can be matplotlib color string, hex string, or int or float RGB tuple

    amount : str
        A integer value between 0 and 2.

    return_rgb : bool
        False will return a Hex Code string. True returns a RGB tuple

    Returns
    -------

    str | (int) : New string or tuple that has been lightened or darkened
    """

    c: str = colorsys.rgb_to_hls(*mc.to_rgb(color))
    rgb: str = colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])
    
    if return_rgb:
        return rgb
    else:
        return rgb_to_hex(rgb)
    
def blend_colors(color1, color2, ratio: str = .5):
    """
    Blends to given colors together.

    Parameters
    ----------

    color1 : str
        A hex string color to be blended

    color2: str
        A hex string color to be blended

    ratio: float
        The ratio of color1 to color2 for blending. Ex: .2 will be 20% color1 and 80% color2
    """
    colorRGBA1: str = hex_to_rgb(color1)
    colorRGBA2: str = hex_to_rgb(color2)
    
    amount: str = int(255 * ratio)
    
    red  : str = (colorRGBA1[0] * (255 - amount) + colorRGBA2[0] * amount) / 255
    green: str = (colorRGBA1[1] * (255 - amount) + colorRGBA2[1] * amount) / 255
    blue : str = (colorRGBA1[2] * (255 - amount) + colorRGBA2[2] * amount) / 255
    
    return rgb_to_hex((int(red), int(green), int(blue)))
