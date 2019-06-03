# pylint: skip-file
import pytest

from juce.projucer import Projucer

JUCER_FILE = "tests/assets/AwesomeAudioApp/AwesomeAudioApp.jucer"


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


@pytest.mark.integration_test
def test_projucer_status():
    projucer = Projucer()
    stdout, stderr = projucer.status(JUCER_FILE)
    assert stdout
    assert isinstance(stdout, bytes)
    assert isinstance(stderr, type(None))


@pytest.mark.integration_test
def test_projucer_resave():
    projucer = Projucer()
    stdout, stderr = projucer.resave(JUCER_FILE)
    assert stdout
    assert isinstance(stdout, bytes)
    assert isinstance(stderr, type(None))


@pytest.mark.integration_test
def test_projucer_resave_resources():
    projucer = Projucer()
    stdout, stderr = projucer.resave_resources(JUCER_FILE)
    assert stdout
    assert isinstance(stdout, bytes)
    assert isinstance(stderr, type(None))
