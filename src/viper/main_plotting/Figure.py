from string import ascii_uppercase
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

class Figure:
    """
    Custom Figure class for creating multi-panelled figures. Constructor allows for a stylesheet to be 
    passed in, allowing each Figure instance to have its own style.

    Inputs
        (optional) figsize: tuple(float, float), default is (6.5, 3). The size of the figure in inches (width, height).
        (optional) dpi: int, default is 150. The dpi of the created figure.
        (optional) style: str, default is None. The given style sheet for the figure. Accepts mpl.style_sheets or a path to a style sheet
        (optional) invert: bool, default is True. Invert's the y-axis of the global axis so that the origin is the upper left corner.

    Output
        Figure class instance.

    ****Note
        This class exists to solve a specific problem with saving figures in matplotlib. Figures in 
        matplotlib have an invisible bounding box, like a picture frame. When saving the figure, only
        content within this bounding box is saved. When working in a notebook environment, this bounding box
        is ignored and the entire figure is always shown. This can cause many plot elements to be un-
        intentionally cut off when saving. with the viper.Figure class, the bounding box is always visible until
        the figure is saved. Thus, the user will always know what plot elements will be saved with the figure. 
    
    
    """
    def __init__(self, figsize = None, dpi = 150, style = None, invert = True):
        
        if figsize is None:
            figsize = (6.5, 3)

        if style is not None:
            with plt.style.context(style):
                self.figure = plt.figure(dpi = dpi, figsize = figsize)
                self.axmain = plt.gca()
        else:
            self.figure = plt.figure(dpi = dpi, figsize = figsize)
            self.axmain = plt.gca()
        
        self.axmain.set_position([0,0,1,1])

        self.axmain.set_ylim(0, figsize[1])
        self.axmain.set_xlim(0, figsize[0])
        
        self.figsize = figsize
        self.dpi = dpi
        self.style = style
        
        self.axmain.spines[["top", "right", "left", "bottom"]].set_visible(True)

        if invert:
            self.axmain.invert_yaxis()
        
        self.letters = [] #letters for annotating figure
        self.panels  = [] #panels for figure
        
    def remove_figure_borders(self):
        """
        Method to remove the window pane-like frame around the figure.
        """
        self.axmain.axis("off")
        
    def remove_panel_borders(self):
        """
        Method to remove borders around all panels within the Figure.
        """
        for panel in self.panels:
            panel.spines.set_visible(False)
        
    def add_letter(self, x, y, letter = None, fontsize = 9, ha = "left", va = "top", color = None, zorder = 20):
        """       
        Method to add a letter to the Figure, useful for marking individual panels.

        Args:
            x (float): x coordinate of the letter in global figure axes coordinates.
            y (float): y coordinate of the letter in global figure axes coordinates.
            letter (str, optional): Letter or text to display. Defaults to next letter in the alphabet.
            fontsize (int, optional): Fontsize of the letter or text string. Defaults to 9.
            ha (str, optional): Horizontal alignment of the letter or text string. Defaults to "left".
            va (str, optional): Vertical alignment of the letter or text string. Defaults to "top".
            color (str, optional): Color of the letter or text string. Defaults to black.
            zorder (int, optional): Zorder of the letter or text string. Defaults to 20.
        """
        if letter == None:
            letter_to_add = ascii_uppercase[len(self.letters)]
        else:
            letter_to_add = letter
        
        self.letters.append(letter_to_add)

        if color is None:
            color = "white" if "dark" in self.style else "black"

        if self.style is not None:
            with plt.style.context(self.style):
                self.axmain.text(x, y, letter_to_add, ha = ha, va = va, fontweight = "bold", color = color, fontsize = fontsize, zorder = zorder)
        else:
            self.axmain.text(x, y, letter_to_add, ha = ha, va = va, fontweight = "bold", color = color, fontsize = fontsize, zorder = zorder)
        
    def add_panel(self, dim = None, style = None):
        """
        Method to add an individual panel to the Figure. The resulting axis is set as the current mpl axis.

        Args:
            dim (list[float], optional): A list containing the position and dimensions of the panel in inches. Defaults to [0.5, 0.3, 5.8, 2.3].
                >>> Ordering is [x, y, width, height]
            style (str, optional): A valid matplotlib.stylesheet name for this panel. Defaults to None.

        Returns:
            matplotlib.Axis: The axis created by add_panel()
        """

        if dim is None:
            dim = [0.5, 0.3, 5.75, 2.3]

        if self.style is not None and style is None:
            with plt.style.context(self.style):
                panel = self.axmain.inset_axes(dim, transform = self.axmain.transData)
        elif style is not None:
            with plt.style.context(style):
                panel = self.axmain.inset_axes(dim, transform = self.axmain.transData)
        else:
            panel = self.axmain.inset_axes(dim, transform = self.axmain.transData)

        self.panels.append(panel)
        self.figure.add_axes(panel)
        plt.sca(panel)
        
        return panel
    
    def highlight_panel(self, panel, color = "red"):
        """
        Method to highlight an individual panel by coloring its axis.

        Args:
            panel (matplotlib.Axis): Panel to color
            color (str, optional): Color of the highlight. Defaults to "red".
        """
        if isinstance(panel, int):
            for spine in self.panels[panel].spines:
                self.panels[panel].spines[spine].set_color(color)
                self.panels[panel].spines[spine].set_visible(True)
                
        elif isinstance(panel, Axes):
            panel.axis("on")
            for spine in panel.spines:
                panel.spines[spine].set_color(color)
                panel.spines[spine].set_visible(True)
                
    def make_transparent(self):
        """
        Method to set the transparency of the Figure and all of its panels to 0.

        """
        self.figure.patch.set_alpha(0)
        self.axmain.patch.set_alpha(0)

        for ax in self.panels:
            ax.patch.set_alpha(0)

    def savefig(self, path, dpi = 300, transparent = False, **kwargs):
        """
        Method to safe the figure in a desired format. 

        Args:
            path (or path-like object): The file path to save the Figure
            dpi (int, optional): Dpi of the image. Defaults to 300.
            transparent (bool, optional): Option to turn the figure transparent. Defaults to False.
            kwargs (optional): Accepts any keyword arguments used by matplotlib.Figure.savefig()
        """
        
        self.remove_figure_borders()

        if transparent:
            self.make_transparent()

        self.figure.savefig(path, dpi = dpi, **kwargs)
