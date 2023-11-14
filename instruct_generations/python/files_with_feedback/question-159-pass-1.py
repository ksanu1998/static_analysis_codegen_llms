from math import sqrt
MAX = 1000000
prime = [True] * (MAX + 1)


def SieveOfEratosthenes():
    prime = [True] * (MAX + 1)
    for p in range(2, int(sqrt(MAX)) + 1):
        if prime[p]:
            for i in range(p * p, MAX + 1, p):
                prime[i] = False
    return [p for p in range(2, MAX + 1) if prime[p]]
