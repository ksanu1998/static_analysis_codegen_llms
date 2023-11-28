primes = []


def SieveofEratosthenes(n):
    visited = [False] * (n + 2)
    for i in range(2, n + 2):
        if (visited[i] == False):
            for j in range(i * i, n + 2, i):
                visited[j] = True
            primes .append(i)


def specialPrimeNumbers(n, k):
    SieveofEratosthenes(n)
    count = 0
    for i in range(len(primes)):
        for j in range(i - 1):
            if (primes[j] + primes[j + 1] + 1 == primes[i]):
                count += 1
                break
        if (count == k):
            return True
    return False


n = 27
k = 2
if (specialPrimeNumbers(n, k)):
    print("YES")
else:
    print("NO")
