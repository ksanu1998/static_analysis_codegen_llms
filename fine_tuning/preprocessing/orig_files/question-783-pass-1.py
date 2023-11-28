def tile_placing(grid, N):
    dp = [0] * (N + 5)
    orig_cost = 0
    for i in range(2):
        for j in range(N):
            orig_cost += grid[i][j]
    dp[0] = 0
    dp[1] = abs(grid[0][0] - grid[1][0])
    for i in range(2, N + 1):
        dp[i] = max(dp[i - 1] + abs(grid[0][i - 1] - grid[1][i - 1]), dp[i - 2] + \
                    abs(grid[0][i - 2] - grid[0][i - 1]) + abs(grid[1][i - 2] - grid[1][i - 1]))
    print(orig_cost - dp[N], end="")


if __name__ == "__main__":
    M = [[7, 5, 1, 3], [8, 6, 0, 2]]
    N = len(M[0])
    tile_placing(M, N)
