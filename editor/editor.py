from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.codeinput import CodeInput
from kivy.uix.tabbedpanel import TabbedPanelHeader

from pygments.lexers import get_lexer_for_filename as glff
from pygments.util import ClassNotFound

from subprocess import Popen
import sys
import os


class EditorWidget(Widget):

    def __init__(self, dirpath):
        super(EditorWidget, self).__init__()
        self.running_process = None
        self.tabbed_panel = self.ids['tabbed_panel']
        self.ids['os_view'].path = dirpath

    def __del__(self):
        if self.running_process:
            self.running_process.kill()

    def save(self):
        out_file = self.tabbed_panel.current_tab.full_path
        with open(out_file, 'w') as f:
            f.write(self.tabbed_panel.current_tab.content.text)

    def open(self, file_selector):
        # TODO: If file is already open, switch to it
        if file_selector.selection:
            # Create CodeInput object from file
            input_file = file_selector.selection[0]
            file_name = input_file.split(os.sep)[-1]
            code_input = CodeInput()
            with open(input_file, 'r') as f:
                code_input.text = f.read()
                try:
                    new_lexer = glff(file_name)
                except ClassNotFound:
                    print(f"No lexer for {file_name}!")
                else:
                    code_input.lexer = new_lexer

            # Add new CodeInput object to the tabbed pane
            th = TabbedPanelHeader(text=file_name)
            th.content = code_input
            th.full_path = input_file
            self.tabbed_panel.add_widget(th)
            self.tabbed_panel.switch_to(th, do_scroll=True)

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

    def __init__(self, dirpath):
        super(EditorApp, self).__init__()
        self.dirpath = dirpath

    def build(self):
        self.title = "PyTextEditor - github.com/xpenalosa/PyTextEditor"
        return EditorWidget(self.dirpath)
