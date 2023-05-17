import matplotlib.pyplot as plt

def figure_panel(figsize = (6, 3), inset_dimensions = None, dpi = 300):
    """
    Generates figure panel to plot on.
    Figsize is in inches (width, height)
    inset dimensions is in inches [x, y, width, height]
    
    returns main axis and axis to plot to
    """
    fig = plt.figure(dpi = dpi, figsize = figsize)
    axmain = plt.gca()
    
    fig.patch.set_alpha(0)
    axmain.patch.set_alpha(0)
    axmain.set_position([0,0,1,1])
    
    axmain.set_ylim(0, figsize[1])
    axmain.set_xlim(0, figsize[0])
    
    if inset_dimensions == None:
        inset_dimensions = [0, 0, figsize[0], figsize[1]]
    ax = axmain.inset_axes(inset_dimensions, transform=axmain.transData)

    ax.patch.set_alpha(0)
    ax.set_ylim(0, inset_dimensions[3])
    ax.set_xlim(0, inset_dimensions[2])
    return axmain, ax
