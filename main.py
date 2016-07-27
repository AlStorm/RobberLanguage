#List of vowels as well as other characters that shouldn't be used.
vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "y", "Y", "ä", "Ä", "ö", "Ö", "å", "Å", "'", "!", " ", ".", "," "?"]

#Initiates either the encoding function or the decoding function.
def robberPrompt():
    codeChoice = input(str(" \nWrite \"e\" to encode a sentence.\nWrite \"d\" to decode a sentence.\n"))
    if codeChoice == "d":
        print(robberDecode(str(input("Decode: "))))
    elif codeChoice == "e":
        print(robberEncode(str(input("Encode: "))))

#Encoding function.
def robberEncode(sentence):
    newSentence = ''
    for i in sentence:
        if i in vowels:
            newSentence += i
        else:
            i += 'o' + i.lower()
            newSentence += i
    return newSentence

#Decoding function.
def robberDecode(code):
    solution = ''
    codeIndex = 0
    while codeIndex < len(code):
        solution += code[codeIndex]
        if code[codeIndex] in vowels:
            codeIndex += 1
        else:
            codeIndex += 3
    return solution

robberPrompt()
