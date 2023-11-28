def countWays(N):

def countWays(N):
    if N == 0:
        return 1
    if N < 0:
        return 0
    return countWays(N-3) + countWays(N-2) + countWays(N-1)
