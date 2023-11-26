import math


def isPerfect(x):
    y = int(math.sqrt(x))
    return x == y * y
