mod = 1000000007


def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n-1) % mod