from math import ceil, sqrt


def FermatFactors(n):
    a = int(n ** 0.5) + 1
    for i in range(2, a):
        if n % i == 0:
            return [i, n // i]
    return [n, 1]