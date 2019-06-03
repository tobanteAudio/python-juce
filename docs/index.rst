Python JUCE
=============

Python classes & functions for manipulating Projucer `.jucer` files. Only vanilla python is used. No dependencies!

|license| |travis-status| |appveyor-status| |coverage|


Features
---------
#. Read & write `.jucer` files
#. Set project attributes (version, company, etc...)
#. Attribute validation

Install
---------
.. code-block:: shell

    git clone https://github.com/tobanteAudio/python-juce.git
    cd python-juce
    make install    # pip install .
    # or
    make develop    # pip install -e .

Quick Start
------------

.. code-block:: python

    from juce.projucer import Projucer, JucerFile

    jucerFile = JucerFile('path/to/project.jucer')


.. code-block:: python

    # Attributes (get)
    print(jucerFile.path)                           # path/to/project.jucer
    print(jucerFile.name)                           # project
    print(jucerFile.project_type)                   # audioplug
    print(jucerFile.cpp_language_standard)          # 17

    # Attributes (set)
    jucerFile.path = 'new/path/to/project.jucer'
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
    jucerFile.cpp_language_standard = '98'


.. code-block:: python

    # Write to file
    jucerFile.save()
    jucerFile.save_as('some/path/project.jucer')

.. code-block:: python

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


References
------------
.. toctree::

    Examples
    Projucer
    JucerFile
    Exporter
    Validation
    Utility

.. |license| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :alt: MIT License
    :target: https://github.com/tobanteAudio/python-juce/blob/master/LICENSE

.. |travis-status| image:: https://img.shields.io/travis/tobanteAudio/python-juce.svg?style=flat
    :alt: Build status Linux/macOS
    :target: https://travis-ci.org/tobanteAudio/python-juce

.. |appveyor-status| image:: https://img.shields.io/appveyor/ci/tobanteAudio/python-juce.svg
    :alt: Build status Windows
    :target: https://ci.appveyor.com/project/tobanteAudio/python-juce

.. |coverage| image:: https://codecov.io/gh/tobanteAudio/python-juce/branch/master/graph/badge.svg
    :alt: Test coverage
    :target: https://codecov.io/gh/tobanteAudio/python-juce



