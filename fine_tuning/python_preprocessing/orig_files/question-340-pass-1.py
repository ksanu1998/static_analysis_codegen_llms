maxLen = 10
dp = [0] * maxLen
visit = [0] * maxLen


def maxSum(arr, i, n, k):
    if (i >= n):
        return 0
    if (visit[i]):
        return dp[i]
    visit[i] = 1
    tot = 0
    dp[i] = maxSum(arr, i + 1, n, k)
    j = i
    while (j < i + k and j < n):
        tot += arr[j]
        dp[i] = max(dp[i], tot + maxSum(arr, j + 2, n, k))
        j += 1
    return dp[i]


if __name__ == "__main__":
    arr = [-1, 2, -3, 4, 5]
    k = 2
    n = len(arr)
    print(maxSum(arr, 0, n, k))
