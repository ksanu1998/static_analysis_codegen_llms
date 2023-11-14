def getResult(n):
    for digit in str(n):
        if n % int(digit) == 0:
            return True
    return False
