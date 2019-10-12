from kivy.input import MotionEvent
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.filechooser import FileChooserListView

from editor.components.dialogs.context_popup import ContextPopup

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
        popup = ContextPopup(
            size_hint=(None, None),
            pos=touch_pos
        )
        popup.set_options(
            ContextPopup.create_option("New", self.new_file),
            ContextPopup.create_option("New 2", self.new_file)
        )
        popup.open()

    def new_file(self, *args, **kwargs):
        print("Creating a new file")
