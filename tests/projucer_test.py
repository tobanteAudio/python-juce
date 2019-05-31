from juce.projucer import JucerFile


def test_cpp_standard_validation():
    path = 'tests/assets/modEQ.jucer'
    jucerFile = JucerFile(path)

    assert jucerFile.cpp_language_standard == '17'

    JucerFile.cpp_language_standard = '11'
    JucerFile.cpp_language_standard = '14'
    JucerFile.cpp_language_standard = '17'
    JucerFile.cpp_language_standard = 'latest'

    JucerFile.cpp_language_standard = 'foo'


def test_GuiApp_project_properties():
    path = 'tests/assets/GuiApp.jucer'
    jucerFile = JucerFile(path)

    # Properties (get)
    assert jucerFile.path == path
    assert jucerFile.id == 'hgSXn0'
    assert jucerFile.name == 'GuiApp'
    assert jucerFile.project_type == 'guiapp'
    assert jucerFile.jucer_version == '5.4.3'
    assert jucerFile.version == None
    assert jucerFile.company == None
    assert jucerFile.company_website == None
    assert jucerFile.company_email == None


def test_modEQ_project_properties():
    path = 'tests/assets/modEQ.jucer'
    jucerFile = JucerFile(path)

    # Properties (get)
    assert jucerFile.path == path
    assert jucerFile.id == 'jWny5A'
    assert jucerFile.name == 'modEQ'
    assert jucerFile.project_type == 'audioplug'
    assert jucerFile.jucer_version == '5.4.3'
    assert jucerFile.version == '0.4.0'
    assert jucerFile.company == 'tobanteAudio'
    assert jucerFile.company_website == 'https://github.com/tobanteAudio'
    assert jucerFile.company_email == 'tobanteAudio@gmail.com'
    # assert jucerFile.bundle_identifier ==
    # assert jucerFile.plugin_name ==
    # assert jucerFile.plugin_description ==
    # assert jucerFile.plugin_manufacturer ==
    # assert jucerFile.plugin_manufacturer_code ==
    # assert jucerFile.plugin_code ==
    # assert jucerFile.plugin_au_exporter_profile ==
    # assert jucerFile.aax_identifier ==
    # assert jucerFile.vst3_category ==
    # assert jucerFile.binary_data_namespace ==
    # assert jucerFile.cpp_language_standard ==
    # assert jucerFile.plugin_formats ==
    # assert jucerFile.company_copyright ==
    # assert jucerFile.display_splash_screen ==
    # assert jucerFile.report_app_usage ==
    # assert jucerFile.compiler_flag_schemes ==
    # assert jucerFile.project_line_feed ==
