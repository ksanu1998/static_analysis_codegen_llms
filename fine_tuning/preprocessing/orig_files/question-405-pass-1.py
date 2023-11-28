def fact(n):
    res = 1
    for i in range(2, n + 1):
        res = res * i
    return res


def nCr(n, r):
    return fact(n) // ((fact(r) * fact(n - r)))


n = 2
print("Number of Non-Decreasing digits: ", nCr(n + 9, 9))
