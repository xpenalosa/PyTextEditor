from kivy.app import App
from kivy.uix.widget import Widget

from subprocess import Popen
import sys

from editor import utils


class EditorWidget(Widget):

    def __init__(self, dir_path):
        super(EditorWidget, self).__init__()
        self.running_process = None
        self.tabbed_panel = self.ids['tabbed_panel']
        self.ids['os_view'].path = dir_path

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
        self.running_process = Popen(["python", out_file])
        while self.running_process.poll() is None:
            self.running_process.wait(0.5)

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
