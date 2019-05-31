# pylint: skip-file

from juce.projucer import Projucer


def test_projucer_status():
    projucer = Projucer()

    if projucer.which:
        projucer.status("tests/assets/pluginA.jucer")


def test_projucer_resave():
    projucer = Projucer()

    if projucer.which:
        projucer.resave("tests/assets/pluginA.jucer")
