"""Getting started
"""
import os

from juce.projucer import Projucer, JucerFile
from juce.util import get_attribute_from_tag

SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

jucerFile = JucerFile('{}/example_plugin.jucer'.format(SCRIPT_DIRECTORY))

# Jucer File

# Attributes (get)
print(jucerFile.path)                           # path/to/project.jucer
print(jucerFile.name)                           # project
print(jucerFile.project_type)                   # audioplug
print(jucerFile.cpp_language_standard)          # 17
print(jucerFile.defines)
print(len(jucerFile.modules))                   # 16
print(jucerFile.modules)

# Exporters
print(len(jucerFile.exporters))
for exporter in jucerFile.exporters:
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
# jucerFile.path = 'new/path/to/project.jucer'
jucerFile.version = '0.2.1'

# Basic validation, the following lines fail silently
jucerFile.cpp_language_standard = '98'
jucerFile.project_line_feed = '98'
jucerFile.project_type = 'foo'
jucerFile.display_splash_screen = "98"
jucerFile.binary_data_namespace = 'BAD NS'
jucerFile.plugin_code = 'too'

# Turn on exceptions
jucerFile.silent_validation = False

# Basic validation, the following line will raise ValueError
# jucerFile.cpp_language_standard = '98'

# Write to file
# jucerFile.save()
# jucerFile.save_as('some/path/project.jucer')


# # PROJUCER
# # projucer = Projucer("/some/path")
# projucer = Projucer()

# # Print all directories in $PATH + optional directory
# for directory in projucer.path:
#     print(directory)

# print(projucer.which)
# print(projucer.path_count)

# projucer.status('{}/example_plugin.jucer'.format(SCRIPT_DIRECTORY))
# # projucer.resave('{}/example_plugin.jucer'.format(SCRIPT_DIRECTORY))
