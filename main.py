import stats

import sys

def getBookText(path):
    with open(path) as f:
        fileContents = f.read()
        return fileContents

def printReport(path, wordCount, sortedCharDict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {wordCount} total words")
    print("--------- Character Count -------")
    for charDict in sortedCharDict:
        char = charDict["char"]
        num = charDict["num"]
        print(f"{char}: {num}")
    print("============= END ===============")

def getPath():
    try:
        path = sys.argv[1]
        return path
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    path = getPath()
    text = getBookText(path)
    wordList = stats.getWordList(text)
    wordCount = stats.countWords(wordList)
    characterDict = stats.countCharacters(text)
    sortedCharDict = stats.sortDict(characterDict)
    printReport(path, wordCount, sortedCharDict)

if __name__ == "__main__":
    main()