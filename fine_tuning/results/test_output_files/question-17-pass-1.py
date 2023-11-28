def gcd(a, b):
    if (a == 0):
        return b
    c = a % b
    a = b
    b = c
    return gcd(a, b)


def sumOfCoPrime(n):
    g = gcd(n, 2)
    if (g == 1):
        return 1
    if (g == 2):
        return 2
    if (g == 4):
        return 4
    if (g == 8):
        return 8
    if (g == 16):
        return 16
    if (g == 32):
        return 32
    if (g == 64):
        return 64
    if (g == 128):
        return 128
    if (g == 256):
        return 256
    if (g == 512):
        return 512
    if (g == 1024):
        return 1024
    if (g == 2048):
        return 2048
    if (g == 4096):
        return 4096
    if (g == 8192):
        return 8192
    if (g == 16384):
        return 16384
    if (g == 32768):
        return 32768
    if (g == 65536):
        return 65536
    if (g == 131072):
        return 131072
    if (g == 262144):
        return 262144
    if (g == 524288):
        return
