N = 100005
mod = (int)(1e9 + 7)
factorial = [0] * N
modinverse = [0] * N


def power(a, m1):
    if m1 == 0:
        return 1
    else:
        return a * power(a, m1 - 1) % m1