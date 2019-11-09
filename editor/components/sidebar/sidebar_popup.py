from kivy.uix.bubble import Bubble, BubbleButton


class SidebarPopup(Bubble):

    @staticmethod
    def create_option(text="", callback=None):
        option = BubbleButton(
            text=text,
            on_press=callback)
        return option

    def __init__(self, **kwargs):
        super(SidebarPopup, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.arrow_pos = "left_top"
        # FIXME buttons not adjusting to height
        self.row_default_height = 10
        # self.row_force_default = True

    def add_option(self, option):
        option.bind(on_press=self.tmp)
        self.add_widget(option)

    def tmp(self, *args):
        print("callback")
