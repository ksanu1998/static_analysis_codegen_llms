import math


def isPrime(n):
    if (n < 2):
        return False
    for i in range(2, n + 1):
        if (n % i == 0):
            return False
        i = i * i
    return True


def mobius(n):
    p = 0
    if (n % 2 == 0):
        n = int(n / 2)
        p = p + 1
        if (n % 2 == 0):
            return 0
    for i in range(3, int(math .sqrt(n)) + 1):
        if (n % i == 0):
            n = int(n / i)
            p = p + 1
            if (n % i == 0):
                return 0
        i = i + 2
    if (p % 2 == 0):
        return -1
    else:
        return 1


N = 17
print("MobiusdefsM(N)atN={}is:{}".format(N, mobius(N)))
print("MobiusdefsM(N)atN=25is:{}".format(mobius(25)))
print("MobiusdefsM(N)atN=6is:{}".format(mobius(6)))
