import math


def gcdOfFactorial(m, n):
    return math .factorial(min(m, n))


m = 5
n = 9
print(gcdOfFactorial(m, n))
