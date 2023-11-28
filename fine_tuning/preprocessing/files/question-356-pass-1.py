from math import log2


def subsetXOR(arr, n, K):
    # Initialize the dp table
    dp = [[0] * (K+1) for _ in range(n+1)]

    # Initialize the first row
    for i in range(n+1):
        dp[i][0] = 1

    # Fill the table
    for i in range(1, n+1):
        for j in range(1, K+1):
            if arr[i-1] ^ arr[i-1] == j:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    # Return the last row
    return dp[n][K]
