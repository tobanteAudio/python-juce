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


if __name__ == "__main__":
    main()
