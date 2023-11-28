import math


def isPower(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n == i ** 2:
            return True
    return False
