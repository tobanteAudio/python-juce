""" Utility functiions & constants"""

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


# def print_subprocess(process):
#     """Prints stdout & stderr
#     """
#     stdout, stderr = process.communicate()

#     if stdout:
#         print(stdout.decode('utf-8'))

#     if stderr:
#         print(stderr.decode('utf-8'))
