import os
from xml.etree import ElementTree

from juce.xml_helpers import XML_HEADER, get_attribute_from_tag
from juce.env_helpers import get_list_of_path_dirs
from juce.validation import (valid_aax_category, valid_au_category,
                             valid_vst2_category, valid_vst3_category)


class Projucer():
    """Represents the Projucer executable"""

    def __init__(self):
        self._path = get_list_of_path_dirs()

    @property
    def path(self):
        """Returns a list of paths equal to the $PATH variable"""
        return self._path


class JucerFile():
    """Represents a jucer file containing a JUCE project"""

    """Xml tree"""
    tree = None
    """Root element in jucer file (JUCERPROJECT)"""
    root = None

    def __init__(self, path):
        """Loads the jucer file as xml"""
        self._path = path
        self.tree = ElementTree.parse(path)
        self.root = self.tree.getroot()

    # SAVE
    def save(self):
        """Saves the jucer file as xml to the current path"""
        self.save_as(self._path)

    def save_as(self, new_path):
        """Saves the jucer file as xml to the given path"""
        self.tree.write(open(new_path, 'wb'), encoding='utf-8')
        with open(new_path, 'r') as original:
            data = original.read()
        with open(new_path, 'w') as modified:
            modified.write(XML_HEADER + '\n' + data)

    # PATH
    @property
    def path(self):
        """Returns the jucer file path"""
        return self._path

    @path.setter
    def path(self, x):
        """Sets the jucer file path"""
        print("Setting path with: {}".format(x))

    # ID
    @property
    def id(self):
        """Returns the project id"""
        return get_attribute_from_tag(self.root, 'id')

    @id.setter
    def id(self, x):
        """Sets the project id"""
        print("Setting id with: {}".format(x))

    # NAME
    @property
    def name(self):
        """Returns the project name"""
        return get_attribute_from_tag(self.root, 'name')

    @name.setter
    def name(self, x):
        """Sets the project name"""
        print("Setting name with: {}".format(x))

    # PROJECT TYPE
    @property
    def project_type(self):
        """Returns the project project type"""
        return get_attribute_from_tag(self.root, 'projectType')

    @project_type.setter
    def project_type(self, x):
        """Sets the project project type"""
        print("Setting projectType with: {}".format(x))

    # JUCER VERSION
    @property
    def jucer_version(self):
        """Returns the project jucer_version"""
        return get_attribute_from_tag(self.root, 'jucerVersion')

    @jucer_version.setter
    def jucer_version(self, x):
        """Sets the project jucer_version"""
        print("Setting jucerVersion with: {}".format(x))

    # VERSION
    @property
    def version(self):
        """Returns the project version"""
        return get_attribute_from_tag(self.root, 'version')

    @version.setter
    def version(self, x):
        """Sets the project version"""
        print("Setting version with: {}".format(x))

    # COMPANY
    @property
    def company(self):
        """Returns the company name"""
        return get_attribute_from_tag(self.root, 'companyName')

    @company.setter
    def company(self, x):
        """Sets the company name"""
        print("Setting company with: {}".format(x))

    # COMPANY WEBSITE
    @property
    def company_website(self):
        """Returns the company website"""
        return get_attribute_from_tag(self.root, 'companyWebsite')

    @company_website.setter
    def company_website(self, x):
        """Sets the company website"""
        print("Setting companyWebsite with: {}".format(x))

    # COMPANY EMAIL
    @property
    def company_email(self):
        """Returns the company email"""
        return get_attribute_from_tag(self.root, 'companyEmail')

    @company_email.setter
    def company_email(self, x):
        """Sets the company email"""
        print("Setting companyEmail with: {}".format(x))

    # BUNDLE IDENTIFIER
    @property
    def bundle_identifier(self):
        """Returns the project bundle identifier"""
        return get_attribute_from_tag(self.root, 'bundleIdentifier')

    @bundle_identifier.setter
    def bundle_identifier(self, x):
        """Sets the project bundle identifier"""
        print("Setting bundleIdentifier with: {}".format(x))

    # PLUGIN NAME
    @property
    def plugin_name(self):
        """Returns the plugin name"""
        return get_attribute_from_tag(self.root, 'pluginName')

    @plugin_name.setter
    def plugin_name(self, x):
        """Sets the plugin name"""
        print("Setting pluginName with: {}".format(x))

    # PLUGIN DESCRIPTION
    @property
    def plugin_description(self):
        """Returns the plugin description"""
        return get_attribute_from_tag(self.root, 'pluginDesc')

    @plugin_description.setter
    def plugin_description(self, x):
        """Sets the plugin description"""
        print("Setting pluginDescription with: {}".format(x))

    # PLUGIN MANUFACTURER
    @property
    def plugin_manufacturer(self):
        """Returns the plugin manufacturer"""
        return get_attribute_from_tag(self.root, 'pluginManufacturer')

    @plugin_manufacturer.setter
    def plugin_manufacturer(self, x):
        """Sets the plugin manufacturer"""
        print("Setting pluginManufacturer with: {}".format(x))

    # PLUGIN MANUFACTURER CODE
    @property
    def plugin_manufacturer_code(self):
        """Returns the plugin manufacturer code"""
        return get_attribute_from_tag(self.root, 'pluginManufacturer')

    @plugin_manufacturer_code.setter
    def plugin_manufacturer_code(self, x):
        """Sets the plugin manufacturer code"""
        print("Setting pluginManufacturerCode with: {}".format(x))

    # PLUGIN CODE
    @property
    def plugin_code(self):
        """Returns the plugin code"""
        return get_attribute_from_tag(self.root, 'pluginCode')

    @plugin_code.setter
    def plugin_code(self, x):
        """Sets the plugin code"""
        print("Setting pluginCode with: {}".format(x))

    # PLUGIN AU EXPORT PROFILE
    @property
    def plugin_au_exporter_profile(self):
        """Returns the plugin AU exporter profile"""
        return get_attribute_from_tag(self.root, 'pluginAUExportPrefix')

    @plugin_au_exporter_profile.setter
    def plugin_au_exporter_profile(self, x):
        """Sets the plugin AU exporter profile"""
        print("Setting pluginAUExportPrefix with: {}".format(x))

    # AAX IDENTIFIER
    @property
    def aax_identifier(self):
        """Returns the plugin aax identifier"""
        return get_attribute_from_tag(self.root, 'aaxIdentifier')

    @aax_identifier.setter
    def aax_identifier(self, x):
        """Sets the plugin aax identifier"""
        print("Setting aaxIdentifier with: {}".format(x))

    # VST3 CATEGORY
    @property
    def vst3_category(self):
        """Returns the plugin vst3 category"""
        return get_attribute_from_tag(self.root, 'pluginVST3Category')

    @vst3_category.setter
    def vst3_category(self, category):
        """Sets the plugin vst3 category"""
        if valid_vst3_category(category):
            print("Setting pluginVST3Category with: {}".format(category))

    # BINARY DATA NAMESPACE
    @property
    def binary_data_namespace(self):
        """Returns the plugin binary data namespace"""
        return get_attribute_from_tag(self.root, 'binaryDataNamespace')

    @binary_data_namespace.setter
    def binary_data_namespace(self, x):
        """Sets the plugin binary data namespace"""
        print("Setting binaryDataNamespace with: {}".format(x))

    # C++ LANGUAGE STANDARD
    @property
    def cpp_language_standard(self):
        """Returns the C++ standard"""
        return get_attribute_from_tag(self.root, 'cppLanguageStandard')

    @cpp_language_standard.setter
    def cpp_language_standard(self, x):
        """Sets the C++ standard"""
        possible_values = ['11', '14', '17', 'latest']
        if x not in possible_values:
            print("{} is not a possible value. {}".format(x, possible_values))
            return
        print("Setting cppLanguageStandard with: {}".format(x))
        self.root.set('cppLanguageStandard', x)

    # PLUGIN FORMATS
    @property
    def plugin_formats(self):
        """Returns the plugin formats"""
        return get_attribute_from_tag(self.root, 'pluginFormats')

    @plugin_formats.setter
    def plugin_formats(self, x):
        """Sets the plugin formats"""
        print("Setting pluginFormats with: {}".format(x))

    # COMPANY COPYRIGHT
    @property
    def company_copyright(self):
        """Returns the company copyright"""
        return get_attribute_from_tag(self.root, 'companyCopyright')

    @company_copyright.setter
    def company_copyright(self, x):
        """Sets the company copyright"""
        print("Setting companyCopyright with: {}".format(x))

    # DISPLAY SPLASH SCREEN
    @property
    def display_splash_screen(self):
        """Returns the plugin splash screen setting"""
        return get_attribute_from_tag(self.root, 'displaySplashScreen')

    @display_splash_screen.setter
    def display_splash_screen(self, x):
        """Sets the plugin splash screen setting"""
        print("Setting displaySplashScreen with: {}".format(x))

    # REPORT APP USAGE
    @property
    def report_app_usage(self):
        """Returns the plugin report app usage setting"""
        return get_attribute_from_tag(self.root, 'reportAppUsage')

    @report_app_usage.setter
    def report_app_usage(self, x):
        """Sets the plugin report app usage setting"""
        print("Setting reportAppUsage with: {}".format(x))

    # COMPILER FLAG SCHEMES
    @property
    def compiler_flag_schemes(self):
        """Returns the plugin compiler flag schemes"""
        return get_attribute_from_tag(self.root, 'compilerFlagSchemes')

    @compiler_flag_schemes.setter
    def compiler_flag_schemes(self, x):
        """Sets the plugin compiler flag schemes"""
        print("Setting compilerFlagSchemes with: {}".format(x))

    # PROJECT LINE FEED
    @property
    def project_line_feed(self):
        """Returns the project line feed"""
        return get_attribute_from_tag(self.root, 'projectLineFeed')

    @project_line_feed.setter
    def project_line_feed(self, x):
        """Sets the project line feed"""
        print("Setting projectLineFeed with: {}".format(x))


# ET.SubElement(root,'TextSummary').set('Status','Completed')

# def get_project_info(root):
#     print("INFO:")
#     print("Name: {}".format(root.attrib['name']))
#     print("Company: {}".format(root.attrib['companyName']))
#     print("Copyright: {}".format(root.attrib['companyCopyright']))
#     print("Category: {}".format(root.attrib['pluginVST3Category']))
#     print("Version: {}".format(root.attrib['version']))
#     print("Jucer Version: {}".format(root.attrib['jucerVersion']))
#     print('')


# def exporter_tag_to_string(tag_name):
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


# def get_exporters(root):
#     for exporters in root.iter('EXPORTFORMATS'):
#         print("EXPORTFORMATS: {}".format(len(exporters)))
#         for exporter in exporters:
#             name = exporter_tag_to_string(exporter.tag)
#             build_folder = exporter.attrib['targetFolder']
#             print("{}:\n    {}".format(name, build_folder))
#     print('')


# def get_modules(root):
#     for modules in root.iter('MODULES'):
#         print("MODULES: {}".format(len(modules)))
#         for module in modules:
#             print("{}".format(module.attrib['id']))
#     print('')
