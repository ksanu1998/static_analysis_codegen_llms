import math


def istetradecagonal(N):
    n = int(math.sqrt(24*N+1))
    return n*(n+1) == 2*N+1
