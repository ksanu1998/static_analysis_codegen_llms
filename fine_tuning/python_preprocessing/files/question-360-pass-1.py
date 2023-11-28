def findMinimumCost(n, x, y):
    return min(x[i] + y[i-1] for i in range(1, n+1))
