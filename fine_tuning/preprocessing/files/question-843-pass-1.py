MOD = 1000000007


def powerLL(x, n):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * x) % MOD
        x = (x * x) % MOD
        n //= 2
    return result
