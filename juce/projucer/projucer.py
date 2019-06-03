"""Holds the Projucer class"""

# pylint: disable=too-many-public-methods,no-self-use

import shutil
import subprocess

from juce.util import (get_list_of_path_dirs, print_subprocess)


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
        return self._which

    def resave(self, project):
        """Resaves all files and resources in a project,
        to generate build files.
        """
        assert isinstance(project, str)
        if self._which:
            proc = subprocess.Popen([self._which, '--resave', project],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def resave_resources(self, project):
        """Resaves just the binary resources for a project.
        """
        assert isinstance(project, str)
        if self._which:
            proc = subprocess.Popen([self._which, '--resave-resources',
                                     project],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def get_version(self, project):
        """Returns the version number of a project.
        """
        assert isinstance(project, str)
        if self._which:
            proc = subprocess.Popen([self._which, '--get-version', project],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def set_version(self, project, version):
        """Updates the version number in a project.
        """
        assert isinstance(project, str)
        if self._which:
            proc = subprocess.Popen([self._which, '--set-version',
                                     version, project],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def bump_version(self, project):
        """Updates the minor version number in a project by 1.
        """
        assert isinstance(project, str)
        if self._which:
            proc = subprocess.Popen([self._which, '--bump-version',
                                     project],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def git_tag_version(self, project):
        """Invokes 'git tag' to attach the project's version
        number to the current git repository.
        """
        assert isinstance(project, str)
        if self._which:
            proc = subprocess.Popen([self._which, '--git-tag-version',
                                     project],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def status(self, project):
        """Displays status info about the Projucer project
        """
        assert isinstance(project, str)
        if self._which:
            proc = subprocess.Popen([self._which, '--status', project],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def build_module(self, target_folder, module_folder):
        """Zips a module into a downloadable file format.
        """
        assert isinstance(target_folder, str)
        assert isinstance(module_folder, str)
        if self._which:
            proc = subprocess.Popen([self._which, '--buildmodule',
                                     target_folder, module_folder],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def build_all_modules(self, target_folder, module_folder):
        """Zips all modules in a given folder and creates an index for them.
        """
        assert isinstance(target_folder, str)
        assert isinstance(module_folder, str)
        if self._which:
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
        assert isinstance(target_folder, str)
        if self._which:
            proc = subprocess.Popen([self._which, '--trim-whitespace',
                                     target_folder],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def remove_tabs(self, target_folder):
        """Scans the given folder for C/C++ source files (recursively),
        and replaces any tab characters with 4 spaces.
        """
        assert isinstance(target_folder, str)
        if self._which:
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
        assert isinstance(target_folder, str)
        if self._which:
            proc = subprocess.Popen([self._which, '--tidy-divider-comments',
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
        assert isinstance(target_folder, str)
        if self._which:
            proc = subprocess.Popen([self._which, '--fix-broken-include-paths',
                                     target_folder],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)

    def obfuscated_string_code(self, string_to_obfuscate):
        """Generates a C++ function which returns the given string,
        but in an obfuscated way.
        """
        assert isinstance(string_to_obfuscate, str)
        if self._which:
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
        assert isinstance(source_binary_file, str)
        assert isinstance(target_cpp_file, str)
        if self._which:
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
        assert isinstance(target_folder, str)
        if self._which:
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
        assert isinstance(pre_translated_file, str)
        assert isinstance(post_translated_file, str)
        assert isinstance(optional_existing_translation_file, str)
        if self._which:
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
        assert isinstance(os_system, str)
        assert isinstance(identifier_to_set, str)
        assert isinstance(new_path, str)
        if self._which:
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
        assert isinstance(path_to_pip, str)
        assert isinstance(path_to_output, str)
        if self._which:
            proc = subprocess.Popen([self._which, '--create-project-from-pip',
                                     path_to_pip, path_to_output],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            print_subprocess(proc)
