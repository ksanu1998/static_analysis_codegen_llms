import math


def findCount(n):import math

def findCount(n):
    a, b, c = 1, 1, 1
    for i in range(n):
        a, b, c = b, c, a + b + c
    return a, b, c
