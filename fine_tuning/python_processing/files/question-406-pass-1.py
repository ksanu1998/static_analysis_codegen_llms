def countWays(n, k):
    if n == 0:
        return 1
    if k == 0:
        return 0
    return countWays(n-1, k) + countWays(n-1, k-1)
