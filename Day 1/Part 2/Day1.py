with open('words-day1.txt') as f:
    lines = f.read()
    strings = lines.split("\n")
    finalResult = 0
    textNumbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0"
    }
    def word_to_number(word):
        return textNumbers.get(word.lower(), word)
    
    for item in strings:
        fullNumber = ""
        firstNumber = None
        lastNumber = None
        for word in textNumbers.keys():
            if word in item.lower():
                item = item.replace(word, word_to_number(word))
        for letter in item:
            if letter.isnumeric():
                if firstNumber is None:
                    firstNumber = letter
                else:
                    lastNumber = letter
        if lastNumber == None:
            lastNumber = firstNumber
        if firstNumber is not None and lastNumber is not None:
            fullNumber = int(str(firstNumber) + str(lastNumber))
            # print(fullNumber)
            print(f"{finalResult} + {fullNumber} = {finalResult + fullNumber}")
            finalResult += fullNumber

    print(finalResult)