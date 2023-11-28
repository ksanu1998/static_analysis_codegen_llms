import math


def solve(n):
    for i in range(1, int(n ** 0.5) + 1):
        j = int(n / i)
        if i < j:
            return i, j
    return -1, -1
