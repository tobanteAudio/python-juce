# pylint: skip-file
import pytest

from juce.projucer import Projucer


@pytest.mark.integration_test
def test_projucer_default_path():
    projucer = Projucer()

    assert projucer.path is not None
    assert projucer.path_count > 0

    assert isinstance(projucer.which, str)


@pytest.mark.integration_test
def test_projucer_custom_path():
    projucer = Projucer(r'C:\Dev\bin')

    assert projucer.path is not None
    assert projucer.path_count > 0

    assert isinstance(projucer.which, str)
