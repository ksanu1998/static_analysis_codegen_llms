mod = 10 ** 9 + 7
N = 1000005
lpf = [0 for i in range(N)]


def least_prime_factor():
    lpf[1] = 1
    for i in range(2, N):
        if (lpf[i] == 0):
            lpf[i] = i
        for j in range(i * 2, N, i):
            if (lpf[j] == 0):
                lpf[j] = i


def solve(A):
    least_prime_factor()
    n = len(A)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n):
        dp[i] = (dp[i - 1] * (A[i] - 1)) % mod
    for i in range(1, n):
        for j in range(1, n):
            if (i == j):
                continue
            if (A[i] == A[j]):
                dp[j] = (dp[j] + dp[i - 1]) % mod
    print(dp[n - 1])


A = [1, 2, 3, 4, 5, 6]
solve(A)
