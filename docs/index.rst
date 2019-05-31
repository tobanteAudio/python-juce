Python JUCE
=============

Python classes & functions for manipulating Projucer `.jucer` files. Only vanilla python is used. No dependencies!

|travis-status| |appveyor-status| |coverage|


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
     make install

Quick Start
------------

.. code-block:: python

     from juce.projucer import JucerFile

     jucerFile = JucerFile('path/to/project.jucer')

     # Attributes (get)
     print(jucerFile.path)                  # path/to/project.jucer
     print(jucerFile.name)                  # project
     print(jucerFile.project_type)          # audioplug
     print(jucerFile.cpp_language_standard) # 17

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

     # Write to file
     jucerFile.save()

     # Save to new location
     jucerFile.save_as('some/path/project.jucer')    


References
------------
.. toctree::

    Projucer
    JucerFile    
    Validation
    Examples

.. |travis-status| image:: https://img.shields.io/travis/tobanteAudio/python-juce.svg?style=flat
    :alt: Build status Linux/macOS
    :target: https://travis-ci.org/tobanteAudio/python-juce

.. |appveyor-status| image:: https://img.shields.io/appveyor/ci/tobanteAudio/python-juce.svg
    :alt: Build status Windows
    :target: https://ci.appveyor.com/project/tobanteAudio/python-juce

.. |coverage| image:: https://codecov.io/gh/tobanteAudio/python-juce/branch/master/graph/badge.svg
    :alt: Test coverage
    :target: https://codecov.io/gh/tobanteAudio/python-juce

License
-------

`MIT`_ © 2019 Tobias Hienzsch

.. _MIT: LICENSE

