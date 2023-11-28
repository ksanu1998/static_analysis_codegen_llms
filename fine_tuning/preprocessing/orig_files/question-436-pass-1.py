MAX = 100
dp = [[[[-1 for col in range(2)]for col in range(MAX)]
       for row in range(MAX)]for row in range(MAX)]


def countPathsUtil(i, j, k, d):
    if (i < 0 or j < 0):
        return 0
    if (i == 0 and j == 0):
        return 1
    if (k == 0):
        if (d == 0 and i == 0):
            return 1
        if (d == 1 and j == 0):
            return 1
        return 0
    if (dp[i][j][k][d] != -1):
        return dp[i][j][k][d]
    if (d == 0):
        dp[i][j][k][d] = countPathsUtil(
            i, j - 1, k, d) + countPathsUtil(i - 1, j, k - 1, not d)
        return dp[i][j][k][d]
    dp[i][j][k][d] = countPathsUtil(
        i - 1, j, k, d) + countPathsUtil(i, j - 1, k - 1, not d)
    return dp[i][j][k][d]


def countPaths(i, j, k):
    if (i == 0 and j == 0):
        return 1
    return countPathsUtil(i - 1, j, k, 1) + countPathsUtil(i, j - 1, k, 0)


if __name__ == '__main__':
    m = 3
    n = 3
    k = 2
    print("Number of paths is", countPaths(m - 1, n - 1, k))
