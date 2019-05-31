# pylint: skip-file

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


def test_line_feed_validation():
    # INVALID
    assert not is_valid_line_feed('\r')   # Too long
    assert not is_valid_line_feed('test')    # No upper

    # VALID
    assert is_valid_line_feed('\n')
    assert is_valid_line_feed('\r\n')


def test_plugin_code_validation():
    # INVALID
    assert is_valid_plugin_code('taetl') is False  # Too long
    assert is_valid_plugin_code('test') is False   # No upper

    # VALID
    assert is_valid_plugin_code('toAu')
    assert is_valid_plugin_code('toAU')
    assert is_valid_plugin_code('Gthl')
    assert is_valid_plugin_code('hTFl')


def test_plugin_manufacturer_code_validation():
    # INVALID
    assert is_valid_plugin_manufacturer_code('taetl') is False  # Too long
    assert is_valid_plugin_manufacturer_code('test') is False   # No upper

    # VALID
    assert is_valid_plugin_manufacturer_code('toAu')
    assert is_valid_plugin_manufacturer_code('toAU')
    assert is_valid_plugin_manufacturer_code('Gthl')
    assert is_valid_plugin_manufacturer_code('hTFl')


def test_project_type_validation():

    # INVALID
    assert is_valid_project_type('application') is False
    assert is_valid_project_type('test-t') is False

    # VALID
    assert is_valid_project_type('audioplug')
    assert is_valid_project_type('consoleapp')
    assert is_valid_project_type('guiapp')
    assert is_valid_project_type('dll')
    assert is_valid_project_type('library')


def test_boolean_to_integer_string():

    assert bool_to_integer_string(True) == '1'
    assert bool_to_integer_string(False) == '0'
    assert bool_to_integer_string(1) == '1'
    assert bool_to_integer_string(0) == '0'


def test_boolean_validation():

    # INVALID
    assert is_valid_boolean('98') is False
    assert is_valid_boolean('test-t') is False

    # VALID
    assert is_valid_boolean(True)
    assert is_valid_boolean(False)
    assert is_valid_boolean(1)
    assert is_valid_boolean(0)


def test_namespace_validation():

    # INVALID
    assert is_valid_namespace('98') is False
    assert is_valid_namespace('test-t') is False
    assert is_valid_namespace('test t') is False

    # VALID
    assert is_valid_namespace("ns")
    assert is_valid_namespace("TobanteData")
    assert is_valid_namespace("DATA17")
    assert is_valid_namespace("foo")


def test_cpp_standard_validation():

    # INVALID
    assert is_valid_cpp_standard('98') is False
    assert is_valid_cpp_standard('2017') is False
    assert is_valid_cpp_standard("2020") is False
    assert is_valid_cpp_standard("20") is False

    # VALID
    assert is_valid_cpp_standard("11")
    assert is_valid_cpp_standard("14")
    assert is_valid_cpp_standard("17")
    assert is_valid_cpp_standard("latest")


def test_vst2_category_validation():

    # INVALID
    assert is_valid_vst2_category('Foo') is False
    assert is_valid_vst2_category('Cool Effect') is False
    assert is_valid_vst2_category("Fx") is False
    assert is_valid_vst2_category("Instrument") is False

    # VALID
    assert is_valid_vst2_category("kPlugCategUnknown")
    assert is_valid_vst2_category("kPlugCategEffect")
    assert is_valid_vst2_category("kPlugCategSynth")
    assert is_valid_vst2_category("kPlugCategAnalysis")
    assert is_valid_vst2_category("kPlugCategMastering")
    assert is_valid_vst2_category("kPlugCategSpacializer")
    assert is_valid_vst2_category("kPlugCategRoomFx")
    assert is_valid_vst2_category("kPlugSurroundFx")
    assert is_valid_vst2_category("kPlugCategRestoration")
    assert is_valid_vst2_category("kPlugCategOfflineProcess")
    assert is_valid_vst2_category("kPlugCategShell")
    assert is_valid_vst2_category("kPlugCategGenerator")


