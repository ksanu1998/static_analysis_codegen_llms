import math


def countNumbers(N):
    count = 0
    for i in range(1, int(math.sqrt(N)) + 1):
        for j in range(1, int(math.sqrt(N - i * i)) + 1):
            if i * i + j * j == N:
                count += 1
    return count
