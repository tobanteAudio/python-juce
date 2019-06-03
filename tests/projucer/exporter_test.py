# pylint: skip-file

from juce.projucer import JucerFile


def test_projucer_exporter():
    path = 'tests/assets/modEQ.jucer'
    jucer_file = JucerFile(path)

    # Basic checks
    assert len(jucer_file.exporters) > 0
    assert isinstance(jucer_file.exporters, list)

    for exp in jucer_file.exporters:
        # Type checks
        assert isinstance(exp.name, str)
        assert isinstance(exp.build_folder, str)
        assert isinstance(exp.configurations, list)
        assert isinstance(exp.module_paths, list)

        # Length
        assert len(exp.configurations) > 0
        assert len(exp.module_paths) > 0

        # Set build folder
        new_folder = "Builds/Folder"
        exp.build_folder = new_folder
        assert exp.build_folder == new_folder
