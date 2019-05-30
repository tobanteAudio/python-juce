# Python JUCE

Python classes & functions for manipulating Projucer `.jucer` files.

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
