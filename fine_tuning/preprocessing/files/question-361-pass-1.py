r = 4
col = 5


def findMinSteps(mat, n, m, dp, vis):
    if n == 0 or m == 0:
        return 0
    if n < 0 or m < 0:
        return float('inf')
    if vis[n][m]:
        return dp[n][m]
    vis[n][m] = True
    min_steps = float('inf')
    for i in range(n):
        for j in range(m):
            min_steps = min(min_steps, findMinSteps(mat, i, j, dp, vis) + 1)
    dp[n][m] = min_steps
    return dp[n][m]
