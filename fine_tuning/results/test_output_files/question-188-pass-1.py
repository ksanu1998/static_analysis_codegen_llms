from math import sqrt, ceil, floor


def perfectSquares(a, b):
    n = 1
    while (n <= b):
        n *= 2
    n /= 2
    if (n < a):
        print("-1")
        exit(0)
    n -= a
    if (n == 0):
        print(0)
        exit(0)
    n = ceil(sqrt(n))
    if (n == 0):
        print(0)
        exit(0)
    n = floor(n)
    print(n)
