from math import log2


def findAandB(N):
    a = 1
    b = N - 1
    while a + b!= N:
        a = a << 1
        b = b >> 1
    return a, b
