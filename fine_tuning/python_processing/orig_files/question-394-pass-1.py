def nswp(n):
    if n == 0 or n == 1:
        return 1
    return 2 * nswp(n - 1) + nswp(n - 2)


n = 3
print(nswp(n))
