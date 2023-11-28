from math import sqrt
MAX = 1005


def SieveOfEratosthenes(primes):# Initialize a boolean array "prime[0..n]"
    # where prime[i] is true if i is prime and false otherwise.
    prime = [True for i in range(MAX)]
    p = 2
    while (p * p <= MAX):
        if (prime[p] == True):
            for i in range(p * p, MAX, p):
                prime[i] = False
        p += 1

    # Create a list of primes
    primes = [p for p in range(MAX) if prime[p]]
    return primes


def minSquareFreeDivisors(n):[/INST]
    # Find the square free part of n
    squareFree = n
    while (squareFree % 2 == 0):
        squareFree //= 2

    # Find the number of divisors of squareFree
    divisors = 1
    for p in SieveOfEratosthenes(sqrt(squareFree)):
        if (squareFree % p == 0):
            divisors *= 2

    # Return the minimum number of square free divisors
    return divisors


# Test the function
print(minSquareFreeDivisors(1005))  # Should print 2
print(minSquareFreeDivisors(1000))  # Should print 4
print(minSquareFreeDivisors(1001))  # Should print 4
print(minSquareFreeDivisors(1002))  # Should print 4
print(minSquareFreeDivisors(1003))  # Should print 4
print(minSquareFreeDivisors(1004))  # Should print 4
print(minSquareFreeDivisors
