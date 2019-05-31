import os


def get_list_of_path_dirs():
    """Returns a list of paths equal to the $PATH variable"""
    path_string = os.environ.get('PATH')
    path_list = path_string.split(';')
    return path_list
