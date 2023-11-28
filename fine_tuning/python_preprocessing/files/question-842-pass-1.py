import math


def printSubstrings(n):
    substrings = []
    for i in range(1, int(math.log10(n)) + 1):
        substrings.append(str(n)[:i])
    return substrings
