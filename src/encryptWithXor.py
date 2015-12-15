__author__ = 'Per'

# decrypts a (binary/Ascii) number with XOR-operator and given cypher

plaintext = "001100"  # STRING!!!     will become input later
plainKey = "0110"
decryptedText = ""



def checkIfOnly_1_used(key, plaintext):  # checks if text and key is in binary code (made of only 1's and 0's)

    textNumbersAreCorrect = None  # if text is binary => true, else => false
    keyNumbersAreCorrect = None  # if key is binary => true, else => false
    allNumbersAreCorrect = None

    for char in key:   # checks on Key

        if (char == "0") or (char == "1"):
            keyNumbersAreCorrect = True
        else:
            keyNumbersAreCorrect = False
            break

    for char in plaintext:  # checks on Text

        if (char == "0") or (char == "1"):
            textNumbersAreCorrect = True
        else:
            textNumbersAreCorrect = False

    if (keyNumbersAreCorrect == True) & (textNumbersAreCorrect == True):  # add's both checks to 1

        allNumbersAreCorrect = True
    else:
        allNumbersAreCorrect = False

    return allNumbersAreCorrect



def matchKeyLengthToPlaintextLenght(key, plaintext):

    matchedKey = key  # for case if length of key and text is the same

    if len(plaintext) > len(key):   # if key is to short

        lengthDiff = len(plaintext) - len(key)  # the length difference between key and plaintext
        matchedKeyAsList = []

        for letter in key:  # makes key a list

            matchedKeyAsList.append(letter)

        matchedKeyAsList.append(matchedKeyAsList[0])  # and add's it's first letter to the end

        if lengthDiff > 1:   # if more than one letter needs to be added to the key

            for i in range (1, lengthDiff):  # it is appended to the end of the list

                matchedKeyAsList.append(matchedKeyAsList[i])

        matchedKey = "".join(matchedKeyAsList)   # joins key list back to String

    elif len(plaintext) < len(key):   # if key is to long

        lengthDiff = len(key) - len(plaintext)  # difference between key and text
        matchedKeyAsList = []

        for letter in key:  # makes key a list

            matchedKeyAsList.append(letter)

        for i in range (0, lengthDiff):  # and removes as many items from 0 to length diff, so length of text and key is equal
            matchedKeyAsList.pop(i)

        matchedKey = "".join(matchedKeyAsList)  # joins key list back to String

    return matchedKey






bool_numbersAreCorrect = checkIfOnly_1_used(plainKey, plaintext)

print(bool_numbersAreCorrect)

matchedKey = matchKeyLengthToPlaintextLenght(plainKey, plaintext)

print(matchedKey)



