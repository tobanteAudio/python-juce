# pylint: skip-file

import os

import pytest

from juce.projucer import JucerFile

GUI_APP_PROPTERY_RESULTS = {
    "path": 'tests/assets/GuiApp.jucer',
    "u_id": 'hgSXn0',
    "name": 'GuiApp',
    "project_type": 'guiapp',
    "cpp_language_standard": 'latest',
    "jucer_version": '5.4.3',
    'defines': 'TOBANTETEST=1\nTOBANTEAUDIO=1,TOBANTEAUDIO2=1',
    "module_count": 12
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
    "project_line_feed": '\n',
    'module_count': 16
}

PROPTERY_RESULTS = [GUI_APP_PROPTERY_RESULTS, MODEQ_PROPTERY_RESULTS]


def none_or(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return None


# PATH
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', 'tests/assets/modEQ.jucer'),
    ('tests/assets/GuiApp.jucer', 'tests/assets/GuiApp.jucer'),
])
def test_jucer_file_path(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.path == expected


# ID
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', 'jWny5A'),
    ('tests/assets/GuiApp.jucer', 'hgSXn0'),
])
def test_jucer_file_id(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.u_id == expected


# NAME
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', 'modEQ'),
    ('tests/assets/GuiApp.jucer', 'GuiApp'),
])
def test_jucer_file_name(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.name == expected


# PROJECT TYPE
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', 'audioplug'),
    ('tests/assets/GuiApp.jucer', 'guiapp'),
])
def test_jucer_file_project_type(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.project_type == expected


# JUCER VERSION
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', '5.4.3'),
    ('tests/assets/GuiApp.jucer', '5.4.3'),
])
def test_jucer_file_jucer_version(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.jucer_version == expected


# VERSION
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', '0.4.0'),
    ('tests/assets/GuiApp.jucer', None),
])
def test_jucer_file_version(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.version == expected


# COMPANY
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', 'tobanteAudio'),
    ('tests/assets/GuiApp.jucer', None),
])
def test_jucer_file_company(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.company == expected


# COMPANY WEBSITE
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', 'https://github.com/tobanteAudio'),
    ('tests/assets/GuiApp.jucer', None),
])
def test_jucer_file_company_website(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.company_website == expected


# COMPANY EMAIL
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', 'tobanteAudio@gmail.com'),
    ('tests/assets/GuiApp.jucer', None),
])
def test_jucer_file_company_email(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.company_email == expected


# COMPANY COPYRIGHT
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', 'GNU GENERAL PUBLIC LICENSE Version 3'),
    ('tests/assets/GuiApp.jucer', None),
])
def test_jucer_file_company_copyright(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.company_copyright == expected


# BUNDLE IDENTIFIER
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', 'com.tobanteAudio.modEQ'),
    ('tests/assets/GuiApp.jucer', None),
])
def test_jucer_file_bundle_identifier(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.bundle_identifier == expected


# PLUGIN NAME
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', 'modEQ'),
    ('tests/assets/GuiApp.jucer', None),
])
def test_jucer_file_plugin_name(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.plugin_name == expected


# PLUGIN DESCRIPTION
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', 'EQ with modulation'),
    ('tests/assets/GuiApp.jucer', None),
])
def test_jucer_file_plugin_description(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.plugin_description == expected


# PLUGIN MANUFACTURER
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', 'tobanteAudio'),
    ('tests/assets/GuiApp.jucer', None),
])
def test_jucer_file_plugin_manufacturer(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.plugin_manufacturer == expected


# PLUGIN MANUFACTURER CODE
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', 'toAu'),
    ('tests/assets/GuiApp.jucer', None),
])
def test_jucer_file_plugin_manufacturer_code(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.plugin_manufacturer_code == expected


# PLUGIN CODE
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', 'tamq'),
    ('tests/assets/GuiApp.jucer', None),
])
def test_jucer_file_plugin_code(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.plugin_code == expected


# PLUGIN AU PROFILE
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', 'modEQAU'),
    ('tests/assets/GuiApp.jucer', None),
])
def test_jucer_file_plugin_au_exporter_profile(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.plugin_au_exporter_profile == expected


# PLUGIN AAX IDENTIFIER
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', 'com.tobanteAudio.modEQ'),
    ('tests/assets/GuiApp.jucer', None),
])
def test_jucer_file_aax_identifier(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.aax_identifier == expected


# PLUGIN VST3 CATEGORY
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', 'Analyzer,EQ,Fx'),
    ('tests/assets/GuiApp.jucer', None),
])
def test_jucer_file_vst3_category(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.vst3_category == expected


# BINARY DATA NAMESPACE
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', 'TobanteAudioData'),
    ('tests/assets/GuiApp.jucer', None),
])
def test_jucer_file_binary_data_namespace(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.binary_data_namespace == expected


# C++ STANDARD
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', '17'),
    ('tests/assets/GuiApp.jucer', 'latest'),
])
def test_jucer_file_cpp_language_standard(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.cpp_language_standard == expected


# PLUGIN FORMATS
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', 'buildAU,buildStandalone,buildVST3'),
    ('tests/assets/GuiApp.jucer', None),
])
def test_jucer_file_plugin_formats(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.plugin_formats == expected


# DISPLAY SPLASH SCREEN
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', '0'),
    ('tests/assets/GuiApp.jucer', None),
])
def test_jucer_file_display_splash_screen(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.display_splash_screen == expected


# REPORT APP USAGE
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', '0'),
    ('tests/assets/GuiApp.jucer', None),
])
def test_jucer_file_report_app_usage(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.report_app_usage == expected


# COMPILER FLAG SCHEMES
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', 'NewScheme'),
    ('tests/assets/GuiApp.jucer', None),
])
def test_jucer_file_compiler_flag_schemes(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.compiler_flag_schemes == expected


# LINE FEED
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', '\n'),
    ('tests/assets/GuiApp.jucer', None),
])
def test_jucer_file_project_line_feed(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.project_line_feed == expected


# DEFINES
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', None),
    ('tests/assets/GuiApp.jucer', 'TOBANTETEST=1\nTOBANTEAUDIO=1,TOBANTEAUDIO2=1'),
])
def test_jucer_file_defines(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert jucer_file.defines == expected


# MODULES LENGTH
@pytest.mark.parametrize("test_case, expected", [
    ('tests/assets/modEQ.jucer', 16),
    ('tests/assets/GuiApp.jucer', 12),
])
def test_jucer_file_modules_length(test_case, expected):
    jucer_file = JucerFile(test_case)
    assert len(jucer_file.modules) == expected


# def test_files():
#     for test in PROPTERY_RESULTS:
#         path = test['path']
#         jF = JucerFile(path)

#         # Properties (get)
#         assert len(jF.modules) == test["module_count"]


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
