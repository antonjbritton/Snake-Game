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
    elif character == ".-.-.-.-.-.-.-.-.-":
        return "..."

parser = argparse.ArgumentParser()
parser.add_argument('input_file_path')
parser.add_argument('output_file_path')

args = parser.parse_args()

for inputFile in os.listdir(args.input_file_path):
    inputFilePath = os.path.join(args.input_file_path, inputFile)
    outputFile = inputFile[:-4] + "_c28644ab.txt"
    outputFilePath = os.path.join(args.output_file_path, outputFile)

    with open(inputFilePath) as file:
        fileText = str(file.readlines())

    fileText = fileText.strip("[]'\\n")
    fileText = fileText.split(":", 1)
    algorithm = fileText[0]
    cipherText = fileText[1]

    if algorithm == "Hex":
        plainText = bytes.fromhex(cipherText).decode("utf-8")
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

    plainTextLower = plainText.lower()

    with open(outputFilePath, "w") as file:
        file.write(plainTextLower)
