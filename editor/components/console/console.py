from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

from editor.components.console import console_log

Builder.load_string("""
#:kivy 1.11.1

<Console>:
    BoxLayout:
        width: root.width
        height: root.height
        pos: root.pos
        orientation: 'vertical'
        Label:
            size_hint_y: 0.1
            text: "Console output"
            text_size: root.size
            halign: 'center'
            valign: 'center'
        ConsoleLog:
            id: console_log
            size_hint_y: 0.9""")


class Console(Widget):

    controller = ObjectProperty()

    def __init__(self, **kwargs):
        super(Console, self).__init__(**kwargs)

