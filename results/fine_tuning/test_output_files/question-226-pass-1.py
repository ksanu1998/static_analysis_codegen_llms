from math import *


def maxResult(n, a, b, c):
    x = (n - a) / (a + b + c)
    y = (n - b) / (a + b + c)
    z = (n - c) / (a + b + c)
    if (x >= 0 and y >= 0 and z >= 0):
        print(ceil(x) + ceil(y) + ceil(z))
    else:
        print(-1)


if __name__ == "__main__":
    n = 12
    a = 3
    b = 2
    c = 5
    maxResult(n, a, b, c)
