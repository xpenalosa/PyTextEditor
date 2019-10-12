from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

Builder.load_string("""
#:kivy 1.11.1

<Toolbar>:
    StackLayout:
        pos: root.pos
        width: root.width
        height: root.height
        ToolbarButton:
            text: 'New'
            on_release: root.controller.new()
        ToolbarButton:
            text: 'Save'
            on_release: root.controller.save()
        ToolbarButton:
            text: 'Run'
            on_release: root.controller.run_code()
        ToolbarButton:
            text: 'Quit'
            on_release: root.controller.quit()

<ToolbarButton@Button>:
    size_hint_x: 0.1
""")


class Toolbar(Widget):

    controller = ObjectProperty()

    def __init__(self, **kwargs):
        super(Toolbar, self).__init__(**kwargs)
