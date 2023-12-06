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
        for x in range(len(item)):
            if item[0].isnumeric():
                if firstNumber is None:
                    firstNumber = item[0]
                else:
                    lastNumber = item[0]
            else:
                for letter in textNumbers:
                    if item.startswith(letter):
                        if firstNumber is None:
                            firstNumber = word_to_number(letter)
                        else:
                            lastNumber = word_to_number(letter)
                # item.startswith("eight")
            item = item[1:]
        if lastNumber == None:
            lastNumber = firstNumber
        if firstNumber is not None and lastNumber is not None:
            fullNumber = int(str(firstNumber) + str(lastNumber))
            # print(fullNumber)
            print(f"{finalResult} + {fullNumber} = {finalResult + fullNumber}")
            finalResult += fullNumber

    print(finalResult)