from math import sqrt


def countOrderedPairs(N):
    count = 0
    for i in range(1, int(sqrt(N)) + 1):
        for j in range(i, N // i + 1):
            count += 1
    return count
