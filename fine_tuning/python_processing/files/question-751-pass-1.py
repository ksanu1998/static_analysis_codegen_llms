def findSet(N, K):
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            if i - j >= 0:
                dp[i] += dp[i - j]
    return dp[N]
