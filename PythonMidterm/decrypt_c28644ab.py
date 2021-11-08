import argparse, os

def morse_code_translator(character):
    if character == ".-":
        return "a"
    elif character == "-...":
        return "b"
    elif character == "-.-.":
        return "c"
    elif character == "-..":
        return "d"
    elif character == ".":
        return "e"
    elif character == "..-.":
        return "f"
    elif character == "--.":
        return "g"
    elif character == "....":
        return "h"
    elif character == "..":
        return "i"
    elif character == ".---":
        return "j"
    elif character == "-.-":
        return "k"
    elif character == ".-..":
        return "l"
    elif character == "--":
        return "m"
    elif character == "-.":
        return "n"
    elif character == "---":
        return "o"
    elif character == ".--.":
        return "p"
    elif character == "--.-":
        return "q"
    elif character == ".-.":
        return "r"
    elif character == "...":
        return "s"
    elif character == "-":
        return "t"
    elif character == "..-":
        return "u"
    elif character == "...-":
        return "v"
    elif character == ".--":
        return "w"
    elif character == "-..-":
        return "x"
    elif character == "-.--":
        return "y"
    elif character == "--..":
        return "z"
    elif character == ".----":
        return "1"
    elif character == "..---":
        return "2"
    elif character == "...--":
        return "3"
    elif character == "....-":
        return "4"
    elif character == ".....":
        return "5"
    elif character == "-....":
        return "6"
    elif character == "--...":
        return "7"
    elif character == "---..":
        return "8"
    elif character == "----.":
        return "9"
    elif character == "-----":
        return "0"
    elif character == "--..--":
        return ","
    elif character == ".-.-.-":
        return "."
    elif character == "..--..":
        return "?"
    elif character == "-.-.-":
        return ";"
    elif character == "---...":
        return ":"
    elif character == "-..-.":
        return "/"
    elif character == "-....-":
        return "-"
    elif character == ".----.":
        return "'"
    elif character == "-.--.":
        return "("
    elif character == "-.--.-":
        return ")"
    elif character == "..--.-":
        return "_"
    elif character == ".--.-.":
        return "@"
    elif character == "-.-.--":
        return "!"
    elif character == ".-...":
        return "&"
    elif character == "-...-":
        return "="
    elif character == ".-.-.":
        return "+"
    elif character == "-...":
        return '"'
    elif character == "...-..-":
        return "$"
    elif character == "/":
        return " "

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')

args = parser.parse_args()

if os.path.exists(args.input_file):
    with open(args.input_file) as file:
        fileText = str(file.readlines())

    fileText = fileText.strip("[]'\\n")
    fileText = fileText.split(":", 1)
    algorithm = fileText[0]
    cipherText = fileText[1]

    if algorithm == "Hex":
        plainText = bytes.fromhex(cipherText).decode("utf-8").lower()
    elif algorithm == "Caesar Cipher(+3)":
        plainText = ""
        ciphertextPosition = 0
        while ciphertextPosition < len(cipherText):
            ciphertextChar = cipherText[ciphertextPosition]
            ASCIIvalue = ord(ciphertextChar)
            ASCIIvalue = ASCIIvalue - 3
            if ASCIIvalue == 29:
                plainText = plainText + " "
            else:
                plainText = plainText + chr(ASCIIvalue)
            ciphertextPosition += 1
    elif algorithm == "Morse Code":
        plainText = ""
        cipherText = cipherText.split(" ")
        for character in cipherText:
            translatedChar = morse_code_translator(character)
            plainText = plainText + translatedChar

    print(plainText)
    with open(args.output_file, "w") as file:
        file.write(plainText)
