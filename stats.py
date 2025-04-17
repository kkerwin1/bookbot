def countWords(wordList):
    numberOfWords = len(wordList)
    return numberOfWords

def getWordList(text):
    wordList = text.split()
    return wordList

def countCharacters(text):
    characterDict = {}
    
    for character in text.lower():
        if character in characterDict:
            characterDict[character] += 1
        else:
            characterDict[character] = 1

    return characterDict

def sort_on(dict):
    return dict["num"]

def sortDict(characterDict):
    dictList = []

    for char in characterDict:
        if char.isalpha():
            num = characterDict[char]
            charDict = {}
            charDict["char"] = char
            charDict["num"] = num
            dictList.append(charDict)
    
    dictList.sort(reverse=True, key=sort_on)
    return dictList