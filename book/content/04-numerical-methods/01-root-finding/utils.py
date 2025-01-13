import numpy as np
import matplotlib.pyplot as plt

def point_gridlines(ax, x, y, lw = 2):
    xlims = ax.get_xlim()
    
    ax.plot([x, x], [0, y], 'k--')
    ax.plot([xlims[0], x], [y, y], 'k--')
    
    ax.set_xlim(xlims)

def _add_xticks(ax, xticks, xtick_labels, fs):
    xticks_prev = ax.get_xticks()

    xtick_labels_prev = ax.get_xticklabels()
    
    xticks = np.concatenate((xticks_prev, xticks))
    xtick_labels = np.concatenate( (xtick_labels_prev, xtick_labels ) )
    
    ax.set_xticks(xticks)
    ax.set_xticklabels(xtick_labels, fontsize = fs)

def _add_yticks(ax, yticks, ytick_labels, fs):
    yticks_prev = ax.get_yticks()

    ytick_labels_prev = ax.get_yticklabels()
    
    yticks = np.concatenate((yticks_prev, yticks))
    ytick_labels = np.concatenate( (ytick_labels_prev, ytick_labels ) )
    
    ax.set_yticks(yticks)
    ax.set_yticklabels(ytick_labels, fontsize = fs)


def points_plot(f, x_vals, xticklabels, yticklabels,
    xlims, fs = 16, lw = 2, figsize = [9, 6]):
    
    #TODO: use annotations to put xticks on the y=0 line
    
    x_vals = np.array(x_vals)
    f_vals = f(x_vals)

    x = np.linspace(xlims[0], xlims[1])
    
    fig, ax = plt.subplots(figsize = figsize)
    
    ax.plot(x, f(x), 'k', linewidth = lw)
    
    for x_v, f_v in zip(x_vals, f_vals):
        point_gridlines(ax, x_v, f_v, lw = lw)
    
    ax.plot(x_vals, f_vals , 'ko')
    
    ax.set_xticks(x_vals)
    ax.set_xticklabels(xticklabels, fontsize = fs)
    
    ax.set_yticks(np.concatenate( (f_vals, [0]) ))
    ax.set_yticklabels(np.concatenate( (yticklabels, ['0'])), fontsize = fs)
    
    xlims = ax.get_xlim()
    ax.plot(xlims, [0,0], 'k')
    ax.set_xlim(xlims)
    
    #ax.grid(linewidth = lw)
    return fig, ax


def interval_plot(f, a, b, xlims, fs = 16, lw = 2, figsize = [9, 6]):
    #TODO: use annotations to put xticks on the y=0 line
    
    return points_plot(f, [a, b], [r'$x_L$', r'$x_R$'],
        [r'$f(x_L)$', r'$f(x_R)$'], xlims, fs, lw, figsize)

    # f_a = f(a)
    # f_b = f(b)
    
    # x = np.linspace(xlims[0], xlims[1])
    
    # fig, ax = plt.subplots(figsize = figsize)
    
    # ax.plot(x, f(x), 'k', linewidth = lw)
    
    
    # point_gridlines(ax, a, f_a, lw = lw)
    # point_gridlines(ax, b, f_b, lw = lw)
    # ax.plot([a, b], [f_a, f_b] , 'ko')
    
    # ax.set_xticks([a, b])
    # ax.set_xticklabels([r'$x_L$', r'$x_R$'], fontsize = fs)
    
    # ax.set_yticks([f_a, 0, f_b])
    # ax.set_yticklabels([r'$f(x_L)$', '0', r'$f(x_R)$'], fontsize = fs)
    
    # xlims = ax.get_xlim()
    # ax.plot(xlims, [0,0], 'k')
    # ax.set_xlim(xlims)
    
    # #ax.grid(linewidth = lw)
    # return fig, ax

def bisect_plot(f, a, b, xlims, fs = 16, lw = 2):
    
    x_m = 0.5*(a + b)
    f_m = f(x_m)
    
    fig, ax = interval_plot(f, a, b, xlims, fs, lw)
    
    point_gridlines(ax, x_m, f_m, lw=lw)
    
    ax.plot(x_m, f_m, 'ko')
    
    
    xticks = ax.get_xticks()
    xtick_labels = ax.get_xticklabels()
    
    xticks = np.concatenate((xticks, [x_m]))
    xtick_labels = np.concatenate( (xtick_labels, [r'$x_M$'] ) )
    
    ax.set_xticks(xticks)
    ax.set_xticklabels(xtick_labels, fontsize = fs)
    
    yticks = ax.get_yticks()
    ytick_labels = ax.get_yticklabels()
    
    yticks = np.concatenate(( yticks, [f_m]) )
    ytick_labels = np.concatenate((ytick_labels, [r'$f(x_M)$']))
    
    ax.set_yticks(yticks)
    ax.set_yticklabels(ytick_labels, fontsize = fs)
    
    return fig, ax

def secant_plot(f, x1, x2, i, xlims, fs = 16, lw =2, 
    figsize = [9, 6]):

    fig, ax = points_plot(f, [x1, x2], 
        [r'$x_{{{}}}$'.format(i), r'$x_{{{}}}$'.format(i+1)],
        [r'$f(x_{{{}}})$'.format(i), r'$f(x_{{{}}})$'.format(i+1)],
        xlims, fs, lw, figsize)
    
    x3 = x2 - f(x2)*(x2 - x1)/(f(x2) - f(x1))
    
    xticks = ax.get_xticks()
    xticklabels = ax.get_xticklabels()

    xticks = np.concatenate( (xticks, [x3]))
    xticklabels = np.concatenate( (xticklabels, [r'$x_{{{}}}$'.format(i+2)]) )

    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels)

    x_plot = np.array([x1, x2, x3])
    order = x_plot.argsort()
    y_plot = np.array([f(x1), f(x2), 0])

    ax.plot(x_plot[order], y_plot[order], 'k:', lw= lw)
    ax.plot(x3, 0, 'ko', fillstyle = 'none')
    return fig, ax

def newton_plot(f, fprime, x, i, xlims, fs = 16, lw = 2, figsize = [9, 6]):

    fig, ax = points_plot(f, [x], [r'$x_{{{}}}$'.format(i)], [r'$f(x_{{{}}})$'.format(i)], xlims, fs, lw, figsize)

    x1 = x - f(x)/fprime(x)

    ax.plot([x, x1], [f(x), 0], 'k:', lw = lw)
    ax.plot(x1, 0, 'ko', fillstyle = 'none')

    _add_xticks(ax, [x1], [r'$x_{{{}}}$'.format(i+1)], fs)

    return fig, ax