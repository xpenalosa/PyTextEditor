from kivy.input import MotionEvent
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.bubble import Bubble
from kivy.uix.filechooser import FileChooserListView

from editor.components.sidebar.sidebar_popup import SidebarPopup

Builder.load_string("""
#:kivy 1.11.1

<SidebarFileChooser>:
    size: root.size
    pos: root.pos
""")


class SidebarFileChooser(FileChooserListView):
    sidebar = ObjectProperty()

    def __init__(self, **kwargs):
        super(SidebarFileChooser, self).__init__(**kwargs)

    def on_submit(self, selected, touch=None):
        self.sidebar.open_file(selected[0])
        super(SidebarFileChooser, self).on_submit(selected, touch)
        return True

    def on_touch_down(self, touch: MotionEvent):
        super(SidebarFileChooser, self).on_touch_down(touch)
        if "button" in touch.profile and touch.button == "right":
            self.display_file_popup(touch.pos)
            return True

    def display_file_popup(self, touch_pos):
        popup = SidebarPopup()
        popup.add_option(SidebarPopup.create_option("New", self.new_file))
        popup.add_option(SidebarPopup.create_option("New 2", self.new_file))
        popup.pos = (touch_pos[0], touch_pos[1] - popup.size[1])
        self.add_widget(popup)

    def new_file(self, *args, **kwargs):
        # TODO
        print("Creating a new file")
