XML_HEADER = r'<?xml version="1.0" encoding="UTF-8"?>'


def get_attribute_from_tag(tag, attribute):
    """Returns a xml attribute from a given tag"""
    element = None
    try:
        element = tag.attrib[attribute]
    except KeyError as e:
        print("Error: attribute {} was not defined in this tag.".format(e))

    return element
