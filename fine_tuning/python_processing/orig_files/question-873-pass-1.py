import math


def isTriangular(num):
    if (num < 0):
        return False
    c = (-2 * num)
    b = 1
    a = 1
    d = (b * b) - (4 * a * c)
    if (d < 0):
        return -1
    root1 = (-b + math .sqrt(d)) // (2 * a)
    root2 = (-b - math .sqrt(d)) // (2 * a)
    if (root1 > 0 and math .floor(root1) == root1):
        return root1
    if (root2 > 0 and math .floor(root2) == root2):
        return root2
    return -1


def isPerfectSquare(x):
    sr = math .sqrt(x)
    if ((sr - math .floor(sr)) == 0):
        return math .floor(sr)
    else:
        return -1


def findS(s):
    sr = isPerfectSquare(s)
    if (sr == -1):
        return -1
    return int(isTriangular(sr))


s = 9
n = findS(s)
if (n == -1):
    print("-1")
else:
    print(n)
