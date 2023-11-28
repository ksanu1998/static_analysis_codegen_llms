def nCr(n, r):

import math

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    if r == 0 or r == n:
        return 1
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
