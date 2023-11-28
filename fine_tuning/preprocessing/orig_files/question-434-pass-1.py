import math


def subsetXOR(arr, n, k):
    max_ele = arr[0]
    for i in range(1, n):
        if arr[i] > max_ele:
            max_ele = arr[i]
    m = (1 << (int)(math .log2(max_ele) + 1)) - 1
    if (k > m):
    return 0
    dp = [[0 for i in range(m + 1)]for i in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(m + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i - 1][j ^ arr[i - 1]])
    return dp[n][k]


arr = [1, 2, 3, 4, 5]
k = 4
n = len(arr)
print("Count of subsets is", subsetXOR(arr, n, k))
