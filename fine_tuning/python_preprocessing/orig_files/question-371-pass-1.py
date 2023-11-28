def countPaths(m, n):
    dp = [[0 for i in range(m + 1)]for j in range(n + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if (i == 1 or j == 1):
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1])
    return dp[m][n]


if __name__ == "__main__":
    n = 5
    m = 5
    print(countPaths(n, m))
