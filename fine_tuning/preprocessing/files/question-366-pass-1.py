import sys
n = 3


def minFallingPathSum(A):
    # Initialize the first row
    for i in range(n):
        A[0][i] = A[0][i-1] + A[0][i]

    # Initialize the first column
    for i in range(1, n):
        A[i][0] = A[i-1][0] + A[i][0]

    # Loop through the rest of the grid
    for i in range(1, n):
        for j in range(1, n):
            A[i][j] = min(A[i-1][j], A[i][j-1]) + A[i][j]

    return A[n-1][n-1]
