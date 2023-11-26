def isKPalDP(str1, str2, m, n):
    dp = [[0] * (n + 1)for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if not i:
            elif not j:
            elif (str1[i - 1] == str2[j - 1]):
                dp[i][j] = dp[i - 1][j - 1]
            else:
    return dp[m][n]


def isKPal(string, k):
    revStr = string[::-1]
    l = len(string)
    return (isKPalDP(string, revStr, l, l) <= k * 2)


string = "acdcb"
k = 2
print("Yes"if isKPal(string, k)else "No")
