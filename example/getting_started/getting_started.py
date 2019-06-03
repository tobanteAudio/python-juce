"""Getting started
"""
import os

from juce.projucer import Projucer, JucerFile
from juce.util import get_attribute_from_tag

SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

PROJECT_NAME = "AwesomeAudioApp"
PROJECT_DIRECTORY = "{}/{}".format(SCRIPT_DIRECTORY, PROJECT_NAME)
SOURCE_DIRECTORY = "{}/{}".format(PROJECT_DIRECTORY, "/Source")
JUCER_FILE_PATH = '{}/{}.jucer'.format(PROJECT_DIRECTORY, PROJECT_NAME)


def main():
    """Entry Point
    """
    # Jucer File
    jucer_file = JucerFile(JUCER_FILE_PATH)

    # Attributes (get)
    print(jucer_file.path)                           # path/to/project.jucer
    print(jucer_file.name)                           # project
    print(jucer_file.project_type)                   # audioplug
    print(jucer_file.cpp_language_standard)          # 17
    print(jucer_file.defines)
    print(len(jucer_file.modules))                   # 16
    print(jucer_file.modules)

    # Exporters
    print(len(jucer_file.exporters))
    for exporter in jucer_file.exporters:
        # Name & Folder
        print("{}: {}".format(exporter.name, exporter.build_folder))
        # Configs
        for config in exporter.configurations:
            print("     {}, with debug: {}".format(
                get_attribute_from_tag(config, 'name'),
                get_attribute_from_tag(config, 'isDebug')))
        # Module Paths
        for module in exporter.module_paths:
            print("     Module: {}, path: {}".format(
                get_attribute_from_tag(module, 'id'),
                get_attribute_from_tag(module, 'path')))

    # Attributes (set)
    # jucer_file.path = 'new/path/to/project.jucer'
    jucer_file.version = '0.2.1'

    # Basic validation, the following lines fail silently
    jucer_file.cpp_language_standard = '98'
    jucer_file.project_line_feed = '98'
    jucer_file.project_type = 'foo'
    jucer_file.display_splash_screen = "98"
    jucer_file.binary_data_namespace = 'BAD NS'
    jucer_file.plugin_code = 'too'

    # Turn on exceptions
    jucer_file.silent_validation = False

    # Basic validation, the following line will raise ValueError
    try:
        jucer_file.cpp_language_standard = '98'
    except ValueError as e:
        print(e)

    # Write to file
    jucer_file.cpp_language_standard = '17'
    jucer_file.save()
    # jucer_file.save_as('some/path/project.jucer')

    # PROJUCER
    # projucer = Projucer("/some/path")
    projucer = Projucer()
    print(projucer.which)

    stdout, stderr = projucer.status(JUCER_FILE_PATH)
    assert not stderr
    print(stdout.decode('utf-8'))

    stdout, stderr = projucer.resave(JUCER_FILE_PATH)
    assert not stderr
    print(stdout.decode('utf-8'))

    stdout, stderr = projucer.resave_resources(JUCER_FILE_PATH)
    assert not stderr
    print(stdout.decode('utf-8'))

    stdout, stderr = projucer.obfuscated_string_code('SOURCE_DIRECTORY')
    assert not stderr
    print(stdout.decode('utf-8'))

    stdout, stderr = projucer.set_global_search_path(
        'linux', 'defaultUserModulePath', '~/modules2')
    assert not stderr

    stdout, stderr = projucer.trans(SOURCE_DIRECTORY)
    assert not stderr
    print(stdout.decode('utf-8'))

    stdout, stderr = projucer.encode_binary(
        PROJECT_DIRECTORY+"/Resource/logo.png", PROJECT_DIRECTORY+"/Resource/binary_data.h")
    assert not stderr
    print(stdout.decode('utf-8'))


if __name__ == "__main__":
    main()
