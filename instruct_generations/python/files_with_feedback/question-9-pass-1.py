import sys


def gcd(a, b):
import sys

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
