import math


def discreteLogarithm(a, b, m):
    n = int(math .sqrt(m) + 1)
    an = 1
    for i in range(n):
        an = (an * a) % m
    value = [0] * m
    cur = an
    for i in range(1, n + 1):
        if (value[cur] == 0):
            value[cur] = i
        cur = (cur * an) % m
    cur = b
    for i in range(n + 1):
        if (value[cur] > 0):
            ans = value[cur] * n - i
            if (ans < m):
                return ans
        cur = (cur * a) % m
    return -1


a = 2
b = 3
m = 5
print(discreteLogarithm(a, b, m))
a = 3
b = 7
m = 11
print(discreteLogarithm(a, b, m))
