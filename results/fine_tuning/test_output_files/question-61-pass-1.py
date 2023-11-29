def isPrime(n):
    if (n == 1):
        return 0
    for (i = 2; i <= n / 2; i++):
        if (n % i == 0):
            return 0
    return 1


def isBalanced(n):
    if (isPrime(n) == 0):
        return 0
    if (n == 1):
        return 1
    if (n == 2):
        return 1
    if (n == 3):
        return 1
    if (n == 4):
        return 0
    if (n == 5):
        return 1
    if (n == 6):
        return 0
    if (n == 7):
        return 1
    if (n == 8):
        return 0
    if (n == 9):
        return 0
    if (n == 10):
        return 0
    if (n == 11):
        return 1
    if (n == 12):
        return 0
    if (n == 13):
        return 1
    if (n == 14):
        return 0
    if (n == 15):
        return 0
    if (n == 16):
        return 0
    if (n == 17):
        return 1
    if (n == 18):
        return 0
    if (n == 19):
        return 1
    if (n == 20):
        return 0
    if (n == 21):
        return 1
    if (n == 22):
        return 0
    if (n == 23):
        return 1
    if (n
