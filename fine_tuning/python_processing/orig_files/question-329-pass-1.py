def max_sum(a, n):
    dp = [[0 for i in range(2)]for j in range(n + 1)]
    dp[0][0] = 0
    dp[0][1] = -999999
    for i in range(0, n):
        dp[i + 1][0] = max(dp[i][0] + a[i], dp[i][1] - a[i])
        dp[i + 1][1] = max(dp[i][0] - a[i], dp[i][1] + a[i])
    return dp[n][0]


if __name__ == '__main__':
    a = [-10, 5, -4]
    n = len(a)
    print(max_sum(a, n))
