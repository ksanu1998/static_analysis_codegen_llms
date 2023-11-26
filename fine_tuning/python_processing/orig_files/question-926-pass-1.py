def findSumSubsets(n):
    return (n * (n + 1) / 2) * (1 << (n - 1))


n = 3
print(findSumSubsets(n))
