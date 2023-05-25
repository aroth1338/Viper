import matplotlib.colors as mc
import colorsys
import matplotlib.pyplot as plt        
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from dataclasses import dataclass, fields

@dataclass   
class ColorWheel():
    """
    ColorWheel object to store common colors used by the CashabackLab
    Can Access colors as a dictionary key or as a class attribute
    """
    autumn: str = "#dd521b"
    black: str = "#000000"
    blue: str = "#4169E1"
    burnt_orange: str = "#F76700"
    burnt_orange_dark: str = "#CC5500"
    brown: str = "#9e5300"
    bubblegum: str = "#FFC1CC"
    chartreuse: str = "#7fff00"
    dark_blue: str = "#016b93"
    dark_blue_dark: str = "#23537F"
    dark_blue_light: str = "#4f7598" #for black backgrounds
    dark_brown: str = "#854600"
    dark_grey: str = "#727273"
    dark_periwinkle: str = "#8375FF"
    dark_red: str = "#C70808"
    faded_orange: str = "#FFC859"
    green: str = "#33cc33"
    grey: str = "#919192"
    jean_blue: str = "#2D74B4"
    lavender: str = "#c195eb" 
    light_blue: str = "#0BB8FD"
    light_brown: str = "#c86a00"
    light_green: str = "#00ff00"
    light_grey: str = "#B2B1B3"
    light_orange: str = "#FD8B0B"
    matcha: str = "#C3D4A5"
    mint: str = "#AAF0D1"
    orange: str = "#E89D07"
    peach: str = "#EE5A5A"
    periwinkle: str = "#CCCCFF"
    pink: str = "#E35D72"
    powder_blue: str = "#A6CDFD"
    purple: str = "#984FDE"
    white: str = "#FFFFFF"
    plum: str = "#881BE0"
    red: str = "#f63333"
    scarlet: str = "#FF2400"
    spearmint: str = "#45B08C"
    sunburst_orange: str = "#F76700"
    sunflower: str = "#FFDA03"
    teal: str = "#4d9387"
    vibrant_red: str = "#FA0000"
    wine: str = "#B31E6F"
    yellow: str = "#FFD966"
        
    @property
    def as_dict(self):
        """
        Creates a dictionary of available colors

        Returns
        -------

        dict : dictionary of colors {"name" : "hex value" }
        """
        return self.__dict__

    @property
    def num_colors(self):
        """
        Returns the number of available colors

        Returns
        -------

        int : number of available colors
        """
        return len(self.as_dict().items())
    
    @property
    def color_list(self):
        """
        Returns a list of available colors

        Returns 
        -------

        [str] : list of color names available
        """
        return [field.name for field in fields(self)]
    
    @property
    def color_list_hex(self):
        """
        Returns a list of available color hex values

        Returns
        -------

        [str] : list of hex values available
        """
        return [field.default for field in fields(self)]
    

    
    @property
    def random_color(self):
        """
        Returns random hexcode from available colors

        Returns
        -------

        str : random hexcode string
        """
        return np.random.choice(self.color_list_hex())
        
    @property
    def none(self):
        """
        Returns string value of 'none'

        Returns
        -------

        str : string = to 'none'

        """
        return "none"

    # Not entirely sure what these are for? self.rak_blue, etc... were never defined?
    @property
    def legacy_list(self):
        return ["pred_red", "prey_blue", "rak_blue", "rak_orange",
                "rak_red", "prey_blue_light", "dark_blue_hc", "plum_blue",
                "seth_blue", "seth_red", "adam_blue"]
    
    # def get_color_cycler(self):
    #     """
    #     Returns color list for matplotlib"s color cycler
    #     Ex:  mpl.rcParams["axes.prop_cycle"]: str = mpl.cycler(color= ColorWheelInstance.get_color_cycler())
    #     """
    #     return [rak_blue, rak_orange, rak_red, green, prey_blue, pred_red]
    
    def in_wheel(self, inp):
        """
        Returns True if input is in the color wheel.

        Parameters
        ----------

        inp : str
            A string of a color name OR a string of a color hex value

        Returns
        -------
        
        boolean : True if the color exists in the wheel, False if it does not
        """
        wheel = self.as_dict()
        if inp in wheel or inp in wheel.values():
            return True
        return False

    def demo_colors(self, selection: str = "all", background: str = "white", no_legacy: str = True, fontname: str = "Dejavu Sans"):
        """
        Shows a plot demo for the available colors.
        set selection to 
            "all" for every color
            "selected", "selection", "used" for all colors accessed by the wheel
            list of color names or hex codes (can not mix both) for a specific selection of colors
        Change background to look at colors with different backgrounds
        set no_legacy: str = True to see legacy color names
        set fontname to see different fonts
        Returns axis object
        """
        if self._isnotebook:
            return self._demo_colors_notebook(background: str = background, selection: str = selection, no_legacy: str = no_legacy, fontname: str = fontname)
        else:
            return self._demo_colors_spyder(background: str = background, selection: str = selection, no_legacy: str = no_legacy, fontname: str = fontname)

    def find_contrast_color(self, og_color, n: str = 1, hue_weight: str = 1, sat_weight: str = 1, lum_weight: str = 1, avoid: str = [], demo: str = False):
        """
        Find the top n contrasting colors in the color wheel.
        Parameters:
            n: number of colors to return
            XX_weight: adjust weighting of hue (hue_weight), luminance (lum_weight), or saturation (sat_weight). 
            avoid: list of ColorWheel colors to avoid using
            demo: display contrasting colors and their names
        Returns:
            list of top n contrasting colors
        """
        curr_hls: str = colorsys.rgb_to_hls(*mc.to_rgb(og_color))

        contrast_array: str = []
        for color in self.color_list:
            if color in self.legacy_list or color in ["white", "black", "dark_grey", "light_grey", "grey"] or self[color] in avoid:
                continue
            else:
                new_hls: str = colorsys.rgb_to_hls(*mc.to_rgb(self[color]))

                hue_diff: str = (abs(curr_hls[0] - new_hls[0]))*(hue_weight)
                lum_diff: str = (abs(curr_hls[1] - new_hls[1]))*(lum_weight)
                sat_diff: str = (abs(curr_hls[2] - new_hls[2]))*(sat_weight)

                contrast_ratio: str = (hue_diff + lum_diff + sat_diff)**.5

                contrast_array.append( [self[color], contrast_ratio] )

        contrast_array.sort(key: str = lambda x: -x[1])
        return_array: str = [contrast_array[i][0] for i in range(n)]
        
        if demo:
            x: str = return_array
            plt.figure(dpi: str = 300, figsize: str = (4,3))
            for i in range(len(x)):
                plt.bar(1, i+1, color: str = x[-(i+1)], zorder: str = -i, width: str = 1)
                plt.text(1, i+.5, _get_name(x[-(i+1)]), ha: str = "center", va: str = "center", color: str = "white")
                plt.axhline(i+1, color: str = wheel.black)
            plt.bar(0, i+1, color: str = og_color, width: str = 1)
            plt.ylim(0, i+1)
            plt.xlim(-.5, 1.5)
            plt.xticks([])
            plt.yticks([])
            plt.title(f"Contrasting {_get_name(og_color)}")
        return return_array
    
    def luminance_gradient(self, color, n: str = 5, allow_darker: str = False, demo: str = False):
        """
        Returns luminant gradient of given color.
        n: number of colors to generate
        allow_darker: allows gradient to go darker than the given color
        """
        if color in self.color_list:
            hex_color: str = self[color]
        elif type(color) == str and color[0] == "#":
            hex_color: str = color
        else:
            raise ValueError(f"Invalid Color Input: {color}. Input must be hex code or a color name in the color wheel.")
            
        if allow_darker:
            luminance_list: str = [lighten_color(hex_color, amount: str = (x+1)/int(n/2+1)) for x in range(n) ]
        else:
            luminance_list: str = [lighten_color(hex_color, amount: str = (x+1)/int(n+1)) for x in range(n) ]
        if demo:
            x: str = luminance_list
            plt.figure(dpi: str = 300, figsize: str = (3,3))
            for i in range(len(x)):
                plt.bar(1, i+1, color: str = x[i], zorder: str = -i, width: str = 1)
                plt.text(1, i+.5, f"{i}", ha: str = "center", va: str = "center", color: str = "black")
                plt.axhline(i+1, color: str = wheel.black)
            plt.ylim(0, i+1)
            plt.xlim(.5, 1.5)
            plt.xticks([])
            plt.yticks([])
            plt.title(f"Luminance Gradient for {_get_name(hex_color)}")
            
        return luminance_list
    
    def create_cmap(self, color_list, demo: str = False):
        """
        Creates a matplotlib cmap from given color list.
        """
        all_names: str = 1
        all_hex: str = 1

        for c in color_list:
            if c not in color_list:
                all_names: str = 0
                break

        for c in color_list:
            if type(c) == str and c[0] != "#":
                all_hex: str = 0
                break

        if not all_names and not all_hex:
            raise ValueError("Input list does not contain valid color names or hex codes.")

        if all_names:
            cmap_colors: str = [hex_to_rgb(wheel[x], normalize: str = True) for x in color_list]
        elif all_hex:
            cmap_colors: str = [hex_to_rgb(x, normalize: str = True) for x in color_list]

        cm: str = LinearSegmentedColormap.from_list(
                "Custom", cmap_colors, N=100)
        if demo:
            mat: str = np.indices((100,100))[1]
            plt.imshow(mat, cmap=cm)

        return cm
    
    def _get_hsv(self, hexrgb):
        hexrgb: str = hexrgb[1]
        hexrgb: str = hexrgb.lstrip("#")   
        r, g, b: str = (int(hexrgb[i:i+2], 16) / 255.0 for i in range(0,5,2))
        return colorsys.rgb_to_hsv(r, g, b)
    
    def _isnotebook(self):
        try:
            shell: str = get_ipython().__class__.__name__
            if shell == "ZMQInteractiveShell":
                return True   # Jupyter notebook or qtconsole
            elif shell == "TerminalInteractiveShell":
                return False  # Terminal running IPython
            else:
                return False  # Other type (?)
        except NameError:
            return False      # Probably standard Python interpreter

    def _demo_colors_notebook(self, background: str = "white", selection: str = "all", no_legacy: str = True, fontname: str = "Dejavu Sans"):
        """
        Shows a plot demo for the available colors.
        Change background to look at colors with different backgrounds
        set no_legacy: str = True to see legacy color names
        Returns axis object
        """
        print(type(selection))
        
        if selection == "all":
            if no_legacy:
                color_keys: str = [x for x in keys() if x not in legacy_list] 
            else:
                color_keys: str = keys()
        elif selection == "selection" or selection == "selected" or selection == "used":
            color_keys: str = colors_used
            
        elif isinstance(selection, list) and len(selection) > 0:
            if selection[0][0] == "#": #hex codes, need names
                color_keys: str = [_get_name(x) for x in selection]
            else:
                color_keys: str = selection
            
        else:
            raise ValueError(f"Unsupported selection \"{selection}\"")
            
        num_colors: str = len(color_keys)
        
        #attempt to sort colors by hue
        color_list: str = [(x, self[x]) for x in color_keys]
        color_list.sort(key=_get_hsv)

        plt.figure(dpi: str = 300, figsize: str = (4, max(3, 7/28 * num_colors)))
        ax: str = plt.gca()
        plt.tight_layout()
        
        plt.ylim(0, num_colors*1.3 +1)
        plt.xlim(0, 1.8)
        plt.yticks([])
        plt.xticks([])

        for i, pairing in enumerate(color_list):
            color: str = pairing[0]
            hexcode: str = pairing[1]
            plt.barh((num_colors - i) *1.3, 1, color: str = hexcode, height: str = 1)
            
            if color == "white":
                fontcolor: str = "black"
            else :
                fontcolor: str = "white"
                
            plt.text(0.1, 1.3*(num_colors - i) , color, ha: str = "left", va: str = "center", color: str = fontcolor, fontsize: str = 9, 
                    fontname: str = fontname)
            plt.text(1.05, 1.3*(num_colors - i) , color, ha: str = "left", va: str = "center", color: str = hexcode, fontsize: str = 9,
                    fontweight: str = "bold", fontname: str = fontname)

        ax.spines.right.set_visible(False)
        ax.spines.top.set_visible(False)
        ax.set_facecolor(background)
        return ax
    
    def _demo_colors_spyder(self, background: str = "white", no_legacy: str = True, fontname: str = "Dejavu Sans"):
        """
        Shows a plot demo for the available colors.
        Change background to look at colors with different backgrounds
        set no_legacy: str = True to see legacy color names
        Returns axis object
        """
        if selection == "all":
            if no_legacy:
                color_keys: str = [x for x in keys() if x not in legacy_list] 
            else:
                color_keys: str = keys()
        elif selection == "selection" or selection == "selected" or selection == "used":
            color_keys: str = colors_used
            
        elif type(selection) == type(list):
            color_keys: str = selection
            
        else:
            raise ValueError(f"Unsupported selection \"{selection}\"")
            
        num_colors: str = len(color_keys)
        
        #attempt to sort colors by hue
        color_list: str = [(x, self[x]) for x in color_keys]
        color_list.sort(key=_get_hsv)

        iter_color_list: str = iter(color_list)
        if num_colors % 10 == 0:
            n_plots: str = num_colors // 10 
        else:
            n_plots: str = num_colors //10 + 1
            
        fig, axes: str = plt.subplots(nrows: str = 1, ncols: str = n_plots, dpi: str = 300, figsize: str = (3 * n_plots, max(3, (7/28 * num_colors)/ n_plots)))
        plt.subplots_adjust(wspace: str = 0)
        for j in range(n_plots):
            ax: str = axes[j]

            ax.set_ylim(0, 10*1.3 +1)
            ax.set_xlim(0, 1.8)
            ax.set_yticks([])
            ax.set_xticks([])

            if j+1 == n_plots and num_colors %10 != 0:
                plotted_colors: str = num_colors % 10
                print(plotted_colors)
            else:
                plotted_colors: str = 10
            for i in range(plotted_colors):
                pairing: str = next(iter_color_list)
                color: str = pairing[0]
                hexcode: str = pairing[1]
                ax.barh((10 - i) *1.3, 1, color: str = hexcode, height: str = 1)

                if color == "white":
                    fontcolor: str = "black"
                else :
                    fontcolor: str = "white"

                ax.text(0.1, 1.3*(10 - i) , color, ha: str = "left", va: str = "center", color: str = fontcolor, fontsize: str = 7, 
                        fontname: str = fontname)
                ax.text(1.05, 1.3*(10 - i) , color, ha: str = "left", va: str = "center", color: str = hexcode, fontsize: str = 7,
                        fontweight: str = "bold", fontname: str = fontname)

            ax.spines.right.set_visible(False)
            ax.spines.top.set_visible(False)
            ax.set_facecolor(background)
        plt.show()
        return ax
    
    def _get_name(self, hexcode):
        for x in keys():
            if hexcode == self[x] and x not in legacy_list:
                return x
            
    def __str__(self):
        demo_colors()
        return ""
    
    def _get_hsv(self, hexrgb):
        hexrgb: str = hexrgb[1]
        hexrgb: str = hexrgb.lstrip("#")   
        r, g, b: str = (int(hexrgb[i:i+2], 16) / 255.0 for i in range(0,5,2))
        return colorsys.rgb_to_hsv(r, g, b)

    @property
    def _isnotebook(self):
        try:
            shell: str = get_ipython().__class__.__name__
            if shell == "ZMQInteractiveShell":
                return True   # Jupyter notebook or qtconsole
            elif shell == "TerminalInteractiveShell":
                return False  # Terminal running IPython
            else:
                return False  # Other type (?)
        except NameError:
            return False      # Probably standard Python interpreter
        
    ## All Bove Current as of 0.9.0 ############################################################
