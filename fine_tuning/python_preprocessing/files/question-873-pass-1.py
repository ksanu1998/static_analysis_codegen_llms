import math


def isTriangular(num):
    x = int(math.sqrt(num))
    return x * (x + 1) == 2 * num
