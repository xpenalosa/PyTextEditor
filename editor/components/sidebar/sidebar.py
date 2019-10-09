from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

from editor import utils
from editor.components.sidebar import sidebar_file_chooser


class Sidebar(Widget):

    controller = ObjectProperty()

    def __init__(self, **kwargs):
        super(Sidebar, self).__init__(**kwargs)

    def open_file(self, file_path):
        if file_path:
            code_tab = utils.get_or_create_tab(file_path)
            self.controller.append_tab(code_tab)

    def get_selected_items(self):
        return self.ids['os_view'].selection


