"""Holds the Projucer & JucerFile classes"""

# pylint: disable=too-many-public-methods,no-self-use

import os
import shutil
from xml.etree import ElementTree

from juce.util import XML_HEADER, get_attribute_from_tag, get_list_of_path_dirs
from juce.validation import (
    is_valid_vst3_category,
    is_valid_cpp_standard,
    is_valid_namespace,
    is_valid_boolean,
    is_valid_project_type,
    is_valid_plugin_code,
    is_valid_plugin_manufacturer_code,
    is_valid_line_feed,
    bool_to_integer_string)


class Projucer():
    """Represents the Projucer executable
    """

    EXE_NAME = 'Projucer'

    def __init__(self, path=None):
        """The script will look in $PATH & the path argument for the Projucer executable
        """
        self._path = []
        if path:
            # Check path is string
            assert isinstance(path, str)
            self._path.append(path)
            # Search in custom path
            self._which = shutil.which(Projucer.EXE_NAME, path=path)
            if not self._which:
                # Fallback to $PATH
                self._which = shutil.which(Projucer.EXE_NAME, path=None)

        # Append $PATH
        self._path += get_list_of_path_dirs()

    # PATH
    @property
    def path(self):
        """List of paths equal to the $PATH variable
        """
        return self._path

    # PATH COUNT
    @property
    def path_count(self):
        """Number of directories in $PATH
        """
        return len(self._path)

    # WHICH
    @property
    def which(self):
        """Path to Projucer executable
        """
        return str(self._which)

    @which.setter
    def which(self, which):
        assert isinstance(which, str)
        exists = os.path.isfile(which)
        if exists:
            self._which = which

    def resave(self, project):
        """Resaves a Projucer project, to generate build files
        """


