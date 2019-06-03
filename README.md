# Python JUCE

Python classes & functions for manipulating Projucer `.jucer` files. Only vanilla python is used. No dependencies!

[**Examples**](https://github.com/tobanteAudio/python-juce/tree/master/example)

[**Github Repository**](https://github.com/tobanteaudio/python-juce)

[**Developer Documentation**](https://python-juce.readthedocs.io/en/latest)

## Status

|                                                   LICENSE                                                   |                                                             Linux                                                             |                                                                        Windows                                                                        |                            Documentation                             |                                                                  Coverage                                                                  |
| :---------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: |
| [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) | [![Build Status](https://travis-ci.org/tobanteAudio/modEQ.svg?branch=master)](https://travis-ci.org/tobanteAudio/python-juce) | [![AppVeyor Build status](https://img.shields.io/appveyor/ci/tobanteAudio/python-juce.svg)](https://ci.appveyor.com/project/tobanteAudio/python-juce) | ![Read the Docs](https://img.shields.io/readthedocs/python-juce.svg) | [![codecov](https://codecov.io/gh/tobanteAudio/python-juce/branch/master/graph/badge.svg)](https://codecov.io/gh/tobanteAudio/python-juce) |

## Features

- Read & write `.jucer` files
- Set project attributes (version, company, etc...)
- Attribute validation

## Install

### Source

```sh
git clone https://github.com/tobanteAudio/python-juce.git
cd python-juce

make install    # pip install .
# or
make develop    # pip install -e .
```

## Usage

```python
from juce.projucer import JucerFile, Projucer

jucerFile = JucerFile('path/to/project.jucer')
```

```python
# Attributes (get)
print(jucerFile.path)                           # path/to/project.jucer
print(jucerFile.name)                           # project
print(jucerFile.project_type)                   # audioplug
print(jucerFile.cpp_language_standard)          # 17

# Attributes (set)
jucerFile.path = 'new/path/to/project.jucer'
jucerFile.version = '0.2.1'

# Attributes (validation), the following lines fail silently
jucerFile.cpp_language_standard = '98'
jucerFile.project_line_feed = '98'
jucerFile.project_type = 'foo'
jucerFile.display_splash_screen = "98"
jucerFile.binary_data_namespace = 'BAD NS'
jucerFile.plugin_code = 'too'

# Turn on exceptions
jucerFile.silent_validation = False

# Attributes (validation), the following line will raise a ValueError
jucerFile.cpp_language_standard = '98'
```

```python
# Write to file
jucerFile.save()
jucerFile.save_as('some/path/project.jucer')
```

```py
# Create a controller for the Projucer executable.
# It searches in $PATH for Projucer
projucer = Projucer()

# Search in custom path
projucer = Projucer("/some/path")

# Info
print(projucer.which)
projucer.status("path/to/project.jucer")

projucer.resave("path/to/project.jucer")

projucer.set_version("path/to/project.jucer", "0.1.0")
projucer.get_version("path/to/project.jucer")

# Cleanup
projucer.fix_broken_include_paths("path/to/src")
projucer.trim_whitespace("path/to/src")
projucer.tidy_divider_comments("path/to/src")
projucer.remove_tabs("path/to/src")
```

## Development

### Makefile

```sh
make install        # pip install .
make deps           # pip install -r requirements-dev.txt
make develop        # pip install -e .
make test           # Unit tests (pytest)
make integration    # Integration tests (require Projucer in $PATH)
make lint           # Linting (pylint)
make docs           # Documentation (sphinx)
make stats          # Repository stats (cloc)
```

## ToDO

- Set preprocessor defines
- Set enablePluginBinaryCopyStep
- Set warning levels, optimizations
- Warnings for useGlobalPath
- Validate `.jucer` files
