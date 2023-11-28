import math


def findNumberOfDigits(n, base):
    dig = (math .floor(math .log(n) / math .log(base)) + 1)
    return dig


def isAllKs(n, b, k):
    len = findNumberOfDigits(n, b)
    sum = k * (1 - pow(b, len)) / (1 - b)
    return sum == N


N = 13
B = 3
K = 1
if (isAllKs(N, B, K)):
    print("Yes")
else:
    print("No")
