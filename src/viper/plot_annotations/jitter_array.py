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
    data_size  = kwargs.get("data_size", 8)
    data_alpha = kwargs.get("data_alpha", 1)
    data_lw    = kwargs.get("data_lw", 0.5)

    include_mean = kwargs.get("include_mean", True)
    
    linewidth    = kwargs.get("linewidth", None) #same as lw
    lw           = kwargs.get("lw", None)        #same as linewidth
    
    data_color   = kwargs.get("data_color", "grey")
    data_edge_color = kwargs.get("data_line_color", "grey")
    data_zorder = kwargs.get("data_zorder", 0)

    mean_color   = kwargs.get("mean_color", '#727273')
    mean_edge_color = kwargs.get("mean_line_color", "#727273")
    mean_zorder = kwargs.get("mean_zorder", 0)
    """
    data_size  = kwargs.get("data_size", 8)
    data_alpha = kwargs.get("data_alpha", 1)

    mean_size  = kwargs.get("mean_size", 8)
    mean_alpha = kwargs.get("mean_alpha", 1)

    include_mean = kwargs.get("include_mean", True)
    linewidth    = kwargs.get("linewidth", None) #same as lw
    lw           = kwargs.get("lw", None)        #same as linewidth

    data_color   = kwargs.get("data_color", "grey")
    data_line_color = kwargs.get("data_line_color", "grey")

    mean_color   = kwargs.get("mean_color", '#727273')
    mean_line_color = kwargs.get("mean_line_color", "#727273")
    data_lw    = kwargs.get("data_lw", 0.5)
    mean_zorder = kwargs.get("mean_zorder", 0)
    data_zorder = kwargs.get("data_zorder", 0)
    
    if linewidth == None and lw == None:
        lw = 0.3
    elif linewidth != None:
        lw = linewidth
        
    x_positions = np.array(x_positions)
    
    #plot individual datapoints
    if isinstance(data_list, list): 
        data_length = len(data_list)
    else: #2D array
        data_length = len(data_list[0])
    for i in range(data_length):
        noise = np.random.normal(0, noise_scale)

        #get first row of data
        data = [x[i] for x in data_list]
        ax.plot(x_positions + noise, data,
                 lw = lw, c = data_line_color, alpha = data_alpha, zorder = data_zorder-1, clip_on = False)

        ax.scatter(x_positions + noise, data,
                    s = data_size, facecolors = 'none',
                   edgecolors=data_color, alpha = data_alpha, lw = data_lw, zorder = data_zorder, clip_on = False)
        
    #Plot mean datapoints
    if include_mean:
        ax.plot(x_positions, [np.nanmean(array) for array in data_list],
                     lw = 2*lw, c = mean_line_color, alpha = mean_alpha, zorder = mean_zorder, clip_on = False)

        ax.scatter(x_positions, [np.nanmean(array) for array in data_list],
                    s = mean_size, facecolors = mean_color,
                   edgecolors = mean_color, alpha = mean_alpha, lw = data_lw, zorder = mean_zorder, clip_on = False)
