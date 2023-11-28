def nswp(n):
    dp = [1 for x in range(n + 1)]
    for i in range(2, n + 1):
        dp[i] = (2 * dp[i - 1] + dp[i - 2])
    return dp[n]


n = 3
print(nswp(n))
