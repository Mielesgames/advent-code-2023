with open('words-day1.txt') as f:
    lines = f.read()
    strings = lines.split("\n")
    finalResult = 0
    for item in strings:
        fullNumber = ""
        firstNumber = None
        lastNumber = None
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
            print(fullNumber)
            finalResult += fullNumber

    print(finalResult)