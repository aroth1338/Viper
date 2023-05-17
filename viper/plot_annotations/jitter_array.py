import matplotlib.pyplot as plt
import numpy as np

def jitter_array(ax, x_positions, data_list, noise_scale = 0.05, **kwargs):
    """
    Plots individual connecting data with a gaussian jitter. 
    noise_scale sets the magnitude of the jitter
    
    Inputs
    ax: axis to plot to
    x_positions: list or 1D array of x_positions to center data on
    data_list: list of 1D arrays or 2D array of data. Columns correspond to x_positions, Rows correspond to individual data
    noise_scale: spread of normal distribution to generate noise
    
    Optional Arguments:
    circle_size  = kwargs.get("circle_size", 8)
    circle_alpha = kwargs.get("circle_alpha", 1)
    circle_lw    = kwargs.get("circle_lw", 0.5)

    include_mean = kwargs.get("include_mean", True)
    
    linewidth    = kwargs.get("linewidth", None) #same as lw
    lw           = kwargs.get("lw", None)        #same as linewidth
    
    data_color   = kwargs.get("data_color", "grey")
    data_edge_color = kwargs.get("data_edge_color", "grey")
    data_zorder = kwargs.get("data_zorder", 0)

    mean_color   = kwargs.get("mean_color", '#727273')
    mean_edge_color = kwargs.get("mean_edge_color", "#727273")
    mean_zorder = kwargs.get("mean_zorder", 0)
    """
    circle_size  = kwargs.get("circle_size", 8)
    circle_alpha = kwargs.get("circle_alpha", 1)
    include_mean = kwargs.get("include_mean", True)
    linewidth    = kwargs.get("linewidth", None) #same as lw
    lw           = kwargs.get("lw", None)        #same as linewidth
    data_color   = kwargs.get("data_color", "grey")
    data_edge_color = kwargs.get("data_edge_color", "grey")
    mean_color   = kwargs.get("mean_color", '#727273')
    mean_edge_color = kwargs.get("mean_edge_color", "#727273")
    circle_lw    = kwargs.get("circle_lw", 0.5)
    mean_zorder = kwargs.get("mean_zorder", 0)
    data_zorder = kwargs.get("data_zorder", 0)
    
    if linewidth == None and lw == None:
        lw = 0.3
    elif linewidth != None:
        lw = linewidth
        
    x_positions = np.array(x_positions)
    
    #plot individual datapoints
    if np.ndim(data_list) == 1: #HALP
        data_length = len(data_list)
    else:
        data_length = len(data_list[0])
    for i in range(data_length):
        noise = np.random.normal(0, noise_scale)

        #get first row of data
        data = [x[i] for x in data_list]
        ax.plot(x_positions + noise, data,
                 lw = lw, c = data_edge_color, alpha = circle_alpha, zorder = data_zorder-1)

        ax.scatter(x_positions + noise, data,
                    s = circle_size, facecolors = 'none',
                   edgecolors=data_color, alpha = circle_alpha, lw = circle_lw, zorder = data_zorder)
        
    #Plot mean datapoints
    if include_mean:
        ax.plot(x_positions, [np.nanmean(array) for array in data_list],
                     lw = 2*lw, c = mean_edge_color, alpha = 1, zorder = mean_zorder)

        ax.scatter(x_positions, [np.nanmean(array) for array in data_list],
                    s = circle_size, facecolors = mean_color,
                   edgecolors=mean_color, alpha = 1, lw = circle_lw, zorder = mean_zorder)
