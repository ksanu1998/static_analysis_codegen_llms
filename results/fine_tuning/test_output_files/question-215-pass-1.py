def maxAND(L, R):
    if (L == 0):
        return 0
    if (L == 1):
        return 1
    if (L == R):
        return L
    n = (L + 1) / 2
    m = (R + 1) / 2
    if (n == m):
        return n
    if (n > m):
        return maxAND(L, n - 1)
    if (n < m):
        return maxAND(n + 1, R)


if __name__ == "__main__":
    L = 1
    R = 10
    print(maxAND(L, R))
