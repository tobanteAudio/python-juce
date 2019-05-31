from juce.env_helpers import get_list_of_path_dirs


def test_get_list_of_path_dirs():

    path_list = get_list_of_path_dirs()
    assert len(path_list) > 0
