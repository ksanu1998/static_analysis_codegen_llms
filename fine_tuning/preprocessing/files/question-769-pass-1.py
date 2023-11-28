import sys


def startingPoint(A, N):
    prefix_sum = 0
    for i in range(N):
        prefix_sum += A[i]
        if prefix_sum < 0:
            return i
    return 0
