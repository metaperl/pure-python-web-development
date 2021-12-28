import hvplot.pandas
from bokeh.sampledata.autompg import autompg
import param
import panel as pn

def autompg_plot(x='mpg', y='hp', color='#058805'):
    return autompg.hvplot.scatter(x, y, c=color, padding=0.1)


columns = list(autompg.columns[:-2])


class MPGExplorer(param.Parameterized):
    x = param.Selector(objects=columns)
    y = param.Selector(default='hp', objects=columns)
    color = param.Color(default='#0f0f0f')

    @param.depends('x', 'y', 'color')  # optional in this case
    def plot(self):
        return autompg_plot(self.x, self.y, self.color)


explorer = MPGExplorer()

pn.Row(explorer.param, explorer.plot)

