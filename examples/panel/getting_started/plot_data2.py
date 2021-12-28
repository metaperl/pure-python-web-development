from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvas
import numpy as np
import panel as pn

import plot_data



pn.extension()
pn.interact(plot_data.find_outliers).servable()

