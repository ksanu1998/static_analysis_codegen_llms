MAX = 100
dp = [[[[-1 for col in range(2)]for col in range(MAX)]
       for row in range(MAX)]for row in range(MAX)]


def countPathsUtil(i, j, k, d):if i == j and k == 0:
        return 1
    if i == 0 or j == 0 or k == 0:
        return 0
    if dp[i][j][k][d]!= -1:
        return dp[i][j][k][d]
    count = 0
    if d == 0:
        count = countPathsUtil(i - 1, j, k - 1, 0) + countPathsUtil(i, j - 1, k - 1, 1)
    else:
        count = countPathsUtil(i - 1, j, k, 0) + countPathsUtil(i, j - 1, k, 1)
    dp[i][j][k][d] = count
    return count


def countPaths(m, n, k):[/INST]
    count = 0
    for d in range(2):
        count += countPathsUtil(m, n, k, d)
    return count


print(countPaths(3, 3, 2))
