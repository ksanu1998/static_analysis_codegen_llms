import math


def findNumber(n):
    x = int(math .floor((-1 + math .sqrt(1 + 8 * n - 8)) / 2))
    base = (x * (x + 1)) / 2 + 1
    return n - base + 1


n = 55
print(findNumber(n))
