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
    jucer_file.cpp_language_standard = '17'
    jucer_file.save()

    print()
    # # Create object controlling the Projucer binary
    # projucer = Projucer()
    # assert projucer.which

    # # Status
    # projucer.status(JUCER_FILE_PATH)

    # # Generate build files
    # projucer.resave(JUCER_FILE_PATH)
    # projucer.resave_resources(JUCER_FILE_PATH)


if __name__ == "__main__":
    main()
