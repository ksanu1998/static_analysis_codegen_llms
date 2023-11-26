def totalWays(N, M, X):
    dp = [0] * (M + 1)
    dp[0] = 1
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if X[j - 1] <= i:
                dp[i] += dp[i - X[j - 1]]
    return dp[M]
