import math


def findNumberOfDigits(n, base):
    return math.floor(math.log(n, base)) + 1
