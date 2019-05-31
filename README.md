# Python JUCE

Python classes & functions for manipulating Projucer `.jucer` files. Only vanilla python is used. No dependencies!

## Status

|                                                   LICENSE                                                   |                                                         Linux / macOS                                                         |                                     Coverage                                     |
| :---------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------: |
| [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) | [![Build Status](https://travis-ci.org/tobanteAudio/modEQ.svg?branch=master)](https://travis-ci.org/tobanteAudio/python-juce) | ![Codecov](https://img.shields.io/codecov/c/github/tobanteAudio/python-juce.svg) |

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

# Properties (get)
print(jucerFile.path)                           # path/to/project.jucer
print(jucerFile.name)                           # project
print(jucerFile.project_type)                   # audioplug
print(jucerFile.cpp_language_standard)          # 17

# Properties (set)
jucerFile.path = 'new/path/to/project.jucer'
jucerFile.version = '0.2.1'

# Write to disc
jucerFile.save()                                # Override on save
jucerFile.save_as('some/path/project.jucer')    # Save to new location

```

## Development

### Makefile

```sh
make deps       # pip install -r requirements.txt
make develop    # pip install -e .
make test       # Unit tests
make coverage   # Coverage report
make docs       # Documentation
make stats      # Repository stats (using cloc)
```
