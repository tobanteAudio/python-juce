"""Holds the JucerFile class"""

# pylint: disable=too-many-public-methods,no-self-use

from xml.etree import ElementTree

# from juce.util import get_attribute_from_tag
from juce.projucer.xml_structure import (ATTRIBUTE_BUILD_FOLDER,
                                         TAG_CONFIGURATIONS,
                                         TAG_MODULEPATHS)


class Exporter():
    """Represents a Projucer exporter

    :param root: Root element for exporter
    :type root: xml.etree.ElementTree.Element
    """

    def __init__(self, root):
        assert isinstance(root, ElementTree.Element)
        self._root = root

    # ROOT
    @property
    def root(self):
        """Root xml element"""
        return self._root

    # NAME
    @property
    def name(self):
        """Exporter Name"""
        return str(self._root.tag)

    # BUILD FOLDER
    @property
    def build_folder(self):
        """Target build folder"""
        return self._root.attrib[ATTRIBUTE_BUILD_FOLDER]

    @build_folder.setter
    def build_folder(self, folder):
        assert isinstance(folder, str)
        self._root.set(ATTRIBUTE_BUILD_FOLDER, folder)

    # CONFIGURATIONS
    @property
    def configurations(self):
        """Configurations"""
        config_list = []
        for configs in self.root.iter(TAG_CONFIGURATIONS):
            for config in configs:
                config_list.append(config)
        return config_list

    # MODULE PATHS
    @property
    def module_paths(self):
        """Module Paths"""
        module_list = []
        for modules in self.root.iter(TAG_MODULEPATHS):
            for module in modules:
                module_list.append(module)
        return module_list
