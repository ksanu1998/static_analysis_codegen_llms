sieve = [1] * (1000000 + 1)



def sieveOfPrimes():
    for i in range(2, 1000000 + 1):
        if sieve[i]:
            yield i
            for j in range(i * i, 1000000 + 1, i):
                sieve[j] = 0
