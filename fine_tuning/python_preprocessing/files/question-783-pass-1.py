def tile_placing(grid, N):
    # Initialize the dp table with infinite cost
    dp = [[float('inf') for _ in range(N)] for _ in range(N)]

    # Base case: If the grid is of size 1x1, the cost is 0
    dp[0][0] = 0

    # Loop through the grid and fill in the dp table
    for i in range(N):
        for j in range(N):
            # If the current cell is not blocked, check the cost of placing a tile of size 2x1
            if not grid[i][j]:
                # Calculate the cost of placing a tile of size 2x1
                cost = dp[i][j-1] + dp[i-1][j] + 1
                # Update the dp table with the minimum cost
                dp[i][j] = min(dp[i][j], cost)
    return dp[N-1][N-1]
