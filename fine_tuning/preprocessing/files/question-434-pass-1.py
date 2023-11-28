import math


def subsetXOR(arr, n, k):
    # Initialize a 2D array to store the results of subproblems
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Initialize the first row of the 2D array
    for i in range(n + 1):
        dp[i][0] = 1

    # Fill the 2D array in a bottom-up manner using the recurrence relation
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if j >= arr[i - 1]:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    # Return the last entry of the last row of the 2D array
    return dp[n][k]
