import numpy as np
import sys
MAXI = 50
INT_MAX = sys .maxsize
dp = np .ones((MAXI, MAXI, MAXI * MAXI))
dp *= -1


def minDifference(x, y, k, b, c):
    # Initialize the dp table with infinite values
    dp = [[[sys.maxsize] * (k + 1) for _ in range(b + 1)] for _ in range(x + 1)]

    # Initialize the first row of the dp table
    for i in range(x + 1):
        dp[i][0][0] = 0

    # Loop through each element of the dp table
    for i in range(1, x + 1):
        for j in range(1, b + 1):
            for k in range(1, k + 1):
                # Calculate the minimum difference between the current element and the previous element
                min_diff = min(abs(i - j), abs(j - k), abs(k - i))

                # Update the dp table with the minimum difference
                dp[i][j][k] = min(dp[i - 1][j][k - 1] + min_diff, dp[i - 1][j - 1][k] + min_diff, dp[i - 1][j][k] + min_diff)

    # Return the minimum difference
    return dp[x][y][k]
