# pylint: skip-file
import pytest

from juce.validation import (is_valid_vst3_category,
                             is_valid_project_type,
                             is_valid_vst2_category,
                             is_valid_au_category,
                             is_valid_aax_category,
                             is_valid_rtas_category,
                             is_valid_cpp_standard,
                             is_valid_namespace,
                             is_valid_boolean,
                             is_valid_plugin_manufacturer_code,
                             is_valid_plugin_code,
                             is_valid_line_feed,
                             bool_to_integer_string)


@pytest.mark.parametrize("test_case, expected", [
    ('\r', False),
    ('test', False),
    ('\n', True),
    ('\r\n', True),
])
def test_line_feed_validation(test_case, expected):
    assert is_valid_line_feed(test_case) == expected


@pytest.mark.parametrize("test_case, expected", [
    ('taetl', False),
    ('test', False),
    ('toAu', True),
    ('toAU', True),
    ('Gthl', True),
    ('hTFl', True),
])
def test_plugin_code_validation(test_case, expected):
    assert is_valid_plugin_code(test_case) == expected


@pytest.mark.parametrize("test_case, expected", [
    ('taetl', False),
    ('test', False),
    ('toAu', True),
    ('toAU', True),
    ('Gthl', True),
    ('hTFl', True),
])
def test_plugin_manufacturer_code_validation(test_case, expected):
    assert is_valid_plugin_manufacturer_code(test_case) == expected


@pytest.mark.parametrize("test_case, expected", [
    ('application', False),
    ('test-t', False),
    ('audioplug', True),
    ('consoleapp', True),
    ('guiapp', True),
    ('dll', True),
    ('library', True),
])
def test_project_type_validation(test_case, expected):
    assert is_valid_project_type(test_case) == expected


@pytest.mark.parametrize("test_case, expected", [
    (True, '1'),
    (False, '0'),
    (1, '1'),
    (0, '0'),
])
def test_boolean_to_integer_string(test_case, expected):
    assert bool_to_integer_string(test_case) == expected


@pytest.mark.parametrize("test_case, expected", [
    ('98', False),
    ('test-t', False),
    (True, True),
    (False, True),
    (1, True),
    (0, True),
])
def test_boolean_validation(test_case, expected):
    assert is_valid_boolean(test_case) == expected


@pytest.mark.parametrize("test_case, expected", [
    ('98', False),
    ('test-t', False),
    ('test t', False),
    ("ns", True),
    ("TobanteData", True),
    ("DATA17", True),
    ("foo", True),
])
def test_namespace_validation(test_case, expected):
    assert is_valid_namespace(test_case) == expected


@pytest.mark.parametrize("test_case, expected", [
    ('98', False),
    ('2017', False),
    ("2020", False),
    ("20", False),
    ("11", True),
    ("14", True),
    ("17", True),
    ("latest", True),
])
def test_cpp_standard_validation(test_case, expected):
    assert is_valid_cpp_standard(test_case) == expected


@pytest.mark.parametrize("test_case, expected", [
    ('Foo', False),
    ('Cool Effect', False),
    ("Fx", False),
    ("Instrument", False),
    ("kPlugCategUnknown", True),
    ("kPlugCategEffect", True),
    ("kPlugCategSynth", True),
    ("kPlugCategAnalysis", True),
    ("kPlugCategMastering", True),
    ("kPlugCategSpacializer", True),
    ("kPlugCategRoomFx", True),
    ("kPlugSurroundFx", True),
    ("kPlugCategRestoration", True),
    ("kPlugCategOfflineProcess", True),
    ("kPlugCategShell", True),
    ("kPlugCategGenerator", True),
])
def test_vst2_category_validation(test_case, expected):
    assert is_valid_vst2_category(test_case) == expected


