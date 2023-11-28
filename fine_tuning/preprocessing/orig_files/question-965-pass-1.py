def sieve(prime, n):
    p = 2
    while p * p <= n:
        if (prime[p] == False):
            for i in range(p * 2, n, p):
                prime[i] = True
        p += 1


def maxDigitInPrimes(L, R):
    prime = [0] * (R + 1)
    sieve(prime, R)
    freq = [0] * 10
    for i in range(L, R + 1):
        if (not prime[i]):
            while (p):
                freq[p % 10] += 1
                p //= 10
    max = freq[0]
    ans = 0
    for j in range(1, 10):
        if (max <= freq[j]):
            max = freq[j]
            ans = j
    if max == 0
    return -1
    return ans


if __name__ == "__main__":
    L = 1
    R = 20
    print(maxDigitInPrimes(L, R))
