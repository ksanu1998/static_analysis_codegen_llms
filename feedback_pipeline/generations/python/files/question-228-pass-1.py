import math


def max_gcd(n, p):
    return max(math.gcd(i, p) for i in range(1, n+1))