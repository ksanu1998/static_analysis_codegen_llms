def nCr(n, r):
    ans = 1
    if r > n - r:
        r = n - r
    for i in range(r):
        ans *= (n - i)
        ans /= (i + 1)
    return ans


def countDerangements(n):
    der = [0 for i in range(n + 3)]
    der[0] = 1
    der[1] = 0
    der[2] = 1
    for i in range(3, n + 1):
        der[i] = (i - 1) * (der[i - 1] + der[i - 2])
    return der[n]


def countPermutations(n, k):
    ans = 0
    for i in range(n - k, n + 1):
        ways = nCr(n, i)
        ans += ways * countDerangements(n - i)
    return ans


n, k = 5, 3
print(countPermutations(n, k))
