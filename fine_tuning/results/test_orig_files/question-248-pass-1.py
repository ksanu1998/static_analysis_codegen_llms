import sys



def minimumX(n, k):
    return n * k // gcd(n, k)
