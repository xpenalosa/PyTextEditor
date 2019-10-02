from editor import Editor
import os

if __name__ == "__main__":
    # Start editor on current folder
    dir_path = os.getcwd()
    e = Editor(dir_path)
    e.run()
