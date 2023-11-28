allPrimes = []


def sieve(n):
    prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if (prime[p]):
            i = p * 2
            while (i <= n):
                prime[i] = False
                i += p
        p += 1
    for p in range(2, n + 1):
        if (prime[p]):
            allPrimes .append(p)


def factorialDivisors(n):
    result = 1
    for i in range(len(allPrimes)):
        p = allPrimes[i]
        exp = 0
        while (p <= n):
            exp = exp + int(n / p)
            p = p * allPrimes[i]
        result = result * (exp + 1)
    return result


print(factorialDivisors(6))
