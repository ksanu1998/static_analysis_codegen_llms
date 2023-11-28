import math
a = [0] * 65


def count(i):
    if i == 0:
        return 0
    return i * (i + 1) // 2
