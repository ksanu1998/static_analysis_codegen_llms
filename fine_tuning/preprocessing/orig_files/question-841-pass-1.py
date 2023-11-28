import math


def nextPerfectSquare(N):
    nextN = math .floor(math .sqrt(N)) + 1
    return nextN * nextN


if __name__ == '__main__':
    N = 35
    print(nextPerfectSquare(N))
