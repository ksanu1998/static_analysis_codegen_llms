from collections import defaultdict


def countQuadraples(N):

def countQuadruplets(N):
    count = 0
    for a in range(1, N):
        for b in range(a, N):
            c = (a + b) // 2
            d = N - c
            if c * c + d * d == a * a + b * b:
                count += 1
    return count
