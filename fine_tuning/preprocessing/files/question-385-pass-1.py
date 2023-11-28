import numpy as np


def LCSubStr(X, Y):
    # Initialize the dp table
    dp = np.zeros((len(X), len(Y)))

    # Initialize the result
    result = ""

    # Loop through the characters of X and Y
    for i in range(len(X)):
        for j in range(len(Y)):
            # If the characters match, set the value in the dp table to 1
            if X[i] == Y[j]:
                dp[i][j] = 1
            # If the characters don't match, set the value in the dp table to 0
            else:
                dp[i][j] = 0

    # Find the maximum value in the dp table
    max_val = max(dp.flatten())

    # Loop through the dp table and find the indices of the maximum value
    for i in range(len(X)):
        for j in range(len(Y)):
            # If the value in the dp table is the maximum value, append the character to the result
            if dp[i][j] == max_val:
                result += X[i]
                break

    return result
