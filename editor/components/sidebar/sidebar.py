from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

from editor.components.codetab import CodeTab
from editor.components.sidebar import sidebar_file_chooser

Builder.load_string("""
#:kivy 1.11.1

<Sidebar>:
    id: sidebar
    BoxLayout:
        size: root.size
        pos: root.pos
        SidebarFileChooser:
            id: os_view
            sidebar: sidebar
            size_hint_x: 0.95
""")


class Sidebar(Widget):
    controller = ObjectProperty()

    def __init__(self, **kwargs):
        super(Sidebar, self).__init__(**kwargs)

    def open_file(self, file_path):
        if file_path:
            code_tab = CodeTab.get_or_create(file_path)
            self.controller.append_tab(code_tab)

    def get_selected_items(self):
        return self.ids['os_view'].selection
