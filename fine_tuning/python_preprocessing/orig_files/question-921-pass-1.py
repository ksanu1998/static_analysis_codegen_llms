import sys


def findPowerOfP(n, p):
    count = 0
    r = p
    while (r <= n):
        count += (n // r)
        r = r * p
    return count


def primeFactorsofK(k):
    ans = []
    i = 2
    while k != 1:
        if k % i == 0:
            count = 0
            while k % i == 0:
                k = k // i
                count += 1
            ans .append([i, count])
        i += 1
    return ans


def largestPowerOfK(n, k):
    vec = primeFactorsofK(k)
    ans = sys .maxsize
    for i in range(len(vec)):
        ans = min(ans, findPowerOfP(n, vec[i][0]) // vec[i][1])
    return ans


print(largestPowerOfK(7, 2))
print(largestPowerOfK(10, 9))
