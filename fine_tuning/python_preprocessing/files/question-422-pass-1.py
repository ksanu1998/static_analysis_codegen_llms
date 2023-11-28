def nCr(n, k):
    r = 1
    for i in range(1, k+1):
        r *= n-i+1
        r //= i
    return r
