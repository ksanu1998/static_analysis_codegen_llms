import math


def digSum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + digSum(n // 10)
