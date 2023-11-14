from math import sqrt


def smallestDivisor(n):from math import sqrt

def smallestDivisor(n):
    sqrt_n = int(sqrt(n))
    for i in range(sqrt_n, 1, -1):
        if n % i == 0:
            return i
    return 1
