import sys


def MinOfCubedDP(k):# Create a 2D array to store the results of subproblems
    dp = [[0 for j in range(k+1)] for i in range(k+1)]

    # Initialize the first row of the 2D array
    for i in range(k+1):
        dp[0][i] = 1

    # Fill in the rest of the 2D array using the recurrence relation
    for i in range(1, k+1):
        for j in range(1, k+1):
            if j >= i:
                dp[i][j] = dp[i-1][j-i] + 1
            else:
                dp[i][j] = dp[i-1][j]

    # Return the result for the given number N
    return dp[k][k]


# Test the function with the given input
print(MinOfCubedDP(10))
