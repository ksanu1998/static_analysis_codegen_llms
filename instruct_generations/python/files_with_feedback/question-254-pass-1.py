import math


def findLargestDivisor(n):import math

def findLargestDivisor(n):
    i = int(math.sqrt(n))
    while i * i!= n:
        i -= 1
    return i
