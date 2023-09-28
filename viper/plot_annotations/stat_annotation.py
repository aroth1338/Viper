import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def stat_annotation(ax, x1, x2, y, p = None, d = None, theta = None, theta_first = False, preamble = None, **kwargs):
    """
    Annotate plot to have statistics.
    d is Cohen's D
    theta is Common Language Effect Size
    preamble is any text that goes before the statistics
    
    Optional Arguments:
    color            = kwargs.get("color", "grey")
    h                = kwargs.get("h", 0.1 * y)
    lw               = kwargs.get("lw", .7)
    fontsize         = kwargs.get("fontsize", 6)
    exact_p          = kwargs.get("exact_p", False)
    indicator_length = kwargs.get("indicator_length", 0)
    stacked          = kwargs.get("stacked", False)
    fontweight 
    """
    main_effect_prong = False
    
    if type(x1) in [np.ndarray, list, tuple]:
        main_effect_prong = True
        if np.size(x1) == 1:
            main_effect_prong = False
        
    if main_effect_prong:
        if np.shape(x1) != np.shape(x2):
            raise ValueError('Wrong Axis Shape')
         
    ylim = ax.get_ylim()         
    color = kwargs.get("color", "grey")
    h = kwargs.get("h", 0.005*(ylim[1] - ylim[0]))
    lw = kwargs.get("lw", .7)
    fontsize = kwargs.get("fontsize", 6)
    exact_p = kwargs.get("exact_p", False)
    indicator_length = kwargs.get("indicator_length", 0)
    stacked = kwargs.get("stacked", False)
    
    #Handle P-Value
    if p == None:
        p_text = ""
    elif p < 0.001 and not exact_p:
        p_text = f"p < 0.001"
    elif p >= 0.001 or exact_p:
        p_text = f"p = {p:.3f}"
        
    #Handle Effect Size and Common Language Effect Size
    if d != None and theta != None: #if both
        
        if theta_first:
            p_text = p_text + r', $\mathbf{\hat{\theta}}$ = ' + f"{theta:.2f}" + f", d = {d:.2f}" 
        else:
            p_text = p_text + f", d = {d:.2f}, " + r'$\mathbf{\hat{\theta}}$ = ' + f"{theta:.2f}"
            
    elif d != None and theta == None: #if only Cohen D
        p_text = p_text + f", d = {d:.2f}" 
        
    elif d == None and theta != None: #if only theta
        p_text = p_text + r', $\mathbf{\hat{\theta}}$ = ' + f"{theta:.2f}"

    if preamble != "" and preamble != None: #If Preamble
        if not stacked:
            p_text = preamble + " " + p_text 
        else:
            p_text = preamble + ", " + p_text
            
    #plot the text
    if main_effect_prong:
        ax.plot([np.nanmean(x1), np.nanmean(x1), np.nanmean(x2), np.nanmean(x2)], [y[1], y[0], y[0], y[2]], lw=lw, c=color)
        ax.plot([x1[0],x1[0],x1[1],x1[1]],[y[1] - indicator_length, y[1], y[1], y[1] - indicator_length], lw=lw, c=color)
        ax.plot([x2[0],x2[0],x2[1],x2[1]],[y[2] - indicator_length, y[2], y[2], y[2] - indicator_length], lw=lw, c=color)
        y_ax = y[0]
    else:
        ax.plot([x1, x1, x2, x2], [y - indicator_length, y, y, y - indicator_length], lw=lw, c=color, clip_on = False)
        y_ax = y

    if not stacked:
        ax.text((np.nanmean(x1)+np.nanmean(x2))*.5, y_ax+h , p_text, ha='center', va='bottom', color=color, fontsize = fontsize, weight = "bold")
    else:
        split_text = p_text.split(", ")
        stacked_text = "\n".join(split_text)
        
        ax.text((np.nanmean(x1)+np.nanmean(x2))*.5, y_ax+h , stacked_text, ha='center', va='bottom', color=color, fontsize = fontsize, weight = "bold")