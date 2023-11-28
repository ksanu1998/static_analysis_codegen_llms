def findSum(n):
    return sum([a * b for a in range(1, n + 1) for b in range(a, n + 1)])
