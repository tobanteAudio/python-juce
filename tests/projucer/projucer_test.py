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
    result = projucer.status(JUCER_FILE)
    assert result['return_code'] == 0
    assert isinstance(result['stdout'], bytes)
    assert isinstance(result['stderr'], type(None))

    output = result['stdout'].decode('utf-8')
    assert 'Name: AwesomeAudioApp' in output
    assert 'UID: nrGl9Q' in output


@pytest.mark.integration_test
def test_projucer_resave():
    projucer = Projucer()
    result = projucer.resave(JUCER_FILE)
    assert result['return_code'] == 0
    assert isinstance(result['stdout'], bytes)
    assert isinstance(result['stderr'], type(None))

    output = result['stdout'].decode('utf-8')
    assert 'Re-saving file:' in output


@pytest.mark.integration_test
def test_projucer_resave_resources():
    projucer = Projucer()
    result = projucer.resave_resources(JUCER_FILE)
    assert result['return_code'] == 0
    assert isinstance(result['stdout'], bytes)
    assert isinstance(result['stderr'], type(None))

    output = result['stdout'].decode('utf-8')
    assert 'Re-saving project resources:' in output


@pytest.mark.integration_test
def test_projucer_get_version():
    projucer = Projucer()
    result = projucer.get_version(JUCER_FILE)
    assert result['return_code'] == 0
    assert isinstance(result['stdout'], bytes)
    assert isinstance(result['stderr'], type(None))

    output = result['stdout'].decode('utf-8')
    assert '0.1.1' in output


@pytest.mark.integration_test
def test_projucer_set_version():
    old_version = '0.1.1'
    new_version = '0.1.2'
    projucer = Projucer()

    # Set to new
    result = projucer.set_version(JUCER_FILE, new_version)
    assert result['return_code'] == 0
    assert isinstance(result['stdout'], bytes)
    assert isinstance(result['stderr'], type(None))

    output = result['stdout'].decode('utf-8')
    assert new_version in output

    # Set to old
    result = projucer.set_version(JUCER_FILE, old_version)
    assert result['return_code'] == 0
    assert isinstance(result['stdout'], bytes)
    assert isinstance(result['stderr'], type(None))

    output = result['stdout'].decode('utf-8')
    assert old_version in output


@pytest.mark.integration_test
def test_projucer_bump_version():
    old_version = '0.1.1'
    new_version = '0.1.2'
    projucer = Projucer()

    # Set to new
    result = projucer.bump_version(JUCER_FILE)
    assert result['return_code'] == 0
    assert isinstance(result['stdout'], bytes)
    assert isinstance(result['stderr'], type(None))

    output = result['stdout'].decode('utf-8')
    assert new_version in output

    # Set to old
    result = projucer.set_version(JUCER_FILE, old_version)
    assert result['return_code'] == 0
    assert isinstance(result['stdout'], bytes)
    assert isinstance(result['stderr'], type(None))

    output = result['stdout'].decode('utf-8')
    assert old_version in output


@pytest.mark.integration_test
def test_projucer_set_global_search_path():
    projucer = Projucer()
    result = projucer.set_global_search_path(
        'linux', 'defaultUserModulePath', '~/modules')

    assert result['return_code'] == 0
    assert isinstance(result['stdout'], bytes)
    assert isinstance(result['stderr'], type(None))


@pytest.mark.integration_test
def test_projucer_trans():
    projucer = Projucer()
    result = projucer.trans(SOURCE_DIR)

    assert result['return_code'] == 0
    assert isinstance(result['stdout'], bytes)
    assert isinstance(result['stderr'], type(None))


@pytest.mark.integration_test
def test_projucer_obfuscated_string_code():
    projucer = Projucer()
    result = projucer.obfuscated_string_code(JUCER_FILE)

    assert result['return_code'] == 0
    assert isinstance(result['stdout'], bytes)
    assert isinstance(result['stderr'], type(None))

    output = result['stdout'].decode('utf-8')
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
    result = projucer.encode_binary(
        'test_data/binary/logo.png', header_file)

    assert result['return_code'] == 0
    assert isinstance(result['stdout'], bytes)
    assert isinstance(result['stderr'], type(None))

    # Check if size changed
    full_size = os.path.getsize(header_file)
    assert full_size > empty_size

    # Delete file
    os.remove(header_file)


@pytest.mark.integration_test
def test_projucer_create_project_from_pip():
    # Create empty header file
    pip_file = 'test_data/pip/ArpeggiatorTutorial.h'
    pip_size = os.path.getsize(pip_file)
    assert pip_size > 0

    # Call Projucer encode binary
    output = 'test_data/pip/output'
    projucer = Projucer()
    result = projucer.create_project_from_pip(
        pip_file, output)

    assert result['return_code'] == 0
    assert isinstance(result['stdout'], bytes)
    assert isinstance(result['stderr'], type(None))

    # Check file does exist
    assert os.path.isfile(
        output + '/ArpeggiatorTutorial/ArpeggiatorTutorial.jucer')

    # Delete file
    import shutil
    shutil.rmtree(output)


@pytest.mark.integration_test
def test_projucer_create_project_from_pip_broken_module_path():
    # Create empty header file
    pip_file = 'test_data/pip/ArpeggiatorTutorial.h'
    # Call Projucer encode binary
    output = 'test_data/pip/output'
    projucer = Projucer()
    result = projucer.create_project_from_pip(
        pip_file, output, juce_modules='foo/', user_modules='/bar')

    assert result['return_code'] == 1
    assert isinstance(result['stdout'], bytes)
    assert isinstance(result['stderr'], type(None))

    # Check file does NOT exist
    assert not os.path.isfile(
        output + '/ArpeggiatorTutorial/ArpeggiatorTutorial.jucer')
