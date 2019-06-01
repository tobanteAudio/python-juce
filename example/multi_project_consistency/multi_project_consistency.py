"""Multi Project Consistency
"""
import os

from juce.projucer import JucerFile

SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


def main():
    """Entry point
    """
    a = JucerFile('{}/pluginA.jucer'.format(SCRIPT_DIRECTORY))
    b = JucerFile('{}/pluginB.jucer'.format(SCRIPT_DIRECTORY))

    assert a.company == b.company
    assert a.company_email == b.company_email
    assert a.company_website == b.company_website
    assert a.company_copyright == b.company_copyright

    assert a.plugin_manufacturer == b.plugin_manufacturer
    assert a.plugin_manufacturer_code == b.plugin_manufacturer_code

    assert a.cpp_language_standard == b.cpp_language_standard
    assert a.display_splash_screen == b.display_splash_screen
    assert a.report_app_usage == b.report_app_usage

    print("Check finished")


if __name__ == "__main__":
    main()
