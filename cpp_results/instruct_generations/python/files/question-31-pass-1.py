from collections import defaultdict


def countQuadruplets(N):
    count = 0
    for a in range(1, int(N**0.5) + 1):
        for b in range(a, int(N**0.5) + 1):
            c = N - a - b
            if c < b:
                break
            if a**2 + b**2 == c**2:
                count += 1
    return count