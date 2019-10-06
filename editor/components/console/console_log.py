from kivy.properties import ObjectProperty
from kivy.uix.codeinput import CodeInput


class ConsoleLog(CodeInput):

    controller = ObjectProperty()

    def __init__(self, **kwargs):
        super(ConsoleLog, self).__init__(**kwargs)

    def clear_output(self):
        self.text = ""
