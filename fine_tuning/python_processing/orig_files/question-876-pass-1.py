def findSum(n):
    sm = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            sm = sm + i * j
    return sm


n = 5
print(findSum(n))
