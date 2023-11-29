from math import *


def countBinaries(N):
    count = 0
    for i in range(N+1):
        if i % 2 == 0:
            count += 1
    return count
