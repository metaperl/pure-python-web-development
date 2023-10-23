from lona_picocss.html import InlineButton, Label, Span, Icon, HTML, Div, H1
from lona_picocss import install_picocss

from lona import View, App

from dataclasses import dataclass

app = App(__file__)

install_picocss(app, debug=True)


@dataclass
class Counter:
    value: int = 0

    def decrease(self):
        self.value -= 1
        print(f"{self.value=}")

    def increase(self):
        self.value += 1
        print(f"{self.value=}")



class CounterView(Div):
    def __init__(self, counter):
        super().__init__()

        self.counter = counter

        self.nodes = [
            Label(
                InlineButton(Icon('minus-circle'), handle_click=self.decrease),
                ' ',
                Span(),
                ' ',
                InlineButton(Icon('plus-circle'), handle_click=self.increase),
            ),
        ]

        self.set_value()

    def set_value(self):
        with self.lock:
            self.query_selector('span').set_text(f'{self.counter.value:03}  ... !')

    def decrease(self, input_event):
        with self.lock:
            self.counter.decrease()
            self.set_value()

    def increase(self, input_event):
        with self.lock:
            self.counter.increase()
            self.set_value()


@app.route('/')
class Index(View):

    def handle_request(self, request):
        c10 = Counter(value=14)
        c20 = Counter(value=22)
        c30 = Counter(value=34)

        return HTML(
            H1('Counter'),
            CounterView(c10),
            CounterView(c20),
            CounterView(c30),
        )


app.run()
