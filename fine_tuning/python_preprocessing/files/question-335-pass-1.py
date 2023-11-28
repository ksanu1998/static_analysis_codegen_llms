def number_of_shortest_paths(n, m):
    # Initialize a 2D array to store the number of shortest paths
    dp = [[0] * m for _ in range(n)]

    # Initialize the first row with 1
    for i in range(m):
        dp[0][i] = 1

    # Calculate the number of shortest paths for each cell
    for i in range(1, n):
        for j in range(m):
            if j == 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[n - 1][m - 1]
