def CountWays(N, M):
    dp = [[0 for i in range(N + 1)] for j in range(M + 1)]
    dp[0][0] = 1
    for i in range(1, M + 1):
        dp[i][0] = 1
    for i in range(1, N + 1):
        dp[0][i] = 1
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    print(dp[M][N])
