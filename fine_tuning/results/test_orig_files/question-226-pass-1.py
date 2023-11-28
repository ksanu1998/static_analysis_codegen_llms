from math import *



def maxResult(n, a, b, c):
    x, y, z = 0, 0, 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            j = n // i
            if a * i + b * j == n:
                x = i
                y = j
                z = n - x - y
                break
            elif a * j + b * i == n:
                x = j
                y = i
                z = n - x - y
                break
    return x + y + z
