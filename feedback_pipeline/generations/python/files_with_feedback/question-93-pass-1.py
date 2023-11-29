def count_ways(n, m):
    # Initialize the dp array
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column
    dp[0][0] = 1
    for i in range(1, m + 1):
        dp[i][0] = 1
    for j in range(1, n + 1):
        dp[0][j] = 1

    # Fill in the rest of the dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m][n]
