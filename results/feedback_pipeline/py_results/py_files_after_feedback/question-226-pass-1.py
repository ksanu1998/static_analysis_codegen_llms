from math import *


def maxResult(n, a, b, c):
    x, y, z = 0, 0, 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            x = i
            y = n // i
            z = a * x + b * y
            if z > n:
                break
    return z
