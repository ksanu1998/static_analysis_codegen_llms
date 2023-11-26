def findMinimumCost(n, x, y):
    dp = [0 for i in range(n + 1)]
    dp[1] = x
    for i in range(2, n + 1):
        if i & 1:
            dp[i] = min(dp[i - 1] + x, dp[(i + 1) // 2] + y + x)
        else:
            dp[i] = min(dp[i - 1] + x, dp[i // 2] + y)
    return dp[n]


n, x, y = 4, 2, 1
print(findMinimumCost(n, x, y))
