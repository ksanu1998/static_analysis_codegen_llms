def SieveOfEratosthenes(prime, n):
    sieve = [True] * (n + 1)
    for p in prime:
        for i in range(p * p, n + 1, p):
            sieve[i] = False
    return [i for i in range(1, n + 1) if sieve[i]]
