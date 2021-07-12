"""
Function to check if the credit card number informed is valid
Validation steps:
 Validation 1 - It must start with a 4, 5 or 6. ok
 Validation 2 - It must contain exactly 16 digits. ok
 Validation 3 - It must only consist of digits (0-9). ok
 Validation 4 - It may have digits in groups of 4, separated by one hyphen "-". ok
 Validation 5 - It must NOT use any other separator like ' ' , '_', etc. ok
 Validation 6 - It must NOT have 4 or more consecutive repeated digits.
"""
def checkCreditCardNumber(creditCardNumber):
    digitsArray = [str(digit) for digit in str(creditCardNumber)]

    #Validation 5
    #It must only contain integer number from 0 to 9 and the separator '-'
    validDigits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']
    if any(digit not in validDigits for digit in digitsArray):
        print("Invalid")
        return False

    #Returns a list with the indexes that contains a separator in the digits array
    separatorsIndexes = [i for i, x in enumerate(digitsArray) if x == '-']

    #If there is separators, ckecks the positions of the separators in the array.
    #It must be in the 4,9 and 14 indexes, to respect Validation 4.
    if separatorsIndexes:
        validSeparatorsIndexes = [4, 9, 14]
        if (separatorsIndexes != validSeparatorsIndexes
                or len(separatorsIndexes) != 3):
            print("Invalid")
            return False

    #Removing the separators, if there's any
    numbersArray = [digit for digit in digitsArray if digit != '-']

    #Validation 1
    validFirstDigit = ['4', '5', '6']
    if numbersArray[0] not in validFirstDigit:
        print("Invalid")
        return False

    #Validation 2
    if len(numbersArray) != 16:
        print("Invalid")
        return False

    #Validation 6
    numbersArraySize = len(numbersArray)
    a = numbersArray
    #Looping till the last digit that could have consecutive repetitions
    for i in range(numbersArraySize - 3):
        if a[i] == a[i + 1] and a[i + 1] == a[i + 2] and a[i + 2] == a[i + 3]:
            print("Invalid")
            return False
    
    print("Valid")
    return True

#Main program

N = int(input())

#Validating N value
if (N > 100) | (N < 0):
    print('N value is invalid. Type a number between 0 and 100')
else:
    creditCardNumbersArray = []
    for n in range(N):
        creditCardNumbersArray.append(input())

    for number in creditCardNumbersArray:
        checkCreditCardNumber(number)