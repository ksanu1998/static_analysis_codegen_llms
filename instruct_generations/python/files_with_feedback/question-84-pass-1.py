import sys

def kthNonDivisible(N, K):
    count = 0
    for i in range(1, N*K + 1):
        if i % N!= 0:
            count += 1
            if count == K:
                return i
    return -1
