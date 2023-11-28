import math


def findNumberOfDigits(n, base):
    return math.ceil(math.log10(n) / math.log10(base))
