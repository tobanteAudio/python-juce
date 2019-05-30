from juce.projucer import JucerFile


def main():

    jucerFile = JucerFile('assets/modEQ.jucer')

    # Properties (get)
    print(jucerFile.path)
    print(jucerFile.id)
    print(jucerFile.name)
    print(jucerFile.project_type)
    print(jucerFile.jucer_version)
    print(jucerFile.version)
    print(jucerFile.company)
    print(jucerFile.company_website)
    print(jucerFile.company_email)
    print(jucerFile.bundle_identifier)
    print(jucerFile.plugin_name)
    print(jucerFile.plugin_description)
    print(jucerFile.plugin_manufacturer)
    print(jucerFile.plugin_manufacturer_code)
    print(jucerFile.plugin_code)
    print(jucerFile.plugin_au_exporter_profile)
    print(jucerFile.aax_identifier)
    print(jucerFile.vst3_category)
    print(jucerFile.binary_data_namespace)
    print(jucerFile.cpp_language_standard)
    print(jucerFile.plugin_formats)
    print(jucerFile.company_copyright)
    print(jucerFile.display_splash_screen)
    print(jucerFile.report_app_usage)
    print(jucerFile.compiler_flag_schemes)
    print(jucerFile.project_line_feed)

    # Properties (set)
    jucerFile.path = 'x'
    jucerFile.id = 'x'
    jucerFile.name = 'x'
    jucerFile.project_type = 'x'
    jucerFile.jucer_version = 'x'
    jucerFile.version = 'x'
    jucerFile.company = 'x'
    jucerFile.company_website = 'x'
    jucerFile.company_email = 'x'
    jucerFile.bundle_identifier = 'x'
    jucerFile.plugin_name = 'x'
    jucerFile.plugin_description = 'x'
    jucerFile.plugin_manufacturer = 'x'
    jucerFile.plugin_manufacturer_code = 'x'
    jucerFile.plugin_code = 'x'
    jucerFile.plugin_au_exporter_profile = 'x'
    jucerFile.aax_identifier = 'x'
    jucerFile.vst3_category = 'x'
    jucerFile.binary_data_namespace = 'x'
    jucerFile.cpp_language_standard = 'x'
    jucerFile.plugin_formats = 'x'
    jucerFile.company_copyright = 'x'
    jucerFile.display_splash_screen = 'x'
    jucerFile.report_app_usage = 'x'
    jucerFile.compiler_flag_schemes = 'x'
    jucerFile.project_line_feed = 'x'

    # Save to disc
    jucerFile.save_as('output/test.jucer')


if __name__ == "__main__":
    main()
