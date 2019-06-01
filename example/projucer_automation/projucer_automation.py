"""Projucer Automation
"""
import os

from juce.projucer import Projucer

SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
PROJECT_NAME = "AwesomeAudioApp"
PROJECT_DIRECTORY = "{}/{}".format(SCRIPT_DIRECTORY, PROJECT_NAME)
JUCER_FILE_PATH = '{}/{}.jucer'.format(PROJECT_DIRECTORY, PROJECT_NAME)


def main():
    """Entry point"""
    # projucer = Projucer("/some/path")
    projucer = Projucer()

    print(projucer.which)

    projucer.status(JUCER_FILE_PATH)
    projucer.resave(JUCER_FILE_PATH)
    projucer.resave_resources(JUCER_FILE_PATH)
    projucer.get_version(JUCER_FILE_PATH)


if __name__ == "__main__":
    main()
