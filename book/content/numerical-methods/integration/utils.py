import numpy as np
import matplotlib.pyplot as plt

FS = 16
LW = 2
FIGSIZE = [9,6]
FILL_COLOR = '0.8'
DOT_COLOR = '0.4'
SOLID_COLOR = '0.4'

#Integration techniques
def plot_midpoint(f, a, b, n, xlims, fs = FS, lw = LW, figsize = FIGSIZE):
    fig, ax = plt.subplots(figsize = figsize)

    dx = float(b-a)/n

    #Instancing ticks
    xticks = [a]
    xtick_labels = [r'$x_0 = a$']
    
    #yticks = []
    #ytick_labels = []

    for i in range(n):
        xl = a + i*dx
        xr = a + (i+1)*dx
        xm = a + (i + 0.5)*dx
        fm = f(xm)

        #Fill
        ax.fill_between([xl, xr], [fm, fm], color = FILL_COLOR)

        #Dotted lines
        #ax.plot([xlims[0], xl], [fm, fm], color = DOT_COLOR, ls = '--', lw = lw)
        ax.plot([xl, xl], [0, fm], color = DOT_COLOR, ls = '--', lw = lw)
        ax.plot([xm, xm], [0, fm], color = DOT_COLOR, ls = '--', lw = lw)

        #Midpoint
        ax.plot(xm, fm, 'ko')

        #Top line
        ax.plot([xl, xr], [fm, fm], color = SOLID_COLOR, lw = lw)

        xm_label = r'\frac{{x_{{{}}} + x_{{{}}}}}{{ 2 }}'.format(i, i+1)
        
        xticks += [xm, xr]
        xtick_labels += [f'${xm_label}$', r'$x_{{{}}}$'.format(i+1)]

        #yticks.append(fm)
        #ytick_labels.append(f'$f({xm_label})$')

    xtick_labels = xtick_labels[:-1] + [r'$x_{{{}}} = b$'.format(n)]

    ax.plot([b, b], [0, f(xm)], '--k', lw)
    
    #y = 0 line
    ax.plot(xlims, [0,0], 'k-', lw = lw)
    #yticks.append(0)
    #ytick_labels.append('0')

    #Plotting f above everything else
    x = np.linspace(*xlims)
    ax.plot(x, f(x), 'k-', lw = lw)

    #Setting xlims
    ax.set_xlim(xlims)
    

    #Set ticks
    ax.set_xticks(xticks)
    ax.set_xticklabels(xtick_labels, fontsize = fs)

    #ax.set_yticks(yticks)
    #ax.set_yticklabels(ytick_labels, fontsize =fs)

    ax.set_yticks([0])
    ax.set_yticklabels(['0'], fontsize = fs)
    ax.set_ylabel(r'$f(x)$', fontsize = fs)

    return fig, ax

def plot_trapezoidal(f, a, b, n, xlims, fs = FS, lw = LW, figsize = FIGSIZE):

    fig, ax = plt.subplots(figsize = figsize)
    
    dx = (b - a)/n


    #Instancing ticks
    xticks = [a]
    xtick_labels = [r'$x_0 = a$']


    for i in range(n):
        xl = a + i*dx
        xr = a + (i+1)*dx
        fl = f(xl)
        fr = f(xr)

        #Fill
        ax.fill_between([xl, xr], [fl, fr], color = FILL_COLOR)

        #Dotted lines
        #ax.plot([xlims[0], xl], [fl, fl], color = DOT_COLOR, ls = '--', lw = lw)
        #ax.plot([xlims[0], xr], [fr, fr], color = DOT_COLOR, ls = '--', lw = lw)

        ax.plot([xl, xl], [0, fl], color = DOT_COLOR, ls = '--', lw = lw)
        ax.plot([xr, xr], [0, fr], color = DOT_COLOR, ls = '--', lw = lw)

        #Top line
        ax.plot([xl, xr], [fl, fr], color = SOLID_COLOR, lw = lw)

        xticks.append(xr)
        xtick_labels.append(r'$x_{{{}}}$'.format(i+1))


    xtick_labels = xtick_labels[:-1] + [r'$x_{{{}}} = b$'.format(n)]

    
    #y = 0 line
    ax.plot(xlims, [0,0], 'k-', lw = lw)
    ax.set_yticks([0])
    ax.set_yticklabels(['0'], fontsize = fs)

    #Plotting f above everything else
    x = np.linspace(*xlims)
    ax.plot(x, f(x), 'k-', lw = lw)

    #Setting xlims
    ax.set_xlim(xlims)

    #Set ticks
    ax.set_xticks(xticks)
    ax.set_xticklabels(xtick_labels, fontsize = fs)

    ax.set_ylabel(r'$f(x)$', fontsize = fs)
    return fig, ax


def plot_simpsons(f, a, b, n, xlims, fs = FS, lw = LW, figsize = FIGSIZE):

    fig, ax = plt.subplots(figsize = figsize)
    
    dx = (b - a)/n


    #Plotting f above everything else
    x = np.linspace(*xlims)
    ax.plot(x, f(x), 'k-', lw = lw)

    #Instancing ticks
    xticks = [a]
    xtick_labels = [r'$x_0 = a$']


    for i in range(n):
        xl = a + i*dx
        xr = a + (i+1)*dx
        xm = 0.5*(xl + xr)

        fl = f(xl)
        fr = f(xr)
        fm = f(xm)

        #Fill
        x = np.linspace(xl, xr)
        fx = lagrange(x, [xl, xm , xr], [fl, fm, fr])

        ax.fill_between(x, fx, color = FILL_COLOR)

        #Dotted lines
        ax.plot([xl, xl], [0, fl], color = DOT_COLOR, ls = ':', lw = lw)
        ax.plot([xm, xm], [0, fm], color = DOT_COLOR, ls = ':', lw = lw)
        ax.plot([xr, xr], [0, fr], color = DOT_COLOR, ls = ':', lw = lw)

        #Top line
        ax.plot(x, fx, color = SOLID_COLOR, ls = '--', lw = lw)

        xticks.append(xr)
        xtick_labels.append(r'$x_{{{}}}$'.format(i+1))


    xtick_labels = xtick_labels[:-1] + [r'$x_{{{}}} = b$'.format(n)]

    
    #y = 0 line
    ax.plot(xlims, [0,0], 'k-', lw = lw)
    ax.set_yticks([0])
    ax.set_yticklabels(['0'], fontsize = fs)


    #Setting xlims
    ax.set_xlim(xlims)

    #Set ticks
    ax.set_xticks(xticks)
    ax.set_xticklabels(xtick_labels, fontsize = fs)

    ax.set_ylabel(r'$f(x)$', fontsize = fs)
    return fig, ax

def lagrange(x, x_data, y_data):
    result = 0

    for i, xi in enumerate(x_data):
        term = y_data[i]
        for xj, yj in zip(x_data[:i] + x_data[i+1:], y_data[:i] + y_data[i+1:]):
            term *= (x - xj)/(xi - xj)
        result += term
    
    return result

# Plots
def point_gridlines(ax, x, y, lw = 2):
    xlims = ax.get_xlim()
    
    ax.plot([x, x], [0, y], ls = '--', color = DOT_COLOR)
    ax.plot([xlims[0], x], [y, y], ls = '--', color = DOT_COLOR)
    
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
    
    return points_plot(f, [a, b], [r'$a$', r'$b$'],
        [r'$f(a)$', r'$f(b)$'], xlims, fs, lw, figsize)
