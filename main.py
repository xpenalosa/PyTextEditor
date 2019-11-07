import os

from kivy.config import Config

from editor.launcher import EditorApp

if __name__ == "__main__":
    Config.read("editor/editor.ini")
    Config.write()
    # TODO: Use configuration file
    # Start editor on current folder
    dir_path = os.getcwd()
    e = EditorApp(dir_path)
    e.run()
