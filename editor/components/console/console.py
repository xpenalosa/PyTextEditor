from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget


class Console(Widget):

    controller = ObjectProperty()

    def __init__(self):
        super(Console, self).__init__()

