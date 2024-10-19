def main():
    contents = getFile('./books/Frankenstein.txt')

    wordsCnt = countWords(contents)
    chars = characterCount(contents)
    printReport(wordsCnt, chars)

def getFile(path):
    with open(path) as f:
        return f.read()

def countWords(text):
    return len(text.split())

def characterCount(text):
    text = text.lower()
    chars = {}

    for char in text:
        if char in chars:
            chars[char] += 1
        elif char.isalpha():
            chars[char] = 1

    return chars

def printReport(wordsCnt, chars):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordsCnt} words found in the document")

    for key in chars:
        print(f"The '{key}' character was found {chars[key]} times")

    print("--- End report ---")

main()