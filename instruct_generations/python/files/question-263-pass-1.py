from math import floor


def solve(n, base):
    sum = 0
    while n > 0:
        sum += n % base
        n //= base
    return sum