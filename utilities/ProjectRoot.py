from pathlib import Path

"""This function returns the project root path"""


def get_project_root():
    return str(Path (__file__).parent.parent)

