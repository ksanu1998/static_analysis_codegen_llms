def minCost(arr, n):
    if (n == 1):
        return 0
    dp = [0] * (n + 1)
    dp[1] = 0
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = min(dp[i - 1] + 1, dp[i - 2] + 1)
    print(dp)
    return dp[n]


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(arr)
    print(minCost(arr, n))
