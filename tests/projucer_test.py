from juce.projucer import Projucer


def test_projucer_class():
    projucer = Projucer()
    assert projucer.path != None
