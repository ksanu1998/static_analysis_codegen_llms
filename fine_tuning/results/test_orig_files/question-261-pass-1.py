def addNDigits(a, b, n):

def addNDigits(a, b, n):
    result = 0
    for i in range(n):
        result = (result * 10 + a) % b
        a = (a * 10 + a) % b
    return result
