"""Functions for validating jucer project attributes"""

# LINE ENDINGS
LINE_FEEDS = ['\n', '\r\n']

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


def is_valid_four_digit_code(code):
    """Returns true if a code with 4 digits and at least
    one upper case letter was given

    :param `code`: String to test
    :returns: Validation result
    :rtype: bool
    """
    if len(code) == 4:
        for char in code:
            if char.isupper():
                return True
    return False


def is_valid_plugin_code(code):
    """Returns true if a valid plugin code was given

    :param `code`: String to test
    :returns: Validation result
    :rtype: bool
    """
    if is_valid_four_digit_code(code):
        return True
    return False


def is_valid_plugin_manufacturer_code(code):
    """Returns true if a valid plugin manufacturer code was given

    :param `code`: String to test
    :returns: Validation result
    :rtype: bool
    """
    if is_valid_four_digit_code(code):
        return True
    return False


def is_valid_project_type(project_type):
    """Returns true if a valid project type was give

    :param `project_type`: String to test
    :returns: Validation result
    :rtype: bool
    """
    if project_type in PROJECT_TYPES:
        return True
    return False


def is_valid_vst2_category(category):
    """Returns true if a valid VST2 category was given

    :param `category`: String to test
    :returns: Validation result
    :rtype: bool

    """
    if category in VST2_CATEGORIES:
        return True
    return False


def is_valid_vst3_category(category):
    """Returns true if a valid VST3 category was given

    :param `category`: String to test
    :returns: Validation result
    :rtype: bool
    """
    if category in VST3_CATEGORIES:
        return True
    return False


def is_valid_au_category(category):
    """Returns true if a valid AudioUnit category was given

    :param `category`: String to test
    :returns: Validation result
    :rtype: bool
    """
    if category in AU_CATEGORIES:
        return True
    return False


def is_valid_aax_category(category):
    """Returns true if a valid AAX category was given

    :param `category`: String to test
    :returns: Validation result
    :rtype: bool
    """
    if category in AAX_CATEGORIES:
        return True
    return False


def is_valid_rtas_category(category):
    """Returns true if a valid RTAS category was given

    :param `category`: String to test
    :returns: Validation result
    :rtype: bool
    """
    if category in RTAS_CATEGORIES:
        return True
    return False


def is_valid_cpp_standard(standard):
    """Returns true if the given standard is valid

    :param `standard`: String to test
    :returns: Validation result
    :rtype: bool
    """
    if standard in CPP_STANDARDS:
        return True
    return False


def is_valid_namespace(namespace):
    """Returns true if the given namespace is valid

    :param `namespace`: String to test
    :returns: Validation result
    :rtype: bool
    """
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if namespace[0] in digits:
        return False
    if namespace.find("-") != -1:
        return False
    if namespace.find(" ") != -1:
        return False
    return True


def is_valid_boolean(boolean):
    """Returns true if the given value represents a bool

    :param `boolean`: Value to test
    :returns: Validation result
    :rtype: bool
    """
    if boolean == 0:
        return True
    if boolean == 1:
        return True

    return False


def is_valid_line_feed(line_feed):
    """Returns true if the line feed is valid

    :param `line_feed`: String to test
    :returns: Validation result
    :rtype: bool
    """
    if line_feed in LINE_FEEDS:
        return True
    return False