@pytest.mark.parametrize("test_case, expected", [
    ('Foo', False),
    ('Cool Effect', False),
    ("Fx", True),
    ("Instrument", True),
    ("Analyzer", True),
    ("Delay", True),
    ("Distortion", True),
    ("Drum", True),
    ("Dynamics", True),
    ("EQ", True),
    ("External", True),
    ("Filter", True),
    ("Generator", True),
    ("Mastering", True),
    ("Modulation", True),
    ("Mono", True),
    ("Network", True),
    ("NoOfflineProcess", True),
    ("OnlyOfflineProcess", True),
    ("OnlyRT", True),
    ("Pitch Shift", True),
    ("Restoration", True),
    ("Reverb", True),
    ("Sampler", True),
    ("Spatial", True),
    ("Stereo", True),
    ("Surround", True),
    ("Synth", True),
    ("Tools", True),
    ("Up-Downmix", True),
])
def test_vst3_category_validation(test_case, expected):
    assert is_valid_vst3_category(test_case) == expected


@pytest.mark.parametrize("test_case, expected", [
    ('Foo', False),
    ('Cool Effect', False),
    ("Fx", False),
    ("Instrument", False),
    ("kAudioUnitType_Effect", True),
    ("kAudioUnitType_FormatConverter", True),
    ("kAudioUnitType_Generator", True),
    ("kAudioUnitType_MIDIProcessor", True),
    ("kAudioUnitType_Mixer", True),
    ("kAudioUnitType_MusicDevice", True),
    ("kAudioUnitType_MusicEffect", True),
    ("kAudioUnitType_OfflineEffect", True),
    ("kAudioUnitType_Output", True),
    ("kAudioUnitType_Panner", True),
])
def test_au_category_validation(test_case, expected):
    assert is_valid_au_category(test_case) == expected


@pytest.mark.parametrize("test_case, expected", [
    ('Foo', False),
    ('Cool Effect', False),
    ("Fx", False),
    ("Instrument", False),
    ("AAX_ePlugInCategory_None", True),
    ("AAX_ePlugInCategory_EQ", True),
    ("AAX_ePlugInCategory_Dynamics", True),
    ("AAX_ePlugInCategory_PitchShift", True),
    ("AAX_ePlugInCategory_Reverb", True),
    ("AAX_ePlugInCategory_Delay", True),
    ("AAX_ePlugInCategory_Modulation", True),
    ("AAX_ePlugInCategory_Harmonic", True),
    ("AAX_ePlugInCategory_NoiseReduction", True),
    ("AAX_ePlugInCategory_Dither", True),
    ("AAX_ePlugInCategory_SoundField", True),
    ("AAX_ePlugInCategory_HWGenerators", True),
    ("AAX_ePlugInCategory_SWGenerators", True),
    ("AAX_ePlugInCategory_WrappedPlugin", True),
    ("AAX_EPlugInCategory_Effect", True),
])
def test_aax_category_validation(test_case, expected):
    assert is_valid_aax_category(test_case) == expected


@pytest.mark.parametrize("test_case, expected", [
    ('Foo', False),
    ('Cool Effect', False),
    ("Fx", False),
    ("Instrument", False),
    ("ePlugInCategory_None", True),
    ("ePlugInCategory_EQ", True),
    ("ePlugInCategory_Dynamics", True),
    ("ePlugInCategory_PitchShift", True),
    ("ePlugInCategory_Reverb", True),
    ("ePlugInCategory_Delay", True),
    ("ePlugInCategory_Modulation", True),
    ("ePlugInCategory_Harmonic", True),
    ("ePlugInCategory_NoiseReduction", True),
    ("ePlugInCategory_Dither", True),
    ("ePlugInCategory_SoundField", True),
    ("ePlugInCategory_HWGenerators", True),
    ("ePlugInCategory_SWGenerators", True),
    ("ePlugInCategory_WrappedPlugin", True),
    ("ePlugInCategory_Effect", True),
])
def test_rtas_category_validation(test_case, expected):
    assert is_valid_rtas_category(test_case) == expected
