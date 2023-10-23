import pandas as pd

from nicegui import ui

from loguru import logger

def plot(datums):
    ui.chart({
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


def ticker_and_close(ticker, df):
    """Return a dictionary suitable for plotting.

    Looks through dataframe and returns a ticker and it's close data in a format like so:
    {'name': 'stock_symbol', 'data': [31, 148, 33, 68, 75, 43]}
    """

    _ = df[df['Ticker'] == ticker]
    data = {'name': ticker, 'data': _['Close'].tolist()}
    return data


def plot_selected(selected):
    source = pd.read_csv('ticker-data.csv')
    source['Date'] = pd.to_datetime(source['Date'])
    datums = [ticker_and_close(x, source) for x in selected]
    plot(datums)


def example_4():
    source = pd.read_csv('ticker-data.csv')
    source['Date'] = pd.to_datetime(source['Date'])
    all_tickers = source.Ticker.unique()
    all_tickers_list = all_tickers.tolist()
    logger.debug(f"{all_tickers_list=}")

    ui.select(all_tickers_list, multiple=True, value=all_tickers_list,
              label='with chips', on_change=lambda e: plot_selected(e.value)
              ).classes('w-64').props('use-chips')

    # plot_selected(all_tickers_list)

example_4()

ui.run()