import pandas as pd

from nicegui import ui


def plot(datums):
    chart = ui.chart({
        'chart': {
            'type': 'spline',
        },
        'legend': {
            'enabled': True,
            'layout': 'vertical',
            'align': 'right',
            'verticalAlign': 'middle',
        },
        'navigator': {
            'enabled': True
        },
        'scrollbar': {
            'enabled': False
        },
        'series': datums
    }, type='stockChart', extras=['stock'])


def toy_example():
    data1 = {'name': 'alice', 'data': [31, 148, 33, 68, 75, 43]}
    data2 = {'name': 'bob', 'data': [3, 28, 7, 5, 8, 3]}
    data3 = {'name': 'john', 'data': [1, 4, 0, 8, 9, 0]}
    plot([data1, data2, data3])


def ticker_and_close(ticker, df):
    """Return a dictionary suitable for plotting.

    Looks through dataframe and returns a ticker and it's close data in a format like so:
    {'name': 'stock_symbol', 'data': [31, 148, 33, 68, 75, 43]}
    """

    _ = df[df['Ticker'] == ticker]
    data = {'name': ticker, 'data': _['Close'].tolist()}
    return data


def example_2():
    """Plot a single ticker in the CSV file."""

    source = pd.read_csv('ticker-data.csv')
    source['Date'] = pd.to_datetime(source['Date'])
    all_tickers = source.Ticker.unique()

    data = ticker_and_close('PTON', source)
    plot([data])

def example_3():
    """Plot all 3 tickers in CSV file."""

    source = pd.read_csv('ticker-data.csv')
    source['Date'] = pd.to_datetime(source['Date'])
    all_tickers = source.Ticker.unique()

    datums = [ticker_and_close(x, source) for x in "PTON TDOC ZM".split()]
    plot(datums)

# toy_example()
# example_2()
# example_3()

ui.run()
