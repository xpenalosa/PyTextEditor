from editor import Editor
import os

if __name__ == "__main__":
    # Start editor on current folder
    dirpath = os.getcwd()
    e = Editor(dirpath)
    e.run()
