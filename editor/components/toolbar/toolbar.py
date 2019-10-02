from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget


class Toolbar(Widget):

    controller = ObjectProperty()

    def __init__(self):
        super(Toolbar, self).__init__()
