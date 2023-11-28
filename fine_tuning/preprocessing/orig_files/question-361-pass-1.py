r = 4
col = 5


def findMinSteps(mat, n, m, dp, vis):
    if (n == 0 or m == 0 or n == (r - 1) or m == (col - 1)):
        return 0
    if (dp[n][m] != -1):
        return dp[n][m]
    vis[n][m] = True
    ans1, ans2, ans3, ans4 = 10 ** 9, 10 ** 9, 10 ** 9, 10 ** 9
    if (mat[n - 1][m] == 0):
        if (vis[n - 1][m] == False):
            ans1 = 1 + findMinSteps(mat, n - 1, m, dp, vis)
    if (mat[n][m + 1] == 0):
        if (vis[n][m + 1] == False):
            ans2 = 1 + findMinSteps(mat, n, m + 1, dp, vis)
    if (mat[n][m - 1] == 0):
        if (vis[n][m - 1] == False):
            ans3 = 1 + findMinSteps(mat, n, m - 1, dp, vis)
    if (mat[n + 1][m] == 0):
        if (vis[n + 1][m] == False):
            ans4 = 1 + findMinSteps(mat, n + 1, m, dp, vis)
    dp[n][m] = min(ans1, min(ans2, min(ans3, ans4)))
    return dp[n][m]


def minimumSteps(mat, n, m):
    twox = -1
    twoy = -1
    for i in range(n):
        for j in range(m):
            if (mat[i][j] == 2):
                twox = i
                twoy = j
                break
        if (twox != -1):
            break
    dp = [[-1 for i in range(col)]for i in range(r)]
    vis = [[False for i in range(col)]for i in range(r)]
    res = findMinSteps(mat, twox, twoy, dp, vis)
    if (res >= 10 ** 9):
        return -1
    else:
        return res


mat = [[1, 1, 1, 0, 1], [1, 0, 2, 0, 1], [0, 0, 1, 0, 1], [1, 0, 1, 1, 0]]
print(minimumSteps(mat, r, col))
