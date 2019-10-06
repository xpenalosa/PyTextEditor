from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

from editor.components.console import console_log


class Console(Widget):

    controller = ObjectProperty()

    def __init__(self, **kwargs):
        super(Console, self).__init__(**kwargs)

