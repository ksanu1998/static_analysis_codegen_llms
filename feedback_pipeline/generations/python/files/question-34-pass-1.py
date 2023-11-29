def findPrimes(arr, n):
    primes = []
    for i in range(2, n+1):
        if i in arr:
            primes.append(i)
    return primes