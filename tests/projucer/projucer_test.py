# pylint: skip-file
import pytest

from juce.projucer import Projucer

JUCER_FILE = "tests/assets/AwesomeAudioApp/AwesomeAudioApp.jucer"


def test_projucer_bad_path():
    with pytest.raises(OSError) as excinfo:
        Projucer('/root')
    assert "Projucer executable could not be found" in str(excinfo.value)


@pytest.mark.integration_test
def test_projucer_default_path():
    projucer = Projucer()
    assert isinstance(projucer.which, str)


@pytest.mark.integration_test
def test_projucer_status():
    projucer = Projucer()
    stdout, stderr = projucer.status(JUCER_FILE)
    assert stdout
    assert isinstance(stdout, bytes)
    assert isinstance(stderr, type(None))

    output = stdout.decode('utf-8')
    assert 'Name: AwesomeAudioApp' in output
    assert 'UID: nrGl9Q' in output


@pytest.mark.integration_test
def test_projucer_resave():
    projucer = Projucer()
    stdout, stderr = projucer.resave(JUCER_FILE)
    assert stdout
    assert isinstance(stdout, bytes)
    assert isinstance(stderr, type(None))

    output = stdout.decode('utf-8')
    assert 'Re-saving file:' in output
    assert 'Finished saving:' in output


@pytest.mark.integration_test
def test_projucer_resave_resources():
    projucer = Projucer()
    stdout, stderr = projucer.resave_resources(JUCER_FILE)
    assert stdout
    assert isinstance(stdout, bytes)
    assert isinstance(stderr, type(None))

    output = stdout.decode('utf-8')
    assert 'Re-saving project resources:' in output


@pytest.mark.integration_test
def test_projucer_get_version():
    projucer = Projucer()
    stdout, stderr = projucer.get_version(JUCER_FILE)
    assert stdout
    assert isinstance(stdout, bytes)
    assert isinstance(stderr, type(None))

    output = stdout.decode('utf-8')
    assert '0.1.1' in output
