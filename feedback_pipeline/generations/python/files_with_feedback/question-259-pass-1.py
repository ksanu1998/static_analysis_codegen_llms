def getNumber(s):
    n = int(s)
    factorial = 1
    for i in range(1, n):
        factorial *= i
    return factorial
