from epyk_studio.core.Page import Report
from epyk.core.css.themes import ThemeBlue
from epyk.tests import data_urls
from epyk.core.js import std
from epyk.core.data import events


page = Report()
page.theme = ThemeBlue.BlueGrey()

data = page.py.requests.csv(data_urls.COUNTRY_WISE_COVID)

title = page.ui.title("Country wise COVID")
button_all = page.ui.button("All")
button_all.style.css.margin_top = 5

button_clear = page.ui.button("Clear")
button_clear.style.css.margin_top = 5
button_clear.style.css.margin_left = 5

cols_keys = page.ui.panels.filters(html_code="data_filters", options={"max_height": 90})
cols_keys.style.css.min_height = 20

items = page.ui.inputs.autocomplete(placeholder="select a country", options={"select": True})
items.enter([cols_keys.dom.add(items.dom.content, category='Country/Region'), items.dom.empty()])

button = page.ui.button("Show")
button.style.css.margin_top = 5

items.options.on_select([
  cols_keys.dom.add(events.value, category='Country/Region'),
  button.dom.events.trigger("click")
])

bar = page.ui.charts.chartJs.bar([], ['Confirmed', 'Deaths', 'Recovered'], 'Country/Region')
bar.options.scales.y_axis().ticks.toNumber()

ref = page.ui.texts.references.website(author="rsharankumar", name="Learn Data Science in 100Days", site="github",
                                       url="https://github.com/rsharankumar/Learn_Data_Science_in_100Days")

box = page.studio.containers.box()
box.extend([title, items, page.ui.div([button_all, button_clear]), cols_keys, button, bar, ref])
box.style.standard()

grp = page.data.js.record(std.var("covidData", global_scope=True)).filterGroup("aggData")

button.click([
  page.js.console.log(cols_keys.dom.content),
  bar.build(grp.match(cols_keys.dom.content).group().sumBy(['Confirmed', 'Deaths', 'Recovered'], ['Country/Region']))
])

countries = set()
for rec in data:
  countries.add(rec['Country/Region'])

button_all.click([
  cols_keys.dom.clear(), cols_keys.dom.add(list(countries), category='Country/Region', no_duplicate=False)])
button_clear.click([cols_keys.dom.clear()])

page.body.onReady([std.var("covidData", data, global_scope=True), items.js.source(list(countries))])