import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvas
import numpy as np
import panel as pn
import load_data

def my_mpl_plot(avg, highlight):
    fig, ax = plt.subplots()
    avg.plot(ax=ax)
    if len(highlight): highlight.plot(style='o', ax=ax)
    return fig


def find_outliers(data=None, variable='Temperature', window=30, sigma=10, view_fn=my_mpl_plot):
    if data is None:
        data = load_data.data
    avg = data[variable].rolling(window=window).mean()
    residual = data[variable] - avg
    std = residual.rolling(window=window).std()
    outliers = (np.abs(residual) > std * sigma)
    return view_fn(avg, avg[outliers])
