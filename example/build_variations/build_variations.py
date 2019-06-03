"""Build Variantions
"""
import os

from juce.projucer import Projucer, JucerFile

SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

PROJECT_NAME = "AwesomeAudioApp"
PROJECT_DIRECTORY = "{}/{}".format(SCRIPT_DIRECTORY, PROJECT_NAME)
SOURCE_DIRECTORY = "{}/{}".format(PROJECT_DIRECTORY, "/Source")
JUCER_FILE_PATH = '{}/{}.jucer'.format(PROJECT_DIRECTORY, PROJECT_NAME)


def main():
    """Entry point"""

    jucer_file = JucerFile(JUCER_FILE_PATH)

    # Set C++ standard
    jucer_file.cpp_language_standard = '17'

    # Set build folder for windows exporter
    for exporter in jucer_file.exporters:
        if exporter.name == "VS2017":
            if exporter.build_folder == "Builds/VisualStudio2017":
                exporter.build_folder = "Builds/NewWindowsBuild"

    # Save changes to .jucer file
    jucer_file.save()

    # Create object controlling the Projucer binary & check that it's in $PATH
    projucer = Projucer()
    assert projucer.which

    # Generate build files
    projucer.resave(JUCER_FILE_PATH)


if __name__ == "__main__":
    main()
