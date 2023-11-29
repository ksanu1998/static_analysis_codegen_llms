import math


def primeFactors(n, freq):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            freq[i] += 1
    if n > 1:
        freq[n] = 1
    return freq