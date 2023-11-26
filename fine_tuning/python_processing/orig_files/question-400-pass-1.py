def maxLength(s, n):
    dp = [[0 for i in range(n)]for i in range(n)]
    for i in range(n - 1):
        if (s[i] == '(' and s[i + 1] == ')'):
            dp[i][i + 1] = 2
    for l in range(2, n):
        i = -1
        for j in range(l, n):
            i += 1
            if (s[i] == '(' and s[j] == ')'):
                dp[i][j] = 2 + dp[i + 1][j - 1]
            for k in range(i, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k + 1][j])
    return dp[0][n - 1]


s = "()(((((()"
n = len(s)
print(maxLength(s, n))
