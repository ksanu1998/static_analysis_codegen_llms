N = 1000005
primeFactors = [0] * N


def findPrimeFactors(N):
    primeFactors = [0] * (N + 1)
    for i in range(2, N + 1):
        if primeFactors[i] == 0:
            primeFactors[i] = i
        for j in range(i * i, N + 1, i):
            if primeFactors[j] == 0:
                primeFactors[j] = i
    return primeFactors