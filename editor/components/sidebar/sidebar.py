from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget


class Sidebar(Widget):

    controller = ObjectProperty()

    def __init__(self):
        super(Sidebar, self).__init__()

