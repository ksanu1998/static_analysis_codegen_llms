def findSum(n):
    multiTerms = n * (n + 1) // 2
    sm = multiTerms
    for i in range(2, n + 1):
        multiTerms = multiTerms - (i - 1)
        sm = sm + multiTerms * i
    return sm


n = 5
print(findSum(n))
