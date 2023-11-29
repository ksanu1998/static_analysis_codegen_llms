mod = 10 ** 9 + 7
N = 1000005
lpf = [0 for i in range(N)]


def least_prime_factor(n):
    if n == 1:
        return 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n