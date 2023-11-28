from math import sqrt
MAX = 1005


def SieveOfEratosthenes(primes):
    prime = [True for i in range(MAX)]
    for p in range(2, int(sqrt(MAX)) + 1, 1):
        if (prime[p]):
            for i in range(p * 2, MAX, p):
                prime[i] = False
    for p in range(2, MAX, 1):
        if (prime[p]):
            primes .append(p)
    return primes


def minimumSquareFreeDivisors(N):
    prime = []
    primes = []
    primes = SieveOfEratosthenes(prime)
    max_count = 0
    i = 0
    while (len(primes) and primes[i] * primes[i] <= N):
        if (N % primes[i] == 0):
            tmp = 0
            while (N % primes[i] == 0):
                tmp += 1
                N /= primes[i]
            max_count = max(max_count, tmp)
        i += 1
    if (max_count == 0):
        max_count = 1
    return max_count


if __name__ == '__main__':
    N = 24
    print(
        "Minimum Number of Square Free Divisors is",
        minimumSquareFreeDivisors(N))
    N = 6
    print(
        "Minimum Number of Square Free Divisors is",
        minimumSquareFreeDivisors(N))
