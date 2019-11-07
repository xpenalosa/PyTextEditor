import sys
from subprocess import Popen, PIPE

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

from editor.components import codetab
from editor.components.toolbar import toolbar
from editor.components.sidebar import sidebar
from editor.components.console import console

Builder.load_string("""
#:kivy 1.11.1

<EditorWidget>:
    id: editor_widget
    BoxLayout:
        width: root.width
        height: root.height
        orientation: 'vertical'
        Toolbar:
            size_hint_y: None
            height: 30
            controller: editor_widget
        BoxLayout:
            size_hint_y: .925
            Sidebar:
                id: sidebar
                size_hint_x: 0.275
                controller: editor_widget
            BoxLayout:
                size_hint_x: 0.675
                orientation: 'vertical'
                TabbedPanel:
                    id: tabbed_panel
                    size_hint_y: 0.775
                    do_default_tab: False
                Console:
                    id: console_panel
                    size_hint_y: 0.175
""")


class EditorWidget(Widget):

    def __init__(self, dir_path):
        super(EditorWidget, self).__init__()
        self.running_process = None
        self.tabbed_panel = self.ids['tabbed_panel']
        self.ids['sidebar'].ids['os_view'].path = dir_path

    def __del__(self):
        if self.running_process:
            self.running_process.kill()

    def new(self):
        self.append_tab(codetab.CodeTab())

    def save(self):
        self.tabbed_panel.current_tab.save_contents()

    def append_tab(self, code_tab):
        if code_tab not in self.tabbed_panel.tab_list:
            self.tabbed_panel.add_widget(code_tab)
        self.tabbed_panel.switch_to(code_tab, do_scroll=True)

    def run_code(self):
        self.tabbed_panel.current_tab.save_contents()
        out_file = self.tabbed_panel.current_tab.full_path
        console_log = self.ids['console_panel'].ids['console_log']
        # Clear previous execution output
        console_log.clear_output()
        # TODO: Avoid blocking. Clock?
        self.running_process = Popen(["python", out_file],
                                     stdout=PIPE, stderr=PIPE)
        for line in iter(self.running_process.stdout.readline, b''):
            console_log.text += line.decode('utf-8')

        for line in iter(self.running_process.stderr.readline, b''):
            # Add error tag to each error line. Limited by implementation
            console_log.text += f"[ERR]{line.decode('utf-8')}[/ERR]"

    def quit(self):
        if self.running_process:
            self.running_process.kill()
        sys.exit(0)


class EditorApp(App):

    def __init__(self, dir_path):
        super(EditorApp, self).__init__()
        self.dir_path = dir_path

    def build(self):
        self.title = "PyTextEditor - github.com/xpenalosa/PyTextEditor"
        return EditorWidget(self.dir_path)

    def build_config(self, config):
        config.setdefaults('input', {
            'mouse': 'mouse,disable_multitouch'
        })
