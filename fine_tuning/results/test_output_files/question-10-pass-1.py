def minSwaps(b):
    n = len(b)
    m = len(b[0])
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if (i == 0 and j == 0):
                dp[i][j] = 0
            elif (i == 0):
                dp[i][j] = dp[i][j - 1]
            elif (j == 0):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
    print(dp)
    print(n * m - dp[n - 1][m - 1])
