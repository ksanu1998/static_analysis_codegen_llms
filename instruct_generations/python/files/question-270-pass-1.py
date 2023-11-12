from math import sqrt


def findAandB(N):
    for i in range(1, int(sqrt(N)) + 1):
        b = N - i
        if b >= i and b % i == 0:
            return i, b
    return None