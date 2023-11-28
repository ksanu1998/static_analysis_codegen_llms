import math


def countdigits(N):
    count = 0
    while N > 0:
        count += 1
        N //= 10
    return count
