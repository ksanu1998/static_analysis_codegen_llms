from math import sqrt, ceil, floor


def perfectSquares(a, b):
    count = 0
    for i in range(a, b+1):
        if i**0.5 == int(i**0.5):
            count += 1
    return count