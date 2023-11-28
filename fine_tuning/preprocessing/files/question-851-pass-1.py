N = 1000000
phi = [0 for i in range(N + 5)]


def computeTotient(n):
    if n == 1:
        return 1
    else:
        return n - sum(computeTotient(i) for i in range(2, int(n ** 0.5) + 1) if n % i == 0)
