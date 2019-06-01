Examples
=============

Some example use cases. Simply clone the repository to run the examples


Consistency between projects
-----------------------------
If you have multiple projects using the Projucer, you can check if the common
settings are set equal.

.. code-block:: python

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

Projucer Automation
--------------------

.. code-block:: python

    """Projucer Automation
    """
    import os

    from juce.projucer import Projucer

    SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

    PROJECT_NAME = "AwesomeAudioApp"
    PROJECT_DIRECTORY = "{}/{}".format(SCRIPT_DIRECTORY, PROJECT_NAME)
    SOURCE_DIRECTORY = "{}/{}".format(PROJECT_DIRECTORY, "/Source")
    JUCER_FILE_PATH = '{}/{}.jucer'.format(PROJECT_DIRECTORY, PROJECT_NAME)


    def main():
        """Entry point"""
        # Create object controlling the Projucer binary
        # projucer = Projucer("/some/path")
        projucer = Projucer()
        print(projucer.which)

        # Status
        projucer.status(JUCER_FILE_PATH)

        # Generate build files
        projucer.resave(JUCER_FILE_PATH)
        projucer.resave_resources(JUCER_FILE_PATH)

        # Version
        projucer.get_version(JUCER_FILE_PATH)
        # projucer.git_tag_version(JUCER_FILE_PATH)
        projucer.set_version(JUCER_FILE_PATH, "0.1.0")
        projucer.get_version(JUCER_FILE_PATH)
        projucer.bump_version(JUCER_FILE_PATH)
        projucer.get_version(JUCER_FILE_PATH)

        # Cleanup
        projucer.fix_broken_include_paths(SOURCE_DIRECTORY)
        projucer.trim_whitespace(SOURCE_DIRECTORY)
        projucer.tidy_divider_comments(SOURCE_DIRECTORY)
        projucer.remove_tabs(SOURCE_DIRECTORY)

        # Other (Not tested yet)
        # projucer.build_module("target", "module_name")
        # projucer.build_all_modules("target", "module_folder")
        # projucer.encode_binary("source", "target_cpp")
        # projucer.obfuscated_string_code("Somestring")
        # projucer.set_global_search_path("os", "identifier", "new/path")
        # projucer.trans("target/folder")
        # projucer.trans_finish("prefile", "postfile", "existing_file")

    if __name__ == "__main__":
        main()