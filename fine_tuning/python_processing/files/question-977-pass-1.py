import math


def farey(n):
    a = [1, 1]
    b = [1, 0]
    c = [1, 1]
    d = [1, 0]
    for i in range(n-1):
        a.append(int(c[0] * d[1] + c[1] * d[0]))
        b.append(int(c[1] * d[1] - c[0] * d[0]))
        c, d = a, b
    return c, d
