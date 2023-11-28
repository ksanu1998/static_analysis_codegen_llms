import math


def solve(A, n, Q, q):
    count = 0
    for i in range(n):
        if A[i] == 1:
            count += 1
    return count
