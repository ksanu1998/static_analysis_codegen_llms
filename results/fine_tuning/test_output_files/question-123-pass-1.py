def countNumber(N, S):
    if (S > (N * (N + 1) / 2)):
        return 0
    if (S == (N * (N + 1) / 2)):
        return 1
    if (S < (N * (N + 1) / 2)):
        return 0
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            if (S - (i * (i + 1) / 2) >= 0):
                dp[i] += dp[j - 1]
    print(dp[N])
