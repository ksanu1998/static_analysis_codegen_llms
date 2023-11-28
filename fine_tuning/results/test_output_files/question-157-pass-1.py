mod = 1000000007
inv2 = 500000004


def modulo(num):
    if (num == 0):
        return 1
    res = 1
    for i in range(1, num):
        res = (res * i) % mod
    res = (res * inv2) % mod
    return res


def sumOfNatural(L, R):
    res = 0
    for i in range(L, R + 1):
        res = (res + modulo(i)) % mod
    return res


if __name__ == "__main__":
    L = 1
    R = 10
    print(sumOfNatural(L, R))
