from .Custom_Legend import *
from .set_Axes_Color import *
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
import numpy as np

def _zero_to_nan(values):
    """Replace every 0 with 'nan' and return a copy."""
    return [float('nan') if x==0 else x for x in values]

def Pair_Plot(parameter_array, labels, **kwargs):
    """
    Plots distribution of parameters, with marginal distributions on the diagonal and joint
    distributions everywhere else.
    #optional parameters
        box_color          = kwargs.get("box_color", 'black')
        dot_color          = kwargs.get("dot_color", '#B2B1B3') #light grey
        cumulative_color   = kwargs.get("cumulative_color", "#218421") #dark green
        marginal_color     = kwargs.get("marginal_color", "#33cc33") #green
        legend_color       = kwargs.get("legend_color", "#218421") #dark green
        significance_color = kwargs.get("significance_color", '#33cc33') #green

        labelcolor       = kwargs.get("labelcolor", box_color)
        labelsize        = kwargs.get("labelsize" , 10)
        confidence_color = kwargs.get("confidence_color", '#727273') #dark grey

        show_cumulative   = kwargs.get("show_cumulative", True)
        show_significance = kwargs.get("show_significance", False)

        figsize = kwargs.get("figsize", (6, 6))
        dpi     = kwargs.get("dpi", 300)
        hspace  = kwargs.get("hspace", .1)
        wspace  = kwargs.get("wspace", .1)

        bins          = kwargs.get("bins", 25)
        tick_size     = kwargs.get("tick_size", 8)
        cumulative_lw = kwargs.get("cumulative_lw", 1.5)

        dot_alpha      = kwargs.get("dot_alpha", 1)
        marginal_alpha = kwargs.get("marginal_alpha", 1)
        
        remove_heavy_outliers = kwargs.get("remove_heavy_outliers", False) #remove data points farther than 5 standard deviations away from the mean (significantly more extreme than 99.99994% of the data)
    """
    num_params = parameter_array.shape[1]

    #optional parameters
    box_color          = kwargs.get("box_color", 'black') 
    dot_color          = kwargs.get("dot_color", '#B2B1B3') #light grey
    cumulative_color   = kwargs.get("cumulative_color", "#218421") #dark green
    marginal_color     = kwargs.get("marginal_color", "#33cc33") #green
    legend_color       = kwargs.get("legend_color", "#218421") #dark green
    significance_color = kwargs.get("significance_color", '#33cc33') #green

    labelcolor       = kwargs.get("labelcolor", box_color)
    labelsize        = kwargs.get("labelsize" , 10)
    confidence_color = kwargs.get("confidence_color", '#727273')#dark grey

    show_cumulative   = kwargs.get("show_cumulative", True)
    show_significance = kwargs.get("show_significance", False)

    figsize = kwargs.get("figsize", (6, 6))
    dpi     = kwargs.get("dpi", 300)
    hspace  = kwargs.get("hspace", .1)
    wspace  = kwargs.get("wspace", .1)

    bins          = kwargs.get("bins", 25)
    tick_size     = kwargs.get("tick_size", 8)
    cumulative_lw = kwargs.get("cumulative_lw", 1.5)

    dot_alpha      = kwargs.get("dot_alpha", 1)
    marginal_alpha = kwargs.get("marginal_alpha", 1)
    
    remove_heavy_outliers = kwargs.get("remove_heavy_outliers", False)
    
    if remove_heavy_outliers:
        for i in range(parameter_array.shape[1]):
            data_values = parameter_array[:, i]
            mean = np.nanmean(data_values)
            std = np.nanstd(data_values)
            outlier_mask = np.abs(data_values - mean) < 5*std 
            nan_mask = _zero_to_nan(np.ones_like(data_values) * outlier_mask)
            parameter_array[:, i] = data_values * nan_mask
    
    if kwargs.get("black_background", False):
        dot_color = "w"
        box_color = "w"
        labelcolor = "w"
        confidence_color = "w"
    
    fontdict = dict(fontsize = tick_size, color = labelcolor)
    
    fig, ax = plt.subplots(nrows = num_params , ncols = num_params, dpi = dpi, figsize = figsize, gridspec_kw = dict(hspace = hspace, wspace = wspace))

    for row in range(num_params):
        for col in range(num_params):
            max_val = np.nanmax(parameter_array[:, col])
            min_val = np.nanmin(parameter_array[:, col])

            max_val += 0.005*max_val
            min_val -= 0.005*min_val

            ymax_val = np.nanmax(parameter_array[:, row])
            ymin_val = np.nanmin(parameter_array[:, row]) 

            ymax_val += 0.005*ymax_val
            ymin_val -= 0.005*ymin_val
        
          #Plot Marginal Distribution at the bottom of the figure
            if row == col:
              #Marginal
                values, base, tmp = ax[row, col].hist(parameter_array[:, col], bins = bins, density = True, color = marginal_color, zorder = 0, alpha = marginal_alpha)

                if show_cumulative:
                    #Plot cumulative behind the marginal
                    axin = ax[row, col].inset_axes([0, 0, 1, 1], zorder = 5)    # create new inset axes in axes coordinates
                    #evaluate the cumulative
                    cumulative = np.cumsum(values)
                    # plot the cumulative function
                    axin.plot(base[:-1], cumulative, c= cumulative_color, lw = cumulative_lw)
                    axin.patch.set_alpha(0)
                    axin.axis("off")
                    axin.set_xlim(min(base[:-1]), max(base[:-1]))
                    axin.set_ylim(min(cumulative), 1.025*max(cumulative) )

                #Plot 95% intervals
                sorted_arr = np.sort(parameter_array[:, col]) 
                low_end = sorted_arr[int(0.025 * sorted_arr.shape[0])]
                high_end = sorted_arr[int(0.975 * sorted_arr.shape[0])]
                interval_height = max(values)
                ax[row, col].plot([low_end, low_end], [0, interval_height], color = confidence_color, lw = cumulative_lw)
                ax[row, col].plot([high_end, high_end],[0, interval_height], color = confidence_color, lw = cumulative_lw)
                #Set Border color
                set_Axes_Color(ax[row, col], box_color, remove_spines = True)

                ax[row, col].set_xlim(min_val, max_val)
            
          #Plot Joint Distributions
            else:
                #get rho and p_val
                rho, p_val = spearmanr(parameter_array[:, col], parameter_array[:, row])
                #If significant, color dots green and display stats
                if p_val < 0.05 :
                    ax[row, col].scatter(parameter_array[:, col], parameter_array[:, row], s = 1, lw = 0, color = dot_color, label = fr'$\rho = {rho:.3f}$', alpha = dot_alpha)
                    ax[row, col].set_xlim(min_val, max_val)

                    if p_val < 0.001: p_string = "p < 0.001"
                    else: p_string = f"p = {p_val:.3f}"
                    
                    if show_significance:
                        if row == col:
                            Custom_Legend(ax[row, col], [p_string, r'$\mathbf{\rho = }$' + f'{rho:.3f}'], [legend_color, legend_color], linewidth = 0, fontsize = 6,loc = "upper left", handlelength = 0, handletextpad = 0)
                        else:
                            Custom_Legend(ax[row, col], [p_string, r'$\mathbf{\rho = }$' + f'{rho:.3f}'], [legend_color, legend_color], linewidth = 0, fontsize = 6,loc = 0, handlelength = 0, handletextpad = -0)

                    set_Axes_Color(ax[row, col], box_color, remove_spines = True)
              #If not significant, grey out the dots
                else:
                    ax[row, col].scatter(parameter_array[:, col], parameter_array[:, row], s = 1, lw = 0, color = dot_color, alpha = dot_alpha)
                    ax[row, col].set_xlim(min_val, max_val)

                    set_Axes_Color(ax[row, col], box_color, remove_spines = True)

                xlims = ax[row, col].get_xlim()
                ylims = ax[row, col].get_ylim()

                ax[row, col].set_xlim(min_val, max_val)
                ax[row, col].set_ylim(ymin_val, ymax_val)

    ###############################################################################################################
    #Set labels and ticks
    for row in range(num_params):
        for col in range(num_params):

            #Set ylabels and ticks
            if col == 0 and row != 0: #Want to handle plot [0, 0] special later on
                ax[row, col].set_ylabel(labels[row], fontsize = labelsize, color = labelcolor)

                y_lims = ax[row, row].get_xlim()
                ax[row, col].set_ylim(y_lims)
                #setting yticklabels to 20% and 80% of limits
                ax[row, col].set_yticks([y_lims[0] + .2 * abs(y_lims[1] - y_lims[0]), y_lims[0] + .8*abs(y_lims[1] - y_lims[0])], fontsize = tick_size, fontcolor = "k")
                ax[row, col].set_yticklabels([f"{y_lims[0] + .2 * abs(y_lims[1] - y_lims[0]):.3f}", f"{y_lims[0] + .8*abs(y_lims[1] - y_lims[0]):.3f}"], fontdict = fontdict)
  
            else:
                ax[row, col].set_yticks([])

          #Set xlabels and ticks
            if row == num_params-1:
                ax[row, col].set_xlabel(labels[col], fontsize = labelsize, color = labelcolor)

                x_lims = ax[row, col].get_xlim()

                ax[row, col].set_xticks([x_lims[0] + .2 * abs(x_lims[1] - x_lims[0]), x_lims[0] + .8*abs(x_lims[1] - x_lims[0])], size = tick_size, fontcolor = "k")
                ax[row, col].set_xticklabels([f"{x_lims[0] + .2 * abs(x_lims[1] - x_lims[0]):.3f}", f"{x_lims[0] + .8*abs(x_lims[1] - x_lims[0]):.3f}"], fontdict = fontdict)

            else:
                ax[row, col].set_xticks([])


          #If at the bottom row, adjust the marginal distribution at [0, 0]
            if row == num_params-1 and col == 0:
                ax[0, 0].set_ylabel(labels[0], fontsize = labelsize, color = labelcolor)

                y_lims = ax[0, 0].get_ylim()
                new_ylims = ax[0, 1].get_ylim()

                ax[0, 0].set_yticks([y_lims[0] + .2 * abs(y_lims[1] - y_lims[0]), y_lims[0] + .8*abs(y_lims[1] - y_lims[0])])
                ax[0, 0].set_yticklabels([f"{new_ylims[0] + .2 * abs(new_ylims[1] - new_ylims[0]):.3f}", f"{new_ylims[0] + .8*abs(new_ylims[1] - new_ylims[0]):.3f}"], fontdict = fontdict)
    return fig, ax
