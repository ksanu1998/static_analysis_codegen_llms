def power(x, y, p):
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        x = (x * x) % p
    return res


def modInverse(a, p):
    return power(a, p - 2, p)


def modFact(n, p):
    if (p <= n):
        return 0
    res = (p - 1)
    for i in range(n + 1, p):
        res = (res * modInverse(i, p)) % p
    return res


n = 25
p = 29
print(modFact(n, p))
