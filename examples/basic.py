from juce.projucer import Projucer, JucerFile

# Projucer
projucer = Projucer()
print(projucer.path)

# jucer file
jucerFile = JucerFile('tests/assets/modEQ.jucer')

# Properties (get)
print(jucerFile.cpp_language_standard)          # 17

# Properties (set)
# Should fail. Not a valid option.
jucerFile.cpp_language_standard = '0.2.1'
print(jucerFile.cpp_language_standard)          # 17
