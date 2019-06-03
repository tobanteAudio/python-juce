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


def bool_to_integer_string(boolean):
    """Returns '0' for False & '1' for True

    :param `boolean`: Value to convert
    :returns: Conversion result
    :rtype: str

    """
    return "{}".format(int(boolean))
