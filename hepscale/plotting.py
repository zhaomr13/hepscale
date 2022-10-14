import matplotlib.pyplot as plt
import numpy as np
from math import log
from .utility import units
from matplotlib.widgets import Slider

def adjust_points(xpoints, ypoints, low_bound, high_bound, max_dist):
    for i in range(len(ypoints)):
        ypoints[i] = 2.0
    setted = {}
    for i in range(len(xpoints)):
        x = xpoints[i]
        if x < low_bound or x > high_bound:
            ypoints[i] = 0
            continue
        while ypoints[i] > 0.001:
            list = setted.get(ypoints[i])
            if list is None: setted[ypoints[i]] = []
            passed = True
            for d in setted[ypoints[i]]:
                if (abs(log(xpoints[i] / d)) < max_dist): 
                    passed = False
                    break
            if passed:
                setted[ypoints[i]].append(x)
                break
            else:
                ypoints[i] -= 0.5

def plotscale(data):

    plottitle = ""
    unitstyle = ""
    xpoints = []
    ypoints = []
    xlines = []
    ylines = []
    names = []
    linenames = []
    colors = []
    linecolors = []
    print(unitstyle)
    with open(data, "r") as f:
        plotstyle = f.readline()
        plottitle = f.readline()
        l = f.readline()
        low_limit = int(l.split()[0])
        high_limit = int(l.split()[1])
        unitstyle = l.split()[2]
        unit = units[unitstyle]
        for line in f:
            l = line.split()
            if (l[0] == "p"):
                colors.append(l[1])
                xpoints.append(float(l[2]) * unit[l[3]])
                names.append("{} {} {}".format(l[4], l[2], l[3]))
                ypoints.append(2)
            if (l[0] == "i"):
                colors.append(l[1])
                xpoints.append(1.0/float(l[2]) * unit[l[3]])
                names.append("{} ({} {})$^{{-1}}$".format(l[4], l[2], l[3]))
                ypoints.append(2)
            elif (l[0] == "l"):
                linecolors.append(l[1])
                xlines.append(float(l[2]) * unit[l[3]])
                linenames.append("{} {}".format(l[2], l[3]))
                ylines.append(3)

    fig, ax = plt.subplots(figsize=(20, 4))
    fig.subplots_adjust(bottom=0.3)
    fig.canvas.manager.set_window_title("hepscale") 

    allowed_range = np.linspace(low_limit, high_limit, high_limit - low_limit + 1)
    slider_low1 = Slider( ax = plt.axes([0.1, 0.15, 0.35, 0.02]), label = "min: $x$", valmin = 0.0, valmax = 10.0, valinit = 1.0)
    slider_low2 = Slider( ax = plt.axes([0.1, 0.07, 0.35, 0.02]), label = "$\\times 10^{y}$", valmin = low_limit, valmax = high_limit, valinit = low_limit, valstep=allowed_range)
    slider_high1 = Slider( ax = plt.axes([0.55, 0.15, 0.35, 0.02]), label = "max: $x$", valmin = 0.0, valmax = 10.0, valinit = 1)
    slider_high2 = Slider( ax = plt.axes([0.55, 0.07, 0.35, 0.02]), label = "$\\times 10^{y}$", valmin = low_limit, valmax = high_limit, valinit = high_limit, valstep=allowed_range)

    def draw(low_bound, high_bound):
        ax.set_title(plottitle)
        limit = log(high_bound / low_bound) / 4
        adjust_points(xpoints, ypoints, low_bound, high_bound, limit)
        ax.vlines(xlines, 0, ylines, color=linecolors)
        ax.vlines(xpoints, 0, ypoints, color=colors)
        ax.plot([low_bound, high_bound], [0, 0], "", color="k", markerfacecolor="w")
        ax.plot(xpoints, np.zeros_like(xpoints), "-o", color="k", markerfacecolor="w")

        for d, l, r in zip(xpoints, ypoints, names):
            if l < 0.5:
                continue
            ax.annotate(r, xy=(d, l),
                        xytext=(-3, np.sign(l)*3), textcoords="offset points",
                        horizontalalignment="right",
                        verticalalignment="bottom" if l > 0 else "top")

        for d, l, r in zip(xlines, ylines, linenames):
            ax.annotate(r, xy=(d, l),
                        xytext=(-3, np.sign(l)*3), textcoords="offset points",
                        horizontalalignment="right",
                        verticalalignment="bottom" if l > 0 else "top")


        ax.set_xscale("log")
        ax.yaxis.set_visible(False)
        ax.set_xlim(low_bound, high_bound)
        ax.spines[["left","right","top"]].set_visible(False)

    def update(val):
        ax.clear()
        draw(10**slider_low2.val * slider_low1.val, 10**slider_high2.val * slider_high1.val)
        fig.canvas.draw_idle()

    draw(10**slider_low2.val * slider_low1.val, 10**slider_high2.val * slider_high1.val)

    slider_low1.on_changed(update)
    slider_low2.on_changed(update)
    slider_high1.on_changed(update)
    slider_high2.on_changed(update)

    plt.show()

if __name__ == "__main__":
    plotscale()
