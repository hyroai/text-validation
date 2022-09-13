import os
import js2py

TRANSLATED_FILE_NAME = "text_validation.py"


def translate():
    # read js file
    with open('index.js', 'r') as file:
        js_code = file.read().split("module.exports")[0].strip()

    # augment and write to disk
    f = open("temp.js", "w")
    f.write(js_code)
    f.close()

    # translate
    js2py.translate_file("temp.js", TRANSLATED_FILE_NAME)

    # remove temp augmented file
    os.remove('temp.js')


if __name__ == '__main__':
    translate()
