primes = []


def SieveofEratosthenes(n):
    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)
    return primes
