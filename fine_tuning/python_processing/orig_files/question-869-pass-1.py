import math


def findNumberOfDigits(n, base):
    dig = (math .floor(math .log(n) / math .log(base)) + 1)
    print("The Number of digits of".format(n, base, dig))n = 1446


base = 7
findNumberOfDigits(n, base)
