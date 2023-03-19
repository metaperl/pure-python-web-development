import param
import panel as pn


class BaseClass(param.Parameterized):
    enter_some_text = param.String(default="str", doc="A string")

    @param.depends('enter_some_text')
    def view(self):
        result = self.enter_some_text.upper()
        return pn.pane.Str(result)


display = BaseClass(name='simple uppercase')
pn.Row(display.param, display.view)

