from math import sqrt
MAX = 10000
prefix = [0 for i in range(MAX + 1)]


def buildPrefix():
    for i in range(2, int(sqrt(MAX)) + 1):
        if prefix[i] == 0:
            for j in range(i * i, MAX + 1, i):
                prefix[j] = 1
    return prefix
