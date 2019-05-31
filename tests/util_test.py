# pylint: skip-file
import subprocess

from juce.util import get_list_of_path_dirs, print_subprocess


def test_get_list_of_path_dirs():

    path_list = get_list_of_path_dirs()
    assert len(path_list) > 0


def test_print_subprocess():
    proc = subprocess.Popen(['ls'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    print_subprocess(proc)

    proc = subprocess.Popen(['ls', '1234567guigiugiug'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    print_subprocess(proc)
