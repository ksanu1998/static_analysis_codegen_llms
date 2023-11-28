def checkFibinnary(n):
    binary = bin(n)[2:]
    return not binary.count('1') >= 2
