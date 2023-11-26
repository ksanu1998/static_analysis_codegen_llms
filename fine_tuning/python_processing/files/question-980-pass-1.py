def countWays(n):
    if n <= 3:
        return n
    else:
        return countWays(n-1) + countWays(n-2) + countWays(n-3)
