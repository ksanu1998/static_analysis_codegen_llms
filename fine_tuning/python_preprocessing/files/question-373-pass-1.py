def binomialCoeff(n, k):from math import factorial

def binomialCoeff(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))
