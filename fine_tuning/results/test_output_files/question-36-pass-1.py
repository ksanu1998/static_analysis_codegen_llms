def countWays(N):
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000007
    print(dp[N])
