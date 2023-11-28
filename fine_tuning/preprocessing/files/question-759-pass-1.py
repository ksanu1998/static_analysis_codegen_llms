prime = [True] * 100001


def SieveOfEratosthenes(n):
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    return sum(prime)
