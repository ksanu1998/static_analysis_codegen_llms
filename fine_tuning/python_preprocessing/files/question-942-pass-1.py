import math


def discreteLogarithm(a, b, m):
    if a == 1 or b == 1:
        return 0
    for i in range(1, m):
        if (a ** i) % m == b:
            return i
    return -1