class JucerFile():
    """Represents a jucer file containing a JUCE project"""

    def __init__(self, path, silent_validation=True):
        """Loads the jucer file as xml"""
        self._path = path
        self.tree = ElementTree.parse(path)
        self.root = self.tree.getroot()
        self._silent_validation = silent_validation

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

    # SILENT VALIDATION
    @property
    def silent_validation(self):
        """Silent validation flag"""
        return self._silent_validation

    @silent_validation.setter
    def silent_validation(self, silent_validation):
        self._silent_validation = bool(silent_validation)

    # PATH
    @property
    def path(self):
        """Jucer file path"""
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    # ID
    @property
    def project_id(self):
        """Project id"""
        return get_attribute_from_tag(self.root, 'id')

    @project_id.setter
    def project_id(self, project_id):
        self.root.set('id', project_id)

    # NAME
    @property
    def name(self):
        """Project name"""
        return get_attribute_from_tag(self.root, 'name')

    @name.setter
    def name(self, name):
        self.root.set('name', name)

    # PROJECT TYPE
    @property
    def project_type(self):
        """Project type"""
        return get_attribute_from_tag(self.root, 'projectType')

    @project_type.setter
    def project_type(self, project_type):
        if is_valid_project_type(project_type):
            self.root.set('projectType', project_type)
            return
        self.fail_silent_or_raise()

    # JUCER VERSION
    @property
    def jucer_version(self):
        """Project jucer version"""
        return get_attribute_from_tag(self.root, 'jucerVersion')

    @jucer_version.setter
    def jucer_version(self, version):
        self.root.set('jucerVersion', version)

    # VERSION
    @property
    def version(self):
        """Project version"""
        return get_attribute_from_tag(self.root, 'version')

    @version.setter
    def version(self, version):
        self.root.set('version', version)

    # COMPANY
    @property
    def company(self):
        """Company name"""
        return get_attribute_from_tag(self.root, 'companyName')

    @company.setter
    def company(self, company_name):
        self.root.set('companyName', company_name)

    # COMPANY WEBSITE
    @property
    def company_website(self):
        """Company website"""
        return get_attribute_from_tag(self.root, 'companyWebsite')

    @company_website.setter
    def company_website(self, company_website):
        self.root.set('companyWebsite', company_website)

    # COMPANY EMAIL
    @property
    def company_email(self):
        """Company email"""
        return get_attribute_from_tag(self.root, 'companyEmail')

    @company_email.setter
    def company_email(self, company_email):
        self.root.set('companyEmail', company_email)

    # BUNDLE IDENTIFIER
    @property
    def bundle_identifier(self):
        """Project bundle identifier"""
        return get_attribute_from_tag(self.root, 'bundleIdentifier')

    @bundle_identifier.setter
    def bundle_identifier(self, identifier):
        self.root.set('bundleIdentifier', identifier)

    # PLUGIN NAME
    @property
    def plugin_name(self):
        """Plugin name"""
        return get_attribute_from_tag(self.root, 'pluginName')

    @plugin_name.setter
    def plugin_name(self, name):
        self.root.set('pluginName', name)

    # PLUGIN DESCRIPTION
    @property
    def plugin_description(self):
        """Plugin description"""
        return get_attribute_from_tag(self.root, 'pluginDesc')

    @plugin_description.setter
    def plugin_description(self, description):
        self.root.set('pluginDesc', description)

    # PLUGIN MANUFACTURER
    @property
    def plugin_manufacturer(self):
        """Plugin manufacturer"""
        return get_attribute_from_tag(self.root, 'pluginManufacturer')

    @plugin_manufacturer.setter
    def plugin_manufacturer(self, manufacturer):
        self.root.set('pluginManufacturer', manufacturer)

    # PLUGIN MANUFACTURER CODE
    @property
    def plugin_manufacturer_code(self):
        """Plugin manufacturer code"""
        return get_attribute_from_tag(self.root, 'pluginManufacturerCode')

    @plugin_manufacturer_code.setter
    def plugin_manufacturer_code(self, code):
        if is_valid_plugin_manufacturer_code(code):
            self.root.set('pluginManufacturerCode', code)
            return
        self.fail_silent_or_raise()

    # PLUGIN CODE
    @property
    def plugin_code(self):
        """Plugin code"""
        return get_attribute_from_tag(self.root, 'pluginCode')

    @plugin_code.setter
    def plugin_code(self, code):
        if is_valid_plugin_code(code):
            self.root.set('pluginCode', code)
            return
        self.fail_silent_or_raise()

    # PLUGIN AU EXPORT PROFILE
    @property
    def plugin_au_exporter_profile(self):
        """AU exporter profile"""
        return get_attribute_from_tag(self.root, 'pluginAUExportPrefix')

    @plugin_au_exporter_profile.setter
    def plugin_au_exporter_profile(self, exporter_profile):
        self.root.set('pluginAUExportPrefix', exporter_profile)

    # AAX IDENTIFIER
    @property
    def aax_identifier(self):
        """AAX identifier"""
        return get_attribute_from_tag(self.root, 'aaxIdentifier')

    @aax_identifier.setter
    def aax_identifier(self, aax_identifier):
        self.root.set('aaxIdentifier', aax_identifier)

    # VST3 CATEGORY
    @property
    def vst3_category(self):
        """Plugin vst3 category"""
        return get_attribute_from_tag(self.root, 'pluginVST3Category')

    @vst3_category.setter
    def vst3_category(self, category):
        if is_valid_vst3_category(category):
            print("Setting pluginVST3Category with: {}".format(category))
            return
        self.fail_silent_or_raise()

    # BINARY DATA NAMESPACE
    @property
    def binary_data_namespace(self):
        """Returns the plugin binary data namespace"""
        return get_attribute_from_tag(self.root, 'binaryDataNamespace')

    @binary_data_namespace.setter
    def binary_data_namespace(self, namespace):
        if is_valid_namespace(namespace):
            self.root.set('binaryDataNamespace', namespace)
            return
        self.fail_silent_or_raise()

    # C++ LANGUAGE STANDARD
    @property
    def cpp_language_standard(self):
        """C++ standard"""
        return get_attribute_from_tag(self.root, 'cppLanguageStandard')

    @cpp_language_standard.setter
    def cpp_language_standard(self, standard):
        if is_valid_cpp_standard(standard):
            self.root.set('cppLanguageStandard', standard)
            return
        self.fail_silent_or_raise()

    # PLUGIN FORMATS
    @property
    def plugin_formats(self):
        """Returns the plugin formats"""
        return get_attribute_from_tag(self.root, 'pluginFormats')

    @plugin_formats.setter
    def plugin_formats(self, formats):
        print("Setting pluginFormats with: {}".format(formats))

    # COMPANY COPYRIGHT
    @property
    def company_copyright(self):
        """Company copyright"""
        return get_attribute_from_tag(self.root, 'companyCopyright')

    @company_copyright.setter
    def company_copyright(self, copyright_text):
        self.root.set('companyCopyright', copyright_text)

    # DISPLAY SPLASH SCREEN
    @property
    def display_splash_screen(self):
        """Plugin splash screen flag"""
        return get_attribute_from_tag(self.root, 'displaySplashScreen')

    @display_splash_screen.setter
    def display_splash_screen(self, toggle):
        if is_valid_boolean(toggle):
            toggle_number = bool_to_integer_string(toggle)
            self.root.set('displaySplashScreen', toggle_number)
            return
        self.fail_silent_or_raise()
    # REPORT APP USAGE
    @property
    def report_app_usage(self):
        """Plugin report app usage flag"""
        return get_attribute_from_tag(self.root, 'reportAppUsage')

    @report_app_usage.setter
    def report_app_usage(self, toggle):
        if is_valid_boolean(toggle):
            toggle_number = bool_to_integer_string(toggle)
            self.root.set('reportAppUsage', toggle_number)
            return
        self.fail_silent_or_raise()

    # COMPILER FLAG SCHEMES
    @property
    def compiler_flag_schemes(self):
        """Plugin compiler flag schemes"""
        return get_attribute_from_tag(self.root, 'compilerFlagSchemes')

    @compiler_flag_schemes.setter
    def compiler_flag_schemes(self, compiler_schemes):
        print("Setting compilerFlagSchemes with: {}".format(compiler_schemes))

    # PROJECT LINE FEED
    @property
    def project_line_feed(self):
        """Project line feed"""
        return get_attribute_from_tag(self.root, 'projectLineFeed')

    @project_line_feed.setter
    def project_line_feed(self, line_feed):
        if is_valid_line_feed(line_feed):
            self.root.set('projectLineFeed', line_feed)
            return
        self.fail_silent_or_raise()

    def fail_silent_or_raise(self):
        """If silent_validation is False a ValueError is raised"""
        if self._silent_validation:
            return
        raise ValueError("Attribute validation failed")

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
