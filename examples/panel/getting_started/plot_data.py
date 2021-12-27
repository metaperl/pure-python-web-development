from matplotlib.figure import Figure
# from matplotlib.backends.backend_agg import FigureCanvas
import numpy as np

# %matplotlib inline


def mpl_plot(avg, highlight):
    fig = Figure()
    # FigureCanvas(fig) # not needed in mpl >= 3.1
    ax = fig.add_subplot()
    avg.plot(ax=ax)
    if len(highlight): highlight.plot(style='o', ax=ax)
    return fig


def find_outliers(data, variable='Temperature', window=30, sigma=10, view_fn=mpl_plot):
    avg = data[variable].rolling(window=window).mean()
    residual = data[variable] - avg
    std = residual.rolling(window=window).std()
    outliers = (np.abs(residual) > std * sigma)
    return view_fn(avg, avg[outliers])


import load_data
f = find_outliers(load_data.data, variable='Temperature', window=20, sigma=10)
f()