from string import ascii_uppercase
import matplotlib.pyplot as plt
import matplotlib as mpl

class Figure:
    def __init__(self, figsize = (6.5, 4), dpi = 150, invert = True):
        
        self.figure = plt.figure(dpi = dpi, figsize = figsize)
        self.axmain = plt.gca()

        self.figure.patch.set_alpha(0)
        self.axmain.patch.set_alpha(0)
        self.axmain.set_position([0,0,1,1])

        self.axmain.set_ylim(0, figsize[1])
        self.axmain.set_xlim(0, figsize[0])
        
        self.figsize = figsize
        self.dpi = dpi
        
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
        
    def add_letter(self, x, y, letter = None, fontsize = 12, ha = "left", va = "top", color = "black", zorder = 20):
        if letter == None:
            letter_to_add = ascii_uppercase[len(self.letters)]
        else:
            letter_to_add = letter
        
        self.letters.append(letter_to_add)
        self.axmain.text(x, y, letter_to_add, ha = ha, va = va, fontweight = "bold", color = color, fontsize = fontsize, zorder = zorder)
        
    def add_panel(self, dim):
        panel = self.axmain.inset_axes(dim, transform = self.axmain.transData)
        self.panels.append(panel)
        
        return panel
    
    def highlight_panel(self, panel):
        if isinstance(panel, int):
            for spine in self.panels[0].spines:
                self.panels[0].spines[spine].set_color("red")
                self.panels[0].spines[spine].set_visible(True)
                
        elif isinstance(panel, mpl.axes.Axes):
            panel.axis("on")
            for spine in panel.spines:
                panel.spines[spine].set_color("red")
                panel.spines[spine].set_visible(True)
                
    def savefig(self, path, dpi = 300, **kwargs):
        self.remove_figure_borders()
        self.figure.savefig(path, dpi = dpi, **kwargs)
