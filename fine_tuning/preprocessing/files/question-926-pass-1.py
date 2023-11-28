def findSumSubsets(n):
    # Initialize a 2D array to store the results
    dp = [[0 for i in range(n+1)] for j in range(n+1)]

    # Initialize the first row of the 2D array
    for i in range(n+1):
        dp[0][i] = i

    # Fill the 2D array in a bottom-up manner using the recurrence relation
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

    # Return the last row of the 2D array
    return dp[n][n]
