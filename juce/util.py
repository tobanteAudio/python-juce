""" Utility functiions & constants"""
import os


XML_HEADER = r'<?xml version="1.0" encoding="UTF-8"?>'


def get_attribute_from_tag(tag, attribute):
    """Returns a xml attribute from a given tag"""
    element = None
    try:
        element = tag.attrib[attribute]
    except KeyError:
        pass
        # print("Error: attribute {} was not defined in this tag.".format(e))
    return element


def get_list_of_path_dirs():
    """Returns a list of paths equal to the $PATH variable"""
    path_string = os.environ.get('PATH')
    path_list = path_string.split(';')
    return path_list


def print_subprocess(process):
    """Prints stdout & stderr
    """
    stdout, stderr = process.communicate()

    if stdout:
        print(stdout.decode('utf-8'))

    if stderr:
        print(stderr.decode('utf-8'))
