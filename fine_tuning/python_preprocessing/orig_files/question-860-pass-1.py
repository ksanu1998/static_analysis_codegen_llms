def mulmod(a, b, mod):
    a = a % mod
    while (b > 0):
        if (b % 2 == 1):
            res = (res + a) % mod
        a = (a * 2) % mod
        b //= 2
    return res % mod


def findProduct(N):
    product = 1
    fact = 1
    MOD = 1e9 + 7
    for i in range(1, N + 1):
        fact = mulmod(fact, i, MOD)
        product = mulmod(product, fact, MOD)
        if not product:
            return 0
    return int(product)


N = 3
print(findProduct(N))
N = 5
print(findProduct(N))
