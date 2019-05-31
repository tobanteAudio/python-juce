"""Functions for validating jucer project attributes"""

# PROJECT TYPES
PROJECT_TYPES = ["guiapp", "consoleapp", "library", "dll", "audioplug"]

# C++
CPP_STANDARDS = ['11', '14', '17', 'latest']

# PLUGIN CATEGORIES
VST2_CATEGORIES = ["kPlugCategUnknown",
                   "kPlugCategEffect",
                   "kPlugCategSynth",
                   "kPlugCategAnalysis",
                   "kPlugCategMastering",
                   "kPlugCategSpacializer",
                   "kPlugCategRoomFx",
                   "kPlugSurroundFx",
                   "kPlugCategRestoration",
                   "kPlugCategOfflineProcess",
                   "kPlugCategShell",
                   "kPlugCategGenerator"]

VST3_CATEGORIES = ["Fx",
                   "Instrument",
                   "Analyzer",
                   "Delay",
                   "Distortion",
                   "Drum",
                   "Dynamics",
                   "EQ",
                   "External",
                   "Filter",
                   "Generator",
                   "Mastering",
                   "Modulation",
                   "Mono",
                   "Network",
                   "NoOfflineProcess",
                   "OnlyOfflineProcess",
                   "OnlyRT",
                   "Pitch Shift",
                   "Restoration",
                   "Reverb",
                   "Sampler",
                   "Spatial",
                   "Stereo",
                   "Surround",
                   "Synth",
                   "Tools",
                   "Up-Downmix"]

AU_CATEGORIES = ["kAudioUnitType_Effect",
                 "kAudioUnitType_FormatConverter",
                 "kAudioUnitType_Generator",
                 "kAudioUnitType_MIDIProcessor",
                 "kAudioUnitType_Mixer",
                 "kAudioUnitType_MusicDevice",
                 "kAudioUnitType_MusicEffect",
                 "kAudioUnitType_OfflineEffect",
                 "kAudioUnitType_Output",
                 "kAudioUnitType_Panner"]

AAX_CATEGORIES = ["AAX_ePlugInCategory_None",
                  "AAX_ePlugInCategory_EQ",
                  "AAX_ePlugInCategory_Dynamics",
                  "AAX_ePlugInCategory_PitchShift",
                  "AAX_ePlugInCategory_Reverb",
                  "AAX_ePlugInCategory_Delay",
                  "AAX_ePlugInCategory_Modulation",
                  "AAX_ePlugInCategory_Harmonic",
                  "AAX_ePlugInCategory_NoiseReduction",
                  "AAX_ePlugInCategory_Dither",
                  "AAX_ePlugInCategory_SoundField",
                  "AAX_ePlugInCategory_HWGenerators",
                  "AAX_ePlugInCategory_SWGenerators",
                  "AAX_ePlugInCategory_WrappedPlugin",
                  "AAX_EPlugInCategory_Effect"]

RTAS_CATEGORIES = ["ePlugInCategory_None",
                   "ePlugInCategory_EQ",
                   "ePlugInCategory_Dynamics",
                   "ePlugInCategory_PitchShift",
                   "ePlugInCategory_Reverb",
                   "ePlugInCategory_Delay",
                   "ePlugInCategory_Modulation",
                   "ePlugInCategory_Harmonic",
                   "ePlugInCategory_NoiseReduction",
                   "ePlugInCategory_Dither",
                   "ePlugInCategory_SoundField",
                   "ePlugInCategory_HWGenerators",
                   "ePlugInCategory_SWGenerators",
                   "ePlugInCategory_WrappedPlugin",
                   "ePlugInCategory_Effect"]


def is_valid_vst2_category(category):
    """Returns true if a valid VST2 category was given"""
    if category in VST2_CATEGORIES:
        return True
    return False


def is_valid_vst3_category(category):
    """Returns true if a valid VST3 category was given"""
    if category in VST3_CATEGORIES:
        return True
    return False


def is_valid_au_category(category):
    """Returns true if a valid AudioUnit category was given"""
    if category in AU_CATEGORIES:
        return True
    return False


def is_valid_aax_category(category):
    """Returns true if a valid AAX category was given"""
    if category in AAX_CATEGORIES:
        return True
    return False


def is_valid_rtas_category(category):
    """Returns true if a valid RTAS category was given"""
    if category in RTAS_CATEGORIES:
        return True
    return False


def is_valid_cpp_standard(standard):
    """Returns true if the given standard is valid"""
    if standard in CPP_STANDARDS:
        return True
    return False
