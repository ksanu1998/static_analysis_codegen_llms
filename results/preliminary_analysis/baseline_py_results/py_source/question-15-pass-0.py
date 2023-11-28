# Count numbers from given range having odd digits at odd places and even digits at even places. 
def getPower(p): 
    return 10**p 
 
def getDigit(n, p): 
    return (n // getPower(p)) % 10 
 
def getOddDigits(n): 
    oddDigits = 0 
    for i in range(1, 5): 
        if getDigit(n, i) % 2!= 0: 
            oddDigits += getPower(i) 
    return oddDigits 
 
def getEvenDigits(n): 
    evenDigits = 0 
    for i in range(1, 5): 
        if getDigit(n, i) % 2 == 0: 
            evenDigits += getPower(i) 
    return evenDigits 
 
def getOddEvenDigits(n): 
    return getOddDigits(n) + getEvenDigits(n) 
 
def getOddEvenDigitsCount(n): 
    return getOddEvenDigits(n) // 10 