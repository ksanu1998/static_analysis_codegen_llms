def countWays(N):
    if N <= 0:
        return 0
    if N == 1:
        return 1
    if N == 2:
        return 2
    if N == 3:
        return 3
    return countWays(N-1) + countWays(N-2) + countWays(N-3)
