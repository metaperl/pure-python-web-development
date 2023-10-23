import panel as pn
import hvplot.pandas
import pandas as pd
import numpy as np

pn.extension(design='material')

csv_file = ("https://raw.githubusercontent.com/holoviz/panel/main/examples/assets/occupancy.csv")
data = pd.read_csv(csv_file, parse_dates=["date"], index_col="date")

print(data.tail())

def transform_data(variable, window, sigma):
    ''' Calculates the rolling average and the outliers '''
    avg = data[variable].rolling(window=window).mean()
    residual = data[variable] - avg
    std = residual.rolling(window=window).std()
    outliers = np.abs(residual) > std * sigma
    return avg, avg[outliers]

def create_plot(variable="Temperature", window=30, sigma=10):
    ''' Plots the rolling average and the outliers '''
    avg, highlight = transform_data(variable, window, sigma)
    return avg.hvplot(height=300, width=400, legend=False) * highlight.hvplot.scatter(
        color="orange", padding=0.1, legend=False
    ).servable()

plot = create_plot(variable='Temperature', window=20, sigma=10)

print(plot)
plot
