import math


def bit(x):
    ans = 0
    while (x):
        x /= 2
        ans = ans + 1
    return ans


def check(d, x):
    if (bit(x / d) <= bit(d)):
        return True
    return False


def bs(n):
    l = 1
    r = int(math .sqrt(n))
    while (l < r):
        m = int((l + r) / 2)
        if (check(m, n)):
            r = m
        else:
            l = m + 1
    if (check(l, n) == False):
        return math .floor(l + 1)
    else:
        return math .floor(l)


def countDivisor(n):
    return n - bs(n) + 1


n = 5
print(countDivisor(n))
