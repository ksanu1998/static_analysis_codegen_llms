N = 3


def solve(v):
    x = v[0]
    y = v[1]
    a = (x + y) / 2
    b = (x - y) / 2
    c = -b
    return a, b, c
