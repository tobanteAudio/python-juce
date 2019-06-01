# pylint: skip-file

import os

import pytest

from juce.projucer.jucer_file import JucerFile

GUI_APP_PROPTERY_RESULTS = {
    "path": 'tests/assets/GuiApp.jucer',
    "u_id": 'hgSXn0',
    "name": 'GuiApp',
    "project_type": 'guiapp',
    "cpp_language_standard": 'latest',
    "jucer_version": '5.4.3',
    'defines': 'TOBANTETEST=1\nTOBANTEAUDIO=1,TOBANTEAUDIO2=1'
}

MODEQ_PROPTERY_RESULTS = {
    "path": 'tests/assets/modEQ.jucer',
    "u_id": 'jWny5A',
    "name": 'modEQ',
    "project_type": 'audioplug',
    "jucer_version": '5.4.3',
    "version": '0.4.0',
    "company": 'tobanteAudio',
    "company_website": 'https://github.com/tobanteAudio',
    "company_email": 'tobanteAudio@gmail.com',
    "bundle_identifier": "com.tobanteAudio.modEQ",
    "plugin_name": 'modEQ',
    "plugin_description": 'EQ with modulation',
    "manufacturer": 'tobanteAudio',
    "manufacturer_code": 'toAu',
    "plugin_code": 'tamq',
    "au_profile": 'modEQAU',
    "aax_identifier": "com.tobanteAudio.modEQ",
    "vst3_category": "Analyzer,EQ,Fx",
    "binary_data_namespace": 'TobanteAudioData',
    "cpp_language_standard": '17',
    "plugin_formats": "buildAU,buildStandalone,buildVST3",
    "company_copyright": "GNU GENERAL PUBLIC LICENSE Version 3",
    "display_splash_screen": '0',
    "report_app_usage": '0',
    "compiler_flag_schemes": 'NewScheme',
    'defines': None,
    "project_line_feed": '\n'
}

PROPTERY_RESULTS = [GUI_APP_PROPTERY_RESULTS, MODEQ_PROPTERY_RESULTS]


def none_or(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return None


def table_tests():
    for test in PROPTERY_RESULTS:
        project_properties(test)


def project_properties(test):
    path = test['path']
    jF = JucerFile(path)

    # Properties (get)
    assert jF.path == none_or(test, "path")
    assert jF.u_id == none_or(test, "u_id")
    assert jF.name == none_or(test, "name")
    assert jF.project_type == none_or(test, "project_type")
    assert jF.jucer_version == none_or(test, "jucer_version")
    assert jF.version == none_or(test, "version")
    assert jF.company == none_or(test, "company")
    assert jF.company_website == none_or(test, "company_website")
    assert jF.company_email == none_or(test, "company_email")
    assert jF.bundle_identifier == none_or(test, "bundle_identifier")
    assert jF.plugin_name == none_or(test, "plugin_name")
    assert jF.plugin_description == none_or(test, "plugin_description")
    assert jF.plugin_manufacturer == none_or(test, "manufacturer")
    assert jF.plugin_manufacturer_code == none_or(test, "manufacturer_code")
    assert jF.plugin_code == none_or(test, "plugin_code")
    assert jF.plugin_au_exporter_profile == none_or(test, "au_profile")
    assert jF.aax_identifier == none_or(test, "aax_identifier")
    assert jF.vst3_category == none_or(test, "vst3_category")
    assert jF.binary_data_namespace == none_or(test, "binary_data_namespace")
    assert jF.cpp_language_standard == none_or(test, "cpp_language_standard")
    assert jF.plugin_formats == none_or(test, "plugin_formats")
    assert jF.company_copyright == none_or(test, "company_copyright")
    assert jF.display_splash_screen == none_or(test, "display_splash_screen")
    assert jF.report_app_usage == none_or(test, "report_app_usage")
    assert jF.compiler_flag_schemes == none_or(test, "compiler_flag_schemes")
    assert jF.project_line_feed == none_or(test, "project_line_feed")
    assert jF.defines == none_or(test, "defines")


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

    assert os.path.isfile(out_dir + out1)
    assert os.path.isfile(out_dir + out2)


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


def test_set_attributes():
    path = 'tests/assets/modEQ.jucer'
    jucerFile = JucerFile(path)

    assert jucerFile.silent_validation

    # Set id, No validation
    new_id = "jWny5B"
    jucerFile.u_id = new_id
    assert jucerFile.u_id == new_id

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

    # Set AU profile
    new_au_profile = "profile"
    jucerFile.plugin_au_exporter_profile = new_au_profile
    assert jucerFile.plugin_au_exporter_profile == new_au_profile

    # Set AAX identifier
    new_aax_id = "profile"
    jucerFile.aax_identifier = new_aax_id
    assert jucerFile.aax_identifier == new_aax_id

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
    new_manufacturer_code = "taMq"
    jucerFile.plugin_manufacturer_code = new_manufacturer_code
    assert jucerFile.plugin_manufacturer_code == new_manufacturer_code
    jucerFile.plugin_manufacturer_code = 'new_manufacturer_code'  # Fail
    assert jucerFile.plugin_manufacturer_code == new_manufacturer_code

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

    # Set line feed, with validation
    new_line_feed = "\r\n"
    jucerFile.project_line_feed = new_line_feed
    assert jucerFile.project_line_feed == new_line_feed
    jucerFile.project_line_feed = 'new_line_feed'           # Fail
    assert jucerFile.project_line_feed == new_line_feed


def test_set_attributes_with_exceptions():
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

    with pytest.raises(ValueError) as excinfo:
        jucerFile.project_line_feed = 'new_plugin_manufacturer_code'
    assert "Attribute validation failed" in str(excinfo.value)
    excinfo = None

    with pytest.raises(ValueError) as excinfo:
        jucerFile.binary_data_namespace = 'BAD NAMESPACE'
    assert "Attribute validation failed" in str(excinfo.value)
    excinfo = None
