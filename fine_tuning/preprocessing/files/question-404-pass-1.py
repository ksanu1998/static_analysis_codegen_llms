MAX = 300
dp = [[0 for i in range(MAX)]for i in range(MAX)]


def minimumSquares(m, n):
    # Initialize the dp table
    dp = [[0 for i in range(m)]for i in range(n)]

    # Loop through each square and fill the dp table
    for i in range(m):
        for j in range(n):
            # Base case: If the current square is a square, return 1
            if i == j:
                dp[i][j] = 1
            # Recursive case: Find the minimum number of squares needed to cover the current square
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[m-1][n-1]
