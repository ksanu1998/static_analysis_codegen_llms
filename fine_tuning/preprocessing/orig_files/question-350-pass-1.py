def maxSum(a, n):
    ans = 0
    arr = [0] * (n + 1)
    for i in range(1, n + 1):
        arr[i] = a[i - 1]
    dp = [[0 for i in range(3)]for j in range(n + 1)]
    for i in range(0, n + 1):
        dp[i][0] = max(arr[i], dp[i - 1][0] + arr[i])
        dp[i][1] = max(0, dp[i - 1][0]) - arr[i]
        if i >= 2:
            dp[i][1] = max(dp[i][1], dp[i - 1][1] + arr[i])
        if i >= 2:
            dp[i][2] = dp[i - 1][1] - arr[i]
        if i >= 3:
            dp[i][2] = max(dp[i][2], dp[i - 1][2] + arr[i])
        ans = max(ans, dp[i][0])
        ans = max(ans, dp[i][1])
        ans = max(ans, dp[i][2])
    return ans


if __name__ == "__main__":
    arr = [-5, 3, 2, 7, -8, 3, 7, -9, 10, 12, -6]
    n = len(arr)
    print(maxSum(arr, n))
