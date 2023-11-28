def weightedMean(n):
    return sum(i*i for i in range(1, n+1)) / sum(range(1, n+1))
