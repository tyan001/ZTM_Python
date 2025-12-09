import argostranslate.package
import argostranslate.translate

from_code = "en"
to_code = "ja"

# Download and install Argos Translate package
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(
    filter(
        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    )
)
argostranslate.package.install_from_path(package_to_install.download())


# Translate
translatedText = argostranslate.translate.translate("Hello World", from_code, to_code)
print(translatedText)

try:
    with open('translate.txt', 'r') as f:
        translatedLines = []
        for line in f:
            translatedLine = argostranslate.translate.translate(line, from_code, to_code)
            print(argostranslate.translate.translate(line, from_code, to_code))
            translatedLines.append(translatedLine)

    with open('translate_ja.txt', 'w') as f2:
        for line in translatedLines:
            f2.write(line)
                
except FileNotFoundError as err:
    print(f'FileNotFound Error {err}')