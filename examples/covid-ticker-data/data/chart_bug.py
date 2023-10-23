from nicegui import ui

# initial data
data1 = {'name': 'alice', 'data': [31, 148, 33, 68, 75, 43]}
data2 = {'name': 'bob', 'data': [3, 28, 7, 5, 8, 3]}
data3 = {'name': 'john', 'data': [11, 42, 10, 18, 9, 0]}

all_data = dict(alice=data1, bob=data2, john=data3)

print(f"keys = {list(all_data.keys())}")

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
    'series': [data1, data2, data3]
}


def plot():
    global chart, chart_options
    chart = ui.chart(chart_options, type='stockChart', extras=['stock'])


def update_chart(selections):
    global chart

    datums = [all_data[selection] for selection in selections]


    chart.options['series'] = datums
    chart.update()



plot()
ui.select(list(all_data.keys()), multiple=True, value=list(all_data.keys()),
          label='with chips', on_change=lambda e: update_chart(e.value)
          ).classes('w-64').props('use-chips')

ui.run(reload=False)
