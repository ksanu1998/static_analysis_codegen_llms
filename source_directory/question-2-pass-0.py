# Generate an N. 
sieve = [1] * (1000000 + 1)


def sieveOfPrimes(): 
    for i in range(2, 1000000): 
        if sieve[i] == 1: 
            for j in range(i*i, 1000000, i): 
                sieve[j] = 0


def isPrime(n): 
    if n <= 1: 
        return False
    if n <= 3: 
        return True
    if n % 2 == 0 or n % 3 == 0: 
        return False
    i = 5
    while(i * i <= n): 
        if n % i == 0 or n % (i + 2) == 0: 
            return False
        i = i + 6
    return True