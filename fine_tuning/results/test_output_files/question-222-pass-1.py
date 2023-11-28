N = 1000005
primeFactors = [0] * N


def findPrimeFactors():
    for (i, j) in enumerate(range(1, N)):
        if (primeFactors[i] == 0):
            primeFactors[i] = i
            for (j, k) in enumerate(range(i, N)):
                if (primeFactors[k] == 0):
                    primeFactors[k] = i


findPrimeFactors()


def findMaxOperations(N):
    if (N == 1):
        return 0
    if (primeFactors[N] == N):
        return 1
    ans = 1
    for (i, j) in enumerate(range(1, N)):
        if (primeFactors[N] == i):
            ans = max(ans, 1 + findMaxOperations(N - i))
    return ans


if __name__ == "__main__":
    N = 1000005
    print(findMaxOperations(N))
