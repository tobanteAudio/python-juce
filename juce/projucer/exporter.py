"""Holds the JucerFile class"""

# pylint: disable=too-many-public-methods,no-self-use

from xml.etree import ElementTree

# from juce.util import get_attribute_from_tag
from juce.projucer.xml_structure import (XML_TAG_BUILD_FOLDER,
                                         XML_TAG_CONFIGURATIONS,
                                         XML_TAG_MODULEPATHS)


# def exporter_tag_to_string(tag_name):
#     """Converts jucer xml tag to readable string
#     """
#     # Windows
#     if tag_name == 'VS2013':
#         return 'Windows (Visual Studio 2013)'
#     if tag_name == 'VS2015':
#         return 'Windows (Visual Studio 2015)'
#     if tag_name == 'VS2017':
#         return 'Windows (Visual Studio 2017)'
#     if tag_name == 'VS2019':
#         return 'Windows (Visual Studio 2019)'

#     # macOS
#     if tag_name == 'XCODE_MAC':
#         return 'macOS (XCode)'

#     # Linux
#     if tag_name == 'LINUX_MAKE':
#         return 'Linux (Makefile)'

#     return 'unkown'


class Exporter():
    """Represents a Projucer exporter"""

    def __init__(self, root):
        """Sets the root xml element"""
        assert isinstance(root, ElementTree.Element)
        self._root = root

    # ROOT
    @property
    def root(self):
        """Root xml element"""
        return self._root

    @root.setter
    def root(self, root):
        assert isinstance(root, ElementTree.Element)
        self._root = root

    # NAME
    @property
    def name(self):
        """Exporter Name"""
        return str(self._root.tag)

    # BUILD FOLDER
    @property
    def build_folder(self):
        """Target build folder"""
        return self._root.attrib[XML_TAG_BUILD_FOLDER]

    @build_folder.setter
    def build_folder(self, folder):
        assert isinstance(folder, str)
        self._root.set(XML_TAG_BUILD_FOLDER, folder)

    # CONFIGURATIONS
    @property
    def configurations(self):
        """Configurations"""
        config_list = []
        for configs in self.root.iter(XML_TAG_CONFIGURATIONS):
            for config in configs:
                config_list.append(config)
        return config_list

    # MODULE PATHS
    @property
    def module_paths(self):
        """Module Paths"""
        module_list = []
        for modules in self.root.iter(XML_TAG_MODULEPATHS):
            for module in modules:
                module_list.append(module)
        return module_list
