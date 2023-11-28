import math


def calculate(a, b, n, m):
    mul = 1
    for i in range(m):
        if (b[i] != 0):
            mul = mul * b[i]
    for i in range(n):
        x = math .floor(a[i] / mul)
        print(x, end=" ")


a = [5, 100, 8]
b = [2, 3]
n = len(a)
m = len(b)
calculate(a, b, n, m)
