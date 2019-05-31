import os

import pytest

from juce.projucer import JucerFile


def test_write_to_file():
    original_path = 'tests/assets/modEQ.jucer'
    jucerFile = JucerFile(original_path)

    out_dir = 'tests/output/'
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)

    out1 = 'output.jucer'
    out2 = 'output2.jucer'
    jucerFile.version = '1.0.0'
    jucerFile.path = out_dir + out1
    jucerFile.save()
    jucerFile.save_as(out_dir + out2)

    assert os.path.isfile(out_dir + out1) == True
    assert os.path.isfile(out_dir + out2) == True


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

    # Set id, No validation
    new_id = "jWny5B"
    jucerFile.id = new_id
    assert jucerFile.id == new_id

    # Set name, No validation
    new_name = "newName"
    jucerFile.name = new_name
    assert jucerFile.name == new_name

    # Set version, No validation
    new_version = "1.0.0"
    jucerFile.version = new_version
    assert jucerFile.version == new_version

    # Set jucer version, No validation
    new_jucer_version = "6.0.0"
    jucerFile.jucer_version = new_jucer_version
    assert jucerFile.jucer_version == new_jucer_version

    # Set path, No validation
    new_path = "somepath/test.jucer"
    jucerFile.path = new_path
    assert jucerFile.path == new_path

    # Set company, no validation
    new_company = "Test Company"
    jucerFile.company = new_company
    assert jucerFile.company == new_company

    # Set company website, no validation
    new_website = "https://example.com"
    jucerFile.company_website = new_website
    assert jucerFile.company_website == new_website

    # Set company email, no validation
    new_email = "example@example.com"
    jucerFile.company_email = new_email
    assert jucerFile.company_email == new_email

    # Set bundle identifier, no validation
    new_bundle = "com.test.testplugin"
    jucerFile.bundle_identifier = new_bundle
    assert jucerFile.bundle_identifier == new_bundle

    # Set plugin name, no validation
    new_plugin_name = "PluginName"
    jucerFile.plugin_name = new_plugin_name
    assert jucerFile.plugin_name == new_plugin_name

    # Set plugin description, no validation
    new_plugin_description = "Long long long text"
    jucerFile.plugin_description = new_plugin_description
    assert jucerFile.plugin_description == new_plugin_description

    # Set plugin manufacturer, no validation
    new_plugin_manufacturer = "Evil Corp"
    jucerFile.plugin_manufacturer = new_plugin_manufacturer
    assert jucerFile.plugin_manufacturer == new_plugin_manufacturer

    # Set copyright, no validation
    new_copyright = "NEW COPYRIGHT"
    jucerFile.company_copyright = new_copyright
    assert jucerFile.company_copyright == new_copyright

    # Set binary data namespace, with validation
    new_namespace = "NEWNAMESPACE"
    jucerFile.binary_data_namespace = new_namespace
    assert jucerFile.binary_data_namespace == new_namespace

    # Set plugin code, with validation
    new_plugin_code = "taMq"
    jucerFile.plugin_code = new_plugin_code
    assert jucerFile.plugin_code == new_plugin_code
    jucerFile.plugin_code = 'new_plugin_code'           # Fail
    assert jucerFile.plugin_code == new_plugin_code

    # Set plugin code, with validation
    new_plugin_manufacturer_code = "taMq"
    jucerFile.plugin_manufacturer_code = new_plugin_manufacturer_code
    assert jucerFile.plugin_manufacturer_code == new_plugin_manufacturer_code
    jucerFile.plugin_manufacturer_code = 'new_plugin_manufacturer_code'           # Fail
    assert jucerFile.plugin_manufacturer_code == new_plugin_manufacturer_code

    # Set project_type, with validation
    new_project_type = "dll"
    jucerFile.project_type = new_project_type
    assert jucerFile.project_type == new_project_type
    jucerFile.project_type = 'new_project_type'           # Fail
    assert jucerFile.project_type == new_project_type

    # Set splash screen, with validation
    jucerFile.display_splash_screen = True
    assert jucerFile.display_splash_screen == '1'
    jucerFile.display_splash_screen = False
    assert jucerFile.display_splash_screen == '0'

    # Set report app usage, with validation
    jucerFile.report_app_usage = True
    assert jucerFile.report_app_usage == '1'
    jucerFile.report_app_usage = False
    assert jucerFile.report_app_usage == '0'


def test_modEQ_project_attributes_with_exceptions():
    path = 'tests/assets/modEQ.jucer'
    jucerFile = JucerFile(path)
    jucerFile.silent_validation = False

    with pytest.raises(ValueError) as excinfo:
        jucerFile.plugin_code = 'new_plugin_manufacturer_code'
    assert "Attribute validation failed" in str(excinfo.value)
    excinfo = None

    with pytest.raises(ValueError) as excinfo:
        jucerFile.plugin_manufacturer_code = 'new_plugin_manufacturer_code'
    assert "Attribute validation failed" in str(excinfo.value)
    excinfo = None

    with pytest.raises(ValueError) as excinfo:
        jucerFile.cpp_language_standard = 'new_plugin_manufacturer_code'
    assert "Attribute validation failed" in str(excinfo.value)
    excinfo = None

    with pytest.raises(ValueError) as excinfo:
        jucerFile.project_type = 'new_plugin_manufacturer_code'
    assert "Attribute validation failed" in str(excinfo.value)
    excinfo = None

    with pytest.raises(ValueError) as excinfo:
        jucerFile.display_splash_screen = 'new_plugin_manufacturer_code'
    assert "Attribute validation failed" in str(excinfo.value)
    excinfo = None

    with pytest.raises(ValueError) as excinfo:
        jucerFile.report_app_usage = 'new_plugin_manufacturer_code'
    assert "Attribute validation failed" in str(excinfo.value)
    excinfo = None
