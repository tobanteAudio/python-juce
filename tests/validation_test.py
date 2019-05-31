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
                             bool_to_integer_string)


def test_plugin_code_validation():
    # INVALID
    assert is_valid_plugin_code('taetl') == False  # Too long
    assert is_valid_plugin_code('test') == False   # No upper

    # VALID
    assert is_valid_plugin_code('toAu') == True
    assert is_valid_plugin_code('toAU') == True
    assert is_valid_plugin_code('Gthl') == True
    assert is_valid_plugin_code('hTFl') == True


def test_plugin_manufacturer_code_validation():
    # INVALID
    assert is_valid_plugin_manufacturer_code('taetl') == False  # Too long
    assert is_valid_plugin_manufacturer_code('test') == False   # No upper

    # VALID
    assert is_valid_plugin_manufacturer_code('toAu') == True
    assert is_valid_plugin_manufacturer_code('toAU') == True
    assert is_valid_plugin_manufacturer_code('Gthl') == True
    assert is_valid_plugin_manufacturer_code('hTFl') == True


def test_project_type_validation():

    # INVALID
    assert is_valid_project_type('application') == False
    assert is_valid_project_type('test-t') == False

    # VALID
    assert is_valid_project_type('audioplug') == True
    assert is_valid_project_type('consoleapp') == True
    assert is_valid_project_type('guiapp') == True
    assert is_valid_project_type('dll') == True
    assert is_valid_project_type('library') == True


def test_boolean_to_integer_string():

    assert bool_to_integer_string(True) == '1'
    assert bool_to_integer_string(False) == '0'
    assert bool_to_integer_string(1) == '1'
    assert bool_to_integer_string(0) == '0'


def test_boolean_validation():

    # INVALID
    assert is_valid_boolean('98') == False
    assert is_valid_boolean('test-t') == False

    # VALID
    assert is_valid_boolean(True) == True
    assert is_valid_boolean(False) == True
    assert is_valid_boolean(1) == True
    assert is_valid_boolean(0) == True


def test_namespace_validation():

    # INVALID
    assert is_valid_namespace('98') == False
    assert is_valid_namespace('test-t') == False
    assert is_valid_namespace('test t') == False

    # VALID
    assert is_valid_namespace("ns") == True
    assert is_valid_namespace("TobanteData") == True
    assert is_valid_namespace("DATA17") == True
    assert is_valid_namespace("foo") == True


def test_cpp_standard_validation():

    # INVALID
    assert is_valid_cpp_standard('98') == False
    assert is_valid_cpp_standard('2017') == False
    assert is_valid_cpp_standard("2020") == False
    assert is_valid_cpp_standard("20") == False

    # VALID
    assert is_valid_cpp_standard("11") == True
    assert is_valid_cpp_standard("14") == True
    assert is_valid_cpp_standard("17") == True
    assert is_valid_cpp_standard("latest") == True


def test_vst2_category_validation():

    # INVALID
    assert is_valid_vst2_category('Foo') == False
    assert is_valid_vst2_category('Cool Effect') == False
    assert is_valid_vst2_category("Fx") == False
    assert is_valid_vst2_category("Instrument") == False

    # VALID
    assert is_valid_vst2_category("kPlugCategUnknown") == True
    assert is_valid_vst2_category("kPlugCategEffect") == True
    assert is_valid_vst2_category("kPlugCategSynth") == True
    assert is_valid_vst2_category("kPlugCategAnalysis") == True
    assert is_valid_vst2_category("kPlugCategMastering") == True
    assert is_valid_vst2_category("kPlugCategSpacializer") == True
    assert is_valid_vst2_category("kPlugCategRoomFx") == True
    assert is_valid_vst2_category("kPlugSurroundFx") == True
    assert is_valid_vst2_category("kPlugCategRestoration") == True
    assert is_valid_vst2_category("kPlugCategOfflineProcess") == True
    assert is_valid_vst2_category("kPlugCategShell") == True
    assert is_valid_vst2_category("kPlugCategGenerator") == True


def test_vst3_category_validation():

    assert is_valid_vst3_category('Foo') == False
    assert is_valid_vst3_category('Cool Effect') == False

    assert is_valid_vst3_category("Fx") == True
    assert is_valid_vst3_category("Instrument") == True
    assert is_valid_vst3_category("Analyzer") == True
    assert is_valid_vst3_category("Delay") == True
    assert is_valid_vst3_category("Distortion") == True
    assert is_valid_vst3_category("Drum") == True
    assert is_valid_vst3_category("Dynamics") == True
    assert is_valid_vst3_category("EQ") == True
    assert is_valid_vst3_category("External") == True
    assert is_valid_vst3_category("Filter") == True
    assert is_valid_vst3_category("Generator") == True
    assert is_valid_vst3_category("Mastering") == True
    assert is_valid_vst3_category("Modulation") == True
    assert is_valid_vst3_category("Mono") == True
    assert is_valid_vst3_category("Network") == True
    assert is_valid_vst3_category("NoOfflineProcess") == True
    assert is_valid_vst3_category("OnlyOfflineProcess") == True
    assert is_valid_vst3_category("OnlyRT") == True
    assert is_valid_vst3_category("Pitch Shift") == True
    assert is_valid_vst3_category("Restoration") == True
    assert is_valid_vst3_category("Reverb") == True
    assert is_valid_vst3_category("Sampler") == True
    assert is_valid_vst3_category("Spatial") == True
    assert is_valid_vst3_category("Stereo") == True
    assert is_valid_vst3_category("Surround") == True
    assert is_valid_vst3_category("Synth") == True
    assert is_valid_vst3_category("Tools") == True
    assert is_valid_vst3_category("Up-Downmix") == True


