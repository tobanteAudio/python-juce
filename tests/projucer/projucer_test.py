# pylint: skip-file
import os

import pytest

from juce.projucer import Projucer

BASE_PATH = "test_data/AwesomeAudioApp/"
JUCER_FILE = BASE_PATH + "AwesomeAudioApp.jucer"
SOURCE_DIR = BASE_PATH + "Source"


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
    assert isinstance(stdout, bytes)
    assert isinstance(stderr, type(None))

    output = stdout.decode('utf-8')
    assert 'Name: AwesomeAudioApp' in output
    assert 'UID: nrGl9Q' in output


@pytest.mark.integration_test
def test_projucer_resave():
    projucer = Projucer()
    stdout, stderr = projucer.resave(JUCER_FILE)
    assert isinstance(stdout, bytes)
    assert isinstance(stderr, type(None))

    output = stdout.decode('utf-8')
    assert 'Re-saving file:' in output


@pytest.mark.integration_test
def test_projucer_resave_resources():
    projucer = Projucer()
    stdout, stderr = projucer.resave_resources(JUCER_FILE)
    assert isinstance(stdout, bytes)
    assert isinstance(stderr, type(None))

    output = stdout.decode('utf-8')
    assert 'Re-saving project resources:' in output


@pytest.mark.integration_test
def test_projucer_get_version():
    projucer = Projucer()
    stdout, stderr = projucer.get_version(JUCER_FILE)
    assert isinstance(stdout, bytes)
    assert isinstance(stderr, type(None))

    output = stdout.decode('utf-8')
    assert '0.1.1' in output


@pytest.mark.integration_test
def test_projucer_set_version():
    old_version = '0.1.1'
    new_version = '0.1.2'
    projucer = Projucer()

    # Set to new
    stdout, stderr = projucer.set_version(JUCER_FILE, new_version)
    assert isinstance(stdout, bytes)
    assert isinstance(stderr, type(None))

    output = stdout.decode('utf-8')
    assert new_version in output

    # Set to old
    stdout, stderr = projucer.set_version(JUCER_FILE, old_version)
    assert isinstance(stdout, bytes)
    assert isinstance(stderr, type(None))

    output = stdout.decode('utf-8')
    assert old_version in output


@pytest.mark.integration_test
def test_projucer_bump_version():
    old_version = '0.1.1'
    new_version = '0.1.2'
    projucer = Projucer()

    # Set to new
    stdout, stderr = projucer.bump_version(JUCER_FILE)
    assert isinstance(stdout, bytes)
    assert isinstance(stderr, type(None))

    output = stdout.decode('utf-8')
    assert new_version in output

    # Set to old
    stdout, stderr = projucer.set_version(JUCER_FILE, old_version)
    assert isinstance(stdout, bytes)
    assert isinstance(stderr, type(None))

    output = stdout.decode('utf-8')
    assert old_version in output


@pytest.mark.integration_test
def test_projucer_set_global_search_path():
    projucer = Projucer()
    stdout, stderr = projucer.set_global_search_path(
        'linux', 'defaultUserModulePath', '~/modules')

    assert isinstance(stdout, bytes)
    assert isinstance(stderr, type(None))


@pytest.mark.integration_test
def test_projucer_trans():
    projucer = Projucer()
    stdout, stderr = projucer.trans(SOURCE_DIR)

    assert isinstance(stdout, bytes)
    assert isinstance(stderr, type(None))


@pytest.mark.integration_test
def test_projucer_obfuscated_string_code():
    projucer = Projucer()
    stdout, stderr = projucer.obfuscated_string_code(JUCER_FILE)

    assert isinstance(stdout, bytes)
    assert isinstance(stderr, type(None))

    output = stdout.decode('utf-8')
    assert 'String createString()' in output
    assert 'jassert (result ==' in output


@pytest.mark.integration_test
def test_projucer_encode_binary():
    # Create empty header file
    header_file = 'test_data/binary/binary_data.h'
    open(header_file, 'a').close()
    empty_size = os.path.getsize(header_file)
    assert empty_size == 0

    # Call Projucer encode binary
    projucer = Projucer()
    stdout, stderr = projucer.encode_binary(
        'test_data/binary/logo.png', header_file)

    assert isinstance(stdout, bytes)
    assert isinstance(stderr, type(None))

    # Check if size changed
    full_size = os.path.getsize(header_file)
    assert full_size > empty_size

    # Delete file
    os.remove(header_file)
