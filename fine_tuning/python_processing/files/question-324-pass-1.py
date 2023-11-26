import numpy as np
N = 101
mod = int(1e9) + 7
exactsum = np .zeros((N, N, N))
exactnum = np .zeros((N, N, N))


def getSum(x, y, z):
    return exactsum[x][y][z]