def test_au_category_validation():

    # INVALID
    assert is_valid_au_category('Foo') == False
    assert is_valid_au_category('Cool Effect') == False
    assert is_valid_au_category("Fx") == False
    assert is_valid_au_category("Instrument") == False

    # VALID
    assert is_valid_au_category("kAudioUnitType_Effect") == True
    assert is_valid_au_category("kAudioUnitType_FormatConverter") == True
    assert is_valid_au_category("kAudioUnitType_Generator") == True
    assert is_valid_au_category("kAudioUnitType_MIDIProcessor") == True
    assert is_valid_au_category("kAudioUnitType_Mixer") == True
    assert is_valid_au_category("kAudioUnitType_MusicDevice") == True
    assert is_valid_au_category("kAudioUnitType_MusicEffect") == True
    assert is_valid_au_category("kAudioUnitType_OfflineEffect") == True
    assert is_valid_au_category("kAudioUnitType_Output") == True
    assert is_valid_au_category("kAudioUnitType_Panner") == True


def test_aax_category_validation():

    # INVALID
    assert is_valid_aax_category('Foo') == False
    assert is_valid_aax_category('Cool Effect') == False
    assert is_valid_aax_category("Fx") == False
    assert is_valid_aax_category("Instrument") == False

    # VALID
    assert is_valid_aax_category("AAX_ePlugInCategory_None") == True
    assert is_valid_aax_category("AAX_ePlugInCategory_EQ") == True
    assert is_valid_aax_category("AAX_ePlugInCategory_Dynamics") == True
    assert is_valid_aax_category("AAX_ePlugInCategory_PitchShift") == True
    assert is_valid_aax_category("AAX_ePlugInCategory_Reverb") == True
    assert is_valid_aax_category("AAX_ePlugInCategory_Delay") == True
    assert is_valid_aax_category("AAX_ePlugInCategory_Modulation") == True
    assert is_valid_aax_category("AAX_ePlugInCategory_Harmonic") == True
    assert is_valid_aax_category("AAX_ePlugInCategory_NoiseReduction") == True
    assert is_valid_aax_category("AAX_ePlugInCategory_Dither") == True
    assert is_valid_aax_category("AAX_ePlugInCategory_SoundField") == True
    assert is_valid_aax_category("AAX_ePlugInCategory_HWGenerators") == True
    assert is_valid_aax_category("AAX_ePlugInCategory_SWGenerators") == True
    assert is_valid_aax_category("AAX_ePlugInCategory_WrappedPlugin") == True
    assert is_valid_aax_category("AAX_EPlugInCategory_Effect") == True


def test_rtas_category_validation():

    # INVALID
    assert is_valid_rtas_category('Foo') == False
    assert is_valid_rtas_category('Cool Effect') == False
    assert is_valid_rtas_category("Fx") == False
    assert is_valid_rtas_category("Instrument") == False

    # VALID
    assert is_valid_rtas_category("ePlugInCategory_None") == True
    assert is_valid_rtas_category("ePlugInCategory_EQ") == True
    assert is_valid_rtas_category("ePlugInCategory_Dynamics") == True
    assert is_valid_rtas_category("ePlugInCategory_PitchShift") == True
    assert is_valid_rtas_category("ePlugInCategory_Reverb") == True
    assert is_valid_rtas_category("ePlugInCategory_Delay") == True
    assert is_valid_rtas_category("ePlugInCategory_Modulation") == True
    assert is_valid_rtas_category("ePlugInCategory_Harmonic") == True
    assert is_valid_rtas_category("ePlugInCategory_NoiseReduction") == True
    assert is_valid_rtas_category("ePlugInCategory_Dither") == True
    assert is_valid_rtas_category("ePlugInCategory_SoundField") == True
    assert is_valid_rtas_category("ePlugInCategory_HWGenerators") == True
    assert is_valid_rtas_category("ePlugInCategory_SWGenerators") == True
    assert is_valid_rtas_category("ePlugInCategory_WrappedPlugin") == True
    assert is_valid_rtas_category("ePlugInCategory_Effect") == True
