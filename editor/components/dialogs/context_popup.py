from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.modalview import ModalView

Builder.load_string("""
#:kivy 1.11.1

<ContextPopup>:
    size: root.size
    pos: root.pos""")


class ContextPopup(ModalView):

    def __init__(self, **kwargs):
        super(ContextPopup, self).__init__(**kwargs)
        self.grid_layout = GridLayout(size=self.size, pos=self.pos, cols=1,
                                      row_default_height=5)
        self.add_widget(self.grid_layout)

    def set_options(self, *options):
        for i in range(len(options)):
            opt = options[i]
            opt.bind(on_press=self.dismiss)
            self.grid_layout.add_widget(opt)

    @staticmethod
    def create_option(text="", callback=None):
        option = Button(
            text=text,
            on_press=callback)
        return option
