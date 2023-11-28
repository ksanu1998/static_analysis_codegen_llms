allPrimes = []


def sieve(n):
    is_prime = [True] * (n + 1)
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    return [p for p in range(2, n + 1) if is_prime[p]]
