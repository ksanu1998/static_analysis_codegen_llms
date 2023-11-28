MAX = 100


def binomialCoeff(n, k):
    C = [0] * (k + 1)
    for i in range(1, n + 1):
        for j in range(min(i, k), 0, -1):
            C[j] = C[j] + C[j - 1]
    return C[k]


def sumOfproduct(n):
    return binomialCoeff(2 * n, n - 1)


n = 3
print(sumOfproduct(n))
