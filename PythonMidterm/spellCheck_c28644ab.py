import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('english_words_file')
parser.add_argument('input_file_path')
parser.add_argument('output_file_path')

args = parser.parse_args()

for inputFile in os.listdir(args.input_file_path):
    inputFilePath = os.path.join(args.input_file_path, inputFile)
    outputFile = inputFile[:-4] + "_c28644ab.txt"
    outputFilePath = os.path.join(args.output_file_path, outputFile)

    with open(inputFilePath) as file:
        fileText = file.readlines()

    fileText = [line.rstrip("\n") for line in open(inputFilePath)]
    file.close()

    fileText = fileText[0].split(" ")

    count = 0
    numbers = 0
    punctuation = 0
    upperLetters = 0
    words = 0
    correctWords = 0
    incorrectWords= 0


    for word in fileText:
        for letter in word:
            if letter in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                fileText[count] = fileText[count].replace(letter,"")
                numbers += 1
            if letter in (".", ",", "'", "\"", "/", "|", "@", "!", "?", "(", ")", "£", "$", "%", "^", "&", "*", "_", "-", "+", "=", "#", "~", ":", ";", "<", ">", "{", "}", "[", "]"):
                fileText[count] = fileText[count].replace(letter,"")
                punctuation += 1
            if letter.isupper():
                upperLetters += 1
        fileText[count] = fileText[count].lower()
        count += 1

    for word in fileText:
        if word == "":
            fileText.remove(word)


    with open(args.english_words_file) as file:
        englishWords = file.readlines()

    englishWords = [line.rstrip("\n") for line in open(args.english_words_file)]
    file.close()


    for word in fileText:
        if word in englishWords:
            correctWords += 1
        else:
            incorrectWords += 1
        words += 1

    with open(outputFilePath, "w") as file:
        file.write("c28644ab\n")
        file.write("Formatting ###################\n")
        file.write("Number of upper case words changed: " + str(upperLetters) +"\n")
        file.write("Number of punctuations removed: " + str(punctuation) +"\n")
        file.write("Number of numbers removed: " + str(numbers) +"\n")
        file.write("Spellchecking ###################\n")
        file.write("Number of words: " + str(words) + "\n")
        file.write("Number of correct words: " + str(correctWords) + "\n")
        file.write("Number of incorrect words: " + str(incorrectWords))
