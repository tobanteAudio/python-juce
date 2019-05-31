from juce.projucer import JucerFile


def test_cpp_standard_validation():
    path = 'tests/assets/modEQ.jucer'
    jucerFile = JucerFile(path)

    assert jucerFile.cpp_language_standard == '17'

    jucerFile.cpp_language_standard = '11'
    assert jucerFile.cpp_language_standard == '11'

    jucerFile.cpp_language_standard = '14'
    assert jucerFile.cpp_language_standard == '14'

    jucerFile.cpp_language_standard = '17'
    assert jucerFile.cpp_language_standard == '17'

    jucerFile.cpp_language_standard = 'latest'
    assert jucerFile.cpp_language_standard == 'latest'

    jucerFile.cpp_language_standard = 'foo'
    assert jucerFile.cpp_language_standard == 'latest'


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
    assert jucerFile.bundle_identifier == "com.tobanteAudio.modEQ"
    assert jucerFile.plugin_name == 'modEQ'
    assert jucerFile.plugin_description == 'EQ with modulation'
    assert jucerFile.plugin_manufacturer == 'tobanteAudio'
    assert jucerFile.plugin_manufacturer_code == 'toAu'
    assert jucerFile.plugin_code == 'tamq'
    assert jucerFile.plugin_au_exporter_profile == 'modEQAU'
    assert jucerFile.aax_identifier == "com.tobanteAudio.modEQ"
    assert jucerFile.vst3_category == "Analyzer,EQ,Fx"
    assert jucerFile.binary_data_namespace == 'TobanteAudioData'
    assert jucerFile.cpp_language_standard == '17'
    assert jucerFile.plugin_formats == "buildAU,buildStandalone,buildVST3"
    assert jucerFile.company_copyright == "GNU GENERAL PUBLIC LICENSE Version 3"
    assert jucerFile.display_splash_screen == '0'
    assert jucerFile.report_app_usage == '0'
    assert jucerFile.compiler_flag_schemes == 'NewScheme'
    assert jucerFile.project_line_feed == '\n'

    # SET COPYRIGHT, NO VALIDATION
    new_copyright = "NEW COPYRIGHT"
    jucerFile.company_copyright = new_copyright
    assert jucerFile.company_copyright == new_copyright
