from math import sqrt



def isPentadecagon(N):
    n = (1 + sqrt(10)) * N
    return int(n) == n
