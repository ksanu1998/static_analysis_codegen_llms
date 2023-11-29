from math import sqrt, floor



def isPerfect(N):
    root = floor(sqrt(N))
    return N == root ** 2
