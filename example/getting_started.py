"""Getting started
"""
from juce.projucer import Projucer


def main():
    """Entry point
    """
    projucer = Projucer()  # or
    # projucer = Projucer("/some/path")

    for directory in projucer.path:
        print(directory)

    print(projucer.which)
    print(projucer.path_count)

    projucer.status("tests/assets/pluginA.jucer")


if __name__ == "__main__":
    main()
