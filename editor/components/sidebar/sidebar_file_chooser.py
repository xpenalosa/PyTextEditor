from kivy.properties import ObjectProperty
from kivy.uix.filechooser import FileChooserListView


class SidebarFileChooser(FileChooserListView):

    sidebar = ObjectProperty()

    def __init__(self, **kwargs):
        super(SidebarFileChooser, self).__init__(**kwargs)

    def on_submit(self, selected, touch=None):
        self.sidebar.open_file(selected[0])
        super(SidebarFileChooser, self).on_submit(selected, touch)
        return True

    def on_touch_down(self, touch):
        super(SidebarFileChooser, self).on_touch_down(touch)
        if "button" in touch.profile and touch.button == "right":
            self.display_file_popup()
            return True

    def display_file_popup(self):
        # TODO
        pass
