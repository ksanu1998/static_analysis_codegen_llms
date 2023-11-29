sieve = [1] * (1000000 + 1)


def sieveOfPrimes():
    sieve = [1] * (1000000 + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(sieve ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, len(sieve), i):
                sieve[j] = 0
    primes = []
    for i, is_prime in enumerate(sieve):
        if is_prime:
            primes.append(i)
    return primes[1000000]
