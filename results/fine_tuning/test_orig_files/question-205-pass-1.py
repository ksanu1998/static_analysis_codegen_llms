def NumbersofWays(n):

def NumbersofWays(n):
    # Initialize a 2D array to store the results
    dp = [[0] * (n * n + 1) for _ in range(n + 1)]

    # Initialize the first row and column
    dp[1][1] = 1
    dp[1][2] = 1
    dp[1][3] = 1
    dp[1][4] = 1

    # Fill in the rest of the 2D array using the recurrence relation
    for i in range(2, n + 1):
        for j in range(1, n * n + 1):
            if j >= i:
                dp[i][j] = dp[i - 1][j - i] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    # Return the result
    return dp[n][n * n]
