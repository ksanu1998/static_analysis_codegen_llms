def getMax(arr, N, K):

def getMax(arr, N, K):
    if K == 0:
        return arr[0]
    if N == 1:
        return max(arr)
    dp = [0] * (N + 1)
    dp[1] = arr[0]
    for i in range(2, N + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i - 1])
    return dp[N]
