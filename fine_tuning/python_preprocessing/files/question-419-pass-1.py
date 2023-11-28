def countStrUtil(dp, n, bCount=1, cCount=2):
    if n == 0:
        return 1
    if dp[n]!= -1:
        return dp[n]
    count = 0
    if bCount > 0:
        count += countStrUtil(dp, n-1, bCount-1, cCount)
    if cCount > 0:
        count += countStrUtil(dp, n-1, bCount, cCount-1)
    dp[n] = count
    return count
