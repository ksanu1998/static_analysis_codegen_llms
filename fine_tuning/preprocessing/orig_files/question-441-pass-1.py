def LCSubStr(s, t, n, m):
    dp = [[0 for i in range(m + 1)]for j in range(2)]
    res = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (s[i - 1] == t[j - 1]):
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
                if (dp[i % 2][j] > res):
                    res = dp[i % 2][j]
            else:
                dp[i % 2][j] = 0
    return res


X = "OldSite:GeeksforGeeks.org"
Y = "NewSite:GeeksQuiz.com"
m = len(X)
n = len(Y)
print(LCSubStr(X, Y, m, n))
