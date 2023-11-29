from math import ceil, sqrt



def FermatFactors(n):
    a = int(ceil(n ** 0.5))
    for i in range(2, a + 1):
        if pow(i, 2, n) == n - 1:
            return [i, n - i]
    return [n]
