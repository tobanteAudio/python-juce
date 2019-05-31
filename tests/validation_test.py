from juce.validation import (valid_vst3_category, valid_vst2_category,
                             valid_au_category, valid_aax_category, valid_rtas_category)


def test_vst2_category_validation():

    # INVALID
    assert valid_vst2_category('Foo') == False
    assert valid_vst2_category('Cool Effect') == False
    assert valid_vst2_category("Fx") == False
    assert valid_vst2_category("Instrument") == False

    # VALID
    assert valid_vst2_category("kPlugCategUnknown") == True
    assert valid_vst2_category("kPlugCategEffect") == True
    assert valid_vst2_category("kPlugCategSynth") == True
    assert valid_vst2_category("kPlugCategAnalysis") == True
    assert valid_vst2_category("kPlugCategMastering") == True
    assert valid_vst2_category("kPlugCategSpacializer") == True
    assert valid_vst2_category("kPlugCategRoomFx") == True
    assert valid_vst2_category("kPlugSurroundFx") == True
    assert valid_vst2_category("kPlugCategRestoration") == True
    assert valid_vst2_category("kPlugCategOfflineProcess") == True
    assert valid_vst2_category("kPlugCategShell") == True
    assert valid_vst2_category("kPlugCategGenerator") == True


def test_vst3_category_validation():

    assert valid_vst3_category('Foo') == False
    assert valid_vst3_category('Cool Effect') == False

    assert valid_vst3_category("Fx") == True
    assert valid_vst3_category("Instrument") == True
    assert valid_vst3_category("Analyzer") == True
    assert valid_vst3_category("Delay") == True
    assert valid_vst3_category("Distortion") == True
    assert valid_vst3_category("Drum") == True
    assert valid_vst3_category("Dynamics") == True
    assert valid_vst3_category("EQ") == True
    assert valid_vst3_category("External") == True
    assert valid_vst3_category("Filter") == True
    assert valid_vst3_category("Generator") == True
    assert valid_vst3_category("Mastering") == True
    assert valid_vst3_category("Modulation") == True
    assert valid_vst3_category("Mono") == True
    assert valid_vst3_category("Network") == True
    assert valid_vst3_category("NoOfflineProcess") == True
    assert valid_vst3_category("OnlyOfflineProcess") == True
    assert valid_vst3_category("OnlyRT") == True
    assert valid_vst3_category("Pitch Shift") == True
    assert valid_vst3_category("Restoration") == True
    assert valid_vst3_category("Reverb") == True
    assert valid_vst3_category("Sampler") == True
    assert valid_vst3_category("Spatial") == True
    assert valid_vst3_category("Stereo") == True
    assert valid_vst3_category("Surround") == True
    assert valid_vst3_category("Synth") == True
    assert valid_vst3_category("Tools") == True
    assert valid_vst3_category("Up-Downmix") == True


def test_au_category_validation():

    # INVALID
    assert valid_au_category('Foo') == False
    assert valid_au_category('Cool Effect') == False
    assert valid_au_category("Fx") == False
    assert valid_au_category("Instrument") == False

    # VALID
    assert valid_au_category("kAudioUnitType_Effect") == True
    assert valid_au_category("kAudioUnitType_FormatConverter") == True
    assert valid_au_category("kAudioUnitType_Generator") == True
    assert valid_au_category("kAudioUnitType_MIDIProcessor") == True
    assert valid_au_category("kAudioUnitType_Mixer") == True
    assert valid_au_category("kAudioUnitType_MusicDevice") == True
    assert valid_au_category("kAudioUnitType_MusicEffect") == True
    assert valid_au_category("kAudioUnitType_OfflineEffect") == True
    assert valid_au_category("kAudioUnitType_Output") == True
    assert valid_au_category("kAudioUnitType_Panner") == True


def test_aax_category_validation():

    # INVALID
    assert valid_aax_category('Foo') == False
    assert valid_aax_category('Cool Effect') == False
    assert valid_aax_category("Fx") == False
    assert valid_aax_category("Instrument") == False

    # VALID
    assert valid_aax_category("AAX_ePlugInCategory_None") == True
    assert valid_aax_category("AAX_ePlugInCategory_EQ") == True
    assert valid_aax_category("AAX_ePlugInCategory_Dynamics") == True
    assert valid_aax_category("AAX_ePlugInCategory_PitchShift") == True
    assert valid_aax_category("AAX_ePlugInCategory_Reverb") == True
    assert valid_aax_category("AAX_ePlugInCategory_Delay") == True
    assert valid_aax_category("AAX_ePlugInCategory_Modulation") == True
    assert valid_aax_category("AAX_ePlugInCategory_Harmonic") == True
    assert valid_aax_category("AAX_ePlugInCategory_NoiseReduction") == True
    assert valid_aax_category("AAX_ePlugInCategory_Dither") == True
    assert valid_aax_category("AAX_ePlugInCategory_SoundField") == True
    assert valid_aax_category("AAX_ePlugInCategory_HWGenerators") == True
    assert valid_aax_category("AAX_ePlugInCategory_SWGenerators") == True
    assert valid_aax_category("AAX_ePlugInCategory_WrappedPlugin") == True
    assert valid_aax_category("AAX_EPlugInCategory_Effect") == True


def test_rtas_category_validation():

    # INVALID
    assert valid_rtas_category('Foo') == False
    assert valid_rtas_category('Cool Effect') == False
    assert valid_rtas_category("Fx") == False
    assert valid_rtas_category("Instrument") == False

    # VALID
    assert valid_rtas_category("ePlugInCategory_None") == True
    assert valid_rtas_category("ePlugInCategory_EQ") == True
    assert valid_rtas_category("ePlugInCategory_Dynamics") == True
    assert valid_rtas_category("ePlugInCategory_PitchShift") == True
    assert valid_rtas_category("ePlugInCategory_Reverb") == True
    assert valid_rtas_category("ePlugInCategory_Delay") == True
    assert valid_rtas_category("ePlugInCategory_Modulation") == True
    assert valid_rtas_category("ePlugInCategory_Harmonic") == True
    assert valid_rtas_category("ePlugInCategory_NoiseReduction") == True
    assert valid_rtas_category("ePlugInCategory_Dither") == True
    assert valid_rtas_category("ePlugInCategory_SoundField") == True
    assert valid_rtas_category("ePlugInCategory_HWGenerators") == True
    assert valid_rtas_category("ePlugInCategory_SWGenerators") == True
    assert valid_rtas_category("ePlugInCategory_WrappedPlugin") == True
    assert valid_rtas_category("ePlugInCategory_Effect") == True
