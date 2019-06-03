"""Holds the Projucer class"""

# pylint: disable=too-many-public-methods,no-self-use

import shutil
import subprocess


class Projucer():
    """Represents a controller to the Projucer executable.

        :param path: Optional path to search for Projucer. Default is $PATH
        :raises: :class:`OSError`: On construction, if exe was not found.
    """

    EXE_NAME = 'Projucer'

    def __init__(self, path=None):
        # Search in $PATH
        if not path:
            self._which = shutil.which(Projucer.EXE_NAME, path=None)

        # Search in custom path
        if path:
            assert isinstance(path, str)
            self._which = shutil.which(Projucer.EXE_NAME, path=path)

        if not self._which:
            raise OSError("Projucer executable could not be found")

    @property
    def which(self):
        """Path to Projucer executable
        """
        return self._which

    def resave(self, project):
        """Resaves all files and resources in a project,
        to generate build files.

        :param project: Path to .jucer file.
        """
        assert isinstance(project, str)
        proc = subprocess.Popen([self._which, '--resave', project],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate()
        return_code = proc.returncode
        return {'return_code': return_code, 'stdout': stdout, 'stderr': stderr}

    def resave_resources(self, project):
        """Resaves just the binary resources for a project.

        :param project: Path to .jucer file.
        """
        assert isinstance(project, str)
        proc = subprocess.Popen([self._which, '--resave-resources',
                                 project],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate()
        return_code = proc.returncode
        return {'return_code': return_code, 'stdout': stdout, 'stderr': stderr}

    def get_version(self, project):
        """Returns the version number of a project.

        :param project: Path to .jucer file.
        """
        assert isinstance(project, str)
        proc = subprocess.Popen([self._which, '--get-version', project],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate()
        return_code = proc.returncode
        return {'return_code': return_code, 'stdout': stdout, 'stderr': stderr}

    def set_version(self, project, version):
        """Updates the version number in a project.

        :param project: Path to .jucer file.
        :param version: New version string.
        """
        assert isinstance(project, str)
        proc = subprocess.Popen([self._which, '--set-version',
                                 version, project],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate()
        return_code = proc.returncode
        return {'return_code': return_code, 'stdout': stdout, 'stderr': stderr}

    def bump_version(self, project):
        """Updates the minor version number in a project by 1.

        :param project: Path to .jucer file.
        """
        assert isinstance(project, str)
        proc = subprocess.Popen([self._which, '--bump-version',
                                 project],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate()
        return_code = proc.returncode
        return {'return_code': return_code, 'stdout': stdout, 'stderr': stderr}

    def git_tag_version(self, project):
        """Invokes 'git tag' to attach the project's version
        number to the current git repository.

        :param project: Path to .jucer file.
        """
        assert isinstance(project, str)
        proc = subprocess.Popen([self._which, '--git-tag-version',
                                 project],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate()
        return_code = proc.returncode
        return {'return_code': return_code, 'stdout': stdout, 'stderr': stderr}

    def status(self, project):
        """Displays status info about the Projucer project

        :param project: Path to .jucer file.
        """
        assert isinstance(project, str)
        proc = subprocess.Popen([self._which, '--status', project],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate()
        return_code = proc.returncode
        return {'return_code': return_code, 'stdout': stdout, 'stderr': stderr}

    def build_module(self, target_folder, module_folder):
        """Zips a module into a downloadable file format.

        :param target_folder: Target path.
        :param module_folder: Module path.
        """
        assert isinstance(target_folder, str)
        assert isinstance(module_folder, str)
        proc = subprocess.Popen([self._which, '--buildmodule',
                                 target_folder, module_folder],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate()
        return_code = proc.returncode
        return {'return_code': return_code, 'stdout': stdout, 'stderr': stderr}

    def build_all_modules(self, target_folder, module_folder):
        """Zips all modules in a given folder and creates an index for them.

        :param target_folder: Target path.
        :param module_folder: Module path.
        """
        assert isinstance(target_folder, str)
        assert isinstance(module_folder, str)
        proc = subprocess.Popen([self._which, '--buildallmodules',
                                 target_folder, module_folder],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate()
        return_code = proc.returncode
        return {'return_code': return_code, 'stdout': stdout, 'stderr': stderr}

    def trim_whitespace(self, target_folder):
        """Scans the given folder for C/C++ source files (recursively),
        and trims any trailing whitespace from their lines,
        as well as normalising their line-endings to CR-LF.

        :param target_folder: Trim target path.
        """
        assert isinstance(target_folder, str)
        proc = subprocess.Popen([self._which, '--trim-whitespace',
                                 target_folder],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate()
        return_code = proc.returncode
        return {'return_code': return_code, 'stdout': stdout, 'stderr': stderr}

    def remove_tabs(self, target_folder):
        """Scans the given folder for C/C++ source files (recursively),
        and replaces any tab characters with 4 spaces.

        :param target_folder: Trim target path.
        """
        assert isinstance(target_folder, str)
        proc = subprocess.Popen([self._which, '--remove-tabs',
                                 target_folder],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate()
        return_code = proc.returncode
        return {'return_code': return_code, 'stdout': stdout, 'stderr': stderr}

    def tidy_divider_comments(self, target_folder):
        """Scans the given folder for C/C++ source files (recursively),
        and normalises any juce-style comment division lines (i.e. any lines
        that look like //===== or //------- or /////////// will be replaced).

        :param target_folder: Tidy target path.
        """
        assert isinstance(target_folder, str)
        proc = subprocess.Popen([self._which, '--tidy-divider-comments',
                                 target_folder],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate()
        return_code = proc.returncode
        return {'return_code': return_code, 'stdout': stdout, 'stderr': stderr}

    def fix_broken_include_paths(self, target_folder):
        """Scans the given folder for C/C++ source files (recursively).
        Where a file contains an #include of one of the other filenames,
        it changes it to use the optimum relative path. Helpful for
        auto-fixing includes when re-arranging files and folders in a project.

        :param target_folder: Fix target path.
        """
        assert isinstance(target_folder, str)
        proc = subprocess.Popen([self._which, '--fix-broken-include-paths',
                                 target_folder],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate()
        return_code = proc.returncode
        return {'return_code': return_code, 'stdout': stdout, 'stderr': stderr}

    def obfuscated_string_code(self, string_to_obfuscate):
        """Generates a C++ function which returns the given string,
        but in an obfuscated way.

        :param string_to_obfuscate:
        """
        assert isinstance(string_to_obfuscate, str)
        proc = subprocess.Popen([self._which, '--obfuscated-string-code',
                                 string_to_obfuscate],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate()
        return_code = proc.returncode
        return {'return_code': return_code, 'stdout': stdout, 'stderr': stderr}

    def encode_binary(self, source_binary_file, target_cpp_file):
        """Converts a binary file to a C++ file containing its contents as
        a block of data. Provide a .h file as the target if you want a
        single output file, or a .cpp file if you want a pair of .h/.cpp files.

        :param source_binary_file: Binary file to encode.
        :param target_cpp_file: Encoded cpp file.
        """
        assert isinstance(source_binary_file, str)
        assert isinstance(target_cpp_file, str)
        proc = subprocess.Popen([self._which, '--encode-binary',
                                 source_binary_file, target_cpp_file],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate()
        return_code = proc.returncode
        return {'return_code': return_code, 'stdout': stdout, 'stderr': stderr}

    def trans(self, *target_folder):
        """Scans each of the given folders (recursively) for any NEEDS_TRANS macros,
        and generates a translation file that can be used with Projucer's
        translation file builder.

        :param target_folder: Variatic number if folder paths.
        """
        assert isinstance(target_folder, tuple)
        target_folder = list(target_folder)
        process_args = [self._which, '--trans'] + target_folder
        proc = subprocess.Popen(process_args,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate()
        return_code = proc.returncode
        return {'return_code': return_code, 'stdout': stdout, 'stderr': stderr}

    def trans_finish(self, pre_translated_file, post_translated_file,
                     optional_existing_translation_file=None):
        """Creates a completed translations mapping file, that can be used to
        initialise a LocalisedStrings object. This allows you to localise
        the strings in your project.
        """
        assert isinstance(pre_translated_file, str)
        assert isinstance(post_translated_file, str)
        process_args = [self._which, '--trans-finish',
                        pre_translated_file, post_translated_file
                        ]
        if optional_existing_translation_file:
            assert isinstance(optional_existing_translation_file, str)
            process_args.append(optional_existing_translation_file)
        proc = subprocess.Popen(process_args,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate()
        return_code = proc.returncode
        return {'return_code': return_code, 'stdout': stdout, 'stderr': stderr}

    def set_global_search_path(self, os_system, identifier_to_set, new_path):
        """Sets the global path for a specified os and identifier.
        The os should be either osx, windows or linux and the identifiers can
        be any of the following: defaultJuceModulePath, defaultUserModulePath,
        vst3Path, vstLegacyPath, aaxPath (not valid on linux),
        rtasPath (not valid on linux), androidSDKPath or androidNDKPath.

        :param os_system: osx, windows or linux.
        :param identifier_to_set:
        :param new_path: New search path.
        """
        assert isinstance(os_system, str)
        assert isinstance(identifier_to_set, str)
        assert isinstance(new_path, str)
        proc = subprocess.Popen([self._which, '--set-global-search-path',
                                 os_system, identifier_to_set,
                                 new_path],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate()
        return_code = proc.returncode
        return {'return_code': return_code, 'stdout': stdout, 'stderr': stderr}

    def create_project_from_pip(self, path_to_pip, path_to_output,
                                juce_modules=None, user_modules=None):
        """Generates a folder containing a JUCE project in the specified
        output path using the specified PIP file. Use the optional JUCE and
        user module paths to override the global module paths.

        :param path_to_pip: Path to pip file.
        :param path_to_output: Path to project output.
        :param juce_modules: Path to JUCE modules.
        :param user_modules: Path to user modules.
        """
        assert isinstance(path_to_pip, str)
        assert isinstance(path_to_output, str)
        process_args = [self._which, '--create-project-from-pip',
                        path_to_pip, path_to_output]

        if juce_modules:
            assert isinstance(juce_modules, str)
            process_args.append(juce_modules)
        if user_modules:
            assert isinstance(user_modules, str)
            process_args.append(user_modules)

        proc = subprocess.Popen(process_args,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate()
        return_code = proc.returncode
        return {'return_code': return_code, 'stdout': stdout, 'stderr': stderr}
