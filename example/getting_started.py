"""Getting started
"""
from juce.projucer import Projucer


def main():
    """Entry point
    """
    projucer = Projucer("~/go/bin")

    for directory in projucer.path:
        print(directory)

    print(projucer.which)
    print(projucer.path_count)


if __name__ == "__main__":
    main()
