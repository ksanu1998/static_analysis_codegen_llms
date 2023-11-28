import sys


def findPowerOfP(n, p):
    count = 0
    while n > 0:
        if n % p == 0:
            count += 1
            n = n // p
        else:
            break
    return count
