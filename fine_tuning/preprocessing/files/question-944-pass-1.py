import math


def countPairs(N):
    count = 0
    for a in range(1, int(math.sqrt(N)) + 1):
        for b in range(a, int(math.sqrt(N - a ** 3)) + 1):
            if a ** 3 + b ** 3 == N:
                count += 1
    return count
