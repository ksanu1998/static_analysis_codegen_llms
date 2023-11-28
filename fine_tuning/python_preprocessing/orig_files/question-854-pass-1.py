import math


def numberOfmeet(a, b):
    ans = 0
    if (a > b):
        ans = a - b
    else:
        ans = b - a
    if (a < 0):
        a = a * (-1)
    if (b < 0):
        b = b * (-1)
    return int(ans / math .gcd(a, b))


a = 1
b = -1
print(numberOfmeet(a, b))
