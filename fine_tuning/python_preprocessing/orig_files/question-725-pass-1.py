def nCk(n, k):
    C = [0] * (k + 1)
    for i in range(1, n + 1):
        j = min(i, k)
        while (j > 0):
            C[j] = C[j] + C[j - 1]
            j = j - 1
    return C[k]


def count_Straightlines(n, m):
    return (nCk(n, 2) - nCk(m, 2) + 1)


n = 4
m = 3
print(count_Straightlines(n, m))
