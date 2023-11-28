from math import gcd


def isPossible(a, b, c):
    gcd_val = gcd(a, b)
    return c % gcd_val == 0
