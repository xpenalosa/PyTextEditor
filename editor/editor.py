from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window


class EditorWidget(Widget):

    def __init__(self):
        super(EditorWidget, self).__init__()


class EditorApp(App):

    def __init__(self):
        super(EditorApp, self).__init__()
        # Window.borderless = True

    def build(self):
        self.title = "PyTextEditor - github.com/fndh/PyTextEditor"
        return EditorWidget()
