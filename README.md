# Python JUCE

Python classes & functions for manipulating Projucer `.jucer` files. Only vanilla python is used. No dependencies!

## Status

|                                                   LICENSE                                                   |                                                             Linux                                                             |                                                                        Windows                                                                        |                                                                  Coverage                                                                  |
| :---------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: |
| [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) | [![Build Status](https://travis-ci.org/tobanteAudio/modEQ.svg?branch=master)](https://travis-ci.org/tobanteAudio/python-juce) | [![AppVeyor Build status](https://img.shields.io/appveyor/ci/tobanteAudio/python-juce.svg)](https://ci.appveyor.com/project/tobanteAudio/python-juce) | [![codecov](https://codecov.io/gh/tobanteAudio/python-juce/branch/master/graph/badge.svg)](https://codecov.io/gh/tobanteAudio/python-juce) |

## Features

- Read & write `.jucer` files
- Set project attributes (version, company, etc...)
- Attribute validation

## Install

### Source

```sh
git clone https://github.com/tobanteAudio/python-juce.git
cd python-juce
pip install -e .
```

## Usage

```python
from juce.projucer import JucerFile

jucerFile = JucerFile('path/to/project.jucer')

# Attributes (get)
print(jucerFile.path)                           # path/to/project.jucer
print(jucerFile.name)                           # project
print(jucerFile.project_type)                   # audioplug
print(jucerFile.cpp_language_standard)          # 17

# Attributes (set)
jucerFile.path = 'new/path/to/project.jucer'
jucerFile.version = '0.2.1'

# Basic validation
jucerFile.cpp_language_standard = '98'          # Not: 11, 14, 17, latest
jucerFile.project_type = 'foo'                  # Not: guiapp, consoleapp, library, dll, audioplug
jucerFile.display_splash_screen = "98"          # Not a boolean
jucerFile.binary_data_namespace = 'BAD NS'      # Includes unvalid char (space)
jucerFile.plugin_code = 'too'                   # Not 4 characters & No upper case

# Write to file
jucerFile.save()                                # Override on save
jucerFile.save_as('some/path/project.jucer')    # Save to new location

```

## Development

### Makefile

```sh
make install    # pip install .
make deps       # pip install -r requirements-dev.txt
make develop    # pip install -e .
make test       # Unit tests
make coverage   # Coverage report
make docs       # Documentation
make stats      # Repository stats (using cloc)
```

## ToDO

- Set preprocessor defines
- Set enablePluginBinaryCopyStep
- Set warning levels, optimizations
- Warnings for useGlobalPath
