import math


def check(n):
    d = int(math .sqrt(n))
    if (d * d == n):
        return True
    return False


def largestNonPerfectSquareNumber(a, n):
    maxi = -1
    for i in range(0, n):
        if (check(a[i]) == False):
            maxi = max(a[i], maxi)
    return maxi


a = [16, 20, 25, 2, 3, 10]
n = len(a)
print(largestNonPerfectSquareNumber(a, n))
