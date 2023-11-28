N = 1000005
primeFactors = [0] * N


def findPrimeFactors():

def findPrimeFactors(N):
    primeFactors = [0] * N
    for i in range(2, int(N ** 0.5) + 1):
        if primeFactors[i] == 0:
            for j in range(i * i, N, i):
                primeFactors[j] = i
    return primeFactors
