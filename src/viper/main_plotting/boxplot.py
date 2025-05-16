import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np 

def boxplot(ax, x, data, jitter_data = False, clip_on = False, **kwargs):

    """
    A function to plot a box plot on a given matplotlib axis with additional options for jittered data. Will omit nans from the data. 
    Parameters:
    ax : matplotlib axis object
        The axis object to plot the box plot on.
    x : float or int
        The x position of the box plot on the axis.
    data : array-like (1D)
        The data to plot in the box plot.
    jitter_data : bool, optional
        If True, adds jittered data to the plot. Default is False.
    clip_on : bool, optional
        If True, allows data to clip past edges of the ax. Default is False.
    **kwargs : keyword arguments, optional
    
    Additional options to customize the plot, including:
        - linewidth (float): The width of the box plot and whiskers. Default is 1.2.
        - box_lw (float): The width of the box edges. Default is the linewidth value.
        - box_width (float): The width of the box. Default is 0.5.
        - whisker_lw (float): The width of the whiskers. Default is the box_lw value.
        - color (str): The color of the box plot and whiskers. Default is "#0BB8FD".
        - noise_scale (float): The scale of the jittered noise added to the data points. Default is 0.06.
        - data_color (str): The color of the jittered data points. Default is the color value.
        - include_mean (bool): If True, adds a marker for the mean of the data. Default is False.

        - data_lw (float): The width of the jittered data points. Default is 0.5.
        - data_size (int): The size of the jittered data points. Default is 40.
        - data_alpha (float): The alpha value of the jittered data points. Default is 1.
        - data_zorder (int): The z-order of the jittered data points. Default is 0.

        - mean_size (int): The size of the mean marker. Default is the data_size value.
        - mean_alpha (float): The alpha value of the mean marker. Default is 1.
        - mean_color (str): The color of the mean marker. Default is "#727273".
        - mean_zorder (int): The z-order of the mean marker. Default is 0.

    Returns:
    ax : matplotlib axis object
        The axis object with the box plot and optional jittered data added.
    """
    if "lw" in kwargs.keys() and "linewidth" in kwargs.keys():
        raise ValueError("Keyword argument repeated.")
        
    linewidth = kwargs.get("linewidth", 1.2)
    lw = kwargs.get("lw", linewidth)
    
    box_lw       = kwargs.get("box_lw", lw)
    box_width    = kwargs.get("box_width", .5)
    whisker_lw   = kwargs.get("whisker_lw", box_lw)

    color = kwargs.get("color",   "#0BB8FD")

    #box properties
    box_props   = {"facecolor": "none", "edgecolor" : color, "linewidth": box_lw, "alpha": 1}

    #whisker properties
    whisker_props = {"linewidth" : whisker_lw, "color": color}

    #cap properties
    cap_props = {"linewidth" : whisker_lw, "color": color}

    #median properties
    median_props = {"linewidth" : whisker_lw, "color": color}

    '''Make Box Plots'''
    ax.patch.set_alpha(0)
        
    data = np.array(data)
    filtered_data = data[~np.isnan(data)]
    
    #Make Box
    bp = ax.boxplot([filtered_data],   positions = [x], patch_artist = True,  showfliers = False, 
                boxprops = box_props  , whiskerprops = whisker_props,
                capprops = cap_props, medianprops = median_props, widths = box_width)
    
    #Add jittered data
    if jitter_data:
        noise_scale = kwargs.get("noise_scale", .06)
        data_color = kwargs.get("data_color", color)
        include_mean = kwargs.get("include_mean", False)
        
        data_lw = kwargs.get("data_lw", .5)
        data_size = kwargs.get("data_size", 40)
        data_alpha = kwargs.get("data_alpha", 1)
        data_zorder = kwargs.get("data_zorder", 0)
        
        mean_size = kwargs.get("mean_size", data_size)
        mean_alpha = kwargs.get("mean_alpha", 1)
        mean_color = kwargs.get("mean_color", '#727273')
        mean_zorder = kwargs.get("mean_zorder", 0)

        noise = np.random.normal(0, noise_scale, len(filtered_data))
        
        ax.scatter(x + noise, filtered_data,
                s = data_size, facecolors = 'none', clip_on = clip_on,
               edgecolors=data_color, alpha = data_alpha, lw = data_lw, zorder = data_zorder)
            
        if include_mean:
            ax.scatter(x, np.nanmean(filtered_data) ,
                        s = data_size, facecolors = mean_color, clip_on = clip_on,
                       edgecolors=mean_color, alpha = mean_alpha, lw = data_lw, zorder = mean_zorder)
        
    return ax
