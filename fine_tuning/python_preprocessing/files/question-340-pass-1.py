maxLen = 10
dp = [0] * maxLen
visit = [0] * maxLen


def maxSum(arr, i, n, k):
    if i == n:
        return 0
    if visit[i]:
        return dp[i]
    visit[i] = 1
    dp[i] = max(arr[i] + maxSum(arr, i + 1, n, k - 1), maxSum(arr, i + 1, n, k))
    return dp[i]
