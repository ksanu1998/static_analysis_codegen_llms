def countPairs(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            if (i % j) % n == 0:
                dp[i] = (dp[i] + dp[j]) % 1000000007
    print(dp[n])
