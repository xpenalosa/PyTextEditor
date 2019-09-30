from kivy.app import App
from kivy.uix.widget import Widget
from pygments.lexers import get_lexer_for_filename
from subprocess import Popen
import sys


class EditorWidget(Widget):

    def __init__(self):
        super(EditorWidget, self).__init__()
        self.running_process = None
        self.open_files = []
        self.current_file_id = -1

    def __del__(self):
        if self.running_process:
            self.running_process.kill()

    def save(self, file_selector, code_input):
        out_file = self.open_files[self.current_file_id]
        with open(out_file, 'w') as f:
            f.write(code_input.text)
        return out_file

    def open(self, file_selector, code_input):
        if file_selector.selection:
            input_file = file_selector.selection[0]
            self.open_files.append(input_file)
            self.current_file_id = len(self.open_files) - 1
            with open(input_file, 'r') as f:
                code_input.text = f.read()
                code_input.lexer = get_lexer_for_filename(input_file)

    def run_code(self, file_selector, code_input):
        out_file = self.save(file_selector, code_input)
        self.running_process = Popen(["python", out_file])
        while self.running_process.poll() is None:
            self.running_process.wait(0.5)

    def quit(self):
        if self.running_process:
            self.running_process.kill()
        sys.exit(0)


class EditorApp(App):

    def __init__(self):
        super(EditorApp, self).__init__()

    def build(self):
        self.title = "PyTextEditor - github.com/fndh/PyTextEditor"
        return EditorWidget()
