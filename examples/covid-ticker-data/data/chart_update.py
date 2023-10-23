from nicegui import ui

# initial data
data1 = {'name': 'alice', 'data': [31, 148, 33, 68, 75, 43]}

# data to update chart options with to exemplify updating a chart.
data2 = {'name': 'bob', 'data': [3, 28, 7, 5, 8, 3]}
data3 = {'name': 'john', 'data': [1, 4, 0, 8, 9, 0]}

chart = None
chart_options = {
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
    'series': [data1]
}


def plot():
    global chart, chart_options
    chart = ui.chart(chart_options, type='stockChart', extras=['stock'])


def update_chart():
    global chart

    chart.options['series'] = [data2, data3]
    chart.update()


plot()
ui.button('Update', on_click=update_chart)
ui.run(reload=False)
