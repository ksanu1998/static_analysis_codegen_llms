def countStrUtil(dp, n, bCount=1, cCount=2):
    if (bCount < 0 or cCount < 0):
        return 0
    if (n == 0):
        return 1
    if (bCount == 0 and cCount == 0):
        return 1
    if (dp[n][bCount][cCount] != -1):
        return dp[n][bCount][cCount]
    res = countStrUtil(dp, n - 1, bCount, cCount)
    res += countStrUtil(dp, n - 1, bCount - 1, cCount)
    res += countStrUtil(dp, n - 1, bCount, cCount - 1)
    dp[n][bCount][cCount] = res
    return dp[n][bCount][cCount]


def countStr(n):
    dp = [[[-1 for x in range(n + 2)]for y in range(3)]for z in range(4)]
    return countStrUtil(dp, n)


if __name__ == "__main__":
    n = 3
    print(countStr(n))
