N = 100005
mod = (int)(1e9 + 7)
factorial = [0] * N
modinverse = [0] * N



def power(a, m1):
    if m1 == 0:
        return 1
    else:
        p = power(a, m1 >> 1)
        p *= p
        if m1 & 1:
            p *= a
        return p % mod
