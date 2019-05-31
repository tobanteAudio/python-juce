"""Getting started
"""

from juce.projucer import JucerFile, Projucer

jucerFile = JucerFile('path/to/project.jucer')

# Jucer File

# Attributes (get)
print(jucerFile.path)                           # path/to/project.jucer
print(jucerFile.name)                           # project
print(jucerFile.project_type)                   # audioplug
print(jucerFile.cpp_language_standard)          # 17

# Attributes (set)
jucerFile.path = 'new/path/to/project.jucer'
jucerFile.version = '0.2.1'

# Basic validation, the following lines fail silently
jucerFile.cpp_language_standard = '98'          # Not: 11, 14, 17, latest
jucerFile.project_line_feed = '98'              # Not: '\n' or '\r\n'
# Not: guiapp, audioplug, etc...
jucerFile.project_type = 'foo'
jucerFile.display_splash_screen = "98"          # Not a boolean
jucerFile.binary_data_namespace = 'BAD NS'      # Includes unvalid char (space)
# Not 4 characters & No upper case
jucerFile.plugin_code = 'too'

# Turn on exceptions
jucerFile.silent_validation = False

# Basic validation, the following line will raise ValueError
jucerFile.cpp_language_standard = '98'          # Not: 11, 14, 17, latest

# Write to file
jucerFile.save()                                # Override on save
jucerFile.save_as('some/path/project.jucer')    # Save to new location

# PROJUCER

# projucer = Projucer("/some/path")
projucer = Projucer()

for directory in projucer.path:
    print(directory)

print(projucer.which)
print(projucer.path_count)

projucer.status("tests/assets/pluginA.jucer")
# projucer.resave("tests/assets/pluginA.jucer")
