from math import sqrt


def findValuesOfK(g):
    for k in range(1, g):
        if sum(range(k, k + g)) == g:
            return k
    return -1
