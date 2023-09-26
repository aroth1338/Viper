from string import ascii_uppercase
import matplotlib.pyplot as plt
import matplotlib as mpl

class Figure:
    def __init__(self, axmain = None, ax = None, figsize = (6.5, 4), dpi = 150, invert = True):
        
        if axmain == None and ax == None:
            fig = plt.figure(dpi = dpi, figsize = figsize)
            axmain = plt.gca()

            fig.patch.set_alpha(0)
            axmain.patch.set_alpha(0)
            axmain.set_position([0,0,1,1])

            axmain.set_ylim(0, figsize[1])
            axmain.set_xlim(0, figsize[0])

            inset_dimensions = [0, 0, figsize[0], figsize[1]]
            ax = axmain.inset_axes(inset_dimensions, transform=axmain.transData)

            ax.patch.set_alpha(0)
            ax.set_ylim(0, inset_dimensions[3])
            ax.set_xlim(0, inset_dimensions[2])

        self.axmain, self.ax = axmain, ax
        
        self.figure = self.axmain.get_figure()
        self.figsize = figsize
        self.dpi = dpi
        
        if invert:
            self.axmain.invert_yaxis()
            self.ax.invert_yaxis()
        
        self.letters = [] #letters for annotating figure
        self.panels  = [] #panels for figure
        
    def remove_figure_borders(self):
        self.axmain.axis("off")
        self.ax.axis("off")
        
    def remove_panel_borders(self):
        for panel in self.panels:
            panel.axis("off")
        
    def add_letter(self, x, y, letter = None, fontsize = 12, ha = "left", va = "top", color = "black", zorder = 20):
        if letter == None:
            letter_to_add = ascii_uppercase[len(self.letters)]
        else:
            letter_to_add = letter
        
        self.letters.append(letter_to_add)
        self.ax.text(x, y, letter_to_add, ha = ha, va = va, fontweight = "bold", color = color, fontsize = fontsize, zorder = zorder)
        
    def add_panel(self, dim):
        panel = self.ax.inset_axes(dim, transform = self.ax.transData)
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
