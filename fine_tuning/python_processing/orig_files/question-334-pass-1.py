def countWays(n):
    dp = [0 for i in range(n + 1)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 3] + 1
    return dp[n]


n = 6
print(countWays(n))
