N = 100005
mod = (int)(1e9 + 7)
factorial = [0] * N
modinverse = [0] * N


def power(a, m1):
    if (m1 == 0):
        return 1
    m = m1
    x = 1
    while (m > 0):
        if (m & 1):
            x = (x * a) % mod
        a = (a * a) % mod
        m >>= 1
    return x


def find(n):
    if (n == 0):
        return 1
    if (factorial[n] == 0):
        factorial[n] = (
            (power(2, n) % mod) *
            (power(2, n - 1) % mod)
        ) % mod
    if (modinverse[n] == 0):
        modinverse[n] = power(factorial[n], mod - 2)
    return (
        (
            (
                (
                    (
                        (
                            (
                                (
                                    (
                                        (
                                            (
                                                (
                                                    (
                                                        (
                                                            (
                                                                (
                                                                    (
                                                                        (
                                                                            (
                                                                                (
                                                                                    (
                                                                                        (
                                                                                            (
                                                                                                (
                                                                                                    (
                                                                                                        (
                                                                                                            (
                                                                                                                (
                                                                                                                    (
                                                                                                                        (
