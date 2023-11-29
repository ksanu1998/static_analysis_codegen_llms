from math import ceil, floor


def sum(N, X, Y):
    count = 0
    for i in range(1, N+1):
        if i % X == 0 or i % Y == 0:
            count += i
    return count
