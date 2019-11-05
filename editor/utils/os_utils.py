from pathlib import Path


def check_file_exists(file_path):
    if file_path is None:
        return False
    return Path(file_path).exists()


def create_file(file_path):
    if file_path and not check_file_exists(file_path):
        Path(file_path).touch()
