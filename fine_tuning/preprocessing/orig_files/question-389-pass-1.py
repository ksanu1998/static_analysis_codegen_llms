N = 1000


def arrangeBraces(n, pos, k):
    h = [False for i in range(N)]
    dp = [[0 for i in range(N)]for i in range(N)]
    for i in range(k):
        h[pos[i]] = 1
    dp[0][0] = 1
    for i in range(1, 2 * n + 1):
        for j in range(2 * n + 1):
            if (h[i]):
                if (j != 0):
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 0
            else:
                if (j != 0):
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1])
                else:
                    dp[i][j] = dp[i - 1][j + 1]
    return dp[2 * n][0]


n = 3
pos = [2, ]
k = len(pos)
print(arrangeBraces(n, pos, k))
