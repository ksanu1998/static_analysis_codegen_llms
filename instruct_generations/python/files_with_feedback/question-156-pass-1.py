MAX = 10000
prime = [True for i in range(MAX + 1)]


def SieveOfEratosthenes():
    for p in range(2, int(MAX ** 0.5) + 1):
        if prime[p]:
            for i in range(p * p, MAX + 1, p):
                prime[i] = False

    prime_numbers = []
    for p in range(2, MAX + 1):
        if prime[p]:
            prime_numbers.append(p)

    xor = 0
    for p in prime_numbers:
        xor ^= p

    return xor
