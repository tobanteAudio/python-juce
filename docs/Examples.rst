Examples
=============

Some example use cases.


Consistency between projects
-----------------------------
If you have multiple projects using the Projucer, you can check if the common
settings are set equal.

.. code-block:: python

    from juce.projucer import JucerFile

    p1 = JucerFile('path/to/project_1.jucer')
    p2 = JucerFile('path/to/project_2.jucer')

    assert p1.company == p2.company
    assert p1.company_email == p2.company_email
    assert p1.company_website == p2.company_website
    assert p1.company_copyright == p2.company_copyright

    assert p1.plugin_manufacturer == p2.plugin_manufacturer
    assert p1.plugin_manufacturer_code == p2.plugin_manufacturer_code

    assert p1.display_splash_screen == p2.display_splash_screen
    assert p1.cpp_language_standard == p2.cpp_language_standard