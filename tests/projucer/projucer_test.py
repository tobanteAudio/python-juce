# pylint: skip-file

from juce.projucer import Projucer


def test_projucer_default_path():
    projucer = Projucer()

    assert projucer.path is not None
    assert projucer.path_count > 0

    NoneType = type(None)
    assert isinstance(projucer.which, (NoneType, str))


def test_projucer_custom_path():
    projucer = Projucer("/home/path")

    assert projucer.path is not None
    assert projucer.path_count > 0

    NoneType = type(None)
    assert isinstance(projucer.which, (NoneType, str))
