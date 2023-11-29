def CountWays(N, M):

def count_ways(n, m):
    # Initialize the dp table with all values as 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column of the dp table
    for i in range(m + 1):
        dp[i][0] = 1
    for j in range(n + 1):
        dp[0][j] = 1

    # Fill the dp table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m][n]
