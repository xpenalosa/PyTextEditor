from pathlib import Path

from editor.components.dialogs.file_chooser_dialog import FileChooserDialog


def check_file_exists(file_path):
    if file_path is None:
        return False
    return Path(file_path).exists()


def create_file(file_path):
    if file_path and not check_file_exists(file_path):
        Path(file_path).touch()


def create_save_file_dialog():
    dialog = FileChooserDialog(size_hint=(0.75, 0.75))
    dialog.set_callback(create_file)
    dialog.open()
