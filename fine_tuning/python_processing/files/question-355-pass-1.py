N = 3


def maxPathSum(tri):
    n = len(tri)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + tri[i - 1])
    return dp[n]