def test_vst3_category_validation():

    assert is_valid_vst3_category('Foo') is False
    assert is_valid_vst3_category('Cool Effect') is False

    assert is_valid_vst3_category("Fx")
    assert is_valid_vst3_category("Instrument")
    assert is_valid_vst3_category("Analyzer")
    assert is_valid_vst3_category("Delay")
    assert is_valid_vst3_category("Distortion")
    assert is_valid_vst3_category("Drum")
    assert is_valid_vst3_category("Dynamics")
    assert is_valid_vst3_category("EQ")
    assert is_valid_vst3_category("External")
    assert is_valid_vst3_category("Filter")
    assert is_valid_vst3_category("Generator")
    assert is_valid_vst3_category("Mastering")
    assert is_valid_vst3_category("Modulation")
    assert is_valid_vst3_category("Mono")
    assert is_valid_vst3_category("Network")
    assert is_valid_vst3_category("NoOfflineProcess")
    assert is_valid_vst3_category("OnlyOfflineProcess")
    assert is_valid_vst3_category("OnlyRT")
    assert is_valid_vst3_category("Pitch Shift")
    assert is_valid_vst3_category("Restoration")
    assert is_valid_vst3_category("Reverb")
    assert is_valid_vst3_category("Sampler")
    assert is_valid_vst3_category("Spatial")
    assert is_valid_vst3_category("Stereo")
    assert is_valid_vst3_category("Surround")
    assert is_valid_vst3_category("Synth")
    assert is_valid_vst3_category("Tools")
    assert is_valid_vst3_category("Up-Downmix")


def test_au_category_validation():

    # INVALID
    assert is_valid_au_category('Foo') is False
    assert is_valid_au_category('Cool Effect') is False
    assert is_valid_au_category("Fx") is False
    assert is_valid_au_category("Instrument") is False

    # VALID
    assert is_valid_au_category("kAudioUnitType_Effect")
    assert is_valid_au_category("kAudioUnitType_FormatConverter")
    assert is_valid_au_category("kAudioUnitType_Generator")
    assert is_valid_au_category("kAudioUnitType_MIDIProcessor")
    assert is_valid_au_category("kAudioUnitType_Mixer")
    assert is_valid_au_category("kAudioUnitType_MusicDevice")
    assert is_valid_au_category("kAudioUnitType_MusicEffect")
    assert is_valid_au_category("kAudioUnitType_OfflineEffect")
    assert is_valid_au_category("kAudioUnitType_Output")
    assert is_valid_au_category("kAudioUnitType_Panner")


def test_aax_category_validation():

    # INVALID
    assert is_valid_aax_category('Foo') is False
    assert is_valid_aax_category('Cool Effect') is False
    assert is_valid_aax_category("Fx") is False
    assert is_valid_aax_category("Instrument") is False

    # VALID
    assert is_valid_aax_category("AAX_ePlugInCategory_None")
    assert is_valid_aax_category("AAX_ePlugInCategory_EQ")
    assert is_valid_aax_category("AAX_ePlugInCategory_Dynamics")
    assert is_valid_aax_category("AAX_ePlugInCategory_PitchShift")
    assert is_valid_aax_category("AAX_ePlugInCategory_Reverb")
    assert is_valid_aax_category("AAX_ePlugInCategory_Delay")
    assert is_valid_aax_category("AAX_ePlugInCategory_Modulation")
    assert is_valid_aax_category("AAX_ePlugInCategory_Harmonic")
    assert is_valid_aax_category("AAX_ePlugInCategory_NoiseReduction")
    assert is_valid_aax_category("AAX_ePlugInCategory_Dither")
    assert is_valid_aax_category("AAX_ePlugInCategory_SoundField")
    assert is_valid_aax_category("AAX_ePlugInCategory_HWGenerators")
    assert is_valid_aax_category("AAX_ePlugInCategory_SWGenerators")
    assert is_valid_aax_category("AAX_ePlugInCategory_WrappedPlugin")
    assert is_valid_aax_category("AAX_EPlugInCategory_Effect")


def test_rtas_category_validation():

    # INVALID
    assert is_valid_rtas_category('Foo') is False
    assert is_valid_rtas_category('Cool Effect') is False
    assert is_valid_rtas_category("Fx") is False
    assert is_valid_rtas_category("Instrument") is False

    # VALID
    assert is_valid_rtas_category("ePlugInCategory_None")
    assert is_valid_rtas_category("ePlugInCategory_EQ")
    assert is_valid_rtas_category("ePlugInCategory_Dynamics")
    assert is_valid_rtas_category("ePlugInCategory_PitchShift")
    assert is_valid_rtas_category("ePlugInCategory_Reverb")
    assert is_valid_rtas_category("ePlugInCategory_Delay")
    assert is_valid_rtas_category("ePlugInCategory_Modulation")
    assert is_valid_rtas_category("ePlugInCategory_Harmonic")
    assert is_valid_rtas_category("ePlugInCategory_NoiseReduction")
    assert is_valid_rtas_category("ePlugInCategory_Dither")
    assert is_valid_rtas_category("ePlugInCategory_SoundField")
    assert is_valid_rtas_category("ePlugInCategory_HWGenerators")
    assert is_valid_rtas_category("ePlugInCategory_SWGenerators")
    assert is_valid_rtas_category("ePlugInCategory_WrappedPlugin")
    assert is_valid_rtas_category("ePlugInCategory_Effect")
