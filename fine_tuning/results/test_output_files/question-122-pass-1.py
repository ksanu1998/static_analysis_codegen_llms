N = 100005
mod = (10 ** 9 + 7)
factorial = [0] * N
modinverse = [0] * N


def factorialfun():
    factorial[0] = 1
    for i in range(1, N):
        factorial[i] = (i * factorial[i - 1]) % mod


def modinversefun():
    modinverse[0] = 1
    for i in range(1, N):
        modinverse[i] = (mod - (mod / i) * modinverse[mod % i]) % mod


factorialfun()
modinversefun()


def f(n):
    if (n == 0):
        return 1
    if (n == 1):
        return 1
    if (n == 2):
        return 2
    if (n == 3):
        return 3
    if (n == 4):
        return 4
    if (n == 5):
        return 5
    if (n == 6):
        return 6
    if (n == 7):
        return 7
    if (n == 8):
        return 8
    if (n == 9):
        return 9
    if (n == 10):
        return 10
    if (n == 11):
        return 11
    if (n == 12):
        return 12
    if (n == 13):
        return 13
    if (n == 14):
        return 14
    if (n == 15):
        return 15
    if (n == 16):
        return 16
    if (n == 17):
        return 1
