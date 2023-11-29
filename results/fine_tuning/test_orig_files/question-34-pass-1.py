def findPrimes(arr, n):

def findPrimes(arr, n):
    primes = [2]
    for i in range(3, n + 1, 2):
        if all(i % j!= 0 for j in range(2, int(i ** 0.5) + 1)):
            primes.append(i)
    return primes
