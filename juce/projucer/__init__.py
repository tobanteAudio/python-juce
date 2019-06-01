"""Holds the Projucer & JucerFile classes"""

# pylint: disable=too-many-public-methods,no-self-use

import shutil
import subprocess
from xml.etree import ElementTree

from juce.util import (XML_HEADER,
                       get_attribute_from_tag,
                       get_list_of_path_dirs,
                       print_subprocess)

from juce.validation import (is_valid_vst3_category,
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
        """The script will look in $PATH & the path argument for
        the Projucer executable
        """
        self._path = []
        self._which = shutil.which(Projucer.EXE_NAME, path=None)
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

    @property
    def path(self):
        """List of paths equal to the $PATH variable
        """
        return self._path

    @property
    def path_count(self):
        """Number of directories in $PATH
        """
        return len(self._path)

    @property
    def which(self):
        """Path to Projucer executable
        """
        return str(self._which)

    def resave(self, project):
        """Resaves all files and resources in a project,
        to generate build files.
        """
        if self._which:
            assert isinstance(project, str)
            proc = subprocess.Popen([self._which, '--resave', project],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def resave_resources(self, project):
        """Resaves just the binary resources for a project.
        """
        if self._which:
            assert isinstance(project, str)
            proc = subprocess.Popen([self._which, '--resave-resources',
                                     project],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def get_version(self, project):
        """Returns the version number of a project.
        """
        if self._which:
            assert isinstance(project, str)
            proc = subprocess.Popen([self._which, '--get-version', project],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def set_version(self, project, version):
        """Updates the version number in a project.
        """
        if self._which:
            assert isinstance(project, str)
            proc = subprocess.Popen([self._which, '--set-version',
                                     version, project],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def bump_version(self, project):
        """Updates the minor version number in a project by 1.
        """
        if self._which:
            assert isinstance(project, str)
            proc = subprocess.Popen([self._which, '--bump-version',
                                     project],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def git_tag_version(self, project):
        """Invokes 'git tag' to attach the project's version
        number to the current git repository.
        """
        if self._which:
            assert isinstance(project, str)
            proc = subprocess.Popen([self._which, '--git-tag-version',
                                     project],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def status(self, project):
        """Displays status info about the Projucer project
        """
        if self._which:
            assert isinstance(project, str)
            proc = subprocess.Popen([self._which, '--status', project],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def build_module(self, target_folder, module_folder):
        """Zips a module into a downloadable file format.
        """
        if self._which:
            assert isinstance(target_folder, str)
            assert isinstance(module_folder, str)
            proc = subprocess.Popen([self._which, '--buildmodule',
                                     target_folder, module_folder],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def build_all_modules(self, target_folder, module_folder):
        """Zips all modules in a given folder and creates an index for them.
        """
        if self._which:
            assert isinstance(target_folder, str)
            assert isinstance(module_folder, str)
            proc = subprocess.Popen([self._which, '--buildallmodules',
                                     target_folder, module_folder],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def trim_whitespace(self, target_folder):
        """Scans the given folder for C/C++ source files (recursively),
        and trims any trailing whitespace from their lines,
        as well as normalising their line-endings to CR-LF.
        """
        if self._which:
            assert isinstance(target_folder, str)
            proc = subprocess.Popen([self._which, '--trim-whitespace',
                                     target_folder],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def remove_tabs(self, target_folder):
        """Scans the given folder for C/C++ source files (recursively),
        and replaces any tab characters with 4 spaces.
        """
        if self._which:
            assert isinstance(target_folder, str)
            proc = subprocess.Popen([self._which, '--remove-tabs',
                                     target_folder],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def tidy_divider_comments(self, target_folder):
        """Scans the given folder for C/C++ source files (recursively),
        and normalises any juce-style comment division lines (i.e. any lines
        that look like //===== or //------- or /////////// will be replaced).
        """
        if self._which:
            assert isinstance(target_folder, str)
            proc = subprocess.Popen([self._which, '--tidy-divider-comment',
                                     target_folder],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def fix_broken_include_paths(self, target_folder):
        """Scans the given folder for C/C++ source files (recursively).
        Where a file contains an #include of one of the other filenames,
        it changes it to use the optimum relative path. Helpful for
        auto-fixing includes when re-arranging files and folders in a project.
        """
        if self._which:
            assert isinstance(target_folder, str)
            proc = subprocess.Popen([self._which, '--fix-broken-include-paths',
                                     target_folder],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def obfuscated_string_code(self, string_to_obfuscate):
        """Generates a C++ function which returns the given string,
        but in an obfuscated way.
        """
        if self._which:
            assert isinstance(string_to_obfuscate, str)
            proc = subprocess.Popen([self._which, '--obfuscated-string-code',
                                     string_to_obfuscate],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def encode_binary(self, source_binary_file, target_cpp_file):
        """Converts a binary file to a C++ file containing its contents as
        a block of data. Provide a .h file as the target if you want a
        single output file, or a .cpp file if you want a pair of .h/.cpp files.
        """
        if self._which:
            assert isinstance(source_binary_file, str)
            assert isinstance(target_cpp_file, str)
            proc = subprocess.Popen([self._which, '--encode-binary',
                                     source_binary_file, target_cpp_file],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def trans(self, target_folder):
        """Scans each of the given folders (recursively) for any NEEDS_TRANS macros,
        and generates a translation file that can be used with Projucer's
        translation file builder.
        """
        # ToDo: Make target_folder arg variatic length
        if self._which:
            assert isinstance(target_folder, str)
            proc = subprocess.Popen([self._which, '--trans',
                                     target_folder],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def trans_finish(self, pre_translated_file, post_translated_file,
                     optional_existing_translation_file):
        """Creates a completed translations mapping file, that can be used to
        initialise a LocalisedStrings object. This allows you to localise
        the strings in your project.
        """
        if self._which:
            assert isinstance(pre_translated_file, str)
            assert isinstance(post_translated_file, str)
            assert isinstance(optional_existing_translation_file, str)
            proc = subprocess.Popen([self._which, '--trans-finish',
                                     pre_translated_file, post_translated_file,
                                     optional_existing_translation_file],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def set_global_search_path(self, os_system, identifier_to_set, new_path):
        """Sets the global path for a specified os and identifier.
        The os should be either osx, windows or linux and the identifiers can
        be any of the following: defaultJuceModulePath, defaultUserModulePath,
        vst3Path, vstLegacyPath, aaxPath (not valid on linux),
        rtasPath (not valid on linux), androidSDKPath or androidNDKPath.
        """
        if self._which:
            assert isinstance(os_system, str)
            assert isinstance(identifier_to_set, str)
            assert isinstance(new_path, str)
            proc = subprocess.Popen([self._which, '--set-global-search-path',
                                     os_system, identifier_to_set,
                                     new_path],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def create_project_from_pip(self, path_to_pip, path_to_output):
        """Generates a folder containing a JUCE project in the specified
        output path using the specified PIP file. Use the optional JUCE and
        user module paths to override the global module paths.
        """
        # ToDo: Add juce_modules & user_modules optional paths
        if self._which:
            assert isinstance(path_to_pip, str)
            assert isinstance(path_to_output, str)
            proc = subprocess.Popen([self._which, '--create-project-from-pip',
                                     path_to_pip, path_to_output],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)


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
    def u_id(self):
        """Project unique id"""
        return get_attribute_from_tag(self.root, 'id')

    @u_id.setter
    def u_id(self, u_id):
        self.root.set('id', u_id)

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
        """Binary data namespace"""
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
        """Plugin formats"""
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

    # DEFINES
    @property
    def defines(self):
        """Project defines"""
        return get_attribute_from_tag(self.root, 'defines')

    @defines.setter
    def defines(self, defines):
        self.root.set('defines', defines)

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
