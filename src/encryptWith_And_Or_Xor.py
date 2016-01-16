__author__ = 'Per'

# decrypts a (binary/Ascii) number with XOR-operator and given cypher

plaintext = "001100"  # STRING!!!     will become input later
plainKey = "0110"



def checkIfBinaryIsUsed(key, plaintext):  # checks if text and key is in binary code (made of only 1's and 0's)

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
            break

    if (keyNumbersAreCorrect == True) & (textNumbersAreCorrect == True):  # add's both checks to 1

        allNumbersAreCorrect = True
    else:
        allNumbersAreCorrect = False

    return allNumbersAreCorrect

def matchKeyLengthToPlaintextLenght(key, plaintext):  # only works if binary_only numbers are used in key and plaintext! elif returns None
    matchedKey = None
    onlyBinaryUsed = checkIfBinaryIsUsed(key, plaintext)
    if onlyBinaryUsed == True:
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

    print("Only binary is used: " , onlyBinaryUsed)
    return matchedKey



matchedKey = matchKeyLengthToPlaintextLenght(plainKey, plaintext)


def encryptWithAnd(matchedKey, plaintext):
    counter = 0
    encryptedTextAsList = []
    for char in plaintext:
        encryptedChar = ""
        charInKey = matchedKey[counter]
        if (char == "0") & (charInKey == "0"):
            encryptedChar = "0"
        elif (char == "0") & (charInKey == "1"):
            encryptedChar = "0"
        elif (char == "1") & (charInKey == "0"):
            encryptedChar = "0"
        elif (char == "1") & (charInKey == "1"):
            encryptedChar = "1"
        encryptedTextAsList.append(encryptedChar)
        counter += 1
    encryptedText = "".join(encryptedTextAsList)
    return encryptedText


def encryptWithOr(matchedKey, plaintext):
    counter = 0
    encryptedTextAsList = []
    for char in plaintext:
        encryptedChar = ""
        charInKey = matchedKey[counter]
        if (char == "0") & (charInKey == "0"):
            encryptedChar = "0"
        elif (char == "0") & (charInKey == "1"):
            encryptedChar = "1"
        elif (char == "1") & (charInKey == "0"):
            encryptedChar = "1"
        elif (char == "1") & (charInKey == "1"):
            encryptedChar = "1"
        encryptedTextAsList.append(encryptedChar)
        counter += 1
    encryptedText = "".join(encryptedTextAsList)
    return encryptedText


def encryptWithXor(matchedKey, plaintext):
    counter = 0
    encryptedTextAsList = []
    for char in plaintext:
        encryptedChar = ""
        charInKey = matchedKey[counter]
        if (char == "0") & (charInKey == "0"):
            encryptedChar = "0"
        elif (char == "0") & (charInKey == "1"):
            encryptedChar = "1"
        elif (char == "1") & (charInKey == "0"):
            encryptedChar = "1"
        elif (char == "1") & (charInKey == "1"):
            encryptedChar = "0"
        encryptedTextAsList.append(encryptedChar)
        counter += 1
    encryptedText = "".join(encryptedTextAsList)
    return encryptedText

# !   1 = And, 2 = Or, 3 = Xor   !
def whichEncryption():
    input_encryption = input("Which encryption do you want to use? (1 = And, 2 = Or, 3 = Xor) ")
    return input_encryption


whichEncryption = whichEncryption()

encryptedText = ""

if whichEncryption == "1":
    encryptedText = encryptWithAnd(matchedKey, plaintext)
elif whichEncryption == "2":
    encryptedText = encryptWithOr(matchedKey, plaintext)
elif whichEncryption == "3":
    encryptedText = encryptWithXor(matchedKey, plaintext)

print(plaintext)
print(matchedKey)
print("\n" + encryptedText)
