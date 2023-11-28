from itertools import permutations


def countWays(n):
    return len(list(permutations(range(1, n+1))))
