def maxSum(arr, k, n):
    if (n == 0):
        return 0
    if (n == 1):
        return arr[0]
    if (n == 2):
        return max(arr[0], arr[1])
    dp = [0] * n
    dp[0] = arr[0]
    for i in range(1, k + 1):
        dp[i] = max(arr[i], dp[i - 1])
    for i in range(k + 1, n):
        dp[i] = max(arr[i], dp[i - (k + 1)] + arr[i])
    max_element = max(dp)
    return max_element


if __name__ == "__main__":
    arr = [6, 7, 1, 3, 8, 2, 4]
    n = len(arr)
    k = 2
    print(maxSum(arr, k, n))
