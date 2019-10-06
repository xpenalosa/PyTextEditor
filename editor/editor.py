from kivy.app import App
from kivy.uix.widget import Widget

from subprocess import Popen, PIPE
import sys

from editor import utils
from editor.components.toolbar import toolbar
from editor.components.sidebar import sidebar
from editor.components.console import console


class EditorWidget(Widget):

    def __init__(self, dir_path):
        super(EditorWidget, self).__init__()
        self.running_process = None
        self.tabbed_panel = self.ids['tabbed_panel']
        self.ids['sidebar'].ids['os_view'].path = dir_path

    def __del__(self):
        if self.running_process:
            self.running_process.kill()

    def save(self):
        utils.store_code_tab(self.tabbed_panel.current_tab)

    def open(self, file_selector):
        if file_selector.selection:
            input_file = file_selector.selection[0]
            code_tab = utils.get_or_create_tab(self.tabbed_panel, input_file)
            self.tabbed_panel.switch_to(code_tab, do_scroll=True)

    def run_code(self):
        out_file = self.tabbed_panel.current_tab.full_path
        console_log = self.ids['console_panel'].ids['console_log']
        # Clear previous execution output
        self.clear_console_log()
        # TODO: Avoid blocking. Clock?
        self.running_process = Popen(["python", out_file],
                                     stdout=PIPE, stderr=PIPE)
        for line in iter(self.running_process.stdout.readline, b''):
            console_log.text += f"OUT - {line.decode('utf-8')}"

        for line in iter(self.running_process.stderr.readline, b''):
            # TODO: Add coloring to errors and output them when they occur
            console_log.text += f"ERR - {line.decode('utf-8')}"

    def clear_console_log(self):
        self.ids['console_panel'].ids['console_log'].clear_output()

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
