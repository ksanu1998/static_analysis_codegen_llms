maxLen = 10
maskLen = 130
dp = [[0 for i in range(maskLen)]for i in range(maxLen)]
v = [[False for i in range(maskLen)]for i in range(maxLen)]


def minSteps(arr, i, mask, n):
    if (i == n - 1):
        return 0
    if (i > n - 1 or i < 0):
        return 9999999
    if ((mask >> i) & 1):
        return 9999999
    if (v[i][mask]):
        return dp[i][mask]
    v[i][mask] = True
    dp[i][mask] = 1 + min(minSteps(arr,
                                   i - arr[i],
                                   (mask | (1 << i)),
                                   n),
                          minSteps(arr,
                                   i + arr[i],
                                   (mask | (1 << i)),
                                   n))
    return dp[i][mask]


arr = [1, 2, 2, 2, 1, 1]
n = len(arr)
ans = minSteps(arr, 0, 0, n)
if (ans >= 9999999):
    print(-1)
else:
    print(ans)
