from kivy.app import App
from kivy.uix.widget import Widget
from subprocess import Popen
import sys


class EditorWidget(Widget):

    def __init__(self):
        super(EditorWidget, self).__init__()
        self.running_process = None

    def __del__(self):
        if self.running_process:
            self.running_process.kill()

    @staticmethod
    def save(code_input):
        # TODO: Add output file selection
        out_file = 'outfile.py'
        with open(out_file, 'w') as f:
            f.write(code_input.text)
        return out_file

    @staticmethod
    def open(code_input):
        # TODO: Add file selection
        with open('outfile.py', 'r') as f:
            code_input.text = f.read()

    def run_code(self, code_input):
        out_file = EditorWidget.save(code_input)
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
