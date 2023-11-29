mod = 1000000007


def power(a, n):
    if (n == 0):
        return 1
    if (n == 1):
        return a
    if (n & 1):
        return (a * power(a, n - 1)) % mod
    a = (a * power(a, n / 2)) % mod
    return (a * a) % mod


def count(n):
    if (n == 1):
        return 1
    if (n == 2):
        return 2
    if (n == 3):
        return 4
    if (n == 4):
        return 7
    if (n == 5):
        return 13
    if (n == 6):
        return 24
    if (n == 7):
        return 44
    if (n == 8):
        return 81
    if (n == 9):
        return 149
    if (n == 10):
        return 274
    if (n == 11):
        return 504
    if (n == 12):
        return 927
    if (n == 13):
        return 1703
    if (n == 14):
        return 3003
    if (n == 15):
        return 5005
    if (n == 16):
        return 8009
    if (n == 17):
        return 13013
    if (n == 18):
        return 21021
    if (n == 19):
        return 34033
    if (n == 20):
        return 550
