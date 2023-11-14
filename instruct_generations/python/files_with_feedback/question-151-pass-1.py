import math

def nCr(n, r):
    if r > n - r:
        r = n - r
    numerator = math.factorial(n) // math.factorial(r)
    denominator = math.factorial(n - r)
    return numerator // denominator
