import math


def findCount(n):
    return int(math .log(n, 2)) + 1


N = 10
print(findCount(N))
