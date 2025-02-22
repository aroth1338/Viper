from string import ascii_uppercase
import matplotlib.pyplot as plt
import matplotlib as mpl

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
        self.axmain.axis("off")
        
    def remove_panel_borders(self):
        for panel in self.panels:
            panel.axis("off")
        
    def add_letter(self, x, y, letter = None, fontsize = 9, ha = "left", va = "top", color = None, zorder = 20):
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
        
    def add_panel(self, dim = None):

        if dim is None:
            dim = [0.5, 0.3, 5.8, 2.3]

        if self.style is not None:
            with plt.style.context(self.style):
                panel = self.axmain.inset_axes(dim, transform = self.axmain.transData)
        else:
            panel = self.axmain.inset_axes(dim, transform = self.axmain.transData)

        self.panels.append(panel)
        self.figure.add_axes(panel)
        plt.sca(panel)
        
        return panel
    
    def highlight_panel(self, panel, color = "red"):
        if isinstance(panel, int):
            for spine in self.panels[panel].spines:
                self.panels[panel].spines[spine].set_color(color)
                self.panels[panel].spines[spine].set_visible(True)
                
        elif isinstance(panel, mpl.axes.Axes):
            panel.axis("on")
            for spine in panel.spines:
                panel.spines[spine].set_color(color)
                panel.spines[spine].set_visible(True)
                
    def make_transparent(self):
        self.figure.patch.set_alpha(0)
        self.axmain.patch.set_alpha(0)

        for ax in self.panels:
            ax.patch.set_alpha(0)

    def savefig(self, path, dpi = 300, transparent = False, **kwargs):
        self.remove_figure_borders()
        if transparent:
            self.make_transparent()
        self.figure.savefig(path, dpi = dpi, **kwargs)
